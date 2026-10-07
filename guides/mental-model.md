# Understanding Econ-Variation

## The decision this repository exists to support

Imagine that a researcher has annual firm outcomes, firm locations, and patents, and asks whether a Chinese environmental program could help identify the effect of regulation on innovation. A policy catalog can answer, "a low-carbon pilot existed." That is not enough to design a study.

The researcher needs to know which instrument created exposure, which jurisdictions entered under the same implementation regime, why and when they entered, how a firm inherits treatment from its location, which observations form a credible comparison, and what would make that comparison fail. The researcher also needs to know whether the available panel can join the treatment, span enough pre- and post-periods, and distinguish the policy from later waves or overlapping programs.

Econ-Variation preserves the knowledge needed to make that decision. It is not a list of policies and it is not a library of claims that a policy is exogenous. A variation becomes useful only in relation to a particular outcome, population, time window, exposure measure, and comparison. The same assignment can be informative for one question and endogenous for another.

This is the project's central mental model:

```text
institutional change
       -> assignment and exposure
       -> treatment and comparison that can be encoded
       -> data contract and plausible design
       -> assumptions, diagnostics, and failure conditions
       -> a query-specific research decision
```

Every field and workflow exists to keep that chain recoverable.

## A variation is an assignment mechanism, not a policy name

A national policy name often hides several different empirical objects. Authorization may occur nationally while implementation is chosen locally. A pilot may have several waves. A threshold and a staggered rollout may coexist under one reform. These objects should not be combined merely because newspapers or papers use one policy label.

One canonical record follows one instrument, one implementation regime, and one primary assignment mechanism. This boundary matters because it determines the treatment, comparison, timing, join keys, and identifying assumptions. If those change, the empirical object has changed.

The existing `china-2014-hukou-local-implementation` record is a useful counterexample. It contains both a national five-million-population threshold and staggered city adoption. Those mechanisms generate different treatment variables and different comparisons. The record is contested because fluent prose cannot make them one coherent variation. A careful agent preserves the conflict and splits the mechanisms when evidence permits; it does not make the file look complete by blending their requirements.

Identity resolution therefore comes before extraction. Ask: *what observable rule changes one unit's exposure relative to another?* If that question has no stable answer, there is not yet a canonical case.

## Keep reality, assignment, and application separate

Three layers must remain connected without being collapsed.

**Institutional reality** explains what existed before, what formally changed, who had authority, and how implementation worked. Official documents are usually strongest here.

**Assignment and exposure** explains how units become treated in practice: eligibility, timing, intensity, exemptions, compliance, nesting, and spillovers. This layer is the bridge from institutions to data.

**Design applications** explain how a paper encoded the change for a particular population and outcome. A paper is evidence about one use of a variation, not the definition of the institution itself.

This separation prevents a common distortion. If a paper codes every named pilot city as treated from an announcement year, the record may report that application. It should not silently convert the paper's coding choice into a verified fact about when substantive local implementation began.

The prose sections preserve institutional meaning and uncertainty. The structured fields expose the same reasoning to search and matching. Neither is decorative: a fresh reader should reach the same treatment and comparison from both.

## Evidence has a boundary

Evidence quality is not only about source prestige. It is about what was actually inspected and what the source can establish.

An official notice may verify a legal identifier, announcement date, designated jurisdictions, and formal selection language. It may not establish actual compliance, a paper's sample construction, or the absence of anticipation. A paper may report a city-by-year treatment table without independently proving every local effective date. An appendix may establish a robustness exercise without validating the institution.

For each important source, a good record makes two things recoverable:

1. what the inspected passage, table, provision, or dataset establishes;
2. what remains reported, inferred, contested, or inaccessible.

That is why evidence uses precise support paths, access levels, and locators. `assignment.rule` communicates more than `assignment`; the narrower path prevents a source from appearing to support an entire block. In the narrative, verified facts, source-reported claims, and analytical inferences remain visibly distinct.

When evidence is unavailable, preserve the blocker. Do not replace missing inspection with plausible prose. An explicit unknown carries more information than false precision.

## What decision-sufficient knowledge looks like

Consider `china-8-7-poverty-county-threshold`. Its value is not that it names a famous poverty program. Its value is that a reader can recover the threshold-based assignment, the units classified around the cutoff, the time and geography needed to encode exposure, the relevant outcome populations, the data identifiers, and the threats from manipulation or other discontinuities. The record connects institutional evidence to a usable comparison while preserving the conditions under which that comparison may fail.

For an overseas method, `us-air-pollution-wind-direction-iv` illustrates a different role. The US exposure is not offered as a Chinese shock. The reusable object is the construction: how wind direction changes pollution exposure, what produces the first stage, what the exclusion restriction requires, which diagnostics matter, and what Chinese monitoring and health data would be needed. Transfer is complete only when the construction and its failure modes are recoverable; prestige or a memorable design label is not enough.

A canonical record is decision-sufficient when a fresh reader can answer, without task history:

- What exact variation does this file represent, and what related change is outside its boundary?
- Who is exposed, when, and through what rule?
- How are treatment and comparison encoded and joined to outcomes?
- What estimand could the design support?
- What data, frequency, period coverage, fields, and identifiers are necessary?
- Which claims are verified, reported, inferred, or unresolved?
- What is the most plausible way the design fails?

These questions are a cold-reader contract, not another score. One answer cannot compensate for a missing answer elsewhere.

## Candidates hold uncertainty; canonical records serve decisions

Discovery is exploratory and should remain so. A promising paper can reveal a candidate before the variation's identity, primary evidence, or treatment construction is recoverable. That information belongs in the candidate lifecycle, where it can retain the source, reason, role, blockers, and next step without pretending to be finished knowledge.

`variations/` is the serving layer. A new record enters it only after its core decision chain is recoverable. For a China-facing variation, that means the institutional identity, timing, assignment, and research application have been grounded. For a transferable method, the construction, first stage or contrast, identifying restriction, diagnostics, data needs, and transfer limits have been inspected and documented.

It is legitimate for a bounded task to end `blocked` or `skipped`. It is not a failure to decline publication. A smaller serving layer with explicit candidate memory is more useful than a large formal directory that makes later agents repeat evidence work.

Existing legacy and extracted records remain visible under their maturity gates. Their presence is historical context, not a template for new publication quality.

## How a long-running agent stays aligned

Long runs degrade when the agent begins optimizing the easiest visible proxy: files created, fields filled, tasks completed, or tests passed. The repository treats those as operational signals, not the objective.

Work in bounded tasks because each task creates a natural feedback point. Before acting, recover state from `AGENTS.md`, `doctor.py`, and the current task brief rather than from conversational memory. During the task, keep returning to the decision chain: boundary, assignment, comparison, join, evidence, failure. At completion, ask whether a new reader could use the record rather than whether the template is full.

The quality gate protects structural invariants, but judgment remains necessary. If source access deteriorates, if the last task would publish another lead, or if identity becomes less clear as evidence accumulates, stop expanding and preserve the uncertainty. More prose is not corrective feedback.

After context compression, a healthy recovery is short:

```text
read the invariant -> run doctor -> resume the one claimed task or take its brief
-> inspect only the candidate, source, and relevant canonical records
-> close one decision gap -> validate -> persist the outcome
```

This loop is stable because the repository, not the conversation, carries state. Its goal is not continuous motion. Its goal is a non-decreasing stock of decision-sufficient knowledge.

## Use judgment without losing the interface

Real institutions have more variety than a schema can enumerate. Do not force a complex policy into a familiar DID story, union unrelated design profiles, or write every possible threat into every record. Use connected prose and a small number of coherent design profiles to preserve what is special about the case.

At the same time, flexibility does not mean ambiguity at the serving boundary. The record still needs a precise identity, an encodable assignment, evidence-scoped claims, and a usable data contract. The project constrains this interface so that reasoning inside it can remain rich.

The best record is not the longest or most confident one. It is the smallest faithful representation from which another agent can reconstruct the right research decision and the reasons it might be wrong.
