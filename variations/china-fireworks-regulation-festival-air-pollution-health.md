---
schema_version: 2
id: china-fireworks-regulation-festival-air-pollution-health
name: Chinese City Fireworks Bans during the Spring Festival and Festival-Season Air Pollution and Health
aliases:
- China fireworks regulation and festival air pollution
- Prefecture fireworks bans CNY exposure
- 烟花爆竹禁放与春节期间空气污染健康
status: contested
provenance:
  task_id: task-adcbd3a30f75
scope:
  country: China
  regions:
  - Mainland China prefectures adopting fireworks restrictions or prohibitions, 2015-2018
  domains:
  - urban-economics
  - environmental-economics
  - public-health
  - regional-economics
  - local-government
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    This record captures the paper-used exposure from local Chinese fireworks bans:
    prefecture governments restricted or prohibited setting off fireworks and
    firecrackers during the Spring Festival window in a staggered wave beginning
    around 2015, which Chen, Jiang, Liu and Song (RSUE 2022) use as a staggered
    difference-in-differences assignment for festival-season PM2.5 and health
    outcomes. It is a distinct instrument from the national Air Pollution Action
    Plan, pollution monitoring, driving restrictions, and winter heating policies,
    although those overlap in the same years and must be kept separate in design.
identity:
  instrument: >
    Local-government restrictions or prohibitions on setting off fireworks and
    firecrackers during the Spring Festival (Chinese New Year) window, adopted by
    Chinese prefecture-level and provincial-level cities in a staggered wave
    beginning around 2015. The usable exposure is the prefecture-by-year ban status
    effective before the festival season, not a single national decree.
  authority: >
    County-level and above local people's governments exercise the authority,
    delegated by Article 28 of the State Council Regulations on the Safety
    Management of Fireworks and Firecrackers, to determine times, places, and
    categories in which setting off is restricted or prohibited. Municipal
    people's congresses and governments implement this through local ordinances,
    regulations, and annual notices; public security organs enforce them.
  legal_identifiers:
  - 国务院令第455号 烟花爆竹安全管理条例, State Council order issued 2006-01-21, effective on promulgation; revised by 国务院令第666号 2016-02-06; Article 28 delegates restriction/prohibition authority to local governments
  - 上海市烟花爆竹安全管理条例, revised ordinance passed 2015-12-30, effective 2016-01-01, banning setting off and sales inside the Outer Ring Expressway
  - 北京市烟花爆竹安全管理规定, amendment passed 2017-12-01, effective on promulgation, converting the area within the Fifth Ring Road from restricted to prohibited
  implementation_regime: >
    Local rules distinguish complete prohibition (禁放, no setting off in the
    designated area) from restricted regimes (限放, setting off allowed only in
    designated times, places, or categories). Bans typically apply to the
    festival window around Chinese New Year, often paired with sales restrictions,
    sales-point curtailment, and fines for violations. The statutory prohibited
    places of Article 30 of Order 455 apply everywhere. The wave's implementation
    is local: Shanghai prohibited setting off and sales within the Outer Ring
    Expressway from 2016-01-01, and Beijing converted the Fifth Ring area to a
    prohibition from the 2018 festival.
  assignment_mechanism: >
    A prefecture is treated when its local government adopts a fireworks
    restriction or prohibition effective for a Spring Festival season. The paper
    codes the staggered adoption of prefectures from 2015 through 2018 and
    separates strict (complete prohibition) from moderate (time- or
    place-restricted) versions, so exposure is a prefecture-year festival-season
    indicator rather than a nationwide treatment date.
  parent: null
  related_variations:
  - china-air-pollution-action-plan-firm-emissions
  - china-pollution-information-disclosure
  - china-heating-policy-air-pollution-wtp
  - china-huai-river-heating-air-pollution
timeline:
  announcement: '2015'
  effective: '2015'
  implementation_start: 2015
  implementation_end: 2018
  local_timing: >
    The enabling framework dates to 2006: Article 28 of State Council Order 455
    delegates to county-and-above local governments the power to determine when
    and where setting off is restricted or prohibited. The paper-used staggered
    wave begins around 2015: its coding reaches 47 regulated prefectures in 2015
    and nearly 160 by end-2018 (preview-reported). Independent dated examples of
    the same wave: Shanghai's revised ordinance banning setting off and sales
    inside the Outer Ring Expressway passed 2015-12-30 and took effect
    2016-01-01; Beijing's amendment converting the Fifth Ring area from
    restricted to prohibited passed 2017-12-01 and was first enforced at the
    2018 Spring Festival. The wave continued after 2018; the paper's clock ends
    around 2018, so a later researcher must not assume later bans share the
    paper's sample window.
  anticipation: >
    Bans and their sales-point curtailments were announced before the festival
    season, sometimes months ahead. Setting-off behavior, sales, and possibly
    pollution can therefore respond before the official effective date, and
    pre-period pollution in adopting cities may already reflect announced bans.
  last_verified: '2026-08-13'
assignment:
  unit: >
    Prefecture (prefecture-level city) by Spring Festival season, with daily
    festival-window outcomes; the paper's health application additionally uses
    internet search-index series during the festival window.
  treated: >
    Prefectures that adopted a fireworks restriction or prohibition effective
    before the festival season, coded separately as strict (complete
    prohibition) or moderate (restricted regime), in the staggered 2015-2018
    wave.
  comparison_pool: >
    Not-yet-regulated prefectures observed in the same festival seasons, using
    prefecture and time fixed effects with weather and holiday controls; the
    paper also interacts initial prefecture socioeconomic characteristics with
    year dummies.
  rule: >
    Code a prefecture-year indicator equal to strict, moderate, or none
    according to the local rule effective for the Spring Festival window, with
    the window running from Chinese New Year's Eve through the Lantern Festival
    (paper coding, preview-reported). CNY dates shift between late January and
    mid-February and must be taken from the Chinese lunar calendar for each
    year.
  intensity: >
    The strict-versus-moderate distinction is the paper's main intensity
    margin: strict prohibitions are reported to reduce festival-month PM2.5 by
    about 8 percent, while moderate restrictions are reported insignificant.
    The exact classification rule applied to each prefecture is not recovered
    from the full text.
  exemptions:
  - 'Statutory prohibited places (Article 30 of Order 455) are banned everywhere: heritage units, transport hubs, flammable and explosive production and storage units, power transmission facilities, medical institutions, schools, and forest and grassland fire-prevention areas.'
  - Restricted regimes allow setting off in designated times and places; for example, Beijing's restricted zone outside the Fifth Ring permits setting off on CNY Eve and Day 1 all day and from 07:00-24:00 on Days 2-15.
  compliance: >
    Enforcement is by public security organs with fines (for example, 100-500
    yuan for individuals under Shanghai's and Beijing's rules) and sales-point
    controls, but actual compliance across prefectures is not recovered from the
    accessible sources; the paper's strict/moderate coding is a stated-rule
    measure, not a compliance measure.
  exposure_construction: >
    Merge a prefecture-year ban status (strict, moderate, none) to daily city
    PM2.5 and to festival-window health search-index series; keep separate
    indicators for the two regime types and use lunar-calendar CNY dates to
    define the window; interact with weather and holiday controls as the paper
    reports.
  required_identifiers:
  - Stable prefecture (地级市) code and year
  - Lunar calendar Spring Festival dates per year (CNY Eve through Lantern Festival)
  - Daily station-level PM2.5 matched to city boundaries
  - Health search-index series for respiratory and cardiovascular terms (paper-reported construction)
  spillovers: >
    Residents of banned cities can travel to nearby unbanned areas to set off
    fireworks, and migrant population flows over CNY change the urban population
    and thus per-capita exposure; both can bias a prefecture-only comparison and
    are not recovered as measured quantities here.
research_compatibility:
  outcome_domains:
  - air-pollution
  - health
  - public-safety
  - festival-consumption
  affected_populations:
  - Urban residents of regulated prefectures during the Spring Festival window
  - City-level ambient PM2.5 measured during festival months
  - Internet search volumes for respiratory and cardiovascular conditions (paper-reported health proxy)
  mechanism_channels:
  - Festival-season fireworks emissions directly raise ambient particulate matter
  - Pollution exposure raises respiratory and cardiovascular illness search/incidence during the festival period
  - Sales-point curtailment and fines reduce setting-off volume
  best_for:
  - 'Staggered DID or event-study designs measuring the short-run, festival-season effect of local bans on ambient PM2.5 and health proxies, with treated and not-yet-treated prefectures observed over several CNY seasons.'
  not_good_for:
  - 'Year-round or industrial air pollution policy inference; mechanisms that require the full prefecture list and per-city effective dates without recovering the paper''s appendix; claims that local ban adoption is exogenous to pollution, health, or central environmental pressure.'
design:
  claim_type: reduced-form
  affordances:
  - staggered-rollout
  - event-study
  - seasonal-window
  candidate_designs:
  - Staggered DID with prefecture and year fixed effects, weather and holiday controls, and initial-socioeconomic-by-year interactions
  - Event-study around first regulated festival season
  - Strict-versus-moderate regime comparison within adopters
  identifying_variation: >
    The staggered adoption of local fireworks bans across prefectures and years
    within the 2015-2018 wave: within-prefecture variation in ban status around
    the Spring Festival window, contrasted with not-yet-regulated prefectures in
    the same festival seasons.
  primary_strategy: difference-in-differences
  estimand: >
    The effect of adopting fireworks regulation (strict or moderate) on
    festival-season ambient PM2.5 and on festival-window health proxies in
    adopting prefectures relative to not-yet-adopting prefectures, under the
    paper's parallel-trends and no-anticipation assumptions.
  treatment_variable: >
    Prefecture by festival-season indicator of ban status, coded strict or
    moderate; separate indicators allow the reported 8 percent strict effect
    and insignificant moderate effect.
  comparison_logic: >
    Within-prefecture before-after change in festival-season outcomes versus
    contemporaneous changes in not-yet-regulated prefectures, with prefecture
    and time fixed effects; the festival window and CNY date shifts are
    seasonality controls rather than treatment.
  estimation_notes: >
    The paper reports prefecture and time fixed effects, weather and holiday
    controls, and interactions of initial prefecture socioeconomic
    characteristics with year dummies, consistent with a staggered DID where
    adoption timing may correlate with local conditions. The exact prefecture
    list, strict/moderate coding rule, festival-month definition, sample end
    year, and clustering choices are in the subscriber-restricted full text and
    appendices and are not recovered here.
  assumptions:
  - Parallel festival-season pollution and health trends between adopters and not-yet-adopters
  - No anticipation, so announced bans do not shift setting-off behavior before the coded effective season
  - No differential seasonal shocks correlated with adoption timing (including CNY date shifts, weather, heating, and other environmental programs)
  - Stated-rule coding captures effective local bans (enforcement and compliance do not systematically differ)
  diagnostics:
  - Event-study estimates around the first regulated festival season
  - Placebo or falsification on non-festival seasons
  - Controls for CNY timing shifts, weather, and holiday dates
  - Robustness separating strict from moderate regimes
threats:
  - type: endogenous adoption
    basis: inferred
    condition: >
      Cities chose whether and when to ban fireworks; adoption timing may respond
      to local pollution, health, fiscal, or central-policy pressure, so the
      timing of treatment is not random.
    evidence_refs:
    - E1
    - E2
    - E6
    possible_diagnostics:
    - Compare early versus late adopters on pre-ban pollution and socioeconomic levels
    - Event-study leads
    - Interactions of initial socioeconomic characteristics with year dummies as reported
  - type: contemporaneous policy overlap
    basis: inferred
    condition: >
      The 2015-2018 ban wave coincides with the tail of the 2013 Air Pollution
      Action Plan, monitoring expansion, driving restrictions, and winter heating
      policies; festival-season improvements could be confounded by those
      programs.
    evidence_refs:
    - E1
    - E6
    possible_diagnostics:
    - Control for or exclude cities under other clean-air programs
    - Compare outcomes outside the festival window
  - type: seasonality and calendar shift
    basis: inferred
    condition: >
      CNY moves between late January and mid-February and the festival window
      spans weeks with strong seasonal pollution and heating patterns, so the
      window definition and year fixed effects must handle calendar shifts.
    evidence_refs:
    - E2
    possible_diagnostics:
    - Lunar-calendar dating of the window
    - Placebo windows in adjacent non-festival weeks
  - type: spillovers and sorting
    basis: inferred
    condition: >
      Setting off can move across city borders, and CNY migration changes urban
      population composition, so city-level PM2.5 and search-index outcomes
      capture net regional behavior rather than only local compliance.
    evidence_refs:
    - E2
    possible_diagnostics:
    - Border or neighbor analysis
    - Population-flow controls
  - type: measurement of health
    basis: reported
    condition: >
      The health outcomes are reported through internet search-index proxies for
      respiratory and cardiovascular disease; the exact terms, index coverage,
      and their validity for actual disease incidence are not recovered from the
      accessible sources.
    evidence_refs:
    - E2
    possible_diagnostics:
    - Validate search proxies against hospital or insurance data where available
  - type: enforcement heterogeneity
    basis: inferred
    condition: >
      Stated bans differ from realized compliance; strictness of enforcement
      (fines, checkpoints, sales points) varies across prefectures and is not
      measured in the accessible sources.
    evidence_refs:
    - E3
    - E4
    - E5
    possible_diagnostics:
    - Sales-point and enforcement data as intensity measures
    - Robustness of results to excluding low-enforcement cities
empirical_requirements:
  contract_version: 1
  population: Chinese prefecture-level cities during Spring Festival seasons, roughly 2014-2019
  observation_unit: Prefecture by day (festival window) or prefecture by festival season, plus daily city PM2.5 and search-index series
  geography_level: Prefecture (地级市)
  time_start: '2014'
  time_end: '2019'
  minimum_frequency: Daily
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - Daily city-level PM2.5 from monitoring stations
  - Lunar calendar CNY and Lantern Festival dates per year
  - Prefecture-year ban status (strict, moderate, none) with effective date before the festival window
  - Weather controls (wind, precipitation, temperature) during the window
  - Health search-index series for respiratory and cardiovascular terms (paper-reported construction)
  - Prefecture administrative code and stable boundaries
  required_identifiers:
  - Prefecture code (统计用区划代码) and year
  - CNY calendar dates
  - Station-to-city mapping for PM2.5
  treatment_key:
  - prefecture-year ban status (strict/moderate/none)
  treatment_source: >
    Local government ordinances and annual notices (for example, the Shanghai
    ordinance effective 2016-01-01 and the Beijing amendment effective for the
    2018 festival); the paper's exact coded list and dates are in the
    subscriber-restricted full text and appendices.
  measurement_risks:
  - PM2.5 monitoring coverage and station relocation over the sample
  - Search-index proxies for disease are not clinical incidence
  - Prefecture boundary changes and CNY migration alter the urban population denominator
  - Stated-rule coding may misstate realized enforcement
design_profiles: []
evidence:
  - id: E1
    source_type: paper
    citation: 'Chen, Shiyi, Lingduo Jiang, Wanlin Liu, and Hong Song. 2022. "Fireworks regulation, air pollution, and public health: Evidence from China." Regional Science and Urban Economics 92:103722. DOI: 10.1016/j.regsciurbeco.2021.103722.'
    url: https://doi.org/10.1016/j.regsciurbeco.2021.103722
    date: 2022
    supports:
    - identity.instrument
    - identity.assignment_mechanism
    - timeline.implementation_start
    - timeline.implementation_end
    - assignment.unit
    - assignment.treated
    - assignment.comparison_pool
    - assignment.intensity
    - design.identifying_variation
    - design.primary_strategy
    - design.estimand
    - design.treatment_variable
    - design.comparison_logic
    - design.estimation_notes
    - design.diagnostics
    - research_compatibility.outcome_domains
    - research_compatibility.affected_populations
    - research_compatibility.mechanism_channels
    - design_applications.paper
    - design_applications.research_question
    - design_applications.outcome
    - design_applications.data_used
    verification_status: verified
    access_level: abstract
    locator: >
      Publisher abstract (PII S016604622100082X) plus the matching Gale,
      scite.ai, and Peeref records, inspected 2026-08-13, establish the final
      article identity, the staggered implementation of fireworks regulation
      across Chinese prefectures since 2015, the DD design with prefecture and
      time fixed effects, weather and holiday controls, and initial
      socioeconomic-by-year interactions, the 8 percent festival-month PM2.5
      reduction under strict regulation, the insignificant moderate effect, the
      respiratory and cardiovascular health improvement, and the fireworks
      industry revenue share of about 0.04 percent of all-industry sales in
      2018. The abstract does not establish the prefecture list, coding rule,
      sample end year, or health-data construction.
  - id: E2
    source_type: paper
    citation: 'ScienceDirect article preview, PII S016604622100082X, and its previously recorded inspection, state/runs.jsonl run-5537ab82466b, 2026-08-12.'
    url: https://www.sciencedirect.com/science/article/pii/S016604622100082X
    date: '2026-08-12'
    supports:
    - timeline.local_timing
    - assignment.rule
    - assignment.exposure_construction
    - assignment.spillovers
    - research_compatibility.affected_populations
    - empirical_requirements.required_fields
    - empirical_requirements.treatment_key
    verification_status: reported
    access_level: abstract
    locator: >
      The preview inspected by the preceding screen run records the paper-used
      festival window from Chinese New Year's Eve through the Lantern Festival,
      strict and moderate regulation versions, 47 regulated prefectures in 2015
      and nearly 160 by end-2018, and internet search-index proxies for
      respiratory and cardiovascular disease. These details are preview-reported
      and were not re-inspected in the full text.
  - id: E3
    source_type: policy-document
    citation: '国务院令第455号 烟花爆竹安全管理条例 (State Council Order No. 455, Regulations on the Safety Management of Fireworks and Firecrackers), adopted 2006-01-11 at the 121st State Council executive meeting, promulgated 2006-01-21, effective on promulgation; revised by Order No. 666, 2016-02-06. Articles 28 and 30.'
    url: https://www.gov.cn/gongbao/content/2006/content_219931.htm
    date: '2006-01-21'
    supports:
    - identity.authority
    - identity.legal_identifiers
    - identity.implementation_regime
    - identity.assignment_mechanism
    - timeline.local_timing
    - assignment.rule
    - assignment.exemptions
    verification_status: verified
    access_level: official-document
    locator: >
      Official State Council gazette page, 2006 issue 7, fetched 2026-08-13.
      Article 28 states that setting off fireworks shall comply with relevant
      laws and that county-level and above local people's governments may
      determine, according to local conditions, the times, places, and
      categories in which setting off is restricted or prohibited. Article 30
      lists statutory prohibited places. The regulation establishes the
      delegation framework; it does not establish which prefectures banned
      fireworks in which years.
  - id: E4
    source_type: policy-document
    citation: '上海市烟花爆竹安全管理条例 (Shanghai Municipal Regulations on the Safety Management of Fireworks and Firecrackers), revised ordinance passed 2015-12-30 by the Standing Committee of the 14th Shanghai Municipal People''s Congress, effective 2016-01-01.'
    url: https://www.thepaper.cn/newsDetail_forward_1415035
    date: '2015-12-30'
    supports:
    - timeline.local_timing
    - assignment.rule
    - assignment.compliance
    - assignment.exemptions
    verification_status: reported
    access_level: official-document
    locator: >
      State and Shanghai media reports of 2015-12-30 and 2015-12-31 (thepaper.cn,
      chinadaily.com.cn, cneb.gov.cn) report the ordinance's passage and
      content: complete prohibition of setting off and sales inside the Outer
      Ring Expressway including during the Spring Festival, a city-wide ban on
      heavy-pollution days, fines of 100-500 yuan for individuals, and penalties
      up to 100,000 yuan for illegal storage. The official ordinance text was
      not independently inspected here.
  - id: E5
    source_type: policy-document
    citation: '北京市烟花爆竹安全管理规定 (Beijing Municipal Regulations on the Safety Management of Fireworks and Firecrackers), amendment passed 2017-12-01 by the Standing Committee of the 14th Beijing Municipal People''s Congress, effective on promulgation; new Article 14 designates the area within the Fifth Ring Road as a prohibition zone.'
    url: http://www.xinhuanet.com/politics/2017-12/02/c_1122046013.htm
    date: '2017-12-01'
    supports:
    - timeline.local_timing
    - assignment.rule
    - assignment.exemptions
    - assignment.compliance
    verification_status: reported
    access_level: official-document
    locator: >
      Xinhua (2017-12-02), chinanews.com.cn (2017-12-15, 2018-02-07, 2018-02-09),
      and the Beijing Municipal People's Congress website report the amendment
      and its first enforcement at the 2018 Spring Festival: the Fifth Ring area
      converted from restricted to prohibited, restricted-zone hours of CNY Eve
      through Day 15, sales points cut from 511 to 87, and fines of 100-500 yuan
      for individuals. The official amendment text was not independently
      inspected here.
  - id: E6
    source_type: scholarship
    citation: 'Xinhua and CCTV report, 2017-01-27: 多地明确春节禁燃措施 违规放鞭炮将面临这些处罚.'
    url: https://news.cctv.com/2017/01/27/ARTIuoedqEclpQicAj0N12FK170127.shtml
    date: '2017-01-27'
    supports:
    - timeline.local_timing
    - assignment.compliance
    - threats.condition
    verification_status: reported
    access_level: metadata
    locator: >
      The report documents tightening measures for the 2017 festival across many
      cities: Beijing's heavy-pollution-day city-wide ban, 511 approved sales
      points (down 208), no outlets inside the Third Ring, a sales window cut
      from 20 to 10 days, and instructions that officials refrain from setting
      off; Shanghai's real-name purchase since 2016 and seven legal outlets in
      2017; and 100-500 yuan fines. This establishes the wave's breadth and
      enforcement texture, not the paper's coding.
design_applications:
- paper: 'Fireworks regulation, air pollution, and public health: Evidence from China'
  doi: 10.1016/j.regsciurbeco.2021.103722
  journal: Regional Science and Urban Economics
  year: 2022
  research_question: >
    Does local fireworks regulation during the Spring Festival improve ambient
    air quality and public health in Chinese prefectures?
  population: >
    Chinese prefectures observed over festival seasons during the staggered
    2015-2018 rollout, with regulated prefectures compared to not-yet-regulated
    ones.
  outcome: >
    Ambient PM2.5 during festival months and internet search-index proxies for
    respiratory and cardiovascular disease during the festival window.
  data_used:
  - 'Daily prefecture PM2.5 monitoring data.'
  - 'Festival-window search-index health proxies reported by the paper.'
  - 'Prefecture-by-year fireworks regulation status coded strict or moderate; exact series and sample years remain unreconstructed.'
  treatment_encoding: 'Prefecture-by-festival-season strict, moderate, or none status, as reported in the accessible paper materials; the exact coded list and effective dates remain unresolved.'
  comparison: 'Regulated prefectures compared with not-yet-regulated prefectures in the same festival seasons, subject to unresolved adoption and spillover concerns.'
  empirical_design: 'Paper-reported staggered difference-in-differences and event-study with prefecture and time fixed effects, weather and holiday controls, and initial socioeconomic-by-year interactions.'
  assumptions:
  - 'Parallel festival-season trends between adopting and not-yet-adopting prefectures.'
  - 'No anticipation before the coded effective festival season.'
  - 'No differential seasonal shocks or policy overlap correlated with adoption timing.'
  threats_addressed:
  - 'The paper reports controls and event-study logic, but the full specification and appendix were not independently inspected.'
  - 'The accessible sources do not establish the exact prefecture list, strict/moderate coding, or health-proxy construction.'
  - 'Local adoption, cross-border setting-off, CNY migration, and concurrent environmental policies remain unresolved threats.'
  evidence_refs:
  - E1
  - E2
method_transfer: null
readiness_blockers:
- The final article full text and appendices are subscriber-restricted; the exact prefecture list, per-prefecture effective dates, strict/moderate coding rule, festival-month definition, sample end year, and clustering choices have not been inspected.
- The 47-regulated (2015) and nearly-160 (end-2018) counts and the CNY Eve-through-Lantern-Festival window are preview-reported from the ScienceDirect preview and have not been independently reconstructed from local government notices.
- The health outcome construction (search-index terms, index coverage, validation) is reported only and has not been verified against clinical or administrative health data.
- Shanghai's and Beijing's ordinances are cited through state-media reports of official acts; the official texts themselves were not individually inspected here, and the many other prefectures' notices are not enumerated.
- The paper's controls for contemporaneous programs (Air Pollution Action Plan, monitoring, driving, heating) are reported but not independently verified; adoption endogeneity is addressed by the paper's stated controls, not established here.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Setting off fireworks and firecrackers during the Spring Festival is a long-standing Chinese custom, and festival-season fireworks are one of the most concentrated episodic sources of urban particulate pollution. The national legal framework is the State Council Regulations on the Safety Management of Fireworks and Firecrackers (Order No. 455, promulgated 2006-01-21, effective the same day, revised 2016-02-06 by Order No. 666). Article 28 delegates to county-level and above local people's governments the power to determine, according to local conditions, the times, places, and categories in which setting off is restricted or prohibited; Article 30 adds a statutory list of prohibited places that applies everywhere. [E3]

Around the mid-2010s, many cities exercised that delegated power in a tightening wave. Shanghai's revised ordinance, passed 2015-12-30 and effective 2016-01-01, completely prohibited setting off and sales inside the Outer Ring Expressway, including during the Spring Festival, and banned setting off citywide on heavy-pollution days. [E4, reported claim] Beijing converted the area within the Fifth Ring Road from a restricted to a prohibited zone by an amendment passed 2017-12-01, first enforced at the 2018 festival, and many other cities tightened measures for the 2017 festival, including heavy-pollution-day bans and sales-point curtailment. [E5, reported claim; E6, reported claim]

This wave is the institutional object behind the paper-used variation. It is separate from the national 2013 Air Pollution Action Plan, from pollution monitoring and information disclosure, from driving restrictions, and from winter heating policies, although all overlap in the same years and must be kept separate in any design.

## What Changed

The change is local: a prefecture or provincial-level city replaces its prior permissive or restricted setting-off rule with a prohibition or a tighter restriction, usually for the Spring Festival window. The rule determines when and where setting off is allowed, which firework categories may be sold, and how violations are punished. Shanghai's rule illustrates the strict form: no setting off and no sales inside the Outer Ring Expressway, with 100-500 yuan fines for individuals and penalties up to 100,000 yuan for illegal storage. [E4, reported claim] Beijing's rule illustrates the moderate form: outside the Fifth Ring, setting off remains allowed in designated hours (CNY Eve and Day 1 all day, Days 2-15 from 07:00 to 24:00), while the Fifth Ring area is fully prohibited. [E5, reported claim] Chen, Jiang, Liu and Song (2022) code this local choice as a staggered prefecture-by-year exposure with strict and moderate versions. [E1]

## Implementation and Assignment

Implementation runs through local ordinances, regulations, and annual notices plus enforcement by public security organs: sales-point approval and curtailment, fines, and checkpoints. [E6, reported claim] A prefecture becomes treated when its rule is effective for a Spring Festival season; the paper's coding reaches 47 regulated prefectures in 2015 and nearly 160 by end-2018, with the festival window running from Chinese New Year's Eve through the Lantern Festival. [E2, reported claim] A researcher encodes exposure as a prefecture-by-season ban status with strict and moderate values, dated by the lunar calendar, and joins it to daily city-level PM2.5 and to festival-window health search-index series. [E1; E2, reported claim]

The comparison pool is not-yet-regulated prefectures in the same festival seasons, so the design is a staggered DID rather than a before-after comparison within adopters alone. [E1]

## Why This Creates Empirical Variation

The assignment-generating feature is the staggered timing of local adoption: within-prefecture variation in ban status across festival seasons, contrasted with contemporaneous outcomes in not-yet-regulated prefectures. Because fireworks pollution is episodic and concentrated in the festival window, the design isolates a seasonal exposure: festival-month PM2.5 and festival-window health proxies. The paper reports an about-8-percent festival-month PM2.5 reduction under strict regulation, an insignificant moderate effect, and improved respiratory and cardiovascular health outcomes, consistent with a sharp seasonal treatment that does not extend year-round. [E1]

The strict-versus-moderate margin is itself informative: complete prohibitions appear to bind, while time- or place-restricted regimes do not, which a researcher can use to separate rule strictness from festival demand. [E1; analytical inference]

## Identification Risks

Adoption is chosen by local governments, not randomly assigned; cities that banned early may differ in pollution, health, fiscal, or political conditions, so adoption timing may be correlated with outcomes. The paper addresses this with prefecture and time fixed effects, weather and holiday controls, and initial socioeconomic-by-year interactions, but the strategy's credibility depends on parallel festival-season trends and no anticipation. [E1]

Anticipation is a real concern: bans and sales-point curtailment are announced before the festival, so setting-off behavior and possibly pre-season pollution can respond before the coded effective season. Seasonality compounds this: CNY dates shift year to year and the window overlaps heating season and other environmental programs, especially the tail of the Air Pollution Action Plan and the monitoring, driving, and heating policies that tightened in the same 2015-2018 years. [E1; E6; analytical inference]

Spillovers and sorting also matter: residents of banned cities can set off across city borders, and CNY migration changes urban populations, so city-level PM2.5 and search-index series capture regional behavior, not only local compliance. The health outcome itself is a reported search-index proxy whose validity for actual disease incidence is not established by the accessible sources. [E2, reported claim; analytical inference]

## Data Requirements

A festival-window design requires daily city-level PM2.5 from monitoring stations, lunar-calendar CNY and Lantern Festival dates, weather controls, and a prefecture-by-year ban status with effective dates. The health application additionally requires search-index series for respiratory and cardiovascular terms, whose exact construction is reported rather than verified. The treatment source is local government ordinances and notices, with the paper's coded list in its restricted full text and appendices; a researcher must reconstruct the prefecture list and dates from local notices or the paper's appendix. Prefecture codes, stable boundaries, station-to-city mapping, and CNY dates are the join keys. [E1; E2, reported claim; E3]

## Evidence Notes

E1 is the publisher abstract and matching independent records: it establishes the article's identity, the staggered-since-2015 assignment, the DID design with the stated controls, and the headline results (8 percent strict, null moderate, health improvement). The abstract does not establish the prefecture list, the coding rule, the sample end year, or the health-data construction. E2 records the ScienceDirect preview details inspected by the preceding screen run: the CNY Eve-through-Lantern-Festival window, strict and moderate versions, the 47 and ~160 counts, and search-index health proxies; these are preview-reported. E3 is the verified official gazette text of Order 455: it establishes the delegation framework and the statutory restriction/prohibition language and prohibited places, but not which prefectures adopted bans in which years. E4-E6 are state- and mainstream-media reports of official acts: they date and describe the Shanghai and Beijing ordinances and the breadth of the 2017 wave, but the official texts themselves and the many other prefectures' notices were not individually inspected here.

The principal blockers are therefore the subscriber-restricted full text and appendices (prefecture list, effective dates, strict/moderate coding, festival-month definition, sample end, clustering), the reported health-proxy construction, and the lack of an independent reconstruction of local notices. None of these is resolved by the accessible evidence; a future task should inspect the full text or an author-supplied version and, if needed, collect the local ordinances.
