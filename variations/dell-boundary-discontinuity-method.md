---
schema_version: 2
id: dell-boundary-discontinuity-method
name: Boundary Discontinuity Design (Dell Mining Mita)
aliases:
- Dell mining mita RD
- geographic regression discontinuity
- spatial boundary discontinuity
- multi-dimensional regression discontinuity
status: extracted
provenance:
  task_id: task-7beb0167a7b7
scope:
  country: Peru
  regions:
  - Southern Peruvian Andes
  - mita boundary catchment districts
  - Departments of Cusco, Puno, Arequipa, Apurímac, Huancavelica
  domains:
  - economic-history
  - development
  - institutions
  - political-economy
  - spatial-econometrics
  - regional-economics
  variation_type: boundary-discontinuity
  knowledge_role: transferable-method
  china_relevance: The geographic boundary discontinuity design transfers directly to Chinese
    settings with sharp historical or administrative borders, such as Huai River heating
    policy boundaries, treaty-port jurisdictions, county administrative borders that
    partition historical land-reform treatment, ecological conservation red lines, and
    special economic zone or development-zone boundaries.
identity:
  instrument: Geographic regression discontinuity at the boundary of a historically assigned
    institution — the Spanish colonial mining mita — comparing observations just inside
    and just outside the subjected region.
  authority: Melissa Dell (2010, Econometrica)
  legal_identifiers:
  - "Dell, Melissa. 2010. 'The Persistent Effects of Peru's Mining Mita.' Econometrica
    78(6): 1863-1903."
  - "Dell, Melissa. 2010. NBER Working Paper No. 16005 (August 2010)."
  implementation_regime: Spanish colonial authorities required indigenous communities
    within a contiguous southern Peruvian region to supply one-seventh of their adult
    male population as rotating forced labor for the Potosi silver and Huancavelica
    mercury mines from 1573 until abolition in 1812. Communities immediately outside
    the boundary were exempt. The boundary was determined by distance to the mines and
    administrative cost, creating a sharp geographic discontinuity in exposure to forced
    labor.
  assignment_mechanism: Deterministic and discontinuous assignment based on geographic
    location relative to the mita boundary. Districts on one side of the boundary were
    subjected; districts on the other side were exempt.
  parent: null
  related_variations:
  - china-huai-river-heating-air-pollution
  - china-heating-policy-air-pollution-wtp
  - china-water-quality-monitoring-rd
  - us-railroad-market-access-method
timeline:
  announcement: null
  effective: '1573'
  implementation_start: 1573
  implementation_end: 1812
  local_timing: The mita operated from 1573 to 1812. Long-run outcome data come from
    the 2001 Peruvian National Household Survey (ENAHO) and a 2000s Ministry of Education
    height census of school children. Historical channel data include a 1689 hacienda
    census, 1876 and 1940 censuses, and modern road and agricultural census data.
  anticipation: Indigenous communities could not anticipate or alter the boundary drawn
    in the 1570s; flight was restricted by colonial residence and land-tenure rules.
  last_verified: '2026-07-14'
assignment:
  unit: Household or district, depending on outcome data; geographic location measured
    at the district capital.
  treated: Districts inside the mita catchment boundary.
  comparison_pool: Districts just outside the mita catchment boundary, within narrow
    geographic bandwidths (e.g., 25, 50, 75, 100 km).
  rule: Assign treatment based on which side of the historical boundary a unit's district
    capital falls. Estimate a local polynomial regression discontinuity using geographic
    location as the running variable.
  intensity: Binary at the boundary (subjected vs. exempt); intensity of forced labor
    historically declined with distance to Potosi/Huancavelica.
  exemptions: []
  compliance: Near-perfect within the catchment; colonial records show communities contributed
    conscripts or cash substitutes.
  exposure_construction: Geocode observations to district capitals. Compute distance
    to the mita boundary or project location onto latitude/longitude or distance to Potosi.
    Interact the mita indicator with smooth functions of location and include boundary-segment
    fixed effects.
  required_identifiers:
  - geographic coordinates (longitude, latitude) or district identifier
  - mita-boundary polygon
  - outcome measure
  - boundary-segment identifier
  spillovers: Cross-boundary migration and trade are examined as potential threats; population
    correlations over time and migration rates do not show large discontinuities, suggesting
    limited arbitrage.
research_compatibility:
  outcome_domains:
  - household-consumption
  - child-stunting
  - human-capital
  - land-tenure
  - public-goods-provision
  - road-infrastructure
  - agricultural-structure
  - long-run-development
  affected_populations:
  - indigenous households in southern Peru
  - smallholder farmers
  - school-age children
  - historical mita conscripts
  mechanism_channels:
  - forced labor extraction
  - restricted hacienda development and communal land tenure
  - lower public goods and education investment
  - weaker road network integration
  - persistence of subsistence agriculture
  best_for:
  - Estimating long-run effects of historical institutions with sharp geographic boundaries
  - Settings where a boundary divides otherwise similar jurisdictions
  - Outcomes measured at the household, firm, or district level with geocoded data
  - Testing whether institutional effects persist through land tenure or public goods
  not_good_for:
  - Boundaries that were drawn endogenously to economic potential
  - Settings with substantial sorting or displacement across the boundary
  - Outcomes without reliable geocoding close to the boundary
  - Cases where the boundary coincides with modern administrative or ethnic divisions
    that also affect outcomes
design:
  claim_type: method-pattern
  affordances:
  - Converts a historical boundary into a credible local counterfactual
  - Allows flexible polynomial control for smooth geographic trends
  - Can be implemented in one or two geographic dimensions
  - Boundary-segment fixed effects absorb heterogeneity along different portions of the
    border
  - Spatial standard errors account for geographic correlation
  candidate_designs:
  - Two-dimensional polynomial in latitude and longitude interacted with the mita indicator
  - One-dimensional polynomial in Euclidean distance to Potosi interacted with the mita
    indicator
  - One-dimensional polynomial in distance to the nearest point on the mita boundary
  - Nonparametric RD with small bandwidths if georeferenced microdata are available
  - Fuzzy RD if assignment was imperfect at the boundary
  identifying_variation: The discrete change in historical forced-labor status at the
    mita boundary, conditional on smooth functions of geographic location.
  primary_strategy: Estimate a regression discontinuity at the boundary using a polynomial
    in geographic location, boundary-segment fixed effects, and geographic controls (elevation,
    slope). Compare outcomes just inside and just outside the boundary.
  estimand: The local average effect of being subjected to the mita at the boundary on
    long-run economic outcomes.
  treatment_variable: Mita indicator equal to 1 if the district was inside the catchment
    boundary and 0 otherwise.
  comparison_logic: Observations immediately outside the boundary provide the counterfactual
    for observations immediately inside, under the assumption that expected potential outcomes
    vary smoothly across the boundary except for the treatment.
  estimation_notes: Dell reports semiparametric specifications because many data sets lack
    precise address-level geocoding. Standard errors are robust and, where noted, adjusted
    for spatial correlation following Conley (1999). Results are reported for multiple bandwidths
    and polynomial orders.
  assumptions:
  - Potential outcomes are continuous in geographic location at the boundary.
  - The boundary was not drawn to select on unobserved determinants of modern outcomes.
  - Geographic controls (elevation, slope) capture the main smooth confounders.
  - Boundary-segment fixed effects absorb local heterogeneity along the border.
  - Migration and sorting are limited enough that the local counterfactual remains valid.
  diagnostics:
  - Test for balance in geographic characteristics (elevation, slope) at the boundary
  - Test for balance in ethnicity, language, pre-mita settlement, and tribute obligations
  - Report estimates for multiple bandwidths and polynomial orders
  - Show robustness to different running variables (lat/long, distance to Potosi, distance
    to boundary)
  - Check for discontinuities in migration rates and population persistence
  - Use Conley spatial standard errors or cluster by district
  - Plot outcome and covariate means against the running variable
threats:
- type: endogenous-boundary-drawing
  basis: reported
  condition: If Spanish authorities placed the boundary to select on economic or demographic
    characteristics that also affect modern outcomes, the RD comparison is invalid.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Test pre-mita tribute and settlement data for discontinuities
  - Compare geographic and ethnic characteristics across the boundary
  - Examine historical documents on boundary placement criteria
- type: selective-migration
  basis: reported
  condition: Forced labor could have induced selective flight from mita districts, generating
    persistent compositional differences.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Compare migration rates across the boundary using census data
  - Test for discontinuities in ancestral residence using parish records
  - Assess sensitivity to population weights
- type: spatial-spillovers
  basis: inferred
  condition: Economic interactions across the boundary may blur the treatment contrast.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Use Conley spatial standard errors
  - Vary the bandwidth to detect spillover patterns
  - Define treatment using distance to boundary rather than side
- type: measurement-error-in-boundary
  basis: inferred
  condition: Modern district boundaries or imprecise geocoding may misclassify observations
    near the historical boundary.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Validate boundary polygon against historical maps
  - Use alternative distance metrics
  - Drop observations very close to ambiguous boundary segments
- type: external-validity
  basis: inferred
  condition: The Peruvian Andean context may differ from other geographic boundary settings
    in ways that affect transferability.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Replicate the design in other boundary settings (e.g., China treaty ports)
  - Test for heterogeneous effects by boundary segment
  - Compare estimates across outcomes and time periods
empirical_requirements:
  contract_version: 1
  population: Geocoded households, districts, or other units located near a sharp historical
    or administrative boundary.
  observation_unit: Household or district.
  geography_level: District capital coordinates or geocoded household coordinates.
  time_start: null
  time_end: null
  minimum_frequency: cross-sectional
  minimum_pre_periods: 0
  minimum_post_periods: 1
  required_fields:
  - geographic coordinates or district identifier
  - boundary polygon
  - outcome of interest
  - geographic controls (elevation, slope, soil, climate)
  - boundary-segment identifier
  - optional pre-boundary covariates for balance tests
  required_identifiers:
  - unit identifier
  - longitude
  - latitude
  treatment_key:
  - unit identifier
  - mita indicator
  - running variable
  treatment_source: Constructed from the historical mita boundary polygon and unit coordinates.
  measurement_risks:
  - Historical boundary maps may be imprecise or contested.
  - Geocoding may be at the district capital rather than the household location.
  - Outcome surveys may undersample remote areas near the boundary.
  - Spatial correlation can bias conventional standard errors.
  - Modern administrative boundaries may not match historical jurisdictions.
evidence:
- id: E1
  source_type: paper
  citation: "Dell, Melissa. 2010. 'The Persistent Effects of Peru's Mining Mita.' Econometrica
    78(6): 1863-1903."
  url: https://doi.org/10.3982/ECTA8121
  date: 2010
  supports:
  - identity
  - timeline
  - design
  verification_status: reported
  access_level: abstract
  locator: Econometrica article abstract and official bibliographic page (DOI 10.3982/ECTA8121)
- id: E2
  source_type: paper
  citation: "Dell, Melissa. 2010. 'The Persistent Effects of Peru's Mining Mita.' Econometrica
    78(6): 1863-1903."
  url: http://www.ralfmeisenzahl.com/uploads/7/6/8/1/76818505/dell.pdf
  date: 2010
  supports:
  - identity
  - timeline
  - assignment
  - design
  - threats
  - empirical_requirements
  - design_applications
  - method_transfer
  verification_status: verified
  access_level: full-text
  locator: PDF of published Econometrica article, Sections 2-4 and Tables I-II
design_applications:
- paper: 'The Persistent Effects of Peru''s Mining Mita'
  doi: 10.3982/ECTA8121
  journal: Econometrica
  year: 2010
  research_question: Did the Spanish colonial mining mita have persistent effects on household
    consumption, child stunting, and institutional channels in subjected districts?
  population: Households and districts in southern Peru within 100 km of the mita boundary.
  outcome: Equivalent household consumption (ENAHO 2001); child stunting (Ministry of Education
    height census); hacienda concentration, education, road integration, and subsistence
    farming.
  data_used:
  - 2001 Peruvian National Household Survey (ENAHO)
  - Ministry of Education height census of 6-9 year old school children
  - 1689 district-level hacienda data
  - 1876 and 1940 census data
  - Modern agricultural census
  - SRTM elevation and slope data
  - Historical mita boundary from Saignes (1984) and Amat y Junient (1947)
  treatment_encoding: Binary mita indicator based on district location relative to the historical
    boundary.
  comparison: Districts just inside vs. just outside the mita boundary, within geographic
    bandwidths of 25-100 km.
  empirical_design: Geographic regression discontinuity with polynomial controls for location,
    boundary-segment fixed effects, and geographic covariates; spatial standard errors.
  assumptions:
  - Potential outcomes vary smoothly across the mita boundary
  - The boundary was not drawn on modern outcome-relevant unobservables
  - Controls for elevation and slope capture smooth geographic confounders
  threats_addressed:
  - Balance tests on elevation, slope, ethnicity, language, tribute, and settlement
  - Multiple running variables and bandwidths
  - Spatial correlation robustness
  - Migration and population persistence checks
  evidence_refs:
  - E1
  - E2
method_transfer:
  source_context: Dell (2010, Econometrica) studies the long-run impacts of the Spanish
    colonial mining mita in Peru and Bolivia. She exploits the sharp geographic boundary
    of the mita catchment to implement a regression discontinuity design comparing modern
    outcomes on either side of the boundary.
  strategy_family: Geographic boundary regression discontinuity
  reusable_logic: When a historical or administrative institution was assigned discontinuously
    at a known geographic boundary, units just on either side of the boundary provide a
    credible local counterfactual. A regression discontinuity design controls for smooth
    geographic variation and identifies the local effect of the institution at the boundary.
  construction_steps:
  - Obtain a georeferenced boundary polygon for the institution or policy region.
  - Geocode observations to coordinates or to district centroids.
  - Assign a binary treatment indicator based on which side of the boundary each observation
    falls.
  - Choose a running variable (e.g., Euclidean distance to the boundary, distance to a focal
    point, or latitude/longitude projection).
  - Restrict the sample to observations within a narrow bandwidth of the boundary.
  - Estimate a local polynomial RD with boundary-segment fixed effects and geographic controls.
  - Report results for multiple bandwidths, polynomial orders, and running variables.
  - Use spatial standard errors to account for geographic correlation.
  - Conduct balance tests on pre-boundary covariates and placebo outcomes.
  source_treatment_or_endogenous_variable: Long-run economic outcomes such as household consumption,
    child health, human capital, land tenure, public goods, and agricultural structure.
  source_instrument_or_assignment: The historical mita boundary, which deterministically assigned
    districts to forced-labor subjection or exemption based on geographic location.
  first_stage_or_contrast: Contrast units immediately inside the mita boundary with units
    immediately outside; the first stage is the near-perfect assignment of districts to
    treatment by the boundary rule.
  identifying_assumptions:
  - Potential outcomes are smooth in geographic location at the boundary.
  - The boundary was not drawn to select on determinants of the outcomes studied.
  - There is limited sorting or selective migration across the boundary.
  - Geographic controls absorb the main smooth confounders.
  diagnostics:
  - Balance tables for geographic, ethnic, and pre-boundary covariates
  - Plots of outcome and covariate means against the running variable
  - Sensitivity to bandwidth and polynomial order
  - Robustness to alternative running variables
  - Spatial standard errors (Conley) or district clustering
  - Checks for migration, sorting, and spillovers
  china_use_cases:
  - Estimate long-run effects of treaty-port boundaries on local development in China
  - Evaluate impacts of Huai River heating policy boundary on health and human capital
  - Study effects of historical land-reform boundaries on modern agricultural productivity
  - Assess consequences of county administrative-border changes on public goods provision
  - Analyze impacts of ecological conservation red lines on land use and welfare
  - Examine special economic zone or development-zone boundary effects on firm outcomes
  china_data_requirements:
  - Georeferenced boundary polygon for the Chinese policy or institution
  - Geocoded household, firm, or district-level data near the boundary
  - Geographic controls such as elevation, slope, distance to rivers, and climate variables
  - Historical maps or gazetteers documenting the boundary origin
  - Outcome data (e.g., census, household surveys, administrative records)
  - Boundary-segment identifiers to allow for local fixed effects
  transfer_limits:
  - Requires a sharp, well-documented boundary and accurate geocoding.
  - Chinese boundaries may coincide with administrative, ethnic, or economic divisions that
    also affect outcomes.
  - Long-run persistence mechanisms may differ between Peru and China.
  - Microdata with precise coordinates are often unavailable; district-centroid geocoding
    can introduce measurement error.
  - Spatial correlation and spillovers across boundaries require careful inference.
readiness_blockers:
- The original replication data and code were not accessed; researchers should reconstruct
  the boundary and geocoding from historical sources and survey data.
- Some institutional background on the mita relies on secondary historical sources cited
  in the published paper.
---
---
## Institutional Background

The Spanish Crown imposed the mining mita in 1573 to supply forced labor to the Potosi silver mines (in modern Bolivia) and the Huancavelica mercury mines (in modern Peru). Indigenous communities within a contiguous southern Peruvian region were required to send one-seventh of their adult male population as rotating conscripts. Communities just outside the boundary were exempt. The boundary was drawn in the 1570s based on distance to the mines and the Crown's administrative cost calculations, producing a sharp geographic discontinuity in exposure to one of colonial Latin America's largest forced-labor systems [E2].

## What Changed

At the mita boundary, the obligation to supply forced labor changed discontinuously from full subjection to exemption. This boundary persisted in administrative memory and affected land-tenure institutions: colonial policy restricted hacienda estates inside the mita region and promoted communal tenure, while large landowners developed outside the boundary. After independence, communal land in mita districts was not replaced by secure individual titling, contributing to a different long-run trajectory of public goods and agricultural structure [E2].

## Implementation and Assignment

Treatment assignment is binary and determined by whether a district lies inside or outside the historical mita boundary. Dell geocodes observations to district capitals and estimates a geographic regression discontinuity. The baseline specification includes a polynomial in latitude and longitude, boundary-segment fixed effects, and controls for elevation and slope. Alternative specifications use a polynomial in Euclidean distance to Potosi or distance to the nearest point on the boundary [E2].

## Why This Creates Empirical Variation

Districts on opposite sides of the boundary were exposed to very different colonial institutions for more than two centuries, yet they are geographically close and share similar Andean terrain. Under the assumption that other determinants of modern outcomes vary smoothly across the boundary, the side of the boundary provides a source of exogenous institutional variation. Dell documents that elevation, slope, ethnicity, language, pre-mita settlement, and tribute obligations are balanced at the boundary, supporting the RD comparison [E2].

## Identification Risks

The main risks are (i) endogenous placement of the boundary if Spanish authorities selected on unobserved characteristics correlated with modern outcomes; (ii) selective migration and flight from mita districts, which could create persistent population composition differences; (iii) spatial spillovers and economic interactions across the boundary; (iv) measurement error in the historical boundary and in geocoding; and (v) limited external validity when transferring the design to Chinese boundaries with different institutional contexts [E2].

## Data Requirements

The design requires a georeferenced boundary polygon, geocoded observations with outcome data, geographic controls, and ideally pre-boundary covariates for balance tests. For Chinese applications, this means digitized boundaries (e.g., treaty-port jurisdictions, Huai River boundary, SEZ boundaries), geocoded household or firm microdata, and historical maps or gazetteers documenting the boundary origin [E2].

## Evidence Notes

The published article is Dell (2010, *Econometrica*, E1). The full text was accessed through a mirrored PDF (E2), which confirms the boundary discontinuity design, balance tests, estimation equations, and main results. Official bibliographic information and abstract are available from the Econometric Society (E1) [E1; E2].
