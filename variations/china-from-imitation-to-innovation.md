---
schema_version: 2
id: china-from-imitation-to-innovation
name: China's Transition from Imitation to Innovation-Driven Growth through Industrial Policy and Resource Reallocation (2000s–2010s)
aliases:
- Konig Song Storesletten Zilibotti imitation innovation China
- 中国产业政策 模仿创新
- industrial policy China innovation
- catching up China

status: contested
provenance:
  task_id: task-e9b64f33e231
scope:
  country: China
  regions:
  - All provinces
  domains:
  - industrial-policy
  - innovation
  - firm
  - growth
  - technology
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: China's industrial policy interventions — including subsidies, tax incentives, credit allocation, and R&D support
    — that differentially affect firms depending on their distance from the technological frontier, creating variation in
    firms' incentives to imitate existing technologies versus develop new innovations
  authority: Chinese government (NDRC, MOST, Ministry of Industry and Information Technology, local governments)
  legal_identifiers:
  - Medium and Long-Term S&T Development Plan (2006–2020)
  - Strategic Emerging Industries initiative
  - Made in China 2025
  - indigenous innovation policies
  - R&D tax deductions and subsidies
  implementation_regime: Chinese industrial policy shifted over time from supporting catch-up through technology transfer
    and imitation (1990s–2000s) toward promoting indigenous innovation (2010s), with different policy instruments creating
    heterogeneous effects across firms at different distances from the technological frontier
  assignment_mechanism: Firm exposure to industrial policies varies by industry, ownership type, and technological level;
    the key variation is in firms' distance from the global technological frontier, which determines whether imitation or
    innovation is the optimal strategy and how industrial policy affects their incentives
  parent: null
  related_variations:
  - china-vat-reform-investment
  - china-wto-accession-firm-performance
  - china-growing-like-china
timeline:
  announcement: null
  effective: null
  implementation_start: 2000
  implementation_end: 2018
  local_timing: Industrial policies were introduced at different times across different industries and regions
  anticipation: Large-scale industrial policy plans were announced in Five-Year Plans and S&T plans; individual firms could
    anticipate support but could not control its allocation
  last_verified: '2026-07-13'
assignment:
  unit: Firm and industry
  treated: Firms receiving industrial policy support (subsidies, tax benefits, credit access, R&D grants); treatment effects
    vary with firm distance from the technological frontier
  comparison_pool: Non-supported firms in the same industry; firms in industries with less policy support; within-firm variation
    before and after policy changes
  rule: Industrial policy support is allocated based on a combination of government priorities (strategic industries, indigenous
    innovation goals) and firm characteristics (size, ownership, technological capability); firms closer to the frontier face
    different innovation incentives than those far from it
  intensity: Continuous — amount of subsidies, tax reduction, preferential credit; distance from the global technological
    frontier (measured by TFP or patent stock relative to frontier firms)
  compliance: Policy support allocation is determined by government decisions; firms cannot self-select into receiving support
  exemptions: []
  exposure_construction: Code firm-year indicators for receiving specific types of industrial policy support; interact policy
    support with firm distance from the technological frontier; use industry-level variation in policy intensity as an alternative
    source of identification
  required_identifiers:
  - firm ID
  - industry code
  - year
  - ownership type
  - policy support indicators
  spillovers: Support for some firms may affect competitors through product market competition, input prices, and technology
    spillovers; knowledge diffusion from frontier to non-frontier firms
research_compatibility:
  outcome_domains:
  - innovation
  - patenting
  - productivity
  - R&D investment
  - technology adoption
  - firm growth
  - industrial upgrading
  affected_populations:
  - Chinese manufacturing and technology firms
  - R&D-intensive industries
  - state-owned and private enterprises
  mechanism_channels:
  - resource reallocation toward innovation
  - reduced imitation incentives
  - technology gap dynamics
  - competition and selection
  - knowledge spillovers
  - policy-driven structural change
  best_for:
  - Studying how industrial policy affects the composition of innovation (imitation vs novel innovation)
  - understanding China's transition from catch-up growth to frontier innovation
  not_good_for:
  - Short-run employment effects
  - service sector innovation
  - cross-country comparisons without similar policy data
design:
  affordances:
  - firm-level panel data with innovation measures
  - variation in policy support across firms and time
  - distance-from-frontier heterogeneity
  - rich patent and productivity data
  candidate_designs:
  - difference-in-differences comparing supported vs non-supported firms
  - heterogeneity analysis by distance from frontier
  - structural estimation of innovation model
  identifying_variation: Firm-level variation in industrial policy support interacted with firm distance from the technological
    frontier; the key prediction is that policy support has heterogeneous effects depending on whether firms are catching
    up (imitation optimal) or at the frontier (innovation optimal)
  assumptions:
  - Policy support allocation is conditionally exogenous to firm innovation trajectories
  - distance from frontier is measured accurately
  - no other concurrent shocks differentially affect frontier vs non-frontier firms
  diagnostics:
  - Test for pre-trends in innovation by policy support status
  - compare firms just above and below policy eligibility thresholds
  - test for heterogeneous effects by initial distance from frontier
  - validate distance-from-frontier measurement
  primary_strategy: Panel analysis with firm and year fixed effects; heterogeneity analysis by distance from technological
    frontier; structural model of firm innovation choice between imitation and innovation
  estimand: The causal effect of the recorded exposure on Patenting rates (total, invention, utility model, design), patent
    quality (citations, originality), firm productivity, R&D expenditure, conditional on the stated design assumptions.
  treatment_variable: Firm-year indicators for industrial policy support; interaction of policy support with firm distance
    from the technological frontier
  comparison_logic: Supported vs non-supported firms; firms at different distances from the frontier; within-firm changes
    in innovation type after policy changes
  estimation_notes: Panel analysis with firm and year fixed effects; heterogeneity analysis by distance from technological
    frontier; structural model of firm innovation choice between imitation and innovation
threats:
- type: endogenous-policy-allocation
  basis: inferred
  condition: Industrial policy support is not randomly assigned; supported firms may be systematically different (more innovative,
    better connected) from non-supported firms
  evidence_refs:
  - E1
  possible_diagnostics:
  - use policy eligibility rules as instruments
  - compare firms around eligibility thresholds (RDD)
  - control for firm fixed effects
  - match on pre-policy characteristics
- type: measurement-of-frontier-distance
  basis: inferred
  condition: The distance from the technological frontier is a theoretical construct that must be operationalized; measurement
    choices (TFP, patents, citations) may affect conclusions
  evidence_refs:
  - E1
  possible_diagnostics:
  - use multiple frontier-distance measures
  - test sensitivity to frontier definition
  - compare with alternative technology-gap measures
empirical_requirements:
  contract_version: 1
  population: Chinese manufacturing and technology firms, ~2000–2018
  observation_unit: Firm-year
  geography_level: National (firm-level)
  time_start: 2000
  time_end: 2018
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 5
  required_fields:
  - firm patents (counts
  - citations
  - type)
  - R&D expenditure
  - TFP
  - output
  - employment
  - capital
  - industry
  - ownership
  - policy support indicators
  - subsidy amounts
  - tax benefits
  required_identifiers:
  - firm ID
  - year
  - industry code
  treatment_key:
  - firm ID
  - year
  - policy support indicator
  - distance from frontier
  - policy × frontier interaction
  treatment_source: China Patent Office (SIPO) patent data matched to firms; Annual Survey of Industrial Firms; listed firm
    financial data; government subsidy and policy support records; global patent data for frontier definition
  measurement_risks:
  - patent quality heterogeneity
  - strategic patenting by Chinese firms
  - matching patents to firm identifiers
  - defining the global technological frontier
  - distinguishing imitation from innovation in patent data
evidence:
- id: E1
  source_type: paper
  citation: 'König, Michael, Zheng Michael Song, Kjetil Storesletten, and Fabrizio Zilibotti. 2022. "From Imitation to Innovation:
    Where Is All That Chinese R&D Going?" Econometrica 90 (4): 1615–1654.'
  url: https://doi.org/10.3982/ECTA18586
  date: 2022
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - structural model
  - innovation analysis
  verification_status: verified
design_applications:
- paper: 'From Imitation to Innovation: Where Is All That Chinese R&D Going?'
  doi: 10.3982/ECTA18586
  journal: Econometrica
  year: 2022
  research_question: How does China's industrial policy affect the allocation of R&D resources between imitation activities
    and genuine innovation?
  population: Chinese manufacturing and technology firms, ~2000–2018
  outcome: Patenting rates (total, invention, utility model, design), patent quality (citations, originality), firm productivity,
    R&D expenditure
  data_used:
  - SIPO patent database matched to Chinese firms
  - Annual Survey of Industrial Firms
  - Firm financial data for listed companies
  - USPTO and global patent data for frontier definition
  treatment_encoding: Firm-year indicators for industrial policy support; interaction of policy support with firm distance
    from the technological frontier
  comparison: Supported vs non-supported firms; firms at different distances from the frontier; within-firm changes in innovation
    type after policy changes
  empirical_design: Panel analysis with firm and year fixed effects; heterogeneity analysis by distance from technological
    frontier; structural model of firm innovation choice between imitation and innovation
  assumptions:
  - policy support conditionally exogenous
  - distance from frontier correctly measured
  - patent-based measures capture innovation and imitation
  - structural model correctly specified
  threats_addressed:
  - endogenous policy allocation via fixed effects and matching
  - frontier measurement via multiple measures
  - patent quality heterogeneity via citation-weighted measures
  - structural interpretation via model comparison
  evidence_refs:
  - E1
readiness_blockers:
- "Admissibility audit (task-e9b64f33e231, 2026-07-13): The paper (König, Song, Storesletten, Zilibotti) combines structural
  estimation with heterogeneity analysis by distance to the technology frontier. Firm exposure to industrial policies is endogenously
  allocated (by industry, ownership, and technological level), not externally assigned. Distance to the global technology
  frontier is a firm characteristic, not an assignment mechanism. The industrial policy dimension may conceptually overlap
  with china-rd-tax-notch (HNTE program), but this paper does not provide a separable identification strategy. Kept contested
  as a low-priority lead; do not invest in grounding."
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
method_transfer: null
---
## Institutional Background
For decades after opening-up began in 1978, China's economic growth was driven by catch-up: importing foreign technology, imitating products developed elsewhere, and competing on cost rather than novelty. By the 2010s, as China approached the global technological frontier in many industries, this growth model faced diminishing returns. The Chinese government responded with ambitious industrial policies aimed at promoting "indigenous innovation" — shifting from copying to creating. Whether these policies have been effective is a central question for understanding China's growth prospects. [E1]

## What Changed
Chinese industrial policy evolved from supporting technology transfer and imitation toward subsidizing R&D and patenting with the explicit goal of fostering indigenous innovation. The key variation exploited is the fact that the optimal innovation strategy — imitation versus novel innovation — depends on a firm's distance from the technological frontier. Firms far from the frontier benefit more from imitation, while those near the frontier need genuine innovation to advance. Industrial policies may have very different effects depending on where firms are in this spectrum. [E1]

## Implementation and Assignment
The paper uses China's massive increase in R&D spending and patenting to study resource allocation across imitation and innovation activities. It distinguishes between different patent types (invention patents requiring novelty, utility model patents with lower standards) and develops a structural model where firms choose between imitation and innovation. The key empirical variation is in how policy support affects firms at different distances from the frontier. [E1]

## Why This Creates Empirical Variation
If industrial policy indiscriminately subsidizes R&D, it may increase patenting without increasing genuine innovation — firms may "game" the system by patenting imitative activities. The distance-from-frontier heterogeneity provides a test: if policy is effective, it should disproportionately increase genuine innovation by firms near the frontier, where the returns to innovation exceed the returns to imitation. [E1; analytical inference]

## Identification Risks
Industrial policy support is not randomly assigned — supported firms and industries are selected by the government based on technological promise, political connections, and other factors. Separating the causal effect of policy from selection requires careful econometric approaches. Patent-based measures of innovation may overstate genuine technological progress if firms respond to policy incentives by patenting low-quality "innovations." [E1; analytical inference]

## Data Requirements
Comprehensive patent data from SIPO (and global patent offices for frontier definition) matched to Chinese firm identifiers, firm-level financial and production data from the Annual Survey of Industrial Firms and listed company databases, detailed information on industrial policy support (subsidies, tax benefits, credit allocation) by firm and year, and R&D expenditure data. [E1]

## Evidence Notes
E1 provides structural evidence on the allocation of Chinese R&D between imitation and innovation. The paper documents that a significant portion of Chinese R&D spending goes toward imitation activities rather than genuine innovation, and that industrial policy incentives may have contributed to this pattern by rewarding patent quantity over patent quality. The findings have important implications for understanding whether and how China can transition from imitation-driven to innovation-driven growth.
