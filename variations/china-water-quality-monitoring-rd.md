---
schema_version: 2
id: china-water-quality-monitoring-rd
name: Spatial Regression Discontinuity in China's Water Quality Monitoring System
  — Upstream vs Downstream Firm Regulation
aliases:
- Water quality monitoring upstream RDD
- He Wang Zhang watering down regulation
- Surface water monitoring China firm TFP
status: grounded
provenance:
  task_id: task-a9b8d963d5ce
scope:
  country: China
  regions:
  - River basins throughout China with surface water quality monitoring stations
  domains:
  - environment
  - firm-productivity
  - regulation
  - political-economy
  variation_type: boundary-discontinuity
  knowledge_role: china-variation
  china_relevance: The fixed location of national water-quality monitoring stations
    creates a sharp upstream-downstream discontinuity in regulatory enforcement for
    Chinese polluting firms, supporting spatial RD designs for firm TFP, emissions,
    and survival.
identity:
  instrument: China's surface water quality monitoring system — local officials are
    evaluated based on pollutant readings at downstream monitoring stations, but these
    stations only capture pollution from upstream firms; this creates a spatial regression
    discontinuity where firms immediately upstream of a monitor face much stricter
    environmental enforcement than those immediately downstream
  authority: Ministry of Environmental Protection (now Ministry of Ecology and Environment)
  legal_identifiers:
  - State Environmental Protection Administration, 《关于印发〈国家环境质量监测网地表水监测断面〉的通知》（环发〔2003〕3号）,
    6 Jan 2003
  - State Council, 《国务院关于落实科学发展观加强环境保护的决定》（国发〔2005〕39号）, 3 Dec 2005
  - General Office of the State Council, 《重点流域水污染防治专项规划实施情况考核暂行办法》（国办发〔2009〕38号）,
    25 Apr 2009
  implementation_regime: Water quality is monitored at fixed stations along major
    rivers; local officials' performance evaluations are tied to readings at these
    stations; because monitors capture upstream but not downstream pollution, enforcement
    is spatially asymmetric
  assignment_mechanism: A firm's location relative to the nearest downstream water
    quality monitor — whether it lies just upstream (within the monitored catchment)
    or just downstream (outside the monitored catchment) — determines regulatory stringency;
    this location is determined by the fixed placement of monitoring stations
  parent: null
  related_variations:
  - china-water-regulation-enforcement
timeline:
  announcement: null
  effective: null
  implementation_start: 2000
  implementation_end: 2014
  local_timing: The monitoring network was progressively expanded; the main RD analysis
    period is 2000–2007, and the enforcement regime analysis extends through 2014
    under the 9th, 10th, 11th, and 12th Five-Year Plans
  anticipation: Firm location decisions may be influenced by knowledge of monitoring
    station locations; however, many stations were placed after existing firms were
    already located
  last_verified: '2026-07-14'
assignment:
  unit: Firm
  treated: Polluting firms located immediately upstream of a surface water quality
    monitoring station — their pollution is captured by the monitor and they face
    strict enforcement of COD (Chemical Oxygen Demand) emissions limits
  comparison_pool: Polluting firms located immediately downstream of the same monitoring
    station — their pollution is NOT captured by the monitor and enforcement is substantially
    weaker
  rule: A firm's distance to the nearest downstream monitoring station determines
    whether it falls within the monitored catchment; firms within ~5–10 km upstream
    are "treated" with stricter regulation
  intensity: The treatment intensity decays with distance upstream from the monitor;
    enforcement is strongest in the immediate upstream vicinity (within ~5 km) and
    weakens at greater distances
  exemptions: []
  compliance: Regulatory enforcement is imperfect — local officials balance environmental
    targets against economic and employment goals, but the monitor creates a sharp
    incentive gradient
  exposure_construction: For each firm, compute the geographic coordinates and the
    distance to the nearest downstream water quality monitoring station along the
    river system; code firms as upstream or downstream; use distance to the monitor
    as the forcing variable in a spatial RD
  required_identifiers:
  - firm ID or name
  - geographic coordinates
  - industry code
  - distance to nearest downstream water quality monitor
  - river basin
  - calendar year
  spillovers: Tighter regulation upstream may cause polluting firms to relocate downstream
    (spatial spillovers); competition effects may shift production from regulated
    to unregulated firms in the same industry
research_compatibility:
  outcome_domains:
  - firm TFP
  - emissions (COD)
  - firm survival
  - employment
  - output
  - industry structure
  affected_populations:
  - water-polluting manufacturing firms
  - particularly in chemical
  - paper
  - textile
  - and food processing industries
  mechanism_channels:
  - emissions reduction
  - abatement costs
  - production process changes
  - output reduction
  - firm exit
  - spatial relocation
  - local official career incentives (promotion evaluation tied to monitored water
    quality)
  - regulatory enforcement intensity variation
  best_for:
  - Estimating the firm-level costs of environmental regulation
  - Spatial RD designs with geographic forcing variables
  - Outcomes observable in Chinese firm-level datasets (Annual Survey of Industrial
    Firms, Environmental Survey)
  not_good_for:
  - Non-point-source pollution (agricultural runoff)
  - Firms not in the Environmental Survey reporting system
  - Outcomes requiring individual-level (worker or household) data
design:
  affordances:
  - fixed monitoring station locations
  - sharp asymmetric enforcement incentive (monitored upstream vs unmonitored downstream)
  - firm-level data with geographic coordinates
  - river network provides a natural spatial ordering
  candidate_designs:
  - spatial regression discontinuity (distance to nearest downstream monitor)
  - difference-in-differences (pre/post monitoring station installation)
  - instrumental variables (distance to monitor as instrument for enforcement intensity)
  identifying_variation: Discontinuous change in regulatory stringency at each monitoring
    station location — firms just upstream of a monitor face much stricter enforcement
    than firms just downstream, driven by the monitor's catchment geometry
  assumptions:
  - Firm location is smooth around monitoring station locations (no sorting just upstream
    vs downstream of a monitor)
  - Monitoring station locations are exogenous to the characteristics of individual
    upstream firms
  - The pollution measurement technology accurately captures upstream but not downstream
    pollution
  - No differential shocks to upstream vs downstream firms other than regulation
  diagnostics:
  - Test for smoothness of firm density and observable characteristics around monitoring
    stations
  - Plot TFP and COD emissions against distance to the monitor
  - Estimate with alternative bandwidths
  - Use alternative measures of regulatory stringency
  - Examine whether effects vary by local officials' promotion incentives
  - Test for firm relocation around monitoring stations
  primary_strategy: Spatial regression discontinuity using distance to the nearest
    downstream water quality monitor as the forcing variable; the cutoff is the monitor
    location (upstream = treated with strict enforcement, downstream = control with
    weak enforcement)
  estimand: The effect of the recorded exposure on firm TFP, COD emissions, firm survival,
    output, and employment, conditional on the stated design assumptions.
  treatment_variable: Firm location upstream versus downstream of the nearest water
    quality monitoring station, interacted with distance to the monitor in a spatial
    RD
  comparison_logic: Firms just downstream versus just upstream of the same monitoring
    station, controlling for distance
  estimation_notes: Spatial regression discontinuity using distance to the nearest
    downstream water quality monitor as the forcing variable; the cutoff is the monitor
    location (upstream = treated with strict enforcement, downstream = control with
    weak enforcement)
  claim_type: causal
threats:
- type: endogenous-monitor-placement
  basis: inferred
  condition: If monitoring stations are placed precisely where polluting firms are
    concentrated (to measure them), the RD is invalid because station placement is
    endogenous to firm characteristics
  evidence_refs:
  - E1
  possible_diagnostics:
  - examine station placement criteria
  - test for smoothness of firm characteristics at station locations
  - analyze within-river segment variation
- type: firm-sorting
  basis: inferred
  condition: New firms may choose to locate downstream of monitors to avoid regulation;
    existing firms may relocate; this sorting would confound the RD estimates
  evidence_refs:
  - E1
  possible_diagnostics:
  - test for bunching of firms just downstream
  - analyze separately by firm age and entry cohort
  - examine firm relocation patterns
- type: spatial-spillovers
  basis: inferred
  condition: Pollution discharged upstream affects downstream water quality (spatial
    externality); reduced output by regulated upstream firms may benefit unregulated
    downstream competitors
  evidence_refs:
  - E1
  possible_diagnostics:
  - model spatial pollution transport
  - estimate effects on downstream firms' market outcomes
  - test for within-industry general equilibrium effects
empirical_requirements:
  contract_version: 1
  population: Water-polluting industrial firms in China, matched between the Annual
    Survey of Industrial Firms and the Environmental Survey of Polluting Firms, 2000–2014
  observation_unit: Firm-year
  geography_level: Firm-level geographic coordinates, linked to river network and
    monitoring station locations
  time_start: 2000
  time_end: 2014
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields:
  - firm TFP
  - COD emissions
  - firm geographic coordinates
  - industry code
  - output
  - employment
  - river basin
  - monitoring station coordinates
  required_identifiers:
  - firm ID
  - year
  - geographic coordinates
  - distance to monitor
  treatment_key:
  - firm coordinates
  - monitoring station coordinates
  - upstream/downstream indicator
  - distance to monitor
  treatment_source: MEP water quality monitoring station data; Annual Survey of Industrial
    Firms (NBS); Environmental Survey of Polluting Firms (MEP); river network GIS
    data
  measurement_risks:
  - firm coordinates may be imprecise (registered vs actual address)
  - monitoring station locations may change over time
  - river network GIS data quality
  - TFP measurement error
  - COD self-reporting bias
evidence:
- id: E1
  source_type: paper
  citation: 'He, Guojun, Shaoda Wang, and Bing Zhang. 2020. "Watering Down Environmental
    Regulation in China." Quarterly Journal of Economics 135 (4): 2135–2185.'
  url: https://doi.org/10.1093/qje/qjaa024
  date: 2020
  supports:
  - identity
  - assignment
  - design
  - research_compatibility
  - empirical_requirements
  - design_applications
  verification_status: verified
  access_level: full-text
  locator: Full article via DOI
- id: E2
  source_type: policy-document
  citation: State Council of China. 2005. "Decision on Implementing the Scientific
    Outlook on Development and Strengthening Environmental Protection" (国务院关于落实科学发展观加强环境保护的决定).
    Guo Fa No. 39 (国发〔2005〕39号), December 3, 2005.
  url: https://www.gov.cn/zwgk/2005-12/13/content_125680.htm
  date: '2005-12-03'
  supports:
  - assignment
  verification_status: verified
  access_level: official-document
  locator: Official State Council decision; establishes the environmental target responsibility
    system and incorporates environmental targets into official performance evaluation.
- id: E3
  source_type: policy-document
  citation: State Environmental Protection Administration. 2003. "Notice on Printing
    and Distributing the National Surface Water Quality Monitoring Network Sections"
    (关于印发《国家环境质量监测网地表水监测断面》的通知). Huan Fa No. 3 (环发〔2003〕3号), January 6, 2003.
  url: https://www.mee.gov.cn/gkml/zj/wj/200910/t20091022_172154.htm
  date: '2003-01-06'
  supports:
  - identity
  - timeline
  verification_status: verified
  access_level: official-document
  locator: Official MEP notice; adjusts the national surface water monitoring sections
    and requires their use for basin water quality monitoring from January 2003.
- id: E4
  source_type: policy-document
  citation: General Office of the State Council. 2009. "Interim Measures for Assessing
    Implementation of Key River Basin Water Pollution Prevention Special Plans" (重点流域水污染防治专项规划实施情况考核暂行办法).
    Guo Ban Fa No. 38 (国办发〔2009〕38号), April 25, 2009.
  url: http://www.qinghai.gov.cn/xxgk/xxgk/qhzb/qhzb2009/201712/P020171204356648902950.pdf
  date: '2009-04-25'
  supports:
  - assignment
  verification_status: verified
  access_level: official-document
  locator: Qinghai provincial government archive of the State Council notice; Article
    4 defines water-quality indicators at assessment sections as the basis for provincial-government
    accountability.
design_applications:
- paper: Watering Down Environmental Regulation in China
  doi: 10.1093/qje/qjaa024
  journal: Quarterly Journal of Economics
  year: 2020
  research_question: What is the effect of water pollution regulation on firm-level
    total factor productivity in China, exploiting spatial discontinuities in enforcement
    created by the water quality monitoring system?
  population: Water-polluting industrial firms in China, 2000–2007
  outcome: Firm TFP, COD emissions, firm survival, output, employment
  data_used:
  - Annual Survey of Industrial Firms (NBS)
  - Environmental Survey of Polluting Firms (MEP)
  - MEP national surface water quality monitoring station coordinates and readings
  - China river network GIS data
  - Prefecture-level official career-incentive and leadership data
  treatment_encoding: Firm location upstream versus downstream of the nearest water
    quality monitoring station, interacted with distance to the monitor in a spatial
    RD
  comparison: Firms just downstream versus just upstream of the same monitoring station,
    controlling for distance
  empirical_design: Spatial regression discontinuity using distance to the nearest
    downstream water quality monitor as the forcing variable; the cutoff is the monitor
    location (upstream = treated with strict enforcement, downstream = control with
    weak enforcement)
  assumptions:
  - firm location is smooth around monitors
  - monitors are exogenously placed
  - no sorting around cutoffs
  - pollution measurement is accurate
  threats_addressed:
  - endogenous placement via smoothness tests
  - sorting via firm-entry analysis
  - spillovers via within-river basin comparisons
  - alternative explanations via multiple specifications
  evidence_refs:
  - E1
readiness_blockers: []
method_transfer: null
---
## Institutional Background

China's surface water quality monitoring system was established to track progress toward national pollution reduction targets. Under the 9th and 10th Five-Year Plans, COD (Chemical Oxygen Demand) — a measure of organic water pollution — was designated a key national target. Starting in 2003, the central government began linking water quality measurements to the career evaluations of local officials, making water quality a binding factor in promotion decisions. Local officials' career advancement depends on meeting these targets, creating strong incentives to reduce monitored pollution. However, a monitor placed in a river only captures pollution from upstream sources; pollution discharged downstream of the monitor flows away unmeasured. This simple hydrologic fact creates an asymmetric enforcement regime: firms upstream of a monitor are tightly regulated; firms downstream are not. [E1]

By 2007, there were approximately 500 national-level surface water quality monitoring stations distributed across China's major river basins. Each station measures multiple pollutants at regular intervals, and the data are reported to provincial and national environmental agencies. The station network was designed to provide representative coverage of water quality, not to equalize regulatory pressure on all firms. The paper shows that the enforcement effect is driven entirely by prefectures where officials have stronger career concerns — specifically, provincial-level leaders above the typical promotion age threshold — confirming the political incentive mechanism. [E1]

## What Changed

The introduction of binding water quality targets in official performance evaluations after 2003 transformed the monitoring network from a measurement system into an enforcement tool. For a firm located near a monitoring station, whether it faces strict or lax enforcement depends on a single geographic fact: is the firm upstream or downstream of the nearest monitor? This creates hundreds of local discontinuities in regulatory stringency, each at a monitoring station. The cumulative economic cost is enormous: the paper estimates that water regulation reduced aggregate TFP by approximately 825 billion RMB (in 2007 prices) during 2000–2007. [E1]

## Implementation and Assignment

The spatial RD design exploits the fact that, near each monitoring station, firms on opposite sides of the station face very different enforcement regimes but are otherwise in similar geographic, economic, and hydrologic environments. The forcing variable is the firm's distance along the river to the nearest downstream monitoring station. Firms with positive distance (upstream) are treated; firms with negative distance (downstream) are controls. [E1]

## Why This Creates Empirical Variation

The monitoring station network creates hundreds of spatial discontinuities in regulatory enforcement. Each station serves as a local RD cutoff. The identification relies on the assumption that, close to the cutoff, firm characteristics vary smoothly — the only thing that changes sharply at the station location is the regulatory regime. This design cleverly exploits a feature of the monitoring technology (downstream measurement) to identify a policy parameter (cost of regulation) that would otherwise be difficult to estimate due to the endogeneity of enforcement. [E1; analytical inference]

## Identification Risks

The central threat is that monitoring stations were not placed randomly — they were located to measure water quality in specific river segments. If stations were systematically placed just downstream of industrial clusters, the upstream/downstream comparison is confounded. The paper addresses this by testing for smoothness of firm density and characteristics at station locations. A subtler threat is firm sorting: if firms anticipate stricter regulation upstream of monitors, they may locate downstream, creating a selected sample of upstream firms. [E1; analytical inference]

## Data Requirements

The design requires: (1) firm-level geographic coordinates linked to the river network; (2) monitoring station coordinates; (3) firm-level TFP, emissions, and economic data from the Annual Survey of Industrial Firms and the Environmental Survey; and (4) a GIS of China's river basin system. The matching of the two firm surveys and the geocoding of firms and stations are the most technically demanding components. [E1]

## Evidence Notes

E1 is the published QJE article. The key findings — that upstream firms face >24% lower TFP and >57% lower COD emissions — are exceptionally large and highlight the economic cost of spatially asymmetric regulation. The paper's calculation that water regulation cost approximately 825 billion RMB in lost TFP is a striking quantification of the trade-off between environmental quality and economic efficiency. The paper also shows that the cost estimates are robust to a wide range of alternative specifications and bandwidth choices.

**Consolidation note (task-27815780789b, 2026-07-13)**: This record was consolidated from two separate entries that described the same variation case. Both entries captured the same instrument (water quality monitoring station spatial RD), same paper (He, Wang, Zhang 2020 QJE), and same assignment mechanism (upstream vs downstream enforcement). The former duplicate `china-water-regulation-enforcement` (deprecated) emphasized the political promotion mechanism and used a wider 30 km bandwidth over 2003–2014. This record now covers the full analysis period (2000–2014) and incorporates both the TFP-cost and political-incentive dimensions. The primary RD specification uses 2000–2007 with narrower bandwidths; the enforcement regime analysis extends through 2014. [analytical inference]
