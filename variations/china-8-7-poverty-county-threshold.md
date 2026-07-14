---
schema_version: 2
id: china-8-7-poverty-county-threshold
name: National Poverty County Eligibility Threshold under China's 8-7 Poverty Reduction Plan (1994–2000)
aliases:
- China 8-7 Plan poverty county threshold
- 国家八七扶贫攻坚计划
- 国家级贫困县
- National Poor Counties
status: grounded
provenance:
  task_id: task-5df5750a87cc
scope:
  country: China
  regions:
  - Rural counties nationwide
  domains:
  - development
  - public-economics
  - fiscal-transfers
  - poverty
  - political-economy
  variation_type: eligibility-threshold
  knowledge_role: china-variation
  china_relevance: The 8-7 Poverty Reduction Plan was China's first national poverty program with explicit income thresholds for county eligibility. Counties with 1992 rural per capita net income below 400 yuan were designated as national poverty counties and received large-scale earmarked transfers and preferential policies. The sharp income cutoff creates a regression-discontinuity design that has been used to evaluate the causal effects of the program on rural income, fiscal capacity, and local development.
identity:
  instrument: Designation as a national poverty county under the State Council's 8-7 Poverty Reduction Plan.
  authority: State Council of China; State Council Leading Group for Poverty Alleviation and Development (国务院扶贫开发领导小组)
  legal_identifiers:
  - 国发[1994]30号《国务院关于印发国家八七扶贫攻坚计划的通知》（15 April 1994)
  - 《国家八七扶贫攻坚计划（1994-2000年）》
  implementation_regime: In 1994 the central government selected 592 national poverty counties based on 1992 rural per capita net income. These counties received earmarked fiscal transfers, subsidized loans, food-for-work programs, and other preferential policies from 1994 through 2000. Counties with 1992 income above 700 yuan that had been designated poor in 1986 exited the program.
  assignment_mechanism: Counties were assigned to treatment largely on the basis of whether their 1992 rural per capita net income fell below the 400-yuan threshold. Counties with income between 400 and 700 yuan were treated if previously designated, producing a fuzzy discontinuity at the upper cutoff. The primary identifying variation is the sharp threshold at 400 yuan.
  parent: null
  related_variations: []
timeline:
  announcement: '1994-04-15'
  effective: '1994-04-15'
  implementation_start: 1994
  implementation_end: 2000
  local_timing: National list announced in April 1994 and applied simultaneously to all counties. Transfers and projects began in 1994 and continued through 2000.
  anticipation: The plan was announced and implemented in 1994; pre-1994 income is the running variable, so anticipation before 1992 is unlikely to affect the threshold.
  last_verified: '2026-07-14'
assignment:
  unit: County
  treated: Counties designated as national poverty counties under the 8-7 Plan.
  comparison_pool: Counties just above and just below the 400-yuan 1992 rural per capita net income cutoff; counties just above and below the 700-yuan upper cutoff for previously designated counties.
  rule: A county is treated if its 1992 rural per capita net income is below 400 yuan. Previously designated poor counties with 1992 income above 700 yuan exited. Counties with income between 400 and 700 yuan were retained if previously designated, creating fuzzy assignment in that interval.
  intensity: Binary designation as a national poverty county; intensity of transfers varies with county size and project mix.
  exemptions:
  - Counties just below the threshold that were not included due to data errors or political considerations
  - Counties just above the threshold that were retained in the fuzzy interval
  compliance: Compliance with the income-based rule was high but not perfect. The 1994 list contains exactly 592 counties, and official documents report the 400/700-yuan rule.
  exposure_construction: Use 1992 rural per capita net income as the running variable and an indicator for national poverty county designation as the treatment variable. For sharp RD, focus on the 400-yuan cutoff. For fuzzy RD, model treatment probability as a function of the running variable around the cutoffs.
  required_identifiers:
  - county code
  - 1992 rural per capita net income
  - national poverty county indicator
  spillovers: Earmarked transfers may affect neighboring counties through labor markets, migration, or local price effects, but these are generally assumed small in the RD literature on this program.
research_compatibility:
  outcome_domains:
  - rural income growth
  - fiscal transfers and public spending
  - infrastructure investment
  - education and health outcomes
  - agricultural productivity
  - poverty headcount
  - local governance and state capacity
  affected_populations:
  - Rural residents in designated poverty counties
  - County governments
  - Poor households targeted by county programs
  mechanism_channels:
  - Earmarked fiscal transfers increase local public investment
  - Subsidized credit and food-for-work programs raise household income
  - Preferential policies attract external resources
  - County designation creates incentives for poverty-reduction reporting
  best_for:
  - Regression discontinuity designs around the 400-yuan threshold
  - Fuzzy regression discontinuity at the 700-yuan upper cutoff
  - Difference-in-differences comparing designated counties before and after 1994
  not_good_for:
  - Outcomes measured only after 2000, when the 8-7 Plan ended and new plans began
  - Settings where manipulation of 1992 income reporting is a major concern
  - Studies requiring individual-level treatment variation rather than county-level designation
design:
  claim_type: causal
  affordances:
  - Sharp income threshold at 400 yuan
  - Fuzzy upper threshold at 700 yuan
  - National policy with common treatment definition
  - Pre-program income available for RD running variable
  candidate_designs:
  - Sharp regression discontinuity at the 400-yuan cutoff
  - Fuzzy regression discontinuity at the 700-yuan cutoff
  - Difference-in-differences using 1994 as treatment onset
  identifying_variation: Discontinuity in treatment probability at the 400-yuan 1992 rural per capita net income threshold.
  primary_strategy: Regression discontinuity around the 400-yuan cutoff.
  estimand: The local average treatment effect of national poverty county designation on outcomes for counties near the 400-yuan threshold.
  treatment_variable: Indicator for being designated a national poverty county in 1994.
  comparison_logic: Counties with 1992 income just below 400 yuan are compared with counties with income just above 400 yuan. Under continuity, the only systematic difference near the cutoff is treatment status.
  estimation_notes: Estimate a local-linear or polynomial regression of the outcome on the running variable, allowing a discontinuity at 400 yuan. Use data-driven bandwidth selection (e.g., Imbens-Kalyanaraman, Calonico-Cattaneo-Titiunik) and report robustness across bandwidths and polynomial orders.
  assumptions:
  - Continuity of potential outcomes and covariates at the 400-yuan threshold
  - No precise manipulation of 1992 rural per capita net income around the cutoff
  - Treatment assignment is a deterministic or strongly increasing function of the running variable at the cutoff
  diagnostics:
  - McCrary density test for manipulation of the running variable
  - Balance tests on pre-determined covariates
  - Placebo cutoffs away from 400 and 700 yuan
  - Robustness to bandwidth and functional-form choices
  - Fuzzy-RD first-stage diagnostics at the 700-yuan cutoff
threats:
  - type: manipulation
    basis: inferred
    condition: Local officials may have misreported 1992 rural income to bring counties below the 400-yuan threshold or keep them above the 700-yuan exit threshold.
    evidence_refs:
    - E2
    - E3
    possible_diagnostics:
    - McCrary density test around the cutoffs
    - Examine bunching in the income distribution
  - type: heterogeneous_effects
    basis: inferred
    condition: The local effect at the 400-yuan cutoff may not generalize to counties far from the threshold.
    evidence_refs:
    - E1
    possible_diagnostics:
    - Report effects across bandwidths
    - Compare RD estimates with DD estimates over the full sample
  - type: concurrent_reforms
    basis: inferred
    condition: Other 1990s reforms such as fiscal decentralization, grain procurement changes, and regional development programs may coincide with the 8-7 Plan.
    evidence_refs: []
    possible_diagnostics:
    - Control for region-by-year fixed effects
    - Test for effects on placebo outcomes
  - type: spillovers
    basis: inferred
    condition: Transfers to designated counties may affect outcomes in adjacent non-designated counties.
    evidence_refs: []
    possible_diagnostics:
    - Estimate spatial RD or include neighbors' treatment status
    - Exclude border counties as a robustness check
  - type: measurement_error
    basis: inferred
    condition: 1992 income data are administrative and may be measured with error, weakening the first stage in fuzzy RD.
    evidence_refs:
    - E2
    possible_diagnostics:
    - Use alternative income measures if available
    - Report first-stage F-statistics in fuzzy RD
empirical_requirements:
  contract_version: 1
  population: Rural Chinese counties
  observation_unit: county-year
  geography_level: county
  time_start: 1985
  time_end: 2000
  minimum_frequency: annual
  minimum_pre_periods: 5
  minimum_post_periods: 5
  required_fields:
  - 1992 rural per capita net income
  - national poverty county indicator
  - outcome variables
  - pre-determined county characteristics
  - fiscal transfer data
  required_identifiers:
  - county code
  - year
  treatment_key:
  - county code
  treatment_source: Official list of 592 national poverty counties and 1992 county-level rural per capita net income from the State Council Leading Group for Poverty Alleviation and Development or published statistical materials.
  measurement_risks:
  - 1992 income may be misreported or revised
  - County boundaries may have changed between 1992 and 2000
  - Outcome data availability varies across counties
evidence:
  - id: E1
    source_type: paper
    citation: "Meng, Lingsheng (2013), \"Evaluating China's poverty alleviation program: A regression discontinuity approach,\" Journal of Public Economics, 101, 1-11."
    url: https://doi.org/10.1016/j.jpubeco.2013.02.004
    date: '2013'
    supports:
    - identity.instrument
    - design.primary_strategy
    - design_applications
    - assignment.rule
    verification_status: reported
    access_level: abstract
    locator: IDEAS/RePEc abstract and ScienceDirect abstract
  - id: E2
    source_type: policy-document
    citation: "国务院，《国务院关于印发国家八七扶贫攻坚计划的通知》，国发[1994]30号，1994年4月15日。"
    url: http://app.shandong.gov.cn/zhengbao/1994/1994-07.pdf
    date: '1994-04-15'
    supports:
    - identity.legal_identifiers
    - timeline.announcement
    - identity.implementation_regime
    verification_status: verified
    access_level: official-document
    locator: Full text in Shandong Provincial Government Gazette, 1994 No. 7
  - id: E3
    source_type: policy-document
    citation: "中国政府网，《中国的农村扶贫开发》，2005年5月26日。"
    url: https://www.gov.cn/govweb/ziliao/flfg/2005-05/26/content_1293.htm
    date: '2005-05-26'
    supports:
    - identity.implementation_regime
    - assignment.rule
    - timeline.implementation_start
    verification_status: verified
    access_level: official-document
    locator: White-paper section stating the 400/700-yuan rule and 592 counties
  - id: E4
    source_type: policy-document
    citation: "国务院扶贫开发领导小组办公室/中国政府网，《国家扶贫开发工作重点县和连片特困地区县的认定历史》，2013年3月1日。"
    url: https://www.gov.cn/gzdt/2013-03/01/content_2343058.htm
    date: '2013-03-01'
    supports:
    - identity.implementation_regime
    - assignment.rule
    - timeline.implementation_end
    verification_status: verified
    access_level: official-document
    locator: Official explanation of 1986, 1994, and 2001 poverty county adjustments
design_applications:
  - paper: Meng (2013)
    doi: 10.1016/j.jpubeco.2013.02.004
    journal: Journal of Public Economics
    year: 2013
    research_question: What was the causal effect of national poverty county designation under the 8-7 Plan on rural income growth?
    population: Rural Chinese counties near the 1992 income threshold
    outcome: Change in log rural net income per capita from 1994 to 2000
    data_used:
    - County-level panel from the Ministry of Agriculture (1981-1995)
    - 1992 rural per capita net income
    - National poverty county status
    treatment_encoding: Indicator for national poverty county designation based on the 400-yuan threshold
    comparison: Counties just above and below the 400-yuan cutoff; difference-in-differences between designated and non-designated counties
    empirical_design: Regression discontinuity and difference-in-differences
    assumptions:
    - Continuity at the 400-yuan threshold
    - No manipulation of 1992 income
    threats_addressed:
    - Checks for discontinuities in covariates
    - Robustness to bandwidth and functional form
    evidence_refs:
    - E1
    - E2
    - E3
method_transfer: null
readiness_blockers: []
superseded_by: null
deprecation_reason: null
---

## Institutional Background

By the early 1990s China's poverty reduction strategy had shifted from broad rural development to targeted support for poor counties. The State Council launched the 8-7 Poverty Reduction Plan in April 1994 with the goal of lifting 80 million rural poor out of poverty within seven years [E2, verified fact]. The plan targeted 592 national poverty counties selected on the basis of 1992 rural per capita net income.

## What Changed

The 8-7 Plan created a formal income-based eligibility rule: counties with 1992 rural per capita net income below 400 yuan were included in the national poverty county list, while previously designated poor counties with income above 700 yuan exited [E3, verified fact]. Designated counties received large fiscal transfers, subsidized loans, food-for-work programs, and other preferential policies through 2000.

## Implementation and Assignment

Treatment assignment was determined primarily by a single pre-program income variable, making the 400-yuan cutoff the central assignment mechanism. The rule was implemented uniformly across the country in 1994. Counties between 400 and 700 yuan retained designation if previously poor, creating a fuzzy upper boundary [E3, verified fact].

## Why This Creates Empirical Variation

The deterministic income threshold produces a sharp regression discontinuity. Counties just below 400 yuan are otherwise similar to counties just above 400 yuan, except for program eligibility. This allows credible estimation of the local effect of national poverty county designation on rural development outcomes [E1, reported claim].

## Identification Risks

The main risks are manipulation of 1992 income reporting, heterogeneous treatment effects far from the cutoff, concurrent regional policies, spillovers to adjacent counties, and measurement error in historical income data. The paper addresses some of these through standard RD diagnostics, but researchers should verify them in each application [analytical inference].

## Data Requirements

A usable study needs county-level 1992 rural per capita net income, the 1994 national poverty county indicator, outcome data for the 1980s and 1990s, and predetermined covariates. The official county list and income data have been used in the published literature and are available from Chinese statistical yearbooks and academic replication files [E1, reported claim].

## Evidence Notes

The full text of the State Council notice is available through a provincial government gazette reproduction [E2]. The precise 400/700-yuan rule and the 592-county list are documented in official government white papers and the State Council poverty alleviation office's historical account [E3, E4]. The empirical application is drawn from Meng (2013) in the Journal of Public Economics [E1].
