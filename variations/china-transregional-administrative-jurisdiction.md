---
schema_version: 2
id: china-transregional-administrative-jurisdiction
name: China's Trans-Regional Jurisdiction Reform for Administrative Litigation
aliases:
- Trans-Regional Jurisdiction reform
- 行政诉讼跨行政区划管辖改革
- 行政案件相对集中管辖
status: grounded
provenance:
  task_id: task-d716fe371f51
scope:
  country: China
  regions: [Mainland China, county and prefectural court jurisdictions]
  domains: [regional-economics, development-economics, firms, local-government, judicial-institutions]
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: The reform changed which county court hears qualifying administrative suits against local governments in mainland China, creating local exposure variation relevant to legal protection, local governance, and firm entry.
identity:
  instrument: Staggered local implementation of trans-regional jurisdiction for first-instance administrative litigation, moving covered cases away from the defendant government's home county court.
  authority: The 2014 amendment authorizes provincial high courts, with Supreme People's Court approval, to designate courts for cross-administrative-region jurisdiction; Supreme People's Court, provincial high courts, and prefectural courts organize and implement local schemes.
  legal_identifiers:
  - Administrative Litigation Law of the PRC (2014 revision), Article 18
  - Supreme People's Court, Notice on Conducting Pilot Work on Relatively Centralized Jurisdiction of Administrative Cases (2013)
  implementation_regime: >
    Article 18 supplies statutory authority, but it does not by itself move every
    case or create one national treatment date. Local plans specify which county
    court hears cases against each defendant jurisdiction. The 2013 relatively
    centralized-jurisdiction pilots predate the revised law's May 2015 effective
    date and form part of the institutional path described by the source study.
  assignment_mechanism: >
    Provincial high courts select prefectural pilots; prefectural courts prepare
    and submit a scheme for provincial ratification, then issue detailed county
    court instructions. Under the source paper's main assignment, a defendant
    county becomes treated when its government, departments, or subordinate
    townships are assigned to a different county court within the same prefecture.
    The defendant-to-court map is prescribed in advance and, according to the
    paper, generally does not vary with case-level characteristics. Pilot and
    implementation locations are selected, not randomized.
  parent: null
  related_variations:
  - china-2014-provincial-court-management-centralization
timeline:
  announcement: '2013-01-04'
  effective: '2015-05-01'
  implementation_start: '2013'
  implementation_end: null
  local_timing: >
    The dates refer to different layers: the Supreme People's Court issued its
    relatively centralized-jurisdiction pilot notice on 2013-01-04; the revised
    law took effect on 2015-05-01; and Cao, Liu, and Zhou report that pioneer
    counties began the paper-defined TRJ implementation in late 2013, with rapid
    expansion in 2015–2016 and more than 40% of sampled counties treated by 2018.
    They reconstruct county-specific dates and defendant-to-court maps from a
    2018 Supreme People's Court administrative-division book, local court notices,
    and local newspaper reports. These are paper-reported coding inputs, not a
    complete locally reverified national ledger.
  anticipation: >
    Local plans and court assignments could be public before the first coded
    treatment year. The 2013 pilots precede the 2014 legislative amendment, while
    the revised statute took effect in 2015; do not collapse these dates into a
    single national post indicator or assume every locality switched on the same
    legal date.
  last_verified: '2026-10-02'
assignment:
  unit: >
    Defendant county (including its subordinate townships and departments) by
    year for the principal treatment map; individual first-instance administrative
    case for the judgment-outcome application. Firm-entry analyses aggregate
    county adoption to the prefecture-year level.
  treated: >
    A defendant jurisdiction is treated from the locally coded year when its
    administrative cases are heard by a basic court in a different county of the
    same prefecture. The treatment is the jurisdictional separation between the
    defendant and adjudicating court, not merely designation of a centralized
    court or the 2014 statute's passage.
  comparison_pool: >
    The paper compares treated counties with not-yet- or untreated counties under
    county and year fixed effects. Its pseudo-reform group consists of counties
    hosting a centralized court whose own government's cases remain in that home
    court; these counties face other parts of the amendment without the focal
    defendant-court separation. Do not treat every county in a pilot prefecture as
    either exposed or cleanly untreated without recovering the local map.
  rule: >
    Join the named defendant government to the county-level jurisdiction plan and
    the adjudicating court. Code the exposure from the map in force for that
    defendant and year; under the paper's definition it switches on only when the
    court is in another county of the same prefecture. Keep genuine cross-county
    treatment distinct from a centralized court hearing cases against its own
    county government (the paper's pseudo-reform placebo).
  intensity: The main case-level treatment is binary. Secondary exposure can count or share the defendant's cases assigned outside its home county, but the source paper's county treatment is based on the prescribed jurisdiction map rather than realized case volume.
  exemptions:
  - Cases against governments above the county level are outside the paper's county-court sample.
  - >
    The source paper drops Shandong and Gansu and five prefectures with special
    schemes: Longyan, Guiyang, Ningbo, Taizhou, and Lishui.
  - In some local schemes plaintiffs could choose between local and trans-regional courts; the paper excludes ambiguous schemes rather than assigning them an assumed treatment.
  - Provincial management of local court personnel and finance, circuit courts, intellectual-property courts, and other specialized courts are different reforms.
  compliance: >
    The source paper codes the formally prescribed assignment map, not each
    plaintiff's awareness, filing choice, or the court's full substantive
    independence. Local maps could be adjusted for practical court-system
    reasons; the paper reports that such changes were one-time and unrelated to
    case characteristics, and tests exclusion of affected counties.
  exposure_construction: >
    Recover the 2018 SPC book's county dates and defendant-to-court correspondences,
    then cross-check with provincial/prefectural court plans and local notices.
    Preserve the defendant jurisdiction, adjudicating court, prefecture, plan
    version, announcement/effective dates, case date, and historical county code.
    The paper reports supplementing the book with court documents and local press;
    the full crosswalk was not independently reconstructed for this record.
  required_identifiers:
  - Defendant government name and administrative level
  - Plaintiff and defendant identifiers
  - Adjudicating court name, level, and county
  - Case filing, judgment, and publication dates
  - County-by-year jurisdiction map and plan effective date
  - Stable historical county and prefecture codes
  - For firm entry, firm registration date and county/prefecture location
  spillovers: >
    Transferred cases change caseloads in both the originating and centralized
    courts. Court workload, litigation, firm entry, local-government behavior, and
    investment may spill across counties within a prefecture; prefecture-level
    aggregation is therefore a distinct exposure rather than a way to make county
    spillovers disappear.
research_compatibility:
  outcome_domains:
  - Administrative case outcomes and filing
  - Firm entry and local investment
  - Local governance and legal protection
  affected_populations:
  - Firms and individuals suing county-level governments
  - County governments and basic people's courts
  - Firms located in treated prefectures
  mechanism_channels:
  - Reduced direct local-government influence over the adjudicating court
  - Changed access to administrative justice
  - Litigation demand and judicial workload
  - Firm entry and local business response
  best_for:
  - Linking administrative-case outcomes to a recovered defendant-to-court map.
  - Studying local economic responses with a separately documented county-to-prefecture exposure aggregation.
  - Comparing actual cross-county assignment with centralized-court counties that did not move their own cases.
  not_good_for:
  - A uniform post-2014 national treatment indicator.
  - Treating statutory authorization as proof every county implemented the same scheme.
  - Calling the reform full judicial independence or assuming rollout was random.
  - Reproducing the published estimate without the local jurisdiction crosswalk and case/firm data.
design:
  claim_type: causal
  affordances:
  - County-specific staggered implementation dates and prescribed court maps reported by the source paper
  - A meaningful distinction between actual defendant-court separation and pseudo-reform counties
  - Case-level legal outcomes and a separate prefecture-level firm-entry application
  candidate_designs:
  - Cohort-aware staggered difference-in-differences
  - Event study with county-specific adoption dates
  - Placebo comparison between genuinely reassigned defendants and centralized-court hosts' own cases
  identifying_variation: >
    The focal contrast is whether cases against the same type of local defendant
    move from its home-county court to a different county court within the
    prefecture, with local jurisdictions adopting the assignment at different
    times. A county's general participation in the 2014 amendment is not enough:
    the specific defendant-to-court map determines exposure.
  primary_strategy: >
    Cao, Liu, and Zhou (2023) use staggered county-level implementation in a
    difference-in-differences design for first-instance judgment documents, with
    county and year fixed effects and case-level controls. They separately use
    a pseudo-reform indicator to distinguish cross-county reassignment from other
    amendment components. Treat the paper's reported TWFE results as an
    application, not a guarantee that the same estimator is appropriate for a
    new cohort profile.
  estimand: >
    In the judgment sample, the conditional change in the probability that the
    local government loses an administrative case when the defendant's case is
    assigned outside its home county, relative to the paper's comparison counties.
    For firm entry, the estimand is a separate prefecture-level response to the
    first subordinate county adoption and should not be read as the same case-level
    effect.
  treatment_variable: >
    Case-level `PostReform`: 1 when the defendant county's cases are assigned to
    a court in another county of the same prefecture in year t. The source's
    firm-entry application separately marks a prefecture once at least one
    subordinate county has adopted.
  comparison_logic: >
    Preserve not-yet-treated and untreated counties, county and year effects, and
    the source's pseudo-reform group. Exclude or separately model the paper's
    special-scheme locations. Before reuse, inspect whether counties in the same
    prefecture or the same centralized court create spillovers into the nominal
    control group.
  estimation_notes: >
    The paper reports 62,392 first-instance administrative judgment documents
    against local governments from 2,000 counties over 2013–2018. Cases against
    county governments, departments, or subordinate townships are mapped to the
    defendant county. The separate firm-entry outcome uses prefecture-year
    aggregation and registration records; it is not the case-level regression
    sample. The paper reports robustness exercises for TWFE concerns and local
    map changes, but has limited pre-reform coverage and selective document
    disclosure.
  assumptions:
  - Conditional on the specified controls and fixed effects, treated and comparison jurisdictions would have had comparable outcome trends absent reassignment.
  - The county-specific adoption dates and defendant-to-court maps correspond to the operative local schemes.
  - Selection of pilot jurisdictions, centralized courts, and local adoption timing does not leave outcome-specific confounding after conditioning.
  - Court-document disclosure and the composition of filed cases do not change differentially in ways that drive measured outcomes.
  - Within-prefecture litigation, firm-entry, and workload spillovers do not invalidate the chosen comparison or are handled explicitly.
  diagnostics:
  - Plot cohort-specific pre-treatment trends and avoid relying on a single early pre-period.
  - Compare the genuine treatment coefficient with the pseudo-reform placebo.
  - Use estimators robust to heterogeneous staggered effects as a complement to TWFE.
  - Re-estimate after excluding special-scheme locations and counties whose court map changed for unrelated operational reasons.
  - Audit publication/disclosure rates and alternative case-sample definitions.
  - Test within-prefecture and centralized-court workload spillovers.
threats:
- type: selected-pilot-and-rollout
  basis: documented
  condition: >
    The 2013 SPC notice directs courts to choose pilot prefectures and centralized
    courts based on local judicial environment, case volume, adjudication capacity,
    and economic development. Adoption and the choice of receiving courts are not
    random, so time-varying governance or economic trends may affect both rollout
    and outcomes.
  evidence_refs: [E2, E3]
  possible_diagnostics: [Cohort-specific pre-trends, Predetermined balance, Adoption timing sensitivity, Pseudo-reform comparison]
- type: amendment-bundle-and-placebo-boundary
  basis: reported
  condition: >
    The 2014 statute changed multiple parts of administrative litigation, not just
    jurisdiction. A general post-amendment coefficient could capture other legal
    changes; the paper's pseudo-reform group helps isolate cases without an actual
    defendant-court separation but does not establish that all concurrent changes
    are harmless.
  evidence_refs: [E1, E3]
  possible_diagnostics: [Keep statute and local map dates separate, Reproduce pseudo-reform test, Exclude or stratify ambiguous schemes]
- type: selective-judgment-disclosure
  basis: reported
  condition: >
    China Judgments Online records do not represent every judgment issued. The
    paper assesses disclosure patterns, but selective publication may still alter
    the observed case mix or measured government-loss rate.
  evidence_refs: [E3]
  possible_diagnostics: [Court-year disclosure-rate analysis, High-disclosure subsample, Alternative case outcomes and sample definitions]
- type: short-pre-period-and-staggered-effects
  basis: reported
  condition: >
    The rollout begins early in the 2013–2018 judgment window, leaving little clean
    pre-treatment history for some cohorts. TWFE can also be sensitive to
    heterogeneous cohort effects; the paper reports alternative estimators but
    this does not remove the need for application-specific cohort checks.
  evidence_refs: [E3]
  possible_diagnostics: [Show event-study support by cohort, Test alternative effective-year coding, Use heterogeneous-treatment estimators]
empirical_requirements:
  contract_version: 1
  population: First-instance administrative suits against county and subordinate local governments; separate applications may use firms registered in the affected prefectures.
  observation_unit: Administrative case for the main application; prefecture-year for the reported firm-entry application.
  geography_level: Defendant county, adjudicating county court, and prefecture, with historical administrative crosswalks.
  time_start: 2013
  time_end: 2018
  minimum_frequency: Annual, with case-level dates retained
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - Defendant identity and government level
  - Plaintiff identity and type
  - Adjudicating court and court county
  - Filing, judgment, and publication dates
  - Judgment outcome, claims, and legal-fee responsibility
  - County-year prescribed jurisdiction map and local plan date
  - Firm registrations and county/prefecture for firm-entry extensions
  required_identifiers:
  - Case ID or a defensible document-level key
  - Stable defendant county and prefecture code
  - Stable adjudicating-court identifier and county code
  - Firm identifier and registration geography for firm-entry work
  treatment_key: [Defendant county code, Case year, Jurisdiction-map version]
  treatment_source: 2018 SPC administrative-jurisdiction reform book and local court plans/notices, as digitized and supplemented in Cao, Liu, and Zhou (2023); source paper data are stated to be available on request.
  measurement_risks:
  - Exact county-by-year treatment crosswalk was not independently reconstructed here.
  - Public judgment documents are selectively disclosed and differ from the universe of court decisions.
  - County and court names/codes can change; defendant geography must not be inferred only from the court that heard the case.
  - Firm-registration access, identifiers, and the source paper's prefecture aggregation must be verified separately.
design_profiles:
- id: administrative-judgment
  label: Defendant-court separation and administrative case outcomes
  design_families: [Staggered difference-in-differences, Event study, Pseudo-reform comparison]
  when_to_use: Use when the application can recover the defendant county's prescribed court map and link it to first-instance case outcomes without treating all 2014 legal changes as the exposure.
  outcome_domains: [Government loss, Case filing, Appeals, Trial time]
  requirements:
    population: Plaintiffs suing county governments, departments, and subordinate townships
    observation_unit: First-instance administrative judgment case
    geography_level: Defendant county and adjudicating county court within prefecture
    time_start: 2013
    time_end: 2018
    minimum_frequency: Case-level dates and annual treatment map
    minimum_pre_periods: 1
    minimum_post_periods: 1
    required_fields: [Defendant county, Adjudicating court, Case and judgment dates, Plaintiff/defendant types, Outcome, Jurisdiction plan, Map effective date]
    required_identifiers: [Case/document ID, Defendant county code, Court ID and county code, Year]
    treatment_key: [Defendant county code, Year, Jurisdiction-map version]
- id: prefecture-firm-entry
  label: Local firm-entry response to county adoption
  design_families: [Staggered difference-in-differences, Event study]
  when_to_use: Use only after defining and defending the source paper's prefecture aggregation, which turns on when at least one subordinate county adopts; this is a separate economic outcome design from case-level court outcomes.
  outcome_domains: [New firm registrations, Local business entry]
  requirements:
    population: Firms registered in mainland Chinese prefectures covered by the local jurisdiction rollout
    observation_unit: Prefecture-year
    geography_level: Prefecture-level city and subordinate counties
    time_start: 2010
    time_end: 2018
    minimum_frequency: Annual
    minimum_pre_periods: 1
    minimum_post_periods: 1
    required_fields: [Firm registration date, Firm identifier, County and prefecture location, County reform adoption year]
    required_identifiers: [Firm ID, County code, Prefecture code, Year]
    treatment_key: [Prefecture code, First subordinate county adoption year]
evidence:
- id: E1
  source_type: policy-document
  citation: People's Republic of China. Administrative Litigation Law, 2014 revision, Article 18; official text reproduced by the National Audit Office.
  url: https://www.audit.gov.cn/n7/n34/n58/c109687/content.html
  date: 2014
  supports: [identity.legal_identifiers, timeline.effective, assignment.rule]
  verification_status: verified
  access_level: official-document
  locator: Page identifies the 2014 NPC Standing Committee revision in its heading, lines under Chapter III, Article 18; the same page states that the revision was effective 2015-05-01 through the linked implementation notice context.
- id: E2
  source_type: implementation-document
  citation: Supreme People's Court. 2013. Notice on Conducting Pilot Work on Relatively Centralized Jurisdiction of Administrative Cases.
  url: https://www.court.gov.cn/zixun/xiangqing/5012.html
  date: '2013-01-04'
  supports: [identity.authority, identity.implementation_regime, identity.assignment_mechanism, timeline.announcement]
  verification_status: verified
  access_level: official-document
  locator: >
    Sections II and V: provincial high courts choose 1–2 intermediate-court pilot
    jurisdictions; pilot intermediate courts choose 2–3 basic courts and publish
    implementation plans. Section II lists the selection considerations—judicial
    environment, administrative caseload, court capacity, and economic/social
    development. Section IV describes transfer to a designated centralized court.
- id: E3
  source_type: paper
  citation: >
    Cao, Guangyu, Chenran Liu, and Li-An Zhou. 2023. “Suing the Government
    Under Weak Rule of Law: Evidence from Administrative Litigation Reform in
    China.” Journal of Public Economics 222, 104895.
  url: https://doi.org/10.1016/j.jpubeco.2023.104895
  date: '2023-04-27'
  supports: [identity.instrument, identity.implementation_regime, identity.assignment_mechanism, timeline.implementation_start, timeline.local_timing, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.intensity, assignment.exemptions, assignment.compliance, assignment.exposure_construction, assignment.required_identifiers, assignment.spillovers, design.claim_type, design.affordances, design.candidate_designs, design.identifying_variation, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, design.assumptions, design.diagnostics, empirical_requirements.population, empirical_requirements.observation_unit, empirical_requirements.geography_level, empirical_requirements.time_start, empirical_requirements.time_end, empirical_requirements.minimum_frequency, empirical_requirements.required_fields, empirical_requirements.required_identifiers, empirical_requirements.treatment_key, empirical_requirements.treatment_source, empirical_requirements.measurement_risks, design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year, design_applications.research_question, design_applications.population, design_applications.outcome, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design, design_applications.assumptions, design_applications.threats_addressed]
  verification_status: reported
  access_level: full-text
  locator: >
    Author-hosted journal-version PDF, 19 pages inspected; printed pp. 3–5 for
    Article 18, implementation steps, mapping, data and timing; pp. 6–9 for DID,
    comparison and sample; pp. 11–12 for pseudo-reform and selective disclosure;
    pp. 15–16 for firm-entry application; p. 17 for on-request data availability.
    The paper reports its county-specific map as digitized from the 2018 SPC
    reform book and local sources; the underlying full crosswalk was not
    separately inspected.
design_applications:
- paper: >
    Suing the Government Under Weak Rule of Law: Evidence from Administrative
    Litigation Reform in China
  doi: 10.1016/j.jpubeco.2023.104895
  journal: Journal of Public Economics
  year: 2023
  research_question: Does moving administrative cases outside the defendant government's home county court change judicial outcomes and private-sector responses?
  population: First-instance administrative cases against county governments, their departments, and subordinate townships; firms in the broader entry analysis.
  outcome: Government probability of losing a case, case volume, trial duration, and new firm registrations in a separate prefecture-level analysis.
  data_used: [China Judgments Online documents available through September 2018, 2018 SPC reform book and local court notices/newspaper reports for treatment maps, State Administration for Industry and Commerce firm-registration data]
  treatment_encoding: Defendant county-year indicator for cases assigned to another county court in the same prefecture; firm-entry design aggregates adoption to prefecture-year once at least one subordinate county adopts.
  comparison: Not-yet- or untreated counties; centralized-court counties whose own government cases remain local form the paper's pseudo-reform group. Special-scheme regions are excluded.
  empirical_design: Staggered DID with county and year fixed effects for case-level outcomes; separate prefecture-year firm-entry analysis. The paper also reports event-study, placebo, alternative-estimator, and selective-disclosure checks.
  assumptions: [Conditional parallel trends, Correct local dates and defendant-to-court maps, No fatal selection into rollout or court assignment, Case-document disclosure does not differentially determine the observed outcome]
  threats_addressed: [Pseudo-reform placebo, Exclusion of special-scheme and map-change counties, Event studies and alternative estimators, Court-year disclosure-rate analysis]
  evidence_refs: [E1, E2, E3]
method_transfer: null
readiness_blockers:
- The paper reports a county-by-year treatment map digitized from a 2018 SPC book and local sources, but the complete crosswalk was not independently recovered here; obtain and audit it before replication or building a new treatment file.
- The paper states that data are available on request. Access to judgment-document collections, firm-registration records, and any author-supplied analytic files is not guaranteed by this record.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Administrative litigation lets people and firms challenge local administrative
acts, but the ordinary venue rule placed the case in the court where the acting
government was located. The Supreme People's Court's 2013 pilot notice responded
to concerns about local influence by allowing selected jurisdictions to
concentrate cases in other basic courts [E2]. The 2014 revision then added an
Article 18 route under which, with Supreme People's Court approval, a provincial
high court can designate courts to hear administrative cases across
administrative boundaries [E1].

This legal authority and the local operating arrangements are related but not
the same event. The pilot process began before the revised law took effect, and
each local plan specified which court heard claims against which government.
That is why the research variation is the county-specific court assignment, not
a nationwide post-2014 legal indicator [E2, E3 reported].

## What Changed

In a covered county, an administrative case against its government, a
department, or a subordinate township can be heard by a different county court
in the same prefecture. The receiving court is outside the defendant county's
direct administrative jurisdiction, although it still sits within the same
prefectural hierarchy. The reform changes the venue and potential local leverage
over adjudication; it does not establish that the judiciary became independent
of higher-level political authority [E3 reported].

## Implementation and Assignment

Provincial high courts selected pilot prefectures; local intermediate courts
prepared a scheme, obtained provincial ratification, and issued a detailed
county-court plan [E2]. Cao, Liu, and Zhou report digitizing county-specific
implementation dates and defendant-to-court correspondences from the 2018 SPC
reform book, supplemented and cross-checked with local court documents and local
newspapers. Under their treatment definition, a defendant county switches on
only when its cases are assigned to a court in another county of the same
prefecture. Pioneers appear in late 2013; implementation accelerated in
2015–2016, and more than 40% of their sampled counties were treated by 2018
[E3 reported].

Local maps varied. A county court could receive cases from several governments,
while its own government's cases might be sent elsewhere; therefore the host
court and the defendant jurisdiction cannot be represented by one shared
treated-city label. The paper calls a host county's own cases “pseudo-reform”
when its court receives other cases but continues hearing cases against its own
government. That contrast helps separate cross-county venue change from other
provisions of the 2014 amendment [E3 reported]. Some provinces used different
or ambiguous arrangements and were excluded from the study sample.

## Why This Creates Empirical Variation

Counties entered at different times, and the local venue map determines whether
a claim against a particular government is genuinely moved away from its home
court. The paper uses that staggered map in a difference-in-differences design
for first-instance judgments. It reports a 62,392-case sample from 2,000
counties over 2013–2018, with county and year fixed effects and case-level
controls [E3 reported]. A separate application aggregates adoption to the
prefecture-year level—turning on once at least one subordinate county adopts—
and studies new firm registration. That economic outcome uses a different unit
and treatment aggregation and should not be mistaken for the case-level
assignment [E3 reported].

## Identification Risks

Pilot choice is selective. The 2013 notice directs courts to consider the
judicial environment, administrative caseload, court capacity, and
economic/social development when choosing pilot courts [E2]. In addition,
other provisions of the 2014 law changed at the same time. The source paper's
pseudo-reform comparison is useful, but does not turn local adoption into a
random assignment [E3 reported].

Treatment also moves workload across courts, which can affect processing times
and the behavior of both treated and comparison jurisdictions. The paper
reports that China Judgments Online did not contain the universe of decisions
and examines disclosure patterns; selective publication and changes in who
files remain central concerns [E3 reported]. Because implementation begins
within a short 2013–2018 window, some cohorts have little clean pre-period.
Event studies and alternative staggered-adoption estimators are diagnostics,
not proof that the identifying assumptions hold.

## Data Requirements

For a court-outcome study, join a defendant's stable county identity and case
date to the local defendant-to-court map, then to the adjudicating court and
judgment outcome. Do not derive the treatment from the receiving court alone.
For a firm-entry study, preserve the separate prefecture-year aggregation and
join registrations to historical county and prefecture geography. The article
states that its data are available on request; neither that statement nor the
public availability of some court judgments guarantees a complete, reusable
case collection, firm database, or treatment crosswalk [E3 reported].

## Evidence Notes

The revised statute and SPC pilot notice establish the formal authority and the
pilot-selection process [E1, E2]. The full-text 2023 paper reports the actual
local mapping, treatment dates, empirical coding, data and limitations [E3].
The local map remains a paper-reported source object rather than a national
crosswalk independently audited in this task. Keep it explicit as a prerequisite
for replication; do not silently replace missing local assignments with the
statute's effective date.
