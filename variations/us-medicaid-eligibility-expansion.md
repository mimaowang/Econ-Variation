---
schema_version: 2
id: us-medicaid-eligibility-expansion
name: State-Level Expansions of Medicaid Eligibility for Pregnant Women and Infants (1980s–1990s)
aliases:
- Medicaid eligibility expansion for pregnant women
- Currie Gruber Medicaid infant mortality
- Saving Babies Medicaid expansion

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: United States
  regions:
  - All US states
  domains:
  - health
  - public-finance
  - insurance
  - maternal-health
  - infant-health
  variation_type: staggered-rollout
  knowledge_role: transferable-method
  china_relevance: The source setting is outside China; retain the reusable identification construction rather than recommend
    the foreign shock as a China treatment.
identity:
  instrument: Federal mandates and state-level options that expanded Medicaid income-eligibility thresholds for pregnant women
    and infants, phased in across states between 1979 and 1992
  authority: US Congress (federal legislation) and state Medicaid agencies
  legal_identifiers:
  - Omnibus Budget Reconciliation Acts of 1986 (OBRA-86)
  - 1987 (OBRA-87)
  - and 1990 (OBRA-90); earlier state-level optional expansions
  implementation_regime: Federal law repeatedly raised the maximum income threshold for Medicaid eligibility among pregnant
    women and children, gradually expanding from categorical eligibility (welfare-linked) to income-based thresholds reaching
    133–185% of the federal poverty line; states also had the option to expand earlier and more generously than federal minimums
  assignment_mechanism: Variation in the timing and generosity of eligibility expansions across states and over time; some
    variation is driven by federal mandates and some by state-level policy choices
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 1979
  implementation_end: 1992
  local_timing: States implemented eligibility expansions at different times; earlier-adopting states created variation in
    effective dates, while federal mandates set nationwide floors
  anticipation: Federal legislative debates may have been anticipated; state-level optional expansions were endogenous to
    state political and fiscal conditions
  last_verified: '2026-07-13'
assignment:
  unit: Woman of childbearing age or infant, by state and year
  treated: Women and infants who became eligible for Medicaid coverage as a result of eligibility expansions (by income, marital
    status, or pregnancy status)
  comparison_pool: Women and infants who were already eligible or remained ineligible; within-state variation over time in
    the fraction eligible
  rule: Eligibility is determined by income relative to the state-year-specific Medicaid threshold for the relevant demographic
    category (pregnant women, infants, children of specific ages)
  intensity: Continuous or semi-continuous — the fraction of the target population made eligible varies by state-year; eligibility
    expansions can be parameterized as the percentage-point change in the eligible fraction
  exemptions: []
  compliance: Take-up of Medicaid coverage among the newly eligible is incomplete; estimated take-up rates range from approximately
    15–50% depending on the population and expansion characteristics
  exposure_construction: Simulate eligibility for each woman in survey data (e.g., CPS, Vital Statistics) based on her state,
    year, income, marital status, and pregnancy status relative to the state-year-specific Medicaid rules; construct the fraction
    eligible at the state-year-demographic cell level
  required_identifiers:
  - state code
  - calendar year
  - income
  - marital status
  - pregnancy status
  - age of child
  spillovers: Expansions may crowd out private insurance coverage; eligibility changes may affect provider behavior, hospital
    financing, and the supply of prenatal care in ways that affect ineligible populations
research_compatibility:
  outcome_domains:
  - infant mortality
  - birth weight
  - prenatal care utilization
  - maternal health
  - health insurance coverage
  - healthcare costs
  - child health
  affected_populations:
  - pregnant women
  - infants
  - low-income families
  - near-poor families
  - unmarried mothers
  mechanism_channels:
  - health insurance coverage
  - prenatal care
  - physician visits
  - hospital care
  - maternal health investments
  - financial protection
  best_for:
  - Studying the health effects of health insurance coverage for vulnerable populations
  - Outcomes recorded in Vital Statistics (birth and death certificates) with state and year identifiers
  - Designs using simulated eligibility instruments to address endogenous take-up
  not_good_for:
  - Outcomes requiring individual-level panel data (Vital Statistics is a repeated cross-section)
  - Long-run outcomes unless linked to administrative data
  - Populations outside the targeted demographic categories
  - Research questions about quality rather than quantity of care
design:
  affordances:
  - staggered timing of federal and state expansions
  - variation in generosity across states at the same point in time
  - ability to simulate eligibility for each woman in nationally representative survey data
  candidate_designs:
  - difference-in-differences with staggered treatment timing
  - simulated eligibility instrumental variables
  - triple differences (e.g., by income group × state × year)
  - event study around expansion dates
  identifying_variation: Changes in predicted Medicaid eligibility — driven by the interaction of federal and state policy
    changes with individual characteristics — over time, across states, and across income groups
  assumptions: &id001
  - Changes in state-level eligibility rules are uncorrelated with other determinants of infant health (conditional on state
    and year fixed effects and observable controls)
  - The simulated eligibility instrument affects outcomes only through actual Medicaid coverage
  - Vital Statistics data accurately identifies state and year of birth for linking to policy rules
  diagnostics: &id002
  - Test whether state-level expansions are predicted by pre-existing infant mortality trends
  - Estimate both reduced-form (eligibility → outcome) and IV (eligibility → coverage → outcome)
  - Compare targeted versus broad expansions (differential take-up and selection)
  - Control for other state-level policies (welfare reform, EITC, WIC)
  - Assess sensitivity to alternative simulation assumptions
  primary_strategy: Difference-in-differences with simulated eligibility instrument; reduced-form estimates of eligibility
    on infant mortality; IV estimates of coverage on infant mortality using simulated eligibility as instrument
  estimand: The causal effect of the recorded exposure on Infant mortality, neonatal mortality, birth weight, prenatal care
    visits, conditional on the stated design assumptions.
  treatment_variable: Simulated eligibility indicator for each woman/infant based on state-year income thresholds relative
    to reported or imputed income; aggregated to the fraction eligible at the state-year-demographic-group level; targeted
    versus broad expansions distinguished
  comparison_logic: Within-state changes in infant mortality associated with changes in the fraction of women eligible for
    Medicaid, relative to states with different expansion timing and magnitude
  estimation_notes: Difference-in-differences with simulated eligibility instrument; reduced-form estimates of eligibility
    on infant mortality; IV estimates of coverage on infant mortality using simulated eligibility as instrument
threats:
- type: endogenous-state-policy
  basis: documented
  condition: States that chose to expand earlier or more generously may differ systematically from late adopters; pre-existing
    trends in infant health may confound the estimates
  evidence_refs:
  - E1
  possible_diagnostics:
  - test for differential pre-trends
  - control for state-specific time trends
  - use only federally mandated variation
  - compare early and late adopters
- type: incomplete-take-up
  basis: documented
  condition: Many newly eligible women do not enroll in Medicaid; the reduced form captures the effect of eligibility, not
    coverage; IV adjustment requires the standard LATE assumptions
  evidence_refs:
  - E1
  possible_diagnostics:
  - estimate both reduced-form and IV
  - report first-stage take-up rates
  - analyze complier characteristics
- type: crowd-out
  basis: reported
  condition: Public insurance expansions may displace private coverage; if healthier individuals drop private insurance in
    favor of Medicaid, the average health effect of coverage may be attenuated
  evidence_refs:
  - E1
  possible_diagnostics:
  - estimate crowd-out rates
  - compare effects among those previously uninsured versus privately insured
  - use alternative data sources with private insurance information
- type: contemporaneous-policies
  basis: inferred
  condition: The same period saw expansions of WIC, AFDC reform, EITC expansion, and hospital Medicaid Disproportionate Share
    Hospital (DSH) payments, making it difficult to isolate Medicaid eligibility effects
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for concurrent policies
  - use policy variation orthogonal to other reforms
  - estimate effects in subpopulations differentially affected by different policies
empirical_requirements:
  contract_version: 1
  population: Pregnant women and infants in the United States, particularly those near the Medicaid eligibility thresholds,
    observed during the expansion period
  observation_unit: Individual birth record (repeated cross-section) or state-year demographic cell
  geography_level: State
  time_start: 1979
  time_end: 1992
  minimum_frequency: annual
  minimum_pre_periods: 5
  minimum_post_periods: 5
  required_fields:
  - state of residence
  - year of birth
  - infant mortality or birth weight
  - maternal age
  - maternal education
  - marital status
  - maternal race/ethnicity
  - plurality
  - parity
  required_identifiers:
  - state code
  - calendar year
  - maternal demographic groups for eligibility simulation
  treatment_key:
  - state code
  - calendar year
  - income-eligibility threshold
  - eligibility indicator
  treatment_source: State Medicaid eligibility rules compiled from federal legislation (OBRA-86, OBRA-87, OBRA-90) and state
    plan amendments; income thresholds documented in HCFA/CMS reports and academic compilations
  measurement_risks:
  - incomplete documentation of early state-level rules
  - income measurement error in survey data
  - retrospective policy coding errors
  - changing state boundaries and codes
  - undocumented state implementation lags
evidence:
- id: E1
  source_type: paper
  citation: 'Currie, Janet, and Jonathan Gruber. 1996. "Saving Babies: The Efficacy and Cost of Recent Changes in the Medicaid
    Eligibility of Pregnant Women." Journal of Political Economy 104 (6): 1263–1296.'
  url: https://doi.org/10.1086/262059
  date: 1996
  supports:
  - identity
  - assignment
  - design
  - eligibility simulation
  - main estimates
  - cost-benefit analysis
  - targeted versus broad expansions
  verification_status: verified
design_applications:
- paper: 'Saving Babies: The Efficacy and Cost of Recent Changes in the Medicaid Eligibility of Pregnant Women'
  doi: 10.1086/262059
  journal: Journal of Political Economy
  year: 1996
  research_question: Did the 1980s–1990s expansions of Medicaid eligibility for pregnant women reduce infant mortality, and
    at what cost per life saved?
  population: Pregnant women and infants in the United States, approximately 1979–1992, using Vital Statistics natality and
    linked birth-death records
  outcome: Infant mortality, neonatal mortality, birth weight, prenatal care visits
  data_used: []
  treatment_encoding: Simulated eligibility indicator for each woman/infant based on state-year income thresholds relative
    to reported or imputed income; aggregated to the fraction eligible at the state-year-demographic-group level; targeted
    versus broad expansions distinguished
  comparison: Within-state changes in infant mortality associated with changes in the fraction of women eligible for Medicaid,
    relative to states with different expansion timing and magnitude
  empirical_design: Difference-in-differences with simulated eligibility instrument; reduced-form estimates of eligibility
    on infant mortality; IV estimates of coverage on infant mortality using simulated eligibility as instrument
  assumptions:
  - changes in eligibility are conditionally exogenous
  - simulated eligibility is a valid instrument
  - Vital Statistics provides consistent state-year identifiers
  - no differential compositional changes in births across expansion states
  threats_addressed:
  - endogenous take-up via simulated IV
  - state-level heterogeneity via fixed effects
  - income measurement error via simulated eligibility
  - concurrent trends via controls
  evidence_refs:
  - E1
readiness_blockers:
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
- Transfer to a Chinese application has not yet been audited against a specific Chinese institution and dataset.
method_transfer:
  source_context: 'United States: State-Level Expansions of Medicaid Eligibility for Pregnant Women and Infants (1980s–1990s)'
  strategy_family: Difference-in-differences with simulated eligibility instrument; reduced-form estimates of eligibility
    on infant mortality; IV estimates of coverage on infant mortality using simulated eligibility as instrument
  reusable_logic: Variation in the timing and generosity of eligibility expansions across states and over time; some variation
    is driven by federal mandates and some by state-level policy choices
  construction_steps:
  - Simulate eligibility for each woman in survey data (e.g., CPS, Vital Statistics) based on her state, year, income, marital
    status, and pregnancy status relative to the state-year-specific Medicaid rules; construct the fraction eligible at the
    state-year-demographic cell level
  source_treatment_or_endogenous_variable: Simulated eligibility indicator for each woman/infant based on state-year income
    thresholds relative to reported or imputed income; aggregated to the fraction eligible at the state-year-demographic-group
    level; targeted versus broad expansions distinguished
  source_instrument_or_assignment: Variation in the timing and generosity of eligibility expansions across states and over
    time; some variation is driven by federal mandates and some by state-level policy choices
  first_stage_or_contrast: Changes in predicted Medicaid eligibility — driven by the interaction of federal and state policy
    changes with individual characteristics — over time, across states, and across income groups
  identifying_assumptions: *id001
  diagnostics: *id002
  china_use_cases:
  - Build a simulated eligibility instrument for Chinese social insurance or public-service programs by applying changing
    policy rules to a fixed reference population.
  china_data_requirements:
  - state of residence
  - year of birth
  - infant mortality or birth weight
  - maternal age
  - maternal education
  - marital status
  - maternal race/ethnicity
  - plurality
  - parity
  transfer_limits:
  - Outcomes requiring individual-level panel data (Vital Statistics is a repeated cross-section)
  - Long-run outcomes unless linked to administrative data
  - Populations outside the targeted demographic categories
  - Research questions about quality rather than quantity of care
---
## Institutional Background

Before the 1980s, Medicaid eligibility for pregnant women was tightly linked to welfare receipt (Aid to Families with Dependent Children, AFDC). Income thresholds were extremely low — typically well below the federal poverty line — and varied dramatically across states. Beginning in the mid-1980s, a series of federal laws (OBRA-86, OBRA-87, OBRA-90) progressively delinked Medicaid from welfare and raised income-eligibility thresholds for pregnant women and infants, eventually reaching 133–185% of poverty. States could, and some did, expand more generously and earlier than federal requirements. [E1]

The policy motivation was straightforward: the US had an infant mortality rate substantially higher than other developed countries, and expanding access to prenatal care through insurance coverage was seen as the most direct policy lever. The question was whether expanding eligibility — as opposed to other interventions — would actually reduce mortality, and at what cost. [E1; analytical inference]

## What Changed

Between 1979 and 1992, the fraction of women aged 15–44 eligible for Medicaid (if pregnant) roughly doubled, from approximately 15% to over 30%. The change was not uniform: some states expanded earlier and more aggressively, creating substantial cross-state and cross-time variation. Eligibility expansions were targeted (higher income thresholds for specific groups like pregnant women) or broad (across-the-board increases affecting many demographic categories). [E1]

## Implementation and Assignment

The key measurement challenge is that eligibility is individual-specific — it depends on income, marital status, state, and year — and income is poorly measured (or unmeasured) in Vital Statistics data. Currie and Gruber address this by simulating eligibility for each woman in the Current Population Survey (CPS) based on the state-year-specific rules, then aggregating to the fraction eligible in each state-year-demographic cell. This simulated eligibility measure is merged to Vital Statistics data. [E1]

## Why This Creates Empirical Variation

The staggered timing of state eligibility expansions, combined with cross-state differences in generosity, creates a difference-in-differences design. States that expanded earlier serve as treated units, with later-expanding states as controls in the early period. The simulated eligibility measure addresses the measurement error problem that would attenuate estimates based on self-reported income. [E1; analytical inference]

## Identification Risks

The central threat is that state adoption of Medicaid expansions may be endogenous to infant health conditions. States with worsening infant mortality may have been more likely to expand. The paper addresses this by testing whether pre-existing infant mortality trends predict subsequent expansions. A subtler threat is that the expansions coincided with other policy changes — welfare reform, WIC, EITC, hospital DSH payments — that independently affected infant health. [E1; analytical inference]

## Data Requirements

This design requires: (1) Vital Statistics birth and death records with state and year identifiers; (2) a state-year database of Medicaid eligibility rules; (3) survey data (CPS) for eligibility simulation; and (4) data on concurrent policies for robustness. The most challenging component is accurately compiling historical Medicaid eligibility rules, which changed frequently and were sometimes documented incompletely. [E1]

## Evidence Notes

E1 is the published JPE article. The central finding — that a 30-percentage-point increase in eligibility reduced infant mortality by 8.5% — was highly influential in subsequent Medicaid policy debates. The finding that targeted expansions were more cost-effective than broad ones (because take-up is higher) has implications for program design. Subsequent work has largely corroborated these findings using alternative identification strategies and more recent data.
