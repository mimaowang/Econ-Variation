---
schema_version: 2
id: land-gradient-iv-infrastructure-rollout
name: Topographic-Cost Instrumental Variable for Infrastructure Rollout (Dinkelman)
aliases:
- land gradient IV
- topographic cost instrument
- rural electrification instrument
- infrastructure placement IV
- Dinkelman electrification IV
status: extracted
provenance:
  task_id: task-0e00020cfdcb
scope:
  country: South Africa
  regions:
  - KwaZulu-Natal ex-homeland communities
  domains:
  - infrastructure
  - energy
  - development
  - labor
  - instrumental-variables
  - economic-geography
  variation_type: other
  knowledge_role: transferable-method
  china_relevance: Topographic cost is a widely proposed instrument for infrastructure
    placement in China, including rural electrification, county grid extension, highway
    and railway routing, broadband rollout, and natural-gas village connection programs.
    The method is portable, but its validity in China depends on whether terrain is
    plausibly excluded from local economic outcomes after conditioning on road access,
    agricultural suitability, and administrative targeting.
identity:
  instrument: Community land gradient (slope/steepness) used as an instrumental variable
    for the timing or probability of infrastructure rollout, exploiting the higher
    construction cost of networks in steeper terrain.
  authority: Taryn Dinkelman (2011, American Economic Review)
  legal_identifiers:
  - "Dinkelman, Taryn. 2011. 'The Effects of Rural Electrification on Employment: New
    Evidence from South Africa.' American Economic Review 101(7): 3078-3108."
  implementation_regime: Post-apartheid South Africa's mass rural electrification program,
    implemented by the national utility Eskom between 1996 and 2001, which connected
    communities in former homeland areas of KwaZulu-Natal. Project prioritization was
    driven in part by cost per household connection, which rises with land gradient.
  assignment_mechanism: Not randomized. The instrument exploits variation in terrain
    slope across communities as a cost shifter that affects the order or probability
    of electrification, conditional on district fixed effects and baseline controls.
  parent: null
  related_variations:
  - us-railroad-market-access-method
  - dell-boundary-discontinuity-method
  - china-highway-network-expansion
  - china-rural-land-titling-reform
timeline:
  announcement: '1994-01-01'
  effective: null
  implementation_start: 1996
  implementation_end: 2001
  local_timing: The electrification rollout studied in the source paper took place between
    1996 and 2001 in rural KwaZulu-Natal. The method can be applied to any infrastructure
    expansion period for which terrain, rollout timing, and outcome data are available.
  anticipation: Communities could not manipulate their land gradient, but political
    targeting of electrification may have responded to local conditions; the IV strategy
    attempts to isolate the cost-driven component of rollout timing.
  last_verified: '2026-07-14'
assignment:
  unit: Community or village-year.
  treated: Communities that received an electrification project (or other infrastructure)
    during the rollout period.
  comparison_pool: Communities that had not yet received a project, or the same communities
    before project arrival.
  rule: Assign treatment based on observed project placement. Instrument treatment with
    a topographic cost measure (land gradient, slope, ruggedness) interacted with time
    in a panel setting.
  intensity: Binary project dummy or continuous electrification rate; the instrument is
    continuous (gradient) interacted with a time trend or period dummy.
  exemptions: []
  compliance: Partial; infrastructure rollout reflects both cost and political/economic
    targeting. The instrument isolates only the cost-driven component.
  exposure_construction: Compute a terrain gradient or ruggedness measure for each community
    from a digital elevation model. Interact it with year or post-period indicators to
    form the instrument for infrastructure placement in a two-stage least squares or
    limited-information maximum likelihood framework.
  required_identifiers:
  - community identifier
  - year
  - terrain gradient or slope
  - infrastructure placement indicator
  spillovers: Electrification in one community may affect labor markets in neighboring
    communities through migration or market access; road and electricity networks are
    spatially correlated, making it hard to separate their effects.
research_compatibility:
  outcome_domains:
  - employment
  - labor-force-participation
  - female-employment
  - time-use
  - household-energy-use
  - microenterprise-development
  - migration
  - wages
  affected_populations:
  - rural households
  - women
  - agricultural workers
  - small business owners
  - infrastructure planners
  mechanism_channels:
  - reduction in home-production time
  - enabling microenterprises
  - lighting and appliance adoption
  - labor-market participation
  - migration responses
  best_for:
  - Evaluating the local effects of infrastructure placement when rollout is endogenous
  - Settings where construction cost varies sharply and observably with terrain
  - Outcomes measured at the community, household, or firm level with panel structure
  not_good_for:
  - Settings where terrain is also correlated with other infrastructure or economic potential
  - Outcomes for which the exclusion restriction cannot be defended
  - Short panels with weak first-stage relationships
  - Cases where political targeting dominates cost considerations
design:
  claim_type: method-pattern
  affordances:
  - Uses widely available GIS terrain data
  - Can be implemented in a standard two-stage least squares framework
  - Allows panel fixed effects to absorb time-invariant community heterogeneity
  - Provides a plausibly exogenous cost shifter for infrastructure placement
  candidate_designs:
  - Two-stage least squares with terrain gradient as the instrument for electrification
  - Panel community fixed-effects IV with gradient interacted with time
  - Limited-information maximum likelihood or weak-IV robust Anderson-Rubin confidence
    intervals
  - Placebo tests using pre-existing infrastructure or non-treated communities
  - Extensions to other infrastructure types (roads, railways, broadband, pipelines)
  identifying_variation: Cross-sectional and over-time variation in infrastructure placement
    driven by differences in terrain-related construction costs across communities.
  primary_strategy: Estimate the effect of infrastructure access on local outcomes by
    instrumenting observed placement with a topographic cost measure, conditioning on
    fixed effects and baseline controls.
  estimand: The local average treatment effect of infrastructure placement on the outcome
    of interest for communities whose rollout timing is shifted by terrain cost.
  treatment_variable: Observed community-level infrastructure placement or access indicator.
  comparison_logic: Compare communities with similar cost-driven rollout probabilities
    but different actual placement, using terrain as the exogenous cost shifter.
  estimation_notes: Include district or community fixed effects and baseline controls.
    Report weak-instrument tests (Kleibergen-Paap F-statistic, Montiel-Olea-Pflueger
    effective F) and weak-IV-robust confidence intervals. Be cautious with point estimates
    when the instrument is weak.
  assumptions:
  - Terrain gradient affects infrastructure placement through construction cost.
  - Terrain gradient is uncorrelated with unobserved determinants of the outcome, conditional
    on fixed effects and controls.
  - Other infrastructure channels correlated with terrain (especially roads) are adequately
    controlled for or do not confound the dynamic path of the outcome.
  - The first-stage relationship is strong enough for reliable IV inference.
  diagnostics:
  - Report first-stage coefficients and weak-instrument tests
  - Construct Anderson-Rubin or similar weak-IV-robust confidence intervals
  - Placebo tests using non-treated communities or pre-existing infrastructure
  - Test for correlation between gradient and outcomes in untreated areas
  - Assess sensitivity to excluding communities near major roads or other infrastructure
  - Compare OLS and IV estimates to evaluate selection bias
  - Examine heterogeneity by baseline road access and market proximity
threats:
- type: weak-instrument
  basis: reported
  condition: The first-stage F-statistic in the source paper is below conventional thresholds
    (around 8), so the IV point estimates may be biased and inference unreliable.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Report Kleibergen-Paap and Montiel-Olea-Pflueger weak-instrument tests
  - Use weak-IV-robust confidence intervals instead of standard errors
  - Avoid interpreting point estimates as precise causal effects
- type: exclusion-restriction-violation
  basis: reported
  condition: Land gradient may affect employment and other outcomes through channels other
    than electrification, such as road construction costs, agricultural suitability, transport
    costs, and migration patterns.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Test for reduced-form effects of gradient on outcomes in non-electrified communities
  - Control flexibly for road access and other infrastructure, while recognizing post-instrument
    bias risks
  - Use heterogeneous-effects specifications by road proximity
- type: post-instrument-bad-control
  basis: reported
  condition: Controlling for road access after instrumenting with gradient may introduce
    bias if road access is itself affected by the instrument and correlated with unobserved
    confounders.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Omit road controls and compare estimates
  - Use pre-determined road measures rather than contemporaneous ones
  - Sensitivity analysis excluding communities near roads
- type: external-validity
  basis: inferred
  condition: The South African post-apartheid context, household electrification technology,
    and labor-market institutions may not transfer directly to other countries.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Replicate in other infrastructure rollouts with similar cost-terrain relationship
  - Test for heterogeneity by baseline development and infrastructure density
- type: measurement-error
  basis: inferred
  condition: Terrain measures and infrastructure placement data may be mismeasured or
    misaligned in space or time.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Cross-validate gradient measures across DEM sources
  - Use alternative topographic cost measures (slope, ruggedness, elevation variance)
empirical_requirements:
  contract_version: 1
  population: Communities or villages experiencing an infrastructure rollout in a setting
    where terrain affects construction cost.
  observation_unit: Community-year or village-year.
  geography_level: Community / village.
  time_start: null
  time_end: null
  minimum_frequency: annual or cross-sectional with two waves
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - community identifier
  - year
  - terrain gradient or slope from DEM
  - infrastructure placement or access indicator
  - outcome of interest
  - baseline community characteristics
  - road access and other infrastructure controls
  - district or region identifier
  required_identifiers:
  - community ID
  - year
  treatment_key:
  - community ID
  - year
  - infrastructure placement indicator
  - terrain gradient
  treatment_source: Constructed from GIS digital elevation models and administrative infrastructure
    rollout records.
  measurement_risks:
  - Terrain gradient may be measured at different resolutions or computed differently across
    studies.
  - Infrastructure placement dates may not match the timing of actual service availability.
  - Community boundaries may change over time.
  - Road and other infrastructure data may be incomplete.
  - Spatial correlation can bias standard errors.
evidence:
- id: E1
  source_type: paper
  citation: "Dinkelman, Taryn. 2011. 'The Effects of Rural Electrification on Employment:
    New Evidence from South Africa.' American Economic Review 101(7): 3078-3108."
  url: https://doi.org/10.1257/aer.101.7.3078
  date: 2011
  supports:
  - identity
  - timeline
  - design
  - assignment
  verification_status: reported
  access_level: abstract
  locator: AER article abstract and citation (DOI 10.1257/aer.101.7.3078)
- id: E2
  source_type: scholarship
  citation: "Bensch, Gunther, Gunnar Gotz, and Joerg Peters. 2020. 'Effects of Rural Electrification
    on Employment: A Comment on Dinkelman (2011).' Ruhr Economic Papers No. 840, RWI –
    Leibniz-Institut fuer Wirtschaftsforschung."
  url: https://www.econstor.eu/bitstream/10419/214184/1/1690488735.pdf
  date: 2020
  supports:
  - identity
  - assignment
  - design
  - threats
  - empirical_requirements
  - method_transfer
  verification_status: verified
  access_level: full-text
  locator: Full comment PDF; Sections 2-3 document weak-instrument tests, exclusion-restriction
    placebo tests, and the road-access confounding problem
design_applications:
- paper: 'The Effects of Rural Electrification on Employment: New Evidence from South Africa'
  doi: 10.1257/aer.101.7.3078
  journal: American Economic Review
  year: 2011
  research_question: Does rural electrification increase female employment by releasing
    women from home production and enabling microenterprises?
  population: Rural communities in former homeland areas of KwaZulu-Natal, South Africa,
    1996-2001.
  outcome: Female and male employment rates, hours worked, wages, energy use, migration.
  data_used:
  - South Africa Census 1996 and 2001
  - Eskom electrification project records
  - GIS land gradient data for communities
  - Road access maps
  - Household survey data on time use and energy sources
  treatment_encoding: Community-level electrification project dummy, instrumented by land
    gradient interacted with time.
  comparison: Communities with steeper vs. flatter terrain within the same district, used
    as a cost-driven instrument for rollout timing.
  empirical_design: Two-stage least squares with community and district fixed effects;
    Anderson-Rubin weak-IV robust confidence intervals.
  assumptions:
  - Land gradient affects electrification timing only through construction cost
  - Gradient is uncorrelated with unobserved labor-market trends after conditioning on
    controls
  - Road access controls do not induce post-instrument bias
  threats_addressed:
  - Endogenous project placement via terrain instrument
  - District fixed effects absorb regional trends
  - Baseline controls for community characteristics
  evidence_refs:
  - E1
  - E2
method_transfer:
  source_context: Dinkelman (2011, AER) studies South Africa's post-apartheid rural electrification
    rollout in KwaZulu-Natal. She instruments community-level electrification placement
    with land gradient, arguing that steeper terrain raises connection costs and therefore
    delays or reduces electrification.
  strategy_family: Topographic-cost instrumental variable for infrastructure placement
  reusable_logic: Infrastructure planners often prioritize low-cost areas. Terrain slope
    or ruggedness is a plausibly exogenous cost shifter that can instrument for the timing
    or probability of infrastructure rollout, provided it is unrelated to outcomes except
    through the infrastructure channel.
  construction_steps:
  - Assemble a panel of communities or villages with infrastructure rollout records.
  - Obtain a digital elevation model and compute terrain gradient, slope, or ruggedness
    for each unit.
  - Construct the endogenous treatment variable (e.g., indicator for having received the
    infrastructure by year t, or continuous coverage rate).
  - Interact the terrain measure with time or post-period indicators to form the instrument.
  - Estimate a two-stage least squares regression of the outcome on treatment, instrumenting
    treatment with the terrain-time interaction.
  - Include unit and time fixed effects, district fixed effects, and baseline controls.
  - Report weak-instrument diagnostics and weak-IV-robust confidence intervals.
  - Conduct placebo tests in untreated or pre-existing-infrastructure areas.
  source_treatment_or_endogenous_variable: Infrastructure placement or access (e.g., electrification,
    road, railway, broadband, pipeline).
  source_instrument_or_assignment: Community land gradient (or other topographic cost measure)
    interacted with time, used as an instrument for infrastructure rollout.
  first_stage_or_contrast: The first stage relates infrastructure placement to terrain cost;
    flatter communities are connected earlier or at higher rates. The contrast compares
    communities whose rollout timing is shifted by terrain cost.
  identifying_assumptions:
  - Terrain affects infrastructure placement through construction cost.
  - Terrain is uncorrelated with unobserved determinants of the outcome, conditional on
    controls and fixed effects.
  - Other terrain-correlated infrastructure channels (especially roads) do not confound
    the outcome path.
  - The first-stage relationship is sufficiently strong.
  diagnostics:
  - First-stage coefficient and R-squared
  - Weak-instrument tests (Kleibergen-Paap F, Montiel-Olea-Pflueger effective F)
  - Weak-IV-robust Anderson-Rubin confidence intervals
  - Placebo tests in untreated or pre-connected communities
  - Tests for gradient-outcome correlation in non-treated areas
  - Sensitivity to road-access controls and distance-to-road cutoffs
  china_use_cases:
  - Instrument rural electrification rollout in China's county/village grid extension programs
  - Study the effect of highway or railway routing on local development using terrain cost
  - Evaluate broadband or natural-gas village connection programs where rollout follows
    cost considerations
  - Analyze the effect of irrigation or water infrastructure placement in hilly vs. flat
    villages
  china_data_requirements:
  - GIS digital elevation model for China (e.g., SRTM, ASTER GDEM) at village or county
    level
  - Administrative records of infrastructure rollout timing and coverage at county, township,
    or village level
  - Population census, household surveys (CFPS, CHIP), or firm data with geographic identifiers
  - Road network, railway, and other infrastructure maps to assess confounding
  - Agricultural suitability and land-use data to test exclusion restriction
  transfer_limits:
  - Terrain in China is often correlated with road access, agricultural potential, ethnic
    minority location, tourism, and administrative targeting, threatening the exclusion
    restriction.
  - The first-stage relationship may be weak if political targeting or central planning
    overrides cost considerations.
  - Controlling for road access as a covariate can introduce post-instrument bias.
  - China's infrastructure rollouts are often coordinated with industrial policy and poverty
    targeting, which may be correlated with terrain.
  - The method captures local average treatment effects for cost-shifted compilers only.
readiness_blockers:
- The full AER paper and replication package were not accessed; cross-check the exact first-stage
  specifications, variable definitions, and robustness checks against the published article.
- No China-specific application of the terrain-cost IV was independently verified inside this
  record; researchers must test the exclusion restriction in their specific Chinese setting.
- The instrument is weak and contested in the source context, so any China transfer should
  report weak-IV robust inference and avoid over-interpreting point estimates.
---
---
## Institutional Background

In post-apartheid South Africa, the national utility Eskom committed to universal electrification. Rural communities in the former homelands of KwaZulu-Natal were among the target areas. Because grid extension is costly, Eskom's planners prioritized communities where connection costs were lower. Taryn Dinkelman (2011) exploits this cost-driven prioritization by using community land gradient as an instrument for electrification placement [E1].

## What Changed

Between 1996 and 2001, many rural communities in KwaZulu-Natal gained electricity access for the first time. The rollout was not random: flatter, cheaper-to-connect communities were more likely to be connected early. Dinkelman compares employment and other outcomes across communities whose connection timing was shifted by terrain cost [E1].

## Implementation and Assignment

The treatment is observed electrification project placement. The instrument is land gradient, a continuous measure of terrain steepness computed from elevation data. The identifying assumption is that, conditional on district fixed effects and baseline controls, gradient affects employment only through its effect on electrification costs and rollout timing. The first stage relates electrification to gradient, with flatter communities connected earlier [E1; E2].

## Why This Creates Empirical Variation

Terrain gradient is largely exogenous to local economic conditions and affects infrastructure construction costs. Where planners use cost to prioritize rollout, gradient creates quasi-experimental variation in the timing of infrastructure access. This variation can be used to estimate the causal effect of infrastructure on local outcomes in a two-stage least squares framework [E1].

## Identification Risks

A replication and extension by Bensch, Gotz, and Peters (2020) raises serious concerns. They show that the first-stage F-statistic is below conventional weak-instrument thresholds, the land gradient is correlated with female employment even in non-electrified communities, and gradient also predicts road access. Controlling for road access may introduce post-instrument bias. These findings imply that the exclusion restriction is questionable and that the IV point estimates are difficult to interpret reliably [E2].

## Data Requirements

The method requires community-level infrastructure rollout data, a digital elevation model from which to compute gradient or slope, and outcome data with geographic identifiers. For China, researchers would need village or county-level electrification (or other infrastructure) records, Chinese DEM data, and household/census or firm data that can be matched to the same geographic units [E1; E2].

## Evidence Notes

The source paper is Dinkelman (2011, *American Economic Review*, E1). The detailed critique and replication by Bensch, Gotz, and Peters (2020, Ruhr Economic Papers, E2) documents weak-instrument problems, exclusion-restriction challenges, and the road-access confounding issue. Any transfer of the topographic-cost IV to China must independently verify the first-stage strength and exclusion restriction [E1; E2].
