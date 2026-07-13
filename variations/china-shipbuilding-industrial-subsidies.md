---
schema_version: 2
id: china-shipbuilding-industrial-subsidies
name: Detection and Impact of Industrial Subsidies in China's Shipbuilding Industry
aliases:
- Kalouptsidi Chinese shipbuilding subsidies
- China shipbuilding industrial policy REStud

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - China and global shipbuilding markets; China
  - Japan
  - South Korea
  - and European shipbuilding industries
  domains:
  - industrial-policy
  - international-trade
  - public-economics
  - firm-dynamics
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: Government subsidies to China's shipbuilding industry, including state-directed lending, export credits, loan
    guarantees, and direct subsidies that reduced shipyard costs by 13–20% between 2006 and 2012, creating exogenous variation
    in shipbuilding costs across countries and over time
  authority: Chinese central government (State Council, National Development and Reform Commission, Ministry of Industry and
    Information Technology, China Development Bank) and provincial/local governments
  legal_identifiers:
  - Shipbuilding Industry Medium and Long-term Development Plan (2006-2015)
  - Several Opinions on Accelerating the Development of the Shipbuilding Industry (2006)
  - Ship Industry Adjustment and Revitalization Plan (2009)
  - Made in China 2025 (2015) – shipbuilding component
  implementation_regime: Subsidies were implemented through multiple channels including policy bank lending at below-market
    rates, export credits, loan guarantees, interest rate subsidies, government-directed consolidation, and direct cash subsidies
    to shipyards; the exact magnitude and form of subsidies varied over time and across firms
  assignment_mechanism: Subsidy policy was determined at the national level but implemented through state-owned banks and
    local governments; exposure varies across countries (China vs. competitors), over time (pre- and post-subsidy periods),
    and across ship types depending on Chinese production specialization
  parent: null
  related_variations: []
timeline:
  announcement: '2006-01-01'
  effective: '2006-01-01'
  implementation_start: 2006
  implementation_end: 2012
  local_timing: Implementation varied across subsidy instruments (policy bank lending, export credits, direct subsidies) and
    firms; the analysis period covers 2006–2012
  anticipation: The 2006 government plans signaled intent to support shipbuilding, but the full scale of subsidization only
    became apparent over time as policy banks extended credit and various subsidy programs were rolled out
  last_verified: '2026-07-13'
assignment:
  unit: Shipyard-country-year or ship-type-country-year
  treated: Chinese shipyards (relative to foreign competitors) after the introduction of shipbuilding subsidies beginning
    in 2006
  comparison_pool: Shipyards in other major shipbuilding countries (Japan, South Korea, European countries) that did not receive
    Chinese subsidies; pre-subsidy periods for Chinese shipyards; variation across ship types with differential Chinese specialization
  rule: Chinese shipyards received subsidies that reduced their costs by 13–20%; the extent of subsidization is inferred from
    a structural model that uses data on ship production, prices, entry, exit, and costs across countries
  intensity: Continuous — the estimated cost reduction (13–20% subsidy equivalent) varies by ship type and over time depending
    on the intensity of Chinese industrial policy interventions
  compliance: High for the Chinese government's policy direction; state-owned banks and local governments generally complied
    with central government directives to support the shipbuilding industry
  exposure_construction: Estimate cost subsidies using a dynamic structural model of entry, exit, and production; code post-2006
    Chinese shipyards as potentially subsidized, with the magnitude of the subsidy inferred from the model as the difference
    between observed costs and costs predicted under competitive conditions
  required_identifiers:
  - country
  - shipyard ID
  - year
  - ship type
  - production quantity
  - price
  - entry/exit status
  exemptions: []
  spillovers: Chinese subsidies led to substantial reallocation of global ship production, with Japanese shipyards losing
    significant market share; subsidies also affected world ship prices and may have depressed shipyard profits in competitor
    countries
research_compatibility:
  outcome_domains:
  - industrial output
  - market share
  - firm entry and exit
  - production costs
  - prices
  - consumer surplus
  - welfare
  - trade patterns
  affected_populations:
  - Chinese shipyards
  - foreign shipyards (Japan
  - South Korea
  - Europe)
  - ship buyers (shipping companies)
  - workers in shipbuilding industry
  mechanism_channels:
  - cost reduction
  - credit access
  - export promotion
  - industrial consolidation
  - state-directed investment
  - production reallocation
  best_for:
  - Studying the effects of industrial subsidies on production reallocation
  - estimating subsidy pass-through to prices and output
  - welfare analysis of industrial policy
  not_good_for:
  - Short-run causal estimation without structural model
  - micro-level outcomes lacking shipyard-level data
  - non-tradable sectors
design:
  affordances:
  - cross-country variation in subsidy exposure
  - time variation (pre vs. post Chinese policy)
  - cross-ship-type variation
  - structural model allowing counterfactual simulations
  candidate_designs:
  - structural estimation of dynamic entry/exit model with subsidy detection
  - difference-in-differences comparing Chinese vs. foreign shipbuilding outcomes
  - event study around major policy announcements
  identifying_variation: Variation across countries (China vs. Japan vs. South Korea vs. Europe), across time (before and
    after 2006 Chinese industrial policy), and across ship types in Chinese production specialization; the structural model
    identifies subsidies from discrepancies between observed production patterns and those predicted under undistorted competition
  assumptions:
  - The dynamic model correctly captures firm behavior (entry
  - exit
  - production decisions)
  - the production technology is correctly specified
  - unobserved cost shocks are orthogonal to policy timing
  - the subsidy estimates are identified through the model structure and cross-country variation
  diagnostics:
  - Model fit tests
  - comparison of model predictions to observed moments
  - sensitivity analysis to alternative model specifications
  - placebo tests on periods before major subsidy programs
  primary_strategy: Structural estimation of a dynamic oligopoly model with endogenous entry, exit, and production; reduced-form
    event studies and difference-in-differences for validation
  estimand: The causal effect of the recorded exposure on Production quantity, market share, prices, costs, entry, exit, consumer
    surplus, conditional on the stated design assumptions.
  treatment_variable: China indicator interacted with post-2006 indicator; subsidy magnitude estimated from structural model
  comparison_logic: Chinese vs. foreign shipyards before and after subsidy programs began
  estimation_notes: Structural estimation of a dynamic oligopoly model with endogenous entry, exit, and production; reduced-form
    event studies and difference-in-differences for validation
threats:
- type: model-dependence
  basis: documented
  condition: The subsidy estimates and welfare conclusions depend on the structural model assumptions about firm behavior,
    production technology, and market structure
  evidence_refs:
  - E1
  possible_diagnostics:
  - sensitivity analysis to modeling assumptions
  - alternative estimation approaches
  - comparison with reduced-form evidence
  - out-of-sample validation
- type: confounding-policies
  basis: inferred
  condition: China's shipbuilding subsidies were part of a broader industrial policy package that included infrastructure
    investment, technology transfer requirements, and trade policies that may independently affect shipbuilding outcomes
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for other Chinese industrial policies
  - examine heterogeneous effects across subsidy instruments
  - test for breaks in outcomes around specific policy announcements
- type: global-financial-crisis
  basis: documented
  condition: The 2008 global financial crisis caused a major contraction in world shipbuilding demand and trade, which differentially
    affected countries and ship types and coincided with intensified Chinese subsidy programs
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for global demand shocks
  - compare Chinese and non-Chinese outcomes controlling for time effects
  - robustness to excluding crisis years
empirical_requirements:
  contract_version: 1
  population: Global shipbuilding industry, 1990–2012
  observation_unit: Shipyard-year or country-ship type-year
  geography_level: Country (with shipyard-level data)
  time_start: 1990
  time_end: 2012
  minimum_frequency: annual
  minimum_pre_periods: 5
  minimum_post_periods: 3
  required_fields:
  - country
  - shipyard ID
  - year
  - ship type
  - production quantity
  - price
  - entry/exit status
  - shipyard costs
  required_identifiers:
  - shipyard ID
  - country
  - year
  - ship type
  treatment_key:
  - China indicator
  - post-2006 indicator
  - China × post-2006 interaction
  treatment_source: Lloyd's Register of Ships (ship production data), shipyard capacity and cost data from industry sources,
    government policy documents, policy bank lending records
  measurement_risks:
  - measurement of subsidy magnitudes requires structural model inference
  - shipyard cost data may be incomplete or measured with error
  - ship production data may miss small yards or non-reporting yards in China
evidence:
- id: E1
  source_type: paper
  citation: 'Kalouptsidi, Myrto. 2018. "Detection and Impact of Industrial Subsidies: The Case of Chinese Shipbuilding." Review
    of Economic Studies 85 (2): 1111–1158.'
  url: https://doi.org/10.1093/restud/rdx050
  date: 2018
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - subsidy detection
  - welfare analysis
  - production reallocation
  verification_status: verified
design_applications:
- paper: 'Detection and Impact of Industrial Subsidies: The Case of Chinese Shipbuilding'
  doi: 10.1093/restud/rdx050
  journal: Review of Economic Studies
  year: 2018
  research_question: How large are Chinese shipbuilding subsidies, and what are their effects on global production reallocation,
    prices, costs, and welfare?
  population: Global shipbuilding industry, 1990–2012
  outcome: Production quantity, market share, prices, costs, entry, exit, consumer surplus
  data_used: []
  treatment_encoding: China indicator interacted with post-2006 indicator; subsidy magnitude estimated from structural model
  comparison: Chinese vs. foreign shipyards before and after subsidy programs began
  empirical_design: Structural estimation of a dynamic oligopoly model with endogenous entry, exit, and production; reduced-form
    event studies and difference-in-differences for validation
  assumptions:
  - Model correctly captures firm dynamics and production technology
  - subsidies are the main source of cost differences between China and competitors after 2006
  - no other major shocks differentially affect Chinese shipbuilding
  threats_addressed:
  - measurement of unobserved subsidies via structural model
  - endogeneity of policy via cross-country and time variation
  - general equilibrium effects via model counterfactuals
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
---
## Institutional Background

The global shipbuilding industry has traditionally been dominated by Japan, South Korea, and European countries. Beginning in 2006, China's central government designated shipbuilding as a strategic industry and implemented a comprehensive set of industrial policies to support its development. These included policy bank lending at below-market rates through China Development Bank, export credits, loan guarantees, interest rate subsidies, government-directed consolidation of state-owned shipyards, and direct cash subsidies. The scale of these interventions was not transparently reported, creating the need for model-based detection of subsidy magnitudes. [E1]

## What Changed

Between 2006 and 2012, China's shipbuilding subsidies reduced shipyard costs by an estimated 13–20%, equivalent to US$1.5–4.5 billion. This cost advantage triggered a massive reallocation of global ship production toward China, with China's global market share rising dramatically. The subsidies affected entry of new Chinese shipyards, expansion of existing yards, and pricing behavior. The paper detects these subsidies using a structural econometric model that infers the subsidy amount from observed production, pricing, entry, and exit patterns relative to the predictions of an undistorted competitive model. [E1]

## Implementation and Assignment

Subsidies were implemented through multiple, overlapping channels: state-owned policy banks extended credit to shipyards at below-market rates, government entities provided loan guarantees and export credits, and local governments offered direct subsidies and tax incentives. The assignment of subsidies was not random — the Chinese government targeted the shipbuilding sector as a whole, and specific firms received different levels of support based on their ownership structure (state-owned vs. private), size, and relationship with local governments. The paper's identification strategy relies on comparing Chinese shipbuilding outcomes to those in other countries before and after the policy, combined with a structural model that accounts for industry dynamics. [E1]

## Why This Creates Empirical Variation

The introduction of large-scale shipbuilding subsidies in China after 2006 generates variation across three dimensions: (1) cross-country: Chinese shipyards received subsidies while those in Japan, South Korea, and Europe did not; (2) time series: pre-2006 vs. post-2006 periods; and (3) cross-ship-type: variation in Chinese specialization across different vessel types. The structural model uses this multi-dimensional variation to detect the subsidy magnitude by finding the cost reduction that best rationalizes observed production patterns, entry/exit dynamics, and pricing behavior. [E1; analytical inference]

## Identification Risks

The main identification challenge is separating the effects of subsidies from other concurrent changes in China's shipbuilding sector, including technological catch-up, infrastructure improvements, labor cost advantages, and broader economic growth. The Chinese shipbuilding policy was also explicitly counter-cyclical, intensifying during the 2008 global financial crisis when world ship demand collapsed, creating a correlation between subsidy timing and demand shocks. The structural model addresses these concerns through modeling assumptions, but the results depend on the credibility of those assumptions. [E1; analytical inference]

## Data Requirements

Comprehensive panel data on the global shipbuilding industry: ship-level production data (quantity, type, price, delivery date) from Lloyd's Register of Ships; shipyard-level characteristics (capacity, ownership, location); industry cost estimates; government policy documents and budget data; entries and exits of shipyards over time. The structural estimation also requires data on ship buyer characteristics and market structure variables. [E1]

## Evidence Notes

E1 develops a novel methodology for detecting subsidies when their magnitude is not directly observable. The paper finds that Chinese subsidies led to substantial reallocation of production away from Japan, while having more modest effects on South Korea and Europe. The welfare analysis shows that the subsidies generated only small surplus gains for ship buyers relative to their fiscal cost, suggesting significant deadweight loss. The paper's structural approach allows counterfactual simulations of alternative subsidy designs and has been influential in the subsequent industrial policy literature.
