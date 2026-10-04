---
schema_version: 2
id: china-2014-hukou-local-implementation
name: Local Implementation of China's 2014 Hukou Reform Framework
aliases:
- 2014 Hukou Reform
- 户籍制度改革
- 国发〔2014〕25号地方实施

status: contested
provenance:
  task_id: task-364b55fe5b53
scope:
  country: China
  regions:
  - All Chinese prefecture-level cities and counties
  domains:
  - labor
  - migration
  - urban
  - public-services
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    The variation occurs in China and assigns exposure to Chinese cities, migrants, and
    local residents. The 2014 State Council framework created two distinct empirical
    structures: a national city-size threshold (megacities vs. non-megacities) and
    staggered local adoption of unified household registration. Researchers must not treat
    either as a uniform national before-after shock.
identity:
  instrument: Local implementation measures issued under the 2014 State Council hukou
    reform framework
  authority: State Council; provincial and municipal governments
  legal_identifiers:
  - State Council Document No. 25 (2014)
  - State Council Order No. 663 (2015) — Regulations on Residence Permits
  implementation_regime: >
    The State Council Document No. 25 of 24 July 2014 establishes a national framework:
    it directs local governments to abolish the agricultural/non-agricultural hukou
    distinction, adopt a unified resident hukou, introduce a residence-permit system, and
    apply differentiated settlement rules by city size. What is actually implemented,
    when, and with what eligibility conditions is left to provincial and municipal
    governments. Therefore the empirical object is local implementation, not the national
    text alone. Some localities had already piloted unified hukou before 2014 (e.g.,
    Chongqing in 2007, Chengdu in 2010), so a simple post-2014 dummy is invalid.
  assignment_mechanism: >
    Two assignment structures are available under the same framework. (1) National
    city-size threshold: the central document explicitly relaxes settlement in non-
    megacities (urban population below 5 million) while retaining strict controls,
    residence permits, and points systems in megacities (5 million and above). This
    creates a sharp population-threshold comparison if city population is measured
    consistently. (2) Staggered local adoption: cities and prefectures adopted concrete
    unified-hukou / agricultural-hukou-abolition measures at different dates, allowing a
    staggered difference-in-differences design. The two structures measure different
    things and should not be pooled without explicit justification.
  parent: null
  related_variations:
  - china-migrants-firms-evidence
  - china-hukou-migration-productivity
timeline:
  announcement: '2014-07-24'
  effective: '2014-07-24'
  implementation_start: 2007
  implementation_end: ongoing
  local_timing: >
    The national framework was signed on 24 July 2014 and publicly issued shortly
    afterward. Provinces and cities were instructed to publish concrete implementation
    measures. Empirical studies report staggered adoption: some pilot cities abolished
    the agricultural hukou before 2014; by the end of 2014 about 17 prefecture-level
    cities had implemented reform, by the end of 2015 about 140, and by the end of 2016
    most had begun. Megacities introduced or retained points systems and tight controls.
    Residence-permit regulations were formalized by State Council Order No. 663 in 2015.
    A national target of granting urban registration to about 100 million people by 2020
    was set in the National New-Type Urbanization Plan (2014–2020).
  anticipation: >
    The general direction of hukou reform was discussed in the 2013 Third Plenum and the
    National New-Type Urbanization Plan, so agents could anticipate change in broad
    terms. The exact timing and content of local measures, however, were not fully known
    in advance, especially for non-megacities.
  last_verified: '2026-09-28'
assignment:
  unit: City-year or individual-year, depending on the design
  treated: >
    Under the city-size threshold design, treated units are non-megacity cities
    (urban population below 5 million) and the migrants or workers residing in them after
    the national reform. Under the staggered design, treated units are cities that have
    formally adopted unified / abolished-agricultural hukou by a given year, and the
    migrants or rural-hukou residents affected by that change.
  comparison_pool: >
    Under the city-size threshold design, megacity cities (urban population 5 million and
    above) serve as the control group, conditional on common trends and smoothness around
    the threshold. Under the staggered design, not-yet-reformed or never-reformed cities
    are the control group, conditional on parallel trends.
  rule: >
    City-size-threshold rule: classify each city by its urban resident population relative
    to the 5 million cutoff used in State Council Document No. 25; treatment is
    post-2014 non-megacity status. Staggered-adoption rule: for each city-year, code
    whether the locality has formally abolished the agricultural/non-agricultural
    distinction and implemented unified resident hukou; treatment is the adoption
    indicator. Both rules require choosing how population is measured (total urban vs.
    native-only) and how formal adoption maps into effective rights.
  intensity: >
    Varies. The city-size design uses a binary threshold but can be enriched with
    settlement-threshold indices or points-system stringency. The staggered design is
    binary at the city-year level but can be weighted by the scope of unified registration
    or service-access expansion.
  exemptions:
  - Megacities retained strict population controls and points systems
  - Some high-barrier cities (Beijing, Shanghai, Shenzhen, Guangzhou, Tianjin) maintained
    much higher thresholds
  - Local eligibility conditions differ by employment, housing, social insurance, and
    education requirements
  compliance: >
    Formal local rules do not equal actual registration conversion or service access.
    Many migrants did not convert hukou even where rules were relaxed, and some retained
    rural land rights. Compliance is partial and selective.
  exposure_construction: >
    For the threshold design: obtain annual city-level urban population (consistent with
    the source used in the paper, e.g., native urban population or total urban population),
    classify cities relative to the 5 million cutoff, and interact non-megacity status
    with a post-2014 indicator. For the staggered design: build a city-by-year panel of
    formal adoption dates of unified hukou, typically hand-collected from local government
    documents or taken from paper-reported tables; merge with individual/city-level
    outcome data by city code and year. In both cases, keep separate codes for service-
    access components (education, health, social security, housing) if available.
  required_identifiers:
  - city code
  - calendar year
  - population measure
  - hukou or migrant status
  spillovers: >
    Relaxation in one city can divert migrants from nearby cities and change labor supply
    in destination markets. Megacities may receive spillover demand from tightened
    non-megacity inflows. Cross-city sorting and network effects can violate the stable-
    unit assumption.
research_compatibility:
  outcome_domains:
  - migration
  - employment
  - wages
  - public services
  - education
  - housing
  - fertility
  - firm performance
  - entrepreneurship
  affected_populations:
  - rural hukou holders
  - migrants
  - local workers
  - urban residents
  - rural stayers
  - firms
  mechanism_channels:
  - settlement eligibility
  - labor supply
  - migration
  - service access
  - local labor-market competition
  - social integration
  - fertility incentives
  best_for:
  - Research that can reconstruct local reform content and link individuals or labor markets
    to locality-specific timing
  - Studies exploiting the national megacity threshold with credible population data
  - Outcomes observable in CMDS, CFPS, census, or firm surveys with city identifiers
  not_good_for:
  - A national before-after comparison using 2014 as a uniform treatment date
  - Designs without migrant or hukou identifiers
  - Outcomes requiring precise registration-conversion timing at the individual level
  - Studies that cannot distinguish the city-size threshold from staggered local adoption
design:
  claim_type: causal
  affordances:
  - local timing differences in unified hukou adoption
  - national city-size threshold at 5 million urban residents
  - differential settlement thresholds and points systems
  - repeated cross-sectional migrant surveys with city identifiers
  - pre-2014 pilot cities for placebo and pre-trend checks
  candidate_designs:
  - difference-in-differences by city-size threshold (megacity vs. non-megacity)
  - staggered difference-in-differences using hand-collected local adoption dates
  - regression discontinuity at the 5 million population cutoff
  - triple differences adding migrant/native or rural/urban status
  - event study around local reform adoption
  identifying_variation: >
    The primary sources of variation are (i) the national rule that treats cities below
    and above 5 million urban residents differently, and (ii) the staggered city-level
    adoption of unified resident hukou after the 2014 framework. These are conceptually
    distinct: the threshold captures cross-sectional differential treatment intensity,
    while staggered adoption captures within-city timing.
  assumptions:
  - The 5 million population cutoff is applied as specified in the national document and
    population is measured consistently across cities
  - Cities on either side of the threshold follow common trends absent the reform, or the
    discontinuity is smooth in covariates
  - Staggered adoption timing is conditionally independent of outcome shocks
  - Migration responses do not create fatal composition changes
  - Policy components are measured correctly and formal rules proxy for effective rights
  diagnostics:
  - Verify local legal texts or paper-reported adoption tables
  - Test sensitivity to population measure (total vs. native urban)
  - Inspect pre-trends in event-study specifications
  - Test for sorting and sample composition changes
  - Separate city-size tiers and compare threshold robustness
  - Use Callaway-Sant'Anna or Sun-Abraham estimators for staggered designs
  primary_strategy: >
    Two-stage empirical strategy: first, choose either the city-size threshold or the
    staggered adoption design; second, estimate intent-to-treat effects on migrants or
    local residents using city-level or individual-level panel data with city and year
    fixed effects and appropriate controls.
  estimand: >
    The local average treatment effect of exposure to the 2014 hukou reform framework on
    migrant or local outcomes, conditional on the chosen design assumptions and the
    specific assignment mechanism (threshold or staggered adoption).
  treatment_variable: >
    Non-megacity indicator interacted with post-2014 (threshold design), or city-year
    unified-hukou adoption indicator (staggered design).
  comparison_logic: >
    Threshold design: non-megacities vs. megacities before and after 2014. Staggered
    design: adopting vs. not-yet-adopting cities before and after each city's adoption
    year.
  estimation_notes: >
    Include city fixed effects, year fixed effects, and, where possible, province-by-year
    fixed effects. Control for city-level time-varying economic conditions and migration
    networks. Cluster standard errors at the city level. For staggered adoption, use
    modern estimators that avoid negative weights from two-way fixed effects. For the
    threshold design, report robustness to population definition and bandwidth.
threats:
- type: endogenous-local-adoption
  basis: inferred
  condition: >
    Local governments chose adoption timing and eligibility rules in response to local
    economic conditions, fiscal capacity, and migration pressure, which may correlate with
    labor-market outcomes.
  evidence_refs:
  - E1
  - E3
  - E4
  possible_diagnostics:
  - model adoption timing
  - inspect pre-trends
  - compare reform content across cities
  - use modern staggered DID estimators
- type: threshold-manipulation
  basis: inferred
  condition: >
    The 5 million cutoff classification depends on whether population is measured using
    total urban population or native-only population; reclassification can change treatment
    status and may be manipulated or mismeasured.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - compare results under alternative population definitions
  - test for sorting or population reporting manipulation around the cutoff
  - use donut RD excluding cities near the cutoff
- type: endogenous-sorting
  basis: inferred
  condition: >
    The reform can change who lives in which city and who obtains local hukou, altering
    sample composition and confounding outcome comparisons.
  evidence_refs:
  - E2
  - E3
  possible_diagnostics:
  - track stable cohorts
  - report composition tests
  - distinguish residents from destination labor markets
  - use individual fixed effects where panel data exist
- type: formal-vs-effective-rights
  basis: inferred
  condition: >
    Abolishing the agricultural hukou label or relaxing settlement rules does not
    automatically grant equal access to public services, especially where local fiscal
    capacity or points systems remain restrictive.
  evidence_refs:
  - E1
  - E3
  possible_diagnostics:
  - code service-specific components separately
  - measure actual registration conversion rates
  - examine outcomes that should respond only if services improved
empirical_requirements:
  contract_version: 1
  population: Migrants, hukou holders, workers, households, or local labor markets in
    Chinese cities
  observation_unit: Individual-year, household-year, firm-year, or city-year linked to
    local reform timing
  geography_level: City or lower implementation jurisdiction
  time_start: 2007
  time_end: 2020
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields:
  - outcome
  - locality
  - year
  - hukou or migrant status
  - city population (for threshold design)
  - local reform adoption date (for staggered design)
  required_identifiers:
  - city code
  - year
  - population eligibility marker
  treatment_key:
  - city code
  - effective date or population classification
  - eligibility category
  treatment_source: >
    State Council Document No. 25 (2014) for the national framework; local government
    implementation notices and residence-permit regulations for city-specific dates and
    rules; China City Statistical Yearbook or Urban Construction Yearbook for population
    data; CMDS, CFPS, census microdata, or firm surveys for outcomes. Paper-reported
    hand-collected city-level reform timing tables (e.g., Cai & Zhong 2025; Dong, Liang &
    Zhang 2023) are available as secondary sources but are not a substitute for primary
    local documents.
  measurement_risks:
  - formal versus actual implementation
  - multidimensional reform content
  - migration sorting
  - changing city codes
  - inconsistency between total and native urban population measures
  - reliance on paper-reported adoption tables without primary verification
evidence:
- id: E1
  source_type: policy-document
  citation: >
    State Council. 2014. "Opinions on Further Promoting Reform of the Household
    Registration System" (Guo Fa [2014] No. 25).
  url: https://www.ndrc.gov.cn/xwdt/ztzl/xxczhjs/ghzc/201605/t20160505_971903.html
  date: '2014-07-24'
  supports:
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.announcement
  - timeline.effective
  - assignment.rule
  - assignment.compliance
  verification_status: verified
  access_level: official-document
  locator: >
    Full text reproduced on NDRC website; signed 24 July 2014. Sections II–IV establish
    the city-size settlement hierarchy (towns/small cities fully open, medium cities
    orderly open, large cities conditional, megacities >5m controlled), unified urban-rural
    hukou, residence permits, and the directive for local governments to issue concrete
    measures.
- id: E2
  source_type: paper
  citation: >
    An, Lei, Yu Qin, Jing Wu, and Wei You. 2024. "The Local Labor Market Effect of
    Relaxing Internal Migration Restrictions: Evidence from China." Journal of Labor
    Economics 42 (1): 161–200.
  url: https://doi.org/10.1086/722620
  date: 2024
  supports:
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.exposure_construction
  - design.primary_strategy
  - design.comparison_logic
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  verification_status: reported
  access_level: full-text
  locator: >
    Uses 2011–2017 CMDS, 2015 census microdata, and 2012/2014/2016/2018 CFPS; treatment
    is non-megacity status (urban population below 5 million) interacted with post-2014;
    difference-in-differences comparing migrants and natives in non-megacities vs.
    megacities. Replication package available.
- id: E3
  source_type: paper
  citation: >
    Cai, Tianxin, and Renyao Zhong. 2025. "Fertility Responses to the Citizenization of
    Rural Migrants: Evidence from the Hukou Reform in China." BMC Public Health 25: 735.
  url: https://doi.org/10.1186/s12889-025-21753-0
  date: 2025
  supports:
  - timeline.local_timing
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.exposure_construction
  - design.primary_strategy
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  verification_status: reported
  access_level: full-text
  locator: >
    Uses CMDS 2011–2018 and manually collected implementation dates for 286 prefecture-
    level cities; reports that 17 cities had implemented by end-2014, 140 by end-2015, and
    most by end-2016; staggered DID with city and year fixed effects and Callaway-Sant'Anna
    robustness check.
- id: E4
  source_type: paper
  citation: >
    Dong, Xiaoqi, Yinhe Liang, and Jiawei Zhang. 2023. "Fertility Responses to the
    Relaxation of Migration Restrictions: Evidence from the Hukou Reform in China." China
    Economic Review 81: 102040.
  url: https://doi.org/10.1016/j.chieco.2023.102040
  date: 2023
  supports:
  - timeline.local_timing
  - assignment.rule
  - assignment.exposure_construction
  verification_status: reported
  access_level: full-text
  locator: >
    Exploits city-by-city rollout of the 2014 hukou reform after manually collecting
    implementation timing for 311 Chinese cities; uses CMDS 2011–2017; supports existence
    of staggered local adoption as an assignment structure.
- id: E5
  source_type: paper
  citation: >
    Jiang, Ye, and Yue Yin. 2026. "Delinking Social Identity From Rural-Urban
    Stereotypes: The Labor Market Effects of Abolishing Agricultural Hukou in China."
    Journal of Regional Science 66(3):746-765. DOI: 10.1111/jors.70032.
  url: https://doi.org/10.1111/jors.70032
  date: 2026
  supports:
  - timeline.local_timing
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.exemptions
  - assignment.exposure_construction
  - design.primary_strategy
  - design.comparison_logic
  - design.estimation_notes
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.required_fields
  verification_status: verified
  access_level: full-text
  locator: >
    Inspected open-access article, sections 2.2, 3, and 4 plus Appendix references.
    It uses five repeated CGSS cross-sections (2010-2013 and 2015) in 89 anonymized
    survey cities. Rather than linking named local notices, it infers each city's
    adoption year as the first survey year with a respondent observed to have changed
    from agricultural to residential hukou: 32 cities in 2010, 16 in 2011, 20 in
    2012, 6 in 2013, 9 in 2015, and six after 2015 (coded never-treated in its sample).
    The article explicitly says city names and precise locations are confidential,
    excludes residents whose hukou is registered elsewhere and same-year registrants,
    and estimates city and year fixed-effect DID with city-clustered standard errors,
    event studies, and a native-born robustness sample. This is a paper-specific
    respondent-observation proxy for reform timing, not verified legal adoption dates
    or a reusable named-city treatment roster.
design_applications:
- paper: 'The Local Labor Market Effect of Relaxing Internal Migration Restrictions:
    Evidence from China'
  doi: 10.1086/722620
  journal: Journal of Labor Economics
  year: 2024
  research_question: How does relaxing internal migration restrictions affect labor-market
    outcomes of incumbent migrants and natives?
  population: Migrants and natives in 228 Chinese cities, 2011–2017
  outcome: Wages, labor-force participation, access to social security
  data_used:
  - China Migrants Dynamic Survey (CMDS) 2011–2017
  - 2015 population census microdata
  - China Family Panel Studies (CFPS) 2012, 2014, 2016, 2018
  - China City Statistical Yearbook
  treatment_encoding: Non-megacity indicator (urban population below 5 million using native
    urban population) interacted with post-2014 indicator
  comparison: Non-megacity vs. megacity migrants and natives before and after 2014
  empirical_design: Difference-in-differences based on the national city-size threshold
  assumptions:
  - common trends between megacity and non-megacity cities
  - population measure consistently identifies the 5 million cutoff
  - no selective migration that breaks the comparison
  threats_addressed:
  - alternative population measures and sample choices reported in robustness
  - pre-trends examined via event study
  evidence_refs:
  - E2
- paper: 'Fertility Responses to the Citizenization of Rural Migrants: Evidence from the
    Hukou Reform in China'
  doi: 10.1186/s12889-025-21753-0
  journal: BMC Public Health
  year: 2025
  research_question: Does obtaining urban citizenship through hukou reform affect fertility
    among rural female migrants?
  population: Rural female migrants aged 20–49 in 286 prefecture-level cities, 2011–2018
  outcome: Fertility in the past 12 months
  data_used:
  - China Migrants Dynamic Survey (CMDS) 2011–2018
  - manually collected prefecture-level reform implementation dates
  treatment_encoding: City-year unified hukou adoption indicator (one-year lag)
  comparison: Migrants in cities that adopted reform vs. not-yet-adopted cities, before
    and after adoption
  empirical_design: Staggered difference-in-differences with city and year fixed effects
  assumptions:
  - staggered adoption is conditionally exogenous
  - parallel trends in fertility across adopting and non-adopting cities
  - no selective migration that confounds the city-year treatment
  threats_addressed:
  - pre-trends via event study
  - robustness using Callaway-Sant'Anna staggered DID estimator
  - placebo using urban migrants
  evidence_refs:
  - E3
- paper: 'Delinking Social Identity From Rural-Urban Stereotypes: The Labor Market Effects
    of Abolishing Agricultural Hukou in China'
  doi: 10.1111/jors.70032
  journal: Journal of Regional Science
  year: 2026
  research_question: >
    How did paper-inferred local abolition of the agricultural/nonagricultural hukou
    distinction affect earnings and employment for rural stayers, rural-urban migrants,
    and urban incumbents?
  population: >
    Adults in five repeated CGSS cross-sections (2010-2013 and 2015) across 89
    anonymized survey cities; individuals whose registered-hukou city differs from
    their current city and same-year registrants are excluded.
  outcome: >
    Deflated annual labor earnings and current agricultural, nonagricultural, or
    nonemployment status, reported separately by original hukou and residence group.
  data_used:
  - Chinese General Social Survey (CGSS) 2010-2013 and 2015 repeated cross-sections
  - respondent-reported hukou category and change history
  - provincial CPI for earnings deflation
  treatment_encoding: >
    A city-year adoption indicator beginning in the first CGSS survey wave in which a
    city has an observed respondent who switched from agricultural to residential hukou.
    The article groups 89 anonymized survey cities by this inferred first-observation
    year; it does not merge a named-city legal-notice roster.
  comparison: >
    Individuals in cities not yet observed to have adopted the residential-hukou
    designation, relative to individuals in cities observed to have adopted it, before
    and after each paper-inferred adoption year.
  empirical_design: >
    City and year fixed-effect staggered DID on repeated cross-sections, with individual
    controls and city-clustered standard errors; event-study leads and a native-born
    restricted-sample robustness check.
  assumptions:
  - First observed residential-hukou respondent is a valid proxy for local reform start.
  - Anonymized CGSS survey-city panels can support comparable pretrends despite no named-city joins.
  - Excluding mismatched registration and residence locations adequately limits exposure miscoding.
  - Reform-timing variation is conditionally unrelated to group-specific labor-market shocks.
  threats_addressed:
  - Event-study leads and pre-reform group-trend tests reported by the paper
  - Exclusion of ambiguous registration-location and same-year-change observations
  - Native-born restricted-sample robustness check
  - Explicit limitation that city identities cannot be linked to external local-policy data
  evidence_refs:
  - E5
readiness_blockers:
- >
  A canonical city-by-year table of local implementation dates has not been independently
  verified from primary local government documents inside this record; current support
  relies on paper-reported hand-collected tables.
- >
  The two main assignment mechanisms (national 5-million threshold vs. staggered local
  adoption) measure different policy margins and should not be conflated. They must be split
  into separate canonical variation cases before either mechanism is recommended or this
  record is promoted beyond extracted.
- >
  Formal abolition of the agricultural hukou label is not equivalent to actual service
  access or registration conversion; a service-component coding remains unverified.
- >
  Population measurement for the 5-million threshold differs across sources (total urban
  vs. native-only), and a replication study suggests the threshold wage effect is sensitive
  to this choice and to flexible population controls.
- >
  No design application in this record has been grounded from a replication package or
  primary data source; exact merge keys and sample construction require full-text or
  replication verification.
- >
  The JRS 2026 application offers an inspected and useful paper-specific staggered
  design, but its city adoption dates are inferred from the first observed residential-
  hukou respondent in anonymized CGSS cities. They cannot validate formal local legal
  adoption, be joined to named-city outcomes, or replace a verified local-notice roster.
method_transfer: null
---
## Institutional Background

China's hukou system historically tied formal registration and access to many local public services to place and registration category. By the early 2010s rural-to-urban migrants could usually live and work in cities but faced unequal access to education, health care, social insurance, and housing. The 2014 State Council framework sought more orderly urban settlement and broader service coverage while retaining differentiated settlement rules by city size. [E1]

The framework did not abolish local discretion. It instructed provinces and cities to formulate concrete and operable measures, making local implementation—not only the national document—the relevant empirical object. Some localities had already begun piloting unified hukou before 2014. [E1; E3]

## What Changed

The national framework called for (1) unified urban-rural registration terminology, abolishing the agricultural/non-agricultural distinction; (2) differentiated settlement rules by city size; (3) a residence-permit system; and (4) broader basic public-service coverage. The actual eligibility conditions, pace, and effective rights differed across jurisdictions. [E1]

## Implementation and Assignment

Researchers must reconstruct local effective dates and policy components. Two assignment structures are available under the same framework. The first is the national city-size threshold: cities with urban population below 5 million were directed to relax settlement substantially, while megacities retained strict controls. The second is staggered local adoption: cities adopted concrete unified-hukou measures at different dates, generating a classic staggered difference-in-differences structure. A national post-2014 indicator does not capture either assignment structure correctly. [E1; E2; E3; E4]

## Why This Creates Empirical Variation

The city-size threshold creates a sharp comparison if population is measured consistently and if cities on either side of the threshold would have followed similar trends absent reform. The staggered rollout creates within-city timing variation if adoption dates are conditionally independent of local outcome shocks. Both designs require explicit handling of migration and sorting. [E2; E3; analytical inference]

## Identification Risks

Local adoption and rule content can respond to migration pressure, labor demand, fiscal capacity, or city-growth strategies. Migration and hukou conversion can change sample composition. Multiple components—settlement, permits, and services—may move at different times. The 5 million population cutoff is sensitive to measurement choices, and a replication study suggests that flexible controls around the cutoff can weaken the wage findings. Formal abolition of the agricultural hukou label does not guarantee equal effective rights. [E1; E2; E3; analytical inference]

## Data Requirements

Microdata need locality, time, hukou or migrant status, and relevant outcomes. For the threshold design, city population must be measured consistently with the national rule. For the staggered design, a city-by-year adoption table is required. The treatment source must preserve document dates, effective dates, city tier, eligibility conditions, and policy components. Primary local documents are preferred; paper-reported tables are a usable secondary source. [E2; E3; E4]

## Evidence Notes

E1 verifies the national framework and the requirement for locally tailored measures. E2 documents a city-size threshold design using CMDS, census, and CFPS data. E3 and E4 document staggered city-level adoption designs using CMDS and hand-collected implementation dates. None of the paper-reported local timing tables has been independently verified from primary local documents inside this record; they are treated as reported claims.
