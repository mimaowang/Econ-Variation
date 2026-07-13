---
schema_version: 2
id: china-sex-ratio-competitive-savings
name: Regional Sex Ratio Imbalances and the Rise of Household Savings in China through Competitive Marriage Markets
aliases:
- Wei Zhang competitive saving motive China
- 性别比 竞争性储蓄
- sex ratio savings China
- marriage market competition savings

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - All provinces
  - with variation by prefecture and county sex ratios
  domains:
  - household-finance
  - gender
  - marriage
  - savings
  - macroeconomics
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: Cross-regional variation in sex ratios (the ratio of males to females in the pre-marital age cohort) in China,
    driven by the interaction of son preference, the One-Child Policy, and differential use of sex-selective abortion, creating
    exogenous variation in marriage market competition and household savings behavior
  authority: Demographic forces (son preference, fertility restrictions, sex-selective technology) generating variation in
    pre-marital sex ratios at the regional level
  legal_identifiers:
  - One-Child Policy (1979–2015)
  - pre-marital sex ratio data from Chinese census and surveys
  implementation_regime: The sex ratio imbalance emerged over the 1980s–2000s as the One-Child Policy interacted with strong
    son preference and the spread of ultrasound technology enabling prenatal sex determination and sex-selective abortion;
    by 2005, the sex ratio at birth reached approximately 120 boys per 100 girls
  assignment_mechanism: Regional sex ratios are determined by historical factors (local son preference intensity, enforcement
    of the One-Child Policy, access to prenatal sex-determination technology); these are plausibly exogenous to contemporaneous
    savings decisions
  parent: null
  related_variations:
  - china-missing-women-tea-price
  - china-land-reform-sex-selection
  - china-one-child-policy-twins-iv
timeline:
  announcement: null
  effective: null
  implementation_start: 1980
  implementation_end: 2005
  local_timing: Sex ratio imbalances emerge gradually as cohorts with imbalanced sex ratios enter the marriage market; timing
    varies by province based on policy enforcement and technology diffusion
  anticipation: Households with sons anticipate future marriage market competition; savings behavior adjusts well before the
    son reaches marriage age
  last_verified: '2026-07-13'
assignment:
  unit: Household
  treated: Households with sons in regions with high male-to-female sex ratios (more intense marriage market competition for
    grooms)
  comparison_pool: Households with daughters in the same region; households with sons in regions with balanced sex ratios;
    same households before vs after sex ratio imbalances emerged
  rule: Households with unmarried sons save more when local sex ratios are more male-biased because parents (and the sons
    themselves) need to increase the son's relative attractiveness in the marriage market, where housing wealth and savings
    are an important signal of groom quality
  intensity: Continuous — local sex ratio (males/females at marriageable ages), interacted with the presence of a son in the
    household
  compliance: Savings behavior is a choice; the sex ratio imbalance creates an incentive to save but does not mechanically
    force higher savings
  exemptions: []
  exposure_construction: 'Construct household-level treatment as: presence of son(s) × local sex ratio; local sex ratio measured
    as the male-to-female ratio in the pre-marital age cohort at the prefecture or county level; include household and region
    fixed effects'
  required_identifiers:
  - household ID
  - prefecture/county code
  - son indicator
  - household demographic composition
  spillovers: Competitive savings by some households may raise housing prices and marriage costs, increasing the savings pressure
    on all households with sons (a positional externality)
research_compatibility:
  outcome_domains:
  - household savings rate
  - housing wealth
  - consumption
  - marriage outcomes
  - household debt
  - asset accumulation
  affected_populations:
  - Households with sons
  - unmarried men
  - parents of sons
  - young couples entering marriage market
  mechanism_channels:
  - competitive savings for marriage-market position
  - housing as status good
  - positional externality
  - precautionary savings
  - marriage-market matching
  best_for:
  - Understanding the macroeconomic implications of demographic imbalances
  - testing positional/competitive savings theories
  - studying how marriage markets affect household finance
  not_good_for:
  - Direct measurement of son preference
  - fertility decisions
  - estimating the causal effect of the One-Child Policy per se
design:
  affordances:
  - substantial regional variation in sex ratios
  - panel data on household savings
  - variation in household composition (son vs daughter)
  - pre/post emergence of sex ratio imbalance
  candidate_designs:
  - difference-in-differences (households with sons in high vs low sex ratio regions)
  - triple-difference (region × son presence × time)
  - household fixed effects
  identifying_variation: The interaction of household composition (having a son) with regional sex ratio imbalances; households
    with sons in regions with more skewed sex ratios have stronger savings incentives
  assumptions:
  - Regional sex ratios are conditionally exogenous to household savings preferences
  - sex ratios are driven by factors (son preference
  - policy enforcement
  - ultrasound access) that do not directly affect savings
  - no omitted regional variables that affect both sex ratios and savings
  diagnostics:
  - Test whether sex ratios predict savings for households without sons (placebo)
  - control for regional economic conditions
  - test for pre-existing savings differences by sex ratio before imbalances emerged
  - use province-level policy variation as instrument
  primary_strategy: Difference-in-differences (son × sex ratio); triple-differences; aggregate analysis linking provincial
    savings rates to provincial sex ratios; instrumental variables using provincial One-Child Policy fines as instrument for
    sex ratios
  estimand: The causal effect of the recorded exposure on Household savings rate, housing wealth accumulation, consumption
    patterns, conditional on the stated design assumptions.
  treatment_variable: Household having son(s) × local sex ratio (male/female at marriageable ages)
  comparison_logic: Households with sons vs daughters; high sex ratio regions vs balanced regions; pre-imbalance vs post-imbalance
    period
  estimation_notes: Difference-in-differences (son × sex ratio); triple-differences; aggregate analysis linking provincial
    savings rates to provincial sex ratios; instrumental variables using provincial One-Child Policy fines as instrument for
    sex ratios
threats:
- type: omitted-variable-bias
  basis: inferred
  condition: Regions with more skewed sex ratios may be systematically different on other dimensions (income, culture, development)
    that independently affect savings behavior
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for regional GDP
  - income
  - demographic composition
  - and cultural attitudes
  - use within-region variation over time
  - test placebo on households without sons
  - instrument sex ratios using policy variation
- type: measurement-error
  basis: inferred
  condition: Local sex ratios may be measured with error (census undercount, migration, age misreporting), attenuating estimates
  evidence_refs:
  - E1
  possible_diagnostics:
  - use multiple data sources for sex ratios
  - instrument with province-level policy intensity
  - report specification robustness
empirical_requirements:
  contract_version: 1
  population: Chinese households, 1980–2005 (with sex ratio imbalances intensifying)
  observation_unit: Household-year
  geography_level: Prefecture or county
  time_start: 1980
  time_end: 2005
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 5
  required_fields:
  - household savings
  - income
  - consumption
  - household composition (age
  - sex
  - marital status of all members)
  - housing wealth
  - prefecture/county code
  required_identifiers:
  - household ID
  - survey year
  - prefecture/county code
  treatment_key:
  - son presence indicator
  - local sex ratio (male/female at age 15-30)
  - son-times-sex-ratio interaction
  treatment_source: China Household Income Project (CHIP), Urban Household Survey (UHS), Chinese population census for sex
    ratios, provincial statistical yearbooks
  measurement_risks:
  - savings measurement error in survey data
  - sex ratio mismeasurement due to internal migration
  - household composition changes between survey waves
  - housing wealth valuation
evidence:
- id: E1
  source_type: paper
  citation: 'Wei, Shang-Jin, and Xiaobo Zhang. 2011. "The Competitive Saving Motive: Evidence from Rising Sex Ratios and Savings
    Rates in China." Journal of Political Economy 119 (3): 511–564.'
  url: https://doi.org/10.1086/660887
  date: 2011
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - mechanism analysis
  - aggregate implications
  verification_status: verified
design_applications:
- paper: 'The Competitive Saving Motive: Evidence from Rising Sex Ratios and Savings Rates in China'
  doi: 10.1086/660887
  journal: Journal of Political Economy
  year: 2011
  research_question: Does competition in the marriage market caused by sex ratio imbalances explain the rise in China's household
    savings rate?
  population: Chinese households across provinces with varying sex ratios, 1980–2005
  outcome: Household savings rate, housing wealth accumulation, consumption patterns
  data_used: []
  treatment_encoding: Household having son(s) × local sex ratio (male/female at marriageable ages)
  comparison: Households with sons vs daughters; high sex ratio regions vs balanced regions; pre-imbalance vs post-imbalance
    period
  empirical_design: Difference-in-differences (son × sex ratio); triple-differences; aggregate analysis linking provincial
    savings rates to provincial sex ratios; instrumental variables using provincial One-Child Policy fines as instrument for
    sex ratios
  assumptions:
  - sex ratios conditionally exogenous to savings
  - son presence does not affect savings through channels other than marriage-market competition
  - policy fines affect savings only through sex ratios
  threats_addressed:
  - omitted variables via household and region fixed effects
  - reverse causality via instrument using policy fines
  - measurement error via multiple data sources
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
---
## Institutional Background
China's household savings rate rose dramatically from about 16% in 1990 to over 30% by the late 2000s — one of the highest savings rates in the world. Simultaneously, the sex ratio at birth became increasingly male-biased, rising from the natural rate of about 105 boys per 100 girls to over 120 by 2005. This sex ratio skew was driven by the interaction of strong son preference, the One-Child Policy's fertility restrictions, and the spread of ultrasound technology enabling sex-selective abortion. [E1]

## What Changed
An increasing share of Chinese men faced a "marriage squeeze" — a shortage of brides in the marriage market. In response, households with sons began saving more to improve their sons' relative attractiveness as marriage partners. The key asset is housing: homeownership has become a prerequisite for marriage in urban China, and families with sons compete to accumulate housing wealth to make their sons more marriageable. [E1]

## Implementation and Assignment
The variation operates at the intersection of household composition (having a son versus a daughter) and regional demographics (the local male-to-female ratio among marriageable young people). Households with sons in regions with more skewed sex ratios face stronger incentives for competitive savings. A key falsification test: sex ratios should not affect savings behavior of households without sons. [E1]

## Why This Creates Empirical Variation
If sex ratio imbalances are driven by historical son preference and policy — not by contemporaneous economic conditions — then the interaction of household son presence and regional sex ratio isolates the causal effect of marriage-market competition on savings. The paper estimates that the rising sex ratio explains about half of the increase in China's household savings rate. The competitive savings mechanism generates a negative externality: one household's additional savings raises the bar for other households, creating a positional arms race. [E1; analytical inference]

## Identification Risks
Regions with skewed sex ratios may differ in income levels, development, or cultural norms that also drive savings. The paper tests the key identifying assumption by examining savings behavior in households without sons — these households should not respond to sex ratio variation if the mechanism operates through marriage-market competition. Using provincial One-Child Policy variation (fine levels) as an instrument for sex ratios provides additional identification. [E1]

## Data Requirements
Household-level survey data with savings, income, consumption, demographic composition, and housing wealth (CHIP, UHS). Regional sex ratios from census data at prefecture or county level. Provincial One-Child Policy fine schedules for IV analysis. Provincial macroeconomic data for aggregate analysis. [E1]

## Evidence Notes
E1 provides compelling evidence that sex ratio imbalances are a major driver of China's high savings rate. The paper estimates that households with sons in high-sex-ratio regions save significantly more than comparable households with daughters, and that this mechanism can explain approximately 50% of the aggregate increase in China's household savings rate. The findings link demographic policies to macroeconomic outcomes through the novel channel of marriage-market competition.
