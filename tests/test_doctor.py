from __future__ import annotations

import json
from datetime import datetime, timedelta

import doctor


def snapshot(*, fresh: bool = True, valid: bool = True, stop: bool = False) -> dict:
    return {
        "repository_valid": valid,
        "validation_error_count": 0 if valid else 1,
        "validation_warning_count": 2,
        "generated_fresh": fresh,
        "health": {
            "knowledge_readiness": {"stop_bulk_discovery": stop},
            "quality_debt": {
                "legacy_backlog": {"record_count": 38, "missing_primary_evidence": 37},
                "managed_active_pipeline": {
                    "record_count": 9,
                    "missing_primary_evidence": 4,
                    "invalid_evidence_paths": 12,
                },
            },
        },
    }


def configure(monkeypatch, tmp_path, rows: list[dict], value: dict) -> None:
    tasks = tmp_path / "tasks.jsonl"
    tasks.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
    candidates = tmp_path / "candidates.jsonl"
    candidates.write_text("", encoding="utf-8")
    monkeypatch.setattr(doctor, "TASKS", tasks)
    monkeypatch.setattr(doctor, "CANDIDATES", candidates)
    monkeypatch.setattr(doctor, "repository_snapshot", lambda: value)


def test_doctor_is_compact_read_only_and_prioritizes_generated_freshness(monkeypatch, tmp_path) -> None:
    rows = [
        {"id": f"task-{number}", "stage": "audit", "goal": "x" * 500, "status": "pending"}
        for number in range(10)
    ]
    configure(monkeypatch, tmp_path, rows, snapshot(fresh=False))
    before = doctor.TASKS.read_bytes()
    report = doctor.build_report()
    assert report["safe_action"] == "regenerate-and-check-generated"
    assert len(report["next_tasks"]) == 3
    assert len(json.dumps(report, ensure_ascii=False).encode()) < 2048
    assert doctor.TASKS.read_bytes() == before


def test_doctor_reports_expired_active_task(monkeypatch, tmp_path) -> None:
    current = datetime.now().astimezone()
    rows = [{
        "id": "task-active",
        "stage": "ground",
        "status": "claimed",
        "claimed_by": "kimi",
        "lease_expires_at": (current - timedelta(minutes=1)).isoformat(),
    }]
    configure(monkeypatch, tmp_path, rows, snapshot())
    report = doctor.build_report(current=current)
    assert report["active_task"]["expired"] is True
    assert report["safe_action"] == "reclaim-expired-task"


def test_doctor_hides_discovery_when_stop_is_active(monkeypatch, tmp_path) -> None:
    rows = [
        {"id": "screen", "stage": "screen", "goal": "Screen", "status": "pending"},
        {"id": "ground", "stage": "ground", "goal": "Ground", "status": "pending"},
    ]
    configure(monkeypatch, tmp_path, rows, snapshot(stop=True))
    report = doctor.build_report()
    assert [task["id"] for task in report["next_tasks"]] == ["ground"]
    assert report["safe_action"] == "claim-next-listed-task"


def test_doctor_prioritizes_china_facing_post_screen_work(monkeypatch, tmp_path) -> None:
    rows = [
        {
            "id": "method-screen", "stage": "screen", "goal": "Method", "status": "pending",
            "knowledge_role_hint": "transferable-method", "created_at": "2026-01-01T00:00:00+00:00",
        },
        {
            "id": "china-resolve", "stage": "resolve", "goal": "China", "status": "pending",
            "knowledge_role_hint": "china-variation", "created_at": "2026-01-02T00:00:00+00:00",
        },
    ]
    configure(monkeypatch, tmp_path, rows, snapshot())
    assert doctor.build_report()["next_tasks"][0]["id"] == "china-resolve"


def test_doctor_validation_failure_takes_precedence(monkeypatch, tmp_path) -> None:
    configure(monkeypatch, tmp_path, [], snapshot(fresh=False, valid=False))
    assert doctor.build_report()["safe_action"] == "inspect-validation-errors"


def test_doctor_flags_multiple_active_tasks(monkeypatch, tmp_path) -> None:
    current = datetime.now().astimezone()
    rows = [
        {
            "id": f"task-{number}",
            "stage": "audit",
            "status": "claimed",
            "claimed_by": f"agent-{number}",
            "lease_expires_at": (current + timedelta(minutes=10)).isoformat(),
        }
        for number in range(2)
    ]
    configure(monkeypatch, tmp_path, rows, snapshot())
    report = doctor.build_report(current=current)
    assert "multiple-active-tasks" in report["issues"]
    assert report["safe_action"] == "resolve-multiple-active-tasks"


def test_doctor_turns_an_unqueued_candidate_into_an_executable_next_action(monkeypatch, tmp_path) -> None:
    configure(monkeypatch, tmp_path, [], snapshot(stop=True))
    doctor.CANDIDATES.write_text(
        json.dumps({
            "id": "candidate-x", "name": "A retained case", "stage": "resolve", "status": "pending",
        }) + "\n",
        encoding="utf-8",
    )
    report = doctor.build_report()
    assert report["safe_action"] == "enqueue-candidate-follow-up"
    assert report["open_candidates"][0]["id"] == "candidate-x"
