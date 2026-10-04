---
schema_version: 2
id: china-2015-local-government-debt-swap-credit-reallocation
name: China 2015 Local-Government Debt Swap and Private-Firm Credit Reallocation
aliases:
- China debt-to-bond swap province exposure
- 2015 local government debt restructuring bank lending
- 地方政府债务置换与民营企业融资
status: grounded
provenance:
  task_id: task-53db0c4e99c8
scope:
  country: China
  regions: [Mainland China, 25 provinces in the published loan application]
  domains: [regional-economics, public-finance, corporate-finance, banking, firm-dynamics]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    Chinese local-government repayment obligations were converted from non-bond
    debt into government bonds. The application compares private and state-owned
    borrowers at one Chinese bank across lender provinces with different initial
    government-debt stocks. It studies debt composition, not simply fiscal expansion.
identity:
  instrument: The 2015 local-government debt-to-bond swap of screened government repayment obligations
  authority: State Council authorization, Ministry of Finance quota administration, and provincial-level bond issuers
  legal_identifiers:
  - 国发〔2014〕43号, 国务院关于加强地方政府性债务管理的意见, dated 2014-09-21 and publicly released 2014-10-02
  - MOF 2015-03-12 explanation of the first RMB 1 trillion swap quota
  - CBRC Order 2012 No. 1, 商业银行资本管理办法（试行）, Article 58
  implementation_regime: >
    Screen government repayment obligations and admit eligible debt to budget
    management; issue government bonds to replace eligible non-bond principal.
    Issuance and repayment belong to provincial-level governments and separately
    planned cities, not to every LGFV as a corporate issuer. The first quota covered
    audited debt outstanding on 30 June 2013 and maturing in 2015. Later quotas
    expanded the program. This record excludes the separate 2024 debt-swap regime.
  assignment_mechanism: >
    Legal eligibility follows screened government repayment responsibility, quota
    allocation and debt maturity. The research exposure is different: demeaned log
    province government debt outstanding at end-2014, interacted with a post-2015
    indicator and private-borrower status. The stock is a proxy for potential swap
    exposure, not observed branch-level swapped debt or randomized assignment.
  parent: null
  related_variations: [china-basel3-branch-risk-monetary-transmission]
timeline:
  announcement: '2014-10-02'
  effective: null
  implementation_start: 2015
  implementation_end: null
  local_timing: >
    The State Council document was dated 21 September 2014 and released publicly
    on 2 October. MOF explained the first quota on 12 March 2015 and reported
    substantial issuance by December. The paper codes Post=1 for 2015 onward.
    This annual clock does not establish that every loan faced an actual conversion
    on 1 January; exact province/branch settlement dates are not recovered here.
  anticipation: >
    The paper excludes 2014Q4 following the reform announcement. Its September
    announcement description differs from the verified public release date; neither
    clock establishes absence of earlier anticipation or changes during 2014.
  last_verified: '2026-10-02'
assignment:
  unit: Loan-firm-lender-province-quarter observation
  treated: >
    Private-firm loans in 2015-2017, with greater paper-defined exposure in lender
    provinces having higher end-2014 government debt. There is no untreated
    province under the nationwide reform and no statutory private-firm lottery.
  comparison_pool: >
    State-owned-firm loans and private-firm loans across provinces with lower
    initial debt, before and after 2015, in the same anonymous bank's eligible
    manufacturing sample. Ownership differences and regional debt are conditional
    comparisons, not evidence of random treatment.
  rule: >
    For loan i to firm f through lender province j in quarter t, construct
    POE_i * 1(year>=2015) * [ln(GovDebt_j,end2014) - sample mean of ln debt].
    Include the lower-order interactions specified in equation 11. Use the
    lender's province (footnote 20), not the firm's address, for GovDebt.
  intensity: Demeaned log level of end-2014 provincial debt, not debt/GDP, actual swap volume or contemporaneous debt
  exemptions:
  - The first swap quota excludes debts repayable from enterprises' own revenues and cannot fund interest or recurrent spending.
  - The paper excludes Xinjiang, Tibet and the four directly administered municipalities; its debt exposure covers 25 provinces.
  - The baseline loan sample excludes 2014Q4 and is restricted to the bank/ASIF match, not all Chinese enterprises.
  compliance: >
    Official rules require debt-project correspondence and repayment agreements.
    The December 2015 ministerial report documents rollout, not equal conversion
    at every branch. The paper explicitly lacks branch-level swapped-debt amounts;
    province debt is therefore an exposure proxy rather than verified compliance.
  exposure_construction: >
    Match loan borrowers to ASIF by firm names where stable common codes are absent.
    Preserve borrower ownership, lender province and loan quarter. Aggregate the
    paper's cited city debt inventory to end-2014 province debt, using a consistent
    monetary unit before logs and demeaning. Restrict loans to 2013Q1-2017Q4,
    omit 2014Q4, and merge average 2011-2013 firm controls. Reproduce the source
    ownership dictionary and matched-sample mean before exact replication.
  required_identifiers: [Loan identifier, Firm identifier and source names, Lender branch and province code, Loan quarter, Borrower ownership code]
  spillovers: >
    Headquarters can reallocate funding across branches and provinces, and firms
    can borrow across regions or banks. The paper reports a cross-province
    spillover check in its supplement, which was not inspected. Low-debt provinces
    and SOEs may respond to the same reform and cannot be treated as unaffected.
research_compatibility:
  outcome_domains: [Loan pricing, Credit allocation, Private-firm financing, Bank risk taking, Regional productivity]
  affected_populations: [Manufacturing borrowers at one Chinese Big Five bank, Private firms and SOEs, Provincial and city bank branches]
  mechanism_channels: [Risk-weighted asset relief, Reallocation toward private borrowers, Fiscal interest-cost relief, Bond-market and loan-demand substitution]
  best_for:
  - Conditional analysis of private-versus-state loan pricing across provincial debt exposure
  - Distinguishing debt-composition changes from increases in the amount of government debt
  - Studying within-bank regional credit reallocation with restricted loan data
  not_good_for:
  - Treating all LGFV debt as eligible government debt or every province as swapped on the same day
  - Estimating all firms' probability of obtaining credit from a sample of issued loans
  - Identifying nationwide average loan-rate or welfare effects from the relative ownership contrast
  - Applying the published treatment directly to a listed-firm panel without lender geography
design:
  claim_type: reduced-form
  affordances: [Nationwide reform with continuous regional exposure, Private-versus-state borrower contrast, Pre-reform loan panel, Multiple-branch borrower demand controls]
  candidate_designs: [Loan-level continuous-exposure triple difference, Ownership-specific event study, Branch-year private-loan share comparison]
  identifying_variation: >
    The identifying contrast is the change in the private-versus-state loan-rate
    gap after 2015 as initial lender-province debt increases. A causal reading
    requires comparable counterfactual ownership gaps across the debt gradient,
    rather than merely a common national reform date.
  primary_strategy: >
    Equation 11 includes POE*Post, POE*Post*GovDebt, GovDebt*POE and
    GovDebt*Post, firm/province/year-quarter effects and initial firm controls
    interacted with year. Initial controls are 2011-2013 average leverage, ROA
    and tangible-assets/total-assets. Double cluster by firm and year-quarter.
  estimand: >
    Differential change in the private-versus-state relative loan-rate markup
    per log-unit of initial provincial debt among observed loans at the sampled
    bank. It is not the total effect on lending or all private firms' credit access.
  treatment_variable: POE_i * Post2015_y * demeaned ln(end2014 province government debt)
  comparison_logic: >
    Compare ownership gaps before and after reform, then compare those changes
    along the provincial debt gradient. Include lower-order interactions and
    retain lender geography. Private status proxies loan risk in this application;
    it is not synonymous with a measured default probability.
  estimation_notes: >
    Table 1 column 2 uses 123,803 loans. LoanRate is the percentage deviation
    of actual interest from the benchmark, not a percentage-point difference in
    actual rates. The full matched database has about 400,000 firm-loan pairs
    over 2008Q1-2017Q4, but the baseline is smaller. Table 1 notes describe controls
    as before 2013 whereas Section 4.2 specifies 2011-2013 averages; follow the
    explicit section definition and verify code before exact reproduction. The
    annual event study uses 2013 as reference and one pre-reform year coefficient.
  assumptions:
  - No other 2015 change drives the private-versus-state gap differently across initial provincial debt levels.
  - End-2014 debt measures eligible exposure sufficiently well rather than only regional size, distress or credit demand.
  - Name matching, ownership and loan selection do not generate a changing composition correlated with exposure.
  - The chosen benchmark rate and loan terms remain comparable across ownership and time.
  - Cross-province funding shifts do not invalidate the specified counterfactual gap.
  diagnostics:
  - Ownership-gap and debt-gradient leads, with explicit power limits from the short pre-period
  - Loan-term and borrower-composition balance before and after reform
  - Firm-by-quarter comparisons for borrowers using multiple branches, as in Table 4
  - Branch-by-quarter controls and sensitivity of the risk-weight channel interpretation
  - Province-level inference sensitivity beyond the reported firm/quarter clustering
  - Separate LGFV, local-SOE and large-firm exclusions; recover supplementary construction before claiming replication
threats:
- type: endogenous-provincial-exposure
  basis: reported
  condition: Province debt reflects prior public investment and macroeconomic conditions; the paper explicitly discusses divergent credit supply and demand across debt levels.
  evidence_refs: [E4]
  possible_diagnostics: [Pre-trend and regional-control sensitivity, Debt/GDP and region-size comparisons, Recover the matched fast/slow-swap implementation exercise]
- type: policy-package-and-timing
  basis: documented
  condition: >
    The official program combined debt screening, quotas, fiscal relief, issuance
    mechanisms and monetary accommodation. The annual 2015 post dummy bundles
    these changes and does not measure loan-specific conversion dates.
  evidence_refs: [E1, E2, E3]
  possible_diagnostics: [Province issuance/settlement timing, Quarter-specific post definitions, Concurrent credit and housing reforms]
- type: loan-selection-and-external-validity
  basis: documented
  condition: >
    One confidential bank and the ASIF name match select observed borrowers.
    Section 4.7's POE-loan dummy concerns the ownership of an issued loan, not
    an application universe including rejected and nonapplicant firms.
  evidence_refs: [E4]
  possible_diagnostics: [Entry/exit and matched-name audit, Separate loan-count and loan-value shares, Obtain application/rejection data for true access probabilities]
- type: regional-clustering-and-spillovers
  basis: inferred
  condition: Treatment intensity varies at only 25 provinces; within-bank allocation can connect comparison regions. Reported firm/quarter clustering alone does not settle province-level correlated shocks.
  evidence_refs: [E4]
  possible_diagnostics: [Province-level small-cluster inference sensitivity, Cross-province spillover construction, Multiple-bank comparison where obtainable]
empirical_requirements:
  contract_version: 1
  population: Manufacturing loans at the sampled bank with private and state-owned borrowers and ASIF-linked baseline controls
  observation_unit: Loan-firm-lender-province-quarter
  geography_level: Lender province with borrower location retained separately
  time_start: 2013
  time_end: 2017
  minimum_frequency: quarterly
  minimum_pre_periods: 4
  minimum_post_periods: 4
  required_fields: [Actual loan interest rate, Applicable benchmark rate, Borrower private/state ownership, End-2014 provincial government debt, 2011-2013 leverage, 2011-2013 ROA, 2011-2013 tangible-assets to total-assets ratio]
  required_identifiers: [Loan ID, Firm ID and matching names, Lender province code, Lender branch ID, Year and quarter]
  treatment_key: [Lender province code, Year and quarter, Borrower ownership]
  treatment_source: Published equation 11 and province debt assembled from the cited Qu et al. inventory; official screened-debt and quota rules bound its institutional meaning.
  measurement_risks: [Debt stock is not actual branch swap amount, Ownership mapping and name-cleaning code not inspected, Confidential bank coverage, Benchmark-rate term matching, Post-2013 firm controls are not contemporaneously observed in ASIF]
design_profiles: []
evidence:
- id: E1
  source_type: policy-document
  citation: State Council, 国务院关于加强地方政府性债务管理的意见, 国发〔2014〕43号
  url: http://www.gov.cn/zhengce/content/2014-10/02/content_9111.htm
  date: '2014-09-21'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.announcement, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: Full text inspected through direct HTTP; document issue/release metadata; II(1)-(4), III and VI(1)-(2), VII
- id: E2
  source_type: implementation-document
  citation: MOF, 财政部有关负责人就发行地方政府债券置换存量债务有关问题答记者问
  url: https://www.mof.gov.cn/zhengwuxinxi/caizhengxinwen/201503/t20150312_1201705.htm
  date: '2015-03-12'
  supports: [identity.implementation_regime, timeline.implementation_start, timeline.local_timing, assignment.compliance, assignment.exemptions]
  verification_status: verified
  access_level: official-document
  locator: Full Q&A; first quota, eligible audited debt, regional allocation 53.8%, issuers and repayment-purpose restrictions
- id: E3
  source_type: implementation-document
  citation: Lou Jiwei, 国务院关于规范地方政府债务管理工作情况的报告, NPC Standing Committee report 22 December 2015
  url: https://www.mof.gov.cn/zhengwuxinxi/caizhengxinwen/201512/t20151223_1626635.htm
  date: '2015-12-22'
  supports: [identity.implementation_regime, timeline.implementation_start, timeline.local_timing, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: I(1)-(3), especially I(2) quota, issuance through 11 December, issuance mechanisms and monetary accommodation; II remaining financing problems
- id: E4
  source_type: paper
  citation: Li, Xiaoming, Zheng Liu, Yuchao Peng and Zhiwei Xu (2026), The crowding-in effects of local government debt in China, Journal of Monetary Economics 159, 103922; online 11 March 2026
  url: https://doi.org/10.1016/j.jmoneco.2026.103922
  date: '2026-03-11'
  supports: [identity.assignment_mechanism, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.intensity, assignment.exposure_construction, assignment.required_identifiers, assignment.spillovers, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.population, empirical_requirements.required_fields, design_applications.paper, design_applications.doi, design_applications.year, design_applications.research_question, design_applications.population, design_applications.outcome, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design]
  verification_status: reported
  access_level: full-text
  locator: >
    Author-linked published typeset PDF, 19 pages, via item 25 at
    https://xuzhiwei09.wixsite.com/econ/research; pages 1-5 and 8-18 inspected,
    Sections 2 and 4.1-4.8, equations 11-12, Tables 1-6, footnotes 17-28;
    DOI is identity anchor, publisher direct access returned 403.
- id: E5
  source_type: policy-document
  citation: CBRC Order 2012 No. 1, 商业银行资本管理办法（试行）, official local-government reprint
  url: https://www.miluo.gov.cn/25221/25222/26735/26736/27199/content_670823.html
  date: '2012-06-07'
  supports: [identity.legal_identifiers, identity.implementation_regime]
  verification_status: verified
  access_level: official-document
  locator: Promulgation/effective-date header; Articles 47-68 directly inspected, particularly 58 public-sector claims including provincial governments and exclusion of their corporate investees, and 63 general corporate claims
design_applications:
- paper: The crowding-in effects of local government debt in China
  doi: 10.1016/j.jmoneco.2026.103922
  journal: Journal of Monetary Economics
  year: 2026
  research_question: Does converting government repayment debt into government bonds change private-versus-state loan pricing and within-bank credit allocation?
  population: Observed manufacturing loans at one unnamed Big Five bank across 25 lender provinces; 2013Q1-2017Q4 excluding 2014Q4
  outcome: Percentage deviation of actual loan rate from benchmark; separate issued-loan ownership and branch private-loan-value shares
  data_used: [Confidential bank loans and borrower ratings, ASIF name-linked baseline firm characteristics, Province debt assembled from Qu et al. (2023)]
  treatment_encoding: POE * Post2015 * demeaned log end2014 lender-province debt, with lower-order terms
  comparison: Private/state loan-rate gaps over time along initial province debt exposure
  empirical_design: Equation 11 continuous-exposure triple difference; firm/province/quarter fixed effects and baseline-controls-by-year; firm/quarter double clustering
  assumptions: [Conditional parallel ownership-gap trends across debt intensity, Consistent borrower selection and debt measurement, No confounding regional ownership-specific reform shock]
  threats_addressed: [Annual pre-trend exercise, Multiple-branch borrower demand controls, Branch-quarter supply controls, Reported supplementary regional spillover and policy controls not independently inspected]
  evidence_refs: [E4]
method_transfer: null
readiness_blockers:
- Bank data are confidential; ownership-code mapping, loan-term benchmark matching, name cleaning and the exact demeaning sample require source materials before exact replication.
- Province debt proxies potential swaps; actual branch holdings/conversions and bank-specific IRB implementation dates are not independently observed. Use the reduced-form contrast, not a certified exclusive risk-weight mechanism.
- The annual policy clock is not an exact settlement date; supplement and code were not inspected, and secondary outcome contracts are not admitted as independently reproducible designs.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Local-government financing through corporate vehicles mixed government repayment
responsibility with corporate obligations. The 2014 State Council decision required
screening and budget recognition rather than assuming every LGFV liability belonged
to government. It authorized government bonds to replace screened budget-managed
debt and kept enterprises responsible for their own debt [E1]. The empirical object
here is the 2015 conversion regime, not the growth of local debt after 2008 or the
new debt measures announced in 2024.

## What Changed

Conversion changes the asset that a bank holds. Article 58 of the capital rules
assigns a 20% weight to qualifying public-sector claims, including provincial
governments, and explicitly excludes their corporate investees from that treatment
[E5]. The paper reports that its bank used IRB weights for corporate loans but a
20% weight for local-government bonds. It links the swap to a relaxation of the
risk-weighted asset constraint [E4, reported claim]. The regulation establishes the
category distinction; it does not independently verify this anonymous bank's
holdings, internal implementation or every loan's prior weight.

The first quota allocated eligible 2015-maturing debt using a common 53.8% ratio.
By December, official reporting described a larger annual quota and substantial
issuance, alongside liquidity and issuance-policy support [E2; E3]. Thus the change
was a rollout within 2015, not proof of simultaneous January conversion. The paper's
post-year indicator remains a usable reported exposure clock only with that limit.

## Implementation and Assignment

The law assigns eligibility to debt obligations, while the paper assigns research
exposure to loans. Take the lender province's end-2014 debt, log and demean it,
then interact it with borrower private status and the post-2015 period. Compare
private/state pricing gaps along that regional gradient [E4, reported claim].
Neither private ownership nor province debt was randomized. The debt measure is
not the value actually swapped at a branch, and using borrower location would
change the construction.

The matched loan panel uses one bank and 25 provinces; Xinjiang, Tibet and the
four municipalities are outside this application. Firm names link loans to ASIF.
Section 4.2 specifies 2011-2013 averages for leverage, ROA and tangible-asset share
because later firm accounts are unavailable, rather than a continuously observed
firm-outcome panel [E4, reported claim]. The match and ownership dictionary must be
recovered before reproducing the exact sample.

## Why This Creates Empirical Variation

The national policy date alone provides no untreated China. The informative
comparison combines ownership and regional exposure: did the private/state gap
change more in initially more indebted lender provinces? Equation 11 makes those
three dimensions and lower-order terms explicit. Firm and time effects do not
remove an ownership-specific regional shock that coincides with 2015
[E4, reported claim; analytical inference].

Table 4 compares multiple-branch borrowers with firm-by-quarter effects and
uses branch-by-quarter effects in a separate supply-control specification. These
are useful mechanism checks, but not proof that fiscal relief, bond-market
substitution and risk weighting can never operate together. A new research question
should start with the reduced-form ownership-gap estimand, then justify a stronger
channel interpretation with its own holdings and conversion evidence.

## Identification Risks

Initial debt can encode regional size, investment history and distress. The short
annual event study cannot certify counterfactual trends. Provincial exposure and
cross-branch funding also make regional dependence relevant to inference, despite
the reported firm/quarter clustering [E4, reported claim; analytical inference].

Section 4.7 clarifies a particularly important denominator: its POE dummy concerns
whether an **issued loan** goes to a private borrower. Its branch-year measure is
the private share of corporate-loan value. Neither measure observes all firms that
applied, were rejected or never applied. Calling either an all-firm probability of
obtaining credit would distort the recorded knowledge [E4, reported claim].

The matched fast/slow-swap exercise, supplementary spillover checks and local-TFP
IV results are not alternate ready records here. In particular, a strong first
stage for initial debt times post does not establish exclusion from productivity,
and a coefficient of 0.022 on log exposure in a log-TFP equation is not a 2.2%
TFP rise for a 1% debt increase [E4, reported claim; analytical inference]. Preserve
the table's estimand and units rather than repeating those interpretations.

## Data Requirements

Use restricted loan data with actual and benchmark rates, quarter, borrower
ownership and lender geography, plus initial provincial debt and linked baseline
firm accounts. A generic annual listed-firm panel cannot substitute for this
contract. For actual access probabilities, obtain the applicant/rejection risk
set; for a holdings mechanism, obtain branch debt conversion and internal risk
management information. Those are different data demands, not mandatory fields
silently unioned into the main loan-pricing contract.

## Evidence Notes

E1-E3 establish authorization, eligibility and the 2015 rollout. E5 establishes
the public-sector/corporate risk-weight boundary through an official reprint;
its page has later agency wording, so it is not a pristine archival copy of every
2012 provision. E4 is the published article, not the earlier FRBSF working paper.
The author-linked typeset PDF was inspected in memory; no paper or confidential
data are stored here. The main article points to a supplement, but that supplement
and code are outside the inspected evidence boundary. This grounded record is a
conditional research lead with an encodable main contrast, not a turnkey public
replication or a claim that government debt is intrinsically exogenous.
