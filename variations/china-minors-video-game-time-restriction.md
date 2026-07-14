---
schema_version: 2
id: china-minors-video-game-time-restriction
name: China's Minors Online Video Game Time Restriction (2021)
aliases:
- China minors gaming ban
- 830新规
- 未成年人网络游戏防沉迷新规
- Online game anti-addiction policy
status: grounded
provenance:
  task_id: task-28aa8a1c5579
scope:
  country: China
  regions:
  - Nationwide
  - Online game service providers
  domains:
  - digital-regulation
  - education
  - health
  - child-development
  - media-policy
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: The policy is the strictest national regulation of minors' online gaming to date, limiting all under-18 users to three hours of online video-game play per week. Because the restriction applies nationwide at a known date and is enforced through real-name registration, it creates a sharp age- and cohort-based treatment that can be used to study time use, education, mental health, digital platform compliance, and family responses.
identity:
  instrument: A nationwide restriction on the hours during which online video-game service providers may offer services to users under 18 years of age.
  authority: National Press and Publication Administration (NPPA, 国家新闻出版署)
  legal_identifiers:
  - 国新出发〔2021〕14号《关于进一步严格管理 切实防止未成年人沉迷网络游戏的通知》（NPPA, 30 August 2021, effective 1 September 2021)
  implementation_regime: All online game companies operating in China must comply immediately from the effective date. Compliance is enforced through mandatory real-name registration and connection to the NPPA online-game anti-addiction real-name verification system. Providers may offer minors access only on Fridays, Saturdays, Sundays, and statutory holidays from 20:00 to 21:00 (one hour per day).
  assignment_mechanism: "Treatment is assigned by age at the national effective date: all registered users below age 18 are restricted, while users aged 18 and above are unaffected. The age threshold generates a regression-kink or cohort comparison, and the before-after date generates a difference-in-differences contrast."
  parent: null
  related_variations: []
timeline:
  announcement: '2021-08-30'
  effective: '2021-09-01'
  implementation_start: 2021
  implementation_end: null
  local_timing: Nationwide simultaneous implementation; enforcement tightened through the NPPA real-name verification system from September 2021 onward.
  anticipation: The policy was announced on 30 August 2021 and took effect on 1 September 2021, leaving minimal anticipation window. An earlier 2019 NPPA notice had introduced less restrictive time limits, so households and firms were already familiar with anti-addiction rules.
  last_verified: '2026-07-14'
assignment:
  unit: Individual user-month or individual user-week; alternatively cohort-year
  treated: Registered online-game users under 18 years of age from 1 September 2021 onward.
  comparison_pool: Registered users aged 18 or older; users who turned 18 before the policy; cohorts just above the age threshold; pre-reform observations for the same age group.
  rule: A user is treated if her real-name registered age is below 18 and the observation date is on or after 1 September 2021. The treatment intensity is the binding weekly cap on permitted gaming hours (three hours per week, all on weekends/holidays).
  intensity: Binary by eligibility (minor vs. adult), with dosage determined by the sharp reduction in permitted hours from the 2019 regime to the 2021 regime.
  exemptions:
  - Users who successfully bypass real-name registration (e.g., using adult family members' accounts)
  - Offline or non-network games not covered by the regulation
  - Users who stop playing online games entirely for reasons unrelated to the policy
  compliance: Compliance is substantial but incomplete. Survey evidence shows a sharp drop in minors' gaming engagement and overall internet use, while administrative and media reports document widespread use of adult accounts to evade restrictions.
  exposure_construction: Code a binary indicator equal to 1 for users under 18 observed on or after 1 September 2021. For cohort designs, code treatment based on birth cohort relative to the cutoff. For difference-in-differences, use age-in-years interacted with post-reform indicator.
  required_identifiers:
  - user age or birth date
  - observation date
  - registered account age
  - user identifier
  spillovers: The restriction may push minors toward short-video platforms, social media, offline games, or shared adult accounts. Within households, siblings or parents may adjust their own screen time or account-sharing behavior.
research_compatibility:
  outcome_domains:
  - time use and leisure
  - academic performance
  - mental health and well-being
  - physical health
  - digital platform engagement
  - household regulation of screen time
  affected_populations:
  - Chinese minors who play online video games
  - Online game service providers
  - Parents and households with adolescents
  mechanism_channels:
  - Direct time constraint reduces gaming hours
  - Substitution toward other online or offline activities
  - Parental monitoring and account-sharing responses
  - Platform compliance and enforcement investment
  best_for:
  - Difference-in-differences comparing minors before and after the policy
  - Regression kink or cohort designs around the age-18 threshold
  - Studies of digital regulation and adolescent behavior
  not_good_for:
  - Outcomes that are unaffected by online gaming time
  - Settings where account-sharing or substitution confounds the treatment effect of interest
  - Long-run outcomes that require many years of post-policy data
design:
  claim_type: causal
  affordances:
  - Sharp national implementation date
  - Clear age-based eligibility rule
  - Existing real-name registration infrastructure
  - Available survey and administrative data
  candidate_designs:
  - Difference-in-differences with minors as treated and adults or pre-policy minors as controls
  - Regression kink at age 18 around the policy date
  - Cohort event-study exploiting birth-month or birth-year variation
  identifying_variation: Variation comes from the interaction of being below age 18 and being observed after 1 September 2021, plus the discrete age threshold at 18.
  primary_strategy: Difference-in-differences and regression kink around the age cutoff.
  estimand: The average effect of being subject to the 2021 restriction on minors' time use, academic, and health outcomes, relative to not being subject to the restriction.
  treatment_variable: Binary indicator for being a registered minor user after 1 September 2021; continuous variable for permitted weekly gaming hours by age.
  comparison_logic: Minors after the policy are compared with minors before the policy and with adults who were never subject to the restriction. The age-18 threshold provides a within-post-period contrast.
  estimation_notes: For DID, include individual and time fixed effects and cluster standard errors at the individual or cohort level. For RKD, use age in months or days relative to the 18-year cutoff after the policy, controlling for baseline age trends.
  assumptions:
  - Parallel trends for treated and control groups in the absence of the policy
  - No discontinuous changes at age 18 other than the gaming restriction
  - Real-name registration accurately assigns treatment by age
  diagnostics:
  - Pre-trend tests using pre-reform periods
  - Placebo tests using older age groups or earlier years
  - Robustness to alternative age thresholds (e.g., 16 vs. 18)
  - Checks for substitution into other online platforms
threats:
  - type: noncompliance
    basis: reported
    condition: Minors may use adult family members' accounts or purchase/rent adult accounts to evade the restriction, weakening the first stage.
    evidence_refs:
    - E1
    - E2
    possible_diagnostics:
    - Measure compliance through self-reported gaming time
    - Compare outcomes by intensity of household monitoring
  - type: substitution
    basis: inferred
    condition: Reduced gaming time may be offset by increased use of short-video apps, social media, or offline entertainment, making net effects on study time or well-being ambiguous.
    evidence_refs:
    - E1
    possible_diagnostics:
    - Include other screen-time categories as outcomes
    - Test for effects on total internet use
  - type: measurement_error
    basis: inferred
    condition: Age and account registration data may be misreported; survey respondents may under-report gaming due to social desirability.
    evidence_refs:
    - E1
    possible_diagnostics:
    - Validate with administrative platform data where available
    - Use objective time-use diaries
  - type: anticipation
    basis: inferred
    condition: The 2019 anti-addiction notice and media discussion may have led some households to adjust behavior before the 2021 restriction.
    evidence_refs:
    - E2
    possible_diagnostics:
    - Include monthly leads in event-study specification
    - Compare post-policy changes with pre-policy trends
  - type: concurrent_reforms
    basis: inferred
    condition: Other education, tutoring, or public-health policies around 2021 may affect adolescent time use and well-being.
    evidence_refs: []
    possible_diagnostics:
    - Control for tutoring regulation timing
    - Use outcomes that are specific to gaming platforms
empirical_requirements:
  contract_version: 1
  population: Chinese minors who play online video games and a comparison group of adult or pre-policy users
  observation_unit: individual-month or individual-week
  geography_level: national or city
  time_start: 2020
  time_end: 2023
  minimum_frequency: monthly
  minimum_pre_periods: 6
  minimum_post_periods: 6
  required_fields:
  - user age or birth date
  - observation date
  - gaming time or engagement
  - outcome of interest
  - covariates (gender, city, household characteristics)
  required_identifiers:
  - user id
  - date
  treatment_key:
  - user age
  - date
  treatment_source: NPPA notice 国新出发〔2021〕14号 and real-name registration records from online game platforms.
  measurement_risks:
  - Account-sharing biases age assignment
  - Self-reported gaming time may be inaccurate
  - Platform-level data may not be representative of all games
evidence:
  - id: E1
    source_type: paper
    citation: "Wang, Zhejian (2026), \"Restricting video games in China: Effects on time use, educational achievement, and health,\" Journal of Development Economics, 182, 103812."
    url: https://doi.org/10.1016/j.jdeveco.2026.103812
    date: '2026'
    supports:
    - identity.instrument
    - design_applications
    - assignment.unit
    - threats
    verification_status: reported
    access_level: abstract
    locator: IDEAS/RePEc abstract
  - id: E2
    source_type: policy-document
    citation: "国家新闻出版署，《关于进一步严格管理 切实防止未成年人沉迷网络游戏的通知》，国新出发〔2021〕14号，2021年8月30日。"
    url: http://www.gov.cn/zhengce/zhengceku/2021-09/01/content_5634661.htm
    date: '2021-08-30'
    supports:
    - identity.legal_identifiers
    - timeline.announcement
    - timeline.effective
    - identity.implementation_regime
    - assignment.rule
    - assignment.exposure_construction
    verification_status: verified
    access_level: official-document
    locator: Full text on gov.cn policy archive
  - id: E3
    source_type: policy-document
    citation: "新华社/中国政府网，国家新闻出版署下发《关于进一步严格管理 切实防止未成年人沉迷网络游戏的通知》，2021年8月30日。"
    url: https://www.gov.cn/xinwen/2021-08/30/content_5634205.htm
    date: '2021-08-30'
    supports:
    - identity.implementation_regime
    - timeline.announcement
    verification_status: verified
    access_level: official-document
    locator: Xinhua/gov.cn news release summarizing the notice
design_applications:
  - paper: Wang (2026)
    doi: 10.1016/j.jdeveco.2026.103812
    journal: Journal of Development Economics
    year: 2026
    research_question: How did the 2021 restriction on minors' online gaming affect their time use, academic performance, and health?
    population: Chinese minors and young adults who play online video games
    outcome: Gaming engagement, overall internet use, academic performance, study time, physical health, mental well-being
    data_used:
    - Nationally representative survey data
    - City-level administrative exam data
    treatment_encoding: Binary indicator for minors after 1 September 2021; regression kink at age 18 using city-level data
    comparison: Adults and pre-policy minors; cohorts just above and below age 18
    empirical_design: Difference-in-differences and regression kink
    assumptions:
    - Parallel trends in outcomes between minors and adults before the policy
    - No other discontinuous changes at age 18
    threats_addressed:
    - Compliance and substitution examined through time-use and internet-use outcomes
    - Robustness checked with city-level RKD on exam scores
    evidence_refs:
    - E1
    - E2
method_transfer: null
readiness_blockers: []
superseded_by: null
deprecation_reason: null
---

## Institutional Background

China had regulated minors' online gaming since at least 2019, when the National Press and Publication Administration introduced daily and holiday time limits and required real-name registration. Despite these rules, public and official concern about excessive gaming persisted, leading to calls for stricter limits in 2021 [E2, reported claim].

## What Changed

On 30 August 2021 the NPPA issued Notice 国新出发〔2021〕14号, effective 1 September 2021. The notice limits online video-game service to minors to one hour per day on Fridays, Saturdays, Sundays, and statutory holidays between 20:00 and 21:00, and prohibits service on all other days. All online game companies must verify users' real identities and connect to the NPPA anti-addiction verification system [E2, verified fact].

## Implementation and Assignment

The regulation applies nationwide and simultaneously to all licensed online games. Treatment is determined by the user's registered age relative to 18 and the calendar date relative to 1 September 2021. Because the age rule is enforced through real-name registration, a user's birth date is the primary assignment variable [E2, verified fact].

## Why This Creates Empirical Variation

The policy combines a sharp calendar-date discontinuity with a clear age threshold. Researchers can compare minors just before and after the policy, or compare individuals just below and just above age 18 after the effective date. The national scope avoids concerns about selective geographic adoption, although compliance and substitution behaviors must be modeled [analytical inference].

## Identification Risks

The main risks are noncompliance through shared adult accounts, substitution into other screen-time activities, measurement error in self-reported gaming, anticipation from the 2019 rules, and concurrent policy changes such as the 2021 private-tutoring regulation. The paper finds that gaming and internet use fell but academic and health benefits were not detectable, suggesting substitution and compliance margins are important [E1, reported claim].

## Data Requirements

Useful data include individual-level gaming time, internet use, study time, academic scores, and health indicators, together with age/birth date and observation date. Platform administrative data on real-name registration would improve compliance measurement, but survey data are sufficient for intent-to-treat estimates [analytical inference].

## Evidence Notes

The full text of 国新出发〔2021〕14号 is available on the gov.cn policy archive [E2]. The paper's abstract and design details are taken from the IDEAS/RePEc entry [E1]. A contemporaneous Xinhua/gov.cn news release confirms the announced rules [E3].
