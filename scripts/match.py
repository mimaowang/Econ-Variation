from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

import yaml

sys.dont_write_bytecode = True

from search import load_router, phrase_matches, search_items  # noqa: E402


FREQUENCY_DAYS = {
    "daily": 1,
    "weekly": 7,
    "monthly": 30,
    "quarterly": 91,
    "semiannual": 182,
    "annual": 365,
    "yearly": 365,
    "biennial": 730,
    "decennial": 3650,
}
IDENTIFIER_ALIASES = {
    "calendar year": "year",
    "survey year": "year",
    "year": "year",
    "city identifier": "city code",
    "prefecture identifier": "prefecture code",
    "province identifier": "province code",
    "firm identifier": "firm id",
    "household identifier": "household id",
    "individual identifier": "individual id",
}


def parse_date(value: Any) -> tuple[date, str] | None:
    if isinstance(value, int):
        return date(value, 1, 1), "year"
    text = str(value or "").strip()
    if re.fullmatch(r"(?:18|19|20)\d{2}", text):
        return date(int(text), 1, 1), "year"
    if re.fullmatch(r"(?:18|19|20)\d{2}-\d{2}", text):
        parsed = date.fromisoformat(f"{text}-01")
        return parsed, "month"
    if re.fullmatch(r"(?:18|19|20)\d{2}-\d{2}-\d{2}", text):
        return date.fromisoformat(text), "day"
    return None


def normalized_name(value: Any) -> str:
    text = re.sub(r"\([^)]*\)", "", str(value or "").casefold())
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", text).strip()
    return IDENTIFIER_ALIASES.get(text, text)


def dimension(
    status: str,
    reason: str,
    *reason_codes: str,
    manual_review: bool = False,
) -> dict[str, Any]:
    result: dict[str, Any] = {"status": status, "reason": reason, "reason_codes": list(reason_codes)}
    if manual_review:
        result["manual_review"] = True
    return result


def knowledge_dimension(item: dict[str, Any]) -> dict[str, Any]:
    eligibility = item["recommendation_eligibility"]
    if eligibility == "direct-candidate":
        return dimension("compatible", "The record is decision-sufficient, subject to query-specific fit.", "knowledge-ready")
    if eligibility == "conditional-candidate":
        return dimension("conditional", "The record is grounded but retains explicit knowledge blockers.", "knowledge-conditional")
    if eligibility == "method-inspiration":
        return dimension("conditional", "This is method inspiration, not a China-facing treatment.", "method-inspiration")
    if eligibility == "method-lead":
        return dimension(
            "incompatible",
            "This transferable method remains an unaudited lead, not an implementation-ready method.",
            "knowledge-excluded",
        )
    if eligibility == "lead-only":
        return dimension("incompatible", "Lead-only knowledge cannot be recommended before grounding.", "knowledge-excluded")
    return dimension(
        "incompatible",
        "Contested or deprecated knowledge is excluded from recommendations.",
        "knowledge-excluded",
    )


def required_frequency(item: dict[str, Any]) -> str:
    text = normalized_name(item.get("data_fit", {}).get("minimum_frequency"))
    return next((name for name in FREQUENCY_DAYS if name in text), "")


def full_months(start: date, end: date) -> int:
    months = (end.year - start.year) * 12 + end.month - start.month
    return months - int(end.day < start.day)


def full_years(start: date, end: date) -> int:
    years = end.year - start.year
    return years - int((end.month, end.day) < (start.month, start.day))


def period_count(start: tuple[date, str], end: tuple[date, str], frequency: str) -> int | None:
    start_date, start_precision = start
    end_date, end_precision = end
    if end_date < start_date:
        return -1
    if frequency in {"annual", "yearly"}:
        return full_years(start_date, end_date)
    if frequency == "biennial":
        return full_years(start_date, end_date) // 2
    if frequency == "decennial":
        return full_years(start_date, end_date) // 10
    if frequency in {"monthly", "quarterly", "semiannual"}:
        if "year" in {start_precision, end_precision}:
            return None
        months = full_months(start_date, end_date)
        divisor = {"monthly": 1, "quarterly": 3, "semiannual": 6}[frequency]
        return months // divisor
    if frequency in {"daily", "weekly"}:
        if "day" not in {start_precision, end_precision} or start_precision != end_precision:
            return None
        days = (end_date - start_date).days
        return days if frequency == "daily" else days // 7
    return None


def time_dimension(item: dict[str, Any], data: dict[str, Any]) -> dict[str, Any]:
    role = item.get("knowledge_role")
    explicit_assignment = data.get("treatment_start", data.get("assignment_date"))
    start = parse_date(data.get("time_start"))
    end = parse_date(data.get("time_end"))
    if start is not None and end is not None and start[0] > end[0]:
        return dimension("incompatible", "Data time_start is later than time_end.", "invalid-time-range")
    if role == "transferable-method" and explicit_assignment is None:
        return dimension(
            "conditional",
            "The overseas source period is not a treatment date for a Chinese analogue; supply data.treatment_start or assignment_date.",
            "source-period-not-transferable",
            manual_review=True,
        )
    assignment = parse_date(explicit_assignment if explicit_assignment is not None else item.get("time", {}).get("start"))
    if start is None or end is None:
        return dimension(
            "conditional",
            "Data start/end were not both supplied with usable precision; temporal fit needs manual review.",
            "time-range-missing",
            manual_review=True,
        )
    if assignment is None:
        return dimension(
            "conditional",
            "The assignment date is not machine-comparable.",
            "assignment-date-manual-review",
            manual_review=True,
        )
    if end[0] < assignment[0]:
        return dimension("incompatible", "The data end before treatment begins.", "no-treatment-overlap")
    frequency = required_frequency(item)
    if not frequency:
        return dimension(
            "conditional",
            "The record's minimum frequency cannot be mapped to deterministic periods.",
            "time-frequency-manual-review",
            manual_review=True,
        )
    available_pre = period_count(start, assignment, frequency)
    available_post = period_count(assignment, end, frequency)
    if available_pre is None or available_post is None:
        return dimension(
            "conditional",
            f"{frequency} pre/post periods require more precise dates than the query supplies.",
            "time-granularity-insufficient",
            manual_review=True,
        )
    requirements = item.get("data_fit", {})
    minimum_pre = int(requirements.get("minimum_pre_periods") or 0)
    minimum_post = int(requirements.get("minimum_post_periods") or 0)
    failures: list[str] = []
    codes: list[str] = []
    if available_pre < minimum_pre:
        failures.append(f"needs {minimum_pre} pre-periods but data provide {available_pre}")
        codes.append("insufficient-pre-periods")
    if available_post < minimum_post:
        failures.append(f"needs {minimum_post} post-periods but data provide {available_post}")
        codes.append("insufficient-post-periods")
    if failures:
        return dimension("incompatible", "; ".join(failures), *codes)
    return dimension(
        "compatible",
        f"Data provide {available_pre} pre-periods and {available_post} post-periods at {frequency} frequency.",
        "time-periods-sufficient",
    )


def frequency_dimension(item: dict[str, Any], data: dict[str, Any]) -> dict[str, Any]:
    available = normalized_name(data.get("frequency"))
    required_text = str(item.get("data_fit", {}).get("minimum_frequency") or "")
    required = required_frequency(item)
    if not available:
        return dimension("conditional", "Data frequency was not supplied.", "frequency-missing", manual_review=True)
    if available not in FREQUENCY_DAYS or required not in FREQUENCY_DAYS:
        return dimension(
            "conditional",
            f"Cannot deterministically compare available '{available}' with required '{required_text}'.",
            "frequency-manual-review",
            manual_review=True,
        )
    if FREQUENCY_DAYS[available] > FREQUENCY_DAYS[required]:
        return dimension(
            "incompatible",
            f"{available} data are less frequent than the required {required} data.",
            "insufficient-frequency",
        )
    return dimension("compatible", f"{available} data meet the minimum {required} frequency.", "frequency-sufficient")


def identifiers_dimension(item: dict[str, Any], data: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    required = item.get("data_fit", {}).get("required_identifiers", [])
    if "identifiers" not in data:
        return dimension(
            "conditional",
            "Available identifiers were not enumerated.",
            "identifiers-not-enumerated",
            manual_review=True,
        ), []
    available = {normalized_name(value) for value in data.get("identifiers", [])}
    derivable = {normalized_name(value) for value in data.get("derivable_identifiers", [])}
    missing = [str(value) for value in required if normalized_name(value) not in available | derivable]
    if missing:
        return dimension(
            "incompatible",
            f"Treatment cannot be joined without: {', '.join(missing)}.",
            "missing-identifiers",
        ), missing
    if derivable:
        return dimension(
            "conditional",
            "Some treatment identifiers are declared derivable and the crosswalk must be verified.",
            "identifier-crosswalk-manual-review",
            manual_review=True,
        ), []
    return dimension("compatible", "All required treatment identifiers were supplied.", "identifiers-sufficient"), []


def fields_dimension(item: dict[str, Any], data: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    required = item.get("data_fit", {}).get("required_fields", [])
    if "available_fields" not in data:
        return dimension(
            "conditional",
            "Available fields were not enumerated.",
            "fields-not-enumerated",
            manual_review=True,
        ), []
    available = {normalized_name(value) for value in data.get("available_fields", [])}
    missing = [str(value) for value in required if normalized_name(value) not in available]
    if missing:
        return dimension(
            "conditional",
            f"Field names need mapping or additional data: {', '.join(missing)}.",
            "missing-fields",
            manual_review=True,
        ), missing
    return dimension("compatible", "All enumerated required fields were supplied.", "fields-sufficient"), []


def comparison_dimension(query: dict[str, Any]) -> dict[str, Any]:
    comparison = query.get("comparison", {})
    if comparison.get("untreated_available") is False:
        return dimension("incompatible", "No untreated or not-yet-treated comparison is available.", "no-comparison")
    if comparison.get("untreated_available") is True:
        return dimension(
            "compatible",
            "The query declares an untreated or not-yet-treated comparison.",
            "comparison-available",
        )
    return dimension(
        "conditional",
        "Comparison-group availability needs manual review.",
        "comparison-manual-review",
        manual_review=True,
    )


def semantic_dimensions(item: dict[str, Any], query: dict[str, Any]) -> dict[str, Any]:
    data = query.get("data", {})
    dimensions: dict[str, Any] = {}
    for key, record_key in (
        ("observation_unit", "observation_unit"),
        ("geography", "geography_level"),
        ("population", "population"),
    ):
        supplied = data.get(key)
        if supplied:
            recorded = item["data_fit"].get(record_key, "")
            if normalized_name(supplied) == normalized_name(recorded):
                dimensions[key] = dimension(
                    "compatible",
                    f"Query '{supplied}' matches the selected design profile.",
                    f"{key}-matched",
                )
            else:
                dimensions[key] = dimension(
                    "conditional",
                    f"Manual review required: query '{supplied}' versus record '{recorded}'.",
                    f"{key}-manual-review",
                    manual_review=True,
                )
    return dimensions


def intent_dimension(item: dict[str, Any], query: dict[str, Any]) -> dict[str, Any] | None:
    intent = query.get("intent", {})
    fit = item.get("research_fit", {})
    matched = {
        key: phrase_matches(intent[key], choices) for key, choices in (
            ("outcome", fit.get("outcomes", []) + fit.get("application_outcomes", [])),
            ("design", fit.get("design_families", [])),
        )
        if intent.get(key)
    }
    unresolved = [key for key, matches in matched.items() if not matches]
    if unresolved:
        result = dimension(
            "conditional", f"The declared research intent needs canonical review: {', '.join(unresolved)}. "
            "Data completeness does not establish substantive fit.", "intent-manual-review", manual_review=True,
        )
        result["matched"] = [key for key, matches in matched.items() if matches]
        return result
    if item.get("profile_selection_basis") == "automatic" and not intent.get("outcome"):
        return dimension(
            "conditional", "Specify an outcome or a profile before treating this application as relevant; "
            "a design family alone does not select its outcome.", "profile-intent-unspecified", manual_review=True,
        )
    if intent.get("outcome") or intent.get("design"):
        result = dimension("compatible", "Declared intent matches the recorded vocabulary; verify substantive fit in the canonical record.", "intent-matched")
        result["matched"] = list(matched)
        return result
    if item.get("profile_selection_basis") == "explicit-profile":
        return dimension("compatible", "The agent explicitly selected this record's research application.", "profile-explicit")
    return None


def fit_rank(result: dict[str, Any]) -> tuple:
    """Preserve intent before data convenience; ties retain recall order, not arbitrary weights."""
    dimensions = result["dimensions"]
    return (
        result["knowledge_eligibility"] not in {"do-not-recommend", "lead-only", "method-lead"},
        "outcome" in dimensions.get("intent", {}).get("matched", []),
        dimensions.get("intent", {}).get("status") == "compatible",
        {"compatible": 3, "conditional": 2, "method-only": 2, "incompatible": 0}[result["decision"]],
        -sum(value["status"] == "incompatible" for value in dimensions.values()),
        -sum(value["status"] == "conditional" for value in dimensions.values()),
        -len(result["missing_join_data"]),
    )


def evaluate_item(item: dict[str, Any], query: dict[str, Any]) -> dict[str, Any]:
    data = query.get("data", {})
    identifiers, missing_identifiers = identifiers_dimension(item, data)
    fields, missing_fields = fields_dimension(item, data)
    dimensions = {
        "knowledge": knowledge_dimension(item),
        "time": time_dimension(item, data),
        "frequency": frequency_dimension(item, data),
        "identifiers": identifiers,
        "fields": fields,
        "comparison": comparison_dimension(query),
        **semantic_dimensions(item, query),
    }
    intent = intent_dimension(item, query)
    if intent is not None:
        dimensions["intent"] = intent
    hard_failure = any(value["status"] == "incompatible" for key, value in dimensions.items() if key != "knowledge")
    knowledge_failure = dimensions["knowledge"]["status"] == "incompatible"
    if knowledge_failure:
        decision = "incompatible"
    elif hard_failure:
        decision = "incompatible"
    elif item["knowledge_role"] == "transferable-method" and item["recommendation_eligibility"] == "method-inspiration":
        decision = "method-only"
    elif any(value["status"] == "conditional" for value in dimensions.values()):
        decision = "conditional"
    else:
        decision = "compatible"
    reason_codes = sorted({code for value in dimensions.values() for code in value.get("reason_codes", [])})
    return {
        "id": item["id"],
        "decision": decision,
        "recommendation_eligible": item["recommendation_eligibility"] in {"direct-candidate", "conditional-candidate"},
        "knowledge_role": item["knowledge_role"],
        "knowledge_eligibility": item["recommendation_eligibility"],
        "reason_codes": reason_codes,
        "dimensions": dimensions,
        "missing_join_data": sorted({*missing_identifiers, *missing_fields}),
        "treatment": item.get("assignment", {}).get("treatment", ""),
        "comparison": item.get("assignment", {}).get("comparison", ""),
        "blockers_requiring_human_judgment": item.get("blocker_codes", []),
        "threats_requiring_human_judgment": item.get("threat_types", []),
        "source_path": item["source_path"],
    }


def evaluate_item_profiles(item: dict[str, Any], query: dict[str, Any]) -> dict[str, Any]:
    profiles = item.get("design_profiles", [])
    requested = query.get("design_profile_ids", {}).get(item["id"])
    if requested is not None:
        profiles = [profile for profile in profiles if profile["id"] == requested]
        if not profiles:
            raise ValueError(f"Unknown design profile '{requested}' for variation '{item['id']}'.")
    if not profiles:
        return evaluate_item(item, query)
    evaluated = []
    for profile in profiles:
        profile_item = {
            **item, "data_fit": profile["data_fit"],
            "research_fit": {"outcomes": profile.get("outcome_domains", []), "design_families": profile["design_families"]},
            "profile_selection_basis": "explicit-profile" if requested is not None else "automatic",
        }
        result = evaluate_item(profile_item, query)
        result["selected_design_profile"] = {
            "id": profile["id"],
            "label": profile["label"],
            "when_to_use": profile["when_to_use"],
            "selection_basis": (
                "explicit-profile" if requested is not None else
                "research-intent" if result["dimensions"]["intent"]["status"] == "compatible" else
                "data-fit-exploration"
            ),
        }
        evaluated.append((result, profile))
    evaluated.sort(key=lambda row: fit_rank(row[0]), reverse=True)
    selected = evaluated[0][0]
    selected["design_profile_results"] = [
        {
            "id": profile["id"],
            "label": profile["label"],
            "decision": result["decision"],
            "reason_codes": result["reason_codes"],
            "missing_join_data": result["missing_join_data"],
            "intent": result["dimensions"]["intent"],
        }
        for result, profile in evaluated
    ]
    return selected


def select_items(query: dict[str, Any], router: dict[str, Any]) -> list[dict[str, Any]]:
    items = router["variations"]
    candidate_ids = query.get("candidate_ids") or []
    include_leads = bool(query.get("include_leads"))
    if candidate_ids:
        by_id = {item["id"]: item for item in items}
        # An explicitly named case is returned for a diagnostic even when it is
        # immature or excluded; knowledge_dimension prevents recommendation.
        return [by_id[item_id] for item_id in candidate_ids if item_id in by_id]
    filters = query.get("filters", {})
    ranked = search_items(
        items,
        roles=filters.get("roles"),
        eligibility=filters.get("eligibility"),
        domains=filters.get("domains"),
        topics=filters.get("topics"),
        design=filters.get("design"),
        identifiers=filters.get("identifiers"),
        text=filters.get("text"),
        variation_types=filters.get("variation_types"),
        include_leads=include_leads,
        limit=len(items),  # Apply the display limit after joint fit, not before it.
    )
    return [result["item"] for result in ranked]


def match_query(query: dict[str, Any], router: dict[str, Any] | None = None) -> dict[str, Any]:
    router = router or load_router()
    for key in ("intent", "design_profile_ids"):
        if not isinstance(query.get(key, {}), dict):
            raise ValueError(f"{key} must be an object.")
    items = select_items(query, router)
    unused = set(query.get("design_profile_ids", {})) - {item["id"] for item in items}
    if unused:
        raise ValueError(f"Profile selectors refer to variations outside the recalled set: {', '.join(sorted(unused))}.")
    if not items or (not query.get("candidate_ids") and int(query.get("limit", 10)) <= 0):
        return {
            "decision": "gap",
            "reason": "No record passed the requested role, knowledge-readiness, and recall gates; do not force a match.",
            "reason_codes": ["knowledge-gap"],
            "results": [],
        }
    results = [evaluate_item_profiles(item, query) for item in items]
    results.sort(key=fit_rank, reverse=True)
    if not query.get("candidate_ids"):
        results = results[:max(int(query.get("limit", 10)), 0)]
    regular = [result for result in results if result["recommendation_eligible"]]
    decisions = {result["decision"] for result in regular}
    if "compatible" in decisions:
        decision = "compatible"
    elif "conditional" in decisions:
        decision = "conditional"
    elif any(
        result["decision"] == "method-only" and result["knowledge_eligibility"] == "method-inspiration"
        for result in results
    ):
        decision = "method-only"
    elif query.get("candidate_ids") and any(result["decision"] == "incompatible" for result in results):
        decision = "incompatible"
    else:
        decision = "gap"
    return {
        "decision": decision,
        "reason": "Candidates are ordered by knowledge eligibility, declared intent and joint data fit; "
        "ties retain recall order. Institutional fit and identifying assumptions still require canonical review.",
        "research_intent": query.get("intent", {}),
        "reason_codes": sorted({code for result in results for code in result["reason_codes"]}),
        "results": results,
    }


def load_query(path: str) -> dict[str, Any]:
    text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    value = yaml.safe_load(text)
    if not isinstance(value, dict):
        raise ValueError("query must be a YAML or JSON object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply deterministic Econ-Variation knowledge and data-fit gates.")
    parser.add_argument("--query", required=True, help="YAML/JSON query path, or '-' for stdin.")
    args = parser.parse_args()
    try:
        payload = match_query(load_query(args.query))
    except (OSError, ValueError, yaml.YAMLError) as exc:
        parser.error(str(exc))
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
