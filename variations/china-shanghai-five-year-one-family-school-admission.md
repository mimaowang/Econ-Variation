---
schema_version: 2
id: china-shanghai-five-year-one-family-school-admission
name: Shanghai Five-Years-One-Family school-admission restriction
aliases:
- Shanghai 5Y1F education policy
- 五年一户学区入学政策
- Five-years-one-family housing and school-admission rule
- Shanghai school-admission loophole restriction
status: grounded
provenance:
  task_id: task-e6f648e1ff1b
scope:
  country: China
  regions:
  - Shanghai municipality, with district-level rollout in Jing'an, Baoshan, Changning, Huangpu, Xuhui, Pudong, Minhang, and Yangpu
  domains:
  - urban-economics
  - regional-economics
  - housing
  - education
  - spatial-economics
  - residential-sorting
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    Shanghai's Five-Years-One-Family rule tightened the link between a residential
    address and priority for a public elementary school: an address could normally
    supply only one same-school admission priority in a five-year window, even when
    ownership or the household changed. The rule was adopted by districts at
    different times rather than imposed as one citywide date. The canonical object
    is the common address-based restriction and its district rollout; a paper's
    ward-by-post indicator is a research encoding, not a claim that every house had
    identical priority status or that the rule applied to every Shanghai school.
identity:
  instrument: >
    The Shanghai Five-Years-One-Family (5Y1F) school-admission restriction for
    selected public elementary-school catchments. After a district adopted it, an
    address in an affected catchment normally provided only one same-school
    admission priority within five years, so reselling a house could no longer
    repeatedly refresh the priority. Twins and second-child exceptions are part of
    the reported implementation, and individual schools or districts can impose
    additional hukou, ownership, or residence-duration ordering rules.
  authority: >
    District education authorities implemented the rule within Shanghai's compulsory
    education enrollment system under the municipal principle of exam-free,
    nearby public-school admission. The Ministry of Education's contemporary
    account identifies Jing'an's address database and five-year rule as a pilot
    experience, while later district implementation notices show that coverage and
    ranking conditions differed across districts and schools.
  legal_identifiers:
  - 静安区“一个门牌号一居住户，五年内只接收一学生”试点（2014）
  - 上海义务教育阶段公办小学对口入学“五年一户”或“五年内只安排一次同校对口入学”规则
  - Shanghai Five-Years-One-Family (5Y1F) school-admission restriction
  implementation_regime: >
    This is a district- and school-level enrollment administration rule, not a
    national statute and not a uniform Shanghai-wide treatment on one date. The
    research application groups houses by the district's adoption year, but the
    underlying institutional exposure is address-to-school specific and can depend
    on hukou migration date, ownership, co-residence, sibling exceptions, and the
    capacity of the assigned school. Later annual enrollment opinions may revise the
    list of schools or the ordering rules.
  assignment_mechanism: >
    Formal assignment follows the residential address and its mapped public
    elementary school. For the published Shanghai application, a transaction is
    coded as post-treatment when it occurs in a district after that district's
    adoption year. Within treated districts, the paper further separates houses in
    good-school catchments, nearby houses outside those catchments (the paper's
    “babysitting communities”), and other ordinary areas. These spatial and
    ward-by-year encodings must be kept separate from the legal address-level rule.
  parent: null
  related_variations: []
timeline:
  announcement: '2014'
  effective: null
  implementation_start: 2014
  implementation_end: 2017
  local_timing: >
    The author thesis underlying the JUE application records first implementation
    in Jing'an in 2014, followed by Baoshan and Changning in 2015, Huangpu, Xuhui,
    and Pudong in 2016, and Minhang and Yangpu in 2017. The 2017 Jing'an district
    government account independently describes seven districts with the restriction
    in 2016 and Yangpu as the new district in 2017. The dates are district adoption
    years; exact school-by-school effective dates and annual enrollment lists still
    need to be joined for a property-level design.
  anticipation: >
    The Jing'an pilot was publicly discussed in 2014 and the rule was expected to
    affect speculative resale and school-district demand. Households, brokers, and
    districts may have adjusted before the coded adoption year; the paper's event
    study is evidence about its chosen sample, not proof that there was no
    anticipation or policy discussion.
  last_verified: '2026-08-11'
assignment:
  unit: >
    The institutional unit is a residential address linked to a public elementary
    school catchment and a five-year admission-use history. The JUE application
    observes secondhand-house transactions across 14 Shanghai districts from 2012
    to 2019 and uses district-by-year exposure as its baseline unit of treatment.
  treated: >
    Institutionally treated observations are addresses in the schools and districts
    covered by a local 5Y1F implementation after that implementation begins. In the
    paper's main DID, a house is treated when its transaction is in one of the eight
    adopting districts after that district's adoption year. In the spatial results,
    treatment intensity is higher for houses assigned to level-1-to-level-3 good
    schools and differs for nearby outside-catchment communities.
  comparison_pool: >
    The baseline comparison combines pre-adoption transactions in adopting districts
    with contemporaneous transactions in the six districts without the rule during
    the study window. The paper's location comparison is within adopting districts:
    houses inside good-school catchments, houses within a matched radius outside the
    catchment, and ordinary houses farther from good schools. Untreated does not mean
    unaffected because parents may move across district and school boundaries.
  rule: >
    Build an address-to-school crosswalk, identify the district's adoption year and
    the applicable school list, then code post_{d,t}=1 for transactions after that
    district-year. Retain the exact address or residential-zone identifier, assigned
    school, school quality category, district, transaction date, and any available
    priority-use history. For the paper's babysitting comparison, draw a 0.7, 0.85,
    1.0, or 1.2 km circle around a good school, exclude the school catchment itself,
    and record the chosen radius rather than treating it as an official boundary.
  intensity: >
    The legal rule is a five-year address-use limit. Research intensity can be coded
    by adoption year, assigned-school quality, distance from a good school, or the
    availability of a recent admission priority. The paper's 0.7 km baseline radius,
    alternative radii, and level-1/2/3 school categories are empirical encodings,
    not legal thresholds.
  exemptions:
  - Twins, second children, and later officially recognized multi-child exceptions
  - Schools or addresses outside the district's published five-year list
  - Families whose hukou, ownership, or co-residence ranking sends them to coordinated placement rather than the mapped school
  - Transactions without a stable historical address, district, school, or date
  - The ward-by-post dummy when the research question requires actual address-level priority availability
  compliance: >
    The rule constrains the admission priority attached to an address; it does not
    guarantee admission, because school capacity, hukou timing, ownership, and
    co-residence ordering can determine who receives a seat. The paper cannot observe
    priority-use history for most listings, so ward-by-post exposure is a proxy for
    the institutional shock and should not be read as perfect compliance.
  exposure_construction: >
    Reconstruct the district adoption-year table from local education notices and
    map every property or residential zone to its assigned public elementary school.
    Merge transaction date, price, structural characteristics, district, school
    quality, and coordinates. For a close-neighbor design, calculate distance from
    the good school and keep the catchment indicator separate from the radius-based
    babysitting indicator. If the five-year history is unavailable, label the
    observation as ward-level exposure rather than inventing current priority status.
  required_identifiers:
  - stable property, residential-zone, or address-history identifier
  - transaction or listing date and year
  - transaction price and house characteristics
  - Shanghai district identifier and district adoption year
  - assigned public elementary-school identifier and catchment version
  - property longitude and latitude or an auditable geocoded address
  - school-quality category and source date
  - five-year priority-use history when a property-level treatment is claimed
  spillovers: >
    Restricting resale can move parents and speculative demand to untreated wards,
    neighboring communities, private schools, or suburban good-school areas. Prices
    and transactions can therefore change outside adopting districts. School-boundary
    revisions, municipal housing controls, subway and amenity changes, and broker
    information can also be correlated with adoption. A comparison ward is a local
    market counterfactual, not a no-exposure population.
research_compatibility:
  outcome_domains:
  - secondhand housing prices and price per square meter
  - transaction volume and speculative resale
  - school-district price premiums
  - residential sorting and income or wealth segmentation
  - spatial spillovers to babysitting communities
  - school-choice and public-service capitalization
  affected_populations:
  - Shanghai households seeking public elementary-school admission
  - homeowners, renters, and prospective buyers in school catchments
  - property brokers and residential communities
  - district education authorities and public elementary schools
  mechanism_channels:
  - reduced ability to refresh admission priority through early resale
  - tighter supply of usable priority addresses in good-school catchments
  - relocation and substitution across school and district boundaries
  - capitalization of school quality into house prices
  - changes in speculative liquidity and residential sorting
  best_for:
  - Staggered-adoption DID using housing transactions and district notices
  - Spatial heterogeneity between school catchments and nearby communities
  - School-premium, housing-sorting, and public-service capitalization studies
  - Designs that can recover historical school boundaries and address identities
  not_good_for:
  - Calling 5Y1F a single citywide reform on one date
  - Treating a ward-by-post indicator as actual admission eligibility
  - Inferring the five-year rule from a property advertisement or current school listing alone
  - Estimating household welfare without observing school admission, migration, or substitution responses
  - Ignoring school-list revisions, hukou ranking, sibling exceptions, or concurrent housing policies
design:
  claim_type: causal
  affordances:
  - Districts adopted a common restriction in staggered years from 2014 to 2017
  - Large secondhand-house transaction sample with structural and location fields
  - Address-to-school assignment and good-school spatial heterogeneity
  - Nearby outside-catchment communities provide a mechanism-relevant spillover comparison
  - Event-study and alternative-radius checks are available in the published application
  candidate_designs:
  - Staggered district-by-year difference-in-differences
  - Event study around each district's adoption year
  - Heterogeneous DID by good-school catchment, babysitting community, and ordinary area
  - Boundary or close-neighbor design using school catchment and geocoded property location
  - Transaction-volume and residential-sorting follow-up designs
  identifying_variation: >
    The common institutional change is an address-level five-year limit, while the
    usable research contrast comes from different district adoption years and from
    pre-existing proximity to good-school catchments. A credible design must keep
    the district adoption-year shock, the assigned-school catchment, and the paper's
    radius-based neighbor category as separate variables.
  primary_strategy: >
    Ding and Itoh pool 156,396 usable transaction observations from 2012–2019,
    compare adopting districts with non-adopting districts and pre-adoption years,
    and control for house characteristics, school-level factors, district effects,
    year effects, and district-specific trends. Their event study uses the different
    district adoption years and examines three years before and after adoption,
    excluding Jing'an from that event-study sample to preserve pre-period length.
    The preferred spatial specifications interact post-adoption exposure with good-
    school, close-neighbor, and ordinary-area indicators.
  estimand: >
    The baseline estimand is the relative change in log secondhand-house transaction
    prices in an adopting district after its local 5Y1F implementation, conditional
    on the paper's controls and trends. Heterogeneous estimands compare the change
    for good-school catchment houses and nearby outside-catchment houses with other
    locations. These are market-price effects of the policy proxy, not the total
    welfare effect of admission restriction or a direct effect on children's scores.
  treatment_variable: >
    Use post_{d,t}=1 when a transaction occurs in district d after its audited
    adoption year, interacted with the relevant house-location category. For a
    stronger property-level design, replace the proxy with address-by-school
    eligibility and the last five-year priority-use date. Keep the district adoption
    year, catchment membership, school quality, and neighbor radius as separate keys.
  comparison_logic: >
    Compare pre/post changes in adopting districts with contemporaneous changes in
    districts not yet adopting, while testing event-study leads and district trends.
    Within adopting districts, compare good-school catchments with matched outside
    circles and ordinary areas. A close-neighbor contrast is informative about the
    paper's babysitting mechanism but is not a clean spatial RD unless boundary,
    distance, and school-list histories are independently reconstructed.
  estimation_notes: >
    The author thesis reports an average price increase of about 3% in treated wards
    after full controls, roughly 8–10% in the best school categories, and a negative
    effect in nearby babysitting communities; the published JUE abstract reports the
    same qualitative pattern and an immediate event-study response that fades somewhat
    in the short run. These are source-reported estimates. They should not be turned
    into universal effects because the data are scraped secondhand-house records and
    the treatment is a district-level proxy for an address rule.
  assumptions:
  - Adoption timing is not driven by a contemporaneous housing-price shock that differentially affects adopting districts
  - Pre-adoption price trends are sufficiently comparable after house, school, district, year, and trend controls
  - The adoption-year table and school lists are measured without differential timing error
  - The transaction sample and listing platform do not change composition differentially at adoption
  - Cross-district migration and price spillovers do not invalidate the chosen local estimand
  - School rankings and catchment assignments are not themselves post-treatment reclassifications
  diagnostics:
  - Plot and jointly test event-study leads for every adoption cohort
  - Re-estimate with alternative district trends, adoption windows, and leave-one-district-out samples
  - Audit school lists, catchment boundaries, and adoption dates against dated district notices
  - Use alternative good-school definitions and 0.7, 0.85, 1.0, and 1.2 km neighbor radii
  - Test transaction counts, listing duration, house age, and other outcomes for platform-composition changes
  - Check spillovers to non-adopting wards and nearby ordinary areas
  - Separate current school assignment from historical five-year priority availability
  - Control or restrict for concurrent housing, school, subway, and district-boundary reforms
design_profiles:
- id: ward-staggered-housing-did
  label: District-adoption housing transaction DID
  design_families:
  - staggered-did
  - event-study
  when_to_use: >
    Use when district adoption years, transaction dates, and stable district and
    property identifiers are available. The result estimates a market-price response
    to local implementation and should retain district-specific timing rather than
    replacing it with a 2014 citywide dummy.
  outcome_domains:
  - log transaction price
  - price per square meter
  - transaction volume
  requirements:
    population: Secondhand residential properties and buyers in Shanghai's 14 districts
    observation_unit: Property transaction or property-year observation
    geography_level: Property, residential zone, district, and school-assignment area
    time_start: 2012
    time_end: 2019
    minimum_frequency: Annual or transaction-level
    minimum_pre_periods: 2
    minimum_post_periods: 2
    required_fields:
    - transaction price and date
    - house structural characteristics
    - stable property or residential-zone identifier
    - district identifier and audited adoption year
    - assigned school and school-quality category
    required_identifiers:
    - property_id or address-history key
    - district_id
    - school_id
    - transaction_year
    treatment_key:
    - district_adoption_year
    - post_district_adoption
    - property_or_zone_id
- id: good-school-babysitting-spillover
  label: Good-school catchment and nearby babysitting-community heterogeneity
  design_families:
  - spatial-did
  - close-neighbor-comparison
  when_to_use: >
    Use when school catchment polygons or a defensible address-to-school crosswalk
    and geocoded property locations are available. Keep the radius used to define a
    nearby outside-catchment house explicit and do not mistake it for a legal border.
  outcome_domains:
  - school-district price premium
  - nearby-community price spillover
  - residential sorting
  requirements:
    population: Properties inside good-school catchments and nearby outside-catchment communities
    observation_unit: Property transaction
    geography_level: Property, school catchment, nearby radius, and district
    time_start: 2012
    time_end: 2019
    minimum_frequency: Annual or transaction-level
    minimum_pre_periods: 2
    minimum_post_periods: 2
    required_fields:
    - assigned school and catchment version
    - good-school category and source date
    - property coordinates
    - distance to good school
    - district adoption year and transaction date
    required_identifiers:
    - property_id or residential-zone_id
    - school_id
    - catchment_version
    - district_id
    treatment_key:
    - good_school_catchment
    - babysitting_radius
    - post_district_adoption
threats:
- type: staggered-adoption-and-timing
  basis: reported
  condition: >
    Districts adopted the rule in different years, and adoption may respond to local
    school pressure, housing speculation, or political priorities. A single pooled
    two-way fixed-effects coefficient can mix cohort effects and negative weights.
  evidence_refs:
  - E2
  - E4
  possible_diagnostics:
  - cohort-specific event studies and modern staggered-DID estimators
  - adoption-window and leave-one-district-out checks
  - district-specific trends and pre-treatment balance
- type: address-level-treatment-misclassification
  basis: reported
  condition: >
    The paper's main treatment is a district-by-post indicator, while actual priority
    depends on the particular address, assigned school, five-year history, hukou,
    ownership, and exceptions. Most records do not reveal whether a priority is
    immediately available after the policy.
  evidence_refs:
  - E1
  - E4
  possible_diagnostics:
  - construct address-level priority histories where administrative records permit
  - compare property-level and district-level exposure
  - separate schools with and without a published five-year list
- type: school-boundary-and-quality-endogeneity
  basis: inferred
  condition: >
    Good-school labels and catchment boundaries are partly based on social-media or
    commercial rankings and can change with school reputation, boundary revisions,
    and local housing demand. A near-school comparison may also capture centrality or
    neighborhood amenities.
  evidence_refs:
  - E4
  possible_diagnostics:
  - freeze rankings and boundaries to pre-treatment dates
  - use alternative ranking sources and school fixed effects
  - compare boundary distance, transit, amenities, and house-age gradients
- type: platform-sample-and-measurement
  basis: reported
  condition: >
    The research sample is scraped from Homelink/Lianjia secondhand-house records,
    not an official transaction census. Listing selection, repeated listings, asking
    versus completed prices, address matching, and platform coverage can change over
    time or across districts.
  evidence_refs:
  - E4
  possible_diagnostics:
  - deduplicate property histories and distinguish asking from completed prices
  - compare with district-level official or alternative-platform series
  - test transaction counts and listing composition around adoption
- type: concurrent-reforms-and-spillovers
  basis: inferred
  condition: >
    Shanghai housing controls, education reforms, school-list changes, subway and
    amenity developments, and parent relocation may coincide with 5Y1F adoption and
    transmit effects to non-adopting wards or babysitting communities.
  evidence_refs:
  - E1
  - E2
  - E4
  possible_diagnostics:
  - audit contemporaneous municipal and district policy calendars
  - test non-adopting wards and alternative local controls
  - model or bound cross-boundary migration and demand substitution
- type: policy-heterogeneity-and-exceptions
  basis: documented
  condition: >
    Districts and schools used different hukou, ownership, co-residence, and sibling
    rules. Treating every address as one identical five-year treatment can hide the
    institutional margin that actually changed.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - retain school-by-year implementation lists
  - stratify by exception and ranking rule where observed
  - report the estimand as the policy-ward market response when address-level data are absent
empirical_requirements:
  contract_version: 1
  population: Secondhand residential properties and households in Shanghai districts with and without 5Y1F adoption
  observation_unit: Property transaction, property-year, or address-by-school enrollment record
  geography_level: Property or residential zone, school catchment, district, and municipality
  time_start: 2012
  time_end: 2019
  minimum_frequency: Annual or transaction-level
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields:
  - transaction or listing price and date
  - stable property or address-history identifier
  - structural housing characteristics
  - district and district adoption year
  - assigned public elementary school and catchment version
  - coordinates or auditable address
  - school-quality category with source date
  - priority-use history or an explicit missingness flag
  required_identifiers:
  - property_id or residential_zone_id
  - address_history_key
  - district_id
  - school_id
  - catchment_version
  - transaction_date
  treatment_key:
  - district_adoption_year
  - post_district_adoption
  - address_school_priority_status
  treatment_source: >
    Dated Shanghai municipal and district enrollment opinions, the Jing'an pilot
    database description, and the Ding–Itoh JUE application. Housing transactions
    and school crosswalks belong in the companion data project Econ Data Know-How;
    this record defines the institution, joins, and identification boundaries rather
    than copying raw data into the variation library.
  measurement_risks:
  - district adoption year is not the same as school-level effective date
  - ward-by-post exposure misclassifies addresses outside the published school list
  - historical school catchments and district boundaries can change
  - five-year priority-use history is absent from most public listings
  - Homelink/Lianjia records may be listings rather than completed transactions and may not be representative
  - school-quality rankings from commercial or social sources are not official test scores
  - concurrent housing and education reforms may be correlated with adoption
evidence:
- id: E1
  source_type: implementation-document
  citation: 'Ministry of Education of the People''s Republic of China. 2015. “依法规范招生 推动优质均衡 提升上海义务教育基本公共服务水平.” Official account of Shanghai''s 2014–2015 enrollment reform and the Jing''an five-year pilot.'
  url: https://hudong.moe.gov.cn/jyb_xwfb/xw_zt/moe_357/jyzt_2015nztzl/2015_zt02/15zt02_gdzcjd/201508/t20150810_199126.html
  date: 2015
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.implementation_start
  - timeline.local_timing
  - assignment.rule
  - assignment.exemptions
  - assignment.compliance
  verification_status: verified
  access_level: official-document
  locator: 'The official account states that Shanghai used exam-free nearby admission and promoted Jing''an''s “one address/household, one student within five years” pilot, with twins and a second child excepted; it does not establish a uniform citywide start date or every school list.'
- id: E2
  source_type: implementation-document
  citation: 'Jing''an District Government. 2017-03-03. “沪幼升小‘五年一户’扩容至8区.” District government account describing the 2016 seven-district coverage and 2017 Yangpu addition, with district-specific rules.'
  url: https://www.jingan.gov.cn/rmtzx/003008/003008003/20170303/2466edb6-006d-48b4-98e9-dff7fa0892e1.html
  date: '2017-03-03'
  supports:
  - timeline.local_timing
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.exemptions
  - assignment.compliance
  verification_status: verified
  access_level: official-document
  locator: 'The page lists Xuhui, Huangpu, Changning, Jing''an, Minhang, Baoshan, and Pudong as the seven districts involved in 2016, Yangpu as the 2017 addition, and describes Baoshan (from 2015), Pudong, and Jing''an implementation differences.'
- id: E3
  source_type: paper
  citation: 'Ding, Kangzhe, and Ryo Itoh. 2023. “JUE Insight: The impact of the school admission restriction policy on the housing market in Shanghai.” Journal of Urban Economics 136:103568. DOI: 10.1016/j.jue.2023.103568.'
  url: https://doi.org/10.1016/j.jue.2023.103568
  date: 2023
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design_applications.treatment_encoding
  - design_applications.comparison
  - design_applications.data_used
  verification_status: reported
  access_level: abstract
  locator: 'Publisher/IDEAS abstract: several Shanghai wards introduced the one-priority-every-five-years rule; the paper uses individual housing prices, good-school districts, nearby babysitting communities, DID, and an event study. The full published article is represented by the author thesis in E4 for the detailed construction.'
- id: E4
  source_type: scholarship
  citation: 'Ding, Kangzhe. 2023. “Empirical studies on policy reform of household registration system, education system, and housing market in China.” Tohoku University doctoral thesis, Chapter 2, pp. 12–27. Author repository version released 2024-09-05.'
  url: https://tohoku.repo.nii.ac.jp/record/2002487/files/230925-Ding-347-1.pdf
  date: 2023
  supports:
  - timeline.local_timing
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.exposure_construction
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - design_applications.population
  - design_applications.outcome
  - design_applications.data_used
  - design_applications.treatment_encoding
  - design_applications.comparison
  - design_applications.empirical_design
  verification_status: verified
  access_level: full-text
  locator: 'Chapter 2, pp. 15–26: district adoption years (Jing''an 2014; Baoshan and Changning 2015; Huangpu, Xuhui, Pudong 2016; Minhang and Yangpu 2017), 183,000 Homelink secondhand-house records from 2012–2019 across 14 districts, 156,396 baseline observations, geocoding, school-quality categories, DID, event study, and 0.7–1.2 km babysitting-community radii. The thesis is an author-repository account of the application, not a public release of raw transactions or priority histories.'
design_applications:
- paper: 'The impact of the school admission restriction policy on the housing market in Shanghai'
  doi: 10.1016/j.jue.2023.103568
  journal: Journal of Urban Economics
  year: 2023
  research_question: >
    How much did restricting the early-resale loophole in public elementary-school
    admission change housing prices in good-school districts and nearby communities?
  population: >
    Secondhand residential properties observed in 14 Shanghai districts from 2012
    through 2019, with the main baseline regression using 156,396 observations.
  outcome: >
    Log transaction price or price per unit area, with supplementary transaction
    counts and location-specific price effects.
  data_used:
  - Homelink/Lianjia open secondhand-house records scraped by the authors
  - Property structural characteristics, transaction date, price, and address
  - Geocoded residential zones and assigned public elementary school
  - School-quality categories from social and commercial education rankings
  - District adoption years and district/year controls
  treatment_encoding: >
    Main treatment is a district-by-post indicator: a transaction in an adopting
    district after its local adoption year. Heterogeneous specifications interact
    post treatment with good-school catchment, a 0.7–1.2 km outside-catchment
    babysitting-community indicator, and ordinary areas. This is a paper-level proxy
    for the address rule; the raw data usually do not reveal the address's remaining
    five-year priority.
  comparison: >
    Pre-adoption transactions in adopting districts and transactions in districts
    without the rule during the study period; within treated districts, compare good
    school catchments, nearby outside-catchment communities, and ordinary areas.
  empirical_design: >
    Difference-in-differences with house characteristics, school-level factors,
    district and year fixed effects, and district-specific trends; event study around
    staggered district adoption years; alternative neighbor radii and school-quality
    interactions.
  assumptions:
  - Adopting and not-yet-adopting districts have comparable pre-trends conditional on controls and trends
  - Adoption-year and school-list coding is accurate enough for the chosen estimand
  - Platform composition and listing measurement do not change differentially at adoption
  - Spillovers and parent sorting do not erase the local market comparison
  threats_addressed:
  - Event-study leads and alternative adoption windows
  - District-specific trends and controls for house and school characteristics
  - Alternative 0.7, 0.85, 1.0, and 1.2 km neighbor radii
  - Separate good-school levels and ordinary areas
  - Transaction-count and spatial-sorting checks
  evidence_refs:
  - E2
  - E3
  - E4
method_transfer: null
readiness_blockers:
- The eight district adoption years are audited at the district-year level, but a property-level serving dataset still needs dated school lists, historical catchment versions, and address-to-school joins.
- The public Homelink/Lianjia records and the paper's cleaned 156,396-observation sample are not archived in this repository; acquisition, deduplication, and platform coverage belong in Econ Data Know-How.
- Most records do not expose the last use of an admission priority, so a district-by-post treatment must not be relabeled as actual address-level eligibility.
- School-quality rankings came from social or commercial sources rather than a single official test-score system; freeze their source date and preserve alternative definitions.
- District-specific hukou, ownership, co-residence, sibling, and school-capacity rules can change the affected population and must be retained in any downstream application.
- Concurrent Shanghai housing, education, school-boundary, and transport reforms can confound a causal interpretation without a dated policy audit.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Shanghai assigns children to nearby public elementary schools using residential address and school-catchment rules. Because school quality differs sharply, a house in a desirable catchment can carry an admission priority and a substantial price premium. Before 5Y1F, a household could exploit a resale loophole: buy a small catchment property, use its priority, resell it, and repeat the cycle or live in a nearby “babysitting community” outside the catchment. The rule studied here closes that particular refresh mechanism; it is not a general school-choice reform.

## What Changed

Starting with Jing'an in 2014, adopting districts limited an address to one same-school public-elementary admission priority in a five-year period, normally regardless of resale or household change. Twins and second children were exceptions, and districts could add hukou, ownership, or co-residence ordering conditions. Baoshan and Changning adopted in 2015, Huangpu, Xuhui, and Pudong in 2016, and Minhang and Yangpu in 2017 [E1; E2; E4]. The rollout therefore has a common institutional idea but district- and school-specific implementation.

## Implementation and Assignment

The legal margin is address-to-school priority history. The published JUE application uses a practical ward-by-post proxy because public housing records usually do not show whether a particular address has already been used in the five-year window. Its baseline treatment is a transaction in an adopting district after that district's adoption year. The paper then separates houses inside good-school catchments, houses within a stated radius outside those catchments, and ordinary locations [E3; E4]. A downstream researcher should retain both layers: the audited local rule and the paper's coarser empirical encoding.

## Why This Creates Empirical Variation

Districts did not adopt simultaneously, creating a staggered before/after contrast across Shanghai's 14-district housing market. Within adopting districts, the policy should matter most where admission priority is valuable: good-school catchments. The nearby outside-catchment “babysitting” areas provide a mechanism-relevant spillover contrast because their demand partly came from families who wanted the school but planned to resell the priority house. The author application reports higher prices in good-school areas and lower prices in nearby babysitting communities after adoption, with an immediate response that moderates in the short run [E3; E4].

## Identification Risks

The ward-by-post indicator is not the same as actual legal exposure. A district can include schools that were not yet on the five-year list, while admission may depend on hukou timing, ownership, residence, school capacity, and sibling status. Adoption may also respond to local housing pressure, school quality, or political priorities. Homelink/Lianjia records are a scraped platform sample, and school rankings and boundaries may be measured with error. Parents and speculators can move to other wards or nearby communities, so a nominal control may be affected. The design is useful when these boundaries are explicit; it should not be presented as a citywide exogenous shock with perfect compliance.

## Data Requirements

A reusable implementation needs a dated district adoption table; school-by-year enrollment lists and catchment polygons; stable property or residential-zone identifiers; transaction or listing date, price, and house characteristics; geocoded addresses; assigned school and school quality; and, for a stronger property-level treatment, the last five-year priority-use date. The housing records and joinable data belong in `Econ Data Know-How`; this variation record stores the policy meaning, identifiers, and evidence limits so the two projects remain complementary.

## Evidence Notes

E1 establishes the Shanghai enrollment framework and Jing'an pilot while explicitly leaving the citywide start date and school lists open. E2 is a dated district-government account that records the 2016 seven-district coverage, 2017 Yangpu addition, and important district differences. E3 is the published JUE metadata and abstract, which establishes the research question and qualitative design. E4 is the authors' full doctoral-thesis chapter: it provides the adoption-year table, Homelink data construction, sample size, geocoding, school-quality coding, DID/event-study setup, and neighbor radii. E4 establishes how the paper constructed its research proxy; it does not make the raw transaction data or five-year priority histories publicly reproducible.
