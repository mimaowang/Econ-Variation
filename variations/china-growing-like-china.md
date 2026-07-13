---
schema_version: 2
id: china-growing-like-china
name: Growing Like China — Firm Heterogeneity, Financial Frictions, and Macroeconomic Growth
aliases:
- Song Storesletten Zilibotti 2011
- China growth model
- firm heterogeneity China
- two-sector China model
- SOE vs private firm productivity China

status: deprecated
provenance:
  task_id: task-e9b64f33e231
scope:
  country: China
  regions:
  - China (national economy)
  domains:
  - growth
  - macroeconomics
  - firm-heterogeneity
  - financial-frictions
  - development
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: Firm-level heterogeneity in productivity and financial constraints between China's high-productivity entrepreneurial
    (private) firms and low-productivity state-owned enterprises (SOEs), generating variation in the allocation of capital
    and labor across firm types over time
  authority: Not a policy intervention; the variation arises from the co-existence of two firm types with differential access
    to credit markets and productivity levels, embedded in China's institutional and financial system
  legal_identifiers:
  - SOE preferential lending policies
  - private firm credit constraints
  - Chinese banking regulations
  - foreign direct investment restrictions
  implementation_regime: 'The Chinese economy features a persistent dual structure:  a low-productivity state sector with
    preferential access to bank credit,  and a high-productivity private/entrepreneurial sector facing binding financial constraints.  This
    institutional arrangement persisted from the 1990s through the 2000s

    '
  assignment_mechanism: Firm type (SOE vs private/entrepreneurial) is determined by ownership structure and registration status;
    within each sector, productivity is heterogeneous across firms. The financial friction regime (preferential credit for
    SOEs) is a structural feature of China's financial system
  parent: null
  related_variations:
  - china-misallocation-trade-liberalization
timeline:
  announcement: null
  effective: null
  implementation_start: 1990
  implementation_end: 2009
  local_timing: The dual-sector structure with differential financial frictions is a persistent feature of China's reform-era
    economy, gradually evolving over the 1990s and 2000s as SOEs were restructured and private firms expanded
  anticipation: The dual-sector structure is a long-standing institutional feature, not a discrete shock; its evolution was
    shaped by gradual reform processes rather than anticipated discrete policy changes
  last_verified: '2026-07-13'
assignment:
  unit: Firm (within the Chinese economy)
  treated: High-productivity entrepreneurial (private) firms that face binding financial constraints and limited access to
    credit, compared to low-productivity SOEs with preferential credit access
  comparison_pool: Within the economy, variation across firms in productivity level and ownership type (state-owned vs private)
    generates differential growth dynamics and resource allocation patterns
  rule: Firms are classified by ownership type (SOE, private/entrepreneurial, foreign-invested) and productivity level; the
    key variation is the interaction between firm-level productivity and the degree of financial constraint faced by the firm's
    ownership category
  intensity: Continuous — firm-level total factor productivity (TFP), firm-level access to credit (debt-to-asset ratio, interest
    rate paid), and the aggregate share of SOEs vs private firms in the economy over time
  exemptions: []
  compliance: The dual-sector structure is a feature of the economic system, not a policy treatment; compliance is not applicable
  exposure_construction: Firm-level productivity measures (TFP or revenue-based productivity) interacted with ownership-type
    indicators; aggregate measures include the share of private employment, share of SOE output, and intersectoral capital
    flows
  required_identifiers:
  - firm identifier
  - year
  - firm ownership type
  - firm TFP
  - firm employment
  - firm capital stock
  - firm output
  - firm debt and interest payments
  spillovers: Resource reallocation between sectors (labor and capital flows from SOEs to private firms) is a key mechanism
    of the model; aggregate spillovers through factor prices (wages, interest rates) and competition in product markets
research_compatibility:
  outcome_domains:
  - economic growth
  - aggregate productivity
  - capital accumulation
  - structural transformation
  - resource allocation
  - savings rates
  - current account
  affected_populations:
  - Chinese firms (SOEs and private enterprises)
  - Chinese workers
  - aggregate Chinese economy
  mechanism_channels:
  - financial frictions
  - credit market segmentation
  - firm dynamics
  - productivity heterogeneity
  - factor reallocation
  - savings and investment
  - structural change
  best_for:
  - Understanding the macroeconomic growth implications of firm-level financial frictions and productivity heterogeneity
  - explaining aggregate patterns (high growth
  - high savings
  - current account surplus) through microeconomic mechanisms
  not_good_for:
  - Causal identification of specific policy reforms
  - micro-level policy evaluation
  - short-run business cycle analysis
  - firm-level treatment effects without structural model
design:
  affordances:
  - firm-level productivity heterogeneity
  - ownership-type variation in financial access
  - aggregate time-series variation in sector composition
  - calibration to Chinese macroeconomic aggregates
  candidate_designs:
  - structural model calibration and simulation
  - quantitative macro-development accounting
  - decomposition of aggregate productivity growth
  - cross-country comparative analysis
  identifying_variation: The interaction between firm-level productivity dispersion and ownership-based credit market segmentation
    generates time-varying aggregate outcomes (savings, investment, growth, current account) that can be matched to Chinese
    macro data through a calibrated structural model
  assumptions:
  - Firms within each sector are heterogeneous in productivity
  - financial frictions are sector-specific (SOEs have preferential credit access)
  - entrepreneurs face borrowing constraints
  - the model captures the key margins of firm behavior and resource allocation
  diagnostics:
  - Model fit to Chinese macro aggregates (growth rate
  - savings rate
  - current account
  - employment shares)
  - sensitivity analysis to key parameters (credit constraint tightness
  - productivity dispersion
  - entry/exit costs)
  - comparison to alternative model specifications
  primary_strategy: Structural macroeconomic model calibrated to firm-level and aggregate data, with quantitative simulation
    and counterfactual analysis
  estimand: The causal effect of the recorded exposure on GDP growth rate, aggregate investment rate, aggregate savings rate,
    current account surplus, sectoral employment shares, conditional on the stated design assumptions.
  treatment_variable: Firm ownership type (SOE vs private/entrepreneurial) interacted with firm-level productivity and financial
    constraint proxies
  comparison_logic: Calibration of model-generated moments against observed Chinese macro aggregates; quantitative decomposition
    of growth across sectors
  estimation_notes: Structural macroeconomic model calibrated to firm-level and aggregate data, with quantitative simulation
    and counterfactual analysis
threats:
- type: omitted-variable
  basis: inferred
  condition: Aggregate growth patterns attributed to firm heterogeneity and financial frictions could also be driven by other
    concurrent factors including trade liberalization, FDI inflows, urbanization, infrastructure investment, or other policy
    reforms
  evidence_refs:
  - E1
  possible_diagnostics:
  - Extend model to incorporate additional mechanisms
  - test model predictions against cross-country data
  - examine contribution of alternative channels quantitatively
  - compare model-implied moments with reduced-form evidence
- type: measurement
  basis: reported
  condition: Firm-level productivity measurement in China is challenging due to limited data on firm-level capital stocks,
    price deflators at the firm level, and output quality differences between SOEs and private firms
  evidence_refs:
  - E1
  possible_diagnostics:
  - Sensitivity analysis to alternative productivity measurement approaches
  - use of revenue-based vs quantity-based productivity
  - robustness to alternative capital stock estimation methods
- type: external-validity
  basis: inferred
  condition: The model's mechanisms are calibrated to China's specific institutional context (e.g., state banking system,
    SOE sector, export-oriented growth model) and may not generalize to other developing or transition economies
  evidence_refs:
  - E1
  possible_diagnostics:
  - Test model predictions against other emerging economies
  - examine whether similar patterns hold in countries with different financial systems
  - conduct cross-country comparative analysis
empirical_requirements:
  contract_version: 1
  population: Chinese non-agricultural firms (both SOEs and private/entrepreneurial firms) and aggregate Chinese economy over
    the reform period (1990s–2000s)
  observation_unit: Firm-level data for micro analysis; national-level time series for aggregate calibration
  geography_level: National (with potential for regional decomposition)
  time_start: 1990
  time_end: 2009
  minimum_frequency: Annual
  minimum_pre_periods: 3
  minimum_post_periods: 5
  required_fields:
  - firm ownership type
  - firm output/revenue
  - firm employment
  - firm capital stock
  - firm investment
  - firm debt
  - interest payments
  - firm entry/exit status
  - aggregate GDP
  - aggregate investment
  - aggregate savings
  - current account balance
  required_identifiers:
  - firm identifier
  - year
  - industry code
  - ownership code
  treatment_key:
  - firm ownership type
  - firm productivity level
  - firm financial constraint measure (debt-to-asset ratio
  - interest rate relative to benchmark)
  treatment_source: Chinese Industrial Census and Annual Survey of Industrial Firms (ASIF) for firm-level data; China National
    Bureau of Statistics and IMF/World Bank data for aggregate macro variables
  measurement_risks:
  - Firm-level data quality concerns (especially for small private firms)
  - price deflator measurement at firm level
  - capital stock estimation (perpetual inventory method assumptions)
  - changing survey coverage and sampling frames over time
  - under-reporting by private firms
  - SOE subsidy and soft-budget constraint measurement
evidence:
- id: E1
  source_type: paper
  citation: 'Song, Zheng, Kjetil Storesletten, and Fabrizio Zilibotti. 2011. "Growing Like China." American Economic Review
    101 (1): 196–233.'
  url: https://doi.org/10.1257/aer.101.1.196
  date: 2011
  supports:
  - identity
  - assignment
  - design
  - threats
  - empirical_requirements
  verification_status: verified
design_applications:
- paper: Growing Like China
  doi: 10.1257/aer.101.1.196
  journal: American Economic Review
  year: 2011
  research_question: What explains China's spectacular growth performance, high savings rate, and large current account surplus
    in the context of firm heterogeneity and financial frictions?
  population: Chinese non-agricultural firms and aggregate Chinese economy, 1990s–2000s
  outcome: GDP growth rate, aggregate investment rate, aggregate savings rate, current account surplus, sectoral employment
    shares
  data_used:
  - Chinese national accounts data (GDP, savings, investment, employment by sector)
  - Chinese Industrial Enterprises Database for firm-level productivity and financial variables
  treatment_encoding: Firm ownership type (SOE vs private/entrepreneurial) interacted with firm-level productivity and financial
    constraint proxies
  comparison: Calibration of model-generated moments against observed Chinese macro aggregates; quantitative decomposition
    of growth across sectors
  empirical_design: Structural macroeconomic model calibrated to firm-level and aggregate data, with quantitative simulation
    and counterfactual analysis
  assumptions:
  - Two-sector model with heterogeneous firms
  - financial frictions specific to ownership type
  - entrepreneurial borrowing constraints
  - monopolistic competition in product markets
  threats_addressed:
  - Alternative channels via robustness and extended model specifications
  - measurement concerns via sensitivity analysis
  - external validity via cross-country comparison and alternative parameterizations
  evidence_refs:
  - E1
readiness_blockers:
- "Catalog admissibility is unresolved: the source is a structural model without a recoverable external assignment mechanism."
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
method_transfer: null
superseded_by: null
deprecation_reason: Structural calibration model without a recoverable assignment-generating feature.
---
## Institutional Background

China's economic transformation since the 1990s has been characterized by remarkably high growth rates, rising savings and investment rates, and a growing current account surplus. A central feature of China's economic structure is the co-existence of a state-owned enterprise (SOE) sector and a dynamic private/entrepreneurial sector. SOEs have historically enjoyed preferential access to bank credit through China's state-dominated banking system, despite having lower average productivity than private firms. In contrast, the more productive private sector has faced binding financial constraints, relying heavily on retained earnings for investment. This institutional segmentation of credit markets is a key feature of China's "dual economy." [E1]

## What Changed

This paper does not study a discrete policy change or natural experiment. Instead, it develops a macroeconomic model that explains China's growth through the lens of firm heterogeneity and financial frictions. The key structural variation is the persistent difference in productivity and financial access between two types of firms: (i) low-productivity SOEs with privileged access to credit, and (ii) high-productivity entrepreneurial (private) firms that face binding financial constraints. Over time, the high-productivity private sector accumulates capital through retained earnings, expands its share of employment and output, and drives aggregate growth — while generating the high savings rate and current account surplus observed in China. [E1]

## Implementation and Assignment

The variation in this framework operates at both the firm level and the aggregate level. At the firm level, there is substantial heterogeneity in productivity within both the SOE and private sectors. Private firms, despite being on average more productive, face credit constraints that limit their ability to borrow and invest, forcing them to rely on internal savings. SOEs, though less productive, can borrow cheaply from state banks. At the aggregate level, the gradual reallocation of resources (labor and capital) from the low-productivity SOE sector to the high-productivity private sector generates sustained aggregate growth. This reallocation is financed by the high savings of the entrepreneurial sector. [E1]

## Why This Creates Empirical Variation

The key empirical variation exploited in the quantitative analysis is the cross-sectional distribution of firm-level productivity and financial constraints across ownership types, combined with the time-series evolution of the relative size of the two sectors. The productivity gap between SOEs and private firms, together with the differential access to credit, creates a mechanism whereby high-productivity firms are initially capital-constrained and must grow through retained earnings. This generates endogenous dynamics of aggregate savings, investment, and the current account that match China's observed macro patterns. The model's parameters are calibrated to firm-level data, and the model's predictions are compared with aggregate time series. [E1; analytical inference]

## Identification Risks

As a structural modeling exercise, this paper faces different identification challenges than reduced-form causal designs. The main risk is that the model's mechanisms — firm heterogeneity and financial frictions — may not be uniquely identified from the data: other structural features or concurrent reforms could generate similar aggregate patterns. The model's assumptions about firm behavior (e.g., monopolistic competition, credit constraints, entry and exit) are strong and may not fully capture institutional complexities such as government subsidies, soft budget constraints for SOEs, or informal credit markets. Measurement of firm-level variables, especially capital stocks and prices, introduces additional uncertainty. [E1; analytical inference]

## Data Requirements

The model is calibrated using both firm-level data from the Chinese Annual Survey of Industrial Firms (ASIF) and aggregate macroeconomic data from Chinese national accounts. Firm-level data requirements include output, employment, capital stock, investment, ownership type, and measures of financial constraints (debt, interest payments). Aggregate data requirements include GDP, investment, savings, consumption, employment by sector, and current account balance — all at annual frequency for the 1990s–2000s period. International comparable data may be needed for cross-country validation exercises. [E1]

## Evidence Notes

E1 is the published American Economic Review article by Song, Storesletten, and Zilibotti. The paper develops a quantitative macroeconomic model in which heterogeneous firms face ownership-specific financial frictions. The model successfully matches China's key macroeconomic patterns: high output growth, rising savings and investment rates, a growing current account surplus, and the declining share of SOEs in employment and output. The paper's contribution is primarily theoretical and quantitative rather than reduced-form causal; its identification comes from the structural model's ability to match multiple aggregate moments simultaneously. The paper has been highly influential in the macro-development literature on China.

## Deprecation Notice

**Deprecated 2026-07-13 (task-e9b64f33e231)**: This record has been deprecated following a catalog admissibility audit. Song, Storesletten, and Zilibotti (2011, AER) is a seminal paper in Chinese macro-development that develops a two-sector structural model calibrated to match China's aggregate growth patterns. Despite its importance and influence, it does not possess a recoverable assignment-generating feature: the firm type (SOE vs. private) is an endogenous structural characteristic, financial frictions are modeled as parametric features of the economy rather than externally assigned variation, and the paper's identification comes from structural calibration rather than quasi-experimental design. Structural calibration models are valuable theoretical contributions but do not constitute causal variation under NIEL's admissibility criteria. This record is preserved for reference but excluded from recommendation pathways. Researchers interested in SOE-related variation should consult `china-soe-decentralization` for potential assignment mechanisms. [analytical inference]
