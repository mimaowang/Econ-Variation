---
schema_version: 2
id: us-hookworm-eradication-campaign
name: Rockefeller Sanitary Commission Hookworm Eradication Campaign in the American South (c. 1910–1915)
aliases:
- Hookworm eradication American South
- Rockefeller Sanitary Commission hookworm campaign
- Bleakley hookworm natural experiment

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: United States
  regions:
  - American South
  - particularly areas with high pre-campaign hookworm infection rates
  domains:
  - health
  - education
  - labor
  - development
  - human-capital
  - economic-history
  variation_type: staggered-rollout
  knowledge_role: transferable-method
  china_relevance: The source setting is outside China; retain the reusable identification construction rather than recommend
    the foreign shock as a China treatment.
identity:
  instrument: The Rockefeller Sanitary Commission for the Eradication of Hookworm Disease (RSC) campaign, which provided screening,
    treatment, and public health education across counties in the American South between approximately 1910 and 1915
  authority: Rockefeller Sanitary Commission (philanthropic organization, later folded into the Rockefeller Foundation)
  legal_identifiers: []
  implementation_regime: The RSC sent teams to southern counties to screen residents for hookworm infection, provide free
    treatment, and conduct public health education about sanitation; the campaign intensity and timing varied across counties
  assignment_mechanism: The campaign targeted areas with high hookworm prevalence; the identifying variation comes from the
    interaction of pre-campaign infection rates (a proxy for the potential benefit from eradication) and the timing of the
    campaign, with pre-campaign infection rates determined by local soil and climate conditions
  parent: null
  related_variations: []
timeline:
  announcement: '1909-10-01'
  effective: null
  implementation_start: 1910
  implementation_end: 1915
  local_timing: RSC teams visited counties on a rolling basis; treatment was administered at the time of the visit, and public
    health infrastructure varied in follow-up intensity
  anticipation: The RSC campaign was announced publicly and local communities knew teams were coming; individual-level anticipation
    was limited because infection status was unknown before screening
  last_verified: '2026-07-13'
assignment:
  unit: County and birth cohort
  treated: Children and adults residing in counties with high pre-campaign hookworm infection rates, who were exposed to the
    RSC eradication campaign during childhood or schooling years
  comparison_pool: Residents of areas with lower pre-campaign infection rates (who benefited less from eradication); cohorts
    born after the campaign in the same areas; cohorts in non-southern states unaffected by the campaign
  rule: Treatment intensity depends on the interaction of the pre-campaign infection rate (determined by soil type, climate,
    and sanitation conditions that favored hookworm transmission) and the timing of the RSC campaign
  intensity: Continuous — counties with higher pre-campaign infection rates received a larger effective treatment dose because
    more residents were cured of hookworm
  exemptions: []
  compliance: Campaign participation was voluntary; not all infected individuals were screened or treated; take-up rates are
    not directly observed at the individual level
  exposure_construction: Assign exposure at the county-of-birth × birth-year level; measure the pre-campaign hookworm infection
    rate by county (from RSC survey data); interact with an indicator for whether the cohort was of school age during the
    campaign to capture the human-capital-accumulation window
  required_identifiers:
  - county of birth
  - birth year
  - pre-campaign hookworm infection rate
  - campaign timing
  spillovers: Reduced hookworm transmission benefits even untreated individuals in treated areas (herd immunity); improved
    labor productivity and school attendance may have spillover effects on local economies
research_compatibility:
  outcome_domains:
  - school enrollment
  - school attendance
  - literacy
  - educational attainment
  - adult income
  - labor productivity
  - health
  affected_populations:
  - school-age children in the early 20th century American South
  - particularly in rural areas with poor sanitation
  mechanism_channels:
  - disease burden reduction
  - nutritional improvement
  - cognitive development
  - school attendance
  - human capital accumulation
  - labor productivity
  best_for:
  - Studying the long-run economic returns to childhood health interventions
  - Research that can link Census data across multiple decades to track cohorts
  - Designs exploiting the interaction of pre-existing disease ecology with a treatment campaign
  not_good_for:
  - Short-run outcome studies (the main interest is in long-run human capital and income effects)
  - Designs requiring individual-level treatment status (treatment is measured at the area-cohort level)
  - Settings without variation in pre-intervention disease burden
design:
  affordances:
  - pre-campaign infection rates vary with local ecological conditions (soil, climate)
  - campaign timing provides before/after variation
  - cohort-level analysis links childhood exposure to adult outcomes
  candidate_designs:
  - difference-in-differences (high-infection vs. low-infection areas × pre/post campaign cohorts)
  - triple differences (adding a non-southern comparison group)
  - continuous treatment intensity (pre-campaign infection rate × post-campaign cohort)
  identifying_variation: The interaction of pre-campaign hookworm prevalence (determined by ecological conditions) with the
    timing of the RSC eradication campaign, across birth cohorts within the same county
  assumptions: &id001
  - Pre-campaign infection rates are determined by ecological conditions (soil type, climate) rather than by economic or institutional
    factors that would independently affect later outcomes
  - In the absence of the RSC campaign, high-infection and low-infection areas would have followed parallel trends in schooling
    and income
  - County of birth is a reasonable proxy for childhood exposure location (limited childhood migration)
  diagnostics: &id002
  - Test whether pre-campaign infection rates predict pre-campaign schooling or income differences
  - Compare cohorts born well after the campaign in high- and low-infection areas (convergence test)
  - Use alternative measures of infection risk (soil type, climate variables) as robustness checks
  - Control for other contemporaneous southern public health and education investments
  - Assess sensitivity to migration by comparing county-of-birth and county-of-residence in adulthood
  primary_strategy: Difference-in-differences with continuous treatment intensity; the baseline infection rate captures the
    potential benefit from eradication, and the cohort indicator captures exposure timing
  estimand: The causal effect of the recorded exposure on School enrollment, school attendance, literacy, years of schooling,
    adult income (occupation-based imputation), conditional on the stated design assumptions.
  treatment_variable: Interaction of county-level pre-campaign hookworm infection rate with an indicator for whether the individual
    was of school age (approximately 6–18) during the RSC campaign period
  comparison_logic: Within-county comparison of cohorts exposed to the campaign during childhood versus cohorts too old to
    benefit (or born after), scaled by the area's pre-existing infection rate
  estimation_notes: Difference-in-differences with continuous treatment intensity; the baseline infection rate captures the
    potential benefit from eradication, and the cohort indicator captures exposure timing
threats:
- type: ecological-confounding
  basis: inferred
  condition: Areas with high hookworm infection rates may have differed from low-infection areas along dimensions other than
    disease burden (poverty, soil productivity, institutional quality) that independently affected economic trajectories
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for pre-campaign economic and institutional characteristics
  - use soil-type instruments
  - compare adjacent counties with similar characteristics but different infection rates
- type: contemporaneous-investments
  basis: inferred
  condition: The same period saw investments in southern education (Rosenwald schools, compulsory schooling laws), agricultural
    extension, and public health that may have differentially benefited high-infection areas
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for concurrent investments
  - use non-southern comparison groups
  - test whether estimated effects are robust to controlling for other interventions
- type: migration-and-measurement
  basis: inferred
  condition: Using county of birth as the treatment assignment may misclassify exposure for individuals who migrated during
    childhood; selective migration (healthier individuals leaving high-infection areas) may bias estimates
  evidence_refs:
  - E1
  possible_diagnostics:
  - compare county-of-birth and county-of-residence in adulthood
  - bound migration effects
  - use state-of-birth as alternative assignment
- type: cohort-definition
  basis: inferred
  condition: Defining exposure cohorts requires assumptions about the critical ages for human capital accumulation; results
    may be sensitive to how "exposed" versus "unexposed" cohorts are coded
  evidence_refs:
  - E1
  possible_diagnostics:
  - test alternative cohort definitions
  - estimate age-specific effects nonparametrically
  - use continuous age-at-campaign measure
empirical_requirements:
  contract_version: 1
  population: Native-born individuals in the American South, born approximately 1890–1930, followed through Census records
    to adulthood (1940 Census or later)
  observation_unit: Individual (Census microdata) or county-cohort cell
  geography_level: County of birth
  time_start: 1890
  time_end: 1940
  minimum_frequency: decennial (Census years); the key comparison is across birth cohorts, not calendar time
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields:
  - county of birth
  - birth year
  - years of schooling
  - literacy
  - adult income or occupation
  - race
  - sex
  required_identifiers:
  - county of birth
  - birth year
  - pre-campaign hookworm infection rate by county
  treatment_key:
  - county of birth
  - birth year
  - pre-campaign infection rate × post-campaign cohort indicator
  treatment_source: Rockefeller Sanitary Commission annual reports (1910–1915) for county-level infection rates and campaign
    activities; US Census microdata (IPUMS) for individual outcomes
  measurement_risks:
  - county boundary changes between 1910 and 1940
  - incomplete RSC survey coverage
  - infection-rate measurement error
  - childhood migration between birth and schooling
  - changing county identifiers in IPUMS
evidence:
- id: E1
  source_type: paper
  citation: 'Bleakley, Hoyt. 2007. "Disease and Development: Evidence from Hookworm Eradication in the American South." Quarterly
    Journal of Economics 122 (1): 73–117.'
  url: https://doi.org/10.1162/qjec.121.1.73
  date: 2007
  supports:
  - identity
  - assignment
  - design
  - ecological identification
  - main estimates
  - long-run income effects
  - return-to-schooling analysis
  verification_status: verified
design_applications:
- paper: 'Disease and Development: Evidence from Hookworm Eradication in the American South'
  doi: 10.1162/qjec.121.1.73
  journal: Quarterly Journal of Economics
  year: 2007
  research_question: What were the long-run economic returns to the near-eradication of hookworm disease in the American South?
  population: Native-born individuals in the American South born approximately 1890–1930, observed in US Census data (primarily
    1940)
  outcome: School enrollment, school attendance, literacy, years of schooling, adult income (occupation-based imputation)
  data_used: []
  treatment_encoding: Interaction of county-level pre-campaign hookworm infection rate with an indicator for whether the individual
    was of school age (approximately 6–18) during the RSC campaign period
  comparison: Within-county comparison of cohorts exposed to the campaign during childhood versus cohorts too old to benefit
    (or born after), scaled by the area's pre-existing infection rate
  empirical_design: Difference-in-differences with continuous treatment intensity; the baseline infection rate captures the
    potential benefit from eradication, and the cohort indicator captures exposure timing
  assumptions:
  - infection rates are driven by ecological conditions orthogonal to economic potential
  - parallel trends across high- and low-infection areas
  - childhood residence coincides with county of birth
  - no differential selective mortality or migration
  threats_addressed:
  - ecological confounding via controls and alternative instruments
  - contemporaneous investments via robustness checks
  - migration via county-of-birth versus residence comparison
  evidence_refs:
  - E1
readiness_blockers:
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
- Transfer to a Chinese application has not yet been audited against a specific Chinese institution and dataset.
method_transfer:
  source_context: 'United States: Rockefeller Sanitary Commission Hookworm Eradication Campaign in the American South (c.
    1910–1915)'
  strategy_family: Difference-in-differences with continuous treatment intensity; the baseline infection rate captures the
    potential benefit from eradication, and the cohort indicator captures exposure timing
  reusable_logic: The campaign targeted areas with high hookworm prevalence; the identifying variation comes from the interaction
    of pre-campaign infection rates (a proxy for the potential benefit from eradication) and the timing of the campaign, with
    pre-campaign infection rates determined by local soil and climate conditions
  construction_steps:
  - Assign exposure at the county-of-birth × birth-year level; measure the pre-campaign hookworm infection rate by county
    (from RSC survey data); interact with an indicator for whether the cohort was of school age during the campaign to capture
    the human-capital-accumulation window
  source_treatment_or_endogenous_variable: Interaction of county-level pre-campaign hookworm infection rate with an indicator
    for whether the individual was of school age (approximately 6–18) during the RSC campaign period
  source_instrument_or_assignment: The campaign targeted areas with high hookworm prevalence; the identifying variation comes
    from the interaction of pre-campaign infection rates (a proxy for the potential benefit from eradication) and the timing
    of the campaign, with pre-campaign infection rates determined by local soil and climate conditions
  first_stage_or_contrast: The interaction of pre-campaign hookworm prevalence (determined by ecological conditions) with
    the timing of the RSC eradication campaign, across birth cohorts within the same county
  identifying_assumptions: *id001
  diagnostics: *id002
  china_use_cases:
  - Interact baseline disease prevalence or ecological suitability with the timing of a Chinese eradication or public-health
    campaign, while testing targeted rollout and direct ecology channels.
  china_data_requirements:
  - county of birth
  - birth year
  - years of schooling
  - literacy
  - adult income or occupation
  - race
  - sex
  transfer_limits:
  - Short-run outcome studies (the main interest is in long-run human capital and income effects)
  - Designs requiring individual-level treatment status (treatment is measured at the area-cohort level)
  - Settings without variation in pre-intervention disease burden
---
## Institutional Background

Hookworm infection was endemic throughout the American South in the early 20th century. The parasite enters through the skin (typically bare feet), migrates to the intestines, and causes iron-deficiency anemia, protein malnutrition, and chronic fatigue. Approximately 40% of school-age children in the South were infected, with rates exceeding 70% in some counties. The disease was widely believed to contribute to the region's economic backwardness — infected children were listless, frequently absent from school, and unlikely to accumulate human capital. [E1]

In 1909, John D. Rockefeller donated $1 million to establish the Rockefeller Sanitary Commission for the Eradication of Hookworm Disease. Between 1910 and 1915, the RSC dispatched teams to hundreds of southern counties to conduct mass screening, dispense free treatment (thymol and Epsom salts), and educate communities about sanitation (building privies, wearing shoes). The campaign reduced hookworm infection rates by roughly 30 percentage points in treated areas, though it fell short of complete eradication. [E1]

## What Changed

The RSC campaign dramatically reduced hookworm prevalence — from approximately 40% to well below 10% in many areas — within approximately five years. For children who were of school age during the campaign, the reduction in disease burden meant improved nutrition, higher school attendance, and greater returns to schooling. For adults, improved health meant higher labor productivity. [E1]

## Implementation and Assignment

The RSC targeted counties based on survey evidence of hookworm prevalence. The identifying variation comes from the interaction of two factors: (1) pre-campaign infection rates, which varied exogenously with local soil type and climate conditions (sandy, well-drained soils in warm, humid areas favor hookworm transmission); and (2) the timing of the campaign, which created sharp cohort differences in exposure. Children who were already past school age when the campaign arrived received little human-capital benefit; children who were young during the campaign received the full benefit. [E1; analytical inference]

## Why This Creates Empirical Variation

This design is a canonical example of a cohort-based difference-in-differences with continuous treatment intensity. The ecological determinants of hookworm prevalence — sandy soil, warm temperatures, high rainfall — are plausibly orthogonal to other determinants of long-run economic development, especially conditional on county-level controls. The campaign timing creates a sharp discontinuity in disease burden across adjacent birth cohorts within the same county. The interaction identifies the effect of childhood disease reduction on adult human capital and income. [E1; analytical inference]

## Identification Risks

The most important threat is that soil and climate conditions that favor hookworm also independently affect agricultural productivity — and thus income — through channels unrelated to disease. If sandy-soil counties were on different economic trajectories before the campaign, the parallel-trends assumption may be violated. The paper addresses this by controlling for agricultural characteristics and by comparing convergence patterns across cohorts. A subtler issue is that the RSC campaign was not randomly timed — the commission chose counties based on perceived need and feasibility — but this concern is mitigated by the cohort-based design. [E1; analytical inference]

## Data Requirements

The design requires: (1) county-level pre-campaign hookworm infection rates from RSC survey records; (2) individual-level Census microdata from IPUMS with county of birth and birth year for multiple Census years; (3) county-level ecological (soil, climate) and agricultural data for controls; and (4) a county boundary crosswalk for geographic consistency across decades. [E1]

## Evidence Notes

E1 is the published QJE article. The key findings — that hookworm eradication significantly increased school enrollment, attendance, and literacy, and generated substantial adult income gains — have been highly influential in the health-and-development literature. A notable feature is the analysis of returns to schooling: the campaign increased both the quantity of schooling and the return per year of schooling, consistent with a health-induced improvement in the productivity of human capital investment.
