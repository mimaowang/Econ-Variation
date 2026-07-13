---
schema_version: 2
id: old-world-potato-introduction
name: Introduction of the Potato from the Americas to the Old World as a Historical Natural Experiment in Agricultural Productivity
aliases:
- Potato introduction Columbian Exchange
- Nunn Qian potato population urbanization
- Columbian Exchange crop diffusion

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: Old World (Europe and Asia broadly)
  regions:
  - Countries and regions of the Old World with suitable potato-growing conditions
  domains:
  - agriculture
  - population
  - urbanization
  - economic-history
  - development
  - trade
  variation_type: continuous-exposure
  knowledge_role: transferable-method
  china_relevance: The source setting is outside China; retain the reusable identification construction rather than recommend
    the foreign shock as a China treatment.
identity:
  instrument: The introduction of the potato to the Old World from the Americas, combined with cross-regional variation in
    land suitability for potato cultivation, interacted with the timing of the potato's diffusion after the Columbian Exchange
    (post-1492)
  authority: Not applicable — historical biological diffusion; the potato was domesticated in the Andes and brought to Europe
    by Spanish explorers in the late 16th century
  legal_identifiers: []
  implementation_regime: The potato diffused gradually across the Old World between approximately 1600 and 1800; its adoption
    depended on local growing conditions (climate, soil, elevation), cultural acceptance, and agricultural knowledge transmission
  assignment_mechanism: Regional variation in land suitability for potato cultivation interacts with the timing of the potato's
    post-Columbian introduction; suitability is determined by agro-climatic conditions (cool temperatures, adequate moisture,
    suitable elevation) that are exogenous to 18th–19th century economic development
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 1600
  implementation_end: 1900
  local_timing: Potato adoption timing varied considerably across the Old World; some regions (Ireland, Low Countries) adopted
    early and intensively, others (southern Europe, much of Asia) adopted later or less intensively
  anticipation: No anticipation — the potato was unknown in the Old World before 1492 and its properties could not have influenced
    pre-Columbian economic trajectories
  last_verified: '2026-07-13'
assignment:
  unit: Country, subnational region, or grid cell
  treated: Regions with high land suitability for potato cultivation, observed after the potato's post-Columbian introduction
  comparison_pool: Regions with low or zero potato suitability; the same regions before the potato's introduction (pre-1600);
    regions outside the Old World
  rule: A region's treatment intensity is determined by the interaction of its agro-climatic suitability for potato cultivation
    (from the FAO Global Agro-Ecological Zones database) with the post-introduction time period (after approximately 1700,
    when potato adoption became widespread)
  intensity: Continuous — the potato suitability index ranges from 0 to 1, reflecting the fraction of land in a region capable
    of supporting potato cultivation; actual adoption intensity is proxied by suitability
  exemptions: []
  compliance: Not all suitable land adopted potatoes; cultural, political, and informational barriers meant actual adoption
    was lower than potential; suitability-based estimates are reduced-form intention-to-treat effects
  exposure_construction: For each Old World country or subnational unit, compute the fraction of land area suitable for potato
    cultivation using GIS data on climate, soil, and elevation; interact suitability with time (post-1700 or post-1750 indicator)
    to create a panel; city-level analyses interact city potato suitability with time
  required_identifiers:
  - country code
  - grid cell or subnational unit
  - calendar period
  - potato suitability index
  spillovers: Potato cultivation in one region may have affected neighboring regions through trade, migration, knowledge diffusion,
    or military competition; high-potato-suitability regions may have attracted migrants from low-suitability regions
research_compatibility:
  outcome_domains:
  - population growth
  - urbanization
  - city growth
  - adult height
  - nutrition
  - agricultural productivity
  - economic development
  - military power
  affected_populations:
  - Old World populations
  - particularly in Europe and temperate Asia; rural agricultural households; urban populations benefiting from lower food
    prices
  mechanism_channels:
  - caloric productivity per acre
  - nutritional improvement
  - population growth
  - surplus labor for urbanization
  - lower food prices
  - reduced famine frequency
  - improved adult health and stature
  best_for:
  - Studying the very-long-run effects of agricultural productivity improvements on population and urbanization
  - Research exploiting the exogenous timing of the Columbian Exchange to identify crop productivity effects
  - Within-country designs using subnational variation in crop suitability
  not_good_for:
  - Short-run or contemporary outcome studies
  - Designs requiring precise adoption timing at high frequency
  - Outcomes not plausibly linked to agricultural productivity or nutrition
  - Identifying mechanisms beyond the reduced-form effect of suitability on population/urbanization
design:
  affordances:
  - the potato was unknown in the Old World before 1492
  - crop suitability is determined by fixed agro-climatic conditions
  - timing of introduction is common across all regions (post-1492)
  - subnational variation in suitability allows within-country comparisons
  candidate_designs:
  - difference-in-differences (potato-suitable versus unsuitable regions × pre/post introduction)
  - panel fixed effects with suitability × time interaction
  - city-level or grid-cell-level cross-sectional regressions
  - instrumental variables using potato suitability as instrument for actual potato adoption
  identifying_variation: The interaction of time-invariant potato land suitability with the post-Columbian introduction period,
    comparing regions that could support potatoes to those that could not, before and after the potato's diffusion
  assumptions: &id001
  - Potato suitability is uncorrelated with other determinants of long-run population and urbanization trends (conditional
    on controls)
  - The potato was the only major crop introduced during the Columbian Exchange whose suitability varied in ways that could
    confound the potato effect
  - Suitability is a reasonable proxy for actual adoption intensity (first-stage relevance)
  - Pre-Columbian population and urbanization trends were not systematically correlated with potato suitability
  diagnostics: &id002
  - Test whether potato suitability predicts pre-1500 population density or urbanization
  - Control for suitability of other New World crops (maize, cassava, sweet potato)
  - Control for Old World crop suitability (wheat, rice) and general agricultural potential
  - Test within-country using subnational variation
  - Use city-level data with city potato suitability and within-country fixed effects
  - Validate using French soldier height data as an individual-level nutritional outcome
  primary_strategy: Difference-in-differences with continuous treatment intensity (potato suitability × post-1700); within-country
    specifications with country fixed effects; city-level analysis with city potato suitability; validation with individual-level
    French soldier height data
  estimand: The causal effect of the recorded exposure on Total population (log), urbanization rate (fraction of population
    living in cities with 10,000+ or 40,000+ inhabitants), adult height (French soldiers), conditional on the stated design
    assumptions.
  treatment_variable: Interaction of country-level or city-level potato land suitability (continuous, 0–1) with an indicator
    for the post-introduction period (after 1700); continuous treatment intensity
  comparison_logic: Within-country comparison across regions with different potato suitabilities; DID comparison of high-suitability
    versus low-suitability regions, before versus after 1700
  estimation_notes: Difference-in-differences with continuous treatment intensity (potato suitability × post-1700); within-country
    specifications with country fixed effects; city-level analysis with city potato suitability; validation with individual-level
    French soldier height data
threats:
- type: correlated-crop-suitability
  basis: inferred
  condition: Potato-suitable land may also be suitable for other productive crops; the estimated potato effect may partly
    reflect general agricultural potential if controls for other crop suitabilities are inadequate
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for suitability of maize
  - cassava
  - sweet potato
  - wheat
  - and rice; test whether potato suitability predicts outcomes incremental to a general agricultural suitability index
- type: differential-pre-trends
  basis: inferred
  condition: Regions suitable for potato cultivation may have been on different population or urbanization trajectories before
    1500; the DID design assumes parallel trends in the absence of the potato
  evidence_refs:
  - E1
  possible_diagnostics:
  - test for pre-1500 population and urbanization differentials by potato suitability
  - use multiple pre-periods
  - restrict to within-country variation
- type: other-Columbian-Exchange-effects
  basis: inferred
  condition: The Columbian Exchange also introduced maize, cassava, sweet potatoes, and other productive crops that may have
    differentially affected regions based on their own suitability patterns; these effects may be conflated with the potato
    effect
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for other New World crop suitabilities
  - compare effect magnitudes across crops
  - examine regions where only one crop is suitable
- type: endogenous-adoption-timing
  basis: inferred
  condition: Within the Old World, earlier-adopting regions may have had different economic or institutional characteristics;
    the reduced-form (suitability × time) design largely avoids this by using potential rather than actual adoption
  evidence_refs:
  - E1
  possible_diagnostics:
  - compare reduced-form (suitability) and IV (suitability → adoption) estimates
  - use recorded adoption dates where available
  - test for correlation between adoption timing and pre-adoption economic characteristics
empirical_requirements:
  contract_version: 1
  population: Old World countries, subnational regions, or cities observed between approximately 1000 and 1900 CE
  observation_unit: Country-period, grid-cell-period, or city-period
  geography_level: Country, subnational region, or city; FAO GAEZ data available at approximately 1 km grid-cell resolution
  time_start: 1000
  time_end: 1900
  minimum_frequency: centennial or 50-year intervals
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields:
  - potato land suitability
  - population
  - urbanization rate
  - other crop suitabilities
  - latitude
  - longitude
  - country or region identifier
  - time period
  required_identifiers:
  - country or region code
  - grid cell ID or city ID
  - time period
  treatment_key:
  - region code
  - time period
  - potato suitability × post-1700 indicator
  treatment_source: FAO Global Agro-Ecological Zones (GAEZ) database for potato land suitability; historical population and
    urbanization data from McEvedy & Jones (1978), Bairoch (1988), and other historical demography sources; French soldier
    height data from Komlos (2003) and other anthropometric history sources
  measurement_risks:
  - historical population data quality varies across regions and periods
  - potato suitability is measured with modern climate data and may not perfectly reflect historical growing conditions
  - potato varieties have changed over time
  - city definitions and boundaries change
  - measurement error in historical urbanization rates
evidence:
- id: E1
  source_type: paper
  citation: 'Nunn, Nathan, and Nancy Qian. 2011. "The Potato''s Contribution to Population and Urbanization: Evidence from
    a Historical Experiment." Quarterly Journal of Economics 126 (2): 593–650.'
  url: https://doi.org/10.1093/qje/qjr009
  date: 2011
  supports:
  - identity
  - assignment
  - design
  - suitability-based identification
  - main estimates
  - within-country analysis
  - height validation
  verification_status: verified
design_applications:
- paper: 'The Potato''s Contribution to Population and Urbanization: Evidence from a Historical Experiment'
  doi: 10.1093/qje/qjr009
  journal: Quarterly Journal of Economics
  year: 2011
  research_question: What was the causal contribution of the potato — a highly nutritious New World crop — to population growth
    and urbanization in the Old World between 1700 and 1900?
  population: Old World countries and cities, approximately 1000–1900
  outcome: Total population (log), urbanization rate (fraction of population living in cities with 10,000+ or 40,000+ inhabitants),
    adult height (French soldiers)
  data_used: []
  treatment_encoding: Interaction of country-level or city-level potato land suitability (continuous, 0–1) with an indicator
    for the post-introduction period (after 1700); continuous treatment intensity
  comparison: Within-country comparison across regions with different potato suitabilities; DID comparison of high-suitability
    versus low-suitability regions, before versus after 1700
  empirical_design: Difference-in-differences with continuous treatment intensity (potato suitability × post-1700); within-country
    specifications with country fixed effects; city-level analysis with city potato suitability; validation with individual-level
    French soldier height data
  assumptions:
  - potato suitability is conditionally orthogonal to long-run development trends
  - other Columbian Exchange crops are not driving the result
  - suitability proxies for actual adoption
  - historical population and urbanization data are sufficiently accurate
  threats_addressed:
  - other crops via suitability controls
  - pre-trends via pre-1500 falsification
  - endogenous adoption via reduced-form design
  - measurement error via multiple outcomes including heights
  - within-country confounding via country fixed effects
  evidence_refs:
  - E1
readiness_blockers:
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
- Transfer to a Chinese application has not yet been audited against a specific Chinese institution and dataset.
method_transfer:
  source_context: 'Old World (Europe and Asia broadly): Introduction of the Potato from the Americas to the Old World as a
    Historical Natural Experiment in Agricultural Productivity'
  strategy_family: Difference-in-differences with continuous treatment intensity (potato suitability × post-1700); within-country
    specifications with country fixed effects; city-level analysis with city potato suitability; validation with individual-level
    French soldier height data
  reusable_logic: Regional variation in land suitability for potato cultivation interacts with the timing of the potato's
    post-Columbian introduction; suitability is determined by agro-climatic conditions (cool temperatures, adequate moisture,
    suitable elevation) that are exogenous to 18th–19th century economic development
  construction_steps:
  - For each Old World country or subnational unit, compute the fraction of land area suitable for potato cultivation using
    GIS data on climate, soil, and elevation; interact suitability with time (post-1700 or post-1750 indicator) to create
    a panel; city-level analyses interact city potato suitability with time
  source_treatment_or_endogenous_variable: Interaction of country-level or city-level potato land suitability (continuous,
    0–1) with an indicator for the post-introduction period (after 1700); continuous treatment intensity
  source_instrument_or_assignment: Regional variation in land suitability for potato cultivation interacts with the timing
    of the potato's post-Columbian introduction; suitability is determined by agro-climatic conditions (cool temperatures,
    adequate moisture, suitable elevation) that are exogenous to 18th–19th century economic development
  first_stage_or_contrast: The interaction of time-invariant potato land suitability with the post-Columbian introduction
    period, comparing regions that could support potatoes to those that could not, before and after the potato's diffusion
  identifying_assumptions: *id001
  diagnostics: *id002
  china_use_cases:
  - Interact agro-climatic crop suitability with documented crop introduction or diffusion timing in Chinese historical regions,
    while separating suitability's direct long-run channels.
  china_data_requirements:
  - potato land suitability
  - population
  - urbanization rate
  - other crop suitabilities
  - latitude
  - longitude
  - country or region identifier
  - time period
  transfer_limits:
  - Short-run or contemporary outcome studies
  - Designs requiring precise adoption timing at high frequency
  - Outcomes not plausibly linked to agricultural productivity or nutrition
  - Identifying mechanisms beyond the reduced-form effect of suitability on population/urbanization
---
## Institutional Background

The Columbian Exchange — the transfer of plants, animals, diseases, and people between the Old and New Worlds following 1492 — was one of the most transformative events in human history. Among the crops transferred, the potato stands out for its exceptional nutritional properties: it provides more calories, protein, and micronutrients per acre than virtually any other Old World staple crop, and it can grow in cool, marginal environments where wheat and rice struggle. [E1]

Before 1492, the potato was unknown outside the Andes. After its introduction by Spanish explorers in the late 16th century, it diffused gradually across Europe and parts of Asia, with adoption concentrated in regions where growing conditions were favorable — Ireland, the Low Countries, the German states, Poland, Russia, and highland areas of southern Europe. By the 18th century, the potato had become a dietary staple for much of northern and eastern Europe. [E1]

## What Changed

The potato dramatically increased agricultural productivity in suitable regions. Its caloric yield per acre was roughly two to three times that of wheat or barley, and it provided vitamin C (preventing scurvy), B vitamins, potassium, and high-quality protein. This nutritional windfall allowed populations in potato-suitable regions to grow more rapidly, support higher urbanization rates, and achieve better adult health outcomes. [E1]

## Implementation and Assignment

The design exploits two sources of variation: (1) the exogenous timing of the potato's introduction — common across all Old World regions due to the Columbian Exchange; and (2) cross-regional variation in land suitability for potato cultivation — determined by climate, soil, and elevation, which are fixed agro-ecological characteristics. The interaction of these two sources of variation identifies the causal effect of potato availability on population and urbanization. Crucially, neither factor is endogenous to 18th–19th century economic development. [E1; analytical inference]

## Why This Creates Empirical Variation

This design is a canonical example of a historical natural experiment using a difference-in-differences strategy. The "treatment" is not a policy but a biological event — the introduction of a highly productive crop to regions capable of growing it. The timing is given by history (the Columbian Exchange); the cross-sectional variation is given by geography (agro-climatic suitability). Neither is under the control of the affected populations. This allows causal identification of agricultural productivity effects on population and urbanization at a multi-century time scale that would be impossible with contemporary data. [E1; analytical inference]

## Identification Risks

The most important threat is that potato-suitable land may have had different long-run development potential for reasons unrelated to potatoes. Cold-climate, higher-elevation regions suitable for potatoes may have followed different development trajectories than warm, lowland regions suitable for wheat or rice. The authors address this by controlling for other crop suitabilities, including country fixed effects (using within-country variation), and testing whether potato suitability predicts pre-1500 population differences. A second concern is that other New World crops (maize, cassava) also diffused during the Columbian Exchange, and their suitabilities may be correlated with potato suitability. [E1; analytical inference]

## Data Requirements

The design requires: (1) GIS-based potato land suitability data (FAO GAEZ); (2) historical population and urbanization estimates covering 1000–1900; (3) suitability data for other crops as controls; (4) subnational or city-level data for within-country specifications. The FAO GAEZ data are publicly available at high resolution; historical population data are more heterogeneous in quality and coverage. The French soldier height data provide a valuable individual-level validation sample. [E1]

## Evidence Notes

E1 is the published QJE article. The central estimate — that the potato accounts for approximately one-quarter of Old World population and urbanization growth between 1700 and 1900 — is remarkably large and has been influential in both the long-run development literature and the agricultural productivity literature. The use of French soldier heights (a direct nutritional outcome) provides a compelling cross-validation of the aggregate population results. The paper is a leading example of how historical natural experiments can be used to answer questions about very-long-run economic development.
