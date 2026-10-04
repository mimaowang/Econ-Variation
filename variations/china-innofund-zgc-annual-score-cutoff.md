---
schema_version: 2
id: china-innofund-zgc-annual-score-cutoff
name: Beijing Zhongguancun Innofund Annual Project-Score Cutoffs, 2005–2010
aliases:
- Wang Li Furman 2017 Innofund fuzzy RD
- Zhongguancun innovation grant score threshold
- 中关村创新基金年度评审分数线
status: design-documented
provenance:
  task_id: task-c8a0cfc5a2b6
scope:
  country: China
  regions: [Beijing Zhongguancun high-technology area; not all Chinese Innofund applicants]
  domains: [innovation-economics, firm-economics, industrial-policy, public-finance]
  variation_type: eligibility-threshold
  knowledge_role: china-variation
  china_relevance: >
    The observed score-based grant decisions concern young technology firms applying
    from Zhongguancun in mainland China. The research object is a Chinese public
    innovation-finance allocation, not a transferable foreign subsidy example.
identity:
  instrument: >
    The annually budget-determined Innofund funding cutoff in the national
    project evaluation score, as applied to Zhongguancun applicants during
    2005–2010. Crossing it sharply raises, but does not guarantee, grant receipt.
  authority: >
    Ministry of Science and Technology Innovation Fund Management Center
    administers project review; the Ministry of Finance funds and oversees the
    program. The 2005 project-management rules require local recommendation,
    expert review and ministry approval [E1, Articles 2, 10–12, 19–20].
  legal_identifiers:
  - 国科发计字〔2005〕60号, 科技型中小企业技术创新基金项目管理暂行办法
  - 国办发〔1999〕47号, original Innofund interim provisions referenced by the 2005 rules
  implementation_regime: >
    The national program began in 1999. Applications from Zhongguancun first
    passed regional screening and then national technical and financial expert
    evaluation. This record covers the paper's 2005–2010 applicant cohorts, not
    the national founding event or an all-China rollout [E1; E2, §§3–4].
  assignment_mechanism: >
    Each application receives a national composite project score; the program
    ranks projects and funds down the list until the year's budget is spent.
    The raw cutoff varies by year, so the paper subtracts that year's threshold
    from each observed score. Actual awards depart from score order because of
    financial disqualification, veto/discretion and documented off-rule awards;
    the threshold is an instrument for receipt, not a deterministic treatment
    rule [E2, §§3–4, 6].
  parent: null
  related_variations: []
timeline:
  announcement: '2005-03-02 project-management interim rules; annual award cutoff not preannounced'
  effective: null
  implementation_start: 2005
  implementation_end: 2010
  local_timing: >
    The application year is the assignment cohort. The authors center each
    project score on its own year's funding threshold; a common raw score
    across 2005–2010 is not a common exposure. Award share rose markedly in
    2008–2010, so the paper reports 2005–2007 and 2008–2010 separately
    [E2, §§4, 6 and Table 3B].
  anticipation: >
    Annual funding budgets determine the realized cutoff independently of
    expert scores, according to the authors, and evaluators do not know the
    cutoff in advance. That is a paper-reported institutional claim, not proof
    that applications or scores were unmanipulated [E2, §3 and Figure 4].
  last_verified: '2026-10-02'
assignment:
  unit: Innofund project application by Zhongguancun firm and year
  treated: Applicants actually awarded an Innofund grant in the paper's 2005–2010 Zhongguancun sample
  comparison_pool: >
    Rejected applicants from the same local applicant pool and application
    cohorts whose observed scores lie close to the corresponding annual cutoff.
    Never substitute all nonrecipient firms or distant low-score applicants.
  rule: >
    The 2005 application guide confirms scored expert review and merit-ranked
    proposal selection, but does not disclose the final annual national
    cutoff [E4]. In the paper, set the running variable to national total
    project score minus that year's
    observed funding threshold. AboveThreshold equals one for a centered score
    of zero or greater. Use AboveThreshold as an instrument for actual grant
    receipt in a fuzzy regression discontinuity, not as grant receipt itself
    [E2, §§4, 6.2–6.3].
  intensity: >
    Binary award and binary above-threshold assignment in the published
    application; award amounts and local matching differ and are not the RD
    running variable [E2, §3].
  exemptions:
  - A financial-expert score below 60/100 disqualifies a project even with a high total score, as reported by the authors.
  - Scores of 60–65 on the financial component require a temporary R&D-related difficulty determination.
  - The program can veto an otherwise favorable expert decision for false application information, IP disputes or serious environmental harm.
  compliance: >
    It is demonstrably fuzzy: the author manuscript reports seven funded
    applications below the cutoff and 51 rejected above it. Another 111 of
    1,086 applications have no official score although they were reviewed;
    missing scores are associated with award receipt. The exact counts are
    manuscript-reported for this sample, not a nationwide compliance rate
    [E2, §§4–6].
  exposure_construction: >
    Link project-level application year, national evaluation score, annual
    cutoff and grant decision. Center the score by the year-specific cutoff;
    estimate the local first stage and use cutoff crossing to instrument
    award receipt. Exclude missing-score applications from the RD sample while
    investigating whether their omission selects a nonrepresentative group
    [E2, §§4, 6 and Tables 7–8].
  required_identifiers: [application or project ID, firm ID, application year, national total score, year-specific funding threshold, grant decision]
  spillovers: >
    The paper does not identify whether funds displaced other firms' finance
    or generated knowledge spillovers. The local fuzzy RD compares award
    compliers at the cutoff; it is not an estimate of program-wide effects.
research_compatibility:
  outcome_domains: [firm survival, invention-patent applications, public and private equity funding]
  affected_populations: [young Zhongguancun technology-firm applicants near an annual funding cutoff]
  mechanism_channels: [public R&D financing, grant certification, local matching finance]
  best_for:
  - A local study of award receipt among near-cutoff Zhongguancun Innofund applicants with lawful access to internal scores and annual cutoffs.
  - Distinguishing grant selection from grant effects when both successful and rejected applications are observed.
  not_good_for:
  - Treating a published grant-recipient list or a fixed national score as sufficient to reconstruct the discontinuity.
  - Claiming the paper's local null results show grants have no effect for all Chinese firms or all Innofund awardees.
design:
  claim_type: causal
  affordances: [annual score cutoff, project-level grant decision, rejected-applicant pool, linked administrative outcomes]
  candidate_designs: [fuzzy regression discontinuity]
  identifying_variation: >
    Within each application year, a score barely above rather than below the
    budget-induced cutoff produces a discontinuous increase in grant receipt.
    The observed first stage is imperfect but substantial [E2, Figure 3 and
    Table 7].
  primary_strategy: >
    Local-linear fuzzy RD / 2SLS. The instrument is crossing the annual score
    cutoff, the endogenous treatment is grant receipt and the outcome is a
    later firm measure. The paper's preferred specification uses a triangular
    kernel and CCT bandwidth; it separates 2005–2007 from 2008–2010
    applicants [E2, §§6.2–6.3 and Table 8].
  estimand: >
    Local effect of receiving a grant for applicants whose award status is
    induced by the threshold, conditional on continuity, exclusion and
    monotonicity. It is not the average effect of the national program.
  treatment_variable: >
    Funded_it; AboveThreshold_it = 1[raw national score_it - annual cutoff_t
    >= 0] instruments for Funded_it. Missing-score applications cannot enter
    this construction [E2, §§4 and 6.3].
  comparison_logic: >
    Compare applicants just above and below the relevant year's cutoff,
    weighting observations by score distance rather than comparing all
    funded with all unfunded firms [E2, §§6.1–6.3].
  estimation_notes: >
    Among 1,086 applications in 2005–2010, the author manuscript reports 540
    funded and 546 unfunded, with 111 lacking official scores. Its Table 7
    reports award rates of 71% versus 6% just above/below within the IK
    window and 79% versus 3% within the CCT window. Table 8 reports no
    statistically persuasive local award effect on survival, invention
    patenting or new equity financing; broad OLS associations are not those
    causal estimates [E2].
  assumptions:
  - Potential outcomes and applicant characteristics evolve continuously through each year's score threshold, absent the award probability jump.
  - The cutoff changes outcomes through grant receipt, not a distinct score-triggered treatment; no defiers for the local instrumental-variable interpretation.
  - Administrative exceptions and nonrandom missing scores do not create a discontinuous unobserved-quality jump among observed near-cutoff applications.
  diagnostics: [funding-probability jump by centered score, near-cutoff balance by application cohort, McCrary score-density test, missing-score and off-rule-award audit, bandwidth and kernel sensitivity]
threats:
- type: discretionary-awards-and-missing-scores
  basis: documented
  condition: >
    Seven below-cutoff awards, 51 above-cutoff denials and 111 missing official
    scores appear in the author manuscript's Zhongguancun application data;
    missingness is positively associated with awards. A clean sharp rule or
    random score availability would misdescribe the data [E2, §§4–6].
  evidence_refs: [E2]
  possible_diagnostics: [reconcile grant decisions with expert records, compare observed and missing-score applicants, report first stage by cohort]
- type: score-and-covariate-sorting
  basis: reported
  condition: >
    The manuscript reports no statistically detected McCrary density jump,
    but notes a dip in score density at the cutoff and a profit imbalance in
    one near-cutoff window. These checks do not establish nonmanipulation
    [E2, §6.2, Table 7 and Figure 4].
  evidence_refs: [E2]
  possible_diagnostics: [repeat density and covariate checks with raw current administrative scores, inspect reviewer and official overrides]
- type: restricted-local-data-and-external-validity
  basis: documented
  condition: >
    The annual national score, exact year cutoffs and rejected applicants
    came from internal program files obtained by the authors for Zhongguancun
    only. Public awardee lists cannot recreate the RD; Beijing's high-tech
    cluster differs from other mainland regions [E2, §4].
  evidence_refs: [E2]
  possible_diagnostics: [secure authorized internal data access before design commitment, document ZGC coverage and test replication in any newly accessible region]
empirical_requirements:
  contract_version: 1
  population: Zhongguancun Innofund applicants, including awarded and rejected projects, in 2005–2010.
  observation_unit: project application with linked firm post-application outcomes
  geography_level: Zhongguancun area, Beijing
  time_start: 2005
  time_end: 2015
  minimum_frequency: annual application cohorts and annual cutoff; post-application outcomes observed by 2015
  minimum_pre_periods: 0
  minimum_post_periods: 1
  required_fields: [application year, raw national total score, year's score cutoff, grant decision and amount, technical and financial score or override, firm characteristics, post-application survival or patenting or equity financing]
  required_identifiers: [application ID, firm ID, application year, BAIC firm registration ID or patent applicant name]
  treatment_key: [application ID, application year, centered national project score]
  treatment_source: >
    Restricted internal Innofund application and evaluation files accessed by
    the study authors, with BAIC registration/ownership and SIPO patent links.
    The public 2005 MOST rules establish process and eligibility, not the
    paper's raw scores or realized annual cutoffs [E1; E2].
  measurement_risks: [nonrandom missing official scores, discretionary award decisions, changing annual thresholds, firm-name linkage errors, uneven post-application follow-up, self-reported application covariates]
evidence:
- id: E1
  source_type: policy-document
  citation: MOST and Ministry of Finance, 科技型中小企业技术创新基金项目管理暂行办法, 国科发计字〔2005〕60号, 2 March 2005.
  url: https://www.most.gov.cn/xxgk/xinxifenlei/fdzdgknr/fgzc/gfxwj/gfxwj2010before/201712/t20171226_137208.html
  date: '2005-03-02'
  supports: [identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.announcement, empirical_requirements.treatment_source]
  verification_status: verified
  access_level: official-document
  locator: >
    Articles 2, 4–7 and 10–12, 19–22: responsible ministries, applicant
    eligibility, support forms, local recommendation, expert review and final
    approval. Inspected 2026-10-02. The page is now marked invalid, but the
    dated 2005 text governs the historical sample; it does not publish annual
    score cutoffs or prove actual adherence to rank order.
- id: E2
  source_type: paper
  citation: >
    Wang, Yanbo, Jizhen Li and Jeffrey L. Furman. Firm Performance and State
    Innovation Funding: Evidence from China's Innofund Program. Author
    manuscript dated 21 November 2016, deposited in Boston University's
    institutional repository for the 2017 Research Policy article.
  url: https://open.bu.edu/items/546dbdb4-12d7-41bf-a6e1-783ffcda41c2
  date: '2016-11-21'
  supports: [identity.assignment_mechanism, timeline.local_timing, timeline.anticipation, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.compliance, assignment.exposure_construction, design.identifying_variation, design.primary_strategy, design.estimation_notes, threats.condition, empirical_requirements.treatment_source, design_applications.empirical_design, design_applications.data_used]
  verification_status: verified
  access_level: full-text
  locator: >
    Full 2016 author manuscript downloaded from the BU repository and
    inspected 2026-10-02: §§3–4, pp. 10–17 for administration, 1,086 ZGC
    applications, scoring, annual threshold and joins; §§5–6, pp. 18–31,
    Tables 3B, 7–8 and Figures 3–4 for missing scores, deviations, first
    stage and fuzzy RD. This is an author manuscript, not independently
    verified final publisher pagination or a public copy of microdata.
- id: E3
  source_type: paper
  citation: >
    Wang, Yanbo, Jizhen Li and Jeffrey L. Furman. 2017. Firm Performance and
    State Innovation Funding: Evidence from China's Innofund Program.
    Research Policy 46(6):1142–1161. DOI 10.1016/j.respol.2017.05.001.
  url: https://doi.org/10.1016/j.respol.2017.05.001
  date: '2017'
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: abstract
  locator: >
    Journal metadata and published abstract inspected 2026-10-02. It confirms
    bibliographic identity and the use of fuzzy RD with nonrandom missing
    scores and off-rule awards; detailed design comes from E2, not this abstract.
- id: E4
  source_type: implementation-document
  citation: MOST Innovation Fund Management Center, 科技型中小企业技术创新基金申请须知（2005年度）, archived by Hunan Provincial Department of Science and Technology.
  url: https://kjt.hunan.gov.cn/xxgk/tzgg/tzgg_1/200902/t20090211_2229532.html
  date: '2005'
  supports: [assignment.rule, identity.implementation_regime, empirical_requirements.treatment_source]
  verification_status: verified
  access_level: official-document
  locator: >
    Chapter 3, application step 6, and Chapter 4, project-review steps 1–4:
    local expert scores enter total evaluation, proposals are ranked locally,
    and evaluated projects are selected by merit for ministry approval.
    Inspected 2026-10-02. This supports the scored-review component of
    assignment, not the paper's realized annual national cutoff or
    Zhongguancun exceptions, which come from E2.
design_applications:
- paper: "Firm Performance and State Innovation Funding: Evidence from China's Innofund Program"
  doi: 10.1016/j.respol.2017.05.001
  journal: Research Policy
  year: 2017
  research_question: Does receiving Innofund support improve young Zhongguancun firms' survival, invention patenting or subsequent equity funding?
  population: 1,086 2005–2010 Zhongguancun Innofund applications; scored near-cutoff subset for the fuzzy RD.
  outcome: Firm death by 2015, post-award invention-patent applications, new SOE/COE or VC/PE equity investment.
  data_used: [internal Innofund applications and expert scores, annual realized cutoff and grant decisions, Beijing Administration of Industry and Commerce registration/ownership, SIPO invention-patent applications]
  treatment_encoding: Actual grant receipt instrumented by centered total score at or above that year's funding threshold.
  comparison: Just-below-cutoff versus just-above-cutoff applicants with observed scores, within annual cohorts.
  empirical_design: Local-linear fuzzy RD estimated by 2SLS, with CCT bandwidth and triangular weighting in preferred specifications; separate early and later award regimes.
  assumptions: [score-continuity near the annual threshold, exclusion of other cutoff-triggered channels, interpretable local first stage and monotonicity, observed-score sample not spuriously selected at the cutoff]
  threats_addressed: [score missingness, above/below-cutoff award exceptions, covariate balance, density sorting, cohort budget changes]
  evidence_refs: [E1, E2, E3, E4]
method_transfer: null
readiness_blockers: []
---

## Institutional Background

The Innofund finances young Chinese technology firms through grants and other support. Under the 2005 rules, local authorities recommend applications, experts evaluate projects, and the science and finance ministries approve awards [E1, Articles 10–12, 19–20]. Wang, Li and Furman use internal files for Zhongguancun applicants in 2005–2010. That is a local application sample of a national program, not a nationwide firm panel [E2, §4].

## What Changed

The relevant variation is not the program's founding in 1999. It is the annual point where the budget stops financing ranked projects. The paper subtracts each year's funding cutoff from the national project score, so an applicant can be just above or below the same-year margin [E2, §§3–4]. The cutoff changes award probability, not eligibility with certainty. Financial-score disqualifications, administrative vetoes and off-rule decisions break any mechanical score-to-grant interpretation [E2, §§3, 6].

## Implementation and Assignment

The authors observe 1,086 Zhongguancun applications, including 540 awards and 546 rejections; 111 applications lack an official score [E2, §4]. Their manuscript reports seven below-cutoff grants and 51 above-cutoff denials. Missing scores are associated with award receipt, so treating missingness as random would conceal a feature of the allocation process [E2, §§5–6]. The public MOST rules verify expert review and ministerial approval, while the annual national score, cutoff and actual exception counts are documented by the paper's internal files, not the public notice [E1; E2].

## Why This Creates Empirical Variation

Within the scored applicant pool, crossing the year-specific cutoff raises the probability of winning a grant. The authors use that jump as an instrument for actual award receipt in a fuzzy RD; their comparison is local to the threshold and to applicants whose grants respond to it [E2, §6 and Table 8]. Broad recipient/nonrecipient differences are selection-laden and should not be reported as the design estimate. The paper's preferred local estimates do not find convincing grant effects on survival, invention patenting or equity financing, despite positive full-sample associations [E2, Tables 6–8]. A null local estimate is not a universal null for all Chinese innovation grants.

## Identification Risks

Discretion matters twice: some scored applications violate rank order, and scored applications may differ from those without official scores. The manuscript's density check does not detect a statistically significant jump, yet the authors note a visible dip at the threshold and one profit imbalance within the CCT window [E2, §6.2, Table 7 and Figure 4]. Those observations call for renewed checks if new administrative data become available; they do not justify discarding the fuzzy design or declaring it automatically causal. The funding expansion after 2007 also changes the applicant margin and motivates cohort-specific analyses [E2, Table 3B].

## Data Requirements and Evidence Boundary

Implementing this design requires both winning and rejected applications, raw national scores, each year's realized cutoff, actual award decisions and outcome joins to firm registration or patent records. A public list of awardees lacks the running variable and comparison pool. The paper obtained restricted internal data for Zhongguancun; it does not establish that a new researcher can access them [E2, §4]. E1 is the historical legal/process source, E2 is a fully inspected author manuscript for the empirical application, and E3 confirms the published article and abstract. The record is decision-sufficient for judging the design and its access barrier, not a claim that its confidential microdata are supplied here.

## Evidence Notes

The 2005 ministry rule establishes the historical administrative route, while the 2005 application guide confirms scored review and merit-ranked proposals; neither publishes the realized annual national cutoff or applicant-level decisions [E1; E4]. Those details, the departures from rank order and the paper's statistical tests come from the inspected 2016 author manuscript [E2]. The 2017 publication metadata and abstract confirm the final article's identity and its fuzzy-RD framing; its final typeset text was not inspected here [E3].
