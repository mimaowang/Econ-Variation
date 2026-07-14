---
schema_version: 2
id: china-straw-burning-ban
name: China Universal Prohibition on Straw Burning (UPSB) and Crop-Residue Burning Bans
aliases:
- China straw burning ban
- UPSB policy
- crop residue burning regulation China
- 秸秆禁烧
status: extracted
provenance:
  task_id: task-180f2fd6694c
scope:
  country: China
  regions:
  - Major grain-producing provinces and counties (e.g., Heilongjiang, Jilin, Liaoning, Henan, Hebei, Shandong, Anhui, Jiangsu, Hubei, Sichuan)
  domains:
  - environment
  - agriculture
  - public-health
  - pollution
  - climate
  - rural-development
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese agricultural counties and provinces, and supports China-focused empirical research on environmental regulation, agricultural externalities, and public health.
identity:
  instrument: Universal Prohibition on Straw Burning (UPSB) policy and related national and local bans on open-field crop-residue burning, enforced through satellite remote sensing, drone patrols, administrative penalties, and official accountability.
  authority: State Council of China; National Development and Reform Commission (NDRC); Ministry of Agriculture and Rural Affairs (MARA); Ministry of Ecology and Environment (MEE); provincial and municipal people's governments.
  legal_identifiers:
  - 《秸秆禁烧和综合利用管理办法》（环发〔1999〕98号）
  - 《国务院办公厅关于加快推进农作物秸秆综合利用的意见》（国办发〔2008〕105号）
  - 《大气污染防治行动计划》（国发〔2013〕37号）
  - 《关于加强农作物秸秆综合利用和禁烧工作的通知》（发改环资〔2013〕930号）
  - 《关于进一步加快推进农作物秸秆综合利用和禁烧工作的通知》（发改环资〔2015〕2651号）
  - 《打赢蓝天保卫战三年行动计划》（国发〔2018〕22号）
  implementation_regime: A national prohibition on open-field straw burning has existed since 1999; enforcement was intensified from 2013 onward through the Air Pollution Prevention Action Plan and the 2015 NDRC-MARA-MEE-Finance notice, which set quantitative targets, mandated satellite and drone monitoring, and tied local officials' accountability to fire-point counts. The 2018 Blue Sky Defense Action Plan reinforced grid-based supervision and harvest-season inspections.
  assignment_mechanism: Spatial and temporal variation in the intensity of the ban and its enforcement. Treatment can be coded as (i) a county/province-year indicator for the intensified campaign period, (ii) a continuous measure of satellite-detected fire-point density, or (iii) an interaction between a post-campaign indicator and baseline straw production or pre-policy burning intensity in a generalized difference-in-differences design.
  parent: null
  related_variations: []
timeline:
  announcement: 1999-04-16 (first national rules); 2013-09-10 (Air Pollution Prevention Action Plan); 2015-11-16 (intensified NDRC/MARA/MEE/Finance notice); 2018-06-27 (Blue Sky Defense Action Plan)
  effective: 1999 (first rules); 2013 (air-pollution action plan); 2015 (intensified campaign); 2018 (Blue Sky plan)
  implementation_start: 1999
  implementation_end: ongoing
  local_timing: 'Enforcement concentrates in harvest windows: late May-June (wheat) and September-October (corn/rice). Local governments issue seasonal bans and grid-based patrols during these periods.'
  anticipation: Farmers and local officials anticipate harvest-season inspections; in response some burning shifts to night-time, less-monitored parcels, or adjacent jurisdictions.
  last_verified: '2026-07-14'
assignment:
  unit: County-year (or province-year) and harvest season; may also be defined at the grid-cell-day level using satellite fire data.
  treated: Localities and time periods subject to intensified UPSB enforcement, measured by reduced satellite fire points, stricter penalties, publicized fire-point bulletins, or inclusion in the post-2015 campaign period.
  comparison_pool: The same county/province before intensification, and/or localities with lower baseline straw-burning intensity or weaker enforcement, conditional on fixed effects and covariates.
  rule: National and local regulations prohibit open-field burning of crop residues; enforcement intensity varies by region and year and is monitored by satellite fire points.
  intensity: Continuous intensity can be measured by satellite-detected fire-point counts per unit crop area; discrete treatment can be defined as the post-2015 intensified campaign interacted with baseline straw production.
  exemptions: []
  compliance: Incomplete. Despite bans, night burning, small-scale burning, and cross-jurisdiction burning persist, especially in regions with weak monitoring or limited straw-utilization infrastructure.
  exposure_construction: Construct a county-year panel; code treatment as a post-2015 indicator (or continuous fire-point reduction) interacted with baseline straw output or pre-policy burning density; include harvest-season indicators.
  required_identifiers:
  - county/province code
  - year
  - harvest season
  - crop type/area
  spillovers: Air pollution from burning travels downwind to urban areas; bans may shift burning to neighboring counties or substitute toward chemical fertilizers and pesticides, affecting water quality and soil ecosystems.
research_compatibility:
  outcome_domains:
  - air quality
  - agricultural productivity
  - public health
  - water quality
  - chemical input use
  - greenhouse gas emissions
  - rural household behavior
  affected_populations:
  - rural farming households
  - rural and urban populations exposed to harvest-season air pollution
  - local government officials subject to environmental accountability
  mechanism_channels:
  - open-field straw burning
  - particulate matter emissions
  - substitution to chemical fertilizers and pesticides
  - soil pest and nutrient management
  - enforcement and monitoring technology
  - inter-jurisdictional pollution transport
  best_for:
  - Estimating the causal effect of straw-burning bans on fires, air pollution, and agricultural input substitution
  - Studying unintended consequences of command-and-control environmental regulation
  - Designs exploiting staggered local enforcement and satellite fire data
  not_good_for:
  - Effects at the individual farm level without parcel-level compliance data
  - Long-run soil carbon and crop-yield effects without multi-year agronomic panels
  - Settings where open-field burning data are unavailable or unreliable
design:
  affordances:
  - National policy with locally varying enforcement generates staggered treatment timing
  - Satellite-detected fire points provide a high-frequency, spatially explicit treatment/outcome measure
  - Air-quality monitoring stations and agricultural input statistics are publicly available
  - Multiple policy milestones create clear pre/post breaks
  candidate_designs:
  - Generalized difference-in-differences with county/province and time fixed effects
  - Event study around the 2015 intensification and the 2018 Blue Sky reinforcement
  - Spatial regression discontinuity at provincial borders with different enforcement intensity
  - Wind-direction instrument for downstream air-pollution exposure
  - Panel fixed-effects regressions linking fire points to pollution monitors
  identifying_variation: Staggered intensification of enforcement across Chinese counties/provinces and harvest seasons, conditional on baseline straw production and regional air-pollution policies.
  assumptions:
  - 'Parallel trends: in the absence of intensified enforcement, treated and comparison counties would have followed similar trends in fires, pollution, and input use.'
  - No other coincident shocks that disproportionately affect treated counties' pollution or input use during harvest seasons.
  - Enforcement intensity is exogenous to local unobserved determinants of the outcomes, conditional on fixed effects, weather, and other pollution controls.
  - Satellite fire points and air/water quality measures accurately capture burning activity and environmental outcomes.
  diagnostics:
  - Event-study plots to assess pre-trends before the 2015 intensification
  - Robustness to heterogeneous treatment timing estimators (Callaway-Sant'Anna, Sun-Abraham, de Chaisemartin-D'Haultfoeuille)
  - Placebo tests using non-harvest seasons or non-agricultural pollutants
  - Sensitivity to weather controls (temperature, precipitation, wind, humidity)
  - Tests for spatial spillovers and cross-border pollution transport
  - Check for pollution substitution via chemical fertilizer and pesticide use
  - Comparison of results using continuous fire-point intensity versus discrete campaign indicators
  primary_strategy: Generalized difference-in-differences exploiting staggered intensification of the UPSB policy across counties/provinces and harvest seasons.
  estimand: The effect of intensified straw-burning prohibition on agricultural fire density, air pollution, water pollution, and chemical input use in Chinese crop-producing regions.
  treatment_variable: Intensified UPSB enforcement, measured either as a post-campaign indicator interacted with baseline straw production or as satellite-detected fire-point density.
  comparison_logic: Within-county/province changes over time, compared with localities that experienced weaker enforcement or had lower baseline burning intensity.
  estimation_notes: Generalized DID with county/province and time fixed effects; harvest-season and weather controls; robustness to modern staggered-DID estimators and spatial standard errors.
  claim_type: causal
threats:
- type: parallel-trends-violation
  basis: inferred
  condition: Counties targeted for intensified enforcement may have been on different pre-existing trends in pollution or agricultural modernization, violating the parallel-trends assumption.
  evidence_refs:
  - E4
  - E6
  possible_diagnostics:
  - Event-study pre-trend tests
  - Include region-specific linear time trends
  - Match on pre-policy fire-point and pollution trajectories
- type: spillovers
  basis: inferred
  condition: Burning may shift to neighboring counties or to night-time, and air pollution travels downwind, biasing within-county estimates toward zero and creating spatial correlation.
  evidence_refs:
  - E5
  - E6
  possible_diagnostics:
  - Define treatment using buffers around each county
  - Include neighbors' treatment or fire-point measures as controls
  - Cluster or Conley standard errors by spatial distance
  - Use wind-direction IV for downwind exposure
- type: omitted-variable-bias
  basis: inferred
  condition: Other air-pollution policies (coal bans, industrial emission standards, traffic restrictions) were implemented concurrently with the UPSB intensification and may confound estimates.
  evidence_refs:
  - E3
  - E5
  possible_diagnostics:
  - Control for other major pollution policies interacted with baseline industrial structure
  - Restrict to harvest-season windows when straw burning is the dominant source
  - Use pollution species strongly tied to biomass burning (e.g., K+, organic carbon)
- type: measurement-error
  basis: inferred
  condition: Satellite fire points may miss small or short fires, misclassify non-agricultural fires, or vary with cloud cover and satellite overpass timing.
  evidence_refs:
  - E6
  possible_diagnostics:
  - Validate fire points against ground reports where available
  - Use alternative satellite products (MODIS, VIIRS, Himawari)
  - Restrict analysis to clear-sky days and harvest windows
- type: general-equilibrium
  basis: inferred
  condition: Reduced burning may increase chemical fertilizer and pesticide use, creating water-pollution substitution that offsets air-quality benefits.
  evidence_refs:
  - E6
  possible_diagnostics:
  - Estimate effects on fertilizer and pesticide expenditures or application rates
  - Examine water-quality indicators in downstream monitoring stations
  - Cost-benefit analysis incorporating both air and water pathways
empirical_requirements:
  contract_version: 1
  population: Crop-producing counties/provinces in China, with focus on major grain-producing regions and harvest seasons from the early 2000s to the early 2020s.
  observation_unit: County-year-season or grid-cell-day
  geography_level: County or province, within China
  time_start: 2000
  time_end: 2024
  minimum_frequency: annual or seasonal (harvest windows); daily for fire-point and pollution analysis
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields:
  - county/province identifier
  - year and season
  - satellite-detected fire-point counts
  - crop area or straw production
  - air-pollution readings (PM2.5, PM10, AQI)
  - weather variables
  - fertilizer and pesticide use or expenditure (for substitution analysis)
  - water-quality indicators (for water-pollution analysis)
  required_identifiers:
  - county/province code
  - year
  - harvest season
  treatment_key:
  - county/province code
  - year
  - harvest season
  - post-intensification indicator or fire-point intensity
  - baseline straw production/burning intensity
  treatment_source: National and provincial straw-burning regulations, MEE/MARA satellite fire-point monitoring bulletins, and official accountability reports.
  measurement_risks:
  - Satellite fire points may miss small or short-duration fires and are affected by cloud cover.
  - Local enforcement intensity may not be fully captured by official fire-point bulletins.
  - Air-pollution monitors are sparse in rural areas and may not represent farm-level exposure.
  - Fertilizer/pesticide data are often available only at province or county level, not farm level.
evidence:
- id: E1
  source_type: policy-document
  citation: 国家环境保护总局、农业部、财政部等《秸秆禁烧和综合利用管理办法》（环发〔1999〕98号），1999年4月16日。
  url: https://www.gov.cn/gongbao/shuju/1999/gwyb199916.pdf
  date: 1999
  supports:
  - identity
  - timeline
  - assignment
  verification_status: verified
  access_level: official-document
  locator: State Council Gazette PDF, 环发〔1999〕98号
- id: E2
  source_type: policy-document
  citation: 国务院办公厅《关于加快推进农作物秸秆综合利用的意见》（国办发〔2008〕105号），2008年7月27日。
  url: https://www.gov.cn/zwgk/2008-08/01/content_1061158.htm
  date: 2008
  supports:
  - identity
  - timeline
  verification_status: verified
  access_level: official-document
  locator: http://www.gov.cn/zwgk/2008-08/01/content_1061158.htm
- id: E3
  source_type: policy-document
  citation: 国务院《大气污染防治行动计划》（国发〔2013〕37号），2013年9月10日。
  url: https://www.gov.cn/zhengce/content/2013-09/13/content_4561.htm
  date: 2013
  supports:
  - timeline
  - assignment
  verification_status: verified
  access_level: official-document
  locator: http://www.gov.cn/zhengce/content/2013-09/13/content_4561.htm
- id: E4
  source_type: implementation-document
  citation: 国家发展改革委、财政部、农业部、环境保护部《关于进一步加快推进农作物秸秆综合利用和禁烧工作的通知》（发改环资〔2015〕2651号），2015年11月16日。
  url: https://www.ndrc.gov.cn/xxgk/zcfb/tz/201511/t20151125_963505.html
  date: 2015
  supports:
  - identity
  - timeline
  - assignment
  verification_status: verified
  access_level: official-document
  locator: http://www.ndrc.gov.cn/xxgk/zcfb/tz/201511/t20151125_963505.html
- id: E5
  source_type: policy-document
  citation: 国务院《打赢蓝天保卫战三年行动计划》（国发〔2018〕22号），2018年6月27日。
  url: https://www.gov.cn/zhengce/content/2018-07/03/content_5303158.htm
  date: 2018
  supports:
  - timeline
  - assignment
  verification_status: verified
  access_level: official-document
  locator: http://www.gov.cn/zhengce/content/2018-07/03/content_5303158.htm
- id: E6
  source_type: paper
  citation: 'Hong, Hai, and Kevin Z. Chen. 2026. "When the fire ends: Straw burning, regulation, and pollution substitution." Journal of Development Economics 181: 103727.'
  url: https://doi.org/10.1016/j.jdeveco.2026.103727
  date: 2026
  supports:
  - design
  - design_applications
  - threats
  - empirical_requirements
  verification_status: verified
  access_level: abstract
  locator: DOI 10.1016/j.jdeveco.2026.103727
design_applications:
- paper: 'When the fire ends: Straw burning, regulation, and pollution substitution'
  doi: 10.1016/j.jdeveco.2026.103727
  journal: Journal of Development Economics
  year: 2026
  research_question: What are the effects of China's Universal Prohibition on Straw Burning (UPSB) policy on agricultural fires, air pollution, and unintended water pollution through chemical input substitution?
  population: Chinese crop-producing counties/provinces, primarily during the 2012-2020 period.
  outcome: Satellite-detected agricultural fire counts; air pollution (PM2.5, PM10, AQI); water pollution proxies; chemical fertilizer and pesticide use; cost-benefit estimates.
  data_used:
  - Satellite fire-point data (e.g., MODIS/VIIRS thermal anomalies)
  - Ground-level air-quality monitoring station readings
  - Agricultural input statistics (chemical fertilizer and pesticide use)
  - Water-quality monitoring data
  - Weather data (temperature, precipitation, wind, humidity)
  - Crop area and straw production statistics
  treatment_encoding: Intensified UPSB enforcement, measured either as a post-2015 campaign indicator interacted with baseline straw-burning intensity or as satellite-detected fire-point density.
  comparison: Generalized difference-in-differences comparing localities and harvest seasons before and after intensified enforcement, with unit and time fixed effects.
  empirical_design: Generalized difference-in-differences exploiting staggered intensification of top-down campaign-style enforcement.
  assumptions:
  - Parallel trends in the absence of intensified enforcement
  - No coincident shocks confounding harvest-season pollution
  - Enforcement intensity is exogenous conditional on controls
  - Accurate measurement of fires, pollution, and inputs
  threats_addressed:
  - Pre-trends via event-study plots
  - Heterogeneous treatment timing via robust estimators
  - Placebo and weather-robustness checks
  - Pollution-substitution analysis
  evidence_refs:
  - E6
readiness_blockers:
- Exact county-level rollout dates and the paper-level treatment coding used in Hong & Chen (2026) need verification from the full text or replication package.
- Downwind air-pollution spillovers and spatial correlation across counties need explicit modeling and robust standard errors.
- The specific sources and construction of water-pollution and chemical-input variables in the JDE paper need to be documented.
method_transfer: null
---
---
## Institutional Background

Open-field burning of crop residues has long been common in China as a low-cost way to clear fields, control pests, and return some nutrients to the soil. Since 1999 the central government has prohibited such burning through the *Measures for the Prohibition of Straw Burning and Comprehensive Utilization* (E1). The 2008 State Council opinion expanded the policy frame from simple bans toward comprehensive utilization and provided the first national targets (E2). The 2013 *Air Pollution Prevention Action Plan* and the 2015 NDRC-MARA-MEE-Finance notice (E3, E4) intensified enforcement by linking local officials' accountability to satellite-detected fire points, mandating drone and grid patrols, and setting quantitative targets (85% comprehensive utilization by 2020; fire points/burned area down 5% from 2016). The 2018 *Blue Sky Defense Action Plan* reinforced harvest-season grid supervision and extended the framework to the Yangtze River Delta and other key regions (E5). [E1; E2; E3; E4; E5]

## What Changed

The UPSB policy shifted from a largely nominal ban to a campaign-style enforcement regime. Local governments became directly accountable for fire-point counts, and penalties for burning increased. The policy also expanded subsidies and technical support for straw return, fodder, energy, and industrial uses. These changes created variation in effective treatment across provinces, counties, and harvest seasons. [E4; E5]

## Implementation and Assignment

Assignment is determined by the interaction of national legal milestones and local enforcement capacity. A clean empirical design treats counties/provinces as treated once they enter the intensified enforcement period (post-2015, with additional reinforcement in 2018), with treatment intensity proxied by the reduction in satellite-detected fire points or by baseline straw production. Because enforcement is seasonal, the relevant comparison is typically within county and harvest window over time. [E4; E6]

## Why This Creates Empirical Variation

The staggered intensification of enforcement generates a classic staggered difference-in-differences: some regions began strict enforcement earlier or more aggressively than others, and fire-point density changed discontinuously around national campaign milestones. Satellite fire data provide a high-frequency, spatially resolved measure of both treatment and outcome, while air-quality monitors and agricultural input statistics allow researchers to trace pollution and substitution effects. [E4; E5; E6]

## Identification Risks

The main risks are (i) violation of parallel trends if targeted counties were already modernizing faster; (ii) spatial spillovers, including downwind pollution and burning displaced to neighboring jurisdictions; (iii) concurrent air-pollution policies that affect the same outcomes; and (iv) imperfect measurement of small or concealed fires. The JDE paper also highlights pollution substitution: reduced burning may increase fertilizer and pesticide use, raising water pollution. [E3; E5; E6]

## Data Requirements

The design requires county- or province-level panels of satellite fire points, crop area/straw production, air-quality monitor readings, weather variables, and—if studying substitution—chemical fertilizer and pesticide use or water-quality data. Administrative records on local enforcement actions and penalties strengthen identification. [E4; E6]

## Evidence Notes

Primary institutional grounding comes from the 1999 national ban, the 2008 State Council opinion, the 2013 Air Pollution Prevention Action Plan, the 2015 four-ministry notice, and the 2018 Blue Sky Defense Action Plan (E1–E5). The empirical design is drawn from Hong & Chen (2026, *Journal of Development Economics*), which uses a generalized DID and reports significant reductions in fires and air pollution but increased water pollution through input substitution (E6). [E1; E2; E3; E4; E5; E6]
