from __future__ import annotations

import yaml

from build_router import entry
from match import match_query
from econvariation_lib import ROOT, load_records


def benchmark() -> dict:
    return yaml.safe_load((ROOT / "benchmarks" / "routing_cases.yaml").read_text(encoding="utf-8"))


def router() -> dict:
    records, failures = load_records()
    assert not failures
    return {"variations": [entry(record) for record in records]}


def test_every_routing_case_has_a_decision_rubric() -> None:
    cases = benchmark()["cases"]
    assert len(cases) == 17
    assert all("evaluation" in case for case in cases)
    for case in cases:
        evaluation = case["evaluation"]
        assert evaluation["decision"] in {
            "compatible",
            "conditional",
            "incompatible",
            "gap",
            "method-only",
            "skip",
        }
        assert "expected_ids" in evaluation
        assert evaluation["expected_reason_codes"]
        assert "allowed_roles" in evaluation
        assert evaluation["must_identify"]


def test_executable_routing_cases_call_the_real_match_kernel() -> None:
    payload = router()
    cases = [case for case in benchmark()["cases"] if "query" in case]
    assert len(cases) == 16
    for case in cases:
        actual = match_query(case["query"], payload)
        expected = case["evaluation"]
        assert actual["decision"] == expected["decision"], case["id"]
        assert [result["id"] for result in actual["results"]] == expected["expected_ids"], case["id"]
        assert set(expected["expected_reason_codes"]) <= set(actual["reason_codes"]), case["id"]
        assert all(result["knowledge_role"] in expected["allowed_roles"] for result in actual["results"]), case["id"]


def test_benchmark_keeps_natural_language_context_but_not_as_match_input() -> None:
    cases = benchmark()["cases"]
    prompts = " ".join(case["prompt"].casefold() for case in cases)
    assert "only" in prompts and "without" in prompts
    assert "transferable" in prompts and "irrelevant foreign policy" in prompts
    assert sum("query" in case for case in cases) == 16
