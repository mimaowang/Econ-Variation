---
schema_version: 2
id: china-thermal-inversion-air-quality-beijing-air-travel
name: China Thermal-Inversion Air-Quality Differentials and Short-Term Air Travel through Beijing (PEK)
aliases:
- Chen Chen Lei Tan-Soo 2020 JoEG air pollution short-term movements flights
- thermal inversion IV air pollution avoidance air travel China
- 热逆温工具变量 空气质量差异 北京首都机场 短期出行
status: grounded
provenance:
  task_id: task-4ff1e6424521
scope:
  country: China
  regions:
  - Beijing Capital International Airport (PEK) and 59 other Chinese cities connected by direct domestic flights, 2008-2010
  domains:
  - environment
  - labor-migration
  - infrastructure-urban
  variation_type: event-shock
  knowledge_role: china-variation
  china_relevance: >
    The variation occurs within China: day-to-day thermal-inversion
    occurrence in Chinese cities shifts near-ground air pollution, and
    Chen, Chen, Lei, and Tan-Soo (2020, Journal of Economic Geography) use
    the resulting origin-destination air-quality differentials, instrumented
    by inversion counts, to estimate short-term avoidance travel on the
    complete set of domestic direct flights through Beijing Capital
    International Airport (PEK). The regional/urban content is the spatial
    air-quality differential between Chinese cities and the intercity
    mobility response, not a policy rollout; this is a meteorological
    instrument, not an administrative reform.
identity:
  instrument: >
    The daily city-level thermal-inversion count: using NASA MERRA-2
    reanalysis temperature profiles on a 0.5-by-0.625-degree grid, an
    inversion is counted in each 6-hour interval when the temperature in the
    first atmospheric layer (about 110 m) is lower than in the second layer
    (about 320 m; the Table 2 note says 330 m, an internal inconsistency the
    paper does not resolve), giving a daily count from 0 to 4 per city.
    Cities are spatially matched to their MERRA-2 grid cells and temperatures
    are averaged. In the paper's 2SLS design the difference in daily
    inversion counts between origin and destination cities instruments the
    difference in daily Air Pollution Index (API); the endogenous variable
    is air quality, not a policy treatment.
  authority: >
    No policy authority assigns treatment. The underlying measurements are
    produced by NASA (MERRA-2 reanalysis, M2I6NPANA), the China National
    Environmental Monitoring Center and Ministry of Environmental Protection
    (daily city API), and the China Meteorological Data Service Center
    (820-station daily weather). The inversion coding rule (layer pair,
    6-hour aggregation) is the authors' construction, following
    Arceo et al. (2016).
  legal_identifiers:
  - 'Chen, Shuai, Yuyu Chen, Ziteng Lei, and Jie-Sheng Tan-Soo. 2020. "Impact of air pollution on short-term movements: evidence from air travels in China." Journal of Economic Geography 20(4): 939-968. DOI: 10.1093/jeg/lbaa005'
  - Open author-archived full text hosted by the Environment for Development (EfD) initiative (efdinitiative.org lbaa005.pdf)
  - 'NASA MERRA-2 dataset M2I6NPANA (0.5 x 0.625 degree, 6-hourly temperature by atmospheric layer)'
  - China National Environmental Monitoring Center daily Air Pollution Index for 120 major cities (PM10, SO2, NO2 composite)
  implementation_regime: >
    Stochastic meteorological realization, not an administrative regime.
    Thermal inversions arise from radiation, subsidence, marine, and
    slope-flow mechanisms and trap pollutants near the ground for short
    episodes. Inversion frequency varies across cities (valley-type and
    northern locations experience more) and across days within city, and the
    design exploits the within-flight-code day-to-day component of that
    variation over 1 March 2008 to 30 April 2010.
  assignment_mechanism: >
    A flight-code-day inherits the API differential between its origin and
    destination cities; day-to-day inversion realizations shift that
    differential with a strong first stage (Kleibergen-Paap F roughly 40-80
    across specifications). Flight-code fixed effects absorb time-invariant
    route characteristics and any preference-based spatial sorting along
    inversion propensity, so identification comes from within-route daily
    variation conditional on date fixed effects and differenced weather
    polynomials. The inversions are not claimed to be intrinsically
    exogenous: validity rests on the stated exclusion restriction and the
    weather controls, not on the instrument's meteorological nature alone.
  parent: null
  related_variations:
  - us-air-pollution-wind-direction-iv
  - china-county-growing-season-rainfall-labor-reallocation
timeline:
  announcement: null
  effective: null
  implementation_start: 2008
  implementation_end: 2010
  local_timing: >
    The flight dataset spans 1 March 2008 to 30 April 2010 per Figure 1,
    Figure 2, and the Table 1 and Table 2 notes; the data-section text says
    "20 April 2010", an unresolved internal discrepancy of ten days. Air
    quality is measured at city-day level (origin API on departure day,
    destination API on arrival day), and inversions are counted per 6-hour
    interval and summed to the day.
  anticipation: >
    The paper argues travellers cannot time trips to inversions themselves
    but can and do use air-quality forecasts, which have been publicly
    available in China since at least 2001: lead-and-lag specifications show
    passenger counts are most sensitive to day-of-travel API, with
    destination leads up to two days also significant, consistent with
    forecast-based planning rather than same-day booking.
  last_verified: '2026-08-15'
assignment:
  unit: >
    Flight-code-day: 499,180 domestic direct flights departing from or
    arriving at Beijing Capital International Airport (PEK) over the study
    period, on 115 unique city routes (122 airport routes) linking 60
    cities, operated by 17 airlines with 32 aircraft types; the data-section
    text reports 1,743 unique flight codes while the regression tables
    report 1,410 flight-code clusters, a discrepancy the paper does not
    explain. Multi-leg flights are excluded.
  treated: >
    Flights whose origin-minus-destination API differential is higher
    (origin dirtier than destination) are expected to carry more passengers;
    treatment intensity is the continuous daily API difference, instrumented
    by the origin-minus-destination difference in daily inversion counts.
    There is no untreated group.
  comparison_pool: >
    The same flight code on other days (flight-code fixed effects absorb
    origin, destination, airline, aircraft type, and scheduled times), and
    other flights on the same date (date fixed effects for month, year,
    day-of-week, holidays, and holiday-makeup weekends).
  rule: >
    Two-stage least squares (paper Equations 1 and 2): regress log
    passengers per flight-code-day on the API difference between origin and
    destination, instrumented by the corresponding inversion-count
    difference, with flight-code fixed effects, date fixed effects,
    second-order polynomials of six differenced weather variables
    (temperature, precipitation, sunshine duration, wind speed, relative
    humidity, atmospheric pressure; city weather built by inverse-distance
    weighting of stations within 100 km of the city centroid), weighting by
    origin-city population, and standard errors clustered by flight code.
  intensity: >
    In the full specification a one-unit increase in origin-over-destination
    API raises flight passengers by about 0.36 percent (0.18 percent without
    controls); by cabin class, about 0.34 percent for economy and 0.87
    percent for first class. Spline specifications show the marginal effect
    rising with the size of the API differential (non-linear response).
    A back-of-the-envelope calculation in the paper implies roughly 92,671
    additional pollution-induced passengers through PEK annually per unit of
    Beijing average annual API.
  exemptions:
  - Multi-leg flights are removed because passenger loads at intermediate stops are unobserved
  - International flights are outside the design and serve as a falsification outcome (visa requirements and cost make them implausible avoidance trips)
  - Days when PM is not the dominant pollutant in both cities form a separate, smaller subsample with weaker results
  compliance: >
    Exposure is measured, not chosen, but two measurement concerns are
    documented in the paper: city API during 2008-2010 is the official
    CNEMC/MEP series that Ghanem and Zhang (2014) show was systematically
    manipulated around the "polluted day" threshold, and city weather and
    inversion exposures are gridded constructs matched to city centroids
    rather than ground truth. The observed API-difference range is -467 to
    467 with mean about 5.3.
  exposure_construction: >
    Author construction: daily city inversion counts from MERRA-2 6-hourly
    layer temperatures (first layer about 110 m versus second layer about
    320 m; robustness uses the third layer, about 540 m, and a daily binary
    coding), city-day API from CNEMC/MEP, and city-day weather from
    inverse-distance-weighted CMDC station data within a 100 km centroid
    radius (alternative radii in robustness). Passengers per flight by cabin
    class, airline, aircraft, and scheduled and actual times come from a
    complete flight load-factor dataset whose provider and access terms are
    not disclosed in the inspected text.
  required_identifiers:
  - flight code stable over the study period (clustering and fixed-effect unit)
  - origin and destination city (or airport) per flight, with a city-airport crosswalk for the 122 airport routes across 60 cities
  - date of departure and arrival for joining city-day API, weather, and inversion counts
  - MERRA-2 grid cell assignment per city for the inversion construction
  spillovers: >
    Substitution between flights serving the same route is tested by
    aggregating to the route-day level (coefficient rises to about 0.49
    percent, so flight-level estimates are not an artifact of within-route
    substitution). Cross-city general-equilibrium effects of induced travel
    on destination air quality or congestion are not modeled; the paper
    notes reverse causality from travel to economic activity and pollution
    as an endogeneity motivation rather than estimating it.
research_compatibility:
  outcome_domains:
  - short-term intercity mobility and avoidance behavior in response to air pollution
  - demand for intercity transport (passenger loads, occupancy) as an environmental-quality response margin
  - income-stratified averting behavior (cabin-class heterogeneity)
  - use of air-quality forecasts in travel planning
  affected_populations:
  - Air passengers on domestic routes through Beijing Capital International Airport, 2008-2010 (about 144 passengers per flight, 65 percent average occupancy)
  - Residents of the 60 connected Chinese cities exposed to daily air-quality fluctuations
  mechanism_channels:
  - thermal inversions trapping pollutants near the ground and worsening city-day air quality
  - origin-destination air-quality differentials changing the relative attractiveness of short trips
  - forecast availability enabling day-of-travel-sensitive planning
  - income or willingness-to-pay differences showing up as cabin-class heterogeneity
  best_for:
  - Designs that need a daily-frequency, plausibly exogenous shifter of city-level air quality in China around 2008-2010 with a strong first stage
  - Studies of short-term avoidance mobility where flight-code and date fixed effects can absorb route attractiveness and calendar shocks
  - Analyses distinguishing push (origin) from pull (destination) air-quality effects and their timing (leads and lags)
  not_good_for:
  - 'Questions that need post-2013 air quality: the API series and the 120-city reporting regime ended with the 2013 AQI transition, and PM2.5 is not separately reported in this API period'
  - Designs about permanent migration or long-run sorting; the unit of analysis is a flight-day, and spatial sorting is absorbed, not estimated
  - Questions needing the traveler's true origin or destination; only the flight's endpoint cities are observed, and onward connections are unobserved
  - Designs that need ground-level pollution measurement independent of the official API series, which carries documented manipulation risk in this period
design:
  claim_type: causal
  affordances:
  - Daily-frequency inversion shocks with a strong first stage (KP F roughly 40-80) on city-day air quality, unusual temporal resolution for Chinese pollution variation
  - A complete flight load-factor panel with cabin-class splits, enabling income-stratified averting estimates on the same flight
  - Flight-code fixed effects that absorb route attractiveness, airline, aircraft, and schedule, isolating within-route daily variation
  - Lead-and-lag API structures that separate forecast-based planning from same-day responses, and spline specifications that expose non-linear responses
  candidate_designs:
  - 2SLS of log flight passengers on origin-minus-destination API instrumented by the inversion-count difference, with flight-code and date fixed effects and differenced weather polynomials
  - Cabin-class-split versions of the same 2SLS for economy versus first-class passenger counts
  - Spline (piecewise-linear) 2SLS in the API differential with two endogenous spline segments instrumented by origin and destination inversion counts
  - Route-day aggregation, occupancy-rate outcomes, and delay/cancellation outcomes as robustness and mechanism checks
  identifying_variation: >
    Within-flight-code, day-to-day variation in the origin-destination API
    differential generated by differential thermal-inversion occurrence,
    conditional on date fixed effects and differenced weather; cross-sectional
    support comes from climatic heterogeneity across the 60 connected cities.
  primary_strategy: >
    Instrumental-variables estimation of the effect of air quality on
    short-term travel. The endogenous variable is the daily API difference
    between origin and destination city; the instrument is the daily
    difference in thermal-inversion counts (0-4 per city-day from MERRA-2
    layer-temperature comparisons); the first stage is reported with
    Kleibergen-Paap F-statistics of roughly 40-80; the exclusion restriction
    asserted is that inversions shift flight demand only through air
    quality, defended by controlling for six differenced weather variables
    as polynomials and by flight-code fixed effects absorbing location-level
    sorting along inversion propensity.
  estimand: >
    The local average effect of a one-unit widening of the
    origin-over-destination daily API differential on log passengers per
    flight-day, for inversion-induced variation in air quality on domestic
    direct flights through PEK, 2008-2010; headline estimate about 0.36
    percent per API unit.
  treatment_variable: >
    Daily origin-minus-destination Air Pollution Index difference (CNEMC/MEP
    city API, composite of PM10, SO2, and NO2), instrumented by the
    origin-minus-destination difference in daily thermal-inversion counts
    from MERRA-2.
  comparison_logic: >
    Within flight code over days, net of common date shocks; the comparison
    fails if inversions correlate with travel through non-air-quality
    channels (weather controls and their cubic versions address this
    partially), if inversion-prone locations attract different traveler
    types (flight-code fixed effects address time-invariant sorting), or if
    the official API is manipulated in ways correlated with true pollution
    (documented for this period by Ghanem and Zhang 2014 and left as a
    measurement concern).
  estimation_notes: >
    Estimating sample is 499,180 flight-code-day observations (1,410
    flight-code clusters in the regression tables). Baseline 2SLS with full
    controls: 0.36 percent per API unit (OLS is smaller and can be negative,
    consistent with attractiveness confounding). Cabin-class split: 0.34
    percent economy, 0.87 percent first class. Temporal heterogeneity:
    insignificant for midnight-5am departures, about 0.27 percent for
    morning, 0.39 percent for afternoon and evening; by season, about 0.65
    percent in winter, insignificant in summer, 0.20-0.25 percent in spring
    and autumn. Spatial heterogeneity: stronger for destinations at least
    1,000 km away and weaker for destinations in the winter-heating season;
    restricting to non-provincial-capital destinations (where onward
    connections are unlikely) raises the coefficient to about 0.6 percent.
    Robustness covers alternative inversion codings (third layer, daily
    binary), PM-dominant subsamples, dropping weather controls (0.28
    percent) and cubic weather (about 0.4 percent), route-day aggregation
    (0.49 percent), occupancy-rate outcomes, delay and cancellation margins
    (no significant relationship), and an international-flight falsification
    (no effect).
  assumptions:
  - 'Exclusion restriction: conditional on differenced weather polynomials, date fixed effects, and flight-code fixed effects, thermal-inversion counts affect flight passenger counts only through air quality'
  - The first stage is strong and monotone (inversions trap pollutants near the ground; KP F roughly 40-80)
  - Time-invariant route attractiveness and traveler sorting are absorbed by flight-code fixed effects, and remaining time-varying attractiveness shocks (major events) are not systematically aligned with inversion episodes
  - Official city API measures true pollution up to error uncorrelated with the instrument, despite documented threshold manipulation in this period
  diagnostics:
  - First-stage Kleibergen-Paap F-statistics of roughly 40-80 across specifications
  - OLS-versus-IV comparison exposing the attractiveness bias (smaller or negative OLS coefficients)
  - International-flight falsification showing no API-differential effect
  - Delay and cancellation outcome regressions showing no significant air-quality relationship, ruling out a supply-side arrival-rate channel
  - Alternative instrument codings (540 m layer, daily binary) and alternative IDW radii leaving estimates at about 0.34-0.35 percent
  - Lead-and-lag API specifications isolating day-of-travel sensitivity, consistent with forecast use
threats:
- type: exclusion_restriction_weather_channels
  basis: reported
  condition: Thermal inversions correlate with temperature, wind, and pressure, which can shift travel demand directly; the paper controls second-order (and, in robustness, cubic) polynomials of six differenced weather variables, but weather-functional-form sensitivity is visible (0.28 percent without weather controls versus 0.36 percent baseline).
  evidence_refs:
  - E1
  possible_diagnostics:
  - Compare weather-control sets and functional forms systematically
  - Test whether inversions predict travel on routes where API is unavailable or flat
- type: api_measurement_manipulation
  basis: documented
  condition: The 2008-2010 official API series is the one Ghanem and Zhang (2014) show was manipulated around the "blue sky" threshold; the paper cites this as a motivation for the IV but cannot correct threshold-specific misreporting, and the instrument only addresses manipulation correlated with inversions.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Rebuild exposure from post-2013 station-level AQI/PM2.5 data or independent monitors and compare
  - Examine bunching of API just below pollution thresholds within the sample cities
- type: spatial_sorting_and_inversion_propensity
  basis: reported
  condition: Inversion-prone locations (valley-type and northern cities) may systematically sort travelers by preference or income; flight-code fixed effects absorb time-invariant sorting, but time-varying sorting correlated with inversion episodes would remain.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Test balance of ticket-price or booking-window proxies across inversion episodes
  - Interact inversion exposure with route-level traveler composition where observable
- type: unobserved_true_itinerary
  basis: reported
  condition: Only the flight's endpoint cities are observed; onward connections mean some travelers' true origins or destinations differ, biasing the API differential toward or away from zero. The paper's smaller-cities restriction (where connections are unlikely) yields a larger coefficient (about 0.6 percent), suggesting baseline estimates are conservative.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Restrict to endpoint-confident subsamples as the paper does
  - Combine with ticketing or itinerary data if a reuse project can obtain them
- type: study_period_boundaries_and_api_regime_change
  basis: inferred
  condition: The variation is bound to the API reporting regime and the 2008-2010 flight dataset; the 2013 transition to AQI with PM2.5 changed both the pollution measure and public information, and the record's internal discrepancy on the sample end date (20 versus 30 April 2010) is unresolved.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Re-verify the exact sample window against the raw flight data before reuse
  - Treat post-2013 replications as a new variation requiring fresh validation
- type: single_hub_scope
  basis: inferred
  condition: All routes pass through PEK, so estimates describe travelers to and from Beijing, a high-income, high-pollution-salience hub; transfer to other Chinese airport systems or to rail and road avoidance margins is untested.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Replicate on another hub's flight data or on high-speed-rail loads
empirical_requirements:
  contract_version: 1
  population: Domestic direct flights through Beijing Capital International Airport (PEK) and their passengers, 1 March 2008 to 30 April 2010; cities are the 60 origin/destination cities on the 115 routes
  observation_unit: flight-code-day (route-day and occupancy-rate versions in robustness)
  geography_level: city (origin and destination), with airport-to-city crosswalk for the 122 airport routes
  time_start: 2008
  time_end: 2010
  minimum_frequency: daily
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields:
  - passengers per flight by cabin class, airline, aircraft type, scheduled and actual departure/arrival times
  - origin and destination city per flight
  - daily city Air Pollution Index (CNEMC/MEP composite of PM10, SO2, NO2)
  - daily city thermal-inversion counts from MERRA-2 layer temperatures (110 m versus 320 m, 6-hourly)
  - 'daily city weather: temperature, precipitation, sunshine duration, wind speed, relative humidity, atmospheric pressure (IDW over stations within 100 km)'
  - origin-city population for weighting
  required_identifiers:
  - flight_code
  - origin_city_id
  - destination_city_id
  - date
  treatment_key:
  - origin_city_id
  - destination_city_id
  - date
  treatment_source: >
    Daily origin-minus-destination API difference from CNEMC/MEP city API,
    instrumented by the origin-minus-destination difference in daily
    thermal-inversion counts built from NASA MERRA-2 6-hourly layer
    temperatures (first layer about 110 m below second layer about 320 m),
    as constructed by the authors.
  measurement_risks:
  - the complete flight load-factor dataset's provider and access terms are not disclosed in the inspected text, so replicability of the outcome data is unverified
  - official API in 2008-2010 carries documented threshold-manipulation risk and no separate PM2.5
  - the paper's internal discrepancies (sample end 20 versus 30 April 2010; 1,743 versus 1,410 flight codes; second layer 320 m versus 330 m) are unresolved in the inspected text
  - inversion exposure is a gridded reanalysis construct matched to city grids, not a ground measurement
design_profiles:
- id: cabin-class-averting-design
  label: Cabin-class-split averting-demand design
  design_families:
  - instrumental variables
  when_to_use: Use when the research question concerns income- or willingness-to-pay-stratified avoidance behavior; first-class and economy passengers on the same flight share the API differential, so the split isolates valuation differences.
  outcome_domains:
  - cabin-class-specific passenger counts as stratified averting demand
  requirements:
    population: Flights through PEK with cabin-class passenger breakdowns (first-class analysis uses 494,023 observations)
    observation_unit: flight-code-day by cabin class
    geography_level: city (origin and destination)
    time_start: 2008
    time_end: 2010
    minimum_frequency: daily
    minimum_pre_periods: 0
    minimum_post_periods: 0
    required_fields:
    - passengers per flight separately for economy and first class
    - the same treatment, weather, and date fields as the base design
    required_identifiers:
    - flight_code
    - origin_city_id
    - destination_city_id
    - date
    treatment_key:
    - origin_city_id
    - destination_city_id
    - date
evidence:
- id: E1
  source_type: paper
  citation: 'Chen, Shuai, Yuyu Chen, Ziteng Lei, and Jie-Sheng Tan-Soo. 2020. "Impact of air pollution on short-term movements: evidence from air travels in China." Journal of Economic Geography 20(4): 939-968. Open author-archived full text hosted by the Environment for Development initiative.'
  url: https://www.efdinitiative.org/sites/default/files/publications/lbaa005.pdf
  date: 2020
  supports:
  - identity.instrument
  - identity.authority
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.local_timing
  - timeline.anticipation
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.exemptions
  - assignment.compliance
  - assignment.exposure_construction
  - assignment.required_identifiers
  - assignment.spillovers
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
  - empirical_requirements.geography_level
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_source
  - design_applications.paper
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
  locator: >
    Open EfD-hosted PDF fetched 2026-08-15 and read in full via two
    independent routes (web text extraction and local pdftotext of the
    downloaded file, 1,275 lines): Abstract; Section 1 (motivation and
    contributions); Section 2 (Equations 1-2, endogeneity discussion,
    exclusion-restriction argument, weather controls, flight-code fixed
    effects, Figure 1 inversion-API correlation); Section 3 (four datasets:
    499,180 PEK flights 2008-2010 on 115 city routes and 122 airport routes
    across 60 cities; CNEMC/MEP daily API for 120 cities; CMDC 820-station
    weather with 100 km IDW; MERRA-2 inversion construction at 6-hour
    intervals with 110 m versus 320 m layers and 540 m and binary
    robustness; Tables 1-2 descriptive statistics); Section 4.1 (Tables 3-4:
    first-stage KP F 40-80, baseline 0.36 percent, OLS comparison); Section
    4.2 (Figure 4 and Table 6 lead-lag analysis, day-of-travel sensitivity);
    Section 4.3 (Table 7 robustness: instrument codings, PM-dominant
    subsamples, weather functional forms, route-day aggregation, occupancy,
    delay/cancellation outcomes in Table A2, smaller-cities test in Table
    A3, international-flight falsification in Table A4); Section 4.4 (cabin
    class 0.34 versus 0.87 percent; departure-time, season, distance, and
    winter-heating heterogeneity; Figure 5 and Table A7 spline
    non-linearity); Section 5 (conclusion and back-of-the-envelope 92,671
    annual passengers). Establishes the design, data construction, results,
    and reported diagnostics as author claims; it does not independently
    verify the flight, API, weather, or MERRA-2 datasets, and the internal
    discrepancies noted in empirical_requirements.measurement_risks are
    unresolved in this text.
- id: E2
  source_type: paper
  citation: 'Chen, Shuai, Yuyu Chen, Ziteng Lei, and Jie-Sheng Tan-Soo. 2020. "Impact of air pollution on short-term movements: evidence from air travels in China." Journal of Economic Geography 20(4): 939-968. DOI: 10.1093/jeg/lbaa005 (bibliographic record and official abstract).'
  url: https://doi.org/10.1093/jeg/lbaa005
  date: 2020
  supports:
  - identity.legal_identifiers
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
  - assignment.intensity
  verification_status: verified
  access_level: metadata
  locator: >
    Crossref record for DOI 10.1093/jeg/lbaa005 queried 2026-08-15,
    establishing title, four authors, journal, volume 20, issue 4, pages
    939-968, and July 2020 issue date; the official abstract was
    additionally captured from search-result text of the OUP article page
    (direct OUP fetch returned 403 and the page itself was not read),
    reporting the 0.36 percent headline estimate, the roughly three-times
    faster first-class response, and day-of-travel sensitivity. Establishes
    publication identity and headline results; design details rest on E1.
- id: E3
  source_type: official-data
  citation: 'NASA Global Modeling and Assimilation Office (GMAO). MERRA-2 inst6_3d_ana_Np: 3d, 6-Hourly, Instantaneous, Pressure-Level, Analysis, Analyzed Meteorological Fields 0.625 x 0.5 degree, V5.12.4 (collection M2I6NPANA). NASA Earthdata Common Metadata Repository record.'
  url: https://cmr.earthdata.nasa.gov/search/collections.json?short_name=M2I6NPANA&version=5.12.4
  date: '2026-08-15'
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - timeline.local_timing
  - assignment.exposure_construction
  verification_status: verified
  access_level: official-document
  locator: >
    NASA Earthdata CMR collection record for M2I6NPANA V5.12.4 queried
    2026-08-15: states that M2I6NPANA (inst6_3d_ana_Np) is an
    instantaneous three-dimensional 6-hourly MERRA-2 collection of
    analyzed meteorological fields at 42 pressure levels including
    temperature, wind components, specific humidity, ozone, and
    geopotential height, on a 0.625 x 0.5 degree grid, available every six
    hours from 00:00 UTC, with temporal coverage beginning 1980-01-01.
    Establishes that the reanalysis collection the paper names exists with
    the stated provider, cadence, resolution, and variables covering the
    2008-2010 study window; it does not verify the paper's city-grid
    matching or the conversion of pressure levels to the 110 m and 320 m
    layer labels, which remain author constructions (E1).
design_applications:
- paper: 'Impact of air pollution on short-term movements: evidence from air travels in China'
  doi: 10.1093/jeg/lbaa005
  journal: Journal of Economic Geography
  year: 2020
  research_question: Do Chinese residents use short-term air travel as an avoidance strategy against day-to-day air-pollution fluctuations, and how does the response vary by cabin class, timing, season, and route characteristics?
  population: 499,180 domestic direct flights through Beijing Capital International Airport on 115 city routes across 60 cities, 1 March 2008 to 30 April 2010 (the data-section text says 20 April 2010)
  outcome: Log passengers per flight-code-day (overall and by cabin class), with occupancy rate, delay, and cancellation margins as robustness outcomes
  data_used:
  - Complete flight load-factor dataset for PEK (passengers by cabin class, airline, aircraft, schedule and actual times); provider not disclosed in the inspected text
  - CNEMC/MEP daily city Air Pollution Index for 120 cities
  - CMDC daily station weather (820 stations, 100 km inverse-distance weighting)
  - NASA MERRA-2 6-hourly layer temperatures for the inversion construction
  treatment_encoding: Daily origin-minus-destination API difference instrumented by the origin-minus-destination difference in thermal-inversion counts; flight-code and date fixed effects; second-order differenced weather polynomials; origin-population weights; flight-code clustering
  comparison: Within flight code across days net of date effects; cabin-class splits on the same flight; lead-lag timing comparisons; spline non-linearity; route-day aggregation
  empirical_design: Two-stage least squares with thermal-inversion counts as the instrument for the air-quality differential, defended by first-stage strength (KP F 40-80), weather controls, fixed effects, and falsification on international flights and delay/cancellation margins
  assumptions:
  - Inversions shift flight demand only through air quality, conditional on weather, date, and flight-code effects
  - The official API measures true pollution up to error uncorrelated with the instrument
  - Sorting along inversion propensity is time-invariant and absorbed by flight-code fixed effects
  threats_addressed:
  - Location attractiveness confounding and reverse causality via the IV
  - Weather-channel violations of the exclusion restriction via polynomial controls and functional-form robustness
  - Supply-side confounding via delay and cancellation outcome checks
  - Unobserved true itineraries via the smaller-cities restriction
  - Within-route substitution via route-day aggregation
  - Non-linear responses via spline specifications
  evidence_refs:
  - E1
  - E2
  - E3
method_transfer: null
readiness_blockers:
- The complete flight load-factor dataset's provider and access terms are not disclosed in the inspected text, so outcome-data replicability is unverified; the companion data repository is the right place for any acquisition path.
- 'Internal inconsistencies in the paper remain unresolved: sample end 20 versus 30 April 2010, 1,743 versus 1,410 flight codes, and second inversion layer 320 m versus 330 m.'
- The variation is bound to the pre-2013 API reporting regime; post-2013 reuse requires rebuilding exposure from AQI/PM2.5 station data and re-validating the first stage.
- The official API's documented threshold manipulation in this period is acknowledged but not corrected; only inversion-correlated manipulation is addressed by the IV.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

China's major cities in the late 2000s experienced severe day-to-day
air-quality fluctuations: even in Beijing, whose 2008-2015 average PM2.5
far exceeded WHO guidelines, more than 220 days in 2015 met safe levels, so
short trips could substitute for permanent relocation as an avoidance
margin, and hukou-related barriers made permanent migration costly [E1].
Daily air quality was reported through the Ministry of Environmental
Protection's Air Pollution Index (API), a composite of PM10, SO2, and NO2
published for 120 major cities, and air-quality forecasts had been publicly
available since at least 2001 [E1]. Thermal inversions - episodes in which
temperature rises with altitude and traps pollutants near the ground - had
recently been proposed as an instrument for air pollution by
Arceo et al. (2016), and this paper was part of the first wave applying
that construction to Chinese cities [E1].

## What Changed

No policy changed: the variation is the day-to-day realization of thermal
inversions across Chinese cities, which shifts near-ground pollution and
hence the air-quality differential between any origin-destination pair
[E1]. The canonical boundary of this record is that meteorological
variation as constructed and used by Chen, Chen, Lei, and Tan-Soo (2020):
daily MERRA-2 inversion counts and CNEMC/MEP API matched to the complete
domestic flight panel through Beijing Capital International Airport over
2008-2010 [E1, E2]. Related but distinct objects - the same authors'
mobile-phone-based short-term mobility work ("Chasing Clean Air", JAERE
2021), permanent-migration responses to medium-run inversion-driven
pollution (Chen, Oliva, and Zhang on county migration), and Chinese
pollution-control policies - are outside this boundary and must not be
merged into it [E1; analytical inference on the boundary].

## Implementation and Assignment

Each flight-code-day inherits the API differential between its origin and
destination cities; the origin-minus-destination difference in daily
inversion counts (0-4 per city-day, from 6-hourly comparisons of the
roughly 110 m and 320 m MERRA-2 layers) instruments that differential with
a first-stage Kleibergen-Paap F of roughly 40-80 [E1]. The estimating
design compares the same flight code across days under flight-code and
date fixed effects, with differenced weather polynomials, origin-population
weights, and flight-code clustering [E1]. A one-unit widening of the
origin-over-destination API differential is reported to raise passengers by
about 0.36 percent, with first-class loads responding about three times
faster than economy (0.87 versus 0.34 percent) [E1, E2].

## Why This Creates Empirical Variation

Climatic heterogeneity across the 60 connected cities generates daily
variation in inversion occurrence that is plausibly unrelated to
route-specific demand shocks once weather, calendar, and route effects are
removed, and the flight load-factor panel turns that into within-route
daily identifying variation at a frequency unusual for Chinese pollution
variation [E1]. The cabin-class split is the distinctive affordance:
passengers on the same flight share the API differential, so differential
first-class responses trace willingness-to-pay for avoidance rather than
exposure differences [E1]. Lead-and-lag specifications showing
day-of-travel sensitivity support a forecast-based planning channel rather
than same-day reactions [E1].

## Identification Risks

Identification rests on the exclusion restriction as stated and defended,
not on any claim that inversions are intrinsically exogenous [E1]. The main
risks are weather channels that correlate with inversions and shift travel
directly (addressed by polynomial controls, with visible sensitivity),
documented manipulation of the 2008-2010 official API series, time-varying
sorting along inversion propensity, unobserved onward itineraries (the
smaller-cities restriction suggests baseline estimates are conservative),
and the single-hub scope of PEK [E1; the last is analytical inference].
The design also says nothing about permanent migration or about
post-2013 air-quality regimes [E1].

## Data Requirements

Reuse requires the complete PEK flight load-factor panel (whose provider
and access terms are not disclosed in the inspected text), CNEMC/MEP daily
city API, CMDC station weather, and NASA MERRA-2 reanalysis for the
inversion construction, joined by flight code, origin and destination
city, and date [E1]. Dataset acquisition paths belong in the companion
data repository; this record stores only the treatment contract.

## Evidence Notes

E1 is the open EfD-hosted author-archived full text of the JoEG article,
read in full on 2026-08-15 through two independent extraction routes; it
establishes the design, data construction, results, and reported
diagnostics as author claims, but does not independently verify the
underlying flight, API, weather, or MERRA-2 datasets, and it leaves the
internal discrepancies listed in empirical_requirements.measurement_risks
unresolved. E2 is the Crossref bibliographic record (read directly) plus
the official OUP abstract captured indirectly because the OUP page
returned 403; it establishes publication identity and headline results.
E3 is the NASA Earthdata CMR official collection record for the MERRA-2
M2I6NPANA reanalysis collection, queried directly; it establishes the
instrument's data producer, 6-hourly cadence, 0.625-by-0.5-degree grid,
42 pressure levels including temperature, and coverage of the 2008-2010
window, but not the paper's layer-to-height labels or city matching.
No evidence in this record was built from search snippets alone, and
nothing here certifies the instrument as exogenous beyond the paper's
stated assumptions.
