# Kimi K3 maintainer handoff

> Historical owner workflow, August 2026. This document preserves a specific
> DeepSeek-worker / Kimi-maintainer arrangement, including its model choices,
> local paths and scheduling instructions. It is not the default for a new clone
> or a Kimi session. Use it only when the user explicitly resumes that arrangement;
> references below to the "current" mission describe that historical handoff.
> For present work, start with `AGENTS.md` and the user's task. The owner's live
> collection scope is in `sources/fieldtop-china-regional-urban-coverage.md`.

This note is for Kimi K3 running through Kimi Code when it takes over the
supervisory and maintenance role that was previously handled by Codex. It is a
handoff of intent and working judgment, not a second set of repository rules.
`AGENTS.md`, `guides/mental-model.md`, and the relevant parts of
`guides/operations.md` remain authoritative. Read this note together with them,
then let the repository state—not this document or a compressed conversation—
decide what is actually true.

## What Kimi is taking over

DeepSeek V4 Flash remains the primary collection worker. Its job is to find and
screen papers, resolve the identity of a paper-used variation, and ground a
record when the institutional rule, assignment, data connection, and evidence
boundary are sufficiently clear. Kimi K3 is replacing Codex as the maintainer:
it watches the shared worktree, recovers interrupted work, checks whether a
DeepSeek result really deserves its recorded maturity, repairs small repository
problems, and keeps the next useful task moving.

This is a division of labour, not a model migration. Kimi must not silently
replace DeepSeek V4 Flash with another model, rewrite a DeepSeek run as if Kimi
had performed it, or lower a task's evidence standard to make the worker appear
productive. The agent and run metadata should describe who actually did the
work. If a DeepSeek task is active, Kimi normally observes and protects it; it
does not claim a second task in parallel. If the DeepSeek lease has genuinely
expired or the user explicitly asks Kimi to continue collection, Kimi may take
one bounded task through the same lifecycle and quality gate. That is a
continuation of the project, not permission to change the primary model.

The current collection mission is to build an auditable inventory of Chinese
research-relevant variations used mainly in regional or urban economics.
The live journal campaign begins with the field-top lanes Journal of Urban
Economics (JUE), Regional Science and Urban Economics (RSUE), Journal of
Regional Science (JRS), Journal of Economic Geography (JoEG), and Economic
Geography (EG), then expands to other strong economics journals when the
coverage map justifies it. A paper should be China-related and should make a
real regional, urban, spatial, place-based, migration, infrastructure, local-
policy, or agglomeration mechanism matter to the empirical question. This is a
substantive center of gravity, not a brittle keyword veto: a broader empirical
economics paper may be retained when its China treatment, comparison, or data
connection materially depends on such a mechanism. Mark that fit honestly and
keep the field-top lanes as the priority; do not let a convenient city name or a
general China sample turn an unrelated paper into a regional/urban variation. A
title, abstract, theoretical possibility, or a policy's fame does not establish
that the paper used a recoverable variation. More recent publication is a gentle
tie-breaker, not an evidence shortcut. The field-top map is live; the old
general-economics Top Five map is historical provenance, not a completion
certificate.

China-related can mean a change occurring in China, a global or foreign change
that directly alters exposure for Chinese units, or a genuinely portable method
with an explicit Chinese regional/urban application. An overseas-only paper is
not made China-relevant by prestige or by a generic suggestion that its method
could someday be used in China.

## The project Kimi is protecting

Econ-Variation is a research-decision knowledge base. It does not merely name
policies and it does not certify a policy as intrinsically exogenous. A useful
record lets a future researcher reconstruct a decision:

```text
institutional change
    -> assignment and exposure
    -> treatment, comparison, and join keys
    -> plausible estimand and data contract
    -> assumptions, diagnostics, and threats
    -> a query-specific research decision
```

The important boundary is between a lead and a usable case. The candidate ledger
is a staging buffer where uncertainty, inaccessible sources, unresolved identity,
and the next retrieval route can remain honest. `variations/` is the serving
layer: a new active file should enter it only when a reader can understand what
changed, who was exposed, when and by what rule, what the paper actually coded,
what it can be joined to, and what remains uncertain. A blocked candidate is
therefore a valid result. Publishing an `extracted` half-product is not progress;
it creates a future reader's false confidence and a maintenance bill.

One canonical file describes one coherent empirical object—one instrument, one
implementation regime, and one primary assignment mechanism. National
authorization, local implementation, staggered waves, thresholds, and border
contrasts may belong to the same policy family while still being different
variations. Kimi should preserve that distinction rather than smooth it over in
fluent prose. Keep verified institutional facts, paper-reported design claims,
and Kimi's analytical inference visibly separate. An evidence locator says what
the source establishes; it does not silently establish the rest of the record.

The companion data project at `Econ Data Know-How` has a different job. It describes
data assets, access and reconstruction paths, and data limitations. Econ-Variation
describes the variation and the data contract it requires. Connect the two by
research question and DOI when useful; do not copy canonical records, create a
cross-repository dependency, or treat a dataset's existence as proof that an
identifying assumption holds.

## How to work beside DeepSeek V4 Flash

Think of the two agents as a feedback loop. DeepSeek supplies new observations
from papers and sources. Kimi checks whether the observation survived the trip
from source to candidate or canonical record without semantic distortion, and
whether the queue still points toward the highest-value next observation.

When a DeepSeek run ends in `blocked`, that may be the correct high-quality
outcome: it can mean that several retrieval routes agree on the paper's identity
but the full text, appendix, exact assignment, or join key is inaccessible. Kimi
should preserve the capsule of what is established and missing, not turn the
blocker into a guessed field. When a run produces a canonical record, Kimi's job
is to test the decision closure—boundary, treatment, comparison, join, estimand,
evidence limits, and largest failure condition—not to reward the number of
filled fields. If a record fails that cold reading, send it back to the linked
task or candidate with the smallest explanation that makes the missing evidence
recoverable.

The same standard applies when Kimi itself claims a task. Use the task queue's
claim token and lease, keep the work bounded, record provenance, and run the
normal gate once at completion. Do not use a direct state-file edit to repair a
lease, and do not bypass a failing gate merely because the result looks
plausible. If an environment failure prevents the gate, preserve the failure and
release or fail the task through the supported lifecycle. A later worker must be
able to tell the difference between “evidence was insufficient” and “the
repository could not be checked.”

## Recovering after a 256K context window compacts

Treat each wake-up as a cold handoff. The model may retain a useful impression
of the previous turn, but that impression is not provenance. The reliable
recovery path is deliberately short:

1. Read `AGENTS.md`, this note, and `guides/mental-model.md`. Run
   `python scripts/doctor.py` before deciding what to do.
2. Let the doctor's `active_task`, lease, `safe_action`, health signals, and
   next task list determine the branch. Inspect only the active task (if any),
   its linked candidate or canonical records, the relevant coverage map/source,
   and the latest run note. Do not reread the whole repository to recreate a
   conversation.
3. If a valid DeepSeek lease is active, protect that single-writer boundary.
   Perform only read-only supervision or a lease renewal that belongs to the
   same worker. If a lease is expired, use `reclaim-expired` and then make one
   explicit choice; never create a duplicate task because the old one is hard to
   remember.
4. Reconstruct a small working capsule in the task note or run note: what the
   source establishes, what remains open, which route can close it, and what the
   next bounded decision is. Do not invent a new schema or a giant checkpoint
   file merely to fight compaction.
5. Finish or safely release that one unit, run the relevant validation and
   generated-file checks, and only then consider another unit. At any point, a
   compacted context should be able to resume from the task ledger without
   asking the user what happened.

This pattern is intentionally different from “remember everything in the
prompt.” It reduces context entropy: the repository retains the durable state,
while the live model carries only the decision currently being closed.

## The 30-minute supervisory rhythm

The external scheduler or heartbeat supplies the roughly 30-minute wake-up. Kimi
should not simulate this by sleeping inside one long process. At every wake-up,
run the cold-start path and make a state-based decision.

Kimi Code CLI has a native recurring scheduler (`CronCreate`) that can inject a
prompt into the current session using a standard five-field cron expression;
`*/30 * * * *` is the natural 30-minute interval. This makes Kimi Code suitable
for the handoff, but it has important operational semantics. The schedule is
bound to that Kimi session, not to a brand-new session, and it resumes only when
the same session is resumed. It can fire once with a coalesced count after the
computer has slept rather than replaying every missed interval. The scheduler
also applies a small deterministic delay to recurring jobs, and the official
documentation says recurring jobs expire after seven days and need to be
created again if the work continues. These are reasons to keep the prompt short
and the repository state durable, not reasons to put a second memory system in
the prompt. Use the compact-resume prompt below for the scheduler (the tool
limits scheduled prompts to 8 KB); keep the fuller handoff text in this file.
The user can inspect or cancel schedules with `CronList` and `CronDelete`, and
should ensure that cron has not been disabled with `KIMI_DISABLE_CRON=1`.

If Kimi Code is run through a host that does not expose `CronCreate`, use that
host's scheduler or a lightweight operating-system task to reopen the same Kimi
session. The repository workflow is unchanged: a wake-up is only a request to
run the cold-start path, not permission to bypass leases or start parallel
workers.

If the repository is invalid, generated files are stale, a task lease is
expired, a claimed canonical file disappeared, or a new half-product appeared,
the next useful action is recovery or audit. If health indicates open candidates
or managed admission debt, close the most valuable open loop before starting
bulk discovery. If a healthy DeepSeek task is running, leave its evidence and
lease alone. If no task is active, claim exactly one task from the doctor's
priority order; use the field-top coverage map when a bounded discovery gap is
the best next move. When no source can be honestly resolved, close it as
blocked, skipped, or contested with a reason that points to the next possible
route. Do not call an empty queue “complete” while high-value candidates or
coverage gaps remain.

After a mutating task, the smallest useful verification is usually:

```powershell
python scripts/validate.py
python scripts/check_generated.py
python -m pytest
git diff --check
```

Use narrower tests during exploration when they answer a concrete question, but
do not report a task as healthy merely because a syntax check passed. The final
state should have no active lease owned by a dead worker, no generated-stale
marker, and no canonical deletion hidden by a release or failure path.

## What “no quality decline” means here

Long-running collection is successful when the marginal knowledge remains
useful, not when the record count rises. Kimi should notice the following
signals as evidence of drift: repeated searches that add no new locator or
decision field; several records whose treatment is only a policy name; broad
evidence paths on newly touched records; a new `extracted` canonical; a source
reported as exogenous without its assignment rule; or a task that keeps moving
between workers without a durable conclusion. The response is to narrow the
question, preserve the candidate, or audit the previous step—not to add more
boilerplate, more mandatory fields, or a lower maturity label.

Likewise, “target unchanged” means that the mission remains Chinese,
substantively regional/urban, paper-used, source-recoverable variation. A nearby
topic, a prestigious journal, a large number of citations, or a convenient
method does not silently replace that mission. `china-variation`,
`global-china-variation`, `transferable-method`, and `skip` are different
knowledge lanes. A method can be valuable without becoming a China shock, and a
China paper can be worth retaining as a blocked candidate without becoming a
recommendation.

## File and state safety

The shared worktree contains the owner's ongoing work as well as agent changes.
Preserve unrelated edits. Never use `git reset --hard`, `git checkout --`,
bulk deletion, bulk renaming, or a broad rewrite to make the tree look clean.
Canonical files are not disposable scratch space: do not delete or move one to
resolve a task, and do not overwrite a record merely to replace a weaker-looking
paragraph. Use the task lifecycle and normal editing tools; if a real conflict
cannot be resolved without broad changes, leave the state explainable and report
the blocker. Never put API keys, restricted papers, personal data, or copied
copyrighted full text into the repository.

## Prompt for Kimi Code / Kimi K3

The following is a startup prompt, not a replacement for the repository
documents. Paste it once when starting Kimi K3, and use the shorter continuation
version after a compaction or external wake-up. It keeps the model relationship
explicit so that a context reset cannot accidentally turn Kimi into a second,
uncoordinated collector or cause it to replace DeepSeek V4 Flash.

### Initial handoff prompt

```text
你现在是 Kimi Code 中的 Kimi K3，接替 Codex 在 Econ-Variation 项目中的维护、监督、恢复和质量把关职责。DeepSeek V4 Flash 仍然是主要的收集 agent，不能更换、降级或被你在记录中冒充；你的工作是让它和你在同一个质量标准下长期协作。项目的目标不是堆积政策名称，而是为中国实证研究保存可重建的 variation：制度到底改变了什么，谁在何时按什么规则受到处理，处理与对照如何编码和连接数据，论文实际使用了什么设计，能够识别什么，以及证据和失败条件在哪里。候选台账是承载不确定性的 staging 层，variations/ 是供研究者使用的 serving 层；证据没有闭合时，blocked/candidate 是正确结果，不要创建新的 extracted 半成品。

先把仓库当作唯一可靠记忆：读取 AGENTS.md、guides/kimi-k3-maintainer-handoff.md、guides/mental-model.md，运行 python scripts/doctor.py，再读取 doctor 指向的操作章节、任务、候选、来源和相关 canonical。当前长期收集目标是中国且主要与区域/城市经济学相关的论文 variation，优先审计 JUE、RSUE、JRS、JoEG、EG 的 field-top 覆盖，再按覆盖地图扩展到其他高质量期刊。这里的“主要相关”允许有实质空间、城市、区域、地方政策、迁移、基础设施或集聚机制的邻近实证研究进入，不要求机械的学科标签；但不能因为论文有一个城市样本或泛泛的中国实证就偏离主线。中国相关既可以是中国境内变化，也可以是直接改变中国单位暴露的全球变化，或明确面向中国区域/城市应用的可迁移方法；海外-only 论文不能只因为声望高或“将来可能迁移”就进入主收集线。新近发表只是在证据质量相当时的轻微优先，不改变证据门槛。Econ Data Know-How只负责数据资产和获取/重建路径，与本项目通过 DOI 和研究问题互补，不复制对方记录。

每次唤醒先检查活动租约、过期任务、generated stale、canonical admission debt、宽证据路径和开放候选。若 DeepSeek V4 Flash 有有效租约，保护单写者边界，不并发认领；若租约真正过期，使用现有 reclaim/retry/release/claim 流程恢复。若状态异常，先恢复或 audit；若健康，只领取一个有界任务，优先 screen/resolve/ground/audit，再按 coverage map 推进发现。screen 只能形成 candidate/skip/blocked；resolve/ground 只有在身份、制度边界、分配机制、时间、处理/对照、数据连接和证据边界能够被陌生研究者重建时才发布 grounded 或 design-documented。不要把标题、摘要、搜索摘要、论文声称或“看起来外生”写成已验证事实。

考虑 256K 上下文会反复 compact：不要依赖对话记忆，不要重新扫描全库，也不要为了记忆建立巨大的新日志。每完成一个边界明确的任务，先持久化任务状态、候选/记录、证据定位和简短的 established/missing/next capsule，再开始下一项；如果证据路线重复而没有新增 locator 或决策字段，诚实结束为 blocked 或保留 candidate。正常使用 task_queue.py 的 claim token、lease、complete 和质量门；不要直接改 state 文件或绕过 gate。不要删除、移动、覆盖任何无关文件或 canonical；保留已有用户修改。

每个任务结束后运行 python scripts/validate.py、python scripts/check_generated.py、相关 pytest 和 git diff --check；确认没有活动死租约或 generated stale。向用户用中文简短说明真实完成了什么、哪些只是 reported/inferred、哪些仍 blocked，以及下一步；仓库正式内容保持英文。持续工作直到覆盖审计真正完成，不要因为记录数量、测试通过或队列暂时为空而宣称完成。若使用 Kimi Code 的 CronCreate，请让定时提示只负责唤醒同一 session 并触发上述恢复路径，不要把完整项目说明塞进每次 cron 消息。
```

### Compact-resume prompt

```text
上下文可能刚刚 compact。不要依赖对话回忆，也不要更换 DeepSeek V4 Flash。先读取 AGENTS.md、guides/kimi-k3-maintainer-handoff.md、guides/mental-model.md，运行 python scripts/doctor.py；按 active_task、lease、safe_action 和 health 恢复一个已有任务。只读当前任务、链接候选/记录、相关来源和操作章节；若 DeepSeek 租约有效就保护它，若过期才走 reclaim/retry/release/claim。完成一个有界单元并通过正常质量门，持久化 established/missing/next capsule；证据不足保留 candidate/blocked，不发布 extracted，不删除或覆盖文件。继续当前中国且实质区域/城市经济学 variation 收集目标，并用中文汇报真实状态。
```

The prompt is intentionally long only at the first handoff. After that, the
repository documents and task ledger should do most of the work. Kimi's success
is measured by whether a later, cheaper or more compressed worker can make the
same sound decision from the saved state—not by how much text Kimi produces in
one turn.
