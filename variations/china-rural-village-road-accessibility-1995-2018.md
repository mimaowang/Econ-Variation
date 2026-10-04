---
schema_version: 2
id: china-rural-village-road-accessibility-1995-2018
name: China's Rural-Village Road Accessibility Expansion (1995–2018; Chen et al. 2026 application)
aliases:
- Rural Roads to Growth in China
- China village road-accessibility change
- NVRCP-period rural road expansion
- 中国乡村道路可达性变化
- 村庄道路可达性扩张
status: design-documented
provenance:
  task_id: task-c70ab772c9d8
scope:
  country: China
  regions:
  - Mainland China's rural administrative villages
  domains:
  - rural-development
  - regional-economics
  - economic-geography
  - transportation
  - infrastructure
  - economic-growth
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    The exposure is the realized change in mainland Chinese villages' proximity
    to paved roads during a nationwide period of rural-network expansion. It is
    useful for rural and regional-development questions, but it is not a single
    centrally assigned cohort or a claim that village road placement was random.
identity:
  instrument: >
    In Chen et al. (2026), the study-specific exposure is the change from 1995
    to 2018 in each village's minimum distance to paved roads, interpreted as
    improved local road accessibility. The paper places this expansion in the
    context of the National Village Road Connectivity Project (NVRCP) and the
    2006 rural-road investment plan, but does not define its treatment as
    eligibility for, or assignment to, either one program. Do not recast this
    continuous access measure as an NVRCP-only policy shock.
  authority: >
    The paper attributes the nationwide expansion context to central rural-road
    initiatives and reports the Ministry of Transport's 2006 rural-road plan.
    The Ministry's 2018 Rural Road Construction and Management Measures define
    county, township, and village roads and describe county- and township-level
    responsibilities; those rules took effect in 2018 and cannot establish the
    exact institutional arrangements or project dates for every earlier year.
  legal_identifiers:
  - National Village Road Connectivity Project (NVRCP; paper's term for the nationwide program context)
  - Ministry of Transport, Rural Road Construction and Management Measures, Order No. 4 of 2018 (effective 2018-06-01; road-class and responsibility context only)
  implementation_regime: >
    The observed 1995–2018 expansion accumulated across a multi-level network
    and multiple road classes. In the paper, NVRCP and the 2006 investment plan
    explain the historical setting, not a common assignment rule. The Ministry's
    2018 regulation defines rural roads as planned county, township, and village
    roads and leaves planning, annual projects, and implementation to several
    local levels. It is evidence about the late-period institutional framework,
    not proof of one uniform national rollout over the full sample window.
  assignment_mechanism: >
    There is no random or fixed-cohort assignment in the paper's main exposure.
    Road locations and investment are selected through the evolving network and
    local planning. The authors explicitly address endogenous placement with
    historical-road and topographic instruments; the exclusion restrictions are
    assumptions to assess, not institutional facts that make treatment
    exogenous.
  parent: null
  related_variations:
  - china-highway-network-expansion
timeline:
  announcement: null
  effective: 2018-06-01 (2018 Ministry regulation only; not the start of the paper's exposure)
  implementation_start: 1995
  implementation_end: 2018
  local_timing: >
    These are the two observed endpoints of the paper's long-difference design,
    not policy launch and completion dates. The paper compares road access in
    1995 with 2018; it does not recover annual village-level road-opening dates
    or a common NVRCP treatment year. Its background dates the NVRCP to around
    the beginning of the 2000s and separately reports a 2006 investment plan.
  anticipation: >
    Not applicable as a single event-study onset: the exposure accumulates over
    a 23-year interval. Villages and local governments may anticipate or
    influence road investment through local plans, and nationwide policy phases
    overlap the same interval.
  last_verified: '2026-10-02'
assignment:
  unit: >
    Village point and its surrounding GIS buffer; the preferred paper sample is
    387,667 mainland rural villages observed at the 1995 and 2018 endpoints.
  treated: >
    A village with a larger reduction in minimum distance to paved roads has a
    larger measured accessibility improvement. The paper's main long-difference
    regressor is signed as 2018 minus 1995 minimum distance, so an improvement
    is negative; for an intuitive positive exposure one may reverse the sign,
    while preserving the paper's coding when replicating.
  comparison_pool: >
    The paper uses continuous cross-village differences in access change, not a
    binary treated-versus-control split. Villages in the same county are
    compared conditional on county fixed effects, observed changes in climate,
    and distances to county and prefecture centers. Those comparison villages
    may themselves benefit from nearby roads or nationwide programs.
  rule: >
    For the paper's baseline, calculate the change in minimum distance from
    each village point to paved roads between the 1995 and 2018 RESDC vector
    maps. The paper considers all four road classes in the network measure so
    that road upgrades do not disappear when a lower-class road is reclassified.
    This is an observed network-access rule, not an administrative eligibility
    threshold or randomized route assignment.
  intensity: >
    Continuous change in minimum distance to paved roads. Alternatives in the
    paper include change in road density within village-centered buffers and
    change in network travel time to the nearest county center. The main
    specification uses 1-km-radius buffers, with 0.5-, 2-, and 3-km alternatives.
  exemptions:
  - The main rural-village sample excludes Hong Kong, Macao, Taiwan, offshore villages, missing values, and outliers; the paper reports 3.1% of its full village sample excluded for missing values or outliers.
  - Urban communities are not part of the preferred rural-village sample, though the paper reports separate expanded-sample checks.
  - Road access can include national, provincial, county, and township roadways; it is not limited to roads legally classified as rural.
  compliance: >
    This is realized network access, not compliance with a single treatment offer.
    The paper reports that township roads were the nearest road for 53.69% of
    village sites in 1995 and 85.29% in 2018, but that does not mean every
    village was assigned or connected under the same project.
  exposure_construction: >
    Geocode village committee points from the 2021 National Bureau of Statistics
    statistical code list, construct a 1-km circular buffer, overlay the 1995
    and 2018 paved-road vector maps, and calculate the nearest-road distances.
    For exact replication, preserve the paper's signed change, rural-village
    sample restrictions, all-class road network, and 2021 point locations. The
    1995 and 2018 maps are snapshots; they do not supply annual opening cohorts.
  required_identifiers:
  - stable village identifier and 2021 National Bureau of Statistics code-list entry
  - village committee coordinates and rural-village classification
  - county identifier and historical county crosswalk
  - 1995 and 2018 road geometries and road-class attributes
  - 1995 and 2018 night-light raster values aligned to the village buffer
  spillovers: >
    Roads connect markets and can affect nearby villages through access,
    migration, remittances, and knowledge flows. The paper notes that within-
    county comparison villages may share access gains and that its local
    estimates need not equal county- or regional-level net effects.
research_compatibility:
  outcome_domains:
  - local economic activity and long-run rural growth
  - market access and spatial development
  - migration, labor allocation, and local spillovers
  - road-class-specific infrastructure returns
  affected_populations:
  - residents of mainland rural administrative villages
  - workers and households connected to village and nearby labor markets
  - firms and producers using local road networks
  mechanism_channels:
  - travel-cost and market-access changes
  - local trade and factor mobility
  - migration and remittance flows
  - links between lower-tier roads and village-level economic activity
  best_for:
  - Studying continuous, long-run changes in village road accessibility rather than a single policy cohort
  - Comparing nearby and distant market access or heterogeneity by baseline development
  - Understanding how village-scale all-road exposure differs from county-level NTHS trunk-highway proximity
  - Designs that can reconstruct village-point, road-map, buffer, and night-light joins and assess the IV assumptions
  not_good_for:
  - Treating NVRCP or the 2006 investment plan as the paper's exact treatment assignment rule
  - Claiming annual treatment timing or a staggered-DID cohort from two road-map snapshots
  - Treating the 1962-road or terrain instruments as automatically exogenous
  - Interpreting village night lights as directly observed village GDP
  - Estimating national aggregate road benefits from the paper's within-county village comparison alone
design:
  claim_type: causal
  affordances:
  - continuous change in village proximity to paved roads
  - long-difference outcome between 1995 and 2018 with county fixed effects
  - historical-road and off-village terrain IVs reported in a recent JRS application
  - heterogeneity by baseline socioeconomic status, market access, and road class
  candidate_designs:
  - village-level long-difference OLS for descriptive or conditional associations
  - 2SLS using the paper's 1962-road and terrain instruments, only with explicit exclusion-restriction analysis
  - alternative continuous access measures based on road density and travel time
  - township-road-specific exposure, keeping the paper's instrumenting restriction distinct from the all-road baseline
  identifying_variation: >
    The paper identifies from differences across villages in how much the
    nearest paved-road distance changed over 1995–2018. Road expansion and
    placement respond to development needs and policy, so the long difference
    removes time-invariant factors but does not by itself randomize exposure.
    The reported IV strategy predicts road-access change using the village's
    distance to the 1962 road network and ring averages of terrain outside the
    village buffer.
  primary_strategy: >
    Chen et al. (2026) estimate a village-level long-difference model for the
    change in log PANDA-China nighttime lights, include county fixed effects and
    controls for climate changes and distances to county and prefecture centers,
    and report 2SLS estimates using distance to 1962 roads and off-village
    slope, ruggedness, and elevation. The paper reports first-stage
    Kleibergen–Paap statistics above 100. This documents the authors' design;
    it does not establish the instruments' exclusion restrictions.
  estimand: >
    Under the paper's IV assumptions, the coefficient is the effect of a
    village's road-access improvement for places whose access responds to the
    historical-road and terrain instruments. With continuous treatment and
    heterogeneous responses, do not call it a general national average effect
    or a policy-assignment LATE without further assumptions.
  treatment_variable: >
    Baseline: ΔMinDistToRoad = minimum distance in 2018 minus minimum distance
    in 1995, measured in kilometers; more negative values mean improved access.
    Alternatives are Δ road density in village buffers and Δ travel time to the
    nearest county center. A separate road-class analysis classifies changes by
    the nearest road type in 2018; its township-road exposure is instrumented
    separately.
  comparison_logic: >
    The long-difference compares village outcome and access changes within a
    county, conditional on measured covariates. The IV estimates further use
    predicted differences in access from historical road proximity and terrain.
    This is not a before/after cohort design, and non-treated status cannot be
    inferred from a village simply being farther from a road.
  estimation_notes: >
    The main sample has 387,667 rural villages across two cross-sections, 1995
    and 2018. The outcome is mean nighttime-light digital number in a 1-km
    village buffer from PANDA-China, a 1-km product resampled to 500 m for
    buffer calculations; the paper calibrates light against prefecture GDP and
    agricultural GDP, but village GDP is not observed. The paper's full IV
    specification reports a second-stage coefficient of -0.571 on the signed
    distance change and Hansen J p=0.000; reported overidentification results
    vary across instrument sets. The article translates the estimate into
    annual GDP growth using a prefecture-level light elasticity. Treat that
    translation as the paper's interpretation, not as a directly observed
    village-GDP result.
  assumptions:
  - Conditional on controls and county fixed effects, distance to 1962 roads affects 1995–2018 village economic change only through subsequent road access.
  - Off-village terrain rings predict road construction feasibility but do not independently affect local growth through agriculture, settlement, amenities, or other channels after controls.
  - The two-point long difference captures the intended long-run contrast without unobserved village-specific trend shocks correlated with road investment.
  - The spatial spillovers and policy overlaps do not invalidate the stated comparison or are modeled separately.
  diagnostics:
  - Report first-stage results and each Hansen J result; a large first-stage F statistic does not verify the exclusion restriction.
  - Test 1962-road IVs separately from terrain instruments and report sensitivity to instrument sets and functional forms.
  - Examine terrain's direct relationship with non-road outcomes and alternative geographic controls; assess off-village ring definitions.
  - Reproduce the 2021 village-point join, sample exclusions, road-class coding, and 1-km buffers against the paper's reported counts.
  - Test alternative road-access measures, buffer radii, night-light treatment, and migration or settlement-light concerns as in the paper's robustness analyses.
  - Separate within-village access effects from county-wide gains, neighboring-village spillovers, and the consequences of population movement.
threats:
- type: endogenous-road-placement-and-targeting
  basis: reported
  condition: >
    The paper acknowledges that road investments may target underdeveloped
    villages and reports evidence that lower-growth villages receive more road
    investment. It uses IVs to address this concern, but this documented
    endogeneity is why simple OLS or the presence of a national campaign should
    not be read as as-if-random assignment [E1].
  evidence_refs:
  - E1
  possible_diagnostics:
  - compare OLS and IV estimates while keeping the estimand change explicit
  - reconstruct time-varying targeting or poverty-alleviation measures where available
  - test alternative road-access measures and sample definitions
- type: historical-road-exclusion
  basis: inferred
  condition: >
    Distance to the 1962 road network predicts later road access, but old
    corridors may also proxy for persistent settlement, trade, or market access.
    The authors argue that long differences and county fixed effects address
    persistent geography; whether they remove all relevant village-specific
    channels remains an identifying assumption, not a verified institutional
    fact [E1].
  evidence_refs:
  - E1
  possible_diagnostics:
  - inspect alternative historic-route measures and pre-period outcomes if available
  - test sensitivity to market-center distances, county trends, and historical settlement controls
  - report specifications with and without the historical-road instrument
- type: terrain-exclusion-and-overidentification
  basis: reported
  condition: >
    Off-village rings are designed to measure construction feasibility, but
    slope, ruggedness, and elevation can also shape settlement, agriculture,
    transport, and amenities. The paper reports Hansen J p-values of 0.0471,
    0.0899, and 0.000 across its Table 6 instrument sets; the all-instrument
    specification rejects the overidentifying restrictions, so its IV result
    must remain conditional rather than treated as independently validated
    [E1].
  evidence_refs:
  - E1
  possible_diagnostics:
  - report each instrument-set test and avoid selecting a specification only for its estimate
  - assess terrain effects on outcomes plausibly unrelated to roads
  - compare the 1962-road-plus-slope specification with alternative terrain sets
- type: night-light-proxy-and-sample-geography
  basis: reported
  condition: >
    Village-level outcomes are night lights because the paper says village GDP
    is not officially observed. Its GDP-light calibration is at prefecture
    level, and its locations come from a 2021 village code list rather than
    historical village-boundary polygons. Light-to-GDP translation, village
    survival, geocoding, and fixed-radius buffers may therefore affect the
    interpretation [E1].
  evidence_refs:
  - E1
  possible_diagnostics:
  - keep night-light estimates separate from the paper's translated GDP interpretation
  - report the point-list vintage, rural-village filters, and alternative buffer radii
  - test settlement-light exclusions and alternative village geographies where possible
- type: spatial-spillovers-and-concurrent-change
  basis: reported
  condition: >
    Nearby villages can share market access, migration, remittance, and
    knowledge gains, while the long interval also contains rural-to-urban
    migration and several nationwide infrastructure phases. The paper discusses
    migration-related light changes and reports robustness checks, but those do
    not turn its village coefficient into a total regional effect [E1].
  evidence_refs:
  - E1
  possible_diagnostics:
  - define a spatial exposure mapping and vary the distance band around roads
  - distinguish within-county redistribution from net county or regional gains
  - assess migration and settlement-light adjustments separately from the baseline
empirical_requirements:
  contract_version: 1
  population: >
    Mainland rural villages represented in the 2021 NBS statistical code list
    and observed in the paper's 1995 and 2018 geospatial cross-sections; the
    authors report a final sample of 387,667 after offshore, missing, and
    outlier exclusions.
  observation_unit: Village-point buffer with a two-date long-difference outcome and exposure
  geography_level: Village within county; road and market-access measures constructed in GIS
  time_start: 1995
  time_end: 2018
  minimum_frequency: Two endpoint cross-sections for the documented long-difference design
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - stable village code, village type, and committee coordinates from the 2021 NBS list
  - county and prefecture codes for fixed effects and market-center distances
  - paved-road geometries and road classes for 1995 and 2018
  - 1995 and 2018 village-buffer night-light measures
  - village-level change in precipitation and spring temperature
  - distance to nearest county and prefecture administrative centers
  - 1962 road geometry and terrain rasters/ring summaries if reproducing 2SLS
  required_identifiers:
  - 2021 NBS village code and village committee coordinate
  - historical county code or documented county crosswalk
  - map vintage and road-class attribute
  - village point, buffer radius, and raster cell alignment
  treatment_key:
  - village code and coordinates
  - 1995 and 2018 nearest paved-road distance
  - signed distance change and road-class measure
  - 1962 historical-road distance and terrain-ring measures for IV replication
  treatment_source: >
    The article reports road vector maps from the Chinese Academy of Sciences'
    Resource and Environmental Science Data Center (RESDC). Xiamen University's
    economics data catalogue lists road shapefiles for 1995, 2012, 2016, and
    2018, with national, provincial, county, township, expressway, railway, and
    other categories; the catalogue directs users to apply for access [E4].
    The paper also uses a 1962 Sino Maps Press road map, the 2021 NBS village
    code list, PANDA-China night lights, NASADEM terrain, and stated climate
    datasets. Availability, licensing, exact GIS processing, and the second
    project's data-acquisition path must be checked separately.
  measurement_risks:
  - 1995 and 2018 are map snapshots, not annual construction timing or cohort data
  - paper's main access metric includes all paved-road classes; it is not an isolated township-road treatment
  - road upgrades and reclassification can change map attributes without a new route
  - 2021 village points may not match historical settlement locations or administrative boundaries
  - 1-km buffers approximate settlement areas because historical village boundaries are unavailable
  - night lights proxy local economic activity and are not village GDP
  - commercial, application-only, or separately licensed data may limit reconstruction
evidence:
- id: E1
  source_type: paper
  citation: >
    Chen, Wei; Chen, Junliang; Qiu, Huanguang; Yu, Jialing; Chen, Wei; and
    Wang, Xinyue. 2026. “Roads to Growth: Evidence From Rural China.” Journal
    of Regional Science 66(2): 542–562. DOI: 10.1111/jors.70045. Full published
    article PDF uploaded by coauthor Junliang Chen as author content; the PDF
    carries Wiley journal pagination and open-access terms.
  url: https://www.researchgate.net/publication/399527685_Roads_to_Growth_Evidence_From_Rural_China
  date: '2026-01-06'
  supports:
  - scope.china_relevance
  - identity.instrument
  - identity.authority
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.implementation_start
  - timeline.implementation_end
  - timeline.local_timing
  - timeline.anticipation
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.compliance
  - assignment.exposure_construction
  - assignment.required_identifiers
  - assignment.spillovers
  - research_compatibility.outcome_domains
  - research_compatibility.affected_populations
  - research_compatibility.mechanism_channels
  - research_compatibility.best_for
  - research_compatibility.not_good_for
  - design.claim_type
  - design.affordances
  - design.candidate_designs
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - design.assumptions
  - design.diagnostics
  - threats.condition
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.geography_level
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_key
  - empirical_requirements.treatment_source
  - empirical_requirements.measurement_risks
  - design_applications.paper
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
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
    Full article, especially pp. 1–2 (question and NVRCP context), pp. 3–5
    (village, night-light, road data and sample), pp. 6–7 (long-difference and
    IV construction), pp. 9–10 Table 6 (first-stage and Hansen J tests), and
    pp. 11–14 (robustness, migration, market access, and road-class analysis).
    Author-upload page identifies the file as author content uploaded
    2026-02-27; the full PDF states it was downloaded from Wiley and is under
    the publisher's OA terms.
- id: E2
  source_type: paper
  citation: >
    Wiley Online Library article record for Chen et al., “Roads to Growth:
    Evidence From Rural China,” Journal of Regional Science, volume 66, issue
    2, pages 542–562; first published 2026-01-06.
  url: https://doi.org/10.1111/jors.70045
  date: '2026-01-06'
  supports:
  - identity.instrument
  - timeline.last_verified
  - design_applications.paper
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
  verification_status: verified
  access_level: metadata
  locator: Wiley Online Library article record and DOI landing page; used for publication identity and date, not for the article's detailed design claims.
- id: E3
  source_type: policy-document
  citation: >
    Ministry of Transport of the People's Republic of China, Rural Road
    Construction and Management Measures, Order No. 4 of 2018, published
    2018-04-08 and effective 2018-06-01.
  url: https://xxgk.mot.gov.cn/jigou/fgs/202006/t20200623_3307957.html
  date: '2018-06-01'
  supports:
  - identity.authority
  - identity.implementation_regime
  - timeline.effective
  - assignment.rule
  - assignment.compliance
  verification_status: verified
  access_level: official-document
  locator: >
    Articles 2–5 define county, township, and village roads and allocate
    responsibilities across county, township, and village levels; Articles
    11–15 describe locally prepared plans, project pools, annual plans, and
    finance. Effective 2018-06-01. This source documents the late-period legal
    framework only; it does not supply village-specific 1995–2018 construction
    dates or a randomized assignment rule.
- id: E4
  source_type: other
  citation: >
    Xiamen University Economics Data Catalog, “China Road Data” (中国道路数据),
    describing the CAS Resource and Environmental Science Data Center road
    vector maps and application-based access.
  url: https://econpub.xmu.edu.cn/elib/db_detail/16/
  date: null
  supports:
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: dataset
  locator: >
    Catalogue entry lists 1995, 2012, 2016, and 2018 vector shapefiles, their
    road categories and the Chinese Academy of Sciences data provider; the
    access field directs researchers to submit an application. It is an access
    catalogue, not the original data provider or a substitute for the separate
    data-asset project.
design_applications:
- paper: >
    Chen, Wei; Chen, Junliang; Qiu, Huanguang; Yu, Jialing; Chen, Wei; and
    Wang, Xinyue. “Roads to Growth: Evidence From Rural China.”
  doi: 10.1111/jors.70045
  journal: Journal of Regional Science 66(2), 542–562
  year: 2026
  research_question: >
    How did long-run rural-road accessibility changes affect local economic
    activity in mainland Chinese villages, and did effects vary by initial
    development, market distance, and road class?
  population: 387,667 mainland rural villages in the 1995/2018 endpoint sample, after stated exclusions
  outcome: >
    Mean PANDA-China nighttime-light digital number in 1-km village-centered
    buffers; the paper uses prefecture-level GDP and agricultural-GDP
    relationships to translate light changes, while village GDP is unavailable.
  data_used:
  - 1995 and 2018 RESDC paved-road vector maps with all road classes
  - 2021 National Bureau of Statistics village statistical code list and village committee coordinates
  - PANDA-China nighttime-light data for 1995 and 2018
  - NASADEM terrain, precipitation, temperature, county/prefecture centers, and village population-density measures
  - Sino Maps Press 1962 road-network map for the historical-road instrument
  treatment_encoding: >
    Change in minimum distance from the village point to paved roads, coded as
    2018 minus 1995 in the paper; lower values mean closer road access. The main
    network measure includes national, provincial, county, and township roads.
    Alternative specifications use buffer road-density or network travel-time
    changes; road-class analyses are distinct encodings.
  comparison: >
    Continuous cross-village differences in 1995–2018 access change, conditional
    on county fixed effects, changes in climate, and distances to county and
    prefecture centers; this is not a binary NVRCP-treated/control comparison.
  empirical_design: >
    Two-date long-difference OLS and 2SLS. The paper instruments road-access
    change with distance to historical 1962 roads and village-exterior ring
    averages of slope, ruggedness, and elevation; its reported first-stage
    statistics are strong, while its overidentification tests vary and reject
    the full instrument set.
  assumptions:
  - Historical-road distance has no direct effect on village outcome growth after the paper's controls and county fixed effects.
  - Off-village terrain-ring measures affect growth only through their influence on road construction after controls.
  - The two endpoint differences and included county effects address the relevant unobserved trends and policy overlap.
  threats_addressed:
  - The authors discuss endogenous targeting of roads to lagging villages and report a 2SLS strategy.
  - They check alternative road-access measures, buffer radii, night-light settlement areas, and migration-related light concerns.
  - These checks do not resolve every historical-road or terrain exclusion concern; Table 6's Hansen J results should be reported.
  evidence_refs:
  - E1
  - E2
method_transfer: null
readiness_blockers: []
superseded_by: null
deprecation_reason: null
---

## Institutional Background

China's road network expanded at several levels during the period studied. Chen et al. describe the National Village Road Connectivity Project as beginning around the start of the 2000s and report a separate 2006 Ministry of Transport investment plan [E1]. These initiatives form the setting for a broad change in village access; they do not supply one common village eligibility list, assignment year, or road-construction cohort. The Ministry's 2018 regulation recognizes county, township, and village roads and assigns planning and management responsibilities across local levels [E3]. Because that rule took effect in the final sample year, it clarifies the road categories and late-period governance context but should not be projected backward as the governing rule for every year since 1995.

The useful research object is therefore the changing network access itself. It speaks to rural development and regional market access, but it is not interchangeable with the National Trunk Highway System case: Faber's NTHS design studies county proximity to selected trunk-road segments and uses simulated network instruments, whereas this study measures the nearest paved-road distance around village points across all four road classes [E1; related record: `china-highway-network-expansion`].

## What Changed

The authors compare village access in 1995 and 2018. Their main measure is the change in minimum distance from each village point to paved roads. They use all road classes—national, provincial, county, and township—to keep the network intact when rural roads are upgraded or reclassified; township roads nevertheless become the nearest road for a larger share of sampled villages by 2018 [E1]. Thus, “more treated” means a larger realized improvement in access, not receipt of an identical road grant or designation.

The paper's long-difference window overlaps the NVRCP period and multiple phases of public road investment. It does not isolate the effect of the NVRCP from other road building, and its main variable is not an indicator for that program. Keeping this distinction prevents a useful exposure measure from being misremembered as a clean policy rollout.

## Implementation and Assignment

The sample is built from village committee coordinates in the 2021 National Bureau of Statistics code list, using village-centered buffers because historical village-boundary polygons are unavailable. The preferred specification uses 1-km-radius buffers and a final sample of 387,667 rural villages; the paper reports excluding offshore villages and records with missing or outlying values [E1]. It compares continuous differences in access change across villages, conditional on county fixed effects, measured climate changes, and distances to county and prefecture centers.

Road placement was not random. Local needs and policy priorities can affect where roads are built, and the authors report evidence consistent with more investment reaching less-developed villages [E1]. Their 2SLS design instruments the road-access change with distance to the 1962 road network and terrain measures averaged in rings outside the village buffer. The paper argues that these features predict subsequent construction; that is the authors' identification argument, not a property guaranteed by the historical or geographic variables themselves. The 2018 regulation confirms that road plans and annual projects involve local governments, but it does not provide the study's village-specific construction roster [E3].

## Why This Creates Empirical Variation

The case offers a continuous, fine-geography measure of realized road-access change over a long period, paired with village-scale economic-activity proxies. It can support questions about local market access, rural growth, infrastructure spillovers, and differences by initial development. The study's two snapshots do not support an annual event study or a staggered-adoption model unless a researcher separately reconstructs yearly routes and opening dates.

The IV should be treated as a conditional design rather than a ready-made stamp of exogeneity. The paper reports first-stage Kleibergen–Paap statistics above 100, but Table 6's Hansen J results vary across instrument sets and the all-instrument specification rejects the overidentifying restrictions (p=0.000) [E1]. This matters because terrain can affect village outcomes directly and historical corridors may proxy for persistent market access. A strong first stage answers relevance, not exclusion.

## Identification Risks

First, road investments respond to local development conditions and may target places experiencing adverse shocks. The paper itself discusses this feedback and reports that lower-growth villages received more road investment [E1]. Second, the exclusion of historical-road distance and off-village terrain from village outcome growth is contestable even after county effects and controls. The reported overidentification tests should travel with any use of the paper's IV estimates rather than being reduced to a generic claim that geography solves endogeneity [E1].

Third, the outcome is nighttime light, not village GDP. The authors calibrate the relationship between light and GDP at the prefecture level, then use that elasticity to express their village estimate in annual GDP-growth terms; that translation is useful as the paper's interpretation but is not direct village-account measurement [E1]. Fourth, the 2021 point list and fixed-radius buffers are practical measurement choices, not historical village boundaries. Migration, remittances, nearby-road spillovers, changing settlement locations, map classification, and the simultaneous expansion of multiple road tiers can all affect interpretation. These conditions make the record suitable for a carefully matched design, not for an unqualified national causal claim.

## Data Requirements

Replication needs the 1995 and 2018 road geometries with road classes, village codes and coordinates, nighttime-light rasters, county crosswalks, and the controls used in the paper. The paper attributes its road maps to CAS's Resource and Environmental Science Data Center; Xiamen University's catalogue lists the 1995/2012/2016/2018 shapefiles and says access is by application [E4]. The article uses the 2021 NBS list for coordinates, PANDA-China lights, NASADEM and ring-based terrain measures for the IV, alongside climate and market-center data [E1]. These are requirements for reproducing the study's design; actual data acquisition and licensing belong in the companion data-asset project.

For an alternative annual or policy-cohort study, the two endpoint maps are insufficient. A researcher would need dated road segments, opening or upgrading dates, historical road-class crosswalks, and time-consistent village geography. Do not interpolate annual treatment dates from the 1995 and 2018 snapshots.

## Evidence Notes

The full published article was inspected as author content uploaded by coauthor Junliang Chen; its PDF carries Wiley journal pagination and the publisher's open-access notice [E1]. The Wiley DOI record independently verifies title, journal, volume, pages, and first-publication date [E2]. The Ministry's 2018 regulation is a primary source for road categories and local responsibilities as of its effective date, not for the paper's full historical rollout [E3]. Xiamen University's data catalogue documents the listed road-map vintages, provider, and application route; it is an access catalogue rather than the original data repository [E4]. Task `task-c70ab772c9d8` reviewed the record against the direct-matching standard: the paper-used treatment, comparison, data contract, and threats are reconstructable, so the record is design-documented. This maturity classification does not validate the IV exclusions; the causal interpretation remains conditional on those assumptions.
