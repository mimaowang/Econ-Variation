# Econ-Variation Operations Guide

## Invariant

From the recorded knowledge alone, an agent must be able to determine whether a variation fits a research idea and explain: what changed and why; who was exposed and when; what comparison the change creates; how treatment can be measured; which designs are plausible; what data are required; and which threats limit causal interpretation.

A smaller collection of decision-sufficient records is better than a large policy list. Health separates the frozen legacy backlog from the managed active pipeline. Bulk-discovery advice is based on active, managed, China-facing work rather than allowing historical leads to freeze the project forever. A user-directed topic or demonstrated coverage gap may override the advice only with an explicit reason recorded in the task lifecycle.

## Knowledge boundary

A canonical record represents one variation case: one policy or event instrument under one implementation regime with one primary assignment mechanism. A policy family is only a parent or related entity, never a directly recommended record. A policy name alone is not a record. Split national authorization, local implementation, pilot assignment, later expansion, or multiple assignment mechanisms when they imply different treatment rules.

Keep three layers distinct:

1. **Institutional reality**: what existed before, what changed, why it changed, and how it was implemented.
2. **Assignment and exposure**: which units were affected, when, with what eligibility, intensity, exemptions, compliance, and spillovers.
3. **Design applications**: how particular papers encoded and used the variation for particular outcomes and populations.

Exogeneity is never a permanent property of the record. A variation may be useful for one outcome and endogenous for another.

## China-first collection boundary

Every paper must pass scope triage before full extraction. Assign exactly one `scope.knowledge_role`:

| Role | Retain when | Collection depth |
|---|---|---|
| `china-variation` | The change occurs in China or assigns exposure to Chinese units. | Full institutional, assignment, design, evidence, and data grounding. |
| `global-china-variation` | A global or foreign-origin change directly changes exposure faced by Chinese units. | Full record centered on the China-facing exposure, not a generic global history. |
| `transferable-method` | A non-China paper contributes a reusable IV, threshold, shift-share, randomization, exposure, or comparison construction that could inform China research. | Method-focused: construction, first stage or contrast, identifying assumptions, diagnostics, China use cases, data needs, and transfer limits. |

If none applies, skip the paper. A prestigious publication is not itself a retention reason. Do not create a full US, UK, Indian, or other foreign policy record merely because the design is credible. For a transferable method, foreign institutional details are included only when necessary to understand assignment or validity.

Screen in this order:

1. Does the policy/event occur in China or assign treatment to Chinese units? Use `china-variation`.
2. Does a global event directly expose China with observable China-specific variation? Use `global-china-variation`.
3. Does an overseas study offer a genuinely portable identification construction? Use `transferable-method` and explain the China transfer.
4. Otherwise record `skipped`; do not publish a canonical record.

## Cold start

1. Run `python scripts/doctor.py`; follow its single safe action if state is invalid, stale, or leased.
2. For idea matching, use focused search and structured matching, then open only the best canonical records. Do not load task history.
3. For maintenance, read only the relevant sections of this guide and the target record/source. Enqueue or select one bounded task and claim it before writing.
4. Preserve the returned claim token, renew before expiry, and finish the task before another mutating claim begins.

## Collection loop

```text
high-quality paper or primary source
  -> China relevance and knowledge-role triage
  -> candidate variation
  -> identity resolution and duplicate check
  -> institutional background verification
  -> timeline, assignment, and exposure reconstruction
  -> design applications and threat assessment
  -> data requirements
  -> create / update / consolidate / candidate / contest / skip / block
  -> validation, router rebuild, and task transition
```

Tasks use stages `screen`, `discover`, `resolve`, `ground`, `audit`, and `consolidate`. One `screen` task evaluates one paper or clearly identified source and records only `candidate`, `skipped`, or `blocked`; it cannot modify canonical records. A retained source is written to the candidate ledger with a source fingerprint and receives a separate post-screen task. Only sources assigned a supported knowledge role proceed to deep extraction. Discovery should not dominate when managed evidence, identity, or duplication debt is high.

Completing a retained screen automatically queues its post-screen task. The candidate then moves through `queued`, `in-progress`, and a terminal state (`resolved`, `contested`, `skipped`, or `blocked`) with the linked task. Historical candidates may be reconciled to an existing canonical record without deleting their original source, reason, or screening provenance. Default queue priority favors bounded China-facing post-screen work over overseas method screening; an explicit task priority or user-directed scope may override that order.

Every canonical record names its task in `provenance.task_id`. The fixed `legacy-untracked` baseline includes per-file hashes: an untouched legacy lead may remain frozen, but any edit requires a real claimed task and current quality standards. For new or audited records, set the claimed task ID before validation. Completion rejects undeclared provenance, expired or mismatched claim tokens, imprecise evidence paths, missing evidence locators, and search-snippet claims. The shared worktree supports one mutating claim at a time.

## Evidence discipline

Prefer sources in this order:

1. laws, regulations, official notices, government gazettes, and implementation documents;
2. paper institutional background, empirical strategy, and data sections;
3. appendices and replication materials;
4. official statistics, archives, and responsible-agency documentation;
5. high-quality scholarship focused on the institution;
6. trusted repositories and institutional metadata.

News and search snippets are leads, not final support. One source never supports an entire record by default. Each evidence item declares precise `supports` paths plus the access level and page, section, table, legal provision, or dataset location actually inspected. A DOI or accessible page is not by itself claim verification.

Use three epistemic categories:

- **verified fact**: supported by suitable evidence;
- **reported claim**: attributed to a paper or source but not independently established;
- **analytical inference**: the agent's reasoned implication, explicitly labeled.

Institutional prose cites evidence IDs such as `[E1]`, labels reported claims as `[E2, reported claim]`, and labels inference as `[analytical inference]`.

## Record actions and states

- `extracted`: a paper or source has been structured, but facts, admissibility, or design details still require audit; never treat it as recommendation-ready;
- `grounded`: institutional identity and core timing have suitable primary support, and the research application is traceable;
- `design-documented`: assignment, design opportunities, threats, and data requirements support direct idea matching;
- `contested`: important evidence conflicts or the common design interpretation is materially disputed;
- `deprecated`: retained only to redirect to a replacement.

Allowed task outcomes are `created`, `updated`, `consolidated`, `candidate`, `contested`, `skipped`, and `blocked`. Skipping and blocking are legitimate; record count is not a quality metric.

## Institutional background standard

Write connected prose explaining the pre-reform institution, pressure or objective behind the change, legal or administrative action, implementation structure, affected actors, local discretion, phase-in and exceptions, and relationship to concurrent or successor reforms. Preserve only details that improve assignment, threat assessment, mechanism reasoning, or study interpretation.

## Design standard

Do not write only "DID" or "RDD." Explain the assignment-generating feature: staggered rollout, threshold, boundary, cohort rule, intensity, event timing, or other comparison. Record the required assumptions and plausible falsification opportunities. Threats must distinguish documented problems from unresolved concerns.

The structured `design` block is core knowledge, not an appendix. It records the primary strategy, estimand, treatment variable, comparison logic, and estimation notes in addition to design affordances. For IV and IV-like methods, the record must make the endogenous variable, instrument or assignment, first stage, exclusion restriction, and diagnostics recoverable from `design`, `design_applications`, or `method_transfer`.

For overseas work, `method_transfer` answers: what is portable; how the variable or comparison is constructed; what produces the first stage; why the exclusion or identifying restriction might hold; which diagnostics are decisive; what analogous Chinese setting could exist; what China data are needed; and when transfer would be invalid.

## Data requirements and dual-repository use

Econ-Variation states a versioned `empirical_requirements` contract rather than duplicating dataset profiles: observation unit, population, geography, time coverage, minimum frequency, pre/post periods, required fields, treatment source, and join keys. Compatibility is evaluated at runtime; Econ-Variation stores no reciprocal dataset IDs.

`empirical_requirements` remains the default contract. When a variation supports genuinely different empirical designs, optional `design_profiles` provide alternative, complete requirements for each design-unit combination. The matcher evaluates profiles separately and selects the best-fitting one; requirements from different profiles are never unioned into artificial missing-data demands.

For joint reasoning, compare:

```text
variation requirement <-> dataset capability
population, unit, geography, time, frequency, fields, identifiers
```

Return `compatible`, `conditional`, or `incompatible` for each dimension and explain any restricted identifiers, timing gaps, aggregation mismatch, or treatment measurement error.

## Idea matching

Translate the idea into outcome, population, observation unit, geography, time, frequency, mechanism, available data, identifiers, and constraints. Use `scripts/search.py` for compact recall and `scripts/match.py` for deterministic compatibility before opening canonical records. Apply hard filters before substantive reasoning. Free-text unit, geography, and population comparisons remain manual-review conditions; the tool does not certify parallel trends, exclusion restrictions, or mechanisms.

Normalize broad topics through `schema/topics.yaml`. `domains` remain detailed descriptive tags, while stable topics and their English/Chinese aliases support recall without requiring users to guess a record's exact wording.

Apply static knowledge eligibility before query-specific compatibility. `direct-candidate` may be recommended after canonical review; `conditional-candidate` must state its remaining conditions; `lead-only` may only be offered as an audit lead; `method-inspiration` supplies audited construction logic but never a China shock; `method-lead` is unaudited overseas inspiration; `do-not-recommend` is excluded. If no eligible case survives, report a knowledge gap rather than silently promoting an immature record.

Every recommendation explains institutional fit, treatment, comparison, exposure, design, required data, assumptions, threats, and close alternatives. Return a clarification, incompatibility, or knowledge gap instead of forcing a recommendation.

Search in two lanes. First retrieve `china-variation` and `global-china-variation` as candidate shocks. Separately retrieve `transferable-method` as design inspiration. A method record may suggest how to construct an IV or comparison, but it must never be returned as if the foreign policy occurred in China. Combine the lanes only after checking that an analogous Chinese assignment mechanism and required data actually exist.

## Long-run controls

- one mutating claim in the shared worktree and one coherent record boundary at a time;
- claim-token fencing, positive leases, explicit renewal, and stale-claim recovery;
- screen decisions separated from canonical extraction;
- stable source and variation fingerprints;
- atomic state writes and workspace locks;
- explicit retryable failures and stale-claim recovery;
- primary-evidence and assignment gates for mature records;
- mandatory knowledge-role classification before publication;
- method-transfer completeness for retained overseas research;
- duplicate alias and related-ID checks;
- generated-view freshness checks;
- health signals for candidate backlog, partial timing, unclear assignment, missing primary evidence, weak threat assessment, source concentration, and stale audits.

External outages justify `blocked`, never weaker evidence. Stop cleanly when source quality, rate limits, or context deteriorate.

## Release gate

Run the commands in `README.md`. Generated health and router files are outputs. A non-zero result means the repository is not ready for unattended continuation.
