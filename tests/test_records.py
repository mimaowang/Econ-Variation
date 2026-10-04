from __future__ import annotations

from validate import run
from econ_variation_lib import identity_fingerprint, knowledge_eligibility, load_records, public_url_issues


def test_repository_records_validate() -> None:
    audit, report = run(write_health=False)
    assert report["record_count"] >= 3
    assert audit.errors == []
    assert report["knowledge_role_counts"]["china-variation"] > report["knowledge_role_counts"]["transferable-method"]
    assert report["repository_health"]["status"] == "valid"
    assert "state_counts" not in report
    assert "operational_provenance" not in report
    assert set(report["quality_debt"]) == {
        "legacy_backlog", "managed_active_pipeline", "possible_duplicate_warnings",
    }
    assert len(report["priority_audit_ids"]) <= 10


def test_identity_fingerprint_is_stable() -> None:
    records, failures = load_records()
    assert not failures
    assert identity_fingerprint(records[0].data) == identity_fingerprint(records[0].data)


def test_public_url_guard() -> None:
    assert "non-http-scheme" in public_url_issues("javascript:alert(1)")
    assert "userinfo-not-allowed" in public_url_issues("https://user:pass@example.org/x")
    assert "sensitive-query-parameter" in public_url_issues("https://example.org/x?token=secret")
    assert "placeholder-host" in public_url_issues("https://example.org/source")
    assert "non-public-ip" in public_url_issues("http://127.0.0.1/x")


def test_scope_roles_and_method_contracts_are_explicit() -> None:
    records, failures = load_records()
    assert not failures
    for record in records:
        role = record.data["scope"]["knowledge_role"]
        if role == "transferable-method":
            assert record.data["scope"]["country"] != "China"
            assert record.data["method_transfer"]["china_use_cases"]
        else:
            assert record.data["method_transfer"] is None


def test_health_and_router_share_one_static_eligibility_contract() -> None:
    from build_router import build

    _, health = run(write_health=False)
    router = build()
    assert health["knowledge_readiness"]["eligibility_counts"] == router["recommendation_eligibility_counts"]
    assert sum(health["knowledge_readiness"]["eligibility_counts"].values()) == health["record_count"]


def test_managed_extracted_method_remains_a_lead_until_grounded() -> None:
    data = {
        "status": "extracted",
        "provenance": {"task_id": "task-managed"},
        "scope": {"knowledge_role": "transferable-method"},
    }
    assert knowledge_eligibility(data) == "method-lead"
    data["status"] = "grounded"
    assert knowledge_eligibility(data) == "method-inspiration"


def test_health_exposes_separate_closed_loop_signals() -> None:
    _, report = run(write_health=False)
    assert report["knowledge_readiness"]["work_mode"] in {"balanced", "close-open-loops"}
    assert isinstance(report["knowledge_readiness"]["feedback_reasons"], list)
    assert isinstance(report["canonical_admission_debt_ids"], list)
    assert isinstance(report["promotion_ready_ids"], list)
    assert "imprecise_evidence_paths" in report["quality_debt"]["managed_active_pipeline"]
    assert "open_candidate_count" not in report["knowledge_readiness"]
