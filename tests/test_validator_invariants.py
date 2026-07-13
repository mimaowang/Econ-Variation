from __future__ import annotations

import hashlib
import json
from types import SimpleNamespace

import validate
from validate import Audit, evidence_url_doi, has_placeholder_metadata, normalize_doi, validate_provenance


def test_placeholder_and_doi_normalization_guards() -> None:
    assert has_placeholder_metadata("10.1016/j.jclepro.2025.XXXXXX")
    assert has_placeholder_metadata("https://example.org/paper")
    assert has_placeholder_metadata("needs-verification")
    assert not has_placeholder_metadata("10.3389/fpubh.2025.1688719")
    assert normalize_doi("https://doi.org/10.3389/FPUBH.2025.1688719/") == (
        "10.3389/fpubh.2025.1688719"
    )
    assert evidence_url_doi("https://doi.org/10.3389/fpubh.2025.1688719") == (
        "10.3389/fpubh.2025.1688719"
    )
    assert evidence_url_doi("https://publisher.example/article") is None


def test_legacy_file_hash_detects_untracked_content_change(tmp_path, monkeypatch) -> None:
    state = tmp_path / "state"
    state.mkdir()
    (state / "tasks.jsonl").write_text("", encoding="utf-8")
    (state / "runs.jsonl").write_text("", encoding="utf-8")
    record_path = tmp_path / "legacy-case.md"
    record_path.write_text("changed content", encoding="utf-8")
    record_id = "legacy-case"
    ids_digest = hashlib.sha256(record_id.encode()).hexdigest()
    baseline = {
        "record_count": 1,
        "record_ids_sha256": ids_digest,
        "record_ids": [record_id],
        "record_sha256": {record_id: "0" * 64},
    }
    (state / "legacy_baseline.json").write_text(json.dumps(baseline), encoding="utf-8")
    monkeypatch.setattr(validate, "STATE_DIR", state)
    record = SimpleNamespace(
        id=record_id,
        path=record_path,
        data={"provenance": {"task_id": "legacy-untracked"}},
    )
    audit = Audit()
    validate_provenance(audit, [record])
    assert any("legacy-untracked content changed" in error for error in audit.errors)


def test_resolved_deprecated_doi_duplicates_are_not_reported() -> None:
    audit, _ = validate.run(write_health=False)
    assert not any("DOI" in warning for warning in audit.warnings)
