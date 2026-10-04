---
schema_version: 2
id: china-2020-2023-driving-restriction-episodes-intercity-travel
name: Six-Province City Driving-Restriction Episodes 2020-2023 and Intercity Travel Spillovers
aliases:
- 京津冀晋豫陕 机动车限行 2020-2023
- 尾号限行与单双号限行 城际出行溢出
- Li (JRS 2026) driving restrictions intercity travel
status: grounded
provenance:
  task_id: task-dafe7b3a2b09
scope:
  country: China
  regions:
  - Beijing (北京)
  - Tianjin (天津)
  - Henan (河南, 20 prefecture cities in the paper sample)
  - Hebei (河北, 11 prefecture cities)
  - Shanxi (山西, 11 prefecture cities)
  - Shaanxi (陕西, 10 prefecture cities)
  domains:
  - urban-economics
  - regional-economics
  - transportation
  - environmental-economics
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    City-level driving restrictions (weekday license-plate tail-number rotation
    and temporary odd-even episodes) enacted and suspended at different times
    across 52 prefecture-level cities in six adjacent Chinese
    provinces/province-level municipalities during 2020-2023 create city-day
    variation in the cost of driving. The paper application uses this
    variation to estimate how restrictions in one city shift daily intercity
    traveler flows between neighboring city pairs, including substitution
    toward unrestricted destinations. This is a China-internal policy regime
    with direct regional/urban content.
identity:
  instrument: >
    Municipal driving restrictions on private cars, coded at the city-day
    level in two rule types [E1]: (i) OD, the long-run weekday tail-number
    rotation (按车牌尾号工作日高峰时段区域限行) under which each vehicle is
    banned one weekday per week inside a designated area (Beijing: within the
    5th Ring Road, 7:00-20:00, per the annual 京政发 notices [E3]); treated as
    non-binding on weekends in the paper's coding; and (ii) OE, temporary
    odd-even (单双号) episodes, typically triggered by heavy-pollution alerts
    or major events, which bind daily including weekends [E1, inferred from
    code structure]. The paper's city-day panel codes 42 of 52 sampled cities
    as restricted on at least one day between 2020-01-10 and 2023-12-31 [E1,
    verified in sample_plot.dta].
  authority: >
    Each restriction episode is a municipal act: city people's governments or
    public security traffic bureaus issue the notices. Beijing's regime rests
    on annual municipal government notices (京政发〔2019〕6号, 京政发〔2020〕13号
    and successors), with COVID-era suspensions decided by the municipal
    government (暂缓实施 from 2022-12-22, resumed 2023-02-13) [E3]. Neighboring
    cities sometimes synchronized with Beijing (e.g. Langfang suspended and
    resumed in step with Beijing) [E3, reported]. The institutional
    documents behind the other cities' episodes were not individually
    inspected in this round.
  legal_identifiers:
  - 京政发〔2019〕6号 北京市人民政府关于实施工作日高峰时段区域限行交通管理措施的通告 (regime 2019-04-08 to 2020-04-05)
  - 京政发〔2020〕13号 北京市人民政府关于实施工作日高峰时段区域限行交通管理措施的通告 (regime 2020-06-01 to 2021-04-04)
  - Beijing municipal government COVID suspension of the weekday tail-number rule, effective 2022-12-22; resumption announced for 2023-02-13 (7:00-20:00, within 5th Ring Road excluding the ring road)
  - Per-city episode dates for the remaining 40 treated cities exist only as the paper author's coding in the replication package [E1]
  implementation_regime: >
    A patchwork regime: Beijing, Tianjin, Zhengzhou, Xi'an and a few other
    large cities ran (near-)continuous weekday tail-number rules with
    COVID-era suspensions, while many Henan/Hebei/Shanxi/Shaanxi prefecture
    cities switched restrictions on and off in short episodes, often
    winter pollution-driven odd-even spells [E1, verified coding pattern].
    Whether an episode also restricted non-locally-registered (outside)
    vehicles varies by episode and is coded separately [E1, restrict_outside].
  assignment_mechanism: >
    Exposure is assigned by city of residence/registration and calendar date:
    a vehicle is restricted when its city has an active episode on that day
    (and, for the tail-number rule, when the weekday matches its plate group).
    For intercity travel the paper treats an origin-destination pair as
    treated when the origin restricts any driving or the destination
    restricts outside vehicles on that date, and constructs a continuous
    spillover exposure equal to the population-weighted share of OTHER
    destinations under outside-vehicle restrictions for the same origin-date
    [E1, verified in code and sample.dta].
  parent:
  related_variations:
  - china-beijing-2008-private-car-driving-restriction-subway-premium
timeline:
  announcement: >
    Episode-specific and municipal; no single announcement. Beijing's
    post-COVID regime was announced late May 2020 for a 2020-06-01 start
    (京政发〔2020〕13号) [E3].
  effective: >
    Within the paper's coded panel, restriction episodes run between
    2020-01-10 and 2023-12-31 across 42 treated cities [E1, verified]. The
    underlying rules in Beijing/Tianjin predate 2020 (annual notices since
    2008/2014 respectively) [E3; E1 coded pre-2020 spells not in the sample
    window].
  implementation_start: '2020-01-10 (first day of the paper''s city-day panel)'
  implementation_end: '2023-12-31 (end of the paper''s analysis window; the Beijing/Tianjin regime continues beyond)'
  local_timing: >
    Highly heterogeneous by design: each city starts, suspends, and resumes
    episodes on its own dates; the replication package hard-codes the full
    city-by-city spell calendar (e.g. Beijing suspended 2022-12-22 to
    2023-02-12; Zhengzhou suspended after the 2021-07-20 flood until
    2021-09-13) [E1, verified in build.do Step 3.1].
  anticipation: >
    Episodes are typically announced days ahead (Beijing promises one week's
    advance notice for resumption [E3]); short announcement-to-effective lags
    make anticipation windows short but non-zero. Not formally tested in the
    inspected materials [analytical inference].
  last_verified: '2026-08-14'
assignment:
  unit: City-day (policy); origin-destination city-pair-day (design)
  treated: >
    42 of the 52 sampled cities experience at least one restricted day in
    2020-2023; treated pair-days are those with a restriction in the origin
    (any rule) or in the destination (episodes binding outside vehicles)
    [E1, verified].
  comparison_pool: >
    Pair-days in the same origin/destination cities on unrestricted dates,
    differenced out by date and origin and destination fixed effects; the 10
    never-restricted sample cities (吕梁, 商洛, 大同, 安康, 延安, 承德, 朔州,
    榆林, 汉中, 衡水) provide clean never-treated cells [E1, verified].
  rule: >
    City-day active restriction indicator; separately: episodes binding
    outside (non-local-plate) vehicles; population-weighted share of other
    destinations restricted for the same origin-date [E1].
  intensity: >
    Rule type varies in bite: odd-even episodes idle roughly half the fleet
    daily, tail-number rotation idles one fifth of the fleet one weekday per
    week; the paper also codes weekend suspension of the tail-number rule
    [E1, verified coding; magnitudes inferred from the rules].
  exemptions:
  - Police, fire, ambulance, engineering rescue; buses, coaches, taxis; pure-electric passenger cars; sanitation and funeral vehicles; diplomatic plates (Beijing notice exemption list) [E3]
  - Episodes not binding outside vehicles (coded restrict_outside = 0) [E1]
  - Weekends for the weekday tail-number rule; statutory holidays (restriction indicators zeroed) [E1]
  compliance: >
    Not directly observed in the inspected materials; enforcement is by
    traffic-police fines (Beijing: 100 yuan per violation period, reported
    media coverage) [E3, reported claim; not independently verified this
    round].
  exposure_construction: >
    flow = Baidu out-migration scale index of the origin city x the pairwise
    destination share from Baidu qianxi (迁徙) data, at daily frequency
    [E1, verified in build.do Step 4.1-4.3 and readme]. Treatment merges the
    author's city-day restriction calendar onto each pair-day; spillover
    exposure share_other2 is the population-weighted share of other
    destinations under outside-vehicle restrictions [E1].
  required_identifiers:
  - City (prefecture) of origin and destination
  - Calendar date (daily)
  - City population (市辖区人口) for spillover weights
  - Pair adjacency / distance for the extended sample
  spillovers: >
    The paper's object of interest: restrictions in one city shift travel
    toward unrestricted neighboring cities; share_other2 (and its interaction
    with own-pair restriction) measures cross-destination substitution
    [E1, verified in estimate.do Table 3]. Baseline estimate: restrictions in
    either endpoint reduce the pair's flow (-3.35, s.e. 0.87); the share of
    other destinations restricted raises the focal pair's flow (+6.84, s.e.
    2.01), with the interaction offsetting it when the focal pair is itself
    restricted (p=0.88 for the sum) [E1, reformatted Table 3].
research_compatibility:
  outcome_domains:
  - Intercity mobility / travel flows
  - Transportation mode and route substitution
  - Air-pollution-policy behavioral margins
  - Intracity work vs leisure travel intensity (secondary city-day design)
  affected_populations:
  - Private-car users in the 52 sampled cities
  - Intercity travelers between neighboring prefecture cities
  mechanism_channels:
  - Driving cost / legal prohibition
  - Spatial substitution of travel destinations
  - Pollution-avoidance travel (companion interpretation)
  best_for:
  - Estimating mobility responses to city-level traffic or environmental regulation with daily granularity
  - Studying spatial spillovers / leakage of local restrictions onto neighbors
  - Gravity-style OD-pair designs with two-way fixed effects and Conley spatial HAC errors
  not_good_for:
  - Long-run welfare or fleet-adjustment questions (multi-car purchase, EV switching); the window is short and COVID-contaminated
  - Designs needing continuous daily coverage 2020-2023; the Baidu pairwise shares are available only in intermittent windows
  - Questions requiring the exact legal text of each city's episode; only anchors are verified here
design:
  claim_type: causal
  affordances:
  - Staggered city-level policy switching with reversals
  - OD-pair treatment and continuous neighbor-exposure spillover variable
  - Event-study windows around episodes (13-day window in the paper)
  - Randomization/permutation inference over pair assignments
  candidate_designs:
  - Two-way fixed effects on pair-day flows (date + origin + destination FE)
  - Event study around destination-restriction episodes
  - Leave-one-pair-out and permutation p-value distributions
  identifying_variation: >
    Within-pair over-time variation in restriction status at both endpoints,
    plus cross-origin variation in the population-weighted share of other
    destinations restricted on the same date [E1].
  primary_strategy: >
    Gravity-style panel: reghdfe of daily pair flow on DR_either (restriction
    in origin or outside-binding restriction in destination), share_other2,
    and their interaction, absorbing date, origin, and destination effects,
    clustering by OD pair; COVID-surge city-days and public holidays excluded
    or zeroed [E1, verified in estimate.do].
  estimand: >
    Effect of an active driving-restriction day at either endpoint on the
    daily flow of travelers between the pair, and the cross-city spillover of
    other cities' restrictions onto the focal pair's flow [E1].
  treatment_variable: >
    DR_either (binary); share_other2 (continuous, 0-1); share_either
    interaction [E1].
  comparison_logic: >
    Same pair on unrestricted dates within 2020-2023; identification assumes
    that absent the policy, pair flows would follow common date shocks and
    time-invariant pair/origin/destination differences [E1, inferred design
    logic].
  estimation_notes: >
    Baseline N = 174,825 pair-day observations after dropping COVID-surge
    days; flow mean 12.96 (Baidu index x share x 100 scaling) [E1,
    reformatted Tables 1-3]. Robustness: province-by-year FE, Conley spatial
    HAC via reg2hdfespatial (dist 145.886 km, lag 10000), polynomial time
    trends, HSR-connection-weighted exposure (share_other3), distance-bin
    subsamples (adjacent / 200-350 km), work-vs-leisure intracity city-day
    specification [E1, estimate.do].
  assumptions:
  - 'No differential trends across pairs correlated with episode timing (event-study and trend robustness reported [E1])'
  - 'COVID exclusion windows remove lockdown confounding (coded 2020-01-23 to 2020-03-18, 2022-12-07 to 2022-12-21, plus city-specific surges) [E1, verified]'
  - 'Restriction episodes are not timed to pair-specific travel shocks [inferred]'
  diagnostics:
  - Event study with 13-day window around episodes (xtevent) [E1]
  - Permutation tests over random pair assignments (Figure 6-7) [E1]
  - Drop-one-pair-at-a-time p-value distribution [E1]
  - 'Neighbor-policy-adoption regression: a neighbor restriction predicts own-city adoption (0.09, s.e. 0.05), documenting correlated adoption [E1, Appendix Table 1]'
threats:
  - type: policy-endogeneity
    basis: reported
    condition: >
      Cities adopt or suspend restrictions in response to pollution, COVID,
      and congestion; adoption is correlated across neighbors (Appendix
      Table 1). If the same shocks move intercity flows, the design is
      contaminated; date FE absorb common but not city-specific shocks.
    evidence_refs: [E1]
    possible_diagnostics:
    - Event-study pre-trends
    - Controlling city-day air pollution (AQI/PM2.5) at both endpoints, as in the paper's robustness [E1]
  - type: measurement
    basis: documented
    condition: >
      The Baidu pairwise destination shares are available only in
      intermittent windows (the merged panel covers 24 non-contiguous months
      in 2020-2023, e.g. no data 2020-04 to 2020-09); 2021-11-26 and
      September 2023 are missing outright. Results may not generalize to the
      uncovered months, which include the first COVID summer [E1, verified
      in code comment and sample.dta].
    evidence_refs: [E1]
    possible_diagnostics:
    - Re-estimate within continuous sub-windows
    - Compare flows against alternative mobility series where available
  - type: spillovers-suta
    basis: inferred
    condition: >
      The estimand is itself a spillover, so SUTVA is violated by design;
      never-treated comparison cells still experience neighbor restrictions
      through share_other2.
    evidence_refs: [E1]
    possible_diagnostics:
    - Distance-ring subsamples (the paper's Table 4)
  - type: concurrent-policy
    basis: documented
    condition: >
      COVID mobility controls overlap the window; the paper zeroes or drops
      lockdown and surge days using Tencent case data, but residual
      pandemic behavior (fear-driven avoidance) is not separately identified
      [E1, verified coding; residual concern is inference].
    evidence_refs: [E1]
    possible_diagnostics:
    - Restrict to post-2023 sub-period
  - type: external-validity
    basis: inferred
    condition: >
      Sample is six adjacent northern provinces with high restriction
      density; LBS-based flows measure Baidu-app user movement, not all
      travelers.
    evidence_refs: [E1, E2]
    possible_diagnostics: []
empirical_requirements:
  contract_version: 1
  population: Daily intercity traveler flows between city pairs with origins in the 52 sample cities (destinations national, 84 in the baseline adjacent-pair sample)
  observation_unit: origin-city x destination-city x date
  geography_level: prefecture-level city
  time_start: '2020-01-10'
  time_end: '2023-12-31'
  minimum_frequency: daily
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields:
  - Daily origin-destination flow (Baidu qianxi out-migration index x pairwise share)
  - City-day restriction status with rule type and outside-vehicle scope
  - City population (weight), pair adjacency/distance
  - Daily weather at origin and destination; COVID case indicators; AQI/PM2.5 (controls)
  required_identifiers:
  - City name/code for origin and destination
  - Date
  treatment_key:
  - City-day restriction calendar (author-collected in the replication package; rebuildable from municipal notices)
  treatment_source: >
    Replication package build.do Step 3.1 hard-codes the episode calendar;
    the underlying municipal notices are public but were individually
    inspected here only for Beijing anchors [E1, E3].
  measurement_risks:
  - Baidu pairwise shares cover only 24 non-contiguous months of the window [E1, verified]
  - LBS sample is Baidu app users; coverage and weighting methodology are Baidu's, not the researcher's [E1, readme]
  - Flow = index x share construction, not observed counts [E1]
design_profiles:
- id: city-day-intracity
  label: City-day design for intracity work/leisure travel intensity (the paper's Table 5)
  design_families:
  - two-way fixed effects city-day panel
  when_to_use: >
    Use when the question concerns within-city travel intensity (work vs
    leisure trips) rather than intercity flows; unit is city x date over the
    same 52-city window.
  outcome_domains:
  - intracity travel intensity
  requirements:
    population: 52 sample cities, daily, 2020-01-10 to 2023-12-31
    observation_unit: city x date
    geography_level: prefecture-level city
    time_start: '2020-01-10'
    time_end: '2023-12-31'
    minimum_frequency: daily
    minimum_pre_periods: 0
    minimum_post_periods: 0
    required_fields:
    - Intracity travel intensity for work and for leisure (Baidu)
    - City-day restriction status and share of own-city population restricted
    - Weather and COVID indicators
    required_identifiers: [city, date]
    treatment_key:
    - City-day restriction calendar (same source as the main contract [E1])
evidence:
- id: E1
  source_type: replication
  citation: 'Li, Wenbo. 2025. "The Spillover Effect of Driving Restrictions on Intercity Travel." Mendeley Data, V4. doi:10.17632/34r56jktx7.4'
  url: https://data.mendeley.com/datasets/34r56jktx7/4
  date: '2025-12-10'
  supports:
  - identity.instrument
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.local_timing
  - timeline.implementation_start
  - timeline.implementation_end
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.exemptions
  - assignment.exposure_construction
  - assignment.spillovers
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - design.diagnostics
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.treatment_source
  - empirical_requirements.measurement_risks
  verification_status: verified
  access_level: replication
  locator: >
    Downloaded and inspected 2026-08-14 (55 MB data_code.zip). readme.pdf
    (data provenance: Baidu qianxi, Tencent feiyan, NOAA GSOD);
    code/build.do Steps 3.1-4.14 (hard-coded city-day episode calendar for
    52 cities, OD/OE rule types, restrict_outside, COVID and holiday
    exclusions, spillover-share construction); code/estimate.do (Tables 1-6,
    event study via xtevent window(13), permutation and leave-one-out
    p-values, Conley HAC via reg2hdfespatial); data/sample_plot.dta (75,504
    city-days, 2020-01-10 to 2023-12-31; exactly 42 of 52 cities ever
    restricted); data/sample.dta (193,543 pair-days, 52 origins x 84
    destinations, 24 non-contiguous months);
    figures_tables/table2/table3/atable1 reformatted outputs. The package
    establishes the paper's coding and design; it does not independently
    verify the legal text of each municipal episode.
- id: E2
  source_type: paper
  citation: 'Li, Wenbo. 2026. "The Spillover Effect of Driving Restrictions on Intercity Travel." Journal of Regional Science 66(3):813-829. doi:10.1111/jors.70043'
  url: https://doi.org/10.1111/jors.70043
  date: '2025-12-22'
  supports:
  - scope.china_relevance
  - identity.instrument
  verification_status: reported
  access_level: abstract
  locator: >
    Wiley landing page blocked (HTTP 403) on 2026-08-14; bibliographic
    metadata (volume 66, issue 3, pages 813-829, first published
    2025-12-22) and the abstract claim of 42 cities across six adjacent
    provinces/municipalities 2020-2023 with high-frequency smartphone
    location data were recovered from search-index snippets of the Wiley
    page and a cross-citing article. Full text not inspected; abstract-level
    claims are corroborated by E1.
- id: E3
  source_type: policy-document
  citation: 'Beijing Municipal People''s Government. 京政发〔2020〕13号 关于实施工作日高峰时段区域限行交通管理措施的通告 (2020-05, effective 2020-06-01); Beijing municipal COVID suspension notice effective 2022-12-22 (beijing.gov.cn); resumption from 2023-02-13.'
  url: https://www.beijing.gov.cn/fuwu/bmfw/bmzt/whts/xxwh/202212/t20221229_2886485.html
  date: '2020-06-01'
  supports:
  - identity.authority
  - identity.legal_identifiers
  - timeline.announcement
  - timeline.anticipation
  - assignment.exemptions
  verification_status: verified
  access_level: official-document
  locator: >
    Inspected 2026-08-14: (i) beijing.gov.cn portal page confirming the
    municipal-government-approved suspension of the weekday tail-number rule
    from 2022-12-22 with a promise of one week's advance notice for
    resumption; (ii) full text of 京政发〔2020〕13号 as reproduced by
    People''s Daily (bj.people.com.cn, 2020-05-29) and cross-referenced in
    Beijing traffic-bureau notices (gaj.beijing.gov.cn 2020-2021 holiday
    adjustment notices), establishing the 2020-06-01 to 2021-04-04 regime,
    7:00-20:00 within the 5th Ring Road (excluding the ring road), the
    five-group 13-week rotation, and the exemption list; the official
    gazette PDF (beijing.gov.cn W020200609567485405208.pdf) was downloaded
    but uses a non-extractable font encoding. The 2023-02-13 resumption and
    the Beijing-synchronized Langfang suspension/resumption rest on
    official-media reproductions of municipal notices (新京报 2023-03-27
    quoting the 通告; 廊坊本地宝 reproducing the Langfang decision), treated
    as reported claims. These anchor documents verify the regime type and
    Beijing/Tianjin timing only; they do not verify other cities' episodes.
design_applications:
- paper: 'Li, Wenbo. 2026. "The Spillover Effect of Driving Restrictions on Intercity Travel." Journal of Regional Science 66(3):813-829.'
  doi: 10.1111/jors.70043
  journal: Journal of Regional Science
  year: 2026
  research_question: >
    Do city driving restrictions reduce intercity travel to and from the
    restricted city, and do they divert travelers toward unrestricted
    neighboring cities?
  population: >
    Daily traveler flows between city pairs whose origins are the 52 sample
    cities in Beijing, Tianjin, Henan, Hebei, Shanxi, and Shaanxi
    (2020-2023).
  outcome: Daily origin-destination flow of travelers (Baidu out-migration index x pairwise destination share)
  data_used:
  - Baidu qianxi (迁徙) migration index and pairwise destination shares
  - Author-collected city-day driving-restriction calendar
  - Tencent COVID-19 case dynamics; NOAA GSOD weather; city AQI/PM2.5; district population; HSR opening dates
  treatment_encoding: >
    City-day restriction indicators (DR_any; odd-even OE; outside-vehicle
    binding restrict_outside), merged to pair-days as DR_either; continuous
    spillover exposure share_other2 = population-weighted share of other
    destinations restricted.
  comparison: >
    Within-pair over time with date, origin, and destination fixed effects;
    COVID-surge city-days dropped; holiday restriction indicators zeroed.
  empirical_design: Gravity-style two-way fixed effects; event study (13-day window); permutation and leave-one-pair-out inference; Conley spatial HAC errors.
  assumptions:
  - No differential pair trends correlated with episode timing
  - COVID exclusions adequately remove lockdown confounding
  - Episode timing is not driven by pair-specific travel shocks
  threats_addressed:
  - Air-pollution confounding (AQI/PM2.5 controls at both endpoints)
  - Spatial correlation of errors (Conley HAC; province-by-year FE)
  - Anticipation and pre-trends (event study)
  evidence_refs: [E1, E2]
method_transfer: null
readiness_blockers:
- 'Per-city episode dates outside the Beijing/Tianjin anchors rest on the author''s coding (E1); municipal notices for the other 40 treated cities were not individually inspected. Ground each city''s spell against its official notice before reusing the calendar in a new study.'
- 'Paper full text inaccessible (Wiley 403); paper-reported design claims beyond the abstract are inferred from the replication code (E1).'
- 'Baidu qianxi pairwise share data are only intermittently available and the raw scrape is not redistributed; a new user must re-collect from qianxi.baidu.com or find an archived copy [E1, readme].'
superseded_by:
deprecation_reason:
---

## Institutional Background

Chinese cities restrict car use through two municipal instruments. The older
is the weekday tail-number rotation (按车牌尾号工作日高峰时段区域限行): each
vehicle is prohibited from driving one weekday per week inside a designated
zone, with the five plate groups rotating every 13 weeks; Beijing has run
this regime continuously since October 2008 under annual 京政发 notices, and
Tianjin, Zhengzhou, Xi'an and other large cities adopted similar standing
rules [E3; E1]. The second is the temporary odd-even episode (单双号限行),
typically declared for days to weeks under heavy-pollution alerts or major
events, which halves the fleet daily [E1, coding pattern; the rule
description is analytical inference from the instrument names and verified
anchor documents].

During 2020-2023 this patchwork interacted with COVID-19: Beijing suspended
its standing rule from 2020-02-03 to 2020-05-31 and again from 2022-12-22 to
2023-02-12, and many prefecture cities switched episodes on and off, often
synchronized with neighbors (Langfang explicitly synchronized with Beijing)
[E3, verified for Beijing, reported for Langfang].

## What Changed

Nothing changed nationally; the variation is the staggered municipal
switching of restrictions. In the paper's coded panel of 52 cities (Beijing,
Tianjin, and all prefecture cities of Henan, Hebei, Shanxi, Shaanxi),
exactly 42 cities have at least one restricted day between 2020-01-10 and
2023-12-31, ranging from single-day episodes (Zhangjiakou, 4 days) to
near-continuous regimes (Zhengzhou, 1,343 coded days) [E1, verified in
sample_plot.dta]. Episodes differ in whether they bind non-locally
registered (outside) vehicles, which is what matters for intercity travel
[E1].

## Implementation and Assignment

A traveler flow between origin i and destination j on date t is exposed when
city i restricts any local driving or city j restricts outside vehicles on
date t. The paper additionally constructs, for each origin-date, the
population-weighted share of other destinations under outside-vehicle
restrictions, so that a pair with no own restriction can still be partially
exposed through its alternatives [E1, verified]. Ten never-restricted cities
anchor the comparison pool. Holiday dates are zeroed out and COVID-surge
city-days are excluded [E1].

## Why This Creates Empirical Variation

The assignment-generating feature is staggered municipal timing with
frequent reversals, not a one-off national reform. Within a pair, the same
origin-destination cell alternates between treated and untreated dozens of
times; across origins on the same date, exposure through other destinations
varies with neighbors' independent episode calendars. This supports a
two-way fixed-effects gravity design at the pair-day level and event
studies around episode starts, with the central caveat that adoption is
correlated across neighbors [E1, Appendix Table 1].

## Identification Risks

Episode timing responds to pollution and COVID, both of which move travel
directly; the paper conditions on city-day AQI/PM2.5 and excludes surge
windows, but a residual correlation between a city's outbreak severity and
its restriction calendar is plausible [E1; analytical inference]. The
spillover estimand deliberately violates SUTVA. The Baidu outcome measures
app-user movement with proprietary weighting, and pairwise destination
shares exist for only 24 non-contiguous months, so estimates interpolate a
patchy window [E1, verified]. Anticipation is short (days to one week) but
untested [E3; analytical inference].

## Data Requirements

A replicating researcher needs daily OD-pair flows (Baidu qianxi, requiring
re-collection since raw data are not redistributed), a city-day restriction
calendar with rule type and outside-vehicle scope (the author's calendar is
in the replication package but should be re-grounded against municipal
notices), city population for weights, pair adjacency/distance, daily
weather, COVID case series, and air-quality controls [E1].

## Evidence Notes

E1 (the Mendeley replication package) is the load-bearing source: it was
downloaded and its code, sample files, and outputs were inspected directly;
it establishes the paper's coding and estimation, not the underlying legal
facts. E2 is abstract-level only because the Wiley page blocks automated
access; its claims are used only where corroborated by E1. E3 verifies the
institutional regime and Beijing's 2020-2023 timing from official documents
and official-media reproductions; the official gazette PDF of
京政发〔2020〕13号 was retrieved but its font encoding is not text-extractable,
so the verbatim text relied on the People's Daily reproduction
cross-referenced against traffic-bureau notices. The remaining 40 treated
cities' episodes are unverified author coding; this is the record's main
open boundary and is listed in readiness_blockers.
