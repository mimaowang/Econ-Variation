---
schema_version: 2
id: china-industrial-park-political-connection-rotation
name: Chinese Industrial-Park Designation and Political-Connection Rotation Exposure (1987–2008)
aliases:
- Kahn Sun Wu Zheng industrial parks political connections
- 1,400 industrial parks China political rotation
- 中国工业园区 政治联系 轮换
status: grounded
provenance:
  task_id: task-f45306a5188c
scope:
  country: China
  regions:
  - Chinese prefecture-level cities competing for national- and provincial-level industrial parks
  domains:
  - urban
  - regional-economics
  - economic-geography
  - infrastructure
  - manufacturing
  - governance
  - political-economy
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    The case records a formal place-based investment in Chinese cities and the paper's
    assignment-relevant political-connection shock. Provincial leader turnover changes
    whether an incumbent city leader is connected to the decision-maker, while the park
    approval list supplies a city-level policy exposure. The connection measure is not a
    universal random assignment; its use is conditional on the rotation and comparison
    assumptions documented below.
identity:
  instrument: >
    National- and provincial-level industrial-park approvals and establishments in China,
    with site selection affected by whether the incumbent city leader is socially connected
    to the provincial decision-maker. The baseline connection is shared workplace between
    city and provincial Communist Party secretaries; birthplace, college, and faction
    measures are alternatives.
  authority: >
    Central and provincial governments formally approve and allocate scarce national- and
    provincial-level park permissions. The National Development and Reform Commission,
    former Ministry of Land and Resources, and Ministry of Construction published the
    reviewed park directory and boundary materials; provincial leaders decide among cities
    within their jurisdiction.
  legal_identifiers:
  - China Development Zone Review and Announcement Directory (2006 edition)
  - Ministry of Land and Resources Announcement No. 17 of 2006 on development-zone boundaries
  - National- and provincial-level industrial-park approval and establishment records
  implementation_regime: >
    Since the 1980s China used national and provincial industrial parks as geographically
    delimited place-based investments with preferential tax, tariff, credit, land, and
    regulatory arrangements. National and provincial parks went through a formal approval
    process; lower-level parks were not treated as the same object because many lacked
    central or provincial approval and were affected by the 2003 clean-up.
  assignment_mechanism: >
    Cities within a province compete for park permissions. A provincial leader weighs
    expected urban growth and distributional effects against rewarding a connected city
    leader. Political connection changes when a key provincial leader turns over under the
    CCP's roughly five-year (or shorter) political cycle, while the incumbent city leader
    remains in office. The paper treats this rotation-induced change as the source of
    plausibly exogenous connection variation, not the park approval itself as random.
  parent: null
  related_variations:
  - china-expressway-market-access-walled-city-mst
timeline:
  announcement: null
  effective: null
  implementation_start: 1987
  implementation_end: 2008
  local_timing: >
    The application follows city and provincial leaders, park approvals, and urban outcomes
    over 1988–2008. Park establishment/approval year and the city-leader/provincial-leader
    connection status in that year must be kept as separate fields. The national directory
    is a historical audit source, not a claim that every listed date is a construction
    completion date.
  anticipation: >
    Cities knew that park permissions and higher-level status brought preferential policies
    and competed for them. Leader rotations and park proposals may therefore be anticipated
    in broad terms; a design should use observed tenure and approval timing rather than a
    single national post dummy.
  last_verified: '2026-08-12'
assignment:
  unit: City-year in a province-level park choice set; alternatively park-city event linked to leader tenure
  treated: >
    For the policy exposure, a city-year is treated when it receives a newly approved or
    established national- or provincial-level industrial park. For the political-connection
    design, the treated state is a city whose incumbent leader is connected to the current
    provincial decision-maker in the relevant year, with connection changing after an
    upper-level rotation.
  comparison_pool: >
    Other prefecture-level cities in the same province-year choice set, including cities
    that have not yet received a qualifying park. For growth analyses, compare park cities
    with similar predicted park propensity and distinguish connected from economically
    selected sites; nearby cities are not automatically clean controls because parks can
    generate labor, firm, and land-market spillovers.
  rule: >
    Build a city-year panel from the official park directory and city statistical yearbooks.
    Mark the first qualifying national/provincial park approval or establishment, preserve
    park level and approval year, and merge the leader-tenure file. Code connection as a
    workplace, birthplace, college, or faction tie between the city leader and the key
    provincial leader; use the workplace connection between same-level party secretaries as
    the baseline. The rotation design compares the same incumbent city's connection status
    before and after turnover while retaining the provincial choice set.
  intensity: >
    Binary first qualifying park or cumulative park count; park level, year, and attributes
    can refine treatment. Connection intensity is binary in the main specification, with
    alternative tie dimensions and the number/type of connected relationships as checks.
  exemptions:
  - Four directly administered municipalities excluded by the paper's sample
  - Qinghai, Tibet, and Ningxia excluded in the paper because of missing data or no qualifying new parks
  - Prefecture-level and lower parks without formal national or provincial approval are not the same treatment
  - Parks approved before the observed leader-tenure window require a separate pre-existing-exposure flag
  compliance: >
    Formal approval does not guarantee timely construction, land development, firm entry, or
    effective preferential treatment. Political connection is a decision-maker attribute,
    not a treatment that cities must comply with; actual park receipt is the policy outcome.
  exposure_construction: >
    Join park name, directory code, city, level, approval/establishment year, and boundary
    information from the official directory to stable prefecture-city identifiers and the
    city-year outcome panel. Join leader names, positions, tenure dates, workplace history,
    birthplace, college, and faction to construct connection measures. Keep approval,
    construction, operation, and later upgrading separate where sources permit.
  required_identifiers:
  - park directory code and name
  - city and province code
  - park level and approval/establishment year
  - city leader and provincial leader identifiers
  - leader position and tenure dates
  - connection dimension and source biography
  spillovers: >
    Parks can attract firms, workers, infrastructure, and land development from nearby
    cities; provincial budgets and quotas may also be reallocated across the choice set.
    A within-province assignment can therefore have both local benefits and displacement.
research_compatibility:
  outcome_domains:
  - urban GDP and GDP per capita
  - total factor productivity
  - manufacturing employment and firm entry
  - foreign direct investment and exports
  - land development and housing
  - regional inequality
  affected_populations:
  - firms and workers in park host cities
  - residents and landowners near park boundaries
  - competing cities within the same province
  - provincial leaders and city officials making allocation decisions
  mechanism_channels:
  - agglomeration and input sharing
  - labor pooling and knowledge spillovers
  - preferential tax, credit, land, and regulatory treatment
  - political favoritism and capital misallocation
  - local government promotion incentives
  best_for:
  - Place-based investment and industrial-park effects in Chinese cities
  - Political economy of spatial public investment
  - Designs that can reconstruct park approval and leader tenure
  - Comparing economically selected and connection-assisted park placement
  not_good_for:
  - A uniform national industrial-policy dummy
  - Treating all industrial parks, including unapproved local zones, as one program
  - Interpreting connection status as random without rotation and pre-trend checks
  - A no-spillover city comparison that ignores provincial competition
design:
  claim_type: causal
  affordances:
  - Formal national/provincial park approval and city-level timing
  - Within-province choice sets
  - Leader-tenure rotations that change connection status
  - Rich city-year outcomes and GIS access controls
  - Park-level heterogeneity and predicted-growth counterfactuals
  candidate_designs:
  - Rotation-based event study of connection changes
  - Within-province conditional-logit park-site selection
  - Propensity-score or matched comparison of connected and economically selected parks
  - Staggered city-level park opening design with spillover checks
  - Heterogeneity by park level, region, connection type, and baseline fundamentals
  identifying_variation: >
    The policy variation is the staggered approval/establishment of national and provincial
    parks across cities. The paper's assignment-relevant variation is the change in a city's
    connection to the provincial decision-maker when the latter turns over, conditional on
    the incumbent city leader remaining and on the province-year choice set. The two should
    not be collapsed into a claim that park openings were random.
  primary_strategy: >
    Estimate city-year park placement models with province-year choice sets, expected growth
    and inequality measures, and connection status. For outcome effects, compare cities with
    similar predicted park propensity and separate parks selected through connection from
    those selected through economic and geographic fundamentals. Where leader rotations are
    reconstructed, use event-time and within-city connection changes with leader and
    province-year controls.
  estimand: >
    The conditional effect of receiving a qualifying industrial park on city growth, or the
    effect of a rotation-induced change in political connection on park placement and the
    subsequent growth return, for Chinese cities in the 1988–2008 application and under the
    stated choice-set and spillover assumptions.
  treatment_variable: >
    First qualifying park approval/establishment indicator and event time; baseline
    connection dummy between city and provincial party secretaries in the park year; and a
    rotation-induced connection-change indicator stored separately.
  comparison_logic: >
    Park placement: compare cities within the same provincial choice set and year. Growth:
    compare actual park sites with counterfactual cities matched on predicted park returns,
    and report connected-site differences separately. A connection switch is informative
    only when the city leader remains and the provincial turnover is dated and observed.
  estimation_notes: >
    The paper reports a 6.6 percentage-point higher park-placement probability for a
    connected city in its baseline model and lower GDP per capita/TFP returns for parks
    selected largely through connections. These are source-reported estimates; the design
    remains sensitive to leader selection, timing, and spillovers.
  assumptions:
  - Provincial leader turnover changes connection status without being timed to the city's
    unobserved park prospects, conditional on observed tenure and controls
  - The park directory measures comparable national/provincial approvals across cities
  - Expected growth and inequality counterfactuals adequately approximate the leader's
    information set
  - Connection measures from biographies capture the relevant relationship and are not
    merely proxies for unobserved ability or factional selection
  - Spillovers and within-province displacement are either modeled or do not overturn the
    chosen estimand
  diagnostics:
  - Reconstruct the leader-tenure and park-year crosswalk from primary files
  - Event-study pre-trends around provincial-leader turnover
  - Compare workplace, birthplace, college, and faction connection definitions
  - Province-year conditional-logit and alternative choice sets
  - Exclude or separately code parks approved before 2003 clean-up and pre-existing parks
  - Test neighboring-city, firm-entry, land, and migration spillovers
threats:
- type: endogenous-leader-selection
  basis: reported
  condition: >
    Provincial leaders may appoint connected or capable city leaders to better cities, so
    connection status can correlate with unobserved park prospects even when the turnover is
    plausibly external to a particular city.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - leader fixed effects or tenure controls where possible
  - pre-rotation outcomes and connection balance
  - rotation-based event studies and alternative connection dimensions
- type: approval-versus-implementation-timing
  basis: documented
  condition: >
    The official directory reports approval and boundary information, while construction,
    land servicing, operation, and firm entry may occur later. Treating approval as the
    exact treatment date can mix anticipation and implementation.
  evidence_refs:
  - E3
  - E4
  possible_diagnostics:
  - keep approval, construction, and operation dates separate
  - event-time windows and alternative start dates
  - park-level verification from local notices
- type: concurrent-place-based-policy
  basis: reported
  condition: >
    Transport, trade, tax, land, and the 2003 development-zone clean-up can coincide with
    park designation and affect urban growth independently.
  evidence_refs:
  - E2
  possible_diagnostics:
  - control for highway, airport, railway, and seaport access
  - exclude the 2008 stimulus transition and test regime periods
  - code park level and policy package separately
- type: spatial-and-provincial-spillovers
  basis: reported
  condition: >
    Parks can attract activity from nearby cities and change provincial allocation, violating
    a simple stable-unit or untreated-neighbor comparison.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - distance bands and province-level totals
  - neighboring-city outcomes and firm relocation measures
  - alternative estimands for local versus provincial growth
- type: historical-data-and-boundary-error
  basis: documented
  condition: >
    Park names, city boundaries, leader biographies, and directory codes change over time;
    a city crosswalk or boundary-only match can misdate or mislocate exposure.
  evidence_refs:
  - E3
  - E4
  possible_diagnostics:
  - preserve original directory code and historical name
  - audit boundary coordinates and city-code crosswalks
  - triangulate leader tenure from multiple biographical sources
empirical_requirements:
  contract_version: 1
  population: 276 Chinese prefecture-level cities and national/provincial industrial parks observed in the 1988–2008 application
  observation_unit: City-year and park-city event within a province-year choice set
  geography_level: Prefecture-level city and official park boundary
  time_start: 1988
  time_end: 2008
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields:
  - park directory code, name, level, city, and approval/establishment year
  - official or audited park boundary and area
  - city GDP, GDP per capita, population, employment, FDI, and industrial outcomes
  - city and provincial leader names, positions, and tenure dates
  - workplace, birthplace, college, and faction connection fields
  - highway, airport, railway, and seaport distances
  - city and province identifiers stable across the historical period
  required_identifiers:
  - park code
  - city code
  - province code
  - year
  - city leader ID
  - provincial leader ID
  - connection type
  treatment_key:
  - city code
  - park level
  - approval or establishment year
  - city leader tenure
  - provincial leader tenure
  - connection status and rotation date
  treatment_source: >
    NDRC/MNR/Construction Ministry China Development Zone Review and Announcement Directory
    (2006 edition), Ministry of Land and Resources boundary announcements, China City
    Statistical Yearbooks, hand-collected official CVs and Duxiu/CNKI biographical records,
    and the published paper's park and leader crosswalk.
  measurement_risks:
  - approval, construction, and operation dates may differ
  - national/provincial versus local park definitions and upgrades
  - historical city and park-boundary changes
  - incomplete or inconsistent official biographies
  - connection measures may proxy ability, faction, or appointment selection
  - city-year growth is affected by concurrent infrastructure and place-based policies
design_profiles: []
evidence:
- id: E1
  source_type: paper
  citation: 'Kahn, Matthew E., Weizeng Sun, Jianfeng Wu, and Siqi Zheng. 2021. "Do political connections help or hinder urban economic growth? Evidence from 1,400 industrial parks in China." Journal of Urban Economics 121:103289. DOI: 10.1016/j.jue.2020.103289.'
  url: https://doi.org/10.1016/j.jue.2020.103289
  date: 2021
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - identity.implementation_regime
  - timeline.implementation_start
  - timeline.implementation_end
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design_applications.treatment_encoding
  - design_applications.comparison
  verification_status: verified
  access_level: abstract
  locator: 'ScienceDirect article page and abstract: 1,400 parks, 1987–2008 leader data, rotation-generated connection changes, placement probability, and heterogeneous urban-growth returns.'
- id: E2
  source_type: paper
  citation: 'Kahn, Matthew E., Weizeng Sun, Jianfeng Wu, and Siqi Zheng. 2018. "The Revealed Preference of the Chinese Communist Party Leadership: Investing in Local Economic Development versus Rewarding Social Connections." NBER Working Paper 24457.'
  url: https://www.nber.org/system/files/working_papers/w24457/w24457.pdf
  date: 2018
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - identity.implementation_regime
  - timeline.local_timing
  - assignment.rule
  - assignment.exposure_construction
  - assignment.required_identifiers
  - design.identifying_variation
  - design.primary_strategy
  - design.assumptions
  - design.diagnostics
  - threats.condition
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_key
  - design_applications.data_used
  - design_applications.treatment_encoding
  verification_status: verified
  access_level: full-text
  locator: 'NBER Working Paper 24457, Data Construction and Sections on park placement: 276 cities, 1,417 national/provincial parks, Ministry directory establishment year/city, city yearbooks, GIS access, connection dimensions, conditional-logit choice model, and 1988–2008 sample.'
- id: E3
  source_type: policy-document
  citation: 'National Development and Reform Commission, Ministry of Land and Resources, and Ministry of Construction. 2007. China Development Zone Review and Announcement Directory (2006 edition), Announcement No. 18.'
  url: https://www.ndrc.gov.cn/xxgk/zcfb/gg/200704/t20070406_961289_ext.html
  date: 2007
  supports:
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.implementation_start
  - assignment.rule
  - assignment.exposure_construction
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: official-document
  locator: 'NDRC official announcement paragraphs 8–11: post-2003 clean-up and review, approval and four-boundary determination, formal directory, and continued suspension of unreviewed provincial development zones.'
- id: E4
  source_type: implementation-document
  citation: 'Ministry of Land and Resources. 2006. Announcement No. 17: Ninth batch of development zones implementing four-boundary ranges.'
  url: https://policy.mofcom.gov.cn/claw/clawContent.shtml?id=12338
  date: 2006
  supports:
  - identity.legal_identifiers
  - identity.implementation_regime
  - assignment.exposure_construction
  - assignment.required_identifiers
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_key
  verification_status: verified
  access_level: official-document
  locator: 'Ministry announcement reproduced in the Ministry of Commerce legal database: boundary text and coordinates were checked against approved areas; 144 provincial development zones announced on 10 July 2006.'
- id: E5
  source_type: scholarship
  citation: 'Kahn, Matthew E., Weizeng Sun, Jianfeng Wu, and Siqi Zheng. 2020. "Industrial parks and urban growth: A political economy story in China." Global Research Unit Working Paper 2020-023, City University of Hong Kong.'
  url: https://www.cb.cityu.edu.hk/ef/doc/GRU/WPS/GRU%232020-023%20Wu_Zheng.pdf
  date: 2020
  supports:
  - identity.implementation_regime
  - assignment.rule
  - assignment.exposure_construction
  - design.primary_strategy
  - design.assumptions
  - threats.condition
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  verification_status: verified
  access_level: full-text
  locator: 'Author working paper pp. 3–13: park types and formal approval, 1,568 directory parks, 1988–2008 city panel, four connection dimensions, rotation rationale, conditional-logit estimates, and spillover/SUTVA caveats.'
design_applications:
- paper: 'Do political connections help or hinder urban economic growth? Evidence from 1,400 industrial parks in China'
  doi: 10.1016/j.jue.2020.103289
  journal: Journal of Urban Economics
  year: 2021
  research_question: Do political connections influence where Chinese provincial leaders place industrial parks, and do connection-assisted parks have different urban growth returns?
  population: 276 Chinese prefecture-level cities and national/provincial industrial parks, with leader data from 1987–2008 and city outcomes from 1988–2008
  outcome: Park placement, city GDP and GDP per capita, TFP, employment, FDI, exports, and provincial inequality counterfactuals
  data_used:
  - China Development Zone Review and Announcement Directory and Ministry boundary materials
  - China City Statistical Yearbooks
  - Hand-collected leader curricula vitae from Duxiu/CNKI and related sources
  - GIS distances to highway entrances, airports, railway stations, and seaports
  - Published paper and NBER working-paper calculations
  treatment_encoding: >
    Park placement is a city-year indicator for a new national/provincial park. The main
    political-connection regressor equals one when the incumbent city leader and key
    provincial leader share a workplace; alternative measures use birthplace, college, or
    faction. The connection changes when the provincial leader turns over and the city
    leader remains in office.
  comparison: >
    Conditional on province-year choice sets and expected growth/inequality, compare cities
    with and without a connected incumbent. For outcomes, compare actual park sites with
    similar predicted park returns and separate connection-assisted placement from
    economically selected placement.
  empirical_design: >
    Conditional-logit and linear-probability park-site models, propensity-score/matched
    growth comparisons, leader-rotation/event-time checks, and heterogeneity by region,
    park level, and connection type.
  assumptions:
  - provincial turnover is plausibly external to city-specific contemporaneous park prospects
  - park directory dates and city joins identify comparable qualifying investments
  - expected growth and inequality measures approximate the provincial leader's information set
  - connection measures are not only proxies for unobserved leader ability or city selection
  - local and provincial spillovers are addressed for the chosen outcome estimand
  threats_addressed:
  - leader selection through tenure data, alternative connection measures, and rotation logic
  - endogenous park placement through within-province choice sets and expected-return controls
  - concurrent policies through GIS access controls, period restrictions, and park-level coding
  - spillovers through nearby-city and province-level sensitivity analyses
  evidence_refs:
  - E1
  - E2
  - E3
  - E4
  - E5
readiness_blockers:
- The official directory and boundary notices establish qualifying park identity, approval dates, and spatial boundaries, but the complete paper's rotation/event-study code and exact city-leader tenure crosswalk are not independently reproduced here.
- Approval, construction, and operation can differ; use the directory date as an approval/establishment field and seek local implementation notices for a precise start date.
- The rotation argument is plausible and paper-reported, not a guarantee that every provincial turnover is unrelated to regional shocks or strategic city appointments.
- The paper's city and leader data cover a historical window and exclude some regions; do not generalize the 1988–2008 estimand to later industrial-park waves without a new audit.
method_transfer: null
superseded_by: null
deprecation_reason: null
---
## Institutional Background

Industrial parks in China are geographically delimited areas with a single management structure and preferential tax, tariff, land, credit, or regulatory arrangements. National- and provincial-level parks were formal place-based investments: the central or provincial government approved their status, while provincial leaders selected among cities within their jurisdictions. The official 2006 directory was issued after a national clean-up and review of development zones, and it recorded approved zones and their four-boundary arrangements [E3; E4].

The paper's object is narrower than “all industrial parks.” It focuses on qualifying national and provincial parks because many lower-level zones lacked formal approval and were affected differently by the 2003 clean-up. The historical working paper records 1,417 qualifying parks in 276 prefecture-level cities during the 1988–2008 application; the publisher article reports the rounded figure of more than 1,400 [E1; E2].

## What Changed

The policy exposure is a city's receipt of a new national- or provincial-level industrial park. Approval brings an intended bundle of infrastructure, land assembly, and preferential policies; the directory date should not be silently treated as the date of construction, operation, or firm entry. Park level, approval/establishment year, boundary, and later upgrades are separate fields [E3; E4].

The political-economy layer records who made the allocation decision. Provincial leaders had incentives to select cities with stronger expected growth or inequality effects, but could also reward connected city leaders. The study constructs workplace, birthplace, college, and faction ties from leader biographies, using workplace connections between provincial and city party secretaries as its main measure [E1; E2; E5].

## Implementation and Assignment

Construct a city-year choice set within each province. For each park, preserve its directory code, level, city, and approval/establishment date, and mark whether the city leader was in office at that date. Merge the leader-tenure and biography data to create the connection indicator. A city leader is connected when the specified relationship exists with the relevant provincial leader; the main baseline is a shared previous workplace.

The assignment-relevant change is provincial-leader turnover. Under the CCP's roughly five-year (or shorter) political cycle, a new provincial leader can change the connection status of an incumbent city leader without the city itself changing. The paper uses this rotation-generated change to address the concern that provincial leaders may appoint connected leaders to better cities. It is still necessary to verify the exact turnover date, that the city leader remains in office, and that the change is not timed to an unobserved park proposal [E1].

## Why This Creates Empirical Variation

The staggered park approvals generate policy exposure across cities and years, while the within-choice-set connection measure explains why otherwise comparable cities may win a park. The paper estimates park-placement models using expected economic growth, expected inequality changes, and connection status. It then compares growth returns for parks selected largely through political connection with returns for parks selected on economic and geographic fundamentals [E1; E2].

The useful treatment contract has two layers: (1) a city receiving a qualifying park, and (2) a rotation-induced connection switch that predicts park placement. Neither layer should be reduced to a national post dummy. A researcher interested in park effects must also decide whether the estimand is local growth, firm attraction, or province-wide allocation, because parks can draw activity from neighboring cities [E2; analytical inference].

## Identification Risks

Connections may reflect leader ability, factional selection, or appointment into cities that already have better prospects. Provincial turnover can be plausibly external without being fully random: a new leader may alter appointments, budgets, or park priorities in ways that affect all cities. The exact leader tenure and park-year crosswalk therefore matters more than the label “rotation shock” [E1; E5].

Approval is not implementation. The 2006 directory and boundary notices establish formal zones, but land servicing, construction, operation, and firm entry may follow later. The historical period also contains highway and airport expansion, trade liberalization, tax and land changes, the 2003 zone clean-up, and the 2008 stimulus. Finally, parks can generate spillovers or displacement across the provincial choice set, violating a simple untreated-neighbor comparison [E2; E3; E4].

## Data Requirements

The minimum contract is a city-year panel with a historical city crosswalk, park code/level/city/date/boundary, urban GDP and population outcomes, leader names and tenure dates, connection dimensions, and measures of access to highways, airports, railways, and ports. A careful replication keeps approval, construction, and operation dates separate and preserves the original directory code. The paper's leader biographies were hand-collected from Duxiu/CNKI and related sources; a new project should store source and confidence for each tie rather than only a binary connection flag [E2; E5].

## Evidence Notes

E1 is the published JUE article and establishes the paper's China setting, study window, rotation argument, connection measures, and reported placement/growth findings from the publisher page; it does not expose the underlying microdata. E2 is the inspectable NBER working paper and establishes the 276-city panel, 1,417 qualifying parks, Ministry directory source, GIS variables, connection dimensions, choice model, and sample exclusions; it is an earlier version and should not be treated as a substitute for the final article's appendix. E3 is the official NDRC/MNR/Construction Ministry announcement and establishes that the 2006 directory followed a formal national review and that unreviewed zones were not equivalent. E4 is an MLR boundary announcement reproduced in the Ministry of Commerce legal database and establishes the boundary/coordinate publication process; its mirror should be checked against the original archive before a machine-readable boundary file is served. E5 is an inspectable author working paper that explains the political-economy framework, leader biography construction, rotation rationale, and spillover assumptions.

The record is grounded as a Chinese place-based investment with an explicit political-rotation design, while retaining the exact crosswalk and timing limitations. It should be used for a conditional park-placement or connection design, not as evidence that every industrial park was randomly assigned.
