<h1 align="center">Econ-Variation</h1>

<p align="center"><strong>Econ-Variation helps researchers find policy changes, reforms, and events they can use to study cause and effect in China.</strong></p>

Econ-Variation is a knowledge base for researchers and AI coding agents such as Claude Code, Codex, and Kimi Code. Tell the agent your research question and what data you have; it uses Econ-Variation to find relevant changes, explain how they could support a study, identify the data still needed, and flag risks that could make the result unreliable.

---

## Quick start

Use Econ-Variation in two ways: **match a research idea against existing knowledge**, or ask an agent to **collect and verify new knowledge**. Both start by reading `AGENTS.md` and running the repository doctor.

Python 3.10 or newer is required. From the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python scripts/doctor.py
```

On macOS or Linux, activate with `source .venv/bin/activate`. `doctor.py` is the short-context entry point: it reports validity, generated-file freshness, the active lease, the next bounded tasks, and one safe next action without modifying the repository.

## Match a research idea

Ask the agent to translate the idea and available data into a small structured query, then use deterministic recall and compatibility checks before reading canonical records.

> I want to study whether local environmental regulation changes firm innovation in China. Read `AGENTS.md`, run the repository doctor, search the China-variation lane, check whether my firm panel can join the treatment and cover enough pre/post periods, then open only the best canonical records. Explain fit, treatment, comparison, data needs, assumptions, threats, and any knowledge gap in Chinese.

Focused recall is compact and excludes immature leads by default:

```powershell
python scripts/search.py --role china-variation --domain environment --text firm --text patent --limit 3
```

Stable topics accept canonical names or Chinese/English aliases, while detailed record domains remain available:

```powershell
python scripts/search.py --role china-variation --topic 环境 --text 中国企业创新 --limit 3
```

For deterministic data-fit, pass YAML or JSON to `match.py`:

```yaml
filters:
  roles: [china-variation]
  domains: [environment]
  text: [firm, patent]
limit: 3
data:
  observation_unit: firm-year
  geography: prefecture
  time_start: 2005
  time_end: 2018
  frequency: annual
  identifiers: [prefecture code, year]
  derivable_identifiers: [province code]
  available_fields: [outcome, patent count, firm id, prefecture code, year]
comparison:
  untreated_available: true
```

```powershell
python scripts/match.py --query query.yaml
```

The matcher returns `compatible`, `conditional`, `incompatible`, `method-only`, or `gap` with dimension-level reasons. It checks reproducible constraints such as knowledge lane, maturity, time coverage, pre/post periods, frequency, fields, and join identifiers. Free-text population, geography, and unit comparisons remain explicit manual-review conditions. The matcher never claims that parallel trends, exclusion restrictions, or causal mechanisms are valid.

Static `recommendation_eligibility` and runtime compatibility are different concepts. `lead-only`, `method-lead`, contested, and deprecated records cannot become recommendations merely because keywords match. Use `--include-leads` only to inspect audit leads. Always open the cited canonical file before making factual claims.

## Collect knowledge

Collection is a staged decision process, not a request to write a large policy card immediately.

> Read `AGENTS.md`, run the doctor, and screen one specified high-quality source on Chinese environmental regulation. First decide whether it contains a recoverable China variation, a China-facing global change, a genuinely transferable method, or nothing in scope. A screen task may only record candidate, skip, or blocked. If retained, create a separate bounded follow-up task for identity resolution and evidence-based extraction. Report in Chinese.

Create one source-specific screen task and claim it. The claim response contains a fencing token required by later lifecycle commands:

```powershell
python scripts/task_queue.py enqueue --stage screen --goal "Triage one CEPI paper" --idempotency-key "doi:<doi>" --source "https://doi.org/<doi>"
python scripts/task_queue.py claim --id <task-id> --agent <agent-name> --lease-minutes 60
```

If the source passes triage, add a durable candidate and finish the screen decision:

```powershell
python scripts/task_queue.py candidate-add --task-id <task-id> --agent <agent-name> --claim-token <token> --name "Candidate variation" --next-stage resolve --reason "Recoverable assignment requires primary-source resolution" --source "https://doi.org/<doi>" --source-fingerprint "doi:<doi>" --knowledge-role china-variation
python scripts/task_queue.py complete --id <task-id> --agent <agent-name> --claim-token <token> --outcome candidate --candidate <candidate-id> --note "Screened one source; retained for resolution."
```

Completion automatically creates and links the bounded follow-up task. Candidate status then follows that task through claim, release, retry, and completion, so resolved candidates no longer remain indefinitely pending.

Screen tasks cannot modify canonical records. Only later `discover`, `resolve`, `ground`, `audit`, or `consolidate` work may write records, and touched records must satisfy the current evidence standard. The shared worktree permits one mutating claim at a time. Expired or mismatched claim tokens cannot complete work. When health advises stopping bulk discovery, a user-directed or coverage-gap exception must be claimed with a recorded `--override-reason`.

---

## Scope and limits

Econ-Variation does **not** label a policy as intrinsically exogenous. Exogeneity and usefulness are query-specific: they depend on the outcome, population, time window, assignment process, exposure measure, comparison group, and identifying assumptions.

The repository distinguishes three knowledge lanes:

- `china-variation`: the change occurs in China or assigns exposure to Chinese units;
- `global-china-variation`: a global or foreign-origin change directly changes exposure faced by Chinese units;
- `transferable-method`: a non-China study contributes a reusable identification construction, not a Chinese shock.

Publication prestige is a discovery prior, not evidence that a design is valid. Collection prioritizes economics Top Five, UTD24, FT50, ABS 3/4, strong SSCI Q1, and respected field journals, then follows papers to primary institutional sources where appropriate.

## Project status

Econ-Variation is a repository-local tool and knowledge base, not a hosted service or PyPI package. The canonical collection currently contains both managed records and a frozen legacy lead backlog. Legacy leads remain available for audit but do not block new targeted work and are not recommended by default. Any legacy record that is edited must enter the current task and evidence workflow.

## Knowledge model

One file in `variations/` represents one variation case: one instrument, one implementation regime, and one primary assignment mechanism. It separates:

- institutional facts and verified timeline;
- assignment, exposure, treatment, and comparison;
- design affordances, estimand, assumptions, and diagnostics;
- identification threats and spillovers;
- empirical requirements and treatment join keys;
- paper-specific design applications;
- verified facts, reported claims, and analytical inferences.

The default `empirical_requirements` contract supports simple cases. Optional `design_profiles` describe distinct alternatives—such as province-year, firm-year, or plant-week designs—so the matcher selects one coherent requirement set instead of combining unrelated fields.

Canonical statuses are `extracted`, `grounded`, `design-documented`, `contested`, and `deprecated`. Status measures knowledge maturity, not universal causal validity.

## Repository map

| Path | Purpose |
|---|---|
| `variations/` | Canonical records and writing template |
| `guides/operations.md` | Authoritative maintenance and reasoning workflow |
| `sources/` | Journal scope and discovery guidance |
| `state/` | Durable tasks, candidates, runs, and frozen legacy manifest |
| `schema/variation.schema.json` | Machine authority for canonical record structure |
| `schema/topics.yaml` | Stable bilingual topic vocabulary and aliases for recall |
| `scripts/doctor.py` | Read-only cold-start and operational readiness check |
| `scripts/search.py` | Compact, maturity-gated recall |
| `scripts/match.py` | Deterministic idea/data compatibility gate |
| `scripts/task_queue.py` | Bounded task, lease, candidate, and recovery lifecycle |
| `benchmarks/routing_cases.yaml` | Executable product behavior cases |
| `dist/router.json` | Generated compact retrieval index |
| `dist/health.json` | Generated canonical knowledge-quality snapshot |

## Quality gate

```powershell
python scripts/validate.py --write-health
python scripts/build_router.py
python scripts/check_generated.py
python -m pytest
python -m ruff check .
```

Validation success means the repository is structurally and operationally consistent; it does not mean every lead is recommendation-ready. Formal repository content is English except official Chinese names and titles needed for evidence and retrieval. Agents report progress, blockers, and necessary questions to the user in Chinese unless asked otherwise.

## Relationship to Econ-Data-Foundry

Econ-Variation and Econ-Data-Foundry remain independent. Econ-Variation states what a variation requires; the data repository states what a dataset supplies. An agent compares population, observation unit, geography, time, frequency, fields, access conditions, and join identifiers at runtime. Neither repository imports the other or stores reciprocal dataset IDs.

## License and contribution

Code and original repository content are available under Apache-2.0; linked papers, government documents, and third-party data retain their own rights. Do not commit copyrighted papers, restricted datasets, credentials, personal data, or sensitive URLs. See `CONTRIBUTING.md`, `SECURITY.md`, and `LICENSE`.
