from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from econ_variation_lib import ROOT, STATE_DIR, read_jsonl


TASKS = STATE_DIR / "tasks.jsonl"
CANDIDATES = STATE_DIR / "candidates.jsonl"
HEALTH = ROOT / "dist" / "health.json"
ROUTER = ROOT / "dist" / "router.json"


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _parse_time(value: object) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None
    return parsed.astimezone() if parsed.tzinfo else parsed.astimezone()


def _expired(task: dict[str, Any], current: datetime) -> bool:
    expiry = _parse_time(task.get("lease_expires_at"))
    return expiry is None or expiry <= current


def repository_snapshot() -> dict[str, Any]:
    try:
        from check_generated import expected_router
        from validate import run

        audit, expected_health = run(write_health=False)
        health_fresh = _read_json(HEALTH) == expected_health
        router_fresh = _read_json(ROUTER) == expected_router()
        return {
            "repository_valid": not audit.errors,
            "validation_error_count": len(audit.errors),
            "validation_warning_count": len(audit.warnings),
            "generated_fresh": health_fresh and router_fresh,
            "health": expected_health,
        }
    except Exception as exc:
        return {
            "repository_valid": False,
            "validation_error_count": 1,
            "validation_warning_count": 0,
            "generated_fresh": False,
            "health": {},
            "snapshot_error": type(exc).__name__,
        }


def build_report(current: datetime | None = None) -> dict[str, Any]:
    current = current or datetime.now().astimezone()
    snapshot = repository_snapshot()
    tasks, task_errors = read_jsonl(TASKS)
    candidates, candidate_errors = read_jsonl(CANDIDATES)
    active_rows = [task for task in tasks if task.get("status") == "claimed"]
    active = [
        {
            "id": task.get("id"),
            "stage": task.get("stage"),
            "agent": task.get("claimed_by"),
            "lease_expires_at": task.get("lease_expires_at"),
            "expired": _expired(task, current),
        }
        for task in active_rows[:1]
    ]
    health = snapshot.get("health") or {}
    stop = bool((health.get("knowledge_readiness") or {}).get("stop_bulk_discovery"))
    pending = [task for task in tasks if task.get("status") == "pending"]
    if stop:
        pending = [task for task in pending if task.get("stage") not in {"screen", "discover"}]
    from task_queue import effective_priority

    pending.sort(key=lambda task: (-effective_priority(task), str(task.get("created_at", "")), str(task.get("id", ""))))
    next_tasks = [
        {
            "id": task.get("id"), "stage": task.get("stage"), "goal": str(task.get("goal", ""))[:160],
            "knowledge_role_hint": task.get("knowledge_role_hint"), "priority": effective_priority(task),
        }
        for task in pending[:3]
    ]
    debt_groups = health.get("quality_debt") or {}
    managed_debt = debt_groups.get("managed_active_pipeline") or {}
    debt = {name: count for name, count in managed_debt.items() if isinstance(count, int) and name != "record_count"}
    top_debt = [
        {"name": name, "count": count}
        for name, count in sorted(debt.items(), key=lambda item: (-item[1], item[0]))[:3]
        if count > 0
    ]
    issues: list[str] = []
    if task_errors:
        issues.append("invalid-task-state")
    if candidate_errors:
        issues.append("invalid-candidate-state")
    if snapshot.get("snapshot_error"):
        issues.append("validation-unavailable")
    if len(active_rows) > 1:
        issues.append("multiple-active-tasks")
    if not snapshot["repository_valid"]:
        action = "inspect-validation-errors"
    elif task_errors or candidate_errors:
        action = "inspect-task-state"
    elif not snapshot["generated_fresh"]:
        action = "regenerate-and-check-generated"
    elif len(active_rows) > 1:
        action = "resolve-multiple-active-tasks"
    elif active and active[0]["expired"]:
        action = "reclaim-expired-task"
    elif active:
        action = "resume-active-task"
    elif next_tasks:
        action = "claim-next-listed-task"
    elif stop:
        action = "enqueue-ground-or-audit-task"
    else:
        action = "queue-empty"
    return {
        "schema_version": 1,
        "repository_valid": snapshot["repository_valid"],
        "generated_fresh": snapshot["generated_fresh"],
        "validation_errors": snapshot["validation_error_count"],
        "validation_warnings": snapshot["validation_warning_count"],
        "stop_bulk_discovery": stop,
        "active_task": active[0] if active else None,
        "next_tasks": next_tasks,
        "candidate_status_counts": {
            status: sum(candidate.get("status") == status for candidate in candidates)
            for status in ("pending", "queued", "in-progress", "resolved", "contested", "skipped", "blocked")
        },
        "top_quality_debt": top_debt,
        "safe_action": action,
        "issues": issues,
    }


def main() -> int:
    report = build_report()
    print(json.dumps(report, ensure_ascii=False, separators=(",", ":")))
    unsafe = (
        not report["repository_valid"]
        or not report["generated_fresh"]
        or bool(report["issues"])
        or bool(report["active_task"] and report["active_task"]["expired"])
    )
    return 1 if unsafe else 0


if __name__ == "__main__":
    raise SystemExit(main())
