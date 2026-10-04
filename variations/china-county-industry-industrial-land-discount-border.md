---
schema_version: 2
id: china-county-industry-industrial-land-discount-border
name: China County-Industry Industrial-Land Discounts at County Borders
aliases:
- 县域产业专门化与工业用地低价出让
- Local industrial favoritism in Chinese land allocation
status: grounded
provenance:
  task_id: task-d8868e2fb797
scope:
  country: China
  regions: [Mainland county-level jurisdictions with observed industrial land transactions]
  domains: [urban-economics, regional-economics, development-economics, industrial-policy, land]
  variation_type: boundary-discontinuity
  knowledge_role: china-variation
  china_relevance: >
    Chinese county governments allocate industrial land within a national minimum-price
    regime. Tian, Wang and Zhang study whether the same industry's nearby land sales
    receive different discounts across county borders according to pre-existing local
    industry specialization. The observed exposure is a mainland county-industry
    pricing choice, not a generic spatial-RD method or a national reform dummy.
identity:
  instrument: County-industry-specific discretionary discounting of industrial land transactions relative to the applicable regulatory minimum
  authority: County-level land-supplying governments operating under central and provincial industrial-land pricing rules
  legal_identifiers:
  - 国土资发〔2006〕307号, 全国工业用地出让最低价标准, effective 2007-01-01
  - 国土资发〔2009〕56号, industrial-land minimum-price implementation adjustments, signed 2009-05-11
  implementation_regime: >
    National county/land-grade floors constrain industrial land reserve prices, while
    local governments administer sales. The 2009 notice permits a reserve price as
    low as 70 percent of the applicable floor for provincially prioritized AND
    sufficiently land-intensive industrial projects, subject to a cost floor; it
    also provides other exceptions and a separate narrow county-standard adjustment
    route. A transaction observed below the benchmark does not itself reveal its
    approval pathway, legal compliance, or the buyer's formal eligibility.
  assignment_mechanism: >
    Firms buy parcels in county jurisdictions. Local government priority, potentially
    related to the county's pre-existing specialization in the buyer's industry,
    can alter the price of an offered industrial parcel. The paper compares parcels
    for the same two-digit industry near opposite sides of a county border, focusing
    on sales below the regulatory benchmark; neither specialization nor the sale
    location was randomly assigned.
  parent: null
  related_variations: [china-industrial-land-minimum-investment-intensity, china-industrial-land-supply-target-area-churn]
timeline:
  announcement: null
  effective: null
  implementation_start: '2007-07'
  implementation_end: '2019-12'
  local_timing: >
    July 2007-December 2019 is the paper's observable land-transaction window,
    not a common policy start and end. The national floor took effect on 2007-01-01;
    the distinct 2009 implementation notice later added specified discount routes.
    County-industry pricing decisions occur on individual land-sale dates.
  anticipation: Buyers and land authorities may negotiate, select parcels, or anticipate priorities before the recorded transaction.
  last_verified: '2026-10-02'
assignment:
  unit: Industrial land sale, linked to its county and two-digit buyer industry
  treated: Below-benchmark industrial parcels in county-industries with greater pre-existing own-industry specialization, interpreted as a continuous comparison rather than a binary eligibility class
  comparison_pool: Same-industry below-benchmark industrial sales near the other side of a stable county border, conditional on observed parcel and local attributes
  rule: >
    Join each sale's county and date to the applicable national floor and identify
    sales priced strictly below that benchmark; attach county-industry employment
    specialization from the prior 2004 or 2008 Economic Census and locate parcels
    relative to a verified county border. This is the paper's analytical sample
    rule, not a statutory rule assigning firms to discounts.
  intensity: Own-industry specialization = county industry employment share divided by the national industry employment share; observed sale-price gap from the regulatory benchmark is an outcome/selection margin
  exemptions:
  - The 2009 notice permits a 70-percent reserve-price floor for provincially prioritized and land-intensive industrial projects meeting both conditions, subject to actual cost.
  - Agricultural-product initial-processing projects and specified western/central-region unused land have different conditional floors under the same notice.
  compliance: Below-benchmark observed prices cannot be classified as lawful concessions or violations without project-level approvals and cost/eligibility facts.
  exposure_construction: >
    Form county-industry specialization using the 2004 census for 2007-2008 sales
    and the 2008 census for later sales, as in the paper. Calculate each parcel's
    applicable benchmark and distance/side relative to a historically stable
    county border; keep price, benchmark, and specialization as distinct variables.
  required_identifiers: [Parcel or transaction ID, sale date, historical county, buyer two-digit industry, county-border pair, census county-industry]
  spillovers: Firms, bidders, and parcels may sort across nearby counties; adjacent counties' industrial structure and policies can affect each other's prices.
research_compatibility:
  outcome_domains: [Industrial land pricing, Local industrial favoritism, Spatial industrial allocation]
  affected_populations: [Industrial land purchasers, Local land-supplying governments]
  mechanism_channels: [County industrial priorities, Selective land-price concessions, Jurisdictional competition]
  best_for:
  - Studying whether local specialization predicts stronger industrial-land price concessions within the same industry and border area
  not_good_for:
  - Treating 2007 or 2009 as a uniform treatment date for this county-industry pricing margin
  - Treating specialization as randomized, every low-price sale as illegal, or the estimated price gradient as a demonstrated effect on firm productivity
design:
  claim_type: reduced-form
  affordances: [Within-industry adjacent-county price contrasts, Multiple county-border bandwidths, Above-floor falsification sample]
  candidate_designs: [Conditional county-border discontinuity in industrial land prices]
  identifying_variation: >
    A county border changes the land-supplying authority and its industry priority
    while nearby parcels for the same industry may share smoothly varying local
    production amenities. Across-border differences in pre-existing county-industry
    specialization index the authority's hypothesized preference, not a legal
    assignment cutoff or randomized treatment.
  primary_strategy: >
    In below-floor sales, regress log parcel sale price on county-industry
    specialization, using same-industry border comparisons with border-by-industry,
    industry-by-year and prefecture effects, parcel/county controls and spatial
    trends. The author manuscript's main 5-km specification has 13,615 sales.
  estimand: Conditional within-border-industry price gradient associated with county-industry specialization among observed below-benchmark sales
  treatment_variable: Pre-existing own-industry county specialization, with the below-benchmark restriction kept separate from treatment
  comparison_logic: Compare same-industry parcels within 5 km of the same stable county border on opposite sides, then test narrower/wider bandwidths and above-floor sales.
  estimation_notes: >
    The manuscript uses 2004 census exposure for 2007-2008 and 2008 census
    thereafter, GB/T4754-2002 two-digit industries, border-industry clustered
    standard errors, and official land-grade controls. Its 10-percent statement
    is a reported association for a one-standard-deviation specialization change
    within the 5-km below-floor sample, not an experimentally identified subsidy effect.
  assumptions:
  - Conditional same-industry demand and other production amenities vary smoothly at the county border.
  - Other county-border institutions do not create the same industry-specific price jump correlated with specialization.
  - Sale selection, parcel composition, and geocoding error do not generate the observed gradient.
  diagnostics: [Residential land-price and 2005 night-light continuity, Narrower border bandwidths, Mountain/water-border exclusions, Above-floor comparison, Below-floor selection models, Post-2008 census-consistent subsample]
threats:
- type: Nonrandom sale and discount selection
  basis: documented
  condition: The main regression conditions on the roughly 16 percent of industrial land sales observed below the regulatory benchmark; selection into that subset can vary with county-industry demand and policy.
  evidence_refs: [E3]
  possible_diagnostics: [Model below-floor selection using all sales, Compare above-floor transactions, Inspect parcel and buyer composition]
- type: County-border confounding
  basis: inferred
  condition: Taxation, enforcement, land grades, and development-zone policy may also change at county borders and correlate with local specialization; residential prices and night lights test only selected observable implications.
  evidence_refs: [E3]
  possible_diagnostics: [Within-prefecture borders, Border-side policy inventory, Residential price and night-light continuity]
- type: Legal-status and measurement ambiguity
  basis: documented
  condition: The 2009 notice has conditional lawful reductions as well as liability for violating minimum-price rules; a price below the base benchmark does not reveal formal eligibility, approval, or illegality.
  evidence_refs: [E2]
  possible_diagnostics: [Retrieve project priority and land-intensity approvals before making legal claims]
empirical_requirements:
  contract_version: 1
  population: Mainland industrial land sales with a two-digit buyer industry, a historical county assignment, and a linkable regulatory price benchmark
  observation_unit: Industrial land sale or parcel
  geography_level: Historical county and county-border pair
  time_start: '2007-07'
  time_end: '2019-12'
  minimum_frequency: Dated transactions with census-period county-industry exposures
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields: [Sale price per square metre, Regulatory floor per square metre, Lot area, Sale date, Parcel location, Buyer two-digit industry, County-industry employment shares, National industry employment shares, Official land grade]
  required_identifiers: [Land transaction ID, County and border-pair ID, Two-digit industry code/version, Census county-industry key, Sale date]
  treatment_key: [Historical county, Two-digit industry, Pre-sale census wave]
  treatment_source: 2004/2008 Economic Census employment structure joined to official land sales and historical minimum-price schedules; source access or joins are not promised here
  measurement_risks: [Baidu-centroid geocoding error near borders, Time-varying administrative boundaries, Incorrect floor or land-grade version, Changing industry classifications, Conditioning on realized sales]
evidence:
- id: E1
  source_type: policy-document
  citation: Ministry of Land and Resources, 全国工业用地出让最低价标准, 国土资发〔2006〕307号, Ministry of Commerce policy database reproduction.
  url: https://policy.mofcom.gov.cn/claw/clawContent.shtml?id=12663
  date: '2006-12'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.local_timing, assignment.rule]
  verification_status: verified
  access_level: official-document
  locator: Notice opening provisions and attached national minimum-price standards with county land-grade table; effective 2007-01-01.
- id: E2
  source_type: policy-document
  citation: Ministry of Land and Resources, 国土资发〔2009〕56号, signed 2009-05-11; official Wuhan natural-resources republication.
  url: https://zrzyhgh.wuhan.gov.cn/zwgk_18/zcfgyjd/gtzyl/202001/t20200107_590106.shtml
  date: '2009-05-11'
  supports: [identity.legal_identifiers, identity.implementation_regime, timeline.local_timing, assignment.exemptions, assignment.compliance, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Articles 1-7, especially article 2 joint priority/intensity conditions, article 5 cost floor, article 6 county adjustment, and article 7 violations.
- id: E3
  source_type: paper
  citation: 'Tian, Wenjia, Zhi Wang, and Qinghua Zhang. Picking Winners: Local Land Allocation and Bottom-Up Industrial Policy in China. Journal of Development Economics 184 (January 2027): 103920. DOI 10.1016/j.jdeveco.2026.103920. Inspected author manuscript dated 2025-11-15.'
  url: https://zhiwang2013brownecon.weebly.com/uploads/4/2/1/9/42190763/price_draft_2025-11-15.pdf
  date: '2025-11-15'
  supports: [scope.china_relevance, identity.assignment_mechanism, timeline.implementation_start, timeline.implementation_end, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.exposure_construction, design.identifying_variation, design.primary_strategy, design.estimand, design.estimation_notes, empirical_requirements.time_start, empirical_requirements.time_end, design_applications.data_used, design_applications.treatment_encoding, design_applications.empirical_design]
  verification_status: verified
  access_level: full-text
  locator: Author manuscript pp.9-16 institutional/data/design sections; pp.17-22 Tables 2-3 and continuity/selection tests; Tables 1-2 on PDF pp.38-39 and Table A2 on p.48. This is an author version, not a line-by-line check against publisher final text.
- id: E4
  source_type: paper
  citation: Tian, Wang and Zhang, Journal of Development Economics publisher article landing page, volume 184 (January 2027), article 103920.
  url: https://doi.org/10.1016/j.jdeveco.2026.103920
  date: '2027-01'
  supports: [design_applications.journal, design_applications.year, design_applications.doi]
  verification_status: verified
  access_level: abstract
  locator: DOI-indexed publisher page at https://www.sciencedirect.com/science/article/pii/S0304387826002038, title, volume/issue metadata and abstract; full published article was not compared with the author manuscript.
design_applications:
- paper: 'Picking Winners: Local Land Allocation and Bottom-Up Industrial Policy in China'
  doi: 10.1016/j.jdeveco.2026.103920
  journal: Journal of Development Economics
  year: 2027
  research_question: Do county governments favor locally specialized industries through industrial-land price discounts?
  population: Chinese industrial land sales, July 2007-December 2019; below-benchmark sales form the main sample
  outcome: Log industrial land sale price
  data_used: [Land China dated parcel transactions, 2004 and 2008 Economic Census county-industry employment, official county land-grade floor schedule, 2010 county boundaries]
  treatment_encoding: Pre-existing county-industry own-industry employment specialization; main regression restricted to sales below the national benchmark
  comparison: Same-industry sales on opposite sides of a county border, with a 5-km main window and alternative bandwidths
  empirical_design: Conditional border discontinuity in sale prices with border-industry and industry-year fixed effects, county/parcel controls and spatial trends
  assumptions: [Smooth same-industry demand near borders, No confounding industry-specific county-border discontinuity, Manageable selection into sale and below-floor subsample]
  threats_addressed: [Residential land and nighttime-light continuity, Geographic-border exclusions, Above-floor comparison, Below-floor selection modelling]
  evidence_refs: [E3, E4]
method_transfer: null
readiness_blockers:
- The publisher final text and any replication package were not compared with the inspected November 2025 author manuscript; recheck version-sensitive coefficients before exact reproduction.
- Formal eligibility or legality of individual below-benchmark transactions cannot be inferred from sale price without project-level files.
---

## Institutional Background

The 2007 national regime set industrial-land price minima by land grade and county, while local governments continued to decide which industrial projects obtained local parcels [E1]. This is distinct from an investment-per-area requirement and from a one-off 2009 county-grade reassignment. The later 2009 notice specified conditional reductions for provincially prioritized, land-intensive projects and other special cases [E2]. Tian, Wang and Zhang use the resulting gap between uniform benchmark logic and local price-setting discretion to observe possible bottom-up industrial priorities in actual transactions [E3, reported interpretation].

## What Changed

This case is not a new universal reform. Its variation is the county-industry-specific discount attached to particular industrial-land sales within an existing floor regime. A government may favor an industry already concentrated locally, but the empirical record sees a sale price, not the internal decision or approval file. The 2009 priority-industry route requires both provincial priority and land-intensity conditions; the paper's own-industry specialization index is an analytical proxy for local preference, not a statutory eligibility condition [E2; E3].

## Implementation and Assignment

The paper links each Land China transaction to its county floor and keeps observed sales strictly below that benchmark for the main price analysis. It joins the buyer's two-digit industry to the county's 2004 Economic Census specialization for 2007-2008 sales and to the 2008 Census for subsequent sales. Addresses are geocoded, joined to 2010 county boundaries, and restricted to historically stable borders for adjacent-county comparison [E3]. A low price is an observed allocation outcome, not an exogenously assigned offer to every potential buyer.

## Why This Creates Empirical Variation

Adjacent counties may prefer different industries despite nearby parcels sharing similar market access and production amenities. Comparing the same industry on opposite sides of a border therefore makes a price discontinuity associated with county specialization informative about local land-allocation choices, conditional on the paper's continuity assumption. The author manuscript reports a negative specialization-price gradient in its 5-km below-floor sample; it does not experimentally assign industrial specialization or estimate the effect of a subsidy on subsequent growth [E3].

## Identification Risks

Specialized firms may bid for different parcels, local governments may offer only selected land, and below-floor sales are themselves a selected subset. Other county-specific policies can jump at the same border. The paper examines residential land prices, pre-period night lights, above-floor sales, multiple bandwidths, geographical barriers and a model of below-floor selection [E3]. Those checks reduce particular concerns but do not prove that every border-side difference is government favoritism. No observed below-benchmark sale should be labeled illegal without the applicable exemption and approval evidence [E2].

## Data Requirements

An empirical reconstruction needs dated parcel prices and locations, county-specific historical floor schedules, a reproducible county-border join, and county-industry employment shares from the correct pre-sale census. It must retain the two-digit classification version, parcel-selection rule, and any administrative-boundary changes. Data-source names guide a join; they do not imply public access to census microdata or a ready-to-run replication package.

## Evidence Notes

The official 2006 and 2009 documents establish the floor and conditional exemptions [E1; E2]. The inspected 51-page author manuscript establishes the paper's actual sample, border comparison, and reported diagnostics [E3]. Publisher indexing confirms its Journal of Development Economics identity and 2027 issue metadata [E4], but the published full text was not line-by-line compared with the 2025 manuscript. The source also cannot classify individual discounted transactions as compliant, formally exempt, or unlawful. This record is grounded as a traceable institutional/design case, not a claim that the exact microdata or legal approvals are already reconstructed.
