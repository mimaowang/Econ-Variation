---
schema_version: 2
id: china-ming-capital-relocation-population-distribution
name: Ming Capital Relocation from Nanjing to Beijing and Chinese Urban Systems
aliases:
- Ming capital relocation, 1421
- Nanjing–Beijing capital shift
- 明成祖迁都北京
- 永乐十九年迁都
status: grounded
provenance:
  task_id: task-e6f648e1ff1b
scope:
  country: China
  regions:
  - Historical Chinese county-level jurisdictions in the Ming and later dynastic sample
  - Nanjing (Yingtian) and Beijing (Shuntian) as the former and new political centers
  domains:
  - regional-economics
  - urban-economics
  - economic-history
  - political-economy
  - population
  - administrative-geography
  variation_type: event-shock
  knowledge_role: china-variation
  china_relevance: >
    Lu, Ou, and Zhong (2024) study the relocation of the Ming primary capital from
    Nanjing to Beijing in 1421 CE as a historical institutional shock to the geography
    of political governance. Their application links historical county population and
    household measures to distance from Beijing and follows the spatial pattern into
    later dynasties and modern China. This is a historical Chinese institutional
    variation, not a modern capital-development policy or a generic Beijing-distance
    control.
identity:
  instrument: >
    The Ming court's relocation of the primary capital from Nanjing (Yingtian) to
    Beijing (Shuntian) at the start of 1421. The official transition began with the
    Yongle-era edict that Beijing would be the capital from the first day of the next
    year; Nanjing remained a secondary capital with residual southern institutions.
    This record follows the governance-center change used in Lu, Ou, and Zhong (2024),
    not later moves of Republican or contemporary Chinese government offices.
  authority: >
    The Yongle Emperor and the Ming imperial court chose and formalized the new
    primary capital. The court's decision involved the palace and administrative
    construction in Beijing, northern frontier governance, and the relocation or
    reweighting of central institutions. The decision was historically selected and
    cannot be treated as a random draw of cities or counties.
  legal_identifiers:
  - Yongle 18 (1420) edict beginning “以明年正月初一日始，北京为京师，不称行在”
  - Yongle 19 (1421) formal Beijing primary-capital designation and Nanjing secondary-capital designation
  - Ming administrative names Shuntian Fu (Beijing) and Yingtian Fu (Nanjing)
  implementation_regime: >
    Beijing's palace and central administrative setting were completed before the
    formal 1421 designation. Beijing became the primary seat of the empire, while
    Nanjing retained a formally recognized southern-capital role and some ministries.
    The exposure therefore has a formal political-center clock and a longer process of
    personnel, military, fiscal, information, and material reorganization; these should
    not be collapsed into one exact implementation date in a new dataset.
  assignment_mechanism: >
    The paper assigns historical locations a continuous exposure through their distance
    to Beijing, the new primary capital, and compares the distance–population
    relationship before and after the relocation. The event changes which political
    center is geographically proximate; it does not assign a binary program to a named
    set of counties. A county's exposure is inherited from its historical location and
    the period-specific population/household observation.
  parent: null
  related_variations: []
timeline:
  announcement: '1420'
  effective: '1421'
  implementation_start: 1421
  implementation_end: null
  local_timing: >
    The official historical account records the 1420 edict and the first-day-of-1421
    Beijing designation. The paper's population panel spans multiple historical periods,
    later dynasties, and modern China; its exact observation years, treatment window,
    and any transition or persistence coding must be recovered from the full article or
    replication materials.
  anticipation: >
    Palace construction, court deliberation, military preparation, and administrative
    relocation preceded the formal 1421 designation. A pre-period close to 1421 can
    therefore contain anticipation or transitional exposure; the formal date is not a
    guarantee that all governance channels changed discontinuously on one day.
  last_verified: '2026-08-13'
assignment:
  unit: >
    Historical county-level jurisdictions or their harmonized successors. The source
    application reports a self-constructed panel of 240 county units and uses local
    population and household size as urban-system measures. The exact county universe,
    historical boundary concordance, and whether every observation is a county or a
    higher-level administrative unit remain full-text recovery items.
  treated: >
    After 1421, a location is exposed to the new Beijing-centered political geography
    according to its distance to Beijing and the governance channels that distance
    represents. The source's main empirical object is the post-relocation change in the
    slope or effect of distance to Beijing, not a binary treated-county indicator.
  comparison_pool: >
    Pre-relocation observations provide the before relationship between location and
    distance to Beijing; post-relocation observations provide the after relationship.
    Counties at different distances supply the spatial gradient, with the paper using
    a difference-in-differences specification. Nanjing and locations near it are not
    automatically valid controls: Nanjing retained secondary-capital institutions and
    the relocation may have affected the whole imperial system.
  rule: >
    Preserve a historical county location, compute or recover its distance to Beijing
    using the paper's historical-geography convention, and interact that exposure with
    a post-1421 indicator (or the paper's equivalent period coding). Keep the former
    capital, new capital, county boundary version, and observation year separate. Do
    not substitute modern county centroids or a contemporary Beijing-distance measure
    without documenting the crosswalk.
  intensity: >
    Distance to Beijing is the primary continuous exposure. Useful secondary measures
    include distance to Nanjing, distance to both political centers, access to delivery
    routes, military-garrison or frontier exposure, and material-supply connectivity.
    These mechanisms must remain separate from the main distance interaction.
  exemptions:
  - County observations lacking a defensible historical location or boundary concordance
  - Periods and jurisdictions for which the paper has no comparable population or household measure
  - Nanjing and Beijing observations if the source analysis excludes political centers themselves
  - Observations affected by dynasty-specific administrative reorganization that cannot be harmonized
  - Modern observations whose geography cannot be linked to the historical county unit
  compliance: >
    Not applicable as legal compliance. The capital designation was binding within the
    imperial administration, but the realized degree of local governance, delivery,
    military protection, and population response is an outcome rather than take-up.
  exposure_construction: >
    Build a dated historical county ledger with original name, dynasty, prefecture,
    successor/crosswalk, coordinates or polygon, and population/household source. Join
    it to the period-specific distance to Beijing and to a post-1421 indicator while
    preserving the paper's sample and interpolation choices. For mechanism work, add
    separate route, material-supply, military, and war records. Store historical GIS,
    digitized population tables, and acquisition paths in Econ Data Know-How; this
    record only defines the variation and its join contract.
  required_identifiers:
  - Historical county or prefecture identifier and dynasty-specific name
  - Harmonized historical boundary or location crosswalk
  - Observation year/period and dynasty
  - Distance to Beijing and, where used, distance to Nanjing
  - Local population and household-size source and unit
  - War, military-garrison, delivery-route, or material-supply identifiers for mechanisms
  spillovers: >
    Moving the capital changes national resource flows, military deployment, migration,
    taxation, transport, and information networks. A county may be affected through
    routes or neighboring jurisdictions even when its direct distance is unchanged.
    Persistence into the Qing dynasty and modern China also raises the possibility that
    later institutions, wars, and infrastructure transmit or replace the original
    governance channel.
research_compatibility:
  outcome_domains:
  - County population and household size
  - Historical urban-system rank and city formation
  - Migration, settlement, and regional population distribution
  - Delivery, transport, and market-access outcomes
  - Military protection, frontier security, and local public goods
  - Long-run institutional persistence and modern regional development
  affected_populations:
  - Residents and households in historical Chinese county jurisdictions
  - Cities and county seats along the Beijing-centered political and delivery network
  - Northern frontier and military-garrison regions
  - Nanjing and southern-capital jurisdictions affected by the dual-capital system
  mechanism_channels:
  - Information and administrative delivery from the political center
  - Military garrisons and protection from frontier conflict
  - Material and fiscal supply to the capital and surrounding regions
  - Migration and settlement induced by state institutions
  - Persistence of administrative and urban hierarchy
  best_for:
  - Historical urban-system and population-distribution research
  - Conditional difference-in-differences using distance to the new political center
  - Mechanism analysis of delivery, security, material supply, and long-run persistence
  - Connecting imperial governance geography to later regional outcomes
  not_good_for:
  - A modern policy rollout or a uniform national post-1421 dummy
  - Treating distance to Beijing as randomly assigned or mechanically causal
  - Ignoring Nanjing's continuing secondary-capital role
  - Mixing the Ming relocation with Republican/PRC capital changes or modern Beijing policies
  - Claims that require precise historical county boundaries or population series not yet reconstructed
design:
  claim_type: causal
  affordances:
  - A dated institutional change in the national political center
  - Continuous geographic exposure through distance to Beijing
  - Pre/post historical population and household measures
  - Persistence checks across dynasties and modern China
  - Mechanism profiles for delivery and national security
  candidate_designs:
  - Continuous-exposure difference-in-differences around 1421
  - Event-time or period-specific distance-gradient models
  - Mechanism designs for delivery routes and military security
  - Long-run persistence comparisons across the Qing dynasty and modern China
  - Historical county panel with spatially robust inference and boundary sensitivity
  identifying_variation: >
    The source's identifying comparison is the change in the relationship between a
    county's distance to Beijing and its population or household size after Beijing
    became the primary capital. The paper presents this as a quasi-natural experiment;
    a user should read the result as conditional on the historical panel, distance
    construction, period coding, and controls rather than as an automatic guarantee of
    random assignment.
  primary_strategy: >
    Lu, Ou, and Zhong use a difference-in-differences strategy with historical county
    population distributions and distance to Beijing. Publisher snippets identify a
    240-county self-constructed panel, log population and log household measures, a
    post-relocation change from positive to negative distance effects, and robustness
    checks. The exact fixed effects, period definitions, distance formula, weighting,
    spatial inference, and all robustness specifications remain to be audited from the
    full article or replication materials.
  estimand: >
    The conditional change in local population or household size associated with a
    one-unit difference in distance to Beijing after the Ming primary-capital relocation,
    relative to the pre-relocation distance gradient, for the historical county panel
    and period definitions used by the source. Persistence estimates have distinct
    estimands and should not be pooled with the initial 1421 effect.
  treatment_variable: >
    Distance_to_Beijing multiplied by an indicator for the post-relocation period, with
    a separate observation-period/dynasty field. Add distance to Nanjing and mechanism
    exposures only as explicitly labeled secondary variables.
  comparison_logic: >
    Compare the distance gradient before and after 1421 across the same harmonized
    historical locations, using the paper's county panel and controls. Keep Nanjing,
    Beijing, frontier regions, war-affected units, and later-dynasty observations in
    separately auditable samples where the source does so. A modern replication should
    show the full distance profile rather than only a single coefficient.
  estimation_notes: >
    Historical panel inference must account for serial correlation, spatial dependence,
    changing administrative units, missing population observations, and dynasty-specific
    shocks. Separate the initial Ming-period contrast from Qing and modern persistence;
    the later estimates are not additional independent replications of the 1421 event.
  assumptions:
  - Historical county locations and population/household measures are harmonized without outcome-driven reassignment
  - Conditional pre/post trends in the distance gradient would be comparable absent the capital relocation
  - The distance-to-Beijing measure captures governance proximity rather than only pre-existing geography or trade
  - Wars, migration, frontier security, canals, and later infrastructure are controlled or included in the estimand
  - Nanjing's secondary-capital institutions and the transition period are modeled rather than ignored
  - Persistence estimates distinguish transmission of the original shock from later institutional changes
  diagnostics:
  - Reconstruct the 240-county universe, historical names, boundaries, and observation years
  - Reproduce distance-to-Beijing and distance-to-Nanjing measures under alternative geographies
  - Plot pre-period distance gradients and placebo relocation dates
  - Test exclusion of Nanjing/Beijing, frontier areas, major wars, and canal corridors
  - Use spatially robust and dynasty/prefecture-clustered inference
  - Audit delivery-route, military-garrison, material-supply, war, and migration controls
  - Separate Ming, Qing, and modern samples and test whether persistence survives alternative crosswalks
design_profiles:
- id: ming-distance-did
  label: Ming capital relocation and historical county population
  design_families:
  - continuous-exposure-did
  - historical-county-panel
  when_to_use: >
    Use when the 1421 institutional date, historical county panel, distance construction,
    and comparable pre/post population or household observations are recoverable. The
    estimand is the distance-gradient change, not a binary treatment effect.
  outcome_domains:
  - population
  - household size
  - city size
  requirements:
    population: Historical Chinese county-level units with comparable population/household observations around the Ming period
    observation_unit: County-period
    geography_level: Historical county and prefecture
    time_start: null
    time_end: null
    minimum_frequency: historical period
    minimum_pre_periods: 1
    minimum_post_periods: 1
    required_fields:
    - Historical county identifier and boundary crosswalk
    - Observation period and dynasty
    - Population or household measure
    - Distance to Beijing and distance to Nanjing
    - Post-1421 indicator and source version
    required_identifiers:
    - historical_county_id
    - period
    - distance_to_beijing
    - population_source
    treatment_key:
    - distance_to_beijing
    - post_1421
- id: governance-mechanisms-persistence
  label: Delivery, security, and long-run persistence of capital relocation
  design_families:
  - mechanism-analysis
  - historical-persistence
  - spatial-panel
  when_to_use: >
    Use for a mechanism or persistence question only after the relevant route, military,
    material-supply, war, and later-institution records are independently dated. The
    mechanisms are explanations of the spatial gradient, not separate treatments unless
    their own assignment rules are documented.
  outcome_domains:
  - delivery access
  - military security
  - population persistence
  - modern regional development
  requirements:
    population: Historical counties followed into later dynasties or modern administrative units
    observation_unit: County-period or county-year after historical crosswalk
    geography_level: Historical county, prefecture, and successor modern unit
    time_start: null
    time_end: null
    minimum_frequency: dynasty/period or annual where modern data exist
    minimum_pre_periods: 0
    minimum_post_periods: 1
    required_fields:
    - Historical-to-modern county crosswalk
    - Delivery-route, military-garrison, material-supply, or war measure
    - Population/household outcome and period
    - Distance to Beijing and Nanjing
    required_identifiers:
    - historical_county_id
    - modern_successor_id
    - period
    - mechanism_source
    treatment_key:
    - distance_to_beijing
    - post_1421
    - mechanism_exposure
threats:
- type: endogenous-capital-selection
  basis: inferred
  condition: >
    The Yongle court selected Beijing for political, military, dynastic, and logistical
    reasons. Those reasons may correlate with geography, frontier conditions, routes,
    and population trends independently of the formal capital designation.
  evidence_refs:
  - E1
  - E2
  - E3
  possible_diagnostics:
  - Historical controls and pre-period gradient tests
  - Alternative capital-distance definitions
  - Placebo dates and placebo political centers
- type: transition-and-anticipation
  basis: documented
  condition: >
    Palace construction, court deliberation, and northern military preparation preceded
    the 1421 designation; Nanjing retained a secondary-capital role afterward.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Exclude transition periods and estimate alternative post dates
  - Separate formal designation from administrative/personnel relocation
  - Keep Nanjing as its own exposure state
- type: historical-boundary-and-data-construction
  basis: documented
  condition: >
    County boundaries, names, population registers, and observation years vary across
    dynasties. The 240-county panel and its interpolation/crosswalk choices can affect
    both distance and population measures.
  evidence_refs:
  - E2
  - E3
  - E4
  possible_diagnostics:
  - Reconstruct source ledgers and historical GIS
  - Alternative county concordances and balanced panels
  - Report missingness and interpolation explicitly
- type: war-frontier-and-spatial-confounding
  basis: documented
  condition: >
    Northern defense, wars, migration, canals, delivery routes, and frontier garrisons
    may change with or independently of the capital move and can be spatially correlated
    with distance to Beijing.
  evidence_refs:
  - E2
  - E3
  possible_diagnostics:
  - War and frontier controls or exclusions
  - Route and military-garrison mechanisms with separate timing
  - Spatially robust inference and regional placebos
- type: persistence-and-later-shocks
  basis: inferred
  condition: >
    Qing institutions, modern administrative changes, industrialization, railways, and
    later capital policies can transmit, alter, or replace any original 1421 channel.
  evidence_refs:
  - E2
  - E3
  possible_diagnostics:
  - Keep Ming, Qing, and modern estimands separate
  - Audit later institutions and modern boundary crosswalks
  - Test persistence under alternative later-period controls
empirical_requirements:
  contract_version: 1
  population: Historical Chinese counties and their harmonized successors with period-specific population or household observations
  observation_unit: County-period or county-year after historical crosswalk
  geography_level: Historical county and prefecture, with modern successor units for persistence
  time_start: null
  time_end: null
  minimum_frequency: historical period or dynasty; annual where modern data permit
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - Historical county identifier, name, and boundary version
  - Observation period and dynasty
  - Population and household-size measure with source
  - Distance to Beijing and Nanjing
  - Post-1421 indicator and sample inclusion flag
  - War, frontier, delivery-route, and military mechanism measures where used
  required_identifiers:
  - historical_county_id
  - successor_county_id
  - period
  - distance_to_beijing
  - population_source
  treatment_key:
  - distance_to_beijing
  - post_1421
  treatment_source: >
    Official historical records of the Ming capital designation, Lu, Ou, and Zhong's
    paper and working-paper metadata, historical population/household registers, and a
    versioned county concordance. Historical data acquisition, OCR, GIS reconstruction,
    and modern joins belong in Econ Data Know-How.
  measurement_risks:
  - Historical county names, boundaries, and administrative levels
  - Population-register coverage, interpolation, and household definitions
  - Distance formula, capital coordinates, and period-specific geography
  - Transition timing and residual Nanjing institutions
  - Wars, frontier security, canals, migration, and later infrastructure
  - Spatial correlation and persistence across dynasties
evidence:
- id: E1
  source_type: archive
  citation: 'Capital Museum (Beijing). 2020. 1420: From Nanjing to Beijing, official exhibition description.'
  url: https://www.capitalmuseum.org.cn/exhibition/5fa1658c7a394b6ab12aa0ca3a92f636
  date: 2020
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.announcement
  - timeline.effective
  - timeline.implementation_start
  - timeline.local_timing
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: >
    The official exhibition account records the Yongle 18 (1420) edict that Beijing
    would be the capital from the first day of the next year, the completion of the
    Beijing palace, and the Yongle 19 (1421) first-day designation. It also states that
    Beijing became the primary capital and Nanjing the southern/secondary capital. It
    establishes the event chronology, not the paper's county sample or identification.
- id: E2
  source_type: paper
  citation: 'Lu, Ming, Haijun Ou, and Yuejun Zhong. 2024. "Political governance and urban systems: A persistent shock on population distribution from capital relocation in ancient China." Regional Science and Urban Economics 108:104034. DOI: 10.1016/j.regsciurbeco.2024.104034.'
  url: https://doi.org/10.1016/j.regsciurbeco.2024.104034
  date: 2024
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design_applications.paper
  - design_applications.research_question
  - design_applications.population
  - design_applications.outcome
  verification_status: verified
  access_level: abstract
  locator: >
    The official article metadata and indexed article preview identify the 1421 capital
    relocation, the difference-in-differences design, the 240-county self-constructed
    panel, log population and household measures, the distance-to-Beijing gradient, and
    the delivery and national-security channels. The publisher full text is restricted;
    exact regression and data-construction details remain blockers.
- id: E3
  source_type: paper
  citation: 'Lu, Ming, Haijun Ou, and Yuejun Zhong. 2022/2023. Political Governance and Urban Systems: A Persistent Shock on Population Distribution from Capital Relocation in Ancient China, SSRN working-paper versions 3671649 and 4285965.'
  url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3671649
  date: 2023
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.assumptions
  - design.diagnostics
  - threats.condition
  - threats.possible_diagnostics
  - design_applications.data_used
  - design_applications.empirical_design
  verification_status: verified
  access_level: abstract
  locator: >
    The SSRN landing page records the authors, versions, 54-page working-paper length,
    1421 event, historical county panel, DID design, and stated persistence/robustness
    claim. The downloadable PDF was not independently inspected in this task, and
    working-paper versions differ from the final article; no uninspected detail is used
    as a verified fact here.
- id: E4
  source_type: archive
  citation: 'Library of Congress. Nanjing xing bu zhi, historical local administrative gazetteer record.'
  url: https://www.loc.gov/resource/lcnclscd.2012402101.1A002/?st=gallery
  date: null
  supports:
  - identity.legal_identifiers
  - assignment.unit
  - assignment.exposure_construction
  verification_status: verified
  access_level: metadata
  locator: >
    The catalogued historical gazetteer is an independent archival anchor for the
    Nanjing administrative and secondary-capital setting after the relocation. It does
    not establish the complete 240-county panel, distance formula, or causal estimate.
design_applications:
- paper: 'Political governance and urban systems: A persistent shock on population distribution from capital relocation in ancient China'
  doi: 10.1016/j.regsciurbeco.2024.104034
  journal: Regional Science and Urban Economics
  year: 2024
  research_question: How did relocating the primary political center alter China’s urban system and the spatial distribution of population?
  population: Historical Chinese county-level units in a self-constructed panel reported as 240 counties, followed across selected Ming, later-dynasty, and modern periods.
  outcome: Log local population and log household size, with persistence and mechanism outcomes where the source application provides them.
  data_used:
  - Historical Chinese county population and household records assembled by the authors
  - Historical county locations and distance to Beijing, with a historical administrative concordance
  - Period and dynasty indicators spanning the Ming relocation and later persistence samples
  - Delivery, military/security, war, and related mechanism measures reported in the paper
  treatment_encoding: >
    Distance to Beijing interacted with a post-1421 indicator or equivalent post-
    relocation period coding; the source's exact distance and period definitions require
    full-text/replication recovery. Keep Nanjing and later-dynasty samples separate.
  comparison: >
    The pre-1421 distance-to-Beijing gradient is compared with the post-relocation
    gradient across the same harmonized historical locations; the design is continuous,
    not a binary treated-county comparison.
  empirical_design: >
    Difference-in-differences on historical county population and household measures,
    with persistence estimates and channel analyses for delivery and national security.
    The publisher preview reports a 240-county panel and robustness exercises, but the
    exact fixed effects, clustering, weights, and sample filters remain uninspected.
  assumptions:
  - Historical county locations and population/household measures are comparable across the selected periods
  - The post-1421 distance-gradient change is not entirely generated by coincident wars, migration, routes, or frontier policies
  - Nanjing's residual institutions and transition period are modeled or excluded transparently
  - Persistence estimates distinguish transmission of the original event from later institutions
  threats_addressed:
  - Historical boundary and population measurement
  - War and frontier-security confounding
  - Delivery-route and material-supply channels
  - Alternative periods, locations, and robustness specifications
  evidence_refs:
  - E1
  - E2
  - E3
  - E4
readiness_blockers:
- The final ScienceDirect article is subscriber-restricted; the indexed preview and SSRN abstracts establish the research object but not the complete regression tables, fixed effects, period definitions, distance formula, or replication code.
- The 240-county historical panel, population/household registers, interpolation rules, and historical county concordance have not been independently reconstructed in this repository.
- The official event source verifies the 1420–1421 capital designation, but it does not establish that the relocation was unrelated to every county-level population trend; the paper's identifying assumptions and historical controls must remain explicit.
- Nanjing retained a secondary-capital role, and palace construction, court planning, military preparation, and later wars create transition and channel overlap.
- Historical data acquisition, OCR/GIS reconstruction, and modern successor joins belong in Econ Data Know-How; this record specifies the data contract without duplicating those assets.
method_transfer: null
superseded_by: null
deprecation_reason: null
---

## Institutional Background

The Ming dynasty initially governed from Nanjing (Yingtian). The official Capital Museum account records a Yongle-era decision to make Beijing the primary capital from the first day of 1421: the Beijing palace had been completed, the court issued the 1420 edict, and Beijing was formally designated the capital while Nanjing retained a secondary-capital status. This is a change in the location of central political authority, not a modern city-development program. [E1]

## What Changed

The empirical object is the relocation of the primary political center from Nanjing to Beijing. That change altered the geography of administrative delivery, military protection, fiscal/material flows, and information. The legal designation was concentrated around 1420–1421, but the construction and movement of institutions preceded and followed it. A researcher should keep the formal date, transition period, and later persistence clocks separate. [E1; E2]

## Implementation and Assignment

Lu, Ou, and Zhong use a self-constructed historical panel of 240 county units and relate local population and household measures to distance from Beijing before and after the relocation. The source application is a continuous-exposure DID: the post-period changes the distance gradient rather than assigning a binary treatment to a named group. The paper follows the pattern into later dynasties and modern China, but those later samples have distinct administrative and institutional environments. [E2; E3]

The practical treatment key is therefore `historical_location × distance_to_Beijing × post_1421`, accompanied by the county concordance and population-source version. Distance to Nanjing, delivery routes, military garrisons, wars, and material supply are separate fields. A modern county centroid or a present-day Beijing-distance measure is not a substitute for the historical geography.

## Why This Creates Empirical Variation

The variation lets a researcher ask whether moving the center of political governance changed the relationship between a locality and the national urban system. The paper reports that the distance-to-Beijing effect on population turns from positive before the relocation to negative afterward, with channels described as delivery and national security. The design can therefore inform work on political centralization, historical urban systems, regional population, and long-run institutional persistence. [E2]

The useful object is conditional, not a universal claim that proximity to a capital is beneficial. The coefficient combines the formal capital move with the court's military, administrative, and material reorganization, and later persistence estimates add subsequent dynastic and modern changes. Those components must be separated when the research question concerns only one channel.

## Identification Risks

The Yongle court did not select Beijing for an experiment. Political succession, northern defense, palace construction, transport, and the existing urban hierarchy all helped shape the relocation and may also predict population trends. Palace construction and deliberation preceded the formal designation; Nanjing continued to operate as a secondary capital. Wars, migration, canals, and later institutions can create the same distance gradient or transmit the original shock. [E1; E2; E3]

Historical measurement is a second central risk. County names and boundaries change across dynasties, population registers are uneven, and the 240-county panel's interpolation and crosswalk choices determine which locations are compared. The final article's complete methods and replication files remain inaccessible in the inspected sources, so a new application must reproduce those choices before treating the headline estimate as portable. [E2; E3; E4]

## Data Requirements

A usable application needs historical county identifiers and successor links, period-specific population and household measures, coordinates or polygons, distance to Beijing and Nanjing, the post-1421 clock, and source-level metadata for every population observation. Mechanism work adds dated delivery routes, military garrisons, wars, migration, and material-supply measures. The acquisition and reconstruction of those assets belong in `Econ Data Know-How`; this record preserves the join contract and the reasons a historical join can fail.

## Evidence Notes

E1 is an official Capital Museum account that establishes the 1420 edict, the 1421 designation, and the continued secondary-capital role of Nanjing; it does not establish the paper's county sample or identification. E2 is the official 2024 RSUE record and indexed article preview: it establishes the paper identity, 240-county panel, distance-gradient DID, headline direction, and mechanisms, but the full article is access-restricted. E3 is the authors' SSRN landing page and abstract for earlier working-paper versions; it corroborates the research object and stated robustness but was not treated as evidence for uninspected tables or data details. E4 is an independent archival catalog anchor for the Nanjing administrative setting; it does not prove the full historical crosswalk. None of these sources turns the capital decision into a universally valid or randomly assigned shock.
