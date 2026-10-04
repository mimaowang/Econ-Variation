from __future__ import annotations

from build_router import entry
from econ_variation_lib import load_records
from search import compact_result, search_items


def items() -> list[dict]:
    records, failures = load_records()
    assert not failures
    return [entry(record) for record in records]


def test_search_tokenizes_phrases_and_ranks_recommendation_ready_results() -> None:
    # Fixed inputs isolate ranking mechanics from changes in the live collection.
    examples = [
        {"id": record_id, "name": "Firm patent reform", "recommendation_eligibility": eligibility}
        for record_id, eligibility in [
            ("z-conditional", "conditional-candidate"),
            ("b-direct", "direct-candidate"),
            ("a-direct", "direct-candidate"),
            ("excluded-lead", "lead-only"),
        ]
    ]
    examples.extend([
        {"id": "lower-score", "topics": ["firm"], "research_fit": {"outcomes": ["patent"]},
         "recommendation_eligibility": "direct-candidate"},
        {"id": "missing-term", "name": "Firm reform", "recommendation_eligibility": "direct-candidate"},
    ])
    for example in examples:
        example["knowledge_role"] = "china-variation"
    results = search_items(examples, roles=["china-variation"], text=["firm patents"], limit=10)
    ids = [result["item"]["id"] for result in results]
    assert ids == ["a-direct", "b-direct", "z-conditional", "lower-score"]
    assert results[0]["score"] > results[-1]["score"]
    assert results[0]["why_matched"] == ["firm:identity", "patent:identity"]


def test_search_excludes_leads_by_default_and_can_include_them_for_audit() -> None:
    default = search_items(items(), roles=["china-variation"], text=["great famine institutional"])
    audited = search_items(
        items(),
        roles=["china-variation"],
        text=["great famine institutional"],
        include_leads=True,
    )
    assert default == []
    assert [result["item"]["id"] for result in audited] == ["china-great-famine-institutional-causes"]
    assert audited[0]["item"]["recommendation_eligibility"] == "lead-only"


def test_search_returns_no_false_policy_match_for_a_catalog_gap() -> None:
    results = search_items(
        items(),
        roles=["china-variation", "global-china-variation"],
        domains=["natural-disaster"],
        variation_types=["event-shock"],
    )
    assert results == []


def test_search_normalizes_stable_topics_and_chinese_aliases() -> None:
    catalog = items()
    topic_results = search_items(catalog, roles=["china-variation"], topics=["环境"], limit=20)
    assert topic_results
    assert all("environment" in result["item"]["topics"] for result in topic_results)
    # Test alias recall, not membership in a changing collection's top twenty.
    chinese_text = search_items(catalog, roles=["china-variation"], text=["中国企业创新"], limit=len(catalog))
    ids = {result["item"]["id"] for result in chinese_text}
    assert "china-intellectual-property-courts-reform" in ids
    assert "china-low-carbon-pilot-first-wave" in ids
    english_text = search_items(catalog, roles=["china-variation"], text=["firm innovation"], limit=len(catalog))
    assert ids == {result["item"]["id"] for result in english_text}


def test_compact_search_result_exposes_decision_fields_without_full_router_entry() -> None:
    result = search_items(items(), text=["low carbon"], limit=1)[0]
    compact = compact_result(result)
    assert compact["id"] == "china-low-carbon-pilot-first-wave"
    assert compact["knowledge_eligibility"] == "conditional-candidate"
    assert compact["treatment"]
    assert compact["comparison"]
    assert compact["data_fit"]["minimum_pre_periods"] == 4
    assert compact["topics"]
    assert len(compact["design_profiles"]) == 3
    assert "aliases" not in compact and "research_fit" not in compact
