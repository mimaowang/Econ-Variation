---
schema_version: 2
id: china-wto-accession-firm-performance
name: China's 2001 WTO Accession as a Trade Liberalization Shock Affecting Firm Productivity and Markups
aliases:
- WTO accession China firm performance
- Brandt Van Biesebroeck Wang Zhang
- 中国加入WTO 企业绩效
- trade liberalization China

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - All provinces
  domains:
  - trade
  - firm
  - productivity
  - industrial-organization
  variation_type: single-date-reform
  knowledge_role: global-china-variation
  china_relevance: A global or foreign policy change directly alters the treatment environment faced by Chinese units.
identity:
  instrument: China's accession to the World Trade Organization (WTO) in December 2001, which substantially reduced tariff
    and non-tariff barriers on both Chinese exports (through permanent MFN status and the end of quota restrictions) and Chinese
    imports (through scheduled tariff reductions)
  authority: World Trade Organization and Chinese government
  legal_identifiers:
  - WTO Accession Protocol (2001)
  - scheduled tariff reduction commitments
  - elimination of Multi-Fiber Arrangement quotas for textiles
  implementation_regime: China formally joined the WTO on December 11, 2001; tariff reductions were phased in over several
    years following accession, with different schedules for different industries
  assignment_mechanism: The accession was a national-level event; identification relies on cross-industry variation in pre-accession
    tariff levels and the differential depth of post-accession tariff cuts across industries
  parent: null
  related_variations:
  - china-vat-reform-investment
timeline:
  announcement: '2001-11-10'
  effective: '2001-12-11'
  implementation_start: 2001
  implementation_end: 2006
  local_timing: Uniform national accession date; tariff reduction phase-in varies by industry according to the WTO accession
    schedule
  anticipation: WTO accession was anticipated since the mid-1990s; the exact date and terms were negotiated and became highly
    certain only in 2001
  last_verified: '2026-07-13'
assignment:
  unit: Firm and industry
  treated: All Chinese manufacturing firms after December 2001; treatment intensity varies by industry-level pre-accession
    tariff levels and post-accession tariff reduction depth
  comparison_pool: Pre-2001 period within firms; cross-industry comparison by tariff reduction intensity
  rule: Industries with higher pre-accession tariffs experienced larger tariff reductions; firms in these industries received
    a larger trade liberalization shock
  intensity: Continuous — industry-level tariff reduction (output tariffs on Chinese exports and input tariffs on imported
    intermediates)
  compliance: WTO accession was binding and irreversible; tariff reductions were implemented according to the agreed schedule
  exemptions: []
  exposure_construction: Code firm-year observations from 2002 onward as post-accession; construct industry-specific treatment
    intensity measures from pre-accession tariff levels; interact post-accession indicator with industry-level tariff change
  required_identifiers:
  - firm ID
  - year
  - industry code (4-digit)
  - ownership type
  spillovers: Trade liberalization creates general equilibrium effects on factor prices, industry composition, and upstream/downstream
    linkages
research_compatibility:
  outcome_domains:
  - firm productivity
  - markups
  - prices
  - output
  - employment
  - entry
  - exit
  - product mix
  affected_populations:
  - Manufacturing firms
  - workers in trade-exposed industries
  - consumers
  mechanism_channels:
  - import competition
  - export market access
  - input tariff reduction
  - pro-competitive effects
  - markup compression
  - productivity improvement
  best_for:
  - Studying the effect of trade liberalization on firm-level productivity and market power
  - understanding how trade affects within-industry reallocation
  not_good_for:
  - Short-run adjustment costs
  - pre-2001 trade reforms
design:
  affordances:
  - sharp accession date
  - cross-industry variation in tariff reductions
  - rich firm-level panel data
  - pre-accession baseline period
  candidate_designs:
  - difference-in-differences with continuous treatment intensity
  - industry-level event study
  identifying_variation: Industry-level variation in the depth of tariff reduction following the common WTO accession date;
    industries with initially higher tariffs experienced a larger liberalization shock
  assumptions:
  - Tariff reductions were driven by WTO commitments
  - not domestic lobbying
  - pre-accession tariff levels are conditionally exogenous to post-accession productivity trends
  - no other concurrent reforms disproportionately affect high-tariff industries
  diagnostics:
  - Test for pre-trends in productivity by industry tariff levels
  - compare MFN tariff changes with bilateral tariff changes
  - use only externally determined (WTO-mandated) tariff changes
  primary_strategy: Difference-in-differences with continuous treatment; production function estimation (proxy methods) for
    TFP; markup estimation using production approach; decomposition of aggregate productivity changes
  estimand: The causal effect of the recorded exposure on Firm total factor productivity, markups, prices, product mix, industry-level
    productivity dispersion, conditional on the stated design assumptions.
  treatment_variable: Post-2001 indicator interacted with industry-level tariff reduction; firm-specific exposure based on
    pre-accession product mix
  comparison_logic: Pre-2001 vs post-2001 within firms; high tariff-reduction industries vs low tariff-reduction industries
  estimation_notes: Difference-in-differences with continuous treatment; production function estimation (proxy methods) for
    TFP; markup estimation using production approach; decomposition of aggregate productivity changes
threats:
- type: concurrent-reforms
  basis: inferred
  condition: The early 2000s saw multiple reforms (SOE restructuring, financial sector reforms, VAT pilot) that may confound
    the WTO effect
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for other reforms
  - use continuous industry-level tariff variation that is specific to WTO commitments
  - compare timing of different reforms
- type: anticipation-effects
  basis: inferred
  condition: Firms may have begun adjusting before 2001 in anticipation of accession, attenuating estimated effects
  evidence_refs:
  - E1
  possible_diagnostics:
  - test for pre-2001 adjustments
  - use multi-year pre-trend tests
  - compare industries with different degrees of accession surprise
empirical_requirements:
  contract_version: 1
  population: Chinese manufacturing firms, 1998–2007
  observation_unit: Firm-year
  geography_level: National (firm-level) with industry variation
  time_start: 1998
  time_end: 2007
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 5
  required_fields:
  - firm output
  - inputs
  - value added
  - employment
  - capital stock
  - industry (4-digit)
  - ownership
  - export status
  - product-level prices and quantities
  required_identifiers:
  - firm ID
  - year
  - industry code
  treatment_key:
  - industry code
  - post-2001 indicator
  - pre-accession output tariff
  - pre-accession input tariff
  - tariff reduction
  treatment_source: WTO tariff schedules matched to Chinese industry classifications; Annual Survey of Industrial Firms (NBS);
    Customs transaction-level trade data for tariff measurement
  measurement_risks:
  - matching tariff lines to industrial classification
  - firm-level output price vs industry-level deflator issues
  - firm entry/exit around accession
evidence:
- id: E1
  source_type: paper
  citation: 'Brandt, Loren, Johannes Van Biesebroeck, Luhang Wang, and Yifan Zhang. 2017. "WTO Accession and Performance of
    Chinese Manufacturing Firms." American Economic Review 107 (9): 2784–2820.'
  url: https://doi.org/10.1257/aer.20121266
  date: 2017
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - productivity analysis
  - markup analysis
  verification_status: verified
design_applications:
- paper: WTO Accession and Performance of Chinese Manufacturing Firms
  doi: 10.1257/aer.20121266
  journal: American Economic Review
  year: 2017
  research_question: How did China's WTO accession affect firm-level productivity, markups, and industry-level resource allocation?
  population: Chinese manufacturing firms, 1998–2007
  outcome: Firm total factor productivity, markups, prices, product mix, industry-level productivity dispersion
  data_used: []
  treatment_encoding: Post-2001 indicator interacted with industry-level tariff reduction; firm-specific exposure based on
    pre-accession product mix
  comparison: Pre-2001 vs post-2001 within firms; high tariff-reduction industries vs low tariff-reduction industries
  empirical_design: Difference-in-differences with continuous treatment; production function estimation (proxy methods) for
    TFP; markup estimation using production approach; decomposition of aggregate productivity changes
  assumptions:
  - tariff reductions exogenous to firm-level productivity trends
  - production function correctly specified
  - markups identified from output elasticities and revenue shares
  threats_addressed:
  - concurrent reforms via continuous treatment approach and timing tests
  - anticipation via pre-trend analysis
  - measurement error via robust production function estimation
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
---
## Institutional Background
Before 2001, China was not a WTO member and faced discriminatory trade treatment including annual MFN renewal in the US, textile quotas under the Multi-Fiber Arrangement, and high tariff barriers. China's WTO accession in December 2001 eliminated these barriers: it locked in permanent MFN status, phased out MFA quotas by 2005, and committed China to substantial tariff reductions averaging from over 40% to under 10%. [E1]

## What Changed
WTO accession dramatically reduced trade barriers facing Chinese firms — both on the export side (permanent MFN eliminated uncertainty, quotas on textiles were phased out) and on the import side (tariffs on inputs and final goods fell). This created a large, plausibly exogenous shock to the competitive environment facing Chinese manufacturers. [E1]

## Implementation and Assignment
All Chinese firms were affected by the post-2001 trade regime, but the intensity of the shock varied by industry: industries with higher pre-accession tariffs experienced larger tariff reductions, and industries subject to MFA quotas (textiles and apparel) experienced a particularly large export-market shock. This cross-industry variation identifies the causal effect of trade liberalization on firm outcomes. [E1]

## Why This Creates Empirical Variation
The combination of a common accession date and cross-industry variation in the depth of liberalization creates a canonical difference-in-differences design. The richness of Chinese firm-level data allows the paper to go beyond standard productivity measurement to estimate the effect of trade liberalization on firm-level markups (market power) and the allocation of resources across firms within industries. [E1; analytical inference]

## Identification Risks
China implemented many other reforms in the early 2000s (SOE privatization, financial reforms, tax changes). Isolating the WTO effect requires the cross-industry tariff variation and careful controls for concurrent policies. Additionally, WTO accession was partially anticipated, so some adjustment may have begun before 2001, attenuating estimated effects. [E1]

## Data Requirements
Firm-level panel data from the Annual Survey of Industrial Firms (1998–2007), product-level output prices and quantities to estimate firm-specific price indices, WTO tariff schedules matched to Chinese industry classifications, and customs transaction data for supplementary trade measures. [E1]

## Evidence Notes
E1 provides comprehensive evidence that WTO accession led to significant productivity gains in Chinese manufacturing, substantial reductions in firm-level markups (particularly in industries with the largest tariff cuts), and improved within-industry resource allocation as more productive firms expanded and less productive firms contracted or exited. The paper provides a structural framework connecting trade liberalization to firm performance and industry efficiency.
