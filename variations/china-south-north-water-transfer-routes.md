---
schema_version: 2
id: china-south-north-water-transfer-routes
name: China's South-to-North Water Transfer First-Phase Routes and County Exposure
aliases:
- South-North Water Diversion Project county exposure
- SNWT middle-line and east-line treatment
- 中国南水北调东中线一期工程
status: grounded
provenance:
  task_id: task-e6f648e1ff1b
scope:
  country: China
  regions:
  - Chinese counties, villages, and households in the first-phase east-line and middle-line water demand and water supply areas
  domains:
  - regional-economics
  - urban
  - rural-development
  - infrastructure
  - environmental-economics
  - water-resources
  - migration
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    The first phase of China's South-to-North Water Transfer project changed
    water access in mapped receiving counties and imposed distinct water-supply
    and land-use constraints in mapped source counties. Its two routes began
    operating at different times and create a place-based infrastructure
    exposure with both rural and urban consequences.
identity:
  instrument: >
    The first-phase east and middle routes of China's South-to-North Water
    Transfer (SNWT) project: a centrally planned, cross-provincial system that
    transfers water from the Yangtze basin toward water-deficient northern
    regions. The west route and later expansion plans are outside this record.
  authority: >
    The State Council approved the overall plan and the central government
    planned, financed, and coordinated the first-phase project through the
    National Development and Reform Commission, Ministry of Water Resources,
    and the State Council South-to-North Water Transfer construction bodies.
    County and provincial governments implemented supporting works, water
    protection, resettlement, and local supply arrangements.
  legal_identifiers:
  - State Council approval of the South-to-North Water Transfer Overall Plan on 2002-12-23
  - First-phase east-line and middle-line project construction and operation
  - State Council Regulation on South-to-North Water Transfer Water Supply and Use (国务院令第647号, 2014-02-16)
  implementation_regime: >
    The first phase consisted of two routes with different engineering
    approaches. The east line connected existing rivers and lakes with pumping
    stations and began operation before the middle line; the middle line raised
    Danjiangkou Dam, expanded the reservoir, and used newly built gravity-fed
    channels and culverts. Official project documents delineate water demand and
    water supply areas by administrative unit. Local supporting works, source
    protection, relocation, and water-quality restrictions are part of exposure,
    not interchangeable national treatment dates.
  assignment_mechanism: >
    Central route planning and least-cost engineering determined which mapped
    counties were designated to receive transferred water and which source-area
    counties supplied or protected water for a route. The published application
    uses the official demand/supply-area map and a nearby spatial comparison; it
    excludes the Beijing-Tianjin-Hebei target region from the baseline because
    target status could bring other changes. Assignment is geographically
    structured, not randomized.
  parent: null
  related_variations: []
timeline:
  announcement: '2002-12-23'
  effective: null
  implementation_start: 2002
  implementation_end: null
  local_timing: >
    The overall plan was approved in December 2002. The east line is reported
    as operating in 2013 or 2014 depending on whether formal operation or the
    study's post-year convention is used; the middle line formally opened in
    December 2014 and is coded as 2015 in the paper's annual panel. The two
    route-specific operation clocks must remain separate in replication work.
    The paper's appendix lists 20 east-line demand prefectures and 18 middle-line
    demand prefectures; the county-level treatment and source-area boundaries
    come from the official project map and yearbook.
  anticipation: >
    Construction, reservoir expansion, resettlement, pollution control, local
    supporting works, and water-quality restrictions preceded operation. The
    source-area middle-line reservoir expansion also flooded cropland and was
    accompanied by government-directed or incentivized migration in some places.
    Operation dates are therefore treatment-onset conventions, not the first
    local response.
  last_verified: '2026-08-11'
assignment:
  unit: >
    County-year is the main treatment unit; village-year and household-year
    applications inherit treatment from the mapped county or village location.
    Demand-area and supply-area exposure, and east-line versus middle-line
    exposure, are separate states within the first-phase project.
  treated: >
    A county is treated when the official first-phase map places it in a water
    demand area receiving transferred water or a water supply area supplying or
    protecting water for a route. The published baseline contains 287 treated
    demand counties and 139 treated supply counties; the paper's treatment
    indicator is interacted with the relevant east-line or middle-line operation
    year.
  comparison_pool: >
    The main control pool contains geographically nearby counties within a
    300-kilometer buffer around the treated group: 595 controls for demand-area
    analyses and 755 for supply-area analyses. Counties in the opposite
    demand/supply group and the Beijing-Tianjin-Hebei target region are excluded
    from the corresponding baseline pool. Nearby controls can still share
    hydrological, transport, policy, or labor-market exposure.
  rule: >
    Digitize the official demand and supply map, join its administrative units
    to stable county identifiers, retain the route designation, and interact the
    mapped treatment state with the east-line or middle-line operation year.
    Do not substitute a county's distance to a canal, water coverage, GDP, or
    later supporting project for the administrative treatment rule.
  intensity: >
    Route, demand-versus-supply status, distance to the trunk or branch line,
    and delivered-water capacity can describe intensity. The paper's core
    estimand uses a binary mapped-area treatment and route-specific post period;
    water volume and distance measures are secondary, not the canonical rule.
  exemptions:
  - Counties outside the official first-phase demand and supply areas
  - Beijing, Tianjin, and Hebei target-area counties excluded from the baseline inconsequential-unit sample
  - Counties in the opposite treatment group when estimating demand or supply effects separately
  - West-route and post-first-phase expansion areas
  compliance: >
    A mapped demand county is designated to receive project water, but actual
    delivery depends on trunk/branch completion, local supporting works, water
    allocation, and timing. A mapped source county is exposed to extraction,
    reservoir or water-quality constraints, but the exact burden varies by route
    and local implementation.
  exposure_construction: >
    Join the official project map and construction-yearbook administrative list
    to county centroids for county panels and to village coordinates for village
    and household panels. Keep the demand/supply direction, route, operation
    year, and BTH exclusion flag as separate fields; audit historical county
    boundaries before joining outcomes.
  required_identifiers:
  - stable county identifier and historical county crosswalk
  - prefecture and province identifier
  - village coordinates or stable village identifier for microdata
  - household identifier where panel data permit
  - route and demand/supply designation
  - operation year and outcome year
  spillovers: >
    Water flows, canals, pumping, source-area restrictions, migration, remittances,
    rural demand, and urban expansion cross county boundaries. The paper also
    treats the rural-urban fringe as a spatial spillover margin; nearby control
    counties and cities may not be unaffected.
research_compatibility:
  outcome_domains:
  - surface-water coverage and water availability
  - county GDP and agricultural/non-agricultural production
  - crop yields, irrigation, fertilizer, machinery, and cultivated land
  - rural household income, consumption, savings, and productive assets
  - village labor composition, non-farm work, and migration
  - urban boundaries, night lights, population density, and rural-urban fringe growth
  affected_populations:
  - Residents and firms in mapped water demand and supply counties
  - Rural households and villages along the first-phase routes
  - Agricultural workers, migrants, and nearby urban populations
  mechanism_channels:
  - water-supply relaxation and agricultural intensification
  - source-area water-quality and land-use restrictions
  - rural income and local demand effects on nearby cities
  - rural-to-urban and non-farm labor reallocation
  - route-specific engineering, reservoir expansion, and displacement
  best_for:
  - County or village panels linking official route exposure to rural and urban outcomes
  - Comparing receiving-area benefits with source-area costs
  - Spatially explicit urban expansion and rural-urban fringe responses
  - Distinguishing dam-based middle-line effects from network-based east-line effects
  not_good_for:
  - Treating the entire north as exposed at one national date
  - Claiming random assignment or ignoring BTH target status
  - Mixing source-area restrictions with receiving-area water benefits
  - Using an unverified map or current administrative boundaries as the treatment key
design:
  claim_type: causal
  affordances:
  - Centrally coordinated infrastructure with route-specific operation dates
  - Officially mapped receiving and source administrative units
  - Nearby spatial comparisons and an inconsequential-unit sample excluding the main target region
  - County, village, household, and urban-fringe outcomes
  - Middle-line versus east-line engineering heterogeneity
  candidate_designs:
  - County fixed-effects DID with route-specific operation post periods
  - Event study of county, village, or household outcomes around operation
  - Demand-area versus nearby controls and supply-area versus nearby controls estimated separately
  - Province-by-year fixed effects and spatially clustered inference
  - Route heterogeneity comparing the dam-based middle line with the network-based east line
  identifying_variation: >
    The identifying contrast is the difference between mapped demand or supply
    counties and nearby non-mapped counties before and after the route's
    operation, conditional on unit and year effects, geography, weather, and
    trend controls. Its plausibility comes from route engineering and least-cost
    geography plus the paper's exclusion of the BTH target region, not from
    random assignment.
  primary_strategy: >
    The JUE application estimates DID and event-study models with county,
    village, or household fixed effects and year effects. It uses a 300-km
    nearby control buffer, excludes BTH and the opposite demand/supply group,
    interacts time-invariant geography and demographics with trends, controls
    flexible weather, and checks Callaway-Sant'Anna estimates, province-by-year
    effects, alternative buffers, propensity-score controls, and spatially
    clustered standard errors.
  estimand: >
    The short-run effect of first-phase SNWT operation on a county, village, or
    household in a mapped water demand or supply area relative to the specified
    nearby comparison, with separate estimands for receiving-area benefits,
    source-area costs, and route-specific engineering effects.
  treatment_variable: >
    Mapped demand-area or supply-area indicator multiplied by the relevant
    east-line or middle-line post-operation indicator. Route and direction must
    remain explicit; surface-water coverage or GDP is an outcome, not treatment.
  comparison_logic: >
    Compare nearby mapped and non-mapped counties within direction-specific
    samples, check pre-trends, and absorb geography, demographics, weather, and
    province-year shocks. Exclude or separately model BTH, opposite treatment
    areas, source-area displacement, and hydrologically connected neighbors.
  estimation_notes: >
    The paper reports positive water, agricultural, and urban-fringe effects in
    demand areas and agricultural losses with non-farm reallocation in supply
    areas, especially for the middle line. These are source-reported estimates;
    this record preserves the design and its limits rather than independently
    re-estimating them.
  assumptions:
  - Conditional on controls and fixed effects, nearby mapped and non-mapped units would have followed comparable trends without operation
  - Official map assignment and route-specific operation dates are measured correctly
  - Excluding BTH removes the main non-water target shock rather than creating a new selected sample
  - Supporting works, resettlement, water-quality enforcement, and migration are measured or interpreted as part of the treatment package
  - Spatial and hydrological spillovers do not invalidate the selected comparison
  diagnostics:
  - Reconstruct the official demand/supply prefecture and county list from the construction yearbook and map
  - Plot event-study leads and test alternative operation-year conventions
  - Replicate 300-km, 200-km, adjacent-county, river-neighbor, and propensity-score control pools
  - Add province-by-year effects and two-way or Conley spatial clustering
  - Separate east and middle lines and demand versus supply direction
  - Exclude counties affected by reservoir flooding, relocation, or major concurrent water projects
threats:
- type: targeted_region_and_route_selection
  basis: reported
  condition: The project was designed to address water scarcity in the Beijing-Tianjin-Hebei region and other strategic areas; route placement may correlate with future growth or public investment.
  evidence_refs:
  - E1
  - E3
  possible_diagnostics:
  - Exclude BTH as in the paper and report its separate estimates
  - Pre-trend tests and controls for baseline geography, population, and development
  - Compare alternative nearby control pools and route-specific samples
- type: least_cost_geography_and_nonrandom_assignment
  basis: reported
  condition: Least-cost engineering is geographically structured by terrain, hydrology, existing waterways, and water scarcity; those factors may directly predict outcomes.
  evidence_refs:
  - E3
  - E4
  possible_diagnostics:
  - Geography-by-time trends and province-by-year fixed effects
  - Terrain, land area, population density, weather, and baseline water controls
  - Falsification on pre-operation years and alternative route buffers
- type: anticipation_construction_and_resettlement
  basis: documented
  condition: Construction, reservoir expansion, compensation, resettlement, pollution control, and supporting works precede operation and may affect outcomes directly.
  evidence_refs:
  - E2
  - E3
  possible_diagnostics:
  - Alternative treatment onset dates and construction/inspection windows
  - Exclude or separately model flooded and relocated areas
  - Control for supporting infrastructure and water-quality enforcement
- type: source_area_government_intervention
  basis: reported
  condition: Middle-line source areas experienced reservoir expansion, crop flooding, agricultural restrictions, and government-directed or incentivized migration that cannot be cleanly separated from water extraction.
  evidence_refs:
  - E3
  - E6
  possible_diagnostics:
  - Middle versus east line heterogeneity
  - Separate source-area migration, land, and water-quality channels
  - Report the combined infrastructure-and-governance estimand rather than a pure water-volume effect
- type: spatial_hydrological_and_labor_spillovers
  basis: inferred
  condition: Water flows, connected rivers, migration, remittances, and urban demand can affect neighboring counties and contaminate the nearby control pool.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Distance bands, river-network exposure, and commuting or migration links
  - Conley standard errors and adjacent-county exclusions
  - Spatially explicit urban-fringe outcomes
empirical_requirements:
  contract_version: 1
  population: Chinese counties, villages, households, and nearby urban areas in first-phase SNWT demand and supply regions
  observation_unit: County-year, village-year, or household-year
  geography_level: County, prefecture, province, village, and urban-fringe grid with historical boundary crosswalks
  time_start: 2010
  time_end: 2018
  minimum_frequency: Annual panel data
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields:
  - county or village location and stable historical identifier
  - official demand/supply and east/middle route assignment
  - route-specific operation year and treatment post indicator
  - county GDP, agricultural and non-agricultural outcomes, or rural household/village outcomes
  - water coverage, weather, terrain, population, and baseline geography controls
  - urban boundary, night-light, and population-density measures for urban spillovers
  required_identifiers:
  - county_id
  - prefecture_id
  - province_id
  - village_id or village coordinates
  - household_id where panel data permit
  - route_id and demand_supply_status
  - year
  treatment_key:
  - official_project_area_assignment
  - route_id
  - demand_or_supply_status
  - operation_year
  treatment_source: >
    Official South-to-North Water Transfer maps, construction yearbooks, State
    Council/NDRC implementation documents, and the paper's digitized spatial
    projection. The public replication package confirms the analysis files but
    de-identifies its research identifiers; the complete historical crosswalk
    must be rebuilt in the separate data repository.
  measurement_risks:
  - official map and yearbook versions may use different administrative boundaries
  - east-line formal operation and study post-year conventions differ
  - county centroids and village coordinates may misclassify route proximity or area exposure
  - de-identified replication files cannot supply public county or household joins
  - construction, displacement, water-quality, and migration policies are bundled with operation
  - nearby and hydrologically connected controls may be contaminated
design_profiles: []
evidence:
- id: E1
  source_type: policy-document
  citation: 'National Development and Reform Commission. 2002-12-27. “南水北调工程的基本情况” [Basic information on the South-to-North Water Transfer Project].'
  url: https://www.ndrc.gov.cn/xwdt/xwfb/200507/t20050708_958444.html
  date: '2002-12-27'
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.announcement
  - timeline.implementation_start
  - timeline.local_timing
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: 'NDRC official project account: State Council approval and 2002-12-27 opening, three-route plan, east/middle engineering objectives, and designated supply targets.'
- id: E2
  source_type: implementation-document
  citation: 'Ministry of Justice. 2014-02-28. “南水北调工程供用水管理条例” [Regulation on South-to-North Water Transfer Water Supply and Use], State Council Order No. 647.'
  url: https://www.moj.gov.cn/pub/sfbgw/flfggz/flfggzxzfg/201402/t20140228_350601.html
  date: '2014-02-16'
  supports:
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - assignment.compliance
  verification_status: verified
  access_level: official-document
  locator: 'Official administrative-regulation text: east/middle scope, central and local responsibilities for source, along-route, and receiving areas, and water-quality/use rules.'
- id: E3
  source_type: paper
  citation: 'Cui, Xiaomeng, Wangyang Lai, and Tao Lin. 2025. “Long-distance Water Infrastructure, Rural Development and Urban Growth: Evidence from China.” Journal of Urban Economics 146:103736. DOI: 10.1016/j.jue.2025.103736.'
  url: https://www.ccap.pku.edu.cn/docs/2025-12/e269920662404f4ca699a4ac5559ab3a.pdf
  date: 2025
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.exposure_construction
  - assignment.spillovers
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.diagnostics
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_source
  verification_status: reported
  access_level: full-text
  locator: 'Inspectably mirrored article PDF, pp. 1–6 and 12–14: project background, official map construction, route operation years, 287/139 treated and 595/755 control counties, 300-km buffer, BTH exclusion, DID/event study, route heterogeneity, and source-area intervention limits.'
- id: E4
  source_type: appendix
  citation: 'Cui, Xiaomeng, Wangyang Lai, and Tao Lin. 2025. “Appendix Tables and Figures” for Long-distance Water Infrastructure, Rural Development and Urban Growth.'
  url: https://ars.els-cdn.com/content/image/1-s2.0-S0094119025000014-mmc1.pdf
  date: 2025
  supports:
  - assignment.treated
  - assignment.comparison_pool
  - assignment.required_identifiers
  - assignment.exposure_construction
  - design.diagnostics
  - empirical_requirements.required_fields
  locator: 'Publisher supplementary appendix, Table A1 and Tables A2–A7: 20 east-line and 18 middle-line demand prefectures, baseline county/village/household counts and balance checks, and route-specific robustness/heterogeneity.'
  verification_status: reported
  access_level: appendix
- id: E5
  source_type: replication
  citation: 'Cui, Xiaomeng, Wangyang Lai, and Tao Lin. 2025. “Replication Data for: Long-distance Water Infrastructure, Rural Development and Urban Growth: Evidence from China.” Harvard Dataverse, DOI 10.7910/DVN/5XM5WA.'
  url: https://doi.org/10.7910/DVN/5XM5WA
  date: 2025
  supports:
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_source
  - design_applications.data_used
  verification_status: verified
  access_level: replication
  locator: 'Public Dataverse metadata and Read_Me file: replication do-files and de-identified county, village, and household analysis files for demand and supply samples.'
- id: E6
  source_type: implementation-document
  citation: 'National Development and Reform Commission and South-to-North Water Transfer Office. 2013. “丹江口库区及上游地区对口协作工作方案” [Coordination plan for the Danjiangkou Reservoir area and upstream].'
  url: https://www.ndrc.gov.cn/fggz/dqzx/dkzyyhz/201507/t20150715_1083736.html
  date: '2013-03-18'
  supports:
  - identity.assignment_mechanism
  - assignment.compliance
  - assignment.spillovers
  - threats.condition
  verification_status: verified
  access_level: official-document
  locator: 'NDRC implementation plan: source-area/receiving-area relationship, water-quality obligations, ecological and economic restrictions, and interregional coordination.'
- id: E7
  source_type: implementation-document
  citation: 'Chinese Government. 2018-12-12. “南水北调4周年 超1亿人直接受益” [Four years of South-to-North transfer: over 100 million direct beneficiaries].'
  url: https://app.www.gov.cn/govdata/gov/201812/12/432990/article.html
  date: '2018-12-12'
  supports:
  - timeline.local_timing
  - identity.implementation_regime
  verification_status: verified
  access_level: official-document
  locator: 'Central government account dates the 2013 east-line operation and 2014-12-12 middle-line full operation, while the paper codes the annual post periods as 2014 and 2015.'
- id: E8
  source_type: paper
  citation: 'Cui, Xiaomeng, Wangyang Lai, and Tao Lin. 2025. “Long-distance Water Infrastructure, Rural Development and Urban Growth: Evidence from China.” Journal of Urban Economics 146:103736. DOI record.'
  url: https://doi.org/10.1016/j.jue.2025.103736
  date: 2025
  supports:
  - identity.instrument
  - design.identifying_variation
  - design.estimand
  - design_applications.treatment_encoding
  - design_applications.comparison
  - design_applications.data_used
  verification_status: reported
  access_level: metadata
  locator: 'DOI metadata record for the JUE application; full treatment and evidence details are supported by E3 and E4.'
design_applications:
- paper: 'Long-distance Water Infrastructure, Rural Development and Urban Growth: Evidence from China'
  doi: 10.1016/j.jue.2025.103736
  journal: Journal of Urban Economics
  year: 2025
  research_question: How does first-phase long-distance water infrastructure affect water resources, rural development, labor allocation, and nearby urban growth in China's demand and supply areas?
  population: Chinese counties, villages, rural households, and urban-fringe areas observed during 2010–2018
  outcome: Surface water coverage, GDP and sectoral production, agricultural inputs, household income and consumption, labor and migration, urban boundaries, night lights, and population density
  data_used:
  - Digitized official SNWT maps and South-to-North Water Transfer Project Construction Yearbooks
  - County-level China Statistical Yearbook and provincial statistical yearbooks
  - Ministry of Agriculture rural household and village panel survey, 2010–2017
  - Global Urban Boundary, night-light, WorldPop, weather, terrain, and surface-water data
  - Public Dataverse replication files with de-identified county, village, and household analysis data
  treatment_encoding: >
    A mapped demand-area or supply-area indicator is interacted with the relevant
    east-line or middle-line operation post period. The baseline counts are 287
    treated demand counties and 139 treated supply counties, with nearby control
    buffers; demand prefecture names are listed in Appendix Table A1.
  comparison: >
    Nearby counties within 300 km, excluding BTH and the opposite demand/supply
    group for each analysis; alternative buffers, adjacent-county exclusions,
    river-neighbor comparisons, and propensity-score controls are reported.
  empirical_design: County, village, and household DID/event-study models with unit and year fixed effects, geographic and demographic trends, weather controls, and route heterogeneity
  assumptions:
  - Conditional parallel trends hold between mapped areas and nearby controls
  - Least-cost route geography plus the BTH exclusion reduces, but does not remove, selection concerns
  - The map, county centroid/village location, and route operation date are correctly joined
  - Bundled construction, resettlement, water-quality, and migration actions are part of the treatment package
  threats_addressed:
  - Event-study pre-trends and alternative DID estimators
  - Province-by-year fixed effects and flexible weather/geography trends
  - Alternative spatial control groups and clustering strategies
  - Separate demand/supply and east/middle-line estimates
  evidence_refs:
  - E3
  - E4
  - E8
method_transfer: null
readiness_blockers:
- The paper and appendix identify the demand prefectures and county treatment counts, but a machine-readable historical county-level demand/supply crosswalk is not included in the public replication metadata and must be reconstructed from the official map/yearbook.
- East-line formal operation is variously reported as 2013 or 2014, while the paper codes its post period as 2014; middle-line formal opening is 2014-12-12 while the paper codes 2015. Route-specific date conventions must be retained.
- Public replication files are de-identified, so they do not independently solve the county/village/household join for a new dataset.
- The route was centrally targeted and shaped by terrain, hydrology, water scarcity, construction, resettlement, water-quality enforcement, and migration; it is not intrinsically exogenous.
- Source-area agricultural restrictions and government-directed migration are bundled with water extraction, especially along the middle line; a pure water-volume estimand is not identified by the reported application.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

China's South-to-North Water Transfer project was developed after decades of planning to address the uneven distribution of water between the Yangtze basin and water-deficient northern regions. The State Council approved the overall plan in December 2002 and the first construction works began that month [E1]. The first phase implemented an east line and a middle line; the west line and later expansion are outside this record. The 2014 administrative regulation assigns responsibilities across water-source, along-route, and receiving areas and requires water-quality and supply management [E2].

## What Changed

The relevant change is the operation of a mapped first-phase route, not a national “south versus north” indicator. Demand counties were designated to receive transferred water; supply counties were exposed to source-area extraction, reservoir expansion, water-quality protection, and related land or migration constraints. The east line used existing rivers and lakes with pumping, while the middle line raised Danjiangkou Dam and built a new gravity-fed channel system [E1; E3]. These directions and engineering regimes must not be collapsed into one undifferentiated treatment.

## Implementation and Assignment

The official project map and construction yearbooks define the administrative demand and supply areas. The JUE paper reports 287 treated demand counties and 139 treated supply counties, with 595 and 755 nearby controls respectively, and excludes the Beijing–Tianjin–Hebei target region from its baseline [E3; E4]. Its operation clock is route-specific: the paper codes the east line as post-2014 and the middle line as post-2015, while official accounts describe formal operation in 2013 and 2014/2014-12-12 [E3; E7]. A replication should preserve both the institutional date and the paper's coding convention until the exact panel construction is audited.

## Why This Creates Empirical Variation

The design compares nearby mapped counties with counties outside the relevant demand or supply area before and after route operation. It uses county, village, household, and urban-fringe outcomes, and contrasts the dam-based middle line with the network-based east line [E3; E4]. The design's plausibility comes from central planning, route engineering, least-cost geography, event-study checks, and removal of the main target region; it is not a claim of random assignment.

## Identification Risks

Route placement follows hydrology, terrain, water scarcity, existing waterways, and strategic targets that can predict later growth. Construction and preparation precede operation. Middle-line source areas experienced reservoir expansion, flooded cropland, water-quality restrictions, compensation, and government-directed or incentivized migration, so a source-area estimate combines water extraction with a broader intervention package [E3; E6]. Nearby counties can share rivers, labor markets, migration, and urban demand. These risks are why the record keeps demand/supply, route, operation-year, and BTH flags separate.

## Data Requirements

A study needs an official route-area map or list, stable historical county and village identifiers, route-specific operation dates, and annual county, village, or household outcomes. The published application uses county statistics, a Ministry of Agriculture rural panel, remote sensing and weather data, urban boundaries, night lights, and population grids [E3; E5]. The replication package is a pointer to the data asset, not a substitute for a public county crosswalk; acquisition, reconstruction, and access limitations belong in Econ Data Know-How.

## Evidence Notes

E1 is an official NDRC project account and establishes approval, central authority, the three-route plan, and route objectives; it does not provide the paper's final county sample. E2 is the State Council regulation and establishes the formal source/route/receiving governance boundary and water-quality obligations; it does not establish actual local compliance. E3 is the inspectable article PDF and reports the map source, treatment counts, control construction, operation conventions, DID design, data, and mechanisms; it is a source-reported application rather than an independent county-list audit. E4 is the publisher appendix and establishes the demand-prefecture list and sample/balance details; it does not replace the historical county crosswalk. E5 verifies the public replication package and its de-identified files; it does not create public identifiers. E6 documents source-area coordination and restrictions; it does not establish a clean exclusion restriction. E7 is a central-government account of operation milestones and explains the date convention discrepancy; it does not prove each county's actual delivery date. The record is grounded in the institutional instrument and application while leaving the exact crosswalk, date harmonization, and bundled source-area mechanisms explicit.
