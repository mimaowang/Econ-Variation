---
schema_version: 2
id: china-shanghai-jingan-zhabei-district-consolidation
name: Shanghai Jing'an–Zhabei Municipal-District Consolidation
aliases:
- Jing'an–Zhabei district merger
- Shanghai two-district consolidation
- 撤二建一（静安区与闸北区）
- 新静安区成立
status: grounded
provenance:
  task_id: task-e6f648e1ff1b
scope:
  country: China
  regions:
  - Former Jing'an District, Shanghai
  - Former Zhabei District, Shanghai
  - Nearby Shanghai districts used as the boundary comparison in the paper
  domains:
  - regional-economics
  - urban-economics
  - administrative-geography
  - local-government
  - public-services
  - housing
  - spatial-economics
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: >
    This case is a specific 2015 consolidation of two existing Shanghai municipal
    districts. The State Council abolished the former Jing'an and Zhabei districts
    and created a new Jing'an district covering both territories. The regional and
    urban variation is the change in one administrative boundary and governance unit,
    used by Yu and Hou (2021) with resale-property transactions and a boundary DID.
    It is distinct from county-to-urban-district conversion, city expansion, and
    housing-purchase restrictions.
identity:
  instrument: >
    The 2015 "withdraw two, establish one" consolidation (撤二建一) of Shanghai's
    former Jing'an District and former Zhabei District. The new Jing'an District
    inherited the two former administrative territories; it was not a new county,
    development zone, or housing subsidy. The recorded empirical object is the legal
    consolidation and its local public-service, reputation, and boundary effects.
  authority: >
    The State Council approved the administrative adjustment, and the Shanghai
    municipal government organized the transition and the new district government.
    District agencies, schools, hospitals, fiscal offices, and other public-service
    units were subsequently reorganized under the new Jing'an administration. The
    legal approval is an administrative decision selected by governments, not a
    randomized assignment.
  legal_identifiers:
  - State Council approval on adjustment of Shanghai administrative divisions, Guohan [2015] No. 183 (国函〔2015〕183号)
  - Shanghai "撤二建一" implementation and transition announcements, November 2015
  - Shanghai Jing'an District 13th Five-Year Plan, 2016, describing the 2015 consolidation
  implementation_regime: >
    The former Jing'an and Zhabei were abolished as separate municipal districts and
    a new Jing'an District was established over the union of their territories. The
    transition was announced and organized in late 2015, while the economic effects
    of service integration, fiscal coordination, and reputation may have unfolded
    over several subsequent years. The legal boundary and the later depth of
    integration are therefore separate clocks.
  assignment_mechanism: >
    A property, household, firm, or public-service unit inherits exposure from the
    historical district polygon and transaction or observation date. Before the
    reform, the same address belonged to either Jing'an or Zhabei; after the reform,
    both fell inside the new Jing'an jurisdiction. The paper's boundary application
    compares transactions near the old district boundary with a spatial comparison
    outside the consolidated area; the exact bands and polygon version must be
    retained rather than inferred from today's map.
  parent: null
  related_variations:
  - china-city-county-merger-consolidation
  - china-jinan-lixia-preschool-fee-reduction
timeline:
  announcement: '2015-10-13'
  effective: '2015-11-04'
  implementation_start: '2015-11-04'
  implementation_end: null
  local_timing: >
    The State Council approval is dated October 2015 in official district materials
    and is identified as Guohan [2015] No. 183 in the approval record. Shanghai held
    the formal "withdraw two, establish one" work meeting on 4 November 2015. The
    paper describes the consolidation as a 2015 event; its exact transaction-level
    post date and any announcement anticipation window are not exposed in the
    accessible abstract and must be recovered from the full article.
  anticipation: >
    The adjustment was discussed and approved before the November transition meeting.
    Residents, schools, firms, and housing-market participants could respond to the
    approval or public preparation before the administrative switch. A post-4-November
    indicator is therefore not evidence that no earlier prices or transactions moved.
  last_verified: '2026-08-13'
assignment:
  unit: >
    The institutional unit is a municipal district and its historical territory. The
    paper's observation unit is a resold apartment transaction; other applications
    may use a household, firm, school, public-service facility, or district-year. Keep
    former-Jing'an and former-Zhabei origin separate even though both become part of
    the new district.
  treated: >
    A location inside the union of former Jing'an and former Zhabei is consolidation-
    exposed after the chosen legal or operation date. For the paper's heterogeneous
    application, transactions are additionally classified by whether they were in
    the less-developed former Zhabei or the more-developed former Jing'an. The legal
    exposure is territorial; it does not mean every resident used a new public service
    or that every property experienced the same intensity.
  comparison_pool: >
    The paper uses a boundary difference-in-differences design with nearby Shanghai
    properties outside the consolidated area as the spatial comparison. The exact
    selected boundary, bandwidths, exclusion zones, and whether the control side is
    drawn from one or multiple neighboring districts remain full-text recovery items.
    A comparison property can still receive citywide Shanghai policies or market
    spillovers and is not automatically untreated in every channel.
  rule: >
    Construct a historical union polygon from the former Jing'an and Zhabei boundaries,
    assign each property to its pre-reform district, and turn on the consolidation
    after the documented legal/operation clock. Preserve the old border as a boundary
    variable and distinguish it from the outer edge of the union. Do not infer treatment
    from a current Jing'an address, a property price increase, or a district name alone.
  intensity: >
    The core exposure is binary and territorial. Useful secondary margins include
    former-district origin, distance to the old boundary, distance to major public
    services, pre-reform development gap, and years since consolidation. These are
    heterogeneity or mechanism measures, not substitutes for the legal treatment.
  exemptions:
  - Transactions before the selected announcement, legal, or operation clock
  - Addresses outside the historical union polygon or without an auditable geocode
  - Properties whose historical district cannot be reconstructed after boundary changes
  - Non-residential observations when the outcome is a residential property value
  - Any observation dropped by the paper's transaction-quality, repeat-sale, or price filters
  compliance: >
    The legal consolidation is mandatory for the territory, but service and fiscal
    integration can be gradual. Schools, hospitals, budgets, land planning, and
    administrative staff may have different transition dates. A property inside the
    union is therefore an intent-to-expose measure, not proof of realized equal access
    to former-Jing'an amenities or of a particular household's take-up.
  exposure_construction: >
    Archive the former-district polygons and successor union, geocode every transaction
    to a stable property or residential-compound identifier, record transaction date,
    old district, distance to the old boundary, and post clock, then reproduce the
    paper's boundary bands and controls. For service or firm applications, add the
    relevant school, hospital, firm, or fiscal crosswalk and preserve each agency's
    own implementation date.
  required_identifiers:
  - Historical former-Jing'an and former-Zhabei boundary polygons and successor union
  - Stable property, residential-compound, address, or geocoded transaction identifier
  - Transaction date, price, floor area, structural characteristics, and listing/transaction status
  - Pre-reform district code, distance to old boundary, and selected boundary-band flag
  - Successor district and any school, hospital, fiscal, firm, or service identifier used in a mechanism
  - Approval, public announcement, transition, and agency-specific implementation dates
  spillovers: >
    Consolidation can change public-service access, school and hospital demand,
    commuting, land use, firm location, local reputation, and housing search across
    the old boundary. Prices in Zhabei may rise through access or reputation while
    Jing'an amenities are diluted, and nearby districts can receive displaced demand.
    These cross-border effects are mechanisms and possible comparison contamination,
    not evidence that the boundary design has no spillovers.
research_compatibility:
  outcome_domains:
  - Residential property prices, rents, and transaction composition
  - Capitalization of local public services and administrative status
  - Housing-market integration and boundary effects
  - School, hospital, transport, and other public-service access
  - Fiscal coordination, land use, firm location, and urban development
  - Reputation, migration, sorting, and neighborhood upgrading
  affected_populations:
  - Households and buyers in former Jing'an and Zhabei
  - Homeowners, renters, developers, and brokers near the old boundary
  - Schools, hospitals, firms, and public agencies in the two former districts
  - Residents and property markets in neighboring Shanghai districts
  mechanism_channels:
  - Economies of scale and coordinated public-service provision
  - Redistribution or dilution of access to former-Jing'an amenities
  - Reputation and place-label change for former Zhabei
  - Removal of an administrative boundary and increased factor mobility
  - Land-use, fiscal, infrastructure, and firm-location coordination
  - Residential sorting and capitalization into property values
  best_for:
  - Boundary difference-in-differences of an urban administrative consolidation
  - Local public-service or administrative-status capitalization in housing markets
  - Heterogeneous effects by former district development and distance to the old border
  - Studies separating legal boundary change from later service integration
  not_good_for:
  - Treating the consolidation as random or as a citywide Shanghai housing shock
  - Treating former Jing'an and former Zhabei as identical exposures
  - Calling a property-side indicator household-level service take-up
  - Estimating long-run fiscal or welfare effects from the short property window alone
  - Combining this record with county-to-district conversions without a distinct legal rule and crosswalk
design:
  claim_type: causal
  affordances:
  - A single documented administrative consolidation with a historical boundary
  - Two pre-reform districts with different development and public-service baselines
  - High-frequency resale transactions with detailed property characteristics and geography
  - A local spatial comparison around the old boundary
  - Separate former-Zhabei and former-Jing'an effects for mechanism exploration
  candidate_designs:
  - Boundary difference-in-differences using properties near the old district boundary
  - Hedonic property-value event study with former-district-by-post interactions
  - Separate capitalization estimates for former Zhabei and former Jing'an
  - Housing-market integration or boundary-effect design using price gaps across the old border
  - Service, school, hospital, or firm-location designs with agency-specific implementation clocks
  identifying_variation: >
    The paper's variation is the 2015 replacement of two adjacent municipal districts
    by one new Jing'an District. A property just inside the relevant boundary becomes
    part of the consolidated administrative unit after the reform, while nearby
    properties outside the selected spatial comparison remain under their original
    district governments. The legal change is documented; the plausibility of the
    local comparison depends on the recovered polygon, bandwidth, timing, and checks.
  primary_strategy: >
    Yu and Hou use resold apartment transaction micro-data from Lianjia and a boundary
    difference-in-differences design. The publisher and independent abstract report a
    roughly 1.6 percent increase for the consolidated region, a 4.8 percent increase
    in former Zhabei, and no significant effect in former Jing'an, with an expanding
    Zhabei effect over time. Reproduction should recover the exact old-boundary bands,
    transaction window, property filters, fixed effects, and post clock before treating
    those numbers as a replicated estimate.
  estimand: >
    The local capitalization effect of the Jing'an–Zhabei consolidation on resale
    property values near the chosen boundary, with separate local effects for former
    Zhabei and former Jing'an. This is an equilibrium housing-market estimand that may
    include public-service, reputation, sorting, and land-market responses; it is not
    a pure effect of administrative cost savings or a direct household-welfare effect.
  treatment_variable: >
    Inside_historical_union multiplied by post_consolidation, with former_district,
    signed distance to the old boundary, selected bandwidth, and separate announcement,
    approval, transition, and operation clocks. For mechanism work, add public-service
    or agency-specific treatment dates rather than folding them into the legal dummy.
  comparison_logic: >
    Use properties on the comparison side of the historical boundary within the paper's
    recovered bands, condition on property characteristics and local geography, and
    check pre-trends and boundary smoothness. Compare former Zhabei and former Jing'an
    separately when their baseline levels or mechanisms differ. The paper's exact
    control-band construction remains a blocker until full text or replication files
    are recovered.
  estimation_notes: >
    Keep transaction-level hedonic estimates, boundary effects, and former-district
    heterogeneity separate. Interpret the reported effect as capitalization and local
    equilibrium incidence. Any service, fiscal, or firm mechanism requires its own
    dated crosswalk and should not be inferred solely from the housing coefficient.
  assumptions:
  - Property characteristics and unobserved amenities vary smoothly at the chosen boundary absent consolidation
  - No other boundary-specific policy, construction, school, or land shock begins at the same time
  - Historical polygons, geocodes, transaction dates, and Lianjia coverage are measured consistently
  - The chosen post clock captures the relevant exposure without unmeasured anticipation dominating it
  - Cross-border sorting and spillovers are limited or interpreted as part of the local equilibrium estimand
  - Former-district heterogeneity is modeled rather than hidden in one pooled coefficient
  diagnostics:
  - Pre-trend and boundary-smoothness plots for prices and property characteristics
  - Alternative bandwidths, distance controls, and nearby comparison boundaries
  - Announcement, approval, transition, and first-full-year event clocks
  - Separate former-Zhabei and former-Jing'an estimates and time-since-treatment effects
  - Transaction composition, listing, repeat-sale, and Lianjia coverage checks
  - School, hospital, infrastructure, fiscal, land, and neighboring-district policy audit
  - Sorting, migration, firm-location, and spatial-spillover checks
design_profiles:
- id: property-boundary-capitalization
  label: Resale-property boundary capitalization
  design_families:
  - geographic-boundary-did
  - hedonic-event-study
  when_to_use: >
    Use when a historical union polygon, the old district boundary, geocoded resale
    transactions, and the paper's comparison bands can be reconstructed.
  outcome_domains:
  - resale property values
  - transaction composition
  - housing-market boundary effects
  requirements:
    population: Resold residential apartments in former Jing'an, former Zhabei, and the recovered comparison area
    observation_unit: Property transaction
    geography_level: Historical municipal-district boundary and property/compound
    time_start: null
    time_end: null
    minimum_frequency: daily or monthly
    minimum_pre_periods: 2
    minimum_post_periods: 2
    required_fields:
    - Historical district polygon and old boundary
    - Property or compound identifier and geocode
    - Transaction date, price, floor area, and structural characteristics
    - Former-district origin, signed distance, band, and post clock
    required_identifiers:
    - stable_property_or_compound_id
    - transaction_date
    - historical_district_code
    - boundary_version
    treatment_key:
    - inside_historical_union
    - post_consolidation
    - former_district
    - signed_distance_to_old_boundary
- id: public-service-integration
  label: Consolidation and public-service integration
  design_families:
  - district-panel
  - mechanism-event-study
  when_to_use: >
    Use for schools, hospitals, fiscal accounts, infrastructure, or firms only after
    each agency's integration date and historical jurisdictional join are independently
    archived; the legal consolidation date alone is not a service-treatment date.
  outcome_domains:
  - public-service access
  - fiscal coordination
  - firm location and urban development
  requirements:
    population: Residents, firms, schools, hospitals, or district-year administrative observations in Shanghai
    observation_unit: District-year, facility-year, household-year, or firm-year
    geography_level: Historical district and successor Jing'an boundary
    time_start: null
    time_end: null
    minimum_frequency: annual
    minimum_pre_periods: 2
    minimum_post_periods: 2
    required_fields:
    - Former and successor district codes
    - Agency-specific implementation date and service/fiscal outcome
    - Historical crosswalk and unit identifier
    required_identifiers:
    - historical_district_code
    - successor_district_code
    - agency_or_unit_id
    - observation_year
    treatment_key:
    - legal_consolidation_date
    - agency_implementation_date
    - former_district
threats:
- type: endogenous-administrative-selection
  basis: inferred
  condition: >
    Shanghai selected this downtown consolidation for planning, governance, resource,
    and development reasons that may also predict housing-price trends and public-
    service changes. The administrative decision does not make the treated territory
    a random draw.
  evidence_refs:
  - E1
  - E2
  - E4
  possible_diagnostics:
  - Pre-reform price and amenity trends
  - Other Shanghai boundary adjustments and placebo boundaries
  - Planning, fiscal, investment, and service covariate audit
- type: boundary-sorting-and-spillover
  basis: inferred
  condition: >
    Households, firms, schools, and developers can sort across the old border, while
    the consolidation itself may change prices and services on both sides. A nearby
    control property may thus be partially exposed.
  evidence_refs:
  - E4
  - E5
  possible_diagnostics:
  - Boundary smoothness and transaction-composition checks
  - Alternative bands and wider spatial rings
  - Migration, school choice, commuting, and neighboring-district outcomes
- type: timing-and-anticipation
  basis: documented
  condition: >
    The October approval, public preparation, and November transition are distinct
    dates. Price changes may precede the formal work meeting, and service integration
    may lag the legal change.
  evidence_refs:
  - E1
  - E2
  - E3
  possible_diagnostics:
  - Separate approval, announcement, transition, and first-full-year event clocks
  - Lead coefficients and a pre-approval placebo window
  - Agency-specific implementation dates
- type: concurrent-local-policy
  basis: inferred
  condition: >
    Shanghai housing controls, school admissions, transport construction, land
    redevelopment, fiscal changes, and other district policies may coincide with the
    consolidation and be concentrated near the old boundary.
  evidence_refs:
  - E1
  - E2
  - E4
  possible_diagnostics:
  - Dated policy and construction inventory
  - Exclude or separately code overlapping projects and school boundaries
  - Alternative comparison boundaries and local trends
- type: platform-and-property-measurement
  basis: reported
  condition: >
    Lianjia coverage, geocoding, property characteristics, transaction quality, and
    listing selection may change over time or differ across districts. Resale prices
    are not a complete census of all housing or household welfare.
  evidence_refs:
  - E5
  possible_diagnostics:
  - Platform coverage and missingness by district and date
  - Property and transaction composition checks
  - Alternative price definitions and repeat-sale restrictions
- type: mechanism-underdetermination
  basis: reported
  condition: >
    Economies of scale, public-service redistribution, and reputation can all move
    property values. The paper's reported former-district pattern is consistent with
    reputation, but the accessible evidence does not isolate that channel from service
    transfers or scale effects.
  evidence_refs:
  - E5
  possible_diagnostics:
  - Direct service, school, hospital, fiscal, and land outcomes
  - Former-district and amenity heterogeneity
  - Mediation evidence with explicit timing and measurement assumptions
empirical_requirements:
  contract_version: 1
  population: Resale properties and, where mechanisms are studied, households, services, firms, and district observations in Shanghai
  observation_unit: Property transaction, with optional district-year, facility-year, household-year, or firm-year extensions
  geography_level: Historical municipal-district boundary, property/compound, and successor Jing'an district
  time_start: null
  time_end: null
  minimum_frequency: daily or monthly for property transactions; annual for administrative panels
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields:
  - Historical former-district and successor polygons with source dates
  - Property/compound identifier, geocode, transaction date, price, and characteristics
  - Old-boundary distance and the exact paper bandwidth/control definition
  - Approval, transition, and agency-specific implementation dates
  - Service, fiscal, land, school, hospital, firm, migration, or neighborhood variables for mechanism work
  required_identifiers:
  - historical_district_code
  - successor_district_code
  - stable_property_or_compound_id
  - transaction_date_or_observation_year
  - boundary_version
  - agency_or_unit_id_where_applicable
  treatment_key:
  - inside_historical_union
  - post_consolidation
  - former_district
  - signed_distance_to_old_boundary
  treatment_source: >
    State Council and Shanghai/Jing'an administrative-division documents, the paper's
    Lianjia transaction application, and a versioned historical boundary crosswalk.
    Property-data acquisition and provider restrictions belong in Econ Data Know-How.
  measurement_risks:
  - Legal approval, transition, and service integration have different dates
  - Current Jing'an geometry cannot replace the pre-2015 district polygons
  - Lianjia transactions may be selected and platform coverage may change
  - Boundary-side properties can differ in schools, amenities, redevelopment, and sorting
  - The accessible paper record does not expose the complete sample window, bands, or raw joins
evidence:
- id: E1
  source_type: implementation-document
  citation: Shanghai Jing'an District Government. 2016-07-28. Jing'an District 13th Five-Year Plan (上海市静安区国民经济和社会发展第十三个五年规划纲要).
  url: https://www.jingan.gov.cn/govxxgk/JA0/2016-08-25/47938347-9f92-415b-ac8e-431e327b698a.html
  date: '2016-07-28'
  supports:
  - identity.instrument
  - identity.authority
  - identity.implementation_regime
  - timeline.announcement
  - timeline.local_timing
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: >
    The official district plan describes the 2015 municipal decision to abolish the
    former Zhabei and Jing'an districts and establish the new Jing'an District, and
    places the new district at the start of its post-consolidation planning period.
    It establishes the local institutional context but does not provide property
    polygons, transaction data, or the paper's boundary bands.
- id: E2
  source_type: implementation-document
  citation: Xinhua/People's Daily. 2015-11-04. Shanghai abolishes Zhabei and Jing'an districts and establishes a new Jing'an District.
  url: https://www.xinhuanet.com/politics/2015-11/04/c_128392377.htm
  date: '2015-11-04'
  supports:
  - identity.instrument
  - identity.authority
  - identity.implementation_regime
  - timeline.effective
  - timeline.implementation_start
  - timeline.local_timing
  - assignment.rule
  - assignment.compliance
  verification_status: verified
  access_level: full-text
  locator: >
    The contemporaneous report records the 4 November 2015 Shanghai work meeting,
    the State Council approval, the "withdraw two, establish one" transition, and
    the stated goals of improving administrative efficiency, coordinating resources,
    and extending services. It does not establish that any one mechanism caused a
    property-price response.
- id: E3
  source_type: policy-document
  citation: State Council. 2015. Approval on adjusting part of Shanghai's administrative divisions, Guohan [2015] No. 183 (国函〔2015〕183号), reproduced in the public legal archive.
  url: https://zh.wikisource.org/wiki/%E5%9B%BD%E5%8A%A1%E9%99%A2%E5%85%B3%E4%BA%8E%E5%90%8C%E6%84%8F%E4%B8%8A%E6%B5%B7%E5%B8%82%E8%B0%83%E6%95%B4%E9%83%A8%E5%88%86%E8%A1%8C%E6%94%BF%E5%8C%BA%E5%88%92%E7%9A%84%E6%89%B9%E5%A4%8D_%282015%E5%B9%B4%29
  date: '2015-10-13'
  supports:
  - identity.legal_identifiers
  - identity.instrument
  - timeline.announcement
  - assignment.rule
  verification_status: reported
  access_level: full-text
  locator: >
    The reproduced approval states that the former Shanghai Zhabei and Jing'an
    districts are abolished and a new Jing'an District is established over their
    former administrative areas. Treat the archive as a convenient transcription of
    the legal text and replace it with an official government scan if one is recovered.
- id: E4
  source_type: paper
  citation: 'Yu, Huayi, and Yujuan Hou. 2021. "A tale of two districts: The impact of district consolidation on property values in Shanghai." Regional Science and Urban Economics 87:103647. DOI: 10.1016/j.regsciurbeco.2021.103647.'
  url: https://ideas.repec.org/a/eee/regeco/v87y2021ics0166046221000077.html
  date: 2021
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.implementation_start
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design_applications.research_question
  - design_applications.outcome
  verification_status: verified
  access_level: abstract
  locator: >
    IDEAS/RePEc reproduces the abstract and article identity: the 2015 consolidation
    of Jing'an and Zhabei, resold property transaction micro-data, boundary DID, a
    1.6 percent overall increase, a 4.8 percent increase in former Zhabei, no
    significant effect in former Jing'an, and an expanding Zhabei effect. The
    publisher full text is restricted, so exact bands, sample dates, filters, and
    estimators remain unresolved.
- id: E5
  source_type: paper
  citation: 'ScienceDirect article page and indexed sections for Yu and Hou (2021), Regional Science and Urban Economics 87:103647.'
  url: https://www.sciencedirect.com/science/article/abs/pii/S0166046221000077
  date: 2021
  supports:
  - identity.instrument
  - assignment.exposure_construction
  - assignment.required_identifiers
  - research_compatibility.outcome_domains
  - design.affordances
  - design.candidate_designs
  - design.estimation_notes
  - empirical_requirements.required_fields
  verification_status: reported
  access_level: abstract
  locator: >
    The indexed article text identifies Lianjia resold-apartment micro-data, daily
    transaction records with property characteristics and geography, the three
    mechanisms considered (scale, public-service transfer, and reputation), and the
    boundary DID robustness discussion. These details remain paper-reported until
    the full article or replication materials are inspectable.
- id: E6
  source_type: paper
  citation: DOI metadata for Yu and Hou, Regional Science and Urban Economics 87 (2021), article 103647.
  url: https://doi.org/10.1016/j.regsciurbeco.2021.103647
  date: 2021
  supports:
  - identity.instrument
  - design.primary_strategy
  - design.estimand
  - design_applications.doi
  verification_status: verified
  access_level: metadata
  locator: >
    DOI metadata establishes the authors, title, journal, volume, article number,
    year, and DOI. Substantive application claims are attributed to E4 and E5.
design_applications:
- paper: 'A tale of two districts: The impact of district consolidation on property values in Shanghai'
  doi: 10.1016/j.regsciurbeco.2021.103647
  journal: Regional Science and Urban Economics
  year: 2021
  research_question: How did the consolidation of Shanghai's former Jing'an and Zhabei districts affect nearby resale property values and the boundary between the two former districts?
  population: Resold residential apartments in the former districts and the paper's nearby Shanghai comparison area; exact transaction window and filters remain to be recovered.
  outcome: Transaction-level property value or price, with heterogeneous estimates for the consolidated region, former Zhabei, and former Jing'an.
  data_used:
  - Lianjia resold-apartment transaction micro-data
  - Property characteristics and geographic information reported by the paper
  - Historical former-district boundary and successor union
  - Shanghai district or neighborhood controls and comparison-band geometry
  treatment_encoding: Historical union of former Jing'an and Zhabei multiplied by a post-consolidation indicator, with former-district origin and distance/band around the old boundary; exact original coding remains pending full-text recovery.
  comparison: Nearby properties outside the consolidated area on the paper's recovered boundary side and bandwidths; the exact comparison set is not visible in the accessible abstract.
  empirical_design: Boundary difference-in-differences with property-level hedonic controls, alternative control groups/bandwidths, and separate former-Zhabei/former-Jing'an estimates as reported by the paper.
  assumptions:
  - Property characteristics and unobserved amenities vary smoothly at the chosen boundary absent consolidation.
  - The historical polygon, geocoder, transaction date, and Lianjia coverage are consistent.
  - Concurrent school, transport, redevelopment, fiscal, and housing policies do not explain the full boundary contrast.
  - Anticipation and cross-border sorting are limited or explicitly incorporated into the estimand.
  - Former-district heterogeneity is modeled rather than treated as noise.
  threats_addressed:
  - Dynamic/pre-trend and parallel-trend checks
  - Alternative control groups and bandwidths
  - Separate former-Zhabei and former-Jing'an estimates
  - Property characteristics and local geographic controls
  - Mechanism discussion for scale, public services, and reputation
  evidence_refs:
  - E4
  - E5
  - E6
method_transfer: null
readiness_blockers:
- The publisher full text and replication package were not accessible through the inspected route. The complete transaction window, sample filters, treatment bands, fixed effects, clustering, and exact post clock remain to be recovered.
- The official local sources establish the consolidation and transition but do not provide a machine-readable historical polygon or property-level geocode crosswalk. The former-district boundary and successor union must be archived before reconstruction.
- The legal decision is selected by Shanghai authorities in a planning and governance context. It should not be described as random, and the boundary comparison must address sorting, redevelopment, school, transport, and other simultaneous changes.
- Lianjia transaction records are a platform sample rather than a census of all housing or household welfare. Acquisition, licensing, and deduplication belong in Econ Data Know-How.
- Public-service, fiscal, reputation, scale, and sorting mechanisms are not separately identified by the accessible abstract; direct mechanism data and agency-specific dates are required for stronger claims.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Shanghai's former Jing'an and Zhabei were two adjacent municipal districts in the
urban core. In 2015, the State Council approved abolishing the two separate districts
and establishing a new Jing'an District over their former territories [E1; E3]. The
municipal transition was formally organized on 4 November 2015, and Shanghai described
the change as a way to coordinate urban functions, resources, and public services [E2].

This is a district-to-district consolidation. It should not be folded into the
repository's county-to-urban-district record: no county was converted here, and the
central empirical boundary is the old border between two already urban districts.
The legal change supplies the institutional treatment; later service and fiscal
integration are mechanisms that may have their own timing [E1; E2].

## What Changed

Before the reform, an address belonged to either Jing'an or Zhabei and interacted with
the two districts' separate administrative and public-service systems. After the
reform, both former territories were governed as the new Jing'an District. The October
approval and November transition are separate clocks, and the paper's exact property-
transaction post date remains unverified [E1; E2; E4].

Yu and Hou use resold apartment transactions and report a 1.6 percent increase in
property values for the consolidated region, a 4.8 percent increase in the less-
developed former Zhabei, and no significant change in the more-developed former
Jing'an. They also report that the Zhabei effect expands over time [E4]. These are
paper-reported estimates, not a claim that all Shanghai housing rose because of the
consolidation.

## Implementation and Assignment

The legal assignment is territorial and document-based: the union of the historical
Jing'an and Zhabei polygons becomes the new Jing'an jurisdiction. A property-level
application therefore needs the old district polygon, a successor union, a geocode,
and a transaction date. Former-district origin matters because the paper reports
different effects for Zhabei and Jing'an [E3; E4].

The paper's boundary DID uses nearby properties outside the consolidated area as a
spatial comparison. Until the full article is recovered, the exact bands, boundary
segments, exclusion zones, and treatment clock should remain open fields rather than
being reconstructed from a modern map. A property inside the union is exposure to a
new administrative regime, not proof that its household gained a particular school,
hospital, or fiscal benefit.

## Why This Creates Empirical Variation

The consolidation changes the jurisdiction while leaving a visible historical border
and two areas with different starting conditions. A local property comparison can
therefore study whether administrative integration is capitalized into prices and
whether the response differs between a formerly less-developed and a formerly more-
developed district. The paper discusses economies of scale, redistribution of public
services, and reputation as possible channels [E5].

The variation is useful for a research decision only when the layers are kept apart:
the legal boundary is the treatment, the old border and nearby properties define a
candidate comparison, Lianjia provides the application data, and the mechanisms need
their own dated outcomes. This prevents a housing-price coefficient from being read
as a pure administrative-cost or welfare effect.

## Identification Risks

Shanghai chose the consolidation for planning and governance reasons, so treated
territories were not selected by a lottery. Residents and firms could anticipate the
approval, sort across the old border, or respond to redevelopment before the formal
transition. Public services, schools, transport projects, fiscal changes, and housing
policies may also change at the same time [E1; E2].

The Lianjia platform supplies detailed transaction observations, but platform coverage
and listing composition can change across districts and dates. Finally, the reported
Zhabei pattern is consistent with a reputation channel but does not by itself separate
reputation from public-service transfer, scale economies, land-market responses, or
sorting [E4; E5].

## Data Requirements

The minimum property contract needs the historical former-district polygons, successor
union, old-boundary geometry, stable property or compound identifiers, geocodes,
transaction dates, prices, and structural characteristics. It must preserve former
district, signed distance, bandwidth, and separate approval, transition, and post
clocks. A mechanism study additionally needs school, hospital, fiscal, land, firm,
migration, or neighborhood identifiers and their own implementation dates.

The Lianjia acquisition and any restricted property data belong in `Econ Data Know-How`;
this record keeps the institutional exposure and the join contract. A fresh agent
should recover the paper's exact sample and boundary construction before describing
the application as replicated.

## Evidence Notes

E1 is an official Jing'an district planning document. It establishes the 2015 municipal
decision and the new district's post-consolidation institutional context, but it does
not establish the paper's transaction sample or boundary bands. E2 is a contemporaneous
Xinhua/People's Daily report of the 4 November transition; it establishes the formal
implementation meeting and stated governance objectives, but not a property-price
effect. E3 is a public transcription of the State Council approval and establishes the
legal predecessor/successor relationship; it should be replaced by an official scan if
one becomes available.

E4 is the independent IDEAS/RePEc abstract for Yu and Hou. It establishes the paper
identity, 2015 consolidation, Lianjia resale-transaction application, boundary DID,
and reported heterogeneous results, but the publisher full text is restricted. E5 is
the publisher-indexed article page and reports additional data and mechanism details;
those remain attributed until the full article or replication files are inspectable.
E6 is DOI metadata only and establishes bibliographic identity, not substantive claims.

The soft recency marker for this application is 2021. It may help order later searches,
but it cannot replace the historical boundary, exact timing, or evidence needed for a
usable spatial design.
