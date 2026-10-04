---
schema_version: 2
id: china-high-speed-rail-recentered-market-access
name: China's High-Speed-Rail Market-Access Growth with Recentered Exposure
aliases:
- Chinese HSR market-access growth
- Recentered HSR market access
- 中国高铁市场可达性再中心化暴露
status: grounded
provenance:
  task_id: task-22b826eb90ff
scope:
  country: China
  regions:
  - Mainland China prefecture-level divisions
  domains:
  - transportation
  - infrastructure
  - urban
  - regional-economics
  - economic-geography
  - employment
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    The empirical application uses the opening of China's high-speed-rail network
    to generate prefecture-level changes in market access between 2007 and 2016.
    The useful object is a continuous network exposure and its recentered version,
    not a uniform national treatment date or a claim that every line opening was
    random.
identity:
  instrument: >
    China's rapidly expanding dedicated passenger high-speed-rail network, used
    to construct prefecture-level market-access growth and a recentered exposure
    that removes expected exposure under counterfactual line assignments.
  authority: >
    Central railway and transport planning authorities; the empirical network is
    assembled from China Railway Yearbooks, planned-line information, geographic
    data, and the paper's replication materials. The paper does not rely on one
    legal pilot identifier.
  legal_identifiers:
  - China Railway Yearbooks (2001–2013), used for network and opening information
  - High-speed-rail lines completed by 2016 and planned or under construction as of April 2019
  implementation_regime: >
    Dedicated passenger HSR lines were built in a rapidly expanding national
    network. Lines opened at different dates after the network began expanding
    around 2007; a prefecture's exposure depends on how those openings changed
    travel time to other population centers. The application uses 83 lines open
    by 2016 and distinguishes them from 66 additional lines completed or under
    construction by April 2019.
  assignment_mechanism: >
    Realized line openings and the network's geometry determine each prefecture's
    market-access growth. Because planned construction was not randomly allocated,
    the paper constructs 1,999 counterfactual networks by permuting the opening
    status of built and unbuilt lines while preserving the number of
    cross-prefecture links. Expected market-access growth from these counterfactuals
    is subtracted from realized growth; this is a recentering rule, not a claim of
    legal eligibility or literal random assignment. [E3, verified code] Opening
    years are shuffled within groups defined by each line's link count; the
    2003 pilot line is assigned a separate, fixed group. The code preserves the
    within-group opening-year distribution, not merely one aggregate link total.
  parent: null
  related_variations:
  - china-highway-network-expansion
  - china-expressway-market-access-walled-city-mst
timeline:
  announcement: null
  effective: null
  implementation_start: 2007
  implementation_end: 2016
  local_timing: >
    Exposure is measured between 2007 and 2016, not from a universal opening date.
    [E3, verified package coding] The baseline includes a 2003 pilot: the supplied
    Lines table codes 秦沈客运专线 opening as 2003-10-12, and the permutation script
    fixes its opening year. This is inspected author coding, not independently
    verified official opening evidence. The baseline is not a no-railway network.
  anticipation: >
    Planned and under-construction lines can affect expectations before opening.
    The paper treats this predictable component as expected market-access growth
    and adjusts for it; a new application must not assume that the residual is
    free of all anticipation or route-selection concerns.
  last_verified: '2026-10-04'
assignment:
  unit: Prefecture-level administrative division-year; the paper uses 340 mainland divisions and 275 with employment outcomes
  treated: >
    A prefecture is more exposed when completed HSR lines reduce its predicted
    travel time to population centers and raise its market-access measure between
    2007 and 2016. Treatment is continuous rather than binary.
  comparison_pool: >
    Other mainland prefectures with smaller, larger, or differently composed
    realized market-access changes. The core comparison is across residualized
    changes after expected market-access growth is removed, not simply connected
    versus unconnected places.
  rule: >
    For prefecture i and year t, compute MA_it as the sum over destination
    prefectures j of exp(-0.02 times predicted travel time tau_ijt) multiplied by
    destination population in the 2000 census. Define realized growth as log
    MA_i,2016 minus log MA_i,2007. Compute expected growth from 1,999 permutations
    of the built and unbuilt line-opening status with the same number of
    cross-prefecture links, and use realized minus expected growth as the
    recentered exposure or instrument. [E3, verified code] The sum includes the
    origin prefecture; a leave-own-city-out alternative is commented out. Each
    scenario is logged before averaging, so expected log access is the mean of
    scenario log access, not the log of mean access levels.
  intensity: Continuous realized, expected, and recentered market-access growth
  exemptions:
  - Hainan and Taiwan are excluded from the mainland sample
  - Hong Kong and Macau are excluded from the mainland sample
  - Six sub-prefecture-level cities without a parent prefecture are retained as separate divisions
  compliance: >
    Observed network openings, rather than a legal enrollment decision, determine
    exposure. The recentered instrument depends on the first-stage relationship
    between the counterfactual construction process and realized market-access
    growth; route deviations and opening-date measurement remain relevant.
  exposure_construction: >
    Join line endpoints and opening status to a stable prefecture geography,
    compute predicted travel times and population-weighted market access for each
    year, form 2007–2016 growth, and separately retain expected and recentered
    measures. Do not replace the observed market-access variable with the
    recentered instrument. [E3, verified code] `ma2007` and `ma0` are log access;
    `dma0=ma0-ma2007`, `dma_nlink_pscore=ma_nlink_pscore-ma2007`, and
    `ma_nlink_rc=ma0-ma_nlink_pscore`. `cityid` comes from the GIS OBJECTID,
    not the official prefecture code; use its retained `adm2_pcode` and names
    to build an explicit external-data crosswalk.
  required_identifiers:
  - stable prefecture or sub-prefecture code
  - calendar year or endpoint year
  - prefecture coordinates, main-city coordinates, or centroid geometry
  - HSR line endpoints and opening status
  - destination population identifier for the 2000 census
  spillovers: >
    Market access is a network-wide object. Improved connections can move firms,
    workers, and activity between prefectures, so a local employment effect can
    combine direct access gains with spatial reallocation and effects on nearby
    places.
research_compatibility:
  outcome_domains:
  - urban employment
  - firm location and entry
  - labor reallocation
  - productivity and industrial composition
  - regional integration
  - market access and spatial equilibrium
  affected_populations:
  - Urban workers in Chinese prefectures
  - Firms and establishments linked to prefecture locations
  - Residents and firms in connected and indirectly exposed areas
  mechanism_channels:
  - lower passenger travel costs
  - improved interregional business connectivity
  - labor-market integration
  - firm relocation and spatial reallocation
  - agglomeration and market expansion
  best_for:
  - Estimating how continuous transport-network access changes regional employment
  - Studying spatial reallocation when all important prefectures remain in the sample
  - Applications that can reconstruct both realized and expected network exposure
  not_good_for:
  - A simple before-after estimate with one national HSR treatment date
  - A binary treated-versus-never-treated design that discards network spillovers
  - Claims that the recentered residual is automatically exogenous without checking the counterfactual construction
design:
  claim_type: causal
  affordances:
  - Continuous prefecture-level market-access exposure
  - Recentered IV that adjusts for expected exposure under counterfactual line openings
  - Network-wide treatment that preserves prominent and peripheral locations
  - Direct comparison of unadjusted, recentered, and geography-controlled estimates
  candidate_designs:
  - Recentered instrumental variables
  - Cross-prefecture market-access growth regression
  - Spatial equilibrium and reallocation analysis
  - Mechanism and heterogeneity analysis by initial access or industry
  identifying_variation: >
    The empirical variation is the residual change in prefecture market access
    generated by realized HSR openings after subtracting expected change from
    counterfactual networks that preserve the number of cross-prefecture links.
  primary_strategy: >
    Regress prefecture urban-employment growth on realized market-access growth,
    instrumenting it with recentered market-access growth or controlling directly
    for expected growth. The identifying comparison is conditional on the stated
    counterfactual assignment process.
  estimand: >
    The effect of HSR-induced market-access growth on urban employment growth in
    Chinese prefectures over 2007–2016 for exposure changes whose expected component
    is captured by the paper's counterfactual networks.
  treatment_variable: >
    Realized market-access growth, log(MA_i,2016) minus log(MA_i,2007), with its
    expected component and the recentered difference stored separately.
  comparison_logic: >
    Compare prefectures with different residualized market-access changes while
    accounting for expected exposure. This is not a comparison of places that
    never receive HSR to places that do; every prefecture may be affected by the
    network and by other prefectures' access changes.
  estimation_notes: >
    The published application reports unadjusted OLS, recentered IV, and expected-
    exposure-controlled OLS. The adjusted estimates are smaller than unadjusted
    estimates, and the record should preserve that distinction rather than
    treating the raw market-access coefficient as the causal estimate.
    [E3, verified code] Table1 uses `emp_growth=dlog_avgnworkers_ppl_wc`, the
    2007–2016 log change in whole-prefecture average employed staff and workers,
    not all resident employment or the urban-core-only series. Outcome filtering
    sets growth missing for sustained jumps above log(2), after inspecting
    adjacent available observations. Recentered IV and OLS controlling expected
    growth are distinct specifications; source code was inspected, not executed.
  assumptions:
  - Counterfactual permutations represent the predictable component of HSR exposure that is related to local growth potential
  - After recentering, the residual market-access shock is orthogonal to relevant unobserved employment-growth determinants, conditional on the design
  - The travel-time and population-weighted market-access measure captures the transport channel relevant to the outcome
  - Stable prefecture joins and line-opening dates make exposure reproducible
  diagnostics:
  - Compare unadjusted, recentered-IV, and expected-exposure-controlled estimates
  - Test first-stage strength for recentered market-access growth
  - Plot realized, expected, and recentered exposure against geography and baseline employment
  - Check sensitivity to travel-time decay, population weights, planned-line definition, and prefecture geography
  - Use spatially clustered or permutation-based inference and inspect reallocation across neighboring prefectures
threats:
- type: Nonrandom route selection and predictable exposure
  basis: documented
  condition: HSR planning targets and line openings correlate with local growth potential, so raw market-access growth is endogenous.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Recenter using the stated counterfactual networks
  - Compare expected-exposure controls with the recentered IV
  - Test baseline geography and employment balance against expected exposure
- type: Counterfactual-network misspecification
  basis: inferred
  condition: Permuting built and unbuilt lines with the same number of cross-prefecture links may not reproduce all features of the planning process.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Vary the permutation restrictions and planned-line universe
  - Report first-stage and placebo results for alternative counterfactuals
  - Compare with historical-route or geography-based instruments where available
- type: Spatial spillovers and general-equilibrium reallocation
  basis: reported
  condition: HSR may move employment and firms across prefectures, so a local gain can coexist with losses elsewhere and nearby places are not clean controls.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Estimate effects by initial access and distance to treated corridors
  - Test neighboring and network-connected prefecture outcomes
  - Distinguish local employment from network-wide employment totals
- type: Exposure measurement and geography error
  basis: reported
  condition: Travel times, centroids, opening dates, population weights, or the 0.02 decay parameter are measured or modeled incorrectly.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Recompute market access with alternative speeds, geocoding, weights, and decay parameters
  - Audit line-level opening records and prefecture crosswalks
- type: Replication-to-outcome and identifier mismatch
  basis: documented
  condition: '[E3, verified code] GIS OBJECTID-derived cityid is not an official administrative code. The outcome is the whole-prefecture staff-and-workers series, and sustained discontinuities are removed rather than winsorized. Substituting a city-code join, an urban-core series or unrestricted endpoint growth changes the published comparison.'
  evidence_refs: [E3]
  possible_diagnostics: [Bridge cityid to adm2_pcode and historical boundaries, Preserve the outcome definition and filtering rule, Report sample loss separately from exposure coverage]
empirical_requirements:
  contract_version: 1
  population: Urban workers and firms located in mainland Chinese prefecture-level divisions
  observation_unit: Prefecture-year panel or prefecture-level 2007–2016 growth observation
  geography_level: Prefecture or sub-prefecture-level administrative division
  time_start: 2007
  time_end: 2016
  minimum_frequency: annual
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - stable prefecture identifier and harmonized boundary version
  - annual urban employment or firm outcome
  - HSR line endpoints, opening year, and completed/planned status
  - predicted travel time between prefectures by year
  - 2000 destination population
  - coordinates or GIS geometry for each prefecture
  - realized, expected, and recentered market-access measures
  required_identifiers:
  - prefecture_id
  - year
  - hsr_line_id
  - destination_prefecture_id
  treatment_key:
  - prefecture_id
  - year
  - ma_growth_2007_2016
  - expected_ma_growth
  - recentered_ma_growth
  treatment_source: >
    Inspected Zenodo package raw/stations.xlsx (Lines and LineStations),
    raw/Population.xlsx and raw/gis/CityCentroids.xls, connected through the
    build_data scripts and server/process_scenarios_2016.do. The supplied
    gis/ma2016.csv exposes prepared access fields but is a map-data file, not
    the final filtered employment sample. Official line dates remain unaudited.
  measurement_risks:
  - Planned versus completed lines may be classified inconsistently
  - Travel-time predictions depend on speed, mode, and geography assumptions
  - Prefecture boundaries and sub-prefecture units may change over time
  - Destination population is fixed at the 2000 census and may not reflect later market size
  - HSR is primarily passenger rail, so the transport channel may differ from freight-market access
design_profiles:
- id: recentered-prefecture-employment
  label: Recentered HSR exposure for prefecture employment
  design_families:
  - recentered-IV
  - market-access-growth
  when_to_use: Use when the outcome is measured for stable prefectures and the analyst can reconstruct realized and counterfactual HSR network exposure.
  outcome_domains:
  - urban employment
  - firm entry
  requirements:
    population: Urban workers or firms in mainland Chinese prefectures
    observation_unit: Prefecture-level growth or prefecture-year panel
    geography_level: Prefecture or sub-prefecture division
    time_start: 2007
    time_end: 2016
    minimum_frequency: annual
    minimum_pre_periods: 1
    minimum_post_periods: 1
    required_fields:
    - urban employment or firm outcome
    - HSR line opening and travel-time data
    - expected and recentered market access
    required_identifiers:
    - prefecture_id
    - year
    - hsr_line_id
    treatment_key:
    - prefecture_id
    - recentered_ma_growth
evidence:
- id: E1
  source_type: paper
  citation: 'Borusyak, Kirill, and Peter Hull. 2023. "Nonrandom Exposure to Exogenous Shocks." Econometrica 91(6): 2155–2185. DOI: 10.3982/ECTA19367.'
  url: https://doi.org/10.3982/ECTA19367
  date: 2023
  supports:
  - identity.instrument
  - identity.implementation_regime
  - timeline.implementation_start
  - timeline.implementation_end
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design_applications.treatment_encoding
  verification_status: verified
  access_level: full-text
  locator: 'Section 4.1, Application: Effects of Transportation Infrastructure; Figure 1; Figure 2; Table I; NBER full-text version of the published paper'
- id: E2
  source_type: appendix
  citation: 'Borusyak, Kirill, and Peter Hull. Online Appendix to "Non-Random Exposure to Exogenous Shocks: Theory and Applications."'
  url: https://back.nber.org/appendix/w27845/shock_exposure_v91_apdx.pdf
  date: 2021
  supports:
  - assignment.exposure_construction
  - assignment.required_identifiers
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_key
  - empirical_requirements.treatment_source
  - threats.type
  verification_status: verified
  access_level: appendix
  locator: 'Appendix A.1, Data for Section 4.1; HSR network construction, prefecture geography, travel-time measure, planned-line universe, and counterfactual permutations'
- id: E3
  source_type: replication
  citation: 'Borusyak, Kirill, and Peter Hull. 2023. Replication package for "Non-Random Exposure to Exogenous Shocks." Zenodo. DOI: 10.5281/zenodo.8286785.'
  url: https://doi.org/10.5281/zenodo.8286785
  date: 2023
  supports:
  - empirical_requirements.treatment_source
  - design_applications.data_used
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.rule
  - assignment.exposure_construction
  - design.estimation_notes
  - design_applications.outcome
  - design_applications.treatment_encoding
  - threats.condition
  verification_status: verified
  access_level: replication
  locator: 'BH replication.zip inspected in memory 2026-10-04, no source programs executed or raw data copied into this repository. README_ECMA.pdf pp1-9; code/master_hsr.do Parts2-6; build_data/1_clean_population.do; 2_clean_cities.do geography and OBJECTID-to-cityid construction; 3_clean_lines.do Lines/LineStations and year_opening; 4_ma2007.do; 5_reshuffle_lines.do seed/group/pilot exception; 12_outcomes.do; 13_outlier_treatment.do; 14_combine_ma_2016.do; 15_merge_data.do; server/process_scenarios_2016.do; code/Table1.do. Supplied Lines, LineStations, CityCentroids and gis/ma2016.csv column headers also inspected; Lines pilot row inspected. This verifies code and available inputs, not executed results or original opening documents.'
- id: E4
  source_type: policy-document
  citation: 'National Railway Administration. 2014. 中国高速铁路发展规划, describing the State Council-approved 2004 中长期铁路网规划 and its 2008 adjustment.'
  url: https://www.nra.gov.cn/ztzl/hy/gsgt/zgtl/fzgh/201602/t20160216_146043.shtml
  date: 2014
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.implementation_start
  - assignment.rule
  - assignment.exposure_construction
  verification_status: verified
  access_level: official-document
  locator: '中国高速铁路发展规划, paragraphs describing the 2004 approval, 2008 adjustment, and the 四纵四横 passenger-rail network'
design_applications:
- paper: 'Nonrandom Exposure to Exogenous Shocks'
  doi: '10.3982/ECTA19367'
  journal: Econometrica
  year: 2023
  research_question: What is the effect of HSR-induced market-access growth on employment in Chinese prefectures after correcting for predictable exposure to planned network expansion?
  population: Urban employment in 275 mainland Chinese prefectures with non-missing outcome data, drawn from a larger set of 340 divisions
  outcome: Whole-prefecture average employed staff-and-workers log growth, 2007-2016, excluding sustained discontinuities under the package rule; not total resident employment
  data_used:
  - China Railway Yearbooks and HSR line information
  - Planned or under-construction lines as of April 2019
  - 2000 census prefecture population
  - United Nations shapefiles and prefecture coordinates
  - China City Statistical Yearbooks
  - Paper replication materials
  treatment_encoding: >
    Realized growth in population-weighted market access from 2007 to 2016,
    instrumented or controlled using expected growth from 1,999 counterfactual
    permutations of built and unbuilt HSR lines with the same number of
    cross-prefecture links. [E3, verified code] Permutations are within line-link-
    count groups with the 2003 pilot fixed; log access is averaged across
    counterfactuals. Preserve actual, expected and recentered fields separately.
  comparison: Prefectures with different residualized market-access growth after expected exposure is removed; not a simple connected/unconnected comparison.
  empirical_design: Cross-prefecture growth regressions reported as unadjusted OLS, recentered IV, and expected-exposure-controlled OLS, with spatially clustered and permutation-based inference.
  assumptions:
  - Counterfactual line permutations capture the predictable component of exposure
  - The recentered component is conditionally orthogonal to unobserved employment growth
  - Market-access construction and prefecture joins are measured consistently
  threats_addressed:
  - Nonrandom exposure to planned network expansion
  - Geographic and spatial correlation
  - Alternative expected-exposure controls and permutation inference
  evidence_refs:
  - E1
  - E2
  - E4
  - E3
method_transfer: null
readiness_blockers:
- The paper and appendix document the network and counterfactual construction, but official line-by-line opening records have not been independently inspected in this repository.
- Package inputs and core construction/regression scripts are now inspected, but the pipeline has not been executed. The archive contains raw inputs and scripts, not precomputed server scenarios or final analysis_data.dta; rebuilding those is a substantial computation, not a missing-file error.
- Before using new outcomes, bridge the GIS OBJECTID-derived cityid to official historical geography and preserve the staff-and-workers outcome boundary and sample filters. Package code does not independently certify a user's new join.
- The counterfactual permutation rule is a design assumption; it does not establish that HSR planning was random or that residual exposure is valid for every outcome.
- The 2007–2016 application is a network-level market-access design, so local estimates require explicit treatment of spatial reallocation and passenger-versus-freight mechanisms.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

China's high-speed-rail network expanded rapidly from the late 2000s. The Econometrica application treats this expansion as a changing transportation network, not as one national policy adoption. It combines line openings, predicted travel times, and the 2000 population of destination prefectures to measure how much each location's access to other markets changed. The paper studies 340 mainland sub-province-level divisions and retains 275 with non-missing urban-employment outcomes [E1].

The relevant institution is therefore the network and its construction process. The paper does not identify a single legal pilot notice that assigned every prefecture to treatment. The appendix traces the network to China Railway Yearbooks, geographic data, and planned-line information. The inspected replication package supplies raw inputs and the construction route; this is not independent confirmation of every underlying line date [E2; E3].

## What Changed

Between 2007 and 2016, completed HSR lines shortened predicted travel times between many prefectures. In the application, 83 lines had opened by 2016; 66 additional lines were completed or under construction by April 2019 and serve as part of the planned-line universe for counterfactuals [E1; E2]. The economic object is the resulting change in market access, not the announcement of a uniform national program.

For prefecture (i), market access in year (t) is constructed from destination population and predicted travel time. The observed treatment-like variable is the log change in this measure from 2007 to 2016. Because locations expected to receive infrastructure may already be on different growth paths, the paper also creates counterfactual HSR networks by permuting the opening status of built and unbuilt lines while holding the number of cross-prefecture links fixed. Expected market-access growth from those permutations is separated from the realized change [E1; E2].

## Implementation and Assignment

Exposure begins when the realized network changes a prefecture's travel-time access, and it can also arise indirectly through links between other prefectures. The application uses the destination population recorded in the 2000 census and geocodes prefectures by their main city or, in some cases, their centroid. The source materials distinguish six sub-prefecture-level cities that do not belong to a parent prefecture from the main mainland sample [E2].

The comparison is continuous. A prefecture with a large realized increase is compared with places whose access changed less, after the expected component is modeled. The recentered exposure is not a legal eligibility variable, and a researcher should keep four quantities separate: observed market access, expected market access, the recentered difference, and any binary indicator for a line opening. Collapsing them into a single “treated city” flag changes the design.

## Why This Creates Empirical Variation

The paper's contribution is to address nonrandom exposure to network shocks. Ordinary market-access growth is related to where planners expect growth, so an unadjusted regression can attribute pre-existing growth potential to HSR. The recentered IV uses the part of realized market-access growth left after expected growth under the specified line permutations is removed. The published application compares raw OLS, recentered IV, and expected-exposure-controlled estimates; the adjusted coefficients are materially smaller than the raw estimate [E1].

This variation can support a regional employment or firm-location study when the researcher can reconstruct the network and preserve the spatial equilibrium. It does not justify treating unaffected neighbors as pure controls: HSR can move workers and firms between places, and passenger connectivity may affect business access differently from freight costs [E1; analytical inference].

## Identification Risks

The design depends on the counterfactual network being a useful representation of predictable exposure. The same number of cross-prefecture links does not guarantee that the permutations reproduce all central planning constraints, corridor priorities, or local lobbying. The recentered residual is therefore conditional on a modeling choice, not automatically exogenous [E2; analytical inference].

Network spillovers create a second problem. A prefecture can gain employment because it becomes more accessible, lose employment because activity moves to another connected place, or experience both through different sectors. A local coefficient should not be described as a national employment effect without an explicit accounting of reallocation. Finally, travel-time predictions, centroid choices, line-opening dates, the planned-line universe, and the 0.02 distance-decay parameter can all change the exposure measure [E1; E2].

## Data Requirements

The minimum data contract is an annual or endpoint prefecture panel with stable geography, urban employment or firm outcomes, HSR line endpoints and opening years, travel-time predictions, coordinates, and 2000 destination populations. To reproduce the published design, the analyst also needs the planned-but-unbuilt line universe and code that generates the 1,999 constrained permutations. If the outcome is firm-level, firms must be linked to prefectures and the estimand must state whether it concerns local employment, firm location, or network-wide reallocation.

[E3, verified code] The following fields recover the published construction;
the archive paths are relative to `BH replication/`, not this repository.

| Package field | Meaning and construction |
|---|---|
| `cityid`; `adm2_pcode` | GIS OBJECTID-derived join ID; separately retained geographic code. Build an external crosswalk rather than equating them. |
| `ma2007`; `ma0` | Baseline and actual 2016 log access, produced by `4_ma2007.do` and scenario0. |
| `ma_nlink_pscore` | Mean of 1,999 counterfactual 2016 log-access values in `14_combine_ma_2016.do`. |
| `dma0`; `dma_nlink_pscore` | Actual and expected 2007–2016 log-access changes. |
| `ma_nlink_rc`; `ma_nlink_rc_1`–`_1999` | Actual and simulated log access minus the same expected log-access term. |
| `emp_growth` | `dlog_avgnworkers_ppl_wc`, constructed by `13_outlier_treatment.do` and assigned in `15_merge_data.do`. |

The network scripts model non-rail travel as `60*1.2*distance/120` minutes
and rail travel as `60*1.3*line_distance/speed`, iteratively allow indirect
routes, impose zero transfer time, and retain origin population in access.
These are modeling choices, not observed passenger timetables. The line
cleaning excludes upgrades and wholly local lines; unopened lines receive
2019 as a coding placeholder, not a verified eventual opening year [E3].

The package's `gis/ma2016.csv` supplies map exposure fields. It does not
contain the final filtered employment dataset. `master_hsr.do` pauses after
network preparation; 2,000 scenario calculations, including actual scenario0,
precede assembly and regressions. README pp5–8 reports about three hours on
the authors' parallel cluster and about70 hours if serial on a local machine;
these are author estimates, not timings tested here. Stata17, Python and
listed dependencies are needed for the pipeline; ArcMap is for reproducing
maps. Do not mistake code inspection for successful numerical replication.

## Evidence Notes

The published paper establishes that the Chinese HSR application is an empirical use of the recentered-exposure method and reports the sample, dates, market-access construction, and estimates [E1]. The appendix supplies the data-assembly details [E2]. The Zenodo archive inspection closes the former package-access and core code-to-field gaps, including the baseline pilot, logged variables, grouping rule and outcome filter [E3]. It does not establish successful execution or independently verified official line dates.

README pp1–4 reports public availability and legitimate author access. Its
separate redistribution-permission checkbox is unmarked. Inspection here
does not establish a blanket redistribution licence for every bundled source;
retain the DOI route rather than copying the archive's raw files into this
knowledge repository [E3, inspected documentation].

The official planning page grounds the network's institutional identity and the four-vertical/four-horizontal planning framework [E4]. It does not establish a line-by-line prefecture opening crosswalk, random assignment, or the absence of anticipation. Those claims remain outside the record's boundary. A researcher who needs a reproducible exposure file should audit the cited China Railway Yearbooks and the replication archive before treating the data contract as fully verified.
