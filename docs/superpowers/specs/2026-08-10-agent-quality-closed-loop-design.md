# Agent Quality Closed-Loop Design

## Purpose

Econ-Variation should let a low-cost agent recover the project's intent quickly, work for a long time without optimizing for record count, and publish knowledge that another agent can use without corrective maintenance. The repository should remain small, legible, and flexible enough to preserve real institutional complexity.

This design distinguishes unavoidable knowledge updates from avoidable corrective maintenance. New evidence will always justify future updates. Incomplete identity resolution, vague evidence boundaries, and records that cannot support a research decision should not be published as canonical knowledge in the first place.

## Control model

The project invariant is the reference signal: a record is useful only when a fresh reader can recover the variation boundary, assignment, treatment, comparison, data join, plausible estimand, assumptions, threats, and evidence limits.

Candidates are the staging buffer for uncertainty. `variations/` is the serving layer for decision-sufficient knowledge. Exploration remains flexible; strong constraints apply only at the canonical publication boundary.

The feedback loop is:

```text
project intent -> bounded task brief -> agent work -> candidate or canonical record
                                                     |
                                      deterministic gates + cold-reader contract
                                                     |
                              quality signals -> next safe task
```

No aggregate quality score is introduced. Several non-substitutable signals are reported so that passing one proxy cannot hide failure on another.

## Information design

A narrative mental model provides a low-entropy semantic attractor for context-constrained agents. It explains the workflow through a single research decision rather than restating rules. It is paired with heterogeneous exemplars: a China-facing variation, a transferable method, and a mixed-mechanism counterexample. Agents imitate the reasoning structure, not wording or record length.

`AGENTS.md` remains the short entry point. It states the invariant, routes by intent, and links to the mental model for maintenance work. `guides/operations.md` remains the lifecycle authority. Existing prompts remain compatible but point to the same conceptual source.

## Canonical admission

Existing records and legacy files are preserved. The stricter admission policy applies to newly created canonical records:

- a new China or global-China record must satisfy the existing grounded institutional core;
- a new transferable method must contain an audited method-transfer contract and verified research evidence;
- unresolved work may finish as `blocked` or `skipped`, or remain a durable candidate, without manufacturing an `extracted` canonical record;
- managed `extracted` transferable methods are leads until their core method has been audited.

Maturity remains epistemic, not a reward. The validator reports records whose observable content satisfies the next maturity gate but does not silently rewrite statuses.

## Evidence boundary

New or touched mature records must map evidence below top-level blocks. `identity`, `timeline`, and `assignment` are too broad to show which claim was inspected. Legacy content remains readable, while the task completion gate requires precise field paths for changed knowledge.

The narrative guidance also asks writers to say what a source establishes and what it does not establish. This is explanatory discipline rather than a large new ontology.

## Task briefs and long-run control

The doctor report gains a compact brief for the next task: why it matters, the relevant candidate/source, the semantic gaps implied by its stage, the publication boundary, and the minimum files to read. This is a state estimator after context compression, not a replacement for judgment.

Health gains transparent signals:

- canonical records apparently ready for promotion;
- managed active extracted records;
- imprecise evidence supports;
- candidate backlog and serving-layer readiness remain separate.

Task priority continues to favor bounded China-facing resolution. Discovery is paused by existing safety logic; the new signals make drift visible without adding an unstable total score or automatically deleting work.

## Compatibility and failure handling

No existing file is deleted. The schema and router contract remain backward compatible. Generated files continue to be derived, never hand-edited. Existing extracted and legacy records remain available under their current gates.

If a new source cannot meet canonical admission, the correct terminal action is to preserve the candidate and report the blocker. If a record mixes assignment mechanisms, it is contested or split rather than made artificially complete. If evidence is inaccessible, access failure remains visible rather than being converted into generic prose.

## Verification

Tests cover method eligibility, new-record admission, precise touched evidence paths, promotion-ready health signals, compact task briefs, generated-file freshness, and all existing behavior. The full release gate remains:

```text
validate --write-health -> build router -> generated check -> pytest -> ruff
```

Success means the repository remains valid and compatible while making the desired behavior easier to understand and the undesired behavior harder to publish.
