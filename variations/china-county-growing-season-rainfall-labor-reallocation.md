---
schema_version: 2
id: china-county-growing-season-rainfall-labor-reallocation
name: China County Growing-Season Rainfall Shocks and Rural Labor Reallocation (RUMiC-RHS)
aliases:
- Minale 2018 JoEG agricultural productivity shocks rural-urban migration
- RUMiC county rainfall z-score labor supply IV
- 中国县级生长季降雨冲击与农村劳动力再配置
status: grounded
provenance:
  task_id: task-25e293833573
scope:
  country: China
  regions:
  - 82 RUMiC-RHS rural-survey counties (about 800 villages) in 9 provinces, outcome years 2008-2010
  domains:
  - labor
  - migration
  - agriculture-rural
  - regional-economics
  variation_type: event-shock
  knowledge_role: china-variation
  china_relevance: >
    The variation occurs within China: year-by-county deviations of
    growing-season (March-May) rainfall from county-specific long-term norms
    shift agricultural productivity in 82 counties surveyed by the Rural
    Household Survey of the Rural-Urban Migration in China (RUMiC) project.
    Minale (2018, Journal of Economic Geography) matches these rainfall shocks
    to individual migration and labor-supply histories and shows that rural
    households reallocate labor away from farming toward local off-farm work
    and rural-urban migration in bad-rainfall years. The regional/urban
    content is the spatial rainfall exposure and the rural-urban migration
    margin, not a policy rollout.
identity:
  instrument: >
    The county-year growing-season rainfall shock: total precipitation over
    March-May in year t, expressed as the deviation from the county's
    1978-2010 long-term mean divided by the county's 1978-2010 standard
    deviation (Zscore_Rain). Daily precipitation comes from the Chinese
    National Ground Surface Dataset provided by the China National
    Meteorological Information Centre; each county is assigned the weather
    station closest to its centroid. In the paper's design this shock is used
    as an instrument for agricultural productivity, but because no detailed
    productivity data are available the reported estimates are reduced-form
    effects of rainfall shocks on labor allocation.
  authority: >
    No policy authority assigns treatment. The underlying measurements are
    produced by the China National Meteorological Information Centre (daily
    station precipitation) and the RUMiC project (Rural-Urban Migration in
    China), whose Rural Household Survey is administered by China's National
    Bureau of Statistics. The shock construction (growing-season definition,
    normalization window, station matching) is the author's.
  legal_identifiers:
  - 'Minale, Luigi. 2018. "Agricultural productivity shocks, labour reallocation and rural-urban migration in China." Journal of Economic Geography 18(4): 795-821. DOI: 10.1093/jeg/lby013'
  - Minale, Luigi. 2018. "Agricultural Productivity Shocks, Labor Reallocation, and Rural-Urban Migration in China." CReAM Discussion Paper CDP 04/18 (RePEc handle crm:wpaper:1804), open full text
  - RUMiC Rural Household Survey rounds 2009, 2010, and 2011 (labor-supply outcomes refer to calendar years 2008, 2009, and 2010)
  implementation_regime: >
    Stochastic weather realization, not an administrative regime. Counties
    differ in both levels and variability of growing-season rainfall, so the
    z-score normalization expresses each county-year shock in units of that
    county's own historical dispersion. The long-term reference window is
    1978-2010; the paper's Figure 3 shows the shock distribution for
    county-years 2000-2010, while the estimating panel covers outcome years
    2008-2010. March-May is chosen as the bulk of the growing season for the
    crops cultivated in the surveyed provinces (following Meng and Yamauchi,
    2015), with broader window definitions and out-of-season months used as
    robustness and falsification checks.
  assignment_mechanism: >
    China's size and climatic heterogeneity generate year-to-year,
    county-level variation in growing-season rainfall that is plausibly
    orthogonal to individual labor-allocation choices once individual and
    year fixed effects are included. Each individual inherits the shock of
    the county of residence in each year; identification is within-individual
    over time. The paper's key assumption is that, conditional on individual
    and year fixed effects, local weather shocks are orthogonal to unobserved
    determinants of sectoral labor supply. Rainfall is not claimed to be
    intrinsically exogenous beyond these identifying assumptions.
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 2008
  implementation_end: 2010
  local_timing: >
    Labor-supply outcomes are recorded in the 2009, 2010, and 2011 RUMiC-RHS
    rounds and refer to the previous calendar year, so the estimating panel
    spans outcome years 2008-2010 with yearly (rather than end-of-period)
    recording, which reduces recall bias. The rainfall reference window
    (1978-2010) predates and contains the outcome window. The working paper
    (February 2018) precedes the journal version (published 2018-03-26,
    issue dated August 2018).
  anticipation: >
    Year-to-year rainfall realizations within a three-year panel are not
    plausibly anticipated at the time of planting or migration decisions in
    the previous season, but the record does not verify forward-looking
    adaptation; households with irrigation are reported to be less exposed,
    and the land-tenure interaction shows that expected future land
    reallocations can condition responses. Treat anticipation as bounded by
    the short panel rather than ruled out.
  last_verified: '2026-08-15'
assignment:
  unit: >
    Individual-year: 18,910 working-age individuals (aged 16-65, not in
    school or disabled) observed in at least two of the three survey rounds,
    giving 48,595 individual-year observations across 82 counties. A
    secondary household-year analysis uses a fixed-composition balanced panel
    of 3,794 households (11,382 household-year observations).
  treated: >
    Individuals resident in counties whose growing-season rainfall z-score in
    year t is below (above) the county long-term mean experience a negative
    (positive) agricultural productivity shock; there is no untreated group
    and treatment intensity is the continuous z-score.
  comparison_pool: >
    The same individual in other years (individual fixed effects) and
    individuals in other counties in the same year (year fixed effects absorb
    national shocks); a household fixed-effects version compares the same
    fixed-composition household across years.
  rule: >
    Compute each county's March-May precipitation total for year t, subtract
    the county's 1978-2010 mean, and divide by the county's 1978-2010
    standard deviation; assign each surveyed individual the shock of the
    county of residence, with counties matched to the nearest weather station
    by distance to the county centroid. Regress sector-specific days of work
    (OLS, unconditional on participation) or participation indicators (linear
    probability model) on the z-score with individual and year fixed effects
    and time-varying controls (marital status, counts of household members
    aged under 16, in the workforce, and over 65, and the working-age sex
    ratio), clustering standard errors at the county level (82 clusters).
  intensity: >
    Continuous z-score. The paper reports that a one-standard-deviation
    negative growing-season rainfall shock reduces farming days by 4.5
    percent and increases urban-sector days by 4.9 percent of baseline, with
    urban participation up 2.1 percent of baseline; at the household level
    about 2.1 percent of the baseline farming share of labor supply shifts to
    urban work.
  exemptions:
  - Individuals outside the labor force (in school or disabled) are excluded from the estimating sample
  - Individuals observed in only one of the three rounds cannot enter the within-individual design; the 8,351 individuals with incomplete years are handled by an attrition robustness check
  - Temperature-shock controls are available only for a subset of county-years, so that robustness check uses a restricted sample
  compliance: >
    Exposure is measured, not chosen, but the nearest-station-to-centroid
    match introduces classical measurement error that grows with
    station-county distance; the record does not verify station coverage per
    county. Labor-supply days are self-reported for the previous calendar
    year; yearly recording reduces but does not eliminate recall error.
  exposure_construction: >
    Author construction: daily station precipitation from the Chinese
    National Ground Surface Dataset (China National Meteorological
    Information Centre) aggregated to March-May totals, matched to RUMiC-RHS
    counties by nearest station to county centroid, then normalized against
    the county's 1978-2010 mean and standard deviation. Rainfall is the main
    shock; temperature shocks constructed the same way enter only robustness
    checks.
  required_identifiers:
  - stable county identifier over 2008-2010 linking survey respondents to weather shocks (82 counties)
  - individual and household panel identifiers across the 2009-2011 rounds
  - village identifier for the land-reallocation-risk (LOWRISK) interaction
  - weather station locations and county centroids for the matching rule
  spillovers: >
    The paper's framework allows local off-farm productivity to fall with
    farm income through local demand, so part of the off-farm margin is
    itself shock-affected; destination labor markets receive the induced
    migrant flows but are not modeled, and no spatial equilibrium effects are
    estimated. Cross-county correlation of weather within province-year is
    addressed by a clustering robustness check, not by a spatial model.
research_compatibility:
  outcome_domains:
  - labor supply reallocation across farm, local off-farm, and urban sectors
  - rural-urban migration participation and duration (days in the city)
  - household risk coping and income smoothing through labor markets
  - agricultural productivity shocks and structural transformation
  affected_populations:
  - Working-age rural residents (16-65) in 82 RUMiC-RHS counties across 9 provinces, 2008-2010
  - Rural households exposed to growing-season rainfall variability, including land-tenure-insecure villages
  mechanism_channels:
  - rainfall-driven agricultural productivity shifts changing the relative return to farm versus off-farm and urban work
  - age-specific migration costs and sectoral productivities shaping who migrates versus who stays in local off-farm work
  - land-reallocation risk constraining labor reallocation out of farming
  - irrigation reducing exposure to rainfall fluctuations
  best_for:
  - Designs that need a plausibly exogenous, within-person county-level agricultural productivity shock in rural China around 2008-2010
  - Studies of migration responses on both participation and intensive (days) margins, since days-of-work data distinguish the two
  - Analyses of how land tenure insecurity or irrigation modulates labor reallocation after weather shocks
  not_good_for:
  - Periods after 2010 or before 2008; the RUMiC-RHS rounds and labor-supply module bound the outcome window
  - Questions that need destination-side outcomes (urban wages, receiving-city effects), which the design does not observe
  - Designs that need a direct measure of agricultural productivity or output; the paper reports reduced-form rainfall effects, not an instrumented productivity elasticity
  - Designs that require many clusters; only 82 counties carry the identifying variation
design:
  claim_type: reduced-form
  affordances:
  - Year-by-county growing-season rainfall variation within a short panel, combined with individual fixed effects that absorb time-invariant ability, preferences, productivity, and migration costs
  - Days-of-work data per sector that separate participation (extensive) from duration (intensive) responses, including responses that never cross the participation margin
  - Out-of-growing-season rainfall falsification checks that support the agricultural-productivity channel
  - A matched meteorological dataset with a transparent, reproducible normalization (1978-2010 county mean and standard deviation)
  candidate_designs:
  - Individual fixed-effects panel regression of sector days of work (OLS) or participation (LPM) on the county rainfall z-score with year fixed effects and county clustering
  - Household fixed-effects version on a fixed-composition balanced panel, including shares of household labor supply by sector
  - Heterogeneity by age group, gender, irrigation, and village land-reallocation risk (interaction with the time-invariant LOWRISK indicator)
  - IV interpretation of the same regressions as a two-step rainfall-to-productivity-to-labor chain, reported by the author as reduced form for lack of productivity data
  identifying_variation: >
    Within-individual, over-time differences in labor allocation to farm,
    local off-farm, and urban sectors associated with the county's
    growing-season rainfall z-score, conditional on individual and year fixed
    effects and time-varying household composition controls; cross-sectional
    support comes from China's climatic heterogeneity across the 82 surveyed
    counties within years.
  primary_strategy: >
    Linear probability and OLS fixed-effects regressions (paper Equations 1
    and 2). Outcomes are days of work per sector (unconditional on
    participation) and participation indicators for farm, local off-farm, and
    urban work. The regressor is the county-year growing-season rainfall
    z-score; standard errors are clustered at the county level, with a
    robustness version allowing contemporaneous correlation across counties
    within province-year. The author describes rainfall as an instrument for
    agricultural productivity but reports reduced-form estimates.
  estimand: >
    The reduced-form change in days of work supplied to each sector (and in
    sector participation) associated with a one-standard-deviation deviation
    of growing-season rainfall from the county long-term norm, for rural
    working-age individuals in the surveyed counties over 2008-2010; at the
    household level, the shift in the share of household labor supply across
    sectors.
  treatment_variable: >
    County-year growing-season rainfall z-score (Zscore_Rain): March-May
    precipitation minus the county 1978-2010 mean, divided by the county
    1978-2010 standard deviation; negative values are drought-like shocks for
    rain-fed crops.
  comparison_logic: >
    Within-individual changes across years net of year fixed effects; the
    comparison fails if county-level shocks are correlated with unobserved
    time-varying determinants of labor allocation (for example local policy
    or price changes coincident with rainfall), if station-to-county
    measurement error is non-classical, or if selective attrition correlates
    with shocks.
  estimation_notes: >
    Estimating sample is 48,595 individual-year observations (18,910
    individuals, 82 counties, outcome years 2008-2010). Baseline: farming
    days -4.5 percent and urban days +4.9 percent of baseline per
    one-standard-deviation negative shock (men +5.7, women +3.6 percent on
    urban days); urban participation +2.1 percent of baseline (men +2.6
    percent, women about zero); local off-farm average response small and
    insignificant but negative for younger and positive for older workers;
    conditional-on-participation farm coefficient about 60 percent of the
    unconditional one. Household balanced panel (3,794 households) shifts
    about 2.1 percent of the baseline farming share to urban work. Robustness
    covers a one-month-wider growing season, August-November and
    July-December out-of-season falsifications (coefficients near zero),
    temperature controls on a restricted sample, province-year-correlated
    standard errors, and attrition-restricted estimates. In villages with
    high land-reallocation risk the migration elasticity is about 70 percent
    of that in low-risk villages and statistically indistinguishable from
    zero; the author explicitly declines a causal reading of this interaction
    (LOWRISK is time-invariant, so its level effect is absorbed).
  assumptions:
  - Conditional on individual and year fixed effects, county growing-season rainfall shocks are orthogonal to unobserved determinants of individual labor allocation
  - Rainfall affects labor allocation through agricultural productivity (supported by out-of-season falsifications), not through direct utility or unrelated channels
  - County of residence is correctly and stably assigned, and the nearest-station match measures the relevant growing-season exposure with classical error
  - Survey attrition is not systematically related to rainfall shocks (supported by the restricted-sample check)
  diagnostics:
  - Out-of-growing-season rainfall falsification (August-November and July-December windows) with coefficients near zero
  - Alternative growing-season definitions (one month wider on each side) leaving estimates unchanged
  - Temperature-shock inclusion on the available subsample leaving rainfall estimates virtually unchanged
  - Standard errors robust to contemporaneous correlation across counties within province-year
  - 'Attrition check: restricted always-observed sample yields estimates very similar in size and significance'
threats:
- type: spatial_correlation_and_few_clusters
  basis: reported
  condition: Only 82 counties carry the identifying variation, and weather is spatially correlated; the paper clusters at the county level and shows robustness to province-year contemporaneous correlation, but inference still rests on a modest number of clusters over three outcome years.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Wild-cluster or randomization-inference procedures at the county level
  - Re-estimation excluding one province at a time
- type: exposure_measurement_error
  basis: inferred
  condition: Counties are matched to the nearest weather station by centroid distance; large or topographically diverse counties may be poorly represented by a single station, and the record does not verify station coverage or distance distribution.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Rebuild exposures from gridded precipitation products and compare
  - Weight or restrict by station-to-centroid distance
- type: land_reallocation_interaction_endogeneity
  basis: reported
  condition: The LOWRISK village indicator is time-invariant and potentially endogenous to village institutions; the author reports that migration elasticity in high-reallocation-risk villages is about 70 percent of that elsewhere and insignificant, and explicitly does not give the interaction a causal interpretation.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Instrument or externally validate village land-reallocation risk following Giles and Mu (2018)
  - Check sensitivity to alternative tenure-insecurity measures
- type: selective_attrition
  basis: reported
  condition: 8,351 of the sampled individuals lack complete labor-supply information in all three years; the paper reports that restricted always-observed samples yield similar estimates, but attrition correlated with shocks or migration would still bias the within-individual design.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Model attrition as a function of lagged shocks and observables
  - Inverse-probability weight the always-observed sample
- type: destination_and_general_equilibrium_effects
  basis: inferred
  condition: Induced migrant flows may affect destination labor markets and origin-local off-farm productivity (the paper's own framework has local off-farm productivity falling with farm income through demand), so the reduced-form shock captures more than a pure farm-productivity movement.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Combine with destination-city data to test receiving-market responses
  - Estimate local off-farm wage or price responses to the same shocks
- type: county_trend_confounding
  basis: inferred
  condition: The specification includes individual and year fixed effects but, in the inspected text, no county-specific trends; slowly trending local conditions (for example irrigation expansion or industrialization) correlated with rainfall realizations would remain.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Add county-specific linear trends and test stability
  - Placebo-test with future or lagged shocks where the panel permits
empirical_requirements:
  contract_version: 1
  population: Working-age rural residents (16-65, not in school or disabled) in the 82 RUMiC-RHS counties of 9 provinces, and their households
  observation_unit: individual-year for the main design; household-year (fixed composition) for the household design
  geography_level: county of residence (82 RUMiC-RHS counties) with village identifiers for tenure-risk splits
  time_start: 2008
  time_end: 2010
  minimum_frequency: annual
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields:
  - days of work in the previous calendar year for farm, local off-farm, and urban sectors
  - sector participation indicators derived from positive days
  - individual demographics (age, gender, education, marital status) and household composition (members under 16, in workforce, over 65, working-age sex ratio)
  - household irrigation access and village land-reallocation-risk indicator for heterogeneity
  - county of residence for each individual-year
  - March-May county precipitation totals and the county 1978-2010 reference distribution
  required_identifiers:
  - individual_id
  - household_id
  - village_id
  - county_id
  - year
  treatment_key:
  - county_id
  - year
  treatment_source: >
    County-year growing-season rainfall z-score built from China National
    Meteorological Information Centre daily station precipitation (nearest
    station to county centroid), March-May totals normalized by the county
    1978-2010 mean and standard deviation, as constructed by the author.
  measurement_risks:
  - nearest-station matching may mismeasure county-level growing-season exposure
  - self-reported previous-year days of work carry recall error despite yearly recording
  - county boundary or code changes over 2008-2010 are not verified in this record
  - RUMiC-RHS access is restricted, and the survey's county list is not published in the inspected text
design_profiles:
- id: household-share-design
  label: Fixed-composition household panel design
  design_families:
  - household fixed-effects panel
  when_to_use: Use when decisions are modeled at the household level and a stable household composition is required; aggregates individual labor supply within families.
  outcome_domains:
  - household labor supply shares across farm, local off-farm, and urban sectors
  requirements:
    population: Fixed-composition balanced panel of 3,794 RUMiC-RHS households whose members report labor supply in all three rounds
    observation_unit: household-year
    geography_level: county of residence
    time_start: 2008
    time_end: 2010
    minimum_frequency: annual
    minimum_pre_periods: 0
    minimum_post_periods: 0
    required_fields:
    - per-member days of work by sector for all workforce members in all three years
    - household participation indicators and shares of total household working days by sector
    - household composition controls
    required_identifiers:
    - household_id
    - county_id
    - year
    treatment_key:
    - county_id
    - year
evidence:
- id: E1
  source_type: paper
  citation: 'Minale, Luigi. 2018. "Agricultural Productivity Shocks, Labor Reallocation, and Rural-Urban Migration in China." CReAM Discussion Paper CDP 04/18, February 2018 (open full text; the working-paper version of the Journal of Economic Geography article).'
  url: https://cream-migration.org/publ_uploads/CDP_04_18.pdf
  date: 2018
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
    Open working-paper PDF fetched and read 2026-08-15 (direct download
    returned 403; the text-extraction route covered the document through
    Section 5.4, and the text contains OCR-style concatenation artifacts):
    Abstract; Section 1 (motivation, RUMiC descriptive facts on migrant
    mobility); Section 3.1 (RUMiC-RHS coverage of 82 counties and about 800
    villages in 9 provinces, NBS administration, 2009-2011 rounds with
    previous-calendar-year days of work, 18,910 individuals and 48,595
    individual-year observations, balanced household panel of 3,794
    households; weather construction from the Chinese National Ground Surface
    Dataset of the China National Meteorological Information Centre,
    nearest-station-to-centroid matching, March-May growing season following
    Meng and Yamauchi 2015, z-score normalization against the 1978-2010
    county mean and standard deviation, Figure 3 distribution for 2000-2010);
    Section 3.2 (Tables 1-2, Figures 4-6 descriptive patterns); Section 4
    (Equations 1-2, individual and household fixed effects, control set,
    county clustering with province-year correlation robustness, reduced-form
    interpretation); Sections 5.1-5.2 (Tables 3-6 baseline, participation,
    intensive-margin, growing-season and out-of-season falsifications,
    temperature robustness); Section 5.3 (Figure 7 age heterogeneity);
    Section 5.4 through the first part of Table 8 discussion (household share
    results). Establishes the design, data construction, and reported
    diagnostics; it does not independently verify the underlying survey or
    meteorological datasets, and the text tail (rest of Section 5.4, the
    land-tenure Section 5.5 detail beyond what E3 records, and the
    conclusion) was outside the inspected extraction.
- id: E2
  source_type: paper
  citation: 'Minale, Luigi. 2018. "Agricultural productivity shocks, labour reallocation and rural-urban migration in China." Journal of Economic Geography 18(4): 795-821. DOI: 10.1093/jeg/lby013 (bibliographic record and official abstract).'
  url: https://doi.org/10.1093/jeg/lby013
  date: 2018
  supports:
  - identity.legal_identifiers
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
  - assignment.intensity
  verification_status: verified
  access_level: abstract
  locator: >
    EconPapers item page for the journal article and the Crossref record for
    DOI 10.1093/jeg/lby013, both read 2026-08-15 (the OUP article page
    returned 403 and was not read). They establish the published identity
    (author, journal, volume 18, issue 4, pages 795-821, publication date
    2018-03-26) and the official abstract, which reports the 4.5 percent
    farming and about 5 percent migration responses to a one-standard-
    deviation negative shock, the intensive/extensive decomposition, the
    generational heterogeneity, and the land-tenure-insecurity moderation.
    Establishes publication identity and headline results; design details
    rest on E1.
- id: E3
  source_type: paper
  citation: 'Minale, Luigi. 2018. CReAM Discussion Paper CDP 04/18, Section 5.5 and Table 9 (land-reallocation-risk interaction), cross-referenced with Giles, John, and Ren Mu. 2018. "Village Political Economy, Land Tenure Insecurity, and the Rural to Urban Migration Decision: Evidence from China." American Journal of Agricultural Economics 100(2): 521-544.'
  url: https://cream-migration.org/publ_uploads/CDP_04_18.pdf
  date: 2018
  supports:
  - design.estimation_notes
  - identity.legal_identifiers
  verification_status: reported
  access_level: full-text
  locator: >
    Section 5.5 of the same working paper: the direct text extraction
    inspected for this record stopped in Section 5.4, so the Section 5.5
    detail (Equation 3 interacting the shock with the time-invariant village
    LOWRISK indicator, the roughly 70-percent relative elasticity in
    high-reallocation-risk villages with insignificance there, footnote 6
    noting the LOWRISK level effect is not separately identified, and the
    explicit refusal of a causal interpretation) is recorded as a reported
    claim pending a full-text re-inspection of that section. The qualitative
    direction is corroborated by the official abstract (E2).
- id: E4
  source_type: official-data
  citation: 'IZA Research Data Center (IDSC). "Longitudinal Survey on Rural Urban Migration in China (RUMiC)." Scientific Use File documentation, DOI: 10.15185/izadp.7680.1.'
  url: https://datasets.iza.org/dataset/58/longitudinal-survey-on-rural-urban-migration-in-china
  date: 2024
  supports:
  - identity.authority
  - identity.legal_identifiers
  - timeline.local_timing
  - assignment.unit
  - empirical_requirements.population
  verification_status: verified
  access_level: official-document
  locator: >
    IDSC dataset page fetched and read 2026-08-15: states that RUMiC
    consists of the Urban Household Survey, the Rural Household Survey, and
    the Migrant Household Survey; that it was initiated by researchers at the
    Australian National University, the University of Queensland, and Beijing
    Normal University with IZA providing the Scientific Use Files; that the
    Rural Household Survey was conducted in nine provinces (Anhui, Chongqing,
    Guangdong, Hebei, Henan, Hubei, Jiangsu, Sichuan, Zhejiang); that the
    design is longitudinal over a multi-year span with low rural attrition
    between the first and second waves; and it lists Minale (2018, Journal of
    Economic Geography 18(4): 795-821, DOI 10.1093/jeg/lby013) among related
    publications. Establishes the survey's identity, responsible repository,
    coverage, and longitudinal frame; it does not document the specific
    days-of-work module wording or the surveyed county list.
- id: E5
  source_type: official-data
  citation: '中国气象局 (China Meteorological Administration). 2013-12-24. "中国气象局发布18个基础气象资料产品" (CMA releases 18 basic meteorological data products). Government portal news release describing the National Meteorological Information Centre (NMIC) quality-controlled national surface meteorological dataset program.'
  url: https://www.cma.gov.cn/2011xwzx/2011xqxxw/2011xqxyw/201312/t20131225_234766.html
  date: '2013-12-24'
  supports:
  - identity.authority
  - identity.instrument
  - assignment.exposure_construction
  verification_status: verified
  access_level: official-document
  locator: >
    CMA government portal release fetched and read 2026-08-15: states that
    the National Meteorological Information Centre (国家气象信息中心, NMIC)
    leads the national basic-meteorological-data program launched in 2011,
    that the 2012 ground-surface basic data products were followed by further
    datasets released on 2013-12-24 (18 products plus homogenized national
    surface-station temperature and precipitation series), and that the
    production applies fusion, quality control, gap-filling, and
    homogenization with over 400 data workers participating. Establishes that
    NMIC is the official producer of quality-controlled national daily
    surface-station datasets including precipitation - the dataset family the
    paper names as the Chinese National Ground Surface Dataset. It does not
    verify the specific station list, variables, or years the author
    extracted, and the data.cma.cn dataset detail page did not render its
    content on 2026-08-15.
design_applications:
- paper: Agricultural productivity shocks, labour reallocation and rural-urban migration in China
  doi: 10.1093/jeg/lby013
  journal: Journal of Economic Geography
  year: 2018
  research_question: Do rural Chinese households reallocate labor away from farming toward local off-farm work and rural-urban migration in response to negative agricultural productivity shocks, and along which margins?
  population: 18,910 working-age individuals (48,595 individual-year observations) in 82 RUMiC-RHS counties across 9 provinces, outcome years 2008-2010; household analysis on 3,794 fixed-composition households
  outcome: Days of work supplied to farm, local off-farm, and urban sectors (participation and intensive margins) and household shares of labor supply by sector
  data_used:
  - RUMiC Rural Household Survey rounds 2009-2011 (individual migration and labor-supply histories, days of work per sector for the previous calendar year)
  - Chinese National Ground Surface Dataset daily precipitation (China National Meteorological Information Centre), matched to counties by nearest station to centroid
  - Survey-based household irrigation and village land-reallocation-risk indicators
  treatment_encoding: County-year growing-season (March-May) rainfall z-score against the county 1978-2010 reference distribution, assigned to individuals by county of residence; individual and year fixed effects with time-varying household composition controls; county-clustered standard errors
  comparison: Within-individual changes across 2008-2010 net of year fixed effects; household fixed-effects replication on a balanced panel; heterogeneity by age, gender, irrigation, and village land-reallocation risk
  empirical_design: Individual and household fixed-effects panel regressions (LPM and OLS) of sector labor supply on a county rainfall shock, interpreted as the reduced form of a rainfall-to-productivity IV chain
  assumptions:
  - Rainfall shocks are orthogonal to unobserved labor-allocation determinants conditional on individual and year fixed effects
  - The effect runs through agricultural productivity (out-of-season falsifications reported near zero)
  - Attrition is not shock-correlated (restricted-sample robustness reported similar)
  threats_addressed:
  - Endogeneity of agricultural productivity via weather shocks rather than measured productivity
  - Growing-season definition sensitivity and out-of-season falsification
  - Temperature confounding on the available subsample
  - Spatial correlation of errors via county clustering and province-year correlation robustness
  - Selective attrition via always-observed-sample re-estimation
  evidence_refs:
  - E1
  - E2
  - E3
  - E4
method_transfer: null
readiness_blockers:
- The working-paper text extraction inspected here stopped before the end of Section 5.4; the land-tenure interaction detail (E3) is a reported claim pending full re-inspection of Section 5.5 and Table 9 in either version of the paper.
- RUMiC-RHS microdata are access-restricted and the surveyed county list is not published in the inspected text, so county identifiers, boundary stability over 2008-2010, and station-to-county distances are unverified.
- The design is reduced-form; no direct agricultural productivity measurement was available to the author, so the rainfall-to-productivity first stage is argued from the agricultural literature and falsification tests rather than estimated.
- The outcome window ends in 2010; post-RUMiC reuse requires a different household panel and re-validation of the whole construction.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Rural Chinese households in the late 2000s earned most of their income from
agriculture, faced incomplete insurance and credit markets, and lived under
institutions that made migration mostly temporary: the hukou system limited
permanent relocation, and village land could be reallocated, so leaving
farming carried a risk of losing land [E1]. Weather accounted for a
substantial share of annual variation in agricultural production (the paper
cites 25-30 percent from Zhang and Carter 1997), and irrigation was only
partially available, so growing-season rainfall was a first-order driver of
farm productivity in the surveyed provinces [E1]. The RUMiC project, whose
Rural Household Survey is administered by China's National Bureau of
Statistics, began yearly longitudinal surveys of rural, urban, and migrant
households in 2008; the 2009-2011 rounds record, for each working-age
member, the days worked in the previous calendar year in farm work, local
off-farm work, and urban work [E1, E4].

## What Changed

No policy changed: the variation is the year-to-year realization of
March-May rainfall in each county relative to its own 1978-2010
distribution [E1]. The canonical boundary of this record is that
weather-shock exposure as constructed and used by Minale (2018): county
growing-season rainfall z-scores matched to RUMiC-RHS individual labor
histories over outcome years 2008-2010 [E1, E2]. Related but distinct
objects - the land-reallocation-risk interaction (which uses village tenure
institutions, not weather), commodity-price-driven migration instruments,
and hukou-policy variation - are outside this boundary and must not be
merged into it [E1, E3; analytical inference on the boundary].

## Implementation and Assignment

Each individual inherits the shock of the county of residence: March-May
precipitation from the nearest weather station to the county centroid,
normalized by the county's 1978-2010 mean and standard deviation [E1]. The
estimating design compares the same individual across the three outcome
years under individual and year fixed effects, with county-level clustering
(82 clusters) and a province-year correlation robustness check [E1]. A
one-standard-deviation negative shock is reported to cut farming days by
4.5 percent and raise urban days by 4.9 percent of baseline, with urban
participation up 2.1 percent of baseline; younger workers shift toward
migration while older workers shift toward local off-farm work, and
households move about 2.1 percent of the baseline farming share into urban
work [E1, E2].

## Why This Creates Empirical Variation

China's size and climatic heterogeneity generate rainfall variation both
across counties within a year and within counties across years, and the
short panel with individual fixed effects turns that into within-person
identifying variation [E1]. The days-of-work data are the distinctive
affordance: responses along the intensive margin (longer or shorter city
spells) are visible even when participation does not change, which
participation-only datasets would miss [E1]. Out-of-growing-season rainfall
falsifications near zero support the agricultural-productivity channel
rather than a generic weather-mood channel [E1].

## Identification Risks

Identification rests on conditional orthogonality of county rainfall shocks,
not on any claim that rainfall is intrinsically exogenous [E1]. The main
risks are the modest 82-county cluster count over three years, measurement
error from nearest-station matching, shock-correlated attrition (tested and
reported similar), destination and local-demand spillovers that the
reduced-form shock bundles into the estimate, and the absence of
county-specific trends in the inspected specification [E1; the last two are
analytical inference]. The land-tenure interaction is explicitly
non-causal: LOWRISK is time-invariant and village institutions may be
endogenous [E3].

## Data Requirements

Reuse requires RUMiC-RHS microdata (access-restricted) with individual and
household panel identifiers, county of residence, and days of work by
sector for 2008-2010, joined to county growing-season rainfall built from
China National Meteorological Information Centre station data with a
1978-2010 reference window [E1]. Village identifiers are needed for the
tenure-risk analysis [E3]. Dataset acquisition paths belong in the
companion data repository; this record stores only the treatment contract.

## Evidence Notes

E1 is the open CReAM working-paper full text, read through Section 5.4; it
establishes the survey, shock construction, equations, controls, results,
and robustness checks, but not the underlying restricted datasets, and its
text carries extraction artifacts. E2 is the official abstract and
bibliographic record of the published JoEG version (the OUP page returned
403), establishing publication identity and headline results. E3 records
the land-tenure Section 5.5 content as a reported claim because the
inspected extraction stopped in Section 5.4; its qualitative direction is
corroborated by the abstract. E4 is the IZA IDSC Scientific Use File
documentation, read directly; it establishes the survey's three-part
structure, nine RHS provinces, longitudinal frame, responsible repository,
and the link to this paper. E5 is the CMA government portal release, read
directly; it establishes NMIC as the official producer of quality-controlled
national daily surface-station datasets including precipitation, but not
the exact stations or years the author extracted. No evidence in this
record was built from search snippets, and nothing here certifies the shock
as exogenous beyond the paper's stated assumptions.
