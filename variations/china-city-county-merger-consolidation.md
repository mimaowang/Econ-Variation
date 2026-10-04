---
schema_version: 2
id: china-city-county-merger-consolidation
name: China's City–County Merger and Prefecture Consolidation Regime (2011–2018)
aliases:
- City–county merger reform in China
- County-to-urban-district reform
- 撤县设区
- 市县合并
- 行政区划调整与辖区整合
status: grounded
provenance:
  task_id: task-adf5d6fc7610
scope:
  country: China
  regions:
  - Chinese prefecture-level cities and their counties and urban districts
  domains:
  - regional-economics
  - urban-economics
  - local-government
  - administrative-geography
  - labor-markets
  - migration
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    Between 2011 and 2018 many Chinese prefectures changed the jurisdictional
    relationship between an urban core and nearby counties. A county or county-level
    city could be re-categorized as an urban district (撤县设区), while the former
    district and county were simultaneously brought under a larger prefecture-level
    administration. This creates place- and year-specific exposure for studies of
    urban expansion, local public finance, market integration, migration, and labor
    outcomes, but the two institutional components must not be treated as the same
    treatment.
identity:
  instrument: >
    A staggered set of county-to-urban-district changes and city–county jurisdictional
    consolidations implemented across Chinese prefecture-level cities during the
    2011–2018 study window. The first component changes the legal category of a
    county or county-level city into a district; the second enlarges the jurisdiction
    governed through the prefecture-level city by coordinating the converted county
    with pre-existing urban districts. This record covers the reform regime as used
    in Bo and Wang (2025), not every earlier or later administrative adjustment.
  authority: >
    The State Council approves the establishment, abolition, naming, and affiliation
    changes of counties and urban districts. Provincial governments and prefecture-
    level city governments implement the approved boundary and institutional changes.
    The prefecture government becomes the relevant higher-level authority for the
    consolidated urban and county jurisdictions.
  legal_identifiers:
  - 行政区划管理条例（国务院令第704号，2018年10月10日通过，2019年1月1日起施行）
  - 国函〔2011〕57号及湖南省关于撤销望城县设立长沙市望城区的实施通知
  - 国函〔2013〕24号及南京市溧水县、高淳县撤县设区后的实施文件
  - 国函〔2014〕118号及湖北省调整十堰市部分行政区划的政府公报
  implementation_regime: >
    Approval is issued for a named administrative change, after which the province
    and prefecture implement the new district or boundary. The legal change can
    preserve transitional county-level fiscal or administrative arrangements even
    while the jurisdiction is formally a district. The empirical exposure therefore
    has at least two clocks: the legal/effective date of the named county change and
    the first year in which the prefecture is coded as having a merger. The public
    replication code uses annual cohort labels rather than a national single date.
  assignment_mechanism: >
    Local governments propose adjustments and the State Council approves them under
    urbanization, spatial-planning, fiscal, and governance considerations. Assignment
    is consequently selected and geographically structured, not randomized. In the
    source application, a prefecture is first treated in the year its coded merger
    begins; county-level files retain the converted county, the other counties in the
    treated prefecture, and the pre-existing urban districts as distinct exposure
    states.
  parent: null
  related_variations:
  - china-2014-hukou-local-implementation
timeline:
  announcement: null
  effective: null
  implementation_start: 2011
  implementation_end: 2018
  local_timing: >
    The study window is coded in annual cohorts from 2011 through 2018. The public
    replication file `figure3_maptreatment.do` assigns `countytreatyear` to named
    county/district changes in each cohort year and separately assigns
    `citytreatyear` to the first merger year of the prefecture. `figure3.do` then
    classifies county observations as (i) urban districts in treated prefectures,
    (ii) converted counties in treated prefectures, (iii) other counties in treated
    prefectures, (iv) urban districts in control prefectures, or (v) other counties
    in control prefectures. The year labels are the paper's treatment convention;
    an applied dataset should retain the underlying State Council/provincial approval
    date and any local transition date rather than silently treating the whole year
    as an exact legal onset.
  anticipation: >
    Proposed adjustments, approval negotiations, land-use planning, infrastructure
    investment, and fiscal or personnel preparation can precede the coded year.
    Transition arrangements can also delay effective integration after the legal
    change. A pre-trend window and alternative approval-versus-operation dates are
    therefore needed before interpreting a post-year coefficient.
  last_verified: '2026-10-02'
assignment:
  unit: >
    The main published treatment is prefecture-year for individuals working in a
    prefecture. County-year is the finer unit for separating converted counties,
    existing urban districts, and other counties within a treated prefecture. The
    observation unit in a labor application is individual-year nested in a
    prefecture or county, depending on the outcome file.
  treated: >
    At the prefecture level, a city is treated from its first `citytreatyear` in the
    replication coding. At the county level, a converted county/district receives
    its own `countytreatyear`; existing urban districts in the same treated prefecture
    are consolidation-exposed but are not county re-categorization units; other
    counties in that prefecture are part of the broader prefecture exposure and must
    not be mislabeled as converted counties. This distinction is central to the
    source paper's attempt to separate consolidation from re-categorization.
  comparison_pool: >
    The baseline prefecture design compares individuals in prefectures that have not
    yet experienced the coded merger, together with never-treated prefectures, before
    and after each treated prefecture's first merger year. The county appendix uses
    urban districts and counties in control prefectures as the control groups and
    reports converted counties, other counties in treated prefectures, and treated
    urban districts separately. Nearby jurisdictions can be affected by commuting,
    migration, land markets, and planning spillovers, so geography-only controls are
    not automatically clean.
  rule: >
    Construct a prefecture-by-year indicator from the first approved/implemented
    merger in the source coding, and a separate county-by-year indicator from the
    named county-to-district changes. Keep the legal change type, original county or
    county-level city, new district name, prefecture, approval date, implementation
    date, and historical administrative code as separate fields. Do not infer
    treatment from a county name containing “区”, from population growth, or from
    the existence of a modern district boundary alone.
  intensity: >
    The canonical treatment is binary and cohort-based. Useful secondary measures
    include the number of counties converted in a prefecture, the number of existing
    districts brought into the consolidation, the share of the prefecture's area or
    population newly governed through the city, and years since each legal change.
    These measures describe intensity; they do not replace the legal assignment rule.
  exemptions:
  - County or county-level-city changes outside the 2011–2018 coding window
  - Pure renamings, township changes, or boundary changes that do not create the two components above
  - Counties in a treated prefecture that were not converted, when estimating the pure re-categorization component
  - Observations without a historical county/prefecture crosswalk or a defensible treatment year
  compliance: >
    The legal category change is mandatory once approved, but the depth and speed of
    fiscal, personnel, service, and planning integration vary. A formal district
    label is therefore not the same as immediate economic or administrative
    integration. The paper's prefecture treatment should be read as an intent-to-
    expose measure for a jurisdictional consolidation package.
  exposure_construction: >
    Start with the approval and local implementation documents, build a versioned
    ledger of original and successor units, and attach both approval and effective
    dates. Join the ledger to historical county and prefecture identifiers before
    merging CMDS, CFPS, census, firm, or administrative outcomes. Reproduce the
    source code's `citytreatyear` and `countytreatyear` only after checking names
    against stable codes; the public code uses name-based regular expressions and
    is a valuable audit trail, not a substitute for the crosswalk.
  required_identifiers:
  - province code
  - prefecture-level city code
  - original county or county-level-city code
  - successor urban-district code
  - approval document number and date
  - local implementation or operation date
  - survey or administrative observation year
  - individual or firm identifier where applicable
  spillovers: >
    A larger prefecture jurisdiction can change commuting, migration, hukou or
    service access, land conversion, firm location, tax enforcement, and public
    investment beyond the converted county. Existing urban districts and other
    counties inside a treated prefecture are therefore part of the mechanism as well
    as possible comparison contamination. Neighboring prefectures may experience
    labor-market and land-market reallocation.
research_compatibility:
  outcome_domains:
  - wages and earnings
  - migrant and local labor-market outcomes
  - employment, occupation, and labor supply
  - population and migration
  - urban expansion and land use
  - fiscal capacity and tax enforcement
  - firm entry, productivity, and investment
  - public services and infrastructure
  affected_populations:
  - migrant workers
  - local and non-migrant workers
  - residents of converted counties and urban districts
  - firms and households in treated prefectures
  - neighboring jurisdictions exposed to commuting or migration spillovers
  mechanism_channels:
  - centralized prefecture governance
  - removal of county–district administrative barriers
  - coordinated infrastructure and land planning
  - tax and fiscal integration
  - local labor-demand expansion
  - migration and labor-market sorting
  best_for:
  - Prefecture-year or individual-year staggered DID with explicit treatment cohorts
  - County-level designs that separate re-categorized counties from existing districts and other counties
  - Studies of urban expansion, public finance, market integration, and labor outcomes
  - Mechanism work using commuting, tax, land, service, and investment outcomes
  not_good_for:
  - A uniform national post-2011 or post-2014 indicator
  - Treating every modern urban district as a merger-treated unit
  - Claiming a pure county-to-district effect from the prefecture-level indicator
  - Designs that cannot recover historical administrative identifiers and dates
  - Ignoring endogenous selection, transition periods, or within-prefecture spillovers
design:
  claim_type: causal
  affordances:
  - Staggered annual cohorts documented in a reproducible treatment-coding file
  - Distinct prefecture and county treatment states
  - Administrative changes that directly alter jurisdictional governance and boundaries
  - Individual labor surveys with prefecture identifiers and migrant/local status
  - County-level mechanisms for travel time, taxes, land, and urban development
  candidate_designs:
  - Prefecture-level staggered DID with prefecture and year fixed effects
  - Event study around each prefecture's first coded merger year
  - County-level design comparing converted counties with existing districts and other counties in treated prefectures
  - Triple differences by migrant/local status, county conversion status, or pre-reform urbanization
  - Modern staggered-adoption estimators robust to heterogeneous treatment effects
  identifying_variation: >
    The source paper's main contrast is within-prefecture timing: workers in a
    prefecture after its first coded merger are compared with workers in the same
    prefecture before the merger and with not-yet- or never-treated prefectures.
    County-level files add a second contrast that separates the legal
    re-categorization of counties from consolidation exposure of existing urban
    districts. The former changes a county's legal category; the latter changes the
    scope of prefecture governance. They can move together but are not interchangeable.
  primary_strategy: >
    Bo and Wang (2025) estimate staggered DID models on individual labor outcomes,
    using prefecture and year fixed effects and event-study and robustness designs.
    The replication code constructs annual `citytreatyear` and `countytreatyear`
    variables, and its county appendix classifies the five exposure groups. A
    modern staggered estimator and an explicit cohort/event-time convention should
    be preferred to an unexamined TWFE coefficient when treatment effects differ by
    cohort or component.
  estimand: >
    For the main application, the estimand is the average effect of becoming part of
    a prefecture that has undergone the coded city–county consolidation package on
    migrant and local workers' labor outcomes. A county-level re-categorization
    estimand instead compares a converted county to a defensible county/district
    counterfactual. These are different estimands; the first includes governance
    consolidation and the second isolates the legal category change only if the
    comparison and timing support that interpretation.
  treatment_variable: >
    Main: `citytreat_pt`, an indicator equal to one for a worker in prefecture p in
    year t after p's first coded merger year. Component-specific alternatives:
    `countytreatyear` for the converted county/district, and indicators for existing
    urban districts or other counties in a treated prefecture. Preserve the original
    unit type and cohort rather than collapsing all three into one binary county flag.
  comparison_logic: >
    Use not-yet-treated and never-treated prefectures for the main timing contrast,
    with prefecture and year effects and checks for pre-trends. For component work,
    compare converted counties to appropriate control counties/districts and use
    existing urban districts as consolidation-exposed but re-categorization-free
    units. Do not use other counties in treated prefectures as untreated without
    stating that this changes the estimand and risks spillover bias.
  estimation_notes: >
    The paper reports wage effects for migrants and non-migrants and uses event
    studies and robustness checks for alternative control groups and spillovers.
    The public replication package contains the programs and derived non-sensitive
    files but not the CMDS, CFPS, or Population Census microdata. Reproduction thus
    requires provider access or a separately documented secure-data workflow.
  assumptions:
  - Cohort-specific treated and comparison prefectures would have followed comparable trends absent the merger package
  - The approval and effective dates are measured consistently across historical boundaries
  - The treatment coding distinguishes re-categorization from consolidation rather than proxying only a new name
  - Migration, commuting, land, fiscal, and investment spillovers are modeled or are not fatal to the chosen comparison
  - Concurrent urbanization and infrastructure programs are controlled for or do not differentially coincide with adoption
  - The observed survey locality identifies the labor market actually exposed to the prefecture reform
  diagnostics:
  - Rebuild the legal approval ledger and compare it with the replication code's annual cohorts
  - Plot event-study leads separately for converted counties, existing districts, and other counties in treated prefectures
  - Use Callaway–Sant'Anna, Sun–Abraham, or other heterogeneous-cohort estimators
  - Test alternative effective-year conventions and exclude transition years
  - Check neighboring-prefecture, commuting, migration, and land-market spillovers
  - Control for or exclude concurrent urbanization, transport, tax, and development-zone programs
  - Audit historical code/name crosswalks before joining CMDS, CFPS, census, firm, or county panels
design_profiles:
- id: prefecture-consolidation
  label: Prefecture-level consolidation exposure
  design_families:
  - staggered-did
  - event-study
  when_to_use: >
    Use when the outcome is observed for a worker, firm, household, or prefecture
    linked to the prefecture where the first coded merger occurs. Interpret the
    effect as the consolidation package, not as a pure county reclassification.
  outcome_domains:
  - wages
  - employment
  - migration
  - firm and urban outcomes
  requirements:
    population: Workers, firms, households, or prefecture residents in Chinese prefecture-level cities
    observation_unit: Individual-year, firm-year, household-year, or prefecture-year
    geography_level: Prefecture-level city
    time_start: 2011
    time_end: 2018
    minimum_frequency: annual
    minimum_pre_periods: 3
    minimum_post_periods: 3
    required_fields:
    - outcome
    - prefecture code
    - year
    - migrant/local or relevant population status
    - citytreatyear
    required_identifiers:
    - prefecture code
    - year
    - individual, firm, or household identifier
    treatment_key:
    - prefecture code
    - citytreatyear
    - year
- id: county-reclassification
  label: County-to-urban-district re-categorization
  design_families:
  - staggered-did
  - event-study
  - county-panel
  when_to_use: >
    Use only when the original county, successor district, effective date, and a
    comparison that is not already exposed to the prefecture consolidation can be
    identified. This profile targets the legal category change and should not be
    reported as the same estimand as prefecture consolidation.
  outcome_domains:
  - county growth
  - land and urban expansion
  - public services
  - firms and pollution
  requirements:
    population: Residents, firms, or county-level outcomes in original and successor jurisdictions
    observation_unit: County-year or firm-year linked to historical county geography
    geography_level: County and prefecture
    time_start: 2011
    time_end: 2018
    minimum_frequency: annual
    minimum_pre_periods: 3
    minimum_post_periods: 3
    required_fields:
    - outcome
    - original county code
    - successor district code
    - approval date
    - effective date
    - year
    required_identifiers:
    - original county code
    - successor district code
    - prefecture code
    - year
    treatment_key:
    - original county code
    - successor district code
    - effective date
    - year
threats:
- type: endogenous-selection-and-urbanization
  basis: inferred
  condition: >
    Local governments propose or support mergers in response to urbanization,
    growth prospects, planning needs, fiscal capacity, or political objectives that
    may also predict labor and land-market outcomes.
  evidence_refs:
  - E1
  - E5
  possible_diagnostics:
  - pre-trend and placebo tests
  - baseline-growth and planning controls
  - cohort-specific estimators and alternative comparison pools
- type: bundled-reclassification-and-consolidation
  basis: reported
  condition: >
    A converted county changes legal category while the prefecture simultaneously
    gains a larger consolidated jurisdiction. Prefecture-level treatment therefore
    cannot by itself identify the pure effect of either component.
  evidence_refs:
  - E5
  - E6
  possible_diagnostics:
  - use existing urban districts as consolidation-exposed but re-categorization-free units
  - separate converted counties and other counties in treated prefectures
  - report component-specific estimands rather than one pooled label
- type: approval-transition-and-anticipation
  basis: documented
  condition: >
    The public cohort code is annual, whereas approval, local announcement,
    institutional transfer, and actual service/fiscal integration can occur in
    different months or years.
  evidence_refs:
  - E2
  - E3
  - E6
  possible_diagnostics:
  - preserve approval and effective dates separately
  - exclude transition years or use month-sensitive event time where available
  - test alternative first-treatment conventions
- type: within-prefecture-and-neighbor-spillovers
  basis: inferred
  condition: >
    Existing districts, other counties in treated prefectures, neighboring
    prefectures, migrants, commuters, firms, and land markets may respond to the
    same consolidation, contaminating simple controls.
  evidence_refs:
  - E5
  - E6
  possible_diagnostics:
  - classify the five county exposure groups explicitly
  - exclude or model neighboring and within-prefecture units
  - use commuting and migration network exposure
- type: name-based-coding-and-boundary-error
  basis: reported
  condition: >
    The public treatment program uses name-based regular expressions and the public
    package does not provide the restricted microdata or a complete legal code
    crosswalk. Historical names and successor codes can therefore be misjoined.
  evidence_refs:
  - E6
  possible_diagnostics:
  - reproduce the code and compare every row with official approval documents
  - use stable administrative codes and versioned boundary crosswalks
  - audit observations around renamings and boundary changes
empirical_requirements:
  contract_version: 1
  population: Workers, migrants, local residents, firms, households, or county/prefecture populations exposed to Chinese city–county mergers
  observation_unit: Individual-year, firm-year, household-year, county-year, or prefecture-year
  geography_level: County, urban district, prefecture-level city, and province with historical crosswalks
  time_start: 2011
  time_end: 2018
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields:
  - outcome and covariates
  - original and successor administrative unit
  - prefecture and province
  - approval and effective dates
  - annual observation year
  - treatment component and cohort
  - migrant/local or other relevant population status for labor outcomes
  required_identifiers:
  - province code
  - prefecture code
  - original county code
  - successor district code
  - individual, firm, household, or county identifier
  - year
  treatment_key:
  - historical administrative crosswalk
  - component type
  - approval/effective date
  - prefecture first-merger cohort
  - observation year
  treatment_source: >
    State Council approval and provincial implementation documents, the Bo–Wang
    paper, and its Mendeley replication package. The replication package provides
    the annual coding programs and derived files; provider-controlled CMDS, CFPS,
    and Population Census microdata and a complete machine-readable legal approval
    ledger must be obtained or rebuilt separately.
  measurement_risks:
  - annual cohort labels may not equal legal effective dates
  - county names and codes change across boundary revisions
  - formal district status may precede actual fiscal/service integration
  - prefecture treatment bundles two institutional components
  - within-prefecture and neighboring spillovers can contaminate controls
  - public replication files do not include the restricted microdata or complete legal crosswalk
evidence:
- id: E1
  source_type: policy-document
  citation: >
    State Council. 2018. 行政区划管理条例 [Regulations on the Administration of
    Administrative Divisions], State Council Order No. 704.
  url: https://www.gov.cn/zhengce/content/2018-11/01/content_5336379.htm
  date: '2018-10-10'
  supports:
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  verification_status: verified
  access_level: official-document
  locator: >
    Articles 7, 13–17: the State Council approval scope for counties and urban
    districts, required change materials, and preservation of approval records and
    administrative codes. Effective2019-01-01; this successor regulation is not
    retroactive evidence of the rules governing all2011–2018 cohorts. Original
    inspection retained; the2026-10-02 re-access returned403.
- id: E2
  source_type: implementation-document
  citation: >
    Hunan Provincial Government. 2011. 关于撤销望城县设立长沙市望城区的通知
    [Notice on abolishing Wangcheng County and establishing Changsha Wangcheng
    District], 湘政函〔2011〕167号.
  url: https://www.hunan.gov.cn/xxgk/tzgg/swszf/201212/t20121210_4862855.html
  date: '2011-06-20'
  supports:
  - identity.legal_identifiers
  - timeline.local_timing
  - assignment.treated
  - assignment.rule
  - assignment.exposure_construction
  verification_status: verified
  access_level: official-document
  locator: >
    The notice states that the State Council approved the adjustment (国函〔2011〕57号),
    abolishes Wangcheng County, establishes Changsha Wangcheng District with the
    former county boundary, and sets the implementation responsibilities.
    Re-inspected2026-10-02, items1–4 and signature: signed2011-06-20,
    posted2011-07-01; posting is not a new treatment date.
- id: E3
  source_type: implementation-document
  citation: >
    Nanjing Municipal Government Office. 2013. 市政府办公厅关于明确溧水县、高淳县撤县设区后相关政策的通知
    [Implementation policies after Lishui and Gaochun counties became districts],
    宁政办发〔2013〕26号.
  url: https://www.nanjing.gov.cn/zdgk/201303/t20130327_1055928.html
  date: '2013-03-18'
  supports:
  - identity.legal_identifiers
  - timeline.local_timing
  - assignment.rule
  - assignment.compliance
  verification_status: verified
  access_level: official-document
  locator: >
    The notice implements the provincial and State Council adjustment of Lishui and
    Gaochun and records transitional fiscal and administrative treatment after the
    formal county-to-district change.
- id: E4
  source_type: implementation-document
  citation: >
    Hubei Provincial Government Gazette. 2015. Issue 1, notice implementing the
    State Council adjustment of Shiyan's administrative divisions (国函〔2014〕118号).
  url: https://www.hubei.gov.cn/gbhis/2015/2015-01.pdf
  date: '2015-01-01'
  supports:
  - identity.legal_identifiers
  - timeline.local_timing
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: >
    Government-gazette notice referring to the State Council approval that abolished
    Yun County and established Shiyan Yunyang District; use together with the paper
    coding for the annual 2014 cohort convention.
- id: E5
  source_type: paper
  citation: >
    Bo, Shiyu, and Yi Wang. 2025. “The Labor Market Outcomes of Jurisdictional
    Consolidation: Evidence from City–County Mergers in China.” Journal of Urban
    Economics 149: 103788.
  url: https://doi.org/10.1016/j.jue.2025.103788
  date: 2025
  supports:
  - identity.instrument
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.implementation_start
  - timeline.implementation_end
  - timeline.local_timing
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - design.primary_strategy
  - design.identifying_variation
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  verification_status: reported
  access_level: full-text
  locator: >
    Publisher full text, “China's urban system,” “Data,” “Identification strategy,”
    and “Conclusions”: city–county mergers during 2011–2018, prefecture-level
    staggered DID, CMDS labor outcomes, and the distinction between county
    re-categorization and consolidation of existing urban districts.
- id: E6
  source_type: replication
  citation: >
    Bo, Shiyu, and Yi Wang. 2025. “The Labor Market Outcomes of Jurisdictional
    Consolidation: Evidence from City–county Mergers in China,” Mendeley Data,
    Version 1, DOI 10.17632/9mywh455tm.1.
  url: https://data.mendeley.com/datasets/9mywh455tm/1
  date: '2025-05-27'
  supports:
  - timeline.local_timing
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.exposure_construction
  - assignment.required_identifiers
  - design.primary_strategy
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_key
  verification_status: verified
  access_level: replication
  locator: >
    `data and code/code/figure3_maptreatment.do` contains annual county cohorts and
    prefecture first-treatment years; `figure3.do` defines the five county exposure
    groups; `tableA6.do` uses the county groups; `figure4.do` constructs event time
    from `citytreatyear`. The package readme states that CMDS, CFPS, and Population
    Census individual data must be requested from their providers.
design_applications:
- paper: 'The Labor Market Outcomes of Jurisdictional Consolidation: Evidence from City–County Mergers in China'
  doi: 10.1016/j.jue.2025.103788
  journal: Journal of Urban Economics
  year: 2025
  research_question: >
    How does jurisdictional consolidation through city–county mergers affect wages
    and labor-market outcomes of migrant and local workers?
  population: >
    Workers observed in Chinese prefectures, with the main analysis distinguishing
    migrant and non-migrant/local workers during the 2011–2018 reform window.
  outcome: >
    Individual wage income and related labor-market, composition, and mechanism
    outcomes; the source paper also examines economic growth and integration channels.
  data_used:
  - China Migrants Dynamic Survey (CMDS), provider-controlled individual data
  - China Family Panel Studies (CFPS), provider-controlled microdata for supporting analyses
  - Population Census microdata, provider-controlled
  - Public Mendeley programs and derived non-sensitive files
  treatment_encoding: >
    Prefecture-year `citytreat_pt` turns on after the prefecture's first coded merger
    year. The public code also retains county-level `countytreatyear` and the five
    county exposure groups, allowing component-specific checks.
  comparison: >
    Individuals in treated prefectures after first treatment versus the same
    prefectures before treatment and individuals in not-yet- or never-treated
    prefectures; county robustness separates converted counties, existing urban
    districts, other counties in treated prefectures, and two control groups.
  empirical_design: >
    Staggered difference-in-differences with prefecture and year fixed effects,
    event-study checks, heterogeneous-cohort robustness, and mechanism tests for
    economic growth, labor demand, and integration.
  assumptions:
  - treated and comparison prefectures have comparable untreated trends after conditioning on fixed effects and controls
  - the coded first-merger year captures the relevant exposure clock
  - migrant/local status and work prefecture are measured consistently across survey waves
  - within-prefecture and neighboring spillovers are modeled or do not overturn the chosen contrast
  threats_addressed:
  - event-study and pre-trend checks
  - alternative control groups and spillover restrictions
  - county-group decomposition of re-categorization versus consolidation
  - mechanism tests for growth, tax, travel-time, labor-demand, and composition channels
  evidence_refs:
  - E5
  - E6
readiness_blockers:
- >
  The public replication code gives the complete annual name-based treatment mapping
  used by the paper, but a machine-readable ledger linking every coded county to its
  State Council approval number, approval date, local effective date, and stable
  historical code has not been independently rebuilt in this record.
- >
  The Mendeley package contains programs and public derived files but explicitly does
  not include the CMDS, CFPS, or Population Census individual datasets. Exact sample
  joins and restricted-data identifiers therefore require provider access or a
  separately documented secure-data workflow.
- >
  The main prefecture treatment bundles county-to-urban-district re-categorization
  with consolidation of existing urban districts. A pure component estimate requires
  the county-level ledger and the five-group comparison logic; it must not be read
  from the pooled prefecture coefficient alone.
- >
  Annual treatment cohorts, local transition arrangements, and anticipated planning
  may differ from the legal approval date. Keep approval, implementation, operation,
  and analysis-year conventions separate in downstream data.
method_transfer: null
---

## Institutional Background

China's political hierarchy places prefecture-level cities above counties and urban districts. Before a merger, a county and the urban districts of the same prefecture were separate county-level jurisdictions even when they shared a labor market and transport system. The Wangcheng notice illustrates a named, approved administrative change, not a statistical reclassification [E2]. The later2019-effective regulation records a successor approval framework; it is not a retroactive legal basis or a common onset date for the2011–2018 sample [E1].

## What Changed

The reform package has two related but distinct changes. First, a named county or county-level city is abolished as a county-level unit and its former territory becomes a city district. Second, the prefecture-level city governs a larger, more integrated jurisdiction containing the new district and its pre-existing urban districts. The first is a legal-category change; the second is a change in the scope of prefecture governance. [E2; E3; E4; E5]

The distinction matters because a converted county receives both exposures, while an existing urban district in the same treated prefecture receives the consolidation exposure without being re-categorized. Other counties in the treated prefecture can be affected by the larger governance and market system without being converted. The public replication code preserves these states instead of treating “district” as a sufficient treatment label. [E6]

## Implementation and Assignment

There is no single national treatment date. The source study codes annual cohorts from 2011 through 2018. Its county program assigns named county/district changes to `countytreatyear` and separately assigns each prefecture a first `citytreatyear`; a map program then creates five exposure groups. These are paper coding conventions that must be anchored to the underlying approval and local implementation documents for a new dataset. [E5; E6]

The legal changes are selected through proposals, planning, and State Council approval. That selection can reflect urbanization, expected growth, fiscal capacity, land planning, or political objectives. The variation is therefore useful because the approval schedule creates staggered timing, not because the treated places are intrinsically comparable or randomly selected. [E1; E5]

## Why This Creates Empirical Variation

At the prefecture level, a worker's exposure changes when the worker's prefecture enters its first coded merger cohort. This supports a staggered labor-market design. At the county level, the same policy offers a sharper conceptual decomposition: the converted county/district reflects re-categorization plus consolidation, existing districts reflect consolidation without re-categorization, and other counties in the treated prefecture are broader within-prefecture exposure. A credible component analysis must retain these contrasts and state which estimand it is estimating. [E5; E6]

## Identification Risks

The main risks are endogenous selection into administrative adjustment, anticipation and transition periods, bundled treatment components, name-based coding and boundary changes, and spillovers within and across prefectures. The paper's public programs are valuable for reproducing its intended coding, but they do not replace a historical legal crosswalk or the restricted survey files. A record that reports only a modern district name or a post-year indicator loses the institutional boundary that makes the comparison interpretable. [E1; E5; E6]

## Data Requirements

The minimum contract is a versioned administrative crosswalk with original county, successor district, prefecture, approval document, approval date, effective or operation date, cohort year, and stable historical codes. Labor applications additionally need the survey year, work prefecture or county, migrant/local or hukou status, outcome, and person identifier. CMDS, CFPS, and Population Census microdata are provider-controlled; the public Mendeley package supplies programs and derived non-sensitive files, not unrestricted individual-level joins. [E5; E6]

## Evidence Notes

E1 establishes the approval authority and the requirement that administrative-division changes be documented and archived; it does not by itself establish every cohort in the paper. E2–E4 provide official examples showing that a county-to-district change names the predecessor and successor and may include transition arrangements; they do not constitute the full national ledger. E5 establishes the paper's research object, prefecture-level staggered design, and two-component interpretation; it reports the study's coding rather than independently verifying every underlying approval. E6 makes the annual treatment program and five-group logic auditable and confirms that the individual survey data remain access-controlled; it does not establish causal validity or provide a complete public legal-code crosswalk.

The owner's2026-10-02 request for 撤县设区 maps to this existing record rather than a new duplicate. The bounded audit re-inspected the Wangcheng notice and Mendeley's public package description, confirming that restricted individual data still require provider access. It did not rerun the earlier code inspection or reconstruct every cohort. The record remains conditional for a pure county-category estimate; the prefecture coefficient cannot isolate that component.
