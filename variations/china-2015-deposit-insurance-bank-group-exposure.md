---
schema_version: 2
id: china-2015-deposit-insurance-bank-group-exposure
name: China2015 Explicit Deposit Insurance and Historical Bank-Group Exposure
aliases:
- 2015 deposit insurance reform
- 存款保险条例
status: grounded
provenance:
  task_id: task-89193510fd2f
scope:
  country: China
  regions: [mainland China]
  domains: [financial-economics, banking, development-economics]
  variation_type: other
  knowledge_role: china-variation
  china_relevance: Chinese deposit-taking banks face the2015 statutory insurance regime; the inspected application compares its marginal effect across historical bank groups.
identity:
  instrument: Introduction of statutory deposit insurance under Order660, not a bank bailout, deposit-rate liberalization or bank-specific risk-premium shock.
  authority: State Council; PBOC and the designated deposit-insurance fund management institution implement the statutory framework.
  legal_identifiers: [中华人民共和国国务院令第660号, 存款保险条例]
  implementation_regime: Initial2015 regime during the paper's2011-2017 window. Subsequent bank resolutions and later changes to institution classification are not additional treatments here.
  assignment_mechanism: National implementation interacted with historical bank group, representing hypothesized differences in marginal protection relative to pre-existing implicit guarantees. Group membership is not randomized and both groups are legally covered.
  parent: null
  related_variations: []
timeline:
  announcement: '2015-03-31'
  effective: '2015-05-01'
  implementation_start: '2015-05-01'
  implementation_end: null
  local_timing: Order signed February17 and publicly released March31; annual2015 observations combine pre- and post-effective months. The2017 sample endpoint is not policy termination.
  anticipation: The PBOC's2015 report describes prior reform and legislation preparations; anticipation before the effective date must be allowed rather than assuming an unanticipated May shock.
  last_verified: '2026-10-04'
assignment:
  unit: Deposit-taking bank legal entity by observation period; insured balances are defined at depositor-by-bank level.
  treated: In the inspected empirical comparison, joint-stock, city and rural commercial banks outside the named historical big five.
  comparison_pool: ICBC, China Construction Bank, Bank of China, Agricultural Bank of China and Bank of Communications; these are lower-marginal-exposure comparators, not legally uninsured controls.
  rule: Domestic deposit-taking institutions must participate. The paper assigns bank-group treatment using the five named institutions and compares other commercial banks in its sample.
  intensity: Statutory compensation is capped at500,000RMB for each depositor's aggregated insured principal and interest at one bank. This is not a500,000RMB bank balance-sheet cutoff or an RD used by this paper. Perceived incremental protection differs by bank group only under the paper's implicit-guarantee argument.
  exemptions:
  - Foreign-bank branches in China and Chinese banks' overseas branches are excluded unless international arrangements specify otherwise; foreign-owned banks incorporated in China are not excluded solely by ownership.
  - Interbank deposits, senior managers' deposits at their own bank and other designated deposits are excluded.
  - Institutions already taken over, revoked or admitted to bankruptcy before implementation fall outside the original regulation.
  compliance: Existing institutions must register within the manager's deadline; newly licensed ones within six months. Banks pay premiums; a depositor does not purchase a private insurance contract. Registration and premium compliance should not be inferred from a bank-group flag.
  exposure_construction: >
    Recover historical bank legal-entity IDs and set group=0 for the five
    named comparators, group=1 for the other sampled commercial banks.
    Join group to bank-period outcomes and the May1,2015 legal event.
    Retain2015 as a transition year; a clean-year sensitivity can compare
    2011-2014 with2016-2017, explicitly labelled a new construction rather
    than the authors' exact code. Equation2 uses group-by-post-by-channel
    interactions and all lower-order terms. Do not assign group from a
    current big-six label, treat a branch as an independent bank, or describe
    the comparison as insured versus uninsured.
  required_identifiers: [bank_legal_entity_id, year, historical_bank_group]
  spillovers: Depositors can move balances between bank groups and banks share interbank exposures; the comparator's funding environment can change even if its implicit guarantee was already strong.
research_compatibility:
  outcome_domains: [Bank liquidity creation, Lending, Deposit funding, Financial intermediation]
  affected_populations: [Mainland commercial banks; indirectly their borrowers and depositors]
  mechanism_channels: [Depositor confidence, Funding stability, Market discipline, Risk-taking, Competition]
  best_for: [Bank-level differential responses to national financial-safety-net reform with historical group identity and adequate financial statements.]
  not_good_for:
  - A nationwide average policy effect from a simple before-after regression.
  - Claiming random bank ownership or an untreated big-five control group.
  - Firm-level financing effects without bank-firm lending links and a defended exposure aggregation.
design:
  claim_type: reduced-form
  affordances: [Known national effective date, Named historical comparison group, Pre-reform observations]
  candidate_designs: [Bank-group differential reform response, Channel-slope interaction analysis]
  identifying_variation: Differences in marginal reform exposure between historical big-five and other banks, conditional on the implicit-guarantee rationale and comparable counterfactual trends.
  primary_strategy: Published equation2 interacts bank group, post2015 and capital/excess-lending/competition/monetary-policy measures, including lower-order interactions; Table9 reports random- and fixed-effects versions.
  estimand: Differential post-reform change in the association between a specified channel and bank liquidity creation across the two groups. A causal channel interpretation needs additional restrictions on the channel variable.
  treatment_variable: Historical non-big-five indicator interacted with post-reform timing; channel interactions use bank capital, lending, competition and monetary-policy measures.
  comparison_logic: Compare changes in channel slopes across groups; the five comparator banks also receive the legal insurance regime. Group-by-post alone is not the entire published estimand.
  estimation_notes: The paper reports bank-clustered robust errors. Its2011-2017 unbalanced sample has126 banks and670 observations. Equation1 is a national pre/post interaction model, not a controlled policy experiment; common national rates are collinear with saturated year effects. Printed wording does not unambiguously establish how2015 itself is coded.
  assumptions:
  - Without the reform, relevant outcome or channel-slope trends would be comparable across historical groups.
  - Other simultaneous reforms do not create the same bank-group differential response attributed to insurance.
  - Channel measures and bank controls are not silently treated as exogenous when policy can change them.
  - Bank mergers, missing financial items and group classifications do not generate an artificial break.
  diagnostics:
  - Examine pre-trends and slope interactions, allowing anticipation and a separate2015 transition.
  - Report sensitivity to excluding2015 and individual comparator banks; nonrejection of short pre-trends is not proof of validity.
  - Inspect interest-rate and capital/liquidity-rule overlap, group-specific balance-sheet changes and inference with only five comparator banks.
  - Separate differential reduced forms from causal claims about endogenous capital or lending channels.
threats:
- type: comparator_also_covered
  basis: documented
  condition: Both groups are insured; treating big-five banks as an unaffected legal control misstates the institution. Lower marginal protection is an interpretation, not a statutory exemption.
  evidence_refs: [E1, E2]
  possible_diagnostics: [Defend implicit-guarantee differences for the outcome, Assess depositor substitution, Report comparator sensitivity]
- type: contemporaneous_banking_reforms
  basis: reported
  condition: The paper examines concurrent interest-rate changes and discusses Basel liquidity requirements. Its checks do not establish that all group-differential confounding is absent.
  evidence_refs: [E2, E3]
  possible_diagnostics: [Map reform timing, Compare balance-sheet composition and regulatory constraints, Use alternative windows]
- type: channel_endogeneity_and_common_time
  basis: inferred
  condition: Capital, loans and market shares can respond to insurance; national monetary rates vary only over time. Slope changes can combine endogenous adjustment and common shocks.
  evidence_refs: [E2]
  possible_diagnostics: [Distinguish descriptive channel slopes from causal channels, Use predetermined measures where justified, Show time-control sensitivity]
- type: annual_transition_and_small_comparator_pool
  basis: documented
  condition: May2015 is within an annual period; five comparator banks and a short panel constrain pre-trend and inference precision. Printed post2015 wording leaves the treatment of2015 to verify before exact replication.
  evidence_refs: [E1, E2]
  possible_diagnostics: [Separate transition year, Recover author code if available, Inspect bank-level influence and dependence]
empirical_requirements:
  contract_version: 1
  population: Mainland commercial-bank legal entities with historical big-five identity; match the paper's exclusions for its application.
  observation_unit: bank-year
  geography_level: mainland national banking system, bank legal entity
  time_start: 2011
  time_end: 2017
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 2
  required_fields:
  - Historical bank identity/type, reporting year, merger/name-change information and sample coverage.
  - Outcome financial items; for published liquidity creation, Table1 asset/liability/off-balance classifications and equation3 weights, normalized by total assets.
  - Capital adequacy, equity, loan histories and market shares for the corresponding channel, with all lower-order interactions.
  - Monetary-rate histories and explicitly specified time controls for monetary-channel applications.
  required_identifiers: [bank_legal_entity_id, year, historical_bank_group]
  treatment_key: [bank_legal_entity_id, year]
  treatment_source: Order660 supplies legal timing and coverage; the paper names the historical big-five comparators. Verify legal-entity identity in contemporaneous bank/regulator reports.
  measurement_risks:
  - BankFocus is supplemented by CSMAR, Wind and annual reports; lawful access and vintage-specific accounting crosswalks are needed. No public microdata or executable replication was inspected.
  - Paper terminology must not exclude all foreign-owned banks or infer actual registration/premium schedules.
  - Bank-year data cannot identify a firm or locality's exposure without borrower/branch linkage and an explicit aggregation design.
evidence:
- id: E1
  source_type: policy-document
  citation: State Council Order660, original2015 存款保险条例, reproduced in the Liaoning government gazette.
  url: https://www.ln.gov.cn/web/zwgkx/lnsrmzfgb/2015n/qk/2015n_dssq95/gwywj/45511531E86D4539BFDFC305A3F9215F/index.shtml
  date: '2015-02-17'
  supports: [identity.instrument, identity.legal_identifiers, identity.implementation_regime, timeline.effective, timeline.implementation_start, assignment.unit, assignment.rule, assignment.intensity, assignment.exemptions, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: Preamble and Articles2-5,7-10,19,22-23 inspected2026-10-04. Covers statutory rules, not realization of every bank's participation or implicit guarantees.
- id: E2
  source_type: paper
  citation: Zhou, Xiangyi, Xinyue Li, Yifan Zhou and Alper Kara. JFSR67(2025),101-137, final open-access article published online2024.
  url: https://link.springer.com/content/pdf/10.1007/s10693-024-00431-z.pdf
  date: 2025
  supports: [assignment.treated, assignment.comparison_pool, assignment.exposure_construction, design.primary_strategy, design.estimand, design.estimation_notes, empirical_requirements.required_fields, empirical_requirements.measurement_risks, design_applications.paper, design_applications.population, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design]
  verification_status: reported
  access_level: full-text
  locator: Printedpp104-107,110-117 Sections3.5-5, equations1-3, Tables1-3; pp124-128 Table9 continuation, Figure1 caption, footnote18 and Sections7.1-7.3 inspected in memory2026-10-04. No data/code execution or independent guarantee measurement.
- id: E3
  source_type: implementation-document
  citation: PBOC Financial Stability Analysis Group. 中国金融稳定报告2015, TopicI.
  url: https://www.gov.cn/xinwen/site1/20150530/85781432949779388.pdf
  date: 2015
  supports: [identity.authority, timeline.anticipation, research_compatibility.mechanism_channels, assignment.exemptions]
  verification_status: verified
  access_level: official-document
  locator: Printedpp131-137 TopicI, especially131,133-136; PDFpages140-146 inspected2026-10-04. Official rationale and framework, not a causal estimate or bank-by-bank premium dataset.
- id: E4
  source_type: implementation-document
  citation: PBOC Ningbo branch. 存款保险知多少.
  url: https://ningbo.pbc.gov.cn/ningbo/127149/4272874/index.html
  date: '2021-06-21'
  supports: [assignment.exemptions, empirical_requirements.measurement_risks]
  verification_status: verified
  access_level: official-document
  locator: Questions2,4-6 inspected2026-10-04; clarifies domestically incorporated foreign banks versus foreign branches. Later explanation, not a historical2015 participation roster.
- id: E5
  source_type: policy-document
  citation: Xinhua authorized publication of State Council Order660.
  url: https://www.xinhuanet.com/politics/2015-03/31/c_1114826603.htm
  date: '2015-03-31'
  supports: [timeline.announcement, timeline.local_timing]
  verification_status: verified
  access_level: official-document
  locator: Authorized release timestamp and signed order text inspected2026-10-04; distinguishes publication, signature and effective dates.
- id: E6
  source_type: paper
  citation: Publisher metadata for Zhou et al., Deposit Insurance and Bank Liquidity Creation.
  url: https://doi.org/10.1007/s10693-024-00431-z
  date: 2025
  supports: [design_applications.doi, design_applications.paper, design_applications.journal, design_applications.year]
  verification_status: reported
  access_level: metadata
  locator: Publisher article header and final PDF title page inspected2026-10-04; onlineJuly2,2024, issue2025, volume67pp101-137.
design_applications:
- paper: 'Deposit Insurance and Bank Liquidity Creation: Evidence from a Natural Experiment in China'
  doi: 10.1007/s10693-024-00431-z
  journal: Journal of Financial Services Research
  year: 2025
  research_question: Does explicit insurance change the relationship between bank characteristics/monetary policy and liquidity creation differently across bank groups?
  population: 126 Chinese commercial banks2011-2017; five big banks,12 joint-stock,77 city and32 rural commercial banks. Policy banks, foreign branches and Postal Savings Bank excluded.
  outcome: Total, on-balance and off-balance liquidity creation per unit of assets.
  data_used: [BankFocus, CSMAR, Wind, Bank annual reports, NBS macroeconomic statistics]
  treatment_encoding: Non-big-five group multiplied by post2015 and channel measures in equation2; exact handling of the transition year is not independently code-verified.
  comparison: Historical big-five banks with hypothesized stronger pre-existing implicit guarantees; both groups legally insured.
  empirical_design: Bank-group DID-style channel-slope interactions; random- and fixed-effects versions, bank-clustered inference.
  assumptions: [Comparable counterfactual channel slopes, No confounding bank-group reform response, Defended channel-variable interpretation]
  threats_addressed: [Reported event-study interactions, Liquidity classification sensitivity, Interest-rate-related robustness checks]
  evidence_refs: [E2, E6]
method_transfer: null
readiness_blockers:
- Obtain lawful bank financial data, historical identity crosswalks and accounting coverage; this is not a turnkey replication.
- Reconcile the published post2015 coding before exact reproduction; retain a separate transition year and report alternative annual windows in new work.
- Defend implicit-guarantee differences, counterfactual trends, concurrent reform separation and channel exogeneity for the chosen outcome; the legal event alone does not certify a causal design.
---

## Institutional Background

China introduced a statutory safety net while pursuing financial reform.
The PBOC linked it to market-based exit, fairer competition for smaller
banks and interest-rate liberalization [E3]. The inspected paper argues
that large state-controlled banks already enjoyed stronger implicit
protection [E2, reported claim]. That argument motivates an empirical
comparison; it is not a law guaranteeing only those five banks.

## What Changed

Order660 provides explicit protection for eligible deposits, with a
depositor-by-bank compensation limit and defined exclusions [E1]. It also
creates premium, early-correction and resolution obligations. The reform
does not insure every financial product or make all uninsured balances
worthless. Nor does it prove that implicit bailouts ceased.

## Implementation and Assignment

The statutory change is national. The paper's exposure contrast comes
from historical bank groups, not phased geographical adoption. ICBC,
CCB, BOC, ABC and Bank of Communications are the named comparators; Postal
Savings Bank is excluded in that application [E2, reported claim].
Foreign ownership must be distinguished from foreign-branch legal status
[E1; E4]. Neither the current big-six label nor a branch-only panel
reproduces this comparison.

## Why This Creates Empirical Variation

If explicit insurance adds more credible protection to smaller banks,
their funding and liquidity behavior can change differently from that of
the already implicitly protected comparators. The paper estimates changes
in channel slopes through three-way interactions [E2, reported claim].
This is a conditional differential-response opportunity, not a clean
national policy effect. A researcher studying lending levels instead
would need to state that different estimand and defend its counterfactual.

## Identification Risks

Bank group captures ownership, size, portfolios and regulatory treatment.
These features can generate differential trends unrelated to insurance.
Depositor substitution also exposes the nominal control group. The paper
reports pre-trend and concurrent-policy checks, but they do not eliminate
these concerns [E2, reported; analytical inference]. Changes in capital
or market shares may be mechanisms of the reform rather than independent
exogenous channels. Short pre-periods and five comparator banks make
non-significance particularly weak evidence of absence.

## Data Requirements

Assignment joins by bank legal entity and period. It does not automatically
join to firm registration location or city outcomes. For liquidity
creation, recover classified financial items rather than replace the
paper's weighted construction with a loans-to-assets ratio [E2, reported].
The institution is grounded even though licensed financial data and
accounting-vintage crosswalks remain necessary implementation conditions.

## Evidence Notes

May1,2015 is the verified effective date, while March31 is public release
and February17 is signature [E1; E5]. The annual transition must remain
visible: the paper's wording alone does not verify its exact2015 switch.
Its foreign-bank and premium summaries should not replace the original
law or PBOC framework. This record does not claim a bank-specific premium
instrument, a completed replication or proof of causal channel effects.
