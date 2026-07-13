from __future__ import annotations

import json

from build_router import build
from check_generated import expected_router
from econvariation_lib import ROOT


def test_router_is_deterministic_and_current() -> None:
    first = build()
    second = build()
    assert first == second == expected_router()
    assert json.loads((ROOT / "dist" / "router.json").read_text(encoding="utf-8")) == first


def test_router_is_compact_and_exposes_recommendation_gate() -> None:
    payload = expected_router()
    assert payload["empirical_requirements_contract_version"] == 1
    assert all("data_fit" in item for item in payload["variations"])
    assert all("source_path" in item for item in payload["variations"])
    assert payload["schema_version"] == 3
    assert "transferable-method" in payload["knowledge_role_counts"]
    assert all("recommendation_eligibility" in item for item in payload["variations"])
    assert all("timeline" not in item and "method_transfer" not in item for item in payload["variations"])
    encoded_entries = [len(json.dumps(item, ensure_ascii=False)) for item in payload["variations"]]
    assert max(encoded_entries) < 8_000
