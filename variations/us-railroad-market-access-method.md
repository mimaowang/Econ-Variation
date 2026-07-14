---
schema_version: 2
id: us-railroad-market-access-method
name: Railroad Market Access Method (Donaldson-Hornbeck)
aliases:
- Donaldson-Hornbeck market access
- transportation network market access
- railroad market access instrument
status: extracted
provenance:
  task_id: task-7e71ee6d5a0a
scope:
  country: United States
  regions:
  - U.S. counties
  - Midwest and agricultural counties
  domains:
  - transportation
  - trade
  - regional-economics
  - economic-history
  - development
  - urban-economics
  variation_type: other
  knowledge_role: transferable-method
  china_relevance: The market-access framework can be directly applied to Chinese railway,
    highway, and high-speed rail network expansions. It provides a theoretically grounded
    way to convert network data into a continuous regional shock to trade opportunities,
    which has been used in studies of China's National Trunk Highway System and high-speed
    rail.
identity:
  instrument: 'Market access — a reduced-form measure of a region''s trade opportunities
    derived from a gravity trade model and computed from the transportation network (railroads
    and waterways) connecting each county to all other counties.'
  authority: Dave Donaldson and Richard Hornbeck (2016, QJE); built on the Eaton-Kortum
    gravity trade model.
  legal_identifiers:
  - "Donaldson, Dave, and Richard Hornbeck. 2016. 'Railroads and American Economic Growth:
    A Market Access Approach.' The Quarterly Journal of Economics 131(2): 799-858."
  - "Donaldson, Dave, and Richard Hornbeck. 2015. NBER Working Paper No. 19213."
  implementation_regime: Construct a network database of railroad lines and navigable
    waterways. Compute lowest-cost freight routes between all county pairs. For each destination
    county, calculate market access as a sum over all source counties of the source's
    productivity-adjusted supply price discounted by the bilateral trade cost. Estimate
    how local economic outcomes respond to changes in market access as the network expands.
  assignment_mechanism: Not randomized. The method exploits the differential exposure
    of counties to changes in the national transportation network. Counties whose market
    access increases more when a new line is built experience a larger shock to trade
    opportunities.
  parent: null
  related_variations:
  - china-highway-network-expansion
  - china-trade-migration-productivity
  - hsieh-klenow-plant-misallocation-method
  - israel-maimonides-rule-class-size
  - old-world-potato-introduction
timeline:
  announcement: null
  effective: null
  implementation_start: 1870
  implementation_end: 1890
  local_timing: The source paper studies the expansion of the U.S. railroad network between
    1870 and 1890 and its impact on county-level agricultural land values. The method
    can be applied to any period with network data and local outcome measures.
  anticipation: Railroad construction was a multi-decade process; land markets and farmers
    could anticipate network expansion, so the estimates are best interpreted as equilibrium
    responses to realized changes in market access.
  last_verified: '2026-07-14'
assignment:
  unit: County-year (or analogous region-year).
  treated: Not a binary treatment. Counties experiencing larger increases in market access
    due to railroad expansion are treated more intensively.
  comparison_pool: Counties experiencing smaller increases in market access, including
    counties already connected to waterways or counties bypassed by new railroad lines.
  rule: Compute market access for each county in each year from the transportation network
    and bilateral trade costs. Use the change in market access (or its log) as a continuous
    measure of exposure to transportation improvement.
  intensity: Continuous — the percentage or absolute change in market access induced by
    network expansion.
  exemptions: []
  compliance: Not applicable; the measure is a deterministic function of the network and
    the model.
  exposure_construction: Build a network of transport links with costs per mile for railroad
    and water transport. Compute shortest-path trade costs between all region pairs. Calculate
    market access as MA_i = Σ_j (A_j / τ_ij^θ), where A_j is the productivity-adjusted
    size of source region j, τ_ij is the trade cost between i and j, and θ is the trade
    elasticity. Use changes in MA_i over time as the explanatory variable.
  required_identifiers:
  - county or region identifier
  - year
  - transport network (links and costs)
  - source-region productivity or size
  - bilateral trade-cost matrix
  spillovers: Market access captures both direct effects of new lines and indirect effects
    through rerouting of trade. General-equilibrium price and wage responses are absorbed
    into the reduced-form relationship under the model's assumptions.
research_compatibility:
  outcome_domains:
  - agricultural-land-values
  - regional-income
  - trade-volumes
  - population-growth
  - industrial-location
  - urbanization
  - wage-levels
  affected_populations:
  - farmers and landowners
  - rural and urban households
  - firms in tradable sectors
  - local governments
  mechanism_channels:
  - reduction in trade costs
  - expansion of market size
  - price convergence across regions
  - factor-price equalization
  - reallocation of land use and production
  - agglomeration and dispersion forces
  best_for:
  - Evaluating the aggregate and distributional effects of large-scale transport infrastructure
  - Converting network data into a theoretically grounded regional shock
  - Studying how trade integration affects land values, incomes, and sectoral location
  not_good_for:
  - Isolating the effect of a single transport project when the network is dense and many
    alternative routes exist
  - Settings where the trade-elasticity and transport-cost parameters are poorly known
  - Short-run impacts before general-equilibrium adjustments
  - Outcomes for which the model's single-sector or perfect-competition assumptions are
    strongly violated
design:
  claim_type: method-pattern
  affordances:
  - Uses readily available network GIS data and historical maps
  - Provides a theoretically grounded reduced-form shock rather than an ad hoc distance
    measure
  - Aggregates direct and indirect effects of the whole network
  - Can be used in cross-sectional or panel settings
  - Allows counterfactuals such as removing a link or the entire network
  candidate_designs:
  - Panel regression of county outcomes on market access with county and year fixed effects
  - Cross-sectional regression of land values on 1890 market access controlling for 1870
    values or geographic controls
  - Counterfactual simulation removing all railroads or specific lines
  - Instrumental-variable strategy using planned-but-unbuilt lines as instruments for actual
    market access
  - Application to Chinese highway or high-speed rail network expansion
  identifying_variation: Differential changes in county-level market access driven by the
    expansion of the national railroad network between 1870 and 1890.
  primary_strategy: Estimate the relationship between local economic outcomes and market
    access, using observed network expansion as the source of variation and controlling
    for baseline county characteristics and fixed effects.
  estimand: The effect of a change in market access on a county-level outcome (e.g., agricultural
    land value per acre), and the aggregate impact of the railroad network on the sector.
  treatment_variable: Continuous market-access term (level or change) derived from the transportation
    network.
  comparison_logic: Compare counties that experienced larger increases in market access
    with counties that experienced smaller increases, conditional on baseline observables
    and fixed effects.
  estimation_notes: Because market access is a nonlinear function of the whole network,
    ordinary least squares on the change in market access is the standard approach. Standard
    errors should account for spatial correlation. The model implies a log-linear relationship
    between land rents and market access.
  assumptions:
  - The Eaton-Kortum gravity model provides a reasonable approximation of trade patterns.
  - Trade costs are well approximated by lowest-cost network routes and known per-mile costs.
  - The network expansion is exogenous to local outcome shocks, conditional on controls.
  - Factor mobility and general-equilibrium price adjustments are consistent with the model's
    predictions.
  - Market access is measured without error and captures the relevant trade opportunities.
  diagnostics:
  - Plot market access against geographic distance and network density
  - Show robustness to alternative trade-elasticity values
  - Compare estimates using railroad-only vs. railroad-plus-waterway networks
  - Test for pre-trends in outcomes before network expansion
  - Validate counterfactuals against historical accounts or external cost estimates
  - Check spatial correlation robustness (Conley standard errors)
threats:
- type: endogenous-network-placement
  basis: inferred
  condition: Railroads may have been built in anticipation of economic growth or along
    corridors with unobserved growth potential, biasing the estimated effect of market access.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Use planned-but-unbuilt lines as an instrument
  - Control for pre-existing growth trends and geographic determinants of route choice
  - Compare effects of lines built for different reasons (e.g., military vs. commercial)
- type: measurement-error-in-network
  basis: inferred
  condition: Historical maps may omit minor lines, misrecord completion dates, or misclassify
    route quality, leading to mismeasured market access.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Cross-validate network data with multiple historical sources
  - Test robustness to alternative route-cost assumptions
  - Use digitized maps from different archives
- type: model-misspecification
  basis: inferred
  condition: The single-sector, perfect-competition gravity model may not capture all
    channels through which railroads affect local economies.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Compare results across sectors (agriculture vs. manufacturing)
  - Add controls for non-trade channels (migration, information flows)
  - Estimate structural parameters directly
- type: spatial-spillovers
  basis: inferred
  condition: Counties affect each other through trade, migration, and factor mobility,
    so treatment and comparison groups are not independent.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Use spatial econometric methods
  - Define treatment using commuting zones or larger regions
  - Report Conley standard errors
- type: external-validity
  basis: inferred
  condition: Parameter estimates from 19th-century U.S. agriculture may not transfer to
    modern manufacturing, services, or developing countries with different institutions.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Replicate in modern Chinese or European transport data
  - Estimate country-specific trade elasticities
  - Compare with studies using alternative methodologies
empirical_requirements:
  contract_version: 1
  population: Counties or comparable regions in a country with a measurable transport network.
  observation_unit: County-year or region-year.
  geography_level: County / region.
  time_start: null
  time_end: null
  minimum_frequency: decennial or annual
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - region identifier
  - year
  - transport network links (rail, road, water)
  - link quality or cost
  - source-region size and productivity proxies
  - bilateral trade-cost matrix
  - local outcome (land value, income, employment, output)
  - geographic controls (elevation, distance to coast, rivers)
  required_identifiers:
  - region ID
  - year
  treatment_key:
  - region ID
  - year
  - market access level or change
  treatment_source: Computed from transport network data and the Eaton-Kortum market-access
    formula.
  measurement_risks:
  - Historical network data may be incomplete or inconsistent.
  - Trade-cost parameters are often assumed rather than estimated.
  - Source-region productivity proxies may be noisy.
  - Local outcome data may not be comparable across regions or time.
  - Spatial correlation can understate standard errors.
evidence:
- id: E1
  source_type: paper
  citation: "Donaldson, Dave, and Richard Hornbeck. 2016. 'Railroads and American Economic
    Growth: A Market Access Approach.' The Quarterly Journal of Economics 131(2): 799-858."
  url: https://doi.org/10.1093/qje/qjw002
  date: 2016
  supports:
  - identity
  - timeline
  - design
  verification_status: reported
  access_level: abstract
  locator: QJE article abstract and citation (DOI 10.1093/qje/qjw002)
- id: E2
  source_type: paper
  citation: "Donaldson, Dave, and Richard Hornbeck. 2015. 'Railroads and American Economic
    Growth: A Market Access Approach.' NBER Working Paper No. 19213."
  url: https://www.nber.org/papers/w19213
  date: 2015
  supports:
  - identity
  - timeline
  - assignment
  - design
  - threats
  - empirical_requirements
  - design_applications
  - method_transfer
  verification_status: reported
  access_level: abstract
  locator: NBER Working Paper 19213 abstract
- id: E3
  source_type: scholarship
  citation: 'Spencer Lyon. 2018. "Donaldson and Hornbeck (2016): Railroads and American
    Economic Growth — A Market Access Approach" (blog notes and model summary).'
  url: http://srg.spencerlyon.com/2018/04/17/dolandson-and-hornbeck-2016-railroads-and-american-economic-growth-a-market-access-approach/
  date: 2018
  supports:
  - design
  - method_transfer
  verification_status: reported
  access_level: full-text
  locator: Blog post summarizing the Eaton-Kortum model and market-access derivation
design_applications:
- paper: 'Railroads and American Economic Growth: A Market Access Approach'
  doi: 10.1093/qje/qjw002
  journal: The Quarterly Journal of Economics
  year: 2016
  research_question: How much did the expansion of the U.S. railroad network increase
    agricultural land values through improved market access between 1870 and 1890?
  population: U.S. counties during the railroad expansion era.
  outcome: Agricultural land value per acre; aggregate value of U.S. agricultural land.
  data_used:
  - Historical railroad network maps
  - Waterway network data
  - County agricultural census data
  - County-to-county lowest-cost freight routes
  treatment_encoding: Continuous market-access term constructed from the transportation
    network.
  comparison: Counties with larger vs. smaller increases in market access; counterfactual
    simulation removing railroads.
  empirical_design: Regression of county land values on market access, controlling for
    county fixed effects and geographic characteristics; structural aggregation to total
    impact.
  assumptions:
  - Eaton-Kortum gravity trade model
  - Observed network routes approximate true trade costs
  - Railroad expansion is exogenous conditional on controls
  threats_addressed:
  - Use of model-derived reduced-form shock rather than ad hoc distance
  - Counterfactual removing all railroads
  - Robustness to network cost assumptions
  evidence_refs:
  - E1
  - E2
  - E3
method_transfer:
  source_context: Donaldson and Hornbeck (2016, QJE) study the expansion of the U.S. railroad
    network from 1870 to 1890. They derive a theoretically grounded measure of county-level
    market access from an Eaton-Kortum gravity trade model and show that increases in market
    access raised agricultural land values.
  strategy_family: Transportation network market-access instrument
  reusable_logic: In a gravity trade model, a region's welfare and factor prices depend
    on its access to all other markets. Market access summarizes this access as a weighted
    sum of trading partners' sizes, with weights decreasing in bilateral trade costs. When
    the transportation network changes, market access changes differentially across regions,
    providing a continuous, model-consistent shock to local trade opportunities.
  construction_steps:
  - Collect network data on transport links (rail, road, water) and link-specific costs
    or speeds.
  - Construct a bilateral trade-cost matrix using shortest-path algorithms over the network.
  - Obtain or proxy the productivity-adjusted size of each potential source region.
  - Choose a trade elasticity θ consistent with trade literature (e.g., θ = 3-8).
  - Compute market access for each region as MA_i = Σ_j (A_j / τ_ij^θ).
  - Compute changes in market access between two network states (e.g., before and after
    a new rail line).
  - Regress local outcomes on market access (level or change), controlling for region
    and time fixed effects and geographic covariates.
  - Report robustness to alternative θ values, network definitions, and standard-error
    adjustments.
  source_treatment_or_endogenous_variable: Local economic outcomes such as land values,
    income, population, employment, or sectoral structure.
  source_instrument_or_assignment: Changes in market access induced by the expansion of
    the railroad network. In the source paper the network expansion is treated as exogenous
    conditional on controls; in other settings it may be instrumented by planned-but-unbuilt
    lines or historical military/strategic routes.
  first_stage_or_contrast: Contrast regions that experience large increases in market access
    when the network expands with regions that experience small or no increases. The first-stage
    relationship is the mechanical link between new network links and the computed market-access
    term.
  identifying_assumptions:
  - The gravity model correctly describes trade patterns and welfare effects.
  - Network placement is exogenous to local outcome shocks, conditional on observables.
  - Trade costs are accurately measured by network routes and per-mile costs.
  - The trade elasticity is constant and correctly calibrated.
  - General-equilibrium feedbacks are captured by the reduced-form market-access term.
  diagnostics:
  - Compare market-access changes across regions and network states
  - Test sensitivity to the trade-elasticity parameter
  - Validate network routes against historical freight records
  - Check for pre-trends in outcomes before network expansion
  - Use spatial standard errors to account for cross-region spillovers
  - Instrument actual market access with planned or quasi-random lines when possible
  china_use_cases:
  - Evaluate the effect of China's National Trunk Highway System on regional industrialization
    and land values
  - Study how high-speed rail expansion changes market access and firm location in Chinese
    cities
  - Assess the impact of historical treaty-port railway networks on long-run development
  - Measure market-access gains from the Belt and Road Initiative's transport corridors
  - Analyze how county-level road network upgrades affect agricultural market integration
  china_data_requirements:
  - GIS network data for Chinese railways, highways, and waterways (historical and contemporary)
  - County- or city-level economic outcomes (GDP, land values, industrial output, employment,
    population)
  - Bilateral distance or travel-time matrices
  - Trade elasticity calibrated to Chinese trade data or borrowed from literature
  - Regional size/productivity proxies (GDP, population, industrial value added)
  - Geographic controls (elevation, ruggedness, distance to coast, river systems)
  transfer_limits:
  - Requires detailed and reliable network data, which may be unavailable for historical
    Chinese periods.
  - The single-sector gravity model abstracts from migration, industrial policy, and other
    non-trade channels.
  - Estimated effects are local-equilibrium responses and may not capture general-equilibrium
    welfare without further assumptions.
  - Results are sensitive to the assumed trade elasticity and transport-cost function.
  - Network expansion is rarely fully exogenous; careful instrumenting or controls are needed.
readiness_blockers:
- The full NBER working paper PDF was not accessed; cross-check the market-access formula,
  parameter values, and robustness details against the published QJE article.
- Replication code or network GIS files from the original paper were not obtained; researchers
  should reconstruct the network and market-access measure from primary sources.
---
---
## Institutional Background

In the nineteenth-century United States, railroads dramatically lowered the cost of shipping agricultural goods to domestic and international markets. Donaldson and Hornbeck (2016) use this episode to develop a theoretically grounded measure of how transport infrastructure affects local economies. They start from an Eaton-Kortum gravity trade model in which each county produces differentiated varieties and trades with all other counties. In equilibrium, the rental rate on land in a county depends on a single summary statistic: the county's "market access," which aggregates the size of all trading partners discounted by trade costs [E2; E3].

## What Changed

The method does not focus on a single policy shock. Instead, it converts the expansion of the entire railroad network into a continuous, county-level shock to market access. Between 1870 and 1890, many counties were connected to the rail network for the first time, while others gained shorter routes to existing markets. These changes increased some counties' market access much more than others, creating variation that can be related to changes in land values, output, and population [E1; E2].

## Implementation and Assignment

Researchers first build a network database of railroad lines and waterways, assign transport costs per mile, and compute the lowest-cost route between every pair of counties. Market access for county i is then calculated as a sum over all source counties j of source productivity (or size) divided by the bilateral trade cost raised to a trade elasticity. The change in this measure between two years is the treatment-like shock. The outcome of interest — for example, agricultural land value per acre — is regressed on market access, controlling for county fixed effects and geographic characteristics [E2; E3].

## Why This Creates Empirical Variation

Because the network expansion was geographically uneven, the implied market-access gains varied widely across counties. A county located between two newly connected hubs could experience a large gain even if no rail line crossed its own borders, because it became a cheaper source or destination for trade. The market-access measure therefore captures both direct and indirect network effects in a single reduced-form term derived from trade theory [E2].

## Identification Risks

The main risks are (i) endogenous placement of railroad lines, which may have targeted counties with better growth prospects; (ii) measurement error in historical network maps; (iii) misspecification of the gravity model or trade-elasticity parameter; (iv) spatial spillovers that violate independence of treatment and comparison counties; and (v) limited external validity to modern or non-agricultural settings [E2].

## Data Requirements

The method requires a transport network in GIS format (links, nodes, and link costs), a set of regions with economic outcomes, and proxies for the size or productivity of each region. For China, this means railway, highway, and waterway network data; county- or city-level economic statistics; and a calibrated trade elasticity. Historical Chinese network data may require digitization of maps or compilation from railway yearbooks and gazetteers [E2].

## Evidence Notes

The method is described in Donaldson and Hornbeck (2016, *Quarterly Journal of Economics*, E1) and in the underlying NBER Working Paper 19213 (E2). A model summary is available in Spencer Lyon (2018, E3). The original paper applies the method to U.S. agriculture; the record documents how to transfer it to Chinese transport-network settings [E1; E2; E3].
