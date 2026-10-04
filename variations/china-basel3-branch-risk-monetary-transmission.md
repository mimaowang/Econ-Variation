---
schema_version: 2
id: china-basel3-branch-risk-monetary-transmission
name: China’s 2013 Bank Capital Rules, Branch Risk History, and Monetary Policy Transmission
aliases:
- Basel III branch-risk channel in China
- 中国银行资本监管与高不良率分支机构的货币政策传导
- Basel III risk-weighting and Chinese bank lending
status: contested
provenance:
  task_id: task-491c85156c8b
scope:
  country: China
  regions: [Mainland China; branches of one anonymized Big Five bank and its industrial borrowers]
  domains: [finance, firm, monetary-policy, banking-regulation, credit-allocation]
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: A national bank-capital rule applies to Chinese commercial banks. The paper studies whether quarterly monetary-policy shocks change loan ratings differently at branches with higher pre-rule nonperforming-loan histories.
identity:
  instrument: Capital Rules for Commercial Banks (Provisional), CBRC Order No. 1 of 2012, in the paper’s branch-level application interacted with monetary-policy shocks
  authority: China Banking Regulatory Commission; the rules apply to commercial banks established in mainland China
  legal_identifiers: [中国银行业监督管理委员会令〔2012〕第1号, 商业银行资本管理办法（试行）]
  implementation_regime: The common capital rules took effect on 2013-01-01. They raised and reorganized capital requirements and allowed banks to apply for advanced capital-measurement methods. Internal ratings-based credit-risk measurement required regulatory approval. The six-bank approval announced in April 2014 is a distinct implementation clock; it is not evidence that all six banks began using IRB on that announcement date.
  assignment_mechanism: The law does not designate high-risk branches as treated. The paper divides branches according to whether their average pre-2013 NPL ratio is above the sample median, then interacts that indicator with a post-2013 dummy and a quarterly model-estimated monetary-policy shock. This is the paper’s empirical exposure rule, not a statutory branch assignment.
  parent: null
  related_variations: []
timeline:
  announcement: '2012-06-07'
  effective: '2013-01-01'
  implementation_start: 2013
  implementation_end: null
  local_timing: The CBRC order states that the national rules take effect on 2013-01-01. Article 47 makes advanced-method use subject to regulatory approval. A CBRC announcement published on 2014-04-24 says that six named large banks had recently been approved; it does not state the exact approval date for each bank. The paper’s appendix describes 2013Q1–2014Q1 as a period when the new regulation was in force but the banks still used the traditional regulatory-weight approach, with the IRB-based capital-adequacy ratio catching up by mid-2014. Its baseline nevertheless codes Post=1 from 2013. The legal reform date is clear; the timing of the risk-weight mechanism for the anonymized loan bank is not.
  anticipation: The order was announced in June 2012, before its effective date. Banks prepared applications and internal risk-management systems. Treat 2013 as the paper’s annual post indicator, not as a verified date on which the confidential bank began applying IRB to loans.
  last_verified: '2026-09-30'
assignment:
  unit: Loan-firm-branch-quarter observation in one anonymized Big Five bank
  treated: Branches with average NPL ratios above the sample median during the pre-2013 period, exposed to the post-2013 regime and each quarter’s monetary-policy shock
  comparison_pool: Branches with below-median pre-2013 average NPL ratios in the same bank; both groups face the national rules, so the comparison is differential exposure rather than treated versus untreated banks
  rule: RiskH is an indicator for a branch whose average NPL ratio before 2013 is above the sample median. Post equals one from 2013 onward. MP is the paper’s quarterly estimated monetary-policy shock, based on the exogenous component of M2 growth in Chen, Ren, and Zha (2018). The coefficient of interest is RiskH × Post × MP.
  intensity: Binary above-median branch risk history interacted with a continuous quarterly monetary-policy shock; the underlying branch risk measure is pre-2013 average NPL.
  exemptions: [The law applies nationally to mainland commercial banks; advanced capital-measurement methods require bank-level regulatory approval. The paper does not observe an exemption or approval date for its anonymized loan bank.]
  compliance: Loan-level application is confidential and not independently observed here. The paper reports branch risk-weight management under head-office plans, but the branch NPL split is not a measure of actual IRB adoption or compliance.
  exposure_construction: Match confidential loan records to ASIF firms by name where a consistent identifier is unavailable; construct each branch’s pre-2013 average NPL ratio and split at the sample median; merge the quarterly monetary-policy shock; set Post=1 for quarters in 2013 or later. Preserve the paper’s actual sample and eligibility rules if reproducing it. Do not replace the 2013 Post indicator with a claimed bank-specific IRB date unless that date is independently recovered.
  required_identifiers: [Loan record or loan-firm pair identifier, Bank branch identifier, Firm identifier or documented name crosswalk, Quarter, Firm province and industry]
  spillovers: Branch lending and headquarters’ risk-weight plans may shift credit across branches and borrowers. The within-bank contrast does not identify the total nationwide effect of the capital rules, and borrower or branch reallocation may affect the comparison group.
research_compatibility:
  outcome_domains: [Bank lending risk, Credit ratings, Loan pricing and volume, SOE credit allocation, Firm productivity and capital allocation]
  affected_populations: [Manufacturing firms matched to loans from one anonymized Big Five bank, Bank branches observed in the confidential loan panel]
  mechanism_channels: [Capital constraints, Risk-sensitive loan weights, Monetary-policy transmission, Credit supply, Preferential lending to state-owned enterprises]
  best_for: [Studying heterogeneous bank-branch responses to monetary easing around the 2013 capital-rule change, Examining the reported link between bank risk weights and borrower credit allocation]
  not_good_for: [Estimating a standalone national average Basel III effect, Treating branch risk rank as randomly assigned, Treating the 2013 date as verified IRB adoption by the sample bank, Interpreting a high internal loan rating as low realized default risk]
design:
  claim_type: reduced-form
  affordances: [Quarterly confidential loan records, Predetermined branch-risk histories, A national capital-rule effective date, Alternative monetary-shock specifications reported in the appendix]
  candidate_designs: [Triple-interaction difference-in-differences, Branch-risk-specific response to quarterly monetary shocks]
  identifying_variation: Difference in the response of above- versus below-median pre-2013 NPL branches to monetary-policy shocks after the 2013 national capital-rule effective date. The law itself has no untreated Chinese branch group.
  primary_strategy: Loan-level regression of a high-credit-rating indicator on branch risk history, post-2013 exposure, the monetary-policy shock and their interactions, with branch and year-quarter fixed effects and reported firm and industry controls.
  estimand: The differential change after 2013 in the association between a monetary-policy shock and the probability that a loan receives a high internal rating, comparing historically high-NPL and low-NPL branches in the sampled bank. This is not the total causal effect of Basel III, a direct effect of IRB adoption, or an effect on realized loan defaults.
  treatment_variable: RiskH_branch × Post2013 × MP_quarter; HighR equals one for an AA+ or AAA loan rating.
  comparison_logic: Compare high-risk-history and low-risk-history branches within the same bank and compare their differential rating response to quarterly shocks before and after the national rule’s effective date. The common shock level is absorbed by year-quarter fixed effects; the identifying term is heterogeneous branch response.
  estimation_notes: The accessible AEA-hosted article text reports branch, year-quarter, industry and firm-location fixed effects and initial firm characteristics interacted with year effects; the published appendix reports a baseline sample of 206,738 observations and branch-clustered standard errors. More stringent firm-location-by-quarter and industry-by-location-by-quarter controls reduce the reported triple-interaction coefficient from 0.848 to 0.512 and 0.504, respectively. The appendix also reports alternative firm and two-way clustering, interest-rate-rule shocks, and controls for concurrent reforms. These are reported checks, not an independent replication.
  assumptions:
  - In the absence of the capital-rule change, high- and low-risk branches would have maintained comparable responses to monetary-policy shocks, conditional on the stated fixed effects and controls.
  - The model-derived monetary-policy shock is not correlated with an omitted contemporaneous shock that changes high-risk branches’ lending differently after 2013.
  - Pre-2013 branch NPL histories capture differential exposure to the rule rather than persistent local borrower risk, branch management, or demand changes that also alter shock responses.
  - The timing of the paper’s post-2013 contrast corresponds closely enough to the relevant capital constraint for the intended mechanism; this is unresolved for IRB and is why this record remains contested.
  diagnostics:
  - Inspect the reported branch-risk-by-shock event coefficients with 2012 as the reference, including the pre-2011 and 2011 coefficients; their lack of significance is not proof of parallel counterfactual responses.
  - Reproduce the baseline with the final article’s code and restricted data, then compare branch, firm, and two-way clustering.
  - Report how the triple interaction changes with firm-location-by-quarter and more saturated demand controls; the published appendix shows attenuation.
  - Re-estimate with the reported 30-day Shibor and pledged-repo Taylor-rule residuals, preserving their opposite easing sign convention relative to the quantity-based shock.
  - Recover the sampled bank’s IRB approval and actual-use dates before labeling post-2013 coefficients as effects of risk-sensitive IRB weights.
  - Separate loan-rating outcomes from overdue/default outcomes and check the stability of the rating measure over time.
threats:
- type: capital-rule-versus-irb-clock
  basis: documented
  condition: The national Capital Rules took effect in 2013, but Article 47 requires regulatory approval for advanced methods, the CBRC publicly reported six large-bank approvals in 2014, and the paper’s own figure note says banks still used traditional regulatory weights through 2014Q1. The anonymous loan bank’s actual IRB-use date is unknown. The 2013 post indicator therefore cannot by itself establish that its branch-level IRB risk-weight channel was active from the first post quarter.
  evidence_refs: [E1, E2, E3, E5, E6]
  possible_diagnostics: [Identify the sample bank and its approval/use dates, Use a bank-specific adoption date only if documented, Re-estimate excluding the transition period, Distinguish common capital-rule effects from the advanced-method mechanism]
- type: endogenous-branch-risk-history
  basis: documented
  condition: The above-median NPL group is formed from realized pre-period branch outcomes, not regulatory assignment. Local borrower composition, branch management, and persistent credit conditions may predict later responses to monetary shocks.
  evidence_refs: [E5, E6]
  possible_diagnostics: [Inspect pre-period differential shock responses, Use the reported alternative pre-period loan-rating measure, Test sensitivity to initial SOE lending and branch characteristics, Avoid treating a median split as random assignment]
- type: model-derived-monetary-shock
  basis: reported
  condition: The baseline M2 shock is estimated from a regime-switching model cited to Chen, Ren, and Zha (2018); the appendix also uses Taylor-rule residuals from Shibor or repo rates. The shocks are not externally randomized and their validity is not independently verified here.
  evidence_refs: [E5, E6]
  possible_diagnostics: [Reconstruct the shock series and sign, Compare quantity and price measures, Check sensitivity to monetary-regime specification, Keep common macro shocks and branch-specific responses distinct]
- type: rating-is-not-default
  basis: documented
  condition: HighR is an AA+ or AAA internal credit-rating indicator. The appendix reports that firm ratings rarely change. A higher rating measures the bank’s assessment and does not establish lower realized default risk; the paper separately studies overdue and nonperforming outcomes.
  evidence_refs: [E5, E6]
  possible_diagnostics: [Use realized overdue/default outcomes where legally available, Report rating stability, Separate ex ante ratings from ex post repayment performance]
- type: confidential-sample-and-name-linkage
  basis: reported
  condition: The loan panel comes from one unnamed Big Five bank and is confidential. The paper reports name-based matching to ASIF where consistent firm identifiers are absent. ASIF coverage thresholds also change over time, so the matched sample is not a census of all borrowers or firms.
  evidence_refs: [E5, E7]
  possible_diagnostics: [Document lawful data access, Audit name-matching precision, Preserve ASIF threshold changes, Report unmatched and changing-coverage samples]
- type: concurrent-policy-and-credit-demand
  basis: documented
  condition: Interest-rate liberalization, the 2012–2013 anti-corruption campaign, and later deleveraging overlap parts of the study window. The appendix reports controls and a deleveraging placebo, but these do not rule out all correlated changes in borrower demand or local credit conditions.
  evidence_refs: [E5, E6]
  possible_diagnostics: [Reproduce the published concurrent-policy checks, Add borrower-by-quarter comparisons where multiple-branch borrowers permit, Retain the smaller and selected sample implied by those comparisons]
empirical_requirements:
  contract_version: 1
  population: Firms in the confidential manufacturing-loan records from one unnamed Big Five bank matched to China’s Annual Survey of Industrial Firms for firm characteristics; the paper reports about 330,000 unique firm-loan pairs over 2008Q1–2017Q4 and 206,738 observations in the published baseline table.
  observation_unit: Loan-firm-branch-quarter
  geography_level: Bank branch and borrower province
  time_start: 2008
  time_end: 2017
  minimum_frequency: quarterly
  minimum_pre_periods: 20
  minimum_post_periods: 20
  required_fields: [Loan rating, Loan amount and rate, Branch-level NPL history before 2013, Bank branch, Firm identity, Firm province and industry, Firm ownership, Quarterly monetary-policy shock, Post-2013 indicator, ASIF baseline firm characteristics]
  required_identifiers: [Loan or loan-firm pair key, Bank branch ID, Stable firm ID or auditable firm-name crosswalk, Quarter, Firm location and industry codes]
  treatment_key: [Above-median pre-2013 branch NPL indicator, Post2013, Quarterly monetary-policy shock]
  treatment_source: Capital Rules for Commercial Banks establish the national effective date; paper-reported confidential branch and loan data plus the cited monetary-shock construction establish the empirical exposure. The statute does not supply branch treatment labels.
  measurement_risks: [Confidential and unnamed bank, Name-based match to ASIF, ASIF eligibility thresholds change, Internal ratings may not proxy realized default, Above-median split depends on the sample, Shock estimates need reconstruction, Bank-specific advanced-method timing is unresolved]
evidence:
- id: E1
  source_type: policy-document
  citation: China Banking Regulatory Commission. 商业银行资本管理办法（试行）, CBRC Order No. 1 of 2012, issued 2012-06-07, effective 2013-01-01.
  url: https://www.moj.gov.cn/pub/sfbgw/flfggz/flfggzbmgz/201305/t20130528_145313.html
  date: '2012-06-07'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, identity.assignment_mechanism, timeline.announcement, timeline.effective, timeline.local_timing, assignment.rule, assignment.exemptions, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: MOJ-hosted full regulation inspected2026-09-29 and2026-09-30. Header identifies CBRC Order No.1, issued2012-06-07 and effective2013-01-01. Article2 applies to commercial banks established in China. Article47 makes IRB capital measurement subject to regulatory approval and phased coverage thresholds; Article48 refers to the internal-rating requirements. Website posting date is not the legal issue date.
- id: E2
  source_type: implementation-document
  citation: State Council portal reproducing CBRC announcement, 银监会发布《商业银行资本管理办法（试行）》, 2012-06-08.
  url: https://www.gov.cn/gzdt/2012-06/08/content_2156784.htm
  date: '2012-06-08'
  supports: [identity.implementation_regime, timeline.announcement, timeline.effective]
  verification_status: verified
  access_level: official-document
  locator: Government portal text attributes the announcement to CBRC, states publication on2012-06-08 and implementation from2013-01-01, and explains the phased capital-requirement structure. This supports the national announcement and effective date, not branch-level exposure.
- id: E3
  source_type: implementation-document
  citation: China Banking Regulatory Commission. 银监会核准六家银行实施资本管理高级方法 and accompanying Q&A, 2014-04-24; reproduced by People's Daily Finance with source attributed to CBRC website.
  url: http://finance.people.com.cn/bank/n/2014/0424/c202331-24939243.html
  date: '2014-04-24'
  supports: [identity.implementation_regime, timeline.local_timing, assignment.exemptions, threats.condition]
  verification_status: reported
  access_level: official-document
  locator: Inspected the complete reproduced CBRC Q&A2026-09-29 and2026-09-30. It says the Capital Rules had been effective since2013-01-01, advanced methods require supervisory approval, and six named banks including the Big Five were recently approved. The article date is not represented as each bank’s exact approval date or first operational-use date.
- id: E4
  source_type: scholarship
  citation: 'American Economic Association, article page and issue metadata for Li, Liu, Peng, and Xu, “Bank Risk-Taking, Credit Allocation, and Monetary Policy Transmission: Evidence from China,” American Economic Journal: Macroeconomics18(1), January2026, pp.384–415.'
  url: https://doi.org/10.1257/mac.20220177
  date: 2026
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: AEA article page and issue record inspected2026-09-30; DOI, title, authors, journal, volume, issue, pages and January2026 publication metadata agree.
- id: E5
  source_type: paper
  citation: 'Li, Xiaoming, Zheng Liu, Yuchao Peng, and Zhiwei Xu. 2026. “Bank Risk-Taking, Credit Allocation, and Monetary Policy Transmission: Evidence from China.” AEA-hosted full-text article PDF associated with DOI10.1257/mac.20220177.'
  url: https://www.aeaweb.org/content/file?id=23127
  date: '2026-09-30'
  supports: [scope.china_relevance, identity.implementation_regime, identity.assignment_mechanism, timeline.local_timing, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.intensity, assignment.compliance, assignment.exposure_construction, assignment.spillovers, research_compatibility.outcome_domains, research_compatibility.affected_populations, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, design.assumptions, design.diagnostics, threats.condition, empirical_requirements.population, empirical_requirements.required_fields, empirical_requirements.required_identifiers, empirical_requirements.treatment_key, empirical_requirements.measurement_risks, design_applications.research_question, design_applications.population, design_applications.outcome, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison]
  verification_status: reported
  access_level: full-text
  locator: AEA-hosted article PDF inspected2026-09-30, pp.2–3 for loan and ASIF data, matched period and monetary-shock description; printed pp.14–20 for equation23, branch-risk/post/shock interaction, outcome, fixed effects, and reported dynamic comparison; pp.34–37 for Appendix A’s regulatory narrative and figure note. Its running headers retain unfilled volume/month placeholders, so the final issue identity is supported separately by E4. Article application and estimates are source-reported, not independently replicated.
- id: E6
  source_type: appendix
  citation: 'Li, Xiaoming, Zheng Liu, Yuchao Peng, and Zhiwei Xu. Online Appendix for “Bank Risk-Taking, Credit Allocation, and Monetary Policy Transmission: Evidence from China,” published with AEJ: Macroeconomics18(1), 2026.'
  url: https://www.aeaweb.org/articles/materials/24386
  date: 2026
  supports: [timeline.local_timing, assignment.rule, assignment.exposure_construction, design.estimation_notes, design.diagnostics, threats.condition, empirical_requirements.population, empirical_requirements.measurement_risks]
  verification_status: reported
  access_level: appendix
  locator: AEA-hosted30-page appendix downloaded and inspected in memory2026-09-30. TablesB.1–B.4 report alternative clustering, increasingly saturated loan-demand controls, Shibor/repo monetary shocks, and interest-rate-liberalization controls; TableB.2 triple-interaction estimates fall from0.848 to0.512/0.504 with more saturated controls. Pages1–5 define the outcome and shock alternatives. These robustness results do not identify the anonymized bank’s IRB start date.
- id: E7
  source_type: replication
  citation: 'Li, Xiaoming, Zheng Liu, Yuchao Peng, and Zhiwei Xu. Data and Code for “Bank Risk-Taking, Credit Allocation, and Monetary Policy Transmission: Evidence from China,” openICPSR231821V1, published2025-12-05.'
  url: https://www.openicpsr.org/openicpsr/project/231821/version/V1/view
  date: '2025-12-05'
  supports: [empirical_requirements.measurement_risks]
  verification_status: blocked
  access_level: metadata
  locator: V1 landing page and directory inventory inspected2026-09-29. README retrieval returned HTTP403; no code, input data, bank identity, or replication output was inspected. Inventory is not evidence that confidential loan data or a runnable reproduction are available.
design_applications:
- paper: 'Li, Liu, Peng, and Xu, Bank Risk-Taking, Credit Allocation, and Monetary Policy Transmission: Evidence from China'
  doi: 10.1257/mac.20220177
  journal: 'American Economic Journal: Macroeconomics'
  year: 2026
  research_question: How do monetary-policy shocks change bank risk-taking and credit allocation after China’s new capital rules, and do responses differ by branches’ prior NPL histories?
  population: Manufacturing firms matched to loan-level records from one anonymized Big Five commercial bank
  outcome: Whether an individual loan has an AA+ or AAA bank credit rating; related reported applications examine loan prices and volumes, SOE lending, and productivity
  data_used: [Confidential bank loan records, China Annual Survey of Industrial Firms for firm characteristics through2013, Listed-bank data for a separate bank-level application]
  treatment_encoding: Above-median branch average NPL before2013 × indicator(year>=2013) × quarterly M2 monetary-policy shock estimated following Chen, Ren, and Zha (2018). The bank-level six-versus-six IRB comparison is a different application and is not merged into this record.
  comparison: Higher- versus lower-pre-2013-NPL branches within one bank, before and after2013, comparing their differential responses to a common quarterly shock
  empirical_design: Loan-level triple-interaction reduced-form regression with branch, year-quarter, industry and firm-location controls as described in the article; published appendix reports alternative clustering and demand controls
  assumptions: [Comparable pre/post shock responses absent the capital-rule change, Predetermined branch risk history is not proxying for changing local demand, Model-derived monetary shocks are valid for the heterogeneous-response contrast, The 2013 post period aligns with the mechanism under study]
  threats_addressed: [Reported dynamic response comparison, Alternative shock measures, More saturated borrower-location demand controls, Controls for interest-rate liberalization and anti-corruption, Deleveraging placebo]
  evidence_refs: [E1, E2, E3, E4, E5, E6, E7]
method_transfer: null
readiness_blockers:
- The 2013 effective date of the common capital rules is verified, but the advanced-method/IRB mechanism is not aligned to that date. The official approval announcement names the Big Five in2014; the article itself reports traditional risk weights through2014Q1. Because the confidential sample bank is unnamed, its approval and actual-use dates cannot be matched. Do not recommend the estimated triple interaction as a clean IRB adoption effect until this timing is reconciled.
- The public replication README and loan data were not accessible in this pass. A researcher needs lawful access, documented branch and firm linkage, and shock construction inputs before reproducing the estimate.
- The branch high-risk indicator is an endogenous pre-period rank and the monetary-policy shock is model-derived. Use the record as a conditional research lead, not as a claim that either source of variation is intrinsically exogenous.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

The CBRC’s Capital Rules for Commercial Banks were issued on 7 June 2012 and took effect on 1 January 2013. They apply to commercial banks established in China and combine minimum capital requirements with rules for calculating risk-weighted assets [E1; E2]. This national date is independently verifiable. It is not a staggered branch rollout.

The rules also permit advanced capital-measurement methods, including internal ratings-based measurement of credit risk, subject to regulatory approval [E1]. In April 2014 the CBRC announced that six large banks, including the Big Five, had recently been approved to implement advanced methods [E3]. The announcement gives the public reporting date, not each bank’s approval or operational start date.

## What Changed

Li, Liu, Peng, and Xu study one unnamed Big Five bank. Their main loan-level comparison classifies branches by whether their average NPL ratio before 2013 is above the sample median. They interact that high-risk indicator with a post-2013 dummy and quarterly monetary-policy shocks constructed from the model-based component of M2 growth [E5, reported claim]. The statutory reform is common to the bank; branch risk history creates the cross-sectional exposure used in the paper.

The dependent variable is whether a loan has an AA+ or AAA internal rating. The paper interprets this as risk-taking, but it is a lender assessment rather than a realized default measure [E5, reported claim]. A positive M2 shock denotes easing in the quantity-based construction. The coefficient therefore describes how the rating response to monetary easing differs for high-risk-history branches after 2013; it is not a standalone effect of the law.

## Implementation and Assignment

The paper’s legal timeline and its proposed risk-weighting mechanism do not line up cleanly. The national rules began in 2013, but advanced methods required approval. The CBRC announced approval of the Big Five and China Merchants Bank in 2014, while the article’s Appendix A says its shaded 2013Q1–2014Q1 period is when the regulation was in force but banks still used traditional regulatory weights; the IRB-based capital ratio caught up by mid-2014 [E1; E3; E5]. The confidential loan bank is not named, so its actual transition cannot be checked.

That distinction matters for interpretation. The published post indicator starts in 2013, and its estimates can still describe heterogeneous responses under the new national capital regime. The evidence available here does not establish that the high-risk branches faced the paper’s proposed IRB risk-weight mechanism from the first post quarter [analytical inference]. Keep the legal reform date, paper-coded post period, and bank-specific advanced-method use as separate clocks.

## Why This Creates Empirical Variation

The national regulation and monetary shocks are common across the sampled bank’s branches. The paper obtains a differential response by comparing branch lending according to pre-2013 NPL history, before and after the regulation, and across quarterly shocks. This interaction can support a conditional heterogeneous-response estimate if high- and low-risk branches would otherwise have responded similarly to those shocks. It does not create an untreated branch group or identify the national average effect of the law [E5, reported claim; analytical inference].

## Identification Risks

The NPL median split is based on realized branch outcomes and may capture persistent differences in borrowers, management, or local demand. The monetary-policy shock is model-derived. The paper reports pre-period response checks and alternative shock measures, but those do not establish random assignment or independently verify the shock series [E5; E6, reported claim]. The 2013 post date also includes a transition period before advanced-method approval and use can be matched to the anonymized loan bank [E1; E3; E5].

The high-rating outcome is a lender assessment rather than default. Concurrent interest-rate liberalization and other reforms overlap the sample. The published appendix addresses selected concerns with richer demand controls and policy checks; these exercises reduce some competing explanations without eliminating all of them [E5; E6, reported claim].

## Data Requirements

The paper reports approximately 330,000 unique firm-loan pairs over 2008Q1–2017Q4 after matching one bank’s confidential loan data to ASIF firm records. It uses firm names where a consistent company identifier is unavailable. The published appendix reports 206,738 observations in the baseline specification and shows that the triple-interaction coefficient declines as loan-demand controls become more saturated [E5; E6, reported claim]. ASIF firm characteristics end in 2013 and its coverage thresholds change over time; they do not provide contemporaneous post-2013 accounts for every loan borrower.

The published checks include branch-risk event coefficients relative to 2012, alternative clustering, more saturated location-by-quarter controls, alternative Shibor and repo shock measures, controls for interest-rate liberalization and anti-corruption, and a deleveraging placebo [E5; E6, reported claim]. They do not identify the anonymous bank’s IRB start date, independently validate the model-derived monetary shock, or make the median split random [analytical inference].

## Evidence Notes

This source can guide research on monetary transmission, bank lending, and credit allocation in China when confidential loan-level data and a defensible branch-firm join are available. Treat the result as a conditional heterogeneous-response design. A new application should recover the bank’s actual approval and use dates, reproduce the shock series, and distinguish internal ratings from realized repayment outcomes. Without those steps, the record is an audit lead rather than a ready-to-use IRB adoption design.
