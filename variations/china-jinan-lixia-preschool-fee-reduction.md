---
schema_version: 2
id: china-jinan-lixia-preschool-fee-reduction
name: Jinan Lixia Preschool Education Fee Reduction and Exemption
aliases:
- Lixia preschool fee waiver
- Jinan Lixia preschool R&E program
- 历下区幼儿园保教费减免
- 历下区学前教育费用减免政策
status: grounded
provenance:
  task_id: task-e6f648e1ff1b
scope:
  country: China
  regions:
  - Lixia District, Jinan, Shandong, and adjacent urban districts used by the border comparison
  domains:
  - regional-economics
  - urban-economics
  - housing
  - education
  - public-finance
  - spatial-economics
  - inequality
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: >
    This record captures a district-funded preschool fee-reduction and exemption
    program, not a nationwide preschool subsidy or a generic education-quality
    change. Its research value is the administrative boundary between Lixia and
    neighboring Jinan districts and the residence-based eligibility that the 2024
    RSUE paper uses to study capitalization into nearby house prices and rents.
identity:
  instrument: >
    Lixia District's Education Fee Reduction and Exemption Program for preschool
    childcare. For qualifying children, the district paid or waived the preschool
    保教费 component by kindergarten category. Meals, optional services, and fees
    above the covered public-kindergarten standard were not automatically the same
    treatment. The program is distinct from the ordinary Jinan fee schedule,
    national hardship-child aid, and later citywide preschool reforms.
  authority: >
    The Lixia district government and education bureau administered the local
    program and reviewed applications through kindergartens. The 2013 Jinan fee
    notice supplies the citywide fee categories and the Lixia-covered area;
    contemporaneous reports describe the district's 2014 fiscal commitment and
    eligibility rules. A 2020 Jinan notice confirms that the pre-existing Lixia
    exemption policy was still being continued during the pandemic. These sources
    establish an administered local program, not randomized assignment.
  legal_identifiers:
  - Jinan Municipal Price, Finance, and Education Bureaus notice on preschool fees, 2013-01-29 (济价费字〔2013〕28号)
  - Lixia District 2014 preschool fee-reduction implementation rules and accompanying parent letter
  - Jinan preschool-fee notice, 2020-05-12, stating that the existing Lixia policy continues
  - Lixia District confirmation that the policy was cancelled in 2021 after a compliance review
  implementation_regime: >
    The district intervention operated through Lixia-registered kindergartens with
    admission qualifications, including public, public-nature, inclusive private,
    and other private kindergartens. Covered amounts followed Jinan kindergarten
    categories. Eligibility was not simply any child attending a Lixia school: the
    rules distinguished Lixia hukou, property and residence, qualifying migrant-
    worker residence, and preschool age. The initial survey covered 83 registered
    kindergartens; later public lists have different counts as registration changed.
  assignment_mechanism: >
    Institutional assignment followed the child's qualifying residence and age,
    processed by the kindergarten and Lixia education bureau. The paper's housing
    application uses the Lixia administrative boundary as a spatial proxy: a house
    inside Lixia could be associated with access to the program, while a nearby house
    outside could not. Residence duration, hukou, property, school registration,
    and approval are separate from a house's geometric side of the boundary.
  parent: null
  related_variations:
  - china-shanghai-five-year-one-family-school-admission
timeline:
  announcement: '2014-01'
  effective: null
  implementation_start: 2014
  implementation_end: 2021
  local_timing: >
    A January 2014 district民生 announcement and contemporaneous local report say
    that the reduction began in January and that already-paid fees could be returned
    or credited. Detailed implementation guidance and public-list review followed in
    February: the first list was to be posted on February 25, and the paper describes
    the local experiment as launched in February 2014. Keep the planned/administrative
    January clock and the public-review/paper February clock separate. An official
    2020 notice still refers to the original Lixia policy, and the district confirmed
    cancellation in August 2021.
  anticipation: >
    The program was announced in January, discussed by parents and kindergartens,
    and implemented through application and public-list procedures before the paper's
    February date. Households could sort, transact, or change kindergarten plans in
    response to the announcement; a post-February indicator is not proof of no early
    market adjustment.
  last_verified: '2026-08-13'
assignment:
  unit: >
    The institutional unit is an eligible preschool child or household served by a
    Lixia-registered kindergarten. The paper's design unit is a geocoded secondhand
    house transaction or rental observation near the Lixia border; a beneficiary and
    a property-side exposure must remain distinct.
  treated: >
    For the paper's spatial encoding, a property is treated when it lies inside the
    historical Lixia boundary and the observation is after the chosen 2014 clock.
    Institutionally, the benefit also requires age, residence or hukou, kindergarten
    registration, and application conditions. Inside-by-post is a local market
    exposure, not a perfect take-up measure.
  comparison_pool: >
    The paper compares observations just outside Lixia with observations just inside
    it, using 500-metre and 750-metre buffers on each side. Nearby outside properties
    are a boundary counterfactual conditional on continuity and no other concurrent
    local program; they are not guaranteed untreated because families, schools, rents,
    and services cross the district line.
  rule: >
    Preserve the historical district polygon and geocode every property or rental.
    Construct side-of-boundary, distance, buffer width, and post fields separately,
    then estimate inside-by-post rather than assigning treatment from a current map.
    Keep child eligibility and property side linked but different. The paper's placebo
    moves the boundary 10 km northwest and shifts the policy date; these are diagnostics,
    not alternative legal boundaries.
  intensity: >
    The institutional margin is fee coverage by kindergarten category. Public
    kindergartens could have covered保教费 waived; public-nature and private categories
    received reductions tied to the public standard, while category-specific charges
    and later fee revisions changed amounts. Category, eligible-child share, and
    residence certainty are possible secondary intensities, not substitutes for the
    binary paper exposure.
  exemptions:
  - Children younger than three or outside the annual 3-6 preschool enrollment rule
  - Children without the reported Lixia hukou, property/residence, or qualifying migrant-worker evidence
  - Children not living with the qualifying parent or without an approved application
  - Fees outside covered保教费, including meals and optional services
  - Properties outside Lixia, without a stable historical geocode, or outside the audited buffer
  compliance: >
    The district paid or waived a fee at the kindergarten rather than sending an
    unconditional transfer to every household. Application, residence, age, and
    kindergarten-category checks created incomplete take-up and sorting. A property
    inside Lixia can receive a price signal even when the buyer has no eligible child.
  exposure_construction: >
    Build a dated Lixia boundary crosswalk, calculate signed distance and side for
    each sale and rental, and retain 500-metre and 750-metre flags. Add transaction
    month, structural controls, and January announcement, February review, chosen
    post date, and 2021 cancellation as separate fields. Beneficiary studies require
    child age, residence duration, hukou, kindergarten, and application records.
  required_identifiers:
  - Historical Lixia and neighboring-district boundary polygon with source date
  - Stable property, compound, or geocoded address identifier
  - Sale or rental date, price or rent, and structural controls
  - Signed distance and 500-metre/750-metre buffer flag
  - Child age, residence duration, hukou/property or migrant-worker eligibility, and kindergarten identifier
  - Kindergarten category and covered fee standard by date
  - Application/review status or fee-waiver amount where individual take-up is claimed
  - Boundary version and crosswalk for post-2014 district changes
  spillovers: >
    The program can capitalize into Lixia prices and rents, move eligible families
    across the line, and alter demand for neighboring schools and rental units.
    Officials may change kindergarten supply or fees in response. Citywide education
    reforms, housing cycles, hukou and school-access rules, and other Jinan services
    can affect both sides; a boundary estimate is local equilibrium incidence, not a
    no-spillover treatment effect.
research_compatibility:
  outcome_domains:
  - secondhand housing prices and price per square meter
  - residential rents and landlord/tenant incidence
  - transaction volume, listing composition, and residential sorting
  - capitalization of preschool and local public-service benefits
  - preschool enrollment, kindergarten finance, and household expenditure
  - distribution between incumbent owners, buyers, and renters
  affected_populations:
  - Preschool-age children and households in Lixia
  - Qualifying migrant-worker and non-local-hukou families
  - Homeowners, buyers, and renters near the district boundary
  - Lixia public and private kindergartens
  - Neighboring-district households and housing markets
  mechanism_channels:
  - Lower expected preschool fees for eligible households
  - Capitalization into house prices and rents
  - Residential sorting across the administrative boundary
  - Kindergarten fee-category and supply responses
  - Distribution from public finance to owners and landlords through land values
  best_for:
  - Boundary difference-in-differences of local public-service capitalization
  - Hedonic price and rent incidence near the Lixia border
  - Incumbent-owner, buyer, and tenant incidence
  - Audited local-policy comparisons that preserve residence eligibility and spillovers
  not_good_for:
  - Calling the program random or nationwide
  - Inferring child enrollment, learning, or welfare from house prices alone
  - Calling every property inside Lixia a beneficiary or every outside property untreated
  - Ignoring the January-versus-February timing distinction or 2021 cancellation
  - Combining this program with later universal preschool subsidies
design:
  claim_type: causal
  affordances:
  - A single district boundary with a described adjacent comparison area
  - January/February 2014 implementation and application timing
  - Geocoded secondhand sale and rental observations on both sides
  - 500-metre and 750-metre bands plus placebo boundary/date checks
  - A residence-based benefit that can affect owners and renters
  candidate_designs:
  - Hedonic boundary difference-in-differences using inside-by-post exposure
  - Geographic boundary design with local distance controls and alternative buffers
  - Separate price and rent incidence for owners, buyers, and tenants
  - Beneficiary-level fee-incidence design after recovering application records
  - Sorting and transaction-composition analysis around announcement and review dates
  identifying_variation: >
    The paper's contrast is the change in the housing-price or rent gap between
    properties just inside and just outside Lixia after the local program begins.
    The policy boundary supplies the spatial discontinuity and the pre/post dimension
    absorbs fixed border differences. The estimand is local only under boundary
    continuity, stable measurement, and no differential concurrent shock at the line.
  primary_strategy: >
    Tang, Chen, Zhang, and coauthors use a hedonic DID with secondhand transaction and
    rental data near the Lixia border, comparing 500-metre and 750-metre bands around
    the 2014 program. They report roughly 5-7 percent higher prices and 10-13 percent
    higher rents on the eligible side. Artificial-boundary and fake-date placebos are
    falsification checks, not proof that the true boundary was unselected.
  estimand: >
    The local capitalization effect of Lixia's fee-reduction program on nearby
    secondhand house prices or rents, within the audited border bands, relative to
    the adjacent outside side and selected pre-period. It is not a direct effect on
    preschool attendance, child outcomes, or all-Jinan welfare.
  treatment_variable: >
    Inside_Lixia multiplied by post, with January announcement and February review or
    launch recorded as separate timing specifications. Beneficiary work should add
    child eligibility and approved fee reduction rather than silently equating them
    with the property-side indicator.
  comparison_logic: >
    Use properties outside Lixia within the corresponding 500-metre or 750-metre band
    as the local comparison and test pre-period smoothness. The 10-kilometre northwest
    artificial boundary and fake-date tests are diagnostics; they do not remove
    cross-border sorting, district-wide trends, or simultaneous policies.
  estimation_notes: >
    Keep sale and rental estimates separate, report both paper and contemporaneous
    timing clocks, and preserve the actual historical boundary version. Interpret the
    result as market capitalization and incidence, not as the policy's full fiscal or
    child-development effect.
  assumptions:
  - Housing characteristics and unobserved amenities vary smoothly at the boundary absent the program
  - No other district-specific policy or construction shock begins at the same line and date
  - Geocoder, boundary, transaction/rental platform, and buffer sample remain comparable
  - January announcement and February review do not create unmeasured differential anticipation beyond the chosen estimand
  - Observed housing markets capture the intended capitalization margin
  - Cross-border sorting and spillovers are either limited or interpreted as equilibrium incidence
  diagnostics:
  - Pre-trend and boundary-smoothness plots for prices and rents
  - 500-metre versus 750-metre bands and alternative distance controls
  - Artificial boundary shifted 10 km northwest and simulated dates
  - Separate sale/rent, house-size, and transaction-composition checks
  - Sensitivity to January announcement, February review, and 2021 cancellation
threats:
- type: boundary-sorting-and-eligibility
  basis: reported
  condition: >
    Lixia differs from neighboring districts and households can sort by residence,
    property, hukou, school access, or residence duration; a property-side indicator
    is not individual fee eligibility.
  evidence_refs:
  - E2
  - E5
  possible_diagnostics:
  - pre-period balance and boundary smoothness
  - child-level eligibility and application records
  - transaction and migration composition checks
- type: concurrent-local-policy
  basis: inferred
  condition: >
    Jinan housing, education, kindergarten-supply, and fee policies may change at
    the same time or differentially across the district boundary.
  evidence_refs:
  - E1
  - E3
  possible_diagnostics:
  - dated local-policy inventory
  - boundary-specific event studies and alternative post clocks
  - leave-one-neighborhood-out estimates
- type: boundary-and-platform-measurement
  basis: reported
  condition: >
    Historical district polygons, geocodes, and sale/rental platform coverage may be
    measured with error or change at the policy date.
  evidence_refs:
  - E5
  possible_diagnostics:
  - polygon-version audit and alternative geocoders
  - 500-metre versus 750-metre bands
  - platform and listing-composition checks
- type: incomplete-take-up-and-category-coverage
  basis: reported
  condition: >
    Application review, age and residence conditions, kindergarten categories, and
    uncovered meals or optional charges mean that inside-Lixia exposure is imperfect.
  evidence_refs:
  - E2
  - E4
  possible_diagnostics:
  - category-specific fee amounts and approved lists
  - beneficiary-level take-up when records exist
- type: cross-border-spillover
  basis: inferred
  condition: >
    Price capitalization, tenant movement, and school or housing substitution can
    affect the outside side and adjacent districts.
  evidence_refs:
  - E5
  possible_diagnostics:
  - wider spatial rings and neighboring-district outcomes
  - rent, sale, and transaction-volume heterogeneity
- type: announcement-versus-review-timing
  basis: documented
  condition: >
    The January announcement and February public review or paper launch allow
    anticipation before the chosen post indicator.
  evidence_refs:
  - E2
  - E5
  possible_diagnostics:
  - separate January and February event clocks
  - lead coefficients and fake-date placebos
empirical_requirements:
  contract_version: 1
  population: Properties, households, and preschool-age children in and near Lixia District
  observation_unit: Property transaction or rental observation; optionally child-kindergarten application
  geography_level: District boundary, property or residential compound, and kindergarten
  time_start: 2011
  time_end: 2021
  minimum_frequency: Monthly or quarterly
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields:
  - Historical Lixia boundary and district version
  - Property or compound identifier and auditable geocode
  - Sale/rental date, price/rent, and structural characteristics
  - Signed boundary distance and 500-metre/750-metre flags
  - Child age, residence or hukou evidence, kindergarten, and fee category for beneficiary work
  required_identifiers:
  - property_id or compound_id
  - transaction_date or rental_month
  - district_boundary_version
  - kindergarten_id and child_application_id where applicable
  treatment_key:
  - inside_lixia
  - post_announcement_or_review
  - signed_distance_to_boundary
  treatment_source: >
    Jinan and Lixia fee notices, the contemporaneous implementation reports, the
    paper's policy clock, and an auditable historical district polygon. Housing data
    acquisition and deduplication belong in Econ Data Know-How.
  measurement_risks:
  - January announcement, February review, and paper launch are different clocks
  - Property side is not individual eligibility or fee take-up
  - Historical boundary and geocoder may be inconsistent
  - Listing or rental platform coverage may change at the policy date
  - Current fee schedules cannot be backfilled to 2014 without source dates
evidence:
- id: E1
  source_type: policy-document
  citation: "Jinan Municipal Price, Finance, and Education Bureaus. 2013-01-29. Notice on regulating preschool charges (济价费字〔2013〕28号)."
  url: https://www.jinan.gov.cn/col25693/art/2013/art_25693_2304703.html
  date: '2013-01-29'
  supports:
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: >
    The official notice defines Jinan保教费, public/private categories, fee ceilings,
    ordinary hardship aid, and the five urban districts including Lixia. It does not
    establish the special Lixia 2014 eligibility list or housing boundary treatment.
- id: E2
  source_type: other
  citation: 'Qilu Evening News. 2014-01-07. Preschool fee reduction begins in Lixia; prior fees could be refunded or credited.'
  url: https://epaper.qlwb.com.cn/Qlwb/PDF/20140107/B03.pdf
  date: '2014-01-07'
  supports:
  - identity.instrument
  - timeline.announcement
  - timeline.implementation_start
  - assignment.rule
  - assignment.treated
  - assignment.exemptions
  - assignment.compliance
  verification_status: verified
  access_level: full-text
  locator: >
    A contemporaneous local report quotes Lixia education officials on the January
    start, two-year residence/hukou conditions, category-specific coverage, and fee
    refunds. It is implementation reporting, not the original district legal notice.
- id: E3
  source_type: policy-document
  citation: 'Jinan Development and Reform, Education, Finance, and Market Regulation Bureaus. 2020-05-12. Notice on preschool charges during COVID-19 prevention and control.'
  url: https://jncz.jinan.gov.cn/attach/0/75555e6b3f8f4d40ac557e7b288b7161.pdf
  date: '2020-05-12'
  supports:
  - identity.instrument
  - identity.authority
  - timeline.implementation_start
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: >
    The official notice says the pre-existing Lixia preschool-fee reduction policy
    continues after the COVID fee suspension. It confirms an established local regime
    by 2020 but does not reproduce the original 2014 rules or beneficiary list.
- id: E4
  source_type: other
  citation: 'The Paper. 2021-08-03. Lixia preschool fee-reduction policy cancelled after a compliance review.'
  url: https://m.thepaper.cn/newsDetail_forward_13865811
  date: '2021-08-03'
  supports:
  - identity.instrument
  - timeline.implementation_end
  - assignment.rule
  verification_status: verified
  access_level: full-text
  locator: >
    The report quotes Lixia education officials confirming cancellation and cites a
    May 2020 district document describing annual fiscal funding since 2014 and
    category-based reductions for resident, qualifying non-hukou, and migrant-worker
    families. It does not supply the original district implementation notice.
- id: E5
  source_type: paper
  citation: 'Tang, Yugang, Meng-Wei Chen, Hehe Zhang, et al. 2024. “A study on the benefit incidence of a place-based education fee reduction program: Evidence from a local housing market in China.” Regional Science and Urban Economics 106:104010. DOI: 10.1016/j.regsciurbeco.2024.104010.'
  url: https://www.sciencedirect.com/science/article/pii/S0166046224000346
  date: 2024
  supports:
  - identity.instrument
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.implementation_start
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
  verification_status: verified
  access_level: abstract
  locator: >
    Publisher preview and indexed article text establish the February 2014 program,
    residence-based eligibility, 500-metre and 750-metre border bands, hedonic DID,
    secondhand sales and rents, artificial-boundary and fake-date placebos, and the
    reported 5-7 percent price and 10-13 percent rent effects. They do not expose raw
    transaction files or a complete legal appendix.
- id: E6
  source_type: paper
  citation: 'DOI and IDEAS/RePEc metadata for Tang, Chen, Zhang, et al., Regional Science and Urban Economics 106 (2024), article 104010.'
  url: https://doi.org/10.1016/j.regsciurbeco.2024.104010
  date: 2024
  supports:
  - identity.instrument
  - design.primary_strategy
  - design.estimand
  verification_status: verified
  access_level: metadata
  locator: 'Metadata establishes article identity, journal, volume, year, and DOI; substantive institutional and design claims come from E1-E5.'
design_applications:
- paper: 'A study on the benefit incidence of a place-based education fee reduction program: Evidence from a local housing market in China'
  doi: 10.1016/j.regsciurbeco.2024.104010
  journal: Regional Science and Urban Economics
  year: 2024
  research_question: How did Lixia's preschool fee-reduction program capitalize into nearby house prices and rents, and who captured or paid for the benefit?
  population: Households, buyers, renters, landlords, and preschool-age families in and around Lixia District, Jinan.
  outcome: Secondhand house prices and rents near the Lixia administrative boundary, with distributional interpretation for owners, buyers, and tenants.
  data_used:
  - Geocoded secondhand house transaction data near the Lixia border
  - Rental observations near the same border
  - Property characteristics, dates, prices/rents, and boundary distances
  - Lixia policy timing, fee standards, and eligibility information
  treatment_encoding: Inside-Lixia property multiplied by a post-2014 program indicator in 500-metre and 750-metre bands; January and February clocks remain separate checks.
  comparison: Properties outside Lixia within the corresponding border band, with artificial-boundary and simulated-date placebo comparisons.
  empirical_design: Hedonic difference-in-differences combined with administrative-boundary comparison and falsification tests.
  assumptions:
  - Housing characteristics and unobserved amenities are locally smooth at the boundary absent the program.
  - No other policy or construction shock changes differentially at the Lixia border in the same window.
  - Transaction and rental samples remain comparable across the policy date.
  - Inside-by-post captures capitalization rather than direct individual take-up.
  threats_addressed:
  - Artificial boundary shifted 10 km northwest
  - Simulated policy implementation dates
  - Alternative 500-metre and 750-metre border bands
  - Separate price/rent incidence and house-size heterogeneity
  evidence_refs:
  - E2
  - E3
  - E5
  - E6
method_transfer: null
readiness_blockers:
- The original 2014 district implementation notice and complete legal appendix were not available in the inspected public sources; reports and later official acknowledgements establish the rule, but a machine-readable eligibility table still needs archival recovery.
- The paper's cleaned housing/rental files, platform provenance, and historical Lixia boundary crosswalk are not archived here; acquisition and deduplication belong in Econ Data Know-How.
- The housing-side proxy does not reveal each child's residence duration, hukou, kindergarten registration, application, or actual fee waiver.
- January announcement, February review/publication, and paper launch must be compared before a narrow event-time estimand is chosen.
- Boundary sorting, concurrent Jinan housing/preschool changes, and spillovers prevent treating the contrast as intrinsically exogenous.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Jinan's ordinary preschool fee system classified kindergartens by ownership, funding,
and quality category. In early 2014, Lixia District layered a local fiscal program
on that schedule: qualifying preschool children received a reduction or waiver of
the 保教费 component, while the district reimbursed kindergartens according to the
public-category standard. The local object is therefore a price-and-eligibility
intervention, not a measured improvement in teaching quality [E1; E2].

## What Changed

The district announced the program in January 2014 and began the application and
public-review process shortly thereafter. The paper describes a February launch;
the local implementation report says January and explains that fees already paid
could be refunded or credited. Announcement, administrative review, and the paper's
coding date should remain separate rather than being collapsed into one precise day
[E2; E5]. The policy continued for several years and was confirmed cancelled in 2021
after a compliance review [E3; E4].

## Implementation and Assignment

The eligible population was defined through Lixia residence and preschool age. The
reported rules included Lixia-hukou children, qualifying children of non-local-hukou
families with property and sustained residence, and children of migrant workers who
worked in Lixia and met the residence condition. Children below the specified age,
families without the required evidence, and charges outside the covered 保教费 were
not equivalent to treated observations. Kindergartens reviewed applications and the
education bureau rechecked and published the lists [E2; E4].

The 2024 RSUE application uses a deliberately observable object: houses inside
versus outside the Lixia administrative boundary. That boundary is a useful market
exposure proxy because the paper reports no simultaneous neighboring-district
program, but it cannot establish that a given buyer or renter qualified for the
subsidy [E5].

## Why This Creates Empirical Variation

Properties close to the boundary share much of the surrounding urban market while
falling on different sides of the district's local program. A pre/post comparison of
sale prices and rents can estimate a local capitalization effect if the boundary is
stable and no other intervention moves at the same line. The paper uses 500-metre and
750-metre bands and reports roughly 5-7 percent higher prices and 10-13 percent higher
rents on the eligible side. This is a market-incidence estimate: incumbent owners
and landlords may gain, while new buyers and tenants may pay more [E5].

## Identification Risks

Lixia was a selected district, not a randomly drawn jurisdiction. It may differ from
neighbors in income, schools, land supply, housing demand, and local policy. The
January announcement could move prices before the paper's February clock. Families
may sort across the boundary, and the policy can itself change that sorting. Housing
listings and rents may reflect platform composition rather than every market
transaction. Artificial-boundary and fake-date tests are useful falsifications, but
they do not prove that the true boundary had no concurrent change [E5].

The 2020 official notice confirms continuation of the old Lixia policy but does not
replace the missing original 2014 legal appendix. A downstream user should recover
that appendix before making beneficiary-level claims and use the housing proxy only
for the local capitalization estimand [E3].

## Data Requirements

The minimum housing contract contains a historical Lixia polygon, a stable geocoded
property or compound identifier, transaction or rental date, price or rent,
structural controls, signed distance to the border, and the 500-metre/750-metre
sample flag. A beneficiary-level study additionally needs child age, hukou or
residence duration, property/rental evidence, kindergarten category, application
status, and fee-waiver amount. Housing acquisition and crosswalk work belongs in
`Econ Data Know-How`; this record preserves the policy meaning and join contract.

## Evidence Notes

E1 is the official 2013 Jinan fee notice. It establishes baseline fee categories,
covered urban districts, and ordinary hardship exemptions, but not the special Lixia
2014 program. E2 is a contemporaneous local newspaper report quoting Lixia education
officials; it establishes the January implementation report, fee mechanism, and
residence conditions while remaining a report rather than the original legal notice.
E3 is the official 2020 Jinan notice that says the existing Lixia exemption policy
continued; it verifies the regime's existence by 2020 but does not reproduce the
original rule. E4 is a later report quoting the district's cancellation and citing
the 2020 district material, supporting the 2014-to-2021 duration and category-based
standard. E5 is the 2024 RSUE article preview/indexed text and establishes the paper's
boundary, buffers, data objects, falsification tests, and reported estimates; it is
not evidence that the subsidy was random. E6 is metadata only and confirms article
identity and DOI.

The record is grounded as a Chinese local place-based fee intervention with a usable
housing-boundary application, while leaving the original legal appendix, individual
take-up, and exact timing clock visible as blockers. It should be recommended for a
conditional local capitalization or incidence design, not as a universal preschool
causal shock.
