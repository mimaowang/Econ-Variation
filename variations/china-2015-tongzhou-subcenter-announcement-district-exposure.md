---
schema_version: 2
id: china-2015-tongzhou-subcenter-announcement-district-exposure
name: Beijing Tongzhou Subcenter Announcement and District Housing Exposure
aliases: [Tongzhou subcenter housing capitalization, 北京城市副中心公告与通州区住房暴露]
status: grounded
provenance:
  task_id: task-dc05db12cc76
scope:
  country: China
  regions: [Beijing, Tongzhou, Chaoyang, Daxing, Shunyi]
  domains: [urban-economics, regional-economics, place-based-policy, housing, development]
  variation_type: boundary-discontinuity
  knowledge_role: china-variation
  china_relevance: A Beijing administrative and economic decentralization program is studied through differential housing-price changes inside Tongzhou versus neighbouring Beijing districts. This is mainland urban policy exposure, not a financial-market instrument.
identity:
  instrument: Designation and development of Beijing's Tongzhou subcenter, studied through district location interacted with the June 2015 announcement period.
  authority: Beijing municipal authorities, with central approval and coordination under the Beijing-Tianjin-Hebei strategy.
  legal_identifiers:
  - 市行政副中心重大工程建设行动计划（2015年版）, identified in the municipal 2015 execution report
  - 北京城市副中心控制性详细规划（街区层面）（2016年—2035年）及2018年12月27日批复
  implementation_regime: Administrative relocation, infrastructure and complementary services support a suburban development pole. The later official plan distinguishes a 155 square kilometre core from Tongzhou including its expansion area. The paper assigns district-wide exposure, not parcel entitlement within that core. Formal operation of the relocated municipal government in January 2019 is a later implementation milestone, not its treatment start.
  assignment_mechanism: Residential complex location inside Tongzhou, compared with complexes in adjacent Chaoyang, Daxing and Shunyi, before and after a common announcement month. Selection of Tongzhou was purposive; distance to its border restricts the comparison, rather than randomizing the program.
  parent: null
  related_variations: [china-industrial-parks-edge-city-spillovers]
timeline:
  announcement: '2015-06 (paper announcement-month convention)'
  effective: null
  implementation_start: '2015 (municipal execution report confirms construction and support activities)'
  implementation_end: null
  local_timing: Post equals one for transactions after May 2015 in Table 2. The paper describes further upgrading in 2016 and municipal relocation in January 2019. Official sources verify development and relocation, but do not independently establish June 2015 as the first public revelation or a statutory effective day. Main window is June 2014-May 2016; one data paragraph reverses those endpoint months, so use Table 2's explicit coding and retain the discrepancy.
  anticipation: Section 5.1 reports early relative price increases near the border and information dissemination before announcement. Earlier satellite-town development and regional planning make a wholly unexpected assignment interpretation unsafe.
  last_verified: '2026-10-07'
assignment:
  unit: Resold private residential housing transaction, linked to a residential complex and month.
  treated: Sampled complexes inside the Tongzhou district administrative boundary, interacted with transactions from June 2015 onward.
  comparison_pool: Sampled complexes in adjacent Chaoyang, Daxing and Shunyi; narrow-boundary specifications restrict both sides to 5, 3 or 1 kilometres from the Tongzhou border.
  rule: Geocode residential complex locations and overlay a documented contemporaneous Tongzhou district boundary. Assign inside versus outside status, calculate minimum border distance in a consistent coordinate system, restrict to declared bands, and join transaction month. Do not replace district status with the later 155 square kilometre core or a ten-kilometre circle around the administrative centre.
  intensity: Main treatment is binary district exposure times post. Distance to the new administrative centre provides reported spatial heterogeneity within the same policy, not a separately assigned shock or an IV.
  exemptions:
  - Public-housing transactions are excluded because prices are regulated; this is a research exclusion, not a legal exemption from subcenter development.
  - New-home transactions are not the core sample because their prices are regulated.
  compliance: District designation does not show that every household received a service or a relocated government job. Announcement exposure measures expected and realized development capitalization together.
  exposure_construction: Retain transaction and listing dates/prices, private/public type, dwelling attributes, complex identifier and coordinates. Exclude missing prices/attributes, transaction prices below 100000 yuan, and floor area below 10 or above 500 square metres as reported. Join district and border distance to each transaction and construct post from its transaction date. The geocoding system and exact archived boundary version require documentation for a new application.
  required_identifiers: [transaction_id, residential_complex_id, district_id, transaction_month, complex_coordinates]
  spillovers: The paper reports price responses in adjacent Chaoyang and Daxing, changing over time. Nearby controls are therefore not demonstrably unaffected; positive spillovers can compress the relative contrast, while displacement can produce different bias.
research_compatibility:
  outcome_domains: [Housing transaction prices, Housing listing prices, Urban housing capitalization]
  affected_populations: [Private resale housing in Tongzhou and its neighbouring Beijing districts]
  mechanism_channels: [Expected administrative relocation, Infrastructure and public-service investment, Housing demand, Local housing supply]
  best_for: [Conditional local housing-capitalization studies with geocoded transaction histories and an explicit overlapping-policy chronology]
  not_good_for:
  - Interpreting the estimate as the isolated effect of civil servants physically moving in 2019.
  - Treating the whole Tongzhou district as identical to the detailed-plan core.
  - Identifying firm productivity or job creation from housing prices alone.
  - Calling June 2015 a verified surprise or the administrative border randomly assigned.
design:
  claim_type: reduced-form
  affordances: [Common paper-defined announcement month, Administrative district border, Repeated complex transactions, Narrow geographic comparisons]
  candidate_designs: [Boundary difference-in-differences, Monthly district-exposure event study]
  identifying_variation: Changes in resale housing prices across the Tongzhou district border around the announcement, conditional on physical attributes, complex effects and time effects.
  primary_strategy: Li and Xia equation 2 uses Tongzhou times post, hedonic controls, residential-complex fixed effects and year/month time effects. Table 2 reports unrestricted comparisons and 5, 3 and 1 kilometre border bands, with standard errors clustered by residential complex.
  estimand: Relative capitalization in observed resold properties inside Tongzhou versus sampled adjacent districts over the declared window; not a national welfare effect, randomized treatment effect or isolated relocation channel.
  treatment_variable: Indicator for location inside Tongzhou multiplied by indicator for transaction month from June 2015 onward.
  comparison_logic: Compare changes in nearby properties across the border, controlling observed dwelling and neighbourhood attributes and stable complex characteristics. Inspect alternative bands and monthly leads; neither proximity nor a high regression fit proves counterfactual continuity.
  estimation_notes: Table 2's full sample is 114863 transactions; the 5, 3 and 1 kilometre samples have 27364, 17442 and 5860. The outcome is log total transaction price except its level-price column, not necessarily price per square metre. Complex clustering does not account for every district-level common shock when only one district is treated. The first-year window already includes Tongzhou-specific purchase restrictions.
  assumptions:
  - Without the program, conditional housing-price changes would be comparable across the chosen border segment and period.
  - Anticipation, differential sales composition, other Tongzhou policies and control-side spillovers do not dominate the contrast.
  - Historical district geometry, geocoding and transaction characteristics are consistently measured.
  - The interpretation explicitly includes or separately addresses contemporaneous demand restrictions and bundled investment.
  diagnostics:
  - Examine monthly leads and band-specific anticipation rather than treating selected insignificant leads as proof.
  - Compare 5, 3 and 1 kilometre bands and alternative border segments.
  - Separate pre-restriction announcement response from longer overlapping-policy periods as an adaptation, not the published baseline.
  - Investigate sales composition, reporting and listings versus realized prices.
  - Evaluate neighbouring-market exposure and inference sensitive to spatial/common-policy correlation.
threats:
- type: purposive-placement-and-anticipation
  basis: reported
  condition: Tongzhou already had infrastructure and development potential; Section 5.1 reports early price movements near the border. Narrow comparisons do not make the district choice random.
  evidence_refs: [E1]
  possible_diagnostics: [Band-specific leads, Earlier planning chronology, Placebo dates and borders]
- type: overlapping-housing-demand-restrictions
  basis: documented
  condition: The August 2015 Tongzhou housing restriction overlaps the first-year sample. Its official household-eligibility conditions are more specific than the paper's summary. The inspected portal dates publication September 3 but the notice is signed August 14 and takes effect after publication; exact historical announcement timing should be recovered before a daily restriction design.
  evidence_refs: [E1, E4]
  possible_diagnostics: [Explicit restriction chronology, Short announcement-only window, Transaction-composition checks]
- type: control-market-spillovers
  basis: reported
  condition: Neighbouring districts are themselves affected; Section 7 reports heterogeneous and increasing spillovers. This changes the interpretation of the relative price response.
  evidence_refs: [E1]
  possible_diagnostics: [Distance-band exposure, Alternative control regions with justified comparability, Spatial inference sensitivity]
- type: transaction-measurement-and-selection
  basis: reported
  condition: HomeLink resales need not represent all housing; reported transaction prices may be manipulated and listing discounts depend on market negotiations. Supply and buyer composition can change after announcement.
  evidence_refs: [E1]
  possible_diagnostics: [Listing versus transaction outcomes, Hedonic balance, Repeated-complex composition and coverage checks]
empirical_requirements:
  contract_version: 1
  population: Private resold homes in Tongzhou and adjacent Chaoyang, Daxing and Shunyi, with comparable transactions before and after announcement.
  observation_unit: housing-transaction
  geography_level: residential complex and district boundary
  time_start: 2014
  time_end: 2016
  minimum_frequency: monthly
  minimum_pre_periods: 12
  minimum_post_periods: 12
  required_fields:
  - Transaction month, total transaction price, complex identifier and coordinates.
  - Private/public housing classification, floor area and hedonic dwelling/building attributes.
  - Historical district polygon, district status and minimum distance to Tongzhou border.
  - Neighbourhood amenity distances and lagged residential land supply within 3 kilometres for the reported controlled model.
  required_identifiers: [transaction_id, residential_complex_id, district_id, transaction_month]
  treatment_key: [residential_complex_id, transaction_month]
  treatment_source: Paper Section 3 and Table 2 specify district-times-June2015 assignment; official execution and planning texts ground the institution. Archive the district boundary and coordinate transformation used in an application.
  measurement_risks:
  - Data availability statement links HomeLink, not an inspected downloadable historical replication package.
  - Published data paragraph reverses endpoint months relative to Table 2's June2014-May2016 window.
  - Exact coordinate reference system and archived border version were not supplied in the inspected text.
  - Long-horizon price and two-wave population analyses need additional data; do not union their requirements into this transaction contract.
evidence:
- id: E1
  source_type: paper
  citation: 'Li, Ling, and Fangzhou Xia. 2023. City subcenter as a regional development policy: Impact on the property market. Journal of Regional Science 63(3): 643-673. DOI: 10.1111/jors.12633; publisher first-online label 2022-12-26.'
  url: https://doi.org/10.1111/jors.12633
  date: 2023
  supports: [identity.instrument, identity.assignment_mechanism, timeline.announcement, timeline.local_timing, timeline.anticipation, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.intensity, assignment.exemptions, assignment.exposure_construction, assignment.spillovers, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, design.diagnostics, threats.condition, empirical_requirements.population, empirical_requirements.observation_unit, empirical_requirements.time_start, empirical_requirements.time_end, empirical_requirements.required_fields, empirical_requirements.treatment_source, empirical_requirements.measurement_risks, design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year, design_applications.research_question, design_applications.population, design_applications.outcome, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design, design_applications.assumptions, design_applications.threats_addressed]
  verification_status: reported
  access_level: full-text
  locator: Publisher HTML https://onlinelibrary.wiley.com/doi/full/10.1111/jors.12633 inspected2026-10-07, Sections2-4.1,5.1-5.2,6-8, Tables2-5 and7-8, Data Availability Statement. Formula2 and Table2 note establish post afterMay2015, complex clustering and bands. Figures were read as captions, not independently digitized; supplementary file not inspected.
- id: E2
  source_type: implementation-document
  citation: 北京市发展和改革委员会, 2015年计划执行情况与2016年计划草案报告, delivered2016-01-22.
  url: https://www.bjrd.gov.cn/zyfb/bg/202012/t20201222_2180286.html
  date: '2016-01-22'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.implementation_start]
  verification_status: verified
  access_level: official-document
  locator: SectionI.(I), paragraph on functional restructuring and administrative-subcenter construction, inspected2026-10-07. Confirms the2015 action plan and development activities; not the exact paper announcement month.
- id: E3
  source_type: policy-document
  citation: 中共中央、国务院, 北京城市副中心控制性详细规划（街区层面）（2016年—2035年）批复,2018-12-27.
  url: https://www.beijing.gov.cn/zhengce/zhengcefagui/201905/t20190522_61790.html
  date: '2018-12-27'
  supports: [identity.authority, identity.legal_identifiers, identity.implementation_regime, assignment.rule]
  verification_status: verified
  access_level: official-document
  locator: Approval SectionsIV-V, inspected2026-10-07. Establishes distinct core/district scales and relocation-based functions; does not establish a2015 GIS treatment boundary.
- id: E4
  source_type: policy-document
  citation: 北京市住房和城乡建设委员会、北京市通州区人民政府, 加强通州区商品住房销售管理的通知,京建法〔2015〕12号.
  url: https://www.beijing.gov.cn/zhengce/gfxwj/sj/201905/t20190522_58704.html
  date: '2015-08-14'
  supports: [threats.condition, design.assumptions]
  verification_status: verified
  access_level: official-document
  locator: Heading, signature, opening effect clause and SectionsI-II, inspected2026-10-07. Includes new and second-hand housing and detailed household restrictions; portal publication metadata differs from signature date.
- id: E5
  source_type: implementation-document
  citation: 北京市人民政府机关驻地迁址公告,2019-01-11.
  url: https://www.beijing.gov.cn/ywdt/gzdt/201901/t20190111_1826667.html
  date: '2019-01-11'
  supports: [identity.implementation_regime, timeline.local_timing]
  verification_status: verified
  access_level: official-document
  locator: Municipal-government announcement and signature, inspected2026-10-07. Verifies formal operation in Tongzhou from this date, not the authors' geocoded centre point.
design_applications:
- paper: 'City subcenter as a regional development policy: Impact on the property market'
  doi: 10.1111/jors.12633
  journal: Journal of Regional Science
  year: 2023
  research_question: How is announced subcenter development capitalized in local resale housing and neighbouring markets?
  population: Private resales in Tongzhou, Chaoyang, Daxing and Shunyi;114863 transactions in the Table2 June2014-May2016 baseline.
  outcome: Log total transaction price; level total price and log listing price alternatives. Population and long-horizon price analyses are supplementary applications, not direct observations of employment/productivity.
  data_used: [HomeLink resale transactions2013-2019, Complex geocodes and neighbourhood amenities, Residential land supply from LandChina, Consulting-firm jiedao population2015/2018 for supplementary mechanism work]
  treatment_encoding: Tongzhou complex indicator times transaction afterMay2015;5/3/1km border restrictions are alternatives. Distance to new centre is used for spatial heterogeneity without replacing district assignment.
  comparison: Adjacent Beijing districts and their near-border complexes before/after announcement; neighbours can receive spillovers.
  empirical_design: Boundary DID with hedonic covariates, complex and year/month effects, complex-clustered errors; monthly interaction diagnostics omitMay2015.
  assumptions: [Conditional parallel trends, Comparable geocodes and sales composition, Explicit anticipation and policy-overlap interpretation, Spillover-aware comparison]
  threats_addressed: [Listing-price alternative, Multiple bands, Monthly leads revealing some early movement, Placebo dates, Reported purchase-restriction chronology and neighbour spillover analysis]
  evidence_refs: [E1, E2, E3, E4, E5]
method_transfer: null
readiness_blockers:
- Conditional matching requires lawful historical transaction access and a documented contemporaneous district geometry/geocode join; these files are not distributed here.
- A pure subcenter-announcement effect requires an explicit treatment of anticipation, August2015 restrictions and neighbouring-market exposure; the published first-year estimate does not isolate all components.
---

## Institutional Background

Beijing sought a suburban development pole by relocating administrative
functions and investing in complementary services. The municipal execution
report confirms2015 development activity [E2]. Later planning defines a smaller
core within the wider Tongzhou district [E3]. This is distinct from an industrial
park opening or the relocation of noncapital functions throughout the region.

## What Changed

The program concentrated administrative functions and supporting investment
in Tongzhou. Housing markets could respond to expected future access and
services before actual relocation, which explains why an announcement clock
differs from a physical-move clock [E1, reported; E2; E5].

## Implementation and Assignment

The paper's empirical object is district-wide announcement exposure: a housing
complex inside Tongzhou, interacted with transactions from June2015. Its
geographic comparisons use neighbouring districts and optional border bands
[E1, reported]. The formal government move in2019 is later implementation
[E5], not another onset assigned to this record. Plan-core membership, district
status and distance to the administrative centre must remain separate.

## Why This Creates Empirical Variation

A border comparison asks whether housing on the Tongzhou side changed
differently around announcement after controlling property features and stable
complex differences. It is useful for conditional local capitalization, not
proof that the site was chosen randomly. Near-border movements preceded the
announcement in some specifications [E1, reported]. Treat surprise and
counterfactual continuity as assumptions to assess, not institutional facts.

## Identification Risks

The same first-year window includes a targeted housing restriction [E4], and
the paper reports responses in nearby control markets [E1, reported]. Thus an
observed relative price effect can reflect bundled development, anticipation,
restrictions and spillovers. Complex-level clustering is the published choice;
it does not eliminate district-wide common shocks [analytical inference].

## Data Requirements

The core join is complex location to district and border distance, then
transaction month to the common post clock. Private resales, not regulated
new homes or public housing, supply the reported outcome. Historical access,
coordinate conversion and border version must be documented; a HomeLink link
does not certify an open replication dataset [E1, reported]. Optional
population/supply mechanism data do not become mandatory for the housing
contrast.

## Evidence Notes

The body recovered the source-access gap of candidate-4e21d30dca46;
its original failed-worker history remains intact. The record is grounded and
conditionally useful, not certified causal truth or an exact replication.
