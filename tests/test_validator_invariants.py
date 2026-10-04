from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from types import SimpleNamespace

import validate
from validate import (
    Audit, evidence_url_doi, has_placeholder_metadata, is_precise_evidence_path, normalize_doi,
    validate_provenance,
)


def test_placeholder_and_doi_normalization_guards() -> None:
    assert has_placeholder_metadata("10.1016/j.jclepro.2025.XXXXXX")
    assert has_placeholder_metadata("https://example.org/paper")
    assert has_placeholder_metadata("needs-verification")
    assert not has_placeholder_metadata("10.3389/fpubh.2025.1688719")
    assert normalize_doi("https://doi.org/10.3389/FPUBH.2025.1688719/") == (
        "10.3389/fpubh.2025.1688719"
    )
    assert evidence_url_doi("https://doi.org/10.3389/fpubh.2025.1688719") == (
        "10.3389/fpubh.2025.1688719"
    )
    assert evidence_url_doi("https://publisher.example/article") is None


def test_precise_evidence_paths_follow_real_schema_fields() -> None:
    assert is_precise_evidence_path("assignment.rule")
    assert is_precise_evidence_path("timeline.announcement")
    assert is_precise_evidence_path("design_applications.treatment_encoding")
    assert not is_precise_evidence_path("assignment")
    assert not is_precise_evidence_path("assignment.unknown")
    assert not is_precise_evidence_path("assignment.rule.extra")


def test_legacy_file_hash_detects_untracked_content_change(tmp_path, monkeypatch) -> None:
    state = tmp_path / "state"
    state.mkdir()
    (state / "tasks.jsonl").write_text("", encoding="utf-8")
    (state / "runs.jsonl").write_text("", encoding="utf-8")
    record_path = tmp_path / "legacy-case.md"
    record_path.write_text("changed content", encoding="utf-8")
    record_id = "legacy-case"
    ids_digest = hashlib.sha256(record_id.encode()).hexdigest()
    baseline = {
        "record_count": 1,
        "record_ids_sha256": ids_digest,
        "record_ids": [record_id],
        "record_sha256": {record_id: "0" * 64},
    }
    (state / "legacy_baseline.json").write_text(json.dumps(baseline), encoding="utf-8")
    monkeypatch.setattr(validate, "STATE_DIR", state)
    record = SimpleNamespace(
        id=record_id,
        path=record_path,
        data={"provenance": {"task_id": "legacy-untracked"}},
    )
    audit = Audit()
    validate_provenance(audit, [record])
    assert any("legacy-untracked content changed" in error for error in audit.errors)


def test_legacy_baseline_detects_a_deleted_frozen_record(tmp_path, monkeypatch) -> None:
    state = tmp_path / "state"
    state.mkdir()
    (state / "tasks.jsonl").write_text("", encoding="utf-8")
    (state / "runs.jsonl").write_text("", encoding="utf-8")
    record_id = "missing-legacy-case"
    baseline = {
        "record_count": 1,
        "record_ids_sha256": hashlib.sha256(record_id.encode()).hexdigest(),
        "record_ids": [record_id],
        "record_sha256": {record_id: "0" * 64},
    }
    (state / "legacy_baseline.json").write_text(json.dumps(baseline), encoding="utf-8")
    monkeypatch.setattr(validate, "STATE_DIR", state)
    audit = Audit()
    validate_provenance(audit, [])
    assert any("frozen legacy records are missing" in error for error in audit.errors)


def test_resolved_deprecated_doi_duplicates_are_not_reported() -> None:
    audit, _ = validate.run(write_health=False)
    assert not any("DOI" in warning for warning in audit.warnings)


def assignment_audit_fixture(tmp_path, monkeypatch):
    monkeypatch.setattr(validate, "STATE_DIR", tmp_path)
    (tmp_path / "tasks.jsonl").write_text(
        json.dumps({"id": "task-review", "stage": "resolve", "status": "completed"}), encoding="utf-8",
    )
    records = [
        SimpleNamespace(id=record_id, data={"evidence": [{
            "id": "E1", "verification_status": "verified", "source_type": "policy-document",
            "supports": ["assignment.rule"],
        }]})
        for record_id in ["city-a", "city-b"]
    ]
    row = {
        "doi": "10.1234/actual-paper", "record_ids": ["city-a", "city-b"],
        "task_id": "task-review", "rationale": "Original rules assign different eligible populations.",
        "evidence_refs": {"city-a": ["E1"], "city-b": ["E1"]},
    }
    return records, row


def test_shared_doi_still_requires_an_explicit_audit(tmp_path, monkeypatch) -> None:
    records, _ = assignment_audit_fixture(tmp_path, monkeypatch)
    audit = Audit()
    assert not validate.shared_doi_is_audited(audit, "10.1234/actual-paper", records)


def test_evidence_backed_exact_group_is_recognized(tmp_path, monkeypatch) -> None:
    records, row = assignment_audit_fixture(tmp_path, monkeypatch)
    (tmp_path / "doi-assignment-audits.jsonl").write_text(json.dumps(row), encoding="utf-8")
    audit = Audit()
    assert validate.shared_doi_is_audited(audit, "10.1234/actual-paper", records)
    assert not audit.errors
    assert not validate.shared_doi_is_audited(audit, "10.1234/another-paper", records)
    records.append(SimpleNamespace(id="city-c", data=deepcopy(records[0].data)))
    assert not validate.shared_doi_is_audited(audit, "10.1234/actual-paper", records)


def test_assignment_audit_rejects_unverified_or_missing_evidence(tmp_path, monkeypatch) -> None:
    records, row = assignment_audit_fixture(tmp_path, monkeypatch)
    (tmp_path / "doi-assignment-audits.jsonl").write_text(json.dumps(row), encoding="utf-8")
    for change in [
        {"verification_status": "reported"},
        {"source_type": "paper"},
        {"supports": ["timeline.effective"]},
        {"id": "E2"},
    ]:
        changed = deepcopy(records)
        changed[0].data["evidence"][0].update(change)
        audit = Audit()
        assert not validate.shared_doi_is_audited(audit, "10.1234/actual-paper", changed)
        assert audit.errors


def test_assignment_audit_needs_reason_and_maintenance_provenance(tmp_path, monkeypatch) -> None:
    records, row = assignment_audit_fixture(tmp_path, monkeypatch)
    for change in [{"rationale": " "}, {"task_id": "unknown"}, {"evidence_refs": {}}]:
        changed = {**row, **change}
        (tmp_path / "doi-assignment-audits.jsonl").write_text(json.dumps(changed), encoding="utf-8")
        audit = Audit()
        assert not validate.shared_doi_is_audited(audit, "10.1234/actual-paper", records)
        assert audit.errors


def test_unreviewed_shared_doi_remains_a_maturity_error(monkeypatch) -> None:
    monkeypatch.setattr(validate, "shared_doi_is_audited", lambda *args: False)
    audit = Audit()
    validate.validate_records(audit)
    assert any("duplicate assignment audit must be resolved" in error for error in audit.errors)
