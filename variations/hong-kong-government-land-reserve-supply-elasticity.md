---
schema_version: 2
id: hong-kong-government-land-reserve-supply-elasticity
name: Hong Kong Government Land Reserves as a Neighborhood Housing-Supply-Elasticity Exposure
aliases:
- Ren Wong Chau 2025 JoEG Hong Kong GovLR supply elasticity
- Hong Kong public leasehold land-ownership supply elasticity
- 香港政府土地储备与社区住房供给弹性
status: grounded
provenance:
  task_id: task-567eb7958e61
scope:
  country: China
  regions:
  - Hong Kong SAR (56 EPRC neighborhoods), 2003-2018
  domains:
  - urban
  - regional-economics
  - economic-geography
  - housing
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    The exposure is created by a China-specific institution: Hong Kong's public
    leasehold system, under which the government owns all land until it is
    leased, so unleased and unallocated government land reserves are the city's
    marginal source of residential development land. Ren, Wong, and Chau (2025,
    Journal of Economic Geography) measure each neighborhood's initial
    government land reserve share (GovLR) and estimate neighborhood housing
    supply elasticity over 2003-2018, identifying the price equation with a
    Bartik-style demand instrument built on Mainland Chinese tourist arrivals
    under the Individual Visit Scheme (IVS), a central-government
    liberalization launched in four Guangdong cities on 2003-07-28 and expanded
    to 49 Mainland cities by 2007.
identity:
  instrument: >
    The inherited spatial distribution of unleased and unallocated
    government-owned land reserved for future residential development, measured
    as each neighborhood's year-2000 government land reserve share (GovLR) of
    total land area. The measurement consolidates a one-off mid-2012
    Development Bureau survey map of unleased and unallocated government land
    zoned Residential or Commercial/Residential, Planning Department records of
    reserves intended for residential rezoning, and an add-back of government
    residential land sales between 2003 and 2012 (Lands Department and MTR
    Corporation), which fixes the baseline at 2000 because MTRC annual reports
    are only available from 2000. In the paper's design, the demand side is
    identified with a Bartik-style instrument: annual Mainland Chinese tourist
    arrivals (the shift, driven by the IVS liberalization) multiplied by each
    neighborhood's 2001 census share of workers in tourism-related industries
    (the share).
  authority: >
    Hong Kong SAR Government. The Development Bureau published the one-off
    land-reserve survey on 2012-10-17 (statistics as at end-June 2012); the
    Lands Department and the MTR Corporation conduct government land sales; the
    Planning Department maintains the Outline Zoning Plans and the Land
    Utilization Map. The Individual Visit Scheme is a central-government
    measure under the Closer Economic Partnership Arrangement (CEPA, signed
    2003-06-29); IVS endorsements are issued by Mainland authorities, not by
    the Hong Kong government.
  legal_identifiers:
  - Development Bureau location maps of unleased and unallocated government land zoned "Residential" or "Commercial/Residential" (after deducting land not suitable for development, not yet available, or with low development potential), released 2012-10-17, statistics as at end-June 2012
  - Individual Visit Scheme (自由行) liberalization measure under the Mainland and Hong Kong Closer Economic Partnership Arrangement (CEPA), launched 2003-07-28 in Dongguan, Zhongshan, Jiangmen, and Foshan
  - Hong Kong Legislative Council question LCQ17 reply by the Secretary for Development, 2013-02-06, confirming the survey's construction and caveats
  implementation_regime: >
    Public leasehold: the government leases parcels to private developers by
    auction or tender, and buyers acquire leasehold rights. Government-owned
    land means land not yet leased; developing it avoids the two cost barriers
    of private land, namely assembling fragmented private titles and negotiating
    land-lease modification premia, because the government is simultaneously
    the land supplier and the lease regulator. There is no quota on how much
    land can be developed at a given time; building permits are approved on
    compliance with building ordinances. The paper reports no observed
    expansion of the residential reserves (for example through reclamation)
    between 2000 and 2012; expansion plans were announced only in the 2012
    policy address.
  assignment_mechanism: >
    No rule assigns neighborhoods to treatment. Exposure is a continuous,
    time-invariant spatial inheritance: neighborhoods with a larger year-2000
    share of unleased government land reserved for residential development hold
    more land that can be converted into new housing at lower assembly and
    lease-modification cost, and are therefore expected to respond more
    elastically to demand shocks. The identifying time variation comes from the
    demand instrument (IVS-driven tourist arrivals scaled by 2001 tourism
    employment shares), not from any rollout of the exposure itself.
  parent: null
  related_variations:
  - china-beijing-soe-relocation-land-supply-iv
timeline:
  announcement: '2003-07-28'
  effective: '2003-07-28'
  implementation_start: 2003
  implementation_end: 2007
  local_timing: >
    The exposure itself is a fixed year-2000 baseline; the dated events concern
    the demand driver and the measurement. The IVS began on 2003-07-28 in four
    Guangdong cities and expanded in stages until 49 Mainland cities were
    covered in 2007; it is a permanent liberalization, not a short-term
    program. The outcome window is July 2003 to July 2018. The reserve
    measurement combines the mid-2012 Development Bureau survey (released
    2012-10-17, statistics as at end-June 2012) with an add-back of 2003-2012
    government land sales, yielding the year-2000 GovLR baseline.
  anticipation: >
    The IVS was announced as an economic-support package after SARS and its
    staged expansion was public, so households and developers could anticipate
    rising tourist inflows; however, the exposure measure (year-2000 GovLR)
    predates the outcome window by at least three years, and the authors report
    low and insignificant correlations between GovLR and neighborhood household
    income, population density, and CBD distance, arguing the government had
    little incentive to accumulate reserves in anticipation of later price
    appreciation.
  last_verified: '2026-08-15'
assignment:
  unit: >
    Neighborhood-year within Hong Kong: 56 neighborhoods defined by the
    private data vendor EPRC (60 classified neighborhoods minus four with
    insufficient transactions, merged with adjacent ones), observed annually
    from July 2003 to July 2018, giving 840 neighborhood-year observations.
  treated: >
    Neighborhoods with a larger year-2000 GovLR share; there is no untreated
    group, and treatment intensity is the continuous reserve share. In the
    demand-identification layer, neighborhoods with higher 2001 tourism-related
    employment shares receive larger Bartik demand shocks from the same
    citywide tourist inflow.
  comparison_pool: >
    Other Hong Kong neighborhoods in the same year; year fixed effects absorb
    citywide shocks (SARS, the 2008 financial crisis, citywide policy changes),
    so identification comes from cross-neighborhood differences in exposure
    interacted with instrumented price changes.
  rule: >
    Compute GovLR per neighborhood by digitizing the mid-2012 Development
    Bureau reserve map (geo-referencing and support-vector-machine
    classification in ArcGIS Pro), adding Planning Department parcels intended
    for residential rezoning, adding back government residential land sales
    2003-2012 (Lands Department and MTRC), and dividing by neighborhood land
    area. The supply-elasticity equation regresses annual log housing-stock
    changes on 1.5-year-lagged log price changes instrumented by the log
    difference of the Tourist IV, with a construction-cost supply shifter
    (citywide construction cost index changes multiplied by each neighborhood's
    initial structure share from a 2000-2002 hedonic regression, lagged 3.5
    years) and year fixed effects; neighborhood elasticity equals alpha1 +
    alpha2 * GovLR + alpha3 * CBD distance from the interacted Equation (5).
  intensity: >
    Continuous on both layers: GovLR share in percent of neighborhood land
    area (one standard deviation is 1.256 percentage points), and Tourist IV
    intensity from the 2001 tourism employment share times the tourist count.
  exemptions:
  - Land not feasible for residential development (for example military reserves or conservation areas), which the Development Bureau survey excludes
  - Land zoned Village Type Development in the New Territories, which is reserved for indigenous-villager small houses and is outside the residential-reserve measure
  - Four EPRC neighborhoods with too few transactions, which are merged into adjacent neighborhoods rather than dropped
  compliance: >
    The record does not verify parcel-level reserve boundaries against the
    original survey; the Development Bureau itself cautioned that unleased or
    unallocated government land is not equivalent to land immediately available
    for development, since remaining sites include irregular fragments between
    buildings, back lanes, and narrow strips alongside existing developments.
    The paper's neighborhood-level GovLR values are author constructions from
    digitization and are not officially published.
  exposure_construction: >
    Digitize the mid-2012 Development Bureau survey map (PDF image) by
    geo-referencing and support-vector-machine classification so each pixel has
    coordinates; combine with Planning Department rezoning intentions for
    residential use; add back Lands Department and MTRC residential land sales
    between 2003 and 2012 to recover the year-2000 baseline; aggregate to EPRC
    neighborhood boundaries. Initial housing stocks (2003) come from overlaying
    iG1000 building projection and elevation maps (assuming a three-meter
    headroom per floor) with the 2003 Land Utilization Map; annual new supply
    is residential floor area from construction permits; quarterly repeat-sales
    price indices are built from EPRC transactions over 1995-2018 and differenced
    over four quarters.
  required_identifiers:
  - neighborhood identifier over the 56-neighborhood EPRC partition, with the merge list for the four low-transaction neighborhoods
  - parcel-level reserve polygons with coordinates from the digitized 2012 survey and rezoning-intention lists
  - government land sale records (Lands Department and MTRC) 2003-2012 with location and residential floor area or site area
  - building-level projection and elevation data (iG1000) and Land Utilization Map 2003 for initial stocks
  - residential construction permit floor areas by neighborhood and year
  - 2001 census tourism-related employment shares and annual Mainland tourist arrivals
  spillovers: >
    Neighborhoods within one city are substitutable in demand, so supply
    responses in high-GovLR neighborhoods damp price appreciation citywide; the
    authors' companion work explicitly models this substitution. The design
    absorbs citywide shocks with year fixed effects but does not model spatial
    dependence across neighborhoods within the elasticity estimation.
research_compatibility:
  outcome_domains:
  - housing supply elasticity and new residential construction
  - housing prices and within-city price heterogeneity
  - urban land use, land ownership, and public land management
  affected_populations:
  - Hong Kong homebuyers and residents across 56 neighborhoods, 2003-2018
  - Private developers bidding for government land at auction or tender
  - Tourism-related workers and businesses exposed to IVS-driven demand
  mechanism_channels:
  - government land reserves lowering land assembly and lease-modification costs
  - lower development costs raising neighborhood housing supply elasticity
  - IVS-driven tourist inflows shifting local housing demand through tourism income
  best_for:
  - Studies of how public land ownership shapes housing supply responses within a leasehold city
  - Within-city designs that need a predetermined spatial exposure to developable residential land
  - Replications or extensions of neighborhood-level supply elasticity estimation with a demand Bartik instrument in Hong Kong or comparable public-leasehold cities (for example Singapore, Shenzhen, or other Mainland cities)
  not_good_for:
  - Designs that need a discrete rollout, eligibility threshold, or time-varying treatment; GovLR is a fixed year-2000 spatial exposure
  - Claims that the tourist instrument is unconditionally valid; its exclusion restriction rests on the paper's argued channels and remains contestable
  - Long-run supply elasticity questions; the paper estimates short-term relationships only, with permit-based stock proxies
  - Cross-city comparisons without re-deriving the exposure under another city's land institution
design:
  claim_type: causal
  affordances:
  - A predetermined (year-2000) spatial exposure that predates the 2003-2018 outcome window, with reported low correlation to income, density, and CBD distance
  - A Bartik-style demand instrument with a strong reported first stage (first-stage F of 133.6 for the Tourist IV) and an overidentification check against a labor-based Bartik instrument (p = 0.90)
  - A within-city panel with year fixed effects that absorb citywide shocks such as SARS, the financial crisis, and citywide policy changes
  - An officially published one-off government land survey and official IVS documentation that anchor the institutional layer
  candidate_designs:
  - Panel 2SLS of neighborhood log housing-stock changes on instrumented lagged log price changes with a construction-cost supply shifter (baseline supply elasticity)
  - Interacted 2SLS estimating supply elasticity as a linear function of GovLR and CBD distance (determinants model)
  - Neighborhood-level supply elasticity imputation from the determinants model, with delta-method significance tests
  identifying_variation: >
    Cross-neighborhood differences in the year-2000 government land reserve
    share, which shift the cost of converting demand pressure into new housing,
    combined with within-neighborhood-over-time demand variation from
    IVS-driven tourist arrivals scaled by 2001 tourism employment shares,
    conditional on year fixed effects and the construction-cost supply shifter.
  primary_strategy: >
    Two-stage least squares. Equation (4) regresses annual log housing-stock
    changes on log price changes lagged 1.5 years and the lagged
    construction-cost Bartik shifter with year fixed effects; the price term is
    instrumented by the log-differenced Tourist IV (Mainland tourist arrivals
    times 2001 tourism employment shares). Baseline elasticity is 0.00916 with
    a first-stage F of 133.6; alternative labor Bartik instruments (Labor-1 and
    Labor-2, the latter excluding investment-related and construction
    industries) give similar estimates, and the overidentification test with
    Tourist IV plus Labor-2 IV has p = 0.90. Equation (5) adds GovLR and CBD
    distance interactions with the instrumented price term; the GovLR
    interaction coefficient is 0.00449 and the CBD-distance interaction is
    0.00066, with a joint F-test chi-square of 22.15 (p = 0.0001).
  estimand: >
    The short-term price elasticity of housing supply for the average Hong
    Kong neighborhood over 2003-2018, and the change in that elasticity
    associated with a one-percentage-point higher year-2000 government land
    reserve share.
  treatment_variable: >
    Year-2000 GovLR share (percent of neighborhood land area) entered as an
    interaction with the instrumented lagged log price change; the endogenous
    regressor is the 1.5-year-lagged annual log price change, instrumented by
    the log-differenced Bartik Tourist IV.
  comparison_logic: >
    Compare supply responses across neighborhoods with different reserve
    shares in the same year; year fixed effects absorb common demand and policy
    shocks. The comparison fails if GovLR correlates with unobserved
    neighborhood attributes that independently shift construction responses, or
    if tourism exposure shifts supply through channels other than housing
    prices (for example commercial redevelopment).
  estimation_notes: >
    Sample is 840 neighborhood-year observations (56 neighborhoods, July 2003
    to July 2018). Price changes are four-quarter log differences of
    neighborhood repeat-sales indices built from 1995-2018 transactions. The
    construction-cost shifter lag is set to 3.5 years after 1.5 years produced
    unexpected positive signs; interaction coefficients are reported as stable
    across lag choices. Neighborhood elasticities (alpha1 + alpha2 * GovLR +
    alpha3 * CBD distance) range from 0.00041 (Central) to 0.02419 (Ma On
    Shan), average 0.00987, and are tested against zero with the delta method;
    regional averages are 0.00530 (Hong Kong Island, insignificant), 0.01044
    (Kowloon), and 0.01592 (New Territories). A one-standard-deviation higher
    GovLR (1.256 percentage points) is associated with 0.00564 higher
    elasticity, 62 percent above baseline.
  assumptions:
  - Mainland tourist arrivals shift Hong Kong housing demand but not housing supply except through prices (the paper's exclusion restriction)
  - Year-2000 GovLR affects 2003-2018 supply responses only through development-cost differences, conditional on year fixed effects and CBD distance
  - The 2001 tourism employment shares are predetermined relative to the study window and do not proxy other neighborhood demand trends
  - Construction permits with a 1.5-year price lag and a 3.5-year cost lag adequately proxy supply responses
  - The EPRC neighborhood partition approximates housing submarkets
  diagnostics:
  - First-stage F statistics for each instrument (133.6 Tourist IV; 150.3 and 151.3 for Labor-1 and Labor-2)
  - Overidentification test combining Tourist IV and Labor-2 IV (p = 0.90)
  - Joint F-test of the price, GovLR-interaction, and CBD-distance-interaction coefficients (chi-square 22.15, p = 0.0001)
  - Robustness of the interaction coefficients to construction-cost lag choices (1.5, 2.5, 3.5 years) and to the alternative Labor-2 instrument in the supplementary appendix
  - Reported low correlations of GovLR with neighborhood income, density, and CBD distance as an exposure plausibility check
threats:
- type: instrument_exclusion_restriction
  basis: reported
  condition: The Tourist IV could shift housing supply through channels other than prices. The paper argues four channels away - endorsements are issued by Mainland city authorities, an estimated 0.001 percent of tourists buy residential property, only about 0.87 hectares were rezoned to commercial over the period, and residential and commercial construction do not correlate negatively - but these are the authors' arguments, and tourism-driven income and commercial-property demand remain potential violations.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Re-estimate with the Labor-2 instrument, which the paper reports gives similar results
  - Test whether tourist-exposed neighborhoods show differential commercial construction or retail conversion
- type: demand_trend_confounding
  basis: inferred
  condition: Mainland tourist arrivals trend upward with Mainland income growth and post-CEPA integration throughout 2003-2018; the Bartik share (2001 tourism employment) may pick up differential neighborhood trends correlated with housing demand, and year fixed effects absorb only citywide shocks.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Add neighborhood-specific trends or interact the Bartik shares with alternative national shifts
  - Check pre-2003 placebo demand shocks where data permit
- type: exposure_measurement
  basis: reported
  condition: GovLR is reconstructed from a one-off PDF survey map digitized by the authors (geo-referencing plus support-vector-machine classification) and an add-back of 2003-2012 land sales; the Development Bureau itself cautioned that unleased or unallocated government land includes irregular fragments not immediately developable, so the measure may overstate usable reserves unevenly across neighborhoods.
  evidence_refs:
  - E1
  - E3
  possible_diagnostics:
  - Cross-check digitized reserves against the statutory planning portal or GeoInfo Map, as other research teams have done
  - Sensitivity to excluding small or irregular parcels below a size threshold
- type: static_exposure_no_rollout
  basis: inferred
  condition: GovLR is a fixed year-2000 baseline with no time variation; designs that need within-neighborhood treatment timing cannot use this exposure directly, and the interaction design attributes all dynamics to prices and the demand instrument.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Rebuild an annual reserve panel from successive land-sale records if parcel-level sales data are obtainable
- type: lag_and_measurement_choices
  basis: reported
  condition: The construction-cost shifter lag (3.5 years) was chosen after the 1.5-year lag produced unexpected positive signs, and housing stocks are proxied by permits rather than completions; both choices are judgment calls that could shape the baseline elasticity.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Replicate with completion-based stocks and alternative lag structures, as the paper partially reports
- type: proprietary_neighborhood_boundaries
  basis: reported
  condition: The 56-neighborhood partition is the private vendor EPRC's classification, with four low-transaction neighborhoods merged into adjacent ones; boundaries are viewable on the company website but are not an official statistical geography.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Rebuild the design on official Tertiary Planning Unit or District Council boundaries and compare elasticity rankings
empirical_requirements:
  contract_version: 1
  population: Residential neighborhoods of Hong Kong (56-neighborhood EPRC partition) and their housing transactions, construction permits, and land reserves
  observation_unit: neighborhood-year for the panel; individual repeat-sale transactions and building footprints for index and stock construction
  geography_level: EPRC neighborhood boundaries within Hong Kong SAR
  time_start: 2003
  time_end: 2018
  minimum_frequency: annual
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields:
  - residential transaction prices with repeat-sale pairing and neighborhood location (1995-2018 for index stability)
  - residential construction permit floor areas by neighborhood and year
  - building projection areas and elevation levels (iG1000) and actual residential land use (Land Utilization Map 2003) for initial stocks
  - year-2000 government land reserve polygons or the digitized mid-2012 survey plus 2003-2012 government land sales (Lands Department and MTRC)
  - 2001 census tourism-related employment shares by neighborhood
  - annual Mainland Chinese tourist arrivals (Census and Statistics Department)
  - citywide construction cost index and neighborhood initial structure shares
  - neighborhood centroids or CBD distance
  required_identifiers:
  - neighborhood_id
  - year
  - parcel or reserve polygon identifier with coordinates
  treatment_key:
  - neighborhood_id
  treatment_source: >
    Year-2000 GovLR per neighborhood from the digitized Development Bureau
    mid-2012 reserve survey, Planning Department rezoning intentions, and
    Lands Department and MTRC land-sale add-backs; demand instrument from
    Census and Statistics Department tourist arrivals and 2001 census tourism
    employment shares.
  measurement_risks:
  - the reserve measure is an author digitization of a PDF map, not an official neighborhood tabulation
  - permit-based stock changes proxy, rather than observe, completions
  - the EPRC partition is proprietary and merges four neighborhoods
  - the year-2000 baseline depends on MTRC annual report availability from 2000
design_profiles: []
evidence:
- id: E1
  source_type: paper
  citation: 'Ren, Ren, Siu Kei Wong, and Kwong Wing Chau. 2025. "Housing supply elasticity and government-owned land: evidence from Hong Kong." Journal of Economic Geography 25(5): 665-683. DOI: 10.1093/jeg/lbaf010.'
  url: https://centaur.reading.ac.uk/120373/9/lbaf010.pdf
  date: 2025
  supports:
  - identity.instrument
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.local_timing
  - timeline.anticipation
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.exemptions
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
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.geography_level
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.treatment_source
  - design_applications.paper
  - design_applications.research_question
  - design_applications.population
  - design_applications.outcome
  - design_applications.data_used
  - design_applications.treatment_encoding
  - design_applications.comparison
  - design_applications.empirical_design
  verification_status: verified
  access_level: full-text
  locator: >
    Open-access CC-BY published-version PDF from the University of Reading
    CentAUR repository, downloaded and read in full on 2026-08-15 (the OUP page
    returned 403): abstract; Section 2 (public leasehold cost advantages);
    Section 3.1 (EPRC 60-to-56 neighborhoods, repeat-sales indices 1995-2018,
    July 2003 to July 2018 window, iG1000 plus LUM 2003 initial stocks,
    permit-based annual supply, construction-cost supply shifter with
    2000-2002 hedonic structure shares of 39-64 percent); Section 3.1.3
    (Tourist, Labor-1, and Labor-2 instrument construction); Section 3.2.4 and
    footnotes 9-11 (mid-2012 Development Bureau survey digitization, Planning
    Department rezoning intentions, 2003-2012 land-sale add-back, year-2000
    baseline, no reserve expansion 2000-2012); Section 4.1 (Equation 4, 1.5-year
    price lag, 3.5-year cost lag choice); Section 4.1.2 (IVS background and the
    four exclusion-restriction rebuttals, including the 0.001 percent buyer
    estimate and 0.87 hectare commercial rezoning figure); Table 3 (baseline
    0.00916, first-stage F statistics, overidentification p = 0.90); Sections
    4.2-4.3 and Tables 4-7 (multicollinearity among geography determinants,
    GovLR interaction 0.00449, CBD-distance interaction 0.00066, joint F-test
    chi-square 22.15, neighborhood elasticity range 0.00041-0.02419); Section 5
    (limitations and generalization claims). Establishes the paper's design,
    data construction, and reported diagnostics; does not independently verify
    the underlying EPRC, Lands Department, or census inputs.
- id: E2
  source_type: policy-document
  citation: 'Hong Kong SAR Tourism Commission. "Individual Visit Scheme." Official scheme description, confirming the 2003-07-28 launch in four Guangdong cities (Dongguan, Zhongshan, Jiangmen, Foshan) under CEPA, staged expansion, Mainland-issued endorsements, and the seven-day stay limit.'
  url: https://www.tourism.gov.hk/en/visitor_ind.php
  date: 2026
  supports:
  - identity.authority
  - identity.legal_identifiers
  - timeline.announcement
  - timeline.effective
  - timeline.local_timing
  verification_status: verified
  access_level: official-document
  locator: >
    Official Tourism Commission page fetched and read 2026-08-15: states the
    scheme was first introduced in four Guangdong cities on 28 July 2003 as a
    liberalization measure under CEPA, that coverage has expanded since
    implementation (59 Mainland cities at inspection; contemporary government
    releases record 49 cities by 2007), that eligible residents apply for exit
    endorsements from the relevant Mainland authorities, and that each stay may
    not exceed seven days with no quota on endorsements. Establishes the IVS
    launch date, institutional authority, and stay limit; the page does not
    list the historical city-by-city expansion dates.
- id: E3
  source_type: policy-document
  citation: 'Hong Kong SAR Development Bureau. 2013-02-06. "LCQ17: Land reserved for building New Territories small houses," written reply by the Secretary for Development, confirming the 2012-10-17 release of the unleased and unallocated government land location maps and the end-June 2012 statistics (391.5 hectares zoned Residential or Commercial/Residential after deductions).'
  url: https://www.devb.gov.hk/en/sdev/press/index_id_7659.html
  date: '2013-02-06'
  supports:
  - identity.instrument
  - identity.authority
  - identity.implementation_regime
  - identity.legal_identifiers
  - assignment.exposure_construction
  - assignment.compliance
  verification_status: verified
  access_level: official-document
  locator: >
    Development Bureau press-record page fetched and read 2026-08-15: the
    reply states that the figures came from a Legislative Council question on
    vacant government land on 2012-10-17, that the location maps of unleased
    and unallocated government land were released on the bureau's website that
    day, that the statistics are as at end-June 2012 (391.5 hectares zoned
    Residential or Commercial/Residential and 932 hectares zoned Village Type
    Development after deducting roads, passageways, man-made slopes, simplified
    temporary land allocations, and fragmented sites below 0.05 hectares), that
    the areas were obtained by subtracting leased or allocated areas from the
    zoning totals on statutory plans, and that unleased or unallocated land is
    not equivalent to land immediately available for development. Establishes
    the survey's existence, release date, reference date, and official caveats;
    the underlying map image itself was not re-digitized here.
- id: E4
  source_type: paper
  citation: 'Ren, Ren, Siu Kei Wong, and Kwong Wing Chau. 2025. "Housing supply elasticity and government-owned land: evidence from Hong Kong." Journal of Economic Geography 25(5): 665-683 (publisher bibliographic record).'
  url: https://doi.org/10.1093/jeg/lbaf010
  date: 2025
  supports:
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
  verification_status: reported
  access_level: metadata
  locator: >
    Publisher DOI record and CentAUR metadata page; the OUP article page
    returned 403 on 2026-08-15 and was not read directly. Bibliographic
    identity (authors, journal, volume 25 issue 5, starting page 665) is
    cross-checked against the University of Reading CentAUR record
    (https://centaur.reading.ac.uk/120373/) and the open-access published
    full text (E1).
design_applications:
- paper: 'Housing supply elasticity and government-owned land: evidence from Hong Kong'
  doi: 10.1093/jeg/lbaf010
  journal: Journal of Economic Geography
  year: 2025
  research_question: Does the availability of government-owned land, alongside topography, zoning, undeveloped land scarcity, and CBD distance, determine within-city heterogeneity in housing supply elasticity?
  population: 56 EPRC neighborhoods of Hong Kong observed annually from July 2003 to July 2018 (840 neighborhood-year observations)
  outcome: Annual log change of neighborhood housing stocks (initial 2003 floor area plus permit-based new supply) and neighborhood-level supply elasticity
  data_used:
  - EPRC residential transactions 1995-2018 and neighborhood boundaries
  - iG1000 building projection and elevation maps with Land Utilization Map 2003 for initial stocks
  - residential construction permits for annual new supply
  - Development Bureau mid-2012 unleased and unallocated government land survey, Planning Department rezoning intentions, and Lands Department and MTRC land sales 2003-2012 for GovLR
  - Outline Zoning Plans 2018 with rezoning records for residential-zoned land in 2003
  - Digital Terrain Model and Land Utilization Map for flat and undeveloped land shares
  - Census and Statistics Department Mainland tourist arrivals and 2001 census industry employment shares
  - Hong Kong construction cost index for the supply shifter
  treatment_encoding: >
    Year-2000 GovLR share (percent of neighborhood land) interacted with the
    1.5-year-lagged log price change; price changes instrumented by the
    log-differenced Bartik Tourist IV (Mainland tourist arrivals times 2001
    tourism employment shares); construction-cost Bartik shifter lagged 3.5
    years; year fixed effects.
  comparison: >
    Cross-neighborhood comparison within Hong Kong in each year under year
    fixed effects; no treated-versus-control rollout; alternative Labor-1 and
    Labor-2 instruments and lag choices as robustness.
  empirical_design: Panel 2SLS supply-elasticity estimation with a Bartik demand instrument and determinant interactions (GovLR, CBD distance)
  assumptions:
  - Tourist arrivals shift demand but not supply except through prices
  - Year-2000 GovLR affects supply responses only through development costs
  - Permit-based stocks with the chosen lags proxy supply responses
  threats_addressed:
  - Weak instruments via first-stage F statistics (all above 78)
  - Instrument validity via overidentification with the Labor-2 instrument (p = 0.90)
  - Four specific exclusion-restriction channels (visa authority, investor-buyers, commercial rezoning, residential-commercial substitution), each argued away with data
  - Multicollinearity among geography determinants by reducing to GovLR and CBD distance
  evidence_refs:
  - E1
  - E2
  - E3
  - E4
method_transfer: null
readiness_blockers:
- The Tourist IV exclusion restriction rests on the paper's own arguments and auxiliary calculations; treat it as a documented construction with an open exclusion question, not as settled.
- Neighborhood GovLR values are author digitizations of a one-off PDF map plus land-sale add-backs and are not officially published at neighborhood level; the Development Bureau cautions that unleased land is not immediately developable.
- The exposure is time-invariant (year-2000 baseline), so the record cannot support designs that need within-neighborhood treatment timing without new data work.
- EPRC neighborhood boundaries are proprietary, and four of sixty neighborhoods were merged; replication on official geographies is untested.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Hong Kong operates a public leasehold system: the government owns all land
until it is leased to private developers, usually by auction or tender, and
remains the lease regulator afterward [E1]. Developing private land faces two
cost barriers that public land avoids: assembling fragmented private titles,
and negotiating land-lease modifications with premia that the paper describes
as substantial and delay-prone [E1]. Because the government is simultaneously
land supplier and regulator, neighborhoods holding more unleased government
land reserved for residential use can convert demand pressure into new housing
more easily [E1]. The reserve measurement rests on a one-off Development
Bureau survey released on 2012-10-17, whose location maps and end-June 2012
statistics (391.5 hectares of unleased or unallocated land zoned Residential
or Commercial/Residential after deductions) are confirmed by the bureau's
official Legislative Council reply, which also cautions that such land is not
equivalent to land immediately available for development [E3].

The demand side of the design rests on the Individual Visit Scheme, a
central-government liberalization under CEPA that began in four Guangdong
cities on 2003-07-28 and expanded in stages to 49 Mainland cities by 2007,
with endorsements issued by Mainland authorities and stays limited to seven
days [E2]. Mainland tourist arrivals grew persistently through the study
window, and tourism-related industries grew faster than most of the Hong Kong
economy [E1].

## What Changed

Nothing assigned the exposure: the relevant institutional fact is the
pre-existing geography of unleased government land, measured at a year-2000
baseline, combined with a demand environment reshaped by the IVS from 2003
onward [E1, E2]. What the paper contributes is the measurement and the
estimation chain: digitizing the 2012 reserve survey, adding back 2003-2012
government land sales to recover the 2000 baseline, and estimating
neighborhood housing supply elasticity over 2003-2018 with a tourist-based
Bartik instrument [E1]. The canonical boundary is this Hong Kong
government-land-reserve exposure; the companion Beijing land-availability
instrument is a related but institutionally distinct variation recorded
separately.

## Implementation and Assignment

The 56-neighborhood EPRC partition (60 classified neighborhoods minus four
merged for sparse transactions) carries different year-2000 GovLR shares
[E1]. The paper codes no treated group; GovLR enters as a continuous
interaction with instrumented price changes, and neighborhood elasticity is
recovered as alpha1 + alpha2 * GovLR + alpha3 * CBD distance [E1]. The
endogenous price term is instrumented by the log-differenced product of
annual Mainland tourist arrivals and 2001 census tourism employment shares;
the reported first-stage F is 133.6, and the overidentification test against
the Labor-2 instrument has p = 0.90 [E1]. The construction-cost supply
shifter follows Saiz (2010): citywide cost changes multiplied by each
neighborhood's initial structure share from a 2000-2002 hedonic regression
[E1].

## Why This Creates Empirical Variation

The assignment-generating feature is the inherited location of government
land reserves, fixed before the study window and reported to correlate weakly
with neighborhood income, density, and CBD distance [E1]. Within one
leasehold city, this supports a cross-neighborhood design that avoids
interjurisdictional confounds, while the IVS provides a citywide demand shift
with predetermined local shares [E1, E2; analytical inference on the design
logic]. The same institution family exists in other public-leasehold
economies, but the exposure must be re-derived city by city [E1].

## Identification Risks

The first-order risk is the tourist instrument's exclusion restriction: the
paper argues away four violation channels (Mainland-issued endorsements, an
estimated 0.001 percent of tourists buying property, 0.87 hectares of
commercial rezoning, no negative residential-commercial construction
correlation), but these are reported arguments, not independent tests, and
tourism income could affect neighborhoods through commercial property or
amenity channels [E1; analytical inference]. The exposure measure is an
author digitization of a PDF map whose own publisher warns that unleased land
includes undevelopable fragments [E1, E3]. GovLR has no time dimension, the
construction-cost lag was selected after sign problems at shorter lags, and
the neighborhood partition is proprietary [E1]. These limits bound what reuse
can claim.

## Data Requirements

Reuse needs EPRC transaction and boundary data (or an alternative price
source and geography), iG1000 and Land Utilization Map 2003 for initial
stocks, residential permit floor areas, the 2012 reserve survey with Planning
Department rezoning intentions and 2003-2012 Lands Department and MTRC sales,
2001 census tourism employment shares, annual Mainland tourist arrivals, the
construction cost index, and CBD distances [E1]. Dataset acquisition paths
belong in the companion data repository; this record stores the treatment
contract.

## Evidence Notes

E1 is the open-access published-version full text from the University of
Reading repository, read in full; it establishes the design, constructions,
and reported diagnostics, but not the underlying proprietary or administrative
inputs. E2 is the official Tourism Commission description of the IVS, read
directly; it establishes the launch date, CEPA framing, Mainland issuance of
endorsements, and seven-day limit, but does not enumerate historical expansion
dates (49 cities by 2007 is consistent with contemporaneous government
releases). E3 is the Development Bureau's official Legislative Council reply,
read directly; it establishes the reserve survey's release date (2012-10-17),
reference date (end-June 2012), construction method, and official caveats.
A companion paper by the same authors (Ren, Wong, and Chau 2023, Journal of
Real Estate Finance and Economics) uses a similar government land share to
study within-city price heterogeneity; it was not fully inspected here and is
retained only as an unverified related lead.
