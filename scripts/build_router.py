from __future__ import annotations

import json
import sys
from collections import Counter

sys.dont_write_bytecode = True

from econ_variation_lib import ROOT, knowledge_eligibility, load_records, write_json, workspace_lock  # noqa: E402


ROUTER_PURPOSE = (
    "Compact recall index. Knowledge eligibility is a static gate; "
    "query-specific compatibility must be evaluated separately."
)


def concise(value: object, limit: int = 240) -> str:
    text = " ".join(str(value or "").split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def blocker_codes(blockers: list[str]) -> list[str]:
    codes: set[str] = set()
    for blocker in blockers:
        text = str(blocker).casefold()
        if "primary institutional evidence" in text:
            codes.add("missing-primary-evidence")
        elif "actual data" in text or "data_used" in text:
            codes.add("missing-application-data")
        elif "transfer" in text or "china analogue" in text:
            codes.add("transfer-not-audited")
        elif "duplicate" in text or "same assignment" in text:
            codes.add("possible-duplicate")
        elif "not an assignment" in text or "admissibility" in text:
            codes.add("admissibility-unresolved")
        else:
            codes.add("other-readiness-debt")
    return sorted(codes)


def entry(record: object) -> dict:
    data = record.data
    scope = data["scope"]
    timeline = data["timeline"]
    assignment = data["assignment"]
    design = data["design"]
    requirements = data["empirical_requirements"]
    role = scope["knowledge_role"]
    blockers = data["readiness_blockers"]
    return {
        "id": record.id,
        "name": data["name"],
        "aliases": data["aliases"],
        "status": data["status"],
        "knowledge_role": role,
        # This is a knowledge-readiness gate, not a claim that the case fits a
        # particular research idea. Query-specific fit is evaluated by match.py.
        "recommendation_eligibility": knowledge_eligibility(data),
        "country": scope["country"],
        "domains": scope["domains"],
        "variation_type": scope["variation_type"],
        "time": {
            "start": timeline["implementation_start"],
            "end": timeline["implementation_end"],
        },
        "assignment": {
            "unit": assignment["unit"],
            "mechanism": concise(data["identity"]["assignment_mechanism"]),
            "treatment": concise(design.get("treatment_variable"), 180),
            "comparison": concise(design.get("comparison_logic"), 180),
            "required_identifiers": assignment["required_identifiers"],
        },
        "research_fit": {
            "outcomes": data["research_compatibility"]["outcome_domains"],
            "application_outcomes": sorted(
                {str(application.get("outcome")) for application in data.get("design_applications", []) if application.get("outcome")}
            ),
            "design_families": design["candidate_designs"],
            "claim_type": design.get("claim_type"),
        },
        "data_fit": {
            "population": concise(requirements["population"], 160),
            "observation_unit": requirements["observation_unit"],
            "geography_level": requirements["geography_level"],
            "time_start": requirements["time_start"],
            "time_end": requirements["time_end"],
            "minimum_frequency": requirements["minimum_frequency"],
            "minimum_pre_periods": requirements["minimum_pre_periods"],
            "minimum_post_periods": requirements["minimum_post_periods"],
            "required_fields": requirements["required_fields"],
            "required_identifiers": requirements["required_identifiers"],
            "treatment_key": requirements["treatment_key"],
        },
        "threat_types": sorted({item["type"] for item in data["threats"]}),
        "blocker_codes": blocker_codes(blockers),
        "blocker_count": len(blockers),
        "source_path": record.path.relative_to(ROOT).as_posix(),
    }


def build() -> dict:
    records, failures = load_records()
    if failures:
        raise RuntimeError("cannot build router from invalid frontmatter")
    entries = [entry(record) for record in sorted(records, key=lambda item: item.id)]
    payload = {
        "schema_version": 3,
        "purpose": ROUTER_PURPOSE,
        "empirical_requirements_contract_version": 1,
        "record_count": len(records),
        "knowledge_role_counts": dict(Counter(item["knowledge_role"] for item in entries)),
        "recommendation_eligibility_counts": dict(Counter(item["recommendation_eligibility"] for item in entries)),
        "variations": entries,
    }
    with workspace_lock("generated"):
        write_json(ROOT / "dist" / "router.json", payload)
    return payload


def main() -> int:
    payload = build()
    print(json.dumps({"record_count": payload["record_count"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
