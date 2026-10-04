---
schema_version: 2
id: china-fukushima-nuclear-accident-land-market-risk-perception
name: Fukushima Nuclear Accident (March 2011) as a Risk-Perception Shock to Land Markets near Chinese Nuclear Power Plants
aliases:
- 福岛核事故 中国核电厂周边土地市场 风险认知
- Zhu-Deng-Zhu-He RSUE 2016 Fukushima land markets China
- FNA China land price distance-band DID
status: grounded
provenance:
  task_id: task-92455edec324
scope:
  country: China
  regions:
  - Coastal and southern provinces hosting nuclear power plant sites (Guangdong, Zhejiang, Jiangsu, Fujian, Liaoning, Shandong, Hainan and others with operating, under-construction, or planned plants as of March 2011)
  domains:
  - environment
  - infrastructure-urban
  - climate-energy
  - risk-perception
  - land-markets
  variation_type: event-shock
  knowledge_role: global-china-variation
  china_relevance: >
    A foreign disaster — the 2011-03-11 Fukushima Daiichi nuclear accident in
    Japan — is used as a common-time information shock that changed perceived
    nuclear-safety risk for Chinese land buyers; exposure varies with each land
    parcel's distance to the nearest Chinese nuclear power plant. The authors
    interpret the response as updated risk perception and report that China
    was not directly affected by earthquake destruction or contamination
    [E1, Introduction, reported claim]. This is not an independently verified
    exclusion of every physical or policy channel: China's concurrent safety
    inspection and approval suspension are documented [E3].
identity:
  instrument: >
    The Fukushima Daiichi nuclear accident triggered by the 2011-03-11
    magnitude-9.0 Tohoku earthquake and tsunami (INES level 7; hydrogen
    explosions and radioactive releases over 12-15 March 2011; 20 km
    evacuation zone) [E2, verified event facts]. In the Chinese application
    the instrument is the accident's information shock interacting with the
    pre-existing geography of China's nuclear power plants [E1]. The accident
    also triggered a Chinese policy response: the State Council executive
    meeting of 2011-03-16 decided on a comprehensive safety inspection of all
    nuclear facilities, strict review of plants under construction, and a
    suspension of approvals for new nuclear projects (including preparatory
    work) until a nuclear safety plan was approved [E3, verified].
  authority: >
    The shock itself is a natural-technological disaster, not a policy act;
    the relevant Japanese emergency measures were ordered by the Japanese
    government and Fukushima prefecture [E2]. The Chinese-side institutional
    response was decided by the State Council (executive meeting chaired by
    Premier Wen Jiabao, 2011-03-16) and implemented by the National Energy
    Administration, the National Nuclear Safety Administration and related
    agencies [E3].
  legal_identifiers:
  - "State Council executive meeting four decisions on nuclear safety (核电“国四条”), 2011-03-16 — full safety inspection; strict management of operating facilities; comprehensive review of plants under construction; suspension of new project approvals pending the nuclear safety plan [E3]"
  - "Fukushima Daiichi accident, INES level 7 — accident phase formally closed with the declaration of cold shutdown condition in mid-December 2011 [E2]"
  implementation_regime: >
    There is no Chinese rollout regime to encode: every Chinese unit faced the
    same event date. What varies is exposure intensity through distance to the
    nearest nuclear plant. The paper reconstructs the plant stock as of March
    2011 from World Nuclear Association records: it reports 15 operating
    commercial reactors at seven plants, 48 reactors under construction, and
    125 planned reactors, grouped into 45 plant sites used for distance
    matching [E1, reported from the paper's WNA-based classification]. The
    IAEA PRIS registry (reactor names, locations, first grid-connection
    dates) independently corroborates the operating fleet's locations; by
    first grid-connection date before 2011-03-11 it implies 13 operational
    reactors (Daya Bay 1-2, Ling Ao 1-3, Qinshan 1, Qinshan 2-1/2-2/2-3,
    Qinshan 3-1/3-2, Tianwan 1-2), slightly fewer than the paper's 15 because
    of classification of late-commissioning units [E4, verified registry;
    reconciliation is an analytical inference].
  assignment_mechanism: >
    Exposure is assigned by fixed geography crossed with one event date: a
    land parcel is treated if it lies within 0-40 km of the nearest Chinese
    nuclear power plant, and the post-treatment period starts April 2011 (the
    first full month after the accident). Parcels in the 100-140 km ring
    around the same plants form the comparison pool; the 40-100 km donut is
    excluded from the baseline specification [E1, verified in Sections 3-4
    and Tables 3-5].
  parent: null
  related_variations: []
timeline:
  announcement: >
    None — the shock is an unanticipated disaster. The earthquake occurred
    2011-03-11 14:46 JST; a nuclear emergency was declared the same evening
    and evacuation zones expanded to 20 km by 2011-03-12 [E2].
  effective: '2011-03-11'
  implementation_start: '2011-04 (first full post-accident month coded as the short-run treatment window in the paper) [E1]'
  implementation_end: '2011-12 (end of the paper''s dynamic post window; estimated effects are statistically insignificant after April 2011) [E1]'
  local_timing: >
    Common event date for all exposed units. The Chinese policy response
    followed within days: State Council four decisions on 2011-03-16, a
    national safety inspection of operating and under-construction plants
    during 2011 (inspection team active mid-April to early August 2011
    [E3, reported scope]), and new project approvals resumed only after the
    nuclear safety plans were adopted in late 2012 [E1, reported claim].
  anticipation: >
    Essentially none for the accident itself; public attention measured by
    search volume spiked immediately after the accident and decayed within
    one to two months, consistent with the estimated one-month price effect
    [E1, reported from the paper's Figure 1 discussion].
  last_verified: '2026-08-15'
assignment:
  unit: Urban land parcel transaction (primary market, local government as seller)
  treated: >
    Land parcels transacted within 0-40 km of the nearest of 45 Chinese
    nuclear plant sites (operating, under construction, or planned as of
    March 2011) [E1]. The exposure-generating plant set is anchored in
    official reactor registries: IAEA PRIS lists the Chinese reactors with
    locations and first grid-connection dates from which the pre-accident
    operating fleet can be reconstructed [E4].
  comparison_pool: >
    Land parcels transacted in the 100-140 km distance band around the same
    plants; the paper verifies effects taper off by 40-60 km, so the outer
    ring is a conservative comparison [E1, Table 3]. Within-band comparisons
    use city-by-distance-band cells, so treated and comparison parcels are
    differenced against same-city outer-ring transactions [E1].
  rule: >
    Binary treatment indicator for the 0-40 km band interacted with
    post-accident month dummies (April 2011 through December 2011); grouped
    windows define April 2011 as short run, May-August 2011 as mid run, and
    September-December 2011 as longer run [E1, Eq. (1)-(4), Tables 4-5].
  intensity: >
    Distance-band gradient: first-month effects are about -25% in the 0-20 km
    band, about -18.5% in the 20-40 km band, and insignificant beyond 40 km,
    which the paper uses to justify the 40 km treatment boundary [E1,
    Table 3, verified]. Heterogeneity by plant status: short-run effects near
    operating and under-construction plants reach about -33%, while effects
    near planned plants are insignificant [E1, Table 6, reported].
  exemptions:
  - Parcels beyond 140 km from any plant are outside the analysis sample entirely [E1]
  - The 40-100 km donut is excluded from baseline treatment/control definitions [E1]
  compliance: >
    Not applicable in the policy sense — exposure is a perceptual state, not a
    regulated behavior. The paper instead checks that estimated effects are
    not driven by seller behavior by re-estimating on auction transactions
    (two-stage auction, English auction, sealed bid; about 56% of
    observations), where local governments cannot easily re-time sales [E1,
    Section 5.4.3, verified].
  exposure_construction: >
    The paper geocodes each parcel's listed address, computes distance to the
    nearest plant site, and matches WNA reactor records (status, construction
    year, capacity) to plants via project names; hedonic controls include
    floor area ratio, land size, lease length, transaction method, land
    origin and class, designated use, 5 km-radius night-light intensity
    (NOAA 2010/2011), and distances to shoreline and inland water [E1,
    Sections 3.1-3.3, verified].
  required_identifiers:
  - Parcel address or coordinates and transaction date (year-month)
  - City code of the parcel (for city-by-distance-band cells)
  - Nuclear plant coordinates, operating status, construction year, capacity as of March 2011
  - Transaction method (negotiated vs auction type)
  spillovers: >
    The information shock is nationwide, so the outer-ring comparison parcels
    may themselves be partially exposed if risk perception travels farther
    than 40 km; the paper's band-by-band search (40-60 km null) bounds this
    concern empirically [E1]. Substitution of demand toward farther parcels
    within the same city is not separately identified [analytical inference].
research_compatibility:
  outcome_domains:
  - Urban land transaction prices (primary market)
  - Housing and property prices near hazardous facilities
  - Public risk perception and its persistence
  - Local government land-sale revenue
  affected_populations:
  - Land buyers (developers) near Chinese nuclear power plants
  - Local governments selling land near plant sites
  - Residents in plant vicinity (via capitalized risk perception)
  mechanism_channels:
  - Risk-perception updating after a foreign disaster
  - Hedonic capitalization of perceived environmental disamenity
  - Short-lived overreaction consistent with prospect-theory-style recency weighting
  best_for:
  - Studying how a salient global disaster transmits into Chinese local asset prices through perception rather than physical exposure
  - Event-study/DID designs needing a sharp common-time shock with geographic exposure gradients
  - Hedonic pricing of hazardous-facility proximity with plant-level heterogeneity (operating vs under-construction vs planned)
  not_good_for:
  - Questions about actual radiation dose or physical disaster damage in China; the paper measures land prices and distance, not those outcomes [E1]
  - A general long-run perception effect inferred from pooled estimates; pooled effects fade after April, but the under-construction subgroup has a significant September-December estimate [E1, Tables 4-6]
  - Designs requiring exogenous variation in plant siting; plant locations are fixed and selected (low-density coastal sites), so levels comparisons across bands are not interpretable without the differencing structure [E1; analytical inference]
design:
  claim_type: causal
  affordances:
  - Sharp common-time event date (2011-03-11) with monthly post windows
  - Geographic exposure gradient in 20 km rings enabling a data-driven boundary search
  - Pre-trend testable window (July 2010 - February 2011) with monthly interactions
  - Plant-status heterogeneity (operating / under construction / planned) as perception-relevant dose variation
  - Auction-only subsample to separate buyer perception from seller timing
  candidate_designs:
  - Dynamic DID of log parcel unit price on 0-40 km treatment x month dummies with city-distance-band and year-month fixed effects
  - Distance-band ring regressions to locate the decay boundary of the effect
  - Triple interactions with plant operating status, construction year, or capacity
  identifying_variation: >
    Cross-sectional distance to pre-existing nuclear plant sites crossed with
    the accident timing; identification rests on common pre-accident price
    trends between the 0-40 km and 100-140 km rings within city-distance-band
    cells. Table 4 columns 1-2 report statistically insignificant
    pre-treatment interactions for October 2010 - February 2011; these fail
    to reject differential trends but do not verify the identifying
    assumption [E1, inspected estimates; analytical inference].
  primary_strategy: >
    Hedonic difference-in-differences: log unit land price on treatment-band
    x post-accident month indicators, land and geographic controls,
    city-distance-band fixed effects and year-month fixed effects; standard
    errors clustered at the city-distance-band group level following
    Bertrand-Duflo-Mullainathan [E1, Section 4 and Tables 3-5, verified].
  estimand: >
    The short-run change in log transaction prices of land parcels within
    0-40 km of Chinese nuclear plants relative to same-city parcels in the
    100-140 km ring after the Fukushima accident, interpreted by the authors
    as the price effect of updated nuclear risk perception [E1].
  treatment_variable: >
    I(0-40 km to nearest plant) x post-accident month indicators; grouped
    versions use April 2011 / May-August 2011 / September-December 2011
    windows; heterogeneity versions interact with plant status, construction
    year, and capacity [E1].
  comparison_logic: >
    Same-city outer-ring parcels (100-140 km) before and after the accident;
    the 40-60 km band's null result supports the choice of the outer ring as
    comparison [E1].
  estimation_notes: >
    Main DID sample N = 34,500 transactions (0-40 km plus 100-140 km) drawn
    from 79,688 transactions within 140 km buffers, themselves filtered from
    305,599 national primary-market transactions July 2010 - December 2011
    [E1, Sections 3.2, 3.4 and Table 4, verified]. Headline result: about
    -0.180 log points in April 2011 (about -16.5% under exact exponentiation;
    the authors report approximately -18% and 2.2 billion RMB of land revenue),
    insignificant thereafter [E1, abstract and Table 4-5, verified]. The
    auction-only subsample reproduces the short-run magnitude [E1, Table 10,
    verified].
  assumptions:
  - Common pre-accident price trends across the 0-40 km and 100-140 km rings within city-distance-band cells (tested, not rejected) [E1]
  - No differential local shock in the window that correlates with distance to plants; the paper checks that all 11 significant domestic earthquakes in the window occurred in far-western China outside the 140 km buffers [E1, verified from Section 3.2]
  - Land-market policy changes in the window were national in scope and did not vary with distance to nuclear plants [E1, reported claim in Section 4]
  diagnostics:
  - Pre-trend interactions for October 2010 - February 2011 (insignificant) [E1]
  - Ring-by-ring effect decay locating the 40 km boundary [E1]
  - Auction-only subsample against seller-timing confounds [E1]
  - Grouped-window decay pattern (April vs May-August vs September-December) [E1]
threats:
- type: concurrent-policy-changes
  basis: documented
  condition: >
    China responded to the same shock with the 2011-03-16 State Council
    decisions: a nationwide nuclear safety inspection and a suspension of new
    plant approvals [E3, verified]. Areas near under-construction or planned
    plants could be differentially affected by the regulatory response itself
    (construction pauses, local expectations), partly confounding a pure
    perception interpretation for those subsamples.
  evidence_refs:
  - E3
  - E1
  possible_diagnostics:
  - Compare operating-plant neighborhoods (no approval channel) with under-construction and planned ones; the paper's status heterogeneity table partly does this [E1]
  - Test whether effects near under-construction plants track inspection milestones rather than the accident date
- type: seller-behavior-selection
  basis: documented
  condition: >
    Local governments are the sole sellers in the primary land market and
    could in principle re-time or re-price supply after the shock, generating
    price changes that are not buyer risk perception [E1].
  evidence_refs:
  - E1
  possible_diagnostics:
  - Auction-only subsample (56% of observations) where sale schedules are fixed in advance; short-run estimates survive [E1, Table 10]
  - Quantity and composition tests (number and type of parcels offered near plants before vs after)
- type: confounding-trends
  basis: documented
  condition: >
    Treated rings could be on different price trajectories (plant vicinity is
    lower-priced, less lit at night per the paper's Table 2), biasing a
    single post dummy; the paper mitigates with city-distance-band fixed
    effects and reports insignificant pre-trend interactions, but only five
    pre months are tested [E1].
  evidence_refs:
  - E1
  possible_diagnostics:
  - Extend the pre window with earlier transactions if data allow
  - Placebo event dates within the pre period
- type: information-and-attention-decay
  basis: inferred
  condition: >
    The effect's one-month lifespan coincides with measured attention decay;
    designs using quarterly or annual outcomes around 2011 would dilute or
    miss the effect entirely [E1; analytical inference].
  evidence_refs:
  - E1
  possible_diagnostics:
  - Keep monthly or finer aggregation; align post windows with the attention profile
- type: measurement-error
  basis: inferred
  condition: >
    Parcel exposure depends on address geocoding quality and on the plant
    classification: the paper's WNA-based count of 15 operating reactors
    differs from the 13 implied by IAEA PRIS first grid-connection dates
    before 2011-03-11, so treatment assignment for parcels near
    late-commissioning units (e.g. Ling Ao 4, Qinshan 2-4) is sensitive to
    the registry convention [E1, E4; analytical inference].
  evidence_refs:
  - E1
  - E4
  possible_diagnostics:
  - Re-derive plant status from IAEA PRIS and re-run band assignments near affected plants
  - Robustness to excluding parcels nearest to commissioning-year reactors
empirical_requirements:
  contract_version: 1
  population: Urban primary-market land transactions within 140 km of Chinese nuclear power plant sites, July 2010 - December 2011
  observation_unit: Land parcel transaction
  geography_level: Parcel coordinates aggregated to city-by-distance-band cells
  time_start: 2010-07
  time_end: 2011-12
  minimum_frequency: monthly
  minimum_pre_periods: 5
  minimum_post_periods: 1
  required_fields:
  - Transaction unit price (or total price and area)
  - Parcel address for geocoding
  - Transaction date (year-month)
  - Transaction method (negotiated, two-stage auction, English auction, sealed bid)
  - Land class, origin (newly converted from rural vs existing urban), designated use
  - Floor area ratio, land size, lease length
  - Night-light intensity around the parcel (NOAA 2010/2011 waves) or a substitute local-activity control
  - Distances to shoreline and inland water
  required_identifiers:
  - Parcel geocode (from address)
  - City code
  - Year-month of transaction
  treatment_key:
  - Distance from parcel to nearest nuclear plant site (0-40 km vs 100-140 km)
  - Post-2011-03-11 indicator (monthly)
  - interaction
  treatment_source: >
    Ministry of Land and Resources land transaction records (publicly posted
    per-transaction results, historically via landchina.com) for parcels
    [E1]; World Nuclear Association reactor records as used by the paper and
    IAEA PRIS reactor registry for cross-checking plant names, locations,
    status and dates [E1, E4].
  measurement_risks:
  - Address geocoding error moves parcels across 20 km rings
  - The raw national transaction file (305,599 records) is filtered to 79,688 within-buffer observations and 34,500 in the DID sample; selection into the buffer sample must be reproducible [E1]
  - Night-light data are annual (2010 and 2011 waves), so the local-activity control cannot vary monthly [E1]
  - Plant status as of March 2011 depends on registry convention (WNA classification vs PRIS first grid connection) [E1, E4]
evidence:
- id: E1
  source_type: paper
  citation: 'Zhu, Hongjia, Yongheng Deng, Rong Zhu, and Xiaobo He. 2016. "Fear of nuclear power? Evidence from Fukushima nuclear accident and land markets in China." Regional Science and Urban Economics 60: 139-154.'
  url: https://doi.org/10.1016/j.regsciurbeco.2016.06.008
  date: 2016
  supports:
  - scope.china_relevance
  - identity.instrument
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.effective
  - timeline.anticipation
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.compliance
  - assignment.exposure_construction
  - assignment.required_identifiers
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - design.assumptions
  - design.diagnostics
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_key
  - empirical_requirements.treatment_source
  - empirical_requirements.measurement_risks
  - design_applications.treatment_encoding
  - design_applications.empirical_design
  verification_status: verified
  access_level: full-text
  locator: 'Open-access full text at PMC (PMC7112941), also retrieved as Europe PMC full-text XML on 2026-10-04: Introduction; Sections 2.1, 3-5; estimation Eqs. 1-4; Tables 1-7 and 10. Table 4 pre-period non-rejections and Tables 6-7 subgroup results re-inspected in task-92455edec324.'
- id: E2
  source_type: archive
  citation: 'World Nuclear Association. "Fukushima Daiichi Accident." Information library paper, continuously updated.'
  url: https://world-nuclear.org/information-library/safety-and-security/safety-of-plants/fukushima-daiichi-accident
  date: 2026
  supports:
  - identity.instrument
  - timeline.effective
  verification_status: verified
  access_level: full-text
  locator: 'Summary bullets and the event-sequence section (earthquake 2011-03-11 14:46 JST, tsunami, INES level 7, evacuation-zone timeline from the National Diet of Japan investigation commission)'
- id: E3
  source_type: policy-document
  citation: '国家能源局. 2012-02-27. "国家能源局全面启动核电安全技术研发计划" (restating the State Council executive meeting decisions of 2011-03-16: comprehensive safety inspection of nuclear facilities, strict review of plants under construction, suspension of new project approvals pending approval of the nuclear safety plan).'
  url: http://www.nea.gov.cn/2012-02/27/c_131433834.htm
  date: 2012
  supports:
  - identity.authority
  - identity.implementation_regime
  - timeline.local_timing
  verification_status: verified
  access_level: official-document
  locator: 'Opening paragraphs of the National Energy Administration notice quoting the 2011-03-16 State Council executive meeting decisions'
- id: E4
  source_type: official-data
  citation: 'IAEA Power Reactor Information System (PRIS). "China, People''s Republic of" country statistics: reactor names, types, status, locations, and first grid-connection dates.'
  url: https://pris.iaea.org/PRIS/CountryStatistics/CountryDetails.aspx?current=CN
  date: 2026
  supports:
  - assignment.treated
  - assignment.exposure_construction
  verification_status: verified
  access_level: dataset
  locator: 'China country-details reactor table accessed 2026-08-15; pre-accident operating fleet reconstructed via first grid-connection dates before 2011-03-11'
design_applications:
- paper: 'Fear of nuclear power? Evidence from Fukushima nuclear accident and land markets in China'
  doi: 10.1016/j.regsciurbeco.2016.06.008
  journal: Regional Science and Urban Economics
  year: 2016
  research_question: Did the 2011 Fukushima nuclear accident change the Chinese public's perceived risk of nuclear power, as capitalized into urban land prices near Chinese nuclear power plants?
  population: Chinese urban primary-market land transactions within 140 km of 45 nuclear plant sites, July 2010 - December 2011 (79,688 transactions; DID sample 34,500)
  outcome: Log unit land price (10,000 RMB per hectare)
  data_used:
  - Ministry of Land and Resources urban land transaction records (305,599 national transactions, July 2010 - December 2011)
  - World Nuclear Association reactor records (location, capacity, construction and operation dates)
  - NOAA night-light imagery (2010 and 2011 waves) for 5 km-radius local activity
  - NOAA significant-earthquake records for China (domestic-disaster confound check)
  treatment_encoding: I(0-40 km to nearest plant) interacted with post-accident month dummies (April-December 2011); grouped windows April 2011 / May-August 2011 / September-December 2011; heterogeneity interactions with plant operating status, construction year, and capacity
  comparison: Parcels in the 100-140 km ring around the same plants, within city-distance-band cells, before vs after 2011-03-11; the 40-100 km donut is excluded from the baseline
  empirical_design: Hedonic difference-in-differences with city-distance-band and year-month fixed effects, clustered at the city-distance-band group; ring-by-ring boundary search; pre-trend interaction test; auction-only subsample mechanism check
  assumptions:
  - Common pre-accident trends across rings (tested, not rejected, October 2010 - February 2011)
  - No distance-correlated local shocks in the window (domestic earthquakes checked against NOAA records)
  - National-scope land policies in the window did not vary with distance to plants (authors' claim)
  threats_addressed:
  - Pre-trends via monthly pre-treatment interactions; band-boundary via ring regressions; seller timing via auction-only subsample; domestic-disaster confounds via NOAA earthquake screen
  evidence_refs:
  - E1
readiness_blockers:
- 'The parcel-level land transaction microdata are not redistributable here; reconstruction requires access to Ministry of Natural Resources (former Ministry of Land and Resources) transaction records or an equivalent licensed extract covering July 2010 - December 2011.'
- 'The paper''s WNA-based plant list (45 sites; 15 reported operating reactors) has not been reconciled reactor-by-reactor against IAEA PRIS, whose first grid-connection dates imply 13 operational reactors before 2011-03-11; treatment near late-commissioning units is sensitive to this convention.'
method_transfer: null
---

## Institutional Background

Before March 2011, China was in the fastest nuclear build-out in the world: the central government had promoted nuclear power since the Tenth Five-Year Plan, and pre-accident targets aimed at 70-80 GWe of nuclear capacity by 2020 [E1, reported]. The operating fleet was concentrated at coastal sites — Qinshan (Zhejiang), Daya Bay and Ling Ao (Guangdong/Shenzhen), and Tianwan (Jiangsu) — with a large pipeline under construction and in planning [E3, E4]. Urban land in China is publicly owned; city governments are the sole legitimate sellers in the primary market, disposing of fixed-term leaseholds through negotiated sales and auctions under an annual local land plan [E1, Section 2.2].

On 2011-03-11 a magnitude-9.0 earthquake off the Tohoku coast of Japan and the ensuing tsunami disabled cooling at the Fukushima Daiichi plant; three reactor cores largely melted within three days, hydrogen explosions and radioactive releases followed over 12-15 March, and the accident was rated INES level 7, with a 20 km evacuation zone [E2, verified]. The authors describe China as not directly affected by earthquake destruction or radiation contamination; this is their institutional premise, not a verified measurement of radiation exposure in this record [E1, Introduction, reported claim]. The Chinese policy response came five days later: the State Council executive meeting of 2011-03-16 ("国四条") ordered an immediate comprehensive safety inspection of all nuclear facilities, strict management of operating plants, a full review of plants under construction, and a suspension of approvals for new nuclear projects — including preparatory work — until a nuclear safety plan was approved [E3, verified]. New project approvals resumed only after the nuclear safety and medium-/long-term development plans were adopted in late 2012 [E1, reported claim].

## What Changed

The paper interprets the land-price response as a change in buyers' perceived nuclear risk [E1, reported interpretation]. The accident was extensively covered in Chinese media, and public attention — measured in the paper by search-frequency patterns — spiked immediately and decayed within one to two months [E1, reported from its Figure 1]. Proximity to fixed plant sites provides the geographic exposure contrast. The measured object is the change in transaction prices, not buyers' beliefs or radiation dose directly; the same event also changed Chinese regulatory expectations [E1, E3; analytical inference].

## Implementation and Assignment

There is no rollout to encode; assignment is fixed geography crossed with one event date. The paper reconstructs the Chinese plant stock as of March 2011 from World Nuclear Association records, grouping reactors by project name into 45 plant sites spanning operating, under-construction, and planned statuses [E1, Section 3.1]. It geocodes each land parcel's address, matches the parcel to its nearest plant, and computes distance [E1, Section 3.2]. Treated parcels are those within 0-40 km of the nearest plant; the comparison pool is the 100-140 km ring; the 40-100 km donut is excluded from baseline specifications [E1, Sections 3-4]. The IAEA PRIS registry independently corroborates the locations and commissioning dates of the pre-accident operating fleet, though its grid-connection convention implies 13 operational reactors before 2011-03-11 versus the 15 the paper reports under the WNA classification [E4, verified; the reconciliation is an analytical inference].

## Why This Creates Empirical Variation

The design compares monthly transaction prices of land parcels near Chinese plants with same-city parcels in an outer ring, before and after the foreign accident. April 2011 is the first full post-accident month. Ring-by-ring regressions locate the strongest response within 40 km; this is a sample-based boundary search, not random assignment of plant locations [E1, Tables 3-5]. The pooled April coefficient is -0.180 log points (approximately -16.5% under exact exponentiation); the authors describe it as about -18% and roughly 2.2 billion RMB of transaction value. Later pooled coefficients are statistically insignificant. That pooled pattern does not apply to every subgroup: Table 6 reports a significant -0.211 log-point September-December effect near under-construction plants. Table 7 does not establish a robust short-run age or capacity gradient after jointly including those attributes [E1, Sections 5.2-5.3 and Tables 4-7, inspected results]. Neither the distance gradient nor these subgroup results by themselves separate perception from the concurrent regulatory channel [analytical inference].

## Identification Risks

The main risks are documented in the record with their diagnostics. (1) China's own regulatory response to Fukushima (the 2011-03-16 State Council decisions) is concurrent with the perception shock; for neighborhoods near under-construction or planned plants, the approval suspension and safety inspection are themselves local economic news, so those subsamples mix a perception channel with a regulatory-expectations channel [E3, verified; E1]. (2) Seller behavior: local governments control primary-market supply, but the auction-only subsample — where sale schedules are fixed about 20 days in advance — reproduces the short-run estimates [E1, Section 5.4.3]. (3) Pre-trend differences: tested pre-treatment interactions (October 2010 - February 2011) are insignificant, but the tested pre window is only five months [E1, Table 4]. (4) Spatial correlation and common shocks are handled by clustering at city-distance-band groups, and all 11 significant domestic earthquakes in the window occurred in far-western China outside the buffers [E1]. (5) Measurement: geocoding error and the registry convention for plant status (WNA vs PRIS) can move marginal parcels across the 40 km boundary [E1, E4; analytical inference].

## Data Requirements

Reproducing the design requires: parcel-level primary-market land transactions with price, area, address, transaction method, land class and origin, designated use, floor area ratio, and lease length for July 2010 - December 2011 (the paper used 305,599 national records from the Ministry of Land and Resources, filtered to 79,688 within 140 km of plant sites and 34,500 in the DID sample) [E1]; a nuclear plant registry with coordinates, status, construction year, and capacity as of March 2011 (the paper used WNA; IAEA PRIS provides an official cross-check) [E1, E4]; NOAA night-light rasters (2010/2011) for the 5 km local-activity control and NOAA significant-earthquake records for the domestic-disaster screen [E1]. Identifiers needed for joins: parcel geocode, city code, and transaction year-month.

## Evidence Notes

E1 is the published RSUE article inspected at open-access full text (PMC7112941): it establishes the design, sample construction, band boundary search, pre-trend tests, dynamic estimates, plant-status heterogeneity, and the auction-subsample mechanism check; claims attributed to it beyond those tables (e.g. media-coverage patterns, approval resumption in late 2012) are marked as reported. E2 is the World Nuclear Association's Fukushima Daiichi reference paper, verifying the accident's date, severity classification, and evacuation timeline. E3 is a National Energy Administration notice verifying the State Council's 2011-03-16 four decisions, including the suspension of new project approvals. E4 is the IAEA PRIS China reactor registry, verifying reactor names, locations, and first grid-connection dates used to cross-check the exposure-generating plant set. What remains open: reactor-by-reactor reconciliation of the paper's 45-site list against PRIS, and direct access to the underlying land transaction microdata (see readiness_blockers).

The 2026-10-04 audit (`task-92455edec324`) re-inspected the published article through the public Europe PMC full-text XML endpoint, including the Introduction, Section 2.1 and Tables 4, 6 and 7. It separated the authors' perception interpretation from independently established facts, corrected log-point conversion, and preserved the longer-lived under-construction subgroup estimate and the limits of pre-trend non-rejections. It did not re-fetch PRIS or reconcile the 45-site roster, change the RSUE 0-40/100-140 km comparison, raise maturity, or count another variation.
