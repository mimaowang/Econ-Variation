---
schema_version: 2
id: us-moving-to-opportunity-experiment
name: Moving to Opportunity Randomized Housing Voucher Experiment
aliases:
- MTO experiment
- Moving to Opportunity demonstration
- HUD Moving to Opportunity

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: United States
  regions:
  - Baltimore
  - Boston
  - Chicago
  - Los Angeles
  - New York City
  domains:
  - education
  - labor
  - housing
  - urban
  - health
  - intergenerational-mobility
  variation_type: pilot-assignment
  knowledge_role: transferable-method
  china_relevance: The source setting is outside China; retain the reusable identification construction rather than recommend
    the foreign shock as a China treatment.
identity:
  instrument: Randomized assignment of housing vouchers to families living in high-poverty public housing, with an experimental
    treatment group receiving vouchers restricted to low-poverty neighborhoods
  authority: US Department of Housing and Urban Development (HUD)
  legal_identifiers:
  - HUD Moving to Opportunity Demonstration
  - authorized under 1992 HUD Appropriations Act
  implementation_regime: Between 1994 and 1998, 4,604 volunteer families in five cities were randomly assigned to one of three
    groups — experimental (low-poverty voucher), Section 8 (traditional voucher), or control (no voucher)
  assignment_mechanism: Random lottery among eligible volunteer families residing in high-poverty public housing
  parent: null
  related_variations: []
timeline:
  announcement: '1992-01-01'
  effective: null
  implementation_start: 1994
  implementation_end: 1998
  local_timing: Enrollment and randomization occurred on a rolling basis across five sites from 1994–1998; take-up of the
    experimental voucher required finding a unit in a census tract with poverty rate below 10%
  anticipation: Families had to volunteer for the program, so those who anticipated moving may have self-selected into the
    lottery; randomization ensures internal validity among volunteers
  last_verified: '2026-07-13'
assignment:
  unit: Household with children residing in high-poverty public housing
  treated: Households randomly assigned to receive a housing voucher restricted to low-poverty neighborhoods (experimental
    group); secondary treatment arm received an unrestricted Section 8 voucher
  comparison_pool: Households randomly assigned to the control group, which received no voucher through the program but retained
    access to public housing
  rule: Random assignment through lottery, stratified by site; experimental-group vouchers required moving to a tract with
    poverty rate below 10% for at least one year
  intensity: Treatment take-up was partial — approximately 47% of the experimental group and 61% of the Section 8 group used
    their vouchers to move; compliance varied by site and family characteristics
  exemptions: []
  compliance: Intent-to-treat (ITT) estimates compare all randomly assigned families; treatment-on-the-treated (TOT) estimates
    adjust for voucher take-up using random assignment as an instrument
  exposure_construction: Binary indicators for random assignment to experimental or Section 8 group; duration-weighted exposure
    for analyses of age-dependent effects; site-specific propensity-score adjustments for differential recruitment
  required_identifiers:
  - household ID
  - random assignment group
  - site
  - child age at randomization
  - survey wave
  spillovers: Moving families may generate neighborhood-level effects on destination tracts; control-group families may be
    affected through peer networks or labor-market competition
research_compatibility:
  outcome_domains:
  - education
  - earnings
  - employment
  - health
  - mental health
  - neighborhood quality
  - crime
  - single parenthood
  - college attendance
  affected_populations:
  - children in low-income families
  - public housing residents
  - single mothers
  - minority households
  mechanism_channels:
  - neighborhood quality
  - school quality
  - social networks
  - environmental exposure
  - role models
  - commuting
  - safety
  best_for:
  - Studying the causal effect of neighborhood environment on long-run child outcomes
  - Research that can follow children longitudinally and link to administrative data (tax records)
  - Designs exploiting the age gradient in exposure effects
  not_good_for:
  - Short-term outcomes without long-run follow-up
  - Populations outside the five demonstration cities
  - Studies requiring full compliance with treatment assignment
design:
  affordances:
  - random assignment to treatment groups
  - age-at-move variation across children in the same household
  - cross-site variation in program implementation and local housing markets
  - long-run administrative data linkage (tax records) for virtually all children
  candidate_designs:
  - intent-to-treat (ITT) comparison of experimental versus control
  - treatment-on-the-treated (TOT) using random assignment as instrument for neighborhood quality
  - difference-in-differences by child age at randomization
  - dosage-response analysis using duration of exposure to low-poverty neighborhoods
  identifying_variation: Random assignment to the experimental voucher group, interacted with child age at the time of move,
    identifies the causal effect of moving to a lower-poverty neighborhood
  assumptions: &id001
  - Random assignment was successfully implemented (balance across groups at baseline)
  - Attrition from longitudinal follow-up is unrelated to treatment assignment
  - The control group provides a valid counterfactual for treated families
  - Administrative data coverage (tax records) is not systematically different across treatment arms
  diagnostics: &id002
  - Test baseline balance across treatment arms on observable pre-randomization characteristics
  - Compare attrition rates across treatment arms
  - Test for differential administrative data coverage
  - Estimate ITT, TOT, and local average treatment effects
  - Analyze heterogeneity by child age, gender, and site
  - Assess robustness to multiple testing adjustments
  primary_strategy: Intent-to-treat (ITT) comparison of experimental versus control children, with age-at-move interaction
    as the key source of identifying variation; treatment-on-the-treated (TOT) estimates using assignment as instrument
  estimand: The causal effect of the recorded exposure on Individual earnings (W-2), college attendance (1098-T forms), neighborhood
    quality in adulthood, single parenthood rates, marriage rates, conditional on the stated design assumptions.
  treatment_variable: Binary indicator for assignment to experimental (low-poverty) voucher group; interacted with child age
    at randomization to estimate age-specific exposure effects; duration-weighted neighborhood poverty as a dosage measure
  comparison_logic: Control-group children versus experimental-group children, by age at randomization
  estimation_notes: Intent-to-treat (ITT) comparison of experimental versus control children, with age-at-move interaction
    as the key source of identifying variation; treatment-on-the-treated (TOT) estimates using assignment as instrument
threats:
- type: partial-compliance
  basis: documented
  condition: Only 47% of experimental-group families used their voucher to move; the ITT is unbiased but TOT requires an additional
    exclusion restriction
  evidence_refs:
  - E1
  possible_diagnostics:
  - estimate both ITT and TOT
  - analyze complier characteristics
  - bound treatment effects with non-compliance
- type: site-and-population-specificity
  basis: inferred
  condition: Results are identified from five large US cities in the mid-1990s and from families who volunteered for the program;
    external validity to other settings or populations is uncertain
  evidence_refs:
  - E1
  possible_diagnostics:
  - compare across sites
  - benchmark against other housing programs
  - compare volunteer characteristics to broader eligible population
- type: general-equilibrium-effects
  basis: inferred
  condition: If MTO at scale would change neighborhood composition, property values, or labor markets, the experimental estimates
    may not capture full-scale policy effects
  evidence_refs:
  - E1
  possible_diagnostics:
  - model equilibrium effects
  - conduct partial-equilibrium sensitivity checks
- type: age-heterogeneity-misinterpretation
  basis: reported
  condition: Negative effects for adolescents who moved may reflect disruption effects rather than a causal effect of neighborhood
    quality; conflating age and duration of exposure requires careful modeling
  evidence_refs:
  - E1
  possible_diagnostics:
  - separate age-at-move from exposure duration
  - model age-specific effects nonparametrically
empirical_requirements:
  contract_version: 1
  population: Children in low-income families originally living in high-poverty public housing in five major US cities, followed
    into adulthood
  observation_unit: Child-year or individual in adulthood, linked to random assignment status and age at move
  geography_level: Census tract and commuting zone
  time_start: 1994
  time_end: 2012
  minimum_frequency: annual for administrative data; periodic for survey waves
  minimum_pre_periods: 0
  minimum_post_periods: 15
  required_fields:
  - random assignment group
  - child date of birth or age
  - adult earnings
  - college attendance
  - neighborhood characteristics
  - family demographics
  required_identifiers:
  - household ID
  - child ID
  - site code
  - randomization date
  treatment_key:
  - household ID
  - treatment group assignment
  - child age at randomization
  treatment_source: HUD MTO demonstration assignment records, linked to IRS tax records via SSN or TIN
  measurement_risks:
  - incomplete tax-record coverage for non-filers
  - measurement error in neighborhood quality
  - variation in age reporting
  - cross-site implementation differences
evidence:
- id: E1
  source_type: paper
  citation: 'Chetty, Raj, Nathaniel Hendren, and Lawrence F. Katz. 2016. "The Effects of Exposure to Better Neighborhoods
    on Children: New Evidence from the Moving to Opportunity Experiment." American Economic Review 106 (4): 855–902.'
  url: https://doi.org/10.1257/aer.20150572
  date: 2016
  supports:
  - identity
  - assignment
  - design
  - main results
  - age-gradient analysis
  - tax-data linkage
  - long-run follow-up
  verification_status: verified
- id: E2
  source_type: replication
  citation: Chetty, Hendren, and Katz replication package, OpenICPSR project 113061
  url: https://www.openicpsr.org/openicpsr/project/113061/
  date: 2016
  supports:
  - data construction
  - code
  - sensitivity analysis
  verification_status: verified
- id: E3
  source_type: policy-document
  citation: 'US Department of Housing and Urban Development, Moving to Opportunity for Fair Housing Demonstration Program:
    Final Impacts Evaluation, 2011'
  url: https://www.huduser.gov/portal/publications/pubasst/MTOFHD.html
  date: 2011
  supports:
  - program design
  - implementation
  - interim survey results
  - recruitment protocols
  verification_status: verified
design_applications:
- paper: 'The Effects of Exposure to Better Neighborhoods on Children: New Evidence from the Moving to Opportunity Experiment'
  doi: 10.1257/aer.20150572
  journal: American Economic Review
  year: 2016
  research_question: What is the causal effect of moving from high-poverty to lower-poverty neighborhoods on children's long-run
    economic outcomes, and how does this effect vary with the child's age at the time of the move?
  population: Children in MTO families who were under age 13 at randomization, followed into adulthood (through 2012 tax records)
  outcome: Individual earnings (W-2), college attendance (1098-T forms), neighborhood quality in adulthood, single parenthood
    rates, marriage rates
  data_used: []
  treatment_encoding: Binary indicator for assignment to experimental (low-poverty) voucher group; interacted with child age
    at randomization to estimate age-specific exposure effects; duration-weighted neighborhood poverty as a dosage measure
  comparison: Control-group children versus experimental-group children, by age at randomization
  empirical_design: Intent-to-treat (ITT) comparison of experimental versus control children, with age-at-move interaction
    as the key source of identifying variation; treatment-on-the-treated (TOT) estimates using assignment as instrument
  assumptions:
  - random assignment was well-implemented
  - control group provides valid counterfactual
  - IRS data coverage is independent of treatment status
  - no differential attrition
  threats_addressed:
  - partial compliance via ITT and TOT
  - age-varying effects via nonparametric age interaction
  - site heterogeneity via stratified estimates
  evidence_refs:
  - E1
  - E2
  - E3
readiness_blockers:
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
- Transfer to a Chinese application has not yet been audited against a specific Chinese institution and dataset.
method_transfer:
  source_context: 'United States: Moving to Opportunity Randomized Housing Voucher Experiment'
  strategy_family: Intent-to-treat (ITT) comparison of experimental versus control children, with age-at-move interaction
    as the key source of identifying variation; treatment-on-the-treated (TOT) estimates using assignment as instrument
  reusable_logic: Random lottery among eligible volunteer families residing in high-poverty public housing
  construction_steps:
  - Binary indicators for random assignment to experimental or Section 8 group; duration-weighted exposure for analyses of
    age-dependent effects; site-specific propensity-score adjustments for differential recruitment
  source_treatment_or_endogenous_variable: Binary indicator for assignment to experimental (low-poverty) voucher group; interacted
    with child age at randomization to estimate age-specific exposure effects; duration-weighted neighborhood poverty as a
    dosage measure
  source_instrument_or_assignment: Random lottery among eligible volunteer families residing in high-poverty public housing
  first_stage_or_contrast: Random assignment to the experimental voucher group, interacted with child age at the time of move,
    identifies the causal effect of moving to a lower-poverty neighborhood
  identifying_assumptions: *id001
  diagnostics: *id002
  china_use_cases:
  - Use genuinely randomized housing, school, relocation, or program lotteries in China as instruments for take-up or neighborhood
    exposure, preserving assignment records and noncompliance.
  china_data_requirements:
  - random assignment group
  - child date of birth or age
  - adult earnings
  - college attendance
  - neighborhood characteristics
  - family demographics
  transfer_limits:
  - Short-term outcomes without long-run follow-up
  - Populations outside the five demonstration cities
  - Studies requiring full compliance with treatment assignment
---
## Institutional Background

The Moving to Opportunity (MTO) demonstration was authorized by the US Congress in 1992 and implemented by HUD between 1994 and 1998. The program's premise was that neighborhood environment causally affects life outcomes, and that housing vouchers could enable low-income families to escape high-poverty neighborhoods. At the time, concentrated urban poverty was a major policy concern, and earlier housing programs had been criticized for reinforcing racial and economic segregation. [E1, E3]

The demonstration recruited 4,604 volunteer families living in high-poverty public housing projects in Baltimore, Boston, Chicago, Los Angeles, and New York. Families had to have children under age 18 and meet income eligibility criteria. The five sites were chosen to represent geographic and housing-market diversity. [E3]

## What Changed

Through a random lottery, families were assigned to one of three groups: (1) an experimental group receiving a housing voucher restricted to census tracts with poverty rates below 10%, plus mobility counseling; (2) a Section 8 group receiving a traditional unrestricted housing voucher; or (3) a control group that received no voucher through the program. The experimental voucher created a strong incentive to move to dramatically lower-poverty neighborhoods. [E1]

## Implementation and Assignment

Random assignment was implemented through a computerized lottery system, stratified by site. Assignment was truly random within each site, creating a clean experiment. However, compliance was imperfect: approximately 47% of experimental-group families and 61% of Section 8 families actually used their vouchers to move. This creates a distinction between the intent-to-treat (ITT) effect — the effect of being offered the voucher — and the treatment-on-the-treated (TOT) effect — the effect of actually moving. Both are policy-relevant. [E1]

## Why This Creates Empirical Variation

Random assignment eliminates selection bias: families that move are not systematically different from families that stay. The key innovation in Chetty et al. (2016) is exploiting variation in the child's age at the time of the move. Because families with children of different ages were randomized in the same way, and because age at move is orthogonal to other family characteristics conditional on randomization, the interaction between treatment assignment and age identifies how the effect of neighborhood exposure varies with child age. [E1; analytical inference]

## Identification Risks

The largest concern is partial compliance: ITT estimates are unbiased but may understate the effect of moving. TOT estimates require the additional assumption that the only channel through which assignment affects outcomes is actual neighborhood change (the exclusion restriction). External validity is limited by the volunteer sample and five-city setting. The finding of negative effects for adolescents could reflect disruption rather than neighborhood quality. [E1; analytical inference]

## Data Requirements

The key data requirement is the ability to link MTO randomization records to long-run administrative data. Chetty et al. achieved this by linking MTO participant identifiers to IRS tax records covering 1996–2012, providing virtually complete coverage of earnings (W-2 forms) and college attendance (1098-T forms) for all children. This eliminated attrition bias that had plagued earlier survey-based analyses. [E1]

## Evidence Notes

E1 is the published AER article presenting the long-run results from tax data. E2 is the replication package. E3 is the HUD final impacts evaluation from 2011, which provides the definitive documentation of program design, recruitment, randomization protocols, and interim (survey-based) results. The contrast between E1 (large positive effects for young children using tax data) and earlier survey-based findings (null or mixed results) illustrates the importance of long-run administrative data and age-specific analysis.
