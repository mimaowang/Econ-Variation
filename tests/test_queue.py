from __future__ import annotations

import os
import time
from contextlib import nullcontext
from datetime import timedelta

import pytest

import econ_variation_lib
import task_queue


def configure(monkeypatch, tmp_path) -> None:
    state = tmp_path / "state"
    state.mkdir()
    tasks = state / "tasks.jsonl"
    tasks.write_text("", encoding="utf-8")
    runs = state / "runs.jsonl"
    runs.write_text("", encoding="utf-8")
    candidates = state / "candidates.jsonl"
    candidates.write_text("", encoding="utf-8")
    monkeypatch.setattr(task_queue, "TASKS", tasks)
    monkeypatch.setattr(task_queue, "RUNS", runs)
    monkeypatch.setattr(task_queue, "CANDIDATES", candidates)
    monkeypatch.setattr(task_queue, "HEALTH", tmp_path / "health.json")
    monkeypatch.setattr(task_queue, "TRANSACTION", state / ".transaction.json")
    monkeypatch.setattr(task_queue, "workspace_lock", lambda name: nullcontext())


def test_enqueue_is_idempotent_and_lease_can_be_renewed(monkeypatch, tmp_path) -> None:
    configure(monkeypatch, tmp_path)
    first = task_queue.enqueue("discover", "Find a case", "paper:10.example/x", None)
    assert task_queue.enqueue("discover", "Duplicate", "paper:10.example/x", None)["id"] == first["id"]
    claimed = task_queue.claim("agent-a", 10)
    old_expiry = claimed["lease_expires_at"]
    renewed = task_queue.renew(claimed["id"], "agent-a", claimed["claim_token"], 20)
    assert renewed["lease_expires_at"] > old_expiry


def test_claim_can_select_the_requested_task(monkeypatch, tmp_path) -> None:
    configure(monkeypatch, tmp_path)
    first = task_queue.enqueue("discover", "Old work", "old", None)
    second = task_queue.enqueue("audit", "Requested work", "requested", None)
    claimed = task_queue.claim("agent-a", 10, task_id=second["id"])
    assert claimed["id"] == second["id"]
    rows = task_queue.load(task_queue.TASKS)
    assert rows[0]["id"] == first["id"] and rows[0]["status"] == "pending"


def test_harness_brief_adds_saturation_cue_only_for_explicit_runtime(monkeypatch, tmp_path) -> None:
    configure(monkeypatch, tmp_path)
    task = task_queue.enqueue("resolve", "Resolve one source", "candidate:x", None)

    harness_claim = task_queue.claim("dsh-deepseek-v4-flash", 10, task_id=task["id"])
    harness_stop = harness_claim["task_brief"]["stop_when"]
    assert "guides/deepseek-harness.md" in harness_stop
    assert "saturated" in harness_stop
    assert "bypassing the gate" in harness_stop
    assert "task_brief" not in task_queue.load(task_queue.TASKS)[0]
    task_queue.release(task["id"], "dsh-deepseek-v4-flash", harness_claim["claim_token"], "test")

    ordinary_claim = task_queue.claim("deepseek-v4-flash", 10, task_id=task["id"])
    ordinary_stop = ordinary_claim["task_brief"]["stop_when"]
    assert "guides/deepseek-harness.md" not in ordinary_stop
    assert "saturated" not in ordinary_stop


def test_release_fail_retry_and_reclaim(monkeypatch, tmp_path) -> None:
    configure(monkeypatch, tmp_path)
    task = task_queue.enqueue("ground", "Ground a case", "case:x", None)
    claimed = task_queue.claim("agent-a", 10)
    task_queue.release(task["id"], "agent-a", claimed["claim_token"], "pause")
    claimed = task_queue.claim("agent-a", 10)
    task_queue.fail(task["id"], "agent-a", claimed["claim_token"], "source_unavailable", "blocked", True)
    assert task_queue.retry(task["id"])["status"] == "pending"
    claimed = task_queue.claim("agent-a", 10)
    rows = task_queue.load(task_queue.TASKS)
    rows[0]["lease_expires_at"] = task_queue.timestamp(task_queue.now() - timedelta(minutes=1))
    task_queue.write_jsonl(task_queue.TASKS, rows)
    assert task_queue.reclaim_expired()["tasks"] == [claimed["id"]]
    reclaimed = task_queue.claim("agent-a", 10)
    with pytest.raises(RuntimeError, match="token"):
        task_queue.release(task["id"], "agent-a", claimed["claim_token"], "stale")
    task_queue.release(task["id"], "agent-a", reclaimed["claim_token"], "done")


def test_interrupted_transaction_recovers(monkeypatch, tmp_path) -> None:
    configure(monkeypatch, tmp_path)
    task_queue.write_json(task_queue.TRANSACTION, {"version": 1, "tasks": [{"id": "old"}], "runs": []})
    task_queue.recover()
    assert task_queue.load(task_queue.TASKS) == [{"id": "old"}]


def test_claim_is_global_single_writer_and_token_is_fenced(monkeypatch, tmp_path) -> None:
    configure(monkeypatch, tmp_path)
    first = task_queue.enqueue("audit", "First", "first", None)
    second = task_queue.enqueue("ground", "Second", "second", None)
    claimed = task_queue.claim("agent-a", 10, task_id=first["id"])
    with pytest.raises(RuntimeError, match="already has claimed task"):
        task_queue.claim("agent-b", 10, task_id=second["id"])
    with pytest.raises(RuntimeError, match="token"):
        task_queue.renew(first["id"], "agent-a", "wrong", 10)
    with pytest.raises(RuntimeError, match="positive"):
        task_queue.renew(first["id"], "agent-a", claimed["claim_token"], 0)


def test_expired_claim_cannot_be_renewed_or_completed(monkeypatch, tmp_path) -> None:
    configure(monkeypatch, tmp_path)
    task = task_queue.enqueue("audit", "Audit", "audit", None)
    claimed = task_queue.claim("agent-a", 10)
    rows = task_queue.load(task_queue.TASKS)
    rows[0]["lease_expires_at"] = task_queue.timestamp(task_queue.now() - timedelta(minutes=1))
    task_queue.write_jsonl(task_queue.TASKS, rows)
    with pytest.raises(RuntimeError, match="expired"):
        task_queue.renew(task["id"], "agent-a", claimed["claim_token"], 10)
    with pytest.raises(RuntimeError, match="expired"):
        task_queue.complete(task["id"], "agent-a", claimed["claim_token"], "skipped", [], None, gate=False)


def test_screen_requires_source_and_obeys_stop_override(monkeypatch, tmp_path) -> None:
    configure(monkeypatch, tmp_path)
    with pytest.raises(RuntimeError, match="require a source"):
        task_queue.enqueue("screen", "Screen", "screen:no-source", None)
    task = task_queue.enqueue("screen", "Screen", "screen:paper", "doi:10.example/paper")
    task_queue.HEALTH.write_text(
        '{"knowledge_readiness":{"stop_bulk_discovery":true}}', encoding="utf-8"
    )
    with pytest.raises(RuntimeError, match="override"):
        task_queue.claim("agent-a", 10, task_id=task["id"])
    claimed = task_queue.claim("agent-a", 10, task_id=task["id"], override_reason="user-requested gap")
    assert claimed["override_reason"] == "user-requested gap"
    released = task_queue.release(task["id"], "agent-a", claimed["claim_token"], "pause")
    assert released["override_reason"] == "user-requested gap"


def test_screen_completion_is_decision_only_and_candidate_must_exist(monkeypatch, tmp_path) -> None:
    configure(monkeypatch, tmp_path)
    monkeypatch.setattr(task_queue, "canonical_digest", lambda: "unchanged")
    task = task_queue.enqueue("screen", "Screen", "screen:paper", "doi:10.example/paper")
    claimed = task_queue.claim("agent-a", 10)
    token = claimed["claim_token"]
    with pytest.raises(RuntimeError, match="only allow outcomes"):
        task_queue.complete(task["id"], "agent-a", token, "created", [], None, gate=False)
    with pytest.raises(RuntimeError, match="existing candidate ID"):
        task_queue.complete(task["id"], "agent-a", token, "candidate", [], None, "candidate-missing", False)
    with pytest.raises(RuntimeError, match="only a screen candidate"):
        task_queue.complete(task["id"], "agent-a", token, "skipped", [], None, "candidate-missing", False)
    candidate = task_queue.add_candidate(
        task["id"], "agent-a", token, "A useful case", "resolve", "Recoverable assignment",
        "https://doi.org/10.1234/case", "doi:10.1234/case", "china-variation",
    )
    completed = task_queue.complete(
        task["id"], "agent-a", token, "candidate", [], "screened", candidate["id"], gate=False
    )
    assert completed["candidate_id"] == candidate["id"]
    assert task_queue.load(task_queue.RUNS)[0]["candidate_id"] == candidate["id"]
    candidates = task_queue.load(task_queue.CANDIDATES)
    assert candidates[0]["status"] == "queued"
    follow_up = task_queue.load(task_queue.TASKS)[1]
    assert follow_up["candidate_id"] == candidate["id"]
    assert follow_up["stage"] == "resolve"
    claimed_follow_up = task_queue.claim("agent-a", 10, task_id=follow_up["id"])
    assert task_queue.load(task_queue.CANDIDATES)[0]["status"] == "in-progress"
    task_queue.complete(
        follow_up["id"], "agent-a", claimed_follow_up["claim_token"], "blocked", [],
        "primary source unavailable", gate=False,
    )
    assert task_queue.load(task_queue.CANDIDATES)[0]["status"] == "blocked"


def test_screen_completion_detects_undeclared_canonical_changes(monkeypatch, tmp_path) -> None:
    configure(monkeypatch, tmp_path)
    digest = {"value": "before"}
    monkeypatch.setattr(task_queue, "canonical_digest", lambda: digest["value"])
    task = task_queue.enqueue("screen", "Screen", "screen:paper", "doi:10.example/paper")
    claimed = task_queue.claim("agent-a", 10)
    digest["value"] = "after"
    with pytest.raises(RuntimeError, match="cannot modify canonical"):
        task_queue.complete(task["id"], "agent-a", claimed["claim_token"], "skipped", [], None, gate=False)


def test_complete_returns_only_after_final_generated_check(monkeypatch, tmp_path) -> None:
    configure(monkeypatch, tmp_path)
    task = task_queue.enqueue("screen", "Screen", "screen:paper", "doi:10.example/paper")
    claimed = task_queue.claim("agent-a", 10)
    calls: list[str] = []
    monkeypatch.setattr(task_queue, "run_gate", lambda: calls.append("gate"))

    def final_check() -> None:
        assert task_queue.load(task_queue.TASKS)[0]["status"] == "completed"
        calls.append("fresh")

    monkeypatch.setattr(task_queue, "run_generated_check", final_check)
    task_queue.complete(task["id"], "agent-a", claimed["claim_token"], "skipped", [], None)
    assert calls == ["gate", "fresh"]


def test_touched_record_gate_requires_locators_and_rejects_search_snippets() -> None:
    class Canonical:
        id = "case-x"
        body = "Clean body"
        data = {
            "status": "extracted",
            "design": {"claim_type": "causal"},
            "evidence": [{
                "id": "E1", "verification_status": "verified", "access_level": "full-text",
                "supports": ["assignment.rule"],
            }],
        }

    with pytest.raises(RuntimeError, match="requires access_level and locator"):
        task_queue.validate_touched_record(Canonical())
    Canonical.data["evidence"][0]["locator"] = "p. 3"
    Canonical.body = "Claim [web search]"
    with pytest.raises(RuntimeError, match="search snippets"):
        task_queue.validate_touched_record(Canonical())


def test_touched_record_gate_requires_precise_support_paths() -> None:
    class Canonical:
        id = "case-x"
        body = "Clean body"
        data = {
            "status": "grounded",
            "design": {"claim_type": "causal"},
            "evidence": [{
                "id": "E1", "verification_status": "verified", "access_level": "official-document",
                "locator": "Article 3", "supports": ["assignment"],
            }],
        }

    with pytest.raises(RuntimeError, match="precise field support paths"):
        task_queue.validate_touched_record(Canonical())
    Canonical.data["evidence"][0]["supports"] = ["assignment.rule"]
    task_queue.validate_touched_record(Canonical())


def write_canonical(path, *, record_id: str, task_id: str, status: str = "grounded") -> None:
    path.write_text(
        "\n".join((
            "---", f"id: {record_id}", f"status: {status}", "provenance:", f"  task_id: {task_id}",
            "design:", "  claim_type: causal", "evidence:", "  - id: E1", "    verification_status: verified",
            "    access_level: official-document", "    locator: Article 3", "    supports: [assignment.rule]",
            "---", "Clean body",
        )),
        encoding="utf-8",
    )


def test_new_canonical_admission_blocks_half_products_and_protects_existing_files(monkeypatch, tmp_path) -> None:
    configure(monkeypatch, tmp_path)
    variations = tmp_path / "variations"
    variations.mkdir()
    monkeypatch.setattr(task_queue, "ROOT", tmp_path)

    task = task_queue.enqueue("resolve", "Resolve a candidate", "candidate:x", None)
    claimed = task_queue.claim("agent-a", 10, task_id=task["id"])
    assert "task_brief" in claimed
    assert "task_brief" not in task_queue.load(task_queue.TASKS)[0]
    write_canonical(variations / "new-case.md", record_id="new-case", task_id=task["id"], status="extracted")
    with pytest.raises(RuntimeError, match="must be grounded or design-documented"):
        task_queue.complete(
            task["id"], "agent-a", claimed["claim_token"], "updated", ["new-case"], None, gate=False,
        )

    (variations / "new-case.md").unlink()
    task_queue.release(task["id"], "agent-a", claimed["claim_token"], "retry grounded")
    claimed = task_queue.claim("agent-a", 10, task_id=task["id"])
    write_canonical(variations / "new-case.md", record_id="new-case", task_id=task["id"], status="grounded")
    completed = task_queue.complete(
        task["id"], "agent-a", claimed["claim_token"], "created", ["new-case"], None, gate=False,
    )
    assert completed["status"] == "completed"

    second = task_queue.enqueue("audit", "Protect existing", "audit:x", None)
    claimed_second = task_queue.claim("agent-a", 10, task_id=second["id"])
    (variations / "new-case.md").unlink()
    with pytest.raises(RuntimeError, match="restore canonical file set"):
        task_queue.release(
            second["id"], "agent-a", claimed_second["claim_token"], "cannot normalize deletion",
        )
    with pytest.raises(RuntimeError, match="cannot be deleted"):
        task_queue.complete(
            second["id"], "agent-a", claimed_second["claim_token"], "skipped", [], None, gate=False,
        )


def test_new_contested_record_does_not_receive_existing_record_safety_exemption(monkeypatch, tmp_path) -> None:
    configure(monkeypatch, tmp_path)
    variations = tmp_path / "variations"
    variations.mkdir()
    monkeypatch.setattr(task_queue, "ROOT", tmp_path)
    task = task_queue.enqueue("resolve", "Resolve a disputed identity", "candidate:contested", None)
    claimed = task_queue.claim("agent-a", 10, task_id=task["id"])
    path = variations / "contested-case.md"
    write_canonical(path, record_id="contested-case", task_id=task["id"], status="contested")
    text = path.read_text(encoding="utf-8").replace("supports: [assignment.rule]", "supports: [assignment]")
    path.write_text(text, encoding="utf-8")
    with pytest.raises(RuntimeError, match="precise field support paths"):
        task_queue.complete(
            task["id"], "agent-a", claimed["claim_token"], "contested", ["contested-case"], None, gate=False,
        )


def test_stale_empty_lock_is_recovered(monkeypatch, tmp_path) -> None:
    monkeypatch.setattr(econ_variation_lib, "STATE_DIR", tmp_path)
    lock = tmp_path / ".broken.lock"
    lock.write_text("", encoding="utf-8")
    old = time.time() - 10
    os.utime(lock, (old, old))
    with econ_variation_lib.workspace_lock("broken", stale_seconds=1):
        assert lock.exists() and lock.stat().st_size > 0
    assert not lock.exists()
