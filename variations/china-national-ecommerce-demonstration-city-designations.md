---
schema_version: 2
id: china-national-ecommerce-demonstration-city-designations
name: China's National E-commerce Demonstration City Designations (2009–2016; paper-coded 2011/2014/2017)
aliases:
- National E-commerce Demonstration City program
- 国家电子商务示范城市
- 国家电商示范城市
- National e-commerce demonstration-city policy
status: design-documented
provenance:
  task_id: task-6b263c7e0629
scope:
  country: China
  regions:
  - Mainland Chinese prefecture-level cities
  - Yiwu and Wujiaqu county-level cities in the national program; excluded from the paper's prefecture-city treatment dataset
  domains:
  - regional-economics
  - urban-economics
  - digital-economy
  - economic-growth
  - firm-economics
  - labor-migration
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    This is a centrally coordinated, place-based Chinese designation program. It
    combines local e-commerce development plans and supporting regulatory,
    payment, logistics, and digital-infrastructure work. Its staggered city
    designation is an empirical exposure used in a 2026 city-panel paper; it is
    not a general measure of e-commerce adoption and not the separate rural
    county demonstration or cross-border e-commerce pilot programs.
identity:
  instrument: >
    National E-commerce Demonstration City (国家电子商务示范城市) creation and
    designation. Shenzhen was approved as the first national demonstration city
    in 2009; the broader multi-city program then designated cities in 2011 and
    subsequent rounds in 2014 and late 2016 (the latter published in January
    2017). The program was intended to improve local e-commerce policy and
    service environments and to demonstrate scalable applications. This record
    covers that designation instrument, not the distinct rural e-commerce
    comprehensive-demonstration county program, national e-commerce demonstration
    bases, or cross-border e-commerce comprehensive pilot zones.
  authority: >
    The National Development and Reform Commission coordinated the program with
    the Ministry of Commerce and other central departments. The issuing
    departments varied across notices: the 2011 guidance and first large cohort
    involved central development, commerce, financial, tax, market-regulation,
    customs, and quality-supervision bodies; later notices renewed the program
    with the corresponding central agencies.
  legal_identifiers:
  - 发改高技〔2011〕463号 — guidance for creating national e-commerce demonstration cities
  - 发改办高技〔2011〕2753号 — first broad multi-city designation notice
  - 发改高技〔2013〕1772号 — second-round application and review procedure
  - 发改高技〔2014〕469号 — second-round designation of 30 cities
  - 发改高技〔2016〕2654号 — third-round designation of 17 cities; signed 2016-12-16 and publicly posted 2017-01-12
  implementation_regime: >
    The designation was a city-level development program rather than a single
    standardized construction project. Central guidance asked cities to improve
    e-commerce rules and services, payments, logistics, network support, and
    applications by firms and households; cities prepared local work plans and
    implementation tasks. The amount and timing of actual investment, services,
    and take-up could therefore differ across places. The designation records
    policy authorization and support, not identical completed infrastructure or
    uniform e-commerce adoption.
  assignment_mechanism: >
    City governments proposed plans in response to central calls, with provincial
    approval or coordination for the second round and central interdepartmental
    expert review and selection. The 2013 notice limited applications by region
    and instructed applicants to meet listed eligibility routes; the 2014 notice
    says the proposals were evaluated before 30 cities were approved. Selection
    thus reflects local economic conditions, existing e-commerce strengths,
    administrative capacity, and proposal quality. It is not randomized. Shenzhen
    is an earlier first-city case, and the paper's coding assigns it to the 2011
    cohort despite official NDRC material reporting its approval in September
    2009.
  parent: null
  related_variations:
  - china-broadband-china-pilot-city-designation
timeline:
  announcement: 2011-03-07 national guidance; Shenzhen's earlier approval is reported as 2009-09
  effective: null
  implementation_start: 2009
  implementation_end: 2016
  local_timing: >
    Institutional timing and the paper's coding are not identical. NDRC reports
    that Shenzhen was formally approved in September 2009. The broad first-round
    notice is dated 2011-11-11; the second-round notice is dated 2014-03-25; and
    the third-round notice was signed 2016-12-16 but posted publicly on
    2017-01-12. Gu and Zhou (2026) describe the empirical rounds as 2011, 2014,
    and 2017. Their publisher-hosted treatment attachment contains 68 treated
    city codes, with `policy_year` counts of 23 for 2011, 29 for 2014, and 16
    for 2017; it codes Shenzhen (440300) in 2011 and excludes the county-level
    cities Yiwu and Wujiaqu. The paper's year convention is reproducible from
    that file, but should not be mistaken for Shenzhen's first official approval
    or the third notice's signature date.
  anticipation: >
    Application and work-plan preparation precede designation. The 2013 call
    required municipal approval and provincial consent before expert evaluation;
    cities could invest in e-commerce policy and infrastructure while preparing
    proposals. Event-time leads and alternative dates are important, especially
    for Shenzhen and the 2016-signed/2017-coded cohort.
  last_verified: '2026-10-02'
assignment:
  unit: >
    City-year in the paper's 286-prefecture-city panel (2006–2023). The wider
    national program also included the county-level cities Yiwu and Wujiaqu, but
    the paper's treatment attachment and outcome sample exclude those two units.
  treated: >
    In Gu and Zhou's application, a prefecture-city code is treated from its
    recorded policy year onward. The publisher-hosted treatment file reports 68
    treated city codes: 23 coded to 2011, 29 to 2014, and 16 to 2017. These are
    the paper's operational cohorts, not a claim that every locality's first
    authorization or substantive implementation began in that calendar year.
  comparison_pool: >
    Other cities in the 286-city panel supply the comparison observations; cities
    in later cohorts are not yet treated before their coded year, while never-
    designated cities remain untreated. The article's baseline uses city and year
    fixed effects and a staggered DID indicator; its summary does not establish a
    fully modern cohort-specific estimator for the headline estimate.
  rule: >
    For replication of the 2026 paper, use its policy attachment's city code and
    `policy_year` fields, with `treat=1` for designated cities and `post=1` in
    and after the paper-coded cohort year; its `dd` field is the resulting
    city-year exposure. Preserve the source file and its 2011 Shenzhen coding.
    For an institutional-onset design, separately use the official approval date
    for Shenzhen (2009) and the dated notices for later waves, document how a
    notice signed in 2016 but published in 2017 is assigned, and report
    sensitivity to those alternatives. Do not silently replace either convention
    with one national post-2011 indicator.
  intensity: >
    The paper's main treatment is binary city designation. It also constructs
    neighboring-city exposure in concentric distance bands for spillover
    analysis; those spatial indicators are derived exposures, not additional
    designation cohorts or a measure of local compliance.
  exemptions:
  - Yiwu and Wujiaqu are national program cities but excluded from the paper's prefecture-city panel and treatment file.
  - National e-commerce growth and internet access without a city designation are not this treatment.
  - Rural e-commerce comprehensive demonstration counties, national e-commerce demonstration bases, and cross-border e-commerce pilot zones are separate instruments.
  compliance: >
    Designation authorized a local creation plan and central support, but the
    program documents do not establish identical local spending, infrastructure
    completion, or firm take-up. Treat designation as an intent-to-expose policy
    measure unless a study separately observes implementation intensity.
  exposure_construction: >
    Begin with the dated central notices and preserve each named jurisdiction's
    administrative type. For exact replication, use the journal's supplementary
    `Policy pilot of national e-commerce demonstration cities at the prefecture
    level from 2006 to 2023` workbook, sheet 1, which supplies `cityid6`,
    `treat`, `post`, `dd`, and `policy_year`. Join annual outcomes with a
    time-consistent city-code crosswalk. The supplied dataset resolves the
    paper's code-level cohort list but does not turn the paper's cohort convention
    into a legal effective date.
  required_identifiers:
  - historical prefecture-city code (`cityid6`)
  - province code
  - designation entity name and administrative level
  - official notice number and signature/publication date
  - paper-coded `policy_year` if reproducing the 2026 application
  - calendar year
  - outcome or firm identifier for the selected design
  spillovers: >
    The paper reports positive growth spillovers within 200 km and estimates
    distance rings extending to 300 km. Nearby untreated cities therefore may
    not be clean controls for a direct designation effect. The nationwide
    program's demonstration intent also makes knowledge and policy spillovers
    plausible beyond the paper's measured rings.
research_compatibility:
  outcome_domains:
  - city economic growth and GDP per capita
  - regional market integration and spatial spillovers
  - firm investment, labor demand, and innovation
  - supply-chain organization and business environment
  - employment and labor reallocation
  affected_populations:
  - firms located in designated cities
  - workers and households participating in local labor and product markets
  - firms and residents in neighboring cities exposed to spillovers
  mechanism_channels:
  - e-commerce regulation and service environment
  - online-payment and logistics support
  - firm digital adoption and supply-chain efficiency
  - market access, competition, and labor reallocation
  - knowledge and economic activity spilling to nearby cities
  best_for:
  - City-year studies of local e-commerce policy support and economic growth
  - Firm outcomes that can be linked to historical city locations and designation cohorts
  - Regional studies that explicitly model 0–300 km neighboring-city exposure
  - Comparing policy authorization with actual e-commerce or infrastructure take-up when those data are available
  not_good_for:
  - Treating designation as random or as a uniform infrastructure treatment
  - Using a single post-2011 indicator that ignores Shenzhen and later cohorts
  - Treating the paper's 2017 label as the third notice's signature date
  - Using neighboring cities as untreated controls without addressing policy spillovers
  - Conflating this program with rural e-commerce counties or cross-border e-commerce pilot zones
design:
  claim_type: causal
  affordances:
  - staggered city designation with publicly inspectable cohort coding
  - annual prefecture-city panel spanning 2006–2023 in the 2026 application
  - local growth outcomes and separately constructed spatial spillover exposure
  - supplementary city-code treatment file downloadable from the journal
  candidate_designs:
  - staggered DID with city and year fixed effects, accompanied by cohort-robust estimates
  - event study around the paper-coded designation cohort with alternative institutional dates
  - distance-ring exposure designs for local and neighboring-city effects
  - firm-level designs linked to historical city location, when the firm data permit
  identifying_variation: >
    The paper compares designated cities before and after their coded designation
    with other cities in its panel, using staggered timing. The empirical contrast
    is between places whose locally proposed e-commerce plans were selected at
    different times and those not yet or never designated, not between randomly
    assigned cities. A separate ring exposure asks how outcomes vary with distance
    from designated cities; it is a spillover application of the same policy.
  primary_strategy: >
    Gu and Zhou (2026) report city and year fixed-effects staggered DID, event-
    study checks, and double/debiased machine learning with four-fold cross-fitting
    using support-vector-machine and random-forest learners. The article also
    constructs concentric distance rings to estimate local spillovers. These are
    reported design choices, not independent proof of identification.
  estimand: >
    In the paper's main specification, the estimand is the conditional average
    effect of a city being designated under the authors' 2011/2014/2017 coding on
    city-level economic growth. Its ring specifications estimate reduced-form
    effects on cities at stated distances from designated centers. Neither
    estimand is automatically the effect of actual platform adoption or completed
    infrastructure.
  treatment_variable: >
    Paper replication: `dd_it = treat_i × post_it`, with city-level `treat` and
    `policy_year` from the journal-hosted treatment workbook; `post` switches on
    in the coded cohort year. Preserve the workbook's 2011 code for Shenzhen and
    report alternative 2009 institutional-onset coding where substantively
    relevant. The article's ring variables indicate whether a designated city is
    present within specified distance bands.
  comparison_logic: >
    Compare each cohort's city outcomes before and after its coded designation
    against not-yet-designated and never-designated cities, conditional on the
    model's controls and fixed effects. For spatial effects, define distance bands
    from designated-city coordinates and estimate nearby-city exposure separately;
    do not assume the same comparison identifies both direct and spillover effects.
  estimation_notes: >
    The paper uses real GDP per capita and fixed-base real GDP growth, with
    NPP/VIIRS night lights as an alternative; controls include labor, capital,
    industrial structure, government expenditure, finance, trade, and HSR access.
    The 2006–2023 city data come from China City Statistical Yearbooks, EPS, and
    local statistical sources, with some interpolation. CSMAR listed-firm data
    support mechanism measures. The journal lists supplementary data and code;
    commercial city or firm data may still require licensed access.
  assumptions:
  - conditional parallel trends between selected and comparison cities before each cohort
  - application and review timing do not select on unobserved outcome trends after controls
  - no material anticipation before each selected paper or institutional onset date
  - cohort-specific treatment effects are handled with an estimator appropriate to staggered adoption
  - direct effects are distinguished from spillovers and concurrent city-level programs
  diagnostics:
  - inspect cohort-specific event-time leads and alternative windows
  - compare paper replication dates with Shenzhen's documented 2009 approval and the 2016-signed third notice
  - estimate cohort-time ATT or another heterogeneity-robust staggered estimator alongside TWFE
  - test nearby-city exposure using alternative distance bands and exclude contaminated comparison areas
  - account for the National Information Consumption, Broadband China, Smart City, and Low-Carbon City programs listed in the paper's robustness materials
threats:
- type: selected-application-and-city-capacity
  basis: documented
  condition: >
    The 2013 notice required locally prepared, municipally approved applications,
    provincial consent, and central expert evaluation; it allowed submission
    routes based on city size, trade-reform status, or e-commerce development
    rankings and limited applications by region [E8, verified]. The 2011 first-
    round notice also approved cities' submitted work plans [E3, verified]. These
    rules make selection on economic readiness, local capacity, and pre-existing
    e-commerce conditions plausible; designation is not random.
  evidence_refs:
  - E3
  - E8
  possible_diagnostics:
  - report cohort-specific pre-trends and selection-related covariates
  - compare eligible applicants with non-applicants if application records can be recovered
  - use a group-time estimator and sensitivity to alternative comparison cities
- type: cohort-date-and-treatment-coding
  basis: documented
  condition: >
    The official NDRC page reports Shenzhen's first approval in September 2009,
    while the paper's supplementary city file codes Shenzhen (440300) as 2011
    [E2, reported claim; E7, verified]. The third designation notice was signed
    on 2016-12-16 and posted in January 2017, while the paper codes that cohort
    as 2017 [E5, verified; E7, verified]. Reproduce the paper coding for
    replication, but distinguish it from institutional dates and test relevant
    alternatives.
  evidence_refs:
  - E2
  - E5
  - E7
  possible_diagnostics:
  - estimate alternative Shenzhen onset in 2009 and 2011
  - compare 2016 and 2017 onset for the final cohort
  - document which date governs anticipation, treatment, and sample eligibility
- type: spatial-interference
  basis: reported
  condition: >
    The paper estimates positive spillovers within 200 km and distance decay;
    nearby non-designated cities can therefore be affected and violate a simple
    no-interference interpretation of the direct-effect comparison [E6, reported
    claim]. The program's demonstration purpose makes additional diffusion
    plausible [E1, verified].
  evidence_refs:
  - E1
  - E6
  possible_diagnostics:
  - estimate direct effects after excluding proximate comparison cities
  - use explicit distance-ring or spatial-exposure definitions
  - compare spillover sensitivity across distance cutoffs
- type: overlapping-digital-policy-and-measurement
  basis: documented
  condition: >
    Broadband China, National Information Consumption, Smart City, and Low-Carbon
    City policies overlap in time; the paper lists exclusions of these programs
    among its robustness materials [E6, verified]. City outcomes also combine
    statistical-yearbook, EPS, local statistical, and interpolated values, while
    listed-firm mechanisms use CSMAR [E6, reported claim]. Residual overlap and
    city-code or interpolation error can affect estimates.
  evidence_refs:
  - E6
  possible_diagnostics:
  - reproduce the paper's concurrent-policy exclusions
  - check the city-code crosswalk and flag interpolated outcome periods
  - keep firm-level mechanism joins distinct from the city-level treatment assignment
empirical_requirements:
  contract_version: 1
  population: Chinese prefecture-level cities, with the paper's 68 treated codes and its 286-city panel definition
  observation_unit: City-year; firm-year or aggregated listed-firm measures only for mechanism-specific applications
  geography_level: Prefecture-level city, linked to policy-list entity and stable historical city code
  time_start: 2006
  time_end: 2023
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 1
  required_fields:
  - city and province identifiers with historical crosswalk
  - year
  - designated-city indicator and cohort year
  - real GDP or GDP per capita and price adjustment
  - labor, capital, industrial structure, fiscal expenditure, finance, trade, and transport controls for paper replication
  - city coordinates and distance-to-designated-city measure for spillover profiles
  - firm identifier and registered city for listed-firm mechanism applications
  required_identifiers:
  - historical prefecture-city code (`cityid6`)
  - province code
  - notice cohort and official notice date
  - calendar year
  - firm identifier where firm outcomes are used
  treatment_key:
  - historical city code
  - paper-coded cohort year or separately documented official onset date
  treatment_source: >
    Central designation notices plus Gu and Zhou's publisher-hosted policy pilot
    workbook. Preserve both the paper-coded cohort and the official date ledger;
    the former supports exact replication, while the latter supports alternative
    institutional timing.
  measurement_risks:
  - paper-coded 2011 onset differs from Shenzhen's earlier 2009 approval
  - third-wave paper coding is 2017 although the notice was signed in 2016
  - county-level Yiwu and Wujiaqu are program members but excluded from the paper panel
  - city selection and timing reflect applications, rankings, and local readiness
  - spatial spillovers contaminate nearby non-designated controls
  - some city outcomes are supplemented by local data or interpolation; CSMAR mechanisms require suitable firm-city links
evidence:
- id: E1
  source_type: policy-document
  citation: >
    NDRC, MOFCOM, PBOC, State Taxation Administration and SAIC, 关于开展国家电子商务示范城市创建工作的指导意见, 发改高技〔2011〕463号, 2011-03-07.
  url: https://zfxxgk.ndrc.gov.cn/web/iteminfo.jsp?id=1188
  date: '2011-03-07'
  supports:
  - identity.instrument
  - identity.implementation_regime
  - scope.china_relevance
  - research_compatibility.mechanism_channels
  verification_status: verified
  access_level: official-document
  locator: Preamble and sections I, III and IV; official NDRC government-information page.
- id: E2
  source_type: implementation-document
  citation: NDRC, 深圳市创建国家电子商务示范城市的工作思路, 2011-06-28.
  url: https://www.ndrc.gov.cn/fzggw/jgsj/gjss/sjdt/201106/t20110628_1153021.html
  date: '2011-06-28'
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.announcement
  - timeline.implementation_start
  verification_status: verified
  access_level: official-document
  locator: Opening paragraph reports NDRC/MOFCOM formal approval of Shenzhen in September 2009 and subsequent city work-plan implementation.
- id: E3
  source_type: policy-document
  citation: >
    NDRC and seven central departments, 关于同意北京市等21个城市创建国家电子商务示范城市的复函, 发改办高技〔2011〕2753号, signed 2011-11-11 and published 2011-11-22.
  url: https://www.ndrc.gov.cn/xxgk/zcfb/tz/201111/t20111122_964834.html
  date: '2011-11-11'
  supports:
  - identity.legal_identifiers
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: Page lines 14–23 and signature block at lines 29–45; notice identifies 21 approved city proposals and implementation responsibilities.
- id: E4
  source_type: policy-document
  citation: NDRC, 关于同意东莞市等30个城市创建国家电子商务示范城市的通知, 发改高技〔2014〕469号, 2014-03-25.
  url: https://www.ndrc.gov.cn/xxgk/zcfb/tz/201403/t20140325_964074.html
  date: '2014-03-25'
  supports:
  - identity.legal_identifiers
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.exemptions
  verification_status: verified
  access_level: official-document
  locator: Opening notice and city list at lines 9–27; the 30-city list includes Yiwu and describes evaluation and local support.
- id: E5
  source_type: policy-document
  citation: >
    NDRC and six central departments, 关于同意大连市等17个城市创建国家电子商务示范城市的通知, 发改高技〔2016〕2654号, signed 2016-12-16 and published 2017-01-12.
  url: https://www.cac.gov.cn/2017-01/12/c_1120299744.htm
  date: '2016-12-16'
  supports:
  - identity.legal_identifiers
  - timeline.local_timing
  - assignment.exemptions
  verification_status: verified
  access_level: official-document
  locator: Notice title/number, 17-city list, purpose clauses and signature date; lines 36–78 on the official repost.
- id: E6
  source_type: paper
  citation: >
    Gu Ran and Zhou Guangyou, “The Economic Growth and Spatial Spillover Effects of the National E-commerce Demonstration City Policy,” Journal of Finance and Economics 52(1), 2026, 108–122. DOI: 10.16538/j.cnki.jfe.20251117.403.
  url: https://doi.org/10.16538/j.cnki.jfe.20251117.403
  date: 2026
  supports:
  - timeline.local_timing
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - design.primary_strategy
  - design.identifying_variation
  - design.treatment_variable
  - design.comparison_logic
  - design.estimand
  - design.estimation_notes
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.treatment_source
  - threats.condition
  verification_status: reported
  access_level: full-text
  locator: Sections II–IV, especially policy background, model, treatment definition, sample/data, event study and distance-ring spillovers; footnote 4 states Yiwu and Wujiaqu are excluded.
- id: E7
  source_type: appendix
  citation: >
    Gu and Zhou (2026), publisher-hosted supplementary workbook, “Policy pilot of national e-commerce demonstration cities at the prefecture level from 2006 to 2023.”
  url: https://qks.sufe.edu.cn/mv_upload/att/202603/ATT260309000021V1Y.xlsx
  date: 2026
  supports:
  - assignment.treated
  - assignment.rule
  - assignment.exposure_construction
  - design.treatment_variable
  - empirical_requirements.treatment_source
  - threats.condition
  verification_status: verified
  access_level: dataset
  locator: Sheet 1; inspected `cityid6`, `treat`, `post`, `dd`, and `policy_year`. Unique treated-code counts are 23 in 2011, 29 in 2014, and 16 in 2017; city code 440300 (Shenzhen) has `policy_year=2011`; Yiwu and Wujiaqu county-level codes are absent from the treatment roster.
- id: E8
  source_type: policy-document
  citation: >
    NDRC and seven central departments, 关于启动第二批国家电子商务示范城市创建工作有关事项的通知, 发改高技〔2013〕1772号, 2013-09-13.
  url: https://www.ndrc.gov.cn/xxgk/zcfb/tz/201309/t20130923_963942.html
  date: '2013-09-13'
  supports:
  - identity.assignment_mechanism
  - timeline.anticipation
  - assignment.rule
  - threats.condition
  verification_status: verified
  access_level: official-document
  locator: Sections III–VI, especially municipal approval, provincial consent, eligibility routes, regional application limits and central expert review of proposals.
design_applications:
- paper: >
    Gu Ran and Zhou Guangyou, “The Economic Growth and Spatial Spillover Effects of the National E-commerce Demonstration City Policy”
  doi: 10.16538/j.cnki.jfe.20251117.403
  journal: Journal of Finance and Economics / 财经研究
  year: 2026
  research_question: Whether city designation promotes local growth and affects nearby cities, firms, and regional market integration.
  population: 286 Chinese prefecture-level cities observed annually from 2006 to 2023; 68 treated city codes in the supplementary treatment file.
  outcome: Real GDP per capita and fixed-base real GDP growth; robustness using night lights; firm-derived measures of competition, supply chains, business environment, labor, investment, and innovation.
  data_used:
  - China City Statistical Yearbooks and EPS city-level data
  - Local statistical sources and interpolation for some missing city outcomes
  - CSMAR listed-company data aggregated to prefecture-city mechanisms
  - Journal-hosted city-code treatment and cohort workbook
  treatment_encoding: >
    City-level `treat × post`; the supplied workbook records 2011, 2014, and 2017
    `policy_year` cohorts and switches `post` on at the coded cohort year. The
    workbook codes Shenzhen 440300 to 2011 even though NDRC reports its approval
    in September 2009. The third cohort is coded 2017 although its notice was
    signed in December 2016.
  comparison: >
    Other cities in the 286-city panel, including cities not yet designated in a
    given year and cities never designated; nearby-city exposures are modeled
    separately in concentric distance rings.
  empirical_design: >
    City and year fixed-effects staggered DID, dynamic event study, four-fold
    cross-fitted double/debiased machine learning with SVM and random-forest base
    learners, and 0–300 km distance-ring spillover models.
  assumptions:
  - selected cohorts and comparison cities would have followed conditionally parallel outcome trends absent designation
  - city application and central review timing do not encode unobserved outcome changes after conditioning
  - anticipation and the 2009/2016–2017 date differences are addressed for the question at hand
  - spatial interference is modeled or limited for the specified comparison
  - the paper's staggered-FE estimates are robust to cohort-specific effect heterogeneity
  threats_addressed:
  - the paper reports event-study pretrend checks and tests alternative distance-ring spillovers
  - the publisher lists exclusions of National Information Consumption, Broadband China, Smart City, and Low-Carbon City policies among supplementary robustness materials
  - the paper reports alternative night-light outcomes and DDML estimates
  evidence_refs:
  - E2
  - E3
  - E4
  - E5
  - E6
  - E7
  - E8
method_transfer: null
readiness_blockers: []
superseded_by: null
deprecation_reason: null
---

## Institutional Background

The program grew out of China's effort to make electronic commerce work across
local markets, not simply to build more internet access. Central guidance framed
e-commerce as a way to improve market rules, payments, logistics, business
services, and the movement of goods and factors. Shenzhen was an earlier first
city, approved in September 2009; a broader national framework followed in 2011
[E1, verified; E2, verified]. The purpose of the designation was to let selected
cities try locally adapted plans and spread useful practices. That origin also
matters for research: the cities entered through policy proposals and selection,
so the program is not a lottery among otherwise similar places.

## What Changed

The empirical event is a city being named a National E-commerce Demonstration
City, with later cohorts joining the same broad program. The official notices
identify a 2011 first broad round, 30 additional cities in 2014, and 17 in the
third round, whose notice was signed at the end of 2016 and posted in January
2017 [E3, verified; E4, verified; E5, verified]. The program list also includes
county-level Yiwu and Wujiaqu; the 2026 paper excludes those two from its
prefecture-city sample [E4, verified; E5, verified; E6, reported claim]. This is
not the rural county demonstration program, nor the separate cross-border
e-commerce pilot-zone program.

## Implementation and Assignment

Cities prepared plans around their own conditions. In the second-round notice,
an applicant needed municipal approval and provincial consent, had to fit an
eligibility route, and was subject to regional application limits and central
expert evaluation [E8, verified]. The first-round notice likewise approved
submitted city work plans [E3, verified]. This gives the variation a useful
place-and-time structure, but it also makes selection on local readiness,
administrative capacity, and prior e-commerce development a central design
question rather than a footnote.

The exact timing depends on whether one wants to reproduce a paper or represent
institutional onset. Gu and Zhou's supplementary city-code file assigns 68
treated codes to 2011, 2014, or 2017, in cohorts of 23, 29, and 16 respectively.
It codes Shenzhen as 2011 although NDRC says the city was approved in 2009; it
also codes the last cohort as 2017 although the approval notice is dated 2016
[E2, reported claim; E5, verified; E7, verified]. Keep the article's code if
replicating its results. For a new study, preserve the official dates separately
and show how conclusions respond to those alternatives.

## Why This Creates Empirical Variation

The city designations give a researcher a staggered policy exposure rather than
a national e-commerce time trend. The 2026 article uses this city-year contrast
to study real GDP per capita and growth, and it also constructs nearby-city
exposure to study regional spillovers [E6, reported claim]. That creates natural
questions about firm entry, investment, innovation, labor demand, and market
integration, provided the relevant outcomes can be joined to the historical city
codes. The designation is an offer of a local development framework; it should
not be read as a direct measure of whether firms adopted platforms or whether
the same infrastructure was built everywhere.

## Identification Risks

The strongest threat is selective entry. Cities submitted plans and were
evaluated; their prior development, state capacity, or expectations about growth
may also have influenced selection and timing [E3, verified; E8, verified]. The
paper's event-study checks are useful evidence about observed pre-trends, but
they do not make the city selection process random [E6, reported claim]. A
second issue is the paper-versus-institution timing difference for Shenzhen and
the last wave; reproduce its convention for replication, but do not pass it off
as the only institutional date [E2, reported claim; E5, verified; E7, verified].

Interference matters too: the paper reports effects extending to nearby cities
and estimates distance rings out to 300 km [E6, reported claim]. A nearby
non-designated city may therefore be an affected comparison unit. Finally,
concurrent digital programs and staggered-treatment estimators can change the
interpretation; the paper's publisher materials list checks involving National
Information Consumption, Broadband China, Smart City, and Low-Carbon City
programs [E6, reported claim].

## Data Requirements

The paper's baseline is an annual 286-city panel from 2006 through 2023. Its
publisher provides a policy workbook with city code, treatment, post-period,
combined exposure, and paper-coded cohort year; that makes the article's
assignment reproducible without manually rebuilding the roster from prose
[E6, reported claim; E7, verified]. City outcomes use statistical yearbooks,
EPS, and local statistical sources, with some interpolation. Firm mechanism
measures are derived from listed-company data and may require licensed access
[E6, reported claim]. A reusable application needs a stable city-code history,
the chosen event-date convention, annual outcomes, and—if spillovers are the
question—coordinates or an equivalent defensible distance measure.

## Evidence Notes

The central guidance and dated designation notices establish what the program
was and when central approval occurred [E1, verified; E3, verified; E4, verified;
E5, verified]. NDRC's own account supplies the earlier Shenzhen date [E2,
verified]. The paper is evidence about how one published study encoded and used
the policy; it does not independently establish that selection was exogenous
[E6, reported claim]. Its downloadable treatment workbook was inspected directly
for city codes and cohort fields [E7, verified]. Thus the canonical record keeps
both institutional timing and paper replication timing visible instead of
silently forcing them into a single date.
