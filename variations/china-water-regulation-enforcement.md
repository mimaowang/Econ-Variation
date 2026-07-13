---
schema_version: 2
id: china-water-regulation-enforcement
name: Spatial Discontinuity in Environmental Regulation Enforcement at Water Monitoring Stations in China (2003–2014)
aliases:
- He-Wang-Zhang water regulation
- monitoring station spatial RD
- 河流监测环境规制

status: deprecated
provenance:
  task_id: task-27815780789b
scope:
  country: China
  regions:
  - All provinces
  - major river basins
  domains:
  - environmental-economics
  - regulation
  - political-economy
  - firm
  - productivity
  - governance
  variation_type: boundary-discontinuity
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: Spatial regression discontinuity at water quality monitoring stations, where firms immediately upstream face
    stricter enforcement than firms immediately downstream due to the design of China's water monitoring system
  authority: Ministry of Environmental Protection (MEP), provincial Environmental Protection Bureaus
  legal_identifiers:
  - Water Pollution Prevention and Control Law
  - national water quality monitoring network
  - environmental target responsibility system
  implementation_regime: China's water quality monitoring stations measure upstream water quality at fixed locations; local
    officials face career consequences based on measured water quality readings, creating incentives to enforce standards
    upstream while tolerating violations downstream
  assignment_mechanism: Assignment to strict enforcement is determined by whether a polluting firm is located immediately
    upstream (within 30 km) of a water quality monitoring station versus immediately downstream
  parent: null
  related_variations: []
timeline:
  announcement: '2003-01-01'
  effective: null
  implementation_start: 2003
  implementation_end: 2014
  local_timing: The water quality monitoring system was established nationally in 2003; enforcement effects at monitoring
    stations persisted through the study period
  anticipation: The monitoring system was announced as part of a broader environmental reforms; firms may not have immediately
    understood the upstream-downstream asymmetry
  last_verified: '2026-07-13'
assignment:
  unit: Polluting firm (water-polluting industries)
  treated: Firms located within 30 km upstream of a water quality monitoring station
  comparison_pool: Firms located within 30 km downstream of the same monitoring stations; firms farther from monitoring stations
  rule: A firm is treated if it is upstream of a monitoring station within a narrow bandwidth; the comparison group is downstream
    firms at the same river segment
  intensity: Binary (upstream vs downstream within 30 km); alternative specifications use distance from monitoring station
  exemptions: []
  compliance: Local governments enforce stricter standards upstream, but compliance is imperfect; some downstream firms temporarily
    reduce emissions when monitoring is anticipated
  exposure_construction: Indicator for upstream location relative to the nearest monitoring station, within a 30 km bandwidth
    along the river; interaction with post-2003 period
  required_identifiers:
  - firm ID
  - year
  - firm address
  - river network
  - monitoring station location
  - upstream/downstream indicator
  - distance to monitoring station
  spillovers: Stricter upstream enforcement may cause firms to relocate downstream or to non-monitored river segments; downstream
    pollution may increase as upstream abates
research_compatibility:
  outcome_domains:
  - total factor productivity
  - pollution emissions
  - firm output
  - environmental compliance
  - firm location decisions
  affected_populations:
  - water-polluting manufacturing firms
  - local government officials
  - downstream communities
  mechanism_channels:
  - regulatory enforcement
  - political promotion incentives
  - compliance costs
  - pollution avoidance
  - firm adaptation
  best_for:
  - Studying causal effects of environmental regulation on firm productivity
  - spatial discontinuities in enforcement
  - political incentives in regulation
  not_good_for:
  - Nationally uniform regulatory effects
  - outcomes not related to water pollution or firm performance
design:
  affordances:
  - Spatial regression discontinuity at river monitoring stations
  - upstream-downstream comparison within narrow bandwidth
  - pre- and post-2003 comparison
  - heterogeneous effects by official promotion incentives
  candidate_designs:
  - Spatial regression discontinuity
  - difference-in-discontinuities (post-2003 vs pre-2003)
  - matched difference-in-differences comparing upstream and downstream firms
  identifying_variation: Plausibly exogenous assignment of firms to strict enforcement based on geographic location relative
    to monitoring stations, controlling for smooth spatial trends in economic conditions
  assumptions:
  - Firms do not precisely sort across the upstream-downstream threshold; spatial characteristics (other than enforcement)
    vary smoothly across the monitoring station; no other discontinuities at the same location
  diagnostics:
  - Test for discontinuities in firm characteristics across the threshold
  - placebo tests at alternative upstream-downstream cutoffs
  - control for smooth spatial polynomials
  - test for sorting via relocation analysis
  primary_strategy: Spatial regression discontinuity with difference-in-differences, using the discontinuity at monitoring
    stations interacted with the post-2003 enforcement regime
  estimand: The causal effect of the recorded exposure on Total factor productivity, COD emissions, chemical oxygen demand,
    regulatory inspections, conditional on the stated design assumptions.
  treatment_variable: Upstream of monitoring station (within 30 km) × post-2003
  comparison_logic: Upstream firms vs downstream firms within the same river segment, before and after the monitoring system
    became binding
  estimation_notes: Spatial regression discontinuity with difference-in-differences, using the discontinuity at monitoring
    stations interacted with the post-2003 enforcement regime
threats:
- type: firm-sorting
  basis: inferred
  condition: Firms may locate or relocate in response to differential enforcement upstream versus downstream, which would
    bias the RD estimates
  evidence_refs:
  - E1
  possible_diagnostics:
  - Test for discontinuities in firm density at the threshold
  - examine relocation patterns
  - use historical firm locations (pre-2003) as instruments
- type: spatial-confounds
  basis: inferred
  condition: Other geographical features (population centers, tributaries, economic zones) may change discontinuously at monitoring
    station locations
  evidence_refs:
  - E1
  possible_diagnostics:
  - Control for geographic covariates (population density
  - GDP per capita
  - altitude)
  - use narrow bandwidths
  - test for discontinuities in placebo outcomes
- type: anticipatory-behavior
  basis: inferred
  condition: Firms downstream may also reduce pollution if they anticipate that monitoring stations could be moved or if they
    share water bodies
  evidence_refs:
  - E1
  possible_diagnostics:
  - Test for downstream effects
  - examine dynamic treatment effects
  - use alternative control groups farther from monitoring stations
empirical_requirements:
  contract_version: 1
  population: Water-polluting manufacturing firms in China, 2000–2014
  observation_unit: Firm-year, with spatial location along river network
  geography_level: Firm location (exact coordinates) relative to monitoring stations
  time_start: 2000
  time_end: 2014
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields:
  - firm ID
  - year
  - firm address
  - latitude/longitude
  - industry
  - total factor productivity
  - output
  - emissions
  - distance to nearest monitoring station
  - upstream/downstream indicator
  required_identifiers:
  - firm ID
  - year
  - monitoring station ID
  - upstream/downstream indicator
  treatment_key:
  - upstream indicator interacted with post-2003 period
  treatment_source: Chinese Industrial Enterprises Database (2000–2014) for firm-level data; Ministry of Environmental Protection
    for monitoring station locations; river network GIS data for upstream/downstream classification
  measurement_risks:
  - firm location measurement error
  - monitoring station coordinate accuracy
  - river flow direction ambiguity (especially near confluences)
  - firm emission reporting quality
evidence:
- id: E1
  source_type: paper
  citation: 'He, Guojun, Shaoda Wang, and Bing Zhang. 2020. ''Watering Down Environmental Regulation in China.'' Quarterly
    Journal of Economics 135 (4): 2135–2185.'
  url: https://doi.org/10.1093/qje/qjaa024
  date: 2020
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - mechanism analysis
  - cost-benefit quantification
  verification_status: verified
design_applications:
- paper: Watering Down Environmental Regulation in China
  doi: 10.1093/qje/qjaa024
  journal: Quarterly Journal of Economics
  year: 2020
  research_question: Does local enforcement of environmental regulation respond to career incentives created by water quality
    monitoring, and at what cost to firm productivity?
  population: Water-polluting Chinese manufacturing firms (approximately 200,000 firm-year observations, 2000–2014)
  outcome: Total factor productivity, COD emissions, chemical oxygen demand, regulatory inspections
  data_used:
  - Chinese Industrial Enterprises Database (firm-level panel
  - 2000–2014)
  - Ministry of Environmental Protection (MEP) monitoring station data
  - river network GIS data
  - county-level political promotion data
  - COD and SO2 emissions data
  treatment_encoding: Upstream of monitoring station (within 30 km) × post-2003
  comparison: Upstream firms vs downstream firms within the same river segment, before and after the monitoring system became
    binding
  empirical_design: Spatial regression discontinuity with difference-in-differences, using the discontinuity at monitoring
    stations interacted with the post-2003 enforcement regime
  assumptions:
  - Firm characteristics are smooth across the monitoring station threshold; no other policies create a discontinuity at the
    same locations; firms cannot costlessly relocate across the threshold
  threats_addressed:
  - Firm sorting via density tests and historical location analysis; spatial confounds via geographic controls and narrow
    bandwidths; anticipatory behavior via dynamic specifications
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
method_transfer: null
superseded_by: china-water-quality-monitoring-rd
---
## Institutional Background

China's environmental regulatory system relies on water quality monitoring stations operated by the Ministry of Environmental Protection and provincial Environmental Protection Bureaus. These stations measure water quality at fixed locations along rivers and report readings upstream of the station. Starting in 2003, the central government began linking water quality measurements to the career evaluations of local officials. Since monitoring stations only capture upstream conditions, officials have a strong incentive to enforce pollution standards on firms upstream of monitoring stations while tolerating violations downstream. [E1]

## What Changed

After 2003, when water quality became a binding factor in official performance evaluations, local governments began enforcing environmental regulations asymmetrically: stricter enforcement upstream of monitoring stations (to improve measured water quality) and lax enforcement downstream (where pollution is not captured by the monitoring station). This created a spatial discontinuity in regulatory stringency at each monitoring station location. [E1]

## Implementation and Assignment

The assignment of firms to strict enforcement is determined purely by geography: firms located upstream of a monitoring station face significantly tighter environmental regulation than firms located downstream. The comparison is between firms on the same river, often within a few kilometers of each other, but on opposite sides of a monitoring station. This spatial discontinuity provides a clean identification strategy for the effects of environmental regulation on firm productivity. [E1]

## Why This Creates Empirical Variation

The spatial discontinuity at monitoring stations provides quasi-experimental variation in regulatory stringency. Since firm location relative to monitoring stations is determined by historical settlement patterns and is plausibly exogenous to firm productivity conditional on smooth spatial trends, the upstream-downstream comparison at narrow bandwidths isolates the causal effect of regulation on firm outcomes. The post-2003 timing allows a difference-in-differences design that controls for time-invariant spatial differences. [E1]

## Identification Risks

Firms may sort across the monitoring station threshold by relocating in response to differential enforcement. Spatial confounds at monitoring station locations (population centers, tributary confluences) may independently affect firm outcomes. The paper addresses these concerns through density tests, spatial controls, narrow bandwidths, and historical firm location analysis. The estimated productivity effects are large: upstream polluters face more than a 24% reduction in total factor productivity. [E1; analytical inference]

## Data Requirements

Firm-level panel data from the Chinese Industrial Enterprises Database (2000–2014) with firm addresses and geographic coordinates. Monitoring station locations from the Ministry of Environmental Protection. River network GIS data to classify firms as upstream or downstream. County-level political promotion data to test the career incentive mechanism. [E1]

## Evidence Notes

E1 provides a back-of-the-envelope calculation that China's asymmetric water regulation imposed an economic cost of over 800 billion yuan (2000–2007). The regulatory local average treatment effect (LATE) reveals that environmental enforcement at monitoring stations caused a 24–57% reduction in TFP for upstream polluters. The effect is driven entirely by prefectures where officials have stronger career concerns (provincial-level leaders above the typical promotion age threshold).

## Deprecation Notice

**Deprecated 2026-07-13 (task-27815780789b)**: This record is superseded by `china-water-quality-monitoring-rd`. Both records describe the same variation case — the spatial RD at China's surface water quality monitoring stations from He, Wang, Zhang (2020, QJE). The assignment mechanism (upstream vs downstream enforcement) is identical. Differences in reported bandwidth (5–10 km vs 30 km) and time windows (2000–2007 vs 2003–2014) reflect alternative specifications within the same paper rather than distinct assignment cases. The retained record consolidates both the TFP-cost and political-incentive dimensions of the analysis. [analytical inference]
