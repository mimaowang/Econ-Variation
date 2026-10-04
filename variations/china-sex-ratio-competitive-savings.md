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
  task_id: task-dce32e3730d6
scope:
  country: China
  regions:
  - Mainland China
  - 122 rural counties and 70 cities in the 2002 CHIP survey
  - provinces in the separate 1980-2007 aggregate analysis
  domains:
  - household-finance
  - gender
  - marriage
  - savings
  - macroeconomics
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: This paper links mainland Chinese census cohorts to Chinese households and provinces to study the domestic marriage-market and savings relationship.
identity:
  instrument: Local male-to-female ratio of the premarital cohort, measured from earlier Chinese population censuses and linked to later household or province-level savings outcomes.
  authority: No authority assigns this exposure; it is a measured demographic condition. Provincial family-planning penalties and minority exemption shares enter the paper's separate instrumental-variable exercise.
  legal_identifiers: []
  implementation_regime: The paper studies sex-ratio imbalance arising across Chinese cohorts and places, with fertility restrictions, son preference and prenatal sex selection discussed as possible drivers. It does not identify a single policy adoption date or treat the one-child policy itself as the exposure.
  assignment_mechanism: Children and families encounter sex ratios of their local marriage-market cohort. Those ratios are not randomly assigned, and local fertility norms, migration, policy implementation or economic change may jointly affect sex ratios and savings.
  parent: null
  related_variations:
  - china-missing-women-tea-price
  - china-land-reform-sex-selection
  - china-one-child-policy-twins-iv
timeline:
  announcement: null
  effective: null
  implementation_start: null
  implementation_end: null
  local_timing: The 2002 household analysis advances the 1990 census age-0-to-9 cohort to ages 12-21; the distinct 1980-2007 province panel infers age-7-to-21 sex ratios from the 2000 census.
  anticipation: Households with sons anticipate future marriage market competition; savings behavior adjusts well before the
    son reaches marriage age
  last_verified: '2026-10-03'
assignment:
  unit: Local premarital-age cohort linked to a 2002 household; separately, province-year in the aggregate analysis.
  treated: Higher male-to-female premarital-cohort ratios, especially among one-child households with a son in the paper's household comparison.
  comparison_pool: One-child son households across different local ratios and analogous daughter households; the province panel compares within-province changes conditional on year effects.
  rule: The paper's marriage-market hypothesis predicts stronger competitive saving among son families where potential brides are scarcer. This is a behavioral response, not statutory treatment eligibility.
  intensity: Continuous census-derived sex ratio; the pooled rural household specification interacts it with a son indicator.
  compliance: No compliance concept for a demographic exposure; households may respond differently or not at all.
  exemptions: []
  exposure_construction: Link the 2002 CHIP household location to the 1990 census local sex ratio for ages 0-9 (ages 12-21 in 2002); county for rural households and city for urban households. Keep rural and urban specifications separate. The pooled rural specification interacts the ratio with a son indicator; no household fixed effects are possible in this one-year household sample.
  required_identifiers:
  - CHIP household identifier and 2002 survey location
  - rural county or urban city census geography
  - son indicator
  - household demographic composition
  spillovers: Competitive saving and housing-market responses may affect other families in the same marriage market; daughter-family responses need not be a zero-effect placebo.
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
  claim_type: reduced-form
  affordances:
  - Census-based local premarital-cohort ratios predate the 2002 household outcome.
  - CHIP identifies one-child son and daughter families in rural and urban locations.
  - A separate province-year panel examines aggregate savings over 1980-2007.
  candidate_designs:
  - Cross-sectional local-ratio gradient estimated separately for son and daughter households.
  - Pooled rural son-indicator-by-local-ratio interaction.
  - Province and year fixed-effects panel, with a distinct and assumption-sensitive IV exercise.
  identifying_variation: Differences in local census cohort ratios among 2002 one-child families, and within-province changes in inferred premarital-cohort ratios in the aggregate panel; neither source is inherently exogenous.
  assumptions:
  - Conditional comparisons must separate marriage-market competition from local culture, fertility behavior, migration and economic conditions that also affect saving.
  - For the IV interpretation, earlier family-planning fines and exemptions must affect later savings only through the measured cohort sex ratio; the paper does not establish this by institutional assignment alone.
  diagnostics:
  - Compare son and daughter household gradients without equating a nonsignificant daughter coefficient with proof of zero spillovers.
  - Audit local income, household composition, migration and cultural confounders.
  - For the province panel, examine instrument exclusion and alternative direct channels from family-planning policy to saving.
  primary_strategy: The paper's 2002 household analysis uses rural and urban local-ratio regressions; rural Tables 5-7 report son/daughter splits and a pooled interaction. Its separate 1980-2007 province panel has province/year fixed effects and instruments inferred sex ratios with lagged family-planning penalties and exemption share.
  estimand: Association of local premarital-cohort sex ratio with the paper's savings measures, differentiated by household child sex; IV causal interpretation requires additional exclusion assumptions.
  treatment_variable: 1990-census local age-0-to-9 male/female ratio linked to 2002 CHIP; for the aggregate panel, inferred province-year age-7-to-21 ratio from the 2000 census.
  comparison_logic: Son versus daughter one-child households along a local-ratio gradient in the 2002 cross-section; separate within-province time variation for aggregate savings, not a household before/after design.
  estimation_notes: Rural Table 5 estimates son and daughter subsamples; Table 7 pools them with a son-by-ratio interaction. Table 16 is the separate province-year 2SLS analysis. Neither the household comparison nor the aggregate panel warrants calling the local sex ratio randomly assigned.
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
  - compare son and daughter gradients
  - inspect alternative direct effects of family-planning enforcement
- type: measurement-error
  basis: inferred
  condition: Local sex ratios may be measured with error (census undercount, migration, age misreporting), attenuating estimates
  evidence_refs:
  - E1
  possible_diagnostics:
  - use multiple data sources for sex ratios
  - examine sensitivity of the province-level IV to policy-related direct saving channels
  - report specification robustness
empirical_requirements:
  contract_version: 1
  population: 2002 CHIP rural and urban one-child households for the household application; a separate 1980-2007 province-year aggregate application.
  observation_unit: household in 2002; province-year for the aggregate analysis
  geography_level: rural county or urban city for CHIP; province for aggregate analysis
  time_start: 2002
  time_end: 2002
  minimum_frequency: cross-section
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields:
  - household savings
  - income
  - consumption
  - household composition including child sex and age
  - marriage status and family type
  - 1990 census local cohort ratio
  - rural county or urban city code
  required_identifiers:
  - household ID
  - 2002 survey year
  - rural county or urban city location
  treatment_key:
  - son presence indicator
  - local sex ratio for the 1990 age-0-to-9 cohort
  - son-times-sex-ratio interaction
  treatment_source: 1990 population census age-sex counts linked to the 2002 Chinese Household Income Project; the separate provincial panel infers sex ratios from the 2000 census.
  measurement_risks:
  - savings measurement error in survey data
  - sex ratio mismeasurement due to internal migration
  - census-to-survey geography matching and local migration
  - comparability of household and provincial savings measures
evidence:
- id: E1
  source_type: paper
  citation: 'Wei, Shang-Jin, and Xiaobo Zhang. 2011. "The Competitive Saving Motive: Evidence from Rising Sex Ratios and Savings
    Rates in China." Journal of Political Economy 119 (3): 511–564.'
  url: https://doi.org/10.1086/660887
  date: 2011
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - assignment.exposure_construction
  - design.primary_strategy
  - design.estimation_notes
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - design_applications.data_used
  verification_status: verified
  access_level: metadata
  locator: 'Journal DOI and publication identity; full-text claims were checked in E4, accessed 2026-10-03.'
- id: E2
  source_type: official-data
  citation: National Bureau of Statistics of China. Communiqué on Major Figures of the 2000 Population Census (No. 1).
  url: https://www.stats.gov.cn/english/NewsEvents/200204/t20020423_25982.html
  date: 2001
  supports: [scope.regions, identity.implementation_regime]
  verification_status: verified
  access_level: official-document
  locator: 'Mainland census coverage, cohort and sex composition sections; this national communiqué confirms the census frame but does not independently reproduce the paper’s county or city premarital-cohort ratios; accessed 2026-10-03.'
- id: E3
  source_type: archive
  citation: Chinese Household Income Project, 2002, ICPSR 21741, version 1.
  url: https://www.icpsr.umich.edu/web/DSDR/studies/21741
  date: 2009
  supports: [empirical_requirements.population, empirical_requirements.treatment_source, design_applications.data_used]
  verification_status: verified
  access_level: metadata
  locator: 'Study description and citation; confirms the 2002 rural and urban household survey exists, not the paper-specific sample construction or field-by-field access; accessed 2026-10-03.'
- id: E4
  source_type: paper
  citation: Wei and Zhang. 2011. Author-hosted published JPE article PDF, with later affiliation erratum.
  url: https://business.columbia.edu/sites/default/files-efs/pubfiles/3534/Wei_Competitive_Saving_Motive.pdf
  date: 2011
  supports: [identity.instrument, identity.assignment_mechanism, assignment.exposure_construction, design.primary_strategy, design.estimation_notes, empirical_requirements.population, empirical_requirements.observation_unit, design_applications.data_used]
  verification_status: verified
  access_level: full-text
  locator: 'Article pp. 528-531 household sample and census linkage; Tables 5-7 pp. 532-537 rural household specifications; pp. 550-559 and Tables 14-16 separate province-year/IV exercise; Appendix pp. 562-563 data definitions; accessed 2026-10-03.'
design_applications:
- paper: 'The Competitive Saving Motive: Evidence from Rising Sex Ratios and Savings Rates in China'
  doi: 10.1086/660887
  journal: Journal of Political Economy
  year: 2011
  research_question: Does competition in the marriage market caused by sex ratio imbalances explain the rise in China's household
    savings rate?
  population: 2002 CHIP one-child households in 122 rural counties and 70 cities; separately, Chinese province-years during 1980-2007.
  outcome: Household log(income/consumption) in the CHIP tables; a separately constructed provincial savings-rate series in the aggregate panel.
  data_used:
  - 2002 Chinese Household Income Project rural and urban surveys (ICPSR 21741)
  - 1990 Chinese population census local age-sex cohorts for 2002 household exposure
  - 2000 Chinese population census cohorts for the separate province-year series
  - Provincial statistical yearbooks for aggregate income and consumption
  - Provincial family-planning penalty and minority-exemption measures for the IV exercise
  treatment_encoding: County (rural) or city (urban) 1990 census age-0-to-9 male/female ratio, interpreted as ages 12-21 in 2002; the pooled rural table interacts it with a one-child son indicator.
  comparison: Son and daughter one-child families across local-ratio gradients in the 2002 household cross-section; distinct within-province aggregate analysis with year effects.
  empirical_design: Household cross-sectional regressions, including rural separate and pooled son/daughter specifications; distinct province-year fixed-effects and 2SLS analyses.
  assumptions:
  - The conditional local sex-ratio gradient is not driven by omitted local determinants of savings or selective migration.
  - Interpreting the son contrast as marriage-market competition requires considering other consequences of child sex and local demography.
  - Province-level IV estimates require family-planning measures to lack direct effects on savings apart from cohort sex ratio.
  threats_addressed:
  - The paper conditions on household and local covariates and examines alternative samples; no household fixed effects in the 2002 cross-section.
  - Provincial fixed effects and earlier policy penalties address some concerns but do not prove exclusion of direct fertility-policy effects.
  - Census-derived exposure can differ from the effective marriage market because of migration or reporting error.
  evidence_refs:
  - E1
  - E3
  - E4
readiness_blockers:
- The independently inspected official census communiqué confirms the national frame, not the 1990 county/city age-sex counts or the paper's exact linked local exposure; the record should not imply those ratios were independently reconstructed.
- The paper documents multiple useful associations, but endogenous local demography and possible direct effects of family-planning instruments preclude presenting this as a clean exogenous shock without a design-specific audit.
method_transfer: null
---
## Institutional Background
This is not a policy rollout or an assigned shock. It is a measured difference in the number of young men relative to young women across Chinese marriage markets. Wei and Zhang ask whether the resulting competition is associated with greater saving by families with sons. Their account connects the demographic imbalance to family-planning restrictions, son preference and sex selection, but the empirical treatment is the cohort sex ratio, not the adoption of the one-child policy. The official 2000 census communiqué establishes the mainland census frame; it does not supply the exact local ratios constructed by the authors. [E1; E2]

## What Changed
For the household exercise, the authors use the 2002 Chinese Household Income Project, covering 122 rural counties and 70 cities. They advance the 0–9 cohort from the 1990 census to ages 12–21 in 2002, measuring exposure at rural county or urban city level. The comparable rural Table 5 sample is a one-child, three-person nuclear family with both parents alive and mother younger than 40. Household saving is operationalized as log(income/consumption), not a household panel savings rate. Rural Tables 5–7 compare son and daughter families across the local ratio; Table 7 includes a son-by-ratio interaction. The study also reports urban results, which should not be silently pooled with rural county exposure. [E1; E3]

## Implementation and Assignment
The local ratio predates the 2002 survey outcome and the son/daughter contrast is informative about the proposed marriage-market mechanism. In the rural estimates, the ratio is positively associated with saving for son families while the daughter-family estimate is not statistically distinguishable from zero. This is not proof that daughter families or prices are unaffected, nor that local ratios are random. The household design is cross-sectional: it has no household fixed effects or before/after household treatment comparison. Regional income, culture, fertility preferences, migration and other demography can confound the gradient. [E1]

## Why This Creates Empirical Variation
The paper additionally constructs a 1980–2007 province-year panel, inferring the 7–21 cohort ratio from the 2000 census, and estimates province and year fixed-effects specifications. Its IV exercise uses family-planning financial penalties and the share exempt from birth quotas, lagged about 14 years. These are *instruments proposed by the paper*, not proof of exogenous assignment: family-planning enforcement could influence fertility, household composition and saving through channels other than the measured sex ratio. Table 16 reports positive 2SLS coefficients, and the paper's claim that the ratio explains a large share of China's aggregate savings rise is an estimate under this identifying and aggregation model, not a census fact. The article's text and appendix do not describe the provincial savings transformation identically, so a replication should verify the underlying series rather than merge it into the CHIP outcome. [E1]

## Identification Risks
The local ratio is not assigned randomly. Regional income, culture, fertility preferences, migration and other demography may jointly shape the census ratio and savings. The son/daughter comparison is a mechanism contrast, not an automatic placebo, and the family-planning instruments can directly alter saving through fertility and household composition. The study's province-level fixed effects and statistical overidentification tests cannot alone close those channels. [E4]

## Data Requirements
For a new study, first choose whether the estimand is a family-level relative saving response or an aggregate provincial response. Obtain the matching CHIP household geography, census age-sex counts and income/expenditure fields for the first; obtain province-year income/consumption and actual historical family-planning measures only if reproducing the second. Treat sex-ratio measurement, migration, local selection and the IV exclusion restriction as active design issues. The value of this record is the documented exposure and comparison logic, not a promise that any sex-ratio regression is causal. [E1; E3]

## Evidence Notes
The 2002 survey and the two census vintages are different inputs for different analyses. The official communiqué and ICPSR catalog confirm the existence and broad frame of those inputs, while the full paper is the source for the actual sample restrictions, exposure construction and estimates. Exact local cohort ratios have not been independently reconstructed here, so this corrected record remains at the extracted layer rather than being promoted as a verified exogenous design. [E2; E3; E4]
