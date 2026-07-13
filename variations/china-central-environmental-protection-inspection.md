---
schema_version: 2
id: china-central-environmental-protection-inspection
name: China's Central Environmental Protection Inspection (CEPI) Rollout
aliases:
- CEPI
- Central Environmental Protection Inspection
- 中央环保督察
- 中央生态环境保护督察

status: extracted
provenance:
  task_id: task-2dd4b886e879
scope:
  country: China
  regions:
  - All provincial-level administrative units
  domains:
  - environment
  - regulation
  - enforcement
  - pollution
  - public-health
  - firm-behavior
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    The variation occurs in China and assigns exposure to Chinese provinces, cities,
    firms, and power plants. The staggered rollout of central environmental inspections
    provides a codable, policy-driven enforcement shock with direct relevance for
    pollution, public health, corporate environmental behavior, and local governance
    research.
identity:
  instrument: Rotating on-site environmental inspections dispatched by the central
    government to provincial-level jurisdictions
  authority: State Council / Ministry of Ecology and Environment (formerly Ministry
    of Environmental Protection)
  legal_identifiers:
  - Environmental Protection Inspection Plan (Trial), approved July 2015
  - State Council / MEE inspection team deployment notices (2016–2017)
  - Central Ecological and Environmental Protection Inspection Work Regulations (2025)
  implementation_regime: >
    A centrally designed campaign-style supervision system. Teams led by ministerial-
    level officials inspect provincial party committees and governments for about one
    month, review environmental law enforcement, accept public complaints, and require
    rectification. The first round covered all 31 provincial-level regions between late
    2015/early 2016 and September 2017; "look-back" inspections followed in 2018, and
    subsequent rounds began in 2019.
  assignment_mechanism: >
    The central leadership sets the timing and roster of inspections by province. Within
    each round, provinces are treated at different dates, creating staggered variation
    in when a province (and the firms and plants within it) come under central scrutiny.
    Treatment can be coded as the inspection month, the post-inspection rectification
    period, or an ever-inspected indicator, depending on the research design.
  parent: null
  related_variations:
  - china-pollution-information-disclosure
  - china-low-carbon-pilot-first-wave
  - china-water-regulation-enforcement
  - china-water-quality-monitoring-rd
  - china-huai-river-heating-air-pollution
  - china-heating-policy-air-pollution-wtp
timeline:
  announcement: '2015-07-01'
  effective: '2015-12-01'
  implementation_start: 2015
  implementation_end: ongoing
  local_timing: >
    The Environmental Protection Inspection Plan (Trial) was approved on 1 July 2015.
    A one-month pilot inspection took place in Hebei around December 2015 / January
    2016. The first formal batch inspected eight provinces (Inner Mongolia, Heilongjiang,
    Jiangsu, Jiangxi, Henan, Guangxi, Yunnan, Ningxia) in July–August 2016. The second
    batch (Beijing, Shanghai, Hubei, Guangdong, Chongqing, Shaanxi, Gansu) followed in
    November 2016; the third batch (Tianjin, Shanxi, Liaoning, Anhui, Fujian, Hunan,
    Guizhou) in April–May 2017; and the fourth batch (Jilin, Zhejiang, Shandong, Hainan,
    Sichuan, Qinghai, Xinjiang, Tibet) in August–September 2017. First-round full
    coverage was completed by September 2017. "Look-back" inspections occurred in 2018,
    and a second round ran from 2019 onward.
  anticipation: >
    The establishment of the inspection system was announced in mid-2015, so provincial
    governments could anticipate scrutiny in general terms. The exact batch and timing
    for each province were centrally determined and not fully predictable to local
    actors.
  last_verified: '2026-07-13'
assignment:
  unit: Province-year or plant-week/city-week depending on outcome frequency
  treated: >
    Provinces, cities, firms, or plants under active central inspection or in the
    post-inspection rectification period.
  comparison_pool: >
    Not-yet-inspected provinces, cities, firms, or plants in the same period, or the
    same units in pre-inspection periods.
  rule: >
    Code a province (or the units located in it) as treated in the year/month when a
    central inspection team is stationed there and, in some designs, in subsequent
    years if the inspection effect persists. The exact timing can be defined as the
    inspection window, the feedback/rectification date, or an indicator for having ever
    been inspected.
  intensity: >
    Binary at the province-year level in most designs; high-frequency designs code the
    active inspection window at the week or day level. Intensity can be refined by the
    number of public complaints, sanctioned officials, or rectification tasks reported.
  exemptions:
  - Xinjiang Production and Construction Corps and a few special administrative units
    may follow a separate schedule
  - Second-round inspections included State Council ministries and central SOEs
  compliance: >
    Provincial and local governments are required to cooperate; actual firm response
    varies (end-of-pipe device operation, output reduction, relocation, or temporary
    shutdown). Compliance is stronger during the inspection window and may revert
    afterward.
  exposure_construction: >
    Build a province-by-month or province-by-year panel of inspection dates from official
    deployment notices. Merge with outcome data by province and time. For high-frequency
    pollution designs, match plant-level pollution readings to the exact inspection
    window. For firm-level designs, assign firms to the province-year treatment.
  required_identifiers:
  - province code
  - calendar year or month
  - inspection round or batch
  spillovers: >
    Pollution and economic activity can shift temporarily across provincial or city
    borders during inspections. Stricter enforcement in one region may divert polluting
    activity to neighbors. Public-complaint channels create feedback loops that can
    affect which issues are recorded.
research_compatibility:
  outcome_domains:
  - air pollution
  - water pollution
  - firm environmental investment
  - corporate green innovation
  - energy use and carbon emissions
  - public health
  - labor productivity
  - tax compliance
  - local fiscal behavior
  - political accountability
  affected_populations:
  - residents of inspected provinces
  - manufacturing workers
  - coal-power plant operators
  - polluting firms
  - local officials
  - migrant workers
  mechanism_channels:
  - strengthened environmental enforcement
  - end-of-pipe abatement
  - output reduction
  - temporary plant closure
  - green investment
  - innovation response
  - intergovernmental accountability
  - public participation and complaints
  best_for:
  - Studies exploiting staggered provincial enforcement shocks
  - Outcomes measurable at province, city, firm, plant, or individual level with geographic
    and temporal identifiers
  - Research on campaign-style governance and regulatory enforcement
  not_good_for:
  - Long-run general-equilibrium effects without a clear post-treatment window
  - Outcomes that cannot be linked to province or inspection timing
  - Designs that cannot distinguish inspection effects from concurrent national pollution
    policies or seasonal factors
design:
  claim_type: causal
  affordances:
  - staggered provincial treatment timing
  - high-frequency pollution and plant-level data during inspection windows
  - repeated rounds and "look-back" inspections
  - public complaint and rectification data
  - heterogeneity by firm ownership, industry, and region
  candidate_designs:
  - staggered difference-in-differences at province-year or city-year level
  - event study around inspection dates
  - plant-week panel with inspection-window treatment
  - triple differences adding polluting vs. non-polluting firms
  - regression discontinuity at jurisdictional boundaries
  identifying_variation: >
    The central government's decision to send inspection teams to provinces at different
    dates within the first round (2016–2017), creating staggered variation in the timing
    of top-down environmental scrutiny.
  assumptions:
  - Inspection timing is conditionally independent of local outcome shocks
  - Not-yet-inspected provinces provide a valid counterfactual for inspected provinces
  - Pollution and economic spillovers across provinces are limited or can be modeled
  - Treatment definition (active window vs. post-inspection) matches the mechanism
  diagnostics:
  - Pre-trends in event-study plots
  - Robustness to staggered DID estimators (Callaway-Sant'Anna, Sun-Abraham)
  - Placebo tests using non-polluting firms or non-target pollutants
  - Sensitivity to treatment window width
  - Cross-border spillover tests
  primary_strategy: >
    Staggered difference-in-differences using province-year or plant-week panels, with
    fixed effects for unit and time and clustered standard errors at the province level.
  estimand: >
    The average effect of central environmental inspection exposure on the outcome of
    interest, conditional on parallel trends and limited spillovers.
  treatment_variable: >
    Province-year or province-month indicator equal to one when a central inspection is
    active or when the province has entered the post-inspection rectification phase.
  comparison_logic: >
    Inspected provinces vs. not-yet-inspected provinces before and after each province's
    inspection date.
  estimation_notes: >
    Include province and year fixed effects; add province-specific linear trends or
    economic controls where appropriate. For plant-level high-frequency data, use plant
    and week fixed effects and cluster by province. Use modern staggered DID estimators
    to avoid negative weights.
threats:
- type: endogenous-inspection-timing
  basis: inferred
  condition: >
    The central government may schedule inspections based on observed pollution severity,
    prior enforcement failures, or political considerations, creating selection on gains.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - test for correlation between inspection timing and pre-treatment outcomes
  - control for lagged pollution and enforcement measures
  - use entropy balancing or matching on observables
- type: spillovers-and-leakage
  basis: inferred
  condition: >
    Polluting activity may relocate temporarily to untreated provinces or cities during
    inspections, biasing intent-to-treat estimates downward and creating cross-border
    pollution effects.
  evidence_refs:
  - E3
  possible_diagnostics:
  - estimate effects in border counties or downwind regions
  - test for pollution increases in neighboring untreated areas
  - exclude border regions in robustness checks
- type: temporary-compliance
  basis: documented
  condition: >
    Some responses (e.g., running scrubbers, temporary shutdowns) occur only during the
    inspection window and revert afterward, so treatment effects may be short-lived.
  evidence_refs:
  - E3
  possible_diagnostics:
  - estimate dynamic effects during and after the inspection window
  - compare short-run and medium-run coefficients
  - examine mechanisms such as end-of-pipe device operation
- type: confounding-policies
  basis: inferred
  condition: >
    Concurrent national air-pollution action plans (e.g., the 2013 Air Pollution Prevention
    and Control Action Plan) and seasonal heating policies may overlap with inspection
    effects.
  evidence_refs:
  - E1
  - E3
  possible_diagnostics:
  - control for city-by-year or province-by-year policy intensity
  - include heating-season fixed effects for pollution outcomes
  - compare effects across pollutants and industries with different regulatory exposure
empirical_requirements:
  contract_version: 1
  population: Chinese provinces, cities, firms, power plants, or residents observed before
    and during the inspection rounds
  observation_unit: Province-year, city-year, firm-year, or plant-week
  geography_level: Province or city
  time_start: 2013
  time_end: 2020
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields:
  - outcome
  - province or city identifier
  - year or week
  - inspection date or batch
  - ownership / industry (for firm designs)
  - pollutant concentration or emissions (for pollution designs)
  required_identifiers:
  - province code
  - year
  treatment_key:
  - province code
  - inspection date
  treatment_source: >
    Official deployment notices from the State Council / Ministry of Ecology and Environment
    and provincial inspection-team entry/exit announcements. Outcome data from China
    City Statistical Yearbooks, firm databases (CSMAR/Wind), power-plant continuous
    emission monitoring systems, satellite or ground-monitor pollution data, and public
    health records.
  measurement_risks:
  - official inspection dates may differ from effective local enforcement dates
  - pollution monitors may be manipulated during inspections
  - firm-level environmental data are often self-reported
  - treatment timing for second-round and look-back inspections needs careful coding
  - province-year aggregation masks within-province heterogeneity
evidence:
- id: E1
  source_type: policy-document
  citation: >
    Ministry of Environmental Protection. 2015. "Central Deep Reform Group approves the
    Environmental Protection Inspection Plan (Trial)" (report on 2015-08-10).
  url: https://www.mee.gov.cn/xxgk/hjyw/201508/t20150810_307921.shtml
  date: '2015-08-10'
  supports:
  - identity
  - timeline
  - assignment
  verification_status: verified
  access_level: official-document
  locator: >
    MEE news report dated 10 August 2015; states that the Central Leading Group for
    Comprehensively Deepening Reform approved the Environmental Protection Inspection Plan
    (Trial) on 1 July 2015, establishing the central environmental inspection mechanism.
- id: E2
  source_type: policy-document
  citation: >
    State Council / Xinhua. 2016. "2016 First Batch of Central Environmental Protection
    Inspections Fully Launched" (published 2016-07-19).
  url: https://www.gov.cn/xinwen/2016-07/19/content_5092816.htm
  date: '2016-07-19'
  supports:
  - identity
  - timeline
  - assignment
  verification_status: verified
  access_level: official-document
  locator: >
    Gov.cn article dated 19 July 2016; lists the eight provinces in the first batch and
    confirms that inspections last about one month and target provincial party committees
    and governments.
- id: E3
  source_type: paper
  citation: >
    Karplus, Valerie J., Shuang Zhang, and Douglas Almond. 2023. "Dynamic Responses of
    SO2 Pollution to China's Environmental Inspections." Proceedings of the National
    Academy of Sciences 120 (17): e2214262120.
  url: https://doi.org/10.1073/pnas.2214262120
  date: 2023
  supports:
  - design_applications
  - assignment
  - design
  verification_status: reported
  access_level: full-text
  locator: >
    PNAS article; uses plant-week SO2 continuous emission monitoring data around the 2016–
    2017 inspections; staggered DID with modern estimators; reports large in-window
    reductions and post-inspection reversion.
- id: E4
  source_type: paper
  citation: >
    Wu, Jianxian. 2024. "The Sword of Damocles: Understanding the Carbon Abatement Effects
    of Top-Down Environmental Management Practices — Insights from China's Campaign-Style
    Governance." Journal of Environmental Management 352: 120306.
  url: https://doi.org/10.1016/j.jenvman.2024.120306
  date: 2024
  supports:
  - design_applications
  - assignment
  verification_status: reported
  access_level: full-text
  locator: >
    JEM article; city-year panel; staggered DID finding that inspected cities reduce carbon
    intensity and carbon emissions; triple-difference mechanism analysis.
- id: E5
  source_type: paper
  citation: >
    Dong, Yukai, Junrong Huang, and Yuhong Li. 2025. "Campaign-Style Enforcement and
    Corporate Environmental Governance: Evidence from China's Central Environmental
    Inspection." Frontiers in Public Health 13: 1688719.
  url: https://doi.org/10.3389/fpubh.2025.1688719
  date: 2025
  supports:
  - design_applications
  - assignment
  verification_status: reported
  access_level: full-text
  locator: >
    Sections 4.1–4.3 and Tables 1–2 define the 2012–2019 A-share sample (3,170 firm-year
    observations), the annual-report environmental-investment measure, and the CEI coding;
    Table 4 reports firm- and year-fixed-effects estimates for CEI × heavy-polluting industry.
design_applications:
- paper: 'Dynamic Responses of SO2 Pollution to China''s Environmental Inspections'
  doi: 10.1073/pnas.2214262120
  journal: Proceedings of the National Academy of Sciences
  year: 2023
  research_question: Do short-lived increases in centralized regulatory enforcement lead
    to lasting improvements in environmental performance at coal power plants?
  population: Coal-fired power plants in China, 2016–2017
  outcome: SO2 concentrations near power plants
  data_used:
  - Continuous emission monitoring system (CEMS) data for SO2
  - Central environmental inspection dates
  - plant and location identifiers
  treatment_encoding: Plant-week treatment indicator for being in a province under active
    central inspection
  comparison: Plants in not-yet-inspected provinces during the same weeks
  empirical_design: Staggered difference-in-differences at plant-week level using TWFE
    and modern staggered estimators
  assumptions:
  - inspection timing is exogenous to plant-level shocks
  - not-yet-inspected plants provide valid counterfactual
  - SO2 changes are driven by inspection-induced abatement or output changes
  threats_addressed:
  - staggered timing via modern estimators
  - alternative control groups
  - pre-trends in event-study plots
  evidence_refs:
  - E3
- paper: 'The Sword of Damocles: Understanding the Carbon Abatement Effects of Top-Down
    Environmental Management Practices'
  doi: 10.1016/j.jenvman.2024.120306
  journal: Journal of Environmental Management
  year: 2024
  research_question: What are the carbon abatement effects of China's central environmental
    inspections?
  population: Chinese cities, panel
  outcome: Carbon intensity and carbon emissions
  data_used:
  - China City Statistical Yearbook
  - central environmental inspection batch dates
  treatment_encoding: City-year dummy equal to one after the province receives a central
    inspection
  comparison: Cities in provinces not yet inspected
  empirical_design: Staggered difference-in-differences with city and year fixed effects;
    triple-difference mechanism analysis
  assumptions:
  - parallel trends across inspected and not-yet-inspected cities
  - no major spillover of emissions across provinces
  threats_addressed:
  - pre-trends
  - robustness to alternative specifications
  evidence_refs:
  - E4
- paper: 'Campaign-Style Enforcement and Corporate Environmental Governance: Evidence from
    China''s Central Environmental Inspection'
  doi: 10.3389/fpubh.2025.1688719
  journal: Frontiers in Public Health
  year: 2025
  research_question: How does campaign-style environmental enforcement affect corporate
    environmental investment, and how do government-business relations moderate the response?
  population: Nonfinancial Chinese A-share listed firms observed from 2012 to 2019; the final
    sample excludes ST/PT firms, missing observations, and firms with zero environmental
    investment throughout the sample, leaving 3,170 firm-year observations
  outcome: Environmental investment reported under construction in progress, divided by
    year-end total assets and multiplied by 100; environmental fines and subsidies are examined
    as mechanisms
  data_used:
  - Manually collected corporate environmental investment from the construction-in-progress
    section of listed-company annual reports
  - Manually collected first-round CEI province and inspection timing
  - CSMAR firm financials and governance controls
  - CRNDS environmental-penalty data and manually collected environmental subsidies
  - 2017 Ranking of Government-Business Relations in Chinese Cities close index
  treatment_encoding: CEI equals one beginning in the year the inspection team enters the
    firm's registered province and remains one afterward to represent continuing rectification
    and look-back supervision; the main regressor is CEI interacted with a heavy-polluting-industry
    indicator defined from the 2008 MEP directory and 2012 CSRC industry classification
  comparison: Differential change in environmental investment for heavy-polluting versus other
    listed firms as provinces enter the first CEI round at different times
  empirical_design: Staggered difference-in-differences with firm and year fixed effects and a
    CEI × heavy-polluting-industry treatment term; event-study and PSM-DID robustness checks
  assumptions:
  - environmental-investment trends for the comparison groups are parallel before provincial CEI arrival
  - no concurrent policy differentially changes heavy-polluting firms' investment at CEI timing
  - permanent post-entry coding reasonably represents continuing rectification and look-back exposure
  - sample exclusions do not generate differential composition changes around CEI arrival
  threats_addressed:
  - pre-trends and dynamic effects via event study
  - selection robustness via radius-matched PSM-DID
  - the 2018 Environmental Protection Tax Law as a concurrent policy
  evidence_refs:
  - E5
readiness_blockers:
- >
  The complete province-by-batch schedule for the first round and the exact dates of
  "look-back" and second-round inspections have not yet been verified from primary
  official notices inside this record.
- >
  Treatment definitions differ across studies (active inspection window, post-inspection
  year, ever-inspected indicator), so the appropriate coding depends on the research
  question.
- >
  High-frequency pollution designs require matching plant-level emissions data to exact
  inspection windows; the merge keys and data access restrictions are not documented here.
- >
  Concurrent national environmental policies (Air Pollution Action Plan, winter heating
  bans, emission standards) may confound the inspection effect and need to be modeled.
- >
  No replication package has been inspected to confirm the exact sample construction or
  treatment coding.
method_transfer: null
---
## Institutional Background

China's environmental enforcement historically suffered from weak local implementation because provincial and city officials faced stronger career incentives for economic growth than for environmental compliance. After severe air-pollution episodes in 2013, the central government shifted toward top-down, campaign-style oversight. The Environmental Protection Inspection Plan (Trial) approved in July 2015 created a system in which central teams, led by senior officials, inspect provincial party committees and governments, accept public complaints, and require rectification. [E1]

## What Changed

Between late 2015 and September 2017, all 31 provincial-level regions received a central environmental inspection. Each inspection lasted roughly one month and was followed by a public feedback report and a rectification plan. The staggered rollout means that at any point during 2016–2017 some provinces had already been inspected while others had not, generating variation in exposure to central scrutiny. [E1; E2]

## Implementation and Assignment

The State Council and the Ministry of Environmental Protection (now Ecology and Environment) determined the batch roster and timing. Firms, plants, and residents in a province become treated when the inspection team is on site and, in many designs, remain treated in subsequent years because rectification obligations persist. The control group consists of provinces that had not yet been inspected in the same period. [E1; E2; analytical inference]

## Why This Creates Empirical Variation

Inspections raise the expected cost of non-compliance for local officials and polluting firms, but only for a short and externally determined window. This creates a staggered enforcement shock that can be used to identify short-run abatement responses, enforcement spillovers, and real effects on firm investment, productivity, and public health. [E3; E4; E5]

## Identification Risks

Inspection timing may respond to pollution severity or political considerations. Polluting activity can relocate temporarily across borders, and some responses may revert after inspectors leave. Concurrent national policies such as the Air Pollution Prevention and Control Action Plan and winter heating restrictions overlap with the inspection period and must be controlled for. [E3; analytical inference]

## Data Requirements

Researchers need a province-by-batch roster of inspection dates from official notices, outcome data with province and time identifiers, and, for some designs, firm or plant identifiers. High-frequency pollution studies require continuous emission monitoring or air-quality data matched to the exact inspection window. [E3; E4; E5]

## Evidence Notes

E1 verifies the creation of the inspection system. E2 verifies the first batch's provinces and one-month duration. E3–E5 report empirical applications using the staggered rollout; their treatment coding and data construction have not yet been verified from replication materials.
