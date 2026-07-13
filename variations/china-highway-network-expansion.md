---
schema_version: 2
id: china-highway-network-expansion
name: China's National Trunk Highway System (NTHS) Construction as a Shock to Market Access and Trade Costs (1992–2009)
aliases:
- Faber highway China
- China national trunk highway system
- NTHS industrialization
- 中国国家干线公路系统
- 高速公路网络

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - All prefectures connected by the NTHS network
  domains:
  - trade
  - infrastructure
  - economic-geography
  - industrialization
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: The construction of China's National Trunk Highway System (NTHS), a network of limited-access highways connecting
    major cities, which created plausibly exogenous variation in market access for prefectures depending on their location
    relative to the planned highway routes
  authority: Chinese central government (Ministry of Transport)
  legal_identifiers:
  - National Trunk Highway System Plan (1992)
  - successive Five-Year Plans for highway construction
  implementation_regime: The NTHS was planned in 1992 as 7 radial and 5 vertical highways connecting provincial capitals and
    major cities with populations over 500,000; construction occurred in stages through the 1990s and 2000s
  assignment_mechanism: The key identifying variation is whether a prefecture lies on the straight-line path connecting two
    targeted major cities (a "least-cost" path determined by geography, not local economic conditions); peripheral counties
    connected to the network gain market access while central counties may lose industrial activity
  parent: null
  related_variations:
  - china-vat-reform-investment
timeline:
  announcement: '1992-01-01'
  effective: null
  implementation_start: 1992
  implementation_end: 2009
  local_timing: Highway segments were constructed at different times depending on their position in the national plan; connectivity
    to a prefecture occurs when the relevant segment opens
  anticipation: The NTHS plan routes were determined by geographical considerations connecting targeted cities; individual
    counties could not influence whether a highway passed through them
  last_verified: '2026-07-13'
assignment:
  unit: Prefecture-county and firm
  treated: Counties connected to the NTHS network after highway segment opening
  comparison_pool: Counties not yet connected to the NTHS; peripheral counties before vs after connection; central (metropolitan)
    counties experiencing industrial outflows vs peripheral counties experiencing inflows
  rule: A county is treated when it lies on or very near the straight-line path connecting two targeted NTHS cities; the targeting
    of which cities to connect was determined by national planning criteria exogenous to county-level economic conditions
  intensity: Binary (connected or not) plus continuous distance-based measures of market access change; peripheral counties
    gain market access, while central connected counties lose industrial activity to lower-cost peripheral areas
  compliance: Highway construction followed the planned routes; compliance with the plan was high
  exemptions: []
  exposure_construction: Code county-year as connected when the nearest NTHS highway segment opens; construct market access
    measures based on travel time to major cities pre- and post-highway; use straight-line "least-cost" path as instrument
    for actual highway location
  required_identifiers:
  - county code
  - year
  - NTHS connection status
  - distance to highway
  spillovers: Industrial activity may relocate from connected central counties to connected peripheral counties; the paper
    explicitly estimates these general equilibrium spatial reallocation effects
research_compatibility:
  outcome_domains:
  - industrial output
  - firm entry
  - employment
  - productivity
  - spatial concentration
  - market access
  affected_populations:
  - Manufacturing firms
  - industrial workers
  - peripheral county residents
  - central county residents
  mechanism_channels:
  - market access improvement
  - trade cost reduction
  - industrial relocation
  - spatial agglomeration
  - specialization
  best_for:
  - Studying how transport infrastructure affects spatial allocation of economic activity
  - market integration effects on industrialization
  not_good_for:
  - Short-run outcomes before spatial equilibrium adjustments occur
  - service-sector outcomes
design:
  affordances:
  - geographically predetermined highway routes connecting targeted cities
  - straight-line least-cost path instrument
  - pre/post highway opening comparison
  - cross-county variation in initial remoteness
  candidate_designs:
  - difference-in-differences
  - instrumental variables using straight-line path
  - spatial general equilibrium analysis
  identifying_variation: Whether a prefecture lies on the straight-line path between targeted provincial capitals and major
    cities (the planned NTHS route); this creates plausibly exogenous variation in highway connectivity because the straight
    line is determined by geography, not local economic conditions
  assumptions:
  - Highway routes are determined by geography connecting targeted cities
  - not local economic lobbying
  - straight-line path is a valid instrument for actual highway location
  - no differential pre-trends between connected and unconnected counties
  diagnostics:
  - First-stage relationship between straight-line path and actual highway location
  - test for pre-trends in industrial outcomes
  - compare peripheral vs central county effects
  - falsification using non-targeted routes
  primary_strategy: IV using straight-line path as instrument for actual highway placement; DID comparing connected vs unconnected
    counties; spatial general equilibrium analysis of industrial relocation
  estimand: The causal effect of the recorded exposure on Industrial output growth, number of firms, employment in manufacturing,
    conditional on the stated design assumptions.
  treatment_variable: County-year indicator for NTHS connection; instrumented by whether the county lies on the straight-line
    path between targeted provincial capitals
  comparison_logic: Peripheral counties gaining connection vs not-yet-connected; central counties losing industry vs peripheral
    counties gaining industry
  estimation_notes: IV using straight-line path as instrument for actual highway placement; DID comparing connected vs unconnected
    counties; spatial general equilibrium analysis of industrial relocation
threats:
- type: endogenous-route-placement
  basis: inferred
  condition: If local economic or political conditions influenced the exact routing of highways (deviations from straight-line
    paths), the instrument may not fully address endogeneity
  evidence_refs:
  - E1
  possible_diagnostics:
  - compare straight-line to actual route
  - test for route deviations correlated with pre-existing economic conditions
  - use only the straight-line instrument
- type: spatial-spillovers
  basis: documented
  condition: The paper's key finding is that connected central counties lose industrial output to peripheral counties; standard
    DID ignoring these spatial general equilibrium effects would be misleading
  evidence_refs:
  - E1
  possible_diagnostics:
  - explicitly model spatial reallocation
  - compare central and peripheral effects
  - use spatial equilibrium framework
empirical_requirements:
  contract_version: 1
  population: Chinese counties and manufacturing firms, 1992–2009
  observation_unit: Firm-year or county-year
  geography_level: County
  time_start: 1992
  time_end: 2009
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 5
  required_fields:
  - county code
  - year
  - NTHS connection indicator
  - straight-line path indicator
  - firm output
  - employment
  - industry
  - location
  required_identifiers:
  - county code
  - year
  - firm ID
  treatment_key:
  - county code
  - NTHS connection year
  - straight-line path indicator
  - market access measure
  treatment_source: GIS data on NTHS highway routes and opening dates; Annual Survey of Industrial Firms; county-level economic
    indicators from statistical yearbooks
  measurement_risks:
  - highway opening dates may be imprecise for some segments
  - market access measures sensitive to travel-time assumptions
  - county boundary changes over the period
evidence:
- id: E1
  source_type: paper
  citation: 'Faber, Benjamin. 2014. "Trade Integration, Market Size, and Industrialization: Evidence from China''s National
    Trunk Highway System." Review of Economic Studies 81 (3): 1046–1086.'
  url: https://doi.org/10.1093/restud/rdu010
  date: 2014
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - spatial reallocation analysis
  verification_status: verified
design_applications:
- paper: 'Trade Integration, Market Size, and Industrialization: Evidence from China''s National Trunk Highway System'
  doi: 10.1093/restud/rdu010
  journal: Review of Economic Studies
  year: 2014
  research_question: How does improved market access through highway construction affect the spatial concentration of industrial
    production?
  population: Chinese counties and manufacturing firms, 1992–2009
  outcome: Industrial output growth, number of firms, employment in manufacturing
  data_used: []
  treatment_encoding: County-year indicator for NTHS connection; instrumented by whether the county lies on the straight-line
    path between targeted provincial capitals
  comparison: Peripheral counties gaining connection vs not-yet-connected; central counties losing industry vs peripheral
    counties gaining industry
  empirical_design: IV using straight-line path as instrument for actual highway placement; DID comparing connected vs unconnected
    counties; spatial general equilibrium analysis of industrial relocation
  assumptions:
  - straight-line path is exogenous to local economic conditions
  - highway placement follows geographic logic of connecting targeted cities
  - no contemporaneous spatially-correlated shocks
  threats_addressed:
  - endogenous route placement via straight-line IV
  - spatial spillovers via explicit modeling of reallocation
  - heterogeneous effects by initial market access
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
---
## Institutional Background
Before the 1990s, China's road network was underdeveloped, limiting market integration and creating fragmented local economies. In 1992, the central government announced the National Trunk Highway System (NTHS) — a network of high-quality, limited-access highways radiating from and crossing the country, designed to connect all provincial capitals and cities with populations exceeding 500,000. By 2009, the network exceeded 50,000 kilometers. [E1]

## What Changed
The NTHS dramatically reduced travel time between connected cities, effectively integrating previously isolated county-level markets into larger regional and national markets. For peripheral (non-metropolitan) counties located along the routes, this meant a substantial improvement in market access — they could now reach distant consumer and input markets at lower cost. [E1]

## Implementation and Assignment
Highway routes were planned to connect targeted provincial capitals and large cities along straight-line paths. Whether a given county lies on the straight line between two targeted cities is determined by geography, not by the county's economic conditions — creating a plausibly exogenous instrument for actual highway connectivity. The staggered construction schedule across different segments creates temporal variation in when counties gain connectivity. [E1]

## Why This Creates Empirical Variation
The key insight: peripheral counties gaining highway connectivity experience a positive market-access shock that attracts industrial firms from central (metropolitan) counties. This creates two-sided spatial variation — some counties gain industry while others lose it — and the straight-line instrument allows causal identification of these general equilibrium effects. The paper's central finding is that highways caused a reduction in industrial output growth in connected metropolitan regions and an increase in connected peripheral regions. [E1; analytical inference]

## Identification Risks
The main threat is that actual highway routes may deviate from straight-line paths for economic or political reasons, compromising the instrument. The paper addresses this by using the straight-line prediction regardless of actual placement. Another concern is that the spatial reallocation effects mean standard DID estimates (comparing connected to unconnected) can be misleading if they ignore the outflow of industry from central areas. [E1]

## Data Requirements
GIS data on NTHS highway segments with opening dates, county-level geographic coordinates, straight-line path calculations between targeted cities, firm-level manufacturing data from the Annual Survey of Industrial Firms (output, employment, fixed assets, industry classification), and county-level controls from statistical yearbooks. [E1]

## Evidence Notes
E1 documents that NTHS highway connections led to a reduction in industrial output growth in connected metropolitan areas and an increase in peripheral areas, consistent with a spatial reorganization of production toward lower-cost locations as market access improves. The straight-line IV strategy provides strong support for causal interpretation of these spatial effects.
