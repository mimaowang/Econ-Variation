# Contributing

Contributions should improve future research decisions, not merely add policy names. Start with `AGENTS.md`; if the project's reasoning is unfamiliar, read `guides/mental-model.md`. For maintenance, open only the relevant part of `guides/operations.md`, and use `variations/template.md` while writing a canonical record. Resolve identity, scope evidence to claims, preserve uncertainty, make one focused change, and run the release gate.

Econ-Variation currently provides repository-local tools rather than an installable Python package. From the repository root, create a Python 3.10 or newer virtual environment and install the development dependencies with:

```text
python -m pip install -r requirements-dev.txt
```

Run scripts from the repository checkout. Commit regenerated `dist/` artifacts when canonical records or durable state change, and do not hand-edit generated files.

Do not commit credentials, restricted source files, copyrighted papers, or personal data. Link to publicly reviewable evidence where possible.

## Verification and release

The release gate checks record structure, generated views, task behavior, and retrieval/matching behavior:

```text
python scripts/validate.py --write-health
python scripts/build_router.py
python scripts/check_generated.py
python -m pytest
python -m ruff check .
```

The normal `task_queue.py complete` command runs this gate for a claimed task. A failure is a reason to inspect the affected behavior, not to weaken a record's evidence or repeatedly run unrelated checks. Knowledge upgrades can legitimately change a live-record benchmark: update its expected decision with the reason, while retaining tests that exclude unresolved knowledge. Test ranking mechanics on fixed inputs rather than freezing the top results of an expanding collection.

For an onboarding or recommendation change, also walk through a few existing prompts in `benchmarks/routing_cases.yaml`: `environmental-firm-innovation` should explain the geographic crosswalk and pilot nesting; `no-pre-period` should reject the specified first-wave comparison if pre-treatment years are absent; `hukou-worker-wages` should preserve the disputed assignment boundary. Use the case's query and `must_identify` notes when assessing the answer. These are research judgments, not word-for-word response templates. The automated cases test agent-normalized inputs; a claim about a particular model's cold-start performance requires a separate actual session with that model.

Before publishing, review `git status --short` and the intended diff. Include new canonical records, their supporting guides and source notes, durable task provenance, and regenerated `dist/` together: a local file that remains untracked is absent from a GitHub clone. Local `.tmp_*` retrieval files, `.tmptest/`, and `.venv/` are ignored without being deleted. Review other untracked material by purpose; a blanket ignore of `sources/`, `state/`, or `variations/` would hide product knowledge.

Use the dated readiness counts from `dist/health.json` in release descriptions. A conditional candidate still requires the stated evidence or data checks; total records are not a count of ready-to-estimate causal designs. Publishing a repository update does not require clearing every historical lead, changing its maturity, or deleting it.
