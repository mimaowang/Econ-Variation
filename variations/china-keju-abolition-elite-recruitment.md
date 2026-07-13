---
schema_version: 2
id: china-keju-abolition-elite-recruitment
name: The 1905 Abolition of China's Civil Service Examination (Keju) as a Shock to Elite Recruitment and Political Stability
aliases:
- Keju abolition 1905
- Bai Jia civil service exam
- 科举废除 精英选拔
- imperial examination abolition

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - 262 prefectures across China
  domains:
  - political-economy
  - history
  - education
  - institutions
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: The 1905 abolition of the keju (科举), China's 1,300-year-old civil service examination system, which eliminated
    the primary channel for elite recruitment and created a sudden loss of upward mobility prospects for educated elites across
    all prefectures
  authority: Qing imperial court (Empress Dowager Cixi)
  legal_identifiers:
  - 1905 Imperial Edict abolishing the civil service examination system
  implementation_regime: The abolition was a single national event in 1905, affecting all prefectures simultaneously; however,
    prefectures had different historical quotas (quotas) for entry-level exam candidates, creating cross-sectional variation
    in the intensity of the shock
  assignment_mechanism: The abolition was a top-down national decision; prefecture-level variation in exposure intensity is
    driven by historical quotas, which were set centuries earlier based on population and tax revenue
  parent: null
  related_variations: []
timeline:
  announcement: '1905-09-02'
  effective: '1905-09-02'
  implementation_start: 1905
  implementation_end: 1905
  local_timing: National single-date abolition; no subnational variation in timing
  anticipation: Reform discussions had occurred since the 1890s; the actual abolition in 1905 was relatively sudden
  last_verified: '2026-07-13'
assignment:
  unit: Prefecture
  treated: All prefectures after 1905 (common shock); treatment intensity varies with prefecture-level historical keju quotas
    (more quota places = more elites whose prospects were disrupted)
  comparison_pool: Pre-1905 period within each prefecture; cross-prefecture variation in quota intensity
  rule: Prefectures with higher historical quotas per capita experienced a larger shock because a larger share of the local
    elite population was affected by the loss of the examination channel
  intensity: Continuous — prefecture-level historical quota (number of shengyuan/xiucai degrees allocated) per capita
  compliance: The abolition was complete and irreversible; there was no non-compliance
  exposure_construction: Code all observations after September 1905 as post-abolition; interact post-abolition indicator with
    prefecture-level historical quota per capita (instrumented using number of small rivers)
  required_identifiers:
  - prefecture code
  - year
  - historical keju quota
  - number of small rivers (instrument)
  exemptions: []
  spillovers: Elites from high-quota prefectures who lost examination prospects may have migrated or mobilized politically,
    affecting neighboring areas
research_compatibility:
  outcome_domains:
  - political participation
  - revolution
  - elite mobility
  - education
  - modernization
  - political stability
  affected_populations:
  - Educated elites
  - examination candidates
  - gentry class
  - local political organizations
  mechanism_channels:
  - blocked upward mobility
  - elite grievances
  - human capital reallocation
  - political mobilization
  - revolutionary participation
  best_for:
  - Studying how institutional changes affecting elite recruitment influence political stability
  - historical natural experiments
  not_good_for:
  - Contemporary outcomes
  - short-run analysis
  - individual-level data (prefecture-level)
design:
  affordances:
  - sharp 1905 cutoff
  - cross-prefecture variation in historical quotas
  - pre/post abolition comparison
  - IV using river geography
  candidate_designs:
  - difference-in-differences (quota × post-1905)
  - instrumental variables using small rivers
  identifying_variation: The interaction of prefecture-level historical quotas with the post-1905 period, instrumented by
    the number of small rivers (which predict quota allocation due to exam hall capacity constraints)
  assumptions:
  - Quotas were set centuries before 1905 and are exogenous to 1905-era political outcomes
  - rivers predict quotas only through exam capacity
  - no other 1905-level shocks correlate with quotas
  diagnostics:
  - Test for relationship between quotas and pre-1905 outcomes
  - examine IV first stage and validity
  - compare with alternative historical instruments
  - test for other concurrent reforms
  primary_strategy: Difference-in-differences with continuous treatment intensity; IV using river geography as instrument
    for quotas
  estimand: The causal effect of the recorded exposure on Revolutionary participation, political protests, elite mobility
    patterns, conditional on the stated design assumptions.
  treatment_variable: Post-1905 indicator interacted with prefecture-level historical quota per capita; quota instrumented
    using number of small rivers
  comparison_logic: High-quota vs low-quota prefectures; pre-1905 vs post-1905
  estimation_notes: Difference-in-differences with continuous treatment intensity; IV using river geography as instrument
    for quotas
threats:
- type: other-concurrent-reforms
  basis: inferred
  condition: The late Qing period saw multiple modernization reforms (New Policies, constitutional movement); the keju abolition
    was part of a broader reform package
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for other reforms
  - use cross-prefecture variation that isolates keju-specific effects
  - compare timing of different reforms
empirical_requirements:
  contract_version: 1
  population: 262 Chinese prefectures observed before and after 1905
  observation_unit: Prefecture-year or prefecture-cohort
  geography_level: Prefecture
  time_start: 1880
  time_end: 1912
  minimum_frequency: annual or by historical period
  minimum_pre_periods: 10
  minimum_post_periods: 5
  required_fields:
  - prefecture code
  - year
  - historical keju quota
  - number of small rivers
  - political participation
  - revolutionary activity
  - elite outcomes
  required_identifiers:
  - prefecture code
  - year/period
  - quota measure
  treatment_key:
  - prefecture code
  - post-1905 indicator
  - quota per capita
  treatment_source: Historical gazetteers for keju quotas; GIS data for river geography; historical records for political
    participation and revolutionary activity
  measurement_risks:
  - historical data quality and completeness
  - prefecture boundary changes over time
  - quota measurement accuracy
  - political participation measurement from historical records
evidence:
- id: E1
  source_type: paper
  citation: 'Bai, Ying, and Ruixue Jia. 2016. "Elite Recruitment and Political Stability: The Impact of the Abolition of China''s
    Civil Service Exam." Econometrica 84 (2): 677–733.'
  url: https://doi.org/10.3982/ECTA13448
  date: 2016
  supports:
  - identity
  - assignment
  - design
  - quota analysis
  - IV construction
  - political stability outcomes
  verification_status: verified
design_applications:
- paper: 'Elite Recruitment and Political Stability: The Impact of the Abolition of China''s Civil Service Exam'
  doi: 10.3982/ECTA13448
  journal: Econometrica
  year: 2016
  research_question: How did the abolition of the keju examination system affect political stability in late Qing China?
  population: 262 Chinese prefectures, ~1880–1912
  outcome: Revolutionary participation, political protests, elite mobility patterns
  data_used: []
  treatment_encoding: Post-1905 indicator interacted with prefecture-level historical quota per capita; quota instrumented
    using number of small rivers
  comparison: High-quota vs low-quota prefectures; pre-1905 vs post-1905
  empirical_design: Difference-in-differences with continuous treatment intensity; IV using river geography as instrument
    for quotas
  assumptions:
  - Quotas are historically predetermined and exogenous to 20th-century outcomes
  - rivers affect outcomes only through exam quotas
  - no other 1905-level shocks confound
  threats_addressed:
  - quota endogeneity via river IV
  - concurrent reforms via prefecture-level controls and timing analysis
  - spatial spillovers via geographic controls
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
---
## Institutional Background
For 1,300 years, the keju examination system was the primary channel for elite recruitment and social mobility in imperial China. Passing the exams was the main route to government office, social prestige, and economic advantage. Each prefecture received an annual quota for the lowest-level degree (shengyuan/xiucai), creating a class of degree-holders whose status and life prospects depended on continued participation in the examination system. [E1]

## What Changed
In September 1905, the Qing court abruptly abolished the entire keju system. For the millions of men who had spent years or decades preparing for examinations, the abolition destroyed their career prospects overnight. The sudden elimination of this institutional channel for upward mobility is arguably one of the largest institutional shocks in human history. [E1]

## Implementation and Assignment
The 1905 abolition was a single national event. However, prefectures with higher historical quotas had more examination candidates relative to their population, and therefore experienced a larger shock to elite prospects. The variation in quotas — set centuries earlier based on population and tax revenue — provides cross-sectional variation in treatment intensity. Rivers serve as an instrument because the number of small rivers in a prefecture predicted its allocated quota (exam halls needed water transport for candidates). [E1]

## Why This Creates Empirical Variation
The common timing of abolition combined with cross-prefecture variation in quota intensity creates a difference-in-differences design. Prefectures with more degree-holders per capita experienced a larger shock. The river IV addresses the concern that quotas may have been correlated with other prefecture characteristics that independently affected political outcomes. [E1; analytical inference]

## Identification Risks
The late Qing period was one of profound change — military defeats, foreign incursions, reform movements, and revolutionary agitation. Isolating the keju abolition effect from these concurrent shocks requires the cross-sectional variation in quota intensity. If high-quota prefectures were already more politically volatile before 1905, the DID estimates may be confounded. [E1; analytical inference]
## Data Requirements

Prefecture-level data on historical keju quotas from Qing dynasty gazetteers, GIS data on river geography for the IV, historical records on revolutionary participation and political instability from county and prefecture gazetteers, and prefecture-level demographic and economic controls.[E1]

## Evidence Notes

E1 is the published Econometrica article. The paper documents that prefectures with higher keju quotas experienced significantly more revolutionary participation after 1905, that the effect operated through blocked elite mobility, and that the river-based IV strategy supports a causal interpretation.
