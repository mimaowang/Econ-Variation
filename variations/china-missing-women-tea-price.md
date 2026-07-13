---
schema_version: 2
id: china-missing-women-tea-price
name: Differential Sex-Specific Agricultural Income Shocks from Tea Cultivation and the Survival of Girls in Reform-Era China
aliases:
- Missing women tea price China
- Qian sex ratio agricultural prices
- 茶叶价格 失踪女性
- Nunn Qian related tea

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - Tea-growing and orchard-growing counties across China
  domains:
  - development
  - gender
  - agriculture
  - health
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: 'Post-Mao agricultural reform (household responsibility system) combined with cross-county variation in the
    suitability of land for tea cultivation versus orchard crops, creating differential sex-specific income shocks: tea cultivation
    uses female labor (women have comparative advantage in tea picking), while orchard cultivation uses male labor'
  authority: Chinese government (agricultural reform) and agro-climatic conditions (crop suitability)
  legal_identifiers:
  - Household Responsibility System reforms
  - agricultural price liberalization
  - post-Mao rural reforms
  implementation_regime: The nationwide agricultural reforms of 1978–1982 gave households control over crop choice and residual
    income; counties with different agro-climatic suitability for tea (female-labor-intensive) versus orchards (male-labor-intensive)
    experienced differential increases in the relative economic value of women's versus men's labor
  assignment_mechanism: The interaction of national agricultural reform timing with county-level crop suitability (determined
    by climate, elevation, and soil conditions set centuries ago) creates variation in the relative income shock to female
    versus male labor
  parent: null
  related_variations:
  - china-land-reform-sex-selection
timeline:
  announcement: null
  effective: null
  implementation_start: 1978
  implementation_end: 1982
  local_timing: Agricultural reforms were rolled out nationally between 1978 and 1982; crop suitability is time-invariant
  anticipation: Agricultural reforms were not anticipated by individual households; crop suitability is geographically predetermined
  last_verified: '2026-07-13'
assignment:
  unit: County
  treated: Counties with high tea-growing suitability after agricultural reform (female income shock); counties with high
    orchard suitability after reform (male income shock — comparison/contrast)
  comparison_pool: Pre-reform period within each county; cross-county comparison across different crop-suitability gradients
  rule: Tea suitability increases relative female income; orchard suitability increases relative male income; the reform allows
    these latent comparative advantages to be expressed through household crop choices and market prices
  intensity: Continuous — county-level tea suitability index and orchard suitability index
  compliance: Households adopted tea or orchard cultivation where agro-climatically suitable and economically profitable;
    compliance with "assignment" (crop suitability) was driven by market incentives under the reform
  exemptions: []
  exposure_construction: Interact post-reform indicator (after 1982) with county-level tea suitability (and separately orchard
    suitability); the double difference (tea-post × sex) identifies the effect of female-specific income on girl survival
  required_identifiers:
  - county code
  - year
  - tea suitability index
  - orchard suitability index
  spillovers: Agricultural price changes may have general equilibrium effects on county-level wages and marriage markets
research_compatibility:
  outcome_domains:
  - sex ratio
  - girl survival
  - education
  - health
  - household income
  - intra-household allocation
  affected_populations:
  - Girls
  - women
  - tea-growing households
  - rural households in reform-era China
  mechanism_channels:
  - relative female labor income
  - intra-household bargaining
  - son preference
  - sex-specific human capital investment
  best_for:
  - Studying how changes in women's relative economic value affect son preference and sex ratios
  - understanding the economic determinants of missing women
  not_good_for:
  - Urban populations
  - post-2000 outcomes
  - causal identification of other agricultural reforms
design:
  affordances:
  - national reform timing
  - cross-county crop suitability variation
  - sex-specific labor intensity of crops
  - pre/post reform comparison
  candidate_designs:
  - difference-in-differences interacting post-reform with crop suitability
  - triple-difference (post × suitability × child sex)
  identifying_variation: The interaction of national agricultural reform with county-level agro-climatic suitability for tea
    (female-labor intensive) versus orchards (male-labor intensive); this creates differential shocks to the relative economic
    value of women that are driven by geography and biology, not local gender attitudes
  assumptions:
  - Crop suitability is exogenous to pre-reform sex ratios
  - the agricultural reform affected sex ratios only through the crop-income channel
  - no other county-level changes correlate with both crop suitability and sex-ratio trends
  diagnostics:
  - Test for pre-reform relationship between crop suitability and sex ratios
  - compare tea-suitable vs orchard-suitable counties before and after reform
  - examine whether effects vary with world tea prices
  primary_strategy: Difference-in-differences and triple-differences; the key estimate compares the change in female survival
    in tea-suitable counties after reform to the change in orchard-suitable counties after reform
  estimand: The causal effect of the recorded exposure on Sex ratios at birth, survival rates for girls relative to boys,
    educational attainment, conditional on the stated design assumptions.
  treatment_variable: Post-reform indicator interacted with county tea suitability; post-reform interacted with county orchard
    suitability; triple-difference with child sex
  comparison_logic: Tea-suitable vs orchard-suitable counties; pre-reform vs post-reform; female vs male children
  estimation_notes: Difference-in-differences and triple-differences; the key estimate compares the change in female survival
    in tea-suitable counties after reform to the change in orchard-suitable counties after reform
threats:
- type: omitted-variable-bias
  basis: inferred
  condition: Tea-suitable and orchard-suitable counties may differ on other dimensions (geography, development level, culture)
    that independently affect sex ratios
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for county characteristics
  - test for pre-existing differences in sex ratios
  - use only within-county variation over time
  - compare effects of tea versus orchard suitability within the same county
- type: measurement-error
  basis: inferred
  condition: Tea and orchard suitability indices based on agro-climatic data may contain measurement error
  evidence_refs:
  - E1
  possible_diagnostics:
  - use multiple agro-climatic data sources
  - report sensitivity to alternative crop suitability measures
  - test for attenuation bias
empirical_requirements:
  contract_version: 1
  population: Chinese counties with varying crop suitability, 1960s–1990s
  observation_unit: County-year or individual-level census/survey data
  geography_level: County
  time_start: 1962
  time_end: 1990
  minimum_frequency: annual or census-period
  minimum_pre_periods: 5
  minimum_post_periods: 10
  required_fields:
  - county code
  - year
  - tea suitability
  - orchard suitability
  - sex ratio at birth
  - child survival by sex
  - agricultural production data
  required_identifiers:
  - county code
  - year
  - crop suitability indices
  treatment_key:
  - county code
  - post-reform indicator
  - tea suitability × post-reform
  - orchard suitability × post-reform
  treatment_source: FAO agro-climatic suitability data for tea and orchards; Chinese census and survey data for sex ratios;
    agricultural production data from statistical yearbooks
  measurement_risks:
  - under-reporting of female births
  - census coverage varying over time
  - crop suitability measurement accuracy at county level
  - migration between counties
evidence:
- id: E1
  source_type: paper
  citation: 'Qian, Nancy. 2008. "Missing Women and the Price of Tea in China: The Effect of Sex-Specific Earnings on Sex Imbalance."
    Quarterly Journal of Economics 123 (3): 1251–1285.'
  url: https://doi.org/10.1162/qjec.2008.123.3.1251
  date: 2008
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - mechanism analysis
  - sex ratio analysis
  verification_status: verified
design_applications:
- paper: 'Missing Women and the Price of Tea in China: The Effect of Sex-Specific Earnings on Sex Imbalance'
  doi: 10.1162/qjec.2008.123.3.1251
  journal: Quarterly Journal of Economics
  year: 2008
  research_question: Does increasing women's relative economic earnings reduce son preference and improve survival rates for
    girls?
  population: Rural Chinese counties with tea and orchard cultivation, 1962–1990
  outcome: Sex ratios at birth, survival rates for girls relative to boys, educational attainment
  data_used: []
  treatment_encoding: Post-reform indicator interacted with county tea suitability; post-reform interacted with county orchard
    suitability; triple-difference with child sex
  comparison: Tea-suitable vs orchard-suitable counties; pre-reform vs post-reform; female vs male children
  empirical_design: Difference-in-differences and triple-differences; the key estimate compares the change in female survival
    in tea-suitable counties after reform to the change in orchard-suitable counties after reform
  assumptions:
  - crop suitability exogenous to pre-existing sex-ratio preferences
  - reform timing exogenous
  - relative price of tea vs other crops drives differential female income
  threats_addressed:
  - omitted variables via county fixed effects and crop-type comparison
  - cultural confounds via within-county variation
  - migration via county-level analysis
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
---
## Institutional Background
Under Mao-era collectivization, individual Chinese households had little control over agricultural production decisions, and the link between local comparative advantage and household income was severed. The household responsibility system (HRS), rolled out between 1978 and 1982, restored household control over crop choice and allowed households to retain residual income from agricultural production. This reform allowed latent comparative advantages — including sex-specific ones — to shape household economic outcomes. [E1]

## What Changed
With the HRS reform, households in tea-suitable regions could plant tea and earn income from it, while those in orchard-suitable regions could plant orchards. Tea production is uniquely female-labor-intensive: the delicate work of picking tea leaves is performed primarily by women. Orchards, by contrast, primarily use male labor. The reform therefore generated a differential increase in the relative economic value of women in tea-growing regions compared to orchard-growing regions. [E1]

## Implementation and Assignment
The interaction of a national reform (HRS rollout) with geographically predetermined crop suitability creates the identifying variation. Counties with high tea suitability experienced a positive shock to the relative economic value of women's labor after the reform. Tea suitability is determined by agro-climatic conditions that are exogenous to local gender attitudes.[E1]

## Why This Creates Empirical Variation
The interaction of a national-level reform (the HRS) with geographically determined crop suitability creates a natural experiment. The key comparison is between tea-suitable counties (where female income rose after reform) and orchard-suitable counties (where male income rose). If son preference responds to women's relative economic contribution, the sex ratio should improve more in tea-suitable counties. The paper finds that it does: increasing female income by about 7% increases the fraction of surviving girls by about 1 percentage point. [E1; analytical inference]

## Identification Risks
Tea-growing and orchard-growing regions may differ on cultural, geographic, or economic dimensions that independently affect sex ratios. The paper addresses this by using within-county variation over time and by comparing the two types of agricultural suitability — if unobserved factors are common to both types of crop regions, the differential effect isolates the sex-specific earnings channel. World tea price fluctuations provide an additional source of temporal variation. [E1]

## Data Requirements
County-level data on agricultural production (tea acreage, orchard acreage) from Chinese statistical yearbooks, agro-climatic crop suitability indices from FAO, sex ratios and child survival from Chinese census data (1982, 1990) and population surveys, and control variables for county economic and demographic characteristics. [E1]

## Evidence Notes
E1 is a seminal paper linking economic incentives to son preference. It shows that increases in female-specific income (from tea) significantly reduce the proportion of missing girls, while increases in male-specific income (from orchards) have the opposite effect. The results are economically meaningful: tea-growing counties experienced substantially smaller increases in sex-ratio imbalance during the reform period compared to non-tea-growing counties.
