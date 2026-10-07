---
schema_version: 2
id: china-xin-county-antipoverty-relocation-participation
name: Xin County anti-poverty relocation participation in 2016–2017
aliases: [新县易地扶贫搬迁, Xin County APRP household relocation, Across a few prohibitive miles]
status: grounded
provenance:
  task_id: task-1e8b26c1b578
scope:
  country: China
  regions: [Xin County, Xinyang, Henan, mainland China]
  domains: [development, poverty, regional-economics, urbanization, migration, structural-transformation]
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: The published JDE application studies mainland registered-poor households moving from remote villages to nearby towns or county centers. The exposure is actual household participation and relocation in Xin County, not nationwide eligibility or an agricultural-production intervention.
identity:
  instrument: Household participation in Xin County's 2016–2017 Anti-Poverty Relocation Program under the Thirteenth Five-Year targeted-poverty-alleviation regime.
  authority: National coordination and provincial responsibility, with city/county implementation; the paper reports village screening and final approval by the county Leading Group Office of Poverty Alleviation and Development.
  legal_identifiers: [“十三五”时期易地扶贫搬迁工作方案（five-department announcement dated2015-12-08）, 全国“十三五”易地扶贫搬迁规划（国家发展改革委，2016年9月）]
  implementation_regime: Registered-poor households voluntarily apply and undergo administrative review, then relocate through public housing or a housing voucher. This record is restricted to the Xin County implementation observed in2016 and2017; it does not pool the2001 pilot, other counties' rules or later follow-up assistance.
  assignment_mechanism: Household eligibility, voluntary application and administrative approval determine participation; actual relocation year activates measured exposure. Housing modality is a selected choice within that participation mechanism. Apartment lotteries among participating households do not randomize program enrollment.
  parent: null
  related_variations: [china-8-7-poverty-county-threshold]
timeline:
  announcement: 2015-12-08 (national five-department announcement; not a Xin County household enrollment date)
  effective: null
  implementation_start: 2016
  implementation_end: 2017
  local_timing: The county fiscal report verifies relocation implementation in2016. The paper reports691 registered-poor participant households moving in2016 and1174 in2017; its treatment clock is each household's actual move year. The national plan covers2016–2020 and does not supply these household dates. No exact county legal effective date or public household roster was inspected.
  anticipation: Applications, approval, destination information and housing construction precede the move. Income or work responses can begin before measured relocation; do not treat the national announcement or approval date as the observed move without separate records.
  last_verified: '2026-10-07'
assignment:
  unit: Registered-poor household, linked across annual observations; individual outcomes require an additional person-to-household join.
  treated: Registered-poor households in Xin County that actually relocate through the program in2016 or2017; the published body reports1865 participating households. Nonpoor accompanying movers are excluded from the research sample.
  comparison_pool: Registered-poor households in the same county that do not participate, subject to observed pretreatment balancing. The paper also reports a separate early-mover versus waiting-participant check, not a substitute randomized comparison.
  rule: National policy targets registered-poor residents of inhospitable or poorly connected areas, respects voluntary participation and delegates eligibility review to local implementers. The paper reports self-application, village committee screening, a public list and review, and final county approval; approved households may still decline. For the study, record ever-participation and actual move year, then activate treatment from that year onward.
  intensity: Binary participation-by-post-move indicator. Public-housing and voucher indicators describe selected modalities, not independent exogenous shocks or randomly assigned treatment doses.
  exemptions:
  - Nonpoor accompanying movers are outside the published registered-poor comparison even though they can share infrastructure.
  - A household that is eligible or approved but never moves is not treated by the paper's actual-relocation indicator.
  - The paper reports single-member households cannot use the local minimum50-square-meter public unit and use vouchers; the national plan allows other local solutions, so this is not a universal national restriction.
  compliance: Approval is not take-up. Voucher users must document a purchase or pass a construction inspection before payment, according to the paper. It could not obtain private purchase contracts and therefore could not establish actual housing expenditure. The baseline measures realized relocation rather than an offer-based intention-to-treat.
  exposure_construction: Link a stable confidential household ID to the administrative participant flag and actual relocation year t_h0; APRP_ht=ever_participant_h times I(year>=t_h0). Join annual registered-poor outcomes and retain origin village for village-level inference. Preserve annual entry and exit from the poverty register. Do not reconstruct household participation from a community coordinate, poverty-county designation or national start year.
  required_identifiers: [household_id, year, actual_relocation_year, origin_village_id, annual_poverty_register_membership]
  spillovers: Public housing is accompanied by infrastructure and nearby poverty-alleviation workshops open to poor and nonpoor workers. Nonparticipants can share jobs or market changes. This household contrast does not measure the county-wide equilibrium or the effect of moving alone without supporting services.
research_compatibility:
  outcome_domains: [household per capita income, wage income, spatial access, structural transformation, poverty reduction]
  affected_populations: [registered-poor households in Xin County, household members moving from remote villages to nearby towns]
  mechanism_channels: [lower spatial and sectoral mobility costs, access to nonfarm jobs, changes in residential amenities, housing and infrastructure assistance]
  best_for: [household-income questions about within-county relocation and development, separating realized relocation from program eligibility, evaluating spatial mobility with linked administrative household panels]
  not_good_for: [city-level national APRP treatment inferred from a2016 dummy, randomized-relocation claims based on apartment lotteries, isolating physical movement from bundled housing and job assistance, interpreting selected public-versus-voucher contrasts as random assignment, national average effects from one county]
design:
  claim_type: reduced-form
  affordances: [household moves in two cohorts, repeated registered-poor outcomes before and after moves, pretreatment covariates for observed selection adjustment]
  candidate_designs: [entropy-balanced household-panel difference-in-differences, relocation-year event study, cohort-aware comparison with untreated households]
  identifying_variation: Within Xin County, participants begin actual relocation exposure in2016 or2017 while nonparticipants remain outside the program. Voluntary application and administrative targeting create selection; timing and fixed effects do not make that selection random.
  primary_strategy: Zhang, Xie and Zheng estimate annual household-income DID using ever-participation interacted with post-actual-move, household and year fixed effects, pretreatment entropy balancing and selected covariates. Table3 clusters errors by village. Its reported within-participant phase-in robustness is secondary and remains an author argument about construction/township timing.
  estimand: A conditional ATT-type contrast for participating registered-poor households under counterfactual parallel trends and selection assumptions. The pooled staggered two-way-fixed-effect coefficient is not automatically a clean cohort-average ATT with heterogeneous effects, nor a nationwide relocation ITT.
  treatment_variable: APRP_ht=I(h ever participates in Xin County2016/2017 relocation) times I(t>=actual household relocation year).
  comparison_logic: Compare participants' household income changes with nonparticipants' changes after pretreatment balancing and household/year effects. The early-versus-waiting participant comparison uses a different risk set; already-relocated households must not silently be treated as unaffected controls.
  estimation_notes: NPADIS is an unbalanced2014–2018 panel because the registered-poor list changes annually. The body reports12616 households and45059 people in the population union; Table3 log per capita income uses58047 observations and11740 households after weights and missing covariates. Table3 selected controls are household size, woodland area, average education, Dibao recipient count, labor-force count, unhealthy-member count, under14 count and over65 count. Equation2 lists event indices -3,-2,-1,0,1,2 with -1 omitted; not every cohort has all indices in2014–2018. AppendixE.1 balancing details and E.3 robustness tables were not inspected.
  assumptions: [conditional counterfactual parallel trends, adequate common support, no differential unmeasured contemporaneous shocks, defensible treatment and register continuity, no material anticipatory outcome response in the reference period, outcome-specific interpretation of bundled assistance and spillovers]
  diagnostics: [cohort-specific pretrends and event support, balance and weight concentration, register entry exit and missing-income patterns, actual-move versus approval clock, concurrent-program exposure, cohort-aware staggered estimates, village-level dependence and spillover sensitivity]
threats:
  - type: voluntary-participation-and-mode-selection
    basis: reported
    condition: Households apply and can decline approval; destination preferences and mode choices differ. The authors explicitly identify participation selection as their main challenge. Balancing adjusts observed characteristics, not unobserved income trajectories.
    evidence_refs: [E3]
    possible_diagnostics: [pretreatment balance and overlap, event-study support, weight concentration, selection sensitivity, do not interpret apartment allocation as randomized enrollment]
  - type: bundled-assistance-and-interference
    basis: reported
    condition: Other targeted-poverty programs operate concurrently and workshops near public housing offer jobs to participants and others. The paper controls other program dummies but this does not isolate movement from all complementary assistance.
    evidence_refs: [E3]
    possible_diagnostics: [household-year program histories, distinguish total relocation-package effect from movement mechanism, spatial spillover checks, avoid controlling post-treatment mediators without stating the estimand]
  - type: dynamic-register-and-timing
    basis: reported
    condition: Annual poverty-register changes create an unbalanced panel. Construction progress and township schedules are the authors' explanation for phase-in comparability, not independently verified random timing.
    evidence_refs: [E3]
    possible_diagnostics: [cohort and register membership audit, approval and actual-move histories, attrition sensitivity, cohort-specific control risk sets]
  - type: administrative-population-definition
    basis: documented
    condition: The published paper reports7676 participating poor individuals, whereas the inspected2019 RUC report Table15 reports7583, both for1865 households. The person-count difference is not reconciled. Do not substitute either total into the other's person sample or infer individual coverage from household counts.
    evidence_refs: [E3, E4]
    possible_diagnostics: [recover roster dates and person definitions, maintain source-specific counts, verify household composition before individual analysis]
  - type: staggered-estimation-and-external-validity
    basis: inferred
    condition: Two-way fixed effects with two move cohorts can mix comparisons under heterogeneous effects. One county's selected participants and changing local labor market do not establish a nationwide average benefit.
    evidence_refs: [E3]
    possible_diagnostics: [cohort-time estimates with never-treated controls, event-support table, distinguish household from aggregate outcomes, test portability against destination labor demand]
empirical_requirements:
  contract_version: 1
  population: Registered-poor Xin County households observed in the administrative panel, including actual2016/2017 participants and nonparticipants; exclude nonpoor accompanying movers.
  observation_unit: household-year
  geography_level: household origin village within Xin County, Henan
  time_start: 2014
  time_end: 2018
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 1
  required_fields: [per_capita_income, actual_relocation_year, ever_participant, annual_poverty_register_membership, household_size, woodland_area, average_education, Dibao_recipient_count, labor_force_count, unhealthy_member_count, under14_count, over65_count, pretreatment_covariates_for_balancing, concurrent_program_exposure]
  required_identifiers: [household_id, year, origin_village_id]
  treatment_key: [household_id, actual_relocation_year, year]
  treatment_source: Authorized NPADIS household panel and Xin County relocation records, interpreted using the published body's actual-move rule. The national plan and public communities list cannot supply confidential household take-up. The paper's DOI identifies the complementary data-knowledge inquiry without redistributing a dataset here.
  measurement_risks: [annual poverty-list entry and exit, household-ID and composition changes, move versus approval dates, zero income and logarithm handling, zero entropy weights and missing covariates, uninspected balancing implementation, contemporaneous assistance, incomplete voucher destination coordinates]
evidence:
  - id: E1
    source_type: policy-document
    citation: NDRC, 全国“十三五”易地扶贫搬迁规划, September2016; government-hosted36-page PDF.
    url: https://www.gov.cn/xinwen/2016-10/31/5126509/files/86e8eb65acf44596bf21b2747aec6b48.pdf
    date: '2016-09'
    supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, assignment.rule, timeline.local_timing]
    verification_status: verified
    access_level: official-document
    locator: Cover; printed pp6–8 (PDF10–12), p11 (PDF15), p13 (PDF17), p23 (PDF27), p29 (PDF33). Registered-poor voluntary scope, local discretion, housing ceiling, national2016–2020 window and city/county review responsibility only; no Xin County household roster or lottery verification.
  - id: E2
    source_type: implementation-document
    citation: Xin County Finance Bureau, 关于新县2016年财政决算草案和2017年上半年财政预算执行情况的报告, presented2017-08-29 and published2017-09-06.
    url: https://www.hnxx.gov.cn/2017/09-06/147982.html
    date: '2017-09-06'
    supports: [identity.authority, timeline.implementation_start, timeline.local_timing]
    verification_status: verified
    access_level: official-document
    locator: Heading and I(三)3, 统筹加快城乡发展. Confirms2016 county relocation execution among pooled projects; CNY260million is the multi-project envelope, not APRP-only spending. No household dates or selection list.
  - id: E3
    source_type: paper
    citation: Li Zhang, Lunyu Xie and Xinye Zheng (2023), Across a few prohibitive miles, Journal of Development Economics160,102945; online22July2022, DOI10.1016/j.jdeveco.2022.102945.
    url: https://doi.org/10.1016/j.jdeveco.2022.102945
    date: 2023
    supports: [identity.assignment_mechanism, timeline.implementation_start, timeline.implementation_end, timeline.local_timing, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.intensity, assignment.exemptions, assignment.compliance, assignment.exposure_construction, assignment.spillovers, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.population, empirical_requirements.observation_unit, empirical_requirements.time_start, empirical_requirements.time_end, empirical_requirements.required_fields, empirical_requirements.required_identifiers, empirical_requirements.treatment_source, design_applications.data_used, design_applications.treatment_encoding, design_applications.empirical_design]
    verification_status: reported
    access_level: full-text
    locator: RUC-hosted final PDF https://ae.ruc.edu.cn/docs/2022-08/bf84e6e9712f4f72910cabbca5965855.pdf inspected in memory. Header p1; §§2.1–2.3 pp3–4; §3.1/Table2 p5; §5.1/Eq1–2 p8 (equations visually checked); Table3/notes p9; §5.1.3 and Eq3 p10; Data availability and supplement route p15. Reports local assignment and empirical methods; appendices and code not inspected.
  - id: E4
    source_type: scholarship
    citation: Xinye Zheng, 精准扶贫政策效果评估, RUC-hosted2019 report; inspected relocation discussion and Table15.
    url: https://ae.ruc.edu.cn/docs/2019-08/4632c8c5c4154e84ae03a432bc5e981a.pdf
    date: 2019
    supports: [assignment.treated, empirical_requirements.measurement_risks]
    verification_status: reported
    access_level: full-text
    locator: Printed/PDF pp80–81, 改善居住状况 and Table15. Reports1865 households,1421 concentrated and444 dispersed, but7583 people rather than the later paper's7676; no reconciliation supplied in the inspected passage.
  - id: E5
    source_type: policy-document
    citation: NDRC announcement of the five-department “十三五”时期易地扶贫搬迁工作方案, December8,2015.
    url: https://www.ndrc.gov.cn/xwdt/xwfb/201512/t20151208_955833.html
    date: '2015-12-08'
    supports: [identity.legal_identifiers, timeline.announcement, assignment.rule]
    verification_status: verified
    access_level: official-document
    locator: Entire announcement, paragraphs beginning《方案》提出/指出/强调. Verifies announcement date, voluntary registered-poor targeting and county implementation; it is an official summary, not the signed plan or a county enrollment instrument.
design_applications:
  - paper: Across a few prohibitive miles — The impact of the Anti-Poverty Relocation Program in China
    doi: 10.1016/j.jdeveco.2022.102945
    journal: Journal of Development Economics
    year: 2023
    research_question: Does within-county relocation improve registered-poor household income by reducing spatial and sectoral mobility barriers?
    population: Registered-poor Xin County households in2014–2018;1865 participating households in2016/2017, with nonpoor accompanying households excluded.
    outcome: Log household per capita income and its wage, operational, property and transfer components; this record's default contract is household income, not the separate individual labor-supply regression.
    data_used: [National Poverty Alleviation and Development Information System Xin County2014–2018 administrative panel, county relocation participation and timing records, household demographic and assistance information]
    treatment_encoding: Ever-participant times post-actual-household-relocation year, with2016 and2017 cohorts. Selected public-housing/voucher interactions in Eq3 reuse this clock and do not create separate variation records.
    comparison: Entropy-balanced registered-poor nonparticipants in the same county; separate paper-reported early versus waiting participant robustness.
    empirical_design: Household/year fixed-effect DID, selected covariates, pretreatment entropy balancing and village-clustered errors; relocation event study omits event year-1. Body inspected, balancing and phase-in appendix tables not inspected.
    assumptions: [conditional parallel trends, observed support and credible residual selection assumptions, valid household and move-year linkage, explicit anticipation and interference interpretation]
    threats_addressed: [body reports event-study leads, controls for other poverty programs and housing renovation, permutation tests and Oster sensitivity, phase-in comparison; appendix execution and tables remain uninspected and these checks do not establish random enrollment]
    evidence_refs: [E1, E2, E3]
method_transfer: null
readiness_blockers:
  - Conditional use requires authorized household data and a participant/move-year join. The authors explicitly cannot share data; public policy dates or destination maps are not substitutes.
  - Recover AppendixC/E.1 and any authorized code before exact replication of register cleaning, entropy targets and weights, zero-income handling and phase-in sample construction. The inspected body suffices to reconstruct the baseline research contrast, not every numerical implementation.
  - Defend counterfactual trends and residual participation selection for the proposed outcome. A new spatial mechanism study also needs origin/destination coordinates; the body locates only364 of444 voucher households, not complete spatial coverage.
  - Reconcile person counts and household membership before individual-level use. The default household-income contract must not silently become a person panel or a lottery-based experiment.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Relocation addressed a development barrier: poor households could live only
a short distance from towns yet remain separated from jobs and services by
terrain, transport and the cost of moving. The national framework targets
registered-poor residents of places with inadequate development conditions,
requires voluntary participation and gives local governments implementation
responsibility [E1,E5]. The policy is not a universal offer to every resident
of a poor county.

Xin County's fiscal report confirms relocation was being implemented in2016
[E2]. Zhang, Xie and Zheng study this county's2016/2017 moves using annual
administrative observations [E3,reported claim]. National implementation
lasted through2020; those national dates do not define this household case.
The poverty-county threshold in the related record is a different mechanism,
not a proxy for household participation.

## What Changed

Participating families moved to public housing or used a voucher to buy or
build a home elsewhere within the county. Public housing sites were chosen
by government; voucher users chose destinations outside their original
natural village. The paper reports CNY26000 per person for vouchers and a
local public-housing apartment lottery among households of the same size,
with disability-related first-floor priority [E3,reported claim]. These are
implementation details, not evidence of randomly assigned relocation.

The national plan sets a25-square-meter per-person ceiling and permits
local solutions for single-person households [E1]. The paper's50-square-
meter minimum public unit, which channels single-member households into
vouchers, is specific to the observed local implementation [E3,reported
claim]. Do not transfer that exception to every county.

## Implementation and Assignment

The paper describes a recoverable sequence: household application, village
screening, public review and county approval, followed by an option to
decline [E3,reported claim]. National documents support voluntary registered-
poor targeting and local review authority, but do not independently verify
every local applicant or the study's individual move dates [E1,E5]. Actual
take-up, rather than eligibility or approval alone, defines treatment.

Join the confidential household participant record to its actual move year
and annual outcomes. The treatment turns on in that year and remains on.
Keep origin village for inference and poverty-register membership for sample
continuity. Community maps cannot reveal which nonparticipant was eligible,
approved or declined [analytical inference]. Public housing and vouchers
remain selected modalities of this one participation mechanism.

## Why This Creates Empirical Variation

Households move in different years while other registered-poor households
remain outside the program. That creates observable differential exposure
within a common county setting, not random enrollment. Household fixed
effects can remove fixed differences; the causal interpretation still rests
on comparable counterfactual changes [E3,reported claim; analytical inference].

## Identification Opportunities

The published baseline compares income changes of movers and nonmovers in
the same county, using household and year fixed effects, pretreatment
entropy balancing and selected controls [E3,reported claim]. Table3 reports
village clustering. The observable contrast is sufficiently specified for
conditional idea matching: actual move-year exposure, annual household
income, registered-poor comparison and stable household/village joins.

That contrast is not a random experiment. The authors' theory expressly
allows households with greater nonfarm comparative advantage to select
into relocation. Balancing cannot remove an unmeasured change in those
households' opportunities. The phase-in check attributes move timing to
construction progress and township schedules; its appendix sample and
results have not been independently inspected [E3,reported claim]. For new
research, assess cohort-specific comparisons rather than assuming the
pooled two-way-fixed-effect coefficient is the desired ATT [analytical
inference].

## Identification Risks

Relocation combines housing, infrastructure, altered amenities and access
to workshops. Controlling other assistance is not equivalent to isolating
physical movement, and a post-move job variable can be a mediator rather
than a confounder [E3,reported claim; analytical inference]. Define the
relocation-package estimand before choosing controls. Nearby nonparticipants
may also gain from jobs or local infrastructure.

The poverty register changes each year, and application or construction can
precede the recorded move. Attrition and anticipation therefore deserve
explicit checks. A failure to reject pretrend differences is not proof of
parallel counterfactual trends [analytical inference]. The one-county sample
also limits generalization to other relocation regimes and national welfare.

## Data Requirements

The default is a household-year income design, not a requirement to acquire
every GIS layer or all individual outcomes. It needs the authorized2014–2018
administrative panel, stable household/village identifiers, actual move year,
pretreatment characteristics and concurrent-assistance histories. At least
two pre-move years and one post-move year are a matching minimum; exact
published replication uses the full available panel. The two cohorts have
different support for event indices [E3,reported claim].

The authors have no permission to share data [E3,reported claim]. Dataset
access and reconstruction belong in the companion data-knowledge project,
linked through the paper DOI. No private observations or paper PDF are
redistributed here. A spatial-access idea additionally needs origin and
destination joins; incomplete voucher coordinates cannot be silently filled
with a county centroid.

## Evidence Notes

The primary sources verify the national institution, assignment framework
and local2016 execution; the final published body establishes the reported
household research clock and comparison. The county report'sCNY260million
covers several projects and is not APRP-only spending [E2]. The2019 RUC
report and2023 paper agree on1865 households and1421/444 modalities but
report different person totals [E3,E4,reported claim]. This remains explicit
measurement uncertainty, not a reason to fabricate a reconciled count.

The body directs readers to the DOI for its supplement. AppendixC/E.1 and
phase-in TableE7 were not read, and no executable code is certified. Those
are exact-replication conditions, while the inspected baseline assignment,
timing, comparison and join contract are already recoverable. This record
is grounded and conditionally usable, not directly certified causal evidence.
