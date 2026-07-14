from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
import yaml

sys.dont_write_bytecode = True

from econ_variation_lib import (  # noqa: E402
    ROOT, SCHEMA_PATH, STATE_DIR, canonical_topics, identity_fingerprint, knowledge_eligibility, load_records,
    load_topic_taxonomy, public_url_issues, read_jsonl, write_json,
)


REQUIRED_HEADINGS = (
    "## Institutional Background", "## What Changed", "## Implementation and Assignment",
    "## Why This Creates Empirical Variation", "## Identification Risks", "## Data Requirements",
    "## Evidence Notes",
)
EVIDENCE_PATH = re.compile(
    r"^(scope|identity|timeline|assignment|research_compatibility|design|threats|"
    r"empirical_requirements|design_applications|method_transfer)(?:\.|$)"
)
MOJIBAKE = re.compile(r"(?:鈥|脳|锟|馃|�)")
CAUSAL_OVERCLAIM = re.compile(
    r"(?:the causal effect of the recorded exposure|intrinsically exogenous|clean identification|"
    r"determined purely by geography)", re.IGNORECASE
)
PLACEHOLDER_METADATA = re.compile(
    r"(?:x{4,}|\btbd\b|placeholder|needs[- ]verification)", re.IGNORECASE
)
DOI_URL = re.compile(r"^https?://(?:dx\.)?doi\.org/(.+)$", re.IGNORECASE)
DOI_VALUE = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)


class Audit:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def evidence_refs(value: Any) -> set[str]:
    refs: set[str] = set()
    if isinstance(value, dict):
        for key, item in value.items():
            if key == "evidence_refs" and isinstance(item, list):
                refs.update(str(ref) for ref in item)
            else:
                refs.update(evidence_refs(item))
    elif isinstance(value, list):
        for item in value:
            refs.update(evidence_refs(item))
    return refs


def has_placeholder_metadata(value: Any) -> bool:
    text = str(value or "")
    return bool(
        PLACEHOLDER_METADATA.search(text)
        or re.match(r"^https?://(?:[^/]+\.)?example\.(?:com|org|net)(?:/|$)", text, re.IGNORECASE)
    )


def normalize_doi(value: Any) -> str:
    text = str(value or "").strip().casefold()
    match = DOI_URL.match(text)
    if match:
        text = match.group(1)
    return text.rstrip("/")


def evidence_url_doi(value: Any) -> str | None:
    match = DOI_URL.match(str(value or "").strip())
    return normalize_doi(match.group(1)) if match else None


def coverage(record: Any) -> dict[str, bool]:
    data = record.data
    verified = [item for item in data.get("evidence", []) if item.get("verification_status") == "verified"]
    verified_primary = [
        item for item in verified
        if item.get("source_type") in {"policy-document", "implementation-document", "official-data", "archive"}
    ]
    research_evidence = [
        item for item in data.get("evidence", [])
        if item.get("source_type") in {"paper", "appendix", "replication", "scholarship"}
        and item.get("verification_status") in {"verified", "reported"}
    ]
    supports = {path for item in verified for path in item.get("supports", [])}
    primary_supports = {path for item in verified_primary for path in item.get("supports", [])}
    return {
        "has_primary_evidence": bool(verified_primary),
        "primary_identity_supported": any(path.startswith("identity") for path in primary_supports),
        "primary_timeline_supported": any(path.startswith("timeline") for path in primary_supports),
        "primary_assignment_supported": any(path.startswith("assignment") for path in primary_supports),
        "has_research_evidence": bool(research_evidence),
        "timeline_supported": any(path.startswith("timeline") for path in supports),
        "assignment_supported": any(path.startswith("assignment") for path in supports),
        "has_application": bool(data.get("design_applications")),
        "has_threat_assessment": bool(data.get("threats")),
        "has_requirements": bool((data.get("empirical_requirements") or {}).get("required_identifiers")),
        "scope_classified": (data.get("scope") or {}).get("knowledge_role") in {
            "china-variation", "global-china-variation", "transferable-method"
        },
        "method_transfer_documented": (
            (data.get("scope") or {}).get("knowledge_role") != "transferable-method"
            or isinstance(data.get("method_transfer"), dict)
        ),
        "application_data_documented": bool(data.get("design_applications")) and all(
            bool(item.get("data_used")) for item in data.get("design_applications", [])
        ),
    }


def validate_records(audit: Audit) -> tuple[list[Any], list[dict[str, Any]]]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    records, failures = load_records()
    for path, message in failures:
        audit.error(f"{path.name}: {message}")
    ids: set[str] = set()
    aliases: dict[str, str] = {}
    fingerprints: dict[str, str] = {}
    coverage_rows: list[dict[str, Any]] = []
    doi_records: dict[str, list[str]] = defaultdict(list)
    for record in records:
        for issue in sorted(validator.iter_errors(record.data), key=lambda item: list(item.path)):
            location = ".".join(str(part) for part in issue.path) or "record"
            audit.error(f"{record.path.name}: {location}: {issue.message}")
        if record.id in ids:
            audit.error(f"duplicate record id: {record.id}")
        ids.add(record.id)
        profile_ids = [str(profile.get("id", "")) for profile in record.data.get("design_profiles", [])]
        if len(profile_ids) != len(set(profile_ids)):
            audit.error(f"{record.id}: duplicate design profile IDs")
        if (record.data.get("provenance") or {}).get("task_id") != "legacy-untracked" and not canonical_topics(
            (record.data.get("scope") or {}).get("domains", [])
        ):
            audit.error(f"{record.id}: managed record domains do not map to the stable topic taxonomy")
        for heading in REQUIRED_HEADINGS:
            if heading not in record.body:
                audit.error(f"{record.id}: missing body heading {heading}")
        evidence = record.data.get("evidence", [])
        evidence_ids = [str(item.get("id", "")) for item in evidence if isinstance(item, dict)]
        if len(evidence_ids) != len(set(evidence_ids)):
            audit.error(f"{record.id}: duplicate evidence IDs")
        referenced = evidence_refs(record.data)
        body_refs = set(re.findall(r"\bE[1-9][0-9]*\b", record.body))
        missing = sorted((referenced | body_refs) - set(evidence_ids))
        if missing:
            audit.error(f"{record.id}: unknown evidence references {missing}")
        for item in evidence:
            for field in ("citation", "url"):
                if has_placeholder_metadata(item.get(field)):
                    audit.error(f"{record.id}: evidence {item.get('id')} has placeholder {field}")
            issues = public_url_issues(item.get("url"))
            if issues:
                audit.error(f"{record.id}: evidence {item.get('id')} has unsafe URL: {', '.join(issues)}")
            invalid_paths = [path for path in item.get("supports", []) if not EVIDENCE_PATH.match(str(path))]
            if invalid_paths and record.status in {"grounded", "design-documented"}:
                audit.error(f"{record.id}: evidence {item.get('id')} has non-field support paths {invalid_paths}")
            if record.status in {"grounded", "design-documented"} and not (
                item.get("access_level") and item.get("locator")
            ):
                audit.error(f"{record.id}: mature evidence {item.get('id')} requires access_level and locator")
        for value in [record.data.get("name", ""), *record.data.get("aliases", [])]:
            normalized = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "", str(value).casefold())
            if normalized in aliases and aliases[normalized] != record.id:
                audit.error(f"alias collision between {aliases[normalized]} and {record.id}: {value}")
            aliases[normalized] = record.id
        fingerprint = identity_fingerprint(record.data)
        if fingerprint in fingerprints:
            audit.warn(f"possible duplicate identity: {fingerprints[fingerprint]} and {record.id}")
        fingerprints[fingerprint] = record.id
        row = {
            "id": record.id,
            "status": record.status,
            "knowledge_role": (record.data.get("scope") or {}).get("knowledge_role"),
            "task_id": (record.data.get("provenance") or {}).get("task_id"),
            **coverage(record),
        }
        row["has_mojibake"] = bool(MOJIBAKE.search(record.path.read_text(encoding="utf-8")))
        row["has_causal_overclaim_lint"] = bool(CAUSAL_OVERCLAIM.search(record.path.read_text(encoding="utf-8")))
        row["invalid_evidence_path_count"] = sum(
            1 for item in evidence for path in item.get("supports", []) if not EVIDENCE_PATH.match(str(path))
        )
        coverage_rows.append(row)
        role = (record.data.get("scope") or {}).get("knowledge_role")
        country = str((record.data.get("scope") or {}).get("country", ""))
        blockers = " ".join(str(item) for item in (record.data.get("readiness_blockers") or [])).casefold()
        if role == "china-variation" and country != "China":
            audit.error(f"{record.id}: china-variation must assign exposure in China")
        if role == "transferable-method" and country == "China":
            audit.error(f"{record.id}: China cases must not be downgraded to transferable-method")
        if role in {"china-variation", "global-china-variation"}:
            if not row["has_primary_evidence"] and "primary institutional evidence" not in blockers:
                audit.error(f"{record.id}: paper-only institutional grounding must remain an explicit readiness blocker")
            if not row["has_research_evidence"]:
                audit.error(f"{record.id}: China-facing variation requires research evidence for its design application")
        if role == "transferable-method" and not isinstance(record.data.get("method_transfer"), dict):
            audit.error(f"{record.id}: transferable-method requires method_transfer")
        generic_scope_text = {
            "The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical research.",
            "A global or foreign policy change directly alters the treatment environment faced by Chinese units.",
            "The source setting is outside China; retain the reusable identification construction rather than recommend the foreign shock as a China treatment.",
        }
        if record.status in {"grounded", "design-documented"} and record.data["scope"]["china_relevance"] in generic_scope_text:
            audit.error(f"{record.id}: mature record requires case-specific scope.china_relevance")
        evidence_by_id = {str(item.get("id")): item for item in evidence}
        for application_index, application in enumerate(record.data.get("design_applications", [])):
            doi = normalize_doi(application.get("doi"))
            if doi:
                if has_placeholder_metadata(application.get("doi")):
                    audit.error(f"{record.id}: design application {application_index} has placeholder DOI")
                elif not DOI_VALUE.match(doi):
                    audit.error(f"{record.id}: design application {application_index} has invalid DOI {doi}")
                doi_records[doi].append(record.id)
                referenced_dois = {
                    evidence_url_doi((evidence_by_id.get(ref) or {}).get("url"))
                    for ref in application.get("evidence_refs", [])
                }
                if doi not in referenced_dois:
                    audit.error(
                        f"{record.id}: design application {application_index} DOI {doi} "
                        "is not matched by a referenced evidence DOI URL"
                    )
        if record.status == "grounded":
            required = (
                "has_primary_evidence", "has_research_evidence", "primary_identity_supported",
                "primary_timeline_supported", "primary_assignment_supported",
            )
            failed = [key for key in required if not row[key]]
            if failed:
                audit.error(f"{record.id}: grounded gate missing {failed}")
            if not (record.data.get("design") or {}).get("claim_type"):
                audit.error(f"{record.id}: grounded record requires design.claim_type")
        if record.status == "design-documented":
            required = (
                "has_primary_evidence", "has_research_evidence", "primary_identity_supported",
                "primary_timeline_supported", "primary_assignment_supported",
                "has_application", "has_threat_assessment", "has_requirements", "scope_classified",
                "method_transfer_documented", "application_data_documented",
            )
            failed = [key for key in required if not row[key]]
            if failed:
                audit.error(f"{record.id}: design-documented gate missing {failed}")
            if record.data.get("readiness_blockers"):
                audit.error(f"{record.id}: design-documented record cannot retain readiness blockers")
            if not (record.data.get("design") or {}).get("claim_type"):
                audit.error(f"{record.id}: design-documented record requires design.claim_type")
            if row["has_mojibake"] or row["has_causal_overclaim_lint"]:
                audit.error(f"{record.id}: design-documented record contains unresolved content lint")
    records_by_id = {record.id: record for record in records}
    redirects: dict[str, str] = {}
    for record in records:
        superseded_by = str(record.data.get("superseded_by") or "").strip()
        reason = str(record.data.get("deprecation_reason") or "").strip()
        if record.status == "deprecated":
            if bool(superseded_by) == bool(reason):
                audit.error(
                    f"{record.id}: deprecated record requires exactly one of superseded_by or deprecation_reason"
                )
            if superseded_by:
                if superseded_by == record.id:
                    audit.error(f"{record.id}: superseded_by cannot refer to itself")
                elif superseded_by not in records_by_id:
                    audit.error(f"{record.id}: superseded_by references missing record {superseded_by}")
                else:
                    redirects[record.id] = superseded_by
        elif superseded_by or reason:
            audit.error(f"{record.id}: only deprecated records may set superseded_by or deprecation_reason")
    for start in redirects:
        seen: set[str] = set()
        current = start
        while current in redirects:
            if current in seen:
                audit.error(f"deprecated redirect cycle includes {start}")
                break
            seen.add(current)
            current = redirects[current]
        if current in records_by_id and records_by_id[current].status == "deprecated" and current not in redirects:
            audit.error(f"{start}: deprecated redirect must terminate at a non-deprecated canonical record")
    for doi, record_ids in sorted(doi_records.items()):
        unique_ids = sorted(set(record_ids))
        active_ids = [record_id for record_id in unique_ids if records_by_id[record_id].status != "deprecated"]
        if len(active_ids) > 1:
            audit.warn(f"DOI {doi} appears in multiple active variation cases: {active_ids}; audit whether assignment differs")
            if any(records_by_id[record_id].status in {"grounded", "design-documented"} for record_id in active_ids):
                audit.error(f"DOI {doi}: duplicate assignment audit must be resolved before either record matures")
    for record in records:
        for related in (record.data.get("identity") or {}).get("related_variations", []):
            if related not in ids:
                audit.error(f"{record.id}: unknown related variation {related}")
    return records, coverage_rows


def validate_state(audit: Audit, record_ids: set[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    task_ids: set[str] = set()
    task_by_id: dict[str, dict[str, Any]] = {}
    for name in ("tasks.jsonl", "candidates.jsonl", "runs.jsonl"):
        rows, errors = read_jsonl(STATE_DIR / name)
        for error in errors:
            audit.error(f"{name}: {error}")
        counts[name.removesuffix(".jsonl")] = len(rows)
        row_ids = [str(row.get("id", "")) for row in rows if row.get("id")]
        if len(row_ids) != len(set(row_ids)):
            audit.error(f"{name}: duplicate row IDs")
        if name == "tasks.jsonl":
            task_ids = {str(row.get("id")) for row in rows}
            task_by_id = {str(row.get("id")): row for row in rows}
            allowed = {"pending", "claimed", "completed", "failed"}
            for row in rows:
                if row.get("status") not in allowed:
                    audit.error(f"tasks.jsonl: task {row.get('id')} has invalid status")
                if row.get("stage") not in {"screen", "discover", "resolve", "ground", "audit", "consolidate"}:
                    audit.error(f"tasks.jsonl: task {row.get('id')} has invalid stage")
                for touched in row.get("records_touched", []) or []:
                    if touched not in record_ids:
                        audit.error(f"tasks.jsonl: task {row.get('id')} references missing record {touched}")
        if name == "candidates.jsonl":
            for row in rows:
                required = {"source_fingerprint", "knowledge_role", "status", "stage", "source", "reason"}
                if not row.get("legacy_migrated"):
                    required.add("task_id")
                missing = sorted(key for key in required if not row.get(key))
                if missing:
                    audit.error(f"candidates.jsonl: candidate {row.get('id')} is missing {missing}")
                if row.get("task_id") and row.get("task_id") not in task_ids:
                    audit.error(f"candidates.jsonl: candidate {row.get('id')} references a missing task")
                if row.get("knowledge_role") not in {
                    "china-variation", "global-china-variation", "transferable-method"
                }:
                    audit.error(f"candidates.jsonl: candidate {row.get('id')} has invalid knowledge role")
                allowed_statuses = {"pending", "queued", "in-progress", "resolved", "contested", "skipped", "blocked"}
                if row.get("status") not in allowed_statuses or row.get("stage") not in {
                    "discover", "resolve", "ground", "audit", "consolidate"
                }:
                    audit.error(f"candidates.jsonl: candidate {row.get('id')} has invalid lifecycle state")
                follow_up = str(row.get("follow_up_task_id") or "")
                if row.get("status") in {"queued", "in-progress"}:
                    task = task_by_id.get(follow_up)
                    if not task or task.get("candidate_id") != row.get("id"):
                        audit.error(f"candidates.jsonl: candidate {row.get('id')} has no valid linked follow-up task")
                    elif row.get("status") == "queued" and task.get("status") != "pending":
                        audit.error(f"candidates.jsonl: queued candidate {row.get('id')} does not link to a pending task")
                    elif row.get("status") == "in-progress" and task.get("status") != "claimed":
                        audit.error(f"candidates.jsonl: in-progress candidate {row.get('id')} does not link to a claimed task")
                if row.get("status") in {"resolved", "contested"}:
                    resolved = row.get("resolved_record_ids") or []
                    if not resolved or any(record_id not in record_ids for record_id in resolved):
                        audit.error(f"candidates.jsonl: terminal candidate {row.get('id')} has invalid resolved records")
    return counts


def validate_provenance(audit: Audit, records: list[Any]) -> None:
    tasks, task_errors = read_jsonl(STATE_DIR / "tasks.jsonl")
    runs, run_errors = read_jsonl(STATE_DIR / "runs.jsonl")
    if task_errors or run_errors:
        return
    task_by_id = {str(row.get("id")): row for row in tasks}
    legacy_records: list[Any] = []
    for record in records:
        task_id = str((record.data.get("provenance") or {}).get("task_id", ""))
        if task_id == "legacy-untracked":
            legacy_records.append(record)
            continue
        task = task_by_id.get(task_id)
        if not task or task.get("status") not in {"claimed", "completed"}:
            audit.error(f"{record.id}: provenance task must exist and be claimed or completed")
            continue
        if task.get("status") == "completed":
            if record.id not in (task.get("records_touched") or []):
                audit.error(f"{record.id}: completed provenance task does not declare this record")
            if not any(row.get("task_id") == task_id and record.id in (row.get("records_touched") or []) for row in runs):
                audit.error(f"{record.id}: completed provenance task has no matching run event")
    baseline_path = STATE_DIR / "legacy_baseline.json"
    if not baseline_path.exists():
        audit.error("legacy_baseline.json is missing")
        return
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    baseline_ids = sorted(str(item) for item in baseline.get("record_ids", []))
    digest = hashlib.sha256("\n".join(baseline_ids).encode()).hexdigest()
    if len(baseline_ids) != baseline.get("record_count") or digest != baseline.get("record_ids_sha256"):
        audit.error("legacy baseline manifest is internally inconsistent")
    baseline_hashes = baseline.get("record_sha256")
    if not isinstance(baseline_hashes, dict):
        audit.error("legacy baseline manifest is missing record_sha256")
        baseline_hashes = {}
    for record_id, expected in baseline_hashes.items():
        if record_id not in baseline_ids or not re.fullmatch(r"[0-9a-f]{64}", str(expected)):
            audit.error(f"legacy baseline has invalid file hash entry for {record_id}")
    legacy_ids = [record.id for record in legacy_records]
    unexpected = sorted(set(legacy_ids) - set(baseline_ids))
    if unexpected:
        audit.error(f"records cannot newly claim legacy-untracked provenance: {unexpected}")
    for record in legacy_records:
        expected = baseline_hashes.get(record.id)
        if not expected:
            audit.error(f"{record.id}: legacy-untracked record has no frozen file hash")
            continue
        actual = hashlib.sha256(record.path.read_bytes()).hexdigest()
        if actual != expected:
            audit.error(
                f"{record.id}: legacy-untracked content changed; assign a claimed task provenance before editing"
            )


def debt_summary(rows: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "record_count": len(rows),
        "missing_primary_evidence": sum(not row["has_primary_evidence"] for row in rows),
        "missing_primary_institutional_core": sum(not (
            row["primary_identity_supported"]
            and row["primary_timeline_supported"]
            and row["primary_assignment_supported"]
        ) for row in rows),
        "missing_application_data": sum(not row["application_data_documented"] for row in rows),
        "mojibake_detected": sum(row["has_mojibake"] for row in rows),
        "causal_overclaim_lint": sum(row["has_causal_overclaim_lint"] for row in rows),
        "invalid_evidence_paths": sum(row["invalid_evidence_path_count"] for row in rows),
    }


def run(write_health: bool) -> tuple[Audit, dict[str, Any]]:
    audit = Audit()
    try:
        load_topic_taxonomy()
    except (OSError, ValueError, yaml.YAMLError) as exc:
        audit.error(f"topic taxonomy is invalid: {exc}")
    records, coverage_rows = validate_records(audit)
    validate_state(audit, {record.id for record in records})
    validate_provenance(audit, records)
    status_counts = Counter(record.status for record in records)
    role_counts = Counter(record.data["scope"]["knowledge_role"] for record in records)
    eligibility_counts = Counter(knowledge_eligibility(record.data) for record in records)
    legacy_rows = [row for row in coverage_rows if row["task_id"] == "legacy-untracked"]
    managed_active_rows = [
        row for row in coverage_rows
        if row["task_id"] != "legacy-untracked" and row["status"] not in {"deprecated", "contested"}
    ]
    managed_china_facing_rows = [
        row for row in managed_active_rows
        if row["knowledge_role"] in {"china-variation", "global-china-variation"}
    ]
    managed_china_debt = debt_summary(managed_china_facing_rows)
    stop_bulk_discovery = bool(managed_china_facing_rows) and (
        managed_china_debt["missing_primary_evidence"] > len(managed_china_facing_rows) / 2
    )
    quality_debt = {
        "legacy_backlog": debt_summary(legacy_rows),
        "managed_active_pipeline": debt_summary(managed_active_rows),
        "possible_duplicate_warnings": sum(
            "duplicate" in warning.casefold() or "doi" in warning.casefold() for warning in audit.warnings
        ),
    }
    actionable_rows = [
        row for row in managed_china_facing_rows
        if row["has_mojibake"]
        or row["has_causal_overclaim_lint"]
        or row["invalid_evidence_path_count"]
        or not row["has_primary_evidence"]
        or not row["application_data_documented"]
    ]
    actionable_rows.sort(key=lambda row: (
        -sum((
            row["has_mojibake"],
            row["has_causal_overclaim_lint"],
            bool(row["invalid_evidence_path_count"]),
            not row["has_primary_evidence"],
            not row["application_data_documented"],
        )),
        row["id"],
    ))
    snapshot_dates = [str(record.data["timeline"]["last_verified"]) for record in records]
    report = {
        "knowledge_snapshot_date": max(snapshot_dates, default=None),
        "repository_health": {
            "status": "error" if audit.errors else "valid",
            "errors": audit.errors,
            "warnings": audit.warnings,
        },
        "record_count": len(records),
        "status_counts": dict(status_counts),
        "knowledge_role_counts": dict(role_counts),
        "knowledge_readiness": {
            "eligibility_counts": dict(eligibility_counts),
            "direct_candidates": eligibility_counts["direct-candidate"],
            "conditional_candidates": eligibility_counts["conditional-candidate"],
            "lead_only": eligibility_counts["lead-only"],
            "method_leads": eligibility_counts["method-lead"],
            "method_inspirations": eligibility_counts["method-inspiration"],
            "do_not_recommend": eligibility_counts["do-not-recommend"],
            "stop_bulk_discovery": stop_bulk_discovery,
            "interpretation": "Repository validity is not research readiness. Lead-only and contested records require audit before recommendation.",
        },
        "quality_debt": quality_debt,
        "priority_audit_ids": [row["id"] for row in actionable_rows[:10]],
    }
    if write_health:
        write_json(ROOT / "dist" / "health.json", report)
    return audit, report


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Econ-Variation canonical knowledge and durable state.")
    parser.add_argument("--write-health", action="store_true")
    args = parser.parse_args()
    audit, report = run(args.write_health)
    print(f"records={report['record_count']} errors={len(audit.errors)} warnings={len(audit.warnings)}")
    for message in audit.errors:
        print(f"ERROR: {message}")
    for message in audit.warnings:
        print(f"WARNING: {message}")
    return 1 if audit.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
