---
schema_version: 2
id: china-beijing-soe-relocation-land-supply-iv
name: Beijing SOE Industrial Relocation Land Release as a Land-Supply Instrument
aliases:
- Zheng Sun Wang 2014 Beijing land supply capitalization IV
- Beijing prereform SOE employment density land-availability instrument
- 北京国企搬迁释放土地供给工具变量
status: grounded
provenance:
  task_id: task-cd4e6501fe6c
scope:
  country: China
  regions:
  - Beijing Metropolitan Area (eight urban districts), 1999-2008
  domains:
  - urban
  - regional-economics
  - economic-geography
  - public-finance
  - education
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    The exposure is a China-specific institutional legacy: prereform state-owned
    manufacturing enterprises occupied centrally located urban land, and
    Beijing's SOE-reform-era relocation program (announced 1999-10-29,
    implemented 1999-2004) released that land for residential redevelopment.
    Zheng, Sun, and Wang (2014, Journal of Regional Science) use the spatial
    distribution of SOE manufacturing employment at the start of SOE reform to
    instrument zone-level land availability when estimating how land supply
    changes the capitalization of school quality and subway access into Beijing
    housing prices, 2006-2008.
identity:
  instrument: >
    The relocation and disassembly of state-owned industrial enterprises from
    central Beijing under the municipal industrial-relocation program, which
    converted SOE-occupied industrial land into land leasable for residential
    development. The paper operationalizes cross-zone exposure with the density
    of SOE manufacturing employment by zone at the beginning of 2000 (Year 2000
    China Manufacturing Census), on the logic that zones with more prereform SOE
    manufacturing had more releasable industrial land thereafter.
  authority: >
    Beijing Municipal Government. The relocation program was announced by
    municipal officials on 1999-10-29 at the Beijing industrial-enterprise
    relocation symposium, and the implementation plan for relocating industrial
    enterprises within the Third and Fourth Ring Roads was approved by the
    Beijing Municipal Government General Office in 2000 under the Beijing
    Industrial Layout Adjustment Plan.
  legal_identifiers:
  - Jing Zheng Ban Han [2000] No. 91, Beijing Municipal Government General Office approval of the Implementation Plan for Relocating Industrial Enterprises within the Third and Fourth Ring Roads, 2000-08
  - (99) Jing Jing Gui Hua Zi No. 200, Beijing implementation measure for relocating polluting and resident-disturbing enterprises and accelerating industrial restructuring, 1999 (referenced in the 2000 plan)
  - Beijing Industrial Layout Adjustment Plan (framing plan cited by the 2000 approval)
  implementation_regime: >
    Public urban land leasehold: the Beijing municipal government is the sole
    supplier of development land, residential leaseholds run 70 years, and since
    2004 leaseholds are in principle sold at public auction. Under the 1999-2004
    program, relocated enterprises' original sites were transferred or leased
    for redevelopment; municipal land acquisition, reserve, and conveyance
    organs managed the released sites, and relocation was phased in annual
    batches with incentives and penalties for delayed movers.
  assignment_mechanism: >
    No rule assigns zones to treatment. Exposure is the inherited spatial
    distribution of prereform SOE manufacturing across 25 BMA zones: zones with
    denser SOE manufacturing employment at the start of SOE reform had more
    industrial land available for release and hence larger subsequent
    residential land supply. The paper therefore instruments zone-level leased
    residential land with log SOE employment density, not with an eligibility
    list, threshold, or rollout date.
  parent: null
  related_variations:
  - china-industrial-land-supply-target-area-churn
timeline:
  announcement: '1999-10-29'
  effective: '2000'
  implementation_start: 1999
  implementation_end: 2004
  local_timing: >
    Enterprise relocation from central Beijing began in 1985 with polluting
    firms, entered a combined relocation-and-restructuring phase in 1995-1999,
    and was accelerated by the 1999-2004 program covering enterprises within
    the Fourth Ring Road, with annual batches scheduled 2000-2004 and a target
    of cutting the industrial land share in the planned central area from 8.74
    percent to 7 percent. The paper's instrument baseline is SOE manufacturing
    employment at the beginning of 2000, and its study window is 2006-2008,
    after much of the relocation wave; land leased in 2004-2008 enters the
    cumulative exposure measure.
  anticipation: >
    The program was publicly announced at the end of 1999 with a 3-5 year
    horizon, and relocation proceeded in announced annual batches, so
    developers and households could anticipate land release in SOE-dense zones
    well before the 2006-2008 study window. The instrument captures inherited
    industrial geography rather than a surprise shock.
  last_verified: '2026-08-15'
assignment:
  unit: >
    Zone within the Beijing Metropolitan Area: 25 zones built by grouping 3-6
    adjacent street offices (jiedaos) with continuous concentrated economic
    activity, following Zheng, Peiser, and Zhang (2009), within the eight urban
    districts and their 123 jiedaos; micro observations are resale housing
    transactions and new housing complexes.
  treated: >
    Zones with greater land availability, measured as the three-year cumulative
    amount of auctioned residential land leased (current year plus two previous
    years, in km2) per zone; in the IV design, high-availability zones are those
    with higher prereform SOE manufacturing employment density.
  comparison_pool: >
    Other BMA zones with less released land in the same cross-section; the
    hedonic regressions include zone and year fixed effects, so identification
    comes from cross-zone differences in instrumented land supply interacted
    with amenity distances, not from a treated-versus-control rollout.
  rule: >
    Aggregate auctioned residential land parcels (China Real Estate Index
    System, 2004-2008) to zone-year leased area; instrument the interaction of
    log leased land with amenity distances using log SOE manufacturing
    employment density by zone (persons/km2, beginning of 2000, Year 2000 China
    Manufacturing Census) interacted with the same amenity distances. Reported
    first stage: correlation 0.36 (p=0.001) between log SOE density and log land
    leased 2006-2008, with near-zero correlations with housing prices.
  intensity: >
    Continuous: leased residential land per zone-year and SOE employment density
    per zone are both continuous; an edge-versus-center subsample split is used
    only as a preliminary descriptive contrast.
  exemptions:
  - Nonresidential land parcels, which do not enter the residential land-availability measure
  - Zone-years with zero leased parcels under short accumulation windows, a measurement limitation rather than a policy exemption
  - New complexes outside a key school's attendance zone despite physical proximity, noted by the authors as a school-capacity exception
  compliance: >
    The record does not verify zone-by-zone relocation completion against the
    1999-2004 annual batch plans; aggregate reports indicate industrial land
    share within the Fourth Ring Road fell from 8.74 percent toward 7.26 percent
    by early 2002, but the paper's exposure measure is leased residential land,
    not audited relocation counts.
  exposure_construction: >
    Join auctioned residential land parcels and housing transactions to the 25
    zones by exact location; compute three-year cumulative leased residential
    land per zone; compute each unit's distance to the nearest subway stop and
    to the nearest of the 40 key primary schools (designated by the Beijing
    Municipal Commission of Education from the late 1950s, policy formally
    abandoned in 2000); merge zone-level SOE manufacturing employment density
    from the Year 2000 China Manufacturing Census.
  required_identifiers:
  - zone identifier over the 25-zone BMA partition, with its jiedao composition
  - parcel identifier with land-use type, area, location, and lease year
  - residential complex location for resale transactions and new complexes
  - SOE manufacturing employment and zone area for the 2000 density baseline
  - the 40 key primary school list and subway station locations
  spillovers: >
    Housing markets are citywide: supply released in one zone can substitute for
    demand in neighboring zones, and capitalization differences partly reflect
    sorting across zones. The paper addresses spatial dependence with spatial IV
    models (spatially lagged prices and disturbances on an inverse-distance
    weights matrix) and finds qualitatively consistent but smaller interaction
    coefficients.
research_compatibility:
  outcome_domains:
  - housing prices and amenity capitalization
  - urban land supply and housing supply elasticity
  - local public goods valuation (school quality, subway access)
  affected_populations:
  - Homebuyers and residential complexes in the Beijing Metropolitan Area, 2006-2008
  - Real estate developers bidding for released industrial land
  - Relocated SOE industrial enterprises and their former sites
  mechanism_channels:
  - land availability lowering housing supply elasticity
  - inelastic supply amplifying capitalization of school quality and subway access
  - SOE relocation releasing centrally located industrial land
  best_for:
  - Studies of how land or housing supply constraints shape the capitalization of local public goods in Chinese cities
  - Designs needing a within-city spatial instrument for residential land availability in Beijing or comparable former-SOE industrial cities
  - Hedonic analyses linking school or transit access to prices under supply constraints
  not_good_for:
  - Designs that need a discrete rollout, eligibility rule, or threshold; the variation is a continuous spatial exposure with an announced, phased program
  - Cross-city land-supply questions, since the instrument and relocation program are Beijing-specific
  - Claims that SOE employment density is unconditionally exogenous for neighborhood outcomes; the authors themselves flag correlations with historical and cultural legacies
  - Post-2008 housing markets without re-deriving the exposure window
design:
  claim_type: causal
  affordances:
  - Cross-zone variation in residential land availability within one metropolitan government, avoiding interjurisdictional fiscal and regulatory confounds
  - A prereform industrial-geography instrument with a reported first stage and weak raw correlation with price levels
  - Two independent housing samples (resale transactions and new complexes) for the same design
  candidate_designs:
  - Hedonic price regression with land-availability-by-amenity interactions instrumented by SOE-density-by-amenity interactions (2SLS)
  - Spatial IV hedonic models with autoregressive prices and disturbances
  - Edge-versus-center subsample capitalization contrast as descriptive preliminary evidence
  identifying_variation: >
    Cross-zone differences in prereform SOE manufacturing employment density,
    which shift subsequent residential land availability through the relocation
    program, conditional on zone and year fixed effects and distance to the CBD.
  primary_strategy: >
    Two-stage least squares hedonic regressions of log price on amenity
    distances interacted with instrumented log leased land; instruments are log
    SOE density interacted with the amenity distances. Joint first-stage
    F-statistics for the two interaction instruments are 5.17 and 15.96 in the
    resale sample and 15.94 and 11.30 in the new-housing sample; a Hausman test
    rejects exogeneity of the land-supply interactions.
  estimand: >
    The effect of zone-level land availability on the capitalization rates
    (implicit prices) of key-primary-school proximity and subway proximity in
    Beijing housing prices, 2006-2008.
  treatment_variable: >
    Three-year cumulative leased residential land (log, km2) per zone-year,
    interacted with log distance to the nearest key primary school and to the
    nearest subway stop; instrumented with log 2000 SOE manufacturing employment
    density per zone interacted with the same distances.
  comparison_logic: >
    Within the BMA, compare capitalization across zones with more versus less
    instrumented land supply; zone fixed effects absorb time-invariant zone
    amenities and year effects absorb common shocks. The comparison fails if
    SOE-dense zones differ in unobserved amenity or demographic composition that
    independently shifts amenity pricing.
  estimation_notes: >
    Resale sample: 13,188 transactions in about 2,600 complexes from the
    WoAiWoJia brokerage (about 10 percent market share), standard errors
    clustered by complex. New-housing sample: 1,129 complexes with
    complex-average attributes. Robustness: one- and two-year land-accumulation
    windows, 800-meter amenity dummies, and spatial autoregressive IV models;
    shorter windows weaken results and spatial models shrink the interactions.
  assumptions:
  - Prereform SOE manufacturing employment density affects 2006-2008 amenity capitalization only through land availability, conditional on zone fixed effects and CBD distance
  - The 25-zone partition preserves the relevant submarket structure despite its admittedly subjective construction
  - Zone fixed effects adequately absorb the historical, cultural, and demographic correlates of SOE siting that the authors flag as threats to exclusion
  - Amenity distances proxy the school-quality and transit-access attributes households price
  diagnostics:
  - First-stage joint F-tests on the SOE-density interaction instruments
  - Hausman test for endogeneity of the land-supply interaction terms
  - Correlation of the instrument with price levels as an exclusion plausibility check (reported as -0.02 resale and 0.06 new housing, insignificant)
  - Rejection of historical population density (1982 census) as an alternative instrument because it correlates with prices but not land leased
  - Alternative land-accumulation windows, 800-meter amenity dummies, and spatial autoregressive specifications
threats:
- type: instrument_exclusion_restriction
  basis: reported
  condition: The authors state that historical SOE manufacturing employment may not be fully exogenous because it can correlate with community attributes such as cultural and historical legacies and local population composition, which may independently affect amenity capitalization.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Zone fixed effects and the reported weak instrument-price correlations
  - Overidentification is unavailable with a single instrument source; test alternative baselines or subsets of zones
- type: subjective_zone_partition
  basis: reported
  condition: The 25-zone aggregation of jiedaos is described by the authors as somewhat subjective; different partitions could change both the exposure measure and the comparison set.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Rebuild exposure on jiedaos or alternative submarket definitions
  - Sensitivity of interaction coefficients to the number and boundaries of zones
- type: residential_sorting_and_anticipation
  basis: inferred
  condition: The relocation program was announced in 1999 with phased annual batches, so households and developers could sort in anticipation of land release and amenity changes before 2006-2008.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Examine price and supply trends in SOE-dense zones between 1999 and 2006 with earlier data
  - Compare results across the one-, two-, and three-year accumulation windows, as the paper does
- type: broker_sample_coverage
  basis: inferred
  condition: The resale sample covers one brokerage with about 10 percent market share; complex-level selection into that broker could distort zone-level price measurement.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Cross-check with the independent new-complex sample, which the paper provides
  - Re-estimate on complex-averaged prices as in the spatial IV robustness
- type: spatial_dependence
  basis: reported
  condition: Omitted spatial dependence in prices and errors biases plain 2SLS; the paper's spatial IV models yield smaller interaction coefficients, indicating non-spatial specifications may overstate supply-constraint differences.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Spatial autoregressive IV specifications with inverse-distance weights, as reported
  - Conley-style spatial standard errors as an additional check in reuse
empirical_requirements:
  contract_version: 1
  population: Housing transactions and auctioned residential land parcels in the eight urban districts of the Beijing Metropolitan Area
  observation_unit: Resale transaction or new housing complex for outcomes; zone-year for the land-availability measure
  geography_level: 25-zone partition of the Beijing Metropolitan Area built from 123 jiedaos
  time_start: 2006
  time_end: 2008
  minimum_frequency: annual
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields:
  - transaction or complex-average price per square meter and housing attributes (size, age, decoration; complex height and floor area)
  - auctioned residential parcel area, land-use type, location, and lease year (2004-2008 for the accumulation windows)
  - SOE manufacturing employment by zone at the beginning of 2000
  - locations of the 40 key primary schools and subway stations
  required_identifiers:
  - zone_id
  - parcel_id
  - complex_id
  - year
  treatment_key:
  - zone_id
  - year
  treatment_source: >
    Zone-year leased residential land aggregated from China Real Estate Index
    System auction records (2004-2008); instrument from SOE manufacturing
    employment in the Year 2000 China Manufacturing Census aggregated to the
    25-zone partition.
  measurement_risks:
  - the 25-zone partition is a research construction and is not published as an official crosswalk
  - single-broker resale coverage of about 10 percent of the market
  - key-school list reflects a designation abandoned in 2000, not current measured school quality
  - short accumulation windows leave many zone-years with zero leased parcels
design_profiles: []
evidence:
- id: E1
  source_type: paper
  citation: 'Zheng, Siqi, Weizeng Sun, and Rui Wang. 2014. "Land Supply and Capitalization of Public Goods in Housing Prices: Evidence from Beijing." Journal of Regional Science 54(4): 550-568. DOI: 10.1111/jors.12095.'
  url: https://www.cre.tsinghua.edu.cn/__local/7/2E/FD/FB06D0C1AFA9C31C0BDEFDEE651_54B1BFBC_121322.pdf
  date: 2014
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.anticipation
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.exposure_construction
  - assignment.spillovers
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
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
    Author-hosted accepted-manuscript PDF on the Tsinghua University Center for
    Real Estate site, full text inspected 2026-08-15 (the Wiley page returned
    403): abstract, data section (13,188 resale transactions in about 2,600
    complexes from WoAiWoJia; 1,129 new complexes from the China Real Estate
    Index System; CREIS auctioned residential parcels 2004-2008; 25 zones from
    123 jiedaos; 40 key primary schools), Section 5 (SOE instrument from the
    Year 2000 China Manufacturing Census, correlation 0.36 with land leased
    2006-2008, near-zero price correlations, rejection of the 1982 population
    density instrument), Table 3 first-stage F-statistics and Hausman test,
    Table 4 accumulation-window robustness, Table 5 spatial IV robustness, and
    the conclusion's own exogeneity and zone-partition caveats. Establishes the
    paper's design and reported diagnostics; does not independently verify the
    underlying administrative land or census records.
- id: E2
  source_type: archive
  citation: 'China Economic Times (中国经济时报). 1999-11-02. "All industrial enterprises within Beijing''s Fourth Ring Road to relocate within 3 to 5 years" (北京四环以内所有工业企业将于3至5年内搬迁), contemporaneous report of the 1999-10-29 Beijing municipal announcement; reprinted by Sina News.'
  url: https://news.sina.com.cn/china/1999-11-2/28214.html
  date: '1999-11-02'
  supports:
  - identity.authority
  - identity.implementation_regime
  - timeline.announcement
  - timeline.effective
  - timeline.local_timing
  - assignment.exposure_construction
  verification_status: verified
  access_level: full-text
  locator: >
    Sina News archive page fetched and read 2026-08-15: reports that on
    1999-10-29 Beijing municipal officials announced at the industrial-
    enterprise relocation symposium that enterprises within the Fourth Ring
    Road would relocate over 3-5 years, involving 738 enterprises and cutting
    the industrial land share in the planned central area from 8.74 percent to
    7 percent, with incentives for movers, land-transfer income rules, and a
    municipal land acquisition-reserve-conveyance mechanism. Establishes the
    announcement date and program scale as contemporaneously reported; the
    original focus.cn link cited by the paper (1999-11-03) is dead (404).
- id: E3
  source_type: policy-document
  citation: 'Beijing Municipal Government General Office. 2000. "Approval of the Implementation Plan for Relocating Industrial Enterprises within the Third and Fourth Ring Roads" (京政办函〔2000〕91号), with the attached implementation plan dated 2000-03-21 and issued 2000-08-30.'
  url: https://www.110.com/fagui/law_281849.html
  date: '2000-08-30'
  supports:
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.local_timing
  verification_status: reported
  access_level: full-text
  locator: >
    Full document text obtained 2026-08-15 through the 110.com legal-database
    entry as indexed in web search; a direct fetch of the same URL returned a
    503 anti-bot page and could not be re-read. The text records a survey of
    783 enterprises within the Fourth Ring Road as of May 1999, the 8.74-to-7
    percent industrial land target, annual relocation batches 2000-2004 (134
    enterprises planned for 1999-2004), transfer of vacated sites, and
    incentives under (99) Jing Jing Gui Hua Zi No. 200. Treated as reported,
    not verified, until an official gazette or government copy is inspected.
- id: E4
  source_type: paper
  citation: 'Zheng, Siqi, Weizeng Sun, and Rui Wang. 2014. "Land Supply and Capitalization of Public Goods in Housing Prices: Evidence from Beijing." Journal of Regional Science 54(4): 550-568 (publisher bibliographic record).'
  url: https://doi.org/10.1111/jors.12095
  date: 2014
  supports:
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
  verification_status: reported
  access_level: metadata
  locator: >
    Publisher DOI record; the Wiley page returned 403 on 2026-08-15 and was not
    read directly. Bibliographic identity (authors, journal, volume 54 issue 4,
    pages 550-568) cross-checked against the XJTLU scholar publication entry and
    the author-hosted accepted manuscript (E1).
design_applications:
- paper: 'Land Supply and Capitalization of Public Goods in Housing Prices: Evidence from Beijing'
  doi: 10.1111/jors.12095
  journal: Journal of Regional Science
  year: 2014
  research_question: Does limited land supply increase the capitalization of school quality and subway accessibility into housing prices in a centralized metropolitan government without local property tax?
  population: Resale housing transactions (13,188 units in about 2,600 complexes) and new housing complexes (1,129) in the Beijing Metropolitan Area, 2006-2008
  outcome: Log transaction price per square meter (resale) and log complex-average price (new housing)
  data_used:
  - WoAiWoJia brokerage resale transactions 2006-2008
  - China Real Estate Index System new housing complexes 2006-2008
  - China Real Estate Index System auctioned residential land parcels 2004-2008
  - Year 2000 China Manufacturing Census SOE manufacturing employment by zone
  - Beijing key primary school list and subway station locations
  treatment_encoding: >
    Three-year cumulative leased residential land per zone (log), interacted
    with log distances to the nearest key primary school and subway stop;
    instrumented by log 2000 SOE manufacturing employment density per zone
    interacted with the same distances.
  comparison: >
    Cross-zone comparison within the BMA under zone and year fixed effects; a
    descriptive edge-versus-center split precedes the IV design; spatial IV
    models address dependence.
  empirical_design: Hedonic 2SLS with instrumented land-availability-by-amenity interactions, plus spatial autoregressive IV robustness
  assumptions:
  - SOE employment density affects capitalization only through land availability conditional on zone fixed effects
  - The zone partition approximates submarket structure
  - Broker-sample and complex-average measurements proxy market prices
  threats_addressed:
  - Endogeneity of land supply via the SOE instrument and Hausman test
  - Spatial dependence via SAR/SARAR IV models
  - Measurement via accumulation windows and 800-meter amenity dummies
  evidence_refs:
  - E1
  - E4
method_transfer: null
readiness_blockers:
- The instrument's exclusion restriction is contested by the authors themselves (historical and demographic correlates of SOE siting); reuse should treat the IV as a documented construction with an open exclusion question, not as settled.
- The 25-zone partition and the zone-level SOE employment and parcel aggregates are author constructions; no official crosswalk was inspected.
- The official implementation plan (京政办函〔2000〕91号) is recorded as reported pending inspection of an official copy, and zone-by-zone relocation compliance was not audited.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Beijing industrialized rapidly after 1949 and by the reform era hosted dense
state-owned manufacturing on centrally located urban land. Enterprise
relocation out of the core began in 1985 with polluting firms, moved into a
combined relocation-and-restructuring phase in 1995-1999, and was accelerated
at the start of SOE reform: on 1999-10-29 municipal officials announced that
industrial enterprises within the Fourth Ring Road would relocate over three
to five years, involving 738 enterprises and aiming to cut the industrial
land share in the planned central area from 8.74 percent to 7 percent [E2].
The General Office approval 京政办函〔2000〕91号 and its attached implementation
plan schedule annual relocation batches for 1999-2004, describe the transfer
of vacated sites, and tie relocation to the Beijing Industrial Layout
Adjustment Plan [E3, reported claim]. Because urban land is state-owned and
the municipality is the sole supplier of development land, released SOE sites
became an important source of residential land leased at auction [E1].

## What Changed

The relocation program converted centrally located industrial land into
redevelopable residential land. The change relevant for research is not the
announcement alone but the spatially uneven legacy it acted on: zones with
more prereform SOE manufacturing had more land to release. Zheng, Sun, and
Wang (2014) turn this into an instrument, using SOE manufacturing employment
density by zone at the beginning of 2000 (Year 2000 China Manufacturing
Census) to instrument subsequent zone-level residential land supply in a
hedonic study of school and subway capitalization, 2006-2008 [E1]. The
canonical boundary is this Beijing SOE-land-release exposure; distinct
variations such as city-level industrial land re-targeting across districts
are recorded separately.

## Implementation and Assignment

There is no eligibility rule or rollout assigning zones. Exposure is a
continuous spatial inheritance: the 25-zone BMA partition (built from 123
jiedaos following Zheng, Peiser, and Zhang 2009) carries different prereform
SOE manufacturing densities, and the relocation program translated that
density into differential land availability [E1]. The paper codes the
endogenous regressor as the three-year cumulative amount of auctioned
residential land per zone-year (log km2), interacted with log distances to
the nearest key primary school and subway stop, and instruments these
interactions with log SOE density interacted with the same distances. The
reported first stage is a 0.36 correlation (p=0.001) between log SOE density
and log land leased 2006-2008, with joint F-statistics of 5.17 and 15.96
(resale) and 15.94 and 11.30 (new housing) on the interaction instruments,
and near-zero raw correlations between the instrument and price levels [E1].

## Why This Creates Empirical Variation

The assignment-generating feature is prereform industrial geography:
central-city SOE siting, decided under the planned economy, predates the
housing market and the relocation program, so it shifts 2006-2008 land
availability without being chosen in response to 2006-2008 amenity pricing
[analytical inference]. Conditional on zone fixed effects and CBD distance,
this supports a within-metropolis IV design that avoids the interjurisdictional
fiscal and regulatory confounds of cross-city capitalization studies, in a
setting where the absence of a local property tax removes the fiscal feedback
channel of the US literature [E1]. The same instrument family is reusable in
other former-SOE industrial cities, but only with city-specific relocation
institutions re-derived.

## Identification Risks

The exclusion restriction is the first-order risk and the authors say so:
SOE employment density can correlate with cultural and historical legacies
and local population composition, and zone fixed effects are the main defense
[E1]. The authors tested and rejected 1982 historical population density as
an alternative instrument precisely because it correlates with prices but not
land leased [E1]. The 25-zone partition is admittedly subjective; the 1999
announcement and phased batches mean sorting and anticipation predate the
study window; the resale sample is one brokerage with about 10 percent market
share; and spatial dependence, when modeled, shrinks the interaction
coefficients [E1; analytical inference on sorting and coverage]. None of
these is a resolved matter; they bound what reuse can claim.

## Data Requirements

Reuse needs auctioned residential parcel records with location, land-use
type, area, and lease year (2004-2008 to rebuild the accumulation windows);
housing transactions or complex averages with prices and attributes for
2006-2008; zone-level SOE manufacturing employment at the beginning of 2000
from the Year 2000 China Manufacturing Census; the 40 key primary school
list and subway station locations; and a stable zone or jiedao geography for
the BMA. Dataset acquisition paths belong in the companion data repository;
this record stores the treatment contract.

## Evidence Notes

E1 is the author-hosted accepted-manuscript full text and establishes the
paper's design, samples, instrument construction, reported diagnostics, and
the authors' own caveats; the Wiley version was inaccessible (403), and E1
does not independently verify the administrative land or census inputs. E2 is
a contemporaneous 1999 news report of the announcement, fetched and read
directly; it establishes the announcement date, scale (738 enterprises), and
land-share target as reported at the time, and replaces the paper's dead
focus.cn citation. E3 is the official implementation approval, but its text
was obtained through a legal-database mirror that blocked direct re-fetching,
so it is recorded as reported rather than verified; its survey count (783
enterprises as of May 1999) and 1999-2004 batch plan (134 enterprises) differ
from the announcement's 738 figure, a discrepancy future work should reconcile
against an official gazette. E4 is the publisher DOI record, reported at
metadata level only, used to anchor the design application's bibliographic
identity. A later Real Estate Economics paper (Sun, Zheng,
and Wang 2017) appears to reuse the same 25-zone and SOE-density construction
for a purchase-restriction heterogeneity analysis, but its full text could not
be inspected here and it is retained only as an unverified reuse lead.
