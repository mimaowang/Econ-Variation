---
schema_version: 2
id: china-2015-drug-review-capacity-category-delay
name: China 2015 drug-review capacity reform and therapeutic-category delay reduction
aliases: [药品审评审批制度改革, therapeutic-category IND review-delay decline]
status: grounded
provenance:
  task_id: task-3734bd55748a
scope:
  country: China
  regions: [Mainland China]
  domains: [firm-innovation, industrial-economics, regulatory-capacity, pharmaceutical-industry, development]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: The national Chinese drug-review reform changes the regulatory environment facing applicants to China's CDE. An inspected working paper uses differential declines in therapeutic-category IND decision duration to study innovative filings and subsequent clinical development.
identity:
  instrument: The 2015 national drug-review capacity and backlog-clearance package, studied through therapeutic-category differences in realized IND review-delay reduction.
  authority: State Council and then China Food and Drug Administration; Center for Drug Evaluation implements technical review.
  legal_identifiers: [国发〔2015〕44号]
  implementation_regime: National review reform combines backlog clearance, professional review capacity, procedure and filing-quality changes with selective priority review and other pharmaceutical reforms. Later 2017 and 2018 clinical-permission procedures are companion changes, not proof of a universally operative 60-working-day clock in 2015.
  assignment_mechanism: National institutional exposure with continuous category-level intensity constructed by the paper from pre/post mean IND decision durations. Categories are not randomly assigned to large delay reductions; realized intensity can reflect queues, application composition and post-reform demand.
  parent: null
  related_variations: []
timeline:
  announcement: State Council opinion signed 2015-08-09 and publicly posted 2015-08-18.
  effective: National reform begins in 2015; no single legal effective day for the entire multi-component package or verified category-specific onset is established here.
  implementation_start: 2015
  implementation_end: null
  local_timing: The paper uses 2015 as the national event year, 2012–2014 and 2015–2017 IND submission cohorts to construct intensity, and 2011–2021 category-year outcomes. National capacity expands gradually. The 2017 opinion provides deemed clinical permission after a specified period; the July 2018 implementing document specifies 60 working days after acceptance and payment absent a negative or query notice. Later outcome responses are not later treatment onset.
  anticipation: The pre-reform backlog and firms' research pipelines can affect expectations and filing decisions. Check pre-2015 dynamics rather than assuming no anticipation from the signature date.
  last_verified: '2026-10-07'
assignment:
  unit: ATC therapeutic category, fourth classification level, interacted with application year.
  treated: Categories with larger observed reductions in mean IND decision duration; all categories face the national package.
  comparison_pool: Categories with smaller reductions and pre-2015 observations. The lowest reduction quartile is a lower-intensity group, not an untreated group.
  rule: For category j subtract mean decision duration for INDs submitted in 2015–2017 from mean duration for those submitted in 2012–2014, then scale by the cross-category standard deviation. Retain categories with filings and usable approval-time information in both windows. The reported main panel has 109 categories and 1,199 category-years in 2011–2021; zero filings in retained category-years remain zeros.
  intensity: Realized post-measured decline in IND decision duration, not a predetermined statutory eligibility score. Main text reports a 227-day standard deviation and Appendix B1 reports 228.45 days; exact replication requires the underlying series rather than selecting one number silently.
  exemptions: [Selected urgent or otherwise qualified products can receive priority review, Bioequivalence filing is a different procedure from the retained IND application object, IND clinical permission is not NDA marketing approval, Overseas data recognition and MAH pilots are companion instruments rather than separate exposure assignments in this record]
  compliance: The official opinion targets clearing accumulated applications by end-2016 and review within prescribed time limits by 2018; targets do not certify every application met a deadline. Filing-quality enforcement and applicant responses can change the pool whose waiting time is measured.
  exposure_construction: Recover IND application identifiers, submission/application dates, official decision dates, decision status and the provider's primary ATC-level-four mapping. Construct category window means from submission cohorts, preserve delayed decisions and missing-duration rules, standardize over the retained categories, and join the fixed intensity to category-year filing counts. Declare co-applicant counting and duration weighting before estimation; reproduce the authors' convention only after obtaining its implementation. Do not parse ATC level four as a literal four-character code or substitute acceptance-to-completion queue statistics for application-to-decision duration.
  required_identifiers: [IND_application_id, primary_ATC_level_four_code, application_year, applicant_names]
  spillovers: Firms can redirect pipelines across therapeutic categories; national capacity changes and competition affect lower-intensity categories too. Therapeutic substitution can violate independent-category comparisons.
research_compatibility:
  outcome_domains: [innovative drug applications, clinical development, pharmaceutical innovation]
  affected_populations: [applicants submitting INDs to China's CDE, retained therapeutic categories]
  mechanism_channels: [regulatory waiting costs, review capacity, research-pipeline adjustment, entry and competition]
  best_for: [Category-level studies of regulatory capacity and innovation with application histories, Conditional continuous-intensity event studies of a national regulatory package]
  not_good_for: [A random priority-review experiment, An isolated effect of review staff alone, A national treated-versus-untreated China DID, Marketing approval or clinical efficacy effects without separate data and design, A predetermined instrument based on realized post-reform duration]
design:
  claim_type: reduced-form
  affordances: [national reform date, therapeutic-category delay heterogeneity, pre-reform backlog alternative, annual filing panel with zeros]
  candidate_designs: [continuous-intensity PPML event study, delay-reduction quartile comparison, pre-reform backlog exposure sensitivity]
  identifying_variation: Differential changes in innovation across categories with larger versus smaller realized review-delay declines after the national reform.
  primary_strategy: The inspected paper estimates PPML filing counts with category and year fixed effects, year-specific coefficients on standardized decline, and demeaned pre-reform category characteristics interacted with the post-2015 indicator. It normalizes the 2014 coefficient to zero and clusters by ATC category. This is a conditional continuous-exposure comparison, not random assignment.
  estimand: Relative proportional changes in category-level IND filings associated with a one-standard-deviation larger delay decline under the national reform; causal interpretation requires ruling out endogenous intensity and differential category shocks.
  treatment_variable: Standardized category decline from 2012–2014 versus 2015–2017 submission cohorts, interacted with year indicators; post is 2015–2021.
  comparison_logic: Compare category trajectories relative to 2014, allowing differential post trends by pre-reform market size, concentration and innovation potential. Every comparison category can benefit from the national package.
  estimation_notes: The reported sample retains 8,920 of 9,642 raw IND applications across 109 of 287 categories. Pre-controls include US sales, filing count/HHI, IND share, target novelty and remaining patent term. The paper also uses the fraction of 2012–2014 filings unapproved at end-2014 as alternative exposure, not a demonstrated excluded instrument in a 2SLS design. Clinical-trial outcomes are linked to IND submission cohorts, not reindexed as trial-calendar-year filings. Exact co-applicant counting and window-mean weighting remain replication conditions.
  assumptions: [No unhandled category-specific innovation trends correlated with realized intensity, Delay reduction is not driven principally by endogenous filing or decision composition, Stable and appropriate ATC mapping and duration measurement, Reform components and later companion policies do not differentially confound the intended estimand, Cross-category spillovers and outcome censoring addressed]
  diagnostics: [Pre-2015 event coefficients with precision assessment, Use pre-reform backlog exposure and audit its selection, Compare quartiles and exclude extreme decline categories, Coarser ATC aggregation and firm-drug deduplication, Reconcile application versus co-applicant counts and duration weighting, Decision completion and trial right-censoring sensitivity, Audit ICH and NRDL timing without treating endogenous post outcomes as predetermined controls]
threats:
  - type: post-measured endogenous intensity
    basis: inferred
    condition: Delay decline uses post-2015 submitted applications and realized decisions, so pipeline demand, selection into filing and decision completion can correlate with both intensity and innovation outcomes. A pre-trend plot does not eliminate this problem.
    evidence_refs: [E1]
    possible_diagnostics: [pre-reform backlog contrast, submission-composition and completion checks, alternative fixed pre-policy exposure]
  - type: bundled and gradual national reform
    basis: documented
    condition: Capacity, quality enforcement, priority procedures and related rules change together; 2017/2018 clinical-permission changes cannot be retroactively assigned a uniform 2015 numerical deadline.
    evidence_refs: [E1, E2, E3, E4]
    possible_diagnostics: [explicit package estimand, cohort timing sensitivity, concurrent-policy and eligibility audit]
  - type: selected categories and counting conventions
    basis: reported
    condition: Retaining categories with usable duration in both windows selects on post-period observations. Appendix descriptions of co-applicant counting are not fully consistent, and exact treatment-mean weighting was not established from code.
    evidence_refs: [E1]
    possible_diagnostics: [retained versus excluded category comparison, unique-application and applicant-weighted alternatives, recover author construction before claiming replication]
  - type: clinical-trial joins and right censoring
    basis: reported
    condition: Trial matches use applicant and medical name or active ingredient. Later submission cohorts have less time to reach later phases, and the trial-matched sample has 108 rather than 109 categories.
    evidence_refs: [E1]
    possible_diagnostics: [harmonized follow-up horizon, unmatched-record audit, cohort-specific phase completion]
  - type: category interference
    basis: inferred
    condition: Competition, therapeutic substitution and firm portfolio reallocation can change outcomes in lower-intensity categories as well as higher-intensity ones.
    evidence_refs: [E1]
    possible_diagnostics: [firm portfolio exposure, adjacent therapeutic-category exclusions, interpretation as relative rather than total national effect]
empirical_requirements:
  contract_version: 1
  population: IND applications submitted to China's CDE, with categories retained according to documented duration coverage in both construction windows.
  observation_unit: ATC-category-year
  geography_level: National China application system; no province-based assignment is needed for the default design.
  time_start: 2011
  time_end: 2021
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields: [application type identifying IND, submission/application date, official decision date and status, primary ATC-level-four classification, co-applicant list and declared counting weights, annual IND filing count including zeros, standardized category delay decline, pre-reform US sales filing count HHI IND share target novelty and patent term for the published full specification]
  required_identifiers: [IND_application_id, primary_ATC_level_four_code, application_year]
  treatment_key: [primary_ATC_level_four_code, application_year]
  treatment_source: Author-linked August 2026 draft Eq2 and Appendix B specify category intensity; official national documents ground the institutional package but do not provide the 109-category intensity series.
  measurement_risks: [provider ATC assignment and data access, missing or negative decisions, co-applicant multiplicity, post-period category retention, post-measured intensity, mixing application-to-decision and acceptance-to-completion clocks]
evidence:
  - id: E1
    source_type: paper
    citation: 'Jia, Ruixue, Xiao Ma, Jianan Yang and Yiran Zhang. Improving Regulation for Innovation: Evidence from China’s Pharmaceutical Industry. Author-linked working draft, August 5, 2026.'
    url: https://www.ruixuejia.com/uploads/4/6/3/3/46339953/medical_reform_in_china__3_.pdf
    date: '2026-08-05'
    supports: [assignment.rule, assignment.intensity, assignment.exposure_construction, design.primary_strategy, design.estimation_notes, empirical_requirements.required_fields, design_applications.treatment_encoding, design_applications.data_used]
    verification_status: reported
    access_level: full-text
    locator: '77-page author PDF read in memory: main printed pp6–11 and14–20, especially Eq2–3 and Sections4.1–4.3; Appendix A1–2, B4–8 including TablesB1/B2a–c and variable definitions; Appendix D19–25 on backlog, outliers, clinical trials, ICH and NRDL. Author code and underlying provider files were not inspected. Publication status was checked on https://www.ruixuejia.com/working-papers.html, which labels R&R at AEJ Economic Policy, not published acceptance.'
  - id: E2
    source_type: policy-document
    citation: State Council opinion on reforming drug and medical-device review and approval, 国发〔2015〕44号, signed 2015-08-09.
    url: https://www.xinhuanet.com/politics/2015-08/18/c_128140289.htm
    date: '2015-08-09'
    supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.announcement, assignment.exemptions, assignment.compliance]
    verification_status: verified
    access_level: official-document
    locator: Full contemporaneous Xinhua reprint attributed to China Government Network, posted2015-08-18; signature and clauses2,6,8–14,19–20 inspected. Original government URL returned403. The document gives backlog targets and capacity measures, not a numerical60-day clock. Clause19 separates fee receipts and expenditures under budget management; it is not direct fee earmarking to review staff.
  - id: E3
    source_type: policy-document
    citation: General Offices of the CPC Central Committee and State Council, opinion deepening review and approval reform to encourage drug and device innovation, published 2017-10-08.
    url: https://app.www.gov.cn/govdata/gov/201710/08/413100/article.html
    date: '2017-10-08'
    supports: [identity.implementation_regime, timeline.local_timing, assignment.exemptions]
    verification_status: verified
    access_level: official-document
    locator: Full government mobile page; clauses5–6,9,28 and30. Clause5 permits clinical trials absent an objection within a specified period but does not itself give a numerical60-working-day duration.
  - id: E4
    source_type: implementation-document
    citation: NMPA announcement adjusting drug clinical-trial review and approval procedures, 2018No50, document signed2018-07-24.
    url: https://www.yjsds.com/web/article/1184822779404685312/web/content_1184822779404685312.html
    date: '2018-07-24'
    supports: [timeline.local_timing, identity.implementation_regime, assignment.exemptions]
    verification_status: verified
    access_level: official-document
    locator: Full agency document reprinted by Chongqing Drug Exchange and attributed to NMPA; opening and clauses6–10,18–19 inspected, not attachments. The reprint is posted July30, not independently authenticated as original publication/effective day. Acceptance plus payment starts the60-day no-objection procedure; clause18 defines working days. This is clinical-trial permission, not marketing approval.
design_applications:
  - paper: Improving Regulation for Innovation — Evidence from China’s Pharmaceutical Industry
    journal: Working paper; author page reports R&R at AEJ Economic Policy, not published
    year: 2026
    doi: null
    research_question: Do therapeutic categories with larger reductions in regulatory waiting time experience larger changes in innovative drug filings and clinical development?
    population: The paper's retained109 ATC categories of IND applications to China's CDE; the trial-matched application has108 categories.
    outcome: Annual IND filing counts and counts of associated applications reaching clinical-trial phases.
    data_used: [CDE application data2011–2021 with provider ATC mapping and durations, Chinese clinical-trial registrations2011–2022 for trial extensions, Pre-reform market-size concentration novelty and patent-term data]
    treatment_encoding: Category mean IND duration2012–2014 minus2015–2017 by submission cohort divided by cross-category SD, interacted with year;2014 reference.
    comparison: Larger versus smaller realized intensity before and after2015; no nationally untreated group.
    empirical_design: Category/year-FE PPML event study with ATC-clustered inference and pre-characteristic-by-post controls; quartile and pre-reform backlog alternatives.
    assumptions: [conditional parallel category trajectories, non-confounded intensity, appropriate selection and counting, valid trial links and follow-up]
    threats_addressed: [displayed pre-trends, alternative backlog exposure, quartiles and extreme-category exclusions, coarser category and deduplication checks, trial censoring and companion-policy sensitivity]
    evidence_refs: [E1]
method_transfer: null
readiness_blockers:
  - Conditional use only; realized post-reform delay reductions are not a predetermined or randomly assigned instrument. Defend the category comparison for the proposed outcome and distinguish the national package from an isolated capacity effect.
  - Obtain application histories and the provider ATC mapping, reconcile co-applicant counting and window-mean weights, and regenerate the SD before claiming exact replication. Body227 versus Appendix228.45-day scaling and inconsistent co-applicant descriptions remain explicit implementation uncertainties; no author code was inspected.
  - Trial outcomes require applicant/ingredient joins and equal follow-up sensitivity. Firm-level exposure, birthyear/ownership joins and international trial classifications are not certified by this default category-year contract.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

The empirical object is a reduction in the regulatory waiting costs of drug
development. Before reform, an applicant needed permission to start clinical
development, while review capacity and accumulated submissions created long
delays. The national2015 opinion seeks both faster review and better filing
quality through backlog clearance, professional teams, procedural reform and
enforcement [E2]. Permission to test a drug is not permission to market it.

## What Changed

The package does not randomly favor selected therapeutic categories. Its
national nature leaves no untreated Chinese system; the paper instead compares
categories whose observed waiting time falls by different amounts [E1, reported
claim]. That construction, not a generic policy name or priority-review label,
defines this record's primary assignment.

## Implementation and Assignment

For each retained primary ATC level-four category, construct mean duration from
application to official decision for2012–2014 submission cohorts and subtract
the corresponding2015–2017 cohort mean. Standardize the decline across retained
categories and attach it to annual filing counts2011–2021, including zeros.
The manuscript's "4-digit" wording refers to classification level, not a
four-character string restriction [E1, reported claim]. Categories without
usable duration in both windows do not become zero-exposure controls.

## Why This Creates Empirical Variation

The paper's fixed-effects PPML compares these trajectories relative to2014,
with pre-reform category characteristics allowed different post-reform trends.
It reports later innovation responses, consistent with a research pipeline,
but that does not shift the institutional event to2017 or2018 [E1, reported
claim]. Pre-reform backlog is an alternative exposure, not automatically an IV.

## The Timing Boundary That Matters

The2015 opinion sets clearance targets but does not establish a universal
60-working-day deadline [E2]. The2017 opinion introduces no-objection clinical
permission after a specified period [E3]. The2018 implementing announcement
explicitly gives60 working days after acceptance and payment, subject to
negative/query notices and continuing safety duties [E4]. Collapsing these
documents into a single2015 statutory clock would misstate the treatment.
Likewise, higher fees in2015 enter budget management; direct fee-to-staff
earmarking is not established by the legal text [E2].

## Identification Risks

Realized delay reduction contains post-reform information. Greater innovation
demand, changes in who files, and which decisions finish can influence the
measured exposure as well as the outcome [analytical inference]. Pre-trends,
backlog alternatives and composition checks help evaluate this comparison but
do not turn it into random assignment. The interpretable object is a conditional
relative response to a regulatory package, not its total national effect.

## Data Requirements

The default usable join is primary ATC category to application year. A new
implementation can declare unique-application counting and compare applicant
weights, but must not claim that this reproduces the author's baseline without
recovering code. Co-applicant descriptions and reported SD differ across the
inspected text; these are replication conditions, not numbers to invent.
Clinical-trial extensions additionally join applicant and active ingredient or
medical name and need equal follow-up horizons [E1, reported claim]. Do not
require registry ownership, M&A or global trial data for the default filing
design merely because the paper also uses them elsewhere.

## Evidence Notes

This grounded record supports conditional idea matching because the national
instrument, cohort windows, category exposure, comparison and minimum data
join are recoverable from inspected institutional documents and actual methods.
It is not an exact replication certificate or an unqualified causal shock.
The inspected version is an August2026 working paper, with R&R status on the
author page. The earlier NBER version is not silently substituted for this
version, and a prospective journal is not represented as a publication [E1].
