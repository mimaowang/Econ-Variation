---
schema_version: 2
id: china-ctrip-work-from-home-experiment
name: Ctrip Work-From-Home Randomized Experiment
aliases:
- Ctrip WFH experiment
- Bloom et al. (2015) Chinese WFH RCT
- Ctrip call-center telecommuting pilot
status: extracted
provenance:
  task_id: task-1c857590bd30
scope:
  country: China
  regions:
  - Shanghai
  domains:
  - labor
  - firms
  - productivity
  - urban-economics
  - management
  variation_type: pilot-assignment
  knowledge_role: china-variation
  china_relevance: The experiment was run by Ctrip, a NASDAQ-listed Chinese travel agency,
    in its Shanghai call center. It is a China-specific randomized firm-level intervention
    that generates clean variation in work location, useful for studying productivity,
    labor supply, attrition, promotion, and work-life balance in a Chinese urban labor
    market.
identity:
  instrument: A nine-month randomized pilot in which eligible Ctrip call-center employees
    who volunteered to work from home four days a week were randomly assigned either
    to work from home (treatment) or to remain in the office (control).
  authority: Ctrip International Corporation (NASDAQ-listed Chinese travel agency);
    Ctrip senior management and human-resources/IT departments; the public lottery
    was conducted by Ctrip Chairman James Liang.
  legal_identifiers:
  - Internal corporate experiment; no public statute or regulation
  implementation_regime: The pilot covered the airfare and hotel booking departments
    of Ctrip's Shanghai call center. Eligible volunteers worked four shifts per week
    from home and one shift in the office on a fixed weekday; control employees worked
    all five shifts in the office. Both groups kept the same team schedule, pay structure,
    CTrip-provided equipment, and centrally routed workflow.
  assignment_mechanism: Random assignment by public lottery based on even or odd birth
    dates among the 249 eligible volunteers. Employees with even birth dates were assigned
    to work from home; those with odd birth dates formed the control group.
  parent: null
  related_variations: []
timeline:
  announcement: '2010-11-01'
  effective: '2010-12-06'
  implementation_start: 2010
  implementation_end: 2011
  local_timing: Employees were informed in early November 2010. The public lottery
    was held one week before the start date. The experiment ran from December 6, 2010
    to August 15, 2011. A firm-wide rollout to qualified volunteers in the same departments
    began on September 1, 2011.
  anticipation: Participants knew the experiment would last nine months and that the
    firm would use the results to decide on a wider rollout, but they did not learn
    the rollout decision until August 15, 2011.
  last_verified: '2026-07-14'
assignment:
  unit: Individual-employee by day or week during the experiment.
  treated: Eligible volunteers assigned an even birth date who were instructed to work
    four of five weekly shifts from home.
  comparison_pool: Eligible volunteers assigned an odd birth date who continued to
    work all shifts in the office. The design also uses eligible employees in Ctrip's
    Nan Tong call center and eligible non-volunteers in Shanghai as quasi-control groups.
  rule: Among the 249 eligible volunteers, those with even-numbered birth dates were
    selected into treatment and those with odd-numbered birth dates into control.
  intensity: Binary treatment assignment, with actual work-from-home compliance around
    80-90 percent during the experiment.
  exemptions: []
  compliance: High but not perfect. IT systems tracked login locations and team leaders
    policed compliance; the paper reports 80-90 percent of the treatment group worked
    from home during the experiment and uses even-birthdate status as an intention-to-treat
    instrument.
  exposure_construction: Create an indicator equal to one for employees with an even
    birth date during the December 6, 2010 to August 15, 2011 experimental period.
    Estimate intention-to-treat effects using employee fixed effects and weekly time
    dummies, comparing treated and control employees before and during the experiment.
  required_identifiers:
  - employee ID
  - birth date (for assignment)
  - team / department
  - shift date
  - work location (home or office)
  spillovers: Within-team spillovers are limited because tasks are individually allocated
    by a central server and there is no group-based pay. The paper checks for demoralization
    of the control group by comparing it with the Nan Tong call-center group and eligible
    non-volunteers and finds no negative spillover.
research_compatibility:
  outcome_domains:
  - productivity
  - labor-supply
  - job-attrition
  - promotion
  - job-satisfaction
  - work-life-balance
  - commuting
  - service-quality
  - management-practices
  affected_populations:
  - Ctrip Shanghai call-center employees
  - airfare and hotel booking staff
  - younger urban workers with measurable output
  mechanism_channels:
  - reduced commuting time and cost
  - quieter home working environment
  - fewer breaks and sick days
  - reduced direct supervision
  - social isolation and loneliness
  - perceived promotion concerns
  - learning and selection effects after rollout
  best_for:
  - Estimating causal effects of working from home on call-center productivity and
    labor supply
  - Studying firm-level adoption of flexible work arrangements in China
  - Analyzing selection effects when employees can later choose their work location
  not_good_for:
  - Generalizing to knowledge workers whose output is hard to measure
  - Estimating economy-wide effects of remote-work policies
  - Settings where employees self-select treatment without a randomized assignment
  - Long-run career dynamics beyond the two-year follow-up window
design:
  claim_type: causal
  affordances:
  - Randomized treatment assignment within a large Chinese firm
  - High-frequency administrative performance data from Ctrip's central IT system
  - Pre-experiment baseline data and parallel trends between treatment and control
  - Comparable quasi-control groups (Nan Tong call center and eligible non-volunteers)
  - Post-experiment reselection phase reveals learning and selection effects
  candidate_designs:
  - Randomized controlled experiment comparing treatment and control employees
  - Difference-in-differences using pre-experiment baseline and employee fixed effects
  - Robustness checks using Nan Tong eligible employees and eligible non-volunteers
    as alternative control groups
  - Event-study plots around the December 2010 treatment start
  identifying_variation: Random assignment to work-from-home status among eligible
    volunteers in the same departments and teams.
  primary_strategy: Randomized experiment / intention-to-treat with employee fixed
    effects and weekly time dummies.
  estimand: The intention-to-treat effect of being assigned to work four days per week
    from home for nine months on call-center performance, labor supply, attrition,
    promotion, and job satisfaction.
  treatment_variable: An indicator for even birth date interacted with the experimental
    period (December 6, 2010 to August 15, 2011).
  comparison_logic: Compare eligible volunteers randomly assigned to work from home
    with eligible volunteers assigned to the office; use additional quasi-control groups
    to rule out control-group demoralization.
  estimation_notes: Employee fixed effects absorb permanent worker heterogeneity; weekly
    time dummies absorb seasonality and demand shocks; cluster standard errors at the
    employee or team level. Because the intervention is randomized, a simple treatment-control
    difference yields a similar estimate to the difference-in-differences specification.
  assumptions:
  - Randomization was implemented as intended and balanced observables across treatment
    and control.
  - Compliance is non-differential or is handled by intention-to-treat interpretation.
  - The control group was not demoralized by losing the lottery (checked against Nan
    Tong and non-volunteers).
  - Performance measures from Ctrip's central server are accurate and comparable across
    locations.
  - No coincident firm-wide policy change differentially affected treated and control
    teams during the experiment.
  diagnostics:
  - Balance table on pre-experiment employee characteristics
  - Event-study plots of performance before and during the experiment
  - Comparison of control group with Nan Tong eligible employees and eligible non-volunteers
  - Lee (2009) bounds for attrition bias
  - Robustness to alternative performance measures and sample restrictions
threats:
- type: attrition-bias
  basis: reported
  condition: Worse-performing employees were more likely to quit in both groups, and
    quit rates were higher in the control group, which could bias the estimated treatment
    effect downward.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Lee bounds on treatment effects
  - Compare attrition patterns across treatment and control
  - Sensitivity of estimates to sample selection corrections
- type: selection-into-volunteering
  basis: reported
  condition: Only about half of eligible employees volunteered, and volunteers differed
    from non-volunteers in commute length, tenure, and family structure. The experimental
    estimates are local to the volunteer population.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Compare treatment effects for volunteers with different observable characteristics
  - Interpret estimates as LATE for the volunteer population
  - Use non-volunteer eligible employees as an external validity check
- type: external-validity
  basis: inferred
  condition: The results come from call-center employees with easily measured output;
    they may not generalize to other occupations, industries, or to mandatory remote-work
    policies.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Replicate in other occupations or datasets
  - Compare with later hybrid-WFH experiments (e.g., Bloom, Han & Liang 2024)
  - Bound external validity by job-task characteristics
- type: imperfect-compliance
  basis: reported
  condition: 10-20 percent of the treatment group did not work from home on a given
    day because of equipment failures, apartment moves, or other logistical issues.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Report intention-to-treat and treatment-on-the-treated estimates
  - Use birth-date assignment as an instrument for actual work location
  - Check that returns to the office were effectively random
- type: spillover-within-team
  basis: inferred
  condition: Although tasks are individually allocated, team members share a team
    leader and physical proximity; control employees could be affected by treatment
    group behavior or morale.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Compare control group with employees outside the experiment (Nan Tong and non-volunteers)
  - Test for changes in control-group performance before and after randomization
  - Include team fixed effects or team-level spillover terms
empirical_requirements:
  contract_version: 1
  population: Call-center employees in Ctrip's Shanghai airfare and hotel booking departments
    during 2010-2011.
  observation_unit: Employee-day or employee-week.
  geography_level: Firm / call center (Shanghai).
  time_start: 2010
  time_end: 2012
  minimum_frequency: daily
  minimum_pre_periods: 11
  minimum_post_periods: 8
  required_fields:
  - employee identifier
  - team / department
  - birth date (for treatment assignment)
  - work location (home or office)
  - shift date
  - phone calls answered
  - minutes logged in
  - orders taken
  - conversion rate
  - call quality score
  - attrition indicator
  - promotion indicator
  - commuting time
  - survey-based job satisfaction
  - demographics
  required_identifiers:
  - employee ID
  - shift date
  treatment_key:
  - employee ID
  - birth date parity
  - experiment-period indicator
  treatment_source: Ctrip administrative HR/IT records and the public lottery assigning
    even/odd birth dates to treatment/control.
  measurement_risks:
  - Performance metrics are proprietary and may not be available outside Ctrip.
  - Call quality scores are based on a 1 percent random sample of calls.
  - Self-reported surveys may be affected by treatment-related reporting bias.
  - Birth-date parity is a coarse randomization device; verify balance and no manipulation.
  - Post-experiment reselection confounds long-run effects with employee learning.
evidence:
- id: E1
  source_type: paper
  citation: 'Bloom, Nicholas, James Liang, John Roberts, and Zhichun Jenny Ying. 2015.
    "Does Working from Home Work? Evidence from a Chinese Experiment." The Quarterly
    Journal of Economics 130(1): 165-218.'
  url: https://doi.org/10.1093/qje/qju032
  date: 2015
  supports:
  - identity
  - timeline
  - design
  verification_status: reported
  access_level: abstract
  locator: QJE article abstract and citation (DOI 10.1093/qje/qju032)
- id: E2
  source_type: paper
  citation: 'Bloom, Nicholas, James Liang, John Roberts, and Zhichun Jenny Ying. 2013.
    "Does Working from Home Work? Evidence from a Chinese Experiment." NBER Working
    Paper No. 18871.'
  url: https://www.nber.org/system/files/working_papers/w18871/w18871.pdf
  date: 2013
  supports:
  - identity
  - timeline
  - assignment
  - design
  - threats
  - empirical_requirements
  - design_applications
  verification_status: verified
  access_level: full-text
  locator: NBER Working Paper 18871 PDF, Sections II.A-B, III.A-C, IV.A-B and Tables
    2-4
design_applications:
- paper: 'Does Working from Home Work? Evidence from a Chinese Experiment'
  doi: 10.1093/qje/qju032
  journal: The Quarterly Journal of Economics
  year: 2015
  research_question: What is the causal effect of working from home on employee performance,
    labor supply, attrition, promotion, and job satisfaction in a Chinese call center?
  population: Eligible volunteers in the airfare and hotel booking departments of Ctrip's
    Shanghai call center.
  outcome: Weekly phone calls answered, minutes on the phone, calls per minute, overall
    performance z-score, conversion rate, call quality score, attrition, promotion,
    job satisfaction, and psychological attitude scores.
  data_used:
  - Ctrip administrative HR and performance database
  - Daily performance records from January 2010 onward
  - Internal employee surveys (November 2010 and August 2011)
  - Author-conducted surveys and interviews
  treatment_encoding: Indicator for even birth date interacted with the experimental
    period; actual work location used for treatment-on-the-treated estimates.
  comparison: Randomized treatment versus control among eligible volunteers; robustness
    checks compare the control group with eligible employees in the Nan Tong call center
    and eligible non-volunteers in Shanghai.
  empirical_design: Randomized controlled experiment with employee fixed effects and
    weekly time dummies; difference-in-differences using pre-experiment baseline.
  assumptions:
  - Random assignment was implemented as intended.
  - Birth-date parity is independent of potential outcomes.
  - No differential firm-level shocks during the experiment.
  threats_addressed:
  - Control-group demoralization checked using Nan Tong and non-volunteer comparison
    groups
  - Attrition bias addressed with Lee bounds
  - Quality-quantity tradeoff checked with conversion and call-quality measures
  - Spillovers within teams minimized by individual task allocation and tested empirically
  evidence_refs:
  - E1
  - E2
method_transfer: null
readiness_blockers:
- "Paper-only primary institutional evidence: the experiment was an internal corporate
  pilot, and independent Chinese-language corporate records (internal memos, lottery
  protocol, HR/IT documentation) have not been accessed."
- The exact variable definitions and robustness checks from the published QJE article
  should be cross-verified against the NBER working paper and any replication package.
- Access to Ctrip administrative data is proprietary; researchers would need a partnership
  or similar firm data to reuse the design.
---
---
## Institutional Background

Ctrip International Corporation was a leading NASDAQ-listed Chinese travel agency with about 16,000 employees at the time of the experiment. Its Shanghai call center handled airline and hotel bookings mainly by telephone because of lower Internet penetration in China. Senior management were interested in allowing call-center employees to work from home to save office rental costs and reduce high attrition, but feared shirking without direct supervision. Because no precedent existed among Chinese firms, Ctrip decided to run a randomized controlled trial [E2].

## What Changed

In the pilot, 996 employees in the airfare and hotel departments of the Shanghai call center were asked whether they wanted to work from home four days a week. About half (503) volunteered, and 249 met eligibility criteria (at least six months tenure, home broadband, and a private workspace). A public lottery assigned employees with even birth dates to work from home and those with odd birth dates to the control group. Treatment employees worked four shifts at home and one shift in the office on a fixed day; controls worked all five shifts in the office. Both groups kept the same team schedule, pay structure, equipment, and centrally routed workflow [E2].

## Implementation and Assignment

The experiment started on December 6, 2010 and ended on August 15, 2011. Assignment was fixed for the full nine months, except for a small number of equipment or housing issues. Compliance was high: 80-90 percent of treatment employees worked from home during the experiment. The IT department policed login locations, and team leaders supervised treatment employees on the one office day per week. Estimates use even-birthdate status as an intention-to-treat instrument [E2].

## Why This Creates Empirical Variation

The random assignment creates a clean comparison between employees who work from home and otherwise identical employees who remain in the office, holding job tasks, pay, technology, and workflow constant. The administrative data include high-frequency performance, labor supply, attrition, promotion, and survey measures. The post-experiment rollout also allows researchers to study learning and selection effects, because employees could reselect their work location [E1; E2].

## Identification Risks

The main risks are (i) differential attrition between treatment and control, which the paper shows biases estimates downward; (ii) limited external validity to occupations other than call-center work; (iii) selection into volunteering, so the experimental estimates are local to volunteers; (iv) imperfect compliance with the assigned work location; and (v) potential spillovers or morale effects within teams, which the paper addresses with quasi-control groups from Nan Tong and eligible non-volunteers [E2].

## Data Requirements

The canonical design requires matched employee-level administrative data on work location, shift timing, performance, labor supply, attrition, promotions, and demographics, plus survey measures of job satisfaction and commuting. The original data are proprietary to Ctrip [E2].

## Evidence Notes

The primary source is Bloom et al. (2015, *Quarterly Journal of Economics*), with bibliographic details from the publisher abstract (E1). Institutional and design details were verified from the NBER Working Paper 18871 PDF (E2), which contains the full experimental protocol, balance checks, and results [E1; E2].
