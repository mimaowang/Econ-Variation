# DeepSeek Harness handoff

This note is only for work claimed by the official DeepSeek Harness. It explains a
runtime tendency, not a new research rule: a long Harness turn can keep producing
web searches even after every accessible route is returning the same source family.
In this repository, that repetition is not knowledge gain.

During a bounded evidence pass, keep the decision chain in view: identity, the
institutional or assignment rule, timing, treatment and comparison, the data join,
and the evidence boundary. After each concrete retrieval route, compare what it
actually added. If it adds no new primary locator or decision-relevant field, the
evidence has reached a useful saturation point. Make a short capsule in the task
note: what is established, what remains inaccessible or only reported, and whether
one named next route could realistically close the gap. If there is no such route,
close as `blocked` or preserve the candidate; do not keep changing search wording.

This is deliberately a judgment cue rather than a search-count limit. A genuinely
new source route should still be followed. The purpose is to help a context-rich
model turn an evidence pass into an honest repository state before its turn starts
optimizing for more tool calls.

Completion is an administrative handoff, not another evidence search. The normal
`task_queue.py complete` command runs the repository release gate. Use that normal
path once at the end; if the gate fails for an environment reason, preserve the
error and release or fail the task for the next worker rather than bypassing it with
a direct Python call or a disabled gate. This keeps an honest blocked candidate from
being traded for an unobserved quality failure.
