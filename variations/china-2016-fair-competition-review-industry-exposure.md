---
schema_version: 2
id: china-2016-fair-competition-review-industry-exposure
name: China fair-competition review reform and administrative-monopoly industry exposure
aliases: [公平竞争审查制度行业差异暴露, administrative-monopoly regulation]
status: grounded
provenance:
  task_id: task-47ffa7746cd8
scope:
  country: China
  regions: [Mainland China]
  domains: [industrial-economics, firm-economics, development, innovation, market-integration]
  variation_type: other
  knowledge_role: china-variation
  china_relevance: A national Chinese policy-review reform is actually used for differential industry exposure in a published firm-innovation study. This is not collection of a financial shock.
identity:
  instrument: National fair-competition review reform introduced in2016, interacted with administrative-monopoly industry membership.
  authority: State Council; policy-making agencies conduct review under coordinated implementation.
  legal_identifiers: [国发〔2016〕34号]
  implementation_regime: Review of new policy measures and gradual cleanup of legacy measures; national industry-relative exposure, not a local pilot or individual enforcement action.
  assignment_mechanism: The study distinguishes18 administrative-monopoly industries from other industries around the national reform. The industry list is a research proxy, not statutory exclusive eligibility.
  parent: null
  related_variations: []
timeline:
  announcement: State Council document signed2016-06-01.
  effective: Central/provincial bodies begin review in July2016; local extension is gradual from2017.
  implementation_start: 2016
  implementation_end: null
  local_timing: National annual onset does not measure a municipality's effective implementation or the repeal date of an individual measure.
  anticipation: A half-year2016 transition and prior competition reforms require sensitivity analysis.
  last_verified: '2026-10-05'
assignment:
  unit: Industry-relative firm exposure to national policy-review reform.
  treated: Firms classified into the18 named monopoly industries; the verified code crosswalk is given below.
  comparison_pool: Other nonfinancial listed-firm industries are lower-relative-exposure comparisons, not legally exempt firms.
  rule: The published interaction is monopoly-industry membership times indicator(year>=2016). Its industry-observation vintage is not specified; conditional reuse must document a prepolicy membership or stable-industry convention rather than impute the author's choice.
  intensity: Binary industry-relative proxy; neither actual policy repeal nor a firm's received support.
  exemptions: [No inference of zero exposure for comparison industries, Public-interest exceptions remain in the institution, Legacy benefits may have transition periods]
  compliance: Policy review and actual removal of restrictions are distinct; compliance cannot be inferred from the national label.
  exposure_construction: Map CSRC2012 codes to the explicit list, preserve firm industry histories, and join firm_id/year to outcomes. For a new design, freeze membership before2016 or restrict to stable-industry firms and audit excluded switchers; these are proposed conventions, not verified author coding. Changes in firm group membership also require a patent aggregation convention.
  required_identifiers: [firm_id, year, industry_code, industry_classification_version]
  spillovers: Competition reform can affect comparison industries through suppliers, customers and entry.
research_compatibility:
  outcome_domains: [firm innovation, patent applications, industrial productivity, market competition]
  affected_populations: [mainland nonfinancial listed firms]
  mechanism_channels: [entry barriers, policy favoritism, factor allocation, competition]
  best_for: [industry-relative national reform exposure with auditable prepolicy industry membership]
  not_good_for: [a local staggered rollout without local evidence, actual repeal of a specific policy, unconditional untreated comparisons, exact author replication without industry vintage and patent crosswalk]
design:
  claim_type: reduced-form
  affordances: [national onset interacted with industry exposure]
  candidate_designs: [firm-panel differential-exposure DID, event study]
  identifying_variation: Differences across the named industries around2016, not a national before-after contrast alone.
  primary_strategy: Published firm/year fixed-effects DID with firm-clustered standard errors.
  estimand: Relative change in outcomes for higher-proxy-exposure industries; attribution to review reform requires excluding differential concurrent shocks.
  treatment_variable: monopoly_industry times post2016, with the membership convention explicit.
  comparison_logic: Compare changes rather than levels; justify counterfactual industry trends and account for nonzero reform exposure in the comparison pool.
  estimation_notes: The published innovation outcome aligns regressors in t to patents in t+1. Preserve that timing in a new dataset rather than joining same-year patents by convenience.
  assumptions: [counterfactual parallel industry trends, defensible predetermined membership, no unhandled differential concurrent reform, comparable patent measurement]
  diagnostics: [pretrend power and confidence intervals, omit transition2016, industry-switcher sensitivity, exclude overlapping capacity-reduction sectors, industry dependence, comparison spillovers]
threats:
  - type: industry-switching
    basis: documented
    condition: Official classifications permit periodic revision. Post-reform industry movement could make observed membership endogenous; the study does not disclose its vintage.
    evidence_refs: [E1, E3]
    possible_diagnostics: [prepolicy freezing, stable-industry subset, switcher trajectories]
  - type: concurrent-industry-shocks
    basis: inferred
    condition: Sector-specific capacity reduction and demand changes can coincide with2016; firm effects and common year effects do not absorb these.
    evidence_refs: [E1]
    possible_diagnostics: [sector exclusions, outcome-specific overlap audit]
  - type: dependence
    basis: inferred
    condition: Industry-common exposure can correlate firm errors beyond the reported firm clusters.
    evidence_refs: [E1]
    possible_diagnostics: [industry-aware inference, justified small-cluster sensitivity]
  - type: legal-proxy-gap
    basis: documented
    condition: The institution covers policy makers and includes phased legacy cleanup and exceptions; industry membership does not verify actual enforcement.
    evidence_refs: [E2]
    possible_diagnostics: [local implementation evidence, separate repeal-based designs rather than conflation]
empirical_requirements:
  contract_version: 1
  population: Mainland nonfinancial listed firms with auditable industry histories; a stable-industry restriction is a proposed reuse convention, not the reported author sample.
  observation_unit: firm-year
  geography_level: national with firm geography audited
  time_start: 2012
  time_end: 2021
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 2
  required_fields: [industry_code, industry_history, patent_applications, invention_applications, financial_controls, sample_exclusion_flags]
  required_identifiers: [firm_id, year, industry_classification_version]
  treatment_key: [industry_code, year]
  treatment_source: Published18-industry list mapped to official CSRC2012 codes; national onset from34号 document. Firm classification vintage must be supplied by the user dataset.
  measurement_risks: [industry revisions, parent versus subsidiary patent aggregation, patent year alignment, non-mainland operations, differential missingness]
evidence:
  - id: E1
    source_type: paper
    citation: '杨兴全、张可欣 (2023). 公平竞争审查制度能否促进企业创新？——基于规制行政垄断的视角. 财经研究49(1):63–78. DOI10.16538/j.cnki.jfe.20220915.101.'
    url: https://doi.org/10.16538/j.cnki.jfe.20220915.101
    date: 2023
    supports: [identity.assignment_mechanism, assignment.treated, assignment.rule, assignment.comparison_pool, design.primary_strategy, design.estimation_notes, design_applications.treatment_encoding, design_applications.data_used]
    verification_status: reported
    access_level: full-text
    locator: 'Actual publisher HTML https://qks.sufe.edu.cn/mv_html/j00001/202301/efdc8eab-6f04-4007-96a8-6ac03e4f5fb5_WEB.htm directly retrieved200: SectionsII–IV, Tables1–5, footnotes4–9. Final16-page PDF https://qks.sufe.edu.cn/J/PDFFullDown/efdc8eab-6f04-4007-96a8-6ac03e4f5fb5?lang=cn retrieved200 in memory; Table4 on printedp70/PDFp8 also text and visually inspected. This establishes the reported method, not an undisclosed classification vintage or subsidiary roster.'
  - id: E2
    source_type: policy-document
    citation: State Council fair-competition review opinion, 国发〔2016〕34号.
    url: https://www.ndrc.gov.cn/xwdt/ztzl/jdstjjqycb/zccs/201705/t20170517_1028533.html
    date: '2016-06-01'
    supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.announcement, timeline.effective, assignment.unit, assignment.compliance, assignment.exemptions]
    verification_status: verified
    access_level: official-document
    locator: SectionsIII(1)–(4), IV(1)–(2) and signature; NDRC republication dated2017-05-17 is not onset.
  - id: E3
    source_type: policy-document
    citation: CSRC公告〔2012〕31号, 上市公司行业分类指引（2012年修订）, official bulletin2012 issue10.
    url: https://www.csrc.gov.cn/csrc/c100024/c1492226/1492226/files/5f2288e304bf41bc9238c19bcfbdd0af.pdf
    date: '2012-10-26'
    supports: [assignment.exposure_construction, empirical_requirements.treatment_source, empirical_requirements.required_identifiers]
    verification_status: verified
    access_level: official-document
    locator: Actual189-page PDF retrieved200 in memory. Printedpp55–63, PDFpp66–74 visually inspected; Section2 revenue classification, Sections6.1–6.3 periodic revisions, Section7 industry table. Text extraction is garbled and was not relied on. No original PDF persisted.
design_applications:
  - paper: Fair-competition review and enterprise innovation
    journal: 财经研究 / Journal of Finance and Economics
    year: 2023
    research_question: Does innovation change differentially in administrative-monopoly industries?
    population: Nonfinancial A-share firms,2012–2020.
    doi: 10.16538/j.cnki.jfe.20220915.101
    outcome: log(1+next-year patent applications), including invention and non-invention outcomes.
    data_used: [CSMAR, Wind, CNRDS]
    treatment_encoding: Named18-industry membership times2016-or-later; industry vintage undisclosed.
    comparison: Other industry firms before and after reform.
    empirical_design: Firm/year DID, firm clustering; Table2 has23,506 observations.
    assumptions: [differential parallel trends, no differential concurrent industry shock]
    threats_addressed: [reported event leads, PSM, described transition-year and steel/coal exclusions]
    evidence_refs: [E1]
method_transfer: null
readiness_blockers:
  - Conditional industry-relative reuse requires prepolicy industry history and a stated membership convention. Do not offer exact author replication or unknown switcher assignment as closed.
  - Firm/group patent crosswalk and mainland operating exposure require dataset-specific audit; outcome2021 is needed for regressors2020 in the published t+1 specification.
  - Assess industry-common inference, nonzero comparison exposure and contemporaneous industry reforms for the chosen outcome; reported pretrend tests do not certify identification.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

The reform addresses restrictions introduced by public authorities through
policy measures. It is not a firm-level antitrust prosecution. Its review
and cleanup mechanisms differ from licenses, subsidies and local pilots
[E2]. A research idea about market integration can use this context, but
needs a comparison linked to the specific barrier of interest.

## What Changed

Policy makers review new measures and progressively clean up existing
ones. Central and provincial review starts in July2016; city/county extension
begins gradually from2017. Contractual transitions and specified exceptions
remain [E2]. Consequently national reform timing is not a local repeal date.

## Implementation and Assignment

The paper supplies the industry names [E1, reported claim]. Mapping those
names to the inspected official2012 table gives the following crosswalk
[E3; crosswalk is our explicit derivation, not an author code file]:

| Codes | Industry group |
|---|---|
| B06, B07, B08, B09, B11 | Coal; oil/gas; ferrous and nonferrous ores; mining support |
| C25, C31, C32, C37 | Petroleum processing; ferrous/nonferrous metallurgy; rail/ship/aerospace transport-equipment manufacture |
| D44, D45, D46 | Electricity/heat, gas and water supply |
| G53, G54, G55, G56 | Rail, road, water and air transport |
| I63, N78 | Telecommunications/broadcast/satellite transmission; public facilities management |

Industry histories matter: the official system revises firm classifications
periodically [E3]. Freezing prepolicy membership or excluding switchers is a
defensible *new-use* convention, not evidence of the author's implementation.
If the question cannot tolerate that distinction, this record is an audit
lead for exact replication rather than a ready-made treatment file.

## Why This Creates Empirical Variation

The useful comparison is relative exposure across industries, not simply
China before and after2016. A comparison firm remains subject to the review
system; the design requires unequal effects, not legal noncoverage
[analytical inference]. It cannot identify a general national effect shared
equally by all firms.

## Identification Risks

Industry-common demand and concurrent reforms can mimic the proposed
effect. Firm clustering alone need not handle that dependence. The paper's
Table4 separately estimates a common Post while labeling year effects as
included [E1, reported claim]; ask for clarification rather than importing
that exercise into a new design. This reporting ambiguity does not make
the baseline cross-industry interaction mechanically unidentified.

## Data Requirements

Retain the classification version, historical memberships and firm keys.
Choose a mainland exposure convention when firms operate across borders;
listing in China alone does not prove every patent arose from a mainland
operation. Patent-parent/subsidiary aggregation must match the outcome
population. Do not shift the outcome calendar to fit available files.

## Evidence Notes

This record serves the documented national industry-relative proxy, with
explicit conditions for new use. It does not establish local compliance,
individual policy repeal, or exact author-code replication. The official
classification table closes the name/code crosswalk, but cannot reveal
the author's choice of annual versus frozen firm membership. That limit
is retained rather than hidden by the grounded label.
