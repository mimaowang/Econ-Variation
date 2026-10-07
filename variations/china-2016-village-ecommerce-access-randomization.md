---
schema_version: 2
id: china-2016-village-ecommerce-access-randomization
name: China village e-commerce access randomization in eight counties
aliases: [AEARCTR-0001582, village terminal access experiment, Connecting the Countryside via E-Commerce]
status: grounded
provenance:
  task_id: task-e0f42c61f7bb
scope:
  country: China
  regions: [Anhui, Henan, Guizhou]
  domains: [development, regional-economics, market-access, household-consumption, retail-commerce]
  variation_type: other
  knowledge_role: china-variation
  china_relevance: A platform-government rural expansion program experimentally assigns village e-commerce access in eight mainland Chinese counties. The published application studies household consumption, incomes and local retail markets rather than agricultural production policy.
identity:
  instrument: Village-level randomized assignment to early e-commerce terminal and associated logistics access during an existing rural expansion program.
  authority: Collaborating e-commerce firm and research team, with government support for the broader program; the published study does not name the firm.
  legal_identifiers: []
  implementation_regime: Platform-specific warehouses and subsidized last-mile shipments combined with a village terminal, operator assistance and cash settlement. Warehouses and subsidies cannot be used for shipments outside that platform. This is not first-time internet provision, a general road improvement or county-level national demonstration designation.
  assignment_mechanism: Computer randomization within county candidate pools, stratified on existing delivery availability and village characteristics. Assigned early access and actual terminal opening differ because implementation is incomplete.
  parent: null
  related_variations: []
timeline:
  announcement: The registry describes a broader rural e-commerce policy priority from2014; it is not the experiment's treatment date.
  effective: Registry intervention start2016-01-14 is a study-level planned date, not a verified opening date for every village.
  implementation_start: 2016
  implementation_end: null
  local_timing: Baselines are December2015–January2016 in Anhui/Henan and April–May2016 in Guizhou, before local installations. Endlines occur12 months after each baseline. Control villages were subsequently prioritized for expansion after endline. Registry planned end2017-12-31 must not replace actual survey or village opening dates.
  anticipation: Candidate selection and terminal operator applications precede opening. Preserve assignment date and survey chronology; do not assume all villages unexpectedly receive treatment on one date.
  last_verified: '2026-10-07'
assignment:
  unit: Village; household and retail outcomes inherit the village assignment.
  treated: Sixty survey villages assigned early program access across eight counties; actual program opening is a separate variable.
  comparison_pool: Forty survey villages assigned control from the same county candidate pools, observed before later expansion; neither village eligibility nor sample counties are randomly selected nationally.
  rule: Extend each county candidate list by five suitable villages, randomly select five controls and seven or eight treated survey villages per county, and leave remaining candidate villages on the ordinary rollout. The survey sample is100 villages from432 candidates. Randomization is by computer in office. Stratification balances preexisting parcel delivery and applicant test score, population and nonagricultural employment. AppendixF.3 qualifies the intended2.5km village-spacing restriction as feasible rather than universal.
  intensity: Binary assigned access for ITT; binary actual program opening for the paper's instrumented TOT. Household use, purchase shares and distance to a terminal are not the randomized assignment.
  exemptions: [Operational eligibility favors sufficient population road accessibility and a capable operator applicant, Existing parcel-delivery villages receive terminal assistance without the same logistics-access change, Remaining candidate villages outside the100 surveyed villages generally receive planned program rollout]
  compliance: The paper reports opening in38 of60 assigned-treatment villages and five of40 assigned-control villages. Operator candidates can reject job offers. Four villages have no endline after local authorities halted data collection. These facts do not authorize recoding assignment to match implementation.
  exposure_construction: Retain a village-level assignment roster and county/stratum information. Join assignment to each survey observation by study village identifier, not terminal usage or county designation. Keep actual opening and local survey dates separately. Household records require round, sampling zone and household/replacement links; retail records additionally require outlet and barcode-equivalent product identity. Names below are logical required fields, not claimed replication variable names. Public deidentified identifiers do not establish an external geographic crosswalk.
  required_identifiers: [study_village_id, county_id, survey_round, household_id]
  spillovers: Residents can use terminals in nearby villages. AppendixC examines assigned-neighbor exposure within3km and10km controlling for all candidate-village proximity; saturation rates were not independently randomized. Do not equate control assignment with zero access or assume the simple contrast identifies a nationwide total effect.
research_compatibility:
  outcome_domains: [household consumption, e-commerce uptake, retail expenditure shares, household income, local retail prices, local business activity]
  affected_populations: [households in operationally selected survey villages, retailers in and near surveyed natural villages]
  mechanism_channels: [last-mile parcel delivery costs, transaction assistance, cash payment access, substitution across retail options]
  best_for: [Short-horizon effects of experimentally offered village e-commerce access, Market integration and consumer access with assignment-linked survey outcomes]
  not_good_for: [National county e-commerce demonstration DID, Randomized separation of logistics and terminal assistance components, First-time broadband access, Unrestricted firm productivity or patent panels without geographic linkage, A national long-run income effect inferred from transaction event profiles]
design:
  claim_type: causal
  affordances: [village random assignment, baseline and endline survey, imperfect implementation, preexisting delivery heterogeneity]
  candidate_designs: [village assignment ITT ANCOVA, assignment-instrumented actual-opening IV]
  identifying_variation: Within-county randomized early-access assignment among selected eligible villages, rather than naturally occurring rollout dates or individual e-commerce adoption.
  primary_strategy: SectionIIA regresses endline household or retail outcomes on village treatment and baseline outcome with village-clustered standard errors. ITT uses assigned treatment. TOT uses actual village program opening instrumented by assigned treatment; household individual adoption is not the endogenous treatment in that specification.
  estimand: ITT of assigned early village access under the realized neighboring rollout and survey observation process. IV can identify an implementation-complier effect only with relevance, exclusion, monotonicity and an appropriate treatment/interference definition.
  treatment_variable: Assigned village access for ITT; actual village opening for IV, instrumented by the assignment indicator.
  comparison_logic: Compare assigned-treated and assigned-control villages within the eligible county pools over the same local baseline/endline window. Preserve county and stratification information and inspect inference accordingly; the paper's displayed baseline specification should not be rewritten as a county-year national DID.
  estimation_notes: Equation1 includes baseline outcomes. For added or replaced endline households AppendixF.5 uses the baseline village-zone mean rather than a nonexistent individual baseline. The second-round inner-zone expansion changes weights. Table1 reports first-stage statistics; weak interacted first stages in Table2 require separate attention. Paper transaction event profiles in roughly12000 villages are a different observational extension and are not protected by the100-village randomization.
  assumptions: [Assignment implemented as registered within the candidate pool, Outcome observation and replacements do not create differential selection, Spillovers handled consistently with the chosen estimand, IV exclusion and monotonicity defended for actual opening, Appropriate village-clustered and randomization-aware inference]
  diagnostics: [Assignment balance within counties and strata, Actual-opening first stage and crossover tabulation, Missing villages and household replacement by assigned arm, Original-panel and expanded-sample sensitivity with zone weights, Neighbor assignment exposure and distance sensitivity, ITT alongside IV rather than selecting uptake-defined households]
threats:
  - type: imperfect implementation and interference
    basis: reported
    condition: Control openings and nearby-terminal use mean control villages need not have zero access. IV exclusion can fail if assignment changes exposure through channels other than own-village opening.
    evidence_refs: [E2, E3]
    possible_diagnostics: [report assignment and opening separately, ITT comparison, neighbor exposure robustness, explicit interference estimand]
  - type: survey attrition replacement and missing villages
    basis: reported
    condition: Four villages lack endline and only71% of original household respondents complete endline. New inner-zone households and replacements receive village-zone mean baselines. Absence of a statistically significant attrition difference does not prove selection is harmless.
    evidence_refs: [E2, E3]
    possible_diagnostics: [arm-specific attrition, retained panel sensitivity, bounds or selection sensitivity, distinguish missing village from replacement household]
  - type: selected sample and bundled treatment
    basis: reported
    condition: Counties depend on rollout timing and manager willingness; villages favor operational suitability. Existing-delivery heterogeneity is not a randomized component experiment. The logistics-plus-assistance package cannot establish a universal effect for all rural China.
    evidence_refs: [E1, E3]
    possible_diagnostics: [candidate-pool scope statement, delivery-status balance and interaction precision, external-validity comparisons without causal relabeling]
  - type: registration timing
    basis: documented
    condition: Registry initial registration2016-10-06 is after the listed trial start2015-12-21 and intervention start2016-01-14. The current June2017 registration is not proof that all specifications were fixed before assignment or baseline.
    evidence_refs: [E1]
    possible_diagnostics: [inspect archived registration versions and analysis-plan timestamps, distinguish registered intentions from published implementation]
empirical_requirements:
  contract_version: 1
  population: Survey households in the100 experimentally selected villages, retaining observed sample and replacement status.
  observation_unit: household-survey-round
  geography_level: study village nested in county
  time_start: 2015
  time_end: 2017
  minimum_frequency: baseline and local12-month endline
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields: [assigned_access, actual_program_opening, survey_date, household_outcome, baseline_outcome_or_zone_mean, sampling_zone, original_or_replacement_status, sampling_weight]
  required_identifiers: [study_village_id, county_id, survey_round, household_id]
  treatment_key: [study_village_id]
  treatment_source: AEARCTR-0001582 assignment protocol plus study village roster in the author replication materials; actual field names and roster content require authenticated inspection.
  measurement_risks: [Deidentified village IDs may not support outside-panel joins, Endline additions and replacements are not all panel households, Durable and nondurable recall periods differ, Program use includes app orders delivered through program terminals, Exact opening dates cannot be imputed from one registry start date]
evidence:
  - id: E1
    source_type: archive
    citation: 'Couture et al. AEA RCT Registry, E-Commerce Integration and Economic Development: Evidence from China, AEARCTR-0001582, version5.0, updated June1 2017.'
    url: https://www.socialscienceregistry.org/trials/1582
    date: '2017-06-01'
    supports: [identity.instrument, identity.implementation_regime, identity.assignment_mechanism, timeline.effective, timeline.local_timing, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule]
    verification_status: verified
    access_level: full-text
    locator: Full registry HTML read through HTTP200 direct request on2026-10-07; General Information registration dates, Interventions start/end and content, Experimental Design candidate pool and surveys, Randomization Method and Unit. This is the investigators' archived protocol, not an independently verified field audit or government notice. Registry status and public-data answers are old entries, not proof of2026 completion/access.
  - id: E2
    source_type: paper
    citation: 'Couture, Victor, Benjamin Faber, Yizhen Gu and Lizhi Liu (2021). Connecting the Countryside via E-Commerce: Evidence from China. AER: Insights3(1):35–50. DOI10.1257/aeri.20190382.'
    url: https://doi.org/10.1257/aeri.20190382
    date: '2021-03'
    supports: [assignment.compliance, assignment.intensity, assignment.spillovers, design.primary_strategy, design.estimand, design.treatment_variable, design.estimation_notes, design_applications.data_used, design_applications.treatment_encoding]
    verification_status: reported
    access_level: full-text
    locator: 'DOI identifies the published paper; publisher landing returned403, so body was read from https://www.lizhiliu.com/uploads/6/0/9/8/60987819/ecommerce_cfgl.pdf (published16-page body plus appendix). Printed pp37–45 SectionsI andIIA/B, Equation1 and Tables1/2; pp47–48 welfare evaluation. Read in memory. Firm identity, individual opening roster and data contents were not independently authenticated.'
  - id: E3
    source_type: appendix
    citation: Couture et al. online appendix, combined author-hosted published-paper PDF.
    url: https://www.lizhiliu.com/uploads/6/0/9/8/60987819/ecommerce_cfgl.pdf
    date: null
    supports: [assignment.rule, assignment.exemptions, assignment.exposure_construction, assignment.spillovers, timeline.local_timing, empirical_requirements.required_fields, empirical_requirements.measurement_risks, design.estimation_notes]
    verification_status: reported
    access_level: appendix
    locator: AppendixB/C printed pp16–18 on indices and spillovers; F.1–F.6 pp22–30 on platform-only logistics, selected counties, natural-village sampling, household replacement, baseline imputation, price product joins and recall-period conversion. TableA.15 cells were not used because text extraction is garbled; attrition description is from F.3.
  - id: E4
    source_type: replication
    citation: Couture et al. Data and Code for Connecting the Countryside via E-Commerce, openICPSR117506V2, DOI10.3886/E117506V2.
    url: https://www.openicpsr.org/openicpsr/project/117506/version/V2/view
    date: '2021-02-18'
    supports: [empirical_requirements.treatment_source]
    verification_status: verified
    access_level: metadata
    locator: Project page and Code/Data folder listings inspected. Listings include Merge_Village_Vars.dta, survey_data_analysis.dta, retail_data_analysis.dta and processing/analysis do-files. README download redirected to login; no files, variable definitions or geographic crosswalk inspected. Metadata verifies deposit existence only.
design_applications:
  - paper: 'Connecting the Countryside via E-Commerce: Evidence from China'
    doi: 10.1257/aeri.20190382
    journal: 'American Economic Review: Insights'
    year: 2021
    research_question: Does rural e-commerce integration alter household economic outcomes and local retail markets, and who benefits?
    population: Survey households and retailers in100 selected villages across eight counties in Anhui/Henan/Guizhou;96 villages retain endline.
    outcome: Household e-commerce usage and expenditure shares, income and business activity, local continuing-product prices and store product additions.
    data_used: [Two-round bespoke household survey2015–2017, Two-round local store and product price surveys, Private platform transaction data for a separate observational extension]
    treatment_encoding: Village assigned early access for ITT, actual program opening instrumented by assigned access for TOT; do not use individual adoption as random assignment.
    comparison: Assigned treated versus control villages in the same county pools, with baseline outcome adjustment and explicit nearby-terminal spillover concern.
    empirical_design: Village-randomized ANCOVA and assignment-instrumented IV with village-clustered inference. Later12,000-village transaction event profiles and model-based welfare calculations are not additional randomized treatments.
    assumptions: [valid randomization within selected pools, nonselective outcome observation, appropriate spillover handling, IV relevance exclusion and monotonicity where invoked]
    threats_addressed: [baseline balance checks, household attrition and migration checks, nearby-terminal exposure analysis, sampling-weight sensitivity, preexisting parcel-delivery heterogeneity]
    evidence_refs: [E1, E2, E3]
method_transfer: null
readiness_blockers:
  - Conditional use requires obtaining and inspecting the deposited assignment/outcome files, field definitions and household replacement links. Their existence is verified but contents were not inspected because download requires login. Exact replication and outside-panel geographic linkage are not certified.
  - Defend the chosen ITT or IV estimand under crossover and neighboring terminal access; do not assume no interference or a universal national effect. Exact village opening dates remain implementation-level data needs, not a fabricated common date.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

The intervention targets a last-mile market-access problem. Internet connections
already existed in the villages, but commercial parcel operators often did not
serve them. The platform-government program adds warehouses, platform-specific
transport subsidies and a staffed village terminal with cash settlement [E1;
E2/E3, reported claim]. It does not build a general road network or supply first
internet access. The relevant development question concerns consumption and
market integration, not whether farming receives a production subsidy.

## What Changed

One operationally selected village is offered early program access while another
eligible village is held back for the survey window. This experimental ordering,
not a county's demonstration title, defines the variation [E1]. National program
scale and private transaction histories are useful context but cannot replace
the randomized sample's assignment roster.

## Implementation and Assignment

Computer assignment takes place within eight county candidate pools, with
stratification on delivery access and village characteristics [E1]. Selection
into those pools is not random. The published implementation opens in38 of60
assigned-treated villages and five of40 assigned controls; manager acceptance
helps explain noncompliance [E2, reported claim]. Preserve both columns.
Randomized assignment is not the same thing as actual opening or household use.

## Why This Creates Empirical Variation

Equation1 uses assignment for ITT and instruments actual village opening with
assignment for TOT [E2, reported claim]. The first contrast concerns the offer
of early access under the surrounding rollout. The second needs an exclusion
and monotonicity argument as well as relevance. Nearby control households can
use treated-village terminals, so own-village opening alone does not exhaust
exposure [E3, reported claim; analytical inference].

## Identification Risks

The survey is not a clean balanced household panel. Missing villages,
household replacement and extra endline inner-zone households change the
observation process. AppendixF.5 supplies village-zone baseline means for added
or replaced households; they are not observed individual baselines [E3,
reported claim]. Sampling weights and retained-household sensitivity matter.

Registered dates also matter. The archived page first registers the trial on
October6 2016, after its listed start and intervention dates [E1]. The paper's
preregistration statement should not be expanded into a claim of universal
pre-assignment specification. The registry's old completion and public-data
answers do not override the later replication deposit.

## Data Requirements

For the default household design, join the assignment roster to survey rounds
using the study village ID, then link households while preserving replacements,
zone and local survey dates. A county identifier or terminal usage indicator is
not an adequate substitute. Logical field names in the contract explain the
join; actual code variable names remain to be inspected [E1/E3; analytical
inference]. Product-price extensions additionally need outlet/product identity.

The deposit lists relevant village, survey and retail files [E4], but listing
names does not verify columns or an external geographic crosswalk. Access to
private platform transactions is not required for the default survey ITT and
is not promised by this record. Durable spending uses a three-month recall
window and nondurables a two-week window converted to monthly values [E3].

## Evidence Notes

The trial registry is primary archived evidence of the investigators' assignment
protocol, not independent proof that every opening followed it. Published body
and appendix establish the reported implementation and analysis. Registry HTML
was read directly after the web reader returned403. The replication directory
was inspected, but its README download requires login; no data were copied into
this repository [E1–E4].

## Sources

- [AEA RCT Registry1582](https://www.socialscienceregistry.org/trials/1582)
- [Published paper and appendix on the author's site](https://www.lizhiliu.com/uploads/6/0/9/8/60987819/ecommerce_cfgl.pdf)
- [Replication117506V2](https://www.openicpsr.org/openicpsr/project/117506/version/V2/view)
