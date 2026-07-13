---
schema_version: 2
id: china-firm-dynamics-reallocation
name: China's Manufacturing Firm Dynamics and the Role of within-Industry Reallocation in Aggregate Productivity Growth (1998–2007)
aliases:
- Roberts Xu Fan Zhang firm dynamics China
- 企业动态 资源配置
- misallocation China manufacturing
- within-industry reallocation China

status: deprecated
provenance:
  task_id: task-e9b64f33e231
scope:
  country: China
  regions:
  - All provinces
  domains:
  - firm
  - productivity
  - industrial-organization
  - development
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: China's economic reforms and market liberalization during the 1998–2007 period, which generated substantial
    within-industry reallocation of resources across heterogeneous firms — entry of new private firms, exit of inefficient
    SOEs, and expansion of productive firms at the expense of less productive ones — with the intensity and nature of this
    reallocation varying across industries and over time
  authority: Market forces combined with government policies (SOE reform, trade liberalization, WTO accession)
  legal_identifiers:
  - SOE restructuring and privatization policies
  - WTO accession (2001)
  - FDI liberalization
  - financial sector reforms
  implementation_regime: 'The 1998–2007 period was one of dramatic structural change in Chinese manufacturing: state-owned
    enterprises were restructured or privatized, private and foreign-invested firms entered and expanded, and market competition
    intensified following WTO accession'
  assignment_mechanism: The key variation is in the intensity of within-industry reallocation (entry, exit, and market share
    shifts across firms with different productivity levels) across industries and time; industries with larger initial distortions
    experienced more reallocation as reforms removed barriers
  parent: null
  related_variations:
  - china-wto-accession-firm-performance
  - china-vat-reform-investment
timeline:
  announcement: null
  effective: null
  implementation_start: 1998
  implementation_end: 2007
  local_timing: Reallocation occurs continuously as firms enter, exit, and adjust market shares; the pace varies across industries
  anticipation: Market liberalization was gradually implemented; individual firms could anticipate increased competition but
    not the precise timing or intensity
  last_verified: '2026-07-13'
assignment:
  unit: Firm and industry
  treated: Firms in industries and periods with more intense reallocation (higher rates of firm entry and exit, larger market
    share shifts from low-productivity to high-productivity firms)
  comparison_pool: Low-reallocation industries or time periods; within-firm comparison before and after major reform events
  rule: Industries with larger initial misallocation (wider within-industry productivity dispersion) have more scope for reallocation-driven
    productivity gains; reforms (WTO, SOE restructuring) enable this reallocation
  intensity: Continuous — industry-year measures of firm entry rate, exit rate, and the covariance between firm size and productivity
    (Olley-Pakes decomposition)
  compliance: Market reallocation is the result of firm decisions, not a policy mandate; firms enter and exit based on profitability
  exemptions: []
  exposure_construction: Construct industry-year measures of reallocation intensity (entry rate, exit rate, job reallocation
    rate, OP decomposition terms); relate these to industry-level and aggregate productivity growth
  required_identifiers:
  - firm ID
  - industry code (4-digit)
  - year
  - entry/exit indicator
  - output
  - inputs
  spillovers: Entry of productive firms may drive exit of incumbents; resource reallocation in one industry affects input
    and output markets for other industries
research_compatibility:
  outcome_domains:
  - productivity
  - firm entry and exit
  - resource allocation
  - market structure
  - aggregate growth
  affected_populations:
  - Manufacturing firms (SOEs
  - private
  - foreign)
  - workers reallocated across firms
  - industries undergoing structural change
  mechanism_channels:
  - within-industry reallocation
  - creative destruction
  - selection
  - productivity convergence
  - entry and exit dynamics
  - market liberalization
  best_for:
  - Decomposing aggregate productivity growth into within-firm and between-firm components
  - understanding how market reforms enable productivity-enhancing reallocation
  not_good_for:
  - Service sector dynamics
  - firm-level analysis without entry/exit tracking
  - periods after 2007
design:
  affordances:
  - rich firm-level panel with entry/exit tracking
  - large sample across all manufacturing
  - major reform events providing temporal variation
  - industry-level heterogeneity in initial distortions
  candidate_designs:
  - Olley-Pakes and related productivity decompositions
  - dynamic Olley-Pakes decomposition
  - industry-level analysis of reallocation and growth
  - entry/exit analysis
  identifying_variation: Cross-industry and time variation in reallocation intensity driven by differential exposure to market-liberalizing
    reforms and differential initial scope for reallocation (size of within-industry productivity gaps)
  assumptions:
  - Firm productivity is measured without systematic error
  - entry and exit are correctly identified in the data
  - reallocation is driven by market forces rather than measurement artifacts
  - no spurious relationship between measured reallocation and growth
  diagnostics:
  - Sensitivity to alternative productivity measures
  - test for measurement-error-driven reallocation
  - verify entry/exit definitions
  - compare reallocation measures with policy reform timing
  primary_strategy: Dynamic Olley-Pakes decomposition of aggregate productivity growth; analysis of the contribution of continuing
    firms, entrants, and exiting firms; industry-level and aggregate-level decomposition
  estimand: The causal effect of the recorded exposure on Aggregate manufacturing productivity growth, decomposed into within-firm,
    between-firm (reallocation), entry, and exit components, conditional on the stated design assumptions.
  treatment_variable: Not a treatment per se; the analysis decomposes productivity growth into components attributable to
    different firm dynamics (within-firm growth, between-firm reallocation, entry, exit)
  comparison_logic: Industries by reallocation intensity; time periods by reform intensity; comparison of actual growth with
    counterfactual no-reallocation growth
  estimation_notes: Dynamic Olley-Pakes decomposition of aggregate productivity growth; analysis of the contribution of continuing
    firms, entrants, and exiting firms; industry-level and aggregate-level decomposition
threats:
- type: measurement-error-in-productivity
  basis: inferred
  condition: Apparent reallocation may partly reflect measurement error; if measured productivity differences across firms
    contain noise, estimated reallocation contributions to growth may be overstated
  evidence_refs:
  - E1
  possible_diagnostics:
  - use multiple productivity estimation methods
  - control for measurement error
  - compare with physical productivity measures where available
- type: data-attrition
  basis: inferred
  condition: Firm exit from the survey may reflect survey attrition rather than true economic exit; entry may reflect survey
    coverage expansion
  evidence_refs:
  - E1
  possible_diagnostics:
  - cross-validate with administrative records
  - use consistent sample definitions
  - test sensitivity to entry/exit definitions
empirical_requirements:
  contract_version: 1
  population: All Chinese manufacturing firms above designated size, 1998–2007
  observation_unit: Firm-year
  geography_level: National (firm-level) with industry variation
  time_start: 1998
  time_end: 2007
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 3
  required_fields:
  - firm output
  - value added
  - capital
  - labor
  - intermediate inputs
  - industry code
  - ownership type
  - entry year
  - exit year
  required_identifiers:
  - firm ID
  - year
  - industry code
  treatment_key:
  - industry code
  - year
  - entry rate
  - exit rate
  - OP covariance term
  - reallocation intensity measure
  treatment_source: Annual Survey of Industrial Firms (National Bureau of Statistics); firm-level data on output, inputs,
    ownership, and industry classification
  measurement_risks:
  - output and input deflators varying across firms
  - capital stock measurement
  - firm ID changes due to restructuring or mergers
  - survey coverage changes over time
  - exit vs attrition distinction
evidence:
- id: E1
  source_type: paper
  citation: 'Roberts, Mark J., Daniel Yi Xu, Xiaoyan Fan, and Shengxing Zhang. 2018. "The Role of Firm Factors in China''s
    Manufacturing Growth: A Dynamic Decomposition of Aggregate Productivity." Review of Economic Studies 85 (1): 292–327.'
  url: https://doi.org/10.1093/restud/rdx039
  date: 2018
  supports:
  - identity
  - assignment
  - design
  - productivity decomposition
  - reallocation analysis
  verification_status: verified
design_applications:
- paper: The Role of Firm Factors in China's Manufacturing Growth
  doi: 10.1093/restud/rdx039
  journal: Review of Economic Studies
  year: 2018
  research_question: How much of China's manufacturing productivity growth is driven by within-firm improvement versus across-firm
    reallocation?
  population: Chinese manufacturing firms above designated size, 1998–2007
  outcome: Aggregate manufacturing productivity growth, decomposed into within-firm, between-firm (reallocation), entry, and
    exit components
  data_used:
  - Annual Survey of Industrial Firms (NBS)
  - Firm-level production data
  treatment_encoding: Not a treatment per se; the analysis decomposes productivity growth into components attributable to
    different firm dynamics (within-firm growth, between-firm reallocation, entry, exit)
  comparison: Industries by reallocation intensity; time periods by reform intensity; comparison of actual growth with counterfactual
    no-reallocation growth
  empirical_design: Dynamic Olley-Pakes decomposition of aggregate productivity growth; analysis of the contribution of continuing
    firms, entrants, and exiting firms; industry-level and aggregate-level decomposition
  assumptions:
  - firm productivity correctly measured
  - entry/exit correctly identified
  - decomposition correctly attributes growth to components
  - no general equilibrium feedback from reallocation to within-firm productivity
  threats_addressed:
  - measurement error via multiple productivity methods
  - entry/exit definition via cross-validation
  - decomposition sensitivity via alternative approaches
  evidence_refs:
  - E1
readiness_blockers:
- "Catalog admissibility is unresolved: productivity decomposition is not itself an assignment-generating variation."
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
method_transfer: null
superseded_by: null
deprecation_reason: Productivity decomposition without a recoverable assignment-generating feature.
---
## Institutional Background
China's manufacturing sector underwent a dramatic transformation between 1998 and 2007. State-owned enterprises (SOEs) were restructured or privatized, private firms entered and expanded, foreign direct investment surged, and WTO accession in 2001 opened Chinese markets to international competition. These reforms created conditions for market-driven reallocation: more productive firms should expand and less productive ones should contract or exit. Whether and how much this reallocation contributed to China's remarkable productivity growth is a central empirical question. [E1]

## What Changed
The reforms of the late 1990s and early 2000s removed barriers to firm entry (licensing requirements, SOE monopolies), exit (hard budget constraints for SOEs), and expansion (access to credit and export markets for private firms). As these barriers fell, within-industry reallocation intensified: high-productivity firms gained market share, low-productivity firms lost share or exited, and new entrants brought new technologies and business models. [E1]

## Implementation and Assignment
The key variation is not a discrete treatment but the continuous process of within-industry reallocation across heterogeneous firms. The paper decomposes aggregate productivity growth into components attributable to within-firm improvement, between-firm reallocation among continuing firms, and the contributions of entering and exiting firms. [E1]

## Why This Creates Empirical Variation
The decomposition reveals whether growth is driven by all firms improving equally (within-firm) or by the market selecting better firms and eliminating worse ones (reallocation). The distinction has important policy implications: if reallocation is the main driver, policies that facilitate firm entry and exit are crucial for sustaining growth. [E1; analytical inference]

## Identification Risks
The decomposition is an accounting exercise, not a causal identification strategy. The measured importance of reallocation depends on productivity measurement, firm classification, and decomposition methodology. If firm productivity is measured with error, the reallocation component may be overstated. [E1]

## Data Requirements
Annual firm-level panel data on all manufacturing firms above a designated size threshold, including output, value added, capital, labor, intermediate inputs, industry classification, ownership type, and entry/exit indicators. Consistent firm identifiers to track firms over time and correctly identify entry and exit. [E1]

## Evidence Notes
E1 provides a comprehensive decomposition of China's manufacturing productivity growth. The analysis shows that within-firm productivity improvement and between-firm reallocation both contributed substantially to growth, with reallocation playing an increasingly important role as reforms progressed. The dynamic decomposition framework allows tracking how the importance of different growth channels evolved over the reform period.

## Deprecation Notice

**Deprecated 2026-07-13 (task-e9b64f33e231)**: This record has been deprecated following a catalog admissibility audit. The paper (Roberts, Xu, Fan, Zhang) is a productivity decomposition exercise using Olley-Pakes and dynamic Olley-Pakes methods — it measures and documents the contribution of within-industry reallocation to aggregate manufacturing TFP growth during 1998–2007. It does not possess a recoverable assignment-generating feature: there is no externally assigned treatment, no policy variation, no instrument, no threshold, no boundary, and no randomization. The within-industry reallocation intensity is an endogenous market outcome, not a manipulable assignment mechanism. Productivity decompositions are valuable descriptive tools but do not constitute causal variation under NIEL's admissibility criteria. This record is preserved for reference but excluded from recommendation pathways. [analytical inference]
