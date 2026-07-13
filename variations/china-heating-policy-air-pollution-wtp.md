---
schema_version: 2
id: china-heating-policy-air-pollution-wtp
name: Huai River Heating Policy as a Spatial Regression Discontinuity for Air Pollution Willingness-to-Pay in China
aliases:
- Willingness to pay clean air China (deprecated — see china-huai-river-heating-air-pollution)

status: deprecated
provenance:
  task_id: task-164ccc1cb13e
scope:
  country: China
  regions:
  - Cities north and south of the Huai River-Qinling Mountains line
  domains:
  - environment
  - energy
  - health
  - household
  - urban
  variation_type: boundary-discontinuity
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: China's Huai River-Qinling Mountains heating policy, which provides subsidized coal-based centralized heating
    to cities north of the boundary but not to cities south of it, creating a sharp spatial discontinuity in ambient air pollution
    (PM10) at the boundary
  authority: Chinese central government (established during the centrally planned period, 1950s)
  legal_identifiers:
  - China centralized heating policy regulations codified in urban planning and energy administration rules
  implementation_regime: Cities north of the Huai River-Qinling Mountains line receive government-subsidized, coal-fired centralized
    heating during winter months (November–March); cities south of the line do not, relying instead on electric heating, individual
    coal stoves, or no heating
  assignment_mechanism: The heating boundary follows the Huai River and Qinling Mountains, a geographic line fixed by historical
    central planning decisions in the 1950s; whether a city is north or south of the line is geographically determined and
    exogenous to contemporary economic outcomes
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 1950
  implementation_end: ongoing
  local_timing: The boundary is fixed; the heating policy has been in place since the 1950s; the spatial discontinuity in
    pollution is a perennial feature of the winter heating season
  anticipation: The boundary was established decades before contemporary air quality concerns; households cannot choose which
    side of the boundary to live on in the short run
  last_verified: '2026-07-13'
assignment:
  unit: City or individual household
  treated: Cities and households located just north of the Huai River-Qinling Mountains boundary, receiving coal-based centralized
    heating that increases ambient PM10 by approximately 24–39 μg/m³ during winter months
  comparison_pool: Cities and households located just south of the boundary, which do not receive centralized heating and
    have systematically lower winter PM10 concentrations
  rule: Geographic location relative to the Huai River-Qinling Mountains line; being north of the boundary = treated (higher
    pollution due to coal heating)
  intensity: Continuous — PM10 increases by ~24–39 μg/m³ north of the boundary; the pollution gradient is strongest near the
    boundary and in winter months
  exemptions: []
  compliance: The policy is strictly implemented — centralized heating infrastructure exists in northern cities and not in
    southern cities
  exposure_construction: Code each city as north or south of the Huai River boundary; use distance to the boundary as the
    forcing variable in a spatial regression discontinuity; measure pollution using city-level PM10 concentrations from China's
    Ministry of Environmental Protection monitoring stations
  required_identifiers:
  - city code
  - geographic coordinates
  - distance to Huai River boundary
  - calendar month/year
  spillovers: Pollution does not respect the boundary; PM10 from northern cities disperses southward, partially attenuating
    the spatial discontinuity; some southern households use individual coal stoves, partially offsetting the north-south pollution
    difference
research_compatibility:
  outcome_domains:
  - air purifier purchases
  - health expenditures
  - defensive investments
  - mortality
  - respiratory health
  - household welfare
  - environmental valuation
  affected_populations:
  - urban households
  - particularly those in cities near the Huai River boundary
  - higher-income households with greater willingness-to-pay for clean air
  mechanism_channels:
  - ambient PM10 exposure
  - health risk perception
  - defensive expenditure
  - air purifier demand
  - media information shocks
  best_for:
  - Estimating households' revealed willingness-to-pay for clean air using market transactions
  - Spatial regression discontinuity designs with geographic forcing variables
  - Studying how information and media coverage affect environmental valuation
  not_good_for:
  - Short panels without detailed household-level purchase data
  - Populations far from the Huai River boundary (the RD identifies a local effect)
  - Outcomes not plausibly linked to air pollution exposure
design:
  affordances:
  - sharp geographic boundary determined by historical central planning
  - large, discontinuous change in winter PM10 at the boundary
  - scanner data on air purifier purchases provides market-based WTP measures
  - variation in information environment over time (2013 "airpocalypse")
  candidate_designs:
  - spatial regression discontinuity at the Huai River boundary
  - difference-in-discontinuity (before vs. after 2013 media shock × north/south of boundary)
  - structural demand estimation using distance-based instruments for air purifier prices
  identifying_variation: Discontinuous change in winter PM10 concentrations at the Huai River heating boundary, used to identify
    the causal effect of pollution on air purifier demand and to recover households' marginal willingness-to-pay for clean
    air
  assumptions:
  - All determinants of air purifier demand other than pollution vary smoothly across the Huai River boundary
  - The boundary location is exogenous — it was not chosen based on pollution levels or air purifier demand
  - Households do not sort across the boundary based on pollution preferences (limited short-run mobility)
  - Distance to manufacturing plants is a valid instrument for air purifier prices
  diagnostics:
  - Plot PM10 and other city characteristics against distance to the boundary
  - Test for smoothness of predetermined city characteristics at the boundary
  - Estimate with alternative bandwidths and polynomial orders
  - Compare winter (heating season) and summer (non-heating season) estimates
  - Test for sorting by examining population density near the boundary
  - Estimate pre-2013 and post-2013 WTP separately
  primary_strategy: Spatial regression discontinuity at the Huai River boundary; structural demand estimation (random-coefficients
    logit) for marginal WTP; difference-in-discontinuity for pre/post-2013 information environment change
  estimand: The causal effect of the recorded exposure on Air purifier sales volume and revenue by city-month; air purifier
    prices and market shares by product, conditional on the stated design assumptions.
  treatment_variable: Spatial RD — cities north of the Huai River boundary are coded as "treated" with higher PM10 due to
    coal heating; instrument for PM10 with the north-side indicator × winter interaction
  comparison_logic: Cities just north versus just south of the Huai River boundary, within winter heating months; structural
    demand estimation with instruments for endogenous prices
  estimation_notes: Spatial regression discontinuity at the Huai River boundary; structural demand estimation (random-coefficients
    logit) for marginal WTP; difference-in-discontinuity for pre/post-2013 information environment change
threats:
- type: other-boundary-differences
  basis: inferred
  condition: The Huai River boundary is also a climatic and geographic dividing line; cities north and south of the boundary
    differ on dimensions other than heating policy (temperature, humidity, agricultural patterns, economic development)
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for temperature
  - humidity
  - and other climatic variables; estimate RD using only the closest cities to the boundary; compare summer (non-heating)
    and winter (heating) pollution gradients
- type: spatial-sorting
  basis: inferred
  condition: Over decades, households may sort across the boundary based on pollution preferences; if pollution-sensitive
    households move south, the RD estimates among the remaining northern households may be attenuated
  evidence_refs:
  - E1
  possible_diagnostics:
  - test for smoothness of population density and demographic characteristics at the boundary
  - examine migration flows
  - use hukou registration data
- type: attenuation-due-to-noncompliance
  basis: documented
  condition: Some southern cities near the boundary also have partial heating or use individual coal stoves, attenuating the
    pollution discontinuity; the fuzzy RD design should account for this
  evidence_refs:
  - E1
  possible_diagnostics:
  - estimate fuzzy RD instrumenting actual pollution with north-of-boundary indicator
  - measure actual heating penetration near the boundary
  - use winter-only PM10 as the endogenous variable
- type: information-shock-confounding
  basis: inferred
  condition: The 2013 "airpocalypse" (high-visibility pollution episodes) and subsequent media coverage increased awareness
    of air pollution nationally; the temporal variation in WTP may reflect changing awareness rather than changing preferences
  evidence_refs:
  - E1
  possible_diagnostics:
  - estimate separate WTP for pre- and post-2013 periods
  - control for media coverage intensity by city
  - use survey data on pollution awareness
empirical_requirements:
  contract_version: 1
  population: Urban Chinese households in approximately 80 cities observed from 2006 to 2014
  observation_unit: City-month or household-year
  geography_level: City
  time_start: 2006
  time_end: 2014
  minimum_frequency: monthly (for pollution and sales data)
  minimum_pre_periods: 24
  minimum_post_periods: 24
  required_fields:
  - air purifier sales by city-month
  - product characteristics
  - PM10 concentration by city-day
  - city geographic coordinates
  - temperature
  - humidity
  - household demographics
  required_identifiers:
  - city code
  - product barcode
  - calendar month
  - north/south of Huai River indicator
  treatment_key:
  - city code
  - north/south indicator
  - distance to Huai River boundary
  - winter month indicator
  treatment_source: China Ministry of Environmental Protection for PM10 data; retail scanner data (Nielsen or similar) for
    air purifier sales; China Meteorological Administration for weather data
  measurement_risks:
  - PM10 monitoring station placement and coverage
  - air purifier sales data may not capture online purchases
  - product characteristics changing over time
  - city boundary changes
  - temperature-humidity-pollution correlation
evidence:
- id: E1
  source_type: paper
  citation: 'Ito, Koichiro, and Shuang Zhang. 2020. "Willingness to Pay for Clean Air: Evidence from Air Purifier Markets
    in China." Journal of Political Economy 128 (5): 1627–1672.'
  url: https://doi.org/10.1086/705554
  date: 2020
  supports:
  - identity
  - assignment
  - design
  - RD estimation
  - WTP calculation
  - information-shock analysis
  verification_status: verified
design_applications:
- paper: 'Willingness to Pay for Clean Air: Evidence from Air Purifier Markets in China'
  doi: 10.1086/705554
  journal: Journal of Political Economy
  year: 2020
  research_question: What is Chinese urban households' marginal willingness-to-pay (MWTP) for clean air, and how does it change
    with access to pollution information?
  population: Urban households in ~80 Chinese cities, 2006–2014
  outcome: Air purifier sales volume and revenue by city-month; air purifier prices and market shares by product
  data_used: []
  treatment_encoding: Spatial RD — cities north of the Huai River boundary are coded as "treated" with higher PM10 due to
    coal heating; instrument for PM10 with the north-side indicator × winter interaction
  comparison: Cities just north versus just south of the Huai River boundary, within winter heating months; structural demand
    estimation with instruments for endogenous prices
  empirical_design: Spatial regression discontinuity at the Huai River boundary; structural demand estimation (random-coefficients
    logit) for marginal WTP; difference-in-discontinuity for pre/post-2013 information environment change
  assumptions:
  - smooth city characteristics across boundary
  - boundary location exogenous
  - distance-to-plant instruments for prices
  - no differential sorting across boundary
  - WTP estimates reflect true preferences
  threats_addressed:
  - boundary confounders via geographic controls and summer placebo
  - endogenous prices via distance instruments
  - sorting via population density tests
  - information effects via pre/post analysis
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
superseded_by: china-huai-river-heating-air-pollution
---
## Institutional Background

China's winter heating policy was established in the 1950s–1960s as part of the centrally planned economy. The government drew a line along the Huai River and Qinling Mountains: cities north of this line receive government-subsidized, coal-fired centralized heating during winter months (November through March); cities south of the line do not. The rationale was climatic — northern China is colder — but the precise boundary follows an ancient geographic and cultural dividing line between northern and southern China. [E1]

The policy has profound environmental consequences. Coal combustion for winter heating is a major source of ambient particulate matter (PM10 and PM2.5). Cities north of the boundary experience PM10 concentrations that are 24–39 μg/m³ higher during winter months than comparable cities just south of the boundary. This pollution differential is large: it represents roughly 20–30% of average ambient PM10 levels in Chinese cities during the study period. [E1]

## What Changed

The heating policy created a persistent, quasi-experimental difference in winter air pollution between cities that are otherwise similar except for their location relative to a historical administrative boundary. From the household's perspective, whether their city has higher or lower winter pollution depends on a decision made by central planners decades before they were born. [E1; analytical inference]

## Implementation and Assignment

The forcing variable is geographic distance to the Huai River-Qinling Mountains boundary (positive on the north side, negative on the south side). Cities just north of the boundary receive centralized heating and have higher winter PM10; cities just south do not. The identifying assumption is that all other determinants of air purifier demand vary smoothly across the boundary. Because the boundary was set in the 1950s based on climatic and historical considerations rather than contemporary air quality or economic factors, it is plausibly exogenous. [E1]

## Why This Creates Empirical Variation

The spatial RD design compares households in cities very close to, but on opposite sides of, the heating boundary. These cities share similar climates, economies, and demographic profiles, but differ sharply in winter air pollution due to the heating policy. This allows estimation of the causal effect of pollution on air purifier purchases — and through a structural demand model, households' marginal willingness-to-pay for pollution reduction. The paper also exploits the 2013 "airpocalypse" — when Beijing's extreme pollution received worldwide media coverage — as a temporal shock to information, finding that WTP approximately tripled after 2013. [E1; analytical inference]

## Identification Risks

The Huai River boundary is a real geographic and climatic divide, not just an arbitrary administrative line. If cities on opposite sides differ in temperature, humidity, economic development, or other factors that independently affect air purifier demand, the RD estimates may be confounded. The paper addresses this by controlling for climatic variables and by comparing winter and summer pollution gradients. A subtler concern is that the boundary's location — following a river — may not be an ideal RD setting because geographic barriers (rivers, mountains) themselves create economic discontinuities. The fuzzy RD design helps address the fact that the pollution "dose" at the boundary is not a perfect step function. [E1; analytical inference]

## Data Requirements

The design requires: (1) retail scanner data on air purifier sales by city and month; (2) city-level PM10 concentration data from MEP monitoring stations; (3) weather data (temperature, humidity) from CMA; (4) city geographic coordinates for computing distance to the Huai River boundary; and (5) household demographic data for the demand model. The scanner data (690 products across 80 cities, 2006–2014) is the most unique component. [E1]

## Evidence Notes

E1 is the published JPE article. The paper's key contributions are: (1) a novel spatial RD design using China's historical heating boundary; (2) market-based revealed-preference estimates of WTP for clean air (approximately $1.34 per household per μg/m³ of PM10 reduction per year); (3) evidence that information dramatically affects valuation (WTP roughly tripled after 2013); and (4) a structural demand model for durable goods (air purifiers) that handles the infrequent-purchase nature of the product. The finding that WTP is larger than typical engineering-cost estimates for pollution abatement suggests that pollution reduction investments may pass cost-benefit tests more easily than previously thought.

## Deprecation Notice

**Deprecated 2026-07-13 (task-164ccc1cb13e)**: This record is superseded by `china-huai-river-heating-air-pollution`. Both records describe the same variation case — the spatial RD at China's Huai River-Qinling Mountains heating boundary. The policy boundary (established 1950s), assignment mechanism (geographic location north vs. south → coal heating → particulate matter), treatment and control definitions, and core identification strategy (spatial RD) are identical. The differences between this record and the retained one are entirely in the research paper applied (Ito and Zhang 2020 JPE vs. Almond et al. 2009 AER), outcomes studied (WTP for clean air vs. mortality/life expectancy), time period (2006–2014 vs. 1981–1993), and specific econometric methods layered on the spatial RD — all appropriately captured as distinct `design_applications` of the same variation in the retained record. [analytical inference]
