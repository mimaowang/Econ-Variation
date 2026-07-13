---
schema_version: 2
id: china-pollution-information-disclosure
name: China's 2013 Real-Time Air Quality Monitoring and Public Disclosure Program
aliases:
- Air pollution monitoring disclosure China
- From Fog to Smog
- Barwick Li Lin Zou pollution information
- 空气污染实时公开

status: extracted
provenance:
  task_id: task-164ccc1cb13e
scope:
  country: China
  regions:
  - Major cities with newly installed monitoring stations
  domains:
  - environment
  - health
  - information
  - household-behavior
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: China's 2013 landmark program rolling out real-time automated air quality monitoring stations with public online
    disclosure, replacing the previous manually-reported Air Pollution Index (API) with the more comprehensive and automated
    Air Quality Index (AQI)
  authority: Ministry of Environmental Protection
  legal_identifiers:
  - Air Pollution Prevention and Control Action Plan (2013)
  - MEP regulations on real-time AQI disclosure
  implementation_regime: Automated monitoring stations were rolled out across major Chinese cities starting in 2013; the key
    innovation was eliminating human manipulation of pollution data by automating measurement and publicly disclosing results
    in real time
  assignment_mechanism: City-level rollout timing of automated monitoring stations
  parent: null
  related_variations:
  - china-huai-river-heating-air-pollution
timeline:
  announcement: '2013-01-01'
  effective: null
  implementation_start: 2013
  implementation_end: 2015
  local_timing: Stations were rolled out on a staggered schedule across cities
  anticipation: The program was announced as part of the 2013 Air Pollution Action Plan; households could not anticipate specific
    local monitoring timing
  last_verified: '2026-07-13'
assignment:
  unit: City and individual household
  treated: Residents of cities after automated real-time AQI monitoring and disclosure begins
  comparison_pool: Same cities before monitoring rollout; cities not yet covered by the program
  rule: City-level timing of automated monitoring station installation and data disclosure
  intensity: All residents in a treated city have access to real-time AQI data; behavioral response intensity varies with
    baseline pollution and income
  exposure_construction: Code city-month as treated after automated monitoring starts; use panel data on household defensive
    behaviors (mask purchases, air purifier purchases, outdoor activity, online search behavior)
  required_identifiers:
  - city code
  - month/year
  - monitoring start date
  exemptions: []
  compliance: Not applicable — universal coverage
  spillovers: Information about pollution in one city may affect behavior in neighboring cities; nationwide increases in pollution
    awareness (media coverage) may amplify local treatment effects
research_compatibility:
  outcome_domains:
  - defensive expenditure
  - health
  - mortality
  - avoidance behavior
  - information demand
  - air purifier purchases
  - mask usage
  affected_populations:
  - Urban residents
  - higher-income households with greater capacity for defensive investment
  mechanism_channels:
  - pollution information provision
  - awareness increase
  - defensive behavior
  - avoidance
  - mortality reduction
  best_for:
  - Studying the value of environmental information
  - how households respond to new information about health risks
  not_good_for:
  - Estimating the direct health effect of pollution reduction itself
  - outcomes in rural areas without monitoring coverage
design:
  affordances:
  - staggered city-level rollout of automated monitoring
  - pre/post comparison
  - real-time high-frequency data on behavior
  candidate_designs:
  - staggered difference-in-differences
  - event study around monitoring station activation
  identifying_variation: City-specific timing of transition from manual to automated, publicly disclosed real-time AQI monitoring
  assumptions:
  - Station rollout timing is exogenous to local health conditions
  - behavioral responses reflect causal effects of information rather than concurrent trends
  diagnostics:
  - Test for pre-trends in defensive behaviors
  - compare cities with different rollout timing
  - analyze intensity of behavioral response by baseline pollution levels
  primary_strategy: Staggered difference-in-differences; event study; analysis of defensive behavior responses by pollution
    levels
  estimand: The causal effect of the recorded exposure on Defensive expenditures (air purifiers, masks), avoidance behavior
    (outdoor time), mortality, conditional on the stated design assumptions.
  treatment_variable: City-level staggered timing of automated real-time monitoring station activation
  comparison_logic: Within-city pre/post monitoring; across-city comparison by rollout timing
  estimation_notes: Staggered difference-in-differences; event study; analysis of defensive behavior responses by pollution
    levels
threats:
- type: concurrent-policy-changes
  basis: inferred
  condition: The monitoring program was part of the broader 2013 Air Pollution Action Plan, which also included emission reduction
    measures
  evidence_refs:
  - E1
  possible_diagnostics:
  - separate information effects from pollution-reduction effects
  - use within-city variation in pollution levels conditional on policy timing
empirical_requirements:
  contract_version: 1
  population: Urban residents in Chinese cities, 2011–2018
  observation_unit: City-month or individual-survey wave
  geography_level: City
  time_start: 2011
  time_end: 2018
  minimum_frequency: monthly
  minimum_pre_periods: 12
  minimum_post_periods: 12
  required_fields:
  - city AQI/PM2.5 data
  - monitoring station rollout dates
  - household defensive behavior measures
  - online search data
  - mortality data
  required_identifiers:
  - city code
  - month/year
  - monitoring station status
  treatment_key:
  - city code
  - post-automated-monitoring indicator
  - baseline pollution level
  treatment_source: MEP air quality monitoring data, e-commerce transaction data for masks/filters, Baidu search index data,
    China Mortality Surveillance System
  measurement_risks:
  - automated AQI differs systematically from previous API
  - making pre/post pollution comparisons difficult; online search and purchase data may not capture all defensive behaviors
evidence:
- id: E1
  source_type: paper
  citation: 'Barwick, Panle Jia, Shanjun Li, Liguo Lin, and Eric Yongchen Zou. 2024. "From Fog to Smog: The Value of Pollution
    Information." American Economic Review 114 (5): 1338–1381.'
  url: https://doi.org/10.1257/aer.20200956
  date: 2024
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - defensive behavior analysis
  - mortality impact
  verification_status: verified
design_applications:
- paper: 'From Fog to Smog: The Value of Pollution Information'
  doi: 10.1257/aer.20200956
  journal: American Economic Review
  year: 2024
  research_question: What is the value of providing real-time, accurate pollution information to the public?
  population: Urban residents in Chinese cities, ~2011–2018
  outcome: Defensive expenditures (air purifiers, masks), avoidance behavior (outdoor time), mortality
  data_used: []
  treatment_encoding: City-level staggered timing of automated real-time monitoring station activation
  comparison: Within-city pre/post monitoring; across-city comparison by rollout timing
  empirical_design: Staggered difference-in-differences; event study; analysis of defensive behavior responses by pollution
    levels
  assumptions:
  - rollout timing exogenous
  - behavioral responses causally linked to information
  - data accurately capture behavioral changes
  threats_addressed:
  - concurrent policies via staggered design and event study
  - selection via pre-trend tests
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
---
## Institutional Background
Before 2013, China reported air pollution using the Air Pollution Index (API), which was manually collected and susceptible to local manipulation. Officials could and did underreport pollution to meet targets. In 2013, following highly publicized "airpocalypse" episodes, the central government launched automated real-time monitoring with public online AQI disclosure. [E1]

## What Changed
The program eliminated the principal-agent problem in pollution reporting. Automated monitors could not be manipulated, and real-time public disclosure meant citizens instantly knew when their air was polluted. This transformed households' information environment — they moved from systematically understated pollution data to accurate, continuously available measurements. [E1]

## Why This Creates Empirical Variation
The staggered rollout of automated monitoring stations across cities creates a difference-in-differences design. Before automated monitoring, households in all cities had similarly biased information. After automated monitoring arrives in a city, households gain access to truthful pollution data and change their defensive behavior accordingly. [E1; analytical inference]

## Identification Risks
The monitoring rollout was part of a broader pollution control effort. Separating the information channel from the pollution-reduction channel requires careful design. The paper uses the fact that behavioral responses (information-seeking, defensive purchases) respond immediately to monitoring, while actual pollution reductions take longer to materialize. [E1]
## Implementation and Assignment

The staggered rollout of automated monitoring stations creates a difference-in-differences design. The central government mandated the program, but installation and activation occurred on a city-by-city basis, creating temporal variation in when residents gained access to truthful, real-time pollution data.[E1]

## Data Requirements

City-level AQI/PM2.5 data from MEP monitoring stations, monitoring station rollout dates by city, household-level defensive behavior data (air purifier and mask purchases from e-commerce platforms), Baidu search index data, mortality data from China Mortality Surveillance System, and weather controls.[E1]

## Evidence Notes

E1 documents large behavioral responses to pollution information: increased defensive expenditures, reduced outdoor activity, reduced mortality, and that the program's health benefits outweigh costs by an order of magnitude.
