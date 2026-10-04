---
schema_version: 2
id: china-big-city-proximity-urban-growth-shadow
name: China Big-City Proximity and Urban Growth Shadows
aliases:
- Structural transformation and the urban growth shadows
- China county distance-to-big-city exposure
- 中国大城市邻近与城市增长阴影
status: grounded
provenance:
  task_id: task-e6f648e1ff1b
scope:
  country: China
  regions:
  - Chinese county-level administrative units and prefectural-city cores with consistent 1990 boundaries
  domains:
  - regional-economics
  - urban-economics
  - economic-geography
  - migration
  - population
  - structural-transformation
  - agriculture
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    Tang, Gao, and You (2025) construct a China-specific spatial exposure from each
    county's distance to the nearest large city. The exposure is recomputed by decade
    using the largest prefectural city cores at the beginning of the period, and is
    studied with county population, agriculture, transport, and migration data from
    1990 to 2020. This is a paper-defined regional exposure, not a government pilot,
    eligibility rule, or randomly assigned shock.
identity:
  instrument: >
    Decade-specific proximity to the nearest big city for Chinese county-level units.
    The source application defines big cities as the 40 largest prefectural city
    cores at the beginning of each decade (1990, 2000, and 2010), with the 20-city
    definition used as a robustness check; it then assigns the remaining county-level
    units to distance rings around the nearest selected city. The principal reported
    contrast is the 150–250 km ring against counties at least 250 km away. The object
    is the spatial exposure and its observed association with subsequent population
    growth, not a legal treatment.
  authority: >
    No public authority assigns this exposure. National and local statistical agencies
    define and publish the population, county, census, and yearbook data used to build
    the research sample; the ring assignment and decade-specific city set are the
    authors' reproducible measurement convention. Big-city selection may reflect
    existing urban hierarchy and therefore must be treated as selected geography.
  legal_identifiers:
  - Official county-level administrative-unit and population-census series used to harmonize the observational frame
  - Paper-defined top-40 (top-20 robustness) prefectural-city-core selection at the beginning of 1990, 2000, and 2010
  implementation_regime: >
    The authors harmonize county, county-level-city, district, and prefectural-city
    core observations to consistent 1990 boundaries, select the largest city cores at
    each decade's start, calculate the nearest-city distance, and compare the resulting
    rings over the 1990–2000, 2000–2010, and 2010–2020 intervals. The city set is
    therefore allowed to change at decade boundaries; a single national treatment date
    would misrepresent the design.
  assignment_mechanism: >
    For each decade, exclude the selected big-city cores from the regression sample.
    For every remaining county-level unit, identify the nearest selected big city and
    place the unit in distance bins (1–50, 50–100, 100–150, 150–200, 200–250, and
    250+ km). The distance variables are constructed from the paper's county/city
    geography and are not an administrative eligibility rule. Initial agricultural
    employment share and transport access are covariates or mechanism measures, not
    alternative assignments.
  parent: null
  related_variations:
  - china-expressway-market-access-walled-city-mst
  - china-highway-network-expansion
  - china-high-speed-rail-recentered-market-access
timeline:
  announcement: null
  effective: null
  implementation_start: 1990
  implementation_end: 2020
  local_timing: >
    The three outcome windows are 1990–2000, 2000–2010, and 2010–2020. City ranking
    and distance exposure are refreshed at the beginning of each decade. These dates
    describe the measurement windows, not policy adoption or an onset of treatment.
  anticipation: >
    Not applicable as a legal anticipation clock. Population, migration, transport,
    and city growth can affect one another before each measurement window, so a user
    must not interpret the ring comparison as a clean before/after experiment.
  last_verified: '2026-08-13'
assignment:
  unit: >
    County-level administrative units, county-level cities, districts, and prefectural
    city cores harmonized to consistent 1990 boundaries; the primary outcome is a
    decade-by-unit population growth rate. Migration mechanisms use county-to-county
    flows from the 2000, 2010, and 2015 population micro-censuses where available.
  treated: >
    The main descriptive exposure is membership in the 150–250 km ring around the
    nearest decade-specific big city. Other rings are retained as separate categories;
    the selected big-city cores are excluded from the regression sample. “Treated” is
    shorthand for this analysis category and does not mean a county received a policy.
  comparison_pool: >
    Counties at least 250 km from the nearest selected big city form the baseline in
    the source regressions. The 1–50, 50–100, 100–150, 150–200, and 200–250 km rings
    are additional comparisons. Distance groups differ in agriculture, transport,
    history, and market access, so the 250+ group is not automatically a causal
    counterfactual.
  rule: >
    At each decade start, rank prefectural city cores by population, retain the top 40
    (top 20 in robustness checks), compute each county-level unit's distance to its
    nearest selected core using the harmonized geography, and assign the corresponding
    ring. Preserve the city-set version, distance measure, county boundary version,
    and exclusion of selected cores in the data ledger.
  intensity: >
    Distance to the nearest selected big city is continuous; the paper's main tables
    use distance-band indicators. Initial agricultural employment share, highway and
    railway access, and bilateral migration flows describe mechanisms and
    heterogeneity. They should not be collapsed into a single treatment score.
  exemptions:
  - Selected top-20 or top-40 big-city cores excluded from the county regression sample
  - Units without a defensible historical boundary, centroid, population observation, or decade join
  - Observations affected by county mergers or reclassifications that cannot be harmonized to the consistent-boundary panel
  - Migration-flow analyses in years without county-level hukou and residence identifiers
  compliance: >
    Not applicable. The exposure is calculated from geography and published data; there
    is no take-up, legal compliance, or implementation intensity to observe.
  exposure_construction: >
    Rebuild the consistent-boundary county panel from the Administrative Division
    Manual and official census/yearbook series; store the decade-specific big-city list,
    city-core coordinates or polygons, county geometry/centroid, nearest-city ID,
    distance, ring, and exclusion flag. Merge population growth, agricultural share,
    transport access, resource-based status, and census migration flows by stable
    historical identifiers. Keep the paper's 40-city construction separate from the
    20-city robustness version and from any modern GIS geography.
  required_identifiers:
  - Historical county or district identifier and stable 1990-boundary crosswalk
  - Prefectural city-core identifier and decade-specific top-20/top-40 rank
  - Decade or census interval
  - County centroid or polygon version and nearest-big-city ID
  - Distance in kilometers and distance-ring code
  - County population, agricultural employment share, and transport-access fields
  - Origin and destination county identifiers for migration-flow applications
  spillovers: >
    Migration, commuting, market access, and firm relocation connect nearby counties
    and selected cores. A county's outcome can respond to changes in other rings, and
    spatial correlation and shared prefecture shocks can make ring standard errors and
    local interpretations fragile. These are part of the regional-equilibrium problem,
    not evidence of clean isolation.
research_compatibility:
  outcome_domains:
  - Decadal population growth and population composition
  - Rural-to-urban migration and county-to-county migration flows
  - Agricultural employment and structural transformation
  - GDP per capita and county growth
  - Transport access, market access, and regional inequality
  - Age, education, and fiscal-population composition
  affected_populations:
  - Residents of Chinese counties and county-level cities
  - Agricultural workers and potential rural-to-urban migrants
  - Prime-age and college-educated residents in peripheral counties
  - Firms and workers linked to county labor markets
  mechanism_channels:
  - Migration toward nearby urban cores
  - Agricultural labor release and structural transformation
  - Transport and commuting access
  - Market access and core-periphery spillovers
  - Fiscal and human-capital reallocation
  best_for:
  - Descriptive or reduced-form comparisons of county growth across distance rings
  - Mechanism work on agriculture, migration, and transport during structural transformation
  - Regional-equilibrium analyses that retain spatial spillovers and selected-city exclusion
  - Reproducible construction of historical county-to-city distance exposure
  not_good_for:
  - A uniform China-wide post-1990, post-2000, or post-2010 policy indicator
  - Calling distance to a big city exogenous or interpreting a ring coefficient as a policy effect
  - Treating 250+ km counties as untreated without addressing spatial selection and spillovers
  - Combining the ring exposure with expressway or HSR treatment without separate network fields
  - Designs that cannot recover historical county boundaries, city lists, or county identifiers
design:
  claim_type: reduced-form
  affordances:
  - Decade-specific distance bands with an explicit 250+ km baseline
  - Consistent-boundary county panel spanning the 1990, 2000, 2010, and 2020 censuses
  - Heterogeneity by initial agricultural employment and transport access
  - County-to-county migration-flow mechanism analysis
  - Alternative top-20 and top-40 city-set definitions
  candidate_designs:
  - Decade-by-ring reduced-form population-growth comparison
  - Repeated cross-section or county-panel models with decade and region controls
  - Interaction of distance rings with initial agricultural employment share
  - Migration gravity models using origin agriculture and proximity to a big city
  - Sensitivity analysis using alternative big-city lists, rings, and spatial inference
  identifying_variation: >
    The source application compares decade-specific population growth across counties
    assigned to different distance rings from the nearest selected big city, conditional
    on the paper's controls and measurement choices. The reported 150–250 km difference
    is a spatial correlation pattern that the authors interpret through structural
    transformation and migration mechanisms; the source explicitly notes that the key
    agriculture and transport variables are endogenous and uses instruments for those
    mechanisms. The ring itself should not be presented as a causal treatment.
  primary_strategy: >
    Tang, Gao, and You estimate decade-specific regressions of county population
    growth on distance-band indicators, with 250+ km omitted, controls for initial
    population, centroid geography, resource-based status, and regions, and standard
    errors clustered at the prefecture level. The full working paper also reports
    transport-access and agricultural-share mechanisms, bilateral migration-flow
    regressions, and IV exercises for those endogenous covariates. Reproduction must
    recover the final article's exact controls, sample, distance calculation, and IV
    specification before treating any estimate as more than source-reported evidence.
  estimand: >
    A source-reported difference in decadal population growth between counties in a
    specified distance ring and counties at least 250 km from the nearest selected big
    city, under the selected decade, city list, boundary harmonization, controls, and
    spatial inference. It is not automatically the causal effect of proximity or of a
    city on a county.
  treatment_variable: >
    A vector of decade-specific distance-band indicators (or continuous nearest-city
    distance), accompanied by top-city-set version, nearest-city ID, distance, county
    boundary version, and exclusion flag. Keep agriculture, transport, and migration
    variables as separate covariates or mechanisms.
  comparison_logic: >
    The paper's baseline omits the 250+ km band, then compares each nearer ring with
    that group within the relevant decade. A defensible application should report the
    full ring profile, alternative 20-city and 40-city lists, spatially robust or
    prefecture-clustered inference, and sensitivity to region, initial population,
    county composition, and spatial overlap. No ring is an untreated status by itself.
  estimation_notes: >
    Preserve the paper's three decadal windows and do not create annual treatment
    timing from the ring labels. Distinguish the population-growth outcome from GDP
    outcomes, migration mechanisms, and IV exercises. The accessible final metadata
    and verified working paper establish the construction and headline results, but
    the final article's complete sample filters, city lists, code, and replication data
    have not been independently audited here.
  assumptions:
  - Historical county boundaries, centroids, city-core populations, and decade lists are measured consistently
  - The chosen rings and city-set definition capture the intended spatial exposure rather than a hidden policy
  - Initial agriculture, transport, resource status, and geography are measured before the relevant growth interval
  - Spatial spillovers, migration, and prefecture shocks are modeled or explicitly included in the estimand
  - Any IV for agricultural share or transport access satisfies its own first-stage and exclusion assumptions
  - Reported associations are not relabeled as causal effects merely because controls or IVs are present
  diagnostics:
  - Reconstruct the top-20 and top-40 city lists for 1990, 2000, and 2010
  - Audit county-boundary harmonization against the official administrative series
  - Plot the full distance-ring profile for each decade and test alternative ring widths
  - Check pre-period population, agriculture, transport, and geography balance across rings
  - Use prefecture-clustered and spatially robust inference with sensitivity to border counties
  - Reproduce the agriculture and transport first stages and report weak-IV diagnostics
  - Test alternative nearest-city, centroid, polygon, and city-core definitions
  - Examine county-to-county migration and neighboring-ring spillovers
design_profiles:
- id: distance-ring-growth
  label: Decadal county growth by distance to selected big cities
  design_families:
  - spatial-exposure-comparison
  - repeated-cross-section
  - county-panel
  when_to_use: >
    Use when a researcher can reproduce the decade-specific city list, historical
    county crosswalk, nearest-city distance, and 250+ km baseline. Interpret the
    coefficient as a reduced-form spatial comparison and retain the selected-city and
    spatial-equilibrium caveats.
  outcome_domains:
  - population growth
  - GDP per capita
  - education and age composition
  requirements:
    population: County-level administrative units in China with consistent 1990 boundaries
    observation_unit: County-decade
    geography_level: County and prefectural-city core
    time_start: 1990
    time_end: 2020
    minimum_frequency: decadal
    minimum_pre_periods: 0
    minimum_post_periods: 0
    required_fields:
    - County identifier and historical boundary version
    - Decade and population outcome
    - Top-city-set version, nearest-city ID, distance, and ring
    - Initial population, centroid geography, region, and resource-based status
    required_identifiers:
    - county_id_1990_boundary
    - decade
    - nearest_big_city_id
    - distance_km
    - distance_ring
    treatment_key:
    - nearest_big_city_id
    - distance_km
    - distance_ring
- id: migration-structural-transformation
  label: Big-city proximity, agricultural labor, and county migration
  design_families:
  - migration-gravity
  - mechanism-heterogeneity
  - reduced-form
  when_to_use: >
    Use when the application has county-to-county migration flows and pre-period
    agricultural employment. The migration model explains a mechanism behind the
    spatial pattern; it does not turn the ring exposure into a randomized treatment.
  outcome_domains:
  - county-to-county migration
  - agricultural employment
  - rural-to-urban labor reallocation
  requirements:
    population: Chinese county residents and migrants observed in the 2000, 2010, or 2015 population micro-censuses
    observation_unit: Origin-destination-county by census year
    geography_level: County and nearest selected big city
    time_start: 2000
    time_end: 2015
    minimum_frequency: census/micro-census
    minimum_pre_periods: 0
    minimum_post_periods: 0
    required_fields:
    - Origin hukou county and current-residence county
    - Census or micro-census year
    - Origin agricultural employment share
    - Nearest big city, distance, ring, and county boundary version
    required_identifiers:
    - origin_county_id
    - destination_county_id
    - census_year
    - nearest_big_city_id
    treatment_key:
    - origin_county_id
    - nearest_big_city_id
    - distance_ring
threats:
- type: selected-city-and-spatial-endogeneity
  basis: documented
  condition: >
    Big cities are selected by population rank and are embedded in the historical urban
    hierarchy; distance rings therefore differ systematically in geography, development,
    transport, and market access. The ring assignment is not random.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Baseline balance and pre-period growth by ring
  - Alternative top-20/top-40 lists and city-core definitions
  - Region, centroid, resource, and initial-population controls
- type: boundary-and-distance-measurement
  basis: documented
  condition: >
    County mergers, district reclassification, changing city cores, and centroid or
    polygon choices can change the nearest-city distance and the ring assignment.
  evidence_refs:
  - E2
  - E3
  - E4
  possible_diagnostics:
  - Rebuild the 1990-boundary panel from the Administrative Division Manual
  - Compare centroid, boundary-to-boundary, and city-core measures
  - Audit every city-list and county crosswalk version
- type: agriculture-and-transport-confounding
  basis: documented
  condition: >
    Initial agricultural employment and transport access vary with distance and predict
    subsequent growth. The authors report that agricultural share explains much of the
    150–250 km pattern, while transport access has a different relationship; neither
    should be treated as a harmless control without its own measurement and mechanism.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Pre-period agricultural-share and transport balance
  - Interaction and mechanism specifications
  - Reproduce the paper's agricultural-suitability/climate and historical-route IVs
  - Report first-stage and exclusion sensitivity rather than treating IV use as proof
- type: spatial-spillovers-and-general-equilibrium
  basis: inferred
  condition: >
    Migration, commuting, firm location, and market access connect counties across rings;
    growth in a big-city core or one peripheral ring can change outcomes elsewhere.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Neighbor and ring-exposure controls
  - County-to-county migration and commuting outcomes
  - Spatially robust inference and prefecture-cluster sensitivity
- type: time-window-and-data-coverage
  basis: documented
  condition: >
    The 1990, 2000, 2010, and 2020 population censuses do not provide identical
    migration detail, and GDP coverage begins later than the population series. The
    2020 micro-census and final article replication materials are not fully public in
    the inspected sources.
  evidence_refs:
  - E2
  - E4
  - E5
  possible_diagnostics:
  - Keep outcome-specific samples and census years explicit
  - Audit missingness and boundary changes by decade
  - Obtain and inspect the final article appendix or replication package
empirical_requirements:
  contract_version: 1
  population: Chinese county-level units and prefectural-city cores observed across the 1990–2020 census intervals
  observation_unit: County-decade, with origin-destination-county extensions for migration mechanisms
  geography_level: County and prefectural-city core
  time_start: 1990
  time_end: 2020
  minimum_frequency: decadal
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields:
  - Outcome and census or yearbook reference year
  - Consistent 1990-boundary county identifier and crosswalk
  - Decade-specific top-city list and nearest-city identifier
  - County geometry or centroid, distance, and distance ring
  - Initial agricultural employment share and transport-access measures
  - Region, longitude, latitude, resource-based status, and prefecture cluster
  - Hukou and residence county identifiers for migration-flow applications
  required_identifiers:
  - county_id_1990_boundary
  - prefecture_id
  - decade
  - nearest_big_city_id
  - distance_ring
  - census_or_yearbook_source
  treatment_key:
  - decade
  - top_city_set_version
  - nearest_big_city_id
  - distance_km
  - distance_ring
  treatment_source: >
    Tang, Gao, and You's verified working-paper construction, final RSUE metadata,
    National Bureau of Statistics population censuses and county-level yearbooks, and
    a versioned historical administrative-boundary crosswalk. Actual census/yearbook
    acquisition, restricted microdata, GIS reconstruction, and join assets belong in
    Econ Data Know-How rather than this variation record.
  measurement_risks:
  - Changing county and district boundaries and name/code crosswalks
  - Top-city rankings and city-core definitions that change at decade boundaries
  - Centroid, polygon, geodesic, and nearest-city calculation choices
  - Census and yearbook coverage, revisions, and missing county observations
  - Endogenous agriculture and transport measures and IV exclusion assumptions
   - Spatial correlation, migration, and general-equilibrium reallocation
evidence:
- id: E1
  source_type: paper
  citation: 'Tang, Enning, Ming Gao, and Wei You. 2025. "Structural transformation and the urban growth shadows: County-level evidence from China, 1990–2020." Regional Science and Urban Economics 115:104141. DOI: 10.1016/j.regsciurbeco.2025.104141.'
  url: https://doi.org/10.1016/j.regsciurbeco.2025.104141
  date: 2025
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.local_timing
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
  - design_applications.outcome
  verification_status: verified
  access_level: abstract
  locator: >
    IDEAS/RePEc metadata for the DOI identifies the final RSUE article, authors,
    China county sample from 1990–2020, the 150–250 km versus 250+ km contrast, the
    2.9–3.6 percentage-point headline difference, and the agriculture/migration
    mechanism. The publisher full text is subscriber-restricted; the metadata does
    not establish the final article's full sample or code.
- id: E2
  source_type: paper
  citation: 'Gao, Ming, Enning Tang, and Wei You. 2023. "Urban Growth Shadows Revisited: County-Level Evidence from China, 1990–2020." Authors working paper, August 17, 2023.'
  url: https://www.efnchina.com/__local/E/55/9B/4DA8BBC7A87EE8C8B485A1643BF_29AD5590_217DF2.pdf?e=.pdf
  date: '2023-08-17'
  supports:
  - identity.instrument
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
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
  - threats.condition
  - threats.possible_diagnostics
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_source
  - empirical_requirements.measurement_risks
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
    Pages 1–9 define the consistent-boundary sample, top-40 city-core selection,
    top-20 robustness, nearest-city distance rings, 250+ km baseline, census and
    county-yearbook sources, transport and agriculture measures, and migration flows.
    Pages 3–4 state that agriculture and transport are endogenous and describe the
    instrument exercises; the working paper is an earlier version of the 2025 article.
- id: E3
  source_type: official-data
  citation: 'National Bureau of Statistics of China. 2021. China County Statistical Yearbook (Township Volume and County/City Volume) catalogue and description.'
  url: https://www.stats.gov.cn/zs/tjwh/tjkw/tjzl/202302/t20230215_1908004.html
  date: 2021
  supports:
  - identity.instrument
  - assignment.unit
  - assignment.exposure_construction
  - empirical_requirements.population
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: official-document
  locator: >
    The National Bureau of Statistics description states that the county/city volume
    covers the basic, economic, and agricultural characteristics of more than 2,000
    county-level units for 2020. It establishes the official county-level data frame
    and producer; it does not establish the paper's nearest-city ring assignment or
    any causal interpretation.
- id: E4
  source_type: official-data
  citation: 'National Bureau of Statistics of China. 1990. Communiqué of the Fourth National Population Census, No. 1.'
  url: https://www.stats.gov.cn/sj/tjgb/rkpcgb/qgrkpcgb/202302/t20230206_1901990.html
  date: 1990
  supports:
  - timeline.implementation_start
  - assignment.unit
  - assignment.exposure_construction
  - empirical_requirements.time_start
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: official-document
  locator: >
    The official census communiqué records the 1990 census reference date and the
    national population-enumeration framework. It anchors the first population window;
    it does not publish the paper's harmonized county panel or distance rings.
- id: E5
  source_type: official-data
  citation: 'National Bureau of Statistics of China. 2021. Communiqué of the Seventh National Population Census, No. 2.'
  url: https://www.stats.gov.cn/sj/tjgb/rkpcgb/qgrkpcgb/202302/t20230206_1902002.html
  date: 2021
  supports:
  - timeline.implementation_end
  - assignment.unit
  - assignment.exposure_construction
  - empirical_requirements.time_end
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: official-document
  locator: >
    The official communiqué states the 2020 population-census reference time and
    national enumeration. It anchors the final population window; it does not establish
    the paper's sample filters, county crosswalk, or distance assignment.
- id: E6
  source_type: archive
  citation: 'National Bureau of Statistics of China. Historical statistical yearbook table: county-level administrative divisions and above.'
  url: https://www.stats.gov.cn/zt_18555/ztsj/hstjnj/sh2009/202303/t20230303_1926624.html
  date: 2009
  supports:
  - identity.legal_identifiers
  - assignment.exposure_construction
  - empirical_requirements.required_identifiers
  verification_status: verified
  access_level: official-document
  locator: >
    The official historical table lists county-level administrative-unit counts by
    year, which is an audit anchor for the changing unit frame. It does not supply
    county polygons, the authors' centroid calculation, or the top-city ranking.
readiness_blockers:
- The final ScienceDirect article is subscriber-restricted; the verified full-text source is the authors' August 2023 working-paper version, so final-paper changes to sample filters, city lists, controls, and appendices remain to be audited.
- The paper's consistent-boundary panel and distance calculations are described but the GIS files, exact city-list tables, code, and county crosswalk have not been independently reconstructed here.
- The reported instruments for agricultural share and transport access are design components with first-stage and exclusion assumptions; they do not make the spatial ring assignment exogenous.
- The census, yearbook, GIS, and migration microdata are acquisition and join work for Econ Data Know-How; this record specifies the data contract and limits but does not duplicate those assets.
- Paper-only institutional grounding: no decree or official program assigns counties to these rings; E3–E6 establish the official observational frame, while E1–E2 establish the paper-defined spatial measurement.
design_applications:
- paper: 'Structural transformation and the urban growth shadows: County-level evidence from China, 1990–2020'
  doi: 10.1016/j.regsciurbeco.2025.104141
  journal: Regional Science and Urban Economics
  year: 2025
  research_question: How does proximity to a large city relate to county population growth during China's structural transformation?
  population: 2,234 Chinese county-level observations harmonized to consistent 1990 boundaries, excluding selected big-city cores; decade samples cover 1990–2020.
  outcome: Decadal resident-population growth, with GDP per capita and population-composition outcomes; county-to-county migration flows for mechanism analysis.
  data_used:
  - China Population Census data for 1990, 2000, 2010, and 2020
  - China Population Mini Census microdata for 2000, 2010, and 2015 migration flows
  - China County-Level Statistical Yearbooks for GDP data in 2001, 2011, and 2021
  - Highway and railway GIS data digitized from 1990, 1999, and 2010 network maps
  - Official resource-based-city definition and harmonized county administrative boundaries
  treatment_encoding: >
    Distance-band indicators for the nearest top-40 prefectural city core at the start
    of each decade, with top-20 city lists as robustness; 250+ km is omitted in the
    baseline. Initial agriculture and transport access enter as covariates or mechanisms.
  comparison: >
    Counties in the 1–50, 50–100, 100–150, 150–200, and 200–250 km rings compared with
    counties at least 250 km from the nearest selected big city, separately by decade.
  empirical_design: >
    Decade-specific reduced-form regressions with initial population, centroid
    longitude/latitude, resource-based status, region controls, and prefecture-clustered
    standard errors; heterogeneity and mechanism regressions use agricultural employment,
    transport access, and bilateral migration flows. The source reports a 2.9–3.6
    percentage-point lower decadal population-growth rate in the 150–250 km range than
    in the 250+ km group, with increasingly favorable near-core associations over time.
  assumptions:
  - The selected city list, historical boundary harmonization, distance construction, and census joins are reproduced correctly
  - Ring coefficients are interpreted as conditional spatial associations or reduced-form contrasts, not as a universal causal proximity effect
  - Mechanism and IV claims are evaluated with their own first-stage, exclusion, and spatial diagnostics
  threats_addressed:
  - Selected-city and geographic confounding
  - Initial agriculture and transport mechanisms
  - County boundary harmonization and data coverage
  - Spatial spillovers and migration reallocation
  - Alternative top-20/top-40 city definitions and distance bands
  evidence_refs:
  - E1
  - E2
  - E3
  - E4
  - E5
readiness_blockers:
- The final ScienceDirect article is subscriber-restricted; the verified full-text source is the authors' August 2023 working-paper version, so final-paper changes to sample filters, city lists, controls, and appendices remain to be audited.
- The paper's consistent-boundary panel and distance calculations are described but the GIS files, exact city-list tables, code, and county crosswalk have not been independently reconstructed here.
- The reported instruments for agricultural share and transport access are design components with first-stage and exclusion assumptions; they do not make the spatial ring assignment exogenous.
- The census, yearbook, GIS, and migration microdata are acquisition and join work for Econ Data Know-How; this record specifies the data contract and limits but does not duplicate those assets.
method_transfer: null
superseded_by: null
deprecation_reason: null
---

## Institutional Background

This case has no decree that assigns counties to treatment. The relevant object is a measurement convention built from China’s changing urban hierarchy. Tang, Gao, and You (2025) study 1990–2020 county data, harmonize the administrative units to consistent 1990 boundaries, select the largest prefectural city cores at the beginning of each decade, and calculate each remaining unit’s distance to its nearest selected city. The official census and county-yearbook sources establish the population and county-level observation frame; the paper supplies the distance-ring construction. [E1; E2; E3; E4; E5]

## What Changed

Nothing legally changed for a county when its distance ring was recorded. What changes across the three observation windows is the paper’s decade-specific spatial exposure: the nearest-city list is refreshed in 1990, 2000, and 2010, and population growth is measured over 1990–2000, 2000–2010, and 2010–2020. The main source comparison puts counties 150–250 km from the nearest selected big city against counties at least 250 km away. The paper reports a 2.9–3.6 percentage-point lower decadal population-growth rate in the former band, while the very-near band becomes more favorable over time. Those are source-reported spatial contrasts, not a claim that a city caused a county’s outcome. [E1; E2]

## Implementation and Assignment

The paper’s top-40 city set is chosen from prefectural city cores at each decade’s beginning; a top-20 set is a robustness definition. Selected cores are excluded from the county regression sample. The remaining county, county-level-city, and district observations are assigned to the nearest selected core and to distance bands from 1–50 km through 250+ km. The working paper reports a 2,234-unit consistent-boundary panel, official population censuses for 1990, 2000, 2010, and 2020, county yearbooks for later GDP outcomes, and county migration flows from the 2000, 2010, and 2015 mini-censuses. [E2; E3; E4; E5]

The construction is useful because it makes the spatial comparison reproducible. It is not useful as a shortcut to exogeneity. City size, historical urban hierarchy, transport, agriculture, and regional location jointly shape both distance and growth. Agriculture and transport are themselves endogenous in the paper’s mechanism analysis; the reported IVs must be checked as separate designs with separate first stages and exclusion restrictions. [E2]

## Why This Creates Empirical Variation

For a county-growth question, the record supplies a versioned way to ask how outcomes differ by distance to a selected urban core during structural transformation. It supports a full ring profile, not just a treated-versus-control dummy: very close counties, intermediate rings, and the 250+ baseline can move differently across decades. The agricultural-employment interaction and county-to-county migration data make it possible to study whether proximity changes the opportunity cost of leaving agriculture and the direction of labor reallocation. [E1; E2]

The correct interpretation is conditional and query-specific. A researcher may use the ring indicators as a reduced-form spatial exposure, a mechanism design, or an input to a regional-equilibrium model. A researcher cannot label 150–250 km counties “treated by big cities,” treat 250+ km counties as untouched, or merge the ring variable with a highway or HSR rollout without adding those separate exposures and their own timing and joins.

## Identification Risks

The main risk is selected geography. The largest cities are not randomly located, and the 150–250 km band differs from the 250+ band in agriculture, transport, initial development, and historical urban structure. Boundary harmonization and distance measurement are equally consequential: a changed county code, a new district boundary, or a different city-core centroid can move an observation between rings. Migration, commuting, and firm relocation create spillovers across the rings, so a local coefficient may describe regional reallocation rather than an isolated county response. [E2; E3; E4]

The paper reports agricultural-suitability/climate instruments for initial agricultural employment and historical-route instruments for transport access. Those constructions can help examine mechanisms, but they introduce their own first-stage and exclusion questions. The final article is subscriber-restricted; the accessible working paper gives the construction and findings, but the final sample, code, city lists, and replication package still need an independent audit before a new application claims reproducibility. [E1; E2]

## Data Requirements

A usable application needs a stable 1990-boundary county crosswalk, the top-20/top-40 city list for each decade, city-core geography, nearest-city distance and ring, census or yearbook population, initial agricultural employment, transport access, region and resource-based status, and prefecture identifiers for clustered inference. Migration mechanisms additionally need origin hukou county and current-residence county from the relevant mini-census. The actual acquisition, restricted-data workflow, GIS files, and joins belong in `Econ Data Know-How`; this record preserves the research contract and the reasons a join can fail. [E2; E3; E4; E5]

## Evidence Notes

E1 is the publisher-independent RePEc metadata for the final 2025 RSUE article: it establishes the authors, DOI, journal, China county period, headline ring contrast, and subscriber restriction; it does not expose the final article’s complete methods or replication files. E2 is the authors’ verified full-text August 2023 working paper: it establishes the top-40/top-20 city definitions, consistent-boundary panel, distance bins, census/yearbook/migration inputs, regression controls, clustering, mechanisms, and the paper’s explicit statement that agriculture and transport are endogenous; it is an earlier version and does not prove that the final article changed nothing. E3–E5 are official National Bureau of Statistics pages for county-level yearbooks, population-census series, and administrative-unit/population records: they establish the official data producers and observation frame, not the paper’s nearest-city ring assignment or causal interpretation. No source here establishes that the spatial exposure is exogenous.
