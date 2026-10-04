---
schema_version: 2
id: china-nanchang-randomized-peer-group-composition
name: Nanchang Randomized Peer-Group Composition among Invited Firms
aliases: [Nanchang randomized manager peers, China experimental peer composition, 南昌企业同伴随机分组]
status: grounded
provenance:
  task_id: task-f79f27d7d3fb
scope:
  country: China
  regions: [Nanchang, Jiangxi]
  domains: [development-economics, urban-economics, regional-economics, firm-networks, industrial-organization]
  variation_type: other
  knowledge_role: china-variation
  china_relevance: Implemented mainland firm experiment assigns peers within local business meetings; the comparison concerns composition among invited Nanchang firms, not a foreign method or national policy.
identity:
  instrument: Conditional random assignment of invited firms to designed local meeting groups
  authority: Jing Cai and Adam Szeidl with Nanchang Commission of Industry and Information Technology
  legal_identifiers: [AEARCTR-0001859, 'Trial registration DOI10.1257/rct.1859-1.0']
  implementation_regime: Researcher-organized monthly manager meetings for one year; peer allocation nested within the invitation arm.
  assignment_mechanism: Random ranks within subregion-size-sector strata fill predetermined slots in four group types; only conditional peer variation is random.
  parent: null
  related_variations: [china-nanchang-interfirm-network-meetings-randomization]
timeline:
  announcement: null
  effective: null
  implementation_start: '2013-08'
  implementation_end: '2014-08'
  local_timing: Summer2013 recruitment/baseline, first meetings August2013, summer2014 and2015 follow-ups. Registry dates August1,2013-August31,2014 are program bounds, not each group's exact dates.
  anticipation: Recruitment and willingness precede assignment. Peer characteristics are measured before meetings, not after peers have changed performance.
  last_verified: '2026-10-04'
assignment:
  unit: Invited firm assigned to a meeting group within one of26 local subregions.
  treated: Invited firms with differing assigned baseline peer compositions, within their feasible conditional allocation.
  comparison_pool: Other invited firms under the same subregion and size-sector allocation constraints; no-meetings firms are a separate invitation contrast and a placebo, not the baseline peer comparison.
  rule: Each subregion splits firms at its sample median baseline employment into small/large and by manufacturing/services. Random ranks within the resulting four strata populate predetermined group slots; groups are small same-sector, large same-sector, mixed-size same-sector, or mixed-size mixed-sector. Assignment targets more mixed groups rather than equal type probabilities.
  intensity: Leave-own-firm-out mean of peers' baseline log employment. It proxies peer composition, not an isolated randomized employment change.
  exemptions: [Firms outside the recruited and invited experimental sample, Cross-subregion composition differences are not random, Other information and cross-group interventions are outside this assignment identity]
  compliance: Attendance and continued response may vary after assignment. Preserve original assigned peers rather than conditioning exposure on actual attendance or survivor membership.
  exposure_construction: Join the invitation roster and fixed group roster to baseline employment and follow-up outcomes by experimental firm ID. Compute mean log employment of other originally assigned group members. For surprise exposure subtract its conditional allocation expectation, estimated by1000 redraws under the actual stratum/rank-to-slot mapping.
  required_identifiers: [Experimental firm ID, Assigned group ID, Subregion, Baseline size stratum, Baseline sector, Survey wave, Feasible allocation slot map]
  spillovers: Outside-group ties and one-time cross-group meetings can change contact; this is the composition effect within the implemented program, not a no-contact environment.
research_compatibility:
  outcome_domains: [Firm revenue and profits, Inputs and employment, Management, Business partners, Finance]
  affected_populations: [Interested young manufacturing and service firms assigned meetings in Nanchang]
  mechanism_channels: [Managerial learning, Business matching, Peer information and capabilities]
  best_for: [Local firm-network composition effects when experimental group and baseline identifiers are available]
  not_good_for: [An isolated causal effect of peer employment holding other peer attributes fixed, Representative national effects, City-year panels without the experimental roster, Regression on unconditioned realized peer size]
design:
  claim_type: causal
  affordances: [Conditional random peer allocation, Baseline and two follow-ups, Original assigned-group rosters]
  candidate_designs: [Conditional peer-exposure panel, Expected-versus-surprise peer exposure specification]
  identifying_variation: Random rank allocation within subregion and baseline size-sector strata, not the endogenous between-subregion difference in available peers.
  primary_strategy: Paper equation4 pools post waves with firm effects and post interacted with allocation-conditioning indicators and all interactions; AppendixA.2 equation8 separates expected from surprise peer exposure.
  estimand: Effect of randomly assigned peer composition on invited participants within the program. Baseline peer size indexes a bundle of skills and connections, not one manipulable firm characteristic.
  treatment_variable: Post multiplied by assigned leave-one-out mean baseline log employment, with conditional allocation controls; surprise specification subtracts conditional expected exposure.
  comparison_logic: Compare changes across invited firms receiving different feasible peers, conditional on original allocation strata; expected peer exposure does not supply a randomized comparison.
  estimation_notes: Main peer panel pools2014/2015 follow-ups and clusters at meeting group. Management and innovation have different wave coverage and omit firm effects when baseline outcomes are unavailable. Expected peer size uses1000 redraws; exact allocation code was not inspected.
  assumptions: [Faithful constrained allocation and roster linkage, Counterfactual response and missingness compatible with assignment, Interpretation allows correlated peer attributes and program spillovers, Original baseline employment is not replaced by post-assignment employment]
  diagnostics: [Conditional balance, Expected-versus-surprise exposure, Leave-one-out exclusion bias, Artificial no-meetings group placebo, Attrition by allocation, Retention of original group roster]
threats:
  - type: conditional_not_unconditional_randomness
    basis: reported
    condition: Peer composition depends on subregion and size-sector strata; between-subregion exposure reflects local firm composition rather than random allocation.
    evidence_refs: [E1, E2]
    possible_diagnostics: [Include post interactions with all allocation-conditioning indicators and interactions, Recreate feasible random draws rather than a city-wide shuffle]
  - type: leave_one_out_exclusion_bias
    basis: reported
    condition: Excluding the focal firm from peer means mechanically correlates own and peer baseline attributes even under random allocation.
    evidence_refs: [E2]
    possible_diagnostics: [Use assignment-expected and surprise exposure, Inspect artificial-control-group placebo]
  - type: bundled_peer_attributes
    basis: reported
    condition: Peer size covaries with managerial skills and business networks; the coefficient does not isolate changing peers' employment alone.
    evidence_refs: [E2]
    possible_diagnostics: [Name the composition estimand, Avoid structural interpretation of the employment proxy]
  - type: attrition_and_realized_contacts
    basis: inferred
    condition: Recomputing peers from respondents or attendees selects post-assignment outcomes and can distort the assigned contrast.
    evidence_refs: [E1, E2]
    possible_diagnostics: [Keep baseline assigned roster, Separate nonresponse and closure, Report contact and attendance without redefining allocation]
empirical_requirements:
  contract_version: 1
  population: Invited firms in the Nanchang recruited experimental sample; final paper reports1500 invited of2820 firms.
  observation_unit: firm-survey wave
  geography_level: experimental subregion and meeting group
  time_start: 2013
  time_end: 2015
  minimum_frequency: baseline and annual follow-up surveys with explicit recall windows
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields: [Invitation assignment, Original group membership, Baseline employment, Baseline sector and size category, Outcome with recall period, Response and closure indicators, Assignment slot structure]
  required_identifiers: [firm_id, group_id, subregion_id, baseline_stratum, survey_wave]
  treatment_key: [firm_id, group_id]
  treatment_source: Original experimental roster and constrained group allocation; registry and final paper explain the mechanism, not a public administrative treatment list.
  measurement_risks: [Mean of log peer employment differs from log of mean employment, Exact slot vectors and code remain uninspected, Survey year differs from outcome recall period, Ordinary firm IDs need a lawful crosswalk to experimental IDs for new outcomes]
evidence:
  - id: E1
    source_type: archive
    citation: Cai and Szeidl, AEA RCT Registry AEARCTR-0001859, author-submitted experimental documentation.
    url: https://www.socialscienceregistry.org/trials/1859
    date: '2017-01-09'
    supports: [identity.instrument, identity.legal_identifiers, identity.implementation_regime, identity.assignment_mechanism, timeline.implementation_start, timeline.implementation_end, assignment.unit, assignment.rule, assignment.exemptions]
    verification_status: verified
    access_level: official-document
    locator: Intervention and Experimental Design sections read via direct HTTP2026-10-04; four group types, regional randomization and additional interventions. Retrospective2017 registry is primary author documentation, not an ex-ante plan or independent assignment audit.
  - id: E2
    source_type: paper
    citation: Cai, Jing and Adam Szeidl2018, Interfirm Relationships and Business Performance, QJE133(3),1229-1282.
    url: https://doi.org/10.1093/qje/qjx049
    date: 2018
    supports: [identity.authority, timeline.local_timing, timeline.anticipation, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.intensity, assignment.compliance, assignment.exposure_construction, assignment.required_identifiers, assignment.spillovers, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.population, empirical_requirements.required_fields, empirical_requirements.required_identifiers, empirical_requirements.measurement_risks, design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year, design_applications.population, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design]
    verification_status: reported
    access_level: full-text
    locator: Author-hosted54-page typeset copy at https://adamszeidl.com/papers/interfirm.pdf and embedded AppendixA; II.B pp1236-1239 and note8, III.B pp1255-1259 equation4/TableVII/note23, AppendixA.2 pp1275-1277 equation8/TableA.3 inspected2026-10-04. Publisher HTTP access failed; no allocation code or separate Online Appendix inspected.
design_applications:
  - paper: Interfirm Relationships and Business Performance
    doi: 10.1093/qje/qjx049
    journal: Quarterly Journal of Economics
    year: 2018
    research_question: Does the composition of assigned business peers affect invited firms' performance?
    population: Invited Nanchang firms; peer analyses use outcome-specific response samples rather than every randomized firm.
    outcome: Revenue, profits, inputs, partners and management.
    data_used: [Experimental allocation and meeting logs, Baseline2013 and follow-up2014/2015 firm surveys]
    treatment_encoding: Post interacted with original peers' mean log baseline employment; conditional controls or separate expected/surprise exposure.
    comparison: Different feasible peer allocations among invited firms; no-meetings artificial groups supply a specification placebo only.
    empirical_design: Conditional randomized composition panel, firm effects where baseline outcomes exist, pooled post waves and meeting-group clustering.
    assumptions: [Faithful original conditional randomization, Adequate treatment of attrition and spillovers, Composition rather than pure employment interpretation]
    threats_addressed: [Conditional allocation controls, Expected/surprise separation, Exclusion-bias placebo]
    evidence_refs: [E1, E2]
method_transfer: null
readiness_blockers:
  - Exact executable reuse requires original group rosters, slot maps and variable crosswalks; replication deposit10.7910/DVN/5ZX8ZI is a lead, not inspected code. Its API retrieval failed this task.
  - New outcomes require a lawful experimental-firm linkage and defense of missingness and spillovers. A public Nanchang firm panel alone cannot encode this assignment.
---

## Institutional Background

The experiment deliberately created local manager networks with CIIT rather than
using an existing city policy. Within its invited arm, it randomized who met whom
[E1; E2, reported]. The separate invitation record asks whether to offer meetings;
this case asks how assigned peers change outcomes among firms offered meetings.

## What Changed

Groups varied by baseline size and sector composition. Four group types describe
one constrained allocation, not four independent variations. Neither the paper's
many outcomes nor alternative estimators multiply this identity [E1-E2].

## Implementation and Assignment

Subregion-size-sector strata supplied the feasible peers. Random ranks filled
predetermined slots, with unequal group-type targets [E2, reported]. The registry
verifies that an implemented peer experiment was documented by its authors; it
does not verify the allocation code or establish prospective registration [E1].

## Why This Creates Empirical Variation

The paper exploits the random component of peer allocation, not differences in
local firm populations. A fresh researcher should recover the original baseline
roster, compute leave-one-out mean log employment and preserve conditional
expectations. Equation8 separates expected and surprise exposure [E2, reported].

## Identification Risks

Own-firm exclusion can induce bias even with random peers. The paper's surprise
and placebo checks address that issue; they are not proof of every future outcome's
validity. Peer employment proxies correlated capabilities, so interpreting it as
an isolated employment intervention would change the estimand [E2, reported].

## Data Requirements

Merge experimental firm IDs across assignment, baseline and surveys, retaining
original group membership. [Analytical inference] Do not rebuild groups from
surviving firms or attendees. Exact redraws need the original slot structure;
an unrestricted shuffle does not reproduce this experiment.

## Evidence Notes

The final typeset article and embedded AppendixA were inspected; separate online
material and executable replication code were not. Registry sample counts differ
from the final paper and are not substituted for its regression population.
The exact-group DOI audit records why this assignment and the invitation case
share one paper without duplicating the same mechanism.
