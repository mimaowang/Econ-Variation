---
schema_version: 2
id: china-broadband-china-pilot-city-designation
name: Broadband China Pilot City Designation and City-Level Digital-Infrastructure Exposure (2014–2016)
aliases:
- Broadband China demonstration city program
- 宽带中国示范城市
- Broadband China Pilot City Program
status: grounded
provenance:
  task_id: task-5ff1722ba693
scope:
  country: China
  regions:
  - Designated cities, city clusters, county-level cities, districts, and autonomous prefectures in the 2014–2016 annual lists
  domains:
  - regional-economics
  - urban-economics
  - digital-infrastructure
  - innovation
  - entrepreneurship
  - economic-growth
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: This is a Chinese central-government demonstration designation that changes the policy and infrastructure environment of named Chinese localities.
identity:
  instrument: '[E3–E5, verified] Annual designation of Broadband China demonstration cities/city clusters in 2014, 2015, and 2016 under the Broadband China strategy. This record is the designation exposure, not the national trend in broadband subscriptions or the paper''s historical/topographical IVs.'
  authority: '[E2, verified] The State Council issued the Broadband China Strategy and Implementation Plan (Guofa [2013] No. 31). [E6, verified] MIIT and NDRC jointly ran the demonstration-city process and announced the annual list after review.'
  legal_identifiers:
  - 国发〔2013〕31号 (Broadband China Strategy and Implementation Plan)
  - 工信厅联通〔2014〕5号 (launch notice for creating Broadband China demonstration cities/city clusters)
  - MIIT/NDRC Announcement No. 61 of 2014
  - MIIT/NDRC 2015 and 2016 annual demonstration-city lists
  implementation_regime: '[E2, verified] The 2013 strategy treats broadband as strategic public infrastructure and sets national access, penetration, network-capacity, and application goals. [E3–E5, verified] Three annual cohorts of 39 named entities were designated in 2014–2016; the paper reports that designation brought a three-year construction period and administrative support, but the exact local implementation bundle varies by locality.'
  assignment_mechanism: '[E6, verified] Cities/city clusters applied; provincial communication authorities pre-reviewed submissions; MIIT/NDRC expert review and field checks determined the annual list. [E1, reported claim] Applicants had to satisfy at least four of six pre-specified broadband/mobile-infrastructure thresholds. Designation timing is therefore policy-selected rather than randomized.'
  parent: null
  related_variations: []
timeline:
  announcement: '2013-08-01'
  effective: '2013-08-01'
  implementation_start: 2014
  implementation_end: 2016
  local_timing: '[E3, verified] 39 entities were announced on 2014-09-26; [E4, verified] the 2015 list contains 39 entities; [E5, verified] 39 entities were announced on 2016-07-22. [E1, reported claim] Cai and Wu code a city as treated from its first designation year through 2019.'
  anticipation: '[E6, verified] Application, provincial pre-review, expert review, and field checks precede designation. [E1, reported claim] Cities meeting technical criteria earlier could apply and coordinate with central ministries sooner, so leads and policy preparation are material threats to an event-study interpretation.'
  last_verified: '2026-10-04'
assignment:
  unit: '[E1, reported claim] City-year in the paper''s 2007–2019 mechanism panel; the official lists include some city clusters, districts, county-level cities, and autonomous prefectures that require a stated crosswalk before use as prefecture-city treatment.'
  treated: '[E1, reported claim] A locality first named in the 2014, 2015, or 2016 annual Broadband China list, coded one from its cohort year onward in the paper''s city-year mechanism analyses.'
  comparison_pool: '[E1, reported claim] Never-designated cities in the paper''s panel are the comparison group for event-study and Callaway–Sant''Anna estimates; other treated cohorts are handled by group-time rather than naively serving as untreated controls.'
  rule: '[E3–E6, verified] The annual official lists define the designation. [E1, reported claim] The paper maps cohort year G in {0, 2014, 2015, 2016} to its city panel, with 0 for never-designated cities.'
  intensity: '[E1, reported claim] Primary exposure is binary first-designation status by year. The paper also uses an ordered participation measure (2014=3, 2015=2, 2016=1, never=0) for firm digital-adoption analysis; it is not a verified measure of implementation effort.'
  exemptions:
  - Localities not on any annual list during the application window
  - Entities whose official geographic type cannot be defensibly crosswalked to the intended city panel
  - National broadband expansion outside the demonstration designation
  compliance: '[E3–E6, verified] Designation records selection, not completed network construction or household take-up. [E1, reported claim] The paper tests post-designation broadband-penetration growth, but this should not be read as proof of identical local compliance.'
  exposure_construction: '[E3–E5, verified] Compile the three annual official lists, preserve entity type and announcement year, and crosswalk each entity to stable empirical city identifiers. [E1, reported claim] In the paper''s application set D_it=1 from first designation onward; retain city and year fixed effects and cohort timing rather than replacing the list with a national post-2013 dummy.'
  required_identifiers:
  - official list entity name
  - designation cohort year
  - entity type (city, city cluster, district, county-level city, or autonomous prefecture)
  - stable prefecture/city identifier and documented crosswalk
  - calendar year
  spillovers: '[E2, verified] The strategy is nationwide, while the program is intended to create demonstration effects. Neighboring, cluster-member, and never-designated cities can therefore receive broadband or knowledge spillovers; no-interference is not automatic.'
research_compatibility:
  outcome_domains:
  - broadband penetration
  - GDP per capita growth
  - innovation
  - entrepreneurship
  - firm digital adoption
  affected_populations:
  - local households and organizations using broadband
  - city firms and prospective entrepreneurs
  - patenting entities
  - local governments and telecom operators
  mechanism_channels:
  - digital-infrastructure availability and adoption
  - administrative facilitation of base-station sites and land acquisition
  - innovation and entrepreneurship
  - firm digital technology adoption
  best_for:
  - City-level studies of a designated digital-infrastructure policy environment
  - Innovation, entrepreneurial entry, and digital-adoption outcomes with a verified cohort crosswalk
  - Studies that explicitly model selection, anticipation, and spatial spillovers
  not_good_for:
  - Treating the national Broadband China strategy as a city-level experiment
  - Inferring engineering-level speed or household take-up solely from designation
  - Using a prefecture-city panel without resolving city clusters, districts, and county-level-list entries
design:
  claim_type: causal
  affordances:
  - three designation cohorts (2014, 2015, 2016)
  - city-year event study and cohort-time ATT estimators
  - official annual lists and paper-reported city-level outcomes
  candidate_designs:
  - staggered difference-in-differences with never-designated comparison cities
  - Callaway-Sant'Anna group-time ATT with covariates
  - event study around first designation
  identifying_variation: '[E1, reported claim] Variation comes from the first designation year across cities, contrasted to never-designated cities conditional on city fixed effects, year fixed effects, observed covariates, and pre-treatment trends. It is not random assignment because qualification and application select places with prior broadband conditions.'
  primary_strategy: '[E1, reported claim] The paper reports an event study, conventional TWFE, and Callaway–Sant''Anna group-time ATT. G=0 denotes never designated; G=2014/2015/2016 denotes first cohort. The paper''s mechanism outcomes use 2007–2019 city-year data.'
  estimand: '[E1, reported claim] Conditional average effect of first Broadband China designation for designated city cohorts on city-level innovation, entrepreneurial activity, broadband-penetration growth, and GDP-per-capita growth, under the stated parallel-trends and limited-spillover assumptions.'
  treatment_variable: '[E1, reported claim] D_it=1 if city i has been designated by year t; event-time indicators are relative to first designation. A separate ordered cohort variable is used only for reported firm digital-adoption analysis.'
  comparison_logic: '[E1, reported claim] Compare each cohort''s post-designation outcomes with never-designated cities and its own pre-designation outcomes; use group-time ATT methods to avoid relying only on TWFE weights in staggered adoption.'
  estimation_notes: '[E1, verified] Table7 uses growth in granted invention patents per100 residents; Table8 uses growth in newly registered firms per100 residents with registered capital below RMB2million. Table7 and Table9 conditional panels list pre-treatment saving-rate growth, human-capital growth and log GDP per capita; Table8 lists pre-treatment population growth, saving rate and human capital. Section6.1 instead describes physical-capital level, human-capital level and population growth for Eqs8-9. Preserve this specification distinction and unresolved prose/table difference; exact transformations and baseline-year coding need replication code. City-clustered bootstrap standard errors accompany the group-time ATT tables.'
  assumptions:
  - conditional parallel trends between each treated cohort and never-designated cities after stated controls
  - application eligibility, review, and timing do not leave unmodeled differential outcome trends
  - the official-list crosswalk aligns treatment entities to outcome geography without material aggregation error
  - interference from nationwide broadband expansion and neighboring demonstration effects is limited or modeled
  diagnostics:
  - inspect event-time leads relative to the omitted year before first designation
  - use group-time ATT estimates in addition to TWFE
  - reproduce placebo assignments holding 39 designations per annual cohort
  - test sensitivity to entity-type crosswalk choices and to excluding city clusters/districts
  - check first-stage effects on broadband penetration separately from outcome effects
threats:
  - type: selected-application-and-timing
    basis: documented
    condition: '[E6, verified] Designation followed application, provincial pre-review, expert evaluation, and field checks. [E1, reported claim] Formal eligibility is based on observable pre-existing broadband/mobile thresholds. Earlier selection can therefore reflect development, administrative capacity, or pre-trends.'
    evidence_refs:
    - E1
    - E6
    possible_diagnostics:
    - event-study lead coefficients
    - conditional group-time ATT with pre-treatment covariates
    - compare eligible applicants and non-applicants if application records are recovered
  - type: treatment-mapping-error
    basis: documented
    condition: '[E3–E5, verified] Official lists mix cities, city clusters, districts, county-level cities, and autonomous prefectures, while the paper reports a city panel. A naive name match can change treatment assignment.'
    evidence_refs:
    - E1
    - E3
    - E4
    - E5
    possible_diagnostics:
    - retain entity type and a reproducible crosswalk
    - rerun after excluding non-prefecture entities
  - type: concurrent-national-digital-policy-and-spillovers
    basis: inferred
    condition: '[E2, verified] The strategy applies nationally and aims at broad infrastructure expansion; demonstration effects can change non-designated and neighboring cities. Designation effects should not be interpreted as the aggregate national broadband effect.'
    evidence_refs:
    - E2
    possible_diagnostics:
    - model neighboring and cluster exposure
    - compare to other contemporaneous digital-policy designations
    - use outcome-specific pre-trends
empirical_requirements:
  contract_version: 1
  population: '[E1, verified] Chinese city-year innovation observations in the 2007–2019 mechanism analysis, after a documented crosswalk from annual pilot-list entities to the city panel. This default is the Table7 conditional application; other outcomes use separate design profiles, not a union of every paper dataset.'
  observation_unit: City-year
  geography_level: City, with explicit handling of listed city clusters, districts, county-level cities, and autonomous prefectures
  time_start: 2007
  time_end: 2019
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 1
  required_fields:
  - city identifier
  - year
  - official Broadband China designation cohort
  - entity-type crosswalk
  - granted invention patents
  - resident population
  - pre-treatment saving-rate growth
  - pre-treatment human-capital growth
  - pre-treatment log GDP per capita
  required_identifiers:
  - stable city code
  - designation-list entity name and cohort year
  - year
  treatment_key:
  - stable city code
  - first-designation year
  - post-first-designation indicator
  treatment_source: '[E3–E5, verified] Annual MIIT/NDRC designation lists. [E1, reported claim] Paper outcome sources include China City Statistical Yearbooks/CEIC, CNIPA city-year granted invention patents, and manually collected firm-registration information; these must be joined only after the official entity crosswalk is audited.'
  measurement_risks:
  - designation is not a direct measure of completed network capacity or individual adoption
  - official list geography does not uniformly equal a prefecture-city boundary
  - broadband subscriber ratios can exceed 100 percent because organization and multiple subscriptions are counted
  - manually assembled city-year firm registrations require reproducible retrieval and classification rules
  - body Eqs8-9 and Tables7-9 describe different controls; exact baseline years, growth transformations and zero handling are not verified without replication code
design_profiles:
- id: city-innovation
  label: City invention-patent growth (Table7 conditional panel)
  design_families: [difference-in-differences, event-study]
  when_to_use: '[E1, verified] Use for city invention-patent growth under the Table7 conditional specification. Firm registrations and subscriber data are not mandatory inputs to this outcome regression; crosswalk and control coding still need audit.'
  outcome_domains: [Innovation, Granted invention patent growth]
  requirements:
    population: Mainland city-year observations with patent outcomes and audited pilot-list geography
    observation_unit: City-year
    geography_level: City
    time_start: 2007
    time_end: 2019
    minimum_frequency: annual
    minimum_pre_periods: 2
    minimum_post_periods: 1
    required_fields: [city identifier, year, official Broadband China designation cohort, entity-type crosswalk, granted invention patents, resident population, pre-treatment saving-rate growth, pre-treatment human-capital growth, pre-treatment log GDP per capita]
    required_identifiers: [stable city code, designation-list entity name and cohort year, year]
    treatment_key: [stable city code, first-designation year, post-first-designation indicator]
- id: city-small-firm-entry
  label: City small-firm entry growth (Table8 conditional panel)
  design_families: [difference-in-differences, event-study]
  when_to_use: '[E1, verified] Use for growth of new registrations per100 residents with registered capital below RMB2million. A city aggregate must preserve the threshold and historical registration clock; patent and broadband-subscriber files are not mandatory for this regression.'
  outcome_domains: [Entrepreneurship, Small-firm entry growth]
  requirements:
    population: Mainland city-year observations with threshold-consistent firm-entry counts and audited pilot-list geography
    observation_unit: City-year
    geography_level: City
    time_start: 2007
    time_end: 2019
    minimum_frequency: annual
    minimum_pre_periods: 2
    minimum_post_periods: 1
    required_fields: [city identifier, year, official Broadband China designation cohort, entity-type crosswalk, newly registered firms with registered capital below RMB2million, resident population, pre-treatment population growth, pre-treatment saving rate, pre-treatment human capital]
    required_identifiers: [stable city code, designation-list entity name and cohort year, year]
    treatment_key: [stable city code, first-designation year, post-first-designation indicator]
- id: city-gdp-growth
  label: City GDP-per-capita growth (Table9 PanelB)
  design_families: [difference-in-differences, event-study]
  when_to_use: '[E1, verified] Use for the designation effect on city GDP-per-capita growth in Table9 PanelB, not the separate historical/topographical IV. Patents, firm registrations and broadband subscribers are not mandatory inputs to this regression.'
  outcome_domains: [Economic growth, GDP per capita growth]
  requirements:
    population: Mainland city-year observations with comparable GDP-per-capita outcomes and audited pilot-list geography
    observation_unit: City-year
    geography_level: City
    time_start: 2007
    time_end: 2019
    minimum_frequency: annual
    minimum_pre_periods: 2
    minimum_post_periods: 1
    required_fields: [city identifier, year, official Broadband China designation cohort, entity-type crosswalk, real GDP per capita, pre-treatment saving-rate growth, pre-treatment human-capital growth, pre-treatment log GDP per capita]
    required_identifiers: [stable city code, designation-list entity name and cohort year, year]
    treatment_key: [stable city code, first-designation year, post-first-designation indicator]
- id: city-broadband-growth
  label: City broadband-penetration growth (Table9 PanelA)
  design_families: [difference-in-differences, event-study]
  when_to_use: '[E1, verified] Use for the designation effect on subscriber-based penetration growth in Table9 PanelA. This is an adoption/availability check, not proof that the effect on another outcome is causal, nor a requirement to collect patents or firm-entry data.'
  outcome_domains: [Broadband penetration growth]
  requirements:
    population: Mainland city-year observations with subscriber-based penetration measures and audited pilot-list geography
    observation_unit: City-year
    geography_level: City
    time_start: 2007
    time_end: 2019
    minimum_frequency: annual
    minimum_pre_periods: 2
    minimum_post_periods: 1
    required_fields: [city identifier, year, official Broadband China designation cohort, entity-type crosswalk, broadband subscribers, resident population, pre-treatment saving-rate growth, pre-treatment human-capital growth, pre-treatment log GDP per capita]
    required_identifiers: [stable city code, designation-list entity name and cohort year, year]
    treatment_key: [stable city code, first-designation year, post-first-designation indicator]
evidence:
  - id: E1
    source_type: paper
    citation: 'Cai, Mengyuan, and Guiying Laura Wu. 2026. "Identifying the Growth Effect of Internet Penetration." Regional Science and Urban Economics 119: 104209.'
    url: https://personal.ntu.edu.sg/guiying.wu/growth_internet.pdf
    date: 2026
    supports:
    - scope.china_relevance
    - identity.instrument
    - identity.implementation_regime
    - identity.assignment_mechanism
    - timeline.local_timing
    - timeline.anticipation
    - assignment.unit
    - assignment.treated
    - assignment.comparison_pool
    - assignment.rule
    - assignment.intensity
    - assignment.compliance
    - assignment.exposure_construction
    - design.identifying_variation
    - design.primary_strategy
    - design.estimand
    - design.treatment_variable
    - design.comparison_logic
    - design.estimation_notes
    - design.assumptions
    - design.diagnostics
    - empirical_requirements.population
    - empirical_requirements.observation_unit
    - empirical_requirements.time_start
    - empirical_requirements.time_end
    - empirical_requirements.required_fields
    - empirical_requirements.required_identifiers
    - empirical_requirements.treatment_key
    - empirical_requirements.treatment_source
    - empirical_requirements.measurement_risks
    - design_applications.paper
    - design_applications.doi
    - design_applications.journal
    - design_applications.year
    - design_applications.research_question
    - design_applications.population
    - design_applications.outcome
    - design_applications.data_used
    - design_applications.treatment_encoding
    - design_applications.comparison
    - design_applications.empirical_design
    - design_applications.assumptions
    - design_applications.threats_addressed
    verification_status: verified
    access_level: full-text
    locator: 'Author-hosted published version inspected: pp.4–11 (city data, subscriber measure, historical/topographical IV construction and limits); pp.13–18 (cohorts, mechanism outcomes, staggered DID and diagnostics). Re-inspected4October2026: p14 Section6.1, Eqs8-9 and footnotes11-13 (patents indexed20December2021; AiQiCha registration collection7December2021; capital thresholds); p17 Table7 notes (patent outcome and conditional controls); p18 Table8 and Table9 notes (entry, GDP and penetration outcomes and distinct conditional controls). No replication code or baseline-year/transformation implementation inspected.'
  - id: E2
    source_type: policy-document
    citation: 'State Council. 2013. "Broadband China Strategy and Implementation Plan" (Guofa [2013] No. 31).'
    url: https://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/201401/t20140106_161881.html
    date: 2013
    supports:
    - identity.authority
    - identity.legal_identifiers
    - identity.implementation_regime
    - timeline.announcement
    - timeline.effective
    - threats.condition
    verification_status: verified
    access_level: official-document
    locator: 'Official State Council notice issued 2013-08-01, identifying broadband as strategic public infrastructure and providing the 2013/2015/2020 national development targets; it does not identify the later annual demonstration-city assignment.'
  - id: E3
    source_type: policy-document
    citation: 'MIIT and NDRC. 2014. "2014 Broadband China Demonstration City (City Cluster) List," Announcement No. 61.'
    url: https://www.miit.gov.cn/ztzl/lszt/qltjkdzg/kdsfcscsq/gzdt/art/2014/art_b2f2d4385e1b43759576532409621f42.html
    date: 2014
    supports:
    - identity.instrument
    - timeline.local_timing
    - assignment.rule
    - assignment.exposure_construction
    - threats.condition
    verification_status: verified
    access_level: official-document
    locator: 'Announcement dated 2014-09-26 names 39 2014 entities and states that selection followed city application, provincial pre-review, expert review, and field checks under Gongxin Ting Liantong [2014] No. 5.'
  - id: E4
    source_type: policy-document
    citation: 'MIIT and NDRC. 2015. "2015 Broadband China Demonstration City (City Cluster) List."'
    url: https://wap.miit.gov.cn/cms_files/filemanager/oldfile/miit/n973401/n1234279/n1234452/n1234453/c4376770/part/4376771.pdf
    date: 2015
    supports:
    - identity.instrument
    - timeline.local_timing
    - assignment.rule
    - assignment.exposure_construction
    - threats.condition
    verification_status: verified
    access_level: official-document
    locator: 'Official MIIT PDF list of 39 2015 demonstration entities, including cities and municipal districts; it establishes the cohort roster, not subsequent construction completion.'
  - id: E5
    source_type: policy-document
    citation: 'MIIT and NDRC. 2016. "2016 Broadband China Demonstration City List," Announcement No. 40.'
    url: https://www.cac.gov.cn/2016-07/26/c_1119279053.htm
    date: 2016
    supports:
    - identity.instrument
    - timeline.local_timing
    - assignment.rule
    - assignment.exposure_construction
    - threats.condition
    verification_status: verified
    access_level: official-document
    locator: 'Officially republished MIIT/NDRC announcement dated 2016-07-22 names 39 2016 cities and notes application, provincial pre-review, and expert comprehensive review.'
  - id: E6
    source_type: implementation-document
    citation: 'MIIT and NDRC. 2014. "Notice Launching Creation of Broadband China Demonstration Cities (City Clusters)" (Gongxin Ting Liantong [2014] No. 5).'
    url: https://www.miit.gov.cn/ztzl/lszt/qltjkdzg/kdsfcscsq/gzdt/art/2014/art_3ba95bb672e34dea901df87e411e34c3.html
    date: 2014
    supports:
    - identity.authority
    - identity.assignment_mechanism
    - timeline.anticipation
    - threats.condition
    verification_status: verified
    access_level: official-document
    locator: 'The launch notice says MIIT/NDRC jointly conduct the program; Article 11 provides for expert review and field checks after applications and before the annual list. It establishes a selected administrative process, not random assignment.'
  - id: E7
    source_type: paper
    citation: 'Cai, Mengyuan, and Guiying Laura Wu. 2026. "Identifying the Growth Effect of Internet Penetration." DOI identifier.'
    url: https://doi.org/10.1016/j.regsciurbeco.2026.104209
    date: 2026
    supports:
    - design_applications.doi
    verification_status: reported
    access_level: metadata
    locator: 'Canonical DOI for the published Regional Science and Urban Economics article; substantive claims are supported by the inspected author-hosted article [E1].'
design_applications:
  - paper: 'Identifying the Growth Effect of Internet Penetration'
    doi: 10.1016/j.regsciurbeco.2026.104209
    journal: Regional Science and Urban Economics
    year: 2026
    research_question: '[E1, verified] Whether broadband penetration raises city GDP-per-capita growth, and whether the Broadband China Pilot City Program increases innovation and entrepreneurship as mechanisms.'
    population: '[E1, verified] Chinese prefecture-city data, with a 2007–2019 city-year mechanism panel and a documented but not independently reconstructed mapping of official pilot entities to that panel.'
    outcome: '[E1, verified] Broadband-penetration growth, GDP-per-capita growth, growth of granted invention patents per100 residents (Table7), growth of newly registered firms per100 residents with registered capital below RMB2million (Table8), and a separate firm digital-adoption analysis.'
    data_used:
    - '[E1, verified] China City Statistical Yearbooks and CEIC city data; broadband subscriber series reported by three major telecom operators.'
    - '[E1, verified] CNIPA granted invention patents indexed by city-year on20December2021; city-year establishment and registered-capital information manually collected from AiQiCha on7December2021, using a main threshold below RMB2million and a robustness threshold below RMB0.5million. These are source-described historical collections, not verified present-day reproducible downloads.'
    - '[E1, verified] OpenCelliD base-station data as a physical availability robustness measure; this is not interchangeable with the Table9 subscriber-based penetration outcome.'
    treatment_encoding: '[E1, verified] For the designation mechanism, D_it switches on at the city''s first 2014/2015/2016 designation, with event-time indicators and G in {0,2014,2015,2016}. The paper''s main broadband-growth IV is a separate construction and is not this record''s treatment.'
    comparison: '[E1, verified] Never-designated cities versus each first-designated cohort before and after designation; group-time ATT complements TWFE.'
    empirical_design: '[E1, verified] Event study, TWFE, and Callaway–Sant''Anna staggered DID for designation mechanisms; separate 2SLS estimates use historical telephone and topographical RDLS interactions to instrument broadband-penetration growth.'
    assumptions:
    - conditional parallel trends for designated and never-designated cities
    - no unmodeled selection-related outcome trends after controls and leads
    - limited or modeled spillovers from nationwide broadband expansion and neighboring pilot cities
    threats_addressed:
    - staggered-TWFE weighting through group-time ATT estimates
    - spurious cohort timing through event-study leads and 1,000 placebo reassignments
    - broadband-measure error through base-station availability and alternative source checks
    evidence_refs:
    - E1
    - E7
method_transfer: null
readiness_blockers:
- The canonical object is the selected pilot-city designation, not the separate historical/topographical IV construction. A later, separately scoped record would be required to serve that IV design directly.
- The three official lists are preserved as sources, but a machine-readable entity-to-prefecture crosswalk and the paper's exact analytic-city roster have not been independently reconstructed.
- The paper's data are publicly described but the authors' full replication package and the original city application dossiers were not inspected.
- Section6.1 and Tables7-9 use different control descriptions; the profiles follow the named conditional table panels, but exact baseline-year choices, growth/zero handling and implemented covariate definitions require replication-code inspection.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

[E2, verified] The State Council's 2013 Broadband China strategy made broadband a strategic public infrastructure and set national access, penetration, capacity, and application targets. The later demonstration program is not the entire strategy. It is a selected local implementation channel inside a nationwide expansion, so a researcher must distinguish a city's designation from the countrywide trend in subscriptions or from later rural universal-service programs.

## What Changed

[E6, verified] MIIT and NDRC launched the process for creating demonstration cities and city clusters in 2014. [E3–E5, verified] They then announced three annual cohorts of 39 entities. Designation supplied a policy environment intended to accelerate construction and application, but the designation is not itself an observation of built fibre, speed, or household use.

## Implementation and Assignment

The official process is selected: local governments apply, provincial authorities pre-review, and MIIT/NDRC organize expert review and field checks. [E1, reported claim] Formal eligibility uses technical broadband and mobile-infrastructure thresholds, and the paper explicitly notes that timing may remain related to wider development characteristics. The useful encoding is therefore an official-list cohort matched carefully to a city panel, not an assertion that all Chinese cities were randomly assigned after 2013.

## Why This Creates Empirical Variation

[E1, verified] Cai and Wu use first designation in 2014, 2015, or 2016 to construct event-time indicators and group-time treatment effects. Their city-year mechanism outcomes are invention-patent growth and small-firm entry, with broadband-penetration and GDP-per-capita growth as cross-validation outcomes. This policy design is distinct from the paper's main historical/topographical IV for broadband penetration; combining them would obscure the source of variation and the assumptions each requires.

## Identification Risks

The primary threat is selection: technical readiness, local capacity, and an active application process can predict future innovation or entrepreneurship. [E1, verified] The paper reports event studies, conventional TWFE, Callaway–Sant'Anna estimates, and placebo reassignments, but these are diagnostics conditional on parallel trends, not proof that assignment was random. A second threat is geographic mapping: the lists contain city clusters, districts, county-level cities, and autonomous prefectures, whereas many outcomes are prefecture-city aggregates. Nationwide expansion and cross-city demonstration spillovers further weaken a simple treated-versus-untreated interpretation.

## Data Requirements

A usable application starts from the three official lists and records the entity type before matching to a stable city code. The common bridge is city, year, first-designation cohort and an audited entity-type crosswalk. Do not turn the three lists'117 named entities into117 prefecture-city treatments by assumption: the paper reports117 treated cities out of241, but that analytic crosswalk has not been independently reconstructed.

[E1, verified] Choose the outcome application before asking for data. Table7 needs granted invention patents and resident population to construct per100-resident patent growth. Table8 needs new registrations below RMB2million in capital and population to construct the growth of that per100-resident entry measure, not total firm stock or all entrants. Table9 PanelB uses GDP-per-capita growth; PanelA separately uses subscriber-based penetration growth. The default contract and the innovation profile describe Table7; the other profiles describe the named alternatives. Patent, registry and subscriber data are not jointly mandatory for every idea. These are source-used specifications, not a certification that an arbitrary firm-level or current-period outcome inherits the design.

The conditional controls also differ: Table7 and Table9 notes list pre-treatment saving-rate growth, human-capital growth and log GDP per capita, while Table8 lists population growth, saving rate and human capital. Section6.1 describes capital levels and population growth for Eqs8-9. The profiles retain the table-specific descriptions rather than silently resolving this difference. Exact baseline years, transformations and zero handling remain a code-recovery gap. Two pre-periods and one post-period are only the matcher's recall floor; they do not reproduce the full2007–2019 panel or certify parallel trends. Preserve the existing selection, anticipation and spillover assessment for every profile.

[E1, verified] The patent indexing and AiQiCha registration collection were dated20December2021 and7December2021 respectively. A contemporary registry query can differ through later deletions, capital changes or surviving-firm coverage, so the historical snapshot and threshold definition matter. This repository records those research requirements; data access and reconstruction belong in the complementary data knowledge base via the paper DOI. Subscriber counts can exceed100 percent because organization and multiple subscriptions enter the measure; they are not a household-coverage percentage.

## Evidence Notes

E2 establishes the national strategy; E3–E6 establish the selected annual designation process and rosters. E1 is a publicly accessible author-hosted published version that establishes the paper's empirical applications, coding, data descriptions, and diagnostics. None of these sources independently reconstructs the authors' analytic-city crosswalk or local construction completion. The record is therefore grounded for the policy and paper application, not design-documented for every possible city-level use.
