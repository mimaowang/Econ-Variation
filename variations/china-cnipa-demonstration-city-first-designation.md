---
schema_version: 2
id: china-cnipa-demonstration-city-first-designation
name: China CNIPA demonstration-city first-designation exposure
aliases:
  - 国家知识产权示范城市
  - CNIPA intellectual-property demonstration cities
status: grounded
provenance:
  task_id: task-9f93cfa16505
scope:
  country: China
  regions: [Mainland China]
  domains: [innovation, firm-behavior, urban-economics, intellectual-property]
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    Mainland firms inherit exposure to a selected local intellectual-property
    governance program through their registered jurisdiction. A 2026 Chinese
    economics-journal article actually uses designation timing to study patent
    knowledge flows. This is not an IP court opening, innovative-city award,
    enterprise-level IP award, or a direct measurement of enforcement intensity.
identity:
  instrument: National intellectual-property demonstration-city designation, with the first four cohorts approved in 2012, 2013, 2015 and 2016.
  authority: State Intellectual Property Office, now CNIPA; provincial IP authorities recommend and supervise local governments.
  legal_identifiers:
    - 国知发管字〔2011〕160号 — assessment framework cited in the original 2013 notices
    - 国知办发管字〔2013〕15号 — 2013 nomination process
    - 国知发管字〔2014〕34号 — revised assessment and management framework cited by subsequent notices
    - 国知发管函字〔2015〕43号 — four third-cohort approvals
    - 国知发管函字〔2016〕53号 — fourth-cohort approval
  implementation_regime: >
    Selected local governments prepare and implement IP governance plans under
    provincial guidance and national assessment. Designation covers creation,
    use, protection, management and services rather than a uniform subsidy or
    judicial intervention. Three-year designation periods and review coexist
    with the paper's absorbing first-designation exposure.
  assignment_mechanism: >
    Voluntary local application, provincial screening and national assessment
    of eligible places with previous pilot or demonstration preparation.
    Selection depends on existing IP capacity and performance. The 2013
    nomination cap was 50 percent of eligible places in each province; it is not
    established as an invariant rule for all cohorts.
  parent: null
  related_variations: [china-intellectual-property-courts-reform]
timeline:
  announcement: First cohort approved in April 2012; later notices have distinct signature, publication and designation-period dates.
  effective: No single national effective date; use the approved jurisdiction's first designation year for annual first-exposure designs.
  implementation_start: 2012
  implementation_end: 2016
  local_timing: >
    This endpoint bounds entry into the first-four-cohort roster, not policy
    termination. The 2015 review notice verifies 23 April-2012 approvals and
    describes their 2012–2014 term. The second cohort's notice was signed
    2013-09-17, posted 2013-10-25 and specifies September 2013–August 2016.
    Eight third-cohort units have March 2015–March 2018 terms under a notice
    signed 2015-02-28; four others have April 2015–April 2018 terms under
    the 2015-04-13 approval. The fourth-cohort notice was signed 2016-05-05,
    posted 2016-07-28 and specifies May 2016–May 2019. The earlier third-cohort
    proposal was signed in October 2014; that proposal is not final designation.
  anticipation: Eligible places already undertook pilot work and prepared applications; designation need not mark the first change in local IP investment or enforcement.
  last_verified: '2026-10-05'
assignment:
  unit: Named local-government jurisdiction at designation; firm-year exposure through registered location in the research application.
  treated: Firms whose registered locations fall inside a designated jurisdiction, from that jurisdiction's first designation year onward for the absorbing exposure application.
  comparison_pool: >
    Firms in not-yet-designated or undesignated jurisdictions. The paper's
    baseline TWFE also permits comparisons involving already-treated groups;
    a new cohort-specific analysis should use appropriate untreated comparisons.
    Other IP policies, later designation and knowledge spillovers must be checked
    before interpreting an apparently untreated location as a clean control.
  rule: >
    Xie, He and Zhang (2026), Section III and Table 1, set IP_Protect to one
    in and after the recognition year of the firm's registered city, otherwise
    zero. This encodes exposure since first designation, not a continuously
    valid designation certificate. For a jurisdiction-faithful reconstruction,
    map the dated official entities below to historical registered locations;
    the first applicable designation supplies onset. A county or district award
    does not assign the rest of its parent municipality. The authors' exact
    administrative aggregation and location-history file were not inspected.
  intensity: Binary first-designation exposure; local plan execution and enforcement intensity are distinct, unmeasured dimensions.
  exemptions:
    - Pilot status and eligibility to apply are not demonstration designation.
    - An approved county-level city or municipal district is not its entire parent city.
    - Strong-city creation, IP protection demonstration zones and enterprise or park awards are separate instruments.
  compliance: Official approvals require local work plans and support; designation alone does not establish identical spending, implementation or firm participation.
  exposure_construction: >
    Preserve each official entity's name, province, administrative level, first
    designation year and applicable boundaries. Join firm registration geography
    to the historical jurisdiction, not a present-day name-only parent-city map.
    Where a prefecture and a nested county are both designated, retain both
    institutional events but use the first applicable exposure for a firm; do
    not create a second observation or count a second variation. Use district
    geography in directly administered municipalities, or transparently exclude
    those municipalities as in the paper's reported robustness exercise.
    Changing registered locations requires an explicit time-varying or fixed
    pre-policy location convention and migration sensitivity analysis.
  required_identifiers:
    - firm identifier and calendar year
    - historical registered-location county or district identifier
    - historical parent-prefecture and province identifiers
    - designated-entity identifier, administrative level and first-designation year
    - patent publication/application identifier and applicant-to-firm crosswalk
    - cited and citing patent identifiers with citation year and firm industry
  spillovers: Knowledge flows between firms can cross administrative borders; an untreated citing or cited partner may still be affected by a treated partner.
research_compatibility:
  outcome_domains: [patent knowledge flows, innovation, knowledge diffusion, firm cooperation]
  affected_populations: [mainland listed nonfinancial firms, firms in designated jurisdictions, patent-linked firms outside those jurisdictions]
  mechanism_channels: [local IP governance and services, enforcement and appropriability, innovation cooperation and knowledge disclosure]
  best_for:
    - Firm innovation or knowledge-flow panels with historical registration geography and patent links.
    - Studying exposure to a local IP governance package rather than one specific enforcement measure.
  not_good_for:
    - Treating selected cities as randomly assigned or treating all 64 entities as disjoint prefecture cities.
    - Claiming that first-designation exposure measures current valid qualification or an isolated court/subsidy effect.
    - Assigning an entire municipality from one district designation when finer registration geography is absent.
design:
  claim_type: reduced-form
  affordances: [staggered first-designation years, public jurisdiction rosters, firm-year patent outcomes]
  candidate_designs: [cohort-specific DID, event study, the published firm-and-year-FE DID application]
  identifying_variation: Differences in first-designation timing across registered jurisdictions, linked to firm outcomes before and after designation.
  primary_strategy: >
    The 2026 application regresses next-year patent knowledge flows on current-
    year IP_Protect, controls and firm/year fixed effects. Baseline standard
    errors are clustered by firm. It reports a Borusyak–Jaravel–Spiess
    imputation check and alternative city clustering; the corresponding
    auxiliary result tables are available on request, not displayed in the
    inspected article.
  estimand: Conditional effect of exposure since designation to the local governance package on subsequent firm knowledge flows; not the isolated causal effect of legal protection intensity.
  treatment_variable: IP_Protect_it = 1 after first recognition, including the recognition year, using the firm's registered jurisdiction.
  comparison_logic: >
    Compare the evolution of outcomes for firms in selected jurisdictions with
    suitable untreated firms, conditioning on common time shocks and firm
    effects. Selection and prior pilot activity can still generate different
    trends. The paper uses the year before designation as event-study reference.
  estimation_notes: >
    The inspected article uses 2009–2021 Shanghai/Shenzhen A-share firm-years,
    retains companies listed by 2012, excludes financial/ST/*ST/PT firms and
    missing main variables, and reports 18,658 observations. Patent collection
    ends in 2022 because the outcome is at t+1. Cross is the IHS of outgoing
    plus incoming same-industry patent citations, not a raw count or a simple
    percentage growth rate. Continuous variables are winsorized at one percent
    in both tails. Baseline controls include firm financial/governance measures,
    IHS authorized-invention patent stock and log city GDP per capita. Reported
    PPML and pre-policy-control trend checks do not constitute inspected code.
  assumptions:
    - Absent designation, selected and comparison firms would have followed comparable outcome trends conditional on the design.
    - Anticipation and prior pilot investments do not invalidate the chosen onset and comparison.
    - Registration changes, later policies and cross-border knowledge spillovers are handled rather than assumed absent.
    - Patent citation coverage and applicant/industry links are comparable across treatment groups and years.
  diagnostics:
    - Inspect pre-treatment trends, prior pilot dates and application preparation; insignificant leads are not proof of random selection.
    - Use cohort-robust estimates and geographic clustering suited to jurisdiction-level assignment.
    - Compare verified county/district assignment with coarser mappings and an explicitly municipality-excluded sample.
    - Check location changes, overlapping IP policies, neighbor exposure and citation coverage/right truncation.
threats:
  - type: selective designation and prior treatment
    basis: documented
    condition: Eligibility and assessment depend on prior IP work, resources, enforcement and patent performance.
    evidence_refs: [E3, E2]
    possible_diagnostics: [pre-policy outcomes and pilot histories, eligible-applicant comparisons, cohort-specific pre-trends]
  - type: administrative aggregation error
    basis: documented
    condition: County-level cities and directly administered municipal districts are mixed with prefectures; the paper itself flags municipality district timing.
    evidence_refs: [E1, E4, E5, E6, E7]
    possible_diagnostics: [historical jurisdiction crosswalk, district-level joins, municipality-excluded estimates]
  - type: designation term versus absorbing exposure
    basis: documented
    condition: Official terms and cancellation/review rules do not imply permanent valid status, whereas the paper keeps first-designation exposure at one.
    evidence_refs: [E1, E2, E4, E5, E6, E7]
    possible_diagnostics: [label estimand as exposure since first designation, separate valid-status history if that is the research question]
  - type: bundled and successor institutions
    basis: documented
    condition: Local plans are heterogeneous and the later strong-city creation process selects from successful demonstration cities.
    evidence_refs: [E4, E7, E8]
    possible_diagnostics: [local plan review, overlapping-policy dates, shorter follow-up windows]
  - type: inference and transformed citation outcome
    basis: reported
    condition: Baseline firm clustering differs from jurisdiction-level assignment; IHS citation outcomes with zeros do not have a universal percentage-effect interpretation.
    evidence_refs: [E1]
    possible_diagnostics: [jurisdiction clustering, PPML/count-outcome sensitivity, incoming versus outgoing citation decomposition]
  - type: registration sorting and network interference
    basis: inferred
    condition: Firms may change registered locations and knowledge links cross jurisdiction boundaries, changing exposure and contaminating comparisons.
    evidence_refs: [E1]
    possible_diagnostics: [pre-policy location exposure sensitivity, relocation sample audit, partner-treatment exposure]
empirical_requirements:
  contract_version: 1
  population: Mainland nonfinancial A-share firms listed by 2012 for the inspected application; other populations require a separate representativeness judgment.
  observation_unit: firm-year
  geography_level: Historical registered county/district nested within prefecture or directly administered municipality.
  time_start: 2009
  time_end: 2021
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields:
    - registered location with historical county/district and parent jurisdiction
    - first designation year and entity administrative level
    - same-industry outgoing and incoming patent citation counts at t+1, through 2022
    - firm listing date, listing status and industry classification
    - patent applicant-to-firm links and authorized-invention patent stock
    - firm financial/governance controls and city GDP per capita for the published specification
  required_identifiers: [firm_id, year, registered_jurisdiction_id, designated_entity_id, patent_id, cited_patent_id, industry_code]
  treatment_key: [registered_jurisdiction_id, year]
  treatment_source: Official first-four-cohort notices and the 2015 first-cohort review roster below; paper Section III specifies absorbing first-year coding, but its exact firm-city mapping file was not obtained.
  measurement_risks: [nested county awards and prefecture overlap, current versus historical registration, patent applicant-name matching, industry classification, next-year outcome and citation truncation]
evidence:
  - id: E1
    source_type: paper
    citation: '解子恒、何祺、张振堃 (2026). “闭门造车”还是“同舟共济”：知识产权保护与创新知识流动. 财经研究 52(7):154–168.'
    url: https://doi.org/10.16538/j.cnki.jfe.20260414.301
    date: '2026-07-03'
    supports: [assignment.rule, assignment.unit, design.primary_strategy, design.treatment_variable, design.estimation_notes, design.comparison_logic, empirical_requirements.population, empirical_requirements.required_fields, design_applications.treatment_encoding, design_applications.data_used]
    verification_status: reported
    access_level: full-text
    locator: 'Actual publisher HTML: https://qks.shufe.edu.cn/mv_html/j00001/202607/s8nSWb20-82vx-qbpG-Db8D-LntaYJ03fZGm_WEB.htm; Sections II–IV, equations 1–2, Tables 1–2 and footnotes 3–9. Sections III–IV retrieved and read as full text, not inferred from the landing abstract.'
  - id: E2
    source_type: policy-document
    citation: CNIPA office notice on 2015 assessment and first-cohort review, signed 2015-02-26.
    url: https://www.cnipa.gov.cn/art/2017/9/22/art_379_137989.html
    date: '2015-02-26'
    supports: [identity.implementation_regime, timeline.implementation_start, timeline.local_timing, assignment.treated, assignment.compliance]
    verification_status: verified
    access_level: official-document
    locator: 'Opening paragraph; I(1) and I(3); II(1) lists all 23 April-2012 approvals; II(2)–II(4) covers term review and cancellation. Web posting date 2017-09-22 is not enactment.'
  - id: E3
    source_type: policy-document
    citation: CNIPA office 2013 demonstration-city nomination notice, 国知办发管字〔2013〕15号.
    url: https://www.cnipa.gov.cn/art/2013/4/12/art_379_138024.html
    date: '2013-02-18'
    supports: [identity.authority, identity.assignment_mechanism, assignment.rule, timeline.anticipation]
    verification_status: verified
    access_level: official-document
    locator: Sections I–IV, especially prior-status eligibility, provincial 50-percent cap, application/assessment process and prior enforcement/patent criteria.
  - id: E4
    source_type: policy-document
    citation: CNIPA notice designating Xiamen and 17 other jurisdictions, signed 2013-09-17.
    url: https://www.cnipa.gov.cn/art/2013/10/25/art_379_137931.html
    date: '2013-09-17'
    supports: [identity.instrument, identity.implementation_regime, timeline.local_timing, assignment.treated, assignment.unit, assignment.compliance]
    verification_status: verified
    access_level: official-document
    locator: Opening approval paragraph with the complete 18-unit roster, September2013–August2016 term and subsequent local-plan paragraph.
  - id: E5
    source_type: policy-document
    citation: CNIPA notice designating Changzhou and seven other jurisdictions, signed 2015-02-28.
    url: https://www.cnipa.gov.cn/art/2015/3/3/art_379_137991.html
    date: '2015-02-28'
    supports: [identity.instrument, timeline.local_timing, assignment.treated, assignment.unit]
    verification_status: verified
    access_level: official-document
    locator: First substantive paragraph names eight approved units and March2015–March2018 term; signature separates approval from the posted date.
  - id: E6
    source_type: policy-document
    citation: 'CNIPA notice designating Foshan and three other jurisdictions, 国知发管函字〔2015〕43号; Official Gazette 2015 issue 2, printed page 41.'
    url: https://www.cnipa.gov.cn/transfer/docs/pub/old/gk/jgb/201608/P020160829312534599722.pdf
    date: '2015-04-13'
    supports: [identity.legal_identifiers, timeline.local_timing, assignment.treated, assignment.unit]
    verification_status: verified
    access_level: official-document
    locator: PDF page45/66, printed41, rendered and visually read; Foshan, Zhongshan, Beijing Chaoyang and Nanchang, April2015–April2018 term and April13 signature.
  - id: E7
    source_type: policy-document
    citation: CNIPA fourth-cohort designation notice, 国知发管函字〔2016〕53号.
    url: https://www.cnipa.gov.cn/art/2016/7/28/art_379_138011.html
    date: '2016-05-05'
    supports: [identity.instrument, identity.implementation_regime, timeline.local_timing, timeline.implementation_end, assignment.treated, assignment.unit, assignment.compliance]
    verification_status: verified
    access_level: official-document
    locator: Approval paragraph names 11 jurisdictions and May2016–May2019 term; subsequent implementation paragraph and May5 signature, distinct from July28 posting.
  - id: E8
    source_type: policy-document
    citation: CNIPA office strong-city creation assessment notice, 国知办函管字〔2016〕864号, signed 2016-12-01.
    url: https://www.cnipa.gov.cn/art/2017/3/21/art_379_138014.html
    date: '2016-12-01'
    supports: [identity.implementation_regime, assignment.exemptions, timeline.anticipation]
    verification_status: verified
    access_level: official-document
    locator: Sections I–II; demonstration review or two years of top-half assessments are eligibility conditions for a separate strong-city creation application and expert review.
design_applications:
  - paper: '解子恒、何祺、张振堃 (2026), “闭门造车”还是“同舟共济”：知识产权保护与创新知识流动.'
    doi: 10.16538/j.cnki.jfe.20260414.301
    journal: Journal of Finance and Economics / 财经研究
    year: 2026
    research_question: Does local IP governance designation change innovation knowledge flows between firms?
    population: 2009–2021 mainland Shanghai/Shenzhen A-share nonfinancial firms listed by2012; 18,658 firm-year observations after stated exclusions.
    outcome: IHS of incoming plus outgoing same-industry patent citations in the following year.
    data_used: [CNIPA patents, CSMAR and CNRDS financial/nonfinancial firm data, manually collected government designation lists and dates]
    treatment_encoding: Registered city's recognition year and subsequent years equal one; 64 designated units reported. Exact district/county aggregation and registration-history file remain uninspected.
    comparison: Other sampled firms before or without coded designation, with firm and year effects; not a randomized local-government comparison.
    empirical_design: Firm-and-year-FE DID, next-year outcome; baseline firm clustering; pre-1 event-study reference; imputation DID and robustness exercises described in text.
    assumptions: [conditional parallel trends, appropriate handling of prior pilots and anticipation, valid registered-geography exposure, no uncontrolled outcome-relevant spillover or bundled-policy confounding]
    threats_addressed: [reported 1000 mixed-placebo draws, reported imputation DID, reported municipality exclusion, reported PPML raw-citation check, reported geographic-clustering alternatives]
    evidence_refs: [E1]
method_transfer: null
readiness_blockers:
  - For exact reproduction obtain the authors' unit-year and firm-registration crosswalk, including county/district aggregation and location changes; official rosters below support a transparent new construction but do not certify the published 64-unit join.
  - For an active-status rather than first-exposure question obtain actual renewal/cancellation histories; absorbing exposure is not that estimand.
  - Auxiliary endogeneity and robustness result tables are on request; no code or independent replication was inspected.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Local governments already performed IP pilot and demonstration-preparation work
before receiving this designation. The 2013 nomination rules select applicants
with specified prior status and assess capacity, patent performance, government
resources and enforcement [E3]. Designation is consequently a selected local
governance intervention, not the invention of IP protection from zero.

## What Changed

Approval brings the named jurisdiction into a nationally assessed demonstration
program. Local governments develop work plans; provincial authorities support
and supervise them [E4, E7]. The package is broader than judicial protection, and
implementation can differ across places. Later strong-city creation uses another
application and assessment process; its awards must not silently extend this
roster [E8].

## Implementation and Assignment

The first four cohorts contain 64 named designation entities. These are not 64
disjoint prefecture cities. The recoverable roster is:

| First designation year | Named units | Source |
|---|---|---|
| 2012, April approvals (23) | 武汉、广州、深圳、成都、杭州、济南、青岛、哈尔滨、南京、大连、西安、长沙、苏州、郑州、南通、镇江、福州、东营、烟台、洛阳、泉州、温州、芜湖 | E2, II(1) |
| 2013 (18) | 厦门、宁波、长春、东莞、无锡、株洲、泰州、潍坊、淄博、合肥、嘉兴、南阳、湖州、昌吉回族自治州、新乡、贵阳、常熟、昆山 | E4 |
| 2015, March term (8) | 常州、安阳、宜昌、湘潭、攀枝花、江阴、丹阳、张家港 | E5 |
| 2015, April term (4) | 佛山、中山、北京市朝阳区、南昌 | E6 |
| 2016, May term (11) | 四川绵阳、广东惠州、四川德阳、北京市海淀区、上海市闵行区、天津市西青区、重庆市江北区、山东即墨、江苏海门、安徽宁国、浙江义乌 | E7 |

Province and historical administrative level matter: the second-cohort 泰州 is
the Jiangsu jurisdiction, not Zhejiang 台州. Changshu and Kunshan are named
county-level cities within an already-designated Suzhou prefecture. Their 2013
awards should not move Suzhou's first exposure from 2012 or create duplicate
treated observations [E2, E4; analytical inference]. Municipal districts require
district identifiers. Without them, a researcher should use a clearly restricted
sample rather than declaring all of Beijing treated in 2015.

The article explicitly chooses an absorbing first-recognition indicator [E1,
reported claim]. That choice can represent exposure since entry even after a
designation term ends. It cannot establish that legal qualification remains
valid: the official review process permits cancellation and renewed terms [E2].
An active-status design would need a separate history, not a renamed copy of the
absorbing variable. First designation and renewal are not two independently
counted variations in this record.

## Why This Creates Empirical Variation

Designation enters at different times and can be linked to firm registration.
The 2026 article studies the following year's same-industry patent knowledge
flows, combining incoming and outgoing citations [E1, reported claim]. A new
researcher can construct jurisdiction-faithful exposure from the roster and
historical registration, while keeping that construction distinct from an exact
replication of the authors' uninspected aggregation file. This distinction makes
the variation usable for conditional idea matching without certifying the paper's
estimates or inventing its missing code.

## Identification Risks

Selection rewards existing IP performance, and prior pilot work can alter
outcomes before designation [E3]. Neither a designation label nor insignificant
pre-trends removes that concern. Nested jurisdictions, registration changes,
knowledge links across borders and successor programs can also change the
comparison [E4, E7, E8; analytical inference]. For a firm-outcome DID, inference
should account for assignment shared across firms in the same jurisdiction.

The article describes municipality exclusion, imputation DID, placebo draws,
alternative clustering and PPML, but footnotes 6 and 8 say the auxiliary tables
are available on request [E1, reported claim]. Those descriptions are not an
independent robustness audit. An IHS coefficient on citation counts, especially
with zeros, should not be relabelled an unconditional percentage increase.

## Data Requirements

The essential join is designation entity and year to historical firm registration,
then firm to patent applicants and citation links. The inspected application
needs firm-years through 2021 and patent outcomes through 2022, not just patents
through 2021 [E1, reported claim]. Annual geography must distinguish county-level
awards from prefecture-wide coverage and district awards from municipality-wide
coverage. Firms with unresolved locations should remain explicitly unmatched.

A researcher investigating a different innovation outcome need not reproduce
the citation variable, but must state the new outcome and retain the same
institutional, exposure and comparison checks. Dataset acquisition and asset
documentation belong in the companion data-knowledge repository; this record
preserves the treatment and design contract.

## Evidence Notes

Grounding uses the actual 2026 full methods and complete official first-four-
cohort roster, not the original 2023 abstract alone. The original Statistical
Research article remains a linked source lead in the campaign note; its one-page
figures do not establish its treatment mapping. The 2026 manuscript's HTML was
retrieved and read from the publisher. The four-city 2015 approval was checked
visually in the official gazette at PDF page45, printed41; no PDF was saved here.

The 2015 nomination/review notice is posted in 2017 but signed in 2015 [E2]; use
the signature and substantive period, not the website migration date. Similarly,
third-cohort proposed eligibility in 2014 is not approval in 2014. The record is
grounded and conditional, not design-documented: exact author crosswalks, active-
qualification histories and undisplayed auxiliary results are not certified.
