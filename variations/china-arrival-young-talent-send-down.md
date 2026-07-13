---
schema_version: 2
id: china-arrival-young-talent-send-down
name: The Arrival of Young Talent — China's Send-Down Movement and Rural Education
aliases:
- Send-down youth education effects
- Up to the Mountains Down to the Countryside
- educated youth rustication
- zhiqing 知青 movement
- SDY rural education

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - Rural counties across China
  domains:
  - education
  - labor
  - development
  - history
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: The Send-Down Movement (上山下乡运动), which mandated approximately 16 million urban "educated youth" (zhiqing) to
    resettle in the Chinese countryside between the mid-1960s and the late 1970s, generating county-level variation in the
    intensity of exposure to urban-educated migrants
  authority: Chinese Communist Party under Mao Zedong; Central Committee directives and local government implementation
  legal_identifiers:
  - 1966 Central Committee directive on the Send-Down Movement
  - 1968 Mao Zedong instruction "It is very necessary for educated youth to go to the countryside"
  implementation_regime: Urban middle-school and high-school graduates were assigned to rural communes and production brigades
    across China; the number of sent-down youths (SDYs) assigned to each county varied based on county reception capacity,
    geographic proximity to urban centers, and central planning decisions
  assignment_mechanism: County-level variation in SDY assignment intensity was driven by a combination of central planning
    priorities, provincial quotas, geographic factors, and county-level reception capacity — factors that are partially exogenous
    to pre-existing local educational outcomes
  parent: null
  related_variations: []
timeline:
  announcement: '1966'
  effective: '1968'
  implementation_start: 1966
  implementation_end: 1978
  local_timing: The movement began in the mid-1960s, intensified dramatically after Mao's 1968 instruction, and gradually
    wound down after the Cultural Revolution ended in 1976, with most SDYs returning to cities by the late 1970s
  anticipation: The movement was a product of the broader Cultural Revolution and was not anticipated by rural communities
    before its onset; the timing and intensity of SDY assignments were determined by central and provincial authorities
  last_verified: '2026-07-13'
assignment:
  unit: County (rural county in China)
  treated: Rural counties that received sent-down youths; treatment is continuous based on the number (or density) of SDYs
    assigned to the county during the movement
  comparison_pool: Counties that received fewer SDYs per capita, providing cross-county variation in treatment intensity;
    within-county variation across cohorts before and after the movement
  rule: Counties with higher SDY-to-population ratios received a larger influx of urban-educated youth, who served as teachers,
    tutors, and role models in local schools and communities
  intensity: Continuous — number of sent-down youths per 1,000 rural residents (or per school-age child) at the county level,
    measured cumulatively over the movement period
  exemptions: []
  compliance: The movement was mandated by central policy and enforced through local government implementation; compliance
    was high, though some youths avoided assignment through health exemptions or family connections
  exposure_construction: Construct county-level SDY density as (total number of sent-down youths assigned to the county) /
    (county population); alternatively, use SDY per school-age child or per rural school
  required_identifiers:
  - county code
  - year
  - sent-down youth count
  - county population
  - school-age population
  spillovers: SDYs may have affected neighboring counties through migration or school attendance across county borders; returning
    SDYs may have transmitted knowledge and attitudes acquired in the countryside to urban areas
research_compatibility:
  outcome_domains:
  - education
  - human capital
  - rural development
  - intergenerational mobility
  - labor market outcomes
  affected_populations:
  - Rural children and adolescents in China
  - 1970s–2000s birth cohorts
  - rural households in recipient counties
  mechanism_channels:
  - teacher supply and quality
  - peer effects from educated youth
  - parental aspiration changes
  - improved school resources
  - knowledge transmission
  best_for:
  - Studying how exposure to educated outsiders affects rural educational outcomes
  - human capital spillovers
  - long-run effects of historical education interventions
  not_good_for:
  - Short-run contemporaneous effects (data lags)
  - individual-level treatment assignment (county-level treatment)
  - effects on the SDYs themselves (the paper focuses on rural children)
design:
  affordances:
  - county-level variation in SDY density
  - variation across birth cohorts within counties
  - pre-movement and post-movement comparison
  - long panel of educational outcomes (1982–2005)
  candidate_designs:
  - difference-in-differences comparing high-SDY and low-SDY counties before and after the movement
  - cohort-based DiD exploiting age-at-exposure variation
  - instrumental variables using geographic determinants of SDY assignment
  identifying_variation: Cross-county variation in the number of sent-down youths assigned per rural resident, which generates
    differential exposure of rural children to urban-educated youth during their school-age years
  assumptions:
  - SDY assignment across counties is orthogonal to county-level trends in educational outcomes conditional on observables
  - no selective migration in response to SDY placement
  - the assignment of SDYs is not correlated with other contemporaneous reforms affecting education
  diagnostics:
  - Pre-trend analysis of educational outcomes across high-SDY and low-SDY counties
  - balance tests on county characteristics
  - robustness to controlling for geographic and economic covariates
  - placebo tests using outcomes unaffected by SDY exposure
  primary_strategy: Difference-in-differences across counties with varying SDY intensity, comparing birth cohorts differentially
    exposed based on age during the movement
  estimand: The causal effect of the recorded exposure on Years of schooling, junior high school completion, literacy rates,
    conditional on the stated design assumptions.
  treatment_variable: County-level cumulative SDY count per capita, interacted with birth cohort exposure (whether the cohort
    was of school age during the movement)
  comparison_logic: High-SDY-density counties vs low-SDY-density counties; cohorts exposed during school age vs those beyond
    school age
  estimation_notes: Difference-in-differences across counties with varying SDY intensity, comparing birth cohorts differentially
    exposed based on age during the movement
threats:
- type: omitted-variable
  basis: inferred
  condition: Counties that received more SDYs may have differed systematically from low-SDY counties in ways that affected
    educational trends (e.g., more developed areas may have had better schools and also received more SDYs)
  evidence_refs:
  - E1
  possible_diagnostics:
  - Control for county GDP
  - urbanization
  - distance to cities
  - and other pre-movement characteristics; test balance on pre-movement education outcomes; use geographic instruments for
    SDY placement
- type: sorting-selection
  basis: inferred
  condition: SDYs were not randomly assigned to counties; assignment reflected central planning priorities, county reception
    capacity, and provincial quotas that may correlate with educational conditions
  evidence_refs:
  - E1
  possible_diagnostics:
  - Instrument SDY density using geographic or political determinants that affect assignment but not educational trends
  - examine assignment process from historical records
- type: other-concurrent-reforms
  basis: inferred
  condition: The Cultural Revolution period (1966–1976) involved widespread disruption to education, including school closures
    and curriculum changes; separating the SDY effect from broader Cultural Revolution disruptions is challenging
  evidence_refs:
  - E1
  possible_diagnostics:
  - Control for Cultural Revolution intensity measures
  - use variation in SDY timing relative to school disruptions
  - examine subsamples with varying disruption levels
empirical_requirements:
  contract_version: 1
  population: Rural counties in China observed over 1982–2005, covering birth cohorts that were school-age during and after
    the Send-Down Movement
  observation_unit: County-cohort or county-year (depending on outcome data structure)
  geography_level: County (rural county, xian)
  time_start: 1982
  time_end: 2005
  minimum_frequency: 'Decennial (census years: 1982, 1990, 2000; plus 2005 mini-census)'
  minimum_pre_periods: 1
  minimum_post_periods: 3
  required_fields:
  - county code
  - year
  - sent-down youth count
  - county population
  - school-age population
  - educational attainment (years of schooling
  - enrollment rates
  - literacy)
  - age cohort
  required_identifiers:
  - county code
  - year
  - SDY count measure
  treatment_key:
  - county code
  - year
  - SDY density (SDYs per capita)
  - birth cohort (for cohort-based designs)
  treatment_source: County-level gazetteers (difangzhi) and published historical records of sent-down youth placement; census
    data for educational outcomes
  measurement_risks:
  - County boundary changes over time
  - incomplete historical records of SDY counts in some counties
  - differential recall or reporting quality across census waves
  - migration of rural residents across counties between treatment and outcome measurement
evidence:
- id: E1
  source_type: paper
  citation: 'Chen, Yi, Ziying Fan, Xiaomin Gu, and Li-An Zhou. 2020. "Arrival of Young Talent: The Send-Down Movement and
    Rural Education in China." American Economic Review 110 (11): 3393–3430.'
  url: https://doi.org/10.1257/aer.20191414
  date: 2020
  supports:
  - identity
  - assignment
  - design
  - threats
  - empirical_requirements
  verification_status: verified
design_applications:
- paper: 'Arrival of Young Talent: The Send-Down Movement and Rural Education in China'
  doi: 10.1257/aer.20191414
  journal: American Economic Review
  year: 2020
  research_question: How did the influx of urban educated youth to the countryside during the Send-Down Movement affect rural
    children's educational outcomes?
  population: Rural counties in China, 1982–2005 census and survey data
  outcome: Years of schooling, junior high school completion, literacy rates
  data_used:
  - Chinese population census (1982, 1990, 2000)
  - 2005 1% mini-census
  - county gazetteers for SDY records
  treatment_encoding: County-level cumulative SDY count per capita, interacted with birth cohort exposure (whether the cohort
    was of school age during the movement)
  comparison: High-SDY-density counties vs low-SDY-density counties; cohorts exposed during school age vs those beyond school
    age
  empirical_design: Difference-in-differences across counties with varying SDY intensity, comparing birth cohorts differentially
    exposed based on age during the movement
  assumptions:
  - SDY assignment is conditionally exogenous to educational trends
  - no differential migration across counties correlated with SDY exposure
  - no other county-level shocks correlated with SDY intensity
  threats_addressed:
  - County-level selection via rich controls and robustness checks
  - pre-trend analysis
  - geographic and historical covariates
  - alternative SDY measures
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
method_transfer: null
---
## Institutional Background

During the Cultural Revolution (1966–1976), the Chinese Communist Party under Mao Zedong launched the "Up to the Mountains, Down to the Countryside" movement (上山下乡运动), also known as the Send-Down Movement. Approximately 16 million urban middle-school and high-school graduates — the "educated youth" or zhiqing (知青) — were sent to rural areas to be "re-educated" by peasants. These urban youths were assigned to rural communes and production brigades across virtually all of China's rural counties, where they lived and worked for years before most returned to cities in the late 1970s. [E1]

## What Changed

The massive influx of urban-educated youth to rural areas brought human capital to previously isolated rural communities. The SDYs were typically better educated than local rural residents, and many served as teachers or tutors in local schools, or otherwise influenced rural children's educational aspirations and opportunities. The presence of these urban youths introduced new knowledge, attitudes, and role models into rural education systems that had been disrupted by the Cultural Revolution. The key variation is the county-level intensity of this influx. [E1]

## Implementation and Assignment

The assignment of SDYs to counties was determined by a combination of central planning (provincial quotas), geographic proximity (counties near cities tended to receive more SDYs), and reception capacity (counties with more available housing and agricultural land could accommodate more youths). This created substantial variation across counties in SDY density — ranging from counties that received almost no SDYs to those that received very large numbers relative to the local population. The paper uses county gazetteers to construct the cumulative number of SDYs assigned to each county. [E1]

## Why This Creates Empirical Variation

The variation exploited is the cross-county difference in SDY density, which generates differences in the intensity of exposure of rural children to educated urban youth during their school-age years. Children in counties that received more SDYs were more likely to be taught by educated youth, to interact with them as peers and role models, and to benefit from the knowledge and resources they brought. The identifying variation combines this cross-county intensity with cohort-level variation in exposure (different birth cohorts were at different ages during the movement). [E1; analytical inference]

## Identification Risks

The non-random assignment of SDYs to counties is the central identification challenge. More developed or more politically connected counties may have received more SDYs and also had better educational trajectories for reasons unrelated to SDY exposure. Conversely, counties with more educational disruption during the Cultural Revolution may have been targeted for more SDY placements. The paper addresses this through extensive controls, pre-trend analysis, and robustness checks, but residual confounding from unobserved county characteristics remains possible. Another concern is selective migration: families who valued education more may have moved to counties with more SDYs, or SDYs themselves may have differentially affected out-migration from treated counties. [E1; analytical inference]

## Data Requirements

The analysis requires county-level data on sent-down youth counts from historical records (primarily county gazetteers and provincial SDY archives). Educational outcomes come from the 1982, 1990, and 2000 population censuses and the 2005 mini-census, which provide individual-level data on educational attainment that can be aggregated to the county-cohort level. County-level socioeconomic controls (GDP, urbanization, distance to nearest city, etc.) are needed for balance tests and robustness. Historical data on the Cultural Revolution's local intensity (e.g., factional violence, school closure periods) can help address confound concerns. [E1]

## Evidence Notes

E1 is the published American Economic Review article by Chen, Fan, Gu, and Zhou. The paper finds that counties with a higher density of sent-down youths experienced significant improvements in rural children's educational outcomes, measured by years of schooling and junior high school completion. The effects are concentrated among cohorts that were of school age during the movement and are larger for girls and children from lower-income families. The paper provides extensive evidence on mechanisms, including SDYs serving as teachers and raising parental educational aspirations. Data construction is carefully documented, including the assembly of historical SDY records from county gazetteers.
