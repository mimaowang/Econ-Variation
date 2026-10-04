---
schema_version: 2
id: china-1986-compulsory-education-law-cohort-enforcement
name: China's 1986 Compulsory Education Law Cohort and County-Enforcement Exposure
aliases:
- 1986 compulsory education law in China
- China compulsory schooling cohort shock
- 中国1986年义务教育法
status: grounded
provenance:
  task_id: task-e6f648e1ff1b
scope:
  country: China
  regions:
  - Chinese provinces and counties of birth
  domains:
  - education
  - human-capital
  - labor-economics
  - migration
  - regional-economics
  variation_type: cohort-rule
  knowledge_role: china-variation
  china_relevance: >
    The 1986 national law changed compulsory-schooling exposure for Chinese
    birth cohorts, while implementation was planned at the provincial level and
    managed locally by counties. The record stores the cohort–county assignment
    used in research, not a claim that local compliance was uniform.
identity:
  instrument: >
    The 1986 Compulsory Education Law of the People's Republic of China and its
    staggered provincial and county implementation. This record focuses on the
    legal exposure of school-age cohorts and local enforcement strength, not the
    separate 1990s compulsory-education promotion inspections or the 2006 law
    revision.
  authority: >
    The National People's Congress enacted the law; the State Council, provincial
    governments, and county-level governments planned and managed implementation;
    education departments and supervisory bodies carried it out.
  legal_identifiers:
  - 中华人民共和国义务教育法, adopted 1986-04-12
  - Presidential Order No. 38, effective 1986-07-01
  - Provincial implementation plans and county education-management records
  implementation_regime: >
    The law established nine-year compulsory education and assigned overall
    planning to provinces while making county governments the main managers.
    Provinces and counties differed in resources, timing, and enforcement, so
    formal enactment and actual schooling completion are separate exposures.
  assignment_mechanism: >
    Cohorts are differentially exposed according to whether the law was in force
    when they reached the relevant school-entry or middle-school age. Within a
    province, research applications use county-of-birth enforcement strength,
    often proxied by a distance-weighted measure involving the provincial capital,
    to predict completion of compulsory education. The composite is a paper-level
    instrument and must not be reduced to the national enactment date alone.
  parent: null
  related_variations: []
timeline:
  announcement: '1986-04-12'
  effective: '1986-07-01'
  implementation_start: 1986
  implementation_end: null
  local_timing: >
    Provincial plans and county implementation produced different effective
    enforcement paths. Cohort exposure depends on birth year and school-entry
    timing, while local enforcement depends on the county-of-birth implementation
    environment; exact provincial rollout dates must be sourced separately for
    designs that use them.
  anticipation: >
    The law was public before the 1986–1987 school cycle, and families or local
    authorities could adjust. Cohorts near the school-entry boundary may also be
    affected by changes in entry-age rules and supply expansion.
  last_verified: '2026-08-11'
assignment:
  unit: >
    Birth-cohort by county-of-birth cell, with individual migrants or residents
    linked to the county and province in which they were born.
  treated: >
    A person is more exposed when their school-age cohort falls after the law's
    relevant implementation threshold and their county of birth has stronger
    enforcement capacity. In the focal paper, the instrument combines cohort
    exposure intensity with a distance-weighted county enforcement measure.
  comparison_pool: >
    Older cohorts not exposed at the relevant schooling stage and cohorts or
    counties with weaker legal exposure provide the comparison, subject to
    province, cohort, and county controls. People born near county or province
    borders require special treatment because the law and enforcement are tied to
    birthplace in the application.
  rule: >
    Code the law-exposure cohort from the 1986 enactment and local rollout, then
    interact it with an audited county enforcement-strength measure. The paper's
    focal weighting uses geographic distance between the birth-county centroid
    and the provincial capital; this is a reported proxy, not a legal rule.
  intensity: >
    Cohort exposure can be binary or continuous by years of schooling covered;
    local enforcement is continuous in the distance-weighted instrument. The
    exact cohort cutoff and distance transformation are paper-specific.
  exemptions:
  - Children in areas whose conditions allowed delayed school entry
  - Cohorts already past the relevant school stage when the law took effect
  - Migrants whose birthplace, schooling location, or hukou differs from the application rule
  compliance: >
    Legal entitlement and actual completion diverged because counties differed in
    fiscal capacity, schools, teachers, and enforcement. The instrument predicts
    education completion; it does not assert full legal compliance.
  exposure_construction: >
    Merge birth year or school-entry cohort with the law's implementation timing,
    attach county-of-birth and province identifiers, and construct the paper's
    enforcement-strength weight. Keep formal law exposure, local implementation,
    and completed schooling as separate variables.
  required_identifiers:
  - birth year or school-entry cohort
  - county and province of birth
  - provincial capital and county centroid or distance measure
  - schooling completion and age at entry
  - individual or household outcome identifier
  spillovers: >
    School resources, migration, teachers, and local fiscal responses can cross
    county borders. Later migrants may be measured in a destination that differs
    from the county assigning their original exposure.
research_compatibility:
  outcome_domains:
  - years of schooling and middle-school completion
  - wages and employment
  - migrant welfare and consumption
  - health and social participation
  - intergenerational mobility
  - fertility and labor supply
  affected_populations:
  - Chinese birth cohorts reaching primary or middle-school age around the reform
  - Rural residents and internal migrants
  - Counties and provincial education systems
  mechanism_channels:
  - compulsory-schooling completion
  - local education supply and enforcement
  - human-capital accumulation
  - migration and labor-market selection
  best_for:
  - Cohort or province-by-cohort designs for schooling and later outcomes
  - IV or MTE designs that explicitly model local enforcement heterogeneity
  - Research on migrant welfare when birthplace and cohort are observed
  not_good_for:
  - Treating the 1986 national law as a single random date
  - Using destination-city location as the assignment when the paper uses county of birth
  - Mixing the 1990s inspection/promotion program with legal cohort exposure
design:
  claim_type: causal
  affordances:
  - National legal change with cohort exposure
  - Provincial and county implementation heterogeneity
  - Individual IV and MTE applications
  - Long-run household, labor, health, and migration outcomes
  candidate_designs:
  - Province-cohort difference-in-differences
  - Cohort-boundary event study or regression discontinuity checks
  - Instrumental variables using cohort exposure weighted by local enforcement
  - MTE designs for heterogeneous returns to completed schooling
  identifying_variation: >
    The identifying contrast combines whether a birth cohort was covered by the
    law at the relevant school stage with variation in county enforcement capacity.
    In the focal application, distance-weighted county exposure predicts schooling
    completion and is used as an instrument for education.
  primary_strategy: >
    Use province and cohort controls for formal legal exposure, add county-of-birth
    enforcement strength, and estimate the first stage for schooling completion
    before interpreting IV or MTE outcomes. Do not call the distance proxy itself
    a law or assume it is exogenous without diagnostics.
  estimand: >
    Depending on the application, the local average or marginal effect of an
    additional year or completion of compulsory education for individuals whose
    schooling responds to the law–enforcement instrument.
  treatment_variable: >
    Completed compulsory schooling instrumented by cohort legal exposure interacted
    with an audited county enforcement-strength measure; reduced-form designs may
    use the cohort–county exposure directly.
  comparison_logic: >
    Compare adjacent or nearby cohorts across provinces or counties while checking
    pre-trends, entry-age discontinuities, baseline education resources, and
    birthplace versus destination selection.
  estimation_notes: >
    The focal 2026 China Economic Review application reports an MTE framework and
    a distance-weighted instrument using the 2017 China Migrants Dynamic Survey.
    Those estimates and the exact first-stage construction remain paper-reported.
  assumptions:
  - Cohort exposure is not confounded by other cohort-specific shocks at the law boundary
  - Conditional on controls, county enforcement strength is not a direct determinant of the outcome except through schooling
  - Birthplace and cohort are measured consistently and are not selectively reported
  - Migration and school-entry timing do not invalidate the intended exposure link
  - The first stage is strong enough for the chosen IV or MTE estimand
  diagnostics:
  - Plot cohort-specific pre-trends and placebo law dates
  - Test alternative school-entry and middle-school cutoffs
  - Compare distance weights with fiscal-capacity and provincial-rollout measures
  - Examine first-stage strength and balance by county resources
  - Separate formal law exposure, local enforcement, and completed schooling
  - Test birthplace-to-destination migration and border-county sensitivity
threats:
- type: endogenous_local_enforcement
  basis: reported
  condition: County fiscal capacity, schools, or administrative quality may affect both enforcement and later wages, health, or migration directly.
  evidence_refs:
  - E2
  possible_diagnostics:
  - County resource controls and pre-trend tests
  - Alternative enforcement proxies
  - Border and within-province comparisons
- type: cohort_boundary_and_entry_age
  basis: reported
  condition: The law changed school-entry and schooling rules near the reform, so cohort discontinuities may mix legal coverage with age or crowding effects.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Multiple cohort windows and placebo cutoffs
  - Explicit entry-age controls
  - Separate primary and middle-school exposure
- type: migration_and_birthplace_measurement
  basis: inferred
  condition: Migrants are observed away from their birth county, and birthplace or hukou errors weaken the assignment link.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Birthplace-based samples and migration controls
  - Destination-versus-birthplace sensitivity
  - County-border and missing-birthplace exclusions
- type: concurrent_education_reforms
  basis: inferred
  condition: School construction, fee, teacher, and later education reforms may coincide with legal exposure and local enforcement.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Control for education spending and school supply
  - Province-specific trends and alternative rollout dates
  - Outcomes unlikely to respond to schooling as placebo checks
- type: weak_or_heterogeneous_first_stage
  basis: reported
  condition: Legal exposure may predict schooling completion differently across gender, rural status, province, or migrant groups.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Report subgroup first stages and weak-IV robust intervals
  - Use MTE or LATE interpretation rather than a universal return
empirical_requirements:
  contract_version: 1
  population: Chinese individuals or migrants whose birth cohort and county of birth are observed
  observation_unit: Individual or birth-cohort-by-county cell
  geography_level: County and province of birth, with provincial-capital geography
  time_start: 1970
  time_end: 2017
  minimum_frequency: Annual or cross-sectional cohort data
  minimum_pre_periods: 3
  minimum_post_periods: 5
  required_fields:
  - birth year and school-entry cohort
  - county and province of birth
  - years of schooling or completion indicator
  - county enforcement or distance-weight measure
  - outcome such as wage, employment, consumption, health, or social activity
  - gender, rural background, and migration controls
  required_identifiers:
  - person_id or household_id
  - birth_county_id
  - province_id
  - birth_year
  - survey_year
  treatment_key:
  - cohort_law_exposure
  - birth_county_id
  - enforcement_strength
  treatment_source: >
    The 1986 law and provincial implementation records for formal exposure;
    county education and geography data for enforcement strength; survey or census
    microdata for schooling and outcomes. The dataset catalog and access details
    belong in Econ Data Know-How.
  measurement_risks:
  - provincial rollout dates and local enforcement are not interchangeable
  - county boundaries and birthplace identifiers change over time
  - distance to the provincial capital is an imperfect enforcement proxy
  - self-reported schooling and migration histories may be noisy
  - later reforms may be correlated with early enforcement
design_profiles: []
evidence:
- id: E1
  source_type: policy-document
  citation: 'National People''s Congress. 1986. “Compulsory Education Law of the People''s Republic of China,” adopted 1986-04-12 and effective 1986-07-01.'
  url: https://www.moe.gov.cn/jyb_sjzl/sjzl_zcfg/zcfg_jyfl/202110/t20211029_575949.html
  date: '1986-04-12'
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.announcement
  - timeline.effective
  - assignment.rule
  - assignment.compliance
  verification_status: verified
  access_level: official-document
  locator: 'Official Ministry of Education text: Articles 2, 5–8 and the enacted/effective dates; formal nine-year system and provincial planning with county management.'
- id: E2
  source_type: paper
  citation: 'Sun, Yucheng, Meizhen Li, Zhewen Pan, and Xianbo Zhou. 2026. “Who Benefits from Compulsory Education? Evidence from the Average and Heterogeneous Effects on Migrant Welfare in China.” China Economic Review 95:102559. DOI: 10.1016/j.chieco.2025.102559.'
  url: https://doi.org/10.1016/j.chieco.2025.102559
  date: 2026
  supports:
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.exposure_construction
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design_applications.treatment_encoding
  - design_applications.comparison
  - design_applications.data_used
  verification_status: reported
  access_level: abstract
  locator: 'Publisher and IDEAS/RePEc abstract and indexed introduction: 2017 CMDS, cohort exposure, county enforcement strength, distance-weighted instrument, and MTE application; full data/code not independently inspected.'
design_applications:
- paper: 'Who Benefits from Compulsory Education? Evidence from the Average and Heterogeneous Effects on Migrant Welfare in China'
  doi: 10.1016/j.chieco.2025.102559
  journal: China Economic Review
  year: 2026
  research_question: What are the average and heterogeneous welfare returns to compulsory schooling for internal migrants?
  population: Internal migrants aged 15 and older in the 2017 China Migrants Dynamic Survey
  outcome: Wages, consumption, health, and social-activity outcomes
  data_used:
  - 2017 China Migrants Dynamic Survey
  - 1986 Compulsory Education Law and provincial or county implementation information
  - Birth-county geography and provincial-capital distance measures
  treatment_encoding: >
    Cohort exposure to the 1986 law is combined with a distance-weighted measure
    of county enforcement strength and used as an instrument for compulsory-school
    completion; the exact code and first-stage files remain paper-reported.
  comparison: Older or less-exposed cohorts and counties with weaker enforcement, conditional on the paper's MTE controls and birthplace rule.
  empirical_design: MTE and instrumental-variables estimation of heterogeneous returns to schooling
  assumptions:
  - The combined law-exposure and enforcement instrument affects welfare through schooling
  - Birth cohort and county enforcement are measured consistently
  - Local enforcement does not directly determine migrant welfare after controls
  threats_addressed:
  - Heterogeneous first stages and selection on gains
  - Alternative exposure and enforcement specifications
  - Migration and county-resource sensitivity
  evidence_refs:
  - E1
  - E2
method_transfer: null
readiness_blockers:
- The exact provincial rollout table, cohort cutoff, distance transformation, and first-stage code have not been independently audited; E2 is a reported paper design.
- The law establishes administrative responsibility but does not itself prove county enforcement intensity or completed schooling; those must remain separate variables.
- The 1990s compulsory-education promotion inspection program and the 2006 law revision are outside this record and should not be folded into its treatment.
- Birthplace, migration, school-entry age, and concurrent education-supply reforms can change the estimand and require query-specific checks.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

The National People's Congress enacted the Compulsory Education Law on 12 April 1986 and set it to take effect on 1 July 1986. The law established a state-guaranteed nine-year system and placed planning with provincial governments while assigning day-to-day management to county governments [E1]. That division is why legal enactment, local enforcement, and a person's completed schooling must be kept distinct.

## What Changed

The law made primary and junior-middle education a formal entitlement and obligation, required governments to allocate resources, and created administrative responsibility for implementation. It did not cause every county to reach the same schooling level at the same time. Provincial plans, county finance, school supply, and local supervision shaped the effective exposure of different cohorts [E1; E2]. This record excludes the later promotion-inspection program and the 2006 revision.

## Implementation and Assignment

For a cohort design, exposure is determined by whether a child reached the relevant school stage after the law's effective threshold, combined with the province or county implementation path. The focal migrant application uses county of birth and a distance-weighted enforcement measure involving the provincial capital as an instrument for completed compulsory schooling [E2]. The distance proxy is not a legal rule and should not be interpreted as exogenous without diagnostics. Destination-city location does not replace the paper's birthplace assignment.

## Why This Creates Empirical Variation

The design supplies a cohort boundary and spatial implementation heterogeneity that can be linked to later schooling, labor, health, and migrant-welfare outcomes. It is useful for IV or MTE research when birth cohort, birthplace, and schooling are observed. Its identifying content comes from the cohort–county contrast and the assumptions about local enforcement, not from the national law alone [E1; E2; analytical inference].

## Identification Risks

County enforcement may reflect fiscal capacity, schools, and administrative quality that directly affect outcomes. Entry-age and cohort crowding changes can sit at the same boundary. Migration can separate birthplace assignment from observed destination, and later education reforms can correlate with early enforcement. The record therefore distinguishes formal law exposure, local enforcement, and completed schooling and preserves the paper-reported instrument as conditional rather than universal [E2; analytical inference].

## Data Requirements

A usable design needs birth year or school-entry cohort, county and province of birth, schooling completion, an audited enforcement-strength measure, and outcomes. The focal application uses the 2017 China Migrants Dynamic Survey and birth-county geography [E2]. Dataset acquisition and coverage belong in `Econ Data Know-How`; this record defines the policy exposure and joins it requires.

## Evidence Notes

E1 verifies the law's enactment, effective date, nine-year objective, and provincial/county implementation responsibilities; it does not establish actual county enforcement or a particular cohort cutoff. E2 reports the cohort–county instrument, distance weighting, sample, and MTE application; the full article, provincial rollout table, raw geography, and code have not been independently inspected. The record is grounded in the institution and legal assignment boundary, while the paper-specific enforcement proxy and reproducibility remain explicit blockers.
