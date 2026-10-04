from __future__ import annotations

import pytest

from build_router import entry
from match import match_query, time_dimension
from econ_variation_lib import load_records


def router() -> dict:
    records, failures = load_records()
    assert not failures
    return {"variations": [entry(record) for record in records]}


def test_low_carbon_firm_patents_is_conditional_not_overclaimed_compatible() -> None:
    result = match_query(
        {
            "candidate_ids": ["china-low-carbon-pilot-first-wave"],
            "data": {
                "time_start": 2005,
                "time_end": 2018,
                "frequency": "annual",
                "identifiers": ["prefecture code", "year"],
                "derivable_identifiers": ["province code"],
                "available_fields": ["outcome", "year", "province code", "prefecture code"],
                "observation_unit": "firm-year",
                "geography": "prefecture",
            },
            "comparison": {"untreated_available": True},
        },
        router(),
    )
    candidate = result["results"][0]
    assert result["decision"] == "conditional"
    assert candidate["dimensions"]["time"]["status"] == "compatible"
    assert candidate["dimensions"]["identifiers"]["status"] == "conditional"
    assert candidate["dimensions"]["observation_unit"]["manual_review"] is True


def test_multi_design_record_selects_one_profile_without_unioning_other_profile_fields() -> None:
    result = match_query(
        {
            "candidate_ids": ["china-central-environmental-protection-inspection"],
            "data": {
                "time_start": 2013,
                "time_end": 2020,
                "frequency": "annual",
                "identifiers": ["firm id", "province code", "year"],
                "available_fields": [
                    "outcome", "firm id", "province code", "year", "inspection date", "industry classification",
                ],
                "observation_unit": "firm-year",
                "geography": "province",
            },
            "comparison": {"untreated_available": True},
        },
        router(),
    )
    candidate = result["results"][0]
    assert candidate["selected_design_profile"]["id"] == "firm-year-staggered-did"
    assert candidate["dimensions"]["fields"]["status"] == "compatible"
    assert "pollutant concentration or emissions (for pollution designs)" not in candidate["missing_join_data"]
    assert {profile["id"] for profile in candidate["design_profile_results"]} == {
        "province-year-staggered-did", "firm-year-staggered-did", "plant-week-inspection-window",
    }


def test_hukou_without_city_is_incompatible_even_when_lead_is_opened_for_audit() -> None:
    result = match_query(
        {
            "candidate_ids": ["china-2014-hukou-local-implementation"],
            "include_leads": True,
            "data": {
                "time_start": 2010,
                "time_end": 2020,
                "frequency": "annual",
                "identifiers": ["year", "hukou status"],
            },
        },
        router(),
    )
    candidate = result["results"][0]
    assert result["decision"] == "incompatible"
    assert candidate["recommendation_eligible"] is False
    assert "city code" in candidate["missing_join_data"]


def test_national_averages_fail_comparison_and_join_gates() -> None:
    result = match_query(
        {
            "candidate_ids": ["china-2014-hukou-local-implementation"],
            "include_leads": True,
            "data": {
                "time_start": 2012,
                "time_end": 2016,
                "frequency": "annual",
                "identifiers": ["year"],
                "observation_unit": "national-year",
                "geography": "national",
            },
            "comparison": {"untreated_available": False},
        },
        router(),
    )
    dimensions = result["results"][0]["dimensions"]
    assert dimensions["comparison"]["status"] == "incompatible"
    assert dimensions["identifiers"]["status"] == "incompatible"
    assert dimensions["time"]["status"] == "incompatible"


def test_no_pre_period_is_a_hard_incompatibility() -> None:
    result = match_query(
        {
            "candidate_ids": ["china-low-carbon-pilot-first-wave"],
            "data": {
                "time_start": 2011,
                "time_end": 2018,
                "frequency": "annual",
                "identifiers": ["province code", "prefecture code", "year"],
            },
        },
        router(),
    )
    assert result["decision"] == "incompatible"
    assert result["results"][0]["dimensions"]["time"]["status"] == "incompatible"


def test_method_lead_audited_method_and_grounded_global_exposure_keep_distinct_roles() -> None:
    method_lead = match_query(
        {"candidate_ids": ["us-medicaid-eligibility-expansion"], "include_leads": True},
        router(),
    )
    audited_method = match_query(
        {
            "candidate_ids": ["us-air-pollution-wind-direction-iv"],
            "data": {"time_start": "2015-01-01", "time_end": "2024-12-31", "frequency": "daily"},
        },
        router(),
    )
    global_candidate = match_query(
        {"candidate_ids": ["china-mfa-quota-removal-textile-exporters"], "include_leads": True},
        router(),
    )
    assert method_lead["decision"] == "incompatible"
    assert "knowledge-excluded" in method_lead["reason_codes"]
    assert audited_method["decision"] == "method-only"
    assert audited_method["results"][0]["knowledge_role"] == "transferable-method"
    assert "source-period-not-transferable" in audited_method["reason_codes"]
    # MFA was grounded on 2026-09-28; an unspecified user dataset still needs review.
    assert global_candidate["decision"] == "conditional"
    assert "knowledge-conditional" in global_candidate["reason_codes"]
    assert "knowledge-excluded" not in global_candidate["reason_codes"]
    assert global_candidate["results"][0]["knowledge_role"] == "global-china-variation"
    assert global_candidate["results"][0]["recommendation_eligible"] is True


def test_audited_daily_method_rejects_an_explicit_target_window_under_180_days() -> None:
    result = match_query(
        {
            "candidate_ids": ["us-air-pollution-wind-direction-iv"],
            "data": {
                "time_start": "2020-01-01",
                "treatment_start": "2020-03-01",
                "time_end": "2020-06-01",
                "frequency": "daily",
            },
        },
        router(),
    )
    assert result["decision"] == "incompatible"
    assert "insufficient-pre-periods" in result["reason_codes"]
    assert "insufficient-post-periods" in result["reason_codes"]


def test_transferable_method_rejects_reversed_data_range_before_source_period_review() -> None:
    result = match_query(
        {
            "candidate_ids": ["us-air-pollution-wind-direction-iv"],
            "data": {
                "time_start": "2024-12-31",
                "time_end": "2015-01-01",
                "frequency": "daily",
            },
        },
        router(),
    )
    assert result["decision"] == "incompatible"
    assert "invalid-time-range" in result["reason_codes"]
    assert "source-period-not-transferable" not in result["reason_codes"]


def test_monthly_and_quarterly_periods_use_calendar_units_and_require_date_precision() -> None:
    payload = router()
    base = next(item for item in payload["variations"] if item["id"] == "china-low-carbon-pilot-first-wave")
    monthly = {**base, "data_fit": {**base["data_fit"], "minimum_frequency": "monthly", "minimum_pre_periods": 3, "minimum_post_periods": 3}}
    quarterly = {
        **base,
        "data_fit": {**base["data_fit"], "minimum_frequency": "quarterly", "minimum_pre_periods": 4, "minimum_post_periods": 4},
    }
    assert time_dimension(
        monthly,
        {"time_start": "2020-01-01", "treatment_start": "2020-04-01", "time_end": "2020-07-01"},
    )["status"] == "compatible"
    imprecise = time_dimension(monthly, {"time_start": 2019, "treatment_start": 2020, "time_end": 2021})
    assert imprecise["status"] == "conditional"
    assert "time-granularity-insufficient" in imprecise["reason_codes"]
    assert time_dimension(
        quarterly,
        {"time_start": "2018-01-01", "treatment_start": "2019-01-01", "time_end": "2020-01-01"},
    )["status"] == "compatible"


def test_natural_disaster_gap_does_not_force_a_policy_match() -> None:
    result = match_query(
        {
            "filters": {
                "roles": ["china-variation", "global-china-variation"],
                "domains": ["natural-disaster"],
                "variation_types": ["event-shock"],
            }
        },
        router(),
    )
    assert result == {
        "decision": "gap",
        "reason": "No record passed the requested role, knowledge-readiness, and recall gates; do not force a match.",
        "reason_codes": ["knowledge-gap"],
        "results": [],
    }


def test_broadband_outcomes_do_not_require_other_applications_data() -> None:
    common = ["city identifier", "year", "official Broadband China designation cohort", "entity-type crosswalk"]
    growth_controls = [
        "pre-treatment saving-rate growth", "pre-treatment human-capital growth", "pre-treatment log GDP per capita",
    ]
    applications = {
        "city-innovation": ["granted invention patents", "resident population", *growth_controls],
        "city-small-firm-entry": [
            "newly registered firms with registered capital below RMB2million", "resident population",
            "pre-treatment population growth", "pre-treatment saving rate", "pre-treatment human capital",
        ],
        "city-gdp-growth": ["real GDP per capita", *growth_controls],
        "city-broadband-growth": ["broadband subscribers", "resident population", *growth_controls],
    }
    current_router = router()
    for profile_id, fields in applications.items():
        result = match_query(
            {
                "candidate_ids": ["china-broadband-china-pilot-city-designation"],
                "data": {
                    "time_start": 2007,
                    "time_end": 2019,
                    "frequency": "annual",
                    "identifiers": ["stable city code", "designation-list entity name and cohort year", "year"],
                    "available_fields": [*common, *fields],
                },
                "comparison": {"untreated_available": True},
            },
            current_router,
        )
        candidate = result["results"][0]
        assert candidate["selected_design_profile"]["id"] == profile_id
        assert candidate["dimensions"]["fields"]["status"] == "compatible"
        assert candidate["missing_join_data"] == []
        assert candidate["decision"] == "conditional"  # Evidence gaps survive a complete field inventory.


def broadband_gdp_query() -> dict:
    return {
        "candidate_ids": ["china-broadband-china-pilot-city-designation"],
        "filters": {"text": ["patent"]},
        "data": {
            "time_start": 2007, "time_end": 2019, "frequency": "annual",
            "identifiers": ["stable city code", "designation-list entity name and cohort year", "year"],
            "available_fields": [
                "city identifier", "year", "official Broadband China designation cohort", "entity-type crosswalk",
                "real GDP per capita", "pre-treatment saving-rate growth", "pre-treatment human-capital growth",
                "pre-treatment log GDP per capita",
            ],
        },
        "comparison": {"untreated_available": True},
    }


def test_patent_intent_is_not_replaced_by_the_more_complete_gdp_application() -> None:
    payload = router()
    query = broadband_gdp_query()
    query["intent"] = {"outcome": "patent"}
    result = match_query(query, payload)["results"][0]
    assert result["selected_design_profile"]["id"] == "city-innovation"
    assert result["selected_design_profile"]["selection_basis"] == "research-intent"
    assert "granted invention patents" in result["missing_join_data"]
    assert result["dimensions"]["fields"]["status"] == "conditional"
    query["intent"]["design"] = "my proposed design"
    result = match_query(query, payload)["results"][0]
    assert result["selected_design_profile"]["id"] == "city-innovation"
    assert result["dimensions"]["intent"]["manual_review"] is True


def test_profile_selection_is_explicit_or_clearly_exploratory_never_silent() -> None:
    payload = router()
    query = broadband_gdp_query()
    explored = match_query(query, payload)["results"][0]
    assert explored["selected_design_profile"]["id"] == "city-gdp-growth"
    assert explored["selected_design_profile"]["selection_basis"] == "data-fit-exploration"
    assert "profile-intent-unspecified" in explored["reason_codes"]
    query["design_profile_ids"] = {"china-broadband-china-pilot-city-designation": "city-innovation"}
    selected = match_query(query, payload)["results"][0]
    assert selected["selected_design_profile"]["id"] == "city-innovation"
    assert selected["selected_design_profile"]["selection_basis"] == "explicit-profile"
    assert "granted invention patents" in selected["missing_join_data"]
    query["design_profile_ids"]["china-broadband-china-pilot-city-designation"] = "typo"
    with pytest.raises(ValueError, match="Unknown design profile"):
        match_query(query, payload)


def test_variation_order_considers_intent_then_joint_fit_without_losing_failures() -> None:
    original = next(item for item in router()["variations"] if item["id"] == "china-broadband-china-pilot-city-designation")
    innovation = {**original, "id": "innovation-only", "design_profiles": original["design_profiles"][:1]}
    gdp = {**original, "id": "gdp-only", "design_profiles": original["design_profiles"][2:3]}
    query = {**broadband_gdp_query(), "candidate_ids": ["gdp-only", "innovation-only"], "intent": {"outcome": "patent"}}
    result = match_query(query, {"variations": [gdp, innovation]})
    assert result["results"][0]["id"] == "innovation-only"
    assert "granted invention patents" in result["results"][0]["missing_join_data"]
    usable = {**innovation, "id": "usable-innovation"}
    unusable = {**innovation, "id": "unusable-innovation", "time": {"start": 2025, "end": 2026}}
    query["candidate_ids"] = ["unusable-innovation", "usable-innovation"]
    result = match_query(query, {"variations": [unusable, usable]})
    assert result["results"][0]["id"] == "usable-innovation"
    assert result["results"][1]["decision"] == "incompatible"
    assert "no-treatment-overlap" in result["results"][1]["reason_codes"]


def test_display_limit_does_not_discard_the_better_joint_fit_at_recall() -> None:
    original = next(item for item in router()["variations"] if item["id"] == "china-broadband-china-pilot-city-designation")
    profile = original["design_profiles"][0]
    less_usable_profile = {
        **profile,
        "data_fit": {**profile["data_fit"], "required_fields": [*profile["data_fit"]["required_fields"], "extra field"]},
    }
    first_in_recall = {**original, "id": "a-first", "design_profiles": [less_usable_profile]}
    better_fit = {**original, "id": "z-better", "design_profiles": [profile]}
    query = broadband_gdp_query()
    query.pop("candidate_ids")
    query.update({"limit": 1, "intent": {"outcome": "patent"}})
    query["data"]["available_fields"] = profile["data_fit"]["required_fields"]
    result = match_query(query, {"variations": [first_in_recall, better_fit]})
    assert [item["id"] for item in result["results"]] == ["z-better"]
    assert result["results"][0]["dimensions"]["fields"]["status"] == "compatible"


def test_poverty_fuzzy_rd_does_not_require_a_five_before_five_after_transfer_panel() -> None:
    result = match_query(
        {
            "candidate_ids": ["china-8-7-poverty-county-threshold"],
            "intent": {"outcome": "rural income growth"},
            "data": {
                "time_start": 1994, "time_end": 2000, "frequency": "annual",
                "identifiers": ["county code", "year"],
                "available_fields": [
                    "1992 rural per capita net income", "national poverty county indicator",
                    "prior national poverty county status", "outcome variables", "pre-determined county characteristics",
                ],
            },
            "comparison": {"untreated_available": True},
        },
        router(),
    )["results"][0]
    assert result["dimensions"]["time"]["status"] == "compatible"
    assert result["dimensions"]["fields"]["status"] == "compatible"
    assert "fiscal transfer data" not in result["missing_join_data"]
