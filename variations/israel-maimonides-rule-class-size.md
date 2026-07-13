---
schema_version: 2
id: israel-maimonides-rule-class-size
name: Maimonides' Rule as a Regression Discontinuity Instrument for Class Size in Israeli Public Schools
aliases:
- Maimonides Rule class size
- Angrist Lavy class size RD
- Maximum class size rule Israel

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: Israel
  regions:
  - Israeli public schools (Jewish secular
  - Jewish religious
  - and Arab school systems)
  domains:
  - education
  - labor
  - human-capital
  - public-finance
  variation_type: eligibility-threshold
  knowledge_role: transferable-method
  china_relevance: The source setting is outside China; retain the reusable identification construction rather than recommend
    the foreign shock as a China treatment.
identity:
  instrument: Maimonides' rule — a 12th-century Talmudic precept stipulating a maximum class size of 40 students — which,
    as incorporated into Israeli public school regulations, creates a rule-driven discontinuity in class size when grade enrollment
    crosses multiples of 40
  authority: Israeli Ministry of Education (incorporating Maimonides' rule into public school staffing regulations)
  legal_identifiers:
  - Israeli public school staffing and class-formation regulations codifying the Maimonidean maximum of 40 students per class
  implementation_regime: When grade enrollment in a school exceeds 40, an additional class must be formed, causing average
    class size to drop discontinuously; the rule applies at multiples of 40 (40, 80, 120, etc.) and is applied uniformly across
    Israeli public schools
  assignment_mechanism: Grade enrollment is the forcing variable; when it crosses a multiple of 40, an additional class is
    formed, generating a discontinuous drop in average class size; the relationship between enrollment and class size is known
    and rule-driven (nonlinear and nonmonotonic)
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 1991
  implementation_end: 1992
  local_timing: The rule is applied annually based on each grade's enrollment at the beginning of the school year; class formation
    occurs before the school year starts
  anticipation: Schools and parents may have some ability to influence enrollment near the thresholds (e.g., through registration
    timing or transfers), creating potential for sorting around the cutoff; the original paper tests for and finds no evidence
    of systematic manipulation
  last_verified: '2026-07-13'
assignment:
  unit: School-grade (e.g., 4th grade at School X)
  treated: Students in grades where enrollment just exceeds a multiple of 40 (e.g., 41 students), causing class size to drop
    sharply as a second class is formed; "treated" means assigned to a smaller class
  comparison_pool: Students in grades where enrollment is just below a multiple of 40 (e.g., 39 students), where only one
    class is formed and average class size is larger
  rule: Average class size = enrollment / ceiling(enrollment / 40); when enrollment crosses 40, ceiling doubles, and average
    class size drops from N to N/2; the rule creates a sawtooth pattern in average class size as a function of enrollment
  intensity: Class size is the treatment; the jump in class size at each threshold (from approximately 40 to 20, 40 to 27
    at 80, etc.) determines the treatment intensity
  exemptions: []
  compliance: The rule is a strict administrative regulation; compliance is nearly universal in Israeli public schools, though
    small schools or combined-grade classrooms may have limited exceptions
  exposure_construction: For each school-grade, compute enrollment and predicted class size based on Maimonides' rule; use
    an indicator for enrollment exceeding a multiple of 40 as an instrument for actual class size in a fuzzy regression discontinuity
    design
  required_identifiers:
  - school ID
  - grade level
  - enrollment count
  - actual class size
  - student test scores
  spillovers: Class-size reduction for one grade may affect resource allocation to other grades in the same school (within-school
    spillovers); students in larger classes may benefit from being assigned to the "better" of two teachers if teacher assignment
    is non-random
research_compatibility:
  outcome_domains:
  - test scores
  - academic achievement
  - educational attainment
  - future earnings
  - non-cognitive skills
  affected_populations:
  - elementary school students (4th and 5th graders)
  - middle school students (3rd graders in the sample)
  mechanism_channels:
  - class size
  - teacher attention
  - individualized instruction
  - classroom disruption
  - teacher effort
  - peer effects
  best_for:
  - Studying the causal effect of class size on academic achievement
  - Designs using administrative school data with enrollment counts and test scores
  - Outcomes observed at the student level within a few years of class-size variation
  not_good_for:
  - Long-run outcomes without linked administrative data (the original study uses test scores at the same grade level)
  - Populations outside the Israeli public school system
  - Grades where Maimonides' rule is not binding or strictly enforced
  - Questions about very small class sizes (the RD identifies effects around class size of 20–40, not 10–15)
design:
  affordances:
  - known deterministic rule relating enrollment to class size
  - sharp discontinuity in class size at multiples of 40
  - enrollment is a continuous forcing variable
  - the RD design is transparent and visual
  candidate_designs:
  - fuzzy regression discontinuity at multiples of 40 enrollment
  - reduced-form comparison of test scores across the threshold
  - parametric and nonparametric RD estimation
  - donut-hole RD (excluding observations very near the threshold to address potential sorting)
  identifying_variation: Discontinuous changes in average class size driven by the rule that an additional class is formed
    when grade enrollment crosses multiples of 40, conditional on a smooth relationship between enrollment and test scores
  assumptions: &id001
  - Enrollment is not manipulable around the thresholds (no systematic sorting)
  - The relationship between enrollment and test scores is smooth through the threshold except for the class-size effect
  - The rule is strictly enforced
  - The functional form of the enrollment-test score relationship is correctly specified (for parametric estimates)
  diagnostics: &id002
  - Plot the first-stage relationship (class size versus enrollment) and verify the sawtooth pattern
  - Check for a discontinuity in the density of enrollment around the threshold (McCrary test)
  - Test for balance in predetermined covariates across the threshold
  - Estimate with alternative bandwidths and polynomial orders
  - Compare parametric and nonparametric (local linear) RD estimates
  - Perform placebo tests at non-threshold enrollment values
  - Estimate separately by school sector (Jewish secular, Jewish religious, Arab)
  primary_strategy: Fuzzy regression discontinuity using Maimonides' rule as an instrument for class size; within-school and
    within-sector comparisons; parametric RD (quadratic and piecewise-linear in enrollment) and graphical analysis
  estimand: The causal effect of the recorded exposure on Standardized test scores in mathematics and reading (Hebrew or Arabic),
    conditional on the stated design assumptions.
  treatment_variable: Actual class size instrumented by predicted class size from Maimonides' rule (enrollment divided by
    ceiling(enrollment/40)); the instrument exploits the discontinuity in class size at multiples of 40 enrollment
  comparison_logic: Students in grades just above a multiple of 40 (smaller predicted class size) versus just below (larger
    predicted class size), within the same school sector and grade level
  estimation_notes: Fuzzy regression discontinuity using Maimonides' rule as an instrument for class size; within-school and
    within-sector comparisons; parametric RD (quadratic and piecewise-linear in enrollment) and graphical analysis
threats:
- type: sorting-around-threshold
  basis: inferred
  condition: Parents or schools could manipulate enrollment to fall just above or below a threshold if the class-size benefits
    are known and valued; this would violate the RD assumption that units cannot precisely control the forcing variable
  evidence_refs:
  - E1
  possible_diagnostics:
  - McCrary density test
  - compare baseline covariates across the threshold
  - estimate donut-hole RD excluding observations very near the threshold
  - survey institutional knowledge about enrollment manipulation
- type: other-threshold-changes
  basis: inferred
  condition: If schools crossing a multiple of 40 also receive additional resources (e.g., an additional classroom, teacher,
    or budget allocation) that affect outcomes through channels other than class size, the exclusion restriction for the fuzzy
    RD is violated
  evidence_refs:
  - E1
  possible_diagnostics:
  - document all resource changes at the threshold
  - test whether teacher characteristics change discontinuously
  - estimate whether non-class-size resources change at the threshold
- type: functional-form-sensitivity
  basis: inferred
  condition: RD estimates can be sensitive to the choice of bandwidth, polynomial order, and kernel; the Maimonides rule generates
    multiple thresholds (40, 80, 120...) that may have different local average treatment effects
  evidence_refs:
  - E1
  possible_diagnostics:
  - report estimates across multiple bandwidths and specifications
  - use modern RD robust inference (Calonico-Cattaneo-Titiunik)
  - estimate separately at each threshold
  - report both parametric and nonparametric results
- type: external-validity
  basis: inferred
  condition: The RD identifies the effect of class size for schools near the enrollment thresholds; these schools may be systematically
    different from schools far from thresholds; the LATE is specific to compliers at the margin
  evidence_refs:
  - E1
  possible_diagnostics:
  - compare characteristics of threshold and non-threshold schools
  - discuss generalizability
  - benchmark against class-size experiments (e.g.
  - Project STAR)
  - replicate in other settings with similar rules
empirical_requirements:
  contract_version: 1
  population: 3rd, 4th, and 5th grade students in Israeli public schools, observed in 1991 and 1992
  observation_unit: Student or class
  geography_level: School, within Israel
  time_start: 1991
  time_end: 1992
  minimum_frequency: annual (school year)
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields:
  - school ID
  - grade level
  - enrollment count
  - class size
  - student test scores (math and reading)
  - student demographics (parental education
  - ethnicity
  - sex)
  required_identifiers:
  - school ID
  - grade level
  - enrollment count
  treatment_key:
  - school ID
  - grade level
  - enrollment count
  - indicator for enrollment above multiple of 40
  - predicted class size
  treatment_source: Israeli Ministry of Education administrative records on school enrollment, class assignments, and standardized
    test scores
  measurement_risks:
  - enrollment measured at a single point in time may not reflect the class-formation enrollment
  - test scores are not vertically scaled across grades
  - class size may differ from Maimonides-rule prediction due to combined-grade classes or special education pullouts
evidence:
- id: E1
  source_type: paper
  citation: 'Angrist, Joshua D., and Victor Lavy. 1999. "Using Maimonides'' Rule to Estimate the Effect of Class Size on Scholastic
    Achievement." Quarterly Journal of Economics 114 (2): 533–575.'
  url: https://doi.org/10.1162/003355399556061
  date: 1999
  supports:
  - identity
  - assignment
  - design
  - RD estimation
  - main results
  - heterogeneity by grade
  - OLS comparison
  verification_status: verified
design_applications:
- paper: Using Maimonides' Rule to Estimate the Effect of Class Size on Scholastic Achievement
  doi: 10.1162/003355399556061
  journal: Quarterly Journal of Economics
  year: 1999
  research_question: What is the causal effect of class size on student test scores, exploiting the discontinuous relationship
    between enrollment and class size created by Maimonides' rule?
  population: 3rd, 4th, and 5th grade students in Israeli public schools, 1991 and 1992
  outcome: Standardized test scores in mathematics and reading (Hebrew or Arabic)
  data_used: []
  treatment_encoding: Actual class size instrumented by predicted class size from Maimonides' rule (enrollment divided by
    ceiling(enrollment/40)); the instrument exploits the discontinuity in class size at multiples of 40 enrollment
  comparison: Students in grades just above a multiple of 40 (smaller predicted class size) versus just below (larger predicted
    class size), within the same school sector and grade level
  empirical_design: Fuzzy regression discontinuity using Maimonides' rule as an instrument for class size; within-school and
    within-sector comparisons; parametric RD (quadratic and piecewise-linear in enrollment) and graphical analysis
  assumptions:
  - no manipulation of enrollment around thresholds
  - smooth relationship between enrollment and test scores
  - strict enforcement of the rule
  - exclusion restriction holds
  threats_addressed:
  - sorting via density tests and covariate balance
  - functional form via multiple specifications
  - heterogeneous effects via grade-level and sector-level analysis
  - OLS bias via comparison with RD results
  evidence_refs:
  - E1
readiness_blockers:
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
- Transfer to a Chinese application has not yet been audited against a specific Chinese institution and dataset.
method_transfer:
  source_context: 'Israel: Maimonides'' Rule as a Regression Discontinuity Instrument for Class Size in Israeli Public Schools'
  strategy_family: Fuzzy regression discontinuity using Maimonides' rule as an instrument for class size; within-school and
    within-sector comparisons; parametric RD (quadratic and piecewise-linear in enrollment) and graphical analysis
  reusable_logic: Grade enrollment is the forcing variable; when it crosses a multiple of 40, an additional class is formed,
    generating a discontinuous drop in average class size; the relationship between enrollment and class size is known and
    rule-driven (nonlinear and nonmonotonic)
  construction_steps:
  - For each school-grade, compute enrollment and predicted class size based on Maimonides' rule; use an indicator for enrollment
    exceeding a multiple of 40 as an instrument for actual class size in a fuzzy regression discontinuity design
  source_treatment_or_endogenous_variable: Actual class size instrumented by predicted class size from Maimonides' rule (enrollment
    divided by ceiling(enrollment/40)); the instrument exploits the discontinuity in class size at multiples of 40 enrollment
  source_instrument_or_assignment: Grade enrollment is the forcing variable; when it crosses a multiple of 40, an additional
    class is formed, generating a discontinuous drop in average class size; the relationship between enrollment and class
    size is known and rule-driven (nonlinear and nonmonotonic)
  first_stage_or_contrast: Discontinuous changes in average class size driven by the rule that an additional class is formed
    when grade enrollment crosses multiples of 40, conditional on a smooth relationship between enrollment and test scores
  identifying_assumptions: *id001
  diagnostics: *id002
  china_use_cases:
  - Use an enforced Chinese class-size cap or enrollment-based class-formation rule to study class size, provided administrative
    compliance and manipulation around the threshold are observable.
  china_data_requirements:
  - school ID
  - grade level
  - enrollment count
  - class size
  - student test scores (math and reading)
  - student demographics (parental education
  - ethnicity
  - sex)
  transfer_limits:
  - Long-run outcomes without linked administrative data (the original study uses test scores at the same grade level)
  - Populations outside the Israeli public school system
  - Grades where Maimonides' rule is not binding or strictly enforced
  - Questions about very small class sizes (the RD identifies effects around class size of 20–40, not 10–15)
---
## Institutional Background

Maimonides' rule originates from a 12th-century Talmudic scholar who prescribed that a class should have no more than 40 students; beyond this number, an additional teacher must be appointed. This precept was formally incorporated into Israeli public school regulations, creating a deterministic relationship between grade enrollment and the number of classes: a school with 40 or fewer students in a grade has one class; 41–80 students, two classes; 81–120, three classes; and so on. [E1]

This administrative rule creates a sawtooth pattern in average class size: as enrollment increases from 1 to 40, class size rises linearly; at 41, a second class is formed and average class size drops to about 20.5. As enrollment climbs from 41 to 80, class size rises again to 40, then drops to about 27 at 81, and so on. This discontinuous, nonmonotonic relationship is deterministic and transparent — and it is entirely rule-driven, not a function of parental choice, school quality, or student ability. [E1]

## What Changed

At each multiple of 40, the formation of an additional class creates a sharp reduction in average class size (from approximately N to N/2). The "treatment" is being assigned to a smaller class because one's grade happened to have enrollment just above a multiple of 40. This creates local random assignment of class size in the neighborhood of each threshold. [E1]

## Implementation and Assignment

The forcing variable is grade enrollment — the total number of students in a given grade at a given school. The treatment is actual class size. The instrument is predicted class size based on Maimonides' rule. Because the rule is not always perfectly predictive of actual class size (some schools may split classes at different points due to special education, combined-grade rooms, or other practical considerations), the design is a fuzzy RD: the rule creates a jump in the probability of smaller classes at the threshold, and actual class size is instrumented by the rule-based prediction. [E1]

## Why This Creates Empirical Variation

The RD design isolates the causal effect of class size by comparing students whose grades have nearly identical enrollment but lie on opposite sides of a threshold, and therefore have substantially different class sizes. Students near the threshold are similar in all respects except the class size they experience. The key assumption is that enrollment is not manipulable around the threshold — parents do not strategically place their children in schools or grades to fall on one side or the other of the 40-student boundary. [E1; analytical inference]

## Identification Risks

If parents can influence which school their child attends, and if they value small classes, they may sort toward grades predicted to have smaller classes — creating a correlation between enrollment and unobserved student characteristics at the threshold. The paper tests for this by examining the density of enrollment around thresholds (no bunching detected) and by testing for balance in observed covariates. A second concern is that class size is not the only thing that changes at the threshold: an additional teacher is hired, an additional classroom is allocated, and the within-class peer group changes. These concurrent changes may independently affect outcomes. [E1; analytical inference]

## Data Requirements

The design requires: (1) school-grade-level enrollment counts; (2) actual class sizes; (3) student-level test scores linked to school and grade; (4) student demographic controls. The data must be at a level where enrollment can be precisely measured and linked to class assignments. Israeli Ministry of Education administrative data met these requirements for the 1991 and 1992 school years. [E1]

## Evidence Notes

E1 is the published QJE article. The paper is a landmark application of the regression discontinuity design in economics of education and has been highly influential in both the class-size literature and the broader causal inference literature. The finding that smaller classes significantly increase test scores for 4th and 5th graders (but not 3rd graders) is consistent with results from the Tennessee STAR experiment, providing external validation. The paper is also notable for its clear exposition of the RD design and for its graphical presentation of the discontinuous relationship between enrollment and class size.
