---
schema_version: 2
id: china-post2005-export-vat-delay-fiscal-upstreamness
name: China post2005 export VAT rebate delays and fiscal-upstreamness exposure
aliases: [出口退税效率与企业出口绩效, post2005 refund delay instrument, fiscal pressure times inverse city upstreamness]
status: grounded
provenance:
  task_id: task-74c14040be70
scope:
  country: China
  regions: [Mainland China]
  domains: [firm-economics, international-trade, development, regional-economics, public-finance]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: A mainland manufacturing-exporter study uses regional fiscal pressure interacted with predetermined city industrial structure to instrument observed export VAT rebate delays.
identity:
  instrument: Regional exposure to export VAT refund administration under the post2005 central-payment and annual local-liability settlement regime.
  authority: Ministry of Finance, State Administration of Taxation and People's Bank of China; provincial and subprovincial fiscal authorities.
  legal_identifiers: [财预〔2005〕438号, 辽政发〔2005〕31号]
  implementation_regime: Central treasury cash refunds from September2005 with annual local settlement of a7.5percent above-base liability. The inspected application is2007–2011; it is not a reform-date DID or the original2004 local cash-payment regime.
  assignment_mechanism: Paper-defined province-year fiscal pressure times inverse city upstreamness fixed before the firm panel predicts differing refund delays. Legal liability supports the regional incentive context, not random assignment or a verified right to withhold central cash payments.
  parent: null
  related_variations: [china-2004-export-vat-refund-local-financing, china-2007-export-vat-rebate-product-cuts]
timeline:
  announcement: '2005-08-22'
  effective: '2005-09-01'
  implementation_start: 2005
  implementation_end: null
  local_timing: The MOF notice is signed August22. Liability changes retrospectively from January1 by refund approval date; central cash payments begin September1. Liaoning implements the successor in its September30 notice. The application uses annual2007–2011 observations, not these dates as treated-firm cohorts. No later regime endpoint is certified here.
  anticipation: The paper observes firms after the successor procedure is established;2005 is not an unanticipated sample treatment event. Its2006 city export weights precede2007 outcomes but can already reflect earlier reforms.
  last_verified: '2026-10-05'
assignment:
  unit: Province-year fiscal pressure interacted with fixed city structure, attached to firm-year rebate accounts.
  treated: Exporters with larger predicted delay exposure; treatment is continuous observed rebate delay, not binary2005 eligibility.
  comparison_pool: Manufacturing exporters facing different predicted delays within the2007–2011 panel after firm and industry-year controls. Processing-trade firms are a reported diagnostic comparison, not automatically valid untreated controls for all outcomes.
  rule: The approved rebate base remains fixed. Above-base liability is92.5percent central and7.5percent local, with local sums remitted annually. The empirical instrument multiplies provincial administrative expenditure/business-tax revenue by inverse city upstreamness; this equation is the paper's construction, not a statutory allocation rule.
  intensity: DelayRatio is year-end outstanding export VAT rebates divided by rebates due that year. It is not a statutory refund rate, elapsed processing days or a reconstructed group-average effective rate.
  exemptions: [Approved base financed centrally, Province-specific subprovincial sharing, No allocation of burden to townships or enterprises in the inspected Liaoning notice, Pure processing trade used as a refund-channel placebo]
  compliance: Central treasury payment and regional financing liability coexist. Observed unpaid claims may reflect approval or administration as well as settlement; neither fiscal liability nor the legal reform alone verifies the delay channel.
  exposure_construction: Construct city upstreamness as2006 city export-share-weighted industry upstreamness based on China's2002 IO table, then take its inverse and interact with contemporaneous provincial fiscal ratio. Preserve firm-year delay accounts separately. Join firm city to province, harmonize industry codes, and match customs products for HS8-weighted statutory-rate controls.
  required_identifiers: [firm_id, city_code, province_code, year, harmonized_industry_code, HS8_product_code]
  spillovers: Fiscal spending, supplier liquidity, regional trade and common product demand can affect other exporters; geographical peers are not necessarily unaffected.
research_compatibility:
  outcome_domains: [firm export value, export participation, exporter liquidity, firm sales]
  affected_populations: [mainland manufacturing exporters in the National Tax Survey]
  mechanism_channels: [refund timing, exporter cash flow, regional administration incentives]
  best_for: [conditional assessment of refund-delay exposure with direct tax accounts and defensible fiscal exclusion]
  not_good_for: [generic post2005 DID, treating fiscal deficits as random, assuming cities directly pay central cash refunds, substituting statutory rates for receipts, transplanting the construction into an uninspected SME paper]
design:
  claim_type: causal
  affordances: [predetermined city export structure, annual regional fiscal variation, direct refund-account measurement]
  candidate_designs: [firm-panel instrumental variables with explicit exclusion and regime checks]
  identifying_variation: Provincial fiscal-ratio variation interacts with fixed inverse city upstreamness to predict firm refund delays; the policy supplies an institutional setting rather than exogenous regional spending.
  primary_strategy: Lu and Ma2024 Equations1–2 use2SLS for log firm exports, firm effects and industry-year effects, instrumenting delay ratio with fiscal-upstreamness exposure.
  estimand: Conditional IV response of log firm export value to fiscal-pressure-induced measured delay, subject to relevance, exclusion and response assumptions; not the effect of centralizing refund payments on all firms.
  treatment_variable: Firm-year outstanding/due rebate ratio; excluded instrument equals province-year administrative expenditure/business-tax revenue times inverse city upstreamness.
  comparison_logic: Identify from continuous regional exposure among observed exporters, rather than a never-treated reform group. Firm effects remove fixed differences, not time-varying fiscal or industrial shocks.
  estimation_notes: Printedp73 specifies firm clustering; Table2 baseline has96,413 observations and reports first-stage KP58.22. Province-level common shocks need additional inference assessment. The paper harmonizes2011 industry coding to earlier years; printedp73 labels industry as CIC2. Table3 conditions on2005–2006 city export growth interacted with year and considers other firm taxes/subsidies; these are reported controls, not exclusion proofs.
  assumptions: [instrument relevance, no direct fiscal or industrial-structure channel after controls, valid baseline weights and IO crosswalk, interpretable refund-account measurement, defensible exporter selection and common-shock inference]
  diagnostics: [processing-trade placebo, pre-panel export growth controls, alternative fiscal ratio times consumer-export-share instrument, other tax and subsidy channels, province-level inference, negative or above-one delay values, later regime changes]
threats:
  - type: fiscal-and-industrial-exclusion
    basis: inferred
    condition: Administrative spending and downstream industrial structure can affect firm exports through demand, services or supply chains without changing refunds. Infrastructure controls and a strong first stage do not establish exclusion.
    evidence_refs: [E3]
    possible_diagnostics: [direct fiscal channels, exposure-specific demand controls, processing-trade placebo, reduced-form and first-stage sensitivity]
  - type: financing-versus-payment
    basis: documented
    condition: Official notices centralize cash refunds while retaining annual local liability. The paper's fiscal-delay story must not be rewritten as a verified local cash-payment prerequisite.
    evidence_refs: [E1, E2, E3]
    possible_diagnostics: [separate approval and payment timestamps, actual administrative responsibility, province-specific settlement provisions]
  - type: measurement-and-selection
    basis: reported
    condition: Outstanding balances and current-year dues can differ in vintage; Table1 reports delay ratios above one. The sample retains exporters and trims or transforms financial values. Missing claims, zero denominators, entry and customs-match selection require code reconstruction.
    evidence_refs: [E3]
    possible_diagnostics: [accounting-vintage checks, explicit denominator handling, balanced and entrant samples, match-rate audit]
  - type: common-shock-inference
    basis: inferred
    condition: Instrument variation shares province-year fiscal components and fixed city structure. Firm clustering alone does not guarantee correct inference for regional shocks.
    evidence_refs: [E3]
    possible_diagnostics: [province or multiway clustering sensitivity, regional support, leave-region-out checks]
empirical_requirements:
  contract_version: 1
  population: Mainland manufacturing exporters observed in the National Tax Survey; no SME restriction is verified for this application.
  observation_unit: firm-year
  geography_level: firm city linked to province
  time_start: 2007
  time_end: 2011
  minimum_frequency: annual
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields: [firm export value, year-end outstanding export VAT rebates, export VAT rebates due that year, provincial administrative expenditure, provincial business-tax revenue,2006 city industry export shares,2002 IO-based industry upstreamness, statutory HS8 rebate rates, firm employment capital productivity controls, provincial infrastructure investment]
  required_identifiers: [firm_id, city_code, province_code, year, harmonized_industry_code, HS8_product_code]
  treatment_key: [province_code, city_code, year]
  treatment_source: Inspected paper SectionsIII–IV; lawful tax/customs records, regional fiscal statistics and baseline IO/export structure. Official2005 notices determine the regime, not firm delay values.
  measurement_risks: [restricted firm joins, code changes, rebate balance vintages, zero dues, baseline export composition, IO-industry crosswalk, processing trade, common regional shocks]
design_profiles: []
evidence:
  - id: E1
    source_type: policy-document
    citation: MOF, SAT and PBOC. 关于出口退税负担机制调整后有关预算管理问题的通知, 财预〔2005〕438号, August22,2005.
    url: https://www.mof.gov.cn/zhengwuxinxi/zhengcefabu/2005zcfb/200805/t20080519_22509.htm
    date: '2005-08-22'
    supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.announcement, timeline.effective, timeline.local_timing, assignment.rule, assignment.compliance]
    verification_status: verified
    access_level: official-document
    locator: Full text SectionsI–V and signature. SectionII(1) central payment from September1; SectionIII annual local remittance; January1 liability uses approval dates. December28 portal date is not signature or implementation.
  - id: E2
    source_type: implementation-document
    citation: Liaoning government. 辽宁省人民政府关于完善出口退税负担机制的通知, 辽政发〔2005〕31号, September30,2005.
    url: https://www.ln.gov.cn/web/zwgkx/zfwj/szfwj/zfwj2005/C97C857B6CF141E5B98A828849F3079D/index.shtml
    date: '2005-09-30'
    supports: [assignment.rule, assignment.exemptions, assignment.compliance, timeline.local_timing]
    verification_status: verified
    access_level: official-document
    locator: Full text SectionsI–IV and signature; province3/cities4.5 shares, Dalian7.5, central cash payment and year-end remittance. Example only, not complete province coverage.
  - id: E3
    source_type: paper
    citation: Lu Bing and Ma Hong2024. 出口退税效率与企业出口绩效, China Economic Quarterly24(1),67–83. DOI10.13821/j.cnki.ceq.2024.01.05.
    url: https://nsd.pku.edu.cn/docs/20240221144541422655.pdf
    date: 2024
    supports: [assignment.intensity, assignment.comparison_pool, assignment.exposure_construction, identity.assignment_mechanism, design.primary_strategy, design.treatment_variable, design.estimation_notes, empirical_requirements.required_fields, design_applications.paper, design_applications.journal, design_applications.year]
    verification_status: reported
    access_level: full-text
    locator: 17-page publisher PDF; printed67,69–77 visually inspected by direct in-memory page rendering after garbled text extraction. SectionIII data/variables and Equations1–2, Tables1–3, printed69 footnote on2005 share. No replication code or CER2025/JPubE2023 full text inspected.
  - id: E4
    source_type: paper
    citation: Lu and Ma2024 publication identifier printed on page67 of the inspected PDF.
    url: https://doi.org/10.13821/j.cnki.ceq.2024.01.05
    date: 2024
    supports: [design_applications.doi]
    verification_status: reported
    access_level: full-text
    locator: DOI and bibliographic header visually read on printed67 of the PDF at E3; DOI landing body is not claimed inspected.
design_applications:
  - paper: 出口退税效率与企业出口绩效
    doi: 10.13821/j.cnki.ceq.2024.01.05
    journal: China Economic Quarterly
    year: 2024
    research_question: How does export VAT rebate delay affect manufacturing firm export performance?
    population: Tax-survey manufacturing exporters2007–2011
    outcome: Log firm export value
    data_used: [National Tax Survey2007–2011, Chinese customs export products, regional fiscal statistics, China2002 input-output table,2006 city export composition]
    treatment_encoding: Outstanding/due rebate ratio instrumented by province fiscal ratio times inverse fixed city upstreamness
    comparison: Differently exposed exporters with firm and industry-year effects; processing trade used as a channel placebo
    empirical_design: Firm-panel2SLS, not post2005 reform DID
    assumptions: [Fiscal exclusion, No direct industrial-structure channel, Relevance and interpretable accounting measurement]
    threats_addressed: [Processing-trade placebo, Pre-panel city export trends, Alternative instrument, Other tax/subsidy controls]
    evidence_refs: [E3, E4]
method_transfer: null
readiness_blockers:
  - Conditional IV candidate, not a ready-to-run causal certificate. Reconcile the approval/payment pathway with the centralized treasury regime and defend direct fiscal/industrial exclusion for the intended outcome.
  - Obtain authorized tax/customs identifiers and reconstruct vintage, zero-denominator, sample selection, industry/IO matching and geographic joins. No executable replication was inspected.
  - The inspected application ends2011; verify subsequent legal regimes before extending it. Assess regional-shock inference rather than inheriting firm clustering without review.
---

## Institutional Background

The original2004 regime involved local cash financing. The successor changed both the local share and the payment procedure: central treasury paid refunds while local authorities settled above-base liabilities annually [E1]. Liaoning's implementing rule retains province and city costs, including a separate Dalian arrangement [E2]. Neither notice says fiscal pressure is exogenous.

## What Changed and What This Case Represents

This record serves the later central-payment/local-settlement regime. It does not add another case because an outcome or DOI changed: its implementation boundary differs from `china-2004-export-vat-refund-local-financing`, which explicitly excludes the successor. Product rebate-rate cuts are also a separate instrument. Within the later regime, Lu and Ma use a constructed fiscal-industrial exposure to predict observed delays [E3, reported claim]; they do not estimate a September2005 reform dummy.

## Implementation and Assignment

First distinguish legal liability, approval, central payment and outstanding firm accounts. Then construct the instrument from a province-year fiscal ratio and a fixed city upstreamness measure. Keep2006 export weights and2002 IO industry measures separate from2007–2011 outcome observations. The instrument is not the official liability formula. Higher exposure predicts more delay in the reported first stage, rather than assigning a binary treatment [E3, reported claim].

## Why This Creates Empirical Variation

The paper connects refund timing to firm exports through2SLS. A researcher with direct refund accounts can recover this contrast, its baseline structure and its diagnostics. Its causal use requires excluding other fiscal and industrial channels; a formal liability and a significant first stage do not supply that exclusion [analytical inference]. Zero required pre/post periods describes an IV panel, not permission to run a DID without pre-periods.

## Identification Risks

The central-payment rule prevents describing this design as local treasuries simply withholding cash. Approval and settlement incentives can be hypotheses, but their actual pathway needs examination for a new study. Fiscal services, local demand and supplier networks are competing channels. The processing-trade placebo and alternative instrument are observed paper diagnostics, not universal validity guarantees [E3, reported claim; analytical inference].

## Data Requirements

Use tax balances for delay, customs products for rebate-rate controls, and historical regional structure for the instrument. A balance exceeding current-year dues need not mean more than a full year's processing delay; vintages matter. Public legal documents do not make firm identifiers public.

## Evidence Notes

The inspected Chinese application does not certify the different CER2025 SME sample or the JPubE2023 article. No estimates, restricted data or executable replication have been reproduced. The official notices establish financing and payment responsibilities, not exclusion or realized firm delays.
