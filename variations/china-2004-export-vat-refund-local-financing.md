---
schema_version: 2
id: china-2004-export-vat-refund-local-financing
name: China2004 Export VAT Refund Local-Financing Exposure
aliases: [出口退税负担机制改革,2004 export rebate fiscal sharing, Local fiscal constraints and exporter VAT refunds]
status: grounded
provenance:
  task_id: task-c72835e5f52c
scope:
  country: China
  regions: [Mainland China]
  domains: [firms, international-trade, public-finance, development-economics, regional-economics]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: Chinese exporters faced geographically different effective refunds when local governments acquired financing responsibility above a fixed rebate base.
identity:
  instrument: The2004 introduction of local fiscal liability for export VAT refunds above the approved2003 base
  authority: State Council, fiscal and tax authorities and treasuries; provincial and subprovincial implementation
  legal_identifiers: [国发〔2003〕24号, 苏政发〔2004〕24号]
  implementation_regime: Original2004 central/local financing arrangement. The2005 reduction and treasury redesign are a successor boundary, not a second shock pooled into the treatment.
  assignment_mechanism: Regional fiscal capacity conditions actual refunds under a newly shared financing obligation; not randomized product rebate rates or random fiscal deficits
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: '2004-01-01'
  implementation_start: 2004
  implementation_end: 2004
  local_timing: The national decision specifies2004 onset. Jiangsu's2004-02-26 implementation applies fromJanuary1 by customs export date. The successor budget notice applies a reduced local share from2005-01-01 by refund approval date, and changes treasury payments fromSeptember1. These clocks are not interchangeable.
  anticipation: Reform was decided in2003 amid arrears;2004 is not an unanticipated date. The source paper excludes2003 from its pre-reform comparison.
  last_verified: '2026-10-02'
assignment:
  unit: Regional financing authority; empirical exposure at province-industry-year attached to a firm
  treated: Exporters whose actual refund availability depends on regional financing obligations above the approved base
  comparison_pool: Differently constrained regional exporter groups in the paper's2004–2006 panel;2000–2002 serves as a pre-reform instrument-relevance comparison, not a clean untreated random group
  rule: From2004 the central government funds the2003 approved rebate base; refunds above it are shared75percent centrally and25percent locally. This is a fixed base, not the previous year's exports. Provincial arrangements determine which local treasury pays.
  intensity: Paper's reconstructed de facto rebate rate averaged within province and two-digit industry; fiscal constraint instrument is (administrative expenditure minus business-tax revenue) divided by administrative expenditure
  exemptions: [Historical arrears financed centrally,2005 successor arrangements outside the original25percent regime, Statutory product-rate changes are not this assignment mechanism]
  compliance: Formal fiscal liability does not observe firm-specific payment delay. Jiangsu's notice assigns initial local treasury payments and later base settlement; actual receipt remains an empirical measurement question.
  exposure_construction: Reconstruct each positive-export firm's rebate rate as (0.17 times revenue minus input VAT minus VAT payable) divided by export value, then average by province/two-digit industry/year. Link provincial administrative expenditure and business-tax revenue by province/year. Retain the fixed approved base and legal regime dates separately from the paper's effective-rate proxy.
  required_identifiers: [Stable firm identifier, Province, Two-digit industry crosswalk, Year]
  spillovers: Export activity changes local service demand and fiscal revenues; refund delays can also propagate through supplier finance and competition.
research_compatibility:
  outcome_domains: [Firm exports, Export participation, Exporter liquidity, Regional trade performance]
  affected_populations: [Manufacturing exporters, Regional fiscal authorities]
  mechanism_channels: [Refund financing capacity, Cash flow, Effective export tax burden]
  best_for: [Conditional assessment of local fiscal constraints and effective exporter refunds]
  not_good_for: [Treating statutory rebate rates as observed receipts, Claiming fiscal deficits are intrinsically exogenous, Fixed25percent exposure throughout2004–2006, Inferring export quantities without price information]
design:
  claim_type: causal
  affordances: [New local financing liability, Regional variation in actual refunds, Pre-reform relevance comparison]
  candidate_designs: [Firm-panel2SLS with explicit regime sensitivity]
  identifying_variation: Provincial routine fiscal deficit as an instrument for province-industry effective rebate rates after local financing begins
  primary_strategy: Chandra and Long2013, Sections3–4, equations2–3 and Tables2–3; firm/year effects and2SLS
  estimand: Conditional response of firm export value to instrument-induced effective rebate rates; not a policy-DID effect or a national welfare calculation
  treatment_variable: Province-industry-year mean reconstructed rebate rate
  comparison_logic: Compare exporter trajectories across effective-rate groups; evaluate instrument relevance before reform and separate the2005 successor procedure
  estimation_notes: Main source uses2004–2006; precomparison2000–2002 omits2003. Firms exported at least once during2000–2006. Baseline clusters at province/two-digit-industry, with firm-clustered variants; neither automatically resolves a province-year instrument's common shocks. Exact zero-export handling in log outcomes requires reconciliation before reproduction.
  assumptions:
  - Fiscal conditions affect exports through refunds rather than services, infrastructure, demand or other local policies.
  - Accounting proxies capture economically relevant refund variation rather than mechanically sharing errors with export outcomes.
  - The post-reform specification remains interpretable despite the2005 financing and payment redesign.
  diagnostics: [First-stage by legal regime, Pre-reform relevance comparison, Alternative fiscal measures, Bonded-input and foreign-firm exclusions, Leave-one-out group rebate sensitivity, Province-level inference sensitivity]
threats:
- type: fiscal-exclusion
  basis: reported
  condition: The paper acknowledges feedback from exports to service-tax revenue and administrative spending. A strong first stage or an insignificant earlier correlation does not prove exclusion.
  evidence_refs: [E3]
  possible_diagnostics: [Direct fiscal channels, Regional demand controls, Alternative instruments, Explicit conditional interpretation]
- type: successor-procedure
  basis: documented
  condition: The2005 notice reduces local liability to7.5percent and shifts cash payments centrally; the paper's2004–2006 discussion cannot establish an unchanged local-payment prerequisite throughout that window.
  evidence_refs: [E2, E3]
  possible_diagnostics: [Separate2004 from2005–2006, Province implementation checks, Regime-specific first stage]
- type: reconstructed-rate-and-selection
  basis: reported
  condition: The rate formula assumes no bonded imports; group means use only positive-export firms, while the ever-exporter sample depends on outcomes in the whole period. Shared numerator/denominator errors and changing exporter composition matter.
  evidence_refs: [E3]
  possible_diagnostics: [Direct receipt data if available, Leave-one-out means, Stable exporters, Bonded-input corrections]
empirical_requirements:
  contract_version: 1
  population: Above-scale manufacturing firms exporting at least once in the paper's2000–2006 window
  observation_unit: Firm-year
  geography_level: Firm linked to province and industry
  time_start: 2000
  time_end: 2006
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields: [Export value, Revenue, Input VAT, VAT payable, Province, Two-digit industry, Provincial administrative expenditure, Provincial business-tax revenue, Firm employment, Capital and productivity controls, Provincial income, Legal regime year]
  required_identifiers: [Stable firm identifier, Province, Industry crosswalk, Year]
  treatment_key: [Province, Two-digit industry, Year]
  treatment_source: NBS industrial-survey accounting proxy plus provincial statistical yearbooks and original fiscal notices
  measurement_risks: [Restricted identified microdata, Bonded inputs, Payment lags, Fiscal-accounting definitions, Group composition, Zero exports,2005 procedure change]
design_profiles: []
evidence:
- id: E1
  source_type: policy-document
  citation: State Council, 国务院关于改革现行出口退税机制的决定, 国发〔2003〕24号
  url: https://zfgb.fj.gov.cn/6970
  date: 2003
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, timeline.implementation_start, assignment.rule, assignment.exemptions]
  verification_status: verified
  access_level: official-document
  locator: Fujian government gazette2003issue30 reproduction, SectionII items3 and5; full text retrieved by direct request. Fixed2003 base,2004 cost sharing and centrally financed arrears. Exact signing day not established on this page.
- id: E2
  source_type: implementation-document
  citation: MOF, SAT and PBOC, 关于出口退税负担机制调整后有关预算管理问题的通知, 财预〔2005〕438号
  url: https://www.mof.gov.cn/zhengwuxinxi/zhengcefabu/2005zcfb/200805/t20080519_22509.htm
  date: '2005-08-22'
  supports: [identity.implementation_regime, timeline.implementation_end, timeline.local_timing, assignment.exemptions, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Signature and itemsI–III; effectiveJanuary1 by approval date,92.5/7.5 liability, September1 central treasury payments and annual local remittance. Page publicationDecember28 is not the effective date.
- id: E3
  source_type: paper
  citation: Chandra and Long2013, VAT rebates and export performance in China, JPubE102,13–22
  url: https://doi.org/10.1016/j.jpubeco.2013.03.005
  date: 2013
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year, assignment.intensity, assignment.comparison_pool, assignment.exposure_construction, design.primary_strategy, design.treatment_variable, design.estimation_notes, empirical_requirements.required_fields]
  verification_status: reported
  access_level: full-text
  locator: Publisher-formatted10-page PDF at https://econpub.xmu.edu.cn/research/repec/upload/201371881397055475115776.pdf; printedpp15–19, Sections2.2–4, equations1–3, Table1 and discussion of Tables2–3, footnotes7–15. No replication code inspected.
- id: E4
  source_type: implementation-document
  citation: Jiangsu government, 省政府关于改革现行出口退税负担办法的通知, 苏政发〔2004〕24号
  url: https://jsz.mof.gov.cn/zhengcefagui/200805/t20080524_42292.htm
  date: '2004-02-26'
  supports: [timeline.effective, timeline.local_timing, assignment.rule, assignment.compliance, identity.legal_identifiers]
  verification_status: verified
  access_level: official-document
  locator: Opening and SectionII, local treasury25percent payment and base settlement, export-date convention. Jiangsu implementation example, not a complete national province ledger.
design_applications:
- paper: 'VAT rebates and export performance in China: Firm-level evidence'
  doi: 10.1016/j.jpubeco.2013.03.005
  journal: Journal of Public Economics
  year: 2013
  research_question: How do effective VAT rebates affect Chinese manufacturing exports?
  population: Paper-defined manufacturing ever-exporters
  outcome: Firm export value
  data_used: [NBS industrial survey2000–2006, China Statistical Yearbooks2000–2006]
  treatment_encoding: Province/two-digit-industry mean reconstructed actual rebate rate; provincial fiscal deficit instrument
  comparison: Differently exposed exporter groups, plus2000–2002 pre-reform relevance check
  empirical_design: 2004–2006 firm-panel2SLS; paper period spans the2005 legal successor
  assumptions: [Fiscal exclusion, Correct accounting proxy, Comparable legal regime interpretation]
  threats_addressed: [Alternative clustering, Pre-reform comparison, Domestic-firm and non-processing samples]
  evidence_refs: [E3]
method_transfer: null
readiness_blockers:
- Conditional for new causal research. The2005 financing/procedure break requires regime-specific first stages or additional implementation evidence; do not reproduce the paper's simplified25percent narrative as a verified2004–2006 rule.
- Identified industrial-survey data, exact longitudinal joins, zero-export outcome handling and accounting fields require lawful access and code reconstruction. A publisher PDF does not make microdata public.
---

## Institutional Background

Refund arrears strained exporter finance. The reform transferred part of the cost above a fixed base to local governments [E1]. This connects a national tax system to regional financing conditions, without making those conditions exogenous.

## What Changed

The original local share was25percent in2004. In2005 the formal share fell and treasury procedure changed [E2]. This record preserves that boundary rather than treating the entire paper window as one unchanged payment system. Product-specific statutory rate reductions are a different empirical object.

## Implementation and Assignment

Jiangsu's implementing notice specifies local treasury responsibilities and base settlement [E4]. A fiscal obligation is not a firm receipt. Chandra and Long infer effective rates from accounting data and attach regional-industry averages to firms [E3, reported claim]; a new study needs to distinguish these proxies from observed approval or payment delays.

## Why This Creates Empirical Variation

The paper uses differences in regional fiscal capacity to predict effective refund rates. That supplies an instrument, not a simple post2004 treatment dummy. Its exclusion argument is the substantive condition: the same regional finances must not change exports through other channels. Earlier-period correlations cannot settle that question [analytical inference].

## Identification Risks

The successor procedure changes the first-stage story. Administrative spending and services can also reflect exporter activity. Group averages reduce some noise but retain composition and shared-accounting errors; a leave-one-out construction is a proposed diagnostic, not something verified in the paper [analytical inference].

## Data Requirements

Keep firm identities, province and industry stable, then reconstruct accounting rates and link regional fiscal data. Missing refunds are not zero refunds, and a nonexporter has no rate under the printed formula. Preserve the separate customs-export, refund-approval and treasury clocks. Public legal texts do not replace provider-controlled firm data.

## Evidence Notes

The institution and original assignment are grounded in official texts. The published application remains a conditional research use spanning a successor regime, not proof of unchanged implementation. The2003 base is fixed; the paper's occasional previous-year wording does not redefine it. No estimate is reproduced, no replication is claimed and no paper or restricted data was stored.
