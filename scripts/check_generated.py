from __future__ import annotations

import json
import sys
from collections import Counter

sys.dont_write_bytecode = True

from build_router import ROUTER_PURPOSE, entry  # noqa: E402
from econ_variation_lib import ROOT, load_records  # noqa: E402
from validate import run  # noqa: E402


def expected_router() -> dict:
    records, failures = load_records()
    if failures:
        raise RuntimeError("canonical records cannot be parsed")
    entries = [entry(record) for record in sorted(records, key=lambda item: item.id)]
    return {
        "schema_version": 3,
        "purpose": ROUTER_PURPOSE,
        "empirical_requirements_contract_version": 1,
        "record_count": len(records),
        "knowledge_role_counts": dict(Counter(item["knowledge_role"] for item in entries)),
        "recommendation_eligibility_counts": dict(Counter(item["recommendation_eligibility"] for item in entries)),
        "variations": entries,
    }


def main() -> int:
    path = ROOT / "dist" / "router.json"
    if not path.exists():
        print("generated check failed: dist/router.json is missing")
        return 1
    actual = json.loads(path.read_text(encoding="utf-8"))
    if actual != expected_router():
        print("generated check failed: dist/router.json is stale")
        return 1
    health_path = ROOT / "dist" / "health.json"
    if not health_path.exists():
        print("generated check failed: dist/health.json is missing")
        return 1
    _, expected_health = run(write_health=False)
    if json.loads(health_path.read_text(encoding="utf-8")) != expected_health:
        print("generated check failed: dist/health.json is stale")
        return 1
    print("generated check ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
