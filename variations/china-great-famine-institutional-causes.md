---
schema_version: 2
id: china-great-famine-institutional-causes
name: Cross-Regional Variation in Institutional Radicalism During China's Great Leap Forward as a Determinant of Famine Mortality
  (1959–1961)
aliases:
- Meng Qian Yared Great Famine China
- 大饥荒 制度因素
- Great Leap Forward institutional variation
- Chinese famine political economy

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - All provinces and prefectures affected by the Great Famine
  domains:
  - political-economy
  - development
  - health
  - institutions
  - history
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: Cross-regional variation in the radicalism of agricultural collectivization and grain procurement policies during
    China's Great Leap Forward (1958–1961), driven by differences in provincial and local leaders' responsiveness to central
    Party directives for rapid collectivization and excessive grain procurement, which created differential famine severity
    across regions
  authority: Chinese Communist Party Central Committee (Great Leap Forward policies, grain procurement targets)
  legal_identifiers:
  - Great Leap Forward campaign (1958)
  - People's Commune movement
  - grain procurement and distribution policies
  - Party directives on agricultural radicalism
  implementation_regime: The Great Leap Forward was launched nationally in 1958, but the intensity of radical policies (speed
    of collectivization, size of communes, grain procurement quotas, suppression of private plots) varied substantially across
    regions depending on local leaders' political incentives and career concerns
  assignment_mechanism: Regional variation in policy radicalism was driven by local Party leaders' career concerns (promotion
    incentives tied to demonstrating revolutionary zeal) interacting with historical grain production norms; regions where
    leaders set unrealistically high procurement targets experienced more severe famine
  parent: null
  related_variations:
  - china-send-down-movement-altruism
  - china-land-reform-sex-selection
timeline:
  announcement: '1958-05-01'
  effective: null
  implementation_start: 1958
  implementation_end: 1961
  local_timing: The Great Leap Forward and associated famine occurred during 1958–1961; the famine peaked in 1959–1960
  anticipation: The Great Leap Forward was announced in 1958; the severity of resulting famine was not anticipated by policymakers
    or citizens
  last_verified: '2026-07-13'
assignment:
  unit: Prefecture, county, and individual birth cohort
  treated: Regions (prefectures/counties) where local leaders implemented more radical collectivization and grain procurement
    policies; individuals born in these regions during the famine years experienced severe nutritional deprivation in utero
    and early childhood
  comparison_pool: Regions with less radical policy implementation; pre-famine and post-famine birth cohorts within the same
    region
  rule: The interaction of region (exposed to more or less radical policies) and birth cohort (in utero during famine vs before/after)
    identifies the causal effect of famine exposure on long-run outcomes
  intensity: Continuous — regional excess mortality rate during 1959–1961; grain procurement rate as a share of production;
    speed and completeness of collectivization
  compliance: Policy implementation was mandatory; the key variation is in the intensity of implementation, not in whether
    policies were implemented
  exemptions: []
  exposure_construction: Construct region-level famine severity measures from historical demographic data (excess mortality,
    fertility decline); interact region-level famine severity with individual birth cohort indicators to estimate long-run
    effects of in utero and early childhood famine exposure
  required_identifiers:
  - prefecture/county code
  - birth year
  - famine severity measure
  - grain procurement rate
  spillovers: Inter-regional grain transfers may have exacerbated famine in surplus regions; post-famine migration may attenuate
    long-run estimates
research_compatibility:
  outcome_domains:
  - mortality
  - health
  - human capital
  - economic outcomes
  - political trust
  - institutional change
  affected_populations:
  - Famine survivors (in utero and early childhood cohorts)
  - rural agricultural households
  - all residents of severely affected regions
  mechanism_channels:
  - excess mortality from starvation
  - in utero nutritional deprivation
  - long-run health and cognitive effects
  - changes in political attitudes and trust
  - institutional reforms following the famine
  best_for:
  - Studying the long-run effects of early-life health shocks
  - understanding how political institutions and career incentives affect policy implementation and human welfare
  not_good_for:
  - Estimating the effects of democratic institutions (China was authoritarian)
  - comparing with non-socialist famines
  - studying urban populations
design:
  affordances:
  - large regional variation in famine severity
  - sharp temporal boundaries (1959–1961)
  - rich historical demographic data
  - pre/post famine cohort comparisons
  - within-region and cross-region variation
  candidate_designs:
  - difference-in-differences (region × birth cohort)
  - instrumental variables using pre-determined grain production norms
  - regression discontinuity in birth cohorts around famine onset/end
  identifying_variation: Regional variation in famine severity (driven by differences in local policy implementation) interacted
    with birth cohort (in utero during famine vs before/after) identifies the causal effect of famine exposure
  assumptions:
  - Regional famine severity is conditionally exogenous to long-run outcome trends (driven by political factors
  - not pre-existing regional characteristics)
  - no selective mortality that differentially affects observed long-run outcomes
  - no differential post-famine migration or fertility responses
  diagnostics:
  - Test for pre-famine outcome differences across high vs low famine severity regions
  - compare in-utero vs early childhood vs post-famine cohorts
  - test for differential mortality selection
  - examine whether effects vary with alternative famine severity measures
  primary_strategy: Difference-in-differences (region × cohort); analysis of institutional determinants of famine severity
    (grain procurement, collectivization radicalism); long-run follow-up of affected cohorts
  estimand: The causal effect of the recorded exposure on Excess mortality during 1959–1961, long-run health and economic
    outcomes of famine-exposed cohorts, conditional on the stated design assumptions.
  treatment_variable: Region-level famine severity (excess mortality rate) interacted with birth cohort indicators (in utero
    during famine)
  comparison_logic: High famine severity vs low famine severity regions; in-utero famine cohort vs pre-famine and post-famine
    cohorts
  estimation_notes: Difference-in-differences (region × cohort); analysis of institutional determinants of famine severity
    (grain procurement, collectivization radicalism); long-run follow-up of affected cohorts
threats:
- type: selective-mortality
  basis: documented
  condition: Famine mortality was selective — weaker individuals died, potentially making survivors appear healthier than
    they would have been absent the famine (survivor bias attenuating estimated effects)
  evidence_refs:
  - E1
  possible_diagnostics:
  - compare in-utero exposure (where selective mortality affects mothers) vs early childhood exposure
  - use bounding approaches
  - compare with non-famine regions to estimate mortality selection
- type: post-famine-migration
  basis: inferred
  condition: Post-famine migration from severely affected to less affected regions may confound regional comparisons
  evidence_refs:
  - E1
  possible_diagnostics:
  - use prefecture-of-birth not current residence
  - track individuals across locations
  - test for systematic migration patterns by famine severity
empirical_requirements:
  contract_version: 1
  population: Chinese birth cohorts from approximately 1950–1970, with particularly affected cohorts born 1959–1961
  observation_unit: Individual (cohort-region)
  geography_level: Prefecture or county
  time_start: 1950
  time_end: 1970
  minimum_frequency: cross-section or repeated cross-section
  minimum_pre_periods: 5
  minimum_post_periods: 10
  required_fields:
  - birth year
  - prefecture/county of birth
  - famine severity measure
  - demographic characteristics
  - long-run outcomes (health
  - education
  - income
  - political attitudes)
  required_identifiers:
  - prefecture/county code
  - birth year
  treatment_key:
  - prefecture/county code
  - famine severity measure
  - in-utero famine exposure indicator
  - early childhood famine exposure indicator
  treatment_source: Historical demographic data (1982 census, 1990 census for reconstructing famine mortality), Chinese administrative
    records on grain procurement, county gazetteers, survey data for long-run outcomes
  measurement_risks:
  - famine mortality data quality at subnational level
  - cohort identification in survey data
  - recall of birth location for migrants
  - confounding of age and cohort effects in cross-sectional data
evidence:
- id: E1
  source_type: paper
  citation: 'Meng, Xin, Nancy Qian, and Pierre Yared. 2015. "The Institutional Causes of China''s Great Famine, 1959–1961."
    Review of Economic Studies 82 (4): 1568–1611.'
  url: https://doi.org/10.1093/restud/rdv016
  date: 2015
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - institutional analysis
  - famine severity analysis
  verification_status: verified
design_applications:
- paper: The Institutional Causes of China's Great Famine, 1959–1961
  doi: 10.1093/restud/rdv016
  journal: Review of Economic Studies
  year: 2015
  research_question: What institutional and political factors caused the cross-regional variation in famine severity during
    China's Great Leap Forward famine?
  population: Chinese prefectures and birth cohorts, 1950s–1960s
  outcome: Excess mortality during 1959–1961, long-run health and economic outcomes of famine-exposed cohorts
  data_used:
  - 1982 and 1990 China Population Census
  - County and prefecture gazetteers
  - Historical grain procurement records
  - Household survey data (CHNS, CHIP)
  treatment_encoding: Region-level famine severity (excess mortality rate) interacted with birth cohort indicators (in utero
    during famine)
  comparison: High famine severity vs low famine severity regions; in-utero famine cohort vs pre-famine and post-famine cohorts
  empirical_design: Difference-in-differences (region × cohort); analysis of institutional determinants of famine severity
    (grain procurement, collectivization radicalism); long-run follow-up of affected cohorts
  assumptions:
  - regional policy radicalism exogenous to pre-existing mortality trends
  - no selective mortality bias
  - birth cohort accurately measured
  threats_addressed:
  - selective mortality via multiple cohort comparisons
  - institutional endogeneity via historical instruments
  - measurement error via multiple data sources
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
method_transfer: null
---
## Institutional Background
The Great Leap Forward (1958–1961) was one of the deadliest famines in human history, with an estimated 15–30 million excess deaths. The famine was not caused by natural disaster — it was a man-made catastrophe driven by radical agricultural policies: forced collectivization into large People's Communes, confiscation of private plots, and excessive state grain procurement that left insufficient food for rural households. Crucially, famine severity varied dramatically across regions, from minor food shortages to catastrophic mortality rates. [E1]

## What Changed
In 1958, Mao Zedong launched the Great Leap Forward, aiming to rapidly industrialize China and catch up with the West. Agriculture was collectivized into massive People's Communes, private farming was abolished, and grain procurement quotas were set based on wildly exaggerated production estimates. The combination of disrupted agricultural production and excessive procurement drained rural food supplies. The policy persisted and even intensified through 1959–1960 despite mounting evidence of starvation. [E1]

## Implementation and Assignment
The key identifying variation is cross-regional differences in the radicalism of policy implementation. Some provincial and local leaders — driven by career incentives in the Party hierarchy — implemented far more aggressive procurement and collectivization than others. Regions with higher grain procurement rates (as a share of actual production) and faster, more complete collectivization experienced more severe famine. [E1]

## Why This Creates Empirical Variation
The cross-regional variation in policy radicalism creates a natural experiment: comparing cohorts born just before, during, and after the famine in regions with different famine severity identifies the causal effect of nutritional deprivation on long-run outcomes. Because the radicalism of implementation was driven by local leader career concerns rather than pre-existing regional characteristics, the variation is plausibly exogenous. [E1; analytical inference]

## Identification Risks
The primary threat is that regions with more radical policies may have differed systematically from other regions on dimensions that independently affect long-run outcomes. Selective mortality (weaker individuals dying) can bias estimates of long-run effects toward zero. Post-famine migration can attenuate regional comparisons if survivors moved away from severely affected areas. [E1; analytical inference]

## Data Requirements
Historical census data (1982, 1990) to reconstruct prefecture-level famine mortality by cohort, administrative records on grain procurement rates and collectivization, county and prefecture gazetteers for policy implementation measures, and contemporary household survey data with birth location, year, and long-run outcomes. [E1]

## Evidence Notes
E1 provides the most comprehensive analysis of the institutional causes of China's Great Famine. The paper demonstrates that cross-regional variation in famine severity was primarily driven by differences in the radicalism of grain procurement and collectivization policies, and that these differences were in turn driven by local leaders' career incentives in the Party hierarchy. The findings provide causal evidence linking political institutions to one of the largest humanitarian disasters in modern history.
