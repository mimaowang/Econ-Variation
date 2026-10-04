---
schema_version: 2
id: china-2001-income-tax-protected-base-incentive
name: China2001 Income-Tax Protected-Base Incentive
aliases: [2001所得税基数激励, 政企互惠与所得税基数, Quid pro quo government-firm relationships]
status: grounded
provenance:
  task_id: task-cca6bf208e13
scope:
  country: China
  regions: [Mainland China]
  domains: [public-finance, firms, regional-economics, development-economics]
  variation_type: event-shock
  knowledge_role: china-variation
  china_relevance: Chinese local governments and domestic firms faced a temporary incentive to raise the2001 local corporate-income-tax base before revenue sharing began.
identity:
  instrument: Late2001 incentive to increase the income-tax revenue base expected to be protected under the impending sharing reform
  authority: State Council and Ministry of Finance; provincial and subprovincial fiscal authorities
  legal_identifiers: [国发〔2001〕37号, 国办发〔2002〕1号, 沪府发〔2002〕36号]
  implementation_regime: The2001 base-setting response window, followed by investigation and base recalculation. Not the permanent2002 fiscal-loss exposure or the separate new-firm tax-bureau assignment.
  assignment_mechanism: Common reform news creates a base-raising incentive; heterogeneous county responses and prior firm relationships are observed, not randomly assigned treatment intensity
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 2001
  implementation_end: 2001
  local_timing: The urgent notice's attached December29 report identifies an October2001 central proposal and abnormal November/December receipts. December31 is the formal sharing decision; January1,2002 is sharing onset and the urgent notice date, not the beginning of the response window. Exact October day is not verified.
  anticipation: The paper describes late-October news as unexpected; the official report establishes October communication but does not establish that every county or firm was surprised.
  last_verified: '2026-10-04'
assignment:
  unit: County fiscal authority and firms attached through county location
  treated: Local governments exposed to prospective protection of the2001 local-income-tax base, with paper-defined domestic industrial firms as potential assisting actors
  comparison_pool: For the response measure, each county's fitted2001 counterfactual using1998–2003 excluding2001; for relationship regressions, counties with different1999–2000 firm-favor proxies within prefectures. These are not randomized treated and untreated counties.
  rule: The sharing scheme protects the2001 local base through settlement; higher eligible receipts can initially appear to increase protected resources. The urgent notice requires removal of artificial receipts and threatens base deductions. This defines the short-lived incentive, not a guarantee that a county's raised base was ultimately retained.
  intensity: In the inspected author version, assistance A equals (observed2001 corporate income tax minus relabeled other taxes) divided by predicted counterfactual2001 corporate income tax; A=1 is the no-extra-assistance benchmark.
  exemptions: [Statutory central-income sectors outside the original sharing pool, Central-state and foreign-controlled firms outside the main domestic ownership comparisons, Later provincial/county base-return rules are not uniform nationwide exposure]
  compliance: Neither actual firm transfers nor county-by-county receipt of the resulting protected base is observed in the application. Authorities prohibited advancing2002 taxes and using fiscal injections or bank loans to inflate receipts. A residual revenue proxy cannot establish compliance with those prohibitions.
  exposure_construction: Fit a county-specific quadratic trend with county effects and log GDP per capita on1998–2003 excluding2001 to predict2001 corporate income tax. Estimate relabeling from negative deviations of other local taxes/fees, subtract it from observed2001 income-tax revenue, then divide by the prediction. Link1999–2000 industrial-firm aggregates by county; retain the level-one benchmark rather than subtracting the prediction a second time.
  required_identifiers: [Historical county code or audited name crosswalk, Prefecture, Province, Year, Longitudinal firm identifier for the micro application]
  spillovers: Fiscal and firm resources can be shifted across budget categories, affiliated firms and jurisdictions; the response can also affect subsequent subsidies and local public spending.
research_compatibility:
  outcome_domains: [Local fiscal response, Government-firm reciprocity, Firm subsidies, Local government incentives]
  affected_populations: [County governments, Local-state-related industrial firms, Private domestic industrial firms]
  mechanism_channels: [Protected-base incentives, Tax relabeling, Informal firm assistance, Government return favors]
  best_for: [Conditional investigation of short-lived fiscal incentives and pre-existing government-firm relationships]
  not_good_for: [Randomly assigned credit or tax favors, A standard nationwide treated-versus-untreated DID, Observed informal transfers, Permanent unadjusted2001-base benefits, An unchanged statutory firm-tax-rate shock]
design:
  claim_type: descriptive
  affordances: [Short response window, County-specific revenue counterfactuals, Pre-event ownership-specific relationship proxies, Firm subsidy triangulation]
  candidate_designs: [Conditional county cross-section, Firm-level abnormal-subsidy association]
  identifying_variation: The paper uses the common base-setting event to reveal heterogeneous responses associated with prior firm-favor proxies. Exogeneity of the event does not imply exogeneity of those relationships or responses.
  primary_strategy: Lei2021 author version Sections4–5, equation1 and AppendixA equation3 construct assistance; Section5 county regressions include prefecture effects and controls, with prefecture-clustered errors.
  estimand: Conditional association of prior government-favor proxies with the inferred2001 assistance ratio, plus ownership-specific association with abnormal firm subsidies; no independently established causal effect of favors.
  treatment_variable: County1999–2000 local-state-related debt leverage and private-firm effective tax rates are explanatory relationship proxies; the assistance ratio is the main county response, not a randomly assigned treatment.
  comparison_logic: Within-prefecture counties differ in pre-event proxies. Counterfactual revenue removes a fitted trend, not an untreated national group. The micro analysis compares ownership-specific pre-favor proxies with each firm's2001 abnormal subsidy.
  estimation_notes: County sample is471 counties in112 prefectures/25 provinces, excluding Tibet/Xinjiang/Qinghai. Debt leverage is aggregate liabilities over aggregate assets; effective rate is an unweighted mean of firm reported tax-paid/tax-base ratios, not aggregate tax divided by aggregate base. Ownership shares use sales. Micro subsidy prediction fits firm-specific quadratics on1999,2000,2002,2003; abnormal subsidy is actual minus predicted, divided by actual. Section5.5 describes firm effects for year-dummy plots but Figure7's caption says county effects; resolve this before reproducing that plot. Zero actual subsidies and nonpositive predictions need code-level handling, not invented imputation.
  assumptions:
  - County revenue counterfactuals are informative despite using post-sharing years and only five non-event annual observations.
  - Other-tax deviations adequately separate relabeling from other changes in revenue collection.
  - Favor proxies distinguish informal relationships from productivity, liquidity, fiscal structure and government control; the record does not certify this.
  diagnostics: [Trend-form and leave-year-out sensitivity, Relabeling sensitivity, Ownership-specific comparisons, Firm tax/enforcement and leverage trends, County sample selection, Province-specific fiscal pass-through, Zero-denominator audit]
threats:
- type: endogenous-relationships
  basis: reported
  condition: Transfers are not observed. Prior leverage and effective rates proxy favors; the paper tests enforcement and government-control alternatives but those tests do not randomly assign relationships.
  evidence_refs: [E4]
  possible_diagnostics: [Liquidity controls, Majority/minority state ownership, Firm tax trends, Alternative relationship evidence]
- type: base-adjustment-and-pass-through
  basis: documented
  condition: Base inflation is subject to audit deductions and subsequent recalculation. Shanghai distinguishes central-to-city from city-to-county bases; a uniform permanent county reward cannot be inferred.
  evidence_refs: [E1, E2, E3]
  possible_diagnostics: [Original province/county fiscal rules, Approved base and actual settlements, Separate expected incentive from realized reward]
- type: generated-response-and-selected-sample
  basis: reported
  condition: Assistance is a generated residual-based ratio; the fitted counterfactual uses post-reform years. Counties with separately available income-tax series are selected, and surveyed firms do not cover all county taxpayers.
  evidence_refs: [E4, E5]
  possible_diagnostics: [Alternative trends, Post-reform exclusion sensitivity, Fiscal category concordance, Sample balance, Survey coverage]
empirical_requirements:
  contract_version: 1
  population: Counties with separately reported local corporate income tax and paper-defined domestic industrial firms
  observation_unit: County-year inputs yielding a county2001 cross-section
  geography_level: County within prefecture and province
  time_start: 1998
  time_end: 2003
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 2
  required_fields: [Local corporate income tax, Other local tax and fee categories, GDP, Population, Fiscal expenditure and revenue, Firm liabilities and assets, Firm tax paid and taxable base, Paid-in capital by ownership, Firm sales, Industry and productivity controls]
  required_identifiers: [Historical county crosswalk, Prefecture, Province, Year]
  treatment_key: [County,2001 response year]
  treatment_source: Local fiscal/tax yearbooks and fiscal statistics;1999–2000 ASIP aggregates for pre-event relationship proxies
  measurement_risks: [Restricted industrial microdata, Historical county joins, Combined income-tax/SOE-profit accounts, Missing county series, Relabeling estimates, Nonpositive counterfactuals, Provincial pass-through]
design_profiles:
- id: firm-subsidy-response
  label: Firm-level abnormal subsidy triangulation
  design_families: [Conditional association]
  when_to_use: For Section5.5-style evidence after obtaining a lawful linked industrial panel; reconcile zero subsidies and the Figure7 fixed-effect discrepancy before reproduction. This is not a distinct variation or causal treatment assignment.
  outcome_domains: [Firm subsidies]
  requirements:
    population: Paper-defined local-state-related and private domestic industrial firms
    observation_unit: Firm-year inputs yielding a firm2001 cross-section
    geography_level: Firm linked to county
    time_start: 1999
    time_end: 2003
    minimum_frequency: annual
    minimum_pre_periods: 2
    minimum_post_periods: 2
    required_fields: [Government subsidy, Debt leverage components, Tax paid and taxable base, Paid-in capital by ownership,2001 profits, Industry, County]
    required_identifiers: [Longitudinal firm identifier, Historical county crosswalk, Year]
    treatment_key: [Firm,2001 response year]
evidence:
- id: E1
  source_type: policy-document
  citation: State Council, 国务院关于印发所得税收入分享改革方案的通知, 国发〔2001〕37号
  url: https://www.mof.gov.cn/gkml/caizhengwengao/caizhengbuwengao2002/caizhengbuwengao20024/200805/t20080519_21080.htm
  date: '2001-12-31'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, assignment.rule, assignment.exemptions, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: MOF fiscal-gazette reproduction read in full; attachment SectionsIII,V,VI establish protected base, sharing scope, audits, subprovincial adjustment and2002 sharing onset.
- id: E2
  source_type: policy-document
  citation: State Council General Office, 国务院办公厅转发财政部关于2001年11月和12月上中旬地方企业所得税增长情况报告的紧急通知, 国办发〔2002〕1号
  url: https://policy.mofcom.gov.cn/claw/clawContent.shtml?id=40615
  date: '2002-01-01'
  supports: [timeline.implementation_start, timeline.implementation_end, timeline.local_timing, identity.implementation_regime, assignment.rule, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: Full notice and attached MOF report dated2001-12-29, opening October proposal and recommendationsII–III. MOFCOM-hosted reproduction credits Pkulaw, not an original signed scan; metadata separately inspected. Prohibits advanced2002 taxes, fiscal injections and bank-loan inflation; announces inspection and base deductions.
- id: E3
  source_type: implementation-document
  citation: Shanghai government, 上海市人民政府印发关于本市贯彻国务院所得税收入分享改革方案意见的通知, 沪府发〔2002〕36号
  url: https://www.shanghai.gov.cn/nw8590/20200906/0001-8590_565.html
  date: '2002-11-07'
  supports: [identity.implementation_regime, assignment.compliance, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Full text, SectionsII–IV. SectionII dates the approved base adjustment June14,2002 and gives2000-based alternatives; IV separates Shanghai district/county settlement. Shanghai example is not a nationwide county rule.
- id: E4
  source_type: paper
  citation: Yu-Hsiang Lei2021, Quid pro quo? Government-firm relationships in China, Journal of Public Economics199,104427; April2021 author manuscript
  url: https://www.dropbox.com/s/skixd0mf4xuecho/Reciprocity_draft_April21.pdf?dl=0
  date: 2021
  supports: [timeline.anticipation, assignment.unit, assignment.treated, assignment.comparison_pool, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.required_fields, design_applications.treatment_encoding, design_applications.data_used]
  verification_status: reported
  access_level: full-text
  locator: Author research page links this60-page manuscript to the publication. Sections2.1,4–5.5, PDFpp6–15,19–26; equation1 PDFp11 visually checked; Figure7 caption PDFp36 read. Publisher typesetting and replication code not independently checked.
- id: E5
  source_type: appendix
  citation: Lei April2021 author manuscript, Online AppendixA Variable Construction
  url: https://www.dropbox.com/s/skixd0mf4xuecho/Reciprocity_draft_April21.pdf?dl=0
  date: 2021
  supports: [assignment.intensity, assignment.exposure_construction, design.estimation_notes, empirical_requirements.measurement_risks]
  verification_status: reported
  access_level: appendix
  locator: PDFp43/printedp42 visually inspected in full, equation3 and items2–5; establishes level-one assistance normalization, aggregate leverage, mean firm tax rate, sales shares and actual-subsidy normalization. No PDF stored.
- id: E6
  source_type: paper
  citation: Lei2021 publication citation and author publication listing
  url: https://doi.org/10.1016/j.jpubeco.2021.104427
  date: 2021
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: Author research page https://sites.google.com/site/leiyhecon/research publication entry gives JPubE199, July2021,104427 and links April2021 manuscript; DOI metadata is identity support, not methods inspection.
design_applications:
- paper: Quid pro quo? Government-firm relationships in China
  doi: 10.1016/j.jpubeco.2021.104427
  journal: Journal of Public Economics
  year: 2021
  research_question: Do prior government favors predict firms' inferred assistance during a short-lived fiscal base-setting incentive, and do firms receive return subsidies?
  population: 471 counties and paper-defined domestic industrial firms in ASIP
  outcome: Inferred2001 county assistance ratio and abnormal firm subsidies
  data_used: [Local fiscal/tax yearbooks1998–2003, Provincial-prefectural-county fiscal statistics, ASIP1999–2003]
  treatment_encoding: Pre-event1999–2000 ownership-specific leverage and mean effective rates; county assistance and firm abnormal-subsidy construction are separate response measures
  comparison: Within-prefecture county associations and within-county ownership-specific firm associations; fitted non-event-year counterfactuals
  empirical_design: County cross-section with prefecture effects and clustered errors; firm subsidy cross-section with county effects and county-clustered errors, as described in the author version
  assumptions: [Informative counterfactuals, Adequate relabeling correction, Interpretable relationship proxies]
  threats_addressed: [Sample selection, Tax enforcement, Liquidity and state control, Revised relabeling measures]
  evidence_refs: [E4, E5, E6]
method_transfer: null
readiness_blockers:
- Conditional research use, not a certified causal instrument. Pre-existing favors and the generated response remain endogenous; countrywide timing alone supplies no untreated comparison.
- Lawful ASIP access, historical county/firm joins and exact zero-denominator handling require reconstruction. The inspected author version is not a verified final-code replication; Figure7's effects specification needs reconciliation.
- A study of realized fiscal rewards must recover province/county approved bases and settlements. Do not extrapolate Shanghai's rule or use the original raw2001 base as a permanent nationwide reward.
---

## Institutional Background

Income-tax allocation by enterprise affiliation linked local fiscal interests to local firms. The impending sharing reform protected an earlier local base while reallocating incremental revenue [E1]. The attached urgent report places central communication in October2001 and records abnormal late-year receipts; it identifies attempts to inflate the protected base and orders correction [E2]. This record preserves that temporary incentive, not the later general reduction in retained income-tax shares.

## What Changed

The anticipated protected base made late2001 receipts consequential for future fiscal resources. Sharing itself starts in2002, while the studied response belongs to2001 [E1; E2]. Keeping those clocks separate prevents a post2002 policy dummy from replacing the paper's actual event.

## Implementation and Assignment

The common news did not randomly assign government-firm relationships. Counties could differ in their ability or willingness to mobilize resources. The paper interprets differences in pre-event leverage and effective tax rates as government-favor proxies [E4, reported claim]. That interpretation remains conditional: credit access is not directly observed, and neither are informal transfers.

Authorities could disallow artificial receipts. Later base recalculation and Shanghai's separate city-to-county arrangements show why an initial incentive is not an observed permanent reward [E2; E3]. A new study must distinguish expected base benefits, booked revenue, audited bases and actual settlements.

## Why This Creates Empirical Variation

The event provides a concentrated window for studying fiscal responses. It does not turn an observational cross-section into random assignment. The paper's counterfactual uses each county's non-event years, and its main regressions relate the resulting response to earlier firm characteristics [E4, reported claim]. The repository therefore describes the application as conditional association rather than certifying a causal effect of favors.

## Identification Risks

The counterfactual includes post-reform years and the assistance measure relies on estimated relabeling. Both can change when the fiscal structure changes. Prior firm characteristics may reflect liquidity, productivity or government control rather than reciprocal favors; the inspected checks address alternatives without proving exchange or causal identification [E4, reported claim]. A new application needs an outcome-specific comparison, not simply reuse of the paper's natural-experiment label [analytical inference].

## Data Requirements

Build comparable county revenue categories before fitting trends, then join pre-event industrial-firm aggregates to the same historical county boundaries. AppendixA settles an important normalization ambiguity: assistance equals observed revenue net of relabeling divided by its counterfactual, so one, not zero, is the baseline [E5, reported claim]. Effective tax rates average firm ratios; leverage aggregates liabilities and assets. These cannot be interchanged.

The subsidy application needs a longitudinal firm panel and a different denominator: actual subsidy [E5, reported claim]. A missing or zero subsidy is not automatically a zero normalized response. Provider-controlled microdata and missing code prevent a turnkey replication claim.

## Evidence Notes

Original institutional texts ground the base-setting mechanism and its timing boundary. The urgent notice is inspected through a government-hosted third-party reproduction; exact October announcement day and universal surprise are not verified. Research construction is attributed to the author's linked April2021 version, with its appendix formula visually inspected. No restricted data, paper PDF or credentials are stored. Related blocked income-tax-sharing candidates concern longer-run fiscal exposure and should not be silently resolved to this temporary incentive case.
