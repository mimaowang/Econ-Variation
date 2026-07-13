---
schema_version: 2
id: us-china-import-competition-shock
name: Rising Chinese Import Competition as a Local Labor Market Shock in the United States
aliases:
- China trade shock
- China Syndrome import competition
- Chinese import exposure shock

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: United States
  regions:
  - All US commuting zones
  domains:
  - trade
  - labor
  - manufacturing
  - local-economy
  - public-finance
  variation_type: continuous-exposure
  knowledge_role: transferable-method
  china_relevance: The source setting is outside China; retain the reusable identification construction rather than recommend
    the foreign shock as a China treatment.
identity:
  instrument: Differential exposure of US local labor markets to rising Chinese import competition, instrumented by Chinese
    exports to other high-income countries
  authority: Not applicable — market-driven trade flows; the identifying instrument exploits supply-driven Chinese export
    growth to other high-income markets
  legal_identifiers: []
  implementation_regime: China's accession to WTO (2001) and subsequent productivity-driven manufacturing export expansion,
    combined with variation in US local industry specialization
  assignment_mechanism: Local labor market exposure depends on pre-existing industry composition interacted with national-level
    growth in Chinese import penetration by industry; the instrument removes US-demand-driven components
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 1990
  implementation_end: 2007
  local_timing: Import exposure accumulates continuously; the main analysis period is 1990–2007, with a focus on post-2000
    acceleration
  anticipation: No direct anticipation by workers of their industry-specific import exposure; industry specialization was
    determined well before the China trade shock
  last_verified: '2026-07-13'
assignment:
  unit: Commuting zone (CZ)
  treated: CZs with higher predicted exposure to Chinese imports based on pre-existing industry mix
  comparison_pool: CZs with lower predicted exposure, conditional on shared pre-trends and similar observable characteristics
  rule: Exposure = ∑_j (L_{ij,t}/L_{i,t}) × (ΔM_{ucj,t}/L_{i,t}) where L_{ij} is CZ i employment in industry j and ΔM_{ucj}
    is the change in US imports from China in industry j; instrument using Chinese exports to other high-income countries
    (Australia, Denmark, Finland, Germany, Japan, New Zealand, Spain, Switzerland) instead of US imports
  intensity: Continuous — exposure varies by CZ based on the share of employment in import-competing manufacturing industries
  exemptions: []
  compliance: Not applicable — exposure is not a policy treatment; it is a market outcome instrumented using supply-driven
    variation
  exposure_construction: Construct CZ-level import exposure per worker using the formula above; instrument with analogous
    measure using Chinese exports to other high-income countries; use 1990 or 2000 industry employment shares for baseline
    exposure
  required_identifiers:
  - commuting zone code
  - calendar year
  - industry code
  spillovers: Input-output linkages generate indirect exposure through upstream supplier industries; non-manufacturing employment
    may be affected through local demand spillovers; migration across CZs may attenuate measured effects
research_compatibility:
  outcome_domains:
  - manufacturing employment
  - labor force participation
  - wages
  - unemployment
  - transfer payments
  - local demand
  - innovation
  affected_populations:
  - manufacturing workers
  - local labor markets
  - low-wage workers
  - non-college workers
  mechanism_channels:
  - import substitution
  - plant closure
  - reduced labor demand
  - local demand decline
  - transfer-program enrollment
  best_for:
  - Studying local labor market adjustment to trade shocks
  - Outcomes that can be measured at the commuting-zone by year level
  - Designs using shift-share (Bartik) instruments with industry specialization as shares
  not_good_for:
  - Individual-level outcomes without geographic identifiers
  - Short panels without pre-1990 data
  - Designs that require random or quasi-random assignment of treatment
design:
  affordances:
  - differential industry specialization across local labor markets
  - supply-driven Chinese export growth to other high-income countries
  - pre/post-2000 acceleration in Chinese import penetration
  candidate_designs:
  - shift-share instrumental variables (Bartik instrument)
  - long-difference regressions (1990–2007 or 2000–2007)
  - panel event study with CZ and year fixed effects
  - generalized difference-in-differences with continuous treatment
  identifying_variation: Cross-CZ differences in import exposure predicted by pre-existing industry composition interacted
    with supply-driven Chinese export growth to other high-income economies
  assumptions: &id001
  - Chinese export growth to other high-income countries is driven by Chinese supply factors (productivity, WTO accession)
    rather than by correlated demand shocks across high-income countries
  - Pre-existing industry specialization is exogenous to contemporaneous US labor demand shocks
  - Conditional on controls and the instrument, CZs with different predicted exposure would have had comparable outcomes in
    the absence of the China shock
  diagnostics: &id002
  - Plot reduced-form relationship between instrument and outcome
  - Test for pre-trends in CZ-level outcomes (1990–2000) by predicted exposure
  - Assess instrument relevance (first-stage F-statistic)
  - Control for CZ-level pre-existing trends, demographics, and computerization
  - Test for spatial spillovers and measure input-output linkages
  - Assess sensitivity to leaving-one-out instrument construction
  primary_strategy: Shift-share instrumental variables with long-difference specification; exposure constructed from pre-existing
    industry employment shares and national import growth
  estimand: The causal effect of the recorded exposure on Manufacturing employment, total employment, wages, labor force participation,
    unemployment, transfer payments (disability, retirement, healthcare), conditional on the stated design assumptions.
  treatment_variable: CZ-level change in Chinese import exposure per worker (1990–2007 or 2000–2007), instrumented with Chinese
    exports to other high-income countries
  comparison_logic: Low-exposure versus high-exposure CZs, conditional on the instrument and controls
  estimation_notes: Shift-share instrumental variables with long-difference specification; exposure constructed from pre-existing
    industry employment shares and national import growth
threats:
- type: correlated-demand-shocks
  basis: inferred
  condition: If Chinese export growth to other high-income countries reflects common demand shocks rather than Chinese supply
    expansion, the exclusion restriction fails
  evidence_refs:
  - E1
  possible_diagnostics:
  - test correlation of Chinese exports across destination markets
  - use alternative instruments such as Chinese productivity or tariff changes
  - control for industry-specific technology shocks
- type: endogenous-industry-specialization
  basis: inferred
  condition: CZs that specialized in import-competing industries may have been on different long-run trajectories unrelated
    to trade
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for pre-1990 trends in manufacturing employment
  - include CZ fixed effects
  - control for routine-task intensity and computerization
- type: spatial-spillovers
  basis: documented
  condition: Negative local demand effects from manufacturing job losses spill over to non-traded sectors; input-output linkages
    propagate upstream and downstream
  evidence_refs:
  - E1
  possible_diagnostics:
  - estimate indirect effects through input-output tables
  - measure non-manufacturing employment responses
  - analyze cross-CZ commuting patterns
- type: migration-and-attrition
  basis: inferred
  condition: Workers may migrate out of highly exposed CZs, attenuating measured wage and employment effects and shifting
    the burden to transfer programs
  evidence_refs:
  - E1
  possible_diagnostics:
  - track population flows
  - analyze outcomes by worker mobility
  - examine transfer-program enrollment
empirical_requirements:
  contract_version: 1
  population: US workers and local labor markets observed before and during the China trade expansion
  observation_unit: Commuting zone-year or individual-year linked to CZ-year exposure
  geography_level: Commuting zone (722 consistent CZs covering the continental US)
  time_start: 1990
  time_end: 2007
  minimum_frequency: annual
  minimum_pre_periods: 5
  minimum_post_periods: 5
  required_fields:
  - employment by industry and CZ
  - trade flows by industry and country
  - outcome variables by CZ and year
  required_identifiers:
  - commuting zone code
  - calendar year
  - NAICS or SIC industry code
  treatment_key:
  - commuting zone code
  - calendar year
  - industry-based import exposure instrument
  treatment_source: UN Comtrade for trade flows; County Business Patterns and BLS for local employment by industry; CZ crosswalk
    for geographic aggregation
  measurement_risks:
  - industry classification changes over time
  - CZ boundary consistency
  - import values versus quantities
  - within-CZ heterogeneity
  - exchange rate effects
evidence:
- id: E1
  source_type: paper
  citation: 'Autor, David H., David Dorn, and Gordon H. Hanson. 2013. "The China Syndrome: Local Labor Market Effects of Import
    Competition in the United States." American Economic Review 103 (6): 2121–2168.'
  url: https://doi.org/10.1257/aer.103.6.2121
  date: 2013
  supports:
  - identity
  - assignment
  - design
  - instrument construction
  - main estimates
  - spillover analysis
  verification_status: verified
- id: E2
  source_type: replication
  citation: Autor, Dorn, and Hanson replication package, OpenICPSR project 112670
  url: https://www.openicpsr.org/openicpsr/project/112670/
  date: 2013
  supports:
  - data construction
  - instrument
  - code
  - robustness checks
  verification_status: verified
design_applications:
- paper: 'The China Syndrome: Local Labor Market Effects of Import Competition in the United States'
  doi: 10.1257/aer.103.6.2121
  journal: American Economic Review
  year: 2013
  research_question: How does rising Chinese import competition affect US local labor market outcomes including employment,
    wages, and transfer payments?
  population: US commuting zones observed from 1990 to 2007
  outcome: Manufacturing employment, total employment, wages, labor force participation, unemployment, transfer payments (disability,
    retirement, healthcare)
  data_used: []
  treatment_encoding: CZ-level change in Chinese import exposure per worker (1990–2007 or 2000–2007), instrumented with Chinese
    exports to other high-income countries
  comparison: Low-exposure versus high-exposure CZs, conditional on the instrument and controls
  empirical_design: Shift-share instrumental variables with long-difference specification; exposure constructed from pre-existing
    industry employment shares and national import growth
  assumptions:
  - Chinese supply-driven export growth is orthogonal to US labor demand shocks
  - pre-existing industry composition is unrelated to concurrent outcome trends
  threats_addressed:
  - correlated demand shocks via instrument
  - pre-existing trends via controls
  - spatial spillovers via input-output analysis
  evidence_refs:
  - E1
  - E2
readiness_blockers:
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
- Transfer to a Chinese application has not yet been audited against a specific Chinese institution and dataset.
method_transfer:
  source_context: 'United States: Rising Chinese Import Competition as a Local Labor Market Shock in the United States'
  strategy_family: Shift-share instrumental variables with long-difference specification; exposure constructed from pre-existing
    industry employment shares and national import growth
  reusable_logic: Local labor market exposure depends on pre-existing industry composition interacted with national-level
    growth in Chinese import penetration by industry; the instrument removes US-demand-driven components
  construction_steps:
  - Construct CZ-level import exposure per worker using the formula above; instrument with analogous measure using Chinese
    exports to other high-income countries; use 1990 or 2000 industry employment shares for baseline exposure
  source_treatment_or_endogenous_variable: CZ-level change in Chinese import exposure per worker (1990–2007 or 2000–2007),
    instrumented with Chinese exports to other high-income countries
  source_instrument_or_assignment: Local labor market exposure depends on pre-existing industry composition interacted with
    national-level growth in Chinese import penetration by industry; the instrument removes US-demand-driven components
  first_stage_or_contrast: Cross-CZ differences in import exposure predicted by pre-existing industry composition interacted
    with supply-driven Chinese export growth to other high-income economies
  identifying_assumptions: *id001
  diagnostics: *id002
  china_use_cases:
  - Construct Chinese prefecture or firm exposure from predetermined industry composition interacted with external product-level
    demand, tariff, or third-market trade shocks.
  china_data_requirements:
  - employment by industry and CZ
  - trade flows by industry and country
  - outcome variables by CZ and year
  transfer_limits:
  - Individual-level outcomes without geographic identifiers
  - Short panels without pre-1990 data
  - Designs that require random or quasi-random assignment of treatment
---
## Institutional Background

Between 1990 and 2007, Chinese manufacturing exports to the United States grew dramatically, driven by China's economic reforms, productivity growth, and especially its 2001 accession to the World Trade Organization (WTO). US imports from China rose from negligible levels to over $300 billion annually. This trade expansion was not uniform across industries: it was concentrated in labor-intensive manufacturing sectors such as apparel, furniture, electronics, and metal products. [E1]

Different US local labor markets had very different pre-existing industry compositions. Some commuting zones specialized heavily in industries that would later face intense Chinese competition (e.g., furniture manufacturing in North Carolina, textiles in South Carolina), while others specialized in less-exposed industries (e.g., services, technology). This interaction between pre-existing local industry structure and national-level import growth created differential local exposure to the trade shock. [E1]

## What Changed

Chinese import penetration in US manufacturing accelerated sharply after 2000, with the product composition tracking Chinese comparative advantage in labor-intensive goods. The annual growth in import exposure per US worker was approximately $1,140 per year between 2000 and 2007, several times the rate of the 1990s. [E1]

The key analytical contribution is the instrument: rather than using US imports from China directly (which may reflect US demand conditions), the authors use Chinese exports to eight other high-income countries. This isolates the supply-driven component of Chinese export growth — productivity improvements, falling trade costs, and policy liberalization in China — that is arguably exogenous to US labor market conditions. [E1]

## Implementation and Assignment

Exposure is not a policy assignment but a market-driven outcome. Each CZ's import exposure per worker is constructed as the sum across industries of (industry employment share in the CZ) × (change in US imports from China in that industry, divided by CZ total employment). The instrument replaces US imports from China with Chinese exports to other high-income countries, removing the US-demand component. [E1; analytical inference]

The design thus produces a continuous treatment: every CZ receives some exposure, and the identifying variation comes from differences in the intensity of exposure across CZs driven by pre-existing industry structure. There is no clean "treated versus control" binary split; the comparison is between higher-exposure and lower-exposure CZs. [analytical inference]

## Why This Creates Empirical Variation

Two sources of variation are combined: (1) cross-CZ differences in industry employment shares (the "shares"), fixed in a baseline period and reflecting historical specialization patterns; and (2) time-series variation in Chinese import growth by industry (the "shift"). The interaction creates a shift-share or Bartik instrument. The key exclusion restriction is that Chinese supply-driven export growth — as proxied by exports to other high-income countries — is uncorrelated with US CZ-level labor demand shocks. [E1; analytical inference]

## Identification Risks

If Chinese exports to all high-income countries reflect correlated demand booms rather than supply expansion, the instrument is invalid. If CZs with high import-competing industry shares were already on declining trajectories before 1990, pre-trends may confound the estimates. Through input-output linkages, negative demand shocks in manufacturing spill over to local services and construction. Migration may attenuate measured wage effects as workers leave highly exposed areas. The authors address many of these concerns with extensive robustness checks, but the exclusion restriction ultimately requires judgment. [E1; analytical inference]

## Data Requirements

A credible design requires: (1) annual trade data by industry and origin country; (2) local employment by industry for constructing exposure shares; (3) outcome variables (employment, wages, transfers) at the CZ-year level; (4) a stable CZ geography crosswalk; (5) sufficient pre- and post-exposure periods. The instrument additionally requires Chinese export data by destination country and industry. [E1]

## Evidence Notes

E1 is the published paper itself, which provides the theoretical framework, empirical strategy, main results, and extensive robustness analysis. The instrument construction, data sources, and specification choices are clearly documented. E2 is the replication package that allows independent verification of the core results.
