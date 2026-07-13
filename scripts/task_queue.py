from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import uuid
from datetime import datetime, timedelta
from pathlib import Path

sys.dont_write_bytecode = True

from econ_variation_lib import ROOT, STATE_DIR, read_frontmatter, read_jsonl, workspace_lock, write_json, write_jsonl  # noqa: E402


TASKS = STATE_DIR / "tasks.jsonl"
RUNS = STATE_DIR / "runs.jsonl"
CANDIDATES = STATE_DIR / "candidates.jsonl"
TRANSACTION = STATE_DIR / ".queue-transaction.json"
HEALTH = ROOT / "dist" / "health.json"
STAGES = {"screen", "discover", "resolve", "ground", "audit", "consolidate"}
OUTCOMES = {"created", "updated", "consolidated", "candidate", "contested", "skipped", "blocked"}
SCREEN_OUTCOMES = {"candidate", "skipped", "blocked"}


def now() -> datetime:
    return datetime.now().astimezone()


def timestamp(value: datetime | None = None) -> str:
    return (value or now()).isoformat(timespec="seconds")


def load(path: Path) -> list[dict]:
    rows, errors = read_jsonl(path)
    if errors:
        raise RuntimeError(f"{path.name} is invalid: {'; '.join(errors)}")
    return rows


def parse_time(value: object) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None
    return parsed.astimezone() if parsed.tzinfo else parsed.astimezone()


def stop_bulk_discovery() -> bool:
    if not HEALTH.exists():
        return False
    try:
        value = json.loads(HEALTH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return bool((value.get("knowledge_readiness") or {}).get("stop_bulk_discovery"))


def canonical_digest() -> str:
    digest = hashlib.sha256()
    for path in sorted((ROOT / "variations").glob("*.md"), key=lambda item: item.name.casefold()):
        digest.update(path.name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def assert_active_claim(task: dict, agent: str, claim_token: str, action: str) -> None:
    if (
        task.get("status") != "claimed"
        or task.get("claimed_by") != agent
        or not claim_token
        or task.get("claim_token") != claim_token
    ):
        raise RuntimeError(f"only the current claiming agent and token can {action} this task")
    expiry = parse_time(task.get("lease_expires_at"))
    if expiry is None or expiry <= now():
        raise RuntimeError(f"task lease expired; reclaim before attempting to {action}")


def recover() -> None:
    if not TRANSACTION.exists():
        return
    value = json.loads(TRANSACTION.read_text(encoding="utf-8"))
    if value.get("version") != 1 or not isinstance(value.get("tasks"), list) or not isinstance(value.get("runs"), list):
        raise RuntimeError("queue transaction is unreadable")
    write_jsonl(TASKS, value["tasks"])
    write_jsonl(RUNS, value["runs"])
    TRANSACTION.unlink()


def commit(before_tasks: list[dict], before_runs: list[dict], tasks: list[dict], runs: list[dict], operation: str) -> None:
    write_json(TRANSACTION, {"version": 1, "operation": operation, "tasks": before_tasks, "runs": before_runs})
    try:
        write_jsonl(TASKS, tasks)
        write_jsonl(RUNS, runs)
    except Exception:
        raise
    else:
        TRANSACTION.unlink()


def enqueue(stage: str, goal: str, idempotency_key: str, source: str | None) -> dict:
    if stage not in STAGES:
        raise RuntimeError(f"invalid stage: {stage}")
    if stage == "screen" and not str(source or "").strip():
        raise RuntimeError("screen tasks require a source")
    with workspace_lock("task-queue"):
        recover()
        tasks = load(TASKS)
        existing = next((row for row in tasks if row.get("idempotency_key") == idempotency_key), None)
        if existing:
            return existing
        task = {
            "id": f"task-{uuid.uuid4().hex[:12]}", "idempotency_key": idempotency_key, "stage": stage,
            "goal": goal, "source": source, "status": "pending", "attempts": 0, "records_touched": [],
            "created_at": timestamp(),
        }
        tasks.append({key: value for key, value in task.items() if value is not None})
        write_jsonl(TASKS, tasks)
        return task


def peek() -> dict:
    tasks = load(TASKS)
    return next((row for row in tasks if row.get("status") == "pending"), {})


def find(tasks: list[dict], task_id: str) -> dict:
    task = next((row for row in tasks if row.get("id") == task_id), None)
    if not task:
        raise RuntimeError(f"task not found: {task_id}")
    return task


def claim(
    agent: str,
    lease_minutes: int,
    task_id: str | None = None,
    stage: str | None = None,
    override_reason: str | None = None,
) -> dict:
    if lease_minutes <= 0:
        raise RuntimeError("lease must be positive")
    with workspace_lock("task-queue"):
        recover()
        tasks = load(TASKS)
        claimed = next((row for row in tasks if row.get("status") == "claimed"), None)
        if claimed:
            raise RuntimeError(
                f"shared worktree already has claimed task {claimed.get('id')}; complete, release, or reclaim it first"
            )
        task = next((
            row for row in tasks
            if row.get("status") == "pending"
            and (task_id is None or row.get("id") == task_id)
            and (stage is None or row.get("stage") == stage)
        ), None)
        if not task:
            selector = task_id or stage or "the requested queue"
            raise RuntimeError(f"no pending task for {selector}")
        if task.get("stage") in {"screen", "discover"} and stop_bulk_discovery() and not str(override_reason or "").strip():
            raise RuntimeError("bulk discovery is stopped; pass a non-empty override reason to claim this task")
        claim_token = uuid.uuid4().hex
        task.update({
            "status": "claimed", "claimed_by": agent, "claimed_at": timestamp(),
            "lease_expires_at": timestamp(now() + timedelta(minutes=lease_minutes)),
            "claim_token": claim_token, "attempts": int(task.get("attempts", 0)) + 1,
        })
        if str(override_reason or "").strip():
            task["override_reason"] = str(override_reason).strip()
        else:
            task.pop("override_reason", None)
        if task.get("stage") == "screen":
            task["canonical_digest_at_claim"] = canonical_digest()
        write_jsonl(TASKS, tasks)
        return task


def renew(task_id: str, agent: str, claim_token: str, lease_minutes: int) -> dict:
    if lease_minutes <= 0:
        raise RuntimeError("lease must be positive")
    with workspace_lock("task-queue"):
        recover()
        tasks = load(TASKS)
        task = find(tasks, task_id)
        assert_active_claim(task, agent, claim_token, "renew")
        task["lease_expires_at"] = timestamp(now() + timedelta(minutes=lease_minutes))
        task["heartbeat_at"] = timestamp()
        write_jsonl(TASKS, tasks)
        return task


def run_gate() -> None:
    commands = [
        [sys.executable, "scripts/validate.py", "--write-health"],
        [sys.executable, "scripts/build_router.py"],
        [sys.executable, "scripts/check_generated.py"],
        [sys.executable, "-m", "pytest", "-q"],
        [sys.executable, "-m", "ruff", "check", "."],
    ]
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=120, check=False)
        if result.returncode:
            raise RuntimeError(f"release gate failed: {' '.join(command)}\n{result.stdout}\n{result.stderr}")


def run_generated_check() -> None:
    command = [sys.executable, "scripts/check_generated.py"]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=120, check=False)
    if result.returncode:
        raise RuntimeError(f"post-completion generated check failed\n{result.stdout}\n{result.stderr}")


def add_candidate(
    task_id: str,
    agent: str,
    claim_token: str,
    name: str,
    next_stage: str,
    reason: str,
    source: str,
    source_fingerprint: str,
    knowledge_role: str,
) -> dict:
    if next_stage not in STAGES - {"screen"}:
        raise RuntimeError("candidate next stage must be post-screen work")
    if knowledge_role not in {"china-variation", "global-china-variation", "transferable-method"}:
        raise RuntimeError("candidate requires a supported knowledge role")
    required = {"name": name, "reason": reason, "source": source, "source_fingerprint": source_fingerprint}
    missing = [key for key, value in required.items() if not str(value or "").strip()]
    if missing:
        raise RuntimeError(f"candidate fields cannot be empty: {missing}")
    with workspace_lock("task-queue"):
        recover()
        task = find(load(TASKS), task_id)
        assert_active_claim(task, agent, claim_token, "add a candidate for")
        if task.get("stage") != "screen":
            raise RuntimeError("only a screen task may add a candidate")
        rows = load(CANDIDATES)
        existing = next((row for row in rows if row.get("source_fingerprint") == source_fingerprint), None)
        if existing:
            return existing
        candidate = {
            "id": f"candidate-{uuid.uuid4().hex[:12]}",
            "name": str(name).strip(),
            "stage": next_stage,
            "reason": str(reason).strip(),
            "source": str(source).strip(),
            "source_fingerprint": str(source_fingerprint).strip(),
            "knowledge_role": knowledge_role,
            "task_id": task_id,
            "status": "pending",
            "created_at": timestamp(),
        }
        rows.append(candidate)
        write_jsonl(CANDIDATES, rows)
        return candidate


def validate_touched_record(canonical, outcome: str = "updated") -> None:
    from validate import EVIDENCE_PATH

    safety_demotion = outcome == "contested" and canonical.data.get("status") == "contested"
    for evidence in canonical.data.get("evidence", []):
        invalid_paths = [path for path in evidence.get("supports", []) if not EVIDENCE_PATH.match(str(path))]
        if invalid_paths and not safety_demotion:
            raise RuntimeError(
                f"{canonical.id}: touched evidence {evidence.get('id')} has non-field support paths {invalid_paths}"
            )
        if evidence.get("verification_status") not in {"verified", "reported"}:
            continue
        if not safety_demotion and (
            not evidence.get("access_level") or not str(evidence.get("locator") or "").strip()
        ):
            raise RuntimeError(
                f"{canonical.id}: verified/reported evidence {evidence.get('id')} requires access_level and locator"
            )
    body = canonical.body.casefold()
    if not safety_demotion and ("[web search]" in body or "search-snippet" in body):
        raise RuntimeError(f"{canonical.id}: search snippets cannot serve as canonical evidence")
    if canonical.data.get("status") != "deprecated" and not (canonical.data.get("design") or {}).get("claim_type"):
        raise RuntimeError(f"{canonical.id}: touched records require design.claim_type")


def complete(
    task_id: str,
    agent: str,
    claim_token: str,
    outcome: str,
    records: list[str],
    note: str | None,
    candidate_id: str | None = None,
    gate: bool = True,
) -> dict:
    if outcome not in OUTCOMES:
        raise RuntimeError(f"invalid outcome: {outcome}")
    with workspace_lock("task-queue"):
        recover()
        task = find(load(TASKS), task_id)
        assert_active_claim(task, agent, claim_token, "complete")
        if task.get("stage") == "screen":
            if outcome not in SCREEN_OUTCOMES:
                raise RuntimeError(f"screen tasks only allow outcomes {sorted(SCREEN_OUTCOMES)}")
            if records:
                raise RuntimeError("screen tasks cannot touch canonical records")
            if outcome == "candidate":
                candidates = load(CANDIDATES)
                candidate = next((row for row in candidates if row.get("id") == str(candidate_id or "")), None)
                if not candidate:
                    raise RuntimeError("screen candidate outcome requires an existing candidate ID")
                if candidate.get("task_id") != task_id:
                    raise RuntimeError("screen candidate must have been created by the current task")
            if outcome != "candidate" and candidate_id:
                raise RuntimeError("only a screen candidate outcome may name a candidate ID")
            if task.get("canonical_digest_at_claim") != canonical_digest():
                raise RuntimeError("screen tasks cannot modify canonical variation files")
    missing = [record for record in records if not (ROOT / "variations" / f"{record}.md").exists()]
    if missing:
        raise RuntimeError(f"touched canonical records do not exist: {missing}")
    if outcome in {"created", "updated", "consolidated", "contested"} and not records:
        raise RuntimeError(f"outcome {outcome} requires at least one touched record")
    for record_id in records:
        canonical = read_frontmatter(ROOT / "variations" / f"{record_id}.md")
        if (canonical.data.get("provenance") or {}).get("task_id") != task_id:
            raise RuntimeError(f"{record_id}: canonical provenance must name task {task_id}")
        validate_touched_record(canonical, outcome)
    if gate:
        run_gate()
    with workspace_lock("task-queue"):
        recover()
        tasks, runs = load(TASKS), load(RUNS)
        before_tasks, before_runs = [dict(row) for row in tasks], [dict(row) for row in runs]
        task = find(tasks, task_id)
        assert_active_claim(task, agent, claim_token, "complete")
        task.update({"status": "completed", "outcome": outcome, "records_touched": records, "finished_at": timestamp()})
        if candidate_id:
            task["candidate_id"] = candidate_id
        for key in ("lease_expires_at", "claim_token", "heartbeat_at"):
            task.pop(key, None)
        event = {
            "id": f"run-{uuid.uuid4().hex[:12]}", "task_id": task_id, "agent": agent, "stage": task["stage"],
            "goal": task["goal"], "source": task.get("source"), "attempt": task.get("attempts"),
            "started_at": task.get("claimed_at"), "outcome": outcome, "records_touched": records,
            "finished_at": task["finished_at"], "note": note, "candidate_id": candidate_id,
            "override_reason": task.get("override_reason"),
        }
        runs.append({key: value for key, value in event.items() if value is not None})
        commit(before_tasks, before_runs, tasks, runs, "complete")
        if gate:
            run_generated_check()
    return task


def fail(task_id: str, agent: str, claim_token: str, reason_code: str, reason: str, retryable: bool) -> dict:
    with workspace_lock("task-queue"):
        recover()
        tasks, runs = load(TASKS), load(RUNS)
        before_tasks, before_runs = [dict(row) for row in tasks], [dict(row) for row in runs]
        task = find(tasks, task_id)
        assert_active_claim(task, agent, claim_token, "fail")
        task.update({"status": "failed", "reason_code": reason_code, "reason": reason, "retryable": retryable, "finished_at": timestamp()})
        for key in ("lease_expires_at", "claim_token", "heartbeat_at"):
            task.pop(key, None)
        runs.append({
            "id": f"run-{uuid.uuid4().hex[:12]}", "task_id": task_id, "agent": agent, "stage": task["stage"],
            "outcome": "failed", "reason_code": reason_code, "retryable": retryable, "finished_at": task["finished_at"],
            "override_reason": task.get("override_reason"),
        })
        commit(before_tasks, before_runs, tasks, runs, "fail")
        return task


def release(task_id: str, agent: str, claim_token: str, note: str | None) -> dict:
    with workspace_lock("task-queue"):
        recover()
        tasks = load(TASKS)
        task = find(tasks, task_id)
        assert_active_claim(task, agent, claim_token, "release")
        task["status"] = "pending"
        task["release_note"] = note
        for key in ("claimed_by", "claimed_at", "lease_expires_at", "heartbeat_at", "claim_token"):
            task.pop(key, None)
        write_jsonl(TASKS, tasks)
        return task


def retry(task_id: str) -> dict:
    with workspace_lock("task-queue"):
        recover()
        tasks = load(TASKS)
        task = find(tasks, task_id)
        if task.get("status") != "failed" or not task.get("retryable"):
            raise RuntimeError("task is not a retryable failure")
        task["status"] = "pending"
        for key in (
            "reason", "reason_code", "retryable", "finished_at", "claimed_by", "claimed_at", "claim_token",
            "lease_expires_at", "heartbeat_at",
        ):
            task.pop(key, None)
        write_jsonl(TASKS, tasks)
        return task


def reclaim_expired() -> dict:
    with workspace_lock("task-queue"):
        recover()
        tasks = load(TASKS)
        reclaimed: list[str] = []
        for task in tasks:
            if task.get("status") != "claimed":
                continue
            expiry = parse_time(task.get("lease_expires_at"))
            if expiry is None or expiry > now():
                continue
            task["status"] = "pending"
            task["reclaimed_from"] = task.pop("claimed_by", None)
            task["reclaimed_at"] = timestamp()
            for key in ("claimed_at", "lease_expires_at", "heartbeat_at", "claim_token"):
                task.pop(key, None)
            reclaimed.append(task["id"])
        if reclaimed:
            write_jsonl(TASKS, tasks)
        return {"count": len(reclaimed), "tasks": reclaimed}


def main() -> int:
    parser = argparse.ArgumentParser(description="Manage bounded Econ-Variation work with leases and recovery.")
    sub = parser.add_subparsers(dest="command", required=True)
    add = sub.add_parser("enqueue")
    add.add_argument("--stage", choices=sorted(STAGES), required=True)
    add.add_argument("--goal", required=True)
    add.add_argument("--idempotency-key", required=True)
    add.add_argument("--source")
    candidate_add = sub.add_parser("candidate-add")
    candidate_add.add_argument("--task-id", required=True)
    candidate_add.add_argument("--agent", required=True)
    candidate_add.add_argument("--claim-token", required=True)
    candidate_add.add_argument("--name", required=True)
    candidate_add.add_argument("--next-stage", choices=sorted(STAGES - {"screen"}), required=True)
    candidate_add.add_argument("--reason", required=True)
    candidate_add.add_argument("--source", required=True)
    candidate_add.add_argument("--source-fingerprint", required=True)
    candidate_add.add_argument(
        "--knowledge-role",
        choices=["china-variation", "global-china-variation", "transferable-method"],
        required=True,
    )
    sub.add_parser("peek")
    sub.add_parser("doctor")
    take = sub.add_parser("claim")
    take.add_argument("--agent", required=True)
    take.add_argument("--lease-minutes", type=int, default=60)
    take.add_argument("--id")
    take.add_argument("--stage", choices=sorted(STAGES))
    take.add_argument("--override-reason")
    heartbeat = sub.add_parser("renew")
    heartbeat.add_argument("--id", required=True)
    heartbeat.add_argument("--agent", required=True)
    heartbeat.add_argument("--claim-token", required=True)
    heartbeat.add_argument("--lease-minutes", type=int, default=60)
    done = sub.add_parser("complete")
    done.add_argument("--id", required=True)
    done.add_argument("--agent", required=True)
    done.add_argument("--claim-token", required=True)
    done.add_argument("--outcome", choices=sorted(OUTCOMES), required=True)
    done.add_argument("--record", action="append", default=[])
    done.add_argument("--candidate")
    done.add_argument("--note")
    failed = sub.add_parser("fail")
    failed.add_argument("--id", required=True)
    failed.add_argument("--agent", required=True)
    failed.add_argument("--claim-token", required=True)
    failed.add_argument("--reason-code", required=True)
    failed.add_argument("--reason", required=True)
    failed.add_argument("--retryable", action="store_true")
    released = sub.add_parser("release")
    released.add_argument("--id", required=True)
    released.add_argument("--agent", required=True)
    released.add_argument("--claim-token", required=True)
    released.add_argument("--note")
    again = sub.add_parser("retry")
    again.add_argument("--id", required=True)
    sub.add_parser("reclaim-expired")
    args = parser.parse_args()
    if args.command == "enqueue":
        result = enqueue(args.stage, args.goal, args.idempotency_key, args.source)
    elif args.command == "candidate-add":
        result = add_candidate(
            args.task_id, args.agent, args.claim_token, args.name, args.next_stage, args.reason,
            args.source, args.source_fingerprint, args.knowledge_role,
        )
    elif args.command == "peek":
        result = peek()
    elif args.command == "doctor":
        from doctor import build_report

        result = build_report()
    elif args.command == "claim":
        result = claim(args.agent, args.lease_minutes, args.id, args.stage, args.override_reason)
    elif args.command == "renew":
        result = renew(args.id, args.agent, args.claim_token, args.lease_minutes)
    elif args.command == "complete":
        result = complete(args.id, args.agent, args.claim_token, args.outcome, args.record, args.note, args.candidate)
    elif args.command == "fail":
        result = fail(args.id, args.agent, args.claim_token, args.reason_code, args.reason, args.retryable)
    elif args.command == "release":
        result = release(args.id, args.agent, args.claim_token, args.note)
    elif args.command == "retry":
        result = retry(args.id)
    else:
        result = reclaim_expired()
    if args.command == "doctor":
        print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    if args.command == "doctor":
        unsafe = (
            not result["repository_valid"]
            or not result["generated_fresh"]
            or bool(result["issues"])
            or bool(result["active_task"] and result["active_task"]["expired"])
        )
        return 1 if unsafe else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
