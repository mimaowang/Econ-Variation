# DeepSeek Harness evidence-loop adaptation

## Intent

DeepSeek V4 Flash in the official Harness has correctly understood the repository's
semantic boundary, but a resolve task can continue searching after the accessible
evidence has stopped changing. The adaptation should improve that handoff without
turning research judgment into a fixed search counter or changing the serving-layer
quality gates.

## Chosen design

The task brief remains the main state estimate. When the claiming agent explicitly
identifies itself as a DeepSeek Harness worker (`dsh-...` or a name containing
`deepseek-harness`), the brief receives one additional explanatory stopping cue:
compare the source set after each concrete retrieval route; when routes return the
same evidence, treat that as saturation, write what is established and missing, and
close as blocked/candidate rather than searching for a differently worded duplicate.
The cue is conditional on the agent identity, is not persisted in the task ledger,
and does not affect Claude Code, Kimi, ordinary DeepSeek API runs, or validators.

A short guide explains why this cue exists and how to turn an evidence pass into a
decision capsule. It is a narrative aid, not a checklist and not a replacement for
the mental model or operations guide. The existing five-key brief shape is retained;
no schema or canonical record is changed.

## Data flow and safety

`task_queue.claim()` builds the brief from the claimed task. The conditional cue is
derived from `claimed_by` and returned only in the in-memory `task_brief`; it is not
written to `tasks.jsonl`. Existing lease, claim-token, canonical-baseline, release,
and completion protections remain authoritative. A task may still continue when a
concrete new source route exists; the cue only makes saturation legible.

The same runtime cue explains the completion path: `complete` is an administrative
handoff and its normal CLI path runs the release gate. A gate failure is preserved
as an environment or repository signal; the Harness worker should release/fail for
recovery rather than silently bypassing the gate.

## Verification

Add focused tests for Harness and non-Harness briefs: the former contains the cue,
the latter remains byte-for-byte equivalent in its stopping guidance. Check that the
brief remains compact and non-persistent. Run the queue tests, validator/generated
checks, doctor, and a bounded DSH resolve/screen task. The task must either produce a
decision-sufficient update or stop honestly in the candidate layer, with no new
`extracted` canonical record and no file deletion.
