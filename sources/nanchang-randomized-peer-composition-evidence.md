# Nanchang randomized peer composition: evidence and admission history

## Audited admission — 2026-10-04

Task `task-f79f27d7d3fb` resumed this already screened assignment after the owner
approved an exact-group shared-DOI exception. The author-submitted registry was
reinspected via direct HTTP; the [author-hosted final typeset article](https://adamszeidl.com/papers/interfirm.pdf)
was read at II.B, III.B and embedded AppendixA.2. Note23 specifies1000 feasible
allocation redraws for expected peer exposure. Note8 illustrates slot vectors;
its numerical prose differs from one listed vector, so exact executable
reconstruction must use the allocation material, not silently repair the example.
The replication API attempt failed at transport; no archive/code contents were
inspected. The mechanism is decision-sufficient with explicit data-access and
exact-replication conditions, not ready for execution from a generic city panel.

Canonical: `variations/china-nanchang-randomized-peer-group-composition.md`.
The invitation-versus-control case is unchanged. An audit in
`state/doi-assignment-audits.jsonl` links both cases to their verified registry
assignment evidence and explains why their treatment/comparison differ. The four
designed group types are not counted separately. The older blocked-admission
account below remains historical provenance, not the current validator rule.

Inspected on 2026-09-28 under `task-852c7bc3396a`. This is a source dossier, not a
canonical variation, and does not increase the usable-record count. The retained
main invitation record is
`variations/china-nanchang-interfirm-network-meetings-randomization.md`.

## Why this is a different assignment question

The main record asks what happens when a recruited firm is invited to organized
monthly meetings rather than assigned no meetings. The present question concerns
which peers an invited firm receives. Its comparison is among invited firms with
different conditional peer assignments, not invited versus no-meetings firms.
The four designed group types are not four additional variations by themselves.

## Sources and inspected boundary

E1: Cai and Szeidl, author-submitted [AEA trial registration
AEARCTR-0001859](https://www.socialscienceregistry.org/trials/1859), DOI
`10.1257/rct.1859-1.0`. The intervention and experimental-design sections were
inspected through direct HTTP because browser retrieval failed. They document
randomized regional peer-group types and the August 2013-August 2014 program.
Registration was submitted on 2017-01-09, after the intervention, and is not
evidence of an ex-ante analysis plan or an independent randomization audit.

E2: Cai and Szeidl (2018), [Interfirm Relationships and Business
Performance](https://doi.org/10.1093/qje/qjx049), QJE 133(3):1229-1282. The open
[publisher HTML](https://academic.oup.com/qje/article/133/3/1229/4768295) was
inspected, including II.B(2), III.B, Table VII, and embedded Appendix A.2,
equations (4) and (8), Table A.3. No allocation code was inspected.

## What the paper establishes

[E2, verified paper report] Allocation uses 26 subregions and baseline
size-sector strata. Random ranks populate designed groups. Baseline peer size
is the leave-own-firm-out mean of logged employment, not the log of mean
employment. The main panel pools the two follow-ups, includes firm effects and
post interactions with the allocation-conditioning variables and their
interactions, and clusters by meeting group. The alternative separates
assignment-expected exposure from its surprise component.

[E2, reported interpretation] The resulting contrast identifies a composition
effect, not the isolated effect of peer employment: size carries correlated peer
attributes. Across-subregion peer-size differences are not random. Even random
allocation can generate leave-one-out exclusion bias; the paper examines the
surprise component and artificial no-meetings groups as specification checks.

## Reconstruction needed for use

The data contract is invited firm-survey-wave observations, 2013-2015, with
baseline and at least one follow-up. It needs stable firm and assigned-group IDs,
subregion, baseline sector and size stratum, employment, outcomes, response flags,
and the constrained group-slot mapping. Recover the expected peer exposure under
the actual feasible allocation, then subtract it from assigned exposure.
An unrestricted city-wide shuffle is not the same assignment.

[Analytical inference] Preserve the baseline group roster when members stop
attending or responding. Recomputing peers from survivors turns assigned
composition into a selected outcome. Attendance, outside-group links and the
separate cross-group meeting intervention can mediate contact; retain them
without redefining the original assignment. An ordinary city-year panel cannot
recover this exposure without experimental identifiers.

Exact slot maps, allocation probabilities, variable names and executable
expectation calculations remain to be inspected in the replication deposit,
`10.7910/DVN/5ZX8ZI`. Metadata establishes the deposit's existence only.

## Why canonical publication stopped on 2026-09-28 (historical)

The attempted separate record was blocked by the current validator's rule in
`scripts/validate.py`: more than one nondeprecated record citing the same
application DOI produces a warning and, if either is mature, an error requiring
a duplicate-assignment audit. The current schema and validator provide no
audited-distinct-assignment exception. That is an interface limitation, not
evidence that the two assignments are identical.

Do not replace the DOI with a working-paper DOI, omit the genuine paper identity,
downgrade the admitted invitation record, or combine these different primary
assignments just to pass. A future maintainer can resolve this supported
multi-assignment case explicitly, with an evidence-based audit and corresponding
tests. Until then this dossier preserves the work and counts as no new canonical.
The only withdrawn file was the unadmitted draft created during this same task;
no pre-existing canonical file was removed or changed.
