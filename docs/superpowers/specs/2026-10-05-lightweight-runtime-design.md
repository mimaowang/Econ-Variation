# Lightweight operational distribution

Approved purpose: ordinary users should receive the knowledge and tools needed to match ideas and continue collection, not developer tests or benchmarks. One source repository remains authoritative; export its tracked operational directories into a ZIP or a fresh user folder. Keep all canonical knowledge, source notes and durable state. Exclude tests, benchmarks, CI configuration, development dependencies and historical design documents. No existing knowledge is deleted or moved.

`python scripts/setup.py` configures an extracted runtime folder with an isolated environment and the two runtime dependencies, then runs doctor. From a Git checkout, `--destination` first copies only operational files into a new or empty folder. It never replaces an existing populated destination. No model, API credentials or harness is installed.

Task completion retains record validation, router generation, generated-state checking and all existing admission/provenance rules. GitHub CI retains the full regression suite, routing benchmarks and lint on both operating systems and Python versions. Only successful CI produces a downloadable runtime artifact. Developer instructions remain available in the full repository.

Verification targets the actual split: runtime membership excludes developer/private scratch files, configuration installs only runtime requirements, and a copied runtime can complete a task without pytest or ruff. Existing regression tests detect unintended lifecycle or matching changes; no canonical data changes are intended.
