from __future__ import annotations

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


def test_method_lead_is_excluded_but_audited_wind_method_is_method_only() -> None:
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
    global_lead = match_query(
        {"candidate_ids": ["china-mfa-quota-removal-textile-exporters"], "include_leads": True},
        router(),
    )
    assert method_lead["decision"] == "incompatible"
    assert "knowledge-excluded" in method_lead["reason_codes"]
    assert audited_method["decision"] == "method-only"
    assert audited_method["results"][0]["knowledge_role"] == "transferable-method"
    assert "source-period-not-transferable" in audited_method["reason_codes"]
    assert global_lead["decision"] == "incompatible"
    assert global_lead["results"][0]["knowledge_role"] == "global-china-variation"
    assert global_lead["results"][0]["recommendation_eligible"] is False


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
