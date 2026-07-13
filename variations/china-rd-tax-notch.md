---
schema_version: 2
id: china-rd-tax-notch
name: Notched Corporate Income Tax Cuts at the R&D Intensity Threshold for High and New Technology Enterprises in China (2006–2011)
aliases:
- Chen-Liu-Suárez Serrato-Xu R&D notch
- HNTE tax notch
- High and New Technology Enterprise notch
- InnoCom program R&D bunching
- 高新技术企业研发税收优惠
- 国科发火2008-172号

status: grounded
provenance:
  task_id: task-9beb75f420fc
scope:
  country: China
  regions:
  - All provinces
  - with concentration in coastal and high-tech industrial regions
  domains:
  - innovation
  - industrial-policy
  - tax
  - firm-behavior
  - public-economics
  - productivity
  variation_type: eligibility-threshold
  knowledge_role: china-variation
  china_relevance: The HNTE certification program is a Chinese central-government industrial policy that creates a discontinuous
    corporate income tax reduction (from 25% to 15%, and from 33% to 15% before 2008) at size-dependent R&D intensity thresholds
    (3%, 4%, or 6%) for Chinese manufacturing and technology firms. The policy was implemented nationally from January 2008
    under 国科发火〔2008〕172号, jointly administered by MOST, MOF, and SAT. The notch structure generates quasi-experimental
    variation in R&D investment incentives that has been used to estimate the elasticity of reported and real R&D to tax incentives,
    to separate relabeling from genuine innovation responses, and to quantify the productivity returns to R&D. The identification
    strategy relies on bunching at the notched thresholds, validated by the absence of bunching before the 2008 reform when
    a uniform 5% threshold applied under the predecessor InnoCom program.
identity:
  instrument: The High and New Technology Enterprise (HNTE, also called InnoCom) certification program creates a notched corporate
    income tax schedule. Under 国科发火〔2008〕172号 (effective 2008-01-01), firms whose R&D expenditure-to-sales-revenue ratio
    exceeds a size-dependent regulatory threshold (3%, 4%, or 6%) qualify for a preferential 15% corporate income tax rate
    (vs. the standard 25%). Before 2008, the predecessor InnoCom program applied a uniform 5% R&D intensity threshold with
    a tax rate reduction from 33% to 15%. The 2008 reform changed the threshold from a uniform 5% to size-dependent notches
    and simultaneously reduced the standard CIT rate from 33% to 25%, creating a plausibly exogenous shift in the location
    and structure of the R&D incentive notch.
  authority: Ministry of Science and Technology (MOST), Ministry of Finance (MOF), State Administration of Taxation (SAT);
    provincial-level certification bodies and tax authorities handle applications and enforcement
  legal_identifiers:
  - 国科发火〔2008〕172号《高新技术企业认定管理办法》(April 14, 2008, effective retroactively January 1, 2008; repealed
    January 1, 2016 by 国科发火〔2016〕32号)
  - 《中华人民共和国企业所得税法》Article 28 (2008 Enterprise Income Tax Law, effective January 1, 2008)
  - 《中华人民共和国企业所得税法实施条例》(Implementing Regulations of the EIT Law)
  - 国科发火〔2016〕32号 (2016 revision, lowered lowest-tier threshold from 6% to 5%)
  implementation_regime: Starting January 1, 2008, the HNTE program grants certified firms a preferential 15% corporate income
    tax rate if their R&D expenditure as a share of sales revenue exceeds a size-dependent threshold — 3% for firms with annual
    sales above RMB 200 million, 4% for firms with sales between RMB 50 million and RMB 200 million, and 6% for firms with
    sales below RMB 50 million. At least 60% of R&D expenditure must be incurred within China. Certification requires meeting
    five additional criteria (IP ownership, high-tech field scope, personnel composition with ≥30% college-educated and ≥10%
    R&D staff, ≥60% high-tech product revenue, and a composite innovation score ≥71/100). Certification is valid for three
    years and must be renewed. Before 2008, the predecessor InnoCom program applied a uniform 5% threshold with a 33% → 15%
    tax rate reduction.
  assignment_mechanism: A firm's eligibility for the 15% preferential tax rate is determined by whether its R&D intensity
    (total R&D expenditure over the prior three fiscal years / total sales revenue over the same period) exceeds the size-dependent
    regulatory threshold, conditional on meeting the other five certification criteria. The notch creates a discontinuous jump
    in the after-tax return to R&D at the threshold. The 2008 reform changed both the location of the notch (from uniform
    5% to size-dependent 3%/4%/6%) and the standard tax rate (from 33% to 25%), generating variation in the incentive to bunch
    that is used to identify behavioral responses.
  parent: null
  related_variations:
  - china-vat-reform-investment
timeline:
  announcement: '2008-04-14'
  effective: '2008-01-01'
  implementation_start: 2008
  implementation_end: 2011
  local_timing: The HNTE program was implemented nationally from January 1, 2008. Local tax authorities and provincial certification
    bodies processed applications with some variation in administrative speed, and some firms received retroactive certification,
    but the policy parameters (thresholds, tax rate, certification criteria) were uniform nationwide. The predecessor InnoCom
    program with a uniform 5% threshold operated before 2008, providing a pre-reform baseline for the paper's identification.
    The paper's study period ends in 2011 due to data availability, though the policy continued (with the 2016 revision lowering
    the lowest tier to 5%).
  anticipation: The 2008 Enterprise Income Tax Law reform was announced in advance (passed March 2007, effective January 2008).
    Firms may have adjusted R&D reporting in anticipation. The paper uses 2006–2007 ASM data as a pre-reform baseline and
    validates identification by showing no bunching at the post-2008 thresholds in the pre-reform period.
  last_verified: '2026-07-13'
assignment:
  unit: Firm (manufacturing and technology firms)
  treated: Firms whose R&D intensity (three-year average R&D expenditure / sales revenue) exceeds the size-dependent HNTE
    certification threshold — 3% for firms with annual sales > RMB 200 million, 4% for sales RMB 50–200 million, or 6% for
    sales < RMB 50 million — entitling them to the 15% preferential CIT rate upon certification
  comparison_pool: Firms with R&D intensity just below their size-dependent threshold; firms before vs. after certification;
    firms in the pre-reform period (2006–2007) when the uniform 5% threshold applied under different rate parameters (33%
    → 15%); firms that lose certification at three-year renewal
  rule: A firm qualifies for the 15% preferential tax rate if its R&D-to-sales ratio (three-year rolling average) meets or
    exceeds the size-dependent threshold, AND it satisfies five additional criteria (IP ownership, high-tech field scope,
    ≥30% college-educated staff, ≥10% R&D staff, ≥60% high-tech product revenue, composite innovation score ≥71/100). The
    R&D threshold creates a notch in the effective tax schedule — firms just below pay the standard 25% rate; firms just above
    pay 15%.
  intensity: Binary at the certification level (certified vs. not), but the effective tax saving is proportional to firm
    profitability. The notch creates a discontinuous jump in the marginal benefit of incremental R&D at the threshold — the
    incentive is strongest for firms close to the threshold.
  exemptions: []
  compliance: Firms have incentives to inflate reported R&D to meet the threshold. Under Chinese Accounting Standards, R&D
    expenditure is a subcategory of "Administrative Expenses" (管理费用), which allows the paper to detect relabeling — if
    firms reclassify non-R&D administrative expenses as R&D, non-R&D administrative expenses should drop sharply at the notch.
    Certification audits by local authorities are imperfect; the paper documents that some firms lose certification at the
    three-year renewal, creating additional within-firm variation.
  exposure_construction: Compute each firm's R&D intensity as the ratio of total R&D expenditure to total sales revenue (three-year
    average per the regulation). Assign firms to size-dependent threshold bins based on annual sales revenue. Code firms as
    treated (above threshold) or control (below threshold). For the bunching design, use R&D intensity as the running variable
    and estimate excess mass at each threshold relative to a smooth counterfactual density estimated from parts of the distribution
    away from the notch. Use pre-2008 data (uniform 5% threshold) to validate that bunching appears only after the 2008 reform.
  required_identifiers:
  - firm ID
  - year
  - R&D expenditure
  - sales revenue
  - R&D intensity
  - industry code
  - firm size (sales revenue bin)
  - corporate income tax paid
  - effective tax rate
  - HNTE certification status
  spillovers: HNTE certification may affect non-certified competitors in the same industry through product market competition;
    certified firms may attract R&D workers from non-certified firms; general equilibrium effects on the returns to R&D may
    shift the counterfactual distribution
research_compatibility:
  outcome_domains:
  - reported R&D expenditure
  - real R&D investment
  - relabeling of non-R&D expenses as R&D
  - total factor productivity
  - innovation output (patents)
  - firm profitability
  - corporate tax revenue
  - resource allocation
  affected_populations:
  - manufacturing firms
  - technology firms
  - R&D-performing firms near the certification thresholds
  - R&D workers
  mechanism_channels:
  - tax incentive for incremental R&D (notch increases after-tax return at threshold)
  - relabeling of non-R&D administrative expenses as R&D to meet the threshold
  - extensive vs. intensive margin R&D response
  - firm selection into certification (and exit at renewal)
  - productivity returns to real R&D investment
  best_for:
  - Estimating the elasticity of reported and real R&D to tax incentives
  - Bunching designs at notched policy thresholds
  - Quantifying real vs. reporting responses to tax policy
  - Studying the productivity returns to R&D investment
  - Welfare analysis of R&D tax incentives accounting for relabeling
  not_good_for:
  - Firms far from the certification thresholds (no first-stage incentive)
  - Non-manufacturing or service-sector R&D (different accounting and threshold structure)
  - General equilibrium effects of innovation policy (partial equilibrium analysis)
  - Post-2011 outcomes without extending the tax data panel
design:
  claim_type: causal
  affordances:
  - size-dependent R&D intensity notches (3%, 4%, 6%) creating sharp discontinuities in tax incentives
  - 2008 reform changed threshold structure from uniform 5% to size-dependent notches — pre-reform period serves as placebo
  - R&D is a subcategory of Administrative Expenses under Chinese Accounting Standards — enables relabeling detection via
    non-R&D admin expense analysis
  - three-year certification renewal creates within-firm variation
  - rich administrative tax data with detailed cost breakdowns
  candidate_designs:
  - bunching estimation at each size-dependent R&D notch
  - pre-2008 vs. post-2008 comparison (uniform 5% → size-dependent 3%/4%/6%)
  - structural estimation via Simulated Method of Moments separating real and reporting responses
  - Diamond-Persson (2016) estimator for treatment effects on firms in the bunching region
  - difference-in-differences around certification and decertification events
  identifying_variation: The 2008 Enterprise Income Tax Law reform changed the R&D intensity threshold from a uniform 5%
    (under the predecessor InnoCom program, with a 33% → 15% tax rate reduction) to size-dependent notches at 3%, 4%, and
    6% (with a 25% → 15% rate reduction). Firms facing the post-2008 notch have a strong incentive to increase reported R&D
    intensity to cross the threshold — observed as excess bunching at each cutoff. The identifying assumption is that the
    counterfactual distribution of R&D intensity would be smooth in the absence of the notch. The pre-2008 absence of bunching
    at the post-2008 threshold locations validates that the bunching is caused by the reform rather than by other factors.
  primary_strategy: Bunching estimation (Kleven-Waseem 2013, Saez 2010) at each size-dependent R&D notch, combined with a
    structural model of firm R&D investment and relabeling decisions estimated via Simulated Method of Moments. The bunching
    estimator measures excess mass at each threshold relative to a smooth counterfactual density. The structural model separately
    identifies the real R&D elasticity and the relabeling share by matching moments from the bunching pattern, the drop in
    non-R&D administrative expenses at the notch, and the joint distribution of R&D and productivity.
  estimand: The causal effect of the notched R&D tax incentive on reported R&D expenditure (bunching estimate); the elasticity
    of real R&D investment with respect to the user cost of R&D; the share of reported R&D attributable to relabeling of
    non-R&D expenses; the causal effect of real R&D on firm TFP (structural parameter); all identified under the smooth counterfactual
    assumption and the structural model's exclusion restrictions
  treatment_variable: Indicator for whether firm R&D intensity exceeds the size-dependent HNTE threshold; R&D intensity as
    the running variable; size bin indicators for the 3%, 4%, and 6% thresholds
  comparison_logic: Firms with R&D intensity just above vs. just below each size-dependent threshold (bunching counterfactual);
    firms in 2006–2007 (pre-reform, uniform 5% threshold) vs. 2008–2011 (post-reform, size-dependent thresholds); firms before
    vs. after certification and firms that maintain vs. lose certification at renewal
  estimation_notes: The bunching estimator fits a flexible polynomial to the R&D intensity distribution excluding a window
    around each notch, then measures excess mass as the difference between observed and counterfactual density. The structural
    SMM model adds heterogeneous firm productivity, R&D adjustment costs, fixed certification costs, and a relabeling technology. Key structural parameters — productivity elasticity of R&D and relabeling cost — are identified from the bunching
    magnitude, the non-R&D admin expense drop, and the R&D-productivity joint distribution. Pre-2008 data validates the identification
    by confirming no bunching at the post-2008 thresholds before the reform.
  assumptions:
  - The counterfactual distribution of R&D intensity would be smooth at each threshold in the absence of the notch
  - Firms cannot perfectly manipulate R&D intensity costlessly; real and reporting adjustments involve distinct costs
  - The 2008 reform did not coincide with other policy changes creating discontinuities at the same R&D intensity levels
  - non-R&D administrative expenses respond to relabeling but not to real R&D changes at the threshold (exclusion restriction
    for the structural decomposition)
  - The productivity process is exogenous to the certification decision conditional on the structural model's state variables
  diagnostics:
  - verify no bunching at post-2008 threshold locations in 2006–2007 data (pre-2008 placebo)
  - density test for manipulation of the running variable (McCrary-type test adapted for bunching)
  - test for sharp drop in non-R&D administrative expenses at each notch (relabeling signature)
  - robustness to bunching window width, polynomial order, and excluded region around the notch
  - placebo thresholds at alternative R&D intensity levels
  - exclude state-owned enterprises, extensive-margin entrants, and firms receiving other R&D subsidies
  - compare results across size bins (3%, 4%, 6% thresholds)
  - compare model-predicted moments to data moments (structural model fit)
threats:
- type: manipulation-of-running-variable
  basis: documented
  condition: Firms may manipulate reported R&D expenditure through relabeling of non-R&D administrative expenses to cross
    the certification threshold. This is the central identification challenge — it biases the estimated real R&D response
    upward if not accounted for. The paper uses the non-R&D admin expense drop at the notch to detect and quantify relabeling,
    and the structural model separates real from reporting responses.
  evidence_refs:
  - E2
  possible_diagnostics:
  - test for excess bunching at each threshold using density tests
  - examine non-R&D administrative expenses for a compensating drop at the notch
  - use administrative audit data to detect relabeling
  - compare reported R&D with alternative innovation measures (patents, new products)
  - implement structural model that separately identifies real and reporting responses
  - verify no bunching in pre-2008 data
- type: selection-bias
  basis: inferred
  condition: Firms that choose to certify may differ systematically from non-certified firms on unobserved dimensions (e.g.,
    productivity trends, management quality). Simple comparisons of certified vs. non-certified firms are confounded by selection.
    The bunching design mitigates this by comparing firms just above and just below the threshold, who are similar in observables.
  evidence_refs:
  - E2
  possible_diagnostics:
  - compare firm characteristics in narrow windows around each threshold
  - use firm fixed effects in panel specifications
  - leverage certification renewal (firms that lose vs. maintain certification) for within-firm variation
  - Diamond-Persson estimator comparing outcomes in the bunching region to counterfactual
- type: concurrent-policies
  basis: inferred
  condition: Other innovation policies (patent subsidies, government R&D grants, high-tech zone incentives, R&D super-deduction
    of 150%) implemented during the same period may affect R&D investment independently of the HNTE notch. The R&D super-deduction
    policy is particularly relevant because the lower HNTE tax rate (15%) reduces the value of the deduction compared to
    the standard 25% rate — creating a countervailing incentive.
  evidence_refs:
  - E2
  possible_diagnostics:
  - control for other policy interventions in robustness checks
  - restrict sample to firms not receiving other R&D subsidies
  - exploit the fact that concurrent policies do not create discontinuities at the exact HNTE thresholds
  - examine geographic variation in other policy exposures
- type: attrition-and-sample-selection
  basis: inferred
  condition: The paper links ASM data (2006–2007) with SAT administrative tax data (2008–2011). Sample composition changes
    across these two data sources, and firm entry/exit may correlate with R&D intensity. The SAT data covers a broader set
    of firms than the ASM, and the linking process may introduce selection.
  evidence_refs:
  - E2
  possible_diagnostics:
  - compare firm characteristics across the two data sources
  - restrict analysis to firms observed in both periods
  - examine extensive-margin vs. intensive-margin responses separately
  - test sensitivity to excluding entrants and exiters
empirical_requirements:
  contract_version: 1
  population: Chinese manufacturing and technology firms in the SAT administrative corporate income tax records (2008–2011)
    and the NBS Annual Survey of Manufacturing (2006–2007), approximately 300,000 firm-year observations per year
  observation_unit: Firm-year
  geography_level: Firm location (city/prefecture)
  time_start: 2006
  time_end: 2011
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 3
  required_fields:
  - firm ID
  - year
  - R&D expenditure (three-year total)
  - sales revenue (three-year total)
  - R&D intensity
  - non-R&D administrative expenses
  - industry code (4-digit CIC)
  - firm size (sales revenue bin for threshold assignment)
  - corporate income tax paid
  - effective tax rate
  - HNTE certification status
  - total factor productivity
  - patents (for validation)
  - ownership type (state-owned, private, foreign)
  required_identifiers:
  - firm ID
  - year
  - industry
  treatment_key:
  - R&D intensity relative to size-dependent regulatory threshold
  - HNTE certification indicator
  - size bin (sales < 50M / 50M–200M / > 200M)
  treatment_source: SAT administrative corporate income tax records (2008–2011) for firm-level financials, R&D expenditure,
    tax payments, and cost breakdowns; NBS Annual Survey of Manufacturing (2006–2007) for pre-reform firm data; MOST HNTE
    certification lists for certification status; State Intellectual Property Office for patent data
  measurement_risks:
  - R&D expenditure in the SAT data may be inflated for tax purposes, introducing measurement error in the running variable
  - non-R&D administrative expenses may include items that are genuinely reclassified for non-tax reasons
  - certification status from administrative lists may not perfectly match the timing of tax rate changes (retroactive certification)
  - linking ASM and SAT data across 2007–2008 may introduce match errors
  - firm ownership changes, mergers, and restructuring during the sample period may affect R&D reporting continuity
  - the three-year averaging rule means reported R&D intensity is a smoothed measure of actual annual R&D effort
evidence:
- id: E1
  source_type: policy-document
  citation: 科技部、财政部、国家税务总局.《高新技术企业认定管理办法》(国科发火〔2008〕172号). 2008年4月14日发布,
    2008年1月1日起施行. (Repealed January 1, 2016 by 国科发火〔2016〕32号.)
  url: https://www.most.gov.cn/xxgk/xinxifenlei/fdzdgknr/fgzc/gfxwj/gfxwj2010before/200811/t20081129_65744.html
  date: '2008-04-14'
  supports:
  - identity
  - timeline
  - assignment
  verification_status: verified
  access_level: official-document
  locator: Articles 2 (definition), 10 (six certification criteria, especially 10(4) for R&D thresholds of 3%/4%/6% by sales
    revenue), 11 (application process), 12 (three-year validity and renewal), 13 (renewal review criteria)
- id: E2
  source_type: paper
  citation: 'Chen, Zhao, Zhikuo Liu, Juan Carlos Suárez Serrato, and Daniel Yi Xu. 2021. "Notching R&D Investment with Corporate
    Income Tax Cuts in China." American Economic Review 111 (7): 2065–2100.'
  url: https://doi.org/10.1257/aer.20191758
  date: 2021
  supports:
  - design
  - design_applications
  - empirical_requirements
  - threats
  - assignment
  - research_compatibility
  verification_status: verified
  access_level: full-text
  locator: 'Section I (institutional background and the InnoCom program), Section II (data: SAT administrative tax records
    2008–2011 and NBS ASM 2006–2007, sample construction, variable definitions), Section III (bunching estimates and relabeling
    analysis), Section IV (structural model, SMM estimation, welfare counterfactuals); Tables 1–4, Figures 1–5'
design_applications:
- paper: Notching R&D Investment with Corporate Income Tax Cuts in China
  doi: 10.1257/aer.20191758
  journal: American Economic Review
  year: 2021
  research_question: What is the effect of notched R&D tax incentives on reported and real R&D investment, what share of
    the reported R&D response reflects relabeling of non-R&D expenses versus genuine innovation, and what are the productivity
    and welfare consequences?
  population: Chinese manufacturing and technology firms in the SAT administrative tax records (2008–2011) and NBS Annual
    Survey of Manufacturing (2006–2007); approximately 300,000 firm-year observations per year, totaling ~1.2 million observations
    in the SAT panel
  outcome: Reported R&D expenditure, real R&D investment, relabeling share, total factor productivity, corporate tax revenue
  data_used:
  - SAT administrative corporate income tax records (2008–2011), with detailed firm-level financials including R&D expenditure,
    non-R&D administrative expenses, sales, costs, tax payments
  - NBS Annual Survey of Manufacturing (2006–2007), for pre-reform firm characteristics and outcomes
  - MOST HNTE certification lists, for certification status and timing
  - State Intellectual Property Office patent data, for validation of innovation output
  treatment_encoding: Firm R&D intensity (three-year average R&D/sales) relative to size-dependent HNTE threshold (3%, 4%,
    or 6%); indicator for exceeding the threshold; size bin assignment based on annual sales revenue
  comparison: Firms with R&D intensity just above vs. just below each size-dependent threshold (bunching counterfactual);
    pre-reform (2006–2007, uniform 5% threshold) vs. post-reform (2008–2011, size-dependent thresholds) as validation
  empirical_design: Bunching estimation at each size-dependent R&D notch (Kleven-Waseem 2013) to measure excess mass and
    the reported R&D elasticity; structural model of firm R&D investment and relabeling decisions estimated via Simulated
    Method of Moments to separate real and reporting responses and estimate productivity returns
  assumptions:
  - smooth counterfactual R&D intensity distribution in the absence of the notch
  - relabeling detected via compensating drop in non-R&D administrative expenses at the notch
  - non-R&D admin expenses respond to relabeling but not directly to real R&D changes (structural model exclusion restriction)
  - productivity evolves exogenously conditional on model state variables
  threats_addressed:
  - Reporting manipulation (relabeling) via non-R&D admin expense analysis and structural decomposition
  - Selection into certification via narrow-window bunching comparisons
  - Pre-existing trends via pre-2008 placebo (no bunching at post-2008 thresholds before the reform)
  - Concurrent policies via robustness to excluding firms receiving other R&D subsidies
  - SOE distortions via robustness to excluding state-owned enterprises
  evidence_refs:
  - E2
readiness_blockers:
- The SAT administrative tax data and NBS ASM data used in the paper are not publicly accessible; replication requires approved
  access through Chinese government data channels.
- The structural model's separation of real and reporting responses relies on the non-R&D administrative expense exclusion
  restriction, which cannot be directly tested.
- The bunching estimates identify local average responses for firms near the thresholds; extrapolation to firms far from
  the thresholds requires the structural model.
method_transfer: null
---
## Institutional Background

China's Enterprise Income Tax Law, effective January 1, 2008, unified the previously dual-track corporate income tax system — domestic firms had faced a 33% statutory rate while foreign-invested enterprises enjoyed rates as low as 15–24%. The new law set a standard 25% rate for all enterprises. Article 28 of the law provided for a preferential 15% rate for firms certified as "High and New Technology Enterprises" (HNTE, 高新技术企业), a program also referred to as "InnoCom" (Innovation Company) in the research literature. [E1, verified fact; E2, reported claim]

The detailed certification criteria were established by 国科发火〔2008〕172号, jointly issued by the Ministry of Science and Technology (MOST), the Ministry of Finance (MOF), and the State Administration of Taxation (SAT) on April 14, 2008, with retroactive effect from January 1, 2008. Article 10 of the regulation specifies six conditions that must all be met simultaneously: (1) ownership or exclusive licensing of core intellectual property for main products or services; (2) products or services must fall within the State-Supported High-Tech Fields catalogue; (3) at least 30% of employees must hold a college diploma or above, and at least 10% must be engaged in R&D; (4) the enterprise's R&D expenditure over the prior three fiscal years, as a share of total sales revenue over the same period, must meet size-dependent thresholds — 6% for firms with annual sales below RMB 50 million, 4% for sales between RMB 50 million and RMB 200 million, and 3% for sales above RMB 200 million — and at least 60% of R&D spending must be incurred within China; (5) revenue from high-tech products or services must account for at least 60% of total annual revenue; and (6) the enterprise must achieve a composite innovation capability score of at least 71 out of 100 on a separately administered assessment. Certification is valid for three years and must be renewed; firms that fail renewal lose the preferential rate. [E1, verified fact]

Before 2008, a predecessor InnoCom program operated with a uniform 5% R&D intensity threshold for all firms, and the tax rate reduction was from 33% to 15%. The 2008 reform therefore changed both the structure of the notch (from one uniform threshold to three size-dependent thresholds) and the standard tax rate (from 33% to 25%). This dual change — a shift in the location and number of notches combined with a change in the tax rate differential — provides the identifying variation that the paper exploits. [E1, verified fact; E2, reported claim; analytical inference]

The regulation was repealed and replaced by 国科发火〔2016〕32号 effective January 1, 2016. The 2016 revision lowered the lowest-tier R&D threshold from 6% to 5% and relaxed personnel requirements (removing the college-degree condition for the 10% R&D staff requirement), but these changes postdate the paper's study period. [E1, verified fact]

## What Changed

The 2008 reform created a new incentive structure for R&D investment. Under the pre-2008 regime, a firm crossing the uniform 5% threshold would see its CIT rate drop from 33% to 15% — an 18 percentage point reduction. Under the post-2008 regime, the standard rate fell to 25%, so crossing the threshold yields a 10 percentage point reduction. But critically, the thresholds became size-dependent: small firms (sales < RMB 50M) now face a 6% threshold, medium firms (RMB 50–200M) face 4%, and large firms (> RMB 200M) face 3%. For a firm near its size-dependent cutoff, the marginal incentive to increase reported R&D intensity is sharp — the effective tax rate jumps discontinuously at the threshold. [E1, verified fact; E2, reported claim]

The paper documents that before 2008, there is no evidence of bunching at the post-reform threshold locations. After 2008, clear excess mass appears at each of the three size-dependent thresholds. The bunching is most pronounced at the 3% threshold (large firms, ~25–31% increase in reported R&D) and weakest at the 6% threshold (small firms, ~10–11%). This pattern is consistent with larger firms having greater capacity to adjust R&D reporting and investment in response to tax incentives. [E2, reported claim]

## Implementation and Assignment

Firms apply for HNTE certification through provincial-level certification bodies (认定机构), which are coordinated by MOST, MOF, and SAT. The application requires: a formal application form; business license and tax registration certificates; IP documentation; employee composition and education data; R&D expenditure statements attested by a qualified intermediary for the preceding three fiscal years, with descriptions of R&D activities; and three-year audited financial statements. Applications are reviewed by experts drawn from a centralized database, and successful applicants are published on the national HNTE certification management website for a 15-business-day public comment period. [E1, verified fact]

The key feature for identification is that the R&D intensity threshold creates a notch — a discrete jump in the tax benefit at a specific value of the running variable. Unlike a kink (which changes the marginal rate), a notch changes the average rate, creating a stronger incentive for firms to locate exactly at or just above the threshold. The paper shows that this notch structure generates substantial bunching: firms actively manage their reported R&D intensity to qualify for the preferential rate. [E2, reported claim; analytical inference]

A crucial institutional detail enables the paper's relabeling analysis. Under Chinese Accounting Standards (企业会计准则), R&D expenditure is reported as a subcategory of "Administrative Expenses" (管理费用). This means the SAT tax data contain both total administrative expenses and the R&D subcategory. If firms relabel non-R&D administrative expenses as R&D to meet the threshold, total administrative expenses remain unchanged, but the non-R&D component drops sharply at the notch. The paper documents precisely this pattern, finding that non-R&D administrative expenses fall by approximately the amount needed to explain a substantial share of the reported R&D increase. [E2, reported claim]

## Why This Creates Empirical Variation

The HNTE notch creates a natural setting for bunching estimation. The logic follows Kleven and Waseem (2013) and Saez (2010): in the absence of the notch, the distribution of R&D intensity across firms should be smooth. The notch creates an incentive for firms just below the threshold to increase reported R&D to cross it, generating excess mass (bunching) at and just above the threshold, and a corresponding hole (missing mass) just below. The amount of bunching identifies the elasticity of reported R&D to the tax incentive. [E2, reported claim; analytical inference]

The 2008 reform provides a critical validation: the pre-2008 distribution of R&D intensity, measured from the NBS Annual Survey of Manufacturing (2006–2007), shows no bunching at the post-2008 threshold locations. After the reform, bunching appears at exactly those locations. This pre-post contrast rules out the possibility that the bunching reflects a pre-existing feature of the R&D intensity distribution or a spurious data pattern. [E2, reported claim]

The structural model extends the analysis beyond the reduced-form bunching estimate. Firms in the model face heterogeneous productivity, convex R&D adjustment costs, and a fixed cost of obtaining and maintaining HNTE certification. They may also relabel non-R&D administrative expenses as R&D at a cost. The structural parameters — the productivity elasticity of R&D and the relabeling cost — are estimated by Simulated Method of Moments, matching the observed bunching magnitude, the non-R&D administrative expense drop, and the joint distribution of R&D and productivity. The structural estimates imply that 24.2% of reported R&D at the threshold reflects relabeling, and that doubling real R&D increases TFP by approximately 9%. [E2, reported claim]

## Identification Risks

The central identification challenge is that firms may manipulate reported R&D to cross the threshold without changing real innovative activity. This is not a hypothetical concern — the paper documents it directly. Under Chinese Accounting Standards, the R&D subcategory of Administrative Expenses makes this manipulation detectable: the compensating drop in non-R&D administrative expenses at the notch provides a "signature" of relabeling. The structural model uses this signature to separate real and reporting responses. However, the decomposition relies on the model's exclusion restriction — that non-R&D administrative expenses respond to relabeling but not to real R&D changes at the threshold. If firms simultaneously adjust both real R&D and the composition of administrative expenses for reasons unrelated to relabeling, the decomposition is biased. [E2, reported claim; analytical inference]

A second concern is that the R&D intensity running variable is constructed from firm self-reports in tax filings. While the SAT data are administrative (not survey) records, firms have incentives to misreport for tax purposes, and the three-year averaging rule smooths annual fluctuations. The paper addresses this by showing that the bunching patterns are robust to alternative constructions of the running variable and by validating against patent data. [analytical inference]

External validity is limited: the bunching estimator identifies the local average response of firms near the thresholds. The structural model extrapolates to inframarginal firms, but this extrapolation depends on functional form assumptions. The welfare counterfactuals — which suggest that modest spillovers justify the program — are model-dependent. [E2, reported claim; analytical inference]

## Data Requirements

The core data are the State Administration of Taxation (SAT) administrative corporate income tax records for 2008–2011, which contain detailed firm-level financial information: R&D expenditure (subcategory of Administrative Expenses), non-R&D administrative expenses, sales revenue, costs, profits, tax payments, and firm characteristics (industry, ownership, location). The pre-reform period uses the NBS Annual Survey of Manufacturing (ASM) for 2006–2007, which covers approximately 300,000 manufacturing firms per year with similar financial variables. The paper links these two data sources using firm identifiers. Supplementary data include: HNTE certification lists from MOST (for certification status and timing), patent data from the State Intellectual Property Office (for validating innovation output), and industry-level deflators. [E2, reported claim]

The SAT administrative tax data are not publicly available; access requires approval through Chinese government data channels or collaboration with domestic research institutions. The ASM data are similarly restricted. The replication package on OpenICPSR (project 131201) provides Matlab code for the structural estimation but requires the user to supply the underlying data. [E2, reported claim; web search, reported claim]

## Evidence Notes

E1 is the official HNTE certification regulation (国科发火〔2008〕172号), published on the MOST website. It establishes the six certification criteria, the size-dependent R&D thresholds (3%/4%/6%), the three-year certification validity, and the application process. The document confirms that the policy was effective January 1, 2008, and was jointly administered by MOST, MOF, and SAT. The 2016 replacement (国科发火〔2016〕32号) lowered the lowest-tier threshold to 5% and relaxed personnel criteria. [E1, verified fact]

E2 is the published AER article. The paper's core empirical contribution is the bunching analysis showing that the HNTE notch causes significant increases in reported R&D — approximately 25–31% for large firms at the 3% threshold, 17–21% for medium firms at the 4% threshold, and 10–11% for small firms at the 6% threshold. Its core methodological contribution is the structural decomposition separating real and reporting responses, which finds that 24.2% of reported R&D at the threshold reflects relabeling. The estimated productivity return — 9% TFP increase from doubling real R&D — is economically significant. The welfare analysis suggests that the program's cost in foregone corporate tax revenue is partly offset by higher tax revenue from increased profits, and that modest R&D spillovers (on the order of 10–20%) would justify the program. The paper's replication package (OpenICPSR 131201) includes Matlab code for the bunching estimator and structural estimation, though the underlying administrative tax data require separate access. [E2, reported claim]

**Grounding note (task-9beb75f420fc, 2026-07-13)**: This record was grounded from `extracted` to `grounded` status. Key corrections made during grounding: (1) sample period corrected from 2005–2014 to 2006–2011 based on the paper's actual data (SAT 2008–2011 + ASM 2006–2007); (2) R&D thresholds corrected from "3%–6% depending on firm size and industry" to the exact size-dependent thresholds of 3%/4%/6% by sales revenue, with the pre-2008 uniform 5% threshold documented; (3) pre-2008 tax rate (33% → 15%) added alongside post-2008 (25% → 15%); (4) the relabeling detection mechanism (R&D as subcategory of Administrative Expenses under Chinese Accounting Standards) documented in detail; (5) primary policy evidence (国科发火〔2008〕172号) verified from the MOST official website; (6) design.claim_type set to "causal" based on the bunching identification strategy; (7) specific diagnostics (pre-2008 placebo, non-R&D admin expense analysis, structural SMM) documented. [analytical inference]
