---
schema_version: 2
id: china-ctrip-work-from-home-experiment
name: Ctrip Work-From-Home Randomized Experiment
aliases:
- Ctrip WFH experiment
- Bloom et al. (2015) Chinese WFH RCT
- Ctrip call-center telecommuting pilot
status: grounded
provenance:
  task_id: task-52aecbc523a7
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
    that assigns work-location eligibility among volunteers, useful for studying productivity,
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
  - AEARCTR-0000276; registry version 1.0 (10.1257/rct.276-1.0), registered retrospectively on April 12, 2017
  implementation_regime: The pilot covered the airfare and hotel booking departments
    of Ctrip's Shanghai call center. Eligible volunteers worked four shifts per week
    from home and one shift in the office on a fixed weekday; control employees worked
    all five shifts in the office. Both groups kept the same team schedule, pay structure,
    CTrip-provided equipment, and centrally routed workflow.
  assignment_mechanism: One public urn draw chose which pre-existing day-of-month birthday
    parity received WFH eligibility among 249 qualified volunteers. The draw selected even
    parity (131 employees); odd parity (118) remained in office. This is not 249 independent
    employee-level random draws, notwithstanding the registry's individual-level label.
  parent: null
  related_variations:
  - china-trip-hybrid-work-eligibility-experiment
timeline:
  announcement: null
  effective: '2010-12-06'
  implementation_start: 2010
  implementation_end: 2011
  local_timing: Employees were informed in early November 2010; the paper does not
    report the exact announcement day; it is left unknown rather than encoded as November 1.
    The public lottery was held one week before the start date.
    The experiment ran from December 6, 2010 to mid-August 2011. The published
    regression tables define the experimental period as ending August 14, 2011,
    while the NBER working paper and the announcement narrative use August 15, 2011.
    Employees were told on August 15, 2011 that the experiment had succeeded, and
    the option was rolled out on September 1, 2011 to qualified employees who wanted
    it in the airfare and hotel booking departments; the published abstract describes
    the subsequent rollout as firm-wide.
  anticipation: Participants knew the experiment would last nine months and that the
    firm would use the results to decide on a wider rollout, but they did not learn
    the rollout decision until August 15, 2011.
  last_verified: '2026-10-03'
assignment:
  unit: Individual-employee by day or week during the experiment.
  treated: Eligible volunteers with an even day-of-month birthday who were instructed to work
    four of five weekly shifts from home.
  comparison_pool: Eligible volunteers assigned an odd birth date who continued to
    work all shifts in the office. The design also uses eligible employees in Ctrip's
    Nan Tong call center and eligible non-volunteers in Shanghai as quasi-control groups.
  rule: Employees volunteered and needed at least six months of tenure, home broadband,
    and their own workspace. Among the 249 qualified volunteers, one public urn draw
    assigned the even day-of-month birthday group to WFH and the odd group to office.
  intensity: Binary treatment assignment, with actual work-from-home compliance around
    80-90 percent during the experiment.
  exemptions: []
  compliance: High but not perfect. IT systems tracked login locations and team leaders
    policed compliance; the paper reports 80-90 percent of the treatment group worked
    from home during the experiment and uses even-birthdate status as an intention-to-treat
    instrument.
  exposure_construction: Create an indicator equal to one for employees with an even
    birth date during the experimental period (December 6, 2010 to August 14, 2011
    in the published regression tables).
    Estimate intention-to-treat effects using employee fixed effects and weekly time
    dummies, comparing treated and control employees before and during the experiment.
  required_identifiers:
  - employee ID
  - day-of-month birthday parity or recorded treatment assignment
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
    period (December 6, 2010 to August 14, 2011 in the published tables; the NBER
    working paper narrates the end date as August 15, 2011).
  comparison_logic: Compare eligible volunteers randomly assigned to work from home
    with eligible volunteers assigned to the office; use additional quasi-control groups
    to rule out control-group demoralization.
  estimation_notes: Published Table II and replication Table 2 use employee fixed effects,
    week dummies, and employee-clustered standard errors (personid); the experimental-only
    comparison omits employee fixed effects. The script excludes transition week 201049.
    Birthday groups, not individual employees, were switched by one lottery, so employee
    clustering handles repeated observations but does not reproduce an independently
    randomized 249-person allocation. Interpret inference conditional on the parity
    comparison being credible and assess baseline balance, pre-trends, and interference.
  assumptions:
  - Randomization was implemented as intended and balanced observables across treatment
    and control.
  - ITT retains original assignment despite noncompliance; an actual-location IV effect
    additionally needs exclusion, a first stage, and a defensible compliance interpretation.
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
  - Lee bounds on attrition-driven selection (the paper's reference list cites Lee,
    Review of Economic Studies 76, printed as 2008; the study is commonly dated 2009)
  - Robustness to alternative performance measures and sample restrictions
threats:
- type: attrition-bias
  basis: reported
  condition: Worse-performing employees were more likely to quit in both groups, and
    quit rates were higher in the control group, which could bias the estimated treatment
    effect downward.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Lee bounds on treatment effects
  - Compare attrition patterns across treatment and control
  - Sensitivity of estimates to sample selection corrections
- type: selection-into-volunteering
  basis: reported
  condition: Only about half of eligible employees volunteered, and volunteers differed
    from non-volunteers in commute length, tenure, education, and having a private room.
    The experimental estimates are local to the volunteer population.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Compare treatment effects for volunteers with different observable characteristics
  - Interpret ITT as the assignment effect among eligible volunteers, not automatically as LATE
  - Use non-volunteer eligible employees as an external validity check
- type: external-validity
  basis: inferred
  condition: The results come from call-center employees with easily measured output;
    they may not generalize to other occupations, industries, or to mandatory remote-work
    policies.
  evidence_refs:
  - E1
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
  - E1
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
  - E1
  - E2
  possible_diagnostics:
  - Compare control group with employees outside the experiment (Nan Tong and non-volunteers)
  - Test for changes in control-group performance before and after randomization
  - Include team fixed effects or team-level spillover terms
empirical_requirements:
  contract_version: 1
  population: Call-center employees in Ctrip's Shanghai airfare and hotel booking departments
    during 2010-2011.
  observation_unit: Employee-week for the default performance ITT application.
  geography_level: Firm / call center (Shanghai).
  time_start: 2010
  time_end: 2011
  minimum_frequency: weekly
  minimum_pre_periods: 48
  minimum_post_periods: 37
  required_fields:
  - employee identifier
  - calendar week
  - original randomized group (or day-of-month birthday parity)
  - experiment-period indicator
  - main-task performance measure or the published composite z-score
  - employment / observation availability for attrition assessment
  required_identifiers:
  - employee ID
  - calendar week
  treatment_key:
  - employee ID
  - recorded treatment assignment or day-of-month birthday parity
  - experiment-period indicator
  treatment_source: AEA trial 276 documents parity assignment; the author-hosted analysis
    extract provides personid, year_week, expgroup and experiment_treatment. Raw Ctrip
    HR/IT access is not implied. The 48 pre and 37 experimental weeks describe the published
    Table II replication window, not a universal minimum for every new application.
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
  - scope.china_relevance
  - identity.instrument
  - identity.authority
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.announcement
  - timeline.effective
  - timeline.implementation_start
  - timeline.implementation_end
  - timeline.local_timing
  - timeline.anticipation
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.compliance
  - assignment.exposure_construction
  - assignment.required_identifiers
  - assignment.spillovers
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - design.assumptions
  - design.diagnostics
  - design.affordances
  - design.candidate_designs
  - threats.condition
  - threats.possible_diagnostics
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.geography_level
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.minimum_frequency
  - empirical_requirements.minimum_pre_periods
  - empirical_requirements.minimum_post_periods
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_key
  - empirical_requirements.treatment_source
  - empirical_requirements.measurement_risks
  - design_applications.paper
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
  - design_applications.research_question
  - design_applications.population
  - design_applications.outcome
  - design_applications.data_used
  - design_applications.treatment_encoding
  - design_applications.comparison
  - design_applications.empirical_design
  - design_applications.assumptions
  - design_applications.threats_addressed
  verification_status: verified
  access_level: full-text
  locator: Published QJE article (54-page PDF of qju032, pages 165-218), full text
    inspected 2026-08-15 via the author-hosted copy linked from the "Does working
    from home work? Evidence from a Chinese experiment" entry on
    nbloom.people.stanford.edu/research (Google Drive file 1DPhkrgydBA7Xt9ZHHQv8ZcpBSbzgfy-F);
    Sections I-II, III.A-III.C, IV.A-IV.C, Tables I-IV and Figure IV. Re-inspected
    2026-10-03 in memory; PDF page 19 (printed 183) documents compliance and ITT;
    PDF page 23 (printed 187), Table II gives 85 total/37 experimental weeks,
    weekly units, employee clustering, and post-quit deletion; pages 30, 33 and 39
    distinguish supplementary controls, post-rollout selection and survey timing. The DOI landing
    page returned HTTP 403 in this environment.
- id: E2
  source_type: paper
  citation: 'Bloom, Nicholas, James Liang, John Roberts, and Zhichun Jenny Ying. 2013.
    "Does Working from Home Work? Evidence from a Chinese Experiment." NBER Working
    Paper No. 18871.'
  url: https://www.nber.org/system/files/working_papers/w18871/w18871.pdf
  date: 2013
  supports:
  - identity.instrument
  - identity.authority
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.announcement
  - timeline.effective
  - timeline.implementation_start
  - timeline.implementation_end
  - timeline.local_timing
  - timeline.anticipation
  - assignment.rule
  - assignment.compliance
  - assignment.intensity
  - assignment.spillovers
  - design.primary_strategy
  - design.estimand
  - design.diagnostics
  - threats.condition
  - threats.possible_diagnostics
  - empirical_requirements.required_fields
  - empirical_requirements.measurement_risks
  - design_applications.data_used
  - design_applications.threats_addressed
  verification_status: verified
  access_level: full-text
  locator: NBER Working Paper 18871 PDF, full text re-inspected 2026-08-15; Sections
    II.A-B, III.A-C, IV.A-B, Tables 2-4 and Figure 2. Corroborates the published
    version; minor numeric differences from the QJE version (996 vs 994 departmental
    headcount; August 15 vs August 14, 2011 end date; ping-pong ball vs ball from an
    urn) are preserved in the record.
- id: E3
  source_type: replication
  citation: 'Bloom, Nicholas, James Liang, John Roberts, and Zhichun Jenny Ying. 2015.
    Replication data archive (wfh.zip) for "Does Working from Home Work?", author-hosted
    on Google Drive and linked from N. Bloom''s Stanford research page.'
  url: https://drive.google.com/file/d/1xvEVI74v3xsfnwNvRwyOz9Mup-aNYiE8/view
  date: 2015
  supports:
  - design.estimation_notes
  - design.diagnostics
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_key
  - empirical_requirements.minimum_frequency
  - empirical_requirements.observation_unit
  - empirical_requirements.treatment_source
  - design_applications.data_used
  - design_applications.treatment_encoding
  - design_applications.comparison
  - design_applications.empirical_design
  verification_status: verified
  access_level: replication
  locator: Public Google Drive download endpoint for wfh.zip, retrieved and inspected
    in memory on 2026-09-28 and re-inspected on 2026-10-03. WFH/Readme.txt states that the archive replicates everything
    in the paper; WFH/Tables2014.do (February 2014) runs the reported tables and appendices.
    The archive contains processed Stata inputs including performance_during_exper.dta,
    treatment_effect.dta, tc_comparison.dta, attrition.dta, promotion.dta, selection_new.dta,
    satisfaction.dta, recording.dta, conversion.dta, daysathome.dta, and wage_new.dta.
    Tables2014.do Table 2 and Appendix O5 explicitly use cluster(personid), expgroup,
    year_week, experiment_treatment and experiment_home; Table 2 drops week 201049.
    The script was inspected, not executed; archive availability alone does not certify
    successful reproduction of every published table.
- id: E4
  source_type: archive
  citation: 'Bloom, Nicholas et al. 2017. Evaluating the Impact of Working from Home on
    Productivity and Work-Life Balance in China. AEA RCT Registry, AEARCTR-0000276,
    version 1.0, April 12. DOI 10.1257/rct.276-1.0.'
  url: https://www.socialscienceregistry.org/trials/276/history/16533
  date: '2017-04-12'
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.effective
  - timeline.implementation_start
  - timeline.implementation_end
  - timeline.local_timing
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  verification_status: verified
  access_level: full-text
  locator: Original archived registration inspected 2026-10-03 via public HTML. General
    Information identifies Ctrip and investigators; Interventions states the 996/503/249
    eligibility funnel, four home days, one office day and intervention dates December 6,
    2010-August 14, 2011; Experimental Design and Randomization Method describe the
    Shanghai departments and public urn draw; Experiment Characteristics gives 131/118
    arms. Initial registration and First published both date April 12, 2017. Post-Trial
    distinguishes the 184 surviving employees from the original 249. This is an
    investigator-submitted retrospective primary archive, not an independent execution
    audit or prospective analysis plan; hidden documents and raw HR records were not inspected.
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
  - E3
method_transfer: null
readiness_blockers:
- "AEA trial 276 supplies a non-paper primary archive for identity, timing and assignment,
  but was registered in 2017 after execution and publication. It cannot establish
  prospective outcome commitment or independently audit actual lottery execution.
  Conditional use must retain the single-parity-draw inference limitation and differential
  attrition; it must not describe the experiment as individually independently randomized."
- "The original Ctrip administrative HR/IT system is proprietary. The public author-hosted
  replication archive contains processed analysis extracts and the script for the paper's
  tables and appendices, not a documented route to the underlying live system; a new study
  would still need a firm partnership or comparable administrative data."
- "The published QJE version and the NBER working paper report minor numeric
  differences (996 vs 994 departmental headcount; August 15 vs August 14, 2011 as the
  experiment end date). The record preserves both; neither changes the design."
---
---
## Institutional Background

Ctrip International Corporation was a leading NASDAQ-listed Chinese travel agency with about 16,000 employees at the time of the experiment. Its Shanghai call center handled airline and hotel bookings mainly by telephone because of lower Internet penetration in China. Senior management were interested in allowing call-center employees to work from home to save office rental costs and reduce high attrition, but feared shirking without direct supervision. Because no precedent existed among Chinese firms, Ctrip decided to run a randomized controlled trial [E2].

## What Changed

In the pilot, the employees in the airfare and hotel departments of the Shanghai call center were asked whether they wanted to work from home four days a week (996 employees in the paper's summary; the published design description reports 994). About half (503) volunteered, and 249 met eligibility criteria (at least six months tenure, home broadband, and a private workspace). A public lottery assigned employees with even birth dates to work from home and those with odd birth dates to the control group; the chairman, James Liang, drew a ball from an urn in a public ceremony one week before the start date to determine which parity received treatment. Treatment employees worked four shifts at home and one shift in the office on a fixed day; controls worked all five shifts in the office. Both groups kept the same team schedule, pay structure, equipment, and centrally routed workflow [E1; E2].

## Implementation and Assignment

The experiment started on December 6, 2010 and ran for nine months: the published regression tables define the experimental period as ending on August 14, 2011, while the announcement narrative and the NBER working paper use August 15, 2011, the day employees were told the experiment had succeeded. Assignment was fixed for the full nine months, except for a small number of equipment or housing issues. Compliance was high: 80-90 percent of treatment employees worked from home during the experiment. The IT department policed login locations, and team leaders supervised treatment employees on the one office day per week. Estimates use even-birthdate status as the intention-to-treat assignment. The published version also reports that the experiment received Stanford University IRB approval with no design changes required. On August 15, 2011 the firm announced a rollout of the option to qualified employees in the airfare and hotel booking departments beginning September 1, 2011; the published abstract describes the subsequent rollout as firm-wide [E1; E2].

## Why This Creates Empirical Variation

The public lottery selected which birthday-parity group received WFH eligibility, holding scheduled tasks, pay, equipment and workflow constant. The paper interprets the comparison as an ITT among eligible volunteers, supported by baseline balance and pre-treatment performance; it does not make the employees otherwise identical. One parity-switch draw is not 249 independent draws, so the published employee-clustered inference must not be presented as exact inference over that lottery. After rollout, employees chose locations: that phase concerns learning and selection, not the unchanged randomized assignment [E1; E3; E4; analytical inference].

## Identification Risks

The main risks are (i) differential attrition between treatment and control, which the paper shows biases estimates downward; (ii) limited external validity to occupations other than call-center work; (iii) selection into volunteering, so the experimental estimates are local to volunteers; (iv) imperfect compliance with the assigned work location; and (v) potential spillovers or morale effects within teams, which the paper addresses with quasi-control groups from Nan Tong and eligible non-volunteers [E1; E2].

## Data Requirements

The default contract is the weekly performance ITT: match employee ID, week, original assignment, experimental-period status, performance and observation availability. Published Table II uses 48 pre-experiment and 37 experimental weeks, excludes the transition week and drops employees after quitting; it is therefore not an attrition-free balanced panel. Phone-call measures apply to fewer employees than the composite main-task score. Wages are monthly; promotion, satisfaction, quality, commuting and actual work location require their own outcome-specific extracts, not mandatory fields for every performance application. Actual-location IV requires the first stage and exclusion/compliance assumptions in addition to assignment. The public archive provides processed inputs and a script; the underlying live HR/IT system remains proprietary [E1, Table II; E3, Table 2 and Appendix O5].

## Evidence Notes

Earlier audits inspected the published QJE article, NBER working paper and author-hosted replication archive; the minor 996/994 headcount and August 14/15 distinctions remain visible. On 2026-10-03, task-52aecbc523a7 recovered the original AEA registration history, re-inspected the published article's Table II and compliance passage, and re-inspected the replication README and script in memory. The original registration confirms the instrument, eligibility, parity lottery, treatment arms and precise intervention dates. It was submitted and published on April 12, 2017, after the experiment and QJE publication: the page's Pre-Trial heading is not evidence of prospective registration. General study dates 2010-01-01 to 2014-11-06 and data-collection completion May 31, 2013 are not the intervention window. Its 184-person final sample is the surviving 110/74 groups by September 1, 2011, not a replacement randomization denominator. The archived non-paper primary source closes the earlier paper-only grounding gap, allowing conditional grounded use; raw execution records, prospective commitment and single-draw inference remain limitations. This 2010-2011 call-center experiment is separate from Trip.com's 2021 graduate-worker hybrid experiment [E1; E3; E4].
