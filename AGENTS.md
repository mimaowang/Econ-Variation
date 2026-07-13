# EconVariation Agent Operating Notes

EconVariation succeeds when recorded knowledge helps a researcher decide whether a variation fits an idea and explain the institution, assignment, treatment, comparison, data needs, feasible design, assumptions, and threats. Never call a policy intrinsically exogenous.

## Start by intent

Run `python scripts/doctor.py` first. If it reports invalid or stale generated state, follow its safe action before writing.

For **idea matching**, do not read the task history or full operations guide. Use `scripts/search.py` for compact recall, `scripts/match.py` for deterministic data-fit, and open only the best canonical records. Keep China shocks, China-facing global variation, and overseas method inspiration in separate lanes. Report `compatible`, `conditional`, `incompatible`, `method-only`, or `gap`; explain treatment, comparison, join keys, missing data, assumptions, and threats. A lead is never promoted by keyword similarity.

For **knowledge maintenance**, read the relevant sections of `guides/operations.md`, inspect the target source/record, and use one bounded task claimed through `scripts/task_queue.py`. A conversation is not provenance. The repository uses one mutating claim in the shared worktree; preserve the returned claim token and renew before expiry.

## Stage discipline

Triage one source per `screen` task. Screen may only produce `candidate`, `skipped`, or `blocked`; it cannot change canonical files. A retained source gets a durable candidate and a separate follow-up task. Resolve variation identity before extraction: one canonical case contains one instrument, implementation regime, and primary assignment mechanism.

Every paper receives exactly one role: `china-variation`, `global-china-variation`, `transferable-method`, or skip. Never retain an overseas policy merely because its paper is prestigious, and never present a transferable method as a Chinese shock.

Canonical records live only in `variations/`. Touched records must use precise evidence field paths; verified or reported evidence needs the inspected access level and locator. Search snippets and unsupported web-search prose are not evidence. Separate verified facts, source-reported claims, and analytical inference. Preserve uncertainty and blockers; never raise maturity to make a result look complete.

Finish through the task lifecycle and quality gate. Generated files are outputs. Do not edit frozen `legacy-untracked` records without assigning a real task provenance. Do not store credentials, restricted documents, copyrighted papers, personal data, or sensitive query URLs.

Repository content is English except official Chinese names and titles required for evidence or retrieval. Report progress, problems, and necessary questions to the user in Chinese unless requested otherwise.
