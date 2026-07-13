# Contributing

Contributions should improve future research decisions, not merely add policy names. Read `AGENTS.md`, `guides/operations.md`, and `variations/template.md`. Resolve identity, scope evidence to claims, preserve uncertainty, make one focused change, and run the release gate.

Econ-Variation currently provides repository-local tools rather than an installable Python package. From the repository root, create a Python 3.10 or newer virtual environment and install the development dependencies with:

```text
python -m pip install -r requirements-dev.txt
```

Run scripts from the repository checkout. Commit regenerated `dist/` artifacts when canonical records or durable state change, and do not hand-edit generated files.

Do not commit credentials, restricted source files, copyrighted papers, or personal data. Link to publicly reviewable evidence where possible.
