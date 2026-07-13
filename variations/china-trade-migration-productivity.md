---
schema_version: 2
id: china-trade-migration-productivity
name: Joint Effects of Internal Trade Cost Reductions and Internal Migration on China's Spatial Productivity (2000–2005)
aliases:
- Tombe Zhu trade migration China
- 贸易成本 移民 生产率
- internal trade costs migration China
- spatial misallocation China

status: deprecated
provenance:
  task_id: task-e9b64f33e231
scope:
  country: China
  regions:
  - All provinces and prefectures
  domains:
  - trade
  - migration
  - productivity
  - spatial-economics
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: The joint reduction of internal trade costs (through infrastructure improvements and market integration reforms)
    and internal migration costs (through hukou relaxation) across Chinese provinces, with the interaction of these two forces
    generating spatial variation in effective market access and labor allocation
  authority: Chinese government (infrastructure investment, hukou reform) and market integration dynamics
  legal_identifiers:
  - Hukou system reforms
  - infrastructure investment programs
  - WTO accession-related market integration
  implementation_regime: Between 2000 and 2005, China experienced dramatic reductions in internal trade costs (from expressway
    construction, logistics improvements) and migration costs (hukou reforms, declining restrictions on labor mobility); these
    changes varied in intensity across provinces
  assignment_mechanism: Provinces are differentially exposed to trade cost reductions based on their geographic position relative
    to major markets and transport corridors; migration cost reductions disproportionately affect provinces with high historical
    out-migration
  parent: null
  related_variations:
  - china-highway-network-expansion
  - china-2014-hukou-local-implementation
  - china-wto-accession-firm-performance
timeline:
  announcement: null
  effective: null
  implementation_start: 2000
  implementation_end: 2005
  local_timing: Trade costs decline gradually with infrastructure improvements; migration costs decline with provincial-level
    hukou reforms
  anticipation: Infrastructure investments were planned under Five-Year Plans; hukou reforms were incremental and not fully
    anticipated
  last_verified: '2026-07-13'
assignment:
  unit: Province-sector and worker
  treated: Workers in provinces with large reductions in migration costs (allowing relocation to higher-productivity areas);
    sectors in provinces with large reductions in internal trade costs (allowing better market access)
  comparison_pool: Cross-province variation in cost reductions; provinces with smaller trade/migration cost declines serve
    as comparison
  rule: The reduction in spatial frictions (trade and migration costs) creates gains by allowing workers to move from low-productivity
    to high-productivity locations and by allowing goods to flow from surplus to deficit areas
  intensity: Continuous — province-level migration cost reduction, province-pair trade cost reduction, change in market access
  compliance: Migration and trade flows respond to cost reductions; actual responses depend on the magnitude of reduced frictions
    and underlying economic incentives
  exemptions: []
  exposure_construction: Construct province-level measures of internal trade cost changes (from price gaps, freight costs,
    infrastructure improvements) and migration cost changes (from hukou reform indices, migration flow data); calibrate a
    spatial general equilibrium model linking these cost changes to productivity and welfare
  required_identifiers:
  - province code
  - year
  - sector
  - migration status
  - hukou type
  spillovers: Migration from one province to another affects wages in both origin and destination; trade integration changes
    production patterns across provinces
research_compatibility:
  outcome_domains:
  - aggregate productivity
  - welfare
  - spatial allocation of labor
  - internal trade flows
  - wage convergence
  - structural transformation
  affected_populations:
  - Rural migrants
  - urban workers
  - all Chinese residents affected by changes in goods prices
  mechanism_channels:
  - reduced trade costs
  - reduced migration costs
  - spatial reallocation of labor
  - goods market integration
  - productivity convergence
  best_for:
  - Quantifying the aggregate productivity and welfare gains from reducing spatial frictions
  - understanding the interaction between goods and labor market integration
  not_good_for:
  - Individual-level migration decision analysis
  - short-run transition dynamics
  - identification of specific policy instruments
design:
  affordances:
  - province-level variation in trade and migration cost reductions
  - rich interprovincial trade and migration flow data
  - structural spatial equilibrium model
  candidate_designs:
  - quantitative spatial equilibrium model
  - decomposition analysis
  - counterfactual simulations
  identifying_variation: Observed changes in interprovincial trade and migration flows between 2000 and 2005, combined with
    province-level changes in trade costs (inferred from price gaps, infrastructure) and migration costs (inferred from hukou
    reform indices)
  assumptions:
  - Spatial equilibrium model correctly captures the key mechanisms
  - trade and migration costs are measured accurately
  - changes in flows reflect changes in frictions rather than unobserved province-level shocks
  diagnostics:
  - compare model predictions with observed changes
  - sensitivity to alternative parameterizations
  - test reduced-form relationships between cost measures and flow changes
  - validate model using out-of-sample predictions
  primary_strategy: Calibrated quantitative spatial equilibrium model linking trade costs, migration costs, productivity,
    and welfare; decomposition of aggregate productivity growth into trade-cost reduction, migration-cost reduction, and other
    components
  estimand: The causal effect of the recorded exposure on Aggregate labor productivity, welfare (real income), spatial allocation
    of workers, interprovincial trade, conditional on the stated design assumptions.
  treatment_variable: Changes in province-pair trade costs (from freight, infrastructure, price gaps) and province-level migration
    costs (from hukou reform indices)
  comparison_logic: 'Counterfactual: what would productivity and welfare be with 2000-level trade/migration costs vs 2005
    costs'
  estimation_notes: Calibrated quantitative spatial equilibrium model linking trade costs, migration costs, productivity,
    and welfare; decomposition of aggregate productivity growth into trade-cost reduction, migration-cost reduction, and other
    components
threats:
- type: model-dependence
  basis: inferred
  condition: Results depend on the structural spatial equilibrium model; different modeling assumptions about production technology,
    preferences, or migration behavior could yield different quantitative conclusions
  evidence_refs:
  - E1
  possible_diagnostics:
  - report sensitivity to model parameters
  - compare reduced-form and structural estimates
  - test alternative model specifications
  - validate model predictions against observed outcomes
- type: measurement-error
  basis: inferred
  condition: Internal trade costs and migration costs are difficult to measure precisely; changes in observed flows may reflect
    measurement error or data quality improvements
  evidence_refs:
  - E1
  possible_diagnostics:
  - use multiple measures of trade and migration costs
  - test sensitivity to measurement approach
  - exploit natural experiments for specific cost components
empirical_requirements:
  contract_version: 1
  population: All Chinese provinces and their workers, 2000–2005
  observation_unit: Province-sector or province-pair
  geography_level: Province
  time_start: 2000
  time_end: 2005
  minimum_frequency: every 5 years (census-to-census)
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - interprovincial trade flows
  - interprovincial migration flows
  - provincial GDP by sector
  - provincial employment
  - wages by province and sector
  - internal trade cost measures
  - migration cost measures
  required_identifiers:
  - province code
  - year
  - sector
  treatment_key:
  - origin province
  - destination province
  - year
  - trade cost change
  - migration cost change
  treatment_source: China interprovincial input-output tables for trade flows; China Population Census (2000, 2005) for migration
    flows; price data for trade cost measurement; provincial statistical yearbooks for economic outcomes
  measurement_risks:
  - interprovincial trade data quality and completeness
  - migration measured at census intervals only
  - trade costs inferred rather than directly observed
  - matching economic outcomes to cost changes
evidence:
- id: E1
  source_type: paper
  citation: 'Tombe, Trevor, and Xiaodong Zhu. 2019. "Trade, Migration, and Productivity: A Quantitative Analysis of China."
    American Economic Review 109 (5): 1843–1872.'
  url: https://doi.org/10.1257/aer.20170222
  date: 2019
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - welfare analysis
  - decomposition
  verification_status: verified
design_applications:
- paper: 'Trade, Migration, and Productivity: A Quantitative Analysis of China'
  doi: 10.1257/aer.20170222
  journal: American Economic Review
  year: 2019
  research_question: How much did reductions in internal trade and migration costs contribute to China's aggregate productivity
    growth and welfare gains between 2000 and 2005?
  population: All Chinese provinces, workers, and sectors, 2000–2005
  outcome: Aggregate labor productivity, welfare (real income), spatial allocation of workers, interprovincial trade
  data_used: []
  treatment_encoding: Changes in province-pair trade costs (from freight, infrastructure, price gaps) and province-level migration
    costs (from hukou reform indices)
  comparison: 'Counterfactual: what would productivity and welfare be with 2000-level trade/migration costs vs 2005 costs'
  empirical_design: Calibrated quantitative spatial equilibrium model linking trade costs, migration costs, productivity,
    and welfare; decomposition of aggregate productivity growth into trade-cost reduction, migration-cost reduction, and other
    components
  assumptions:
  - spatial equilibrium holds
  - trade costs correctly inferred
  - migration responds to real income differences
  - model parameters stable over period
  threats_addressed:
  - model uncertainty via sensitivity analysis
  - measurement error via multiple cost measures
  - alternative explanations via decomposition
  evidence_refs:
  - E1
readiness_blockers:
- "Catalog admissibility is unresolved: the source is a general-equilibrium exercise rather than a recoverable assignment case."
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
superseded_by: china-hukou-migration-productivity
---
## Institutional Background
China's rapid economic growth has been accompanied by two major spatial transformations: (1) the integration of previously fragmented provincial goods markets, and (2) the largest internal migration in human history. Between 2000 and 2005 alone, an estimated 40–50 million workers migrated from rural to urban areas and from inland to coastal provinces. Simultaneously, infrastructure investment and market reforms reduced the cost of trading goods across provinces. [E1]

## What Changed
Internal trade costs fell due to expressway construction, railway expansion, logistics sector deregulation, and the removal of local protectionist barriers. Internal migration costs fell due to gradual hukou reform, declining discrimination against migrants in urban labor markets, and the expansion of migrant networks that lower the effective cost of moving. These two forces interacted: trade integration can substitute for migration (goods move instead of people), and migration can complement trade (people move to produce goods for distant markets). [E1]

## Implementation and Assignment
Provinces are differentially exposed to internal trade and migration cost reductions. Trade cost reductions from expressway construction and logistics improvements vary by a province's geographic position. Migration cost reductions from hukou reforms vary by province. The paper uses all these sources of variation to calibrate a spatial equilibrium model that separately identifies the effects of trade cost and migration cost changes.[E1]

## Why This Creates Empirical Variation
The paper uses a quantitative spatial equilibrium model calibrated to rich Chinese data to separately identify the contributions of trade cost reductions and migration cost reductions. By comparing actual outcomes against model-generated counterfactuals (what would happen with 2000-level costs), the paper quantifies the aggregate importance of each channel. The geographic variation in cost reductions across provinces provides the identifying variation for the model's key elasticities. [E1; analytical inference]

## Identification Risks
The results are primarily model-based rather than reduced-form; the quantitative decomposition depends on model structure, parameter values, and the measurement of trade and migration costs. Different model specifications could yield different conclusions about the relative importance of trade versus migration cost reductions. [E1; analytical inference]

## Data Requirements
Province-level and province-pair data: interprovincial trade flows from input-output tables, interprovincial migration flows from 2000 census and 2005 mini-census, provincial GDP by sector, employment and wages, price indices for trade cost inference, and measures of hukou reform intensity across provinces. [E1]

## Evidence Notes
E1 finds that reductions in internal trade and migration costs account for a substantial share of China's aggregate productivity growth between 2000 and 2005. The paper quantifies the interaction between goods market integration and labor market integration, showing that both are important and that the joint gains exceed the sum of individual effects.

## Deprecation Notice

**Deprecated 2026-07-13 (task-e9b64f33e231)**: This record is superseded by `china-hukou-migration-productivity`. Both records describe the same paper — Tombe & Zhu (2019, AER) — and the same quantitative spatial equilibrium model. They share the same DOI (10.1257/aer.20170222), same time period (2000–2005), and same methodology. Neither record possesses a recoverable assignment-generating feature, as the paper is a calibrated structural model rather than a causal identification exercise. The retained record `china-hukou-migration-productivity` remains `contested` for the same reason: quantitative spatial equilibrium models do not constitute recoverable assignment-generating variation under NIEL's admissibility criteria. Both records are catalogued as low-priority leads only. [analytical inference]
