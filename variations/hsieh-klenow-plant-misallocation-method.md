---
schema_version: 2
id: hsieh-klenow-plant-misallocation-method
name: Hsieh-Klenow Plant-Level Misallocation Measurement
aliases:
- Hsieh-Klenow TFPR method
- plant-level misallocation decomposition
- revenue-productivity dispersion method
status: extracted
provenance:
  task_id: task-2efe0b47d739
scope:
  country: United States
  regions:
  - U.S. manufacturing benchmark
  - China manufacturing application
  - India manufacturing application
  domains:
  - productivity
  - misallocation
  - development
  - firms
  - industrial-organization
  - macroeconomics
  variation_type: other
  knowledge_role: transferable-method
  china_relevance: The Hsieh-Klenow method is the canonical way to quantify resource
    misallocation using plant-level data and has been widely applied to Chinese manufacturing
    surveys (Annual Survey of Industrial Enterprises) to measure the costs of distortions
    and track allocative efficiency over time.
identity:
  instrument: The Hsieh-Klenow method of measuring resource misallocation from the
    cross-sectional dispersion of plant revenue productivity (TFPR) within narrowly
    defined industries, relative to a benchmark efficient allocation.
  authority: Chang-Tai Hsieh and Peter J. Klenow (2009, QJE); building on Restuccia
    and Rogerson (2008) and Foster, Haltiwanger, and Syverson (2008).
  legal_identifiers:
  - "Hsieh, Chang-Tai, and Peter J. Klenow. 2009. 'Misallocation and Manufacturing TFP
    in China and India.' The Quarterly Journal of Economics 124(4): 1403-1448."
  - "Hsieh, Chang-Tai, and Peter J. Klenow. 2007. NBER Working Paper No. 13290."
  implementation_regime: Apply the method to plant- or firm-level survey data. For
    each plant, compute physical productivity (TFPQ) and revenue productivity (TFPR)
    using industry production functions. Compare the within-industry dispersion of
    log TFPR to an efficient benchmark (typically the U.S.). Compute the aggregate
    TFP gain from hypothetically reallocating capital and labor to equalize TFPR across
    plants within each industry.
  assignment_mechanism: Not applicable. The method uses observed cross-sectional plant
    heterogeneity and a structural model of monopolistic competition; it does not rely
    on an exogenous treatment assignment.
  parent: null
  related_variations:
  - china-misallocation-trade-liberalization
  - china-growing-like-china
  - china-firm-dynamics-reallocation
  - china-trade-migration-productivity
timeline:
  announcement: null
  effective: null
  implementation_start: 1977
  implementation_end: 2005
  local_timing: The source paper uses U.S. Census of Manufactures (1977, 1982, 1987,
    1992, 1997), Chinese Annual Survey of Industrial Production (1998-2005), and Indian
    Annual Survey of Industries (1987-1994). The method itself can be applied to any
    comparable plant-level dataset.
  anticipation: Not applicable for a measurement method.
  last_verified: '2026-07-14'
assignment:
  unit: Plant-year or firm-year within a narrowly defined industry.
  treated: Not applicable as a treatment. Researchers often compare plants with high
    TFPR (constrained or taxed) and low TFPR (subsidized or protected) within the same
    industry.
  comparison_pool: Other plants in the same 4-digit industry; the U.S. distribution
    of TFPR serves as an efficient benchmark.
  rule: Classify plants by their deviation of log TFPR from the industry geometric mean.
    Compute the variance of log TFPR and the implied TFP loss relative to a counterfactual
    in which TFPR is equalized across plants.
  intensity: Continuous — the absolute or relative deviation of plant TFPR from the
    industry mean.
  exemptions: []
  compliance: Not applicable; the method relies on observed data rather than on a treatment
    take-up decision.
  exposure_construction: Compute plant-level TFPR and TFPQ from revenue, value added,
    capital stock, and labor compensation using industry-specific production elasticities.
    Measure within-industry dispersion of log TFPR and compare it to the U.S. benchmark.
    Simulate reallocation by assigning each plant the industry-average TFPR while keeping
    aggregate resources fixed.
  required_identifiers:
  - plant or firm identifier
  - year
  - 4-digit industry code
  - nominal revenue or value added
  - capital stock
  - labor compensation or employment
  - intermediate inputs (if value added is not directly available)
  spillovers: General-equilibrium effects from reallocation are not captured by the partial-equilibrium
    counterfactual. Factor-price and demand responses, as well as entry and exit, are
    typically ignored.
research_compatibility:
  outcome_domains:
  - aggregate-productivity
  - resource-misallocation
  - distortion-measurement
  - welfare-gains-from-reform
  - firm-heterogeneity
  - industrial-policy-evaluation
  affected_populations:
  - manufacturing plants and firms
  - workers in reallocated plants
  - policymakers assessing reform gains
  mechanism_channels:
  - capital and labor market distortions
  - output distortions (taxes, subsidies, size restrictions)
  - markup variation under monopolistic competition
  - reallocation of factors toward higher-productivity plants
  - comparison with an efficient benchmark allocation
  best_for:
  - Quantifying the aggregate TFP cost of within-industry factor misallocation
  - Comparing allocative efficiency across countries, regions, or time periods
  - Evaluating how reforms or policies change the dispersion of marginal revenue products
  not_good_for:
  - Identifying the causal effect of a specific policy without additional variation
  - Capturing dynamic adjustment, entry, exit, or general-equilibrium effects
  - Settings where plant-specific prices, output quality, or markups are poorly measured
  - Industries where the assumptions of monopolistic competition and Cobb-Douglas production
    are strongly violated
design:
  claim_type: method-pattern
  affordances:
  - Uses widely available plant-level survey data
  - Provides a single sufficient statistic (variance of log TFPR) that summarizes the
    TFP cost of distortions under log-normality
  - Can be decomposed by ownership, size, age, region, or other plant characteristics
  - Enables cross-country and cross-time comparisons
  candidate_designs:
  - Cross-country comparison of TFPR dispersion (China/India vs. U.S.)
  - Event-study or difference-in-differences of TFPR dispersion before and after a reform
  - Decomposition of TFPR variance by observable plant characteristics
  - Robustness checks using alternative elasticities of substitution and capital shares
  identifying_variation: Cross-sectional variation in plant revenue productivity within
    narrowly defined industries, combined with a structural model that links TFPR dispersion
    to aggregate TFP losses.
  primary_strategy: Compute plant-level TFPR and TFPQ, measure within-industry dispersion,
    and compare it to a benchmark efficient allocation (usually the U.S.).
  estimand: The aggregate manufacturing TFP gain from eliminating within-industry factor
    misallocation, or the change in this gain associated with a policy or over time.
  treatment_variable: Not a treatment variable. The key endogenous object is plant-level
    TFPR, which reflects the combined effect of physical productivity and distortions.
  comparison_logic: Compare the distribution of TFPR in the study country to the U.S.
    benchmark, or compare the same country before and after a reform.
  estimation_notes: Set the elasticity of substitution σ (benchmark σ = 3), the rental
    rate of capital R (benchmark 0.10), and industry capital shares from the U.S. Infer
    plant-level distortions from first-order conditions. Trim extreme tails to limit outlier
    influence. Report TFP gains under alternative parameter values.
  assumptions:
  - Plants operate under monopolistic competition with a constant elasticity of demand.
  - Production functions are Cobb-Douglas with industry-specific factor shares.
  - The U.S. allocation provides a plausible efficient benchmark.
  - Plant-level revenue and inputs are measured comparably across countries and over time.
  - The number of firms is fixed; entry, exit, and dynamic responses are ignored.
  diagnostics:
  - Compare TFPR and TFPQ distributions across countries
  - Report variance of log TFPR and TFP gains under σ = 3 and σ = 5
  - Decompose TFPR variance by ownership, size, age, and region
  - Check robustness to trimming tails and measuring labor by wage bill vs. employment
  - Validate that the U.S. benchmark produces plausible results in undistorted settings
threats:
- type: measurement-error
  basis: reported
  condition: Plant-level revenue, capital stock, and labor compensation are measured
    with error, especially in developing-country surveys. Measurement error inflates TFPR
    dispersion and can mimic or mask true misallocation.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Compare results using alternative capital and labor measures
  - Assess sensitivity to trimming outliers
  - Use simulated data to quantify bias from measurement error
- type: model-misspecification
  basis: inferred
  condition: The assumed production function, demand elasticity, and market structure
    may not fit all industries or countries.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Estimate industry-specific elasticities where feasible
  - Test robustness to alternative σ values
  - Compare results with non-parametric or structural alternatives
- type: omitted-distortions
  basis: inferred
  condition: TFPR dispersion captures the net effect of many distortions and cannot
    identify individual policies without additional covariates or exogenous variation.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Correlate TFPR dispersion with candidate policies
  - Use firm-level regressions or decompositions
  - Combine with natural experiments that change specific distortions
- type: general-equilibrium
  basis: inferred
  condition: The counterfactual reallocation holds aggregate capital and labor fixed
    and ignores factor-price responses, demand effects, and entry/exit.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Compare partial- and general-equilibrium counterfactuals in a model
  - Report gains as upper-bound potential rather than equilibrium predictions
  - Allow for capital accumulation response in sensitivity analysis
- type: external-validity
  basis: inferred
  condition: Parameter choices and benchmark values calibrated to U.S. manufacturing
    may be inappropriate for service sectors, informal firms, or non-manufacturing industries.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Apply the method to multiple sectors and countries
  - Use sector-specific benchmarks and production functions
  - Document differences between formal and informal firms
empirical_requirements:
  contract_version: 1
  population: Manufacturing plants or firms in a country with comparable survey data.
  observation_unit: Plant-year or firm-year.
  geography_level: Plant / firm, aggregated to industry or country.
  time_start: null
  time_end: null
  minimum_frequency: annual
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields:
  - plant or firm identifier
  - year
  - industry code
  - nominal revenue or value added
  - capital stock
  - labor compensation or employment
  - intermediate inputs
  - ownership status
  - age or entry year
  required_identifiers:
  - plant or firm ID
  - year
  - industry code
  treatment_key:
  - plant or firm ID
  - year
  - industry code
  - log TFPR deviation
  treatment_source: Not a treatment; computed from plant-level production data using
    the Hsieh-Klenow formulas.
  measurement_risks:
  - Revenue deflators may not capture plant-specific prices, conflating markups with
    distortions.
  - Book values of capital may mismeasure the true capital stock.
  - Labor compensation may omit non-wage benefits or hours variation.
  - Industry codes must be harmonized across countries and over time.
  - Small sample sizes within industries produce noisy TFPR estimates.
evidence:
- id: E1
  source_type: paper
  citation: "Hsieh, Chang-Tai, and Peter J. Klenow. 2009. 'Misallocation and Manufacturing
    TFP in China and India.' The Quarterly Journal of Economics 124(4): 1403-1448."
  url: https://doi.org/10.1162/qjec.2009.124.4.1403
  date: 2009
  supports:
  - identity
  - timeline
  - design
  verification_status: reported
  access_level: abstract
  locator: QJE article abstract and citation (DOI 10.1162/qjec.2009.124.4.1403)
- id: E2
  source_type: paper
  citation: "Hsieh, Chang-Tai, and Peter J. Klenow. 2007. 'Misallocation and Manufacturing
    TFP in China and India.' NBER Working Paper No. 13290, revised December 2008."
  url: https://www.nber.org/system/files/working_papers/w13290/w13290.pdf
  date: 2007
  supports:
  - identity
  - timeline
  - assignment
  - design
  - threats
  - empirical_requirements
  - design_applications
  - method_transfer
  verification_status: verified
  access_level: full-text
  locator: NBER Working Paper 13290 PDF, Sections II-IV and Tables 1-4
design_applications:
- paper: 'Misallocation and Manufacturing TFP in China and India'
  doi: 10.1162/qjec.2009.124.4.1403
  journal: The Quarterly Journal of Economics
  year: 2009
  research_question: How much does the misallocation of capital and labor across manufacturing
    plants lower aggregate TFP in China and India relative to the U.S.?
  population: Manufacturing plants in China (1998-2005), India (1987-1994), and the
    U.S. (1977-1997).
  outcome: Aggregate manufacturing TFP and the dispersion of plant-level revenue productivity
    (TFPR) within 4-digit industries.
  data_used:
  - Chinese Annual Survey of Industrial Production
  - Indian Annual Survey of Industries
  - U.S. Census of Manufactures
  - NBER Productivity Database for industry factor shares
  treatment_encoding: Not a treatment. Plant-level TFPR computed from revenue, capital,
    and labor using industry production functions.
  comparison: Compare within-industry TFPR dispersion in China and India to the U.S.
    benchmark; compute TFP gains from equalizing TFPR.
  empirical_design: Structural measurement exercise using plant-level data and a monopolistic-competition
    model.
  assumptions:
  - Monopolistic competition with constant elasticity of demand
  - Cobb-Douglas production with U.S. industry factor shares
  - U.S. provides an efficient allocation benchmark
  - Fixed number of plants
  threats_addressed:
  - Measurement error robustness checks
  - Alternative elasticities of substitution
  - Comparison of TFPQ and TFPR dispersion
  - Sensitivity to trimming tails
  evidence_refs:
  - E1
  - E2
method_transfer:
  source_context: Hsieh and Klenow (2009, QJE) apply the method to manufacturing plants
    in China, India, and the U.S. to quantify how much aggregate TFP is lowered by the
    misallocation of capital and labor across plants within industries.
  strategy_family: Plant-level misallocation measurement using revenue-productivity dispersion
  reusable_logic: Under monopolistic competition with heterogeneous firms, revenue productivity
    (TFPR) should be equalized across plants within an industry in the absence of distortions.
    Deviations of TFPR from the industry mean reveal the combined effect of output and capital
    distortions. The variance of log TFPR provides a sufficient statistic for the TFP loss
    from misallocation when the joint distribution of productivity and distortions is log-normal.
    Comparing this variance to a benchmark efficient economy yields an estimate of potential
    TFP gains from reallocation.
  construction_steps:
  - Assemble plant-level data on revenue or value added, capital stock, labor compensation,
    intermediate inputs, industry code, and year.
  - Assign industry-specific capital and labor elasticities, typically from the U.S.
    benchmark.
  - Choose an elasticity of substitution σ between differentiated products (benchmark
    σ = 3).
  - Compute plant physical productivity TFPQ and revenue productivity TFPR using the
    Hsieh-Klenow formulas.
  - Trim extreme tails of log TFPR and log TFPQ to reduce outlier influence.
  - Calculate the within-industry variance of log TFPR.
  - Compare the variance to the U.S. benchmark or to the same country in another period.
  - Compute the aggregate TFP gain from hypothetically equalizing TFPR across plants
    within each industry.
  - Optionally decompose TFPR variance by plant characteristics such as ownership, size,
    age, or region.
  source_treatment_or_endogenous_variable: Plant-level output and capital distortions,
    which drive wedges between marginal revenue products of capital and labor across plants.
  source_instrument_or_assignment: No instrumental variable. Identification comes from
    the structural assumption that TFPR would be equalized absent distortions, combined
    with a benchmark efficient allocation (the U.S.).
  first_stage_or_contrast: Contrast the observed distribution of plant TFPR in the study
    country or period with the efficient benchmark distribution; the difference in dispersion
    identifies the potential TFP gain from reallocation.
  identifying_assumptions:
  - Plants face a constant-elasticity demand curve and produce with Cobb-Douglas technology.
  - Industry production elasticities are known and can be borrowed from a benchmark economy.
  - The benchmark economy (U.S.) is undistorted enough to serve as an efficient counterfactual.
  - Distortions are the only source of TFPR dispersion within industries.
  - The number of plants and aggregate factor supplies are held fixed in the counterfactual.
  diagnostics:
  - Plot distributions of log TFPQ and log TFPR across countries
  - Report variance of log TFPR and implied TFP gains for σ = 3 and σ = 5
  - Decompose TFPR variance by ownership, size, age, and region
  - Trim tails and re-estimate to assess outlier influence
  - Compare results using employment vs. wage bill as labor input
  china_use_cases:
  - Apply to Chinese Annual Survey of Industrial Enterprises to measure misallocation
    across provinces, ownership types, or industries
  - Evaluate the TFP impact of reforms that reduce capital-market frictions or privatize
    state-owned enterprises
  - Study how local government subsidies, tax enforcement, or financial constraints affect
    the dispersion of marginal revenue products
  - Compare allocative efficiency before and after China's WTO accession or other policy
    shocks
  china_data_requirements:
  - Chinese plant-level survey data with revenue or value added, capital stock, labor
    compensation, employment, intermediate inputs, and industry codes
  - Comparable data for a benchmark economy such as the U.S.
  - Industry-level factor shares and an assumed elasticity of substitution
  - Deflators for output, capital, and intermediate inputs
  transfer_limits:
  - The method does not identify specific policies; it measures the combined effect of
    all distortions.
  - It assumes away dynamic adjustment, entry, exit, and general-equilibrium feedback.
  - Results are sensitive to measurement error in capital, labor, and prices.
  - The log-normality-based closed form is an approximation; non-log-normal distributions
    require numerical integration.
  - Borrowing U.S. production elasticities and benchmarks may be inappropriate for sectors
    or countries with very different technologies.
readiness_blockers:
- Replication code for the exact Hsieh-Klenow calculations was not accessed; researchers
  should implement the formulas independently or obtain the authors' code.
- The published QJE article's full text was not accessed; cross-check parameter choices
  and robustness details against the final version.
---
---
## Institutional Background

The Hsieh-Klenow method builds on two strands of work. Restuccia and Rogerson (2008) showed that misallocation of resources across heterogeneous firms can substantially lower aggregate TFP. Foster, Haltiwanger, and Syverson (2008) emphasized the distinction between physical productivity (TFPQ) and revenue productivity (TFPR), showing that plant-specific prices cause measured revenue productivity to differ from true technical efficiency. Hsieh and Klenow (2009) combine these insights in a standard monopolistic-competition model and use plant-level data from China, India, and the U.S. to quantify the TFP cost of misallocation [E1; E2].

## What Changed

The method does not exploit a policy change. Instead, it uses the cross-sectional distribution of plant TFPR within industries to infer the economy-wide cost of distortions. In the absence of distortions, TFPR should be equalized across plants within an industry because more efficient plants expand until lower prices offset their higher physical productivity. When TFPR differs across plants, it indicates that output or capital distortions are preventing resources from flowing to their most productive uses [E2].

## Implementation and Assignment

There is no treatment assignment. Researchers compute TFPR and TFPQ for each plant using observed revenue, capital, labor, and intermediate inputs. They then measure the within-industry dispersion of log TFPR and compare it to the U.S. benchmark. The counterfactual reallocates capital and labor so that all plants within an industry have the same TFPR, holding aggregate inputs fixed. The resulting TFP gain is interpreted as an upper-bound estimate of the cost of misallocation [E2].

## Why This Creates Empirical Variation

The variation comes from differences in plant-level marginal revenue products within narrowly defined industries. These differences can arise from capital-market frictions, output subsidies or taxes, size-dependent regulations, monopoly power, or other distortions. By comparing the dispersion of TFPR across countries or over time, researchers can quantify how much aggregate TFP is lost to misallocation and how reforms affect allocative efficiency [E2].

## Identification Risks

The main risks are (i) measurement error in plant-level inputs and outputs, which inflates TFPR dispersion; (ii) model misspecification if production functions, demand elasticities, or market structure differ from the assumptions; (iii) inability to identify specific distortions without additional covariates or exogenous variation; (iv) partial-equilibrium counterfactuals that ignore general-equilibrium responses; and (v) limited external validity when U.S. benchmarks are applied to very different sectors or countries [E2].

## Data Requirements

The method requires plant- or firm-level panel data with revenue or value added, capital stock, labor compensation (or employment), intermediate inputs, industry codes, and ideally ownership and location indicators. For China, the Annual Survey of Industrial Enterprises is the standard source. A benchmark economy such as the U.S. Census of Manufactures is used to calibrate industry factor shares and the efficient level of TFPR dispersion [E2].

## Evidence Notes

The method and its application are documented in Hsieh and Klenow (2009, *Quarterly Journal of Economics*, E1) and in greater detail in NBER Working Paper 13290 (E2). The working paper provides the full model, formulas, data description, and results [E1; E2].
