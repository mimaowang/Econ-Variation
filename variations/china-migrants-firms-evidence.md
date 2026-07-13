---
schema_version: 2
id: china-migrants-firms-evidence
name: Rural-Urban Migration Shocks to Chinese Manufacturing Firms through Local Labor Supply Variation
aliases:
- Imbert Seror Zhang Zylberberg migrants firms China
- 农民工 企业
- migration shock firm productivity
- rural-urban migration China

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - Urban areas receiving rural migrants
  - rural sending areas
  domains:
  - labor
  - firm
  - migration
  - development
  variation_type: event-shock
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: Exogenous variation in rural-urban migration flows to Chinese cities, driven by origin-area agricultural productivity
    shocks (push factors in rural areas that are unrelated to urban labor demand), which generate plausibly exogenous increases
    in the supply of migrant workers to urban firms
  authority: Economic forces (agricultural productivity shocks) and Chinese government (hukou system)
  legal_identifiers:
  - Hukou system regulations
  - rural land tenure system
  implementation_regime: Rural-urban migration expanded dramatically in China from the 1990s onward; the variation exploited
    is the differential exposure of urban locations to migration flows from specific rural origin areas, driven by agricultural
    shocks in those origin areas
  assignment_mechanism: Urban firms are "treated" by increased migrant labor supply; the key identifying variation comes from
    agricultural productivity shocks in migrant-sending rural areas, which push workers to migrate for reasons unrelated to
    urban labor demand conditions
  parent: null
  related_variations:
  - china-2014-hukou-local-implementation
  - china-land-reform-sex-selection
timeline:
  announcement: null
  effective: null
  implementation_start: 2000
  implementation_end: 2006
  local_timing: Migration flows vary continuously over time and across origin-destination pairs; agricultural shocks affect
    timing
  anticipation: Agricultural shocks (weather, pests) are largely unanticipated at the household level
  last_verified: '2026-07-13'
assignment:
  unit: Firm and city
  treated: Urban manufacturing firms receiving increased inflows of migrant workers due to agricultural shocks in their specific
    migrant-origin areas
  comparison_pool: Firms in the same city with different migrant-origin exposure; same firms in periods without large migration
    inflows
  rule: The interaction of a firm's historical reliance on migrant labor from specific origin areas with agricultural productivity
    shocks in those origin areas; firms relying on origin areas experiencing negative agricultural shocks receive a positive
    labor supply shock
  intensity: Continuous — predicted migration inflow based on origin-area shocks and historical migration patterns
  compliance: Migration responds to economic incentives; not all affected workers migrate, but agricultural shocks create
    significant variation in out-migration
  exemptions: []
  exposure_construction: Construct firm-level predicted migration using pre-period migration shares from each origin to each
    city × origin-specific agricultural productivity shocks; this shift-share (Bartik-style) instrument isolates labor supply
    variation exogenous to local urban labor demand
  required_identifiers:
  - firm ID
  - city code
  - year
  - migration origin region
  - agricultural shock measure
  spillovers: Increased migrant labor supply may affect wages and employment of local urban workers; general equilibrium effects
    on firm entry and exit in urban product and labor markets
research_compatibility:
  outcome_domains:
  - firm productivity
  - employment
  - wages
  - output
  - factor mix
  - technology adoption
  - firm entry and exit
  affected_populations:
  - Rural migrant workers
  - urban incumbent workers
  - manufacturing firm owners
  - local urban residents
  mechanism_channels:
  - labor supply increase
  - wage effect
  - capital-labor substitution
  - technology adoption
  - firm entry
  - agglomeration
  best_for:
  - Studying how labor supply shocks affect firm behavior and productivity
  - understanding migration's role in structural transformation
  not_good_for:
  - Long-run effects of hukou reform
  - individual migrant welfare
  - sending-area outcomes
design:
  affordances:
  - origin-specific agricultural shocks
  - historical migration patterns
  - rich firm-level panel data
  - geographic variation in migration networks
  candidate_designs:
  - shift-share (Bartik) instrument using origin shocks × historical migration
  - difference-in-differences
  - event study around large migration episodes
  identifying_variation: Agricultural productivity shocks in migrant-sending rural areas interacted with historical (pre-period)
    migration patterns from those areas to specific urban destinations
  assumptions:
  - Agricultural shocks are exogenous to urban labor demand
  - historical migration shares reflect persistent network effects rather than contemporaneous urban conditions
  - shift-share exclusion restriction holds
  diagnostics:
  - Test for pre-trends in urban outcomes before migration shocks
  - verify agricultural shocks are not predictable
  - compare with alternative instruments
  - check sensitivity to shift-share construction
  primary_strategy: Shift-share (Bartik) IV using origin agricultural shocks and historical migration patterns; firm-level
    panel analysis; event study around large migration episodes
  estimand: The causal effect of the recorded exposure on Firm employment, output, capital, wages, total factor productivity,
    factor shares, conditional on the stated design assumptions.
  treatment_variable: 'Shift-share instrument: predicted migration inflow = historical (pre-period) migration share from each
    origin to each city × origin-specific agricultural productivity shock'
  comparison_logic: Firms with high vs low predicted migration exposure; pre-shock vs post-shock within firms
  estimation_notes: Shift-share (Bartik) IV using origin agricultural shocks and historical migration patterns; firm-level
    panel analysis; event study around large migration episodes
threats:
- type: endogenous-migration-networks
  basis: inferred
  condition: Historical migration patterns may reflect persistent differences in urban labor demand across cities; if these
    differences persist (autocorrelated demand), the shift-share instrument may not be valid
  evidence_refs:
  - E1
  possible_diagnostics:
  - use long-lagged historical shares
  - test for autocorrelation in urban labor demand
  - sensitivity to alternative construction of migration shares
  - Adao-Kolesar-Morales inference for shift-share designs
- type: general-equilibrium-wage-effects
  basis: inferred
  condition: In-migration may affect local wages and prices, creating general equilibrium effects that complicate interpretation
    of firm-level estimates
  evidence_refs:
  - E1
  possible_diagnostics:
  - estimate wage effects separately
  - model firm labor demand with endogenous wages
  - report both partial and general equilibrium estimates
empirical_requirements:
  contract_version: 1
  population: Chinese manufacturing firms in urban areas, 2000–2006
  observation_unit: Firm-year or city-year
  geography_level: City (destination) and county (origin)
  time_start: 2000
  time_end: 2006
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 5
  required_fields:
  - firm employment
  - output
  - capital
  - wages
  - industry
  - location
  - historical migrant-sending regions by city
  - agricultural productivity by origin region
  required_identifiers:
  - firm ID
  - city code
  - year
  - origin region
  treatment_key:
  - city code
  - year
  - predicted migration inflow (shift-share)
  - actual migrant share change
  treatment_source: The published paper reports linked firm, migration-network, and origin-area agricultural-shock measures;
    exact source files and construction must be recovered from the full text or replication package.
  measurement_risks:
  - migration measured at census intervals requiring interpolation
  - agricultural shock measurement accuracy at county level
  - matching firm location to migration destinations
  - informal sector firms not captured
evidence:
- id: E1
  source_type: paper
  citation: 'Imbert, Clément, Marlon Seror, Yifan Zhang, and Yanos Zylberberg. 2022. "Migrants and Firms: Evidence from China."
    American Economic Review 112 (6): 1885–1914.'
  url: https://doi.org/10.1257/aer.20191234
  date: 2022
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - firm analysis
  - wage analysis
  verification_status: verified
design_applications:
- paper: 'Migrants and Firms: Evidence from China'
  doi: 10.1257/aer.20191234
  journal: American Economic Review
  year: 2022
  research_question: How do rural-urban migration shocks affect urban manufacturing firms' production, factor mix, and productivity?
  population: Chinese manufacturing firms in urban destinations, 2000–2006
  outcome: Firm employment, output, capital, wages, total factor productivity, factor shares
  data_used: []
  treatment_encoding: 'Shift-share instrument: predicted migration inflow = historical (pre-period) migration share from each
    origin to each city × origin-specific agricultural productivity shock'
  comparison: Firms with high vs low predicted migration exposure; pre-shock vs post-shock within firms
  empirical_design: Shift-share (Bartik) IV using origin agricultural shocks and historical migration patterns; firm-level
    panel analysis; event study around large migration episodes
  assumptions:
  - agricultural shocks are exogenous and not correlated with urban demand shocks
  - historical migration shares represent persistent networks not current demand
  - no differential pre-trends
  threats_addressed:
  - endogenous migration via shift-share IV
  - local demand shocks via origin-specific variation
  - spatial correlation via clustered standard errors and AKM inference
  evidence_refs:
  - E1
readiness_blockers:
- The official article metadata describes a 2000–2006 firm sample; exact data sources, sample construction, and IV inputs still require full-text or replication-package audit.
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
---
## Institutional Background
China's hukou (household registration) system restricts permanent rural-urban migration but has been gradually relaxed since the 1990s, allowing massive temporary migration. By the 2010s, over 270 million rural workers had migrated to urban areas — the largest internal migration in human history. These migrants provide a flexible labor supply to urban manufacturing firms, but their migration decisions respond to both urban pull factors (labor demand) and rural push factors (agricultural conditions). [E1]

## What Changed
The paper exploits the fact that some urban firms — due to historical migration networks — rely more heavily on labor from specific rural origin areas. When those origin areas experience negative agricultural productivity shocks (droughts, floods, price drops), out-migration increases for reasons unrelated to urban labor demand. This creates a plausibly exogenous increase in the supply of workers to firms connected to the affected origin areas. [E1]

## Implementation and Assignment
The key empirical strategy is a shift-share (Bartik) instrument: predicted migration to a city is the sum over sending regions of (historical migration share from that region to the city × current agricultural shock in that region). Because agricultural shocks are determined by weather and global commodity prices — not urban labor demand — the instrument isolates labor supply variation that is exogenous to firm-level outcomes. [E1; analytical inference]

## Why This Creates Empirical Variation
Without an instrument, the correlation between migration and firm outcomes is confounded: migrants go to cities with booming labor demand, which also directly affects firm productivity and wages. The agricultural-shock instrument breaks this simultaneity by exploiting only the push-driven variation in migration. The paper uses this to estimate how exogenous changes in labor supply affect firm production technology, factor mix, and productivity. [E1; analytical inference]

## Identification Risks
The Bartik instrument's validity requires that historical migration shares are not correlated with current urban labor demand shocks. If migration networks formed due to historical industrial patterns that persist (e.g., certain cities always specializing in labor-intensive manufacturing), the instrument may conflate supply and demand. Recent econometric work on shift-share inference (Adao, Kolesar, Morales) provides frameworks for addressing this concern. [E1; analytical inference]

## Data Requirements
Firm-level panel data from the Annual Survey of Industrial Firms including employment, output, capital, and wages. Migration flow data from China's decennial population census and inter-census surveys to construct origin-destination migration shares. County-level agricultural production and weather data to construct agricultural productivity shocks. [E1]

## Evidence Notes
E1 finds that exogenous increases in migrant labor supply lead firms to expand employment and output, with limited capital-labor substitution in the short run. The effects on native workers' wages and employment are examined, and the paper provides evidence on how migration shapes the structural transformation of China's manufacturing sector.
