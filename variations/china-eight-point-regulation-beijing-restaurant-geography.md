---
schema_version: 2
id: china-eight-point-regulation-beijing-restaurant-geography
name: China's Eight-Point Regulation and Beijing Restaurant Political Geography
aliases:
- Eight-Point Regulation restaurant demand shock
- 8PR Beijing restaurant proximity design
- Central Eight-Point Regulation and restaurant locations
- 中央八项规定与北京餐饮空间
status: grounded
provenance:
  task_id: task-87a0d0df625d
scope:
  country: China
  regions:
  - Beijing's Dongcheng, Xicheng, Chaoyang, Haidian, Fengtai, and Shijingshan districts
  domains:
  - urban-economics
  - regional-economics
  - political-economy
  - restaurants
  - urban-amenities
  - corruption
  - spatial-economics
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: >
    The 4 December 2012 announcement was a national political signal, but the text
    itself states requirements for Central Political Bureau members rather than a
    restaurant rule or a blanket reimbursement ban for every public institution.
    A separate 2013 regulation later set thrift, reception, and meeting-spending
    controls across a broader range of party-state bodies. The JUE application treats
    the 2012 anti-corruption campaign as a common shock and interacts it with
    Beijing restaurants' pre-existing proximity to government offices. That is a
    paper-defined spatial exposure, not a 1.5-kilometer legal eligibility rule or an
    estimate that isolates the 2012 text from subsequent campaign measures.
identity:
  instrument: >
    The Central Political Bureau's Eight-Point Regulation on improving work style and
    maintaining contact with the public, approved on 2012-12-04. Its eight provisions
    directly address Central Political Bureau members' research visits, meetings,
    official travel, security, media, publications, and thrift; the last provision
    bars banquets and high-grade dishes at their meetings and research visits. The
    paper places this rule within a broader anti-corruption campaign and studies an
    indirect restaurant-demand exposure in Beijing. The distinct 2013 party-and-
    government thrift regulation is relevant post-period context, not the spatial
    assignment mechanism recorded here.
  authority: >
    The Central Political Bureau approved the 2012 text, whose operative clauses
    repeatedly name Central Political Bureau members. Later party and government
    guidance and the separate 2013 thrift regulation document broader implementation
    across party-state bodies. Restaurants were not recipients of a legal treatment;
    the paper infers that proximity exposed them more strongly to changes in
    government-related demand.
  legal_identifiers:
  - 中共中央政治局关于改进工作作风、密切联系群众的八项规定（2012年12月4日）
  - Central Political Bureau Eight-Point Regulation on improving work style and maintaining contact with the public
  implementation_regime: >
    Keep the formal 2012 text distinct from the campaign and its later administrative
    rules. The 2012 provisions directly specify conduct expected of Central Political
    Bureau members, including thrift and restrictions on banquets at their meetings
    and research visits. The authors describe the broader 8PR initiative as curbing
    official extravagance and reimbursement for receptions, meetings, and business
    meals; that is their campaign-level characterization, not the literal scope of
    the 2012 text. A separate 2013 regulation explicitly applies thrift and spending
    controls to a broader list of Party, state, and people's organizations [E4].
    The JUE paper's restaurant linkage remains inferred from proximity to 120
    geocoded Beijing bureaus (74 central and 46 local), not from legal restaurant
    eligibility. Its post-2013 estimates do not isolate the contribution of the
    later regulation or other enforcement measures.
  assignment_mechanism: >
    Institutional exposure is common in calendar time, while intensity is assigned by
    pre-existing political geography. The paper first estimates a continuous spatial
    gradient of distance to the nearest government office and then uses a 1.5-km
    radius as a research threshold because effects are concentrated inside that
    radius. A restaurant's distance is not a legal cutoff and must not be presented
    as an official eligibility rule. The identifying contrast is near-office versus
    farther restaurants within the six inner districts after 2012-12-04.
  parent: null
  related_variations:
  - china-anti-corruption-land-market
  - china-anti-corruption-city-inspection-labor-strikes
timeline:
  announcement: '2012-12-04'
  effective: null
  implementation_start: '2012-12-04'
  implementation_end: null
  local_timing: >
    The Central Political Bureau approved the Eight-Point Regulation on 4 December
    2012. The paper codes 2013 Q1 onward as post and Q4 2012 as event time -1; this
    is the authors' empirical clock, not independent evidence that behavior changed
    exactly on 1 January. The separate 2013 thrift regulation is dated 29 October in
    its text and was published on the MIIT-hosted People's Daily page on 18 December
    2013 [E4], inside the restaurant panel's post period. The design does not
    separately identify that later rule or other enforcement changes.
  anticipation: >
    The paper argues that the announcement was abrupt and largely unforeseen, and its
    event studies show no visible pre-treatment divergence. That is evidence for the
    paper's design, not a verified absence of prior discussions, informal behavior
    changes, or subsequent enforcement anticipation. The policy may also have had
    gradual effects through restaurant entry, exit, and adaptation after 2014.
  last_verified: '2026-09-30'
assignment:
  unit: >
    The primary unit is a restaurant-quarter in Beijing's six inner districts. The
    establishment-level panel covers 2010–2014. A secondary spatial-reallocation
    application uses 1-km-by-1-km grid cells and restaurant counts through 2016.
    The institutional rule itself applies to official conduct, whereas the recorded
    treatment is the restaurant's spatial exposure to the demand shock.
  treated: >
    In the paper's preferred binary design, a restaurant is treated when its geocoded
    location is within 1.5 km of the nearest of the 120 government bureaus. The
    authors also use continuous distance and 200-meter buffer rings, central versus
    local offices, office density, political-scandal exposure, and government-
    designated hotels. These are alternative exposure encodings, not separate legal
    policies.
  comparison_pool: >
    The baseline control group consists of restaurants farther than 1.5 km from any
    listed government office within the same six inner districts and time window.
    Restaurant fixed effects and cell-by-year-quarter fixed effects absorb fixed
    establishment differences and local common shocks. The paper also tests
    business-center proximity and unrelated businesses as placebo comparisons, but
    those do not prove that all farther restaurants are untouched by the national
    regulation.
  rule: >
    First geocode each restaurant address and each listed government bureau, compute
    the distance to the nearest bureau, and retain both the continuous distance and
    the paper's indicator I[distance < 1.5 km]. Interact the exposure with a post
    indicator beginning in 2013 Q1. Keep the six-district sample, office type, grid
    cell, restaurant identity, and quarter as separate join fields. Do not infer the
    treatment from restaurant price, name, district label, or a generic anti-
    corruption keyword.
  intensity: >
    Distance to the nearest office is the canonical continuous intensity. Useful
    secondary measures are central versus municipal office, the number of offices
    near a restaurant, reported political scandals near the office, government-
    designated hotel status, pre-2012 price tier, weekday exposure, and restaurant
    counts by grid cell. A binary 1.5-km indicator is a paper-selected summary of the
    gradient, not an immutable feature of the institution.
  exemptions:
  - Restaurants outside Beijing's six inner districts in the main panel
  - Establishments without a recoverable historical address or geocode
  - The 1.5-km cutoff when a continuous-gradient design is being estimated
  - Grocery stores, supermarkets, laundromats, and business-center proximity used as placebo outcomes or exposures
  - Later nationwide anti-corruption measures that cannot be separated from the 2012 regulation
  compliance: >
    The 2012 clauses directly name Central Political Bureau members; the broader
    campaign and later administrative rules concern a wider set of public bodies.
    Neither the formal text nor the paper's office-distance measure observes which
    restaurants actually received official spending. A nearby restaurant may have
    served ordinary consumers, private firms, or tourists as well as officials;
    location therefore proxies heterogeneous exposure and is not restaurant-level
    legal eligibility or verified compliance.
  exposure_construction: >
    Reconstruct the paper's historical bureau list and coordinates, geocode restaurant
    addresses, calculate nearest-office distance, and link establishments to a stable
    1-km grid cell and one of the six districts. Build a quarterly panel from Dianping
    review dates, average expenditure, restaurant identity, and establishment status.
    For post-2014 counts, use the separate grid-cell series and do not pretend that
    restricted individual reviews and prices remain publicly reproducible.
  required_identifiers:
  - restaurant identifier or stable address-history key
  - restaurant latitude and longitude or geocoded address
  - government bureau identifier, type, and coordinates
  - nearest-office distance and 1.5-km indicator
  - 1-km grid-cell identifier
  - Beijing district identifier
  - calendar quarter and year
  - review count, average expenditure, price tier, and establishment status
  spillovers: >
    The national rule may reduce official demand beyond the six districts and may
    shift spending toward farther or lower-end restaurants. Restaurants near offices
    compete with each other, customers may relocate across the threshold, and entry
    and exit change the composition of the panel. Nearby businesses, hotels, land
    markets, subway expansion, and office relocations can also alter restaurant
    geography. The 1.5-km control group is therefore a local comparison, not a clean
    no-exposure population.
research_compatibility:
  outcome_domains:
  - restaurant customer traffic
  - per-person dining expenditure
  - restaurant entry and exit
  - high-end, middle-end, and low-end establishment composition
  - spatial concentration of urban amenities
  - political-geography and public-demand spillovers
  - household dining-out expenditure in supplementary data
  affected_populations:
  - restaurants and restaurant workers in Beijing's inner six districts
  - consumers and households exposed to local restaurant supply
  - government officials and public employees whose official consumption was restricted
  - hotels and other establishments dependent on government-related demand
  mechanism_channels:
  - contraction of official banquet and reception demand
  - reduced political-connection value of near-office locations
  - customer and restaurant relocation across the spatial exposure gradient
  - entry, exit, pricing, and composition changes in urban amenities
  - competition and aggregate-demand spillovers across restaurant tiers
  best_for:
  - Within-city spatial difference-in-differences around political power centers
  - Urban amenity reallocation and demand-shock studies with establishment geocodes
  - Heterogeneity by office rank, hotel designation, price tier, weekday, and distance
  - Medium-run entry/exit and spatial concentration analysis using grid-cell counts
  not_good_for:
  - Treating 1.5 km as a nationwide legal eligibility threshold
  - Estimating the total welfare effect of the full anti-corruption campaign
  - Designs without historical restaurant addresses, office coordinates, or quarter-level outcomes
  - Claims that the regulation affected only restaurants near offices
  - Separating official from private demand without direct customer or payment data
design:
  claim_type: causal
  affordances:
  - Abruptly announced campaign signal, as characterized by the authors
  - Dense within-city variation in distance to political power centers
  - Restaurant fixed effects and cell-by-year-quarter fixed effects
  - Continuous spatial gradient followed by a transparent threshold design
  - Placebo sectors and business-center exposure tests
  candidate_designs:
  - Restaurant-level spatial difference-in-differences
  - Continuous distance-gradient event study
  - Heterogeneous effects by central/local office, office density, hotel designation, and price tier
  - Grid-cell count/event-study design for medium-run entry and exit
  - Household supplementary DID using government-employment exposure in CFPS
  identifying_variation: >
    The policy shock is common in time, but its predicted demand effect varies with
    pre-existing distance to government offices. The design compares the change in
    near-office restaurants with the change in farther restaurants inside the same
    urban sample, conditional on establishment and local cell-time effects. This is a
    spatial exposure design; the distance threshold is selected from the paper's
    observed gradient and is not a legal discontinuity.
  primary_strategy: >
    Campante, Du, Sun, Wang, and Zheng estimate restaurant-quarter models with
    restaurant fixed effects, cell-by-year-quarter fixed effects, a post indicator
    from 2013 Q1, and clustering at the grid-cell level. They first estimate 200-meter
    distance rings and then use the 1.5-km indicator suggested by the gradient. Event
    studies use Q4 2012 as the omitted pre-period; subway distance is a time-varying
    control for transport expansion.
  estimand: >
    The main estimand is the relative change in restaurant reviews or per-person
    expenditure after the Eight-Point Regulation for establishments within the
    paper's near-office exposure radius, relative to farther establishments in the
    six-district comparison, under parallel spatial demand trends. The grid-count
    application estimates medium-run changes in establishment location, not only
    short-run customer demand.
  treatment_variable: >
    Preferred binary treatment is I[nearest government-office distance < 1.5 km]
    multiplied by I[quarter >= 2013 Q1]. Alternative specifications use log distance,
    200-meter rings, office rank/density, government-designated hotel status, and
    continuous post exposure. These encodings should not be collapsed into one
    undifferentiated anti-corruption dummy.
  comparison_logic: >
    Compare near-office and farther restaurants before and after the announcement,
    absorb restaurant and local cell-time effects, and inspect pre-event coefficients.
    Use business-center distance and unrelated sectors as falsification exercises;
    they help distinguish political geography from generic centrality but do not
    guarantee no spillover to the farther group.
  estimation_notes: >
    The paper reports relative post-policy declines in reviews and expenditure near
    offices, with stronger patterns near central offices, government-designated
    hotels, higher office density, weekdays, and high-end establishments. These are
    source-reported estimates. A new application should preserve the review-proxy,
    entry/exit, and general-equilibrium limitations rather than interpret the
    coefficient as a pure change in official spending.
  assumptions:
  - Near and farther restaurants would have followed parallel demand trends absent the regulation
  - Historical bureau locations and restaurant geocodes are measured without differential error after 2012
  - Online review volume and expenditure proxies do not change differentially by distance solely because of review behavior
  - Cell-time fixed effects and subway controls absorb relevant local shocks without conditioning away the treatment mechanism
  - Restaurant entry, exit, customer relocation, and office relocation do not overturn the chosen estimand
  - The policy timing is not confounded by a simultaneous spatially concentrated shock affecting only near-office restaurants
  diagnostics:
  - Estimate the continuous 200-meter distance gradient before selecting a threshold
  - Plot event-study leads through Q4 2012 and test joint pre-trends
  - Use alternative radii, log distance, and leave-one-office-out nearest-distance measures
  - Separate central and local offices, weekdays and weekends, and price tiers
  - Test government-designated hotels and office-density/scandal measures
  - Use business-center distance and unrelated sectors as placebos
  - Control for subway expansion, land sales, zoning, and office relocation where available
  - Compare review outcomes with entry/exit and grid-count outcomes to diagnose platform behavior
design_profiles:
- id: restaurant-quarter-demand
  label: Restaurant-quarter spatial demand DID
  design_families:
  - spatial-did
  - event-study
  when_to_use: >
    Use when restaurant addresses and quarterly Dianping outcomes are available for
    2010–2014 and the application can reconstruct the nearest-office exposure and
    six-district sample. This profile estimates differential demand exposure rather
    than the nationwide average effect of the regulation.
  outcome_domains:
  - reviews
  - per-person expenditure
  - restaurant demand
  requirements:
    population: Restaurants and consumers in Beijing's six inner districts
    observation_unit: Restaurant-quarter
    geography_level: Restaurant, 1-km grid cell, and district
    time_start: 2010
    time_end: 2014
    minimum_frequency: quarterly
    minimum_pre_periods: 8
    minimum_post_periods: 8
    required_fields:
    - restaurant outcome
    - restaurant geocode
    - nearest-office distance
    - grid cell
    - quarter
    required_identifiers:
    - restaurant key or stable address
    - government office key
    - grid-cell key
    - quarter
    treatment_key:
    - nearest-office distance
    - 1.5-km indicator
    - post-2013-Q1 indicator
- id: grid-count-reallocation
  label: Grid-cell establishment reallocation
  design_families:
  - spatial-event-study
  - urban-amenity-reallocation
  when_to_use: >
    Use when only post-2014 grid-cell counts can be recovered. Treat the result as
    medium-run entry/exit and spatial reallocation evidence, not as a substitute for
    the establishment-level demand panel.
  outcome_domains:
  - restaurant counts
  - spatial concentration
  - urban amenities
  requirements:
    population: Restaurant establishments in Beijing's six inner districts
    observation_unit: 1-km grid-cell-year or grid-cell-quarter
    geography_level: 1-km grid cell and nearest government office
    time_start: 2010
    time_end: 2016
    minimum_frequency: annual or quarterly
    minimum_pre_periods: 2
    minimum_post_periods: 2
    required_fields:
    - establishment count
    - grid-cell centroid
    - nearest-office distance
    - year or quarter
    required_identifiers:
    - grid-cell key
    - government office key
    - year or quarter
    treatment_key:
    - grid-cell nearest-office distance
    - post-2013-Q1 indicator
threats:
- type: indirect-spatial-exposure
  basis: inferred
  condition: >
    Near-office location is a proxy for prior government-related demand, not a legal
    treatment assignment. It can also capture centrality, land prices, foot traffic,
    clientele, and unobserved urban amenities that evolve differently over time.
  evidence_refs:
  - E2
  possible_diagnostics:
  - local cell-time fixed effects and restaurant fixed effects
  - continuous gradients, alternative radii, and pre-trend tests
  - business-center and unrelated-sector placebos
- type: review-proxy-and-platform-measurement
  basis: reported
  condition: >
    Reviews and Dianping's average expenditure are proxies for visits and spending.
    A post-policy change in officials' willingness to review or in platform coverage
    could mimic a demand change, even though entry/exit evidence helps address one
    such concern.
  evidence_refs:
  - E2
  possible_diagnostics:
  - compare reviews with establishment entry/exit and grid counts
  - test weekday versus weekend effects
  - use alternative outcome sources when available
  - document platform access and missingness by quarter
- type: concurrent-urban-shocks
  basis: reported
  condition: >
    Beijing subway expansion, land sales, zoning, office relocation, and local
    economic changes overlap the 2012–2014 period and may alter restaurant geography.
  evidence_refs:
  - E2
  possible_diagnostics:
  - time-varying subway distance control
  - land-use and development-intensity placebo tests
  - office relocation audit and alternative sample windows
- type: general-equilibrium-and-spillover
  basis: inferred
  condition: >
    The national rule can reduce or redirect spending across the entire restaurant
    market. Customers, restaurants, and workers may move across the 1.5-km radius,
    while lower-end restaurants may be affected through competition and aggregate
    demand externalities.
  evidence_refs:
  - E2
  possible_diagnostics:
  - distance-band and spatial spillover estimates
  - entry/exit and price-tier decomposition
  - compare near-office effects with citywide and sectoral changes
- type: timing-and-enforcement-bundle
  basis: inferred
  condition: >
    The paper's December 2012 campaign date, its 2013 Q1 post coding, later
    disciplinary enforcement, and the separate 2013 national thrift regulation do
    not form one perfectly dated intervention. The 2013 regulation covers a wider
    set of party-state bodies and falls inside the paper's post sample; the design
    may estimate a bundled accountability and spending-control shock rather than the
    isolated effect of the original 2012 text.
  evidence_refs:
  - E1
  - E2
  - E4
  possible_diagnostics:
  - alternative announcement and post-date conventions
  - event-time plots and shorter windows
  - distinguish the Eight-Point Regulation from later inspections and local rules
- type: geocoding-and-office-list-error
  basis: reported
  condition: >
    The paper geocodes 120 offices and restaurant addresses, but the full coordinate
    files and a versioned historical office roster are not part of the public paper
    record. Office additions, moves, or address ambiguity can change nearest-office
    treatment classification.
  evidence_refs:
  - E2
  possible_diagnostics:
  - reproduce Tables A.2–A.5 and retain office type and coordinates
  - leave-one-office-out and alternative geocoding checks
  - maintain historical address versions and uncertainty flags
empirical_requirements:
  contract_version: 1
  population: Restaurants, consumers, and urban amenity establishments in Beijing's six inner districts
  observation_unit: Restaurant-quarter or 1-km grid-cell-year/quarter
  geography_level: Restaurant, grid cell, district, and government office
  time_start: 2010
  time_end: 2016
  minimum_frequency: quarterly
  minimum_pre_periods: 8
  minimum_post_periods: 8
  required_fields:
  - restaurant reviews or visits
  - average expenditure per person
  - restaurant entry/exit and price tier where available
  - restaurant address and coordinates
  - government bureau list, type, and coordinates
  - nearest-office distance and exposure radius
  - grid-cell and district identifiers
  - quarter/year and post-policy indicator
  required_identifiers:
  - restaurant key or stable historical address
  - government-office key
  - grid-cell key
  - district key
  - quarter/year
  treatment_key:
  - announcement date 2012-12-04
  - post indicator from 2013 Q1
  - nearest-office distance
  - 1.5-km exposure indicator
  - office type and density
  treatment_source: >
    The original 2012 text establishes its approval date and formal scope; the paper
    frames a broader campaign as the common shock, while the distinct 2013 regulation
    establishes overlapping later spending controls. The paper's inspected full text
    and appendix establish the Beijing office list, Dianping construction, spatial
    threshold, and research coding. Restaurant microdata, geocodes, and full office
    coordinate files are not assumed to be open merely because the paper is inspectable.
  measurement_risks:
  - 1.5-km radius is a paper-selected summary, not a legal cutoff
  - review volume and expenditure are platform proxies
  - historical office locations and restaurant addresses may be misgeocoded
  - national and later local anti-corruption measures are bundled
  - market-wide demand shifts contaminate farther restaurants
  - entry/exit changes the composition of establishment-level panels
evidence:
- id: E1
  source_type: policy-document
  citation: >
    Central Political Bureau. 2012-12-04. 中共中央政治局关于改进工作作风、密切联系群众的八项规定
    [Eight-Point Regulation on improving work style and maintaining contact with the public].
  url: https://gxj.zhoukou.gov.cn/sitesources/gyxxhj/page_pc/tslm/djlz/article14b5948f875f4fb5a2f0272e42a0876f.html
  date: '2012-12-04'
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.announcement
  - timeline.implementation_start
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: >
    Government-hosted full text: introductory date and scope at the 4 December 2012
    approval (opening paragraph); provisions 1–8, especially provisions 1–2 and 8,
    which repeatedly address Central Political Bureau members and specify restrained
    reception/meeting arrangements, no banquets, and no high-grade dishes. The text
    does not itself set nationwide restaurant eligibility, a blanket reimbursement
    ban, or the paper's restaurant radius and sample.
- id: E2
  source_type: paper
  citation: >
    Campante, Filipe, Rui Du, Weizeng Sun, Jianghao Wang, and Siqi Zheng. 2025.
    “JUE Insight: Political Geography and the Spatial Allocation of Economic Activity:
    Evidence from China's Anti-Corruption Campaign.” Journal of Urban Economics 149:
    103797.
  url: https://filipecampante.org/wp-content/uploads/2023/08/CDSWZ_Jul25_JUECI.pdf
  date: 2025
  supports:
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.local_timing
  - timeline.anticipation
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.exposure_construction
  - assignment.required_identifiers
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - empirical_requirements.observation_unit
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_key
  verification_status: verified
  access_level: full-text
  locator: >
    Author-hosted PDF (filename contains Jul25): pp. 1–3 (research object and campaign
    characterization), pp. 5–8 (institutional background and Dianping sample), pp.
    8–12 (120 bureaus, spatial DID and 1.5-km threshold), pp. 13–18 (event study,
    heterogeneity and placebos), and appendix Tables A.2–A.5, A.8–A.19 (office list
    and robustness). DOI/publisher metadata match the article identity, but this file
    was not compared line-by-line with the final typeset version. Its description of
    a campaign banning reimbursements is reported author framing, not a substitute
    for the 2012 rule's narrower operative text.
- id: E3
  source_type: paper
  citation: >
    Crossref/DOI metadata for Campante, Du, Sun, Wang, and Zheng, Journal of Urban
    Economics 149 (2025), article 103797.
  url: https://doi.org/10.1016/j.jue.2025.103797
  date: 2025
  supports:
  - design_applications.paper
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
  verification_status: verified
  access_level: metadata
  locator: DOI and bibliographic record; use E2 for substantive claims.
- id: E4
  source_type: policy-document
  citation: >
    Central Committee and State Council. 2013. 党政机关厉行节约反对浪费条例
    [Regulation on Party and Government Organs Practicing Thrift and Opposing Waste],
    dated 2013-10-29; full text reprinted by the MIIT portal from People's Daily.
  url: https://www.miit.gov.cn/ztzl/lszt/kzqzlxjydljqzfjs/zyjs/art/2020/art_b04fe361f147481eb0b35680f22a0cf1.html
  date: '2013-10-29'
  supports:
  - identity.implementation_regime
  - timeline.local_timing
  - threats.condition
  verification_status: verified
  access_level: official-document
  locator: >
    Full-text government-hosted reprint, published 2013-12-18: Articles 2 and 5
    define the covered Party, state, people's-organization and civil-service-managed
    bodies and national/local coordination; Articles 8, 20–21 and 30–31 set budget,
    official-reception, and meeting-spending controls. This is a distinct later
    regulation, not the text or assignment rule of the 2012 Eight-Point Regulation.
design_applications:
- paper: 'JUE Insight: Political Geography and the Spatial Allocation of Economic Activity: Evidence from China''s Anti-Corruption Campaign'
  doi: 10.1016/j.jue.2025.103797
  journal: Journal of Urban Economics
  year: 2025
  research_question: >
    How does a change in official spending and accountability alter the spatial
    allocation and composition of urban restaurant activity around political power
    centers?
  population: >
    Restaurants in Beijing's Dongcheng, Xicheng, Chaoyang, Haidian, Fengtai, and
    Shijingshan districts, observed quarterly from 2010 to 2014; grid-cell counts
    extend the spatial analysis through 2016.
  outcome: >
    Quarterly Dianping customer-review counts as a traffic proxy, average expenditure
    per person, restaurant entry/exit, high/middle/low price composition, and grid-
    cell establishment counts.
  data_used:
  - Dianping restaurant records, addresses, reviews, prices, and establishment dates
  - Geocoded restaurant locations and 1-km grid cells
  - 120 geocoded Beijing government bureaus (74 central, 46 local)
  - Subway distance and land-market/placebo data
  - China Family Panel Studies (CFPS) 2012 and 2014 for a supplementary household check
  treatment_encoding: >
    Near-office exposure is I[distance to nearest listed government bureau < 1.5 km]
    interacted with a post indicator from 2013 Q1. Continuous distance, 200-meter
    rings, office rank/density, hotel designation, and price tier are alternative
    encodings.
  comparison: >
    Near-office restaurants versus restaurants farther than 1.5 km in the same six
    inner districts, before and after 2012 Q4/2013 Q1, with restaurant fixed effects
    and cell-by-year-quarter fixed effects; business-center and unrelated-sector
    placebos provide additional contrasts.
  empirical_design: >
    Spatial gradient followed by spatial DID and event studies, with grid-cell
    clustered standard errors, subway-distance controls, office-rank heterogeneity,
    hotel and price-tier checks, and establishment-count reallocation analysis.
  assumptions:
  - near- and far-office restaurants would have had parallel demand trends without 8PR
  - Dianping reviews and expenditure track actual demand sufficiently for the chosen outcome
  - historical office and restaurant geocodes are comparable across quarters
  - spillovers and market-wide policy effects do not erase the relative spatial contrast
  threats_addressed:
  - pre-trend event studies
  - continuous distance gradient and alternative thresholds
  - subway and land/development controls
  - central/local office and hotel/price-tier heterogeneity
  - business-center and unrelated-business placebo tests
  evidence_refs:
  - E2
  - E3
readiness_blockers:
- >
  The 1.5-km radius is selected from the paper's spatial gradient; it is not stated
  in the official Eight-Point Regulation. Any reuse must preserve the continuous
  distance measure and treat the binary radius as an application-specific encoding.
- >
  The paper lists 120 bureaus and names them in Tables A.2–A.5, but the full geocoded
  coordinate file, historical address versions, and restaurant-level Dianping data
  are not established as publicly reproducible by the inspected sources.
- >
  Online reviews and platform-reported expenditure are proxies. A change in review
  propensity, platform coverage, or restaurant composition could affect measured
  outcomes even if actual visits changed less or differently.
- >
  The authors' campaign interpretation, December 2012 announcement, 2013 Q1 post
  period, later enforcement, and separate 2013 nationwide thrift regulation overlap.
  The paper does not isolate their individual contributions; do not interpret its
  spatial contrast as the clean effect of one sentence or the total welfare effect
  of anti-corruption.
- >
  Near-office restaurants were likely different before the policy. Fixed effects and
  event studies support the paper's comparison but do not make political geography
  intrinsically exogenous or eliminate general-equilibrium spillovers.
method_transfer: null
---

## Institutional Background

On 4 December 2012 the Central Political Bureau approved the Eight-Point Regulation on improving work style and maintaining contact with the public. Its clauses directly address Central Political Bureau members: they cover research visits, meetings, travel, security, reporting, publications, and thrift. The eighth clause bars banquets and high-grade dishes at their meetings and research visits. The text does not itself state a blanket ban on reimbursing all receptions or meals by every public institution. [E1]

A distinct regulation dated 29 October 2013 set thrift and spending controls for a much broader list of Party and state organs, people's organizations, and civil-service-managed institutions, including national and local coordination and controls on official receptions and meetings. It falls within the paper's post-2013 Q1 window, but the restaurant design does not separately identify its effect. [E4]

## What Changed

The authors frame the 2012 Eight-Point initiative as part of a broader anti-corruption campaign that curtailed official extravagance; their manuscript describes it as banning reimbursements for receptions, meetings, business meals, and leisure activities. That is the paper's campaign-level characterization, not the narrower wording of the original eight clauses. [E2, reported claim] The empirical object is the campaign shock as dated by the authors, interacted with pre-existing Beijing political geography. Nearby restaurants are presumed to have had greater government-related demand; the paper does not observe individual public-fund transactions. [Analytical inference]

The 1.5-kilometer radius is not in either rule. The paper first estimates a semiparametric distance gradient and says its subsequent binary cutoff is empirically determined from that gradient; it then codes restaurants within 1.5 km as exposed. This is a research-defined summary, not legal eligibility. [E2]

## Implementation and Assignment

The author-hosted PDF studies 30,974 restaurants in Beijing's six inner districts—Dongcheng, Xicheng, Chaoyang, Haidian, Fengtai, and Shijingshan—using quarterly Dianping data from 2010 to 2014. It geocodes 120 bureaus, 74 central and 46 local, and assigns each restaurant its nearest-office distance. The preferred spatial DID sets post to 2013 Q1 onward, with Q4 2012 as the omitted event period. DOI metadata identify the corresponding 2025 JUE article, but the hosted file was not independently compared line-by-line with the final typeset version. [E2; E3]

The treatment is thus an exposure construction: near-office restaurants versus farther restaurants in the same urban sample. Restaurant fixed effects and cell-by-year-quarter fixed effects absorb persistent establishment differences and local common shocks; subway distance is allowed to vary over time. The paper also uses continuous rings, office rank and density, government-designated hotels, price tiers, weekdays, and unrelated sectors as diagnostics or alternative exposure definitions. [E2]

## Why This Creates Empirical Variation

The common policy date alone would be a simple before–after comparison and would not isolate the restaurant mechanism. The usable contrast comes from the paper's claim that official demand was more concentrated near offices before the campaign, while farther restaurants in the same six districts provide a spatial countertrend. [E2, reported claim] The design can speak to relative demand and urban-amenity reallocation under the authors' campaign interpretation; because the separate 2013 rule overlaps the post period, it does not isolate the original eight clauses or identify the nationwide average effect. [E4; analytical inference]

## Identification Risks

Distance to an office also captures centrality, land prices, foot traffic, clientele, and other urban amenities. The paper's event studies and local time effects make the comparison more credible, but they do not make the location rule random. Review counts and platform-reported expenditure are proxies, and a national demand shock can spill across the 1.5-km boundary through customer relocation, entry, exit, and competition. Subway expansion, land use, office relocation, later enforcement, and changes in review behavior must remain visible in any reuse. [E2]

## Data Requirements

A replication-ready treatment key needs historical bureau identities and coordinates, restaurant address histories and coordinates, nearest-office distance, district and grid-cell IDs, quarter, reviews, expenditure, price tier, and establishment status. The paper also uses a supplementary CFPS household check, but that is a different exposure (government-employed household member) and should not be substituted for the spatial restaurant treatment. The inspected paper does not establish that the full Dianping microdata or office geocodes are openly available. [E2]

## Evidence Notes

E1 establishes the 2012 approval and the original text's scope and clauses; it does not establish a blanket nationwide reimbursement ban, restaurant locations, or a spatial threshold. E4 establishes that a distinct 2013 regulation later covered broader party-state bodies and controlled reception and meeting spending; it does not show which provision caused the restaurant results. E2 is the inspected author-hosted PDF and establishes the reported sample, office list, exposure construction, model, timing, data proxies, and diagnostics; the filename includes “Jul25,” but it is not a line-by-line verified copy of the final typeset paper. E3 confirms the DOI/article bibliographic identity only. The remaining limits are retained rather than filled by inference.
