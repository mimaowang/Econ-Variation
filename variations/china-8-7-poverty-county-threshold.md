---
schema_version: 2
id: china-8-7-poverty-county-threshold
name: National Poverty County Eligibility Threshold under China's 8-7 Poverty Reduction Plan (1994–2000)
aliases:
- China 8-7 Plan poverty county threshold
- 国家八七扶贫攻坚计划
- 国家级贫困县
- National Poor Counties
status: design-documented
provenance:
  task_id: task-c843b1804831
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
  china_relevance: The 8-7 Poverty Reduction Plan used 1992 rural per-capita-net-income rules to revise national poverty-county eligibility. Counties below 400 yuan entered, while previously designated counties above 700 yuan exited; legacy designation in the intervening range means the income rule creates a fuzzy, not mechanically sharp, regression-discontinuity opportunity. Designation bundled earmarked transfers, subsidized loans, food-for-work, and preferential policies from 1994 through 2000.
identity:
  instrument: Designation as a national poverty county under the State Council's 8-7 Poverty Reduction Plan.
  authority: State Council of China; State Council Leading Group for Poverty Alleviation and Development (国务院扶贫开发领导小组)
  legal_identifiers:
  - 国发[1994]30号《国务院关于印发国家八七扶贫攻坚计划的通知》（15 April 1994)
  - 《国家八七扶贫攻坚计划（1994-2000年）》
  implementation_regime: In 1994 the central government selected 592 national poverty counties based on 1992 rural per capita net income. These counties received earmarked fiscal transfers, subsidized loans, food-for-work programs, and other preferential policies from 1994 through 2000. Counties with 1992 income above 700 yuan that had been designated poor in 1986 exited the program.
  assignment_mechanism: '[E3, verified] Counties below 400 yuan in 1992 entered the national key-support list, while previously designated counties above 700 yuan exited. Legacy poverty-county status therefore modifies treatment in the 400–700 yuan interval. [E5, reported claim] The published design treats the resulting change in designation probability as fuzzy RD rather than assuming that 1992 income deterministically assigns treatment.'
  parent: null
  related_variations: []
timeline:
  announcement: '1994-04-15'
  effective: '1994-04-15'
  implementation_start: 1994
  implementation_end: 2000
  local_timing: National list announced in April 1994 and applied simultaneously to all counties. Transfers and projects began in 1994 and continued through 2000.
  anticipation: '[E3, verified] The running variable predates the 1994 plan, so post-announcement behavior cannot change its recorded 1992 value. That timing does not itself rule out measurement error, prior designation politics, or strategic classification in the historical income/status data.'
  last_verified: '2026-10-04'
assignment:
  unit: County
  treated: Counties designated as national poverty counties under the 8-7 Plan.
  comparison_pool: '[E5, reported claim] Counties near the 400-yuan 1992 rural-income entry cutoff, with treatment inferred from the discontinuous probability of national-poverty-county designation rather than a clean treated-versus-untreated split. Previously designated counties in the 400–700 yuan interval require separate treatment-status coding.'
  rule: '[E3, verified] A county below 400 yuan in 1992 was included; a previously designated county above 700 yuan exited. The 400–700 yuan interval depends on legacy designation, so a reproducible analysis must merge the 1986/1993 status and the 1994 list rather than impute treatment from income alone.'
  intensity: Binary designation as a national poverty county; intensity of transfers varies with county size and project mix.
  exemptions:
  - Counties just below the threshold that were not included due to data errors or political considerations
  - Counties just above the threshold that were retained in the fuzzy interval
  compliance: '[E3, verified] The 1994 list contains 592 counties and the official account states the 400/700-yuan rules. [E5, reported claim] Actual designation is nonetheless not fully determined by income alone, so the relevant empirical issue is treatment-rule fidelity and first-stage strength, not individual compliance with a binary rule.'
  exposure_construction: '[E5, reported claim] Use 1992 rural per capita net income as the running variable, the400-yuan eligibility-side indicator as the instrument, and actual1994 national poverty county designation as the endogenous treatment. Estimate the local designation first stage rather than replacing actual status with eligibility. Prior designation matters; the700-yuan legacy exit rule is not a second interchangeable cutoff for this application.'
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
  - Local designation effects at400 yuan with a verified first stage and historical status
  - Difference-in-differences comparing designated counties before and after 1994
  not_good_for:
  - Attributing outcomes after2000 solely to the8-7 Plan without separating successor programs
  - Settings where manipulation of 1992 income reporting is a major concern
  - Studies requiring individual-level treatment variation rather than county-level designation
design:
  claim_type: causal
  affordances:
  - Fuzzy treatment-probability discontinuity at the 400-yuan entry rule
  - Legacy-status and 700-yuan exit rule that can be separately encoded
  - National policy with common treatment definition
  - Pre-program income available for RD running variable
  candidate_designs:
  - Fuzzy regression discontinuity at the 400-yuan entry cutoff
  - Difference-in-differences using 1994 as treatment onset
  identifying_variation: '[E5, reported claim] A discontinuity in the probability of national-poverty-county designation at the 400-yuan 1992 rural per-capita-net-income entry rule, with legacy designation preventing deterministic assignment.'
  primary_strategy: '[E1, reported claim; E5, reported claim] Fuzzy regression discontinuity around the 400-yuan entry cutoff, using the income-side indicator as an instrument for actual national-poverty-county designation.'
  estimand: '[E5, reported claim] A local average treatment effect of national-poverty-county designation for counties whose designation changes with eligibility at the 400-yuan entry rule.'
  treatment_variable: Indicator for being designated a national poverty county in 1994.
  comparison_logic: '[E5, reported claim] Counties just below and above 400 yuan are compared locally, but their designation status is not perfectly determined by income; the first-stage discontinuity in actual designation is part of the estimand, not a nuisance to be ignored.'
  estimation_notes: '[E5, reported claim] Estimate the local first stage from the 400-yuan eligibility-side indicator to actual designation and use a fuzzy-RD/IV specification for outcomes. Bandwidth, functional-form, density, covariate-continuity, and first-stage checks remain decision-critical.'
  assumptions:
  - Continuity of potential outcomes and covariates at the 400-yuan threshold
  - No precise manipulation of 1992 rural per capita net income around the cutoff
  - Eligibility changes the probability of actual designation sufficiently at the cutoff for a locally interpretable fuzzy-RD first stage
  diagnostics:
  - McCrary density test for manipulation of the running variable
  - Balance tests on pre-determined covariates
  - Placebo cutoffs away from 400 and 700 yuan
  - Robustness to bandwidth and functional-form choices
  - Fuzzy-RD first-stage diagnostics at the 400-yuan entry cutoff
threats:
  - type: manipulation
    basis: inferred
    condition: '[Analytical inference] Misreported historical income or status could affect entry below400 yuan or retention below the700-yuan exit threshold. This is a potential threat, not verified evidence that counties changed the1992 values after the1994 announcement.'
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
  population: Rural Chinese counties near the400-yuan entry cutoff with actual1994 and prior designation status
  observation_unit: county-year
  geography_level: county
  time_start: 1994
  time_end: 2000
  minimum_frequency: annual
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields:
  - 1992 rural per capita net income
  - national poverty county indicator
  - prior national poverty county status
  - outcome variables
  - pre-determined county characteristics
  required_identifiers:
  - county code
  - year
  treatment_key:
  - county code
  treatment_source: '[E3, verified; E5, reported claim] Merge the official 1994 list of 592 national poverty counties, 1992 county rural per-capita-net-income running variable, and prior national-poverty-county status. Income alone is not a valid substitute for the actual designation indicator.'
  measurement_risks:
  - 1992 income may be misreported or revised
  - County boundaries may have changed between 1992 and 2000
  - Outcome data availability varies across counties
  - The default contract is for designation-based fuzzy RD, not a universal five-before/five-after DID panel. Historical assignment and pre-treatment covariates still need inspection; outcome periods depend on the question.
  - Transfer amounts are needed for transfer-channel or amount-specific analyses, not every designation effect. A published use of historical data does not establish a currently accessible replication package.
evidence:
  - id: E1
    source_type: paper
    citation: "Meng, Lingsheng (2013), \"Evaluating China's poverty alleviation program: A regression discontinuity approach,\" Journal of Public Economics, 101, 1-11."
    url: https://doi.org/10.1016/j.jpubeco.2013.02.004
    date: '2013'
    supports:
    - identity.instrument
    - assignment.rule
    - design.primary_strategy
    - design_applications.paper
    - design_applications.doi
    - design_applications.journal
    - design_applications.year
    - design_applications.research_question
    - design_applications.population
    - design_applications.outcome
    verification_status: reported
    access_level: abstract
    locator: 'Abstract plus publisher section previews inspected: empirical-strategy preview reports1994-to2000 log rural-income change; data preview describes1946 counties in a1981–1995 Ministry of Agriculture panel. Full Meng text, construction of the2000 endpoint and replication files were not inspected; detailed fuzzy-RD reasoning is attributed to E5, not inferred from the abstract.'
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
  - id: E5
    source_type: paper
    citation: 'Lü, Xiaobo. 2015. "Intergovernmental transfers and local education provision — Evaluating China''s 8-7 National Plan for Poverty Reduction." China Economic Review 33: 200–211.'
    url: https://doi.org/10.1016/j.chieco.2015.02.001
    date: '2015'
    supports:
    - identity.assignment_mechanism
    - assignment.comparison_pool
    - assignment.rule
    - design.identifying_variation
    - design.primary_strategy
    - design.estimand
    - design.comparison_logic
    - design.estimation_notes
    - design.assumptions
    - design.diagnostics
    - empirical_requirements.treatment_source
    - assignment.exposure_construction
    - empirical_requirements.population
    - empirical_requirements.time_start
    - empirical_requirements.time_end
    - empirical_requirements.minimum_pre_periods
    - empirical_requirements.minimum_post_periods
    - empirical_requirements.required_fields
    - empirical_requirements.measurement_risks
    verification_status: reported
    access_level: full-text
    locator: 'Author-hosted published PDF re-inspected4October2026: https://www.xiaobolu.com/_files/ugd/265480_8331f98fb95544a58dbe2701f917f997.pdf ; printedpp201–202 explain legacy retention below700; pp203–205 Sections3.1–3.2 describe1994–2000 outcomes, pre-treatment1990/1993 covariates and previous designation, unavailable program-specific education transfers, actual designation instrumented at400, rejection of700 for this application, and fuzzy rather than sharp RD. This supports no universal five-year pre-outcome panel requirement, not permission to omit historical assignment or diagnostics.'
design_applications:
  - paper: Meng (2013)
    doi: 10.1016/j.jpubeco.2013.02.004
    journal: Journal of Public Economics
    year: 2013
    research_question: '[E1, reported claim] What was the effect of national poverty county designation under the8-7 Plan on rural income growth?'
    population: Rural Chinese counties near the 1992 income threshold
    outcome: '[E1, reported claim] Change in log rural net income per capita from1994 to2000, as shown in the publisher empirical-strategy preview.'
    data_used:
    - '[E1, reported claim] Publisher data preview describes a Ministry of Agriculture panel of1946 counties from1981–1995; construction of the2000 endpoint was not inspected.'
    - 1992 rural per capita net income
    - National poverty county status
    treatment_encoding: '[E5, reported claim about Meng] Actual national poverty county designation, instrumented by eligibility around400 yuan; do not equate the designation indicator with the threshold-side indicator.'
    comparison: '[E5, reported claim about Meng] Local counties around400 yuan with a discontinuity in actual designation probability. The publisher preview begins with a DD framework, not evidence that simple designated-versus-other DD identifies the final causal estimate.'
    empirical_design: '[E1, reported claim; E5, reported claim about Meng] RD for income growth; E5 explicitly attributes the same fuzzy-RD approach to Meng. The full original implementation has not been independently inspected here.'
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
    - E5
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

The national rule uses1992 income and previous designation together: legacy counties in the400–700 interval can retain status [E3, verified fact]. Income alone is therefore not actual treatment. [E5, reported claim] The inspected application estimates a fuzzy first stage at400 and excludes700 because political selection there is a concern; neither nationwide rules nor a named cutoff imply mechanically sharp assignment.

## Why This Creates Empirical Variation

The documented income rules create an eligibility discontinuity, but not a mechanically sharp treatment boundary. [E5, reported claim] Actual designation is not fully determined by 1992 income because legacy poverty-county status matters; the usable contrast is therefore fuzzy RD around the 400-yuan entry rule, with an eligibility-side indicator providing a first stage for actual designation. Whether this contrast is credible still depends on local continuity, no sorting/manipulation, and a meaningful first stage.

## Identification Risks

The main risks are manipulation of 1992 income reporting, heterogeneous treatment effects far from the cutoff, concurrent regional policies, spillovers to adjacent counties, and measurement error in historical income data. The paper addresses some of these through standard RD diagnostics, but researchers should verify them in each application [analytical inference].

## Data Requirements

A designation-based fuzzy RD needs the1992 running variable, actual1994 designation, previous status, outcomes around the cutoff, county identifiers and pre-treatment characteristics for continuity checks. Its default contract does not impose five pre- and five post-outcome years. [E5, reported claim] The inspected application uses1994–2000 outcomes with historical covariates; a single post-program outcome can support an RD comparison across counties, whereas income growth needs its stated endpoints and a DID requires its own pre/post outcomes and assumptions [analytical inference]. The zero period minima remove a spurious universal panel requirement, not the need for observed outcomes, historical assignment or diagnostics.

Fiscal-transfer amounts are additional inputs when studying amounts or channels, not mandatory for every designation effect. [E5, reported claim] Program-specific education transfers were unavailable in the described sources; an aggregate specific-purpose transfer proxy is not the same variable. Published data descriptions establish prior use, not current download access. No author replication package or the original income paper's2000-endpoint construction was inspected. Preserve these access and application limits when proposing an implementation.

## Evidence Notes

The prior official-document inspections establish the national notice and400/700 rules [E2–E4]; those pages were not newly certified in this audit. Meng's abstract and publisher previews support the income application only to their stated access boundary [E1]. Lü's inspected author-hosted full text supports the fuzzy designation first stage and clarifies both the historical-data requirements and what was unavailable [E5]. A new outcome still needs its own continuity, sample and measurement assessment; the entry rule does not certify every application.
