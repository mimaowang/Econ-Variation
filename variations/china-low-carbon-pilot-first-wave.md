---
schema_version: 2
id: china-low-carbon-pilot-first-wave
name: China Low-Carbon Province and City Pilot, First Wave
aliases:
- National Low-Carbon Pilot Program, first batch
- 国家低碳省区和低碳城市试点（第一批）
- 发改气候〔2010〕1587号

status: grounded
provenance:
  task_id: task-72d10c4ecd9d
scope:
  country: China
  regions:
  - Guangdong (province pilot)
  - Liaoning (province pilot)
  - Hubei (province pilot)
  - Shaanxi (province pilot)
  - Yunnan (province pilot)
  - Tianjin (municipal pilot)
  - Chongqing (municipal pilot)
  - Shenzhen, Guangdong (city pilot)
  - Xiamen, Fujian (city pilot)
  - Hangzhou, Zhejiang (city pilot)
  - Nanchang, Jiangxi (city pilot)
  - Guiyang, Guizhou (city pilot)
  - Baoding, Hebei (city pilot)
  domains:
  - environment
  - energy
  - urban
  - firm
  - innovation
  variation_type: pilot-assignment
  knowledge_role: china-variation
  china_relevance: The first-wave low-carbon pilot is a Chinese central-government policy
    experiment that created administrative variation in exposure to low-carbon planning,
    targets, and supporting policies across five provinces and eight cities from 2010.
    Because assignment was based on local applications and central assessment of work
    foundations and representativeness, it is not randomly allocated, but the staggered
    expansion to second (2012) and third (2017) waves generates not-yet-treated comparison
    groups for event-study and staggered difference-in-differences designs. Researchers
    must handle province-city nesting, heterogeneous local implementation, and later-wave
    contamination.
identity:
  instrument: First-wave national low-carbon province and city pilot designations under
    NDRC Climate No. 1587 (2010)
  authority: National Development and Reform Commission (NDRC)
  legal_identifiers:
  - NDRC Climate No. 1587 (2010) — 国家发展改革委关于开展低碳省区和低碳城市试点工作的通知
  - NDRC Climate No. 3760 (2012) — 关于开展第二批低碳省区和低碳城市试点工作的通知
  - NDRC Climate No. 66 (2017) — 关于开展第三批国家低碳城市试点工作的通知
  implementation_regime: The NDRC designated five provinces (Guangdong, Liaoning, Hubei,
    Shaanxi, Yunnan) and eight cities (Tianjin, Chongqing, Shenzhen, Xiamen, Hangzhou,
    Nanchang, Guiyang, Baoding) as the first-wave low-carbon pilots in July 2010. Tianjin
    and Chongqing are province-level municipalities; the other six city pilots are prefecture-level
    cities nested in non-pilot provinces (Shenzhen in Guangdong, Xiamen in Fujian, Hangzhou
    in Zhejiang, Nanchang in Jiangxi, Guiyang in Guizhou, Baoding in Hebei). Province-level
    pilots expose all prefectures within the province, creating a nesting problem for
    city-only designs because Guangdong contains both a province pilot and the city pilot
    Shenzhen. The notice required pilot regions to submit implementation plans by 31 August
    2010, but actual local policies were developed and approved afterwards. Two later
    waves (2012 with Beijing, Shanghai, Hainan and 26 cities; 2017 with 45 cities) expanded
    the program, so the first-wave record is most cleanly used either as a single 2010
    shock or as the first cohort in a staggered multi-wave design.
  assignment_mechanism: Administrative selection from local applicants. The NDRC considered
    local work foundations and the representativeness of the pilot layout. Formal designation
    is observable from the July 2010 notice; substantive exposure depends on locally tailored
    plans and policies that vary in content and timing.
  parent: China national low-carbon pilot program
  related_variations: []
timeline:
  announcement: '2010-07-19'
  effective: '2010-07-19'
  implementation_start: 2010
  implementation_end: ongoing
  local_timing: >
    The NDRC notice was issued on 19 July 2010 and published on 10 August 2010. Pilot
    regions were required to submit implementation plans by 31 August 2010. First-wave
    plans were reportedly approved by the NDRC in early 2012. The second wave was announced
    on 5 December 2012 (NDRC Climate [2012]3760) and the third wave on 7 January 2017
    (NDRC Climate [2017]66). Many empirical papers treat the first wave as effective
    from 2010 for intention-to-treat, while some code the second wave as effective from
    2013 to allow for a lag between announcement and implementation.
  anticipation: Local governments applied before designation, and preparatory behaviour
    can precede the formal notice. The July 2010 announcement followed the State Council's
    November 2009 carbon-intensity target, so anticipation was possible.
  last_verified: '2026-07-13'
assignment:
  unit: Province or prefecture-level city
  treated: The five province-level pilots and eight city-level pilots named in NDRC Climate
    No. 1587. Province-level pilots expose all prefectures within the province; city-level
    pilots expose only the named city.
  comparison_pool: Non-designated provinces or cities not indirectly covered by a treated
    province, subject to later-wave and contamination checks. A clean city-level comparison
    must decide whether to exclude or separately code cities inside the five treated
    provinces.
  rule: Administrative designation after local applications and central consideration
    of existing foundations and representativeness
  intensity: Local policy packages, targets, and implementation effort vary substantially.
    Province-level pilots also vary in how aggressively lower-level governments implemented
    the framework.
  exemptions: []
  compliance: Formal designation is observable, but the content and timing of actual
    local implementation are heterogeneous. NDRC evaluation reports indicate that most
    pilots submitted plans and established target responsibility systems, yet the concrete
    policy mix differs by locality.
  exposure_construction: Code designated jurisdictions as exposed from 2010 for an intention-to-treat
    design; use local plans and implementation dates for designs claiming substantive
    policy exposure. For city-level designs, choose a rule for cities inside province-level
    pilots and for province-level municipalities.
  required_identifiers:
  - prefecture code
  - province code
  - calendar year
  spillovers: Treated provinces contain cities not separately named, so province-level
    treatment can contaminate nominal city-level controls. Policy learning, industrial
    relocation, and factor markets can generate spatial spillovers to neighbouring jurisdictions.
    Later waves expand treatment and alter the comparison pool.
research_compatibility:
  outcome_domains:
  - carbon emissions
  - carbon emission efficiency
  - energy transition
  - green innovation
  - industrial structure
  - firm productivity
  - urban land use
  affected_populations:
  - cities
  - regulated firms
  - energy users
  - urban residents
  mechanism_channels:
  - planning targets
  - environmental regulation
  - green investment
  - technology adoption
  - industrial restructuring
  - fiscal subsidies and tax incentives
  best_for:
  - Studying outcomes plausibly affected by local low-carbon planning and policy packages
    after the first-wave designation
  - Designs that can distinguish province-level exposure, named-city exposure, and later
    pilot waves
  - Staggered DID using first, second, and third waves as separate cohorts
  not_good_for:
  - Designs that treat designation as randomly assigned
  - Outcomes requiring a single uniform intervention date or identical policy content
    across pilots
design:
  claim_type: causal
  affordances:
  - cross-jurisdiction pilot designation
  - pre/post timing
  - later untreated or not-yet-treated jurisdictions
  - multi-wave staggered rollout
  candidate_designs:
  - difference-in-differences
  - event study
  - matched difference-in-differences
  - synthetic controls for selected cities
  - staggered difference-in-differences across three waves
  identifying_variation: Differences between designated and eligible non-designated jurisdictions
    before and after the first-wave notice, with later waves handled explicitly. The identifying
    claim is that, conditional on jurisdiction and year fixed effects and observable pre-treatment
    characteristics, selection into the first wave is uncorrelated with outcome shocks.
  assumptions:
  - Conditional outcome trends would have evolved comparably without designation.
  - Pilot application and selection are not driven by unobserved shocks that also change
    the outcome.
  - Spillovers and province-city nesting do not contaminate the comparison definition.
  - Later pilot waves and concurrent environmental policies are handled explicitly.
  diagnostics:
  - Plot event-time coefficients and jurisdiction-specific pre-trends.
  - Reconstruct applications, baseline environmental policy, and prior green investment.
  - Exclude or separately classify cities inside treated provinces.
  - Test sensitivity to later pilot waves and heterogeneous-treatment estimators.
  - Compare first-wave adopters with later-wave adopters on observables.
  primary_strategy: Staggered difference-in-differences
  estimand: The intention-to-treat effect of first-wave low-carbon pilot designation on
    the outcome of interest, conditional on the stated design assumptions.
  treatment_variable: Indicator equal to one for a jurisdiction designated in the first
    wave from 2010 onward, possibly interacted with post-2010 years and later-wave cohort
    indicators.
  comparison_logic: Non-pilot or not-yet-pilot cities/provinces in the same year
  estimation_notes: Standard staggered DID with jurisdiction and year fixed effects.
    For multi-wave designs, code treatment cohorts by wave (2010, 2012 effective 2013,
    2017) and implement heterogeneity-robust estimators (Callaway-Sant'Anna, Sun-Abraham,
    Borusyak-Jaravel-Spiess) given potentially heterogeneous treatment effects across
    cohorts.
threats:
- type: endogenous-selection
  basis: documented
  condition: The notice states that selection considered local applications, existing
    foundations, and representativeness.
  evidence_refs:
  - E1
  possible_diagnostics:
  - model application and selection predictors
  - match on pre-policy environmental capacity
  - report sensitivity to differential trends
- type: heterogeneous-treatment
  basis: documented
  condition: Pilot jurisdictions were instructed to design locally tailored plans and
    supporting policies rather than implement one uniform intervention.
  evidence_refs:
  - E1
  possible_diagnostics:
  - code local implementation packages
  - estimate cohort and policy-content heterogeneity
- type: spillover-and-nesting
  basis: inferred
  condition: Province-level pilots can expose cities that appear untreated in a city-only
    designation list, while industrial relocation and policy learning can cross borders.
    Later waves change the control group.
  evidence_refs:
  - E1
  - E3
  possible_diagnostics:
  - separate province and city pilots
  - use border buffers
  - test neighboring jurisdictions
  - exclude cities inside treated provinces or code them as treated
- type: anticipation
  basis: inferred
  condition: Local governments applied before the July 2010 notice and may have adjusted
    behaviour in anticipation of designation.
  evidence_refs:
  - E1
  possible_diagnostics:
  - test for pre-trends in the years after the 2009 State Council target announcement
  - use event-study leads to detect anticipatory effects
empirical_requirements:
  contract_version: 1
  population: Chinese prefectures, firms, or residents observed before and after 2010
  observation_unit: Prefecture-year or lower-level unit linkable to prefecture-year exposure
  geography_level: Province and prefecture
  time_start: 2005
  time_end: 2015
  minimum_frequency: annual
  minimum_pre_periods: 4
  minimum_post_periods: 4
  required_fields:
  - outcome
  - year
  - province code
  - prefecture code
  required_identifiers:
  - province code
  - prefecture code
  - calendar year
  treatment_key:
  - province code
  - prefecture code
  - calendar year
  treatment_source: Official NDRC pilot notices plus local implementation plans when
    substantive exposure timing matters
  measurement_risks:
  - province-city nesting
  - later pilot waves
  - local implementation lag
  - boundary-code changes
  - concurrent environmental policies (carbon trading pilots, eco-cities, etc.)
evidence:
- id: E1
  source_type: policy-document
  citation: National Development and Reform Commission. 2010. "Notice on Launching Low-Carbon
    Province and Low-Carbon City Pilot Work" (关于开展低碳省区和低碳城市试点工作的通知).
    NDRC Climate No. 1587 (发改气候〔2010〕1587号), July 19, 2010.
  url: https://www.ndrc.gov.cn/xxgk/zcfb/tz/201008/t20100810_964674.html
  date: '2010-07-19'
  supports:
  - identity
  - timeline
  - assignment
  verification_status: verified
  access_level: official-document
  locator: Full notice; Section II confirms the first-wave list of five provinces and
    eight cities and the selection criteria (local application, work foundations, representativeness);
    Section III lists the five tasks; Section IV requires implementation plans by 31
    August 2010
- id: E2
  source_type: paper
  citation: 'Wang, Y., Zhang, N., and Li, Y. 2022. "Going Carbon-Neutral in China: Does
    the Low-Carbon City Pilot Policy Improve Carbon Emission Efficiency?" Sustainable
    Production and Consumption 33: 312–329.'
  url: https://doi.org/10.1016/j.spc.2022.07.002
  date: '2022'
  supports:
  - design_applications
  verification_status: verified
  access_level: full-text
  locator: Sections 2–3 and Table 1; uses 285 Chinese cities 2003–2018 with multi-period
    DID and finds a 2.04% increase in carbon emission efficiency in pilot cities
- id: E3
  source_type: policy-document
  citation: National Development and Reform Commission. 2012. "Notice on Launching the
    Second Batch of Low-Carbon Province and Low-Carbon City Pilot Work" (关于开展第二批低碳省区和低碳城市试点工作的通知).
    NDRC Climate No. 3760 (发改气候〔2012〕3760号), December 5, 2012.
  url: http://www.ncsc.org.cn/SY/dtsdysf/202003/t20200319_769716.shtml
  date: '2012-12-05'
  supports:
  - timeline
  - assignment
  verification_status: verified
  access_level: official-document
  locator: Full notice archived on NCSC; Section II lists the second-wave list (Beijing,
    Shanghai, Hainan and 26 cities), confirming the multi-wave staggered structure
- id: E4
  source_type: paper
  citation: 'Ma, Jintao, Qiuguang Hu, Weiteng Shen, and Xinyi Wei. 2021. "Does the Low-Carbon
    City Pilot Policy Promote Green Technology Innovation? Based on Green Patent Data
    of Chinese A-Share Listed Companies." International Journal of Environmental Research
    and Public Health 18 (7): 3695.'
  url: https://doi.org/10.3390/ijerph18073695
  date: '2021'
  supports:
  - design_applications
  - research_compatibility
  verification_status: verified
  access_level: full-text
  locator: Sections 2–3 and Table 1; uses A-share listed enterprises 2005–2019 with multi-period
    DID and finds low-carbon city pilot policy stimulates green invention patents, with
    stronger effects in eastern cities and high-carbon-emission industries
- id: E5
  source_type: paper
  citation: 'Yu, Yantuan, and Ning Zhang. 2021. "Low-Carbon City Pilot and Carbon Emission
    Efficiency: Quasi-Experimental Evidence from China." Energy Economics 96: 105125.'
  url: https://doi.org/10.1016/j.eneco.2021.105125
  date: '2021'
  supports:
  - design_applications
  - research_compatibility
  verification_status: verified
  access_level: full-text
  locator: Sections 2–3; uses Chinese prefecture-level cities with DID/PSM-DID and finds
    low-carbon city pilots improve carbon emission efficiency
design_applications:
- paper: "Going carbon-neutral in China: Does the low-carbon city pilot policy improve
    carbon emission efficiency?"
  doi: 10.1016/j.spc.2022.07.002
  journal: Sustainable Production and Consumption
  year: 2022
  research_question: Whether low-carbon pilot designation improves city carbon-emission
    efficiency
  population: 285 Chinese cities observed from 2003 to 2018
  outcome: Carbon-emission efficiency
  data_used: []
  treatment_encoding: Pilot city interacted with post-designation periods across pilot
    waves
  comparison: Non-pilot or not-yet-pilot cities
  empirical_design: Staggered difference-in-differences
  assumptions:
  - conditional parallel trends
  - no unmodeled spillovers
  - correct pilot timing
  threats_addressed:
  - pre-trends and selection require inspection in the full paper
  evidence_refs:
  - E2
- paper: "Does the Low-Carbon City Pilot Policy Promote Green Technology Innovation? Based
    on Green Patent Data of Chinese A-Share Listed Companies"
  doi: 10.3390/ijerph18073695
  journal: International Journal of Environmental Research and Public Health
  year: 2021
  research_question: Whether low-carbon city pilot policy promotes corporate green technology
    innovation
  population: Chinese A-share listed enterprises, 2005–2019
  outcome: Green invention patent applications
  data_used:
  - CSMAR/RESSET for listed-firm financials and green patents
  - NDRC pilot lists for treatment assignment
  treatment_encoding: Indicator equal to one if the firm's registered city is a low-carbon
    pilot city and the year is 2010 or later, with later-wave cohorts coded accordingly
  comparison: Firms in non-pilot cities in the same year
  empirical_design: Multi-period difference-in-differences
  assumptions:
  - conditional parallel trends in green patent applications
  - no spillovers across cities through factor markets
  - stable firm registration location
  threats_addressed:
  - PSM-DID and robustness checks reported in the paper
  - heterogeneous effects by region and industry
  evidence_refs:
  - E4
- paper: "Low-carbon city pilot and carbon emission efficiency: Quasi-experimental evidence
    from China"
  doi: 10.1016/j.eneco.2021.105125
  journal: Energy Economics
  year: 2021
  research_question: Whether low-carbon city pilots improve urban carbon emission efficiency
  population: Chinese prefecture-level cities
  outcome: Carbon emission efficiency
  data_used:
  - City-level carbon emissions and socioeconomic data
  - NDRC pilot lists for treatment assignment
  treatment_encoding: Pilot city indicator interacted with post-2010 period, with later
    waves coded separately
  comparison: Non-pilot cities, with PSM-DID to balance observables
  empirical_design: Difference-in-differences with propensity-score matching
  assumptions:
  - parallel trends after matching
  - no spillovers
  - stable city boundaries
  threats_addressed:
  - selection bias addressed by PSM
  - robustness checks including placebo tests
  evidence_refs:
  - E5
readiness_blockers:
- Exact approval dates of first-wave local implementation plans and the actual start
  years of substantive local policies remain to be verified from provincial NDRC documents.
- The rule for province-city nesting (whether cities inside the five province-level pilots
  should be coded as treated in city-only designs) has not been resolved with primary
  evidence.
- Concurrent environmental policies (carbon-trading pilots, eco-cities, smart cities)
  and their overlap with low-carbon pilots are not yet documented in this record.
method_transfer: null
---
## Institutional Background

China announced a national 2020 carbon-intensity objective in late 2009 while industrialization and urbanization were still increasing energy demand. The first-wave program was designed as a decentralized policy experiment: local governments would integrate climate objectives into development planning and explore regulatory, investment, technology, industrial, statistical, and lifestyle instruments suited to local conditions. [E1]

The program therefore did not introduce one uniform tax or emissions standard. It created an administrative framework in which selected provinces and cities were expected to formulate local low-carbon plans, targets, and supporting policies. [E1]

## What Changed

The NDRC named five provinces and eight cities as the first national pilots. Designated governments were required to prepare low-carbon development plans, create supporting policies, promote low-carbon industries and technology, build greenhouse-gas statistics, and report implementation arrangements. [E1]

The first-wave list is: Guangdong, Liaoning, Hubei, Shaanxi, Yunnan (provinces); Tianjin, Chongqing, Shenzhen, Xiamen, Hangzhou, Nanchang, Guiyang, Baoding (cities). Tianjin and Chongqing are province-level municipalities; Shenzhen is in Guangdong, Xiamen in Fujian, Hangzhou in Zhejiang, Nanchang in Jiangxi, Guiyang in Guizhou, and Baoding in Hebei. [E1; analytical inference]

## Implementation and Assignment

Assignment was administrative rather than random. The notice reports that localities applied and that the NDRC considered their existing foundations and the representativeness of the pilot layout. [E1] Formal treatment is therefore easy to code, but substantive exposure varies because local plans and implementation instruments differ. A city-level design must also decide how to treat cities located inside a pilot province and how to handle the two province-level municipalities (Tianjin and Chongqing).

The notice required implementation plans by 31 August 2010; first-wave plans were reportedly approved in early 2012, but the exact schedule and local policy start dates require provincial-level verification. [E1; reported claim]

## Why This Creates Empirical Variation

The first-wave list creates cross-jurisdiction and pre/post variation. It can support conditional DID or event-study designs when researchers reconstruct later waves, province-city nesting, applications, and implementation timing. The designation is an intention-to-treat shock; it should not automatically be interpreted as a common environmental-policy dose.

## Identification Risks

Pilot selection can reflect pre-existing environmental capacity, political commitment, development strategy, or expected green investment. Local applications create anticipation risk. Province-level treatment can contaminate city controls, later waves alter the comparison pool, and industrial relocation or policy learning can generate spillovers. These concerns follow from the documented selection and decentralized implementation structure rather than from a claim that the policy is unusable. [E1; analytical inference]

## Data Requirements

A credible design needs annual outcomes with several pre-2010 and post-2010 periods, stable province and prefecture identifiers, a complete pilot-wave table, and a rule for province-city nesting. Firm or household outcomes require geographic linkage to the relevant local government. Local plan dates are necessary when the estimand concerns actual policy implementation rather than designation.

## Evidence Notes

E1 verifies the first-wave list, central objectives, application-based selection, and decentralized tasks. E3 verifies the second-wave list and confirms the staggered structure. E2, E4, and E5 verify that the policy has been used in city-panel and firm-panel DID/PSM-DID designs, but they do not establish random assignment or uniform treatment content.
