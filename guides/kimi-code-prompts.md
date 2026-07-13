# Kimi Code Prompt Playbook

This playbook provides copy-ready prompts for running Econ-Variation with Kimi Code and Kimi K2.7 under an approximately 260k, frequently compacted context window. The prompts are intentionally written in Chinese because user-facing communication is Chinese; repository content, canonical records, task notes, field names, and formal documentation remain English unless an official Chinese title or name is needed for retrieval or evidence.

Use one prompt at a time. Prompt 1 is the default entry point for unattended continuation; the remaining prompts are task-specific. Do not combine the entire playbook into one large prompt. The repository—not the conversation—must carry durable memory: after every bounded source or record task, Kimi should leave task state, provenance, evidence, and generated outputs in a recoverable condition. A new or compacted context should recover from `AGENTS.md` and `python scripts/doctor.py`, not from a long narrative recap.

The prompts favor direction and judgment over a dense list of prohibitions. They do not replace `AGENTS.md`, `guides/operations.md`, the schema, or the task lifecycle; they help Kimi enter those mechanisms with the right intent.

---

## 1. Continue the highest-value work

Use this when Kimi should resume the project without requiring a new topic from the user.

```text
请把 Econ-Variation 仓库本身视为本次工作的长期记忆，而不要依赖当前对话中可能很快被 compact 的上下文。先阅读 AGENTS.md 并运行 python scripts/doctor.py，根据仓库当前状态选择一个最有研究价值、同时能够在本轮可靠闭合的下一任务。只读取该任务所需的操作指南、候选记录和来源，不要重新通读全部 variations 或历史任务。完成当前任务的认领、证据核验、内容处理、质量门和状态保存后，如果没有真实阻塞，就继续下一个优先级最高的有界任务；每完成一个任务都要先把判断和进度持久化，再开始下一项，使任何时点发生上下文压缩都不会丢失工作。始终围绕中国实证研究价值决定优先级，正式仓库内容使用英文，向我用中文简洁汇报已完成内容、证据质量、记录状态、剩余风险和下一步。不要为了显得有进展而降低证据标准或提升成熟度，也不要让历史维护无限挤占新的高价值知识收集。
```

## 2. Run a topic-focused collection campaign

Use this for a sustained collection run. Add a topic on the last line when desired; if it is left blank, Kimi should select a high-value coverage gap rather than stop for clarification.

```text
请围绕本消息末尾给出的主题开展一轮持续但可恢复的 Econ-Variation 收集工作。先阅读 AGENTS.md、运行 doctor，并用现有搜索和健康信息确认该主题是否已有记录、候选或重复线索，再从高质量经济学及相关领域文献中寻找真正能够恢复 assignment mechanism 的中国 variation、直接影响中国的全球变化，或具有明确中国迁移价值的识别方法。不要一开始就批量写政策卡；先筛选来源，再逐个完成 identity resolution、制度背景、时间与处理分配、论文设计、数据要求、识别威胁和证据定位。每篇来源和每条 canonical case 都应作为可独立闭合的工作单元，完成并保存后再继续，以抵抗频繁 compact。优先形成少量 decision-sufficient 的可靠记录，而不是积累大量看似丰富但无法推荐的线索；若主题未填写，则根据当前可推荐覆盖缺口自主选择一个中国研究价值高、原始制度证据可获得的主题继续，不要因此停住。正式内容写英文，向我用中文汇报。

主题（可选）：
```

## 3. Screen a source batch without contaminating the catalog

Use this when the user has a paper list or wants efficient screening before deep extraction.

```text
请对本消息末尾的文献清单进行高效率范围筛选。先按 AGENTS.md 和 doctor 恢复仓库状态，并把每篇文献作为独立的 screen task 依次处理，不要在筛选阶段直接修改 canonical records。对每篇文献先判断它属于中国 variation、面向中国的全球 variation、可迁移识别方法，还是不应保留；判断依据是能否恢复有识别价值的分配、阈值、时点、边界、随机化、暴露或工具变量构造，而不是期刊声望或关键词相似。通过筛选的来源应留下去重所需的稳定指纹、清楚的保留理由和独立后续任务，未通过的来源应明确 skip，证据暂时无法取得则诚实 blocked。每完成一篇就闭合并保存其任务状态后再处理下一篇，这样 compact 不会让同一文献被重复筛选。清单为空时，可从当前主题中选择三到五篇高相关来源开始，但仍逐篇完成任务。最后用中文给出紧凑的保留、跳过、阻塞及后续任务概览。

文献或 DOI 清单（可选）：
```

## 4. Resolve variation identity and duplicates

Use this before extraction when a policy family, rollout, threshold, or existing records have ambiguous boundaries.

```text
请处理当前队列中最优先的 resolve 或 consolidate 问题；如果我在消息末尾指定了候选，则以该候选为目标。先运行 doctor，搜索 variations、candidate ledger、别名、DOI、法律标识和 assignment fingerprint，判断它究竟是一条新 variation、现有记录的同一 case、应拆分的政策家族，还是不具备可恢复识别来源的线索。划分边界时关注“一种制度工具、一个实施制度、一个主要分配机制”，不要因为政策名称相同就合并不同批次、不同地方实施、不同阈值或不同处理边际，也不要因论文不同而重复创建同一 variation。用原始制度文件和论文设计说明支持最终边界，保留必要的 related、parent、superseded 或 contested 关系，并把无法确认的部分留作 blocker。只在边界真正解决后进入抽取或合并，完成质量门和任务状态，再用中文说明为什么合并、拆分、保留或放弃。

候选或记录（可选）：
```

## 5. Ground a China-related variation

Use this to turn a retained China lead into reliable, decision-sufficient knowledge.

```text
请将本消息末尾指定的中国相关 variation 进行一次以研究可用性为目标的 grounding；若未指定，则从 doctor 推荐且最有希望形成 conditional candidate 的记录中选择一条。不要把“补齐字段”当作目标，而要让未来 Agent 能够据此判断某个研究 idea 是否真的适配。先核验政策或制度的原始文件，再核对高质量论文正文、附录或复制材料，连贯解释改革前制度、变化动因、正式规则、实施过程、受影响对象、时间、地方裁量、例外和同期政策。随后恢复处理组、对照组、暴露强度、连接键、论文如何编码处理、实际使用数据、识别假设、诊断和威胁。明确区分已验证事实、论文报告和分析推断，每项证据写明实际访问层级和可复查 locator；找不到的核心信息应成为 blocker，而不是被合理猜测填满。完成后根据证据真实程度决定状态，不追求升级本身，并闭合任务与质量门。正式记录使用英文，向我用中文汇报其研究价值、尚存条件和是否值得推荐。

目标 variation（可选）：
```

## 6. Collect a global change that directly exposes China

Use this for trade rules, international shocks, global events, or foreign-origin changes with measurable Chinese exposure.

```text
请围绕一个直接改变中国单位所受暴露的全球或境外变化开展收集。先从 AGENTS.md 和 doctor 恢复状态，并确认它对中国的作用不是泛泛的宏观相关性，而是存在可观察的中国处理对象、暴露强度、时间或比较结构。记录应以中国面对的处理边际为中心：哪些中国地区、行业、企业或群体受到什么变化，如何构造处理和对照，怎样连接中国数据，以及全球同期冲击和一般均衡效应会如何破坏解释。境外制度历史只保留理解中国 assignment 所必需的部分；如果该事件没有直接作用于中国，但方法可迁移，则转入 transferable-method，而不是勉强建立 global-China record。逐项核验国际规则或官方来源与论文应用，完成任务和质量门后，用中文说明它为何真正属于 global-china-variation，或为何应改道、跳过或阻塞。

主题或来源（可选）：
```

## 7. Extract a transferable overseas identification method

Use this for an overseas IV, simulated eligibility measure, shift-share construction, boundary, threshold, or randomized design that may inform China research.

```text
请从指定的非中国高质量研究中提取真正可迁移的识别构造，而不是完整收集当地政策本身。先阅读 AGENTS.md、运行 doctor，并确认该论文的方法价值能够超越原国家背景。重点恢复内生变量、工具变量或比较构造的精确定义、第一阶段来源、排除限制或核心识别假设、所需数据、关键诊断、安慰剂和失败方式；随后寻找是否已有中国应用或接近的制度与数据条件，说明哪些部分可以迁移、哪些只属于原研究环境，以及在中国使用前必须重新验证什么。若缺乏可执行的中国 analogue，应保留为 method lead 或直接 skip，而不能仅因设计著名就包装成方法启发；若已有足够论文、复制材料和中国证据，仍应诚实保留 transfer limits。任务处理要在一个有界方法 case 内完成并保存，正式内容写英文，向我用中文汇报构造步骤、中国可行性和最关键的阻塞条件。

论文、DOI 或方法（可选）：
```

## 8. Upgrade one legacy lead efficiently

Use this when maintenance is justified, without falling back into endless backlog repair.

```text
请从 legacy backlog 中选择一条最值得升级的记录，但先证明这次维护能够明显增加用户价值。优先考虑研究需求常见、assignment 清楚、原始制度证据可获得、论文数据路径可恢复，并且升级后有希望进入 conditional candidate 或可靠 method inspiration 的记录；不要按文件顺序机械修补，也不要一次认领多条历史记录。运行 doctor、创建并认领真实任务后，重新核验身份边界、原始政策文件、论文设计、数据和威胁，使被触碰的记录达到当前标准；如果发现它不是 variation、混合多个机制、与现有记录重复或无法可靠验证，应选择拆分、contested、deprecated 或保持 lead，而不是为了回报投入而强行升级。完成一条后运行质量门，并根据 health 判断下一步应继续升级还是回到新知识收集。用中文说明这条记录为什么值得维护、实际改善了什么，以及下一条工作是否仍有更高边际价值。
```

## 9. Match a research idea to variation and data requirements

Use this when the user presents a research question, tentative idea, or available dataset.

```text
请把我在本消息末尾描述的研究 idea 转换为 outcome、研究对象、地区、时期、观察单位、频率、机制、已有字段、连接标识和现实约束，然后按 AGENTS.md 的 idea-matching 路径工作。先用紧凑搜索分别召回中国 variation、面向中国的全球 variation 和可迁移方法，再用结构化 match 检查知识成熟度与数据兼容性，只打开少量最相关的 canonical records。不要把关键词相似当成适配，也不要把海外方法当成发生在中国的冲击；如果成熟记录不足，应明确报告 gap，并可将最接近的 lead 作为“需要先审计的线索”单独说明。最终用中文比较少量候选，解释制度匹配、处理与对照、可利用差异、所需数据和 join keys、可能设计、关键假设、威胁以及下一步最值得验证的问题。结论可以是 conditional、incompatible、method-only 或 gap，不必为了给出答案而强行推荐。

研究 idea 与已有数据：
```

## 10. Match Econ-Variation jointly with the data knowledge base

Use this when the same agent can read both Econ-Variation and `D:\外生冲击数据库\经济数据知识库`.

```text
请围绕我在本消息末尾提供的研究 idea，联合读取 Econ-Variation 与 D:\外生冲击数据库\经济数据知识库，但保持两个项目的职责和状态彼此独立。分别遵循两个仓库各自的 Agent 说明，先在 variation 侧找有识别价值的变化及其 empirical requirements，再在数据侧找真实可获得或可构建的数据能力；不要因为主题相似就宣称二者能够连接。逐项比较研究对象、观察单位、地域层级、时间覆盖、频率、结果变量、处理构造、字段、访问条件和 join identifiers，说明哪些组合 compatible、哪些 conditional、哪些 incompatible。允许研究问题、数据和 variation 之间迭代收敛：如果现有问题无法成立，可以提出最小幅度的研究对象、时期或数据调整，但不要偷偷改变核心研究问题。最终用中文给出少量“variation × data × design”组合、成立所需条件、最大风险和仍缺失的证据；不要向任一仓库写入对方的内部 ID 或制造紧耦合。

研究 idea：
```

## 11. Recover safely after context compaction or interruption

Use this immediately after Kimi compacts its context, loses conversational detail, or resumes an interrupted task.

```text
当前上下文可能已经压缩或丢失，请不要依据残余对话猜测之前做到哪里，也不要重新从头扫描整个仓库。把持久化仓库视为唯一可信交接：先阅读 AGENTS.md，运行 python scripts/doctor.py，检查是否存在 active task、租约、候选、失败状态或 stale generated output，再只打开该任务对应的记录、来源和 operations 相关章节。若已有有效认领，就从已保存的证据和任务状态继续；若租约过期、token 不匹配或上次失败，则使用项目已有的 renew、retry、release 或 reclaim 流程恢复，而不是重复创建任务或绕过状态管理。若没有活动任务，再选择 doctor 给出的安全下一步。恢复后先完成一个最小可闭合单元并通过质量门，再继续长期工作；所有正式内容使用英文，向我用中文给出很短的恢复说明、当前真实状态和接下来正在执行的动作。
```

## 12. Review portfolio value and prevent maintenance drift

Use this after several completed tasks, before a new long run, or when collection begins to feel dominated by repair work.

```text
请进行一次只读的阶段性产品复盘，用来决定接下来一段时间应收集新知识、ground 高价值候选，还是处理少量真正阻塞使用的历史债务。先运行 doctor，并结合 health、candidate queue、最近完成任务和默认检索结果判断：哪些研究主题缺少可推荐 variation，哪些 lead 最接近产生真实用户价值，哪些维护只是让文件看起来更整齐但不会改善匹配。不要用记录数量、测试全绿或字段完整代替研究可用性，也不要因为存在大量 legacy debt 就默认逐条修复。给出一个很短的下一阶段优先序，并立即认领其中第一个可执行任务继续工作；每完成若干有界任务再复盘一次，避免目标漂移和标准退化。只有当来源不可访问、外部资源不足、仓库状态异常或确实需要用户作出会改变结果的选择时才停下，并用中文留下足够让下一次 compact 后继续的简洁交接。
```

---

These prompts deliberately avoid asking Kimi to “remember everything.” Reliable long-running behavior comes from repeatedly recovering intent and state from the repository, closing one bounded task at a time, and refusing to convert missing evidence into confident prose.
