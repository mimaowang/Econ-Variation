---
schema_version: 2
id: china-land-reform-sex-selection
name: China's Household Responsibility System Land Reform as a Driver of Rural Sex Ratio Imbalance (1978–1986)
aliases:
- Household Responsibility System sex selection
- HRS land reform sex ratio
- 家庭联产承包责任制 性别选择

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - 914 rural counties
  domains:
  - agriculture
  - demography
  - gender
  - household
  - development
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: Staggered county-level implementation of the Household Responsibility System (HRS) land reform (1978–1984),
    which shifted agricultural production from collectives to individual households and increased the economic value of male
    labor
  authority: Chinese central government, progressively authorized and implemented at the county level
  legal_identifiers:
  - Household Responsibility System reform documents
  - county-level implementation records
  implementation_regime: Counties adopted HRS at different times between 1978 and 1984; the reform assigned land use rights
    to individual households, making family labor — and especially male labor for heavy agricultural work — more economically
    valuable
  assignment_mechanism: County-level adoption timing was driven by administrative authorization and local political conditions
    rather than pre-existing sex ratio trends
  parent: null
  related_variations: []
timeline:
  announcement: '1978-12-01'
  effective: null
  implementation_start: 1978
  implementation_end: 1984
  local_timing: Counties adopted HRS on a staggered schedule; newly collected data on 914 counties provides precise timing
  anticipation: Reform direction was discussed nationally; some counties may have anticipated implementation
  last_verified: '2026-07-13'
assignment:
  unit: County and household
  treated: Rural households in counties after their HRS adoption date
  comparison_pool: Counties that had not yet adopted HRS; pre-reform period in treated counties
  rule: County-level HRS adoption, coded from archival county gazetteers and government documents
  intensity: Binary — county is treated after HRS adoption; the reform increased the returns to male agricultural labor
  exemptions: []
  compliance: Adoption was near-universal once authorized; the reform was top-down with limited opt-out
  exposure_construction: Code each county-year as pre- or post-HRS adoption; link to household-level birth records to analyze
    sex ratios by birth parity
  required_identifiers:
  - county code
  - year
  - HRS adoption date
  - child sex
  - birth order
  - sibling sex composition
  spillovers: Land reform effects may interact with One Child Policy implementation, which was also rolling out during the
    same period
research_compatibility:
  outcome_domains:
  - sex ratio at birth
  - son preference
  - fertility
  - household labor allocation
  - agricultural productivity
  affected_populations:
  - rural households
  - second and higher-parity births
  - families with firstborn daughters
  mechanism_channels:
  - increased returns to male agricultural labor
  - land reallocation
  - household production decisions
  - son preference in fertility
  best_for:
  - Studying how economic reforms affect gender-biased fertility decisions
  - county-level staggered rollout designs
  not_good_for:
  - Urban populations
  - outcomes unrelated to fertility or household labor allocation
design:
  affordances:
  - staggered county-level adoption
  - newly collected county HRS timing data
  - linked birth records with sibling composition
  - pre/post comparison within county
  candidate_designs:
  - staggered difference-in-differences
  - event study around HRS adoption
  identifying_variation: County-specific HRS adoption timing, comparing births within the same county before vs after reform,
    with particular focus on second births following a firstborn girl
  assumptions:
  - County adoption timing is unrelated to pre-existing sex ratio trends
  - adjacent counties serve as valid controls during staggered rollout
  diagnostics:
  - Test for pre-trends in sex ratios before HRS adoption
  - control for county-level One Child Policy timing
  - analyze by birth parity and sibling sex composition
  primary_strategy: Staggered difference-in-differences with county fixed effects; event study around HRS adoption
  estimand: The causal effect of the recorded exposure on Sex ratio at birth (male/female), particularly for second births
    following firstborn girls, conditional on the stated design assumptions.
  treatment_variable: Post-HRS indicator at the county-year level; interaction with sibling sex composition
  comparison_logic: Within-county pre/post HRS comparison; across-county comparison by adoption timing
  estimation_notes: Staggered difference-in-differences with county fixed effects; event study around HRS adoption
threats:
- type: contemporaneous-one-child-policy
  basis: documented
  condition: The One Child Policy was implemented concurrently; the sex ratio effect attributed to HRS could partly reflect
    fertility restrictions interacting with son preference
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for county-level OCP implementation timing
  - compare HRS effects in counties with different OCP enforcement intensity
  - analyze within-sibling comparisons that are less affected by fertility policy
- type: endogenous-adoption
  basis: inferred
  condition: Earlier-adopting counties may have had different economic or demographic characteristics that independently affected
    sex ratios
  evidence_refs:
  - E1
  possible_diagnostics:
  - test whether pre-HRS sex ratio trends predict adoption timing
  - use only plausibly exogenous variation in adoption timing
empirical_requirements:
  contract_version: 1
  population: Rural births in 914 Chinese counties, 1978–1986
  observation_unit: Individual birth record (county-year-sibling composition cell)
  geography_level: County
  time_start: 1978
  time_end: 1986
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields:
  - county code
  - birth year
  - child sex
  - birth order
  - sex of older siblings
  - HRS adoption date
  required_identifiers:
  - county code
  - year
  - HRS adoption status
  treatment_key:
  - county code
  - year
  - post-HRS indicator
  treatment_source: County gazetteers and government archives for HRS timing; county-level birth records
  measurement_risks:
  - underreporting of female births
  - county boundary changes
  - HRS adoption date measurement error
evidence:
- id: E1
  source_type: paper
  citation: 'Almond, Douglas, Hongbin Li, and Shuang Zhang. 2019. "Land Reform and Sex Selection in China." Journal of Political
    Economy 127 (2): 560–585.'
  url: https://doi.org/10.1086/701030
  date: 2019
  supports:
  - identity
  - assignment
  - design
  - HRS timing data
  - main estimates
  - OCP interaction analysis
  verification_status: verified
design_applications:
- paper: Land Reform and Sex Selection in China
  doi: 10.1086/701030
  journal: Journal of Political Economy
  year: 2019
  research_question: Did the shift from collective to household farming (HRS) increase sex-selective childbearing in rural
    China?
  population: Rural births in 914 Chinese counties, 1978–1986
  outcome: Sex ratio at birth (male/female), particularly for second births following firstborn girls
  data_used: []
  treatment_encoding: Post-HRS indicator at the county-year level; interaction with sibling sex composition
  comparison: Within-county pre/post HRS comparison; across-county comparison by adoption timing
  empirical_design: Staggered difference-in-differences with county fixed effects; event study around HRS adoption
  assumptions:
  - HRS timing exogenous to sex ratio trends
  - OCP effects separable from HRS effects
  - birth records accurately capture sex and parity
  threats_addressed:
  - OCP concurrency via county-level OCP timing controls
  - selection via pre-trend tests
  - sibling composition via parity-specific analysis
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
---
## Institutional Background
China's rural land reform between 1978 and 1984 abolished collective farming under the Household Responsibility System (HRS). Each household received use rights to a plot of land in proportion to family size. Production decisions and residual claims shifted from the collective to the household. This made family labor — especially male labor for physically demanding farm work — more valuable at the margin. [E1]

## What Changed
After HRS adoption in their county, rural households faced stronger economic incentives to have sons. The reform created approximately 1 million "missing girls" between 1978 and 1986 — roughly half of the total increase in rural sex ratios. Among second births following a firstborn girl, the sex ratio rose from 1.1 to 1.3 boys per girl in the four years post-reform. [E1]

## Implementation and Assignment
HRS was not implemented on a single national date. Different counties adopted the reform at different times between 1978 and 1984, based on administrative authorization from provincial and central authorities. This staggered rollout creates county-level variation in exposure timing that can be exploited for identification. [E1]

## Why This Creates Empirical Variation
The staggered county-level adoption of HRS provides within-county pre/post variation and across-county variation in treatment timing. By comparing births before and after HRS adoption in the same county, and by focusing on second births (where sex selection is most detectable), the design identifies the causal effect of the land reform on gender-biased fertility. [E1]

## Identification Risks
The One Child Policy was being implemented during the same period and also affected fertility decisions. The paper addresses this by controlling for county-level OCP rollout timing. A subtler concern is that HRS adoption timing may have been endogenous to county economic and demographic conditions. [E1; analytical inference]

## Data Requirements
County-level HRS adoption dates (newly collected from archival sources), county-level birth records with child sex and parity, and county-level controls for OCP implementation timing. [E1]

## Evidence Notes
E1 is the published JPE article. The key contribution is documenting a previously unrecognized mechanism — agricultural reform — as a driver of China's elevated sex ratios, independent of and additive to the One Child Policy effect.
