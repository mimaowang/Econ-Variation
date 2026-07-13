---
schema_version: 2
id: africa-rainfall-civil-conflict-iv
name: Year-to-Year Rainfall Variation as an Instrument for Economic Growth in Sub-Saharan African Civil Conflict Studies
aliases:
- Rainfall instrument for conflict
- Miguel rainfall IV
- Weather shocks and civil war

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: Sub-Saharan Africa
  regions:
  - 41 Sub-Saharan African countries
  domains:
  - political-economy
  - conflict
  - development
  - agriculture
  - climate
  variation_type: event-shock
  knowledge_role: transferable-method
  china_relevance: The source setting is outside China; retain the reusable identification construction rather than recommend
    the foreign shock as a China treatment.
identity:
  instrument: Year-to-year deviations in rainfall from long-run country averages, used as an instrumental variable for GDP
    growth in civil conflict equations
  authority: Not applicable — meteorological phenomenon
  legal_identifiers: []
  implementation_regime: Annual rainfall is a naturally occurring climatic variable that strongly predicts agricultural output
    and GDP growth in rain-fed agricultural economies; rainfall shocks are short-term deviations from mean rainfall that are
    plausibly exogenous to political and social conditions
  assignment_mechanism: Year-to-year rainfall variation is determined by large-scale climatic processes (e.g., El Niño Southern
    Oscillation, Indian Ocean Dipole) and is orthogonal to country-level political, social, and institutional factors
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 1981
  implementation_end: 1999
  local_timing: Annual rainfall is measured at the country-year level; growth shocks are identified from contemporaneous rainfall
    deviations
  anticipation: Rainfall shocks are short-term and largely unpredictable at annual horizons, especially in tropical Africa
    where seasonal forecasting skill is limited
  last_verified: '2026-07-13'
assignment:
  unit: Country-year
  treated: Country-year observations with negative rainfall deviations (droughts) that reduce GDP growth
  comparison_pool: Country-year observations with normal or positive rainfall deviations; within-country variation in rainfall
    over time
  rule: For each country-year, compute rainfall growth (annual change in log rainfall) and rainfall level deviation from the
    country's long-run mean; these serve as instruments for GDP growth
  intensity: Continuous — the magnitude of the rainfall shock (in standard deviations from the country mean) determines the
    magnitude of the economic growth shock
  exemptions: []
  compliance: Not applicable — rainfall is a natural phenomenon; the instrument affects conflict only through GDP growth (exclusion
    restriction)
  exposure_construction: Compute annual rainfall growth and rainfall level deviations at the country-year level from gridded
    precipitation data (e.g., GPCP, CRU); link to annual GDP growth from national accounts or Penn World Tables
  required_identifiers:
  - country code
  - calendar year
  spillovers: Rainfall may affect neighboring countries through agricultural markets, food prices, migration, or shared water
    resources; conflict may also spill across borders
research_compatibility:
  outcome_domains:
  - civil conflict
  - political violence
  - regime stability
  - ethnic violence
  - democratization
  affected_populations:
  - rural populations
  - agricultural households
  - low-income countries
  - ethnic minorities in conflict-prone regions
  mechanism_channels:
  - agricultural output
  - GDP growth
  - poverty
  - government revenue
  - food prices
  - labor-market opportunities (opportunity cost of fighting)
  best_for:
  - Studying the causal effect of economic conditions on political violence in low-income, rain-fed agricultural economies
  - Country-year panel analyses of conflict determinants
  - Designs requiring a plausibly exogenous source of GDP variation
  not_good_for:
  - Within-country subnational analyses (unless using subnational rainfall data)
  - Countries where agriculture is largely irrigated
  - Short panels (requires multiple rainfall realizations per country)
  - Outcomes that are directly affected by rainfall through non-economic channels
design:
  affordances:
  - year-to-year rainfall variation is driven by large-scale climate processes
  - rain-fed agriculture dependence makes the first stage strong in sub-Saharan Africa
  - within-country variation in rainfall provides multiple observations per country
  candidate_designs:
  - instrumental variables (rainfall → GDP growth → conflict)
  - reduced-form regression of conflict on rainfall
  - panel fixed effects (country and year)
  - overidentified IV using both rainfall growth and rainfall levels
  identifying_variation: Country-specific deviations of annual rainfall from long-run means, conditional on country and year
    fixed effects
  assumptions: &id001
  - Rainfall is orthogonal to other determinants of civil conflict (conditional on fixed effects)
  - Rainfall affects conflict only through GDP growth (exclusion restriction)
  - The first stage is sufficiently strong (rainfall meaningfully predicts GDP growth in the sample)
  - Country-year rainfall is well-measured by gridded precipitation datasets
  diagnostics: &id002
  - Report first-stage F-statistic for instrument relevance
  - Test for direct effects of rainfall on conflict controlling for GDP
  - Examine sensitivity to alternative rainfall measures (satellite vs. station-based)
  - Assess whether rainfall predicts conflict in non-agricultural economies (falsification)
  - Use alternative instruments (e.g., commodity price shocks, terms-of-trade shocks) for robustness
  - Test whether rainfall changes in non-growing seasons affect conflict (placebo test)
  primary_strategy: Two-stage least squares (2SLS) with country and year fixed effects; rainfall growth and rainfall level
    deviations serve as excluded instruments for GDP growth in a linear probability model of conflict incidence
  estimand: The causal effect of the recorded exposure on Civil conflict incidence (binary indicator for armed conflict with
    at least 25 battle deaths per year); also conflict onset, conditional on the stated design assumptions.
  treatment_variable: GDP growth rate instrumented by current and lagged rainfall growth and rainfall level deviations from
    country means
  comparison_logic: Within-country variation in conflict associated with rainfall-driven GDP changes versus non-rainfall-driven
    GDP changes
  estimation_notes: Two-stage least squares (2SLS) with country and year fixed effects; rainfall growth and rainfall level
    deviations serve as excluded instruments for GDP growth in a linear probability model of conflict incidence
threats:
- type: exclusion-restriction-violation
  basis: reported
  condition: Rainfall may affect conflict through channels other than GDP growth — for example, impassable roads during heavy
    rains may physically impede military operations, or drought may directly trigger resource competition irrespective of
    income
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for economic growth and test whether rainfall has residual predictive power for conflict
  - use overidentifying restrictions tests
  - distinguish growing-season from non-growing-season rainfall
- type: weak-instrument
  basis: inferred
  condition: In samples or specifications where the first-stage relationship between rainfall and GDP growth is weak, IV estimates
    are biased toward OLS and standard errors are unreliable
  evidence_refs:
  - E1
  possible_diagnostics:
  - report first-stage F-statistic
  - use limited-information maximum likelihood (LIML)
  - report reduced-form estimates
  - use alternative or additional instruments
- type: spatial-and-temporal-aggregation
  basis: inferred
  condition: Country-level annual rainfall aggregates mask substantial subnational and seasonal heterogeneity; using country
    averages may attenuate the first stage or introduce measurement error
  evidence_refs:
  - E1
  possible_diagnostics:
  - use subnational rainfall data
  - disaggregate by growing season
  - test alternative aggregation methods
- type: generalizability
  basis: inferred
  condition: The instrument's strength depends on the importance of rain-fed agriculture; results from sub-Saharan Africa
    may not extend to more industrialized or irrigated agricultural economies
  evidence_refs:
  - E1
  possible_diagnostics:
  - test in alternative samples
  - compare with results from commodity-price or terms-of-trade instruments
empirical_requirements:
  contract_version: 1
  population: 41 Sub-Saharan African countries observed annually from 1981 to 1999
  observation_unit: Country-year
  geography_level: Country
  time_start: 1981
  time_end: 1999
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields:
  - annual rainfall
  - GDP growth
  - civil conflict incidence or onset
  - population
  - ethnic fractionalization
  - democracy index
  required_identifiers:
  - country code
  - calendar year
  treatment_key:
  - country code
  - calendar year
  - rainfall deviation instrument
  treatment_source: Global Precipitation Climatology Project (GPCP) or Climatic Research Unit (CRU) gridded precipitation
    data; Penn World Tables or World Development Indicators for GDP; UCDP/PRIO Armed Conflict Dataset or Correlates of War
    for conflict
  measurement_risks:
  - rainfall measurement error in data-sparse regions
  - GDP mismeasurement in conflict zones
  - conflict underreporting
  - changing country boundaries
  - spatial aggregation error
evidence:
- id: E1
  source_type: paper
  citation: 'Miguel, Edward, Shanker Satyanath, and Ernest Sergenti. 2004. "Economic Shocks and Civil Conflict: An Instrumental
    Variables Approach." Journal of Political Economy 112 (4): 725–753.'
  url: https://doi.org/10.1086/421174
  date: 2004
  supports:
  - identity
  - assignment
  - design
  - instrument construction
  - main estimates
  - Africa-wide results
  verification_status: verified
design_applications:
- paper: 'Economic Shocks and Civil Conflict: An Instrumental Variables Approach'
  doi: 10.1086/421174
  journal: Journal of Political Economy
  year: 2004
  research_question: Does negative economic growth cause civil conflict in Sub-Saharan Africa?
  population: 41 Sub-Saharan African countries, 1981–1999
  outcome: Civil conflict incidence (binary indicator for armed conflict with at least 25 battle deaths per year); also conflict
    onset
  data_used: []
  treatment_encoding: GDP growth rate instrumented by current and lagged rainfall growth and rainfall level deviations from
    country means
  comparison: Within-country variation in conflict associated with rainfall-driven GDP changes versus non-rainfall-driven
    GDP changes
  empirical_design: Two-stage least squares (2SLS) with country and year fixed effects; rainfall growth and rainfall level
    deviations serve as excluded instruments for GDP growth in a linear probability model of conflict incidence
  assumptions:
  - rainfall is orthogonal to conflict determinants conditional on fixed effects
  - rainfall affects conflict only through GDP
  - first stage is strong
  - linear probability model is a reasonable approximation
  threats_addressed:
  - reverse causality (conflict → GDP) via IV
  - omitted variables via fixed effects and instrument
  - measurement error in GDP via IV
  - overidentification via multiple instruments
  evidence_refs:
  - E1
readiness_blockers:
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
- Transfer to a Chinese application has not yet been audited against a specific Chinese institution and dataset.
method_transfer:
  source_context: 'Sub-Saharan Africa: Year-to-Year Rainfall Variation as an Instrument for Economic Growth in Sub-Saharan
    African Civil Conflict Studies'
  strategy_family: Two-stage least squares (2SLS) with country and year fixed effects; rainfall growth and rainfall level
    deviations serve as excluded instruments for GDP growth in a linear probability model of conflict incidence
  reusable_logic: Year-to-year rainfall variation is determined by large-scale climatic processes (e.g., El Niño Southern
    Oscillation, Indian Ocean Dipole) and is orthogonal to country-level political, social, and institutional factors
  construction_steps:
  - Compute annual rainfall growth and rainfall level deviations at the country-year level from gridded precipitation data
    (e.g., GPCP, CRU); link to annual GDP growth from national accounts or Penn World Tables
  source_treatment_or_endogenous_variable: GDP growth rate instrumented by current and lagged rainfall growth and rainfall
    level deviations from country means
  source_instrument_or_assignment: Year-to-year rainfall variation is determined by large-scale climatic processes (e.g.,
    El Niño Southern Oscillation, Indian Ocean Dipole) and is orthogonal to country-level political, social, and institutional
    factors
  first_stage_or_contrast: Country-specific deviations of annual rainfall from long-run means, conditional on country and
    year fixed effects
  identifying_assumptions: *id001
  diagnostics: *id002
  china_use_cases:
  - Instrument agricultural income or local economic activity in Chinese counties with crop-relevant rainfall shocks only
    when direct weather effects on the outcome can be excluded or modeled.
  china_data_requirements:
  - annual rainfall
  - GDP growth
  - civil conflict incidence or onset
  - population
  - ethnic fractionalization
  - democracy index
  transfer_limits:
  - Within-country subnational analyses (unless using subnational rainfall data)
  - Countries where agriculture is largely irrigated
  - Short panels (requires multiple rainfall realizations per country)
  - Outcomes that are directly affected by rainfall through non-economic channels
---
## Institutional Background

The relationship between economic conditions and civil conflict is a central question in political economy. Poor economic conditions are consistently correlated with civil war, but identifying causation is difficult because conflict also destroys economic output (reverse causality); both conflict and economic decline may be driven by weak institutions (omitted variables); and GDP is measured with substantial error in poor countries (attenuation bias). [E1]

Sub-Saharan Africa provides a particularly relevant setting: the region has experienced both the highest rates of civil conflict and the heaviest dependence on rain-fed agriculture. In many African countries, a single growing season's rainfall determines a large share of annual agricultural output, which in turn drives aggregate GDP. This creates a strong first-stage relationship between rainfall and economic growth. [E1]

## What Changed

Year-to-year rainfall in tropical Africa is highly variable and largely unpredictable at annual horizons. Some years bring abundant rain and bumper harvests; others bring drought and economic contraction. Crucially, this rainfall variation is driven by large-scale climatic processes (El Niño, Indian Ocean Dipole, Atlantic sea-surface temperatures) that are unrelated to within-country political or institutional conditions. [E1; analytical inference]

## Implementation and Assignment

The instrument is constructed from gridded precipitation data aggregated to the country-year level. Two variants are used: rainfall growth (the annual percentage change in rainfall) and rainfall level deviations from the country's long-run mean. These are separately included as excluded instruments in a 2SLS regression where GDP growth is the endogenous regressor and civil conflict is the outcome. Country and year fixed effects absorb time-invariant country characteristics and common time shocks. [E1]

## Why This Creates Empirical Variation

Rainfall provides a source of exogenous variation in GDP that is not driven by conflict, institutions, or measurement error. Because rain falls from the sky rather than from political decisions, it breaks the simultaneity between economic conditions and conflict. The identifying assumption is that, conditional on country and year fixed effects, the only channel through which rainfall affects civil conflict is its effect on GDP growth. [E1; analytical inference]

## Identification Risks

The most debated threat is the exclusion restriction: rainfall may affect conflict through non-economic channels. Heavy rains can impede military logistics; drought can trigger resource competition independent of income effects; and rainfall may affect food prices, migration, or disease environments through channels not fully mediated by GDP. The original paper reports that rainfall does not predict conflict in OECD countries (where agriculture is a small share of GDP), providing indirect support for the economic mechanism. Subsequent replications and extensions (Ciccone 2011, among others) have debated specification choices. [E1; analytical inference]

## Data Requirements

The design requires: (1) gridded precipitation data at monthly or annual frequency, aggregated to country boundaries; (2) annual GDP growth from national accounts or Penn World Tables; (3) conflict event data (UCDP/PRIO or Correlates of War); (4) country-level political and demographic controls. All are publicly available, making this a relatively accessible design to replicate. [E1]

## Evidence Notes

E1 is the published JPE article. The paper sparked a substantial methodological debate, particularly around the specification of the rainfall instrument (growth rates versus levels) and the handling of serial correlation. Ciccone (2011, AEJ: Applied Economics) argued that rainfall levels, rather than changes, are econometrically preferable due to rainfall's mean-reverting properties. The core finding — that economic downturns causally increase civil conflict risk — has been corroborated by studies using alternative instruments including commodity price shocks and terms-of-trade variation.
