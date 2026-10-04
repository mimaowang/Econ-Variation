---
schema_version: 2
id: china-regional-carbon-market-operations
name: China Regional Carbon-Market Operations and ETS-City Exposure
aliases:
- China regional ETS pilots
- China eight regional carbon markets
- 中国区域碳排放权交易市场运营
status: grounded
provenance:
  task_id: task-238f1d65d5e9
scope:
  country: China
  regions:
  - Beijing, Tianjin, Shanghai, Chongqing, Guangdong, Hubei, Shenzhen, and Fujian regional carbon markets
  domains:
  - environmental-regulation
  - regional-economics
  - industrial-development
  - local-governance
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    Regional carbon-market operation changes the regulatory and allowance-trading
    environment facing Chinese emitters and the cities in which they operate. The
    published application studies city exposure, not a foreign carbon-price shock.
identity:
  instrument: >
    Operation of a regional carbon emissions trading market (ETS) in the paper's
    covered city, following locally designed caps, allowance allocation, reporting,
    verification, compliance, registry, and exchange arrangements.
  authority: >
    NDRC Office Notice Fa Gai Ban Qi Hou [2011] 2601 authorized seven pilot
    jurisdictions and required each to prepare a local implementation plan, rules,
    cap, allocation scheme, supervision system, registry, and trading platform.
    Fujian later established a separate provincial market under Fujian Government
    Notice Min Zheng [2016] 40 [E1; E2].
  legal_identifiers:
  - 'NDRC Office Notice on Launching Carbon Emissions Trading Pilots, Fa Gai Ban Qi Hou [2011] 2601, 29 October 2011.'
  - 'Fujian Provincial Government Notice on the Implementation Plan for Building Fujian Carbon Emissions Trading Market, Min Zheng [2016] 40, 26 September 2016.'
  implementation_regime: >
    A central authorization followed by jurisdiction-specific market construction.
    Seven jurisdictions were authorized in 2011; the published city panel adds
    Fujian's market, which officially started trading in December 2016. Local
    coverage, allocation, monitoring, and enforcement differ, so this is an
    operation exposure—not a homogeneous national regulation.
  assignment_mechanism: >
    A city is assigned in the paper when it is covered by one of the operating
    regional markets. The paper's city treatment is reported as 45 covered
    prefecture-level cities across eight markets, but the exact city-year/sector
    crosswalk is not in the inspected public material [E3, reported claim].
  parent: null
  related_variations:
  - china-low-carbon-pilot-first-wave
timeline:
  announcement: '2011-10-29'
  effective: null
  implementation_start: 2013
  implementation_end: 2016
  local_timing: >
    E1 authorized seven pilots in October 2011 but instructed them to develop
    local schemes before implementation. E3 reports market operations beginning
    in 2013 and 2014, with Fujian as an additional market initiated in 2016;
    E2 set Fujian's goal of formal operation by end-2016 and official Fujian
    records report the market opening on 22 December 2016. Exact operation dates
    for each of the original seven remain a reuse requirement.
  anticipation: >
    Authorization preceded operation by at least a local-plan and infrastructure
    phase, so firms and cities could anticipate market exposure. The paper reports
    an SDID event study that did not find effects driven by anticipation, but this
    is a design diagnostic, not proof that market construction was unanticipated
    [E3, reported claim].
  last_verified: '2026-09-28'
assignment:
  unit: >
    In the published application, prefecture-level city-year observations in a
    228-city panel from 2007 to 2019; 45 cities are reported as covered by a
    regional market [E3, reported claim].
  treated: >
    Cities covered by an operating regional ETS under the paper's coding. At the
    underlying institution, direct compliance obligations belong to covered
    emitting entities, so city treatment is an exposure aggregation rather than
    universal firm treatment.
  comparison_pool: >
    Non-ETS cities in the paper's panel, weighted/selected through synthetic DID;
    valid comparison depends on the donor-pool construction, pre-operation fit,
    and absence of concurrent differential policy paths.
  rule: >
    For a city-year replication, create an indicator that turns on when the
    relevant regional market is operating and the city belongs to that market's
    published coverage roster. Do not code all cities of Guangdong, Hubei, or
    Fujian as treated without the paper's roster and sector logic.
  intensity: >
    The paper also studies heterogeneity by market trading volume/turnover,
    allowance price, power-sector competition, and local fiscal capacity; these
    are effect-modifier measures, not the baseline assignment rule [E3, reported claim].
  exemptions:
  - Firm compliance is limited to locally covered sectors/entities rather than every city resident or firm.
  - Fujian's 2016 initial scope covered nine industrial sectors and entities meeting a stated energy-consumption threshold [E2].
  compliance: >
    The NDRC required pilots to create allocation, registration, supervision, and
    trading systems, but actual market liquidity, local enforcement, and coverage
    varied. City-level exposure therefore has imperfect compliance with the
    underlying entity-level regime [E1; E3, reported claim].
  exposure_construction: >
    The paper reports a city-level ETS-operation indicator for 45 covered cities
    in eight regional markets. It combines grid-level emissions and nighttime
    lights with firm, patent, city-sector, trade, and fiscal data, but its exact
    grid-to-city and market-to-city crosswalks are not publicly reconstructed
    here [E3, reported claim].
  required_identifiers:
  - prefecture-level city code and stable boundary crosswalk
  - regional ETS jurisdiction and operation-date table
  - covered-sector/entity roster with city location
  - year and, where applicable, firm/plant identifier
  spillovers: >
    Carbon leakage to neighboring or production-linked non-ETS cities is a
    central threat. The paper reports no such increase in its tests, but firms,
    electricity dispatch, supply chains, and provincial policy coordination can
    still transmit effects across the formal market boundary [E3, reported claim].
research_compatibility:
  outcome_domains:
  - carbon emissions and emission intensity
  - city economic activity and industrial composition
  - green technology adoption and trade
  - local environmental regulation
  affected_populations:
  - covered emitting entities and cities in regional ETS jurisdictions
  - firms and workers exposed indirectly through city industrial structure
  mechanism_channels:
  - allowance price and compliance incentives
  - reallocation from carbon-intensive sectors toward services
  - imported environmental equipment and local enforcement capacity
  best_for:
  - City or firm panels that can reconstruct covered entities, operation dates, and pre-treatment outcomes.
  - Research on heterogeneous market-based environmental regulation where local market design is measured rather than ignored.
  not_good_for:
  - A generic province-level DID that assumes every local firm entered simultaneously.
  - Separating a carbon-market effect from concurrent low-carbon pilots, targets, and energy reforms without explicit controls and diagnostics.
design:
  claim_type: causal
  affordances:
  - Staggered regional market operation with a long city panel.
  - Synthetic DID can construct a transparent counterfactual when a conventional staggered TWFE comparison is weak.
  - Entity/sector rosters can support a more direct firm or plant exposure design than city treatment.
  candidate_designs:
  - Synthetic difference-in-differences on city outcomes with market-operation timing.
  - Event study using exact market-city operation dates and pre-trend fit.
  - Entity-level DID using allowance coverage, with city and sector-year controls.
  identifying_variation: >
    Differential transition of covered cities into operating regional carbon
    markets relative to weighted non-covered cities. This is conditional variation:
    pilot selection and local implementation capacity are not random.
  primary_strategy: >
    Li and Zhao use city-level TWFE DID and their preferred staggered synthetic
    DID, with 2007-2019 data, policy controls, event-study estimates, and placebo
    tests [E3, reported claim].
  estimand: >
    The reported average treatment effect on treated ETS cities after operation,
    relative to the synthetic/non-ETS comparison; it is not automatically an
    entity-level allowance-price elasticity.
  treatment_variable: City covered by an operating regional ETS in year t.
  comparison_logic: >
    SDID weights non-ETS cities to approximate treated-city pre-operation paths;
    treatment timing and donor exclusions must be reconstructed before reuse.
  estimation_notes: >
    The paper reports grid-level emissions aggregated to cities, nighttime lights,
    firm outcomes, patents, city-sector employment/production/trade, and fiscal
    measures. It reports controls for provincial reduction targets and concurrent
    city policy, plus assignment/outcome placebos [E3, reported claim].
  assumptions:
  - After SDID weighting and stated controls, untreated potential outcomes of ETS cities are approximated by donor cities.
  - Pilot choice, local capacity, and operation timing do not leave unmodeled city-specific changes that drive outcomes.
  - City aggregation is a meaningful exposure measure for entity-level compliance.
  diagnostics:
  - Pre-operation fit and event-study lead estimates.
  - Alternative donor pools and placebo treatment assignment/outcomes.
  - Direct leakage tests for neighboring and production-linked non-ETS cities.
threats:
- type: selected-pilot-and-local-market-design
  basis: documented
  condition: >
    E1 says selection reflected local applications and work foundations, and
    delegates caps, allocation, and systems to the pilots; this creates a direct
    risk that adoption and effectiveness track pre-existing capacity.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Audit application/selection materials, local rules, pre-trends, and capacity trajectories.
- type: city-treatment-versus-entity-coverage
  basis: inferred
  condition: >
    Compliance is entity/sector based while the paper estimates city exposure;
    unobserved coverage shares can attenuate or composition-bias city effects.
  evidence_refs:
  - E1
  - E3
  possible_diagnostics:
  - Reconstruct covered-emitter rosters and emissions shares by city-year.
empirical_requirements:
  contract_version: 1
  population: Prefecture-level Chinese cities or covered emitting entities.
  observation_unit: city-year; entity-year for direct-compliance extensions
  geography_level: prefecture-level city linked to regional ETS jurisdiction
  time_start: 2007
  time_end: 2019
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields:
  - carbon emissions or a transparently constructed proxy
  - ETS market operation dates and covered entity/sector roster
  - city economic and industrial-structure outcomes
  - concurrent carbon-target and environmental-policy measures
  required_identifiers:
  - prefecture city code
  - year
  - market jurisdiction
  - covered entity or sector code where applicable
  treatment_key:
  - market jurisdiction
  - operation date
  - city code
  treatment_source: NDRC pilot authorization plus local market rules, opening notices, and covered-emitter rosters
  measurement_risks:
  - province-level jurisdiction versus city/entity-level market coverage
  - local opening versus formal authorization date
  - grid-to-city emissions aggregation and changing city boundaries
design_profiles: []
evidence:
- id: E1
  source_type: policy-document
  citation: 'National Development and Reform Commission Office, Notice on Launching Carbon Emissions Trading Pilots, Fa Gai Ban Qi Hou [2011] 2601.'
  url: https://www.ndrc.gov.cn/xxgk/zcfb/tz/201201/t20120113_964370_ext.html
  date: '2011-10-29'
  supports:
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.announcement
  - assignment.compliance
  verification_status: verified
  access_level: official-document
  locator: 'Notice body: addressees; authorization of seven jurisdictions; requirements for local plans, caps, allocations, supervision, registry, and platform; closing date.'
- id: E2
  source_type: implementation-document
  citation: 'Fujian Provincial Government, Implementation Plan for Building Fujian Carbon Emissions Trading Market, Min Zheng [2016] 40.'
  url: https://www.fujian.gov.cn/zwgk/zfxxgk/szfwj/jgzz/hjnyzcwj/201610/t20161002_1186289.htm
  date: '2016-09-26'
  supports:
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.local_timing
  - assignment.exemptions
  verification_status: verified
  access_level: official-document
  locator: 'Sections I-IV: formal-operation target by end-2016, nine initial industrial sectors, energy-consumption threshold, and later expansion.'
- id: E3
  source_type: paper
  citation: 'Li, Yue, and Jing Zhao. 2026. "The effectiveness of carbon emission trading system: Evidence from China’s regional markets." Journal of Development Economics 179:103631.'
  url: https://doi.org/10.1016/j.jdeveco.2025.103631
  date: '2026-09-28'
  supports:
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.intensity
  - assignment.exposure_construction
  - assignment.spillovers
  - timeline.local_timing
  - timeline.anticipation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - design.diagnostics
  - empirical_requirements.observation_unit
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.required_fields
  verification_status: reported
  access_level: full-text
  locator: 'ScienceDirect full-text page: Introduction, Sections 2-3, Difference-in-differences estimation, Main results, and concluding remarks.'
design_applications:
- paper: 'The effectiveness of carbon emission trading system: Evidence from China’s regional markets'
  doi: 10.1016/j.jdeveco.2025.103631
  journal: Journal of Development Economics
  year: 2026
  research_question: Did operation of China’s regional carbon markets reduce city emissions without reducing economic activity, and through which mechanisms?
  population: 228 prefecture-level cities, including 45 reported ETS-covered cities, 2007-2019.
  outcome: Per-capita CO2 emissions, nighttime lights, firm revenue/profit, city-sector employment/production/trade, patents, and fiscal measures.
  data_used:
  - grid-level emissions and nighttime lights aggregated to cities
  - firm performance and inventor patent data
  - city-sector economic, trade, and fiscal data
  treatment_encoding: City covered by an operating regional ETS; eight markets have staggered operation dates.
  comparison: Non-ETS city donor pool under SDID, supplemented by TWFE, event-study, policy-control, and placebo analyses.
  empirical_design: Staggered synthetic difference-in-differences with city panel data.
  assumptions:
  - SDID donor weights recover credible untreated city paths.
  - Concurrent policies and pilot selection are sufficiently addressed by controls and diagnostics.
  threats_addressed:
  - staggered-DID weighting problems
  - policy confounding and anticipation
  - spatial and production-linkage carbon leakage
  evidence_refs:
  - E3
method_transfer: null
readiness_blockers:
- The public sources inspected do not provide the paper’s full city-year treatment roster, covered-sector/entity shares, or exact opening dates for each of the seven original pilots.
- The record is grounded at the institutional and paper-design level; direct reuse requires reconstructing local market rules and the city/entity crosswalk rather than assigning all provincial cities automatically.
- Paper-reported grid-to-city emissions, SDID donor weights, and policy-control code have not been independently reproduced from a public replication package.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

China sought a market-based way to control greenhouse-gas emissions during the
Twelfth Five-Year Plan. NDRC's 2011 notice did not impose one national market:
it selected seven jurisdictions after considering their applications and work
foundations, then required each to construct its own implementation plan, cap,
allocation, registry, supervision, and exchange [E1]. Fujian later created a
separate provincial market with its own 2016 plan and industrial scope [E2].

## What Changed

The relevant change is local market operation, through which covered entities
receive an emissions constraint and tradable allowances. Central authorization
is not the treatment date. The empirical application combines seven authorized
pilots with Fujian, treating their staggered operating markets as eight regional
exposures [E3, reported claim]. National ETS construction from 2017 onward and
low-carbon-city pilots are related but distinct institutions.

## Implementation and Assignment

The central notice named jurisdictions but delegated core rules to them, so a
city's exposure depends on its market, operating date, and covered emitters.
Li and Zhao report 45 treated cities in a 228-city panel; that is a paper-level
city aggregation of an entity-level regime, not proof that every city firm was
directly regulated [E3, reported claim].

## Why This Creates Empirical Variation

Operation dates differ across regional markets, allowing city outcomes to be
compared with a weighted non-ETS donor pool before and after operation. The
paper uses SDID because conventional staggered TWFE can be misleading when
treatment effects and timing differ [E3, reported claim]. The design remains
conditional on selected pilots and locally chosen market details.

## Identification Risks

Pilot selection and local state capacity are central rather than peripheral:
the authorizing notice explicitly used applications and work foundations, and
then left major design choices local [E1]. City aggregation may also obscure
entity coverage; leakage, electricity dispatch, and supply-chain reallocation
can spill beyond a market. The paper reports no neighboring or production-linkage
leakage, but that is a reported diagnostic, not a universal guarantee [E3].

## Data Requirements

Direct reuse needs a city/entity crosswalk, local market opening notices and
rules, emissions and economic outcomes, and enough pre-operation years to
evaluate synthetic-control fit. The companion data repository should document
restricted raw sources and reconstruction paths; this record retains only the
treatment contract.

## Evidence Notes

E1 independently verifies the seven-jurisdiction authorization and its delegated
implementation structure. E2 independently verifies Fujian's separate 2016
construction plan and initial scope. E3 is the published application's full-text
evidence for its eight-market/45-city panel, SDID encoding, data families, and
diagnostics. It does not substitute for the missing city/entity roster or each
local opening notice, which remain explicit blockers.
