---
schema_version: 2
id: china-minimum-wage-firm-competitive-shocks
name: Local Minimum-Wage Revisions and Differential Firm Exposure in Mainland China, 2002–2008
aliases:
- Hau Huang Wang minimum wage China
- China minimum wage firm productivity REStud
- minimum wage competitive shock
status: grounded
provenance:
  task_id: task-0c9086dbc0bf
scope:
  country: China
  regions:
  - Mainland counties and cities represented in the paper's industrial-firm sample
  domains:
  - labor-economics
  - firm-dynamics
  - productivity
  - industrial-organization
  - regional-economics
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    Mainland local minimum-wage revisions expose industrial firms to different
    labor-cost changes depending on both their location and their prior
    average wage relative to the local statutory floor.
identity:
  instrument: >
    Revisions of local statutory minimum wages, combined in Hau, Huang, and
    Wang (2020) with a firm-specific, lagged average-wage-based impact factor.
    This is a sequence of local wage-floor changes, not a single 2004 adoption.
  authority: >
    Provincial-level labor authorities draft differentiated local standards
    for provincial-government approval and publication. City and county
    conditions influence applicable local standards; counties do not
    independently enact a new national minimum-wage law.
  legal_identifiers:
  - Labor Law of the People's Republic of China, Article 48 (1994)
  - Minimum Wage Regulations, Ministry of Labor and Social Security Decree No. 21 (issued 2004-01-20; effective 2004-03-01)
  - Shenzhen Labor and Social Security Bureau notice 深劳社规〔2007〕15号 (one documented local schedule)
  implementation_regime: >
    Local monthly and hourly standards differ across administrative areas
    within a province and are revised over time. The 2004 national regulation
    refined coverage, hourly wages, supervision, and a minimum adjustment
    frequency; it did not itself assign the paper's yearly firm treatment.
  assignment_mechanism: >
    A firm inherits the local wage floor of its matched county or city and
    calendar year. A given increase has stronger predicted labor-cost impact
    where last year's firm average wage was closer to last year's local
    minimum. The paper estimates a nonlinear impact factor from this lagged
    ratio, then interacts it with the current local minimum-wage log change.
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 2002
  implementation_end: 2008
  local_timing: >
    These are the paper's firm-sample years, not one national implementation
    window. Local revisions can occur within a year; the authors use the
    calendar-year average local wage floor for annual firm observations.
    The inspected Shenzhen notice records 2007-07-01 and 2007-10-01
    applicability periods, with the latter published after it began.
  anticipation: >
    Firm behavior can respond to expected revisions. The paper describes
    short advance notice as anecdotal evidence, not a guarantee for every
    locality; the Shenzhen notice demonstrates that formal publication and
    stated effective dates need separate checking.
  last_verified: '2026-10-02'
assignment:
  unit: Industrial firm-year matched to a local minimum-wage jurisdiction
  treated: >
    Firms facing a positive local minimum-wage change, with heterogeneous
    exposure measured by the paper's impact factor. A low lagged average
    wage relative to the local floor implies higher predicted exposure.
  comparison_pool: >
    The same firms across years and other firms within the same industry-year
    with different local wage changes or prior wage-to-minimum ratios.
    The comparison is conditional on firm and industry-by-year effects.
  rule: >
    Construct each county/city's annual-average minimum wage if revisions
    occur within the calendar year. Compute annual log change in that floor;
    combine it with the nonlinear impact factor estimated from the prior
    firm average-wage/local-minimum ratio. Retain the minimum-wage change
    and impact factor separately in the regression.
  intensity: Nonlinear impact factor times annual log change in local minimum wage
  compliance: >
    The regulation requires employers to meet the applicable floor and
    supplies supervision and penalties. Actual firm-level compliance is
    unobserved in this record; statutory exposure is not proof of payment.
  exposure_construction: >
    The paper lacks the within-firm employee wage distribution. Its proxy
    uses prior-year average firm wage divided by prior-year local minimum
    wage, raised to a negative estimated exponent; it is not an observed
    share of workers paid at or near the minimum wage.
  required_identifiers:
  - stable firm ID and year
  - firm county or city jurisdiction
  - local minimum-wage schedule and applicability dates
  - firm wage bill and employment to calculate prior average wage
  - industry code
  exemptions:
  - Informal workers and firms outside the covered industrial-firm sample are not measured by this application
  spillovers: >
    Product-market competitors and labor markets link firms across locations.
    A local wage change may influence nominally less-exposed firms, so this
    is a relative exposure contrast, not automatically a no-spillover design.
research_compatibility:
  outcome_domains:
  - employment growth
  - capital-to-labor substitution
  - revenue-based total factor productivity
  - output and capital growth
  - export quantities and prices in a linked robustness sample
  affected_populations:
  - industrial firms covered by ASIF/CIED
  - workers at firms with different predicted wage-floor exposure
  mechanism_channels:
  - higher wage cost at initially low-wage firms
  - substitution of capital for labor
  - within-firm productivity response
  best_for:
  - Firm-panel questions about heterogeneous responses to local labor-cost changes
  - Comparing low- and high-average-wage firms within industry-years
  not_good_for:
  - Inferring the actual share of minimum-wage employees from the proxy
  - Treating the 2004 regulation as a randomized national rollout
  - Direct inference about informal, agricultural, or all small firms
design:
  claim_type: causal
  affordances:
  - Local wage floors vary across jurisdictions and years
  - Lagged firm wage-to-floor ratio differentiates exposure within a location
  - Firm panel allows comparisons around time-varying local revisions
  candidate_designs:
  - Firm-year continuous-exposure panel design following the paper
  identifying_variation: >
    Time-varying within-firm exposure to local minimum-wage changes,
    differentiated by lagged average wage relative to the statutory floor,
    after firm and industry-by-year fixed effects. The impact factor is
    constructed from firm characteristics, not randomly assigned.
  primary_strategy: >
    The paper first estimates the nonlinear impact factor in a wage-response
    equation. Reduced-form outcome regressions interact it with the annual
    local minimum-wage log change, include both components separately,
    and add firm and industry-by-year fixed effects. Other robustness and
    dynamic-panel specifications do not turn this into a randomized design.
  estimand: >
    Conditional differential response of more versus less exposed industrial
    firms to local minimum-wage changes, not the unconditional national
    effect of the 2004 regulation or the effect on all Chinese workers.
  treatment_variable: Estimated impact factor based on lagged firm average wage / lagged local minimum wage, interacted with current annual log minimum-wage change
  comparison_logic: >
    Compare outcome growth at firms with different predicted exposure as
    their local floors change, net of common industry-year shocks and
    firm-specific average growth patterns.
  estimation_notes: >
    The wage-floor panel spans 1996–2012, but the main industrial-firm
    application in the inspected manuscript is 2002–2008. Its design
    supports a conditional causal interpretation only if local revision
    timing and firm exposure are not confounded by omitted shocks.
  assumptions:
  - Conditional on model controls, local wage-floor revisions do not track unobserved shocks with differential effects on low-wage firms
  - The lagged average-wage proxy ranks meaningful labor-cost exposure adequately
  - Attrition, reporting changes, and cross-market spillovers do not create the observed differential response
  diagnostics:
  - Check whether local business-cycle variables predict revisions
  - Inspect lead/lag outcomes and other timing evidence for anticipation
  - Compare ownership and size strata without equating heterogeneity with mechanism proof
  - Use export quantities/prices and alternative productivity measures for price-deflator concerns
threats:
- type: endogenous-policy-timing
  basis: documented
  condition: Local conditions enter standard-setting by law; the authors' prediction tests mitigate but cannot prove exogenous revision timing.
  evidence_refs: [E1, E2]
  possible_diagnostics: [local trend controls, lead/lag checks, matched local policy calendar]
- type: endogenous-firm-exposure
  basis: documented
  condition: Lagged mean wages proxy low-wage employment and are correlated with firm quality, ownership, and prior trends.
  evidence_refs: [E1]
  possible_diagnostics: [firm effects, industry-year effects, pre-change trend comparison]
- type: measurement-and-selection
  basis: documented
  condition: ASIF incompletely covers small firms; revenue TFP lacks firm-specific output deflators; statutory floors need not equal paid wages.
  evidence_refs: [E1, E2]
  possible_diagnostics: [coverage checks, export-price robustness, wage-response first stage]
empirical_requirements:
  contract_version: 1
  population: Mainland industrial firms represented in the paper's ASIF/CIED sample
  observation_unit: Firm-year
  geography_level: County or city wage-floor jurisdiction
  time_start: 2002
  time_end: 2008
  minimum_frequency: annual
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - firm ID, year, and location
  - wage bill and employment
  - capital, value added, and output
  - industry and ownership
  - local statutory minimum-wage amount and applicable dates
  required_identifiers: [firm ID, year, local wage-floor jurisdiction, industry]
  treatment_key: [local wage-floor jurisdiction, year, lagged firm ID]
  treatment_source: >
    Paper's 1996–2012 county/city minimum-wage panel from MOHRSS and China
    Academy of Labor and Social Security, joined to ASIF/CIED firm data.
    Official notices such as the inspected Shenzhen schedule can verify
    individual locality-periods but do not reproduce the full panel.
  measurement_risks:
  - No employee-level wage distribution to observe true low-wage worker share
  - Within-year revisions are compressed to an annual average
  - Small-firm coverage and firm survival vary in ASIF
  - Statutory rates do not directly verify compliance
  - Revenue TFP uses industry deflators rather than firm-specific output prices
evidence:
- id: E1
  source_type: paper
  citation: 'Hau, Harald, Yi Huang, and Gewei Wang. 2019. "Firm Response to Competitive Shocks: Evidence from China''s Minimum Wage Policy." ECGI Finance Working Paper 561/2018, June 16 author manuscript; published in Review of Economic Studies 87(6), 2639–2671 (2020), DOI 10.1093/restud/rdz058.'
  url: https://www.ecgi.global/sites/default/files/working_papers/documents/finalhauhuangwang_0.pdf
  date: 2019
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.unit
  - assignment.exposure_construction
  - design.identifying_variation
  - design.primary_strategy
  - design.treatment_variable
  - empirical_requirements.population
  - empirical_requirements.treatment_source
  - design_applications.treatment_encoding
  - design_applications.empirical_design
  verification_status: verified
  access_level: full-text
  locator: '93-page author manuscript dated 2019-06-16: §4.1 printed pp.12–13; §4.2 pp.13–14; §5 pp.15–17, equations (2)–(3); §6.1 p.18, equation (4); introduction pp.1–3. Inspected 2026-10-02.'
- id: E2
  source_type: implementation-document
  citation: 'Ministry of Labor and Social Security. 2004. Minimum Wage Regulations (最低工资规定), Decree No. 21; full decree reproduced by Hubei Department of Human Resources and Social Security.'
  url: https://rst.hubei.gov.cn/zfxxgk/zc/qtzdgkwj/200612/t20061201_704560.shtml
  date: 2004
  supports:
  - identity.authority
  - identity.implementation_regime
  - timeline.effective
  - assignment.compliance
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: official-document
  locator: 'Government-hosted full decree, preamble and Articles 2–13, 15: issued 2004-01-20, effective 2004-03-01; differentiated areas, provincial approval and publication, two-year minimum adjustment, employer payment and penalties. Inspected 2026-10-02.'
- id: E3
  source_type: implementation-document
  citation: 'Shenzhen Labor and Social Security Bureau. 2007. 深圳市劳动和社会保障局关于公布深圳市2007年度最低工资标准的通知, 深劳社规〔2007〕15号, government gazette 2007 no. 45.'
  url: https://www.sz.gov.cn/zfgb/2007/gb575/content/post_4943282.html
  date: 2007
  supports:
  - timeline.local_timing
  - identity.implementation_regime
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: 'Full Shenzhen government-gazette notice: 2007-07-01 to 2007-09-30 SEZ/outside monthly 810/700 RMB; 2007-10-01 to 2008-06-30 850/750 RMB; notice signed 2007-11-28 and web-published 2007-12-13. One locality only. Inspected 2026-10-02.'
- id: E4
  source_type: paper
  citation: 'Oxford University Press. 2020. Publisher DOI metadata for Hau, Huang, and Wang, Review of Economic Studies 87(6), 2639–2671.'
  url: https://doi.org/10.1093/restud/rdz058
  date: 2020
  supports: [design_applications.journal, design_applications.year, design_applications.doi]
  verification_status: verified
  access_level: metadata
  locator: 'Oxford Academic Review of Economic Studies volume 87 issue 6 contents lists this title on pp.2639–2671 with DOI 10.1093/restud/rdz058; the author listing independently confirms the publication. Metadata only, not the substantive design. Inspected 2026-10-02.'
design_applications:
- paper: 'Firm Response to Competitive Shocks: Evidence from China''s Minimum Wage Policy'
  doi: 10.1093/restud/rdz058
  journal: Review of Economic Studies
  year: 2020
  research_question: How do mainland industrial firms with different predicted labor-cost exposure change input use and productivity after local minimum-wage increases?
  population: ASIF/CIED industrial firms observed 2002–2008; small firms incompletely covered
  outcome: Employment, capital-to-labor ratio, value added, capital, and revenue-based productivity growth; export quantities/prices in a linked robustness sample
  data_used:
  - Annual Survey of Industrial Firms / Chinese Industrial Enterprise Database, 2002–2008
  - Local minimum-wage panel from MOHRSS and China Academy of Labor and Social Security, 1996–2012
  - Chinese customs export quantity/value data for robustness
  - Separate management-practices survey for exploratory interpretation, not the main firm-panel treatment
  treatment_encoding: Annual local minimum-wage log change times nonlinear impact factor estimated from prior firm mean wage / prior local minimum wage
  comparison: Differential firm-year outcome response by predicted exposure within changing local wage-floor regimes, conditional on firm and industry-year effects
  empirical_design: Two-step wage-response impact-factor estimation followed by firm-panel reduced-form outcome regressions
  assumptions:
  - Conditional revision timing and predicted exposure are not driven by omitted differential firm shocks
  - Lagged mean wage adequately proxies true incidence of a wage-floor increase
  threats_addressed: [local economic conditions, firm heterogeneity, incomplete small-firm coverage, output-price deflator error]
  evidence_refs: [E1, E2, E3, E4]
method_transfer: null
readiness_blockers:
- The full locality-by-year wage-floor panel and firm microdata were not independently reconstructed; E3 checks one local schedule, not all paper-coded changes.
- Detailed methods were inspected in the 2019 author manuscript; the final 2020 journal PDF was not compared line by line.
- The impact factor proxies low-wage labor with lagged firm mean wages; no employee-level pay shares or firm-level compliance panel were verified.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

China's Labor Law introduced a local minimum-wage system before the paper's sample. The 2004 decree changed its regulatory framework—coverage, hourly rates, review, publication, supervision, and adjustment frequency—but did not constitute one uniform firm-level treatment on one date [E1, paper-reported history; E2, verified regulation]. Provincial authorities approve locally differentiated standards. Shenzhen's gazette provides one concrete schedule with different rates inside and outside the then-special economic zone [E3, verified local example].

## What Changed

The empirical shock is a sequence of local wage-floor revisions during the 2002–2008 industrial-firm observation window. The authors draw the minimum-wage panel from government and labor-research sources and average rates within a calendar year when a locality changes them midyear [E1, reported construction]. A dated local notice is useful for checking one jurisdiction; it does not validate all the author's 17,000-plus coded changes.

## Implementation and Assignment

A firm's location determines its statutory floor, but the same local increase should have very different labor-cost effects for firms paying different average wages. The decisive distinction is measurement: the paper **does not observe employee-level wage shares**. It estimates a nonlinear impact factor from last year's firm average wage relative to last year's local minimum wage and interacts that factor with this year's local wage-floor change [E1, §5]. Calling the treatment an observed share of low-wage workers would misdescribe the actual design.

## Why This Creates Empirical Variation

With firm effects and industry-by-year effects, the paper asks whether a firm's outcome changes more in a revision year when its predicted wage-floor exposure is high. It reports labor-to-capital substitution and ownership-specific productivity responses; those are paper estimates, not legal facts [E1, §§5–6]. The research claim depends on conditional comparability of firms and local revision timing. The regulation itself says standard-setting considers local costs, wages, development, and employment, so a wage-floor hike must not be presented as random assignment [E2, Article 6].

## Identification Risks

Local policy can track unobserved local changes, while initially low-average-wage firms may have different trends for reasons unrelated to a new wage floor. The paper tests some local-cycle predictors and includes firm and industry-year effects, but these steps do not prove randomness [E1, §§4–6]. Annual averaging conceals exact within-year exposure; the Shenzhen notice even documents a stated start that predates the published notice [E3]. Incomplete small-firm coverage and industry rather than firm output-price deflators also limit broader interpretation [E1, §4.2].

## Data Requirements

Reuse requires the firm-year panel, location and industry crosswalks, wage bill and employment to calculate lagged mean wages, plus dated local minimum-wage schedules to construct annual averages. Capital, employment, and value-added fields support the primary outcomes; customs exports and management survey data support distinct secondary checks [E1, §4]. The project record points to the evidence and design, not a substitute for validating access to those microdata.

## Evidence Notes

The government decree establishes the institutional framework, and the Shenzhen gazette independently confirms one differentiated local revision [E2–E3, verified]. The author manuscript establishes the paper's exposure formula and application [E1, reported design]. The grounded status therefore means this conditional design is sufficiently described for research triage, **not** that every county-year rate, enforcement outcome, or final publisher-version detail has been independently reproduced.
