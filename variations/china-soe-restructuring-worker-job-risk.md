---
schema_version: 2
id: china-soe-restructuring-worker-job-risk
name: China Late-1990s SOE Restructuring and Urban Worker Job-Risk Contrast
aliases: [Breaking the iron rice bowl precautionary wealth, 国企改制就业风险与预防性储蓄]
status: grounded
provenance:
  task_id: task-e3fa2c44f25c
scope:
  country: China
  regions: [Mainland China urban CHIP survey households]
  domains: [labor-economics, household-finance, development-economics, urban-economics]
  variation_type: event-shock
  knowledge_role: china-variation
  china_relevance: The late-1990s restructuring changed employment security faced by Chinese urban state-sector workers; the application compares SOE and government-sector households across 1995 and 2002.
identity:
  instrument: Late-1990s SOE restructuring and workforce shedding, as a worker-sector employment-security contrast
  authority: Central government reform direction and enterprise/local-government implementation
  legal_identifiers:
  - 国发〔1997〕10号, 国务院关于在若干城市试行国有企业兼并破产和职工再就业有关问题的补充通知, dated 1997-03-02
  - 中发（1998）10号, 中共中央、国务院关于切实做好国有企业下岗职工基本生活保障和再就业工作的通知
  implementation_regime: >
    A restructuring transition, not one universal dismissal date. The 1997
    document regulates pilot-city enterprise restructuring; the 1998 document
    regulates layoffs and reemployment support. Neither makes the survey's
    broad SOE ownership group identical to statutory eligibility.
  assignment_mechanism: >
    Compare the SOE-versus-GOV household wealth/permanent-income coefficient
    before and after the restructuring period. Employment sector supplies the
    differential job-risk exposure, with government-assigned current jobs used
    to reduce occupational self-selection. This is not random individual layoff
    assignment or a geographic reform-intensity instrument.
  parent: null
  related_variations: [china-soe-decentralization]
timeline:
  announcement: null
  effective: null
  implementation_start: 1997
  implementation_end: 2002
  local_timing: >
    These years bound the paper-reported large layoff wave, not every enterprise's
    legal adoption. The pilot document is dated March 2, 1997; Beijing forwarded
    it April 30. The Shanghai reprint labels the 1998 notice June 9; that is page
    publication metadata. The research observes 1995 pre and 2002 post only.
  anticipation: >
    The article describes the scale as largely unexpected to individual workers,
    but earlier labor-contract reforms and enterprise distress precede 1997.
    Two survey waves cannot test absence of differential anticipatory saving.
  last_verified: '2026-10-02'
assignment:
  unit: Urban household classified by its working head's employment sector and survey year
  treated: >
    Heads working in the paper's SOE group in 2002, relative to that group's
    1995 observations. The paper includes directly government-owned firms,
    government-controlled shareholding firms AND collective enterprises.
  comparison_pool: >
    Heads employed by government at any level or public institutions (GOV),
    surveyed in 1995 and 2002. The principal subsample requires current jobs
    obtained through government assignment in both sectors and both years.
  rule: >
    SOE=1 for the article's ownership group and 0 for GOV. Estimate equation 12
    separately by year and take beta_SOE,2002 minus beta_SOE,1995. The government
    assignment indicator describes the channel of obtaining the CURRENT job,
    not an inferred pre-1986 cohort or a randomized reform treatment.
  intensity: Binary employment-sector contrast; local ownership and demographic heterogeneity are applications, not separate admitted variations
  exemptions:
  - The application restricts head age to 25-55 and excludes households outside the two employment sectors.
  - The head is the sole breadwinner or the highest-income person in a multiple-earner household.
  - Actual dismissed or departed SOE workers are not an independently observed treatment cohort in the post sample.
  compliance: >
    The 1998 notice requires employer layoff plans, consultation and regulated
    local implementation, rather than mechanically dismissing every SOE worker.
    Sector membership proxies exposure to employment uncertainty; the article
    does not observe each surviving worker's dismissal probability or each
    employer's reform date. Survey collectives must remain explicit rather than
    being silently relabeled as legally identical SOEs.
  exposure_construction: >
    Harmonize urban CHIP 1995/2002 employment ownership and current-job acquisition
    responses, select working heads aged 25-55, and retain sector, survey year,
    province and industry. Construct financial wealth from six asset categories
    and permanent income from retrospective head earnings. Keep survey-wave
    identifiers distinct; this is not a longitudinal household-ID join.
  required_identifiers: [Household and person IDs within survey wave, Survey year, Head employment ownership, Current-job acquisition channel, Province and industry]
  spillovers: >
    Spouses' employment risk and local restructuring can affect GOV households
    as well as SOE households; the government group is a relative comparison,
    not an economy unaffected by reform.
research_compatibility:
  outcome_domains: [Financial wealth accumulation, Household saving responses, Employment uncertainty]
  affected_populations: [Urban working households in the article's SOE and GOV groups]
  mechanism_channels: [Precautionary wealth, Expected permanent income, Pension participation, Household employment insurance]
  best_for: [Conditional research on sector-relative employment insecurity and wealth stocks spanning the late1990s transition]
  not_good_for: [Random layoff effects, All displaced workers' welfare, Annual saving-rate effects inferred from wealth, Firm-control decentralization, Modern household panels without historical assignment and wealth questions]
design:
  claim_type: reduced-form
  affordances: [Sector-by-period contrast, Government-assigned job restriction, Observable composition reweighting]
  candidate_designs: [Repeated-cross-section difference in sector coefficients]
  identifying_variation: The change in SOE versus GOV wealth-to-permanent-income differences between CHIP 1995 and 2002
  primary_strategy: Separate annual IV-Tobit regressions in equation 12, followed by a coefficient-difference comparison
  estimand: >
    Conditional change in the SOE-GOV financial-wealth/permanent-income gap
    among sampled working heads, principally government-assigned jobs. A pure
    precautionary-risk interpretation requires separating changes in expected
    income, benefits and household composition.
  treatment_variable: SOE ownership dummy in each year; post-period difference of its coefficient
  comparison_logic: GOV supplies the sector counterfactual, 1995 supplies the pre-wave gap; no household fixed effects or observed individual layoff treatment
  estimation_notes: >
    Equation 12 controls log permanent income, RISK and demographics, province
    and industry. Education dummies and education-by-age/age-squared instruments
    target permanent income, NOT SOE assignment. Zero wealth is censored in
    IV-Tobit; excluding it is a separate 2SLS sensitivity. Full sample sizes are
    4390/3027; assigned-job Table 5 samples are 3627/2170. Table 5 reports robust
    standard errors and Chow tests, not a demonstrated province-cluster design.
  assumptions:
  - No unaccounted sector-specific change in wealth formation would generate the same 1995-2002 gap without the restructuring.
  - Government-assigned current jobs sufficiently reduce risk-preference sorting; workers' expressed preferences can still matter.
  - Changes in surviving employed sample composition are adequately addressed for the intended population.
  - Permanent-income instruments satisfy relevance and exclusion in the selected wealth model.
  - Health, housing, pension and expected-income changes are distinguished before attributing the gap solely to precautionary motives.
  diagnostics:
  - Balance and overlap of pooled survey-wave propensity scores; sensitivity to extreme inverse weights
  - Compare assigned-job and full samples without interpreting the difference as randomized correction
  - Replicate income-expectation and pension controls; the expectation question exists only in 2002
  - Spouse-sector controls and wealth-definition/zero-wealth sensitivities
  - Additional pre-wave evidence if compatible questions exist; two waves alone do not establish parallel trends
threats:
- type: survivor-and-occupational-selection
  basis: documented
  condition: The 2002 sample conditions on remaining employed in SOE or GOV. Government-assigned jobs mitigate but do not eliminate preference selection; observable reweighting cannot recover unobserved selection or all dismissed households.
  evidence_refs: [E3]
  possible_diagnostics: [Overlap and weighted balance, Separate departures where data permit, Sensitivity to unobserved selection]
- type: simultaneous-benefit-and-income-changes
  basis: reported
  condition: Health and housing reforms and pension participation changed during the same interval; expected-income declines can raise saving through permanent-income effects rather than uncertainty alone.
  evidence_refs: [E3]
  possible_diagnostics: [Table 6 income/pension controls, Spouse-sector checks, Avoid causal conditioning on post-treatment benefit mediators without a defined estimand]
- type: exposure-boundary
  basis: inferred
  condition: The survey treatment includes collectives, whereas legal restructuring provisions have narrower and varying applicability. Sector membership is a risk proxy, not an individual legal eligibility list.
  evidence_refs: [E1, E3]
  possible_diagnostics: [Disaggregate ownership groups, Obtain employer-specific timing, Preserve broad-sample versus legal eligibility distinction]
empirical_requirements:
  contract_version: 1
  population: Urban CHIP households with working heads aged 25-55 in SOE/GOV, principally government-assigned current jobs
  observation_unit: Household within survey wave, not linked household panel
  geography_level: Province with industry and urban survey strata preserved
  time_start: 1995
  time_end: 2002
  minimum_frequency: repeated-cross-section
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields: [Head employment ownership, Current-job acquisition channel, Six financial asset categories, Head retrospective earnings 1990-1995 or 1998-2002, Education, Age, Occupation, Gender, Marital status, Health coverage, Housing ownership, Household size and children, Pension participation, 2002 income expectations]
  required_identifiers: [Within-wave household and person IDs, Survey year, Province, Industry]
  treatment_key: [Survey year, Head employment ownership]
  treatment_source: Published equation 12 and Table 1 sector/current-job definitions; official documents bound the institutional transition, not survey recoding values.
  measurement_risks: [Survey harmonization and ownership codebook required, Conditional employment sample, Retrospective earnings error, Current highest-earner head may change, Wealth stock is not annual saving flow]
design_profiles: []
evidence:
- id: E1
  source_type: policy-document
  citation: State Council 国发〔1997〕10号, official Beijing forwarding and full reprint
  url: https://www.beijing.gov.cn/zhengce/zfwj/zfwj/szfwj/201905/t20190523_72105.html
  date: '1997-03-02'
  supports: [identity.legal_identifiers, identity.implementation_regime, timeline.local_timing]
  verification_status: verified
  access_level: official-document
  locator: Reprinted State Council title and March 2 signature; introductory scope, Sections I-II, VIII and X; Beijing forwarding dated April 30. Gazette PDF retrieved but scanned text not used as verification.
- id: E2
  source_type: policy-document
  citation: 中发（1998）10号, official Shanghai HRSS reprint
  url: https://rsj.sh.gov.cn/tgwyxzfgwj_17255/20200617/t0035_1388257.html
  date: '1998-06-09'
  supports: [identity.legal_identifiers, identity.implementation_regime, timeline.local_timing, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: Title/identifier and page publication date; Sections II-III and V on layoff regulation, reemployment centers and continuing support. Date is reprint metadata, not independently verified signature date.
- id: E3
  source_type: paper
  citation: He, Huang, Liu and Zhu (2018), Breaking the iron rice bowl, Journal of Monetary Economics 94, 94-113
  url: https://doi.org/10.1016/j.jmoneco.2017.12.002
  date: 2018
  supports: [identity.assignment_mechanism, timeline.implementation_start, timeline.implementation_end, timeline.anticipation, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.exposure_construction, assignment.required_identifiers, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.population, empirical_requirements.required_fields, empirical_requirements.treatment_source, design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year, design_applications.research_question, design_applications.population, design_applications.outcome, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design]
  verification_status: reported
  access_level: full-text
  locator: Author-hosted published typeset PDF at https://huihe.weebly.com/uploads/1/3/6/1/13611032/hhlz_jme_2018_journalprint.pdf, 20 pages, DOI on first page; printed pp94-97,100-106,109-111 inspected, Sections2,4,5.1-5.4,6.1-6.4; Eq12-13, Tables1-5,7-8. Table6 notes also inspected. Not the November2017 working-paper pagination.
- id: E4
  source_type: appendix
  citation: He et al. November16,2017 supplemental appendix, FRASER transcription of FRBSF working-paper supplement
  url: https://fraser.stlouisfed.org/title/working-papers-federal-reserve-bank-san-francisco-7038/breaking-iron-rice-bowl-precautionary-savings-639797/content/fulltext/frbsf_pacificBasin_wp2014-04_appendix
  date: '2017-11-16'
  supports: [design.diagnostics]
  verification_status: reported
  access_level: appendix
  locator: Supplemental cover, version date and table inventory including A1 income/pension controls, A5 weighting and A9 pre1986 sensitivity. This is a working-paper supplement, not verified final-journal Appendix A or replication code.
design_applications:
- paper: 'Breaking the iron rice bowl: Evidence of precautionary savings from the Chinese state-owned enterprises reform'
  doi: 10.1016/j.jmoneco.2017.12.002
  journal: Journal of Monetary Economics
  year: 2018
  research_question: Did differential employment insecurity change SOE workers' precautionary wealth relative to GOV households?
  population: Urban CHIP 1995/2002 working heads aged25-55; government-assigned current-job samples3627/2170
  outcome: Financial wealth divided by permanent income; model-predicted wealth accumulation share is a separate calculation
  data_used: [Urban CHIP1995 and2002 repeated cross sections, Retrospective head earnings, Financial asset holdings and employment responses]
  treatment_encoding: SOE=1 including government-owned/controlled and collective firms; GOV=0; compare separately estimated1995/2002 SOE coefficients
  comparison: Relative wealth-to-income gap across sectors and survey waves within government-assigned jobs
  empirical_design: Equation12 IV-Tobit plus coefficient difference; Eq13 predicted versus SOE-dummy-zero counterfactual wealth share
  assumptions: [Counterfactual sector-gap stability, Adequate selection adjustment, Valid permanent-income IV, Separate expected-income and benefit changes]
  threats_addressed: [Government-assigned-job restriction, Propensity reweighting, Income expectations and pension controls, Spouse and wealth-definition sensitivities]
  evidence_refs: [E3]
method_transfer: null
readiness_blockers:
- Conditional comparison only; two survey waves and observable weighting do not prove counterfactual trends or recover all displaced workers.
- Exact questionnaire codes and cleaning/estimation code were not inspected; obtain the relevant CHIP codebooks before replication. No restricted survey data are stored.
- Final-journal Appendix A was not inspected; the archived 2017 supplement is version-labeled and does not verify the paper's case-study anticipation claim.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

State-sector jobs had provided employment security and associated benefits.
The article describes labor-contract liberalization, private competition and
loss-making enterprises before the late-1990s layoff wave [E3, reported claim].
The 1997 pilot rules and the 1998 layoff-support notice establish a regulated
transition, not a nationwide lottery or simultaneous dismissal [E1; E2].

## What Changed

SOE workers faced greater perceived unemployment risk relative to government
employees. The study follows remaining working households, not dismissed workers'
subsequent outcomes [E3, reported claim]. Reemployment centers and social-insurance
support mean that layoffs should not be described as instant elimination of every
benefit [E2].

## Implementation and Assignment

The legal pilot boundary is not the paper's treatment. The 1997 bankruptcy rules
are restricted to specified pilot-city enterprise categories [E1]. The survey's
SOE group also includes collectives; GOV includes public institutions. Preserve
this broad coding instead of silently substituting a narrow legal ownership
definition. Government assignment refers to how the head obtained the current
job. It is neither an automatic pre-1986 indicator nor evidence of random sector
placement [E3, reported claim].

## Why This Creates Empirical Variation

Estimate the conditional SOE-GOV financial-wealth/permanent-income difference
separately in 1995 and 2002, then compare coefficients. This preserves the actual
equation12 construction; there are no household fixed effects. The assigned-job
coefficients are -0.012 and0.539. Their difference is0.551 units of annual
permanent income, not a55.1% rise in the annual saving rate. Equation13's43.1%
is instead the model-attributed share of predicted wealth accumulation
[E3, reported claim]. Neither quantity proves a universal Chinese saving effect.

## Identification Risks

Occupational sorting and selective retention are different problems. The assigned
job restriction reduces preference-driven sector choice but workers could express
preferences. The2002 sample excludes people who left these sectors. Section6.1
fits a pooled Logit probability p of belonging to the2002 sample conditional on
age, gender, education, occupation, industry and location; weights are1/p for2002
and1/(1-p) for1995. These are survey-wave probabilities, not longitudinally
observed individual survival probabilities [E3, reported claim]. Observable
balance cannot remove unobserved exits [analytical inference].

Expected income, pensions, housing and health coverage changed over the interval.
Controls and reported sensitivity exercises inform interpretation but do not
automatically isolate a single uncertainty channel, especially if benefits are
mediators [E3, reported claim; analytical inference]. Education instruments the
permanent-income measure; it does not establish exogenous reform assignment.

## Data Requirements

Table1 financial wealth sums checking accounts, savings accounts, stocks, bonds,
employer-fund contributions and loans to others. It is a stock, not expenditure
minus income. Section4.3 constructs permanent income from each year's earnings
relative to the survey mean, averages those relative earnings over time, then
multiplies survey-year head earnings by that average. Retrospective periods are
1990-1995 and1998-2002. RISK is log variance of log head income across those
years, conditional on employment; it is distinct from SOE job-loss exposure.
Footnote11 excludes box-plot outliers beyond Q1-3IQR and Q3+3IQR
[E3, reported claim]. Source questionnaires and code remain necessary for exact
harmonization, denominator populations and filtering.

## Evidence Notes

E3 is the published article, recovered through the author's site and inspected
in memory. E4 is an explicitly dated working-paper supplement; its inventory
does not substitute for the final Appendix A case study or prove no anticipation.
No paper files or survey microdata are saved in this repository.

This worker-sector comparison is distinct from the existing firm-control
decentralization record and the blocked ReStud prefecture-industry exposure
candidate candidate-182bc9807ee8. Shared reform history does not make their
assignments identical. Demographic splits, local-SOE comparisons and alternate
wealth measures stay inside this one case rather than inflating the record count.
