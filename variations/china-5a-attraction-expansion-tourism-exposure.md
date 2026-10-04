---
schema_version: 2
id: china-5a-attraction-expansion-tourism-exposure
name: China's 5A Tourist-Attraction Expansion and Local Tourism Exposure
aliases:
- China national 5A tourist-attraction designation
- China 5A scenic-spot expansion
- 中国国家5A级旅游景区认定扩张
status: grounded
provenance:
  task_id: task-e6f648e1ff1b
scope:
  country: China
  regions:
  - Mainland China prefectures and counties containing nationally rated tourist attractions
  domains:
  - regional-economics
  - urban
  - tourism-economics
  - human-capital
  - economic-geography
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    The national 5A quality-rating program created dated, place-linked tourism
    expansion when an attraction in a county or prefecture first received the
    top rating. The record separates that institutional designation from the
    later tourism revenue, jobs, or education outcomes used by researchers.
identity:
  instrument: >
    China's national tourist-attraction quality-rating system, focusing on the
    first designation of an attraction as a 5A (AAAAA) national tourist
    attraction and the subsequent expansion of 5A attractions across places.
  authority: >
    The former China National Tourism Administration issued the first national
    5A certificates and plaques; the Ministry of Culture and Tourism now
    maintains the national A-level attraction knowledge base. Provincial and
    local tourism authorities document the local attraction and administrative
    location.
  legal_identifiers:
  - National 5A (AAAAA) tourist-attraction quality-rating designation
  - 2007 first batch of 66 national 5A tourist attractions
  - Ministry of Culture and Tourism A-level tourist-attraction knowledge base
  implementation_regime: >
    Attractions were evaluated under a national quality-rating system and
    designated in batches rather than by one nationwide local-treatment date.
    The first 66 certificates and plaques were presented on 2007-08-17, while
    local official records commonly report the first-batch recognition date as
    2007-05-08; later attractions entered in additional years. The date of the
    first 5A designation in a county or prefecture, not the date of a later
    tourism project, is the relevant exposure clock.
  assignment_mechanism: >
    Tourist attractions were selected through a national rating and inspection
    process. For the published regional application, a prefecture is treated as
    exposed when its first 5A attraction is established; for the individual
    education application, exposure is assigned at the county containing a 5A
    attraction. The rating is therefore an administrative selection tied to
    attraction quality and local development effort, not a random draw.
  parent: null
  related_variations: []
timeline:
  announcement: '2007-05-08'
  effective: '2007-08-17'
  implementation_start: 2007
  implementation_end: null
  local_timing: >
    The first national batch comprised 66 attractions and received certificates
    and plaques at a 2007-08-17 ceremony. The Ministry knowledge base records
    attraction-specific years (for example 2007, 2011, 2012, and later years),
    so a usable panel must recover each attraction's first designation date and
    map it to a stable county and prefecture identifier. [E3, reported claim]
    The published application maps establishments from 2007 through 2020; later
    designations in the current Ministry database are outside that paper's stated
    application window unless a new design documents them.
  anticipation: >
    Local governments and attraction managers prepared applications and made
    infrastructure, service, and environmental investments before inspection.
    A first-5A date can therefore include anticipation and should not be read
    as the first day on which tourism activity changed.
  last_verified: '2026-08-11'
assignment:
  unit: >
    Attraction, county, and prefecture by designation cohort; the JUE
    application uses prefecture-year tourism outcomes and county-by-birth-cohort
    individual education outcomes as two linked but distinct exposure units.
  treated: >
    A prefecture-year is treated after the first attraction in that prefecture
    receives a 5A designation. In the individual application, a person is
    exposed when their county contains a first-designated 5A attraction before
    the relevant age/cohort cutoff.
  comparison_pool: >
    Not-yet-designated or never-designated counties and prefectures form the
    initial comparison pool, with event-time and cohort comparisons separating
    people exposed before age 17 from those whose schooling decision was already
    made. Nearby places and attractions preparing for designation may be
    contaminated comparisons.
  rule: >
    Build an attraction-level list with the first 5A recognition date, join each
    attraction to its county and prefecture, and code first-designation cohorts.
    Do not replace the designation with tourism revenue, tourist counts, a
    generic scenic-spot label, or an endogenous local tourism investment.
  intensity: >
    Natural intensity measures include the number of 5A attractions, the first
    designation cohort, and time since first designation. The published study's
    main treatment is the first-designation indicator; exact attraction counts
    and date harmonization require the audited national list.
  exemptions:
  - Counties or prefectures without a 5A attraction by the study cutoff
  - Attractions that were only 4A or another tourism label
  - Later upgrades or tourism projects that do not change the first 5A date
  compliance: >
    A recorded designation establishes administrative exposure, not automatic
    compliance with a fixed tourism-production treatment. Attractions can be
    upgraded, renamed, merged, or geographically redefined, and local tourism
    responses can differ substantially.
  exposure_construction: >
    Combine official attraction names, first-recognition dates, and local
    administrative locations with stable county and prefecture crosswalks. Keep
    attraction-level dates, county-level exposure, prefecture-level exposure,
    and individual age-at-exposure separate until the paper's coding is audited.
  required_identifiers:
  - attraction name and stable attraction identifier
  - first 5A recognition date and designation batch
  - county and prefecture identifier at designation
  - individual county of residence and Hukou county where applicable
  - birth year or age and survey year
  - tourism and education outcome year
  spillovers: >
    Tourism demand, service-firm entry, wages, labor reallocation, and public
    investment can cross county and prefecture borders. Neighboring attractions
    and common tourist corridors can also expose nominal controls.
research_compatibility:
  outcome_domains:
  - tourism revenue and tourist arrivals
  - service-sector firm entry and employment
  - wages and labor demand
  - high-school enrollment and educational attainment
  - parental education expectations and school investment
  - local public education inputs
  affected_populations:
  - Residents and firms in counties or prefectures containing 5A attractions
  - Children whose schooling decisions overlap with local tourism expansion
  - Tourism, accommodation, catering, retail, and related service workers
  mechanism_channels:
  - tourism-sector labor demand and opportunity cost of schooling
  - parental expectations and educational investment
  - service-sector agglomeration and firm entry
  - local income and wage changes
  best_for:
  - Dated place-based tourism expansion with explicit cohort exposure
  - County or prefecture event studies with an audited designation list
  - Education and labor-market responses to tourism-led local development
  not_good_for:
  - Treating 5A designation as random or intrinsically exogenous
  - Using a current 5A list without reconstructing the first designation date
  - Calling tourism revenue itself the treatment
  - Inferring attraction boundaries or county exposure from names alone
design:
  claim_type: causal
  affordances:
  - Staggered first-designation timing across Chinese places
  - Prefecture-level tourism outcomes and county-level cohort exposure
  - Age-at-exposure contrasts around the high-school enrollment decision
  - Service-sector and education mechanisms
  candidate_designs:
  - Prefecture fixed-effects DID and event studies around first 5A designation
  - County-by-birth-cohort DID comparing exposure before and after age 17
  - Cohort/event-time designs with county and prefecture-by-birth-year controls
  - Spatial spillover and service-sector mechanism analyses
  identifying_variation: >
    The reported design uses variation in the first 5A designation date across
    prefectures and counties, combined with age or birth-cohort timing for
    individuals. Its identifying content comes from the dated administrative
    designation and the chosen comparison, not from an assumption that the
    national rating process was random.
  primary_strategy: >
    The JUE application first estimates prefecture-level DID and event studies
    for tourism outcomes, then estimates county-level event-time and cohort DID
    models for high-school enrollment. County and prefecture-by-birth-year
    controls, cohort comparisons, and modern staggered-DID corrections are used
    to address differential trends and heterogeneous treatment effects.
  estimand: >
    The average effect of a county or prefecture's first 5A designation on local
    tourism activity, service-sector labor demand, or the probability that an
    individual exposed before age 17 enrolls in high school, relative to the
    specified not-yet/never-designated and age-based comparisons.
  treatment_variable: >
    First 5A designation indicator or event time at the attraction's county or
    prefecture, interacted with individual age/birth cohort where the outcome
    is education. The treatment is not a 5A label observed after the outcome or
    a continuous tourism-revenue measure.
  comparison_logic: >
    Compare places before and after their first designation while accounting for
    place and cohort differences; for education, distinguish teenagers exposed
    before age 17 from older individuals who had likely already made the
    enrollment decision. Treat nearby places, pre-application investment, and
    other attractions as possible contamination.
  estimation_notes: >
    Publisher text reports a 58.9 percent increase in tourism revenue per capita,
    a 32.7 percent increase in tourists per capita, service-sector firm entry,
    and a 3.5 percentage-point decline in high-school enrollment for early
    exposure. These are reported estimates and should not be treated as an
    independent replication.
  assumptions:
  - Conditional pre-trends and controls make first-designation timing informative for the target comparison
  - The official first-designation date and county/prefecture join are measured without material misclassification
  - Age 17 is a meaningful approximation to the high-school enrollment decision point
  - Anticipatory local investment and other policies are measured or do not fully explain the contrast
  - Cross-border tourism, migration, and service-sector spillovers are modeled or limited
  diagnostics:
  - Reconstruct every attraction's first designation from dated official lists
  - Plot event-study pre-trends and test alternative age cutoffs
  - Separate first-batch 2007 designations from later cohorts and upgrades
  - Test county versus prefecture exposure and alternative boundary crosswalks
  - Examine neighboring-place and tourist-corridor spillovers
  - Control for or exclude concurrent transport, education, and tourism programs
threats:
- type: selective_attraction_designation
  basis: reported
  condition: Attractions were selected through inspection and local preparation, which may reflect pre-existing tourism potential, infrastructure, political effort, or local growth.
  evidence_refs:
  - E2
  - E3
  possible_diagnostics:
  - Pre-trend and pre-period tourism controls
  - Event-study leads and placebo designation dates
  - Exclude highly established tourist destinations or model baseline attraction quality
- type: anticipation_and_preparation
  basis: documented
  condition: Local governments and attractions invested in facilities and services before the certificate ceremony or recorded first-designation date.
  evidence_refs:
  - E2
  - E3
  possible_diagnostics:
  - Alternative start dates based on application, inspection, certificate, and opening records
  - Leads and exclusion windows around the designation
  - Separate infrastructure from rating effects where data allow
- type: spatial_and_labor_spillovers
  basis: reported
  condition: Tourists, firms, workers, and public investment can move across county and prefecture borders, contaminating nominal controls.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Neighbor and distance-band exposure measures
  - Tourist-corridor and labor-market clusters
  - Exclude adjacent treated places and test broader commuting zones
- type: cohort_and_boundary_measurement
  basis: reported
  condition: County boundaries, attraction names, Hukou versus residence, and age-at-exposure coding may not align across the official list and the 2015 survey.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Historical county crosswalk and attraction geocoding audit
  - Residence/Hukou alternative samples
  - Alternative age cutoffs and first-designation definitions
empirical_requirements:
  contract_version: 1
  population: Chinese residents, firms, and prefectures/counties linked to nationally rated 5A attractions
  observation_unit: Prefecture-year, county-year, or individual birth-cohort observation
  geography_level: Attraction, county, prefecture, and province with historical boundary crosswalks
  time_start: 2000
  time_end: 2015
  minimum_frequency: Annual local outcomes and individual survey birth cohorts where available
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields:
  - first 5A designation date and attraction identity
  - attraction-to-county and county-to-prefecture crosswalk
  - tourism revenue, tourist arrivals, firm entry, or wage outcomes
  - individual birth year, county of residence/Hukou, education, and demographics when studying schooling
  - concurrent infrastructure, education, and tourism-policy controls
  required_identifiers:
  - attraction_id
  - county_id
  - prefecture_id
  - designation_year or designation_date
  - birth_year and survey_year where applicable
  treatment_key:
  - first_5a_designation_date
  - county_id or prefecture_id
  - age_or_birth_cohort_at_exposure
  treatment_source: >
    Ministry of Culture and Tourism attraction records, contemporaneous tourism
    authority announcements, and the JUE paper's reported designation and survey
    crosswalk. The complete attraction-level first-date panel and exact code are
    not yet independently reproduced.
  measurement_risks:
  - incomplete or changing national attraction lists and date conventions
  - attraction renaming, mergers, upgrades, and boundary changes
  - county and prefecture boundary changes
  - residence versus Hukou location in survey data
  - selection into designation and pre-treatment tourism investment
  - cross-border tourism, migration, and service-sector spillovers
design_profiles: []
evidence:
- id: E1
  source_type: official-data
  citation: 'Ministry of Culture and Tourism. A-level tourist-attraction knowledge base: 5A tourist attractions.'
  url: https://sjfw.mct.gov.cn/site/dataservice/base
  date: 2026
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.local_timing
  - assignment.rule
  - assignment.exposure_construction
  verification_status: verified
  access_level: official-document
  locator: 'Official Ministry data-service page, 5A filter and attraction entries; examples show 2007, 2011, 2012, and later designation years.'
- id: E2
  source_type: implementation-document
  citation: 'Hunan Provincial Department of Culture and Tourism. 2007-08-22. “张家界武陵源旅游区、南岳衡山获得首批国家5A级旅游景区证书和标牌”.'
  url: https://whhlyt.hunan.gov.cn/news/wlyw/201909/t20190910_5478612.html
  date: '2007-08-22'
  supports:
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.effective
  - timeline.implementation_start
  - timeline.local_timing
  - timeline.anticipation
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: 'Official provincial tourism portal: 66 first-batch attractions received certificates and plaques at the 2007-08-17 ceremony; local preparation began in 2006.'
- id: E3
  source_type: paper
  citation: 'He, Zeyi, Zhi-An Hu, Wei Huang, and Yankun Kang. 2025. “Tourism growth, education decline: Evidence from China’s 5A attraction expansion.” Journal of Urban Economics 150:103811. DOI: 10.1016/j.jue.2025.103811.'
  url: https://www.sciencedirect.com/science/article/pii/S0094119025000762
  date: 2025
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.exposure_construction
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.assumptions
  - design.diagnostics
  - design_applications.data_used
  - design_applications.treatment_encoding
  - design_applications.comparison
  - design_applications.empirical_design
  - design_applications.assumptions
  - design_applications.threats_addressed
  - empirical_requirements.observation_unit
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_source
  verification_status: reported
  access_level: full-text
  locator: 'Inspected publisher-indexed article text: introduction and empirical-design discussion describe first-5A timing, prefecture tourism DID/event studies, county-by-age exposure, 2015 China Population Sample Survey, CFPS mechanisms, age-17 cohort contrast, staggered-DID corrections, comparability restrictions, and the remaining selection/anticipation/spillover concerns. These are paper-reported findings, not an independent replication.'
- id: E4
  source_type: paper
  citation: 'He, Zeyi, Zhi-An Hu, Wei Huang, and Yankun Kang. 2025. “Tourism growth, education decline: Evidence from China’s 5A attraction expansion.” IDEAS/RePEc metadata record.'
  url: https://doi.org/10.1016/j.jue.2025.103811
  date: 2025
  supports:
  - identity.instrument
  - scope.knowledge_role
  - design.identifying_variation
  - design.estimand
  verification_status: reported
  access_level: abstract
  locator: 'Public bibliographic record confirming title, authors, journal, DOI, and the reported tourism-expansion/high-school-enrollment question.'
design_applications:
- paper: 'Tourism growth, education decline: Evidence from China’s 5A attraction expansion'
  doi: 10.1016/j.jue.2025.103811
  journal: Journal of Urban Economics
  year: 2025
  research_question: How does tourism expansion following a first 5A attraction designation affect local tourism activity and human-capital accumulation?
  population: Chinese prefectures/counties and individuals observed in local panels, the 2015 China Population Sample Survey, and mechanism data
  outcome: Tourism revenue, tourist arrivals, service-sector firm entry, wages, high-school enrollment, parental expectations, and educational investment
  data_used:
  - Official 5A attraction designations and local attraction-to-county/prefecture links
  - Prefecture-level tourism and firm outcomes
  - 2015 China Population Sample Survey with education, county residence/Hukou, birth year, gender, and ethnicity
  - China Family Panel Studies and local school/teacher inputs for mechanisms
  treatment_encoding: >
    First 5A designation at the prefecture for local tourism outcomes and at the
    county for individual exposure, with event time and a cohort indicator for
    exposure before age 17. [E3, reported claim] The paper's application maps
    establishment cohorts from 2007 through 2020. Exact attraction-list
    construction and historical date harmonization remain to be independently
    audited.
  comparison: >
    Not-yet/never-designated places in staggered DID and event studies, plus
    individuals already at or above the likely enrollment-decision age when the
    county received its first 5A designation.
  empirical_design: Prefecture DID/event study for tourism outcomes and county-by-birth-cohort staggered DID/event study for high-school enrollment
  assumptions:
  - Conditional trends and controls support the chosen place and cohort comparisons
  - First designation and county/prefecture coding are measured correctly
  - Age 17 captures the relevant high-school enrollment decision margin
  - Spillovers and anticipatory investments are addressed sufficiently
  threats_addressed:
  - Differential county trends through geographic, climatic, historical, and economic controls interacted with birth year
  - Heterogeneous staggered effects through modern event-study estimators
  - Mechanism tests for labor demand, parental expectations, and public education inputs
  evidence_refs:
  - E3
  - E4
method_transfer: null
readiness_blockers:
- The complete attraction-level national list, first-recognition dates, and historical attraction-to-county crosswalk have not yet been independently reconstructed.
- The article's full appendix and code are not available in the inspected source set; the publisher text supports the reported design but not independent reproduction of every coefficient or cohort rule.
- Local application and infrastructure investment precede certification, so first 5A designation is not intrinsically exogenous.
- County versus prefecture exposure, residence versus Hukou, and attraction boundary changes can alter treatment and comparison coding.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

China's A-level tourist-attraction system ranks attractions using a national quality-rating process. The Ministry of Culture and Tourism's knowledge base identifies 5A as the top national level and records attraction locations and designation years [E1]. The first national batch comprised 66 attractions: the former National Tourism Administration presented their certificates and plaques on 2007-08-17, after local preparation and inspection work [E2]. Later attractions entered in additional years, so the relevant exposure is a dated first designation rather than a current 5A label.

## What Changed

The change is an administrative upgrade/designation that made an attraction the top national-rated tourist attraction and was followed, in the published application, by increased local tourism activity and service-sector demand. The canonical object is the designation and its place/date mapping. Tourism revenue, tourist counts, a hotel opening, or a local government's generic tourism investment are outcomes or mechanisms, not interchangeable treatments.

## Implementation and Assignment

The rating was not assigned randomly. Attractions and local governments prepared facilities, services, environmental management, and inspection materials before certification [E2]. A research design therefore needs the attraction-level first-recognition date and a stable county/prefecture crosswalk. The JUE application uses prefecture first-designation exposure for tourism outcomes and county first-designation exposure for individuals in the 2015 China Population Sample Survey; these are related but not identical units [E3].

## Why This Creates Empirical Variation

Different places received their first 5A attraction in different cohorts. The reported study combines this staggered timing with prefecture and county outcomes, and with individual age at exposure: teenagers exposed before age 17 are compared with older individuals who had likely already made the high-school enrollment decision [E3; E4]. The identifying contrast is therefore a dated administrative exposure plus a stated comparison, not a claim that 5A selection was exogenous.

## Identification Risks

Attractions with strong tourism potential, infrastructure, political support, or local preparation may be selected earlier. Preparation can begin before the certificate date. Tourists, workers, firms, and public investment can cross county and prefecture borders, while attraction names, county boundaries, residence, and Hukou may not align across years. These risks must be addressed before treating the variation as a clean shock [E2; E3; analytical inference].

## Data Requirements

A study needs an attraction-level list with first designation dates, attraction coordinates or official administrative locations, stable county/prefecture identifiers, and local tourism or labor outcomes. The individual education application additionally needs birth year, education, county of residence/Hukou, and survey year from the 2015 China Population Sample Survey. Dataset acquisition and cleaning belong in `Econ Data Know-How`; this record specifies the treatment key and joins that data work must satisfy.

## Evidence Notes

E1 establishes the national 5A instrument and attraction-level designation-year entries through the official Ministry knowledge base; it does not by itself provide a historical panel of every first designation or prove causal assignment. E2 is an official contemporaneous/local implementation account and establishes the 66-attraction first batch, the 2007-08-17 certificate ceremony, and substantial pre-certification investment and inspection work; it does not identify every county or prefecture in the national panel. E3 is the publisher-indexed paper text and reports the prefecture/county exposure, 2007–2020 application window, 2015 survey, age-17 cohort comparison, and main design; it is not an independently audited replication package. E4 corroborates the paper identity and research question through a public metadata record. The record is grounded in the institutional boundary and reported application while keeping the attraction list, exact date harmonization, and selection limits open for later audit.
