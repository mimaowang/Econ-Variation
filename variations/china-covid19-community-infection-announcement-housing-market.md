---
schema_version: 2
id: china-covid19-community-infection-announcement-housing-market
name: China COVID-19 Community Infection Announcements (January-March 2020) as a Housing-Market Shock
aliases:
- Liu-Tang RSUE 2021 epidemic shocks housing price responses
- 中国新冠疫情 确诊小区公告 房价冲击
- Tencent Watchtower infected communities DID housing
status: grounded
provenance:
  task_id: task-4b6f2f12b6e5
scope:
  country: China
  regions:
  - 34 major Chinese cities covered by the Fang.com community panel (city list not enumerated in the inspected text; sample infections concentrated in February 2020)
  domains:
  - health
  - infrastructure-urban
  - housing-markets
  - risk-perception
  variation_type: event-shock
  knowledge_role: global-china-variation
  china_relevance: >
    A global pandemic creates highly localized exposure inside Chinese cities:
    from January to March 2020, local health commissions publicly announced
    the residential communities (小区) of confirmed COVID-19 cases, so each
    named community received a salient, dated health-risk shock while nearby
    uninfected communities did not. Liu and Tang (2021, Regional Science and
    Urban Economics) exploit this community-level announcement variation
    across 34 major Chinese cities, matching infected communities to nearby
    uninfected ones by geographic distance and estimating hedonic
    difference-in-differences and event-study responses of secondhand housing
    prices, transaction volumes, and rents. The regional/urban content is the
    within-city spatial contrast between infected and neighboring uninfected
    communities, not a city-level lockdown comparison [E1, E2].
identity:
  instrument: >
    The public announcement that a residential community contains at least
    one confirmed COVID-19 case. Local health commissions and Centers for
    Disease Control and Prevention disclosed case counts, movement
    trajectories, and residential locations of infected persons through press
    conferences and official websites beginning with the National Health
    Commission's daily reporting on 2020-01-11; the paper obtained community
    names, addresses, cities, and infection dates (January-March 2020) from
    the Tencent Watchtower infected-communities query platform, which
    aggregated these official announcements, and mapping apps such as Baidu
    Maps and Tencent Maps mirrored the same information [E1]. The instrument
    is the announcement event itself, so treatment timing is the date the
    community became publicly known as infected, which is close to but not
    identical to the underlying infection onset [E1; analytical inference on
    the onset-announcement gap].
  authority: >
    No single authority assigns treatment. Case confirmation and disclosure
    were produced by local health commissions and CDCs under the National
    Health Commission's reporting framework (daily national reporting from
    2020-01-11; home-isolation guidance issued 2020-02-05); the Tencent
    Watchtower platform republished the community-level announcements [E1].
    The shock construction (community infection indicator, buffer definition,
    matching design) is the authors'.
  legal_identifiers:
  - 'Liu, Yanan, and Yugang Tang. 2021. "Epidemic shocks and housing price responses: Evidence from China''s urban residential communities." Regional Science and Urban Economics 89: 103695. DOI: 10.1016/j.regsciurbeco.2021.103695 (epub 2021-05-27)'
  - National Health Commission of China daily outbreak reporting beginning 2020-01-11; "Guidelines for Home Isolation Medical Observation" issued 2020-02-05 [E1, paper-reported institutional background]
  - Tencent Watchtower (腾讯) "infected communities" query platform, community names and infection dates, January-March 2020 [E3, reported]
  - 'National Health Commission Announcement No. 1 of 2020 (2020-01-20): statutory Class B classification with Class A measures [E4]'
  - 'Joint Prevention and Control Mechanism community-prevention notice 肺炎机制发〔2020〕5号 (2020-01-24): community case definition, daily community epidemic information disclosure, close-contact observation [E5]'
  implementation_regime: >
    Stochastic infection realizations disclosed through a disclosure regime,
    not a policy rollout. Once a community was identified as infected, close
    contacts were placed under home or centralized medical observation and
    affected sites disinfected under the 2020-01-24 community-prevention
    notice [E5, verified]; the paper reports that infected communities were
    immediately quarantined and observed for two weeks or more [E1, reported
    claim about the intervention regime]. Infection announcements in the
    sample concentrate in a short window: among the 652 matched infected
    communities, 55 outbreaks occurred in January, 593 in February, and 4 in
    March 2020 [E1]. The epidemic was effectively contained in China by March
    2020, and Wuhan ended its blockade on 2020-04-08 [E1, paper-reported
    background]. Because announcement and quarantine coincide, the treatment
    bundles infection-risk information with the immediate public intervention
    [analytical inference].
  assignment_mechanism: >
    Whether a community is publicly announced as having a confirmed case.
    Communities with active housing markets, more buildings, and more
    households were mechanically more likely to host an infected person, so
    infection is not random across communities; the paper mitigates this by
    restricting the comparison to uninfected communities within a 750 m
    buffer of each infected community (nearest-neighbor and radius matching),
    with community fixed effects absorbing time-invariant differences [E1].
    Identification therefore compares an infected community to its immediate
    neighbors before and after the announcement month, not to the citywide
    pool. No exogeneity claim beyond these identifying assumptions is made or
    warranted.
  parent: null
  related_variations: []
timeline:
  announcement: '2020-01'
  effective: null
  implementation_start: 2020-01
  implementation_end: 2020-03
  local_timing: >
    Community infection dates in the estimating sample run from January to
    March 2020 (55, 593, and 4 outbreaks by month among 652 matched infected
    communities) [E1]. The outcome panel is monthly, May 2019 to June 2020,
    giving roughly eight pre-shock months for the February outbreak mass
    [E1]. Because secondhand transaction registration on Fang.com records the
    brokerage-contract signing date and closings lag by roughly one month,
    the paper sets the price and transaction-volume post period to begin one
    month before the announcement month (period -1), while the rental post
    period begins in the announcement month (period 0); the event study uses
    period -2 as the benchmark [E1].
  anticipation: >
    Buyer default or renegotiation between brokerage-contract signing and
    closing shifts part of the measured effect one month earlier than the
    announcement, which the paper explicitly builds into the treatment
    timing; broader anticipatory avoidance before any local announcement is
    bounded by the rapid, localized disclosure regime but is not separately
    tested [E1; the last clause is analytical inference].
  last_verified: '2026-08-15'
assignment:
  unit: >
    Community-month: residential communities (小区, enclosed residential
    complexes under unified property management) observed monthly from May
    2019 to June 2020 across 34 major cities. The price/rent analysis uses an
    unbalanced panel of 10,437 matched communities (652 infected, 9,785
    uninfected; 130,807 community-month observations); the transaction-volume
    analysis uses the same communities balanced to 146,118 observations with
    zero-transaction months coded as 0 [E1].
  treated: >
    The 652 communities with at least one publicly announced confirmed case
    between January and March 2020 that have nonzero total transactions over
    the sample period (725 matched infected communities before the
    zero-transaction exclusion) [E1].
  comparison_pool: >
    Uninfected communities matched within a 750 m buffer centered on each
    infected community (9,785 in the main sample); the paper implements
    one-to-one, one-to-two, and one-to-three nearest-neighbor matching and
    radius matching at 350 m, 450 m, and 550 m, without duplicate matches
    [E1].
  rule: >
    Assign Infected_i = 1 to any community ever announced as infected;
    define the buffer-time post indicator Post_bt = 1 from one month before
    the announcement month for prices and volumes (registration-lag
    assumption) and from the announcement month for rents; estimate
    Y_it = alpha + beta * Infected_i * Post_bt with community fixed effects
    and either buffer-specific linear time trends plus month fixed effects
    (Model 1) or buffer-by-month fixed effects (Model 2); event study (Model
    3) interacts Infected_i with event-time dummies m in [-8, 4], benchmark
    -2, with multiple shock months normalized; standard errors clustered by
    buffer, with a community-specific AR(1) error process [E1].
  intensity: >
    Binary exposure. Reported average effects: secondhand transaction prices
    about -1.3 percent (range -1.1 to -2.0 percent across matching
    specifications); monthly transaction volumes about -0.22 to -0.27 units;
    guided rents of 3-bedroom homes about -1.4 to -1.7 percent with no
    significant effect on 1- or 2-bedroom rents; all effects short-lived,
    returning to trend within about three to four months (prices, volumes)
    or two periods (rents) [E1, E2].
  exemptions:
  - Infected communities with zero total transactions over May 2019-June 2020 are excluded from the price, rent, and volume analyses (725 matched drop to 652)
  - Communities with no transaction in a given month enter the volume panel with volume 0 but contribute no price observation that month (unbalanced price panel)
  - Communities outside the 750 m buffer of any infected community are outside the matched analysis sample entirely
  compliance: >
    Exposure is the official announcement record, measured rather than
    chosen, but announcement probability rises with community size and market
    activity; the descriptive statistics show infected communities have
    significantly more buildings and households, which motivates the
    within-buffer matched design and community fixed effects rather than a
    raw citywide comparison [E1]. Whether the Tencent Watchtower aggregation
    captured all announced communities is not independently verified [E3,
    reported].
  exposure_construction: >
    Author construction: infected-community names, addresses, cities, and
    infection dates from the Tencent Watchtower infected-communities query
    platform (itself aggregating local health commission and CDC disclosures),
    name- and address-matched to Fang.com communities and spatially matched
    by latitude and longitude; community physical characteristics (year
    built, landscaping ratio, floor area ratio, buildings, households) and
    monthly secondhand prices, volumes, and guided rents from Fang.com; city
    GRP per capita and employment share from the China City Statistical
    Yearbook (2019) [E1, E3].
  required_identifiers:
  - community identity (name, address, latitude/longitude) stable across May 2019-June 2020 for the Fang.com-to-announcement match
  - community infection date (announcement month) from the disclosure platform
  - buffer membership linking each infected community to its matched uninfected communities
  - city identifier for the China City Statistical Yearbook (2019) city features
  spillovers: >
    Quarantine of infected communities was intended to contain spread to
    adjacent neighborhoods [E1, reported claim]. The paper tests spillovers
    by treating the nearest uninfected community as a fake treated unit and
    other buffer communities as controls; coefficients are insignificant,
    interpreted as no spillover discount onto immediate neighbors [E1].
    City-level common shocks are absorbed by month fixed effects in levels
    but not in any differential city exposure [analytical inference].
research_compatibility:
  outcome_domains:
  - housing prices and willingness to pay to avoid localized health risk
  - housing transaction volumes and market liquidity after a localized shock
  - rental prices by unit size (family versus non-family demand)
  - negative urban externalities and public-intervention recovery dynamics
  affected_populations:
  - Homebuyers, sellers, and tenants in 652 infected and 9,785 matched uninfected communities across 34 major cities, May 2019-June 2020
  - Households with children or higher ability to pay (3-bedroom rental demand) as the more risk-averse margin
  mechanism_channels:
  - health-risk aversion reducing demand for housing in announced-infected communities
  - immediate community closure and quarantine containing the externality and supporting rapid price recovery
  - transaction-registration lag moving part of the measured price and volume response into the pre-announcement month
  best_for:
  - Designs that need a dated, geocoded, within-city health-risk shock at the residential-community level in early 2020 China
  - Hedonic willingness-to-pay estimates for avoidance of infectious-disease risk, with a matched within-buffer comparison
  - Event-study analyses of short-run housing-market resilience and public-intervention recovery
  not_good_for:
  - Separating the pure infection-information effect from the coincident community closure and quarantine; announcement and intervention are bundled in treatment
  - Post-2020 epidemic episodes or other countries without a comparable community-level disclosure regime
  - Designs requiring random assignment of infection; infection risk correlates with community size and market activity, so the design depends on the matched buffer and fixed effects
  - City-level or aggregate pandemic questions; identifying variation is within city, within buffer
design:
  claim_type: reduced-form
  affordances:
  - Dated community-level infection announcements (January-March 2020) with geocoded locations, giving sharp event-time and spatial variation within cities
  - A 14-month community panel (May 2019-June 2020) of transaction prices, volumes, and guided rents from one platform, allowing matched event studies with about eight pre-shock months
  - Two complementary matching schemes (nearest-neighbor and radius within 750 m buffers) plus buffer-by-month fixed effects that relax the linear-trend assumption
  - Placebo, spillover, and alternative-similarity robustness designs built from the same spatial frame
  candidate_designs:
  - Hedonic DID of community log prices on Infected x Post with community fixed effects and buffer-by-month fixed effects, buffer-clustered errors
  - Event study over event months -8 to +4 (benchmark -2) for prices, volumes, and rents, testing parallel pre-trends and recovery dynamics
  - Rental-market DID by unit size (1/2/3-bedroom guided rents) with post period starting in the announcement month
  - Placebo design assigning fake infection to uninfected buffer communities, and spillover design treating the nearest uninfected community as fake treated
  identifying_variation: >
    Within-buffer, within-community changes around the announcement month
    between an infected community and its matched uninfected neighbors,
    conditional on community fixed effects and either buffer linear trends or
    buffer-by-month fixed effects; cross-sectional support comes from the
    staggered January-March announcement timing and the spatial dispersion of
    infected communities across 34 cities [E1].
  primary_strategy: >
    Hedonic difference-in-differences (paper Models 1-2) with an event-study
    dynamic specification (Model 3). Outcomes are log monthly average
    transaction price, monthly transaction volume, and log monthly guided
    rent by bedroom count. Treatment is the time-invariant infection
    indicator interacted with the buffer-time post indicator; errors follow a
    community-specific AR(1) process with buffer-clustered robust standard
    errors [E1].
  estimand: >
    The reduced-form difference in post-announcement housing prices,
    transaction volumes, or rents between an infected community and its
    matched uninfected neighbors, interpretable as homebuyers' willingness to
    pay (about 1.3 percent of price) to avoid the localized health risk
    bundled with the immediate public intervention [E1; the bundling caveat
    is analytical inference].
  treatment_variable: >
    Infected_i x Post_bt: the ever-infected community indicator times the
    post indicator, which turns on one month before the announcement month
    for prices and volumes (brokerage-contract registration lag) and in the
    announcement month for rents [E1].
  comparison_logic: >
    Matched uninfected communities inside the same 750 m buffer share the
    local environment; buffer-by-month fixed effects absorb any shock common
    to a buffer in a month, so identification comes from the infected
    community deviating from its immediate neighbors after its announcement.
    The comparison fails if infection announcements correlate with
    time-varying within-buffer shocks specific to the infected community, if
    infected and matched communities differ on unobserved trends, or if the
    registration-lag timing assumption is wrong [E1; failure conditions are
    analytical inference].
  estimation_notes: >
    Main price estimates: -0.0131 to -0.0142 under radius matching with
    buffer-by-month fixed effects, about -0.011 to -0.020 across all matching
    schemes (Table 2); volumes about -0.24 units per month (Table 7); rents
    insignificant for 1- and 2-bedroom units and about -0.014 to -0.017 for
    3-bedroom units (Table 8). Event studies show declines concentrated in
    the first three to four months with return to trend. Heterogeneity:
    larger price declines in high-density communities (top-quartile
    households per community), muted responses in communities with strong
    education amenities, and larger declines in lower-GRP-per-capita cities.
    Placebo tests with fake infected communities inside the buffers are null
    (Table 4); the nearest-uninfected spillover test is null (Appendix Table
    4); matching on October 2019 price proximity and unconstrained one-to-one
    matching leave results similar (Tables 5-6) [E1].
  assumptions:
  - Conditional on community fixed effects and buffer-specific time controls, infection announcement timing is orthogonal to unobserved within-buffer price trends (supported by flat pre-trends in the event studies)
  - The 750 m buffer and the matching scheme make treated and control communities comparable on observable and unobservable local characteristics
  - The one-month registration lag correctly re-times the price and volume treatment window
  - Fang.com community-month prices reflect actual transaction prices, and platform coverage does not change differentially around announcements
  diagnostics:
  - Event-study pre-trend inspection over months -8 to -3 relative to benchmark -2
  - Placebo test assigning infection to a randomly chosen uninfected community within each buffer (null)
  - Spillover test with the nearest uninfected community as fake treated (null)
  - Alternative neighborhood-similarity definition using October 2019 historical prices, and one-to-one matching without the 750 m constraint
  - Matching-scheme robustness across 1:1/1:2/1:3 nearest-neighbor and 350/450/550 m radius definitions
threats:
- type: nonrandom_infection_selection
  basis: reported
  condition: Communities with more buildings, more households, and more active housing markets were more likely to host an announced case; the paper mitigates this with within-buffer matching and community fixed effects, but selection on time-varying unobservables (for example within-buffer differences in foot traffic) remains possible.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Covariate-balance checks within buffers beyond the reported physical characteristics
  - Sensitivity to matching on pre-shock price levels (partially addressed via the October 2019 price-proximity matching)
- type: treatment_bundles_infection_and_intervention
  basis: inferred
  condition: Announcement, community closure, and quarantine coincide (the community-prevention notice mandates close-contact observation and disinfection for case-communities), so the estimand bundles health-risk information with the public intervention; the paper interprets interventions as a recovery mechanism, not as a separable treatment component.
  evidence_refs:
  - E1
  - E5
  possible_diagnostics:
  - Compare effects across communities or cities with different intervention intensity where measurable
  - Use later re-opening dates to trace whether recovery tracks quarantine end
- type: announcement_timing_measurement
  basis: reported
  condition: Treatment timing is the public announcement month, not infection onset; the paper handles the registration lag by starting the post period one month early for prices and volumes, but misdated or delayed disclosures would blur event time.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Re-time treatment using alternative lag assumptions and check stability
  - Cross-check announcement dates against an independent disclosure archive
- type: platform_coverage_and_price_measurement
  basis: inferred
  condition: Outcomes come from one transaction platform (Fang.com); community-month average prices are missing in zero-transaction months and thin-market communities may have unrepresentative average prices; the record does not audit platform coverage across the 34 cities.
  evidence_refs:
  - E1
  - E3
  possible_diagnostics:
  - Replicate with a second listing or registration data source
  - Weight or trim communities by transaction density
- type: unenumerated_city_sample
  basis: inferred
  condition: The inspected text states 34 major cities but does not enumerate them, so city composition (including whether Wuhan enters the estimating sample) and city-level confounds such as differential lockdown intensity cannot be verified from the record.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Obtain the appendix city table from the published article or the authors
  - Re-estimate excluding epicenter cities if they enter the sample
empirical_requirements:
  contract_version: 1
  population: Residential communities (小区) with active secondhand markets in 34 major Chinese cities, May 2019-June 2020
  observation_unit: community-month
  geography_level: community, matched within 750 m buffers around infected communities
  time_start: 2019-05
  time_end: 2020-06
  minimum_frequency: monthly
  minimum_pre_periods: 7
  minimum_post_periods: 3
  required_fields:
  - monthly average secondhand transaction price per community
  - monthly transaction volume per community (zero-transaction months retained as 0 for the volume design)
  - monthly guided rental price by bedroom count (1/2/3-bedroom)
  - community characteristics (year built, landscaping ratio, floor area ratio, number of buildings, number of households)
  - community infection status and announcement month (January-March 2020)
  - city GRP per capita and urban employment share for city-level heterogeneity
  required_identifiers:
  - community_id
  - buffer_id
  - city_id
  - year_month
  treatment_key:
  - community_id
  treatment_source: >
    Community infection announcements (name, address, city, infection date,
    January-March 2020) from the Tencent Watchtower infected-communities
    query platform aggregating local health commission and CDC disclosures,
    matched to Fang.com communities by name, address, and latitude/longitude
    [E1, E3].
  measurement_risks:
  - Tencent Watchtower's historical community lists are not independently re-queried in this record, so completeness of the infected-community roster is unverified
  - announcement month proxies infection timing; disclosure delays vary across cities
  - community-month average prices are undefined in zero-transaction months and noisy in thin markets
  - the 34-city list and the Fang.com coverage rule are not enumerated in the inspected text
design_profiles:
- id: rental-market-design
  label: Rental-market response by unit size
  design_families:
  - hedonic DID
  - event study
  when_to_use: Use when the outcome is guided rents rather than transaction prices; the post period starts in the announcement month (no registration lag) and the identifying contrast separates family-sized (3-bedroom) from 1- and 2-bedroom demand.
  outcome_domains:
  - guided rental prices by bedroom count
  requirements:
    population: Communities with rental listings in the 34 cities, May 2019-June 2020
    observation_unit: community-month
    geography_level: community within 750 m buffers
    time_start: 2019-05
    time_end: 2020-06
    minimum_frequency: monthly
    minimum_pre_periods: 7
    minimum_post_periods: 2
    required_fields:
    - monthly guided rental price for 1-, 2-, and 3-bedroom homes per community
    - community infection status and announcement month
    required_identifiers:
    - community_id
    - buffer_id
    - year_month
    treatment_key:
    - community_id
evidence:
- id: E1
  source_type: paper
  citation: 'Liu, Yanan, and Yugang Tang. 2021. "Epidemic shocks and housing price responses: Evidence from China''s urban residential communities." Regional Science and Urban Economics 89: 103695. DOI: 10.1016/j.regsciurbeco.2021.103695 (open PMC mirror, PMC9754793).'
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9754793/
  date: 2021
  supports:
  - identity.instrument
  - identity.authority
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.announcement
  - timeline.implementation_start
  - timeline.implementation_end
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
  - design.assumptions
  - design.diagnostics
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.geography_level
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_source
  - design_applications.paper
  - design_applications.research_question
  - design_applications.population
  - design_applications.outcome
  - design_applications.data_used
  - design_applications.treatment_encoding
  - design_applications.comparison
  - design_applications.empirical_design
  - design_applications.assumptions
  - design_applications.threats_addressed
  verification_status: verified
  access_level: full-text
  locator: >
    PMC9754793 full text fetched and read 2026-08-15 (HTML and Europe PMC
    full-text XML): Abstract; Section 1 (announcement-based DID motivation,
    Fang.com panel of 34 cities, May 2019-June 2020); Section 2.1 (NHC daily
    reporting from 2020-01-11, Wuhan transport suspension 2020-01-23,
    home-isolation guidelines 2020-02-05, containment by March 2020, Wuhan
    blockade end 2020-04-08); Section 2.2 (theory, quarantine of infected
    communities for two weeks or more); Section 3.1 (community definition;
    Fang.com monthly prices, rents, volumes, characteristics; Tencent
    Watchtower infection dates January-March 2020; China City Statistical
    Yearbook 2019 city features; brokerage-contract registration lag and the
    period -1 treatment timing for prices/volumes versus period 0 for rents);
    Section 3.2 (750 m buffer, 725 matched infected communities, exclusion of
    zero-transaction infected communities leaving 652 infected and 9,785
    uninfected, 55/593/4 outbreaks by month, 130,807 and 146,118
    observations); Section 3.3 (Table 1 descriptive differences); Section 3.4
    (Models 1-3, buffer trends, buffer-by-month fixed effects, event window
    -8 to +4, benchmark -2, AR(1) errors, buffer clustering); Section 4
    (Tables 2-6: main -1.3 percent price effect, heterogeneity by density,
    income, city GRP, education amenities, placebo and spillover tests,
    October 2019 price-proximity and unconstrained matching robustness);
    Section 5 (Tables 7-8: volume effect about -0.24, 3-bedroom rent effect,
    null 1- and 2-bedroom rents). Establishes the design, data construction,
    and reported results; it does not independently verify Fang.com or
    Tencent Watchtower data, and the 34-city list is not enumerated in the
    inspected text.
- id: E2
  source_type: paper
  citation: 'PubMed record PMID 36540690 for Liu and Tang (2021), Regional Science and Urban Economics 89: 103695 (bibliographic record, official abstract, JEL R21, R28, I18, H41; epub 2021-05-27).'
  url: https://doi.org/10.1016/j.regsciurbeco.2021.103695
  date: 2021
  supports:
  - identity.legal_identifiers
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
  - assignment.intensity
  verification_status: verified
  access_level: abstract
  locator: >
    PubMed record (PMID 36540690) and the journal abstract page read
    2026-08-15: confirms authorship (Yanan Liu, Yugang
    Tang), journal, volume 89, article 103695, DOI
    10.1016/j.regsciurbeco.2021.103695, epub date 2021-05-27, keywords, JEL
    classification, and the official abstract reporting the approximately
    1.3 percent infected-community price discount, the heterogeneity, the
    short-lived declines in prices, volumes, and rents, and the public-
    intervention recovery interpretation. Establishes publication identity
    and headline results; design details rest on E1.
- id: E3
  source_type: paper
  citation: 'Tencent Watchtower (腾讯) infected-communities query platform and the local health commission / CDC disclosure regime it aggregated, as described in Liu and Tang (2021) Sections 2.1 and 3.1.'
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9754793/
  date: 2020
  supports:
  - identity.instrument
  - assignment.compliance
  - assignment.exposure_construction
  - empirical_requirements.treatment_source
  verification_status: reported
  access_level: full-text
  locator: >
    The paper's data section states that infected-community names, addresses,
    cities, and infection dates (January-March 2020) were obtained from the
    Tencent Watchtower infected-communities query platform, which republished
    local health commission and CDC announcements, and that Baidu Maps and
    Tencent Maps maintained similar infected-community maps. The platform's
    historical lists were not independently re-queried for this record
    (2026-08-15), so roster completeness and per-community announcement dates
    remain paper-reported claims.
- id: E4
  source_type: policy-document
  citation: '国家卫生健康委员会 (National Health Commission of China). 2020-01-20. 中华人民共和国国家卫生健康委员会公告 2020年第1号 (NHC Announcement No. 1 of 2020): classifying pneumonia caused by the novel coronavirus as a Class B statutory infectious disease under the Law on the Prevention and Treatment of Infectious Diseases, with Class A prevention and control measures.'
  url: https://www.nhc.gov.cn/jkj/s7916/202001/44a3b8245e8049d2837a4f27529cd386.shtml
  date: '2020-01-20'
  supports:
  - identity.authority
  - identity.legal_identifiers
  - timeline.announcement
  verification_status: verified
  access_level: official-document
  locator: >
    NHC website announcement page fetched and read 2026-08-15: Announcement
    No. 1 of 2020, dated 2020-01-20 and approved by the State Council,
    classifies novel-coronavirus pneumonia as a Class B statutory infectious
    disease with Class A prevention and control measures and as a
    quarantinable disease under the Frontier Health and Quarantine Law; the
    attached interpretation states that governments, health authorities, and
    medical institutions may lawfully isolate patients and place close
    contacts under isolated medical observation. Establishes the statutory
    reporting-and-control regime underlying community-level case disclosure
    and quarantine from late January 2020; it does not itself mandate
    publication of infected-community lists.
- id: E5
  source_type: policy-document
  citation: '应对新型冠状病毒感染的肺炎疫情联防联控工作机制 (Joint Prevention and Control Mechanism). 2020-01-24. 关于加强新型冠状病毒感染的肺炎疫情社区防控工作的通知 (肺炎机制发〔2020〕5号, Notice on strengthening community-level prevention and control of the novel-coronavirus pneumonia epidemic), with the attached 新型冠状病毒感染的肺炎疫情社区防控工作方案（试行).'
  url: http://www.gov.cn/zhengce/zhengceku/2020-01/26/content_5472235.htm
  date: '2020-01-24'
  supports:
  - identity.authority
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.rule
  - assignment.compliance
  verification_status: verified
  access_level: official-document
  locator: >
    Full text of 肺炎机制发〔2020〕5号 inspected 2026-08-15 via the
    waizi.org.cn verbatim mirror (https://www.waizi.org.cn/doc/76184.html);
    the canonical gov.cn URL cited above returned no renderable content on
    that date, and the same text appears in a Guiyang municipal government
    republication. The notice, issued 2020-01-24 by the Joint Prevention
    and Control Mechanism, orders grid-style community management; defines
    "社区出现病例" as one confirmed case among community residents;
    requires daily publication of local and community epidemic information
    (每日发布本地及本社区疫情信息); and prescribes, for communities with a
    case, close-contact tracing with home or centralized medical observation
    and disinfection, escalating to area lockdown for community-transmission
    areas. Establishes the official definition of a case-community, the
    mandated community-level disclosure practice, and the quarantine measures
    bundled with an announcement; it does not verify the paper's sample,
    dates, or matched design, which rest on E1.
design_applications:
- paper: 'Epidemic shocks and housing price responses: Evidence from China''s urban residential communities'
  doi: 10.1016/j.regsciurbeco.2021.103695
  journal: Regional Science and Urban Economics
  year: 2021
  research_question: How do urban housing prices, transaction volumes, and rents respond to a publicly announced COVID-19 infection in a residential community, how heterogeneous and persistent are the responses, and what do they imply about willingness to pay to avoid health risk?
  population: 652 infected and 9,785 matched uninfected communities (750 m buffers) in 34 major Chinese cities, monthly May 2019-June 2020; up to 146,118 community-month observations in the balanced volume panel
  outcome: Log monthly average secondhand transaction price, monthly transaction volume, and log monthly guided rents by bedroom count at the community level
  data_used:
  - Fang.com community-month secondhand transaction prices, volumes, guided rents, and community physical characteristics, 34 cities, May 2019-June 2020
  - 'Tencent Watchtower infected-communities platform: community names, addresses, and infection dates, January-March 2020'
  - 'China City Statistical Yearbook (2019): city GRP per capita and urban employment share'
  treatment_encoding: Time-invariant ever-infected community indicator interacted with a buffer-time post indicator beginning one month before the announcement month (prices, volumes) or in the announcement month (rents); community fixed effects with buffer linear trends or buffer-by-month fixed effects; buffer-clustered AR(1) errors
  comparison: Matched uninfected communities within the 750 m buffer (nearest-neighbor 1:1/1:2/1:3 and radius 350/450/550 m); event study over event months -8 to +4 with benchmark -2
  empirical_design: Hedonic difference-in-differences with spatial matching and an event-study dynamic specification; interpreted as a reduced-form willingness-to-pay estimate for avoiding localized infection risk
  assumptions:
  - Parallel pre-trends between infected and matched uninfected communities within buffers (inspected in event studies)
  - The matched buffer design controls for the nonrandom selection of infected communities on size and market activity
  - The one-month registration lag correctly times the price and volume response
  threats_addressed:
  - Spatial pretrends via placebo assignment of infection to uninfected buffer communities
  - Spillovers onto nearest neighbors via the fake-treated nearest-uninfected test
  - Matching-similarity sensitivity via historical (October 2019) price-proximity matching and unconstrained one-to-one matching
  - Functional-form sensitivity of local trends via buffer-by-month fixed effects
  evidence_refs:
  - E1
  - E2
  - E3
method_transfer: null
readiness_blockers:
- The 34-city list is not enumerated in the inspected full text, so city composition (including any Wuhan presence) and city-level lockdown-intensity confounds are unverified; obtain the published appendix city table before reusing the design across cities.
- The Tencent Watchtower historical community rosters and exact announcement dates were not independently re-queried; treatment dates remain paper-reported.
- Treatment bundles the infection announcement with the coincident community closure and quarantine; the record does not support a pure information-effect interpretation without additional institutional timing.
- Fang.com platform coverage, listing-to-transaction mapping, and thin-market price construction are not audited; replication with a second data source is the natural next step.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Chinese urban housing is organized around the residential community (小区):
a spatially contiguous, usually walled complex managed by a single property
agent [E1]. When COVID-19 emerged in December 2019, the National Health
Commission began daily national reporting on 2020-01-11, and local health
commissions and CDCs disclosed case counts, movement trajectories, and the
residential locations of confirmed cases through press conferences and
official websites; the 2020-01-24 community-prevention notice defined a
community with a case (社区出现病例) as one with a single confirmed case
among its residents and required daily publication of local and community
epidemic information [E4, E5]. Platforms such as Tencent Watchtower, Baidu
Maps, and Tencent Maps aggregated these disclosures into queryable
infected-community lists [E1, E3]. Once a community was identified as
infected, close contacts were traced into home or centralized medical
observation and affected sites were disinfected [E5]; the paper reports
that infected communities were immediately quarantined and observed for two
weeks or more [E1, reported claim]. The epidemic was effectively contained in China by March 2020, and
Wuhan's blockade ended on 2020-04-08 [E1, paper-reported background].

## What Changed

Nothing in housing policy changed. What changed was information and risk:
between January and March 2020, a named set of communities became publicly
known as hosting confirmed cases, creating a dated, geocoded health-risk
shock at the community level while neighboring communities remained
uninfected [E1]. The canonical boundary of this record is that announcement
variation as used by Liu and Tang (2021): 652 matched infected communities
across 34 major cities, compared with uninfected communities inside 750 m
buffers over a May 2019-June 2020 monthly panel [E1, E2]. Related but
distinct objects - city-level lockdown and mobility-restriction variation,
aggregate national case-count shocks, and the Fukushima risk-perception
land-market record - are outside this boundary and must not be merged into
it [analytical inference].

## Implementation and Assignment

A community is treated once any confirmed case among its residents is
publicly announced; the infection dates in the estimating sample concentrate
in February 2020 (593 of 652; 55 in January, 4 in March) [E1]. Because
secondhand transactions are registered at brokerage-contract signing while
closing takes roughly a month, the paper re-times the price and volume post
period to begin one month before the announcement month; rental contracts
complete quickly, so rents are treated from the announcement month [E1].
The comparison is deliberately local: each infected community is matched
only to uninfected communities within 750 m, under nearest-neighbor or
radius matching, and specifications use community fixed effects with either
buffer-specific linear trends or buffer-by-month fixed effects [E1].

## Why This Creates Empirical Variation

The disclosure regime made infection status salient, dated, and geocoded, so
buyers and tenants could and did react to a specific community's risk rather
than to a diffuse citywide threat [E1]. The staggered January-March timing
and the spatial dispersion of infected communities generate event-time
variation within cities, and the 14-month panel supplies about eight
pre-shock months for the February mass [E1]. The reported average response
is a price discount of about 1.3 percent in infected communities, a volume
drop of about 0.24 units per month, and a 3-bedroom rent decline of about
1.4-1.7 percent, all returning to trend within a few months [E1, E2].

## Identification Risks

Infection is not randomly assigned: larger, denser, more market-active
communities were more likely to host a case, so the design leans on the
matched buffer, community fixed effects, and flat event-study pre-trends
rather than on any claim of exogeneity [E1]. Treatment timing is the
announcement month, not infection onset, and the registration-lag
assumption is untested beyond the event-study dip at period -1 [E1]. The
announcement bundles the closure and quarantine intervention, so the
estimand is not a pure information effect [analytical inference]. Platform
coverage (Fang.com) and the completeness of the Tencent Watchtower roster
are unverified, and the 34-city list is not enumerated in the inspected
text [E1, E3].

## Data Requirements

Reuse requires a community-month panel of secondhand prices, volumes, and
guided rents (May 2019-June 2020 or an analogous window), community
geocodes and physical characteristics, and a dated roster of
infection-announcement communities joined by name, address, and
latitude/longitude, with buffer membership constructed by the researcher
[E1]. City features for heterogeneity come from the China City Statistical
Yearbook (2019) [E1]. Dataset acquisition paths belong in the companion
data repository; this record stores only the treatment contract.

## Evidence Notes

E1 is the open PMC full text of Liu and Tang (2021), read directly (HTML and
Europe PMC XML) through the design, results, heterogeneity, placebo,
spillover, and robustness sections; it establishes the design and reported
results but not the underlying platform data. E2 is the PubMed
bibliographic record and official abstract, read directly; it fixes
publication identity and headline results. E3 records the Tencent
Watchtower provenance of the treatment roster as a reported claim because
the historical lists were not re-queried. E4 is NHC Announcement No. 1 of
2020, read directly from nhc.gov.cn; it establishes the statutory Class
B-with-Class-A reporting and control regime from 2020-01-20. E5 is the
Joint Prevention and Control Mechanism community-prevention notice
(肺炎机制发〔2020〕5号, 2020-01-24), read in full via a verbatim mirror
(the gov.cn canonical page did not render); it establishes the official
case-community definition, mandated daily community-level epidemic
information disclosure, and the close-contact observation and lockdown
measures bundled with an announcement. No evidence in this record was
built from search snippets, and nothing here certifies infection
announcements as exogenous beyond the paper's stated matched-DID
assumptions.
