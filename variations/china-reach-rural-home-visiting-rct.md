---
schema_version: 2
id: china-reach-rural-home-visiting-rct
name: China REACH Rural Home-Visiting Randomized Intervention
aliases:
- China REACH
- Huachi home-visiting RCT
- China Rural Education and Child Health program
status: grounded
provenance:
  task_id: task-a159f9ebb157
scope:
  country: China
  regions:
  - Gansu Province
  - Huachi County
  - 111 administrative villages in the 2015 trial
  domains:
  - education
  - child-development
  - health
  - rural-development
  - human-capital
  variation_type: pilot-assignment
  knowledge_role: china-variation
  china_relevance: >-
    China REACH is a China-specific, village-randomized early-childhood
    intervention. It supplies a bounded rural experiment rather than a generic
    claim that parenting or nutrition policies are exogenous: treatment is
    assigned within matched villages in Huachi County, while the JPE application
    separately studies skill dynamics under the intervention.
identity:
  instrument: >-
    China REACH, a home-visiting parenting intervention that provides eligible
    households with weekly one-hour caregiving guidance and a curriculum for
    cognitive, language, motor, and socioemotional development.
  authority: >-
    China Development Research Foundation (CDRF), working with Huachi County
    and local health and research institutions; the program page describes the
    trial and its follow-up supervision.
  legal_identifiers:
  - China Rural Education and Child Health (China REACH) program
  implementation_regime: >-
    The 2015 pilot enrolled children aged 6 to 42 months in Huachi County. The
    intervention was delivered by trained village-linked home visitors to
    households in treatment villages; paired control villages did not receive
    the home-visiting protocol during the trial window.
  assignment_mechanism: >-
    Villages were paired using nonbipartite Mahalanobis matching on resident and
    village characteristics. One village within each pair was randomly selected
    for treatment and the other for control. Child enrollment and age at entry
    then determine the amount of curriculum exposure.
  parent: null
  related_variations: []
timeline:
  announcement: '2015-07'
  effective: '2015-09'
  implementation_start: 2015
  implementation_end: 2016
  local_timing: >-
    CDRF launched China REACH in July 2015 in Huachi County. The JPE paper
    describes enrollment around September 2015, weekly assessments during the
    intervention, and midline/endline assessments for treatment and control
    children. The exact village-level service calendar should be recovered from
    the field roster when extending the design.
  anticipation: >-
    Village matching and program preparation preceded enrollment. Households
    could know that the local pilot existed, and control villages may later have
    encountered related early-childhood programs; analyses should therefore use
    the trial assignment and document later expansion rather than assume no
    information or spillovers.
  last_verified: '2026-08-11'
assignment:
  unit: Child-household nested within a trial village; the treatment is assigned at village level.
  treated: >-
    Eligible children aged 6 to 42 months in a village assigned to treatment,
    whose households were offered weekly one-hour home visits and the China
    REACH caregiving curriculum.
  comparison_pool: >-
    Eligible children in the paired village assigned to control. The JPE paper
    states that midline and endline measures were collected for both arms,
    although its main dynamic-skill analysis focuses on treated children.
  rule: >-
    Within each matched village pair, randomize one village to the home-visiting
    treatment and the other to control; assign child exposure from village arm,
    enrollment age, and the calendar of weekly lessons.
  intensity: >-
    The protocol offers one hour of home visiting per week. Effective exposure
    varies with age at enrollment, visit completion, caregiver response, and
    home-visitor quality.
  exemptions:
  - Severely impaired children were not enrolled in the trial.
  - Children outside the 6-42 month enrollment range were not eligible for the core sample.
  compliance: >-
    Home visitors were selected from target villages and were broadly comparable
    in education to the mothers they visited. The protocol was assigned at the
    village level, but realized caregiver interactions and visit quality can vary;
    the JPE paper notes negligible attrition apart from deaths in its analytic
    sample.
  exposure_construction: >-
    Join child ID to village ID, matched-pair ID, assignment arm, enrollment age,
    and visit date. Construct an intention-to-treat indicator for treatment-village
    assignment and, when visit logs exist, a dose measure based on completed
    weekly visits. Keep the JPE paper's treated-arm skill-dynamics estimand
    separate from the treatment-control RCT estimand.
  required_identifiers:
  - child or household ID
  - village ID
  - matched-pair ID
  - treatment-arm indicator
  - enrollment date and child age
  - visit date or week
  spillovers: >-
    Information may travel within villages or between paired villages, and later
    program expansion may contaminate the control condition. The record therefore
    treats no-spillover as a design assumption to diagnose, not as a permanent
    fact about the institution.
research_compatibility:
  outcome_domains:
  - child cognitive skills
  - language and motor skills
  - socioemotional development
  - parenting practices
  - nutrition and early health
  - intergenerational mobility
  affected_populations:
  - children aged 6-42 months in low-income rural households
  - caregivers and home visitors in Huachi County
  mechanism_channels:
  - caregiver information and stimulation
  - repeated home-based practice
  - child nutrition and health support
  - home-visitor quality
  - caregiver education and home environment
  best_for:
  - estimating the local intention-to-treat effect of a village-randomized early-childhood home-visiting program
  - studying heterogeneous treatment effects by caregiver, child age, and home environment
  - modeling dynamic skill formation with repeated weekly measures
  not_good_for:
  - national estimates of early-childhood policy without a scaling argument
  - city-level labor or housing questions
  - interpreting the JPE treated-arm model as a treatment-control estimate
design:
  claim_type: causal
  affordances:
  - paired village randomization with an explicit control village
  - rural China setting with a bounded county and village roster
  - repeated weekly skill measurements and baseline/midline/endline assessments
  - linked caregiver, home-environment, and home-visitor information
  candidate_designs:
  - cluster randomized intention-to-treat comparison with matched-pair effects
  - treatment-effect heterogeneity by child age, caregiver education, and home environment
  - event-time or dose analyses using weekly visit records, subject to compliance checks
  - dynamic skill-formation models using the JPE paper's treated-arm weekly outcomes
  identifying_variation: >-
    The primary variation is the random selection of one village within each
    matched pair to receive China REACH home visits in 2015.
  primary_strategy: >-
    Cluster-randomized intention-to-treat estimation with matched-pair fixed
    effects and inference at the village or pair level; the JPE application uses
    a latent dynamic skill model and is not itself a standard treatment-effect
    regression.
  estimand: >-
    The local average intention-to-treat effect of assignment to weekly home
    visits on eligible children in the Huachi trial. A separate application
    estimand is the dynamic evolution of measured skills under the intervention
    among treated children.
  treatment_variable: >-
    Indicator for a child's village being assigned to treatment, interacted with
    the post-enrollment trial period; optional secondary measures encode completed
    weekly visits and age-specific curriculum exposure.
  comparison_logic: >-
    Compare eligible children in the treated village with eligible children in its
    matched control village, preserving the pair boundary. Do not substitute all
    untreated villages in Gansu for the randomized comparison without documenting
    the new estimand.
  estimation_notes: >-
    Use matched-pair effects and village-clustered uncertainty. Check balance and
    attrition, report intention-to-treat before dose or treatment-on-the-treated
    estimates, and separate midline/endline treatment-effect applications from
    the JPE weekly treated-arm model.
  assumptions:
  - The village randomization was implemented as described and was not altered after matching.
  - Control villages did not receive the same home-visiting protocol during the trial window.
  - Child enrollment and outcome measurement are comparable across arms.
  - Missing visits and caregiver response do not create unaddressed differential attrition.
  - The estimand is local to Huachi County and the 2015 trial population unless external validity is separately established.
  diagnostics:
  - matched-pair balance table for village and child baseline characteristics
  - treatment and control attrition and missing-visit audit
  - contamination or later-program-exposure checks in control villages
  - intention-to-treat estimates before dose-response specifications
  - age-at-entry and caregiver-education heterogeneity with pre-specified interactions
threats:
- type: external-validity
  basis: inferred
  condition: >-
    The experiment covers one low-income county in Gansu and a selected age range;
    effects may not transport to urban children, other provinces, or a national
    early-childhood program.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - compare baseline village and child composition with target populations
  - replicate the protocol in additional counties or urban settings
- type: spillover-contamination
  basis: inferred
  condition: >-
    Caregivers or home visitors may share information across village boundaries,
    and later CDRF expansion could reduce the contrast between paired villages.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - inspect control-village service records and later program dates
  - test outcomes against distance or social links to treated villages
- type: imperfect-compliance
  basis: reported
  condition: >-
    Assignment is at village level, while caregiver take-up, visit completion, and
    visitor quality determine realized exposure.
  evidence_refs:
  - E2
  - E4
  possible_diagnostics:
  - report assignment effects before dose measures
  - use visit logs and pre-specified compliance strata
- type: age-cohort-exposure
  basis: reported
  condition: >-
    Children enrolled at different ages receive different portions of the common
    age-indexed curriculum, so age at entry is part of the exposure definition.
  evidence_refs:
  - E2
  possible_diagnostics:
  - plot exposure calendars by age at enrollment
  - estimate pre-specified age-cohort interactions
empirical_requirements:
  contract_version: 1
  population: Eligible children aged 6-42 months and their caregivers in the 2015 Huachi County China REACH trial.
  observation_unit: Child-week, with village and matched-pair clustering.
  geography_level: Village within Huachi County, Gansu Province.
  time_start: 2015
  time_end: 2016
  minimum_frequency: weekly
  minimum_pre_periods: 1
  minimum_post_periods: 4
  required_fields:
  - child identifier
  - household identifier
  - village and matched-pair identifiers
  - assignment arm
  - child birth date or age at enrollment
  - enrollment and visit dates
  - weekly skill measures
  - caregiver education and characteristics
  - home-environment measures
  - home-visitor identity and quality measures
  - attrition and missingness indicators
  required_identifiers:
  - child ID
  - village ID
  - matched-pair ID
  - visit week
  treatment_key:
  - village assignment arm
  - matched-pair ID
  - enrollment age
  - trial-period indicator
  treatment_source: China REACH village randomization roster and CDRF field visit records.
  measurement_risks:
  - Original child-level data and village identifiers may require Dataverse or author access.
  - Weekly skill scales are level-specific and should not be treated as a common cardinal score without the measurement model.
  - Visit completion and caregiver response are not the same as randomized assignment.
  - Later program expansion can alter the control condition.
design_profiles: []
evidence:
- id: E1
  source_type: implementation-document
  citation: China Development Research Foundation, China REACH program page.
  url: https://cdrf-en.cdrf.org.cn/hyzg/index.htm
  date: 2015
  supports:
  - scope.regions
  - identity.authority
  - identity.implementation_regime
  - timeline.implementation_start
  - timeline.local_timing
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: China REACH program page, “About the Program” and follow-up assessment description.
- id: E2
  source_type: paper
  citation: "Heckman, James J., and Jin Zhou. 2026. ‘A Study of the Microdynamics of Early-Childhood Learning.’ Journal of Political Economy 134(1): 49–85."
  url: https://doi.org/10.1086/739256
  date: 2026
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.effective
  - timeline.implementation_start
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.exposure_construction
  - design.claim_type
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_key
  verification_status: verified
  access_level: full-text
  locator: NBER Working Paper 34294, published JPE version, Section II “China REACH,” pp. 3–5 and Data Availability statement.
- id: E3
  source_type: replication
  citation: "Heckman, James J., and Jin Zhou. 2025. ‘Replication Data for: A Study of the Microdynamics of Early Childhood Learning.’ Harvard Dataverse."
  url: https://doi.org/10.7910/DVN/GQBPPO
  date: 2025
  supports:
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_source
  - design_applications.data_used
  verification_status: reported
  access_level: metadata
  locator: JPE Data Availability statement and Harvard Dataverse DOI named in the published paper.
- id: E4
  source_type: paper
  citation: "Zhou, Jin, James J. Heckman, Bei Liu, and Mai Lu. 2026. ‘The Impact of a Prototypical Home Visiting Program on Child Skills.’ Journal of Labor Economics 44(1): 119–148."
  url: https://doi.org/10.1086/732301
  date: 2026
  supports:
  - design_applications.research_question
  - design_applications.population
  - design_applications.outcome
  - design_applications.treatment_encoding
  - design_applications.comparison
  - design_applications.empirical_design
  - design_applications.data_used
  - design_applications.assumptions
  - design_applications.threats_addressed
  verification_status: reported
  access_level: abstract
  locator: Journal of Labor Economics article abstract and citation page.
design_applications:
- paper: A Study of the Microdynamics of Early-Childhood Learning
  doi: 10.1086/739256
  journal: Journal of Political Economy
  year: 2026
  research_question: How do early-childhood skills evolve week by week under a structured home-visiting curriculum, and how do caregiver and home environments mediate that evolution?
  population: Children enrolled in the China REACH trial, with the main dynamic analysis focused on treated children in Huachi County.
  outcome: Weekly cognitive, language, motor, and socioemotional skill measures and latent skill states.
  data_used:
  - China REACH weekly child skill assessments
  - age-indexed curriculum and enrollment timing
  - caregiver and home-environment measures
  - home-visitor quality records
  - treatment and control enrollment records for the trial context
  treatment_encoding: Age-specific curriculum exposure among treated children; the paper describes the village RCT but its main model follows treated skill dynamics rather than estimating a standard treatment-control effect.
  comparison: The published JPE analysis is not a conventional treatment-control estimate; midline/endline treatment-control comparisons are attributed to the linked Journal of Labor Economics application.
  empirical_design: Latent dynamic skill-formation model estimated from repeated weekly measurements, with the RCT supplying the institutional context and exogenous curriculum timing.
  assumptions:
  - Skill levels are interpreted through the paper’s level-specific measurement model.
  - Enrollment age and curriculum timing are observed accurately.
  - Treated-arm dynamics are not presented as a treatment-control causal estimate.
  threats_addressed:
  - level-specific measurement and apparent fade-out
  - caregiver and home-environment heterogeneity
  evidence_refs:
  - E2
  - E3
- paper: The Impact of a Prototypical Home Visiting Program on Child Skills
  doi: 10.1086/732301
  journal: Journal of Labor Economics
  year: 2026
  research_question: What is the causal effect of assignment to the China REACH home-visiting intervention on measured and latent child skills?
  population: Eligible children and caregivers in the paired-village China REACH RCT in Huachi County.
  outcome: Child skill tests and latent skill measures across cognitive, language, motor, and socioemotional domains.
  data_used:
  - China REACH treatment and control child assessments
  - village assignment and matched-pair information
  - caregiver, home-environment, and visit data
  treatment_encoding: Indicator for assignment of the child’s village to weekly home visits, with secondary measures of realized visit exposure.
  comparison: Eligible children in the matched control village within the same randomized pair.
  empirical_design: Cluster randomized treatment-control comparison combined with item-response and latent-skill measurement.
  assumptions:
  - The paired-village randomization is valid and preserved through follow-up.
  - Control villages do not receive the same intervention during the study window.
  - Item difficulty and latent-skill measurement are modeled consistently across arms.
  threats_addressed:
  - conventional test-score scaling
  - caregiver heterogeneity and treatment-response mediation
  - local external validity of the Huachi trial
  evidence_refs:
  - E1
  - E2
  - E4
method_transfer: null
readiness_blockers:
- The JPE paper’s main weekly model focuses on treated-child skill dynamics; use the linked Journal of Labor Economics application for a treatment-control estimand.
- Exact village rosters, visit logs, and child-level identifiers should be cross-checked against the CDRF field records or the Dataverse package before extending the design beyond Huachi County.
- The original microdata are not assumed to be publicly reusable merely because a replication DOI is listed.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

China REACH (China Rural Education and Child Health) is a CDRF early-childhood program launched in Huachi County, Gansu Province. The CDRF describes it as an integrated rural intervention with randomized controlled trials and follow-up assessments, supervised with Huachi health authorities and national survey and health institutions [E1]. The JPE paper places the experiment in a low-income county with 111 administrative villages and frames it as a scaled adaptation of the Jamaican home-visiting protocol [E2]. The record is therefore about a bounded randomized intervention, not about China’s national early-childhood policy or a claim that rural parenting is intrinsically exogenous.

## What Changed

In 2015, China REACH offered weekly one-hour home visits to eligible households in treatment villages. Trained home visitors taught caregivers activities intended to build cognitive, language, motor, and socioemotional skills. Children aged 6–42 months were enrolled; age at entry determined how much of the age-indexed curriculum a child could receive [E2]. The paired control villages supplied the comparison condition during the trial, while later CDRF programs and the broader institutional setting remain outside this case’s treatment boundary [E1, E2].

## Implementation and Assignment

The assignment operates at the village level. Researchers paired villages using nonbipartite Mahalanobis matching and randomly selected one village in each pair for treatment and the other for control [E2]. Eligible children in treated villages were offered weekly visits; the JPE paper records that midline and endline measures existed for both arms, even though its main dynamic analysis concentrates on treated children [E2]. A reusable treatment variable is the village-arm indicator interacted with the post-enrollment period. A richer exposure measure adds enrollment age and completed visits, but that measure should not replace the randomized intention-to-treat variable.

## Why This Creates Empirical Variation

The variation comes from the matched-pair lottery, not from comparing Huachi with other counties. The same local setting contains a treatment village and a control village, so a researcher can estimate an intention-to-treat effect with pair effects and village-level inference. Repeated weekly measures allow a second, different application: modeling how skills evolve as children receive age-specific lessons. The JPE article uses that second object; the linked Journal of Labor Economics paper uses the RCT for treatment-control skill effects [E2, E4]. Keeping these estimands separate prevents a dynamic treated-arm model from being cited as if it were the randomized treatment effect.

## Identification Risks

The trial is local to one county and a selected age range. Information may cross village boundaries, and later program expansion can change the control condition. Assignment is randomized, but realized exposure depends on visit completion, caregiver response, and home-visitor quality. Children entering at different ages receive different curriculum segments, so age-at-entry must be part of the treatment definition. Finally, weekly skill scales are level-specific; analyses must use the published measurement model rather than treating every score as a common cardinal outcome [E2, E4].

## Data Requirements

The minimum contract is a child-week panel linked to village, matched-pair, assignment arm, enrollment age, visit dates, skill measures, caregiver characteristics, home environment, and home-visitor quality. The CDRF and the papers establish the field setting and design, while the replication DOI indicates where code/data metadata are named; access to the original microdata and village identifiers still requires verification [E1, E2, E3].

## Evidence Notes

E1 is an official CDRF program page. It establishes the program’s institutional owner, Huachi location, 2015 launch, randomized-trial framing, and follow-up supervision; it does not by itself establish the Mahalanobis pairing or the exact child roster. E2 is the full-text working-paper version of the published JPE article and establishes the 1,500-child, 111-village sample, 2015 timing, paired-village randomization, weekly protocol, age-based exposure, and the boundary between treated-arm dynamics and treatment-control analysis. E3 is the Dataverse DOI named in the published Data Availability statement; it is recorded as reported metadata until the package and access conditions are directly inspected. E4 is the linked treatment-effect application; its publisher abstract establishes that it compares treatment and control skills in a large randomized study, but the detailed roster and measurement implementation remain subject to the blocker above.
