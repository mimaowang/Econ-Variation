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
ROLE_PRIORITY = {"china-variation": 30, "global-china-variation": 20, "transferable-method": 0}
STAGE_PRIORITY = {"ground": 50, "resolve": 45, "audit": 40, "consolidate": 40, "screen": 15, "discover": 10}
CANDIDATE_TERMINAL = {"resolved", "contested", "skipped", "blocked"}


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


def canonical_ids() -> list[str]:
    return sorted(path.stem for path in (ROOT / "variations").glob("*.md") if path.name != "template.md")


def is_deepseek_harness_agent(agent: object) -> bool:
    """Recognize the explicit runtime marker used by DeepSeek Harness workers."""
    name = str(agent or "").casefold()
    return name.startswith("dsh-") or "-dsh-" in name or "deepseek-harness" in name


def build_task_brief(task: dict, candidate: dict | None = None) -> dict:
    """Build a compact, non-persistent state estimate for a context-constrained agent."""
    stage = str(task.get("stage", ""))
    purpose = {
        "screen": "Decide whether one source contains recoverable knowledge worth deeper work.",
        "discover": "Close a demonstrated coverage gap without publishing an ungrounded lead.",
        "resolve": "Resolve one variation's identity and primary assignment mechanism before extraction.",
        "ground": "Replace a named knowledge gap with inspected institutional and research evidence.",
        "audit": "Test whether an existing record is decision-sufficient for a fresh reader.",
        "consolidate": "Restore one coherent assignment boundary across overlapping records.",
    }.get(stage, "Complete one bounded knowledge decision.")
    finish_when = {
        "screen": "Record candidate, skipped, or blocked; canonical files remain unchanged.",
        "resolve": "The identity and assignment are resolved; publish only if the canonical admission gate is met.",
        "ground": "A fresh reader can recover the institutional core, assignment, evidence boundary, and data join.",
        "audit": "A fresh reader can reconstruct treatment, comparison, data needs, threats, and unresolved limits.",
        "consolidate": "Each surviving record has one implementation regime and one primary assignment mechanism.",
    }.get(stage, "The bounded goal is closed with evidence or an explicit blocker.")
    focus = str(task.get("goal", "")).strip()[:240]
    if candidate:
        reason = " ".join(str(candidate.get("reason", "")).split())
        if reason:
            focus = f"{focus} Candidate reason: {reason}"[:420]
    read_first = ["AGENTS.md", "guides/mental-model.md"]
    if candidate:
        read_first.append(f"candidate:{candidate.get('id')}")
    elif task.get("source"):
        read_first.append(str(task.get("source"))[:180])
    stop_when = (
        "If identity or core evidence cannot be recovered, preserve the candidate and finish blocked or skipped; "
        "do not publish an extracted canonical record."
    )
    if stage == "screen":
        stop_when = "Do not modify canonical records; inaccessible evidence is blocked, not replaced by search prose."
    if is_deepseek_harness_agent(task.get("claimed_by")):
        stop_when = (
            f"{stop_when} Read guides/deepseek-harness.md. After each concrete retrieval route, compare what it added; "
            "if the same source family returns without a new locator or decision-relevant field, treat the evidence pass "
            "as saturated, write established/missing/next, and close blocked or preserve the candidate. Continue only for "
            "a named new route that could close a real gap; do not change query wording merely to prolong the turn. "
            "At completion use the normal task_queue.py complete path once; if its knowledge gate fails, preserve the "
            "error and release or fail the task rather than bypassing the gate with a direct Python call."
        )
    return {
        "purpose": purpose,
        "focus": focus,
        "read_first": read_first[:3],
        "finish_when": finish_when,
        "stop_when": stop_when,
    }


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


def assert_canonical_workspace_restored(task: dict, action: str) -> None:
    """Prevent release-like transitions from normalizing undeclared canonical file changes."""
    if "canonical_digest_at_claim" in task:
        if task.get("canonical_digest_at_claim") != canonical_digest():
            raise RuntimeError(f"restore canonical variation files before attempting to {action}")
        return
    if "canonical_ids_at_claim" not in task:
        return
    before = set(task.get("canonical_ids_at_claim") or [])
    after = set(canonical_ids())
    if before != after:
        deleted = sorted(before - after)
        added = sorted(after - before)
        raise RuntimeError(
            f"restore canonical file set before attempting to {action}; deleted={deleted}, added={added}"
        )


def recover() -> None:
    if not TRANSACTION.exists():
        return
    value = json.loads(TRANSACTION.read_text(encoding="utf-8"))
    if value.get("version") not in {1, 2} or not isinstance(value.get("tasks"), list) or not isinstance(value.get("runs"), list):
        raise RuntimeError("queue transaction is unreadable")
    write_jsonl(TASKS, value["tasks"])
    write_jsonl(RUNS, value["runs"])
    if value.get("version") == 2:
        if not isinstance(value.get("candidates"), list):
            raise RuntimeError("queue transaction candidates are unreadable")
        write_jsonl(CANDIDATES, value["candidates"])
    TRANSACTION.unlink()


def commit(
    before_tasks: list[dict],
    before_runs: list[dict],
    tasks: list[dict],
    runs: list[dict],
    operation: str,
    *,
    before_candidates: list[dict] | None = None,
    candidates: list[dict] | None = None,
) -> None:
    with_candidates = before_candidates is not None or candidates is not None
    if with_candidates and (before_candidates is None or candidates is None):
        raise RuntimeError("candidate transaction requires before and after state")
    transaction = {"version": 2 if with_candidates else 1, "operation": operation, "tasks": before_tasks, "runs": before_runs}
    if before_candidates is not None:
        transaction["candidates"] = before_candidates
    write_json(TRANSACTION, transaction)
    try:
        write_jsonl(TASKS, tasks)
        write_jsonl(RUNS, runs)
        if candidates is not None:
            write_jsonl(CANDIDATES, candidates)
    except Exception:
        raise
    else:
        TRANSACTION.unlink()


def effective_priority(task: dict) -> int:
    explicit = int(task.get("priority") or 0)
    return explicit + STAGE_PRIORITY.get(str(task.get("stage")), 0) + ROLE_PRIORITY.get(
        str(task.get("knowledge_role_hint")), 0
    )


def new_task(
    stage: str,
    goal: str,
    idempotency_key: str,
    source: str | None,
    *,
    candidate_id: str | None = None,
    knowledge_role: str | None = None,
    priority: int = 0,
) -> dict:
    task = {
        "id": f"task-{uuid.uuid4().hex[:12]}", "idempotency_key": idempotency_key, "stage": stage,
        "goal": goal, "source": source, "status": "pending", "attempts": 0, "records_touched": [],
        "created_at": timestamp(), "priority": priority,
        "candidate_id": candidate_id, "knowledge_role_hint": knowledge_role,
    }
    return {key: value for key, value in task.items() if value is not None}


def enqueue(
    stage: str,
    goal: str,
    idempotency_key: str,
    source: str | None,
    candidate_id: str | None = None,
    knowledge_role: str | None = None,
    priority: int = 0,
) -> dict:
    if stage not in STAGES:
        raise RuntimeError(f"invalid stage: {stage}")
    if stage == "screen" and not str(source or "").strip():
        raise RuntimeError("screen tasks require a source")
    with workspace_lock("task-queue"):
        recover()
        tasks = load(TASKS)
        before_tasks = [dict(row) for row in tasks]
        existing = next((row for row in tasks if row.get("idempotency_key") == idempotency_key), None)
        if existing:
            return existing
        candidates = load(CANDIDATES)
        candidate = None
        if candidate_id:
            candidate = next((row for row in candidates if row.get("id") == candidate_id), None)
            if not candidate:
                raise RuntimeError(f"candidate not found: {candidate_id}")
            if candidate.get("status") in CANDIDATE_TERMINAL:
                raise RuntimeError(f"candidate is already terminal: {candidate_id}")
            if stage != candidate.get("stage"):
                raise RuntimeError(f"candidate requires stage {candidate.get('stage')}")
            knowledge_role = str(candidate.get("knowledge_role") or knowledge_role or "")
        if knowledge_role and knowledge_role not in ROLE_PRIORITY:
            raise RuntimeError("invalid knowledge role hint")
        task = new_task(
            stage, goal, idempotency_key, source, candidate_id=candidate_id,
            knowledge_role=knowledge_role, priority=priority,
        )
        tasks.append(task)
        if candidate is not None:
            before_tasks, before_candidates = [dict(row) for row in tasks[:-1]], [dict(row) for row in candidates]
            candidate.update({"status": "queued", "follow_up_task_id": task["id"]})
            commit(
                before_tasks, load(RUNS), tasks, load(RUNS), "enqueue-candidate",
                before_candidates=before_candidates, candidates=candidates,
            )
        else:
            write_jsonl(TASKS, tasks)
        return task


def peek() -> dict:
    tasks = load(TASKS)
    pending = [row for row in tasks if row.get("status") == "pending"]
    pending.sort(key=lambda row: (-effective_priority(row), str(row.get("created_at", "")), str(row.get("id", ""))))
    return pending[0] if pending else {}


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
        before_tasks = [dict(row) for row in tasks]
        claimed = next((row for row in tasks if row.get("status") == "claimed"), None)
        if claimed:
            raise RuntimeError(
                f"shared worktree already has claimed task {claimed.get('id')}; complete, release, or reclaim it first"
            )
        eligible = [
            row for row in tasks
            if row.get("status") == "pending"
            and (task_id is None or row.get("id") == task_id)
            and (stage is None or row.get("stage") == stage)
        ]
        eligible.sort(key=lambda row: (-effective_priority(row), str(row.get("created_at", "")), str(row.get("id", ""))))
        task = eligible[0] if eligible else None
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
        else:
            task["canonical_ids_at_claim"] = canonical_ids()
        candidate_id = task.get("candidate_id")
        candidate = None
        if candidate_id:
            candidates = load(CANDIDATES)
            before_candidates = [dict(row) for row in candidates]
            candidate = next((row for row in candidates if row.get("id") == candidate_id), None)
            if not candidate:
                raise RuntimeError(f"linked candidate not found: {candidate_id}")
            candidate["status"] = "in-progress"
            commit(
                before_tasks, load(RUNS), tasks, load(RUNS), "claim-candidate",
                before_candidates=before_candidates, candidates=candidates,
            )
        else:
            write_jsonl(TASKS, tasks)
        result = dict(task)
        result.pop("canonical_ids_at_claim", None)
        result["task_brief"] = build_task_brief(task, candidate)
        return result


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
    ]
    for command in commands:
        # Daily knowledge checks; code regressions, benchmarks and lint run in CI.
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=300, check=False)
        if result.returncode:
            raise RuntimeError(f"knowledge gate failed: {' '.join(command)}\n{result.stdout}\n{result.stderr}")


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


def linked_candidate(candidates: list[dict], task: dict) -> dict | None:
    candidate_id = task.get("candidate_id")
    if not candidate_id:
        return None
    candidate = next((row for row in candidates if row.get("id") == candidate_id), None)
    if not candidate:
        raise RuntimeError(f"linked candidate not found: {candidate_id}")
    return candidate


def close_candidate(candidate_id: str, status: str, records: list[str], note: str) -> dict:
    if status not in CANDIDATE_TERMINAL:
        raise RuntimeError("candidate close status must be terminal")
    if status in {"resolved", "contested"} and not records:
        raise RuntimeError(f"candidate status {status} requires at least one canonical record")
    missing = [record for record in records if not (ROOT / "variations" / f"{record}.md").exists()]
    if missing:
        raise RuntimeError(f"candidate close references missing records: {missing}")
    if not note.strip():
        raise RuntimeError("candidate close requires a reconciliation note")
    with workspace_lock("task-queue"):
        recover()
        tasks, runs, candidates = load(TASKS), load(RUNS), load(CANDIDATES)
        before_candidates = [dict(row) for row in candidates]
        candidate = next((row for row in candidates if row.get("id") == candidate_id), None)
        if not candidate:
            raise RuntimeError(f"candidate not found: {candidate_id}")
        if candidate.get("status") in CANDIDATE_TERMINAL:
            return candidate
        candidate.update({
            "status": status,
            "outcome": "historical-reconciliation",
            "closed_at": timestamp(),
            "resolved_record_ids": records,
            "closure_note": note.strip(),
        })
        commit(
            tasks, runs, tasks, runs, "candidate-close",
            before_candidates=before_candidates, candidates=candidates,
        )
        return candidate


def validate_touched_record(canonical, outcome: str = "updated", *, is_new: bool = False) -> None:
    from validate import EVIDENCE_PATH, is_precise_evidence_path

    safety_demotion = not is_new and outcome == "contested" and canonical.data.get("status") == "contested"
    for evidence in canonical.data.get("evidence", []):
        invalid_paths = [path for path in evidence.get("supports", []) if not EVIDENCE_PATH.match(str(path))]
        if invalid_paths and not safety_demotion:
            raise RuntimeError(
                f"{canonical.id}: touched evidence {evidence.get('id')} has non-field support paths {invalid_paths}"
            )
        imprecise_paths = [path for path in evidence.get("supports", []) if not is_precise_evidence_path(path)]
        if imprecise_paths and not safety_demotion:
            raise RuntimeError(
                f"{canonical.id}: touched evidence {evidence.get('id')} requires precise field support paths; "
                f"replace {imprecise_paths} with schema-backed paths such as assignment.rule"
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
        has_canonical_baseline = "canonical_ids_at_claim" in task
        claimed_ids = set(task.get("canonical_ids_at_claim") or [])
        current_ids = set(canonical_ids())
        if has_canonical_baseline:
            deleted_ids = sorted(claimed_ids - current_ids)
            if deleted_ids:
                raise RuntimeError(f"canonical records cannot be deleted during a task: {deleted_ids}")
        new_ids = current_ids - claimed_ids if has_canonical_baseline else set()
        undeclared_new_ids = sorted(new_ids - set(records))
        if undeclared_new_ids:
            raise RuntimeError(f"new canonical records must be declared at completion: {undeclared_new_ids}")
    missing = [record for record in records if not (ROOT / "variations" / f"{record}.md").exists()]
    if missing:
        raise RuntimeError(f"touched canonical records do not exist: {missing}")
    if outcome in {"created", "updated", "consolidated", "contested"} and not records:
        raise RuntimeError(f"outcome {outcome} requires at least one touched record")
    for record_id in records:
        canonical = read_frontmatter(ROOT / "variations" / f"{record_id}.md")
        if (canonical.data.get("provenance") or {}).get("task_id") != task_id:
            raise RuntimeError(f"{record_id}: canonical provenance must name task {task_id}")
        if record_id in new_ids:
            status = canonical.data.get("status")
            if status == "contested" and outcome != "contested":
                raise RuntimeError(f"{record_id}: a new contested record requires outcome contested")
            if status in {"grounded", "design-documented"} and outcome not in {"created", "consolidated"}:
                raise RuntimeError(f"{record_id}: a new active canonical record requires outcome created or consolidated")
            if status not in {"grounded", "design-documented", "contested"}:
                raise RuntimeError(
                    f"{record_id}: new canonical records must be grounded or design-documented; "
                    "keep unresolved knowledge in the linked candidate and finish blocked or skipped"
                )
        validate_touched_record(canonical, outcome, is_new=record_id in new_ids)
    if gate:
        run_gate()
    with workspace_lock("task-queue"):
        recover()
        tasks, runs, candidates = load(TASKS), load(RUNS), load(CANDIDATES)
        before_tasks, before_runs = [dict(row) for row in tasks], [dict(row) for row in runs]
        before_candidates = [dict(row) for row in candidates]
        task = find(tasks, task_id)
        assert_active_claim(task, agent, claim_token, "complete")
        task.update({"status": "completed", "outcome": outcome, "records_touched": records, "finished_at": timestamp()})
        if candidate_id:
            task["candidate_id"] = candidate_id
        for key in (
            "lease_expires_at", "claim_token", "heartbeat_at", "canonical_ids_at_claim", "canonical_digest_at_claim",
        ):
            task.pop(key, None)
        event = {
            "id": f"run-{uuid.uuid4().hex[:12]}", "task_id": task_id, "agent": agent, "stage": task["stage"],
            "goal": task["goal"], "source": task.get("source"), "attempt": task.get("attempts"),
            "started_at": task.get("claimed_at"), "outcome": outcome, "records_touched": records,
            "finished_at": task["finished_at"], "note": note,
            "candidate_id": candidate_id or task.get("candidate_id"),
            "override_reason": task.get("override_reason"),
        }
        runs.append({key: value for key, value in event.items() if value is not None})
        if task.get("stage") == "screen" and outcome == "candidate":
            candidate = next((row for row in candidates if row.get("id") == candidate_id), None)
            if not candidate:
                raise RuntimeError("screen candidate disappeared before completion")
            if not candidate.get("follow_up_task_id"):
                follow_up = new_task(
                    candidate["stage"],
                    f"Resolve candidate: {candidate['name']}. {candidate['reason']}",
                    f"candidate:{candidate['id']}",
                    candidate.get("source"),
                    candidate_id=candidate["id"],
                    knowledge_role=candidate.get("knowledge_role"),
                )
                tasks.append(follow_up)
                candidate.update({"status": "queued", "follow_up_task_id": follow_up["id"]})
        elif task.get("candidate_id"):
            linked = next((row for row in candidates if row.get("id") == task["candidate_id"]), None)
            if not linked:
                raise RuntimeError(f"linked candidate not found: {task['candidate_id']}")
            terminal = {
                "created": "resolved", "updated": "resolved", "consolidated": "resolved",
                "contested": "contested", "skipped": "skipped", "blocked": "blocked",
            }.get(outcome)
            if terminal:
                linked.update({
                    "status": terminal,
                    "outcome": outcome,
                    "closed_at": task["finished_at"],
                    "resolved_record_ids": records,
                })
        commit(
            before_tasks, before_runs, tasks, runs, "complete",
            before_candidates=before_candidates, candidates=candidates,
        )
        if gate:
            run_generated_check()
    return task


def fail(task_id: str, agent: str, claim_token: str, reason_code: str, reason: str, retryable: bool) -> dict:
    with workspace_lock("task-queue"):
        recover()
        tasks, runs, candidates = load(TASKS), load(RUNS), load(CANDIDATES)
        before_tasks, before_runs = [dict(row) for row in tasks], [dict(row) for row in runs]
        before_candidates = [dict(row) for row in candidates]
        task = find(tasks, task_id)
        assert_active_claim(task, agent, claim_token, "fail")
        assert_canonical_workspace_restored(task, "fail")
        task.update({"status": "failed", "reason_code": reason_code, "reason": reason, "retryable": retryable, "finished_at": timestamp()})
        for key in (
            "lease_expires_at", "claim_token", "heartbeat_at", "canonical_ids_at_claim", "canonical_digest_at_claim",
        ):
            task.pop(key, None)
        runs.append({
            "id": f"run-{uuid.uuid4().hex[:12]}", "task_id": task_id, "agent": agent, "stage": task["stage"],
            "outcome": "failed", "reason_code": reason_code, "retryable": retryable, "finished_at": task["finished_at"],
            "override_reason": task.get("override_reason"),
        })
        candidate = linked_candidate(candidates, task)
        if candidate:
            candidate.update({"status": "blocked", "failure_task_id": task_id, "failure_reason": reason})
        commit(
            before_tasks, before_runs, tasks, runs, "fail",
            before_candidates=before_candidates, candidates=candidates,
        )
        return task


def release(task_id: str, agent: str, claim_token: str, note: str | None) -> dict:
    with workspace_lock("task-queue"):
        recover()
        tasks, runs, candidates = load(TASKS), load(RUNS), load(CANDIDATES)
        before_tasks, before_candidates = [dict(row) for row in tasks], [dict(row) for row in candidates]
        task = find(tasks, task_id)
        assert_active_claim(task, agent, claim_token, "release")
        assert_canonical_workspace_restored(task, "release")
        task["status"] = "pending"
        task["release_note"] = note
        for key in (
            "claimed_by", "claimed_at", "lease_expires_at", "heartbeat_at", "claim_token",
            "canonical_ids_at_claim", "canonical_digest_at_claim",
        ):
            task.pop(key, None)
        candidate = linked_candidate(candidates, task)
        if candidate:
            candidate["status"] = "queued"
        commit(
            before_tasks, runs, tasks, runs, "release",
            before_candidates=before_candidates, candidates=candidates,
        )
        return task


def retry(task_id: str) -> dict:
    with workspace_lock("task-queue"):
        recover()
        tasks, runs, candidates = load(TASKS), load(RUNS), load(CANDIDATES)
        before_tasks, before_candidates = [dict(row) for row in tasks], [dict(row) for row in candidates]
        task = find(tasks, task_id)
        if task.get("status") != "failed" or not task.get("retryable"):
            raise RuntimeError("task is not a retryable failure")
        task["status"] = "pending"
        for key in (
            "reason", "reason_code", "retryable", "finished_at", "claimed_by", "claimed_at", "claim_token",
            "lease_expires_at", "heartbeat_at", "canonical_ids_at_claim", "canonical_digest_at_claim",
        ):
            task.pop(key, None)
        candidate = linked_candidate(candidates, task)
        if candidate:
            candidate["status"] = "queued"
            candidate.pop("failure_task_id", None)
            candidate.pop("failure_reason", None)
        commit(
            before_tasks, runs, tasks, runs, "retry",
            before_candidates=before_candidates, candidates=candidates,
        )
        return task


def reclaim_expired() -> dict:
    with workspace_lock("task-queue"):
        recover()
        tasks, runs, candidates = load(TASKS), load(RUNS), load(CANDIDATES)
        before_tasks, before_candidates = [dict(row) for row in tasks], [dict(row) for row in candidates]
        reclaimed: list[str] = []
        for task in tasks:
            if task.get("status") != "claimed":
                continue
            expiry = parse_time(task.get("lease_expires_at"))
            if expiry is None or expiry > now():
                continue
            assert_canonical_workspace_restored(task, "reclaim")
            task["status"] = "pending"
            task["reclaimed_from"] = task.pop("claimed_by", None)
            task["reclaimed_at"] = timestamp()
            for key in (
                "claimed_at", "lease_expires_at", "heartbeat_at", "claim_token",
                "canonical_ids_at_claim", "canonical_digest_at_claim",
            ):
                task.pop(key, None)
            reclaimed.append(task["id"])
            candidate = linked_candidate(candidates, task)
            if candidate:
                candidate["status"] = "queued"
        if reclaimed:
            commit(
                before_tasks, runs, tasks, runs, "reclaim-expired",
                before_candidates=before_candidates, candidates=candidates,
            )
        return {"count": len(reclaimed), "tasks": reclaimed}


def main() -> int:
    parser = argparse.ArgumentParser(description="Manage bounded Econ-Variation work with leases and recovery.")
    sub = parser.add_subparsers(dest="command", required=True)
    add = sub.add_parser("enqueue")
    add.add_argument("--stage", choices=sorted(STAGES), required=True)
    add.add_argument("--goal", required=True)
    add.add_argument("--idempotency-key", required=True)
    add.add_argument("--source")
    add.add_argument("--candidate")
    add.add_argument("--knowledge-role", choices=sorted(ROLE_PRIORITY))
    add.add_argument("--priority", type=int, default=0)
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
    candidate_close = sub.add_parser("candidate-close")
    candidate_close.add_argument("--id", required=True)
    candidate_close.add_argument("--status", choices=sorted(CANDIDATE_TERMINAL), required=True)
    candidate_close.add_argument("--record", action="append", default=[])
    candidate_close.add_argument("--note", required=True)
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
        result = enqueue(
            args.stage, args.goal, args.idempotency_key, args.source,
            args.candidate, args.knowledge_role, args.priority,
        )
    elif args.command == "candidate-add":
        result = add_candidate(
            args.task_id, args.agent, args.claim_token, args.name, args.next_stage, args.reason,
            args.source, args.source_fingerprint, args.knowledge_role,
        )
    elif args.command == "candidate-close":
        result = close_candidate(args.id, args.status, args.record, args.note)
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
