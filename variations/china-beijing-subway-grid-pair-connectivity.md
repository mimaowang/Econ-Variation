---
schema_version: 2
id: china-beijing-subway-grid-pair-connectivity
name: Beijing Subway Expansion and Grid-Pair Connectivity for Patent Collaboration
aliases:
- Beijing subway collaborative matching
- Koh Li Xu subway innovation
- 北京地铁扩张 网格对连通性 专利合作
status: grounded
provenance:
  task_id: task-822b16c0cbc7
scope:
  country: China
  regions:
  - Beijing, mainland China
  domains:
  - urban
  - regional-economics
  - transportation
  - innovation
  - patents
  - economic-geography
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    Beijing's staged subway-network expansion changed the feasible fastest route and
    modeled travel time between pairs of small city grids. The published study uses
    that within-city change to study collaborative patent applications. This is not
    a nationwide subway-opening indicator or an intrinsically exogenous policy.
identity:
  instrument: >
    Staged opening of Beijing subway stations and line segments during 2000–2018,
    represented as changing subway-network connectivity between pairs of 0.5 km
    Beijing grids. A paper-specific distance-by-aggregate-expansion instrument is
    an analytical use of this same network change, not another government program.
  authority: >
    Beijing municipal transport, construction, and operating authorities opened
    lines and stations in stages. The paper reconstructed historical station
    coordinates, opening years, and network links; official transport announcements
    independently establish selected openings, not the complete paper grid panel.
  legal_identifiers:
  - Beijing 2008 Government Work Report, planned Line 10 phase I, Olympic branch, and Airport Line
  - Beijing Municipal Commission of Transport 2017-12-28 opening announcement
  - Beijing Municipal Commission of Transport 2018-12-29 opening announcement
  implementation_regime: >
    A growing municipal rail network with line- and station-specific opening dates,
    not one adoption date. The paper's 2000–2018 network includes changing paths,
    station access, and connections. Construction, scheduled opening, and actual
    operation are distinct; the official 2018 notice explicitly names two stations
    whose opening was deferred.
  assignment_mechanism: >
    A grid pair's exposure changes when newly operating stations or links alter
    its modeled fastest route. The paper measures the subway distance on that
    route continuously and also defines a first-treatment cohort when modeled
    pairwise travel time falls by more than 30 minutes. Neither variable is a
    randomized assignment or a direct observed trip time.
  parent: null
  related_variations:
  - china-beijing-2008-private-car-driving-restriction-subway-premium
timeline:
  announcement: null
  effective: null
  implementation_start: 2000
  implementation_end: 2018
  local_timing: >
    Each annual grid-pair network is reconstructed from operating station and link
    dates. The 2008 government work report planned several Olympic-era openings;
    the transport commission separately documents openings at the end of 2017 and
    2018. The study's 2000–2018 window is a sample boundary, not a universal
    treatment interval for every pair.
  anticipation: >
    Route plans and construction could change innovator location and collaboration
    before service begins. The paper reports event-study pre-trends, but these do
    not independently prove unanticipated or random completion timing.
  last_verified: '2026-10-02'
assignment:
  unit: Pair of 0.5 km by 0.5 km Beijing grids by calendar year
  treated: >
    For the staggered-DiD application, a grid pair first becomes treated in the
    year its modeled fastest-route travel time drops by more than 30 minutes.
    The continuous application instead measures kilometers of subway travel on
    that fastest route; a one-hour travel-time reduction is an interpretation
    via a modeled first stage, not the primitive observed treatment.
  comparison_pool: >
    Grid pairs that never cross the paper's travel-time-reduction threshold are
    the DiD controls. Pairs can still experience smaller network improvements,
    so the estimand is differential exposure, not treated versus wholly untouched.
    The continuous and IV analyses compare pairs with different route changes
    conditional on grid-pair and year effects.
  rule: >
    Geocode patent applicants and historical stations to 0.5 km grids. For each
    grid pair and year, use operating station links to find the minimum modeled
    travel-time route from one grid centroid to the other. Count subway kilometers
    on that route as Length_ijt and compute modeled TravelTime_ijt. For binary
    DiD, the first year a pair's fastest-route time falls by over 30 minutes
    establishes its cohort; do not replace this with the year either grid first
    receives a station, which is a separate grid-level exercise in the paper.
  intensity: Subway kilometers on fastest modeled grid-pair route; alternatively a >30-minute modeled travel-time reduction
  exemptions:
  - Baseline grid-pair sample uses grids ever within 2 km of a subway station during the study window
  - Other distance cutoffs and a one-hour treatment threshold are robustness variants, not separate policy regimes
  compliance: >
    Operation of a line is observable in principle, but inventor trips and actual
    route choice are not observed. The study assumes subway speed of 36 km/h and
    off-subway speed of 8–12 km/h; the fastest path is a model construct.
  exposure_construction: >
    Join station coordinates, opening year, and time-varying network edges to
    applicant-address grids, then calculate annual minimum-time paths. Retain
    subway route length, modeled travel time, Euclidean pair distance, and the
    citywide cumulative subway-network length as separate variables. The study's
    IV interacts time-invariant pair distance with aggregate network expansion;
    it must not be confused with a station-proximity indicator.
  required_identifiers:
  - stable grid_id_i and grid_id_j
  - calendar year
  - station_id, coordinates, and operation year
  - network edge or line-section identifier and opening year
  - patent application identifier, date, and applicant geocoded address
  spillovers: >
    New links can change many pairs' feasible routes at once, including pairs
    without a new station in either grid. Inventors can move, enter, or switch
    collaborators, making nominal controls partly exposed and effects dependent
    on the evolving city network.
research_compatibility:
  outcome_domains:
  - collaborative patent applications
  - inventor matching and location
  - within-city knowledge exchange
  - firm and university innovation links
  affected_populations:
  - Beijing patent applicants and inventors with geocoded addresses
  - firms and institutions linked to stable Beijing grid locations
  mechanism_channels:
  - lower modeled face-to-face travel cost
  - matching among high-productivity innovators
  - inventor entry and spatial relocation
  best_for:
  - Studying within-city pairwise connectivity and geographically separated collaborations
  - Comparing network-improved grid pairs with less-improved or never-threshold-crossing pairs
  - Designs with historical network GIS and geocoded applicant-level outcomes
  not_good_for:
  - Treating all Beijing observations as exposed on a common opening date
  - Claiming actual individual travel time is observed from the network model
  - Treating station siting, construction completion, or the distance-based IV as automatically exogenous
design:
  claim_type: causal
  affordances:
  - Staggered first crossing of a pairwise travel-time threshold
  - Continuous network-route exposure and modeled travel-time first stage
  - Distance-by-citywide-network-expansion IV for heterogeneous pair exposure
  candidate_designs:
  - Staggered grid-pair difference-in-differences
  - Grid-pair fixed-effects continuous exposure regression
  - Distance-by-aggregate-expansion instrumental variables
  identifying_variation: >
    Annual Beijing subway openings alter fastest feasible routes between
    pre-defined grid pairs. The binary design groups pairs by first large modeled
    travel-time reduction. The IV uses fixed Euclidean grid-pair distance times
    time-varying citywide subway length to predict route connectivity.
  primary_strategy: >
    The accessible manuscript estimates grid-pair and year fixed-effects models,
    a staggered DiD using never-threshold-treated pairs, and an IV for route
    Length. The IV's first stage depends on distant pairs benefiting more from
    aggregate network growth; exclusion requires distance-specific innovation
    trends not to respond through other channels.
  estimand: >
    A conditional effect of improved modeled pairwise connectivity on patent
    collaborations among applicant locations in the paper's Beijing grid-pair
    sample; the IV is a local average causal response for pairs whose route
    exposure responds to the distance-by-expansion instrument.
  treatment_variable: >
    Binary >30-minute modeled travel-time reduction for DiD; subway kilometers
    on the fastest modeled route for continuous and IV analyses. Modeled travel
    time is a first-stage and interpretation variable, not observed commute time.
  comparison_logic: >
    Compare first-threshold-crossing pairs to never-crossing pairs by cohort
    under conditional parallel trends; compare within-pair route changes over
    years with year effects; and compare distance-related differences in route
    responses to common network expansion under the IV restriction.
  estimation_notes: >
    The published abstract reports a 14.85–37.69% increase in collaborated
    patents associated with a one-hour modeled travel-time reduction; this is
    an author-reported estimate, not an institutional fact. The inspected 2021
    manuscript explains the construction; the final article's detailed methods
    were not independently inspected and may differ in small specifications.
  assumptions:
  - Conditional parallel trends between treated cohorts and never-threshold-treated grid pairs
  - Opening timing and route improvements are not jointly selected with unobserved pair-specific innovation shocks
  - Euclidean distance times common network growth affects collaboration through connectivity rather than another distance-varying trend
  - Applicant-address geocoding, network chronology, and assumed speeds measure the intended exposure consistently
  diagnostics:
  - Event-study pre-trends for both grid and grid-pair outcomes
  - Compare 30-minute and one-hour threshold definitions
  - Report first stage, leave-one-out aggregate shift, and far-versus-near heterogeneity
  - Vary off-subway speed, station access radius, and pair centrality controls
  - Check inventor relocation, entry, and competing place-based innovation policies
threats:
- type: endogenous-route-and-station-placement
  basis: reported
  condition: Subway phase-in can coincide with innovation hubs or other local investment, so the route-change coefficient need not isolate transport alone.
  evidence_refs: [E1]
  possible_diagnostics:
  - inspect plans and opening delays against local innovation policies
  - check pair-level pre-trends and location-by-year controls
- type: nonrandom-distance-exposure
  basis: reported
  condition: Farther-apart pairs may differ in peripheral location or long-run collaboration trends, potentially violating the IV exclusion restriction.
  evidence_refs: [E1]
  possible_diagnostics:
  - exclude most distant pairs and inspect centrality gradients
  - interact baseline pair distance with pre-period indicators
- type: network-measurement-and-partial-controls
  basis: inferred
  condition: Station dates, geocoding, speed assumptions, and omitted travel modes affect computed routes; never-threshold-treated pairs may still benefit from smaller reductions.
  evidence_refs: [E1, E4]
  possible_diagnostics:
  - audit individual station dates against official announcements
  - vary speed and access assumptions and examine sub-threshold exposure
empirical_requirements:
  contract_version: 1
  population: Geocoded Beijing patent applicants and potential collaborators
  observation_unit: Beijing grid-pair-year panel
  geography_level: 0.5 km Beijing grid pair
  time_start: 2000
  time_end: 2018
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 1
  required_fields:
  - patent application identifier, year, applicant identifiers, and applicant addresses
  - collaborated-patent count by grid pair and year
  - station coordinates, operation year, and historical network links
  - modeled fastest-route travel time and subway kilometers by grid pair and year
  - Euclidean grid-pair distance and citywide cumulative subway length for the IV
  required_identifiers:
  - grid_id_i
  - grid_id_j
  - year
  - station_id
  - patent_application_id
  treatment_key:
  - grid_id_i
  - grid_id_j
  - year
  treatment_source: >
    Historical Beijing subway network and station operation dates reconstructed by
    the paper, with official municipal transport announcements available for
    spot checks; patent applications and applicant addresses from CNIPA.
  measurement_risks:
  - The paper's subway chronology originally draws on Wikipedia and needs a line-by-line official crosswalk for full independent replication
  - The modeled fastest route excludes full time-varying multimodal travel networks
  - Applicant-address changes can reflect relocation, not only new collaboration
  - The 2 km ever-near-a-station baseline universe is a selected study population
evidence:
- id: E1
  source_type: paper
  citation: 'Koh, Yumi, Jing Li, and Jianhuan Xu. 2021. "Subway, Collaborative Matching, and Innovation," AEA conference full manuscript.'
  url: https://www.aeaweb.org/conference/2022/preliminary/paper/ht8FnFrG
  date: 2021
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.implementation_start
  - timeline.implementation_end
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.exposure_construction
  - design.identifying_variation
  - design.primary_strategy
  - design.treatment_variable
  - empirical_requirements.required_fields
  - design_applications.treatment_encoding
  verification_status: verified
  access_level: full-text
  locator: 'pp. 6–14, §§2–4 (institution, models, station/patent data, grid construction, routes); pp. 16–18, §5.2 (grid-pair DiD, continuous exposure, IV); pp. 9–11, §3 (IV restriction and distance-centrality checks)'
- id: E2
  source_type: policy-document
  citation: 'Beijing Municipal Government. 2008 Government Work Report (2008年政府工作报告).'
  url: https://www.beijing.gov.cn/gongkai/jihua/zfgzbg/201903/t20190321_1838376.html
  date: 2008
  supports:
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.local_timing
  verification_status: verified
  access_level: official-document
  locator: 'Government work priorities, Olympic infrastructure paragraph naming Line 10 phase I, Olympic branch, and Airport Line'
- id: E3
  source_type: policy-document
  citation: 'Beijing Municipal Commission of Transport. 2017-12-28. 本市轨道交通运营线路达22条 总里程608公里.'
  url: https://jtw.beijing.gov.cn/xxgk/tpxw/201801/t20180108_342268.html
  date: 2017
  supports:
  - identity.implementation_regime
  - timeline.local_timing
  verification_status: verified
  access_level: official-document
  locator: 'Opening paragraph naming 2017-12-30 trial operation of Yanfang, S1, and Xijiao lines'
- id: E4
  source_type: policy-document
  citation: 'Beijing Municipal Commission of Transport. 2018-12-29. 6号线西延、8号线三期四期12月30日开通试运营.'
  url: https://jtw.beijing.gov.cn/xxgk/xwfbh/201912/t20191209_1007609.html
  date: 2018
  supports:
  - identity.implementation_regime
  - timeline.local_timing
  - assignment.compliance
  verification_status: verified
  access_level: official-document
  locator: 'Opening paragraphs naming line segments, network length, and deferred opening of 苹果园 and 大红门 stations'
- id: E5
  source_type: paper
  citation: 'Koh, Yumi, Jing Li, and Jianhuan Xu. 2025. "Subway, Collaborative Matching, and Innovation." Review of Economics and Statistics 107(2): 476–493. DOI 10.1162/rest_a_01279.'
  url: https://doi.org/10.1162/rest_a_01279
  date: 2025
  supports:
  - design_applications.year
  - design_applications.journal
  - design.estimation_notes
  verification_status: reported
  access_level: abstract
  locator: 'Publisher DOI search-indexed metadata and abstract, corroborated by SMU acceptedVersion landing page; full text download was inaccessible during this audit'
- id: E6
  source_type: replication
  citation: 'Koh, Yumi, Jing Li, and Jianhuan Xu. 2022. Replication data for Subway, Collaborative Matching, and Innovation. Harvard Dataverse. DOI 10.7910/DVN/WBUJ5Q.'
  url: https://smusg.elsevierpure.com/en/datasets/replication-data-for-subway-collaborative-matching-and-innovation/
  date: 2022
  supports:
  - empirical_requirements.treatment_source
  verification_status: reported
  access_level: replication
  locator: 'SMU dataset metadata reporting Harvard Dataverse package with README and Stata/Matlab code; contents not independently inspected'
design_applications:
- paper: Subway, Collaborative Matching, and Innovation
  doi: 10.1162/rest_a_01279
  journal: Review of Economics and Statistics
  year: 2025
  research_question: Does improving within-Beijing subway connectivity increase patent collaboration between spatially separated innovators?
  population: Beijing patent applicants assigned to 0.5 km grids, baseline pairs drawn from grids ever within 2 km of a station
  outcome: Annual collaborative patent applications formed by applicants in each grid pair
  data_used:
  - CNIPA patent application identifiers, dates, applicants, IPC classes, and addresses
  - Beijing station coordinates, opening years, and historical subway network as reconstructed by the authors
  treatment_encoding: >
    Pair-specific first year of a >30-minute modeled fastest-route time decline
    for staggered DiD; alternatively subway route kilometers on the fastest path
    for continuous models, with time-invariant pair distance times citywide
    cumulative network length as an IV.
  comparison: Never-threshold-treated grid pairs for cohort DiD; within-pair changes and distance-related network responses in continuous and IV analyses.
  empirical_design: Grid-pair fixed-effects models, staggered cohort DiD, and distance-by-aggregate-network-expansion IV.
  assumptions:
  - Untreated potential collaboration trends are parallel across threshold cohorts and never-crossing pairs
  - Network timing and pair-distance interactions are not confounded by other place-specific innovation changes
  - Modeled route changes meaningfully approximate the relevant travel-cost channel
  threats_addressed:
  - route siting and contemporaneous innovation policies
  - nonrandom pair distance and center-periphery gradients
  - threshold, speed, and spatial-radius sensitivity
  evidence_refs: [E1, E2, E3, E4, E5]
method_transfer: null
readiness_blockers:
- The inspected empirical-method source is the accessible 2021 full manuscript, not the final 2025 journal full text; final detailed specifications and appendix should be reconciled before exact replication claims.
- The authors' complete station-by-station chronology was not independently matched to official operation records. The 2018 transport notice explicitly distinguishes announced segments from deferred individual stations.
- The Dataverse package is identified but its README/code were not unpacked; this record provides a data contract, not a turnkey treatment panel.
- Pair-distance by citywide expansion is a conditional IV, not proof that route siting or pair exposure is random.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Beijing expanded its subway as a municipal network over many years, rather than assigning all locations to one policy date. The 2008 government work report names specific Olympic-era lines as planned transport infrastructure [E2]. The municipal transport commission later documented separate end-2017 and end-2018 line openings [E3; E4]. The 2018 notice also states that two named stations on otherwise opening extensions were deferred, which illustrates why a line-level announcement cannot simply be copied into a station-level treatment table [E4].

The paper studies how this network changed the ability of inventors in different parts of Beijing to meet. Its core object is a pair of small grids, not whether a firm is merely close to any station. A newly operating segment can shorten the best route for two locations even when neither location acquires a station that year. Conversely, a nearby station need not greatly change their pairwise route [E1; analytical inference].

## What Changed

The changing network altered the modeled fastest route and travel time between pairs of locations. There was no single date or boundary that treated every Beijing innovator; each pair could gain connectivity when relevant links began operating [E1; E3; E4].

## Implementation and Assignment

The accessible full manuscript divides Beijing into 0.5 km grids, geocodes patent applicants and stations, and reconstructs each year's operating subway network. It computes the fastest modeled route between two grid centroids. The main continuous variable is subway distance traveled on that route. Modeled travel time is calculated using assumed subway and off-subway speeds; it is not a measure of actual trips. A pair enters the staggered-treatment cohort when the modeled time falls by more than 30 minutes, with never-crossing pairs used as controls [E1].

## Why This Creates Empirical Variation

The same study also instruments pairwise route connectivity with fixed Euclidean distance between the grids interacted with cumulative citywide subway expansion. The intuition is that farther-apart locations can gain more from a growing rail network. This is a paper-specific identifying construction, not an additional municipal policy. Its exclusion restriction is vulnerable if distant pairs differ systematically in location, innovation opportunity, or other policies [E1; reported design and analytical inference].

## Identification Risks

This record is useful when a researcher has historically geocoded applicant-level outcomes and can rebuild an annual transport network. It should not be offered as a ready-made city-level subway DID. The 2 km ever-near-station baseline sample, speed assumptions, and location-pair construction are substantive parts of the design. Never-crossing pairs can still receive smaller time savings, and inventors may enter, relocate, or change partners as the network evolves [E1].

## Data Requirements

Reconstructing the published exposure requires station opening dates and network links, fixed grid geometry, annual fastest-route calculations, CNIPA applicant addresses, and a stable grid-pair-year outcome panel. The IV additionally requires Euclidean pair distance and cumulative network length for each year [E1].

## Evidence Notes

Official notices verify selected openings and the existence of a staged municipal expansion. They do not verify the paper's complete station-year GIS, applicant geocoding, or causal assumptions. The accessible 2021 manuscript supplies the detailed empirical construction; the 2025 journal metadata and abstract confirm publication and the broad result, while the final full text and replication code have not been independently inspected here [E1; E5; E6]. Reusers should reconcile those materials before claiming exact replication or transferring this design to another city.
