---
schema_version: 2
id: china-natural-gas-pipeline-city-proximity-rollout
name: China Natural-Gas Pipeline Rollout and City-Proximity Exposure
aliases:
- 西气东输及主要天然气管道分段投产 城市距离暴露
- Lai Lin Shen Zhou gas infrastructure mortality
status: grounded
provenance:
  task_id: task-8c1b0627bdbd
scope:
  country: China
  regions: [Mainland China along major gas transmission pipelines]
  domains: [urban, regional-economics, energy, environment, health, infrastructure, development]
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: Major pipeline openings change gas availability near Chinese cities; the recorded application links this exposure to mainland mortality and household gas use.
identity:
  instrument: Staged commissioning of major natural-gas transmission pipelines, represented by city-centroid proximity and the nearest pipeline's operating quarter.
  authority: Central energy authorities and pipeline operators; CNPC documents individual West-East pipeline segments and branches.
  legal_identifiers:
  - CNPC West-East pipeline facilities disclosure,2016 archive
  implementation_regime: Physical expansion of long-distance transmission infrastructure; trunk, branch and local distribution connections need not open together. This is not the2017 coal-to-gas mandate.
  assignment_mechanism: Geographic proximity to a commissioned pipeline changes the paper's city-level supply-access proxy at different dates. Routes and dates are not randomized.
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 2004
  implementation_end: 2015
  local_timing: The dates delimit the application, not nationwide implementation. Operator records give different dates by segment; obtain the matched segment's operating quarter rather than apply one project completion year to every city.
  anticipation: Public plans and construction can induce fuel investments or development before supply begins; examine leads and construction timing.
  last_verified: '2026-10-04'
assignment:
  unit: City supply-access cohort, inherited by constituent DSP counties; outcomes are county-quarter or city-year.
  treated: Cities within50km of their nearest included pipeline, exposed from its operating quarter; cities already exposed before2004 are excluded from the application.
  comparison_pool: Different commissioning cohorts within the near-pipeline sample; the paper's CS check uses not-yet-treated units. Cities50-200km away are a separate placebo sample, not the baseline untreated pool.
  rule: Match each city's centroid to the nearest pipeline geometry and its commissioning quarter, then join constituent counties. Retain the distance restriction and pre2004 exclusion; this coding is a paper-defined proxy, not statutory household eligibility.
  intensity: Baseline supply-access event; distance bands are sample definitions, not measured household consumption doses.
  exemptions:
  - Exclude cities with pipeline operation before2004 in the recorded application
  - The farther50-200km band is reserved for the placebo application
  compliance: A functioning transmission segment does not prove a specific household's local connection or fuel switching. Measure realized gas use separately.
  exposure_construction: Compute centroid-to-pipeline distance using a consistent coordinate system; attach the closest segment's year-quarter; merge county-to-city membership and calendar period. Audit multiple nearby lines, administrative changes and partially commissioned projects.
  required_identifiers: [city_id, county_id, pipeline_segment_id, commissioning_year_quarter, calendar_year_quarter, city_centroid_coordinates]
  spillovers: Connected networks and local distribution can transmit supply beyond the distance band; migration and industrial responses can affect other jurisdictions.
research_compatibility:
  outcome_domains: [mortality, household energy use, air pollution, regional development]
  affected_populations: [Residents of near-pipeline mainland cities, DSP county populations]
  mechanism_channels: [fuel availability, household fuel substitution, industrial energy substitution]
  best_for:
  - Conditional event studies of infrastructure access with dated pipeline GIS and geographic outcome panels
  - Outcomes observable before and after multiple commissioning cohorts
  not_good_for:
  - Treating proximity as an observed household connection
  - Isolating indoor pollution or household fuel use without additional mechanism evidence
  - A common nationwide opening-date design
design:
  claim_type: reduced-form
  affordances: [Geographic exposure proxy with staggered commissioning]
  candidate_designs: [Cohort-aware event study, Group-time DID with not-yet-treated controls]
  identifying_variation: Nearby cities inherit different operating quarters from the matched pipeline; changes in outcomes are compared across cohorts over calendar time.
  primary_strategy: The paper reports a conventional event study with province rather than unit effects, an IW event study using its2015 reference group, and a CS robustness specification with not-yet-treated controls. Preserve the specification chosen; do not describe all as the same TWFE model.
  estimand: A conditional reduced-form effect of geographically proxied transmission access on outcomes among the selected near-pipeline population, not an effect per actual household connection or unit of indoor pollution.
  treatment_variable: Relative quarters since the closest pipeline operates for mortality; annual event time for household gas use. The pre-event period is the omitted reference in the event study.
  comparison_logic: The reusable CS comparison uses cohort-specific changes against units not yet exposed, subject to overlap and parallel trends; the remote distance band tests a placebo and is not silently substituted as a control group.
  estimation_notes: Published Tables2-8 distinguish county/time effects in post-opening summaries from the conventional full-lead event study. Mortality event time spans21 pre-opening and24 post-opening quarters, omitting minus1; gas-use event time spans minus4 through3 years. Standard errors are city-clustered and regressions population-weighted. Exact IW reference coding and supplementary implementation were not inspected in code.
  assumptions:
  - Conditional parallel trends and no anticipation for the cohorts compared
  - Commissioning does not coincide with differential unobserved development or health interventions
  - City-distance exposure and county membership measure the intended supply opportunity consistently
  - Adequate not-yet-treated comparisons remain over the chosen event horizon
  diagnostics:
  - Plot cohort-aware pre-trends and report calendar-time support
  - Reconcile segment dates against operator records and vary proximity definitions
  - Check local distribution, anticipation and concurrent development
  - Report spillovers and sensitivity to destination cities
threats:
- type: selected-routing-and-timing
  basis: reported
  condition: Central planning does not eliminate selection toward growing cities; routes and commissioning may track outcome trends.
  evidence_refs: [E1]
  possible_diagnostics: [Inspect plans and delays, Compare cohort pre-trends, Examine destination-city exclusions]
- type: transmission-versus-household-access
  basis: inferred
  condition: Centroid proximity can misclassify local distribution access and within-city heterogeneity.
  evidence_refs: [E1, E2]
  possible_diagnostics: [Validate local connection timing, Vary distance and centroid definitions]
- type: cohort-and-reference-implementation
  basis: inferred
  condition: Full-lead event-study normalization and the2015 IW reference require code reconciliation; late-period comparisons cannot be assumed available indefinitely.
  evidence_refs: [E1]
  possible_diagnostics: [Inspect cohort code and support, Use explicitly documented not-yet-treated comparisons]
- type: indirect-mechanisms-and-spillovers
  basis: inferred
  condition: Infrastructure affects households and industry; mortality responses do not alone identify an indoor-air pathway or exclude neighboring exposure.
  evidence_refs: [E1]
  possible_diagnostics: [Measure realized household fuel use, Test neighboring exposure and competing interventions]
empirical_requirements:
  contract_version: 1
  population: Residents of70 mainland DSP counties within the near-pipeline city sample; the source surveillance universe contains161 counties.
  observation_unit: county-quarter
  geography_level: county with city membership and city-centroid pipeline exposure
  time_start: 2004
  time_end: 2015
  minimum_frequency: quarterly
  minimum_pre_periods: 2
  minimum_post_periods: 1
  required_fields:
  - Age-adjusted mortality or deaths and age-specific population denominators
  - Cause and sex categories when studying heterogeneous mortality
  - Pipeline geometry and operational quarter
  - City centroid and county-to-city crosswalk
  - Weather and baseline economic conditions for the chosen specification
  required_identifiers: [county_id, city_id, pipeline_segment_id, year, quarter]
  treatment_key: [city_id, year, quarter]
  treatment_source: ARARP proprietary pipeline map and quarterly operating dates reported by the paper; operator disclosures permit segment checks but do not reproduce the full licensed geometry.
  measurement_risks:
  - DSP access requires authorization; the application uses the older161-county surveillance universe
  - GIS licensing and commissioning-date vintage must match the study window
  - City-centroid distance is not county or household connection distance
  - Two pre-periods are a minimum data-fit screen, not a sufficient parallel-trends assessment
design_profiles:
- id: annual-household-gas
  label: City-year household natural-gas usage
  design_families: [event-study, difference-in-differences]
  when_to_use: Aggregate energy-use outcomes from China City Construction Yearbook, without importing confidential mortality requirements. Licensed pipeline GIS and annual commissioning coding still need reconciliation; consumption combines adoption and intensity.
  requirements:
    population: Mainland near-pipeline cities
    observation_unit: city-year
    geography_level: city
    time_start: 2005
    time_end: 2015
    minimum_frequency: annual
    minimum_pre_periods: 2
    minimum_post_periods: 1
    required_fields: [Residential gas volume, Population denominator, Pipeline geometry and operating dates, City centroid, Chosen controls]
    required_identifiers: [city_id, pipeline_segment_id, year]
    treatment_key: [city_id, year]
evidence:
- id: E1
  source_type: paper
  citation: 'Lai, Wangyang, Liguo Lin, Xiaochi Shen and Maigeng Zhou.2025. Investing in a transition fuel: The remarkable decline in mortality from China''s rollout of natural gas infrastructure. JEEM130:103131. DOI10.1016/j.jeem.2025.103131.'
  url: https://ccap.pku.edu.cn/docs/2025-12/0146c871f45b4455bac15c8620359d3f.pdf
  date: 2025
  supports: [identity.instrument, identity.assignment_mechanism, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.exposure_construction, design.primary_strategy, design.comparison_logic, design.estimation_notes, empirical_requirements.required_fields, empirical_requirements.treatment_source, design_applications.treatment_encoding, design_applications.data_used]
  verification_status: verified
  access_level: full-text
  locator: 'Final18-page paper: Sections2-4 printedpp3-6; Section6 pp9-10 and Table8 p13; data/code availability p17. Methods p6 visually inspected; separate appendix and code not inspected.'
- id: E2
  source_type: implementation-document
  citation: 'CNPC. West-East pipeline company facilities disclosure,2016 archive: 西气东输管道公司油气管网设施基本情况表.'
  url: https://www.cnpc.com.cn/cnpc/yqgwssslqy/201611/a0df4f9533924fec959ce4c1184fdd13/files/f525a30993cd4319993b85d13a56c714.pdf
  date: 2016
  supports: [identity.instrument, identity.authority, identity.implementation_regime, timeline.local_timing, assignment.rule]
  verification_status: verified
  access_level: official-document
  locator: 'Single-page table inspected as text: West-I east trunk2003/10/1; West-II east trunk2010/11/10, Huangpi-Guangzhou2011/6/20 and Nanchang-Shanghai2012/7/6. Does not verify the paper GIS. Later direct retrieval403; no visual table inspection claimed.'
- id: E3
  source_type: official-data
  citation: 'NDRC Economic Operations Regulation Bureau.2016-04-26. 西气东输成全球惠及人口最多的输气工程.'
  url: https://www.ndrc.gov.cn/xwdt/ztzl/trqyfdd/2015trq/201604/t20160426_1189978.html
  date: 2016
  supports: [identity.implementation_regime, timeline.local_timing, assignment.spillovers]
  verification_status: verified
  access_level: official-document
  locator: 'Main paragraph: West-I2004, West-II2012 and West-III2015 project-level milestones; connections through Zhongwei. Project milestones are not local segment or household opening dates.'
- id: E4
  source_type: scholarship
  citation: 'Economic Daily, hosted by NEA.2012-10-12. 西气东输工程建设步伐加快.'
  url: https://www.nea.gov.cn/2012-10/12/c_131902354.htm
  date: 2012
  supports: [timeline.local_timing, identity.implementation_regime]
  verification_status: reported
  access_level: full-text
  locator: 'Main paragraph distinguishes2003 trial operation,2004 Shanghai supply and2004 full commercial operation. Agency-hosted news is not treated as the underlying operating dataset.'
- id: E5
  source_type: paper
  citation: 'Lai, Lin, Shen and Zhou.2025. JEEM130:103131, publication metadata and abstract.'
  url: https://doi.org/10.1016/j.jeem.2025.103131
  date: 2025
  supports: [design_applications.paper, design_applications.journal, design_applications.year, design_applications.research_question]
  verification_status: verified
  access_level: abstract
  locator: 'Publisher abstract and bibliographic header for PII S0095069625000154; agrees with the institutional final PDF first page. Publisher full methods were not retrieved through this route.'
design_applications:
- paper: 'Investing in a transition fuel: The remarkable decline in mortality from China''s rollout of natural gas infrastructure'
  doi: 10.1016/j.jeem.2025.103131
  journal: Journal of Environmental Economics and Management
  year: 2025
  research_question: Health and household energy responses to new transmission access
  population: Mainland sample of96 near-pipeline cities for city-level analysis and70 constituent DSP counties for mortality; full retained mortality panel has2661 county-quarter observations.
  outcome: Age-adjusted quarterly mortality and annual household gas usage
  data_used: [Confidential DSP mortality, Proprietary ARARP pipeline GIS and dates, China City Construction Yearbook household gas and population, Meteorological station weather]
  treatment_encoding: City-centroid distance and nearest pipeline commissioning date; county exposure inherited from city; exclude pre2004 access.
  comparison: Cohort-based temporal contrasts; CS not-yet-treated robustness; remote band tested separately as placebo.
  empirical_design: Event studies and cohort-aware DID robustness, with city-clustered inference and population weights.
  assumptions: [Conditional parallel trends, No confounded commissioning shocks, Reliable proxy for supply availability]
  threats_addressed: [Pre-trends, Remote-distance placebo, Alternative controls, CS estimator, Coastal-destination exclusions]
  evidence_refs: [E1, E5]
method_transfer: null
readiness_blockers:
- Obtain licensed geometry and dated segment access, plus authorized outcomes or an appropriate accessible alternative, before estimation.
- Reconcile annual event coding, IW2015 reference and sample support against supplementary materials or code; availability was promised but no inspectable repository was located in this pass.
- Validate local supply access and concurrent development for the new outcome; central planning is not an exogeneity certificate.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Transmission expansion makes distant gas resources accessible to downstream regions, but a trunk is not a household distribution connection. The operator's facilities table records different commissioning dates for trunks and branches, while the NDRC describes an interconnected network [E2,E3]. Treat this as infrastructure supply access, not a legal mandate to replace a household's fuel.

## What Changed

Previously unavailable segments became operational. Local exposure depends on the relevant segment and distribution network, not the date the entire national project was declared complete [E2,E3]. The application predates the2017 clean-heating campaign and remains a separate empirical object [E1].

## Implementation and Assignment

The research assignment is a geographic proxy: map a city centroid to its closest pipeline, attach that line's operating quarter, and let counties inherit city exposure [E1]. Do not attach the full project's completion year to every branch or interpret the50km restriction as statutory eligibility [E1,E2]. Observed gas consumption is an outcome or uptake measure, not the primitive assignment.

## Why This Creates Empirical Variation

Different operating dates create before/after contrasts across locations. The documented CS robustness comparison supplies not-yet-treated controls; the farther band is a placebo [E1]. Conditional parallel trends still require a substantive argument. The record preserves the conventional and IW specifications without certifying the uninspected reference-cohort code.

## Identification Risks

Routing, sequencing and local distribution can track development; population responses or network spillovers can contaminate comparisons [analytical inference]. A reduced-form access effect cannot be called an isolated indoor-pollution effect. The absence of a comprehensive indoor-air panel is acknowledged in the paper's mechanism discussion [E1, reported claim].

## Data Requirements

Preserve segment IDs, dates, geometry, city centroids and historical county membership. Join outcomes at their actual frequency rather than averaging away commissioning timing. The quarterly mortality and annual energy-use profiles are alternatives, not a union of mandatory datasets. DSP authorization and pipeline-map licensing are explicit source restrictions [E1, data/code availability].

## Evidence Notes

The [institution-hosted final paper](https://ccap.pku.edu.cn/docs/2025-12/0146c871f45b4455bac15c8620359d3f.pdf) was inspected, not merely its abstract. Appendix/code retrieval remains unresolved: publisher access failed and a Harvard Dataverse search endpoint returned403; neither proves materials absent. CNPC table text supports selected segment checks, not a complete city assignment dataset. Its Changlv branch row has the impossible date2004/6/31; do not silently repair it if using that branch. NDRC reports West-III2015 while the paper describes2016; do not backfill that project into the baseline's explicitly listed network without route/version reconciliation [E1,E2,E3]. No restricted data or source PDF is redistributed.
