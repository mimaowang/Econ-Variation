from __future__ import annotations

from build_router import entry
from econvariation_lib import load_records
from search import compact_result, search_items


def items() -> list[dict]:
    records, failures = load_records()
    assert not failures
    return [entry(record) for record in records]


def test_search_tokenizes_phrases_and_ranks_recommendation_ready_results() -> None:
    results = search_items(items(), roles=["china-variation"], text=["firm patents"], limit=10)
    ids = [result["item"]["id"] for result in results]
    assert ids[:2] == ["china-low-carbon-pilot-first-wave", "china-rd-tax-notch"]
    assert all(result["item"]["recommendation_eligibility"] != "lead-only" for result in results)


def test_search_excludes_leads_by_default_and_can_include_them_for_audit() -> None:
    default = search_items(items(), roles=["china-variation"], text=["central environmental inspection"])
    audited = search_items(
        items(),
        roles=["china-variation"],
        text=["central environmental inspection"],
        include_leads=True,
    )
    assert default == []
    assert [result["item"]["id"] for result in audited] == ["china-central-environmental-protection-inspection"]
    assert audited[0]["item"]["recommendation_eligibility"] == "lead-only"


def test_search_returns_no_false_policy_match_for_a_catalog_gap() -> None:
    results = search_items(
        items(),
        roles=["china-variation", "global-china-variation"],
        domains=["natural-disaster"],
        variation_types=["event-shock"],
    )
    assert results == []


def test_compact_search_result_exposes_decision_fields_without_full_router_entry() -> None:
    result = search_items(items(), text=["low carbon"], limit=1)[0]
    compact = compact_result(result)
    assert compact["id"] == "china-low-carbon-pilot-first-wave"
    assert compact["knowledge_eligibility"] == "conditional-candidate"
    assert compact["treatment"]
    assert compact["comparison"]
    assert compact["data_fit"]["minimum_pre_periods"] == 4
    assert "aliases" not in compact and "research_fit" not in compact
