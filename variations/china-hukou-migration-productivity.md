---
schema_version: 2
id: china-hukou-migration-productivity
name: Internal Migration Barriers (Hukou) and Aggregate Productivity in China (2000–2005)
aliases:
- Tombe-Zhu hukou trade migration
- internal migration costs China
- 户籍迁移生产率

status: contested
provenance:
  task_id: task-e9b64f33e231
scope:
  country: China
  regions:
  - All provinces
  - 30 regions
  domains:
  - migration
  - trade
  - productivity
  - labor
  - regional-development
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: Variation in internal trade and migration costs across Chinese provinces and over time, driven by institutional
    barriers (hukou system) and geographic factors
  authority: Chinese central government, provincial governments (hukou administration), Ministry of Commerce
  legal_identifiers:
  - Hukou registration system
  - provincial migration regulations
  - interprovincial trade policies
  implementation_regime: Migration costs are determined by hukou-based restrictions on access to public services (education,
    healthcare, housing) in destination provinces; trade costs are determined by provincial border effects, transport infrastructure,
    and local protectionism
  assignment_mechanism: Migration and trade costs vary by province-pair and over time, determined by institutional and geographic
    factors largely exogenous to individual worker productivity
  parent: null
  related_variations:
  - china-trade-migration-productivity
timeline:
  announcement: null
  effective: null
  implementation_start: 2000
  implementation_end: 2005
  local_timing: Migration costs declined unevenly across provinces during 2000–2005, with some provinces implementing hukou
    reforms earlier than others
  anticipation: The gradual nature of hukou reform meant that migration cost reductions were partially anticipated
  last_verified: '2026-07-13'
assignment:
  unit: Worker (rural-urban migrant) and province-pair trade flow
  treated: Workers in provinces or sectors with lower migration barriers; regions with lower trade costs
  comparison_pool: Workers in provinces with higher migration barriers; regions with higher trade costs
  rule: A worker faces migration costs determined by the province-pair origin-destination barriers; trade costs vary by province-pair
    and sector
  intensity: Migration costs expressed in consumption-equivalent units; estimated to decline 18% on average from 2000–2005
  exemptions: []
  compliance: Some migration occurs even with high barriers through informal channels; compliance is embedded in the estimated
    cost parameters
  exposure_construction: Estimated migration costs from a structural model calibrated to province-level migration flows and
    wage differentials; trade costs inferred from observed trade flows and price differentials
  required_identifiers:
  - province code (origin and destination)
  - year
  - sector
  - migration flow
  - trade flow
  - wage differentials
  spillovers: Reductions in migration costs in one province affect labor supply and wages in connected provinces through migration
    flows
research_compatibility:
  outcome_domains:
  - productivity
  - wages
  - migration flows
  - internal trade
  - regional specialization
  - welfare
  affected_populations:
  - rural-urban migrants
  - urban workers
  - farmers
  - manufacturing workers
  - service sector workers
  mechanism_channels:
  - labor reallocation across sectors
  - labor reallocation across regions
  - trade integration
  - specialization
  best_for:
  - Studying the aggregate effects of internal migration barriers
  - hukou reform counterfactuals
  - trade-migration interactions
  not_good_for:
  - Individual-level migration decisions
  - short-run dynamics of adjustment
  - outcomes requiring annual variation in migration costs
design:
  affordances:
  - Quantitative general equilibrium model calibrated to China
  - province-pair variation in trade and migration costs
  - observed changes over 2000–2005
  - counterfactual policy simulations
  candidate_designs:
  - Quantitative spatial equilibrium model
  - structural estimation of migration costs
  - counterfactual welfare analysis
  identifying_variation: Variation in trade and migration costs across province-pairs and over time, estimated from observable
    trade and migration flows using a structural model
  assumptions:
  - Model structure (constant elasticity substitution preferences
  - iceberg trade costs
  - exogenous productivity) accurately captures the economy
  - migration costs are stable within each year
  - parameters are identified from observed flows
  diagnostics:
  - Model fit tests comparing predicted and observed flows
  - sensitivity analysis to elasticity parameters
  - validation with auxiliary data on hukou reforms
  primary_strategy: Quantitative general equilibrium model with internal and international trade, and migration across sectors
    and regions
  estimand: The causal effect of the recorded exposure on Aggregate labor productivity, welfare, sectoral employment shares,
    conditional on the stated design assumptions.
  treatment_variable: Estimated province-pair migration costs and trade costs from a structural model
  comparison_logic: Counterfactual scenarios where trade/migration costs are reduced to different levels
  estimation_notes: Quantitative general equilibrium model with internal and international trade, and migration across sectors
    and regions
threats:
- type: model-dependence
  basis: inferred
  condition: The quantitative results depend on functional form assumptions (CES, iceberg costs) and key elasticity parameters
    that may not be precisely estimated
  evidence_refs:
  - E1
  possible_diagnostics:
  - Sensitivity analysis across a range of parameter values
  - comparison with reduced-form estimates
  - out-of-sample validation
- type: endogenous-policy
  basis: inferred
  condition: The decline in migration costs between 2000 and 2005 may be partly endogenous to economic conditions (e.g., high-growth
    provinces relaxed hukou restrictions)
  evidence_refs:
  - E1
  possible_diagnostics:
  - Compare results using only variation in geographic determinants of trade costs
  - use instrumental variables for policy reforms
- type: measurement-error
  basis: inferred
  condition: Migration flows from census and survey data may undercount temporary migrants and those without official registration
  evidence_refs:
  - E1
  possible_diagnostics:
  - Cross-check with alternative data sources (labor force surveys
  - social security registrations)
  - adjust for undercount
empirical_requirements:
  contract_version: 1
  population: Chinese provinces (30 regions), including agriculture, manufacturing, and service sectors, 2000–2005
  observation_unit: Province-pair-sector-year (trade flows); province-pair-year (migration flows)
  geography_level: Province
  time_start: 2000
  time_end: 2005
  minimum_frequency: one-time (2000 and 2005 cross-sections)
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields:
  - interprovincial trade flows
  - interprovincial migration flows
  - provincial GDP by sector
  - provincial employment by sector
  - provincial wages
  - transport costs
  required_identifiers:
  - province code
  - year
  - sector
  treatment_key:
  - estimated migration costs
  - estimated trade costs
  treatment_source: Input-output tables for trade flows; population census (2000) and 1% population survey (2005) for migration
    flows; statistical yearbooks for provincial economic data
  measurement_risks:
  - migrant undercount
  - informal sector employment
  - smuggling and informal trade
  - transport cost approximation
evidence:
- id: E1
  source_type: paper
  citation: 'Tombe, Trevor, and Xiaodong Zhu. 2019. ''Trade, Migration, and Productivity: A Quantitative Analysis of China.''
    American Economic Review 109 (5): 1843–1872.'
  url: https://doi.org/10.1257/aer.20150811
  date: 2019
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - counterfactual analysis
  - parameter sensitivity
  verification_status: verified
design_applications:
- paper: 'Trade, Migration, and Productivity: A Quantitative Analysis of China'
  doi: 10.1257/aer.20150811
  journal: American Economic Review
  year: 2019
  research_question: How do internal trade and migration costs affect aggregate labor productivity in China, and what accounts
    for changes between 2000 and 2005?
  population: 30 Chinese provinces (including municipalities) in agriculture, manufacturing, and services
  outcome: Aggregate labor productivity, welfare, sectoral employment shares
  data_used:
  - Chinese provincial input-output tables (2000
  - 2005)
  - China Population Census (2000)
  - China 1% Population Sample Survey (2005)
  - China Statistical Yearbooks (provincial GDP
  - employment
  - wages)
  - transport cost data
  treatment_encoding: Estimated province-pair migration costs and trade costs from a structural model
  comparison: Counterfactual scenarios where trade/migration costs are reduced to different levels
  empirical_design: Quantitative general equilibrium model with internal and international trade, and migration across sectors
    and regions
  assumptions:
  - CES preferences
  - iceberg trade costs
  - exogenous sectoral productivity
  - migration responds to real income differences
  threats_addressed:
  - Model dependence via extensive sensitivity analysis
  - parameter uncertainty via comparative statics
  - endogeneity via structural approach
  evidence_refs:
  - E1
readiness_blockers:
- "Admissibility audit (task-e9b64f33e231, 2026-07-13): This is a quantitative spatial equilibrium model (Tombe and Zhu 2019
  AER), not a recoverable assignment case. The paper calibrates a structural model to observed trade and migration flows rather
  than exploiting an externally assigned treatment. No instrument, threshold, boundary, or randomization is present. Kept
  contested as a low-priority lead; do not invest in grounding. The duplicate record china-trade-migration-productivity has
  been deprecated and redirected here."
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
method_transfer: null
---
## Institutional Background

China's hukou (household registration) system, established in the 1950s, ties access to public services (education, healthcare, housing) to a person's registered location. Rural-to-urban migrants face severe barriers: without urban hukou, they are excluded from local public schools, subsidized housing, and formal healthcare in destination cities. These migration barriers, combined with interprovincial trade barriers (local protectionism, transport infrastructure deficits, provincial border effects), create large frictions in China's internal goods and labor markets. [E1]

## What Changed

Between 2000 and 2005, both internal trade costs and migration costs in China declined substantially. Internal trade costs fell by 10–15% (driven by transport infrastructure investment and reduced provincial protectionism). Migration costs declined by approximately 18% on average, with even larger reductions (approximately 40%) for cross-province moves. Hukou reforms in some provinces relaxed restrictions on access to urban public services for migrants. [E1]

## Implementation and Assignment

The assignment of treatment (migration cost levels) is not through a specific policy reform but rather through the overall institutional and geographic environment. Migration costs are estimated from observed migration flows and wage differentials using a structural model. The key variation is across province-pairs: moving costs differ by distance, cultural proximity, and the severity of hukou restrictions in destination provinces. [E1]

## Why This Creates Empirical Variation

Province-pair variation in trade and migration costs arises from geography (distance, transport infrastructure), institutions (hukou policy stringency, local protectionism), and policy changes over time. This variation allows identification of the aggregate effects of internal frictions through a structural model that maps observed costs to productivity and welfare outcomes. [E1]

## Identification Risks

The quantitative results depend on model structure and parameter choices. Migration cost declines may partly reflect endogenous policy responses to economic growth rather than exogenous reforms. Migration flow data may undercount temporary migrants who do not change their official registration. [E1; analytical inference]

## Data Requirements

Province-pair trade flows from China's interregional input-output tables (2002, 2007) and interprovincial migration flows from the population census (2000) and 1% population survey (2005). Provincial GDP, employment, and wages from statistical yearbooks. Transport cost and distance data. [E1]

## Evidence Notes

E1 estimates that the decline in internal trade and migration costs accounts for 36% of China's aggregate labor productivity growth between 2000 and 2005. The reductions in internal frictions were more important than reductions in international trade costs. Despite these declines, migration costs remained high: moving China's migration costs to US-equivalent levels would increase GDP per worker by approximately 13%.
