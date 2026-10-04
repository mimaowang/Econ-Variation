---
schema_version: 2
id: china-anti-corruption-city-inspection-labor-strikes
name: China's Central Inspection Shock and City-Level Labor Strikes
aliases:
- Anti-corruption inspections and labor activism in China
- Central inspection teams and strikes
- 中央巡视与劳工罢工
status: grounded
provenance:
  task_id: task-cb54cbb66e36
scope:
  country: China
  regions:
  - Mainland China city-level geographic units
  domains:
  - political-economy
  - labor
  - urban
  - regional-economics
  - corruption
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    The empirical application uses provincial CCDI-team arrival and the first
    high-profile inspection recorded for a Chinese city-level unit to measure a
    change in its local political environment. The object is the city-level
    inspection exposure and its timing,
    not a blanket claim that the national anti-corruption campaign was random.
identity:
  instrument: >
    China's post-2012 central anti-corruption inspection system, represented in
    the paper by the first high-profile city-level corruption inspection after
    a central inspection team arrives in the province.
  authority: >
    The Central Commission for Discipline Inspection and the central inspection
    work leading group; official CCDI pages document the dispatched teams,
    inspected provinces and units, and feedback dates.
  legal_identifiers:
  - 2012 central anti-corruption campaign and September 2012 launch described by the paper
  - Central inspection-team deployment records published by the CCDI
  - Official CCDI 2013 inspection-entry and feedback notices
  implementation_regime: >
    Central teams entered provinces and inspected party-state units on a
    staggered schedule. The paper distinguishes a city's first high-profile
    inspection event from later or lower-profile events and conditions the
    baseline comparison on the arrival of a CCDI team in the province. The
    paper's city-level event is reconstructed from the investigation data; it
    should not be read as evidence that the central team directly inspected
    every treated city under one formal citywide rollout rule.
  assignment_mechanism: >
    A city-level unit receives the paper's treatment at the date of its first
    high-profile city-level inspection, conditional on the central team having arrived in its
    province. Inspection timing was not disclosed in advance and is not assumed
    to be random; the design uses event timing, not an intrinsic exogeneity
    label.
  parent: null
  related_variations:
  - china-anti-corruption-land-market
  - china-soe-decentralization
timeline:
  announcement: '2012-09'
  effective: null
  implementation_start: 2013
  implementation_end: 2017
  local_timing: >
    The paper studies monthly outcomes from 2011–2020 and dates treatment to
    the first high-profile city inspection. The central campaign began in 2012,
    while the observed provincial team arrivals and city-level investigations
    occur in separate waves. The author manuscript reports 26 cohorts for the
    first any-rank city inspection after provincial team arrival and 28 cohorts
    for the high-profile baseline event; the first any-rank dates span May 2013–
    August 2015 [E4]. Exact high-profile dates must be retained from the paper's
    CID-based city crosswalk rather than inferred from the national launch.
  anticipation: >
    National announcements, team arrival, media attention, and low-profile
    inspections may affect workers before the coded first high-profile date.
    The paper's conditional event-time design does not remove every form of
    anticipation or local selection.
  last_verified: '2026-09-30'
assignment:
  unit: >
    Monthly geographic unit, which the author calls a city for convenience. The
    February 2026 author manuscript's 362-unit panel contains 333 prefecture-level
    cities, four direct-administered municipalities, 24 province-administered
    county-level regions, and Laiwu (then a separate Shandong city); it yields
    43,440 unit-month observations over 2011–2020 [E4]. Firm-level assignment is
    unavailable because the strike data do not identify employers.
  treated: >
    A city-level unit is treated from the month of its first high-profile
    city-level inspection after a CCDI inspection team has arrived in its province.
  comparison_pool: >
    Cities not yet experiencing their first high-profile inspection, including
    later-treated cities in the same province. Neighboring and network-connected
    cities are analyzed as spillovers and should not be treated as automatically
    clean controls.
  rule: >
    Join each city-level unit to the paper's Corruption Investigation Dataset,
    identify the first high-profile inspection event after provincial team arrival, and
    code event time relative to that month. Low-profile inspections and later
    inspections are not interchangeable with the baseline treatment. In the
    February 2026 author manuscript, high-profile means an investigated official
    with CCP rank 1–6 on the paper's scale (rank 1 is highest; rank 6 is deputy-
    bureau-director level), which the author treats as a city-level-or-higher
    official; lower-ranked cases are classified as low-profile [E4]. This is the
    paper's coding rule, not an independently reconstructed city roster.
  intensity: >
    Event-time exposure to the first high-profile inspection, with post-treatment
    months and repeated inspection counts used for mechanisms and enforcement
    checks rather than collapsed into one national post dummy.
  exemptions:
  - The author manuscript reports 128 units with no high-profile inspection and 234 that receive one during the sample; four units have no recorded city inspection after provincial team arrival [E4]
  - Low-profile inspections are not baseline treatment
  compliance: >
    An inspection is an observed administrative event, but its timing reflects
    central selection and local conditions. The paper reports that inspection
    decisions were not disclosed in advance; this supports limited anticipation
    reasoning, not random assignment.
  exposure_construction: >
    Harmonize unit and province identifiers across the Corruption Investigation
    Dataset and the China Labour Bulletin Strike Map, retain the first
    high-profile city-level inspection date conditional on provincial team arrival,
    and create monthly event-time indicators. Preserve neighboring, same-province,
    and Laoxiang-network exposures separately when estimating spillovers. The
    manuscript reports 128 units with no high-profile inspection and 234 exposed
    units; the raw event-to-unit crosswalk has not been inspected here [E4].
  required_identifiers:
  - stable city identifier
  - province identifier
  - calendar month
  - inspection identifier and date
  - high-profile inspection flag and paper-defined city-level event assignment
  - strike record identifier and city
  - sector and grievance category when available
  spillovers: >
    Strikes rise in cities awaiting inspection when another city in the province
    is inspected, and in nearby cities; migrant workers connected through
    same-origin (Laoxiang) networks may transmit information and expectations.
research_compatibility:
  outcome_domains:
  - labor strikes and protests
  - wage arrears
  - labor bargaining and worker grievances
  - firm-government political ties
  - local political accountability
  affected_populations:
  - Workers in Chinese cities, especially migrant and low-skilled workers
  - Private construction and manufacturing firms
  - Local governments and inspected officials
  mechanism_channels:
  - weakened firm-government ties
  - shifted government attention toward worker grievances
  - increased expected returns to striking
  - information and network diffusion across cities
  best_for:
  - Studying how a visible central inspection changes local labor activism
  - Event-time and staggered-treatment designs with city and month data
  - Designs that model same-province, neighboring, and migrant-network spillovers
  not_good_for:
  - Treating the national anti-corruption campaign as one random nationwide date
  - Using inspected cities' neighbors as uncontaminated controls without a network model
  - Interpreting more strikes as more grievances being created rather than grievances becoming more actionable or visible
design:
  claim_type: causal
  affordances:
  - City-level first-inspection timing
  - Monthly strike outcomes before and after treatment
  - Same-province and spatial/network spillover comparisons
  - Sector and grievance heterogeneity
  candidate_designs:
  - Staggered difference-in-differences
  - Event-study around the first high-profile inspection
  - Same-province and neighboring-city spillover designs
  - Heterogeneity by pre-campaign corruption, sector, and migrant networks
  identifying_variation: >
    The identifying contrast is the change in city strike activity around the
    first high-profile inspection, relative to cities not yet inspected and
    conditional on central team arrival in the province. In the author manuscript,
    high-profile cases target officials at CCP ranks 1–6 (rank 1 is highest), and
    128 of 362 geographic units never receive such an inspection. The paper presents
    an event-study design, not a randomized assignment; province arrival is a
    conditioning boundary, not proof that later city timing is random [E4].
  primary_strategy: >
    The paper estimates a monthly event study around each city's first high-profile
    inspection after provincial CCDI-team arrival, with city and month-year fixed
    effects, city-level controls, and standard errors clustered by city. It also
    reports a quarterly specification using Callaway–Sant'Anna, Gardner estimates
    as a robustness check, and separate same-province, neighboring-city, and
    migrant-network spillover analyses [E4].
  estimand: >
    The effect of a city's first high-profile central inspection on monthly
    strike incidents among observed Chinese city-level units during 2011–2020,
    conditional on the paper's inspection-timing and spillover assumptions.
  treatment_variable: >
    Monthly event-time indicators relative to the first city-level investigation
    of an official at CCP rank 1–6 on the paper's rank scale after provincial
    CCDI-team arrival; lower-profile investigations and the first inspection of
    any rank are different event definitions [E4].
  comparison_logic: >
    Compare a city to its own pre-inspection months and to cities whose first
    high-profile inspection occurs later or never occurs. The author reports 234
    treated and 128 never-high-profile units in the 362-unit sample. Same-province,
    neighboring, and migrant-origin networks can transmit exposure, so the paper
    models them rather than treating all not-yet-treated units as clean controls [E4].
  estimation_notes: >
    The published application reports a sharp post-inspection rise, robust
    staggered-DID estimates, and network spillovers. The record should preserve
    the distinction between observed strike reporting and the underlying stock
    of grievances.
  assumptions:
  - No unmeasured city-specific shock changes strike reporting exactly at the first high-profile inspection after conditioning on the design controls
  - Inspection timing and high-profile classification are measured consistently
  - Not-yet-treated cities provide a defensible counterfactual after accounting for spillovers
  - Strike-map coverage and reporting propensity do not change differentially at treatment for unrelated reasons
  diagnostics:
  - Plot event-study pre-trends and placebo inspection dates
  - Compare Callaway-Sant'Anna and Gardner-style staggered estimators
  - Test sensitivity to excluding same-province or neighboring cities
  - Separate private construction/manufacturing, SOE, and other sectors
  - Test wage-arrears and migrant-network mechanisms
  - Audit first-inspection dates against official CCDI notices
threats:
- type: endogenous-inspection-timing
  basis: reported
  condition: Central inspection timing is centrally selected and may correlate with corruption, political conflict, or local economic conditions.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - pre-trend and placebo tests
  - condition on provincial team arrival
  - compare alternative first-inspection definitions
- type: network-spillovers
  basis: reported
  condition: Inspections in one city raise strikes in same-province, nearby, or migrant-origin-connected cities, contaminating not-yet-treated comparisons.
  evidence_refs:
  - E1
  possible_diagnostics:
  - explicit province and distance exposure measures
  - exclude connected controls and estimate spillover effects separately
- type: strike-reporting-selection
  basis: inferred
  condition: The China Labour Bulletin map records visible strikes; inspection-related attention may change reporting or discovery even when underlying grievances do not change.
  evidence_refs:
  - E1
  possible_diagnostics:
  - compare grievance categories and scale
  - use alternative labor-dispute sources if available
  - test media-attention and social-media channels
- type: treatment-definition
  basis: reported
  condition: The distinction between high-profile, lower-profile, first any-rank, and later inspection events is essential; collapsing them changes the treatment.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - reproduce the inspection classification from the CID
  - audit city dates against official notices
empirical_requirements:
  contract_version: 1
  population: Workers and firms in Chinese city-level geographic units, with emphasis on private construction and manufacturing labor markets
  observation_unit: City-month
  geography_level: City and province
  time_start: 2011
  time_end: 2020
  minimum_frequency: monthly
  minimum_pre_periods: 12
  minimum_post_periods: 12
  required_fields:
  - monthly strike incident count
  - strike sector and grievance category
  - stable city and province identifiers
  - inspection date and city/province target
  - high-profile and paper-defined city-level inspection indicators
  - provincial CCDI team arrival date
  - neighboring-city and migrant-network measures for spillover work
  required_identifiers:
  - city_id
  - province_id
  - year_month
  - inspection_id
  - strike_id
  treatment_key:
  - first_high_profile_city_inspection_month
  - provincial_team_arrival_month
  - city_id
  treatment_source: >
    Corruption Investigation Dataset for inspection events and China Labour
    Bulletin Strike Map for strike incidents, joined to official CCDI inspection
    entry and feedback notices. The author manuscript describes the CID as 18,947
    public investigations from 2012 through January 2017 with city, month, official
    position, CCP rank, and reason fields; it reports the rank 1–6 high-profile
    threshold. It describes CLB strikes for 2011–2020 and uses China Judgements
    Online labor-dispute cases for supplementary outcomes. The raw CID/CLB files,
    the event-to-unit crosswalk, and replication code have not been independently
    audited here [E4].
  measurement_risks:
  - high-profile classification and first-city inspection dates
  - city boundary and identifier changes
  - under-reporting and media visibility in the strike map
  - the paper reports CLB coverage of only about 5–10% of all strikes, with coverage varying over time and censorship as a possible source of measurement error [E4]
  - central selection of inspection timing
  - spillover contamination of comparison cities
  - missing or inconsistent sector and grievance coding
design_profiles:
- id: city-inspection-strike-event-study
  label: First high-profile city inspection and labor strikes
  design_families:
  - staggered-did
  - event-study
  when_to_use: Use when city-month strike outcomes and inspection dates can be joined, and spillovers are modeled rather than ignored.
  outcome_domains:
  - labor strikes and protests
  requirements:
    population: Workers and firms in Chinese cities
    observation_unit: City-month
    geography_level: City and province
    time_start: 2011
    time_end: 2020
    minimum_frequency: monthly
    minimum_pre_periods: 12
    minimum_post_periods: 12
    required_fields:
    - strike incidents
    - first high-profile inspection date
    - city and province identifiers
    required_identifiers:
    - city_id
    - year_month
    treatment_key:
    - first_high_profile_city_inspection_month
evidence:
- id: E1
  source_type: paper
  citation: 'Chen, Huiyi. 2026. "Raising Grievances to the State: The Political Economic Effects of Anti-Corruption Crackdowns on Labor Activism in China." Journal of Development Economics 181: 103758. DOI: 10.1016/j.jdeveco.2026.103758.'
  url: https://doi.org/10.1016/j.jdeveco.2026.103758
  date: 2026
  supports:
  - identity.instrument
  - identity.implementation_regime
  - timeline.announcement
  - timeline.implementation_start
  - timeline.local_timing
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
  - design_applications.treatment_encoding
  - design_applications.comparison
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_source
  verification_status: reported
  access_level: abstract
  locator: 'Publisher page highlights, abstract, introduction, and indexed section excerpts; the full article and raw inspection/strike files require a separate access and replication audit.'
- id: E2
  source_type: implementation-document
  citation: 'Central Commission for Discipline Inspection. 2013. Central inspection-team entry and feedback notices for the first and second rounds of provincial inspections.'
  url: https://www.ccdi.gov.cn/special/zyxszt/2013dyl_zyxs/xsjz_dyl_zyxs/
  date: 2013
  supports:
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.implementation_start
  - timeline.local_timing
  - assignment.unit
  verification_status: verified
  access_level: official-document
  locator: 'CCDI 2013 inspection-entry index and linked provincial entry/feedback notices, including dated team arrivals and inspected provinces/units.'
- id: E3
  source_type: paper
  citation: 'Chen, Huiyi. 2025. "Raising Grievances to the State: The Political Economic Effects of Anti-Corruption Crackdowns on Labor Activism in China." SSRN Working Paper 5195218.'
  url: https://ssrn.com/abstract=5195218
  date: 2025
  supports:
  - assignment.treated
  - assignment.comparison_pool
  - design.identifying_variation
  - design.estimand
  - design_applications.treatment_encoding
  - design_applications.data_used
  verification_status: reported
  access_level: abstract
  locator: 'SSRN abstract and manuscript metadata; use as a working-paper crosswalk, not as independent proof of raw-data contents.'
- id: E4
  source_type: paper
  citation: >
    Chen, Huiyi. 2026. "Raising Grievances to the State: The Political Economic
    Effects of Anti-Corruption Crackdowns on Labor Activism in China." Author-hosted
    manuscript last updated February 2026; preceding the Journal of Development
    Economics article, DOI 10.1016/j.jdeveco.2026.103758.
  url: https://hui-yi-chen.com/files/draft_corrstrikes_feb2026.pdf
  date: '2026-02'
  supports:
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.local_timing
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
  - design.comparison_logic
  - design.assumptions
  - design.diagnostics
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_source
  - empirical_requirements.measurement_risks
  - design_applications.research_question
  - design_applications.population
  - design_applications.outcome
  - design_applications.data_used
  - design_applications.treatment_encoding
  - design_applications.comparison
  - design_applications.empirical_design
  - design_applications.assumptions
  - design_applications.threats_addressed
  verification_status: reported
  access_level: full-text
  locator: >
    Author page links this 74-page manuscript; its title page states "Last Updated:
    February 2026." Inspected pp. 3, 8–9, 12–14, 18–23, Table 3, and Appendix
    Table B6 for the event definition, rank threshold, unit composition, data
    sources, event cohorts, estimator, controls, and measurement limits. This is
    an author version, not the final publisher text; the raw CID/CLB files and
    crosswalk are not included in this record.
design_applications:
- paper: 'Raising Grievances to the State: The Political Economic Effects of Anti-Corruption Crackdowns on Labor Activism in China'
  doi: 10.1016/j.jdeveco.2026.103758
  journal: Journal of Development Economics
  year: 2026
  research_question: How does a high-profile central inspection change workers' expected returns to striking and the visibility of pre-existing grievances?
  population: >
    362 city-level geographic units observed monthly from 2011–2020: 333
    prefecture-level cities, four centrally administered municipalities, 24
    province-administered county-level units, and Laiwu (then a separate
    Shandong city), yielding 43,440 unit-month observations [E4]. These are
    geographic units, not a firm panel; the strike data do not identify employers.
  outcome: >
    Monthly incidents on the China Labour Bulletin Strike Map, with sector and
    grievance heterogeneity. The paper reports using China Judgements Online
    labor-dispute cases as supplementary outcomes [E4].
  data_used:
  - >
    Corruption Investigation Dataset (CID): the author manuscript describes
    18,947 public investigation records from 2012 through January 2017, with
    city, month, official position, CCP rank, and reason fields [E4].
  - >
    China Labour Bulletin Strike Map, used for strike outcomes in 2011–2020;
    the paper reports that it captures only about 5–10% of strikes, with
    coverage varying over time and censorship affecting reporting [E4].
  - >
    China Judgements Online labor-dispute cases, used as supplementary
    outcomes in the author manuscript [E4].
  - >
    Official CCDI inspection-entry and feedback notices for provincial team
    arrival and institutional cross-checking; these notices do not independently
    reproduce the paper's complete city-level CID classification [E2, E4].
  treatment_encoding: >
    The paper codes the first high-profile city-level investigation after a
    CCDI team arrives in the province, represented by monthly event-time
    indicators. In the February 2026 author manuscript, high-profile means an
    investigated official at CCP rank 1–6 on the paper's scale (rank 1 highest,
    rank 6 deputy-bureau-director level); lower-ranked cases are low-profile.
    This is the paper's coding threshold, not a verified official designation
    rule. The first any-rank city investigation is a separate event definition;
    later and low-profile inspections are not baseline treatment [E4].
  comparison: >
    Own pre-inspection months and cities not yet experiencing their first
    high-profile inspection, conditional on provincial team arrival. The author
    manuscript reports 234 exposed and 128 never-high-profile units; four units
    have no recorded city inspection after provincial team arrival [E4]. Same-
    province, neighboring, and migrant-origin-connected cities can be exposed
    through spillovers and are not automatically clean controls.
  empirical_design: >
    Monthly event study with city and month-year fixed effects, city-level
    controls, and standard errors clustered by city. The paper also reports
    Callaway–Sant'Anna estimates for a quarterly specification, Gardner-style
    estimates as a robustness check, and separate same-province, neighboring-
    city, and migrant-network spillover analyses [E4].
  assumptions:
  - Inspection timing and high-profile coding are measured consistently
  - Not-yet-treated comparisons remain informative after spillover controls
  - Strike-map reporting changes do not mechanically coincide with inspection publicity
  - The sparse and time-varying Strike Map captures changes in recorded incidents rather than the full incidence of strikes
  threats_addressed:
  - >
    Endogenous inspection timing through event-study pre-trends, placebo checks,
    and conditioning on provincial team arrival; the manuscript's reported
    diagnostics do not establish random timing [E4].
  - Network contamination through same-province, neighboring, and migrant-network analyses
  - Treatment-definition risk through high-profile versus low-profile distinctions
  - >
    Outcome under-coverage and time-varying reporting through supplementary
    labor-dispute outcomes and alternative specifications; the paper's 5–10%
    Strike Map coverage figure is itself a reported estimate, not an audited
    count of all strikes [E4].
  evidence_refs:
  - E1
  - E2
  - E3
  - E4
method_transfer: null
readiness_blockers:
- The paper and publisher excerpts identify the city-month design and data sources, but the raw Corruption Investigation Dataset, Strike Map extract, and code-to-field crosswalk have not yet been independently audited.
- The February 2026 author manuscript supplies the rank 1–6 high-profile threshold, but the exact CID-to-city roster, city-level event construction, and first-event dates have not been independently reconstructed. The CCDI archive verifies provincial team-entry context, not the full city-level CID crosswalk.
- The author manuscript was not compared line by line with the final publisher version, and the raw files, crosswalk, and replication code remain unaudited; retain its details as author-reported rather than as independently verified final-version facts.
- Inspection timing is centrally selected and the design has documented province, neighborhood, and migrant-network spillovers; the record does not call the campaign intrinsically exogenous.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

China's post-2012 anti-corruption campaign used central inspection teams that entered provinces and inspected party-state units on a staggered schedule. The CCDI's contemporary notices document dated team entry and feedback events [E2]. The February 2026 author manuscript then operationalizes a city-level labor-market exposure using the first high-profile investigation after provincial team arrival; it does not equate the national campaign launch with treatment for every city [E4, reported claim].

## What Changed

After a city's first coded high-profile inspection, the author manuscript reports a rise in recorded strikes, concentrated in private construction and manufacturing and associated with wage arrears [E4, reported claim]. Its interpretation is that inspections weakened firm–government ties or shifted government attention, making existing grievances more actionable; the design does not show that inspections created the underlying grievances [E4, reported claim]. Because the Strike Map captures only an estimated 5–10% of strikes and its coverage varies over time, the outcome is recorded activism, not a complete count of labor disputes [E4, reported claim].

## Implementation and Assignment

The treatment date is the first high-profile city-level investigation after a central team arrives in the relevant province. In the author manuscript, "high-profile" means an investigated official at CCP rank 1–6 on the paper's scale; rank 1 is highest and rank 6 is deputy-bureau-director level. That threshold is the paper's coding rule, not a separately verified CCDI rule [E4, reported claim]. It is also distinct from the paper's first-any-rank event used in another analysis. The manuscript reports 234 exposed and 128 never-high-profile geographic units, with four units lacking any recorded city inspection after provincial team arrival; reproducing those counts requires the CID-to-city crosswalk, which has not been audited. Later-treated units form part of the comparison pool, while same-province, neighboring, and migrant-origin networks can transmit exposure [E4]. CCDI notices ground provincial entry dates, not the paper's full city list or rank coding [E2].

## Why This Creates Empirical Variation

The application turns a visible administrative event into city-month event time. The author manuscript reports a monthly event study with city and month-year fixed effects, city controls, and city-clustered standard errors; it also reports a quarterly Callaway–Sant'Anna specification and Gardner-style robustness estimates [E4]. The design is useful for studying how local political protection and worker expectations change around inspections, but it does not make inspection timing random. Central selection, pre-existing corruption, local political conflict, and shifts in strike visibility may affect measured event timing or outcomes [E4; analytical inference].

## Identification Risks

The central risk is selection into inspection timing. An inspection in one city can also alter strikes elsewhere through provincial, geographic, or migrant networks, so “not yet inspected” is not necessarily untreated. A further limit is outcome measurement: the author manuscript reports that the Strike Map captures only about 5–10% of strikes and that coverage varies over time, in part in a censorship-sensitive information environment [E4]. Publicity around an inspection could therefore change discovery or reporting as well as worker behavior [analytical inference]. A researcher must preserve the first-high-profile distinction and audit the raw inspection and strike files before treating the published coefficient as reproducible. The 362 units are geographic aggregates rather than firm-level observations, so employer-specific effects cannot be recovered from this outcome file without an additional linkable source [E4].

## Data Requirements

The reported sample contains 362 geographic units—333 prefecture-level cities, four centrally administered municipalities, 24 province-administered county-level units, and Laiwu—over 2011–2020, or 43,440 unit-months [E4]. The minimum data contract is a city-month panel with stable unit and province identifiers, strike counts and categories, investigation dates and official rank, and the provincial team-arrival date. Reproducing the application requires the CID (described in the author manuscript as 18,947 public investigations from 2012 through January 2017), the CLB Strike Map, and the code or crosswalk that reproduces the rank threshold, city-level event, and first-event dates. The manuscript also uses China Judgements Online labor-dispute cases as supplementary outcomes [E4]. Network analyses need geographic neighbors, same-province exposure, and migrant-origin (Laoxiang) links. The CLB data do not identify employers, so a firm-level treatment-outcome join needs another source and cannot be assumed available from this design.

## Evidence Notes

E1 is the final publisher record and abstract; it establishes the paper's identity and broad reported design, but not the detailed rank threshold, city composition, or estimator. E2 verifies dated provincial team-entry and feedback notices; it does not establish the paper's city roster or high-profile coding. E3 is the 2025 working-paper metadata route. E4 is the author's 74-page manuscript, last updated February 2026, inspected at pp. 3, 8–9, 12–14, 18–23, Table 3, and Appendix Table B6. It supplies the detailed sample, event definition, data boundaries, estimator, and paper-reported diagnostics, but it has not been matched line by line to the publisher's final article, and its raw CID/CLB files, event crosswalk, and replication code were not audited. Thus the precise details remain attributed to the author manuscript rather than independently verified institutional facts.
