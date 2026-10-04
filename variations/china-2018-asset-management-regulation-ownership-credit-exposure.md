---
schema_version: 2
id: china-2018-asset-management-regulation-ownership-credit-exposure
name: China2018 Asset-Management Regulation and Ownership-Conditioned Credit Exposure
aliases: [2018 asset-management new regulations, 资管新规, 银发〔2018〕106号]
status: grounded
provenance:
  task_id: task-88dd0e7f7e66
scope:
  country: China
  regions: [mainland China]
  domains: [financial-economics, firm-economics, development-economics]
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: Mainland corporate issuers face the2018 asset-management reform; the inspected paper compares credit and profitability changes by ultimate state control.
identity:
  instrument: Initial national asset-management regulatory reform under106, not a blanket prohibition of nonstandard debt investment or a firm-level bailout assignment.
  authority: PBOC, CBIRC, CSRC and SAFE with State Council approval.
  legal_identifiers: [银发〔2018〕106号, 关于规范金融机构资产管理业务的指导意见]
  implementation_regime: April2018 publication with new/old product separation and supervised institution-specific transition; the empirical window ends2020Q2 before the July2020 extension.
  assignment_mechanism: A common regulatory event interacted with quarterly ultimate-controller ownership, interpreted by the paper as differential vulnerability to liquidity tightening given implicit government support. Ownership is not randomized or a statutory exemption.
  parent: null
  related_variations: []
timeline:
  announcement: '2018-04-27'
  effective: '2018-04-27'
  implementation_start: '2018-04-27'
  implementation_end: null
  local_timing: Article29 initially sets transition through2020 year-end; July20 clarifies product treatment. The July31,2020 extension to2021 occurs after the paper's June2020 endpoint. The reform did not end with its sample.
  anticipation: A public consultation opened November17,2017; April2018 is not an unanticipated first disclosure. The draft proposed a different transition endpoint.
  last_verified: '2026-10-04'
assignment:
  unit: Corporate issuer-quarter; bond-quarter for pricing. Legal obligations apply to asset managers/products rather than assignment of firms by ownership.
  treated: Non-SOE issuers in the paper's differential comparison, identified by a non-state ultimate controller.
  comparison_pool: SOE issuers with state ultimate controllers, including central/local SASAC and government institutions; also exposed to the reform.
  rule: The law regulates specified asset-management institutions and products nationally. The empirical NSOE indicator is updated quarterly from ultimate-controller information; it is not a statutory treatment list.
  intensity: Government shareholdings proxy potential support; realized2018Q2 change in unified default measure is a model-dependent response. Neither is observed policy dose. Liquidity intensity changing from1 to2 is calibrated, not assigned.
  exemptions:
  - Asset securitization under financial-regulator rules and pension products under human-resources/social-security rules are outside106; private investment funds follow their special laws where specified.
  - The law does not exempt SOE issuers or forbid all nonstandard debt investments; limits, maturity matching and disclosure apply.
  compliance: New products must comply; old products may reconnect outstanding assets within a shrinking stock ceiling during transition. Institution-specific rectification plans require supervisory recognition; immediate full compliance is not established.
  exposure_construction: >
    Link corporate bonds to issuer legal IDs and listed equity IDs, then join
    quarterly controller histories, financial statements and equity prices.
    Set NSOE=1 for non-state ultimate control and0 for state control, updating
    by quarter as the paper does. Event t is2018Q2. For performance, subtract
    each firm's mean ROA over t-4 through t-1 from ROA in t+tau; pool tau=1..2
    or1..8 and regress on contemporaneous NSOE, equity size and quarter/industry
    controls (equation18 and note30). The event quarter itself is not tau=1.
    SOEs form a differential comparator, not an untreated population. Equation19
    predicts subsequent changes using event-quarter DM less its four-quarter
    pre-event mean. Equation20 splits on that realized change above its median;
    do not relabel this split predetermined assignment. Do not duplicate the
    reform for ROE, credit pricing, PSM or the model-based high/low comparison.
  required_identifiers: [issuer_legal_id, bond_id, listed_equity_id, quarter, ultimate_controller_history]
  spillovers: Portfolio substitution, investor safety preference and shared bank/shadow-bank/bond funding can transmit changes to both groups. The ownership contrast cannot recover the national total effect.
research_compatibility:
  outcome_domains: [Corporate credit spreads, Profitability, Bond liquidity, Financing conditions]
  affected_populations: [Mainland nonfinancial corporate issuers, Primarily publicly listed issuers in the real-performance application]
  mechanism_channels: [Asset-manager funding constraints, Debt rollover, Liquidity risk, Perceived government support]
  best_for: [Conditional ownership-differential responses to a national financial reform with historical controllers and quarterly issuer outcomes.]
  not_good_for: [An automatic causal effect of ownership or bailouts, An untreated-SOE DID, SME effects without corresponding borrower data, A model-free causal effect of realized default-measure changes]
design:
  claim_type: reduced-form
  affordances: [Known national event date, Recoverable quarterly ownership classification, Four-quarter pre-event performance baseline]
  candidate_designs: [Baseline-differenced ownership comparison, Model-conditioned credit-response prediction]
  identifying_variation: Differential post-event changes by ultimate ownership, conditional on counterfactual comparability and separation of concurrent ownership-specific shocks.
  primary_strategy: Equation18 compares baseline-differenced issuer profitability by quarterly NSOE status; equations19-20 examine predictive heterogeneity using event-quarter model-implied credit deterioration.
  estimand: Conditional difference between non-SOE and SOE changes in quarterly ROA, not the aggregate effect of106 or a causal bailout effect.
  treatment_variable: Quarterly NSOE interacted with the post-event comparison implicit in baseline-differenced outcomes; model-response sorting is secondary, endogenous heterogeneity.
  comparison_logic: Each firm's four-quarter pre-event mean defines its baseline; SOE issuers supply the cross-group comparator for non-SOE changes after2018Q2.
  estimation_notes: >
    Equation18 is not a generic staggered-adoption or firm-fixed-effects
    specification; note30 reports equity size and quarter/industry controls.
    TableVII clusters by firm and quarter. ROA uses net profit divided by
    lagged book assets; the two- and eight-quarter windows start2018Q3 and
    end2018Q4/2020Q2 respectively. PSM matches within industry using2018Q1
    characteristics; it does not randomize ownership. Keep ownership switches
    visible; freezing ownership would be a separate construction.
  assumptions: [Comparable counterfactual ownership-specific changes, Defensible anticipation and compliance windows, Adequate separation of concurrent differential shocks, Reliable historical controller joins]
  diagnostics: [Plot pre-event group gaps and composition, Inspect switches and missingness, Compare industry and tariff exposures, Separate pandemic quarters, Test model mapping sensitivity without treating response as allocation]
threats:
  - type: anticipation_and_transition
    basis: documented
    condition: Consultation precedes the event and implementation is phased; a single2018Q2 break need not measure immediate full compliance.
    evidence_refs: [E1, E2, E3]
    possible_diagnostics: [Allow announcement effects, Separate transition periods, Inspect funding composition and implementation paths]
  - type: ownership_and_concurrent_shocks
    basis: reported
    condition: The paper discusses2016-17 SOE deleveraging and the trade war; these checks do not eliminate all differential trends. Later windows include2020 pandemic disruption.
    evidence_refs: [E4]
    possible_diagnostics: [Assess pre-event ownership gaps, Compare industry/export exposure, Separate late windows, Inspect ownership switches]
  - type: realized_response_and_model_dependence
    basis: documented
    condition: Unified DM depends on calibrated liquidity and an assumed government-holdings-to-bailout mapping; High uses a realized event-quarter response and is not exogenous allocation.
    evidence_refs: [E4]
    possible_diagnostics: [Separate reduced form from predictive heterogeneity, Test alternative mappings, Avoid post-event sorting as an instrument]
  - type: selected_issuers_and_proxy_measurement
    basis: reported
    condition: Active-price and default exclusions change the pricing sample; real-performance coverage is broader. Controller and shareholder histories are imperfect, and observed government holdings are not actual bailout commitments.
    evidence_refs: [E4]
    possible_diagnostics: [Preserve sample-specific filters, Inspect missingness and defaults, Audit historical controller joins, Test proxy sensitivity]
empirical_requirements:
  contract_version: 1
  population: Listed mainland nonfinancial issuers participating in the corporate credit market; distinguish real-performance from actively traded bond-pricing samples.
  observation_unit: issuer-quarter
  geography_level: mainland national corporate credit market
  time_start: 2010
  time_end: 2020
  minimum_frequency: quarterly
  minimum_pre_periods: 4
  minimum_post_periods: 2
  required_fields: [Quarterly net profit and lagged book assets, Historical ultimate controller and state attribution, Equity size and industry, Corporate bond-to-issuer and issuer-to-equity crosswalks, Quarter dates and sample eligibility]
  required_identifiers: [issuer_legal_id, listed_equity_id, bond_id, quarter, ultimate_controller_history]
  treatment_key: [issuer_legal_id, quarter]
  treatment_source: 106 establishes the common event; Wind controller histories and the author's AppendixIA.III establish the empirical ownership classification, not legal eligibility.
  measurement_risks:
  - Lawful Wind access and vintage-specific crosswalks are required. Real-impact analysis includes issuers without active bond trading; do not impose every pricing-sample filter on it.
  - Exact replication requires author code/version reconciliation; the final typeset body and publisher ZIP were not inspected. The author-linked November2023 forthcoming manuscript includes an18-page Internet Appendix after the main text.
  - Model heterogeneity additionally requires equity volatility, liabilities/maturity inputs and robust government holdings; consult AppendixIA.III's Wind/CSMAR/raw merge, NSSF exclusion and conditional carry-forward/maximum rule rather than substituting a current ownership percentage.
evidence:
  - id: E1
    source_type: policy-document
    citation: PBOC Gazette2018 No9, original106 dated April27.
    url: https://www.pbc.gov.cn/chubanwu/114566/114579/4356045/4356157/2021100915240830815.pdf
    date: '2018-04-27'
    supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.announcement, timeline.effective, timeline.implementation_start, assignment.rule, assignment.exemptions, assignment.compliance]
    verification_status: verified
    access_level: official-document
    locator: Printedpp6-16, especially Articles2-3,10-11,13,15,29,31 and signature inspected2026-10-04; PDFpages8-18. The preceding107 instrument is not106.
  - id: E2
    source_type: implementation-document
    citation: PBOC explanation of the July2018 clarification notice.
    url: https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2025092212545284472/index.html
    date: '2018-07-20'
    supports: [timeline.local_timing, assignment.exemptions, assignment.compliance]
    verification_status: verified
    access_level: official-document
    locator: SectionsI-IV read2026-10-04; conditional nonstandard investment, old-product stock ceiling, valuation and residual asset handling. Page date is2018 despite migrated URL.
  - id: E3
    source_type: implementation-document
    citation: PBOC public consultation announcement.
    url: https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2025092212544884514/index.html
    date: '2017-11-17'
    supports: [timeline.anticipation]
    verification_status: verified
    access_level: official-document
    locator: Date and announcement body inspected2026-10-04; draft transition endpoint is not the final instrument's endpoint.
  - id: E4
    source_type: paper
    citation: Geng, Zhe and Jun Pan, November2023 JF forthcoming manuscript with embedded Internet Appendix.
    url: https://en.saif.sjtu.edu.cn/junpan/Credit_JF.pdf
    date: 2023
    supports: [assignment.treated, assignment.comparison_pool, assignment.intensity, assignment.exposure_construction, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.required_fields, empirical_requirements.measurement_risks, design_applications.population, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design]
    verification_status: reported
    access_level: full-text
    locator: Mainpp7-15,37-49, equations18-20, TablesVI-VIII and note30; embedded AppendixIA.II-III pp2-8 (PDF54-60) inspected2026-10-04. Methods use this version, not the materially different2020 conference draft. Pricing and real-impact samples are distinct.
  - id: E5
    source_type: paper
    citation: JF publisher metadata, Geng and Pan,79(5),3041-3103.
    url: https://doi.org/10.1111/jofi.13380
    date: 2024
    supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
    verification_status: reported
    access_level: metadata
    locator: Publisher header, author names and issue details inspected2026-10-04; metadata does not establish final-body/code equivalence.
  - id: E6
    source_type: implementation-document
    citation: SAFE reproduction of PBOC transition-extension questions and answers.
    url: https://www.safe.gov.cn/safe/2020/0731/16822.html
    date: '2020-07-31'
    supports: [timeline.local_timing, identity.implementation_regime]
    verification_status: verified
    access_level: official-document
    locator: Opening and questions1-5 read2026-10-04; extension through2021 year-end and institution-specific rectification. Outside the inspected sample endpoint.
design_applications:
  - paper: The SOE Premium and Government Support in China's Credit Market
    doi: 10.1111/jofi.13380
    journal: Journal of Finance
    year: 2024
    research_question: How do ownership and potential government support condition credit pricing and performance around liquidity tightening?
    population: Mainly publicly listed nonfinancial corporate issuers2010Q1-2020Q2; real-performance sample includes inactive bond traders. Corporate debt comprises MTNs, corporate and enterprise bonds, not LGFV/Chengtou bonds.
    outcome: Credit spreads and quarterly ROA/ROE; predictive credit-performance heterogeneity.
    data_used: [Wind bond/equity/financial/controller data, Wind and CSMAR shareholder information]
    treatment_encoding: 2018Q2 event with quarterly ultimate-controller NSOE classification; equation18 subtracts four pre-event quarters' mean ROA. Equations19-20 use realized/model-dependent event-quarter credit changes.
    comparison: SOE versus non-SOE baseline-differenced profitability; model-based high/low groups only for predictive heterogeneity.
    empirical_design: Ownership-differential event comparison with equity size and quarter/industry controls; firm/quarter clustered inference, industry-constrained PSM and trade/deleveraging robustness.
    assumptions: [Comparable counterfactual ownership-specific changes, Defensible anticipation/window choice, No unaccounted concurrent differential exposure, Valid historical controller joins]
    threats_addressed: [Reported trade-war sorting tests, Reported deleveraging comparisons, PSM and alternative government-support mappings]
    evidence_refs: [E4, E5]
method_transfer: null
readiness_blockers:
  - Obtain lawful quarterly data and historical ID/controller crosswalks; reconcile the author manuscript with final code before claiming exact replication.
  - Defend ownership comparability, anticipation, phased compliance and concurrent shocks for the proposed outcome. SOEs are not untreated.
  - Model response is predictive heterogeneity, not exogenous treatment dose; a causal credit/bailout channel needs additional identification.
---

## Institutional Background

The reform sought uniform supervision across asset-management activities,
reducing regulatory arbitrage and opaque financing while retaining financing
functions [E1]. It directly regulates asset managers and products. Corporate
issuers inherit changes through investors and credit channels, not through
a statutory SOE/non-SOE treatment list [E1; E4, reported claim].

## What Changed

106 tightened product accounting, maturity matching, guarantees and supervision.
It did not prohibit all nonstandard debt investment: Articles11 and15 impose
conditions, and July's clarification expressly permits appropriate investment
[E1, E2]. The paper's blanket-ban wording on p14 is therefore not adopted as
institutional fact. This distinction changes how a researcher should measure
funding exposure rather than merely changing terminology.

## Implementation and Assignment

New products and legacy products followed different transition arrangements;
institution-level plans prevent interpreting publication as universal immediate
compliance [E1, E2]. The paper classifies firms by ultimate controller using
quarterly histories, with state control distinguished from minority government
holdings [E4, reported claim]. Both ownership groups face the national change.

## Why This Creates Empirical Variation

The paper uses ownership differences around the event to examine differential
credit conditions and subsequent performance. The baseline-differenced ROA
comparison is reconstructable from issuer-quarter outcomes and controller
histories. Its causal use depends on an outcome-specific defense of ownership
comparability; publication alone does not supply it [analytical inference].
The unified-DM and high/low analyses add model-conditioned predictions, not
another allocation mechanism or another record [E4, reported claim].

## Identification Risks

Consultation creates anticipation; transition creates heterogeneous compliance.
The paper's trade and deleveraging tests leave other counterfactual concerns
open [E3; E4, reported claim]. Current ownership, realized credit responses,
and government-holdings proxies can reflect firm changes or measurement errors.
SOE support is an interpretation, not a legally assigned bailout entitlement.

## Data Requirements

The minimum ownership comparison needs historical controllers, quarterly
profitability, industry and equity size joined by issuer ID. Pricing additionally
requires bond transactions, characteristics and issuer crosswalks. Model-based
heterogeneity has substantially heavier requirements and should not be imposed
on an otherwise coherent reduced-form application [E4, reported claim].

## Evidence Notes

Original106, the2017 consultation, July2018 clarification and2020 extension
were inspected. The author-linked69-page file includes its Internet Appendix;
the publisher-hosted supplement and code remain uninspected. Publication
metadata is verified only as reported bibliographic evidence, not a claim that
the2023 and final executable specifications are identical. No proprietary
data or copyrighted source files are stored in this repository.
