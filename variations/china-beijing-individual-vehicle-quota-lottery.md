---
schema_version: 2
id: china-beijing-individual-vehicle-quota-lottery
name: Beijing Individual Vehicle-Ownership Quota Lottery
aliases:
- Beijing license plate lottery
- 北京小客车个人指标摇号
status: grounded
provenance:
  task_id: task-0c52f9d806cb
scope:
  country: China
  regions: [Beijing, mainland China]
  domains: [urban-economics, transport-economics, environmental-economics, household-economics]
  variation_type: other
  knowledge_role: china-variation
  china_relevance: Beijing residents face randomized allocation of ordinary passenger-car purchase/registration quotas; winner status provides the inspected Chinese urban travel application.
identity:
  instrument: Individual ordinary passenger-car quota allocation by lottery, not weekday road-use restrictions or a household car-ownership ban.
  authority: Beijing municipal government and passenger-car quota management office, coordinated by the transport commission.
  legal_identifiers: [北京市人民政府令第227号, 京交发〔2010〕3号, 京交发〔2011〕5号, 京交发〔2013〕160号]
  implementation_regime: >
    This record follows individual ordinary-quota draws during2011-2014,
    including the documented2014 probability and renewal changes. Corporate
    quotas, commercial vehicles, replacement quotas and separate new-energy
    allocation are outside its assignment pool. Later family allocation is
    not interchangeable with this historical regime.
  assignment_mechanism: >
    Eligible application codes enter computerized draws. Original individual
    draws are monthly. From2014 draws are bimonthly and odds depend on
    accumulated unsuccessful draws, with separate C5-driver weights.
    Randomness is within the relevant draw and probability class, not
    unconditional equality across all people who ever applied.
  parent: null
  related_variations: [china-beijing-2008-private-car-driving-restriction-subway-premium]
timeline:
  announcement: '2010-12-23'
  effective: '2010-12-23'
  implementation_start: '2011-01-01'
  implementation_end: null
  local_timing: Applications begin January1,2011; original draws occur on the26th. Renewal amendments apply January1,2012; weighted/bimonthly rules apply January1,2014. The application ends with the2014 survey, not termination of the policy.
  anticipation: Pre-existing registered vehicles and qualifying pre-rule purchase contracts follow separate rules; an announcement-date citywide DID is not the entrant lottery comparison.
  last_verified: '2026-10-04'
assignment:
  unit: Eligible individual application code within a draw and probability class.
  treated: Individual entrant allocated an ordinary quota by the outcome observation date.
  comparison_pool: Unsuccessful individual ordinary-quota entrants with comparable entry and active-draw histories, within the same probability rules.
  rule: >
    Applicants need a valid driving licence, no Beijing-registered passenger
    car in their own name, and qualifying residence. Residence includes
    Beijing hukou, specified military categories, qualified residents from
    abroad, work-residence permit holders and qualifying nonlocal residents
    with the required tax/social-insurance history. Eligibility and entry
    are not randomized; an eligible household can contain multiple entrants.
  intensity: >
    Before2014 the code participates in the relevant monthly pool. From2014
    ordinary weights are1 for up to24 unsuccessful draws,2 for25-36,3 for
    37-48, increasing thereafter; C5 weights start at2 and increase similarly.
    Quota totals and pool size also vary. Never assign a constant citywide
    winning probability or infer active draws solely from first entry.
  exemptions:
  - Replacement after selling or scrapping an existing registered vehicle does not require a new lottery win.
  - Commercial-use quotas and specified pre-rule contracts/property transfers are separately governed.
  - Corporate application eligibility and code counts differ; do not pool firms with individual entrants.
  compliance: Winning grants a nontransferable quota valid for six months in the inspected rules; expiry is possible. Registration/purchase is take-up, not the randomized assignment.
  exposure_construction: >
    Link entrant ID, first entry, observed win date and survey date; define
    winning by that date, not future eventual success. Link household IDs
    for car stock and member outcomes. For renewed or weighted draws,
    recover active participation, cumulative failures and C5 eligibility;
    otherwise disclose continuous-participation assumptions and conduct
    restricted-cohort sensitivity. Do not recode any-household-win as the
    individual instrument or discard nonpurchasing winners.
  required_identifiers: [entrant_id, household_id, entry_month, win_date, survey_date, district_id]
  spillovers: Multiple entrants share household vehicles; lending and externally registered cars can weaken the car-stock first stage and change interference/exclusion conditions.
research_compatibility:
  outcome_domains: [Travel modes, Commuting, Vehicle ownership, Household mobility]
  affected_populations: [Eligible Beijing individual lottery participants and their households]
  mechanism_channels: [Access to vehicle registration, Car acquisition, Travel-mode substitution, Household mobility constraints]
  best_for: [Entrant-level mobility questions with documented lottery history and linked outcomes.]
  not_good_for:
  - Treating all Beijing residents or all households as randomly assigned vehicle owners.
  - Identifying nationwide development or aggregate congestion effects without additional evidence and modelling.
design:
  claim_type: reduced-form
  affordances: [Computerized quota allocation, Entry cohorts, Noncompliance distinguishable from winning]
  candidate_designs: [Entry-cohort reduced form, Winner-status IV for household cars]
  identifying_variation: Individual winning within comparable entry histories and draw probabilities; selection into applying is outside randomization.
  primary_strategy: JEEM equations1-3 compare entrants with entry-month effects and use winning to instrument household car stock.
  estimand: Effect of receiving a quota among entrants; car-stock IV additionally needs exclusion and monotonicity and is local to induced acquisition.
  treatment_variable: Won an ordinary quota by observation date; household car stock is endogenous take-up.
  comparison_logic: Compare winners with unsuccessful entrants, not participants with nonparticipants or car owners with nonowners.
  estimation_notes: The paper uses age, sex, education and diary-day controls; IV tables cluster by district. Entry-month controls alone need scrutiny when renewal histories or2014 probability classes differ.
  assumptions:
  - Conditional draw assignment is preserved and entrant/win histories are measured accurately.
  - Outcome observation and continuing participation do not induce unaddressed selective samples.
  - IV requires winning to affect the chosen outcome through the specified vehicle channel, with appropriate monotonicity and household interference assumptions.
  diagnostics:
  - Test predetermined balance within comparable cohorts; inspect actual draw counts, renewal lapses and C5 weights.
  - Inspect the first stage without dropping nonpurchasers, and compare entrant-level versus household-level constructions.
  - Assess missing diary outcomes, household dependence and inference with only16 districts; balance and a strong first stage do not prove exclusion.
threats:
- type: dynamic_probability_and_participation
  basis: documented
  condition: Renewal is required from2012;2014 changes both frequency and probability weights. Equal first-entry month need not imply equal actual chances.
  evidence_refs: [E3, E4]
  possible_diagnostics: [Recover active-draw histories, Condition on rule classes, Restrict observation before weighted allocation where feasible]
- type: assignment_take_up_and_interference
  basis: inferred
  condition: Quota expiry, household sharing and alternative vehicle access separate winning from car stock; psychological or option-value channels can violate a car-stock-only IV exclusion restriction.
  evidence_refs: [E1, E5]
  possible_diagnostics: [Separate reduced form from IV, Recover all household entrants, Examine alternative vehicle access and direct winning channels]
- type: selected_population_and_measurement
  basis: reported
  condition: Applicant histories are recalled and survey/table sample counts differ. The2014 diary does not directly measure citywide emissions or general-equilibrium congestion.
  evidence_refs: [E5]
  possible_diagnostics: [Reconcile analysis exclusions, Validate histories with lawful administrative linkage if available, Avoid extrapolation without explicit assumptions]
empirical_requirements:
  contract_version: 1
  population: Beijing individual ordinary-quota entrants with linked household and outcome observations.
  observation_unit: individual entrant at survey observation
  geography_level: Beijing district and household
  time_start: 2011
  time_end: 2014
  minimum_frequency: dated assignment history plus outcome survey
  minimum_pre_periods: 0
  minimum_post_periods: 1
  required_fields:
  - Entry and win dates, survey date, active-draw/renewal history, probability class and ordinary-quota type.
  - Household car stock and purchase dates for IV; entrant covariates and district identifiers.
  - Dated travel diary with mode, duration and origin/destination zones for the inspected travel application.
  required_identifiers: [entrant_id, household_id, entry_month, win_date, survey_date, district_id]
  treatment_key: [entrant_id, survey_date]
  treatment_source: Lawful original lottery history or survey-reported entry/win history; official rules establish allocation but do not provide an outcome-linked public roster.
  measurement_risks:
  - No public outcome-linked microdata or replication code was inspected; obtain lawful access before promising execution.
  - Generic household panels without entry/win history cannot recover the instrument.
  - First-entry month does not establish renewal continuity; district aggregates cannot reproduce entrant assignment.
evidence:
- id: E1
  source_type: policy-document
  citation: 北京市人民政府令第227号, original2010 北京市小客车数量调控暂行规定.
  url: https://sfj.beijing.gov.cn/sfj/index/483217/517312/index1.html
  date: '2010-12-23'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, timeline.announcement, timeline.effective, assignment.rule, assignment.compliance, assignment.exemptions]
  verification_status: verified
  access_level: official-document
  locator: Original historical text, articles1-11, especially3-6 and9, inspected2026-10-04; not later consolidated amendments.
- id: E2
  source_type: implementation-document
  citation: 京交发〔2010〕3号, original implementation rules.
  url: https://jtgl.beijing.gov.cn/jgj/jgxx/94246/95332/140920/
  date: '2010-12-23'
  supports: [identity.implementation_regime, identity.assignment_mechanism, timeline.implementation_start, timeline.local_timing, timeline.anticipation, assignment.unit, assignment.rule, assignment.exemptions, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: Articles3-10 and13-17,22-23 inspected2026-10-04; individual versus corporate pools, eligibility, monthly26th draw, carryover, six-month use, replacement and transition.
- id: E3
  source_type: implementation-document
  citation: 京交发〔2011〕5号, implementation rules effective2012.
  url: https://jtw.beijing.gov.cn/xxgk/tzgg/201112/t20111230_1274711.html
  date: '2011-12-27'
  supports: [identity.legal_identifiers, timeline.local_timing, assignment.rule, assignment.exposure_construction]
  verification_status: verified
  access_level: official-document
  locator: Notice and articles15-18,27 inspected2026-10-04; article16 establishes three-month code retention and renewal. Publication date is December30.
- id: E4
  source_type: implementation-document
  citation: 京交发〔2013〕160号, rules effective2014.
  url: https://www.beijing.gov.cn/zhengce/zhengcefagui/201905/t20190522_57824.html
  date: '2013-11-27'
  supports: [identity.legal_identifiers, identity.assignment_mechanism, timeline.local_timing, assignment.intensity, assignment.exposure_construction]
  verification_status: verified
  access_level: official-document
  locator: Notice and articles5,9,14-17 inspected2026-10-04; bimonthly frequency, cumulative-failure weights including C5 and six-month renewal. Current rule-page invalidity does not erase historical application.
- id: E5
  source_type: paper
  citation: Yang, Jun, Antung A. Liu, Ping Qin and Joshua Linn. JEEM99(2020),102269, final typeset article.
  url: https://ae.ruc.edu.cn/docs/2020-09/641be7ed6683454ca1548608c3fcb2a5.pdf
  date: 2020
  supports: [design.primary_strategy, design.estimation_notes, design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year, design_applications.population, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design, empirical_requirements.required_fields, empirical_requirements.measurement_risks]
  verification_status: reported
  access_level: full-text
  locator: Printed pp3-9 Sections2-5, equations1-3, Tables1-6; pp12-14 Appendix Tables1-5 inspected in memory2026-10-04. Identity/DOI onp1; Section6 opening distinguishes partial equilibrium. No PDF or microdata stored and no replication executed.
- id: E6
  source_type: implementation-document
  citation: 北京市小客车指标调控管理办公室,2011 implementation-rule explanation.
  url: https://www.beijing.gov.cn/zhengce/zcjd/201905/t20190523_77106.html
  date: '2011-12-30'
  supports: [identity.assignment_mechanism, assignment.exposure_construction]
  verification_status: verified
  access_level: official-document
  locator: SectionsI andII(2), III(2), inspected2026-10-04; computerized seed/draw procedure and transitional renewal dates. This verifies official procedure documentation, not an independent audit of every realized draw.
- id: E7
  source_type: paper
  citation: DOI printed on the final JEEM2020 article title page.
  url: https://doi.org/10.1016/j.jeem.2019.102269
  date: 2020
  supports: [design_applications.doi, design_applications.paper, design_applications.journal, design_applications.year]
  verification_status: reported
  access_level: metadata
  locator: DOI, authors and journal citation inspected onp1 of E5; identity reference, not a claim that the DOI landing page supplies empirical methods.
design_applications:
- paper: 'The effect of vehicle ownership restrictions on travel behavior: Evidence from the Beijing license plate lottery'
  doi: 10.1016/j.jeem.2019.102269
  journal: Journal of Environmental Economics and Management
  year: 2020
  research_question: Does quota allocation change household vehicles and travel?
  population: Individual entrants in the2014 Beijing household travel survey.
  outcome: Vehicle stock, travel modes, distance and commuting.
  data_used: [2014 BTRC household survey, Added lottery histories, 24-hour travel diaries]
  treatment_encoding: Individual win by survey; household cars instrumented with winning.
  comparison: Entrants conditional on entry month.
  empirical_design: Reduced form and two-stage least squares.
  assumptions: [Conditional allocation, Additional IV exclusion and monotonicity]
  threats_addressed: [Predetermined balance, Entry-cohort balance, First-stage strength]
  evidence_refs: [E5, E7]
method_transfer: null
readiness_blockers:
- Obtain lawful entrant/outcome microdata and reconcile analysis exclusions; no executed or turnkey replication is claimed.
- Verify renewal continuity and2014 probability classes before treating entry-month conditioning as sufficient.
- Justify outcome-specific exclusion, household interference and inference; only the allocation mechanism is grounded, not every proposed causal interpretation.
---

## Institutional Background

Beijing restricted additions to its passenger-car fleet through free quota
allocation. The administrative unit is an individual application code, not
a household. A person without a car registered in their own name can qualify
even when another household member owns one. Replacement rights explain why
existing owners are not simply untreated lottery losers [E1-E2].

## What Changed

Registration access became conditional on obtaining an appropriate quota.
Winning is an offer of registration access; a six-month use window does not
force purchase. This is distinct from restrictions on when an already owned
vehicle may use the road [E1-E2].

## Implementation and Assignment

The allocation remains a lottery, but its probability classes are historical.
Original codes roll forward;2012 introduces renewal, and2014 weights repeated
failures and C5 applicants while reducing draw frequency [E2-E4]. Recording
these changes within this ordinary-quota mechanism does not merge corporate,
electric-vehicle or later family allocation into the same risk set.

## Why This Creates Empirical Variation

Official documentation describes computerized allocation [E6]. Random
allocation operates after selection into an eligible pool. It therefore does
not validate comparisons between applicants and nonapplicants. The inspected
paper uses entrant comparisons rather than a citywide policy timing contrast
[E5, reported].

## Identification Risks

More chances to draw mean a different cumulative probability of winning.
First-entry date is insufficient if renewal lapses or probability classes
differ. A new application should recover those histories or make its
restrictions and continuity assumptions explicit [E3-E4; analytical inference].
For car-stock IV, an allocated option can also affect expectations or borrowing
before purchase; institutional randomness alone does not establish exclusion.

## Data Requirements

Entrant identity links allocation to an outcome observation; household identity
links vehicles and member outcomes without replacing the individual assignment.
An outcome-only city or household panel cannot reconstruct this instrument.
Survey access is a practical condition, not evidence that the institutional
allocation is unknown. Travel outcomes require their own diary definitions.

## Evidence Notes

Grounded means the historical institution, probability changes and paper-used
comparison are recoverable. It does not certify the paper's pooled conditioning
as sufficient or assert public data availability. Rule texts were inspected at
their historical dates, not substituted with today's consolidated regulations.
