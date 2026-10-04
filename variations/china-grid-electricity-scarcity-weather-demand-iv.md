---
schema_version: 2
id: china-grid-electricity-scarcity-weather-demand-iv
name: China Regional-Grid Electricity Scarcity and Weather Demand Instruments, 1999-2004
aliases:
- Fisher-Vanden Mansur Wang electricity shortages and firm productivity
- China thermal generation capacity factor and degree-day IV
- 中国区域电网电力短缺 制冷供暖度日工具变量
status: grounded
provenance:
  task_id: task-20265183a742
scope:
  country: China
  regions: [Mainland China in six regional electricity grids; Tibet excluded]
  domains: [development-economics, firm-economics, industrial-organization, regional-economics, energy-economics, infrastructure]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    Chinese industrial enterprises faced different annual degrees of electricity
    scarcity across regional grids. Fisher-Vanden, Mansur and Wang use this
    exposure, instrumented by grid-level heating and cooling degree days, to
    study production costs and input substitution in 1999-2004. The recorded
    mechanism is weather-driven demand pressure on constrained electricity
    supply. It is distinct from precipitation-driven hydropower supply shocks.
identity:
  instrument: >
    Annual regional-grid thermal generation divided by thermal installed
    capacity measures electricity scarcity; its logarithm is instrumented by
    annual cooling and heating degree days around 65 degrees Fahrenheit
    (about 18.3 degrees Celsius), with interactions needed for the cost model.
    The endogenous exposure measures shortage risk, not observed firm outage
    hours or a binary policy treatment.
  authority: >
    Weather has no assignment authority. Government authorities and grid
    operators allocate constrained supply and manage loads. The authors
    construct scarcity from China Electricity Yearbook generation and capacity
    statistics and instruments from NOAA/NCDC hourly surface temperatures.
  legal_identifiers:
  - '国办发〔2004〕47号, 国务院办公厅关于做好电力迎峰度夏工作的通知; contemporaneous institutional evidence, not the instrument'
  - 'JDE application DOI: 10.1016/j.jdeveco.2015.01.002'
  implementation_regime: >
    Under constrained capacity and regulated electricity supply, local
    authorities used load shifting and selective curtailment. The 2004 State
    Council notice protected essential users and favored certain enterprises,
    instructed authorities to rank other users, and restricted high-energy,
    low-output or disfavored activities. That notice verifies an observed
    study-period regime; it does not establish identical rules in every grid
    or every year of 1999-2004.
  assignment_mechanism: >
    Enterprises inherit their historical regional grid's annual scarcity.
    Hotter and colder days raise electricity demand, shifting grid scarcity
    when capacity is constrained. Actual firm curtailment remains selective.
    The research comparison relies on differential annual grid weather after
    fixed effects and covariates, with a separate exclusion assumption that
    this weather does not directly change industrial costs or output.
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 1999
  implementation_end: 2004
  local_timing: >
    The application observes firms and grid exposure annually in 1999-2004.
    Shortages intensified in the early 2000s; the national 2004 notice
    documents electricity and fuel constraints and selective summer load
    management. There is no common treatment start year for this continuous
    exposure. Reconstruct weather separately for every grid-year.
  anticipation: >
    The authors study responses to shortage risk, including changes made
    before a firm actually loses power. Annual exposure combines forecastable
    seasonal demand and realized weather; it is not an unexpected outage event.
  last_verified: '2026-10-03'
assignment:
  unit: Firm-year, with scarcity and weather instruments measured at regional-grid-year level.
  treated: Enterprises exposed to relatively high thermal generation-to-capacity ratios in their grid-year.
  comparison_pool: >
    The same enterprises in other observed years and enterprises in other
    grids, conditional on firm and industry-year effects in the cost equation.
    There is no permanently untreated grid. The factor-share equations in
    the joint system do not contain firm effects; singleton firms can affect
    joint estimates through cross-equation restrictions.
  rule: >
    Join a firm's location to its historical grid and year. Let S_gt be thermal
    generation divided by thermal capacity. Average station temperature to
    a daily grid temperature as described by the authors, then sum
    max(T_gd-65F,0) and max(65F-T_gd,0) within each year for CDD and HDD.
    Instrument log(S_gt), accounting for its interactions with input prices
    and log output. The manuscript's Equation 4 and Table 4 note differ on
    the precise weather polynomial; exact reproduction needs that reconciliation.
  intensity: Continuous log scarcity; CDD and HDD are grid-year demand shifters, not counts of actual outages.
  exemptions:
  - Tibet is outside the six-grid dataset; Taiwan is also excluded in the paper and outside this campaign.
  - Electricity-generation enterprises are excluded from the industrial-response estimation.
  - Firms with missing covariates or reported input-price outliers are removed under the paper's sample rules.
  compliance: >
    The 2004 official notice orders differentiated supply: essential users
    and favored firms receive protection, while other users are ranked for
    restrictions. A common grid exposure therefore does not imply a common
    firm outage. The authors prefer an aggregate scarcity proxy partly to
    avoid conditioning on selectively allocated firm blackouts.
  exposure_construction: >
    Six historical grids: Central, East, North, Northeast, Northwest and South.
    China Electricity Yearbook thermal generation and capacity produce an
    annual scarcity measure. NOAA/NCDC station temperatures produce annual
    grid CDD/HDD. The manuscript explains the aggregation order but provides
    no inspected station roster, averaging weights or complete firm-grid
    crosswalk. Year-invariant conversion of capacity to available annual
    energy changes the level of log scarcity, not its within-grid time variation.
  required_identifiers: [firm_id, year, firm_location, historical_grid_id, weather_station_id, station_date]
  spillovers: >
    Outsourcing can shift intermediate production toward firms in other
    provinces. The paper examines neighbors' scarcity with inverse-distance
    province weights and input-output relationships. This is evidence of a
    potential transmission channel; grid comparisons need not satisfy no
    interference across firms or regions.
research_compatibility:
  outcome_domains: [production costs, input substitution, firm productivity, outsourcing, self-generation]
  affected_populations: [Large mainland Chinese industrial energy users observed in the NBS financial and energy surveys]
  mechanism_channels: [Weather-driven electricity demand, constrained supply, selective load management, substitution toward purchased materials]
  best_for:
  - Studies of how supply reliability changes industrial costs and production organization with firm-level input expenditure and quantity data.
  - Regional infrastructure questions where grid exposure and weather can be linked to Chinese enterprises over time.
  not_good_for:
  - Estimating the effect of a specific number of firm blackout hours; that exposure is not observed here.
  - A nationwide post-2002 DID or an assumed randomized rationing schedule.
  - Outcomes directly sensitive to heat or cold unless a credible exclusion argument survives those channels.
design:
  claim_type: causal
  affordances: [Repeated grid scarcity, Weather demand first stage, Joint cost and factor-share outcomes]
  candidate_designs: [SUR with an IV first stage for scarcity, Firm-panel IV for explicitly measured self-generation outcomes]
  identifying_variation: >
    Weather-driven annual variation in thermal capacity utilization across
    grids after fixed effects, rather than economic-demand variation taken
    as exogenous. Industrial demand could otherwise jointly determine both
    production and grid scarcity.
  primary_strategy: >
    The author manuscript estimates a translog production-cost equation
    jointly with factor cost-share equations. It predicts scarcity with
    CDD/HDD and weather interactions, substitutes fitted scarcity and
    associated interactions into the SUR system, and imposes symmetry and
    price-homogeneity restrictions. This is the reported SUR-IV procedure;
    it is not a simple binary-treatment two-stage DID.
  estimand: >
    Changes in industrial production costs and factor shares induced by
    electricity scarcity, holding output and included factor prices fixed
    under the cost-model assumptions. It does not separately identify the
    causal effect of measured firm outage duration or of the 2004 notice.
  treatment_variable: log of annual grid thermal generation divided by thermal installed capacity, with cost-model interactions.
  comparison_logic: >
    Compare firm costs and input shares under different grid-year scarcity,
    conditional on firm effects in the cost equation and industry-year
    controls. Aggregate weather instruments isolate a demand-pressure
    component only if their direct industrial channels can be excluded.
  estimation_notes: >
    The manuscript reports a first-stage F of 12.4 with grid-year clustering
    versus 1293 under independent errors. The main system table does not
    clearly document corresponding shock-level inference or uncertainty from
    generated regressors. Only six grids and six years underlie the exposure.
    The authors use fixed effects after proposed output-demand instruments
    prove weak; this does not itself establish exogenous output. Several
    cost-function restrictions fail Wald tests but are retained theoretically.
  assumptions:
  - CDD/HDD affect industrial costs and output through electricity scarcity after included controls, without direct heat/cold productivity effects.
  - The cost-function and factor-share restrictions are adequate, and residual output and input-price endogeneity do not drive the estimates.
  - Historical grid matching and weather aggregation measure the relevant supply market consistently.
  diagnostics:
  - Reassess first-stage strength and inference at the small number of actual weather and grid shocks.
  - Inspect direct temperature channels and whether any controls would eliminate the identifying weather variation.
  - Compare alternative scarcity measures, leave-one-grid-out results and balanced-panel estimates.
  - Check changing survey coverage, especially the 2004 census expansion, and test exposure-related sample selection.
threats:
- type: weather_exclusion
  basis: reported
  condition: The authors acknowledge direct temperature effects on workers and argue they are secondary; this claim does not verify exclusion for another outcome.
  evidence_refs: [E1]
  possible_diagnostics: [Outcome-specific direct-weather checks, Sensitivity to alternative weather specifications and exposure windows]
- type: selective_curtailment
  basis: documented
  condition: Official 2004 rules differentiate users by essential status, industrial policy, output and energy intensity; grid scarcity is not randomized firm outage exposure.
  evidence_refs: [E2]
  possible_diagnostics: [Compare supported and restricted industries, Use observed curtailment schedules when the question concerns realized outages]
- type: few_grid_shocks
  basis: inferred
  condition: Many firm observations share only six grids over six years; firm-level sample size cannot establish precise shock-level inference.
  evidence_refs: [E1]
  possible_diagnostics: [Grid-level sensitivity and suitable small-cluster inference, Account for first-stage fitted exposure uncertainty]
- type: sample_and_model_dependence
  basis: reported
  condition: Energy-use and sales thresholds create changing nonrandom survey inclusion; joint cost/share estimates depend on restrictions and potentially endogenous output.
  evidence_refs: [E1]
  possible_diagnostics: [Balanced-panel and census-exclusion checks, Alternative specifications with credible output-demand controls]
empirical_requirements:
  contract_version: 1
  population: Mainland industrial enterprises in the 1999-2004 NBS financial and energy samples, excluding generators and Tibet.
  observation_unit: firm-year
  geography_level: historical regional electricity grid linked from firm location
  time_start: 1999
  time_end: 2004
  minimum_frequency: annual
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields:
  - Annual firm production costs, real gross output, wages and employment, fixed assets, materials, purchased electricity and other energy expenditures/quantities.
  - Annual thermal electricity generation and installed capacity by historical grid, with consistent units.
  - Hourly station temperatures, station locations and daily coverage to construct annual grid CDD/HDD at 65F.
  - Firm locations and the historical province-to-grid membership, industry and year controls, and industry materials-price information.
  required_identifiers: [firm_id, year, firm_location, historical_grid_id, weather_station_id, station_date]
  treatment_key: [historical_grid_id, year]
  treatment_source: China Electricity Yearbook thermal generation/capacity plus author-constructed NOAA/NCDC degree-day instruments.
  measurement_risks:
  - NBS enterprise and energy files require lawful access and a stable firm crosswalk; availability was not established in this task.
  - The manuscript reports 22902 firms and 36943 observations in its main sample, while Appendix A1 lists 23865 firms for the main column; use Table 1/main text until reconciled.
  - Station selection, grid averaging weights and historical grid membership must be documented before coding; current grid borders cannot be assumed valid for 1999-2004.
  - The generation/capacity proxy omits outage timing, duration and within-grid selective allocation.
evidence:
- id: E1
  source_type: paper
  citation: Fisher-Vanden, Karen, Erin T. Mansur and Qiong (Juliana) Wang. Electricity Shortages and Firm Productivity; author revised manuscript dated 27 October 2014, linked from Mansur's research page.
  url: https://mansur.host.dartmouth.edu/papers/fisher-vanden_mansur_wang_blackouts.pdf
  date: '2014-10-27'
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.local_timing
  - timeline.anticipation
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.exemptions
  - assignment.exposure_construction
  - assignment.required_identifiers
  - assignment.spillovers
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - design.assumptions
  - design.diagnostics
  - empirical_requirements.population
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_source
  - empirical_requirements.measurement_risks
  - design_applications.data_used
  - design_applications.treatment_encoding
  - design_applications.empirical_design
  verification_status: reported
  access_level: full-text
  locator: >
    Fetched in memory and text-extracted 2026-10-03 (63-page PDF).
    Cover date; Sections 2/4/5/6, PDF pp5-6,11-21,24-37;
    Table1 p46, Table4 p49, AppendixA1-A6 pp55-58. Establishes the
    inspected manuscript's sample, scarcity construction, weather IV,
    cost-system specification and reported checks. Does not certify the
    underlying restricted data or equivalence of every detail to the final
    2015 typeset article. Equation4/weather-interaction description and
    Table4 note (quadratic degree days) are not fully reconciled.
- id: E2
  source_type: policy-document
  citation: State Council General Office. Notice on electricity supply during the summer peak, 国办发〔2004〕47号, reproduced in the Fujian government gazette.
  url: https://zfgb.fujian.gov.cn/6845
  date: '2004'
  supports:
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.local_timing
  - assignment.compliance
  verification_status: verified
  access_level: official-document
  locator: >
    Full official reproduction inspected 2026-10-03, title/document number,
    introduction and Section1 (selective protection, ranked curtailment and
    peak shifting), Section2 (differential prices), Section3 (regional
    dispatch), Sections6-7 (capacity and conservation). Establishes actual
    2004 shortages and discretionary supply management; does not assign the
    paper's thermal ratio, weather instrument or full 1999-2004 grid roster.
- id: E3
  source_type: official-data
  citation: NOAA NCEI. Global Hourly Integrated Surface Database (ISD), official product documentation.
  url: https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database
  date: '2026-10-03'
  supports: [identity.authority, assignment.exposure_construction, empirical_requirements.required_fields]
  verification_status: verified
  access_level: official-document
  locator: >
    Product description, Global Hourly, Global Summary of the Day and
    Coverage inspected 2026-10-03. Confirms station-based hourly/synoptic
    surface temperature observations and daily summaries, with station
    coverage gaps. Does not establish the authors' exact archive release,
    chosen stations, grid averaging weights or instrument coding.
- id: E4
  source_type: other
  citation: Crossref publisher-deposited record for Fisher-Vanden, Mansur and Wang, Journal of Development Economics 114 (May 2015), 172-188.
  url: https://doi.org/10.1016/j.jdeveco.2015.01.002
  date: '2015'
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: >
    DOI identity linked here; publisher-deposited metadata directly inspected
    2026-10-03 through https://api.crossref.org/works/10.1016/j.jdeveco.2015.01.002
    for DOI, title, authors, journal, volume114, pages172-188 and published
    date-parts [2015,5]. This is metadata access, not inspection of the final
    publisher full text.
design_applications:
- paper: "Electricity shortages and firm productivity: Evidence from China's industrial firms"
  doi: 10.1016/j.jdeveco.2015.01.002
  journal: Journal of Development Economics
  year: 2015
  research_question: How do Chinese industrial enterprises adjust production costs and inputs when grid electricity becomes scarce?
  population: 22902 enterprises and 36943 firm-years in the inspected manuscript's 1999-2004 combined financial/energy sample.
  outcome: Production costs and five factor cost shares; supplementary self-generation and neighboring supplier-output outcomes.
  data_used:
  - NBS firm financial survey and energy-use survey/census, 1999-2004.
  - China Electricity Yearbook regional thermal generation and capacity.
  - NOAA/NCDC hourly station temperatures aggregated to grid-year degree days.
  - NBS industry materials-price statistics; input-output shares and province distances for the supplementary outsourcing test.
  treatment_encoding: Log thermal generation/capacity at grid-year level, instrumented by CDD/HDD and model interactions; weather polynomial requires reconciliation of Equation4 and Table4 note.
  comparison: Repeated firm and cross-grid annual variation conditional on firm effects in the cost equation and industry-year controls.
  empirical_design: Author manuscript SUR-IV cost/share system; supplementary firm-panel IV specifications for self-generation and supplier responses.
  assumptions: [Weather exclusion from direct production channels, Adequate cost-model restrictions and output controls, Consistent historical grid matching]
  threats_addressed: [Scarcity endogeneity and measurement error through weather instruments, Sample composition and alternative scarcity measures through robustness checks, North/East grid dependence through exclusions]
  evidence_refs: [E1, E2, E3, E4]
method_transfer: null
readiness_blockers:
- Confirm the weather polynomial and interacted first-stage coding against final methods or replication code; the inspected author manuscript has inconsistent Equation4 and Table4 descriptions.
- Rebuild and document the historical firm/grid and station/grid crosswalks; the inspected sources do not supply those rosters or station weights.
- Establish lawful access and stable joins for the NBS financial and energy microdata; reconcile the AppendixA1 firm-count discrepancy for exact reproduction.
- Defend outcome-specific weather exclusion and inference with six regional grids; publication and first-stage significance do not settle these conditions.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Electricity reliability can change how firms organize production even before a
blackout occurs. The inspected manuscript describes rapidly growing industrial
demand meeting constrained capacity in the early 2000s [E1, reported claim].
The 2004 State Council notice independently documents tight electricity and fuel
supply and directs selective curtailment, price changes and load shifting [E2].
The empirical object is this regional scarcity exposure over time; the notice
provides institutional context rather than a common policy adoption date.

## What Changed

Annual electricity supply pressure differed across six regional grids during
1999-2004. The authors encode that pressure with thermal generation divided by
thermal installed capacity, and use hot and cold weather as demand shifters
[E1, reported claim]. The ratio captures a threat to reliable supply. It cannot
tell a researcher whether a particular factory lost electricity for two hours,
changed its shift schedule or received priority protection.

## Implementation and Assignment

A firm receives its grid-year exposure through its historical location. CDD and
HDD sum daily deviations above and below 65F after constructing daily grid
temperature [E1, reported claim]. This makes the grid-year crosswalk and weather
aggregation indispensable. Actual curtailment is selective: the official notice
protects some users and limits others according to their characteristics [E2].
Consequently, treating the scarcity proxy as assigned firm blackout hours would
change the research question and misrepresent the institution [analytical inference].

## Why This Creates Empirical Variation

Unobserved regional growth raises both industrial activity and electricity
demand, so a raw scarcity regression is vulnerable to reverse causality. Weather
provides a proposed demand shifter. The manuscript combines its first-stage
fitted scarcity with a cost and factor-share system to study substitution toward
materials, conditional on its model and exclusion assumptions [E1, reported
claim]. An application to innovation, employment or emissions must explain why
temperature would affect that outcome only through scarcity; the published use
does not supply that explanation automatically.

## Identification Risks

Direct weather effects on workers and production are an acknowledged exclusion
concern. Selective rationing is documented, and outsourcing allows exposure in
one region to affect production elsewhere [E1, reported claim; E2]. Inference
must reflect the small number of shared grid shocks, rather than the many firm
observations [analytical inference]. Changing survey inclusion and cost-model
restrictions also matter: the main cost equation and factor-share equations
use different fixed-effect structures, so singleton firms are not simply
irrelevant to the jointly restricted estimates [E1, reported claim].

## Data Requirements

Join annual firm financial and energy observations by a stable firm identifier,
then attach historical grid membership and annual generation/capacity. Build
grid-year CDD/HDD from station temperatures with documented station selection,
coverage handling and averaging weights. NOAA verifies that suitable surface
temperature observations and daily summaries exist, but it does not verify the
paper's aggregation [E1, reported claim; E3]. The companion data repository can
document acquisition paths; this record specifies the fields and joins needed
to assess feasibility.

## Evidence Notes

The research source is an accessible author revised manuscript dated 27 October
2014; publication identity is independently confirmed for the 2015 JDE article
[E1, E4]. The final typeset full text and replication code were not inspected.
The manuscript leaves two reproduction ambiguities: Equation4 and Table4 give
different descriptions of weather functions, and AppendixA1 reports a different
main-sample firm count from Table1. These are preserved as conditions, together
with the missing station weights and crosswalks. The institutional notice
verifies 2004 load-management practice, while NOAA verifies the temperature
source's capabilities. Neither source validates exclusion or claims identical
allocation rules for every year [E2, E3].
