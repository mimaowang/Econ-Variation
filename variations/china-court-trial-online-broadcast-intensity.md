---
schema_version: 2
id: china-court-trial-online-broadcast-intensity
name: China Court Trial Online Reform and Court-Dispute-Quarter Broadcast Intensity
aliases: [China 2016 live-trial-broadcast reform, Women in the Courtroom judicial transparency exposure, 中国庭审公开网直播强度]
status: grounded
provenance:
  task_id: task-852806dce60b
scope:
  country: China
  regions: [Mainland China]
  domains: [judicial-institutions, governance, gender, digital-economy, development-economics]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    Chinese civil judgments are exposed to changing courtroom publicity during
    the 2016 national trial-broadcast platform expansion. The documented application
    concerns individual litigants in mainland courts; it does not establish an
    effect on firms or on foreign courts.
identity:
  instrument: Deployment of China Court Trial Online and varying local live-broadcast intensity
  authority: Supreme People's Court, with local courts selecting and implementing broadcasts
  legal_identifiers:
  - China Court Trial Online (中国庭审公开网), trial operation 2016-07-01 and formal launch 2016-09-27
  - People's Court Courtroom Rules (人民法院法庭规则), 2016 revision 法释〔2016〕7号, Articles 10-11
  - Provisions on Live and Recorded Trial Broadcasts (最高人民法院关于人民法院直播录播庭审活动的规定), 法发〔2010〕48号
  implementation_regime: >
    A national platform with phased court connection and locally selected case
    broadcasts. Universal connection is not universal broadcasting. The platform
    expansion is distinct from China Judgments Online's publication of judgments
    and from the requirement to record hearings for court use.
  assignment_mechanism: >
    Actual broadcasting varies across courts, legal dispute categories and quarters.
    The paper reports superior-court quotas and subordinate-court case selection;
    official rules establish permitted selection and public-hearing boundaries.
    This record follows observed broadcast intensity, with rollout timing used as
    an auxiliary event-study diagnostic rather than a second counted variation.
  parent: null
  related_variations: []
timeline:
  announcement: '2016-09-27'
  effective: null
  implementation_start: '2016-07-01'
  implementation_end: null
  local_timing: >
    Official reporting distinguishes July 2016 trial operation from September
    formal opening and nationwide connection by 2017-12-31. The paper's analysis
    spans 2014-2018 and uses prefecture-specific introduction quarters in its
    event study. Do not substitute the national launch for every local start.
  anticipation: >
    Live broadcasts and their legal framework predate this platform. Its measured
    pre-period is not proof of no previous publicity; preparation or early trial
    operation can precede a local formal start.
  last_verified: '2026-10-02'
assignment:
  unit: Court by legal dispute category by year-quarter, attached to individual civil judgments
  treated: Cases in court-dispute-quarter cells with greater observed live-broadcast intensity
  comparison_pool: >
    Other cells and quarters in the same documented judicial sample, using
    court-category, quarter and judge fixed effects; female and male plaintiffs
    supply the additional contrast for the paper's gender-gap estimand.
  rule: >
    Courts choose broadcasts within public-hearing rules. The 2016 Courtroom Rules
    permit broadcasts for public-interest, socially influential or legally
    educational hearings; mandatory hearing recording does not mandate public
    streaming. The paper reports a hierarchy of quotas and case selection, not
    random assignment of individual broadcasts.
  intensity: Live-broadcast cases divided by total cases within the paper's court-dispute-category-quarter universe
  exemptions:
  - The 2010 broadcast provisions exclude legally nonpublic cases and certain justified objections, and require protection of unsuitable content.
  - Individual-only civil judgments define this paper's application; corporate, criminal and administrative cases are not its comparison pool.
  compliance: >
    Connected courts may broadcast only a fraction of cases. Paper-reported quotas,
    resources and selection generate heterogeneous realized intensity; no inspected
    source establishes a common binding national quota for every local court.
  exposure_construction: >
    Link judgment and broadcast records with validated case identifiers and court
    information; retain legal category and the date used to assign quarters.
    Aggregate matched broadcast status and the corresponding case denominator
    before attaching the ratio to judgment outcomes. The paper identifies case
    numbers as merge information; exact cleaning, denominator and unmatched-case
    decisions require the referenced sample-construction code before executable reuse.
  required_identifiers: [Case number, Court identifier, Legal dispute category, Analysis year-quarter, Judge name together with court, Prefecture identifier]
  spillovers: >
    Judges can respond to oversight beyond a broadcast case. Nearby courts' publicity
    can also affect behavior directly, which matters when their intensity supplies
    the leave-one-court-out instrument.
research_compatibility:
  outcome_domains: [Gender differences in civil litigation outcomes, Judicial attention and effort, Institutional accountability]
  affected_populations: [Individual civil litigants in published mainland Chinese judgments during 2014-2018]
  mechanism_channels: [Public scrutiny, Judicial attention, Judicial effort, Court performance incentives]
  best_for: [Studying changing female-male judicial outcome gaps under measured courtroom publicity with a matched case corpus]
  not_good_for:
  - A binary randomized broadcast-versus-nonbroadcast case experiment
  - A uniform national September 2016 treatment applied to an arbitrary city or firm panel
  - Inferring corporate contract enforcement effects from this individual-litigant application alone
design:
  claim_type: causal
  affordances: [Continuous implementation intensity, Within-court legal-category differences, Gender interaction, Predetermined-share IV diagnostic]
  candidate_designs: [Continuous-treatment gender-gap DID, Conditional Bartik IV for the same exposure]
  identifying_variation: >
    The female-male outcome gap is compared across changes in court-category-quarter
    intensity. National platform expansion motivates the exposure, but local
    intensity remains potentially endogenous; its identifying assumptions are
    outcome- and population-specific.
  primary_strategy: >
    Paper equation (2) includes intensity and Female times intensity, with
    court-category, year-quarter and judge fixed effects and case/regional controls.
    The interaction coefficient is the main gender-gap parameter, not the average
    publicity effect on all litigants.
  estimand: Conditional change in the female-male plaintiff outcome gap per unit increase in broadcast intensity in the documented sample
  treatment_variable: Observed court-category-quarter broadcast fraction and its interaction with female-plaintiff status
  comparison_logic: >
    Compare gender gaps as cell intensity changes, conditional on the stated fixed
    effects and controls. The case-level broadcast indicator is a component of
    exposure construction, not an independently randomized treatment.
  estimation_notes: >
    The paper clusters standard errors by court. Its Bartik predictor Z_kt sums
    2014 court-specific dispute-category shares times contemporaneous prefecture-
    category intensity excluding that court. Table 3 instruments intensity and
    Female times intensity using Z and Female times Z. It reports first-stage and
    Kleibergen-Paap statistics, but strength does not establish exclusion. The
    prefecture-start event study uses the preceding quarter as reference and bins
    distant leads/lags; its timing roster is a separate input, not inferred here
    from national connection totals.
  assumptions:
  - Conditional gender-gap trends and counterfactual responses across intensity levels support the continuous DID interpretation.
  - Selection into published judgments, observed gender and matched broadcasts does not produce the changing gap.
  - IV interpretation requires early case shares not to load on omitted differential outcome trends; other courts' broadcasts affect focal outcomes only through the modeled exposure after conditioning.
  - Exposure interference, concurrent judicial reforms and changing case mix do not invalidate the specified comparison.
  diagnostics: [Gender-gap event-study leads, Court trends and court-quarter fixed effects, Broadcast case selection, Small-cell sensitivity, Gender missingness and imputation, Share-view placebo and Rotemberg diagnostics, IV first stages and weak-identification checks]
threats:
- type: Case selection and endogenous intensity
  basis: documented
  condition: The paper's balancing exercise finds that plaintiff gender and other characteristics predict individual broadcasts; aggregation alone does not prove local intensity exogenous.
  evidence_refs: [E2, E3, E4]
  possible_diagnostics: [Replicate Table A2, Examine changing case composition, Use the paper's trend and fixed-effect checks]
- type: Shift-share exclusion and correlated oversight
  basis: inferred
  condition: Predetermined shares need not be exogenous, and prefecture-wide oversight can directly change focal-court gender gaps even after own-court broadcasts are excluded from the predictor.
  evidence_refs: [E4]
  possible_diagnostics: [Inspect 2014-share balance and placebo results, Recover Rotemberg weights, Test contemporaneous regional reforms and spillovers]
- type: Observed-judgment and gender selection
  basis: reported
  condition: The paper begins with 6424324 individual-party civil judgments, retains 4601718 with relevant gender information, and reports 3974316 observations in the main DID/IV regressions; these are different sample layers.
  evidence_refs: [E4, E5]
  possible_diagnostics: [Trace exclusions in sample_construction.do, Check publication and gender missingness by exposure, Compare two-litigant and imputed-gender analyses]
- type: Administrative connection counts versus analytic exposure
  basis: documented
  condition: The final paper reports 383 connected courts by September 2016 and 3517 by December 2017; the official report gives 427 on formal launch day and 3520 at end-2017. Exact roster/date definitions were not reconciled and neither aggregate is a treatment assignment list.
  evidence_refs: [E1, E4]
  possible_diagnostics: [Inspect the underlying court and prefecture start rosters before a rollout application, Preserve dated source counts]
- type: Outcome interpretation
  basis: reported
  condition: The main outcome is the defendant's share of litigation costs, used as a proxy for plaintiff success; it is not a binary probability, a conviction measure or an independently audited measure of discrimination.
  evidence_refs: [E4]
  possible_diagnostics: [Inspect cost-allocation extraction, Compare the paper's coarse winning indicator, Retain claim and case-type controls]
empirical_requirements:
  contract_version: 1
  population: Individual-party civil judgments in the paper's mainland court sample
  observation_unit: Civil judgment with court-category-quarter exposure
  geography_level: Court, mapped to prefecture for regional controls and the IV
  time_start: 2014
  time_end: 2018
  minimum_frequency: Quarterly exposure linked to dated case-level judgments
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields: [Broadcast status and matched-case universe, Court-category-quarter broadcast numerator and denominator, Plaintiff and defendant gender, Litigation-cost allocation outcome, Judge identifier, Case and regional controls, Sample and missingness flags]
  required_identifiers: [Case identifier, Court identifier, Legal dispute category, Analysis year-quarter, Judge identifier]
  treatment_key: [Court identifier, Legal dispute category, Analysis year-quarter]
  treatment_source: Matched China Court Trial Online records and the paper's sample-construction code; the national announcement alone supplies no cell intensity
  measurement_risks:
  - Legal dispute category is called area in the paper; it does not mean geographic district.
  - Trial, decision, upload and broadcast dates can differ; preserve the exact analysis-quarter convention.
  - Total cases must follow the documented denominator universe, not be silently replaced by every court filing or every website entry.
  - The paper codes multiple-party gender from the first listed party and identifies judges by name together with court; neither is a universal individual ID.
  - The IV additionally needs 2014 category shares and leave-one-court-out prefecture-category-quarter broadcasts; the event-study diagnostic needs data/begin.dta.
evidence:
- id: E1
  source_type: implementation-document
  citation: Supreme People's Court-hosted People's Court Daily report. 2018. 让公正看得见能评价受监督：中国庭审公开网直播庭审突破200万场.
  url: https://www.court.gov.cn/zixun/xiangqing/132651.html
  date: '2018-11-28'
  supports: [identity.instrument, identity.authority, identity.implementation_regime, timeline.announcement, timeline.implementation_start, timeline.local_timing, assignment.compliance, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Sections 从无到有，庭审公开实现全覆盖 and 遍地开花，庭审公开向纵深推进; trial/formal opening dates, 427/3520 connection counts and the separately dated Jiangsu 2018 requirement, inspected 2026-10-02. Administrative reporting does not verify the paper's analytic roster.
- id: E2
  source_type: policy-document
  citation: Supreme People's Court. 2016. 最高人民法院关于修改《中华人民共和国人民法院法庭规则》的决定; revised Rules Articles 10-11 and 27.
  url: https://www.court.gov.cn/zixun/xiangqing/19372.html
  date: '2016-04-13'
  supports: [identity.legal_identifiers, assignment.rule, timeline.anticipation]
  verification_status: verified
  access_level: official-document
  locator: Decision dated 2016-04-13, posted 2016-04-14; XIII-XIV and appended Courtroom Rules Articles 10-11, effective 2016-05-01. Recording requirement and permission to broadcast selected public hearings inspected 2026-10-02. This is not a uniform local broadcast quota.
- id: E3
  source_type: policy-document
  citation: Supreme People's Court. 2010. 最高人民法院关于人民法院直播录播庭审活动的规定, 法发〔2010〕48号; official Qingyun County Court reprint dated 2020-01-06.
  url: https://www.sdcourt.gov.cn/dzqyfy/393504/393506/5842730/index.html
  date: 2010
  supports: [identity.legal_identifiers, assignment.exemptions, assignment.rule, timeline.anticipation]
  verification_status: verified
  access_level: official-document
  locator: Full reprinted text retrieved directly by HTTP on 2026-10-02; Articles 1-6 and 8 establish pre-platform broadcasting, exclusions, case approval and local implementation. Read with the 2016 Rules' precedence clause; not an independently verified 2016 local quota roster.
- id: E4
  source_type: paper
  citation: 'Chen, Heng, Yuyu Chen, and Qingxu Yang. 2026. Women in the Courtroom: Technology and Justice. Review of Economic Studies 93(3):1574-1601. DOI 10.1093/restud/rdaf066; online 2025-08-01.'
  url: https://doi.org/10.1093/restud/rdaf066
  date: 2026
  supports: [identity.assignment_mechanism, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.intensity, assignment.compliance, assignment.exposure_construction, assignment.required_identifiers, timeline.local_timing, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, design.assumptions, design.diagnostics, design_applications.population, design_applications.outcome, design_applications.data_used, design_applications.treatment_encoding, design_applications.empirical_design, threats.condition]
  verification_status: verified
  access_level: full-text
  locator: Published article https://academic.oup.com/restud/article/93/3/1574/8220859, full publisher HTML retrieved through https://oup.silverchair-cdn.com/article-minimal/8220859 on 2026-10-02; Sections 2.2, 3.1-3.3, 4.2-4.4, equations 2-4 and Tables 2-3. Compared these core sections with https://www.restud.com/wp-content/uploads/2025/07/MS32629manuscript.pdf, pp.6-9 and 13-20; publication metadata and the core count/design statements agree. Empirical findings and sample completeness remain author-reported, not an executed reproduction.
- id: E5
  source_type: replication
  citation: Chen, Chen, and Yang. 2025. Replication Guide for Women in the Courtroom, Zenodo deposit 10.5281/zenodo.15729271.
  url: https://zenodo.org/records/15729271/files/readme.pdf
  date: '2025-06-24'
  supports: [empirical_requirements.treatment_source, empirical_requirements.measurement_risks, threats.condition]
  verification_status: reported
  access_level: replication
  locator: All five README pages inspected in memory via direct HTTP and PDF extraction on 2026-10-02; provenance statement and file/code table name raw.dta, regression.dta, begin.dta, share14.dta and sample/DID/IV scripts. README inspection does not verify archive contents, case joins, raw-source availability or a successful rerun.
design_applications:
- paper: 'Women in the Courtroom: Technology and Justice'
  doi: 10.1093/restud/rdaf066
  journal: Review of Economic Studies
  year: 2026
  research_question: Does greater judicial publicity change gender disparities in individual civil litigation outcomes?
  population: Individual-party Chinese civil judgments from 2014-2018; main DID/IV regression has 3974316 observations, and its two-litigant counterpart has 2063379
  outcome: Defendant's litigation-cost share as a proxy for plaintiff success; judicial-text attention and effort measures are additional outcomes
  data_used: [China Judgments Online documents acquired in 2020, China Court Trial Online broadcast records acquired through April 2021, China City Statistical Yearbook regional controls]
  treatment_encoding: Broadcast fraction at court-legal-category-year-quarter level and Female times that fraction
  comparison: Female-male outcome-gap changes across exposure cells and quarters conditional on court-category, quarter and judge fixed effects
  empirical_design: Continuous DID in equation 2; Bartik IV using 2014 category shares and leave-one-court-out prefecture-category broadcasting in equation 4 and Table 3
  assumptions: [Conditional gender-gap counterfactual trends and responses, Stable selection and measurement, Share-view IV exclusion for the instrumented application]
  threats_addressed: [Nonrandom case broadcasting, Court trends and court-quarter shocks, Gender missingness, Small-cell intensity, Initial-share confounding and instrument strength]
  evidence_refs: [E4, E5]
method_transfer: null
readiness_blockers:
- Before executable reuse, inspect the named sample-construction and regression scripts to confirm case joins, the analysis-quarter convention, intensity denominators, missing cells and sample exclusions; only the full paper and replication README were inspected here.
- A rollout-based application additionally needs the prefecture/court start roster; administrative connection totals and the unresolved 383/427 and 3517/3520 count differences cannot replace it.
- Extension to firms, new years or a new outcome requires an appropriate observed population and a fresh assessment of intensity/IV exclusion; the documented individual-litigant comparison does not supply these automatically.
---

## Institutional Background

[E2-E3, verified rules] Public courtroom broadcasts existed before the centralized
2016 platform. Courts could select suitable public hearings; exclusions and approval
procedures limited what could be shown. Recording a hearing for court purposes and
streaming it to the public are different actions. This history matters: the reform
expands and organizes publicity rather than introducing the first possible camera
or public observation in Chinese courts.

## What Changed

[E1, verified official reporting] China Court Trial Online began trial operation on
July 1, 2016, formally opened on September 27 and subsequently connected the national
court system. [E4, reported implementation] The paper describes local resources,
superior-court quotas and subordinate-court case selection as drivers of uneven
broadcasting. The policy object here is this platform-era publicity exposure.
China Judgments Online supplies the outcome documents and has a different institutional
history; its 2013 launch is not the treatment studied in this record.

## Implementation and Assignment

[E4, inspected design] The main exposure is a fraction for each court, legal dispute
category and quarter. The word area denotes a category such as contract or tort,
not a district. Every case in a cell receives that aggregate exposure for the main
specification, including cases not broadcast themselves. This allows publicity to
affect a judge's wider behavior while retaining an explicit case-selection problem.
Court connection, realized intensity and individual broadcast status cannot replace
one another. The event-study start dates must be recovered from their own input.

## Why This Creates Empirical Variation

[E4, inspected equations] The study estimates whether the female-male outcome gap
changes as publicity increases, conditional on court-category, quarter and judge
fixed effects. Its instrument predicts a court's exposure using its 2014 case mix
and other courts' contemporaneous category-specific broadcasts within the prefecture.
Both intensity and its female interaction are instrumented. [Analytical inference]
The relevant question is whether this exposure predicts a changing gender gap through
publicity rather than omitted local change; neither national sponsorship nor an
earlier share measurement answers that question by itself.

## Identification Risks

[E4, reported tests] Observed attributes predict which cases are broadcast. The
authors therefore avoid treating broadcast cases as a randomly selected arm and
report aggregate-exposure, event-study, fixed-effect and IV checks. [Analytical
inference] Aggregation still leaves endogenous court implementation, case-mix
changes and differential publication as possible threats. Similarly, leaving the
focal court out of a prefecture shift removes mechanical own-observation linkage
but does not remove a common oversight shock or publicity spillover. A strong first
stage and similar DID/IV estimates are informative diagnostics, not proof of exclusion.

## Data Requirements

[E4-E5] A city-year policy dummy is insufficient. Research needs the case corpus,
matched broadcasts, legal category, quarter, gender, cost outcome and judge/court
identifiers. Preserve the distinction between the full document corpus, gender-
observed sample and actual regression sample. The outcome called chances of winning
is constructed from cost allocation, so its substantive interpretation must remain
visible. The README identifies the sample-construction script and the separate
begin/share inputs needed for event-study and IV work; it does not establish that
today's websites can reproduce the historical corpus. Dataset access and rebuilding
belong in the companion data knowledge base, linked by the paper DOI.

## Evidence Notes

[E1-E4] The published version and the author-hosted manuscript agree on the inspected
core design and paper counts. They differ from official connection totals, whose
roster and date definitions remain unresolved. Preserve both dated statements;
the primary intensity record does not depend on interpreting either total as a
court-level treatment list. [E5, reported guide] The replication README was read,
but the 432 MB archive's scripts and datasets were not inspected or executed. This
grounded record is consequently a conditional research candidate, with explicit
preparation steps for a new application rather than an unconditional causal claim.
