from __future__ import annotations

import argparse
import json
import re
import sys
from typing import Any

sys.dont_write_bytecode = True

from econ_variation_lib import ROOT  # noqa: E402


TOKEN_RE = re.compile(r"[a-z0-9]+|[\u4e00-\u9fff]+", re.IGNORECASE)
ELIGIBILITY_ORDER = {
    "direct-candidate": 4,
    "conditional-candidate": 3,
    "method-inspiration": 2,
    "method-lead": 1,
    "lead-only": 1,
    "do-not-recommend": 0,
}


def normalize_token(token: str) -> str:
    token = token.casefold()
    if len(token) > 4 and token.endswith("ies"):
        return f"{token[:-3]}y"
    if len(token) > 3 and token.endswith("s") and not token.endswith("ss"):
        return token[:-1]
    return token


def tokenize(value: Any) -> set[str]:
    if isinstance(value, (list, tuple, set)):
        return {token for item in value for token in tokenize(item)}
    if isinstance(value, dict):
        return {token for item in value.values() for token in tokenize(item)}
    return {normalize_token(token) for token in TOKEN_RE.findall(str(value or ""))}


def weighted_fields(item: dict[str, Any]) -> list[tuple[str, int, set[str]]]:
    assignment = item.get("assignment", {})
    research_fit = item.get("research_fit", {})
    data_fit = item.get("data_fit", {})
    return [
        ("identity", 6, tokenize([item.get("id"), item.get("name"), item.get("aliases", [])])),
        ("domain", 5, tokenize(item.get("domains", []))),
        ("outcome", 5, tokenize([research_fit.get("outcomes", []), research_fit.get("application_outcomes", [])])),
        ("assignment", 4, tokenize(assignment)),
        (
            "data",
            4,
            tokenize(
                [
                    data_fit.get("required_identifiers", []),
                    data_fit.get("required_fields", []),
                    data_fit.get("treatment_key", []),
                ]
            ),
        ),
        ("design", 3, tokenize(research_fit.get("design_families", []))),
        ("risk", 2, tokenize([item.get("threat_types", []), item.get("blocker_codes", [])])),
    ]


def phrase_matches(value: str, choices: list[Any]) -> bool:
    wanted = tokenize(value)
    return bool(wanted) and any(wanted <= tokenize(choice) for choice in choices)


def knowledge_gate(item: dict[str, Any], eligibility: str | None, include_leads: bool) -> bool:
    actual = item["recommendation_eligibility"]
    if eligibility:
        return actual == eligibility
    if actual == "do-not-recommend":
        return False
    return actual not in {"lead-only", "method-lead"} or include_leads


def score_item(item: dict[str, Any], query_tokens: set[str]) -> tuple[int, list[str]] | None:
    if not query_tokens:
        return 0, []
    fields = weighted_fields(item)
    available = {token for _, _, field_tokens in fields for token in field_tokens}
    if not query_tokens <= available:
        return None
    score = 0
    why: list[str] = []
    for token in sorted(query_tokens):
        best = max(((weight, name) for name, weight, field_tokens in fields if token in field_tokens), default=None)
        if best:
            score += best[0]
            why.append(f"{token}:{best[1]}")
    return score, why


def search_items(
    items: list[dict[str, Any]],
    *,
    roles: list[str] | None = None,
    eligibility: str | None = None,
    domains: list[str] | None = None,
    design: str | None = None,
    identifiers: list[str] | None = None,
    text: list[str] | None = None,
    variation_types: list[str] | None = None,
    include_leads: bool = False,
    limit: int = 10,
) -> list[dict[str, Any]]:
    roles = roles or []
    domains = domains or []
    identifiers = identifiers or []
    variation_types = variation_types or []
    query_tokens = tokenize(text or [])
    ranked: list[dict[str, Any]] = []
    for item in items:
        if not knowledge_gate(item, eligibility, include_leads):
            continue
        if roles and item["knowledge_role"] not in roles:
            continue
        if variation_types and item["variation_type"] not in variation_types:
            continue
        if domains and not all(phrase_matches(domain, item.get("domains", [])) for domain in domains):
            continue
        if design and not phrase_matches(design, item.get("research_fit", {}).get("design_families", [])):
            continue
        required_identifiers = item.get("data_fit", {}).get("required_identifiers", [])
        if identifiers and not all(phrase_matches(identifier, required_identifiers) for identifier in identifiers):
            continue
        scored = score_item(item, query_tokens)
        if scored is None:
            continue
        score, why = scored
        ranked.append({"item": item, "score": score, "why_matched": why})
    ranked.sort(
        key=lambda result: (
            -result["score"],
            -ELIGIBILITY_ORDER[result["item"]["recommendation_eligibility"]],
            result["item"]["id"],
        )
    )
    return ranked[: max(limit, 0)]


def compact_result(result: dict[str, Any]) -> dict[str, Any]:
    item = result["item"]
    assignment = item["assignment"]
    data_fit = item["data_fit"]
    return {
        "id": item["id"],
        "name": item["name"],
        "knowledge_role": item["knowledge_role"],
        "knowledge_eligibility": item["recommendation_eligibility"],
        "status": item["status"],
        "score": result["score"],
        "why_matched": result["why_matched"],
        "variation_type": item["variation_type"],
        "time": item["time"],
        "treatment": assignment.get("treatment", ""),
        "comparison": assignment.get("comparison", ""),
        "data_fit": {
            "minimum_frequency": data_fit.get("minimum_frequency"),
            "minimum_pre_periods": data_fit.get("minimum_pre_periods"),
            "minimum_post_periods": data_fit.get("minimum_post_periods"),
            "required_identifiers": data_fit.get("required_identifiers", []),
            "required_fields": data_fit.get("required_fields", []),
            "treatment_key": data_fit.get("treatment_key", []),
        },
        "blocker_codes": item.get("blocker_codes", []),
        "threat_types": item.get("threat_types", []),
        "source_path": item["source_path"],
    }


def load_router() -> dict[str, Any]:
    return json.loads((ROOT / "dist" / "router.json").read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Recall Econ-Variation candidates before deterministic idea/data matching.")
    parser.add_argument("--role", action="append", choices=["china-variation", "global-china-variation", "transferable-method"])
    parser.add_argument(
        "--eligibility",
        choices=[
            "direct-candidate", "conditional-candidate", "lead-only", "method-inspiration", "method-lead",
            "do-not-recommend",
        ],
    )
    parser.add_argument("--domain", action="append")
    parser.add_argument("--design")
    parser.add_argument("--identifier", action="append")
    parser.add_argument("--variation-type", action="append")
    parser.add_argument("--text", action="append", default=[])
    parser.add_argument("--include-leads", action="store_true", help="Include lead-only records for audit, never as recommendations.")
    parser.add_argument("--verbose", action="store_true", help="Return full router entries instead of compact decision summaries.")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    router = load_router()
    results = search_items(
        router["variations"],
        roles=args.role,
        eligibility=args.eligibility,
        domains=args.domain,
        design=args.design,
        identifiers=args.identifier,
        text=args.text,
        variation_types=args.variation_type,
        include_leads=args.include_leads,
        limit=args.limit,
    )
    if not results:
        payload: dict[str, Any] = {
            "decision": "gap",
            "reason": "No record passed the knowledge gate and requested recall filters; do not force a match.",
            "results": [],
        }
    else:
        payload = {
            "decision": "matches",
            "result_count": len(results),
            "results": [result["item"] if args.verbose else compact_result(result) for result in results],
        }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
