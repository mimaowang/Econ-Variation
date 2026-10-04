---
schema_version: 2
id: china-2020-2022-city-lockdown-truck-flow-exposure
name: China City-Scale COVID Lockdowns and Intercity Truck-Flow Exposure, April 2020–January 2022
aliases:
- China city lockdown truck flow
- Chen Chen Liu Luo Song lockdown
- 城市封控 城际货运
status: grounded
provenance:
  task_id: task-6a7b9047cfe3
scope:
  country: China
  regions:
  - Mainland prefecture-level cities in the paper's 315-city sample, excluding Tibet and Xinjiang
  domains:
  - urban
  - regional-economics
  - trade
  - transport
  - public-health
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    Locally timed Chinese city and district COVID controls changed exposure of
    mainland city pairs to mobility and freight restrictions. The study uses
    monthly truck flows to evaluate this episode-specific exposure, not a
    universal effect of all pandemic restrictions.
identity:
  instrument: >
    Full-scale city/main-urban-district lockdown episodes and partial
    county/district lockdown episodes identified by Chen et al. from local
    announcements after the Wuhan first wave. Community-only controls are a
    lower category and are not the main treatment.
  authority: >
    Local epidemic prevention and control authorities imposed and lifted
    restrictions; central community-control guidance supplied a framework.
    The inspected Xi'an government-hosted announcement confirms one full-scale
    example beginning 2021-12-23, not every episode in the paper's table.
  legal_identifiers:
  - Xi'an epidemic-control announcement effective 2021-12-23 00:00
  implementation_regime: >
    Locally activated, temporary restrictions with different geographic scales
    and durations. The paper codes full city/main-urban-district, county/district,
    and community-only controls separately. Local outbreak response and policy
    exposure are linked, so assignment is not random.
  assignment_mechanism: >
    An unordered city pair becomes exposed in a month if either endpoint has a
    full-scale lockdown; otherwise it is partially exposed if either endpoint
    has a county/district lockdown. The paper also uses the fraction of days in
    the month under each measure. This is endpoint exposure, not proof that
    every road on the route was directly closed.
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 2020
  implementation_end: 2022
  local_timing: >
    The paper's event sample runs April 2020 through January 2022. Appendix
    Tables A1–A2 give dates for 16 full-scale and 22 partial episodes across
    34 cities. The authors infer six ending dates from clearance timing or the
    sample boundary; these must not be presented as independently verified
    lifting announcements. The Xi'an government-hosted notice confirms a
    2021-12-23 start, while the paper codes Xi'an through 2022-01-15.
  anticipation: >
    Outbreaks and announcements may change behavior before formal restrictions.
    The paper inspects pre-event truck-flow trends, but no-anticipation remains
    an assumption rather than an institutional fact.
  last_verified: '2026-10-02'
assignment:
  unit: Unordered pair of mainland prefecture-level cities by month
  treated: >
    A pair-month with full-scale lockdown at either endpoint; if neither has
    full-scale lockdown, a pair-month with partial lockdown at either endpoint
    enters the separate partial category.
  comparison_pool: >
    City pairs with neither endpoint under full-scale nor partial lockdown in
    the same month, in the study's event and normal windows. Community-only
    restrictions are included in the main comparison pool and checked
    separately, so controls are not literally restriction-free.
  rule: >
    Assign the paper's daily full/partial episode dates to city endpoints;
    aggregate to monthly pair indicators in full-before-partial order. For a
    duration design, use the share of days of type-k exposure in that month.
    Do not substitute case counts, provincial emergency status, or the 2020
    Wuhan lockdown for this post-first-wave episode list.
  intensity: Full or partial category and fraction of month exposed
  exemptions:
  - Community-only controls are outside the main full/partial treatment
  - Tibet and Xinjiang cities are outside the paper's 315-city truck-flow sample
  compliance: >
    Official announcements establish formal measures; actual movement and
    enforcement can vary. The paper observes truck counts, not individual
    compliance, freight volumes, or all routes within cities.
  exposure_construction: >
    Join episode city identifiers and daily start/end dates to both endpoints
    of a monthly truck-flow pair. Full-scale overrides partial when both occur.
    A recorded end date with an asterisk in Appendix A1/A2 is imputed, not an
    official lifting date. Route-specific 2019 truck flows supply weights in
    the paper's baseline analysis.
  required_identifiers:
  - city_id_i and city_id_j
  - year_month
  - episode city, geographic scale, start date, end date, and imputed-end flag
  spillovers: >
    Freight can reroute through other cities. The paper's structural exercise
    explicitly models network spillovers; the reduced-form endpoint comparison
    by itself does not identify the national GDP effect.
research_compatibility:
  outcome_domains:
  - intercity freight movement
  - market access and supply-chain disruption
  - city economic activity under temporary mobility controls
  affected_populations:
  - city pairs with measured long-haul truck flows
  - firms and residents linked to affected city trade networks
  mechanism_channels:
  - restricted travel and loading or unloading
  - interruption of intercity trade links
  - network rerouting and general-equilibrium propagation
  best_for:
  - Monthly intercity-flow outcomes with both endpoint identifiers
  - Distinguishing full-city from subcity restriction exposure
  not_good_for:
  - Treating every COVID case or community control as a full-city lockdown
  - Using the paper's truck-flow coefficient as a model-free GDP effect
  - Annual analyses that cannot recover episode duration or contemporaneous outbreaks
design:
  claim_type: causal
  affordances:
  - Repeated, temporary city-month shocks with different intensities
  - City-pair endpoint exposure and within-pair monthly outcomes
  - Event-time inspection around non-absorbing restrictions
  candidate_designs:
  - City-pair event study
  - City-pair and month fixed-effects exposure regression
  identifying_variation: >
    Different city endpoints enter full or partial restrictions at different
    months after local outbreaks. The paper compares changes in truck flows on
    exposed pairs with changes on non-exposed pairs in the same month, after
    controlling for pair and time factors; this is conditional variation, not
    a randomized policy assignment.
  primary_strategy: >
    The author's reduced form uses pair fixed effects, month effects,
    pair-specific time trends, 2019-flow weights, and event-study checks.
    It reports case-count controls and checks alternative treatment-effect
    estimators because episodes are staggered and non-absorbing.
  estimand: >
    Conditional monthly effect of full or partial endpoint lockdown on measured
    truck flow of covered city pairs. The paper's real-income and national
    counterfactual statements additionally require its gravity/Armington model.
  treatment_variable: >
    Pair-month full-lockdown indicator, otherwise partial-lockdown indicator;
    alternative exposure is proportion of that month under each type.
  comparison_logic: >
    Compare covered pairs involving a locked-down endpoint with covered pairs
    involving no full or partial locked-down endpoint in the same month;
    interpret community-only controls, spillovers, and outbreak severity as
    limits on the contrast.
  estimation_notes: >
    The paper's 54% one-month truck-flow reduction is an author estimate after
    controlling for cases, not a verified institutional magnitude. The model
    maps truck flows to real income under additional assumptions. The full
    author manuscript was inspected; final publisher typesetting was not.
  assumptions:
  - Absent lockdown, exposed and comparison pair flows would follow comparable trends after stated controls
  - Local outbreaks and fear-driven responses do not fully explain the estimated policy contrast after case controls
  - Spillovers into comparison routes do not erase the intended reduced-form contrast
  - Episode dates, category, and observed pair flows are measured sufficiently well
  diagnostics:
  - Event-study pretrends and post-event persistence
  - Control for city-month case counts and test community-only periods
  - Exclude nearby, major trading-partner, and route-intersecting pairs from controls
  - Recheck six imputed episode endings and full-versus-partial categorization
threats:
- type: outbreak-policy-confounding
  basis: documented
  condition: Local case severity drives restrictions and can independently reduce mobility through fear or voluntary prevention.
  evidence_refs: [E1]
  possible_diagnostics: [condition on cases, inspect pretrends, compare different policy scales]
- type: network-spillovers
  basis: documented
  condition: Rerouting and trade-link effects can contaminate untreated pairs, while the structural GDP translation depends on model assumptions.
  evidence_refs: [E1]
  possible_diagnostics: [exclude connected controls, model intercity network, distinguish reduced form from structural counterfactual]
- type: episode-date-measurement
  basis: documented
  condition: Six paper-listed lockdown ends are inferred rather than independently announced; a citywide start need not imply a uniform citywide lifting date.
  evidence_refs: [E1, E2]
  possible_diagnostics: [verify original local notices, vary imputed end dates, use day-share exposure]
empirical_requirements:
  contract_version: 1
  population: Mainland city pairs represented in the paper's long-haul truck-flow provider panel
  observation_unit: City-pair-month
  geography_level: Prefecture-level city pair
  time_start: 2019
  time_end: 2022
  minimum_frequency: monthly
  minimum_pre_periods: 2
  minimum_post_periods: 1
  required_fields:
  - monthly pair truck-flow count or another pair-level economic outcome
  - city full/partial lockdown start and end dates
  - local COVID case counts
  - baseline pair flow and month
  required_identifiers: [city_id_i, city_id_j, year_month]
  treatment_key: [city_id_i, city_id_j, year_month]
  treatment_source: >
    Chen et al. Appendix A1–A2 episode list, constructed from local official
    announcements; independently inspect local notices for a new application.
    The paper's proprietary GPS provider underlies the truck-flow outcomes.
  measurement_risks:
  - Six ending dates are imputed by the authors
  - Measured routes cover about 60% of potential pairs and favor nearer, richer cities
  - GPS truck counts are not observed freight value or city GDP
  - Full and partial administrative categories simplify heterogeneous enforcement
evidence:
- id: E1
  source_type: paper
  citation: 'Chen, Jingjing, Wei Chen, Ernest Liu, Jie Luo, and Zheng Song. 2025. "The economic cost of locking down like China: Evidence from city-to-city truck flows." Journal of Urban Economics 145:103729. Author-hosted manuscript dated 2024-11-12. DOI 10.1016/j.jue.2024.103729.'
  url: https://ernestliu.scholar.princeton.edu/sites/g/files/toruqf4426/files/ernestliu/files/covid_truck_web.pdf
  date: 2024
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.exposure_construction
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_source
  - design_applications.treatment_encoding
  verification_status: verified
  access_level: full-text
  locator: '57-page author manuscript, §§2.1–2.4 pp.6–12; §3 pp.12–17; Appendix A.1 Tables A1–A2 pp.37–38, including asterisked imputed endings; inspected 2026-10-02.'
- id: E2
  source_type: implementation-document
  citation: 'Xi’an High-tech Industrial Development Zone government portal. 2021-12-22. 最新！西安全市小区（村）单位封闭管理！每户2天1人外出采购物资.'
  url: https://xdz.xa.gov.cn/ztzl/gdzt/xgyqfk/yqfk/61c32ad4f8fd1c0bdc76e8ea.html
  date: 2021
  supports:
  - identity.authority
  - identity.implementation_regime
  - timeline.local_timing
  - assignment.compliance
  verification_status: verified
  access_level: official-document
  locator: 'Government-hosted Xi’an announcement text: citywide residential/unit closed management and effective 2021-12-23 00:00; ending to be announced separately. Inspected full page 2026-10-02; supports this one city start, not all events or the paper-coded end.'
- id: E4
  source_type: paper
  citation: 'Elsevier. 2025. Publisher DOI metadata for Chen et al., Journal of Urban Economics 145:103729.'
  url: https://doi.org/10.1016/j.jue.2024.103729
  date: 2025
  supports: [design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: 'Published JUE title, journal, year and DOI; substantive methods from E1, not metadata.'
design_applications:
- paper: 'The economic cost of locking down like China: Evidence from city-to-city truck flows'
  doi: 10.1016/j.jue.2024.103729
  journal: Journal of Urban Economics
  year: 2025
  research_question: How do temporary Chinese city lockdowns change intercity truck flows and model-implied network-wide real income?
  population: 315 mainland prefecture-level cities, excluding Tibet and Xinjiang, with 2019–2022 truck-flow coverage
  outcome: Monthly change in covered city-pair truck counts; model-implied real income is a separate structural outcome
  data_used:
  - Proprietary GPS records covering 1.8 million long-haul trucks, city-pair monthly flows
  - Local government lockdown announcements and COVID case counts
  treatment_encoding: Full-scale endpoint-city lockdown, otherwise partial endpoint-city lockdown, with monthly day-share alternatives
  comparison: Same-month city pairs without full or partial lockdown at either endpoint, conditional on pair and time effects
  empirical_design: Pair-month event study and weighted fixed-effects regression, followed by an Armington trade-network model
  assumptions:
  - Conditional parallel trends and no anticipatory truck-flow changes
  - Case controls and design checks sufficiently separate policy from outbreak responses
  - Structural real-income mapping follows the specified gravity-model assumptions
  threats_addressed: [outbreak severity and voluntary behavior, network spillovers, heterogeneous temporary treatment, imputed episode endings]
  evidence_refs: [E1, E2, E4]
method_transfer: null
readiness_blockers:
- The 38 episode dates are the paper's Appendix A1–A2 coding, not a fully independently audited collection of local notices; six ending dates are explicitly imputed.
- The Xi’an government-hosted text verifies one start, but not its paper-coded end or other cities; the exact policy scale and lifting should be rechecked for any city-specific reuse.
- The underlying truck GPS data are provider-derived and do not measure freight value; the open replication deposit was identified but not unpacked.
- The published 2025 article metadata were verified, while detailed methods were read from the 2024 author manuscript; the final publisher PDF was not compared line by line.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

China's post-first-wave COVID controls were activated locally after outbreaks, rather than on one national adoption date. The paper distinguishes controls confined to communities, controls affecting counties or districts, and controls extending across a city or its main urban district [E1, reported claim]. Xi'an's government-hosted announcement is a concrete example: citywide residential and workplace closed management began at 00:00 on 23 December 2021, with a later lifting date to be announced [E2, verified]. It does not independently validate every episode in the paper's list.

## What Changed

The relevant variation is the timing, geographic scale, and duration of these local measures from April 2020 to January 2022. The authors list 16 full-scale and 22 partial episodes across 34 cities; six endpoints are inferred rather than taken from a lifting announcement [E1, reported claim]. Thus an asterisked appendix date is a research coding decision, not a verified government effective date.

## Implementation and Assignment

The paper pairs each city's restriction dates with monthly flows between two cities. If either endpoint has a full-scale lockdown, the pair takes the full category. If neither is full but either is partially locked, the pair takes the partial category. The authors also count the share of days exposed during a month [E1, reported claim]. This hierarchy avoids silently merging a district measure with a whole-city closure. Community-only periods remain in the main comparison pool, which means the contrast is between stronger and weaker or absent restrictions, not necessarily policy versus no policy.

## Why This Creates Empirical Variation

Because city episodes occur at different times, truck flows on an affected route can be compared with other routes in the same month and with its own prior flow. The paper controls for pair and time effects and examines pretrends. Its truck-flow estimate is a reduced-form result. The much larger or smaller national-income consequences depend on a trade-network model, so the two quantities must not be conflated [E1, reported design].

## Identification Risks

Outbreaks trigger restrictions and can themselves suppress movement. Case controls and event-study plots help but cannot make the local policy randomly assigned. Freight can also reroute onto nominally untreated city pairs. The paper reports checks excluding nearby, major-partner, and route-intersecting controls; a reuse should inspect whether those diagnostics still work for its outcome. Ending-date imputation and uneven GPS-pair coverage add measurement limits [E1, reported claim; analytical inference].

## Data Requirements

A usable reconstruction needs a city-by-day event table with geographic scale and date provenance, a stable city crosswalk, monthly city-pair outcomes, baseline route weights or a defensible alternative, and local case counts. The paper's Appendix supplies a starting event inventory, not a fully verified public administrative panel. Its truck counts are not direct freight tonnage or GDP [E1, reported claim].

## Evidence Notes

This record is grounded only for the paper-defined episode exposure and a verified Xi'an example. It does not certify all 38 local orders or every lifting date. Research use should preserve the paper-reported versus officially verified distinction and avoid describing the restrictions as automatically exogenous.
