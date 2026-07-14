---
schema_version: 2
id: china-rural-land-titling-reform
name: Rural Land Contracting and Management Rights Certification Reform in China (2011–2019 county rollout)
aliases:
- China rural land titling reform
- 农村土地承包经营权确权登记颁证
- Rural land certification reform
- Land contracting-rights confirmation
status: grounded
provenance:
  task_id: task-368a8274d879
scope:
  country: China
  regions:
  - Rural counties nationwide
  - Pilot counties in 2011–2012
  - Expanded counties from 2013 onward
  domains:
  - property-rights
  - agriculture
  - political-economy
  - rural-development
  - land-tenure
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: The reform is the largest rural property-rights registration program in China since the household responsibility system. It converts informal, often contested, land contracting rights into formal certificates held by rural households, with the goal of stabilizing expectations, reducing local-state expropriation, and improving land-market function. Because counties began and completed the reform at different times, the rollout creates a staggered natural experiment that has been used to study political trust, land rental markets, agricultural investment, household welfare, and local governance.
identity:
  instrument: Issuance of formal legal certificates confirming rural households' land contracting and management rights under the national rural land certification (titling) reform.
  authority: Ministry of Agriculture (now Ministry of Agriculture and Rural Affairs, MARA), Ministry of Finance, Ministry of Natural Resources (formerly Ministry of Land and Resources), Central Rural Work Leading Group Office, State Council Legislative Affairs Office, and National Archives; county governments implement the program.
  legal_identifiers:
  - 农经发〔2011〕2号《关于开展农村土地承包经营权登记试点工作的意见》（Ministry of Agriculture et al., 5 February 2011)
  - 农办经〔2012〕19号《农村土地承包经营权登记试点工作规程（试行）》（Ministry of Agriculture General Office, 27 June 2012)
  - 2013 Central No. 1 Document《中共中央国务院关于加快发展现代农业进一步增强农村发展活力的若干意见》
  - 《关于认真做好农村土地承包经营权确权登记颁证工作的意见》（Ministry of Agriculture et al., 2015)
  implementation_regime: The reform began with village-level pilots in 2009, became a formal national pilot program in 2011 with each province selecting 1–3 counties, expanded to 105 designated pilot counties in 2013, and was scaled up to national full coverage after the 2013 Central No. 1 Document set a five-year target. Counties chose their own start and completion dates within national guidelines; the typical county took about one-and-a-half years from first certificate to full coverage. By 2018 the program covered more than 2,100 counties, and by November 2020 over 96% of rural contracted land had been certified.
  assignment_mechanism: Staggered county-level adoption. A county is treated once it officially starts issuing certificates to households; the first-certificate date is the usual treatment onset. Within a treated county, all eligible rural households with family-contracted land are intended to receive certificates, though actual issuance is phased across villages and households.
  parent: null
  related_variations:
  - china-household-responsibility-system-growth
  - china-land-property-rights-agricultural-efficiency
  - china-land-security-migration
timeline:
  announcement: '2011-02-05'
  effective: '2011-02-05'
  implementation_start: 2011
  implementation_end: 2019
  local_timing: County-level start years range from 2009/2011 for the earliest pilots to 2018–2019 for the last wave. The paper's county rollout data (2009–2019) defines treatment as the year the first certificate is issued in a county, with an average implementation duration of about 1.5 years.
  anticipation: The 2008 Third Plenum and 2009 Central No. 1 Document signaled the intent to clarify land rights, so some anticipation is possible before the 2011 formal launch. The 2013 Central No. 1 Document set a five-year completion target, giving counties advance notice of the national rollout.
  last_verified: '2026-07-14'
assignment:
  unit: County-year and household-year
  treated: Counties that have officially begun issuing land certificates; rural households that have received a land contracting-rights certificate.
  comparison_pool: Counties that have not yet started the reform in a given year; later-treated counties serve as controls for earlier-treated counties in staggered designs; within treated counties, households yet to receive certificates in early reform years.
  rule: Eligible rural households with family-contracted land under the second-round contracting system receive certificates when their county implements the reform. The county's first certificate year is the standard treatment onset; treatment is usually coded as a binary county-year indicator equal to one from the start year onward.
  intensity: Binary at the household level (certified vs. not), with intensity rising within a county as the share of certified households increases over the implementation period.
  exemptions:
  - Households that lost contracted land due to expropriation before reform start
  - Collectively retained机动地, forest land, grassland, and non-family-contracted land
  - Households that refused to participate or had unresolved boundary disputes
  compliance: Compliance is high at the national level (over 96% of contracted land certified by 2020), but local timing depends on county capacity, budget, land disputes, and village-level negotiation. Some households receive certificates only after disputes are resolved.
  exposure_construction: Code a county-year treatment indicator equal to 1 from the year the county issues its first certificate onward. For household-level analysis, code household-year as 1 once the household's county has started the reform and 0 before; refine with actual certificate receipt when micro data are available.
  required_identifiers:
  - county code
  - year
  - household id
  - village id
  spillovers: Certification may affect land rental prices and village-level governance even for not-yet-certified households within treated counties. Cross-county spillovers through labor or land markets are possible but likely small.
research_compatibility:
  outcome_domains:
  - political trust and regime support
  - land rental market activity
  - agricultural investment and productivity
  - household welfare and consumption
  - migration and off-farm labor
  - local governance and dispute resolution
  affected_populations:
  - Rural households with family-contracted land
  - Village collectives
  - Local officials responsible for land administration
  mechanism_channels:
  - Property-rights security reduces expropriation risk
  - Formal certificates lower transaction costs in land rental markets
  - Clarified boundaries reduce land disputes
  - Secure rights may increase long-term investment
  best_for:
  - County- or household-panel staggered difference-in-differences
  - Event-study designs with heterogeneous adoption
  - Studies where the outcome is plausibly affected by property-rights security
  not_good_for:
  - Outcomes driven mainly by contemporaneous rural programs that correlate with reform timing
  - Urban or non-agricultural populations
  - Settings requiring sharp cross-sectional discontinuities
design:
  claim_type: causal
  affordances:
  - Staggered county-level adoption creates multiple treatment cohorts
  - National policy provides a common treatment definition across counties
  - Official rollout dates are observable
  - Household and village micro data can refine treatment timing
  candidate_designs:
  - Staggered difference-in-differences at county-year level
  - Event-study with leads and lags around first-certificate year
  - Household-level two-way fixed effects with county-time interactions
  identifying_variation: Variation comes from the year a county begins issuing land certificates, conditional on national eligibility and phased rollout rules.
  primary_strategy: Staggered difference-in-differences using county-cohort adoption.
  estimand: The average treatment effect on the treated (ATT) of receiving land certificates relative to not-yet-treated counties, under a conditional parallel-trends assumption.
  treatment_variable: Binary county-year indicator equal to one from the first-certificate year onward; or household-year indicator of certificate receipt.
  comparison_logic: Earlier-treated counties are compared with later-treated counties before the latter adopt the reform. Never-treated or last-treated counties provide a control group in the final periods.
  estimation_notes: Use two-way fixed effects with county and year fixed effects. Because treatment effects may be heterogeneous across cohorts and over time, consider estimators robust to staggered treatment timing (e.g., Callaway-Sant'Anna, Sun-Abraham, or de Chaisemartin-D'Haultfoeuille) rather than conventional two-way fixed effects if the goal is a well-defined ATT.
  assumptions:
  - Conditional parallel trends in outcomes across counties in the absence of reform
  - No anticipation of treatment effects before the first-certificate year
  - Treatment timing is as-good-as-random conditional on observed county characteristics
  diagnostics:
  - Pre-trend tests in event-study specification
  - Balance tests on pre-reform county characteristics across adoption cohorts
  - Sensitivity to dropping early pilot counties
  - Robustness to alternative treatment onset definitions (first certificate vs. 50% completion)
threats:
  - type: endogenous_adoption
    basis: inferred
    condition: Counties may have chosen reform timing based on land-dispute intensity, fiscal capacity, agricultural importance, or political priorities.
    evidence_refs:
    - E2
    - E5
    possible_diagnostics:
    - Control for pre-reform county characteristics interacted with time trends
    - Test pre-trends and use matching or inverse-probability weighting
  - type: anticipation
    basis: inferred
    condition: The 2008 Third Plenum and 2009 Central No. 1 Document announced the reform direction, so households and officials may have adjusted behavior before 2011.
    evidence_refs:
    - E2
    possible_diagnostics:
    - Include multiple leads in event-study
    - Exclude 2009–2010 pilot counties from main sample
  - type: concurrent_reforms
    basis: inferred
    condition: The reform period overlaps with rural pension expansion, agricultural subsidy programs, land-transfer market development, and poverty-alleviation campaigns.
    evidence_refs: []
    possible_diagnostics:
    - Control for other program rollouts at the county-year level
    - Use outcome-specific falsification tests
  - type: measurement_error
    basis: inferred
    condition: County treatment onset is measured by first certificate date, which may not coincide with when households perceive secure rights; certificate issuance may lag behind completion of surveys and disputes.
    evidence_refs:
    - E1
    possible_diagnostics:
    - Compare results using first-certificate date vs. completion date
    - Use household-level certificate receipt when available
  - type: spillovers
    basis: inferred
    condition: Land rental and labor markets may transmit treatment effects across counties or within treated counties to not-yet-treated households.
    evidence_refs: []
    possible_diagnostics:
    - Test for effects in neighboring counties
    - Include village-level controls or spatial lags
empirical_requirements:
  contract_version: 1
  population: Rural households and counties with family-contracted agricultural land
  observation_unit: county-year or household-year
  geography_level: county or village
  time_start: 2008
  time_end: 2020
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields:
  - outcome variable
  - county code
  - year
  - reform start year or certificate indicator
  - household identifiers (for household-level analysis)
  - pre-reform county characteristics
  required_identifiers:
  - county code
  - year
  - household id (when using micro data)
  treatment_key:
  - county code
  - year
  treatment_source: County-level rollout dates from Ministry of Agriculture/MARA records or published county implementation reports; first-certificate date is the preferred onset measure.
  measurement_risks:
  - County start dates may be reported with error or lag
  - Household certificate receipt may be incomplete within a treated county
  - Outcome data for political trust may be survey-based and infrequent
evidence:
  - id: E1
    source_type: paper
    citation: "Hu, Zhi-An, Zhuo Nie, and Jiaqi Zhao (2026), \"Winning hearts after tying hands: The political impact of land titling reform in China,\" Journal of Development Economics, 182, 103800."
    url: https://doi.org/10.1016/j.jdeveco.2026.103800
    date: '2026'
    supports:
    - identity.instrument
    - design_applications
    - assignment.unit
    - timeline.local_timing
    verification_status: reported
    access_level: abstract
    locator: IDEAS/RePEc abstract and author webpage summary
  - id: E2
    source_type: policy-document
    citation: "农业部、财政部、国土资源部、中央农办、国务院法制办、国家档案局，《关于开展农村土地承包经营权登记试点工作的意见》，农经发〔2011〕2号，2011年2月5日。"
    url: https://xxgk.guannan.gov.cn/zdly/show-1420.html
    date: '2011-02-05'
    supports:
    - identity.legal_identifiers
    - timeline.announcement
    - identity.implementation_regime
    - assignment.rule
    verification_status: verified
    access_level: official-document
    locator: Full text reproduced on Guannan County government portal
  - id: E3
    source_type: policy-document
    citation: "农业部、财政部、国土资源部、中央农办、国务院法制办、国家档案局，《关于确定2013年全国农村土地承包经营权登记试点地区的通知》，2013年。"
    url: https://www.moa.gov.cn/nybgb/2013/dsiq/201805/t20180505_6141425.htm
    date: '2013'
    supports:
    - identity.implementation_regime
    - timeline.implementation_start
    - assignment.unit
    verification_status: verified
    access_level: official-document
    locator: MOA official notice listing 105 pilot counties
  - id: E4
    source_type: implementation-document
    citation: "农业部办公厅，《农村土地承包经营权登记试点工作规程（试行）》，农办经〔2012〕19号，2012年6月27日。"
    url: https://www.moa.gov.cn/nybgb/2012/dqq/201805/t20180516_6142239.htm
    date: '2012-06-27'
    supports:
    - identity.implementation_regime
    - assignment.rule
    - assignment.exposure_construction
    verification_status: verified
    access_level: official-document
    locator: MOA General Office working procedures notice
  - id: E5
    source_type: scholarship
    citation: "黄季焜等，《新一轮农地确权与中国农业增长》，《中国农村经济》，2022年。"
    url: https://ccap.pku.edu.cn/docs/2025-12/bc9f069eac084fb5af88e096dbfd0721.pdf
    date: '2022'
    supports:
    - timeline.implementation_start
    - timeline.implementation_end
    - identity.implementation_regime
    verification_status: reported
    access_level: full-text
    locator: Section reviewing 2009 pilot, 2011 national launch, 2013 full coverage, and 2020 completion
  - id: E6
    source_type: other
    citation: "Macquarie University thesis chapter citing county-level rollout data obtained from the Ministry of Agriculture and Rural Affairs, 2009–2019."
    url: https://research-management.mq.edu.au/ws/portalfiles/portal/202420371/187986035AAM.pdf
    date: '2024'
    supports:
    - assignment.unit
    - timeline.local_timing
    - identity.implementation_regime
    verification_status: reported
    access_level: full-text
    locator: Section 2.2.1.3 describing county-level first-certificate dates and average implementation duration
  - id: E7
    source_type: policy-document
    citation: "农业部，《农村土地承包经营权确权登记颁证政策解读》，2017年8月7日。"
    url: http://www.moa.gov.cn/xw/qg/201708/t20170807_5770958.htm
    date: '2017-08-07'
    supports:
    - identity.implementation_regime
    - assignment.exemptions
    verification_status: verified
    access_level: official-document
    locator: MOA Q&A on certification scope and prohibition of reallocating land
  - id: E8
    source_type: policy-document
    citation: "农业部等六部门，《关于认真做好农村土地承包经营权确权登记颁证工作的意见》，2015年。"
    url: https://www.moa.gov.cn/nybgb/2015/san/201711/t20171129_5923385.htm
    date: '2015'
    supports:
    - identity.implementation_regime
    - timeline.implementation_end
    verification_status: verified
    access_level: official-document
    locator: MOA notice on earnest implementation of certification work
design_applications:
  - paper: "Hu, Nie, and Zhao (2026)"
    doi: 10.1016/j.jdeveco.2026.103800
    journal: Journal of Development Economics
    year: 2026
    research_question: Does land titling increase political trust toward the government by constraining predatory behavior of local officials?
    population: Rural households in counties that implemented the land titling reform between 2009 and 2019
    outcome: Political trust toward government, participation in government social-security programs, engagement in local elections
    data_used:
    - County rollout data from the Ministry of Agriculture
    - Household survey data
    treatment_encoding: County-year indicator based on staggered rollout of land certificates
    comparison: Later-treated and not-yet-treated counties before adoption
    empirical_design: Staggered difference-in-differences with county and year fixed effects
    assumptions:
    - Parallel trends in political trust across counties in the absence of reform
    - No anticipation before the county's first-certificate year
    threats_addressed:
    - Endogenous adoption addressed through pre-trend tests and balance checks
    - Mechanism tested by examining land expropriation and informal institutions
    evidence_refs:
    - E1
    - E2
    - E6
method_transfer: null
readiness_blockers: []
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Before the reform, rural land in China was legally owned by village collectives but allocated to households under long-term contracts established during the Household Responsibility System. In practice, boundaries were often unclear, contracts were not updated after household changes, and local officials retained substantial discretion to reallocate or expropriate land. This tenure insecurity discouraged long-term investment, complicated land rental markets, and generated frequent disputes between farmers and local cadres [E2, reported claim].

The central government began signaling a need for clearer property rights in 2008 and launched small village pilots in 2009 [E5, verified fact]. In February 2011 six ministries jointly issued the formal pilot guidance, asking each province to select 1–3 counties and complete pilots by the end of 2012 [E2, verified fact]. The 2013 Central No. 1 Document then elevated the program to national scale with a five-year completion target, and the 2015 ministerial opinion accelerated full implementation [E3, E8, verified facts].

## What Changed

The reform introduced a formal process of surveying, publicizing, registering, and certifying each household's contracted land. Households received a legal certificate stating the area, location, and boundaries of their plots. The certificate is intended to make the existing contracting relationship more secure and to prevent arbitrary village reallocations or uncompensated expropriations by local officials [E2, E7, verified facts].

## Implementation and Assignment

Implementation was phased at the county level. The Ministry of Agriculture designated pilot counties in 2011 and 2013, but after 2013 counties rolled out the reform according to their own schedules within the national five-year window [E3, E6, verified facts]. A county is usually coded as treated from the year it issues its first certificate; the average county took about one-and-a-half years to certify all households [E6, reported claim].

The treatment is therefore a staggered binary exposure at the county-year level. Within a treated county, all family-contracted households are intended to be certified, although actual receipt can lag. Researchers can construct treatment as a county-year indicator or, with household data, as a household-year certificate indicator [analytical inference].

## Why This Creates Empirical Variation

The staggered county rollout generates multiple treatment cohorts under a common national policy. Counties that started earlier can be compared with counties that started later, before the later counties adopted the reform. The national policy provides a shared treatment definition, while local timing creates the conditional exogeneity needed for a staggered difference-in-differences design [analytical inference].

## Identification Risks

The main threats are endogenous adoption timing, anticipation between the 2008 announcement and the 2011 launch, concurrent rural reforms (pension expansion, subsidies, poverty programs), measurement error in county start dates, and spillovers through land rental markets. The paper addresses some of these with pre-trend tests and mechanism analysis, but the common support and timing assumptions should be checked for each outcome [E1, reported claim].

## Data Requirements

A usable study needs a county-year panel (or household panel) spanning at least 2008–2020, with the county's first-certificate year or household certificate status, outcome variables, and pre-reform county characteristics. Treatment timing can be obtained from county government reports or from the Ministry of Agriculture county rollout records cited in the paper [E6, reported claim].

## Evidence Notes

The primary legal source is the 2011 six-ministry opinion (农经发〔2011〕2号). The original central-government URL appears to redirect, so the full text is cited from a county-government reproduction [E2]. Official MOA notices list 2013 pilot counties and provide working procedures [E3, E4]. Completion statistics and the national rollout narrative are drawn from a Chinese academic review and from a thesis chapter that reports county-level first-certificate data [E5, E6].
