---
schema_version: 2
id: us-air-pollution-wind-direction-iv
name: Daily Wind Direction as an Instrument for Acute PM2.5 Air Pollution Exposure among US Elderly
aliases:
- Wind direction instrument for air pollution
- PM2.5 mortality wind IV
- Deryugina air pollution Medicare

status: extracted
provenance:
  task_id: task-e91234691f77
scope:
  country: United States
  regions:
  - All US counties within 100 miles of air pollution monitors
  domains:
  - environment
  - health
  - public-finance
  - mortality
  - healthcare-costs
  variation_type: event-shock
  knowledge_role: transferable-method
  china_relevance: The source setting is outside China; retain the reusable identification
    construction rather than recommend the foreign shock as a China treatment. The wind-direction
    IV logic has been partially transferred to China studies of firm productivity, straw-burning
    mortality, and ozone-mortality, but each transfer uses a different source-to-receptor
    construction and none replicates the full US Medicare county-day design.
identity:
  instrument: Daily county-level wind direction interacted with spatial monitor groups,
    used as an instrument for daily county-level PM2.5 concentrations
  authority: Not applicable — meteorological phenomenon; instrument exploits physical
    atmospheric transport
  legal_identifiers: []
  implementation_regime: The construction relies on (1) daily PM2.5 readings from EPA
    Air Quality System monitors, (2) daily wind direction from NCEP NARR reanalysis
    interpolated to monitor locations, and (3) county-day mortality/healthcare outcomes
    from Medicare. Monitors are grouped into 100 geographic clusters (k-means on longitude/latitude)
    to force a common first-stage effect within each group, reducing measurement error
    from local source-monitor configuration. The excluded instruments are interactions
    of 90-degree wind-direction quadrant indicators with monitor-group indicators,
    omitting the [270,360) quadrant.
  assignment_mechanism: Conditional on county, state-by-month, month-by-year fixed effects
    and flexible weather controls, daily variation in wind direction within a monitor
    group is plausibly exogenous to county-day health shocks and affects mortality only
    through transported PM2.5
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 1999
  implementation_end: 2013
  local_timing: Daily variation — each day wind direction assigns different counties to
    high or low pollution exposure. The main US paper uses 1999–2011 for pollution/weather
    and 1999–2011 Medicare claims; later work extends to 2013.
  anticipation: Wind direction is unpredictable beyond short-term weather forecasts;
    local residents cannot systematically anticipate and avoid exposure based on wind
    patterns
  last_verified: '2026-07-13'
assignment:
  unit: County-day
  treated: Counties that lie downwind of pollution sources on a given day, as predicted
    by their monitor group's wind-direction quadrant
  comparison_pool: Same county on days with different wind-direction-driven PM2.5 levels;
    counties in the same monitor group on days with different wind directions
  rule: For each county-day, determine the monitor group and the daily average wind direction
    quadrant; the excluded instruments are group × quadrant interactions. The first stage
    predicts county-day PM2.5 from these interactions plus controls and fixed effects.
  intensity: Continuous — predicted PM2.5 from downwind monitors, with coefficient allowed
    to vary by monitor group and quadrant
  exemptions: []
  compliance: Not applicable — exposure is determined by physical atmospheric processes,
    not individual choice
  exposure_construction: >
    Step 1: Assign each county to a monitor group (k-means cluster of PM2.5 monitors).
    Step 2: For each monitor, interpolate daily u/v wind components from NARR reanalysis
    and convert to wind direction. Step 3: Code wind direction into 90-degree quadrants
    [0,90), [90,180), [180,270), omitting [270,360). Step 4: Construct excluded instruments
    as monitor-group indicators interacted with quadrant indicators. Step 5: First-stage
    regression predicts county-day PM2.5 using these instruments, flexible weather controls
    (temperature bins, precipitation/wind-speed deciles and interactions), two leads and
    two lags of weather, county FE, state-by-month FE, and month-by-year FE. Step 6: Use
    predicted PM2.5 in the second stage for county-day mortality/healthcare outcomes.
  required_identifiers:
  - county code
  - calendar date
  - monitor group
  - wind direction quadrant
  spillovers: Pollution disperses continuously; downwind definition requires arbitrary
    distance and direction cutoffs; modeling choices about the downwind window affect exposure
    classification. Neighboring counties in the same monitor group share common wind shocks,
    so standard errors are clustered by county.
research_compatibility:
  outcome_domains:
  - mortality
  - healthcare utilization
  - medical costs
  - hospital admissions
  - emergency room visits
  - drug expenditures
  - firm productivity
  - labor productivity
  - cognitive performance
  affected_populations:
  - elderly (Medicare population, age 65+)
  - individuals with pre-existing respiratory or cardiovascular conditions
  - low-income elderly
  - manufacturing workers
  - students
  mechanism_channels:
  - acute PM2.5 inhalation
  - respiratory inflammation
  - cardiovascular stress
  - oxidative stress
  - systemic inflammation
  - cognitive impairment
  - worker absenteeism and productivity
  best_for:
  - Studying the acute (daily to weekly) health or productivity effects of PM2.5 exposure
  - Outcomes measurable in high-frequency administrative claims or firm/worker data
  - Designs requiring a source of quasi-random variation in pollution exposure at fine spatial
    and temporal scales
  not_good_for:
  - Chronic (multi-year) exposure effects
  - Populations or outcomes without high-frequency geographic identifiers
  - Areas without dense pollution-monitor coverage
  - Outcomes requiring precise individual exposure measurement rather than county/city averages
design:
  claim_type: method-pattern
  affordances:
  - daily variation in wind direction is driven by large-scale weather systems
  - fixed pollution monitor locations provide spatial anchors
  - high-dimensional fixed effects absorb confounding
  - can be extended to co-pollutants (ozone, CO) and other outcomes
  candidate_designs:
  - instrumental variables with wind direction × monitor-group interactions
  - county fixed effects panel using within-county variation over time
  - day fixed effects absorbing common daily shocks
  - distributed-lag models for cumulative exposure effects
  identifying_variation: Daily changes in which counties are downwind of transported pollution,
    identified by the interaction of 90-degree wind-direction quadrants with 100 geographic
    monitor groups. This isolates variation in PM2.5 driven by non-local pollution transport
    rather than local economic activity.
  assumptions:
  - Daily wind direction within a monitor group is as good as randomly assigned conditional
    on county, state-by-month, and month-by-year fixed effects and flexible weather controls
  - Wind direction affects the outcome only through PM2.5 (exclusion restriction)
  - County-day PM2.5 from monitors adequately proxies population exposure
  - No systematic avoidance behavior based on short-term wind forecasts
  diagnostics:
  - First-stage F-statistic for the excluded wind-direction × monitor-group instruments
  - Placebo test — instrument should not predict outcomes on adjacent days
  - Test sensitivity to alternative numbers of monitor groups and wind-direction windows
  - Compare IV and OLS estimates for evidence of measurement error or avoidance bias
  - Test for effects on planned (non-ER) hospital admissions as a placebo
  - Examine effects by cause of death and pre-existing conditions
  - Cluster standard errors by county and test alternative clustering
  primary_strategy: Two-stage least squares with high-dimensional fixed effects, using
    monitor-group × wind-direction-quadrant interactions as excluded instruments for daily
    county-level PM2.5
  estimand: The local average treatment effect of acute PM2.5 exposure on county-day mortality,
    healthcare utilization, or medical costs among the population observed, conditional on
    the stated exclusion restriction
  treatment_variable: Daily county-level PM2.5 concentration, instrumented with predicted
    PM2.5 from the first stage; distributed-lag models estimate cumulative effects over
    multiple days
  comparison_logic: Same county on days with different wind-direction-driven PM2.5 levels,
    after conditioning on fixed effects and weather
  estimation_notes: First stage interacts 90-degree wind-direction quadrant indicators with
    100 monitor-group indicators; second stage uses predicted PM2.5. Include flexible weather
    controls, two leads and two lags of weather, county FE, state-by-month FE, month-by-year
    FE. Weight by population when outcomes are per capita. Cluster standard errors by county.
threats:
- type: exclusion-restriction-violation
  basis: inferred
  condition: Wind direction may affect health through channels other than PM2.5 (e.g., temperature,
    humidity, pollen, other pollutants) — though day fixed effects and flexible weather controls
    absorb many shared meteorological factors
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for temperature, humidity, and co-pollutants
  - test whether instrument predicts non-respiratory outcomes
  - assess robustness to wind-speed conditioning
- type: measurement-error-in-exposure
  basis: documented
  condition: County-day PM2.5 from distant monitors is a noisy proxy for individual-level exposure,
    which varies with indoor versus outdoor time, personal mobility, housing quality, and individual
    susceptibility
  evidence_refs:
  - E1
  possible_diagnostics:
  - compare IV and OLS estimates
  - use alternative exposure measures
  - bound attenuation bias
- type: spatial-misclassification
  basis: inferred
  condition: Wind direction instrument construction requires arbitrary decisions about monitor
    groups, distance cutoffs, and direction sectors that may affect results
  evidence_refs:
  - E1
  possible_diagnostics:
  - test alternative numbers of monitor groups
  - use continuous wind-direction measures
  - apply machine-learning-based exposure classification
- type: population-selection
  basis: inferred
  condition: The Medicare population (65+) has elevated baseline mortality risk; estimates may
    not generalize to younger populations, and harvesting may affect interpretation
  evidence_refs:
  - E1
  possible_diagnostics:
  - estimate distributed-lag models to detect harvesting
  - compare effects by age and baseline health
  - analyze cause-specific mortality
- type: china-data-availability
  basis: inferred
  condition: China lacks a national daily mortality/healthcare claims file equivalent to US Medicare,
    so the exact county-day health design is not directly replicable without restricted-access data
  evidence_refs:
  - E3
  - E4
  - E5
  possible_diagnostics:
  - verify availability of China CDC DSP county-month mortality or hospital administrative records
  - verify CNEMC monitor coverage and CMA/NCEP wind data for the study period
  - verify the ability to link outcomes to county/city of residence
empirical_requirements:
  contract_version: 1
  population: Counties, firms, or individuals observed before and during the study period with
    geographic identifiers linkable to pollution monitors and weather data
  observation_unit: County-day or lower-level unit linkable to county-day exposure
  geography_level: County or city
  time_start: 1999
  time_end: 2013
  minimum_frequency: daily
  minimum_pre_periods: 180
  minimum_post_periods: 180
  required_fields:
  - PM2.5 daily concentration by monitor
  - wind direction by monitor or county
  - mortality or outcome count by county-day
  - temperature
  - precipitation
  - humidity or wind speed
  required_identifiers:
  - county code
  - calendar date
  - monitor group
  - wind direction quadrant
  treatment_key:
  - county code
  - calendar date
  - monitor group
  treatment_source: >
    EPA Air Quality System for PM2.5 monitor data; NCEP NARR reanalysis for wind direction
    and meteorological data; Medicare administrative claims for health outcomes. For China
    transfers: CNEMC for PM2.5, CMA/NCEP/ERA5 for wind, China CDC DSP or hospital administrative
    data for outcomes, NBS ASIF or firm payroll data for productivity.
  measurement_risks:
  - monitor-to-county distance interpolation error
  - wind direction measurement error at individual monitors
  - exposure misclassification due to indoor time and mobility
  - temporal mismatch between 24-hour average PM2.5 and daily wind patterns
  - restricted access to China health administrative data
  - inconsistent city/county boundary codes over time in China
evidence:
- id: E1
  source_type: paper
  citation: 'Deryugina, Tatyana, Garth Heutel, Nolan H. Miller, David Molitor, and Julian
    Reif. 2019. "The Mortality and Medical Costs of Air Pollution: Evidence from Changes
    in Wind Direction." American Economic Review 109 (12): 4178–4219.'
  url: https://doi.org/10.1257/aer.20180279
  date: 2019
  supports:
  - identity
  - assignment
  - design
  - design_applications
  verification_status: verified
  access_level: full-text
  locator: Sections II–IV; equation (2) for the first-stage specification using monitor-group
    × wind-direction-quadrant interactions; Table A12 for first-stage and reduced-form estimates;
    Section III for data sources (EPA AQS, NARR, Medicare 1999–2011)
- id: E2
  source_type: replication
  citation: Deryugina et al. replication package via AEA Data and Code Repository
  url: https://doi.org/10.1257/aer.20180279
  date: 2019
  supports:
  - design_applications
  - method_transfer
  verification_status: verified
  access_level: replication
  locator: AEA Data and Code Repository; contains county-day construction code, first-stage
    algorithms, and robustness checks
- id: E3
  source_type: paper
  citation: 'Fu, Shihe, V. Brian Viard, and Peng Zhang. 2021. "Air Pollution and Manufacturing
    Firm Productivity: Nationwide Estimates for China." The Economic Journal 131 (640):
    3241–3273.'
  url: https://doi.org/10.1093/ej/ueab033
  date: 2021
  supports:
  - method_transfer
  verification_status: verified
  access_level: full-text
  locator: Main instrument is thermal inversions; Online Appendix reports an alternative
    wind-direction IV using upwind-city PM10 as an instrument for focal-city productivity,
    demonstrating partial transfer of the wind-direction logic to Chinese firm data
- id: E4
  source_type: paper
  citation: 'He, Guojun, Tong Liu, and Maigeng Zhou. 2020. "Straw Burning, PM2.5, and Death:
    Evidence from China." Journal of Development Economics 145: 102468.'
  url: https://doi.org/10.1016/j.jdeveco.2020.102468
  date: 2020
  supports:
  - method_transfer
  verification_status: verified
  access_level: full-text
  locator: Section 5 reports IV estimates using upwind straw burning (wind direction × satellite
    fire locations) as an instrument for county-month PM2.5, linking to China CDC Disease
    Surveillance Point mortality; shows wind-direction logic can be combined with a point-source
    event in China
- id: E5
  source_type: paper
  citation: 'Qiu, Yuqian, Ying Liu, Wenbiao Shi, and Maigeng Zhou. 2024. "The Impact of Ozone
    Pollution on Mortality: Evidence from China." Journal of Environmental Economics and
    Management 125: 102980.'
  url: https://doi.org/10.1016/j.jeem.2024.102980
  date: 2024
  supports:
  - method_transfer
  verification_status: verified
  access_level: full-text
  locator: Constructs IV as average ozone in nearby upwind cities weighted by inverse distance
    and cosine of wind angle; uses weekly city-level mortality data and weather controls;
    another China application of source-to-receptor wind logic
design_applications:
- paper: 'The Mortality and Medical Costs of Air Pollution: Evidence from Changes in Wind Direction'
  doi: 10.1257/aer.20180279
  journal: American Economic Review
  year: 2019
  research_question: What is the causal effect of acute PM2.5 exposure on mortality, healthcare
    utilization, and medical costs among the US elderly, and how large are the associated
    external costs?
  population: US Medicare beneficiaries (age 65+) from 1999 to 2011, residing in counties with
    PM2.5 monitor coverage
  outcome: Daily all-cause mortality, cause-specific mortality, emergency room visits, hospital
    admissions, drug expenditures, total medical spending
  data_used:
  - EPA Air Quality System daily PM2.5 monitor readings
  - NCEP NARR daily reanalysis wind direction and weather
  - Medicare enrollment, MedPAR inpatient, outpatient claims 1999–2011
  - county-to-monitor spatial crosswalk
  treatment_encoding: Daily county-level PM2.5 concentration instrumented with predicted PM2.5
    from monitor-group × wind-direction-quadrant interactions; distributed-lag models estimate
    cumulative effects over multiple days
  comparison: Same county on days with different wind-direction-driven PM2.5 levels (within-county
    variation, conditional on day fixed effects)
  empirical_design: Instrumental variables with high-dimensional fixed effects (county, state-by-month,
    month-by-year), using monitor-group × wind-direction-quadrant interactions as excluded
    instruments for PM2.5
  assumptions:
  - wind direction is as good as randomly assigned conditional on fixed effects and weather
  - exclusion restriction holds
  - monitor PM2.5 adequately proxies county-level exposure
  threats_addressed:
  - measurement error via IV
  - avoidance behavior via IV
  - confounding meteorological factors via flexible weather controls and fixed effects
  - mortality displacement via distributed lags and life-years-lost machine-learning approach
  evidence_refs:
  - E1
  - E2
readiness_blockers:
- China lacks a national daily county-level mortality/healthcare claims file equivalent to US
  Medicare; the exact source-paper design is therefore not directly replicable without restricted
  China CDC Disease Surveillance Point or hospital administrative data.
- The first-stage strength of the Deryugina et al. construction in China has not been tested
  with CNEMC monitors and CMA/NARR wind data; monitor density and wind-reanalysis resolution
  may differ materially from the US.
- No China study has implemented the full k-means monitor-group × 90-degree wind-quadrant
  specification at the county-day level; existing transfers use coarser city-week/county-month
  data or source-specific events (straw burning), so generalizability of the precise IV to
  routine daily PM2.5 in China remains unverified.
- Concurrent environmental policies (e.g., Air Pollution Prevention and Control Action Plan,
  winter heating switching, straw-burning bans) and data manipulation concerns may violate
  the exclusion restriction or create regime-specific first-stage instability in China.
method_transfer:
  source_context: United States. Deryugina et al. (2019) use daily county-level wind direction
    interacted with 100 geographic monitor groups as an IV for daily county PM2.5, estimating
    effects on US elderly mortality and Medicare costs.
  strategy_family: Instrumental variables with high-dimensional fixed effects, using daily
    wind-direction × monitor-group interactions as excluded instruments for PM2.5
  reusable_logic: Large-scale weather systems determine daily wind direction, which in turn
    determines whether a given location receives pollution transported from upwind sources.
    Conditional on location and time fixed effects and flexible weather controls, this daily
    wind-driven reshuffling of pollution exposure is plausibly exogenous to local health shocks.
  construction_steps:
  - Identify all PM2.5 monitors in the study area and cluster them into geographic groups (k-means
    on coordinates) so that monitors in the same group face similar upwind source regions.
  - Obtain daily wind direction at each monitor by interpolating u/v wind vectors from reanalysis
    data (e.g., NARR, ERA5, CMA) and converting to a 0–360 degree bearing.
  - Code wind direction into quadrants (e.g., 90-degree bins) and create excluded instruments
    as monitor-group indicators interacted with quadrant indicators.
  - Estimate a first-stage regression of county-day PM2.5 on the excluded instruments, flexible
    weather controls, and fixed effects (county, state-by-month, month-by-year).
  - Use predicted PM2.5 in a second-stage regression of the outcome (mortality, hospitalization,
    productivity) on county-day PM2.5, with the same controls and fixed effects.
  source_treatment_or_endogenous_variable: Daily county-level PM2.5 concentration (or other
    pollutant such as ozone or CO). In China transfers the endogenous variable is typically
    city-day or county-month PM2.5/ozone.
  source_instrument_or_assignment: Excluded instruments are monitor-group indicators interacted
    with 90-degree wind-direction quadrant indicators. Other papers use variants such as upwind-city
    pollutant concentrations weighted by inverse distance and cosine of wind angle, or upwind
    straw-burning counts.
  first_stage_or_contrast: The first stage predicts county-day PM2.5 from group × quadrant
    interactions. Deryugina et al. (2019) report strong first-stage coefficients (e.g., 2.3–2.6
    μg/m3 for the high-pollution wind-direction indicator) and the F-statistic is well above
    conventional weak-instrument thresholds.
  identifying_assumptions:
  - Daily wind direction within a monitor group is as good as randomly assigned conditional
    on county, state-by-month, month-by-year fixed effects and flexible weather controls.
  - Wind direction affects the outcome only through transported PM2.5 (exclusion restriction).
  - Monitor readings adequately proxy population exposure; grouping monitors reduces local-source
    measurement error.
  diagnostics:
  - Report first-stage F-statistics and coefficients by monitor group and quadrant.
  - Placebo test using adjacent-day or non-target outcomes.
  - Sensitivity to number of monitor groups, quadrant width, and monitor-radius restrictions.
  - Compare IV and OLS estimates to assess measurement-error bias.
  - Test for effects on planned admissions or other outcomes that should not respond to acute
    pollution.
  china_use_cases:
  - Estimate acute effects of PM2.5 on daily mortality in Chinese cities using CNEMC monitors,
    ERA5/CMA wind, and city/county mortality data from China CDC DSP or local CDC.
  - Estimate effects of PM2.5 or ozone on hospital emergency-room visits using hospital administrative
    data linked to city-day pollution and wind.
  - Estimate effects of PM2.5 on short-run manufacturing firm productivity or worker output
    using NBS firm surveys or matched employer-employee data with firm/city-day pollution.
  - Use source-specific events (straw burning, sandstorms, industrial accidents) combined with
    wind direction to instrument pollution in rural or industrial counties.
  china_data_requirements:
  - >
    Daily PM2.5 (and optionally ozone/CO/NO2/SO2) concentrations from CNEMC ground monitors or
    validated satellite/reanalysis products; monitor coordinates and operational status.
  - >
    Daily wind direction and weather variables from CMA surface stations, NCEP NARR, or ERA5
    reanalysis; interpolation method to monitor/county centroids.
  - >
    High-frequency health or productivity outcomes with geographic identifiers. Mortality:
    China CDC Disease Surveillance Point county-month or city-day death records (restricted).
    Healthcare: hospital admission/emergency-visit records from HQMS or provincial hospital
    information systems (restricted). Productivity: NBS Annual Survey of Industrial Firms,
    tax survey, or matched employer-employee data at city-year or firm-year frequency (daily
    productivity data are rare).
  - >
    County/city boundary crosswalks and population denominators; stable administrative codes
    over the study period.
  transfer_limits:
  - China has no national daily county-level mortality or healthcare claims file comparable
    to US Medicare, so the full county-day design is feasible only in cities or counties with
    accessible, high-frequency administrative records.
  - Monitor density and data quality vary across China; the first stage may be weaker or more
    measurement-error-prone in western or rural areas with sparse monitors.
  - Pollution in China is dominated by different sources (coal combustion, industry, straw burning,
    dust, secondary aerosols) than in the US, so the exclusion restriction must be reassessed
    for each source region and season.
  - Concurrent policies (heating switching, straw-burning bans, Air Pollution Action Plan, COVID-19
    lockdowns) and potential air-quality data manipulation can break the exclusion restriction
    or create structural breaks in the first stage.
  - The method identifies acute, short-run effects only; it cannot be used for chronic multi-year
    exposure without a different source of variation.
  - The instrument relies on stable upwind source regions; rapid urbanization, relocation of
    pollution sources, or monitor-network expansion can make monitor groups unstable over time.
---
## Institutional Background

Ambient fine particulate matter (PM2.5) is causally linked to respiratory and cardiovascular mortality. The wind-direction instrument exploits a physical fact: whether a given location is downwind of a pollution source on a given day depends on wind direction, which is determined by large-scale weather systems. Conditional on day and location fixed effects and flexible weather controls, the within-location variation in whether an area lies downwind of distant pollution sources is driven by the interaction of fixed monitor locations and daily wind patterns — a source of variation that is plausibly orthogonal to local daily health shocks. [E1]

## What Changed

On any given day, some counties lie downwind of pollution monitors and receive transported PM2.5, while others are upwind or crosswind. The instrument captures the daily reshuffling of which areas receive distant pollution, holding constant the fixed spatial distribution of monitors and pollution sources. [E1]

## Implementation and Assignment

The instrument construction proceeds in several steps: (1) cluster PM2.5 monitors into 100 geographic groups using k-means on coordinates; (2) for each monitor, obtain daily wind direction from reanalysis data; (3) classify each county-day into a 90-degree wind quadrant; (4) construct excluded instruments as monitor-group × quadrant interactions; (5) predict county-day PM2.5 in a first-stage regression with flexible weather controls and high-dimensional fixed effects; (6) use predicted PM2.5 in the second-stage health regression. [E1; E2]

## Why This Creates Empirical Variation

The wind-direction instrument addresses three endogeneity problems in pollution-health relationships: (1) economic activity simultaneously increases pollution and income; (2) individuals may avoid exposure on high-pollution days; and (3) monitors measure location-level, not individual-level, exposure. The instrument isolates the component of PM2.5 variation driven by wind patterns, which is uncorrelated with local economic activity and avoidance behavior. [E1; analytical inference]

## Identification Risks

The exclusion restriction requires that wind direction affects mortality only through PM2.5. This could be violated if wind transports other harmful pollutants (or beneficial substances) from the same sources, or if wind direction correlates with temperature or humidity in ways not absorbed by controls. Measurement error in instrument construction may affect precision. The focus on the elderly Medicare population limits generalizability. [E1; analytical inference]

## Data Requirements

This design requires daily, geographically precise data on: (1) PM2.5 concentrations from monitors; (2) wind direction and weather from reanalysis or weather stations; (3) high-frequency health or productivity outcomes linked to county/city of residence; (4) a spatial crosswalk between monitors and administrative units. In China, the main bottleneck is access to daily county/city mortality or hospital records comparable to Medicare claims. [E1; E3; E4; E5]

## Evidence Notes

E1 provides the complete methodological framework, first-stage specification, main results, and robustness analysis. E2 is the replication package. E3–E5 document China applications that use related wind-direction logic, but they employ coarser temporal scales, source-specific events, or alternative instrument constructions; they do not replicate the full Deryugina et al. county-day Medicare design.
