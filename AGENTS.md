# Econ-Variation Agent Operating Notes

Econ-Variation succeeds when recorded knowledge helps a researcher decide whether a variation fits an idea and explain the institution, assignment, treatment, comparison, data needs, feasible design, assumptions, and threats. Never call a policy intrinsically exogenous.

On first use, read `guides/mental-model.md` to understand why the repository is organized this way. It follows one research decision from institutional change to assignment, data fit, evidence limits, and a query-specific conclusion. Treat its examples as reasoning patterns, not wording templates. After context compaction, recover the current task from the repository and return to the relevant explanation when a judgment is unclear; there is no need to reload every guide or record.

## Start by intent

Run `python scripts/doctor.py` first. If it reports invalid or stale generated state, follow its safe action before writing.

The lightweight runtime has all knowledge, sources, task state and operational checks, but intentionally has no tests or benchmarks. Configure it with `python scripts/setup.py` and use its `.venv` Python. Daily completion checks knowledge and generated state; full code regressions, benchmarks and style checks run in GitHub CI. Do not install developer tools merely to collect knowledge. Code changes belong in the full source checkout, where `CONTRIBUTING.md` explains verification.

For **idea matching**, do not read the task history or full operations guide. Use `scripts/search.py` for compact recall, `scripts/match.py` for deterministic data-fit, and open only the best canonical records. Keep China shocks, China-facing global variation, and overseas method inspiration in separate lanes. Report `compatible`, `conditional`, `incompatible`, `method-only`, or `gap`; explain treatment, comparison, join keys, missing data, assumptions, and threats. A lead is never promoted by keyword similarity.

Carry the user's outcome into the match query's `intent.outcome`, using the record's vocabulary without changing the question. Optional `intent.design` describes the intended design. If a case has distinct applications, read their labels and `when_to_use`; `design_profile_ids: {variation-id: profile-id}` locks the intended application. A data-fit exploration is not a recommendation: do not replace a missing patent outcome with an available GDP outcome. Intent vocabulary matches still need institutional and substantive judgment.

For **knowledge maintenance**, read `guides/mental-model.md` once, then use only the relevant sections of `guides/operations.md`, the task brief, and the target source/record. Use one bounded task claimed through `scripts/task_queue.py`. A conversation is not provenance. The repository uses one mutating claim in the shared worktree; preserve the returned claim token and renew before expiry.

The workflow is shared across agents; it does not require a particular model or a scheduler. If the user chooses DeepSeek Harness, `guides/deepseek-harness.md` offers a runtime-specific cue for recognizing evidence saturation. `guides/kimi-k3-maintainer-handoff.md` preserves an August 2026 owner-specific supervision arrangement and applies only if the user explicitly resumes that arrangement. Opening the repository in Kimi Code does not activate it. Current user instructions and the live task determine who does the work.

## Stage discipline

Triage one source per `screen` task. Screen may only produce `candidate`, `skipped`, or `blocked`; it cannot change canonical files. A retained source gets a durable candidate and a separate follow-up task. Resolve variation identity before extraction: one canonical case contains one instrument, implementation regime, and primary assignment mechanism.

Candidate follow-up tasks are created automatically when a retained screen task completes. Claim, release, retry, failure, and completion keep the linked candidate status synchronized. Prefer queued China-facing resolve/ground work over overseas method screening unless the user names a method or a demonstrated coverage gap justifies it.

Candidates are the staging layer; `variations/` is the serving layer. Keep unresolved identity or core evidence in the candidate lifecycle. A new active canonical record must be grounded or design-documented at admission, while a genuinely disputed case may enter as contested. Existing extracted and legacy records remain available under their maturity gates but are not the publication standard.

Every paper receives exactly one role: `china-variation`, `global-china-variation`, `transferable-method`, or skip. Never retain an overseas policy merely because its paper is prestigious, and never present a transferable method as a Chinese shock.

Canonical records live only in `variations/`. Touched records must use precise evidence field paths; verified or reported evidence needs the inspected access level and locator. Search snippets and unsupported web-search prose are not evidence. Separate verified facts, source-reported claims, and analytical inference. Preserve uncertainty and blockers; never raise maturity to make a result look complete.

Use stable topics from `schema/topics.yaml` for recall while preserving detailed record domains. When one variation supports materially different units, frequencies, or field requirements, add a small number of `design_profiles`; do not combine every possible design's fields into one mandatory list.

For the owner's ongoing collection, use `sources/fieldtop-china-regional-urban-coverage.md` as the live campaign map, including its dated mainland-China, non-agricultural focus. The earlier `sources/top5-china-regional-urban-coverage.md` is a closed historical audit, not a completion certificate for the live campaign. Campaign priorities guide what to collect next; they do not redefine existing records or authorize deleting knowledge outside the current focus. Other users may name their own research question or collection task within the project's China-focused knowledge boundary.

Finish through the task lifecycle and quality gate. Generated files are outputs. Do not edit frozen `legacy-untracked` records without assigning a real task provenance. Do not store credentials, restricted documents, copyrighted papers, personal data, or sensitive query URLs.

Repository content is English except official Chinese names and titles required for evidence or retrieval. Respond in the user's language; Chinese is the current owner's preference.
