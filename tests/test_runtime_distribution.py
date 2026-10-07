from __future__ import annotations

import subprocess
import sys

import pytest

import runtime_bundle
import setup
import task_queue


def test_runtime_membership_preserves_knowledge_and_excludes_development(monkeypatch, tmp_path):
    files = [
        "AGENTS.md", "requirements.txt", "scripts/setup.py", "scripts/task_queue.py",
        "variations/case.md", "sources/evidence.md", "state/tasks.jsonl", "schema/topics.yaml",
        "dist/health.json", "guides/operations.md", "assets/econ-variation-hero.png",
        "tests/test_queue.py",
        "benchmarks/routing_cases.yaml", "requirements-dev.txt", "pyproject.toml",
        ".github/workflows/validate.yml", "docs/superpowers/specs/design.md", "evbase2/private.txt",
    ]
    monkeypatch.setattr(runtime_bundle.subprocess, "run", lambda *a, **k: subprocess.CompletedProcess(
        a, 0, stdout="\0".join(files).encode("utf-8"),
    ))
    paths = runtime_bundle.runtime_paths(tmp_path)
    assert paths == sorted(files[:11])
    for name in files:
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(name, encoding="utf-8")
    destination = tmp_path / "runtime"
    runtime_bundle.copy_runtime(destination, tmp_path)
    assert sorted(p.relative_to(destination).as_posix() for p in destination.rglob("*") if p.is_file()) == paths
    with pytest.raises(ValueError, match="not overwritten"):
        runtime_bundle.copy_runtime(destination, tmp_path)
    assert (destination / "variations/case.md").read_text() == "variations/case.md"


def test_knowledge_gate_does_not_require_developer_tools(monkeypatch):
    calls = []
    monkeypatch.setattr(task_queue.subprocess, "run", lambda command, **kwargs: (
        calls.append(command) or subprocess.CompletedProcess(command, 0)
    ))
    task_queue.run_gate()
    assert calls == [
        [sys.executable, "scripts/validate.py", "--write-health"],
        [sys.executable, "scripts/build_router.py"],
        [sys.executable, "scripts/check_generated.py"],
    ]


def test_setup_uses_runtime_requirements_and_existing_environment(monkeypatch, tmp_path):
    python = tmp_path / ".venv" / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
    python.parent.mkdir(parents=True)
    python.touch()
    calls = []
    monkeypatch.setattr(setup.subprocess, "run", lambda command, **kwargs: calls.append(command))
    monkeypatch.setattr(setup.venv, "EnvBuilder", lambda **kwargs: pytest.fail("Existing environment was recreated"))
    setup.configure(tmp_path)
    assert calls == [
        [str(python), "-m", "pip", "install", "-r", str(tmp_path / "requirements.txt")],
        [str(python), "scripts/doctor.py"],
    ]
