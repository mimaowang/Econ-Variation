---
schema_version: 2
id: china-trip-hybrid-work-eligibility-experiment
name: Trip.com Hybrid Work Eligibility Experiment in Shanghai, 2021-2022
aliases: [Trip.com hybrid work experiment, Bloom Han Liang 2024 hybrid WFH, 携程混合办公资格实验]
status: grounded
provenance:
  task_id: task-1ccde5eae671
scope:
  country: China
  regions: [Shanghai]
  domains: [labor, firms, digital-economy, management, commuting]
  variation_type: pilot-assignment
  knowledge_role: china-variation
  china_relevance: A Shanghai employer assigned hybrid-work eligibility among university-graduate staff. The experiment concerns Chinese employees' retention and workplace outcomes, not a foreign lockdown or a national remote-work policy.
identity:
  instrument: Employer experimental eligibility for hybrid home working rather than compulsory fully remote work
  authority: Trip.com management; researchers analysed employer-collected records
  legal_identifiers: [AEARCTR-0008075, Internal employer experiment rather than public legislation]
  implementation_regime: The final publication concerns Airfare and IT staff in 2021-2022, offered optional Wednesday/Friday home working with the other three weekdays in the office. It differs from the 2010-2011 call-centre four-home-days trial and from the later company-wide rollout.
  assignment_mechanism: The final article and its reporting summary specify odd day-of-month birthdays as eligible and even birthdays as controls. The summary reports a coin flip choosing the eligible parity; this is not a documented independent draw for every employee. Registry text contains conflicting descriptions and is not used to overwrite the final published rule.
  parent: null
  related_variations: [china-ctrip-work-from-home-experiment]
timeline:
  announcement: null
  effective: '2021-08-09'
  implementation_start: 2021
  implementation_end: 2022
  local_timing: Final Methods reports a volunteer cohort starting the week of August 9 and a non-volunteer cohort starting the week of September 13, 2021. Common WFH after a workplace COVID case effectively ended the experimental contrast on January 21, 2022; the attrition figure counts departures through January 23. The registry's planned January 30 end is not the effective exposure end.
  anticipation: Staff were surveyed and invited to volunteer in July 2021. Non-volunteers were notified on September 6 before the second start. Expectations of eventual general rollout can influence controls; exact invitation date is not recovered.
  last_verified: '2026-09-29'
assignment:
  unit: Employee eligibility within two enrolment cohorts
  treated: Odd-birthday employees offered optional Wednesday/Friday WFH under the final published design
  comparison_pool: Even-birthday employees in the same eligible divisions who initially continued office work; compare within the relevant enrolment timing
  rule: Use the final study's eligibility indicator, not voluntary take-up or a policy inferred from employment after the experiment. The published reporting summary confirms the described parity rule; actual personnel assignment records have not been inspected.
  intensity: Binary eligibility; actual home-working days are a separate endogenous uptake measure
  exemptions: [Interns excluded, New hires in probation excluded, Attendance and leave exceptions do not redefine assigned eligibility]
  compliance: Treatment offered an option rather than requiring two home days. Published Methods reports partial uptake and a late common-WFH interruption; do not code every eligible employee as working at home twice every week.
  exposure_construction: Retain employer assignment and cohort start, attach outcomes by permitted anonymized employee key, and define the active contrast only before common eligibility. Birth-date parity reconstructs the published rule only where lawful source identifiers and cohort membership can be verified; published anonymized outcome files are not assumed mutually linkable.
  required_identifiers: [Within-outcome anonymized employee ID, Assigned eligibility indicator, Enrolment cohort and start, Outcome observation or departure date]
  spillovers: Colleagues and managers work together; controls can learn about hybrid work or expect rollout. Company-wide adoption ends the untreated comparison. Later outcomes concern original assignment histories rather than ongoing exclusive eligibility.
research_compatibility:
  outcome_domains: [Employee attrition, Job satisfaction, Performance reviews, Promotions, Software code output]
  affected_populations: [University-graduate engineering marketing and finance staff in Shanghai Airfare and IT divisions]
  mechanism_channels: [Commuting relief, Workplace amenity, Home and office task allocation, Retention, Signalling concerns about volunteering]
  best_for: [Employer eligibility effects on retention during the experiment, Studying uptake and selection separately from assignment]
  not_good_for: [National Chinese remote-work effects, Effects of fully remote work, Treating realized home days as randomly assigned, Unqualified claims of zero productivity effect, Combining this sample with the older call-centre trial]
design:
  claim_type: reduced-form
  affordances: [Employer eligibility allocation, Two enrolment cohorts, Administrative departures, Published balance and uptake descriptions]
  candidate_designs: [Intention-to-treat contrast in experimental attrition, Cohort-specific eligibility comparisons]
  identifying_variation: Eligibility by birthday parity under the reported employer procedure; identification requires comparability of parity groups and a defensible allocation/inference account, not random selection of a representative Chinese workforce
  primary_strategy: Compare experimental-window departure indicators by assigned eligibility, preserving volunteer and non-volunteer cohorts
  estimand: Effect of an offer of hybrid eligibility among the included employees over the specified experimental window; not the effect of two realized home days or a national policy effect
  treatment_variable: Employer eligibility indicator corresponding to odd day-of-month birthdays in the final published design
  comparison_logic: Eligible versus initially ineligible employees within the experimental population; timing and pooled versus cohort-specific estimates must remain explicit
  estimation_notes: The article reports unadjusted two-sided t-tests unless otherwise specified. Its coin-flip parity description is not evidence of 1612 independent random assignment draws; inspect the allocation procedure before constructing design-based inference. Performance equivalence uses stated outcome-specific bounds, not proof of an exactly zero effect or evidence that those bounds were prospectively registered. Actual take-up is not instrumented by this record without additional assumptions.
  assumptions:
  - Birthday-parity groups are comparable for the chosen outcome under the documented allocation procedure; balance tests alone cannot establish this.
  - Departure ascertainment covers assigned participants and follows a common rule in both arms.
  - Cohort start differences and within-team interactions do not silently change the intended eligibility contrast.
  - Post-experiment comparisons require an account of common rollout and treatment-related retention; surviving workers are not automatically the original randomized population.
  diagnostics:
  - Reconcile allocation indicators with final design documentation and registry history before reproducing estimates.
  - Examine baseline balance and volunteer versus non-volunteer results; retain distinct start dates.
  - Compare assigned eligibility with measured uptake and identify the common-WFH break.
  - Track original participants separately from survivors in later reviews or surveys.
  - For null claims state outcome-specific equivalence bounds and confidence intervals, not just a non-significant coefficient.
threats:
- type: conflicting-registration-and-published-allocation
  basis: documented
  condition: The original registry describes both odd and even treatment and a smaller planned sample. Its 2025 changes add publication/data information without reconciling those design fields. Final article and reporting summary agree on the published odd-eligible design; code and personnel allocation have not been inspected.
  evidence_refs: [E1, E2, E3, E4]
  possible_diagnostics: [Registry version comparison, Replication assignment map, Employer protocol clarification, Do not claim a fully aligned preregistration]
- type: uptake-and-selection
  basis: reported
  condition: Volunteering precedes cohort enrolment and home-working uptake is optional. A regression on actual home days can reflect employee preferences rather than assignment.
  evidence_refs: [E2]
  possible_diagnostics: [ITT by cohort, Uptake by assignment and cohort, Separate offer from receipt]
- type: interference-and-common-rollout
  basis: reported
  condition: Staff collaborate within teams and all employees gain WFH access after the workplace COVID event; later company adoption changes the comparison.
  evidence_refs: [E2]
  possible_diagnostics: [Restrict experimental exposure window, Manager/team exposure, Distinguish original assignment from ongoing eligibility]
- type: survivor-outcomes-and-external-validity
  basis: inferred
  condition: Retention can affect who receives later reviews. One employer's graduate staff and outcome proxies do not identify effects for Chinese workers generally.
  evidence_refs: [E2]
  possible_diagnostics: [Original participant denominators, Missing review/survey patterns, Bounds or explicit survivor estimand, Separate code-line count from quality or innovation]
empirical_requirements:
  contract_version: 1
  population: The final article's 1612 included graduate employees in Shanghai Airfare and IT divisions, with interns and probationary new hires excluded
  observation_unit: Employee with experimental-window departure outcome
  geography_level: Shanghai workplace
  time_start: 2021
  time_end: 2022
  minimum_frequency: monthly
  minimum_pre_periods: 0
  minimum_post_periods: 1
  required_fields: [Assigned eligibility, Enrolment cohort and start, Experimental-window departure indicator or departure date, Baseline balance covariates for the intended audit]
  required_identifiers: [Within-outcome anonymized employee ID, Cohort, Observation date or outcome window]
  treatment_key: [Assigned eligibility, Cohort start, Experimental-window end]
  treatment_source: Final article Methods and official reporting summary define published eligibility; lawful employer or replication assignment variables are needed for reproduction. No personnel records or replication code were executed here.
  measurement_risks: [Registry design discrepancy, Volunteering and assignment differ, Monthly extraction does not imply identical follow-up duration, Anonymized outcome files may not share joinable IDs, Departure coding differs from missing reviews, Actual WFH receipt is not assignment]
evidence:
- id: E1
  source_type: implementation-document
  citation: Bloom Han and Liang, Nature Portfolio Reporting Summary accompanying Nature 630, 920-925 (2024).
  url: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-024-07500-2/MediaObjects/41586_2024_7500_MOESM1_ESM.pdf
  date: '2024-06-12'
  supports: [identity.instrument, identity.authority, identity.implementation_regime, identity.assignment_mechanism, timeline.effective, assignment.rule, assignment.treated, assignment.comparison_pool, assignment.exemptions]
  verification_status: verified
  access_level: official-document
  locator: PDF page2 visually inspected2026-09-29, Behavioural and social sciences study design, research sample, sampling strategy, collection, timing, non-participation and randomization boxes. Confirms what the official published design document specifies, including coin flip and odd eligibility; not an independent audit of personnel allocation or executed code.
- id: E2
  source_type: paper
  citation: Bloom Nicholas, Ruobing Han and James Liang.2024. Hybrid working from home improves retention without damaging performance. Nature630,920-925.
  url: https://doi.org/10.1038/s41586-024-07500-2
  date: '2024-06-12'
  supports: [scope.china_relevance, identity.implementation_regime, timeline.local_timing, timeline.anticipation, assignment.rule, assignment.compliance, assignment.exposure_construction, assignment.spillovers, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, design.diagnostics, empirical_requirements.population, empirical_requirements.required_fields, empirical_requirements.measurement_risks, design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year, design_applications.data_used, design_applications.treatment_encoding, threats.condition]
  verification_status: reported
  access_level: full-text
  locator: Publisher HTML Main, The experiment, Discussion; Methods Location and set-up, Randomization, Employee characteristics and balancing tests, Null results, Data sources, Subsamples and Testings; Data/code availability. Inspected2026-09-29. Published effect estimates and execution are source-reported, not independently reproduced.
- id: E3
  source_type: archive
  citation: AEA RCT Registry, AEARCTR-0008075, original version1.0 published August19,2021.
  url: https://www.socialscienceregistry.org/trials/8075/history/98185
  date: '2021-08-19'
  supports: [identity.legal_identifiers, timeline.anticipation, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Full original registry inspected2026-09-29. Submitted August16 after the August9 start; intervention text says odd treatment whereas randomization-method text says even. Planned494 sample and call-centre labels differ from final article. Verifies the historical registered descriptions, not which personnel assignments actually occurred.
- id: E4
  source_type: archive
  citation: AEA RCT Registry, AEARCTR-0008075, version1.1 changes published March27,2025.
  url: https://www.socialscienceregistry.org/trials/8075/history/257247/changes
  date: '2025-03-27'
  supports: [threats.condition, empirical_requirements.measurement_risks]
  verification_status: verified
  access_level: official-document
  locator: Fields Changed and Papers inspected2026-09-29; status/data/code/publication additions listed, with no displayed reconciliation of allocation or planned-sample fields. Compare original and current full registry, not the update date alone.
- id: E5
  source_type: replication
  citation: Harvard Dataverse, Replication Data for Hybrid working from home improves retention without damaging performance, doi10.7910/DVN/6X4ZZL.
  url: https://doi.org/10.7910/DVN/6X4ZZL
  date: '2026-09-29'
  supports: [empirical_requirements.measurement_risks]
  verification_status: blocked
  access_level: metadata
  locator: Repository landing returned an empty HTTP202 response and dataset API HTTP403 on2026-09-29. Author page and article link the deposit; no file inventory, assignment variable, code or replication result inspected. Reopen with legitimately accessible deposit or author-provided materials.
design_applications:
- paper: Bloom Han and Liang, Hybrid working from home improves retention without damaging performance
  doi: 10.1038/s41586-024-07500-2
  journal: Nature
  year: 2024
  research_question: How does offering hybrid working affect employee retention and workplace outcomes?
  population: Shanghai Airfare/IT graduate staff; volunteer and later non-volunteer enrolment
  outcome: Experimental departures; separate survey, review, promotion and software-output outcomes
  data_used: [Employer HR departure and assignment records, Baseline and endline surveys, Half-year reviews and promotions, Daily code output for software engineers]
  treatment_encoding: Original assigned hybrid eligibility; final article specifies odd birthdays. Start dates vary by enrolment cohort; actual uptake and later common access are distinct variables.
  comparison: Initially eligible versus ineligible employees, pooled and cohort/subgroup checks; later outcomes retain original assignment labels
  empirical_design: Employer eligibility experiment analysed principally through differences in group means; outcome-specific equivalence tests for selected null results
  assumptions: [Comparable assignment groups, Outcome ascertainment and attrition accounted for, Optional uptake distinct from offer, Common rollout and survivor populations explicit]
  threats_addressed: [Baseline balance, Volunteer and non-volunteer comparison, Uptake description, Outcome-specific null-equivalence tests, Subgroup and manager-exposure analyses]
  evidence_refs: [E1, E2, E3, E4]
method_transfer: null
readiness_blockers:
- Before numerical reproduction reconcile final eligibility coding with original registry contradictions and accessible code or allocation documentation; no fully aligned prospective preregistration is claimed.
- Obtain lawful outcome-specific data and document anonymized join keys; Harvard deposit content and results were inaccessible on this pass.
- Later review or promotion questions need their own survivor and common-rollout estimand; this default contract covers experimental attrition only.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

This is an employer experiment, not a Chinese policy mandate. Its identity is
fixed by the final published design: a hybrid eligibility offer for graduate
staff, rather than the older call-centre trial's work arrangement [E1]. The
company's operational purpose and measured outcomes are reported by the article
[E2, reported claim]. The related older record is preserved, not merged.

## What Changed

Workers gained an option, not an obligation. Cohort entry and the later common
access break determine the exposure window [E2, reported claim]. A researcher
who uses a single start for everyone or treats later labels as continuing
exclusive eligibility would change the empirical object [analytical inference].

## Implementation and Assignment

The official reporting summary specifies the eligible birthday parity [E1].
That verifies the published protocol, not every employee's actual assignment.
The registry's competing description remains visible [E3; E4]. The final
paper/reporting-summary rule is the recorded application; it is not replaced by
a mixture of registered and final sample counts. A researcher can understand
the offer contrast without being told that the registration discrepancy has
been solved by an uninspected replication package.

## Why This Creates Empirical Variation

An eligibility offer can identify a workplace amenity effect under the stated
comparability conditions. Realized home-working days can instead reflect
preferences and constraints. Moving from offer to receipt requires a separate
argument; random assignment language alone does not supply an exclusion
restriction or validate inference for the parity procedure [analytical inference].

## Identification Risks

Keep changing outcome populations separate from treatment. Departures are an
outcome in the original population, whereas later assessments can exist only
for retained staff [E2, reported claim; analytical inference]. Outcome-specific
equivalence bounds support bounded statements, not proof that every dimension
of productivity is unaffected. Team spillovers and general adoption likewise
limit comparisons with an entirely untreated workplace [analytical inference].

## Data Requirements

The default contract is deliberately for experimental departures. Survey,
review and daily-output questions need different observation windows and
outcome availability; do not union their fields into mandatory requirements.
Anonymized records need an explicit linkage account, not an assumed shared ID
across files [E2, reported claim; analytical inference]. No data assets are
copied into this repository.

## Evidence Notes

Grounded means the final published instrument and comparison can be recovered,
with conditional use, not that the allocation was independently audited.
E1 supports the final design description; E2 reports its application. E3-E4
preserve the historical registration discrepancy. E5 remains inaccessible.
The record does not certify numerical replication, prospective alignment,
national external validity, or a new outcome's identification.
