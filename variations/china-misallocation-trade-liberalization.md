---
schema_version: 2
id: china-misallocation-trade-liberalization
name: Deprecated — Misallocation under Trade Liberalization Is a Structural Counterfactual, Not a China Variation
aliases:
- Bai Jin Lu 2024
- trade liberalization welfare misallocation
- distortionary taxes trade China
- firm-level distortions China trade

status: deprecated
provenance:
  task_id: task-f3160acf58ef
scope:
  country: China
  regions:
  - Chinese manufacturing sector
  domains:
  - trade
  - public-finance
  - firm-heterogeneity
  - misallocation
  - industrial-organization
  variation_type: other
  knowledge_role: china-variation
  china_relevance: The paper calibrates a trade model using Chinese manufacturing data, but does not assign an observed Chinese policy exposure; this retained file exists only to prevent that model exercise from being misread as a usable variation.
identity:
  instrument: '[E1, verified] No observed policy instrument is identified in the paper. It estimates a structural Melitz-style model with model-inferred firm wedges and runs counterfactual changes in iceberg trade costs.'
  authority: '[E1, verified] Not applicable: the model''s wedges are latent objects intended to summarize distortions, not a dated Chinese tax, subsidy, or regulatory assignment.'
  legal_identifiers:
  - 'None: no policy identifier is the paper''s assigned treatment'
  implementation_regime: '[E1, verified] The 1998 and 2005 Chinese firm distributions parameterize model counterfactuals. The paper does not map a law, tariff schedule, or subsidy program to firm-by-time treatment.'
  assignment_mechanism: '[E1, verified] None recoverable: model-inferred wedges and trade costs are not observed administrative assignment variables.'
  parent: null
  related_variations:
  - china-growing-like-china
timeline:
  announcement: null
  effective: null
  implementation_start: 1998
  implementation_end: 2005
  local_timing: '[E1, verified] The paper compares model calibrations based on 1998 and 2005 distributions; these are not implementation dates or treatment cohorts.'
  anticipation: '[E1, verified] Not an event-study design; anticipation cannot be evaluated as if 1998-2005 were a policy rollout.'
  last_verified: '2026-07-13'
assignment:
  unit: Firm (Chinese manufacturing firm)
  treated: '[E1, verified] None: the paper does not define observed treated firms.'
  comparison_pool: '[E1, verified] No empirical treatment-control comparison. Its comparisons are model counterfactuals holding different parameter groups at 1998 or 2005 values.'
  rule: '[E1, verified] No observable assignment rule. Revenue-productivity wedges are inferred model primitives and cannot be equated with observed taxes or subsidy receipt.'
  intensity: Continuous — firm-level distortion measure (revenue productivity relative to efficient benchmark, or the gap
    between marginal revenue product of capital/labor and the market price), and industry-level trade cost reduction (tariff
    reductions or trade cost shock)
  exemptions: []
  compliance: Not applicable; this is not an intervention or take-up measure.
  exposure_construction: '[E1, verified] No reusable policy-exposure construction. The model estimates latent trade costs and wedges from distributional moments, then alters parameter values in counterfactual decompositions.'
  required_identifiers:
  - firm identifier
  - industry code
  - year
  - firm output
  - firm capital stock
  - firm labor input
  - firm intermediate inputs
  - firm tax payments
  - firm subsidy receipts
  - firm ownership type
  spillovers: Trade liberalization affects product market competition, factor prices, and the reallocation of resources across
    firms and industries; distortions in one sector may affect resource allocation in linked sectors through input-output
    relationships
research_compatibility:
  outcome_domains:
  - trade welfare
  - resource misallocation
  - aggregate productivity
  - fiscal externalities
  - firm-level adjustment to trade
  - industrial policy
  affected_populations:
  - Chinese manufacturing firms
  - workers in manufacturing sectors
  - consumers of manufactured goods
  - government fiscal authorities
  mechanism_channels:
  - distortionary fiscal policy
  - trade-induced reallocation
  - welfare decomposition through sufficient statistics
  - fiscal externality (trade affects government revenue through distorted firms)
  - productivity selection
  best_for:
  - Studying how pre-existing distortions affect the welfare gains from trade liberalization
  - quantifying the fiscal externality of trade
  - understanding the interaction between industrial policy and trade policy
  not_good_for:
  - Short-run firm-level treatment effects
  - dynamic adjustment processes (cross-sectional analysis)
  - non-manufacturing sectors
  - countries without detailed firm-level data on distortions
design:
  affordances:
  - firm-level distortion measures
  - industry-level trade exposure variation
  - sufficient statistics approach to welfare measurement
  - decomposition of trade welfare into direct and distortion-interaction channels
  candidate_designs:
  - sufficient statistics welfare decomposition using cross-sectional firm moments
  - industry-level DiD with firm distortion heterogeneity
  - quantitative trade model with heterogeneous firms and distortions
  identifying_variation: Cross-firm variation in distortion wedges combined with cross-industry variation in trade cost reductions;
    the covariance between firm-level distortions and trade exposure determines the aggregate welfare impact of trade liberalization
    beyond the direct gains from trade
  assumptions:
  - Firm-level distortions are captured by measured revenue productivity wedges
  - trade cost reductions are exogenous to firm-level distortion patterns (at least conditional on industry)
  - the sufficient statistics approach captures the relevant general equilibrium effects
  - no offsetting policy changes correlated with trade liberalization
  diagnostics:
  - Test relationship between industry-level trade exposure and firm-level distortion patterns
  - examine robustness of welfare moments to alternative distortion measures
  - compare sufficient statistics results with structural model estimates
  - placebo tests using alternative trade shock measures
  primary_strategy: Sufficient statistics approach using cross-sectional firm moments combined with a quantitative trade model
    with heterogeneous firms and distortionary fiscal policies
  estimand: The causal effect of the recorded exposure on Aggregate welfare (real consumption equivalent), aggregate productivity,
    government revenue, welfare decomposition into direct trade gains and distortion-interaction effects, conditional on the
    stated design assumptions.
  treatment_variable: Firm-level distortion wedges (measured as revenue productivity deviations from efficient allocation)
    interacted with industry-level trade cost reductions
  comparison_logic: Welfare decomposition comparing economies with and without firm-level distortions, across industries with
    varying trade exposure
  estimation_notes: Sufficient statistics approach using cross-sectional firm moments combined with a quantitative trade model
    with heterogeneous firms and distortionary fiscal policies
threats:
- type: measurement
  basis: documented
  condition: Firm-level distortion measures based on revenue productivity wedges may capture measurement error, price variation,
    or other non-distortion factors (e.g., demand shocks, markups, adjustment costs) rather than actual fiscal distortions
  evidence_refs:
  - E1
  possible_diagnostics:
  - Robustness to alternative methods for measuring distortions (physical productivity vs revenue productivity)
  - test sensitivity to markup assumptions
  - compare with direct measures of tax and subsidy wedges where available
- type: omitted-variable
  basis: inferred
  condition: Industry-level trade exposure may be correlated with other industry characteristics (e.g., technology, competition,
    regulatory environment) that independently affect the covariance between distortions and welfare
  evidence_refs:
  - E1
  possible_diagnostics:
  - Control for industry-level characteristics (concentration
  - SOE share
  - FDI share)
  - test sensitivity to alternative industry classifications
  - examine within-industry distribution of distortions
- type: external-validity
  basis: inferred
  condition: The cross-sectional analysis using 2005 data captures a specific point in China's development; the relationship
    between distortions and trade welfare may differ in other periods or countries with different institutional and fiscal
    environments
  evidence_refs:
  - E1
  possible_diagnostics:
  - Extend analysis to multiple years
  - test robustness across time periods
  - apply framework to other countries with available data
  - compare results with similar studies for other contexts
- type: general-equilibrium
  basis: inferred
  condition: The sufficient statistics approach may not fully capture general equilibrium effects through factor prices, intermediate
    linkages, or endogenous policy responses to trade liberalization
  evidence_refs:
  - E1
  possible_diagnostics:
  - Compare sufficient statistics results with full structural model
  - incorporate input-output linkages
  - test sensitivity to general equilibrium closure assumptions
empirical_requirements:
  contract_version: 1
  population: Chinese manufacturing firms covered by the Annual Survey of Industrial Firms (ASIF) in 2005, matched with industry-level
    trade and tariff data
  observation_unit: Firm (with industry-level aggregation for trade exposure)
  geography_level: Firm (with industry classification for trade exposure)
  time_start: 2005
  time_end: 2005
  minimum_frequency: Cross-sectional (single year for core analysis; panel data helpful for robustness and dynamics)
  minimum_pre_periods: 0
  minimum_post_periods: 1
  required_fields:
  - firm identifier
  - industry code (CIC or ISIC)
  - output/revenue
  - value-added
  - employment
  - capital stock
  - intermediate inputs
  - wage bill
  - tax payments (all major tax categories)
  - subsidy receipts
  - ownership type
  - export status
  - firm age
  required_identifiers:
  - firm identifier
  - industry code
  - year
  treatment_key:
  - firm-level distortion wedge (TFPQ or TFPR gap)
  - industry-level tariff rate or trade cost measure
  - interaction of firm distortion and industry trade exposure
  treatment_source: Chinese Annual Survey of Industrial Firms (ASIF) for firm data; WTO tariff data, Chinese customs data,
    and input-output tables for trade exposure measures
  measurement_risks:
  - Firm-level output and input price deflation (required for physical productivity measurement)
  - capital stock estimation (perpetual inventory method)
  - distinction between tax and subsidy wedges vs other sources of revenue productivity dispersion (markups
  - demand shocks
  - adjustment costs)
  - sample selection and survey coverage changes
  - under-reporting by private firms
  - informal sector firms not in the survey
evidence:
- id: E1
  source_type: paper
  citation: 'Bai, Yan, Keyu Jin, and Dan Lu. 2024. "Misallocation under Trade Liberalization." American Economic Review 114
    (7): 1949–1985.'
  url: https://www.keyujin.co/pdf/BJL_2023_mainPaper.pdf
  date: 2024
  supports:
  - identity.instrument
  - identity.authority
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.local_timing
  - timeline.anticipation
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.compliance
  - assignment.exposure_construction
  - design.primary_strategy
  - design.identifying_variation
  - design.comparison_logic
  - design_applications.research_question
  - design_applications.population
  - design_applications.outcome
  - design_applications.empirical_design
  verification_status: verified
  access_level: full-text
  locator: 'Author-hosted December 2023 version inspected: pp. 1-3 (model and model-inferred wedges), pp. 18-19 (quantitative exercise), pp. 35-39 (1998-versus-2005 counterfactual decomposition and caveats).'
- id: E2
  source_type: other
  citation: 'Bai, Yan, Keyu Jin, and Dan Lu. 2024. "Misallocation under Trade Liberalization." American Economic Review 114 (7): 1949-1985.'
  url: https://doi.org/10.1257/aer.20200596
  date: 2024
  supports:
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
  verification_status: verified
  access_level: metadata
  locator: 'AEA article page identifies the published version, journal, pages, and DOI; substantive claims are supported by E1.'
design_applications:
- paper: Misallocation under Trade Liberalization
  doi: 10.1257/aer.20200596
  journal: American Economic Review
  year: 2024
  research_question: How do pre-existing distortions (taxes and subsidies) at the firm level affect the welfare consequences
    of trade liberalization in Chinese manufacturing?
  population: Chinese manufacturing firms in the Annual Survey of Industrial Firms (ASIF), 2005 cross-section
  outcome: Aggregate welfare (real consumption equivalent), aggregate productivity, government revenue, welfare decomposition
    into direct trade gains and distortion-interaction effects
  data_used: []
  treatment_encoding: Firm-level distortion wedges (measured as revenue productivity deviations from efficient allocation)
    interacted with industry-level trade cost reductions
  comparison: Welfare decomposition comparing economies with and without firm-level distortions, across industries with varying
    trade exposure
  empirical_design: Sufficient statistics approach using cross-sectional firm moments combined with a quantitative trade model
    with heterogeneous firms and distortionary fiscal policies
  assumptions:
  - Firm-level wedges capture distortionary fiscal policies
  - trade cost reductions are exogenous to distortion patterns conditional on industry
  - sufficient statistics capture general equilibrium welfare effects
  - model primitives are stable across counterfactuals
  threats_addressed:
  - Measurement error via alternative distortion measures and robustness checks
  - omitted industry characteristics via industry controls
  - external validity via comparison with alternative data periods and specifications
  evidence_refs:
  - E1
  - E2
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
deprecation_reason: 'Audit established that the paper provides structural counterfactuals calibrated to Chinese firm distributions, not an observed Chinese assignment mechanism or reproducible policy exposure. It is retained only to prevent future agents from treating latent wedges as a variation.'
method_transfer: null
---
## Institutional Background

**Deprecated serving record.** [E1, verified] Bai, Jin, and Lu (2024) is a structural/quantitative study, not evidence that a Chinese policy assigned firms to a treatment. It estimates latent wedges and iceberg trade costs from firm-distribution moments, then compares model counterfactuals. Do not retrieve it as a variation or treat “subsidized firms” as an observed subsidy-recipient group. Its valid value is methodological background for a separately documented policy or trade-cost design.

China's manufacturing sector has been shaped by extensive government intervention through taxes, subsidies, and regulatory policies that create substantial heterogeneity in the effective fiscal environment facing firms. State-owned enterprises, foreign-invested firms, and private domestic firms face different tax regimes, subsidy programs, and regulatory burdens. These firm-level distortions create misallocation of resources across firms — a well-documented feature of the Chinese economy. At the same time, China has undergone significant trade liberalization, particularly after its WTO accession in 2001, which reduced both Chinese import tariffs and foreign trade barriers against Chinese exports. [E1]

## What Changed

This paper examines how trade liberalization interacts with pre-existing firm-level fiscal distortions to determine aggregate welfare. The key insight is that when firms face differential taxes and subsidies, trade liberalization changes the relative profitability and market share of distorted firms, generating a "fiscal externality": trade reallocates activity toward or away from subsidized/taxed firms, affecting government revenue and aggregate efficiency. The paper develops a sufficient statistics framework showing that the aggregate welfare effect of trade depends on the covariance between firm-level distortions and trade exposure, in addition to the standard gains-from-trade channel. [E1]

## Implementation and Assignment

The variation exploited is at two levels. First, firm-level distortions are measured as wedges between the marginal revenue product of inputs (capital, labor) and their market prices, following the misallocation literature. These wedges capture the net effect of taxes, subsidies, and other policy-induced distortions. Second, industry-level trade exposure is measured through tariffs and trade costs. The interaction of these two dimensions — firms with high distortions operating in industries with large trade cost reductions — generates the key identifying variation for the welfare decomposition. The analysis uses the 2005 Chinese manufacturing census, which provides detailed firm-level data on output, inputs, tax payments, and subsidies. [E1]

## Why This Creates Empirical Variation

The empirical variation arises from the cross-sectional distribution of firm-level distortion wedges and the cross-industry distribution of trade exposure. Industries differ substantially in the degree of trade liberalization they experienced, and within each industry, firms differ in the extent to which they are distorted by fiscal policies. The key parameter for welfare is the covariance between these two dimensions: if highly distorted firms are in industries with large trade cost reductions, trade liberalization may exacerbate misallocation and reduce welfare relative to the benchmark gains; conversely, if trade exposure is concentrated in less-distorted firms, trade liberalization may improve allocation. The sufficient statistics approach allows the aggregate welfare effect to be computed from the joint distribution of distortions and trade exposure. [E1; analytical inference]

## Identification Risks

The central identification challenge is that firm-level distortion measures based on revenue productivity wedges may reflect factors other than actual fiscal distortions — such as measurement error, demand shocks, markup heterogeneity, or adjustment costs. If these non-distortion factors are correlated with trade exposure, the welfare decomposition may be biased. Industry-level trade exposure may also be endogenous to domestic distortion patterns if policymakers set tariffs strategically in sectors with particular distortion characteristics. The cross-sectional nature of the 2005 analysis limits the ability to control for unobserved time-invariant firm or industry characteristics. [E1; analytical inference]

## Data Requirements

The analysis requires firm-level data from the Chinese Annual Survey of Industrial Firms (ASIF) for 2005, including output, value-added, employment, capital stock, intermediate inputs, wage bill, and crucially, detailed information on tax payments and subsidy receipts. Industry-level trade data includes tariff schedules (both Chinese and foreign), trade flows, and input-output tables for constructing effective rates of protection. Firm-level prices (output and input deflators) are important for distinguishing physical productivity from revenue productivity wedges. The cross-sectional nature of the core analysis means that multiple years of data are not strictly required for the sufficient statistics approach, though panel data would strengthen robustness analysis. [E1]

## Evidence Notes

E1 is the published American Economic Review article by Bai, Jin, and Lu (2024). The paper finds that firm-level distortions in Chinese manufacturing are substantial and that trade liberalization can generate a welfare-reducing fiscal externality: because subsidized firms expand when trade costs fall, the government's fiscal position worsens. The quantitative results suggest that ignoring the interaction between distortions and trade would significantly overstate the welfare gains from trade liberalization for China. The paper develops a clear sufficient statistics framework that transparently identifies the key moments driving the welfare results. A limitation is the reliance on a single cross-section (2005), which limits the ability to address dynamic considerations or policy endogeneity.
