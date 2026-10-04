---
schema_version: 2
id: china-workweek-reduction-reform
name: China 1995 Workweek Reduction Reform
aliases:
- China 40-hour workweek reform
- China five-day workweek reform
- 国务院关于职工工作时间的规定
- 1995年双休制改革
status: grounded
provenance:
  task_id: task-ced64d06bdd3
scope:
  country: China
  regions:
  - Mainland China
  domains:
  - labor
  - gender
  - household-economics
  - education
  - health
  - development
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: The reform is a nationwide Chinese labor-market regulation that reduces
    the statutory standard workweek and generates individual-level variation in exposure
    by employment type, supporting China-focused research on time use, gender division
    of labor, human capital, and household welfare.
identity:
  instrument: The 1995 reduction of the statutory standard workweek from six days/48
    hours to five days/40 hours for employees, announced by the State Council and implemented
    with sector-specific exemptions and staggered deadlines.
  authority: National People's Congress of China; State Council of China; Ministry
    of Labor (now Ministry of Human Resources and Social Security); Ministry of Personnel.
  legal_identifiers:
  - 《中华人民共和国劳动法》（1994年7月5日主席令第二十八号公布，1995年1月1日起施行）
  - 《国务院关于职工工作时间的规定》（1994年2月3日国务院令第146号发布，1995年3月25日国务院令第174号修订）
  - 《国务院关于修改〈国务院关于职工工作时间的规定〉的决定》（1995年3月25日国务院令第174号）
  - 《〈国务院关于职工工作时间的规定〉的实施办法》（劳部发〔1995〕143号）
  - 《国家机关、事业单位贯彻〈国务院关于职工工作时间的规定〉的实施办法》（人薪发〔1995〕32号）
  implementation_regime: The 1994 Labor Law set a 44-hour weekly ceiling. The State
    Council's March 25, 1995 amendment lowered the standard to 40 hours per week and
    fixed Saturday-Sunday rest days for state organs and public institutions, effective
    May 1, 1995. Enterprises could delay full implementation until May 1, 1997, and
    could adopt flexible, comprehensive, or irregular working-hour systems with labor-administration
    approval.
  assignment_mechanism: Exposure is assigned by employment relationship and sector.
    Standard-hours employees in state organs, public institutions, and regular enterprises
    were most tightly bound by the 40-hour cap; employees in approved flexible or shift
    systems were less affected; the self-employed were largely unaffected and serve as
    a comparison group.
  parent: null
  related_variations: []
timeline:
  announcement: '1995-03-25'
  effective: '1995-05-01'
  implementation_start: 1995
  implementation_end: 1997
  local_timing: State organs and public institutions switched to a Saturday-Sunday
    weekend from May 1, 1995; enterprises could arrange weekly rest days flexibly after
    consulting trade unions and workers.
  anticipation: The amendment was published on March 25, 1995, roughly five weeks before
    implementation. Enterprises facing difficulties could apply for delayed implementation
    until May 1, 1997, and public institutions until January 1, 1996.
  last_verified: '2026-08-15'
assignment:
  unit: Individual-year or household-year in a panel such as the China Health and Nutrition
    Survey (CHNS).
  treated: Standard-hours employees bound by the 40-hour statutory week after 1995.
    Non-standard-hours employees can be coded as a secondary treatment group.
  comparison_pool: Self-employed workers who were not covered by the statutory standard
    workweek, compared before and after 1995.
  rule: The State Council lowered the statutory workweek to 40 hours for employees;
    actual exposure depends on whether an individual's employment type falls under the
    standard-hours regime.
  intensity: The intensity of the hour reduction equals the difference between pre-reform
    actual weekly hours and the 40-hour cap; in practice the literature encodes treatment
    as a standard-hours employee indicator interacted with a post-1995 indicator.
  exemptions:
  - Enterprises with special production characteristics could adopt flexible, comprehensive,
    or irregular working-hour systems after labor-administration approval.
  - Enterprises could delay implementation of the 40-hour week until May 1, 1997.
  - Public institutions could delay implementation until January 1, 1996.
  compliance: Partial. Official weekly hours fell, but overtime and informal extra hours
    persisted, especially where weekly pay was held constant while nominal hours were
    cut.
  exposure_construction: Classify respondents in a pre-reform panel by employment status
    (standard-hours employee, non-standard-hours employee, self-employed). Interact
    a post-1995 dummy with the standard-hours indicator, add individual and year fixed
    effects, and control for province, sector, and household composition.
  required_identifiers:
  - individual ID
  - year
  - employment status / standard-hours indicator
  - household ID
  - province
  spillovers: Within-household reallocation of domestic work and childcare is a key
    mechanism rather than contamination. General-equilibrium effects on wages, prices,
    and labor demand may affect comparison groups over time.
research_compatibility:
  outcome_domains:
  - time-use
  - gender-division-of-labor
  - domestic-work
  - childcare
  - labor-earnings
  - occupational-promotion
  - education
  - health
  - household-consumption
  affected_populations:
  - employed urban and rural workers
  - dual-earner households
  - married women with children
  - self-employed workers as a comparison group
  mechanism_channels:
  - statutory working-time cap
  - household specialization
  - intra-household time reallocation
  - overtime and informal extra hours
  - human-capital investment
  - gender norms and comparative advantage
  best_for:
  - Estimating how a mandatory workweek reduction affects time allocation within households
  - Studying gendered labor-market consequences of shorter standard hours
  - Designs exploiting employment-type variation in exposure to a national reform
  not_good_for:
  - Effects on the intensive margin of firm-level production without employer data
  - Long-run firm dynamics or product-market equilibrium effects without matched firm-worker
    panels
  - Settings that require clean geographic variation, because the reform was nationwide
    with only delayed implementation as spatial variation
design:
  claim_type: causal
  affordances:
  - A nationwide policy generates a sharp 1995 break in statutory working hours.
  - Employment-type variation creates treatment and comparison groups within the same
    panel.
  - Multiple outcome domains (market work, domestic work, education, earnings, health)
    are observed in household panels such as CHNS.
  - The reform is a canonical 1990s labor-market shock that can be combined with other
    policy changes.
  candidate_designs:
  - Difference-in-differences comparing standard-hours employees with self-employed
    workers before and after 1995
  - Event-study around the 1995 reform date
  - Triple-difference by gender within dual-earner households
  - Robustness check replacing the comparison group with non-standard-hours employees
  identifying_variation: Cross-sectional exposure by employment type interacted with
    the post-1995 reform period.
  primary_strategy: Difference-in-differences using standard-hours employees as the
    treatment group and self-employed workers as the comparison group.
  estimand: The effect of being subject to the 40-hour statutory workweek on individual
    time use, intra-household labor division, earnings, education, and health.
  treatment_variable: Post-1995 indicator interacted with a standard-hours employee
    dummy.
  comparison_logic: Within-individual changes over time and between employees covered
    by the reform and self-employed workers not covered.
  estimation_notes: Individual and year fixed effects; controls for province, sector,
    age, household composition, and baseline wages; cluster standard errors at the province
    or individual level.
  assumptions:
  - Parallel trends in outcomes between standard-hours employees and self-employed workers
    in the absence of the reform.
  - Employment-type classification is stable or correctly measured before the reform.
  - No other coincident national shock differentially affects standard-hours employees
    relative to the self-employed.
  - Self-reported hours and domestic-work time are measured comparably across groups
    and years.
  diagnostics:
  - Event-study plots to test for pre-trends
  - Robustness to using non-standard-hours employees as an alternative comparison group
  - Placebo tests using alternative reform years
  - Sensitivity to sample restrictions and province-specific linear time trends
  - Checks for differential attrition across employment types
threats:
- type: parallel-trends-violation
  basis: inferred
  condition: Standard-hours employees and self-employed workers may have been on different
    pre-reform trends in earnings, education, or time use, invalidating the DID comparison.
  evidence_refs:
  - E6
  - E7
  possible_diagnostics:
  - Event-study pre-trend tests
  - Include group-specific linear time trends
  - Match on pre-reform observables
- type: selection-into-employment-type
  basis: inferred
  condition: Workers who select into standard-hours employment may differ unobservably
    from the self-employed in ways correlated with the outcomes of interest.
  evidence_refs:
  - E6
  - E7
  possible_diagnostics:
  - Control for pre-reform individual characteristics
  - Use occupation or sector fixed effects
  - Bounding analysis under selection assumptions
- type: measurement-error
  basis: inferred
  condition: Self-reported weekly work hours, domestic work, and childcare time are
    subject to recall and social-desirability bias; employment-status classification
    may change over waves.
  evidence_refs:
  - E6
  - E7
  possible_diagnostics:
  - Validate against objective proxies such as earnings or occupational category
  - Restrict to respondents with consistent employment classification across adjacent
    waves
  - Compare results using alternative time-use measures
- type: omitted-variable-bias
  basis: inferred
  condition: Concurrent 1990s reforms, including state-owned-enterprise restructuring,
    minimum-wage changes, and housing reforms, may differentially affect standard-hours
    employees and bias estimates.
  evidence_refs:
  - E1
  - E3
  - E6
  possible_diagnostics:
  - Control for province-specific macroeconomic trends
  - Interact treatment with baseline sectoral composition
  - Robustness checks restricted to provinces less exposed to SOE reforms
- type: general-equilibrium
  basis: inferred
  condition: A shorter standard workweek may change aggregate labor demand, wages, and
    prices, affecting both treated and comparison groups and violating the partial-equilibrium
    interpretation.
  evidence_refs:
  - E6
  possible_diagnostics:
  - Estimate effects on local wage and employment levels
  - Compare results across labor-market regions with different enforcement intensity
  - Interpret estimates as reduced-form effects on household behavior
empirical_requirements:
  contract_version: 1
  population: Working-age individuals and households in China, typically observed in
    panel surveys spanning the early 1990s to the early 2000s.
  observation_unit: Individual-year or household-year.
  geography_level: Individual / household, with province controls.
  time_start: 1989
  time_end: 2011
  minimum_frequency: biennial or annual panel waves
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields:
  - individual and household identifiers
  - survey year
  - employment status
  - weekly work hours
  - domestic work and childcare time
  - individual wages or earnings
  - education level
  - self-reported health indicators
  - household composition
  - province
  required_identifiers:
  - individual ID
  - year
  - household ID
  treatment_key:
  - individual ID
  - year
  - employment status / standard-hours indicator
  - post-1995 indicator
  treatment_source: State Council Order 174, the 1994 Labor Law, Ministry of Labor implementation
    measures, and survey-based employment-status coding.
  measurement_risks:
  - Self-reported time use is noisy and may be systematically biased by gender norms.
  - Employment-type classification may not cleanly map onto legal standard-hours status.
  - The reform was nationwide, so variation relies on cross-group exposure rather than
    geographic variation.
  - Delayed enterprise implementation and informal overtime may attenuate the estimated
    treatment effect.
evidence:
- id: E1
  source_type: policy-document
  citation: 《中华人民共和国劳动法》（1994年7月5日第八届全国人民代表大会常务委员会第八次会议通过，1995年1月1日起施行），第三十六条、第三十八条、第四十一条。
  url: http://www.npc.gov.cn/npc/c2/c30834/201905/t20190521_296651.html
  date: 1994
  supports:
  - identity.instrument
  - identity.legal_identifiers
  - identity.implementation_regime
  verification_status: verified
  access_level: official-document
  locator: 中国人大网，第四章“工作时间和休息休假”
- id: E2
  source_type: policy-document
  citation: 《国务院关于职工工作时间的规定》（1994年2月3日国务院令第146号发布，1995年3月25日修订），第三条、第七条、第九条。
  url: https://www.mohrss.gov.cn/xxgk2020/fdzdgknr/zcfg/fg/202011/t20201103_394935.html
  date: 1995
  supports:
  - identity.instrument
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.effective
  - timeline.implementation_start
  - timeline.implementation_end
  - timeline.local_timing
  - assignment.rule
  - assignment.exemptions
  verification_status: verified
  access_level: official-document
  locator: 人力资源和社会保障部官网
- id: E3
  source_type: policy-document
  citation: 《国务院关于修改〈国务院关于职工工作时间的规定〉的决定》（1995年2月17日国务院第8次全体会议通过，1995年3月25日国务院令第174号发布）。
  url: https://www.ccdi.gov.cn/fgk/law_display/5009
  date: 1995
  supports:
  - identity.instrument
  - identity.legal_identifiers
  - timeline.announcement
  - timeline.effective
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: 中央纪委国家监委网站法规库，国务院令第174号
- id: E4
  source_type: implementation-document
  citation: 劳动部《〈国务院关于职工工作时间的规定〉的实施办法》（劳部发〔1995〕143号），第三条、第五条、第九条、第十二条。
  url: https://www.beijing.gov.cn/zhengce/zhengcefagui/qtwj/201710/t20171009_780941.html
  date: 1995
  supports:
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.implementation_end
  - assignment.rule
  - assignment.exemptions
  verification_status: verified
  access_level: official-document
  locator: 北京市政府门户网站政策法规库转载全文（附劳动部实施办法劳部发〔1995〕143号），第十二条规定企业最迟1997年5月1日施行
- id: E5
  source_type: implementation-document
  citation: 人事部《国家机关、事业单位贯彻〈国务院关于职工工作时间的规定〉的实施办法》（人薪发〔1995〕32号），第三条、第五条、第八条。
  url: https://www.gov.cn/zhengce/2022-08/31/content_5711279.htm
  date: 1995
  supports:
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.local_timing
  - assignment.rule
  - assignment.exemptions
  verification_status: verified
  access_level: official-document
  locator: 中国政府网转载
- id: E6
  source_type: paper
  citation: 'Sun, Ang, Wei Sun, Wang Xiang, Huili Zhang, and Junsen Zhang. 2026. "Narrowing
    or widening the gender gap in market and domestic work? The impact of workweek reduction
    reform in China." Journal of Development Economics 179: 103672.'
  url: https://doi.org/10.1016/j.jdeveco.2025.103672
  date: 2026
  supports:
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design_applications.research_question
  - design_applications.population
  - design_applications.outcome
  - design_applications.treatment_encoding
  - design_applications.empirical_design
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  verification_status: reported
  access_level: abstract
  locator: DOI 10.1016/j.jdeveco.2025.103672
- id: E7
  source_type: scholarship
  citation: 浙江大学公共管理学院，"我院张俊森教授的合作论文在Journal of Development Economics发表"，2025年11月17日（研究简介与实证设计说明）。
  url: https://icpd.zju.edu.cn/2025/1121/c70711a3108814/page.htm
  date: 2025
  supports:
  - design.primary_strategy
  - design_applications.data_used
  - design_applications.treatment_encoding
  - design_applications.empirical_design
  verification_status: reported
  access_level: full-text
  locator: 浙江大学公共管理学院官网新闻页面
design_applications:
- paper: 'Narrowing or widening the gender gap in market and domestic work? The impact
    of workweek reduction reform in China'
  doi: 10.1016/j.jdeveco.2025.103672
  journal: Journal of Development Economics
  year: 2026
  research_question: Does China's 1995 workweek reduction reform narrow or widen the
    gender gap in market and domestic work?
  population: Working-age individuals and dual-earner households in China observed
    in the China Health and Nutrition Survey (CHNS) panel.
  outcome: Women's and men's time in domestic work, childcare, market work, overtime,
    educational attainment, occupational promotion, earnings, health, and children's
    nutrition and schooling.
  data_used:
  - China Health and Nutrition Survey (CHNS) panel
  - Individual employment status
  - Weekly work hours
  - Domestic work and childcare time
  - Wages and education
  - Health indicators
  treatment_encoding: Post-1995 indicator interacted with a dummy for standard-hours
    employees; non-standard-hours employees as a secondary treatment group; self-employed
    as the comparison group.
  comparison: Difference-in-differences comparing standard-hours employees with self-employed
    workers before and after the 1995 reform.
  empirical_design: Difference-in-differences exploiting individual-level variation
    in exposure to the national workweek reduction by employment type.
  assumptions:
  - Parallel trends between standard-hours employees and self-employed workers
  - Employment-type classification captures legal exposure to the 40-hour cap
  - No coincident shocks that differentially affect the two groups around 1995
  threats_addressed:
  - Pre-trends via event-study plots
  - Alternative comparison group using non-standard-hours employees
  - Robustness checks on sample composition and time trends
  evidence_refs:
  - E6
  - E7
method_transfer: null
readiness_blockers:
- Full text of Sun et al. (2026, JDE) was not accessed; exact sample restrictions,
  variable definitions, and robustness checks need verification from the published paper
  or replication package.
- The precise CHNS waves and employment-status coding used to define standard-hours,
  non-standard-hours, and self-employed groups need to be documented from the paper.
- Cross-region variation in enterprise compliance and delayed implementation has not
  yet been quantified.
---
---
## Institutional Background

China's standard working-time regime was established by the 1994 Labor Law (E1) and the 1994 State Council Regulations on Working Hours (E2), which initially set a 44-hour workweek. On March 25, 1995, the State Council issued Order 174, amending the regulations to lower the standard workweek to 40 hours and introducing Saturday-Sunday rest days for state organs and public institutions, effective May 1, 1995 (E2, E3). The Ministry of Labor's enterprise implementation measures (E4) and the Ministry of Personnel's public-sector implementation measures (E5) detailed exemptions, flexible scheduling, and delayed implementation for enterprises (until May 1, 1997) and public institutions (until January 1, 1996). [E1; E2; E3; E4; E5]

## What Changed

The reform shortened the statutory standard workweek from six days to five days while keeping weekly pay largely unchanged. It created a binding time constraint for standard-hours employees and a weaker or no constraint for workers in approved flexible, comprehensive, or irregular hour systems and for the self-employed. The change affected not only market work but also the allocation of time within households. [E2; E3; E4]

## Implementation and Assignment

Assignment is driven by employment relationship rather than geography. Standard-hours employees in state organs, public institutions, and ordinary enterprises faced the 40-hour cap most directly. Non-standard-hours employees in shift, seasonal, or approved flexible systems were less constrained. Self-employed workers, who are not covered by the statutory employee workweek, provide a natural comparison group. This employment-type variation is the basis for the difference-in-differences design used by Sun et al. (2026). [E4; E5; E6; E7]

## Why This Creates Empirical Variation

The reform is a nationwide shock, but its bite differs across individuals according to their pre-reform employment status. In a panel such as CHNS, one can compare standard-hours employees before and after 1995 with self-employed workers over the same period. The sharp policy break and the availability of detailed time-use, earnings, education, and health variables allow researchers to estimate effects on both market and domestic outcomes. [E6; E7]

## Identification Risks

The main risks are (i) differential pre-trends between standard-hours employees and the self-employed; (ii) selection into employment type correlated with unobserved outcomes; (iii) measurement error in self-reported hours and domestic work; (iv) coincident 1990s labor-market reforms that may differentially affect employees; and (v) general-equilibrium effects on wages and labor demand that spill over to the comparison group. [E6; E7]

## Data Requirements

The canonical design requires a panel of individuals and households with information on employment status, weekly work hours, domestic work and childcare time, wages, education, health, and household composition. The China Health and Nutrition Survey (CHNS) is the dataset used in the leading published application. [E6; E7]

## Evidence Notes

Primary institutional grounding comes from the 1994 Labor Law (E1), the 1994 and 1995 State Council regulations and amendment (E2, E3), and the Ministry of Labor and Ministry of Personnel implementation measures (E4, E5). The empirical design and results are drawn from Sun et al. (2026, *Journal of Development Economics*) and its institutional summary at Zhejiang University (E6, E7). [E1; E2; E3; E4; E5; E6; E7]
