---
schema_version: 2
id: china-industrial-land-supply-target-area-churn
name: China Place-Based Industrial Policy Target-Area Churn in City Industrial Land Supply
aliases:
- Disrupted Development place-based policy target-area changes
- China industrial land supply spatial churn PC index
- 中国区位导向性产业政策目标区域变动
status: grounded
provenance:
  task_id: task-e6f648e1ff1b
scope:
  country: China
  regions:
  - 285 prefecture-level Chinese cities and their county-level districts, 2008-2016
  domains:
  - regional-economics
  - urban
  - economic-geography
  - political-economy
  - local-government
  - productivity
  - innovation
  - land
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    The exposure is a China-specific institutional behavior: prefecture city
    governments, which control the supply of state-owned urban industrial land,
    repeatedly redirect that supply across county-level districts as the targeted
    areas of place-based industrial policy change. Shen, Wu, Wu, and Zheng (2026)
    measure this churn for 285 cities over 2008-2016 and relate it to city TFP and
    innovation. This is a paper-defined continuous exposure constructed from
    endogenous local-government behavior, not a government eligibility rule,
    rollout, or randomly assigned shock.
identity:
  instrument: >
    Within-city spatial reallocation of industrial land supply, used by the paper
    as the observable footprint of changes in the targeted areas of place-based
    industrial policies (development zones and industrial parks). Because urban
    land is state-owned, a city government implements place-based industrial
    policy by allocating new industrial land parcels to chosen districts; shifts
    in the spatial distribution of that supply across a city's county-level
    districts are measured with a policy-change index (PC), following Shen et al.
    (2022), that counts rank reversals of districts by industrial land supplied
    per unit area between consecutive years.
  authority: >
    No authority assigns this exposure. The surrounding zone regime is defined by
    the State Council and national ministries: the 2003 State Council General
    Office notice ordered a nationwide cleanup of unauthorized development zones
    and centralized zone approval, and the 2006 national audit catalog announced
    1568 qualified development zones, revised to 2543 in the 2018 catalog. City
    governments decide where to supply industrial land within this regime; the PC
    exposure is the authors' reproducible measurement convention over those
    decisions.
  legal_identifiers:
  - State Council General Office notice Guo Ban Fa [2003] No. 70 on cleaning up development zones and strengthening construction-land management, 2003-07-30
  - 2006 edition of the China Development Zone Audit Announcement Catalog (1568 zones), NDRC with Ministry of Land and Resources and Ministry of Construction
  - '2018 edition of the China Development Zone Audit Announcement Catalog (2543 zones: 552 national-level and 1991 provincial-level), Announcement No. 4 of 2018'
  implementation_regime: >
    After the 2003-2006 national cleanup abolished most locally created zones and
    restricted new zone approval to the State Council or provincial governments,
    prefecture city governments continued to steer industry spatially through
    industrial land allocation. The paper's institutional account attributes
    frequent target-area changes to the promotion-tournament incentive of city
    leaders, who favor new zones over a predecessor's "political legacy" areas;
    zones repeatedly pass through establishment, abolition, and redevelopment
    cycles.
  assignment_mechanism: >
    There is no external assignment rule. A city-year is more "treated" when the
    ranking of its county-level districts by industrial land supplied per unit
    administrative area changes more between consecutive years. At the micro
    level the paper uses Getis-Ord Gi* hot-spot transitions of district-level
    industrial land supply to define new and disappearing "hot" industrial zones,
    reporting that new hot zones last on average 1.7 years and over 60 percent
    last no more than one year. Assignment is therefore endogenous city
    government behavior and must not be read as an exogenous policy event.
  parent: null
  related_variations:
  - china-industrial-park-political-connection-rotation
  - china-industrial-parks-edge-city-spillovers
timeline:
  announcement: null
  effective: null
  implementation_start: 2008
  implementation_end: 2016
  local_timing: >
    The paper measures target-area churn annually over 2008-2016 and enters it
    with a one-year lag in the city panel. The framing regime is earlier: the
    2003 notice required the zone cleanup to be completed by end-2003, the 2006
    catalog then announced 1568 qualified zones, and the 2018 revision listed
    2543. There is no single treatment date; each city-year has its own measured
    churn value.
  anticipation: >
    Land supply decisions are discretionary and may anticipate or follow city
    leader turnover; the companion Shen et al. (2022) study links target-area
    changes to city-chief succession. Buyers of industrial parcels may also
    anticipate local re-targeting. Timing is therefore part of the behavior being
    measured, not an externally imposed surprise.
  last_verified: '2026-08-14'
assignment:
  unit: >
    County-level district within a prefecture city, aggregated to a city-year
    panel of 285 prefecture-level cities, 2008-2016; the micro extension uses
    district-level hot-spot transitions and firm-year outcomes.
  treated: >
    A city-year with a larger PC index value, meaning larger rank reversals among
    its districts in industrial land supply per unit area relative to the
    previous year; the paper winsorizes PC at 2 percent and lags it one year.
    At the district level, units gaining or losing a "hot" industrial zone under
    the Gi* statistic are the treated cells of the micro analysis.
  comparison_pool: >
    Primarily the same city in other years (city fixed effects) and cities with
    smaller measured churn in the same year (year fixed effects). Non-industrial
    land supply changes serve as a placebo. The comparison is associational:
    high-churn cities differ systematically in leadership incentives and
    development pressure.
  rule: >
    Aggregate industrial land parcels disclosed on the official China Land
    Market Network to district-year totals, divide by district administrative
    area, rank districts within each city-year, and sum absolute rank changes
    between consecutive years to form PC, following Shen et al. (2022). The
    exact normalization and parameter choices come from an author-team research
    note and have not been verified against the article full text.
  intensity: >
    PC is a continuous intensity measure; the paper reports a non-linear
    relationship in which larger churn is associated with larger TFP declines,
    and isolates "excessive" changes through short-lived hot zones.
  exemptions:
  - Non-industrial (e.g., residential or commercial) land supply, used as placebo rather than treatment
  - City-years with no district rank change, which form the low-churn comparison rather than a treated group
  compliance: >
    Parcel-level industrial land transfer disclosure on the official land-market
    platform is the data basis; the record does not verify coverage, reporting
    lags, or district boundary consistency of that disclosure for 2008-2016.
  exposure_construction: >
    Join landchina.com industrial parcel records to county-level districts and
    prefecture cities with stable identifiers, build district-year supply per
    unit area, compute within-city rank changes, and merge the resulting
    city-year PC with city outcomes. For the micro analysis, apply the Getis-Ord
    Gi* statistic to district-level supply and track hot-spot appearance and
    disappearance.
  required_identifiers:
  - parcel identifier with industrial land-use type, area, and transfer year
  - county-level district identifier with administrative area
  - prefecture city identifier with consistent 2008-2016 boundaries
  - firm identifier for the patent and firm-TFP extensions
  spillovers: >
    Industrial re-targeting in one city can shift firms, investment, and land
    prices in neighboring cities; the paper reports spatial-spillover checks and
    states its baseline survives their exclusion, but spillover treatment in any
    reuse must be re-derived from the article.
research_compatibility:
  outcome_domains:
  - city total factor productivity and its Malmquist decomposition
  - manufacturing patenting and innovation
  - city GDP, employment, and investment
  - industrial land allocation and zone lifecycles
  affected_populations:
  - Manufacturing firms in the 285 sampled prefecture-level cities
  - City governments and city leaders making land-allocation decisions
  - County-level districts gaining or losing targeted industrial areas
  mechanism_channels:
  - innovation suppression through unstable policy targets
  - technological-progress decline within the TFP decomposition
  - promotion-tournament incentives of city leaders
  - factor-input substitution masking short-run GDP effects
  best_for:
  - Measuring the productivity cost of place-based policy instability and short-lived industrial zones
  - Studies needing a city-year or district-year panel of industrial land supply reallocation, 2008-2016
  - Documenting political-economy drivers of local industrial-policy churn
  not_good_for:
  - Designs that need an exogenous assignment rule, threshold, rollout, or eligibility list
  - Treating PC rank churn as equivalent to formal zone designation or revocation
  - Causal claims without addressing that churn is chosen by city governments under promotion incentives
  - Questions about the level effect of having a development zone, which designation-based records cover instead
design:
  claim_type: reduced-form
  affordances:
  - Annual within-city variation in the spatial targeting of industrial land supply for 285 cities, 2008-2016
  - District-level hot-spot transitions that isolate short-lived industrial zones
  - Links from city-year churn to TFP decomposition and manufacturing patent counts
  - Political-incentive outcomes (leader promotion) that document the churn driver
  candidate_designs:
  - City and year fixed-effects panel with lagged PC and city-clustered errors
  - District-level event-style analysis of hot-zone appearance and disappearance
  - Firm-year TFP regressions on district-level policy-change indicators
  - Spatial-spillover specifications excluding neighboring-city exposure
  identifying_variation: >
    Within-city over-time changes in the district ranking of industrial land
    supply, conditional on city and year fixed effects and lagged city controls.
    There is no external instrument in the accessible evidence; identifying
    content rests on the fixed-effects structure, the placebo on non-industrial
    land, and the paper's reported endogeneity robustness, none of which removes
    the fact that churn is a chosen local-government behavior.
  primary_strategy: >
    Regress city-year Malmquist TFP on one-year-lagged PC with city and year
    fixed effects, controls, and city-clustered or two-way clustered standard
    errors; the author-team note reports that a 10-percentage-point larger lagged
    policy change is associated with about 0.4 percent lower TFP, concentrated in
    the technological-progress component, with matching declines in manufacturing
    patenting.
  estimand: >
    The association between the intensity of within-city place-based policy
    target-area churn and subsequent city TFP, technological progress, and
    innovation, interpreted by the authors as a negative effect of excessive
    policy change.
  treatment_variable: >
    Lagged PC index of within-city district rank changes in industrial land
    supply per unit area, winsorized at 2 percent; micro versions use Gi*
    hot-zone appearance, disappearance, and short-lived-zone indicators.
  comparison_logic: >
    Compare a city with its own other years and with same-year cities
    experiencing less churn; use non-industrial land churn as a falsification
    dimension and test spatial spillovers explicitly.
  estimation_notes: >
    Reported robustness includes alternative PC constructions, firm-level TFP
    outcomes, the non-industrial-land placebo, multiple approaches to
    endogeneity, and spatial-spillover exclusions; the exact methods are known
    only from the author-team summary and await full-text verification. The note
    also reports that churn raises incumbent leaders' promotion probability while
    leaving short-run GDP statistically unchanged.
  assumptions:
  - Conditional on city and year fixed effects and lagged controls, lagged land-supply churn is unrelated to other simultaneous determinants of city TFP growth
  - Industrial land supply rank changes proxy actual place-based policy target-area changes rather than market-driven parcel demand
  - The Malmquist city TFP aggregate and patent counts measure the intended productivity and innovation outcomes
  - Spatial spillovers are either absent or adequately removed in the chosen specification
  diagnostics:
  - Placebo regressions using non-industrial land supply churn
  - Alternative PC constructions and firm-level TFP outcomes
  - Spatial-spillover specifications and neighbor exclusions
  - Non-linearity checks separating excessive changes and short-lived zones
  - Pre-trend and anticipation checks around city-leader turnover when personnel data are added
threats:
- type: endogenous_policy_churn
  basis: reported
  condition: Target-area churn is itself a choice of city governments and is attributed by the paper to promotion-tournament incentives; the same local conditions that produce churn may independently lower TFP, so the panel association is not an externally assigned contrast.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - The paper's reported endogeneity robustness methods, to be recovered from the full text
  - Linking churn to leader turnover and promotion incentives as the paper does
  - Instrumental or event-study strategies built on the companion turnover-based design rather than on PC alone
- type: measurement_proxy_gap
  basis: inferred
  condition: Land-supply rank churn proxies policy target-area changes, but industrial parcel supply also responds to market demand, land quotas, and macro conditions, so PC may mix policy re-targeting with other forces.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Compare PC with formal zone designation and revocation lists from the 2006 and 2018 catalogs
  - Placebo tests on non-industrial land, as reported
  - Sensitivity to district boundary harmonization
- type: spatial_spillovers
  basis: reported
  condition: Re-targeting can move firms and investment across city borders, contaminating same-year cross-city comparisons.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Spatial-lag or neighbor-exposure specifications, which the paper reports using
  - Excluding province-border city pairs
- type: anticipation_and_turnover_timing
  basis: inferred
  condition: Land allocation may shift before or after city-leader changes, so a one-year lag may mis-time exposure relative to the actual political decision.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Merge city-chief tenure dates and test alternative lag windows
  - Event-time profiles around turnover years
- type: tfp_measurement_aggregation
  basis: inferred
  condition: City TFP is a DEA-Malmquist aggregate built from firm-level inputs and outputs aggregated by city; aggregation and frontier-estimation choices can drive the decomposition into technological progress.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Re-estimate with firm-level TFP as the paper's reported robustness does
  - Alternative productivity estimators on the same firm data
empirical_requirements:
  contract_version: 1
  population: 285 prefecture-level Chinese cities and their county-level districts, with manufacturing firms above the reported sales threshold in mechanism analysis
  observation_unit: City-year for the main panel; district-year for hot-spot transitions; firm-year for the micro extension
  geography_level: Prefecture city and county-level district with consistent boundaries
  time_start: 2008
  time_end: 2016
  minimum_frequency: annual
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - industrial land parcel area, land-use type, location, and transfer year
  - district administrative area for normalization
  - city GDP, employment, investment, and yearbook controls
  - city export value from customs data
  - manufacturing patent applications by city and year
  - firm inputs and outputs for Malmquist TFP construction
  required_identifiers:
  - city_id
  - district_id
  - parcel_id
  - firm_id
  - year
  treatment_key:
  - city_id
  - district_id
  - year
  treatment_source: >
    Parcel-level industrial land transfer disclosures on the China Land Market
    Network (landchina.com), an official platform hosted by the Ministry of
    Natural Resources Real Estate Registration Center; the PC index construction
    follows Shen et al. (2022) as reported in the 2026 article and its author-team
    summary.
  measurement_risks:
  - district boundary changes across 2008-2016 city samples
  - parcel disclosure coverage and reporting delays on the platform
  - PC sensitivity to the winsorization and ranking convention
  - city TFP sensitivity to Malmquist aggregation choices
  - patent counts restricted to manufacturing firms above the sales threshold
design_profiles: []
evidence:
- id: E1
  source_type: paper
  citation: 'Shen, Yang, Jing Wu, Shuping Wu, and Jiaxin Zheng. 2026. "Disrupted Development: Urban Productivity Under Changing Place-Based Industrial Policies in China." Journal of Regional Science 66(3): 868-890. DOI: 10.1111/jors.70050.'
  url: https://doi.org/10.1111/jors.70050
  date: 2026
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - empirical_requirements.population
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - design_applications.paper
  - design_applications.research_question
  - design_applications.outcome
  verification_status: reported
  access_level: abstract
  locator: >
    CrossRef/publisher metadata inspected 2026-08-14: title, authors, journal
    volume 66 issue 3 pages 868-890, and the full official abstract stating the
    319,276-parcel, 285-city, 2008-2016 design, the land-supply spatial-shift
    measurement, the political-incentive driver, the innovation and TFP decline,
    and the short-lived industrial zone decomposition. The Wiley full text
    returned 403 and was not inspected.
- id: E2
  source_type: scholarship
  citation: 'Tsinghua University Hang Lung Center for Real Estate research team note. 2026-01. "Disrupted Development: Urban Productivity Under Changing Place-Based Industrial Policies in China" (Chinese-language author-team research summary, reposted).'
  url: https://m.cehome.com/news/20260113/370603.shtml
  date: '2026-01'
  supports:
  - identity.instrument
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.local_timing
  - timeline.anticipation
  - assignment.rule
  - assignment.intensity
  - assignment.exposure_construction
  - assignment.spillovers
  - design.primary_strategy
  - design.estimation_notes
  - design.diagnostics
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_source
  - empirical_requirements.measurement_risks
  - design_applications.data_used
  - design_applications.treatment_encoding
  - design_applications.comparison
  - design_applications.empirical_design
  verification_status: reported
  access_level: full-text
  locator: >
    Full text of the author-team dissemination note inspected 2026-08-14:
    institutional background on zone churn and promotion incentives, the PC
    formula narrative following Shen et al. (2022), data sources (landchina.com
    parcels, China Customs exports, city statistical yearbook, SIPO patents),
    DEA-Malmquist TFP with DEAP 2.1, the lagged-PC fixed-effects specification,
    winsorization, placebo and spatial-spillover robustness, the Gi* hot-zone and
    short-lived-zone analysis (average duration 1.7 years, over 60 percent within
    one year), and the promotion-probability result. This is a secondary summary,
    not the article or its appendix.
- id: E3
  source_type: policy-document
  citation: 'General Office of the State Council. 2003. "Notice on Cleaning Up and Rectifying Various Development Zones and Strengthening Construction Land Management" (Guo Ban Fa [2003] No. 70), 2003-07-30.'
  url: https://www.gov.cn/zhengce/content/2008-03/28/content_2471.htm
  date: '2003-07-30'
  supports:
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.local_timing
  verification_status: verified
  access_level: official-document
  locator: >
    gov.cn full text inspected 2026-08-14: orders a comprehensive cleanup of
    development zones established without State Council or provincial approval,
    requires completion by end-2003, centralizes approval of new zones,
    expansions, relocations, and upgrades, and channels industrial projects into
    legally established national and provincial zones. Establishes the
    zone-cleanup regime, not the paper's land-supply measurement.
- id: E4
  source_type: policy-document
  citation: 'National Development and Reform Commission. 2018. "Explanation of the China Development Zone Audit Announcement Catalog (2018 edition)", 2018-03-02.'
  url: https://www.ndrc.gov.cn/xwdt/xwfb/201803/t20180302_954222.html
  date: '2018-03-02'
  supports:
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.local_timing
  verification_status: verified
  access_level: official-document
  locator: >
    ndrc.gov.cn full text inspected 2026-08-14: states that the 2003-2006 cleanup
    led to the 2006 catalog of 1568 qualified development zones issued by NDRC
    with the land and construction ministries, and that the 2018 revision
    (Announcement No. 4 of 2018) lists 2543 zones with 552 national-level and
    1991 provincial-level, documenting the abolish-and-rebuild churn the paper
    describes. Does not establish any city's land-supply pattern.
- id: E5
  source_type: official-data
  citation: 'China Land Market Network (landchina.com), hosted by the Real Estate Registration Center of the Ministry of Natural Resources under the guidance of the Department of Natural Resources Development and Utilization.'
  url: https://www.landchina.com/
  date: 2026
  supports:
  - assignment.exposure_construction
  - assignment.compliance
  - empirical_requirements.treatment_source
  - empirical_requirements.required_fields
  verification_status: verified
  access_level: dataset
  locator: >
    Platform footer inspected 2026-08-14: confirms the site is the official land
    market monitoring and disclosure platform of the Ministry of Natural
    Resources. Confirms the data source identity only; parcel coverage for
    2008-2016 was not audited.
design_applications:
- paper: 'Disrupted Development: Urban Productivity Under Changing Place-Based Industrial Policies in China'
  doi: 10.1111/jors.70050
  journal: Journal of Regional Science
  year: 2026
  research_question: Do frequent changes in the targeted areas of place-based industrial policies reduce urban productivity, and what political-incentive mechanism drives the changes?
  population: 285 prefecture-level Chinese cities, 2008-2016, with district-level land-supply detail and manufacturing firms for mechanism analysis
  outcome: City Malmquist TFP and its technological-progress component, manufacturing patent applications, and secondary GDP, employment, investment, and leader-promotion outcomes
  data_used:
  - 319,276 industrial land parcels from the China Land Market Network, 2008-2016
  - China Customs city export values
  - China City Statistical Yearbook city controls
  - SIPO patent applications for manufacturing firms above the reported sales threshold
  - DEAP 2.1 Malmquist TFP construction from aggregated firm inputs and outputs
  treatment_encoding: >
    One-year-lagged PC index of within-city district rank changes in industrial
    land supply per unit area, winsorized at 2 percent; micro extensions code
    Getis-Ord Gi* hot-zone appearance, disappearance, and short-lived zones.
  comparison: >
    Within-city over time with city and year fixed effects, relative to
    same-year low-churn cities; non-industrial land churn as placebo; spatial
    spillover checks reported.
  empirical_design: City-year fixed-effects panel with lagged continuous treatment, district-level hot-spot transition analysis, and firm-year mechanism regressions
  assumptions:
  - Lagged land-supply churn is conditionally unrelated to other drivers of city TFP growth
  - Land-supply rank changes proxy actual place-based policy re-targeting
  - Fixed effects, placebos, and reported endogeneity robustness adequately address selection into churn
  threats_addressed:
  - Endogeneity through multiple reported methods, details not yet full-text verified
  - Spatial spillovers through dedicated specifications and exclusions
  - Measurement through alternative PC constructions and firm-level outcomes
  - Falsification through the non-industrial land placebo
  evidence_refs:
  - E1
  - E2
method_transfer: null
readiness_blockers:
- The Wiley full text and appendix are inaccessible (403), so the exact PC normalization, endogeneity strategy, sample-screening rules, and spatial-spillover specification are known only from the official abstract and an author-team summary.
- Assignment is endogenous city-government behavior under promotion incentives; the record documents a measured exposure and its reported associations, not an externally assigned treatment.
- Parcel coverage, district boundary harmonization, and the mapping from land-supply churn to formal zone designation or revocation (2006/2018 catalogs) remain unaudited.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Chinese place-based industrial policy operates through development zones and
industrial parks whose number and location have churned for decades. The State
Council's 2003 notice [E3] ordered a nationwide cleanup of zones created without
State Council or provincial approval, required completion by end-2003, and
centralized approval of new zones, expansions, relocations, and upgrades. The
NDRC's official 2018 explanation [E4] records that this cleanup produced the
2006 audit catalog of 1568 qualified zones and that the 2018 revision listed
2543 (552 national-level, 1991 provincial-level), with zones repeatedly added,
merged, expanded, relocated, or abolished between catalogs. Within this regime,
prefecture city governments allocate state-owned urban industrial land to chosen
districts, and the paper's institutional account attributes frequent re-targeting
to promotion-tournament incentives that favor a new leader's zones over a
predecessor's [E1; E2].

## What Changed

Nothing in this record is a single dated reform. The variation is the ongoing
within-city spatial reallocation of industrial land supply across county-level
districts, interpreted by Shen, Wu, Wu, and Zheng (2026) as the observable
footprint of place-based policy target-area changes [E1; E2]. The canonical
boundary is the churn measure itself: formal zone designation lists, zone
boundary discontinuities, and city-chief turnover designs are related but
distinct variations covered elsewhere or held in the candidate ledger.

## Implementation and Assignment

Because urban land is state-owned, a city government steers industry by
deciding which districts receive new industrial parcels. The paper aggregates
319,276 industrial parcels disclosed on the official land-market platform [E5]
to district-year supply per unit area, ranks districts within each city-year,
and sums rank changes between consecutive years into a policy-change index (PC)
following Shen et al. (2022), winsorized at 2 percent and lagged one year in the
regressions [E2]. A micro extension applies the Getis-Ord Gi* statistic to
district-level supply and finds that newly emerging hot zones last on average
1.7 years, with over 60 percent disappearing within one year — the "short-lived"
zones that drive the decomposition result [E2]. Assignment is therefore measured
local-government behavior, not an eligibility rule, and the comparison is a
city's own other years and same-year low-churn cities under fixed effects [E1].

## Why This Creates Empirical Variation

The design exploits annual within-city differences in how much the spatial
targeting of industrial land supply changes, linked to city Malmquist TFP, its
technological-progress component, and manufacturing patenting [E1; E2]. Its
research value is the measurement construction and the documentation of policy
instability costs; its identifying content is limited to the fixed-effects
panel, the non-industrial-land placebo, and robustness steps reported in the
abstract and author-team note. This variation should not be used where a
research question requires an externally assigned treatment [analytical
inference].

## Identification Risks

The central risk is that churn is chosen: the same promotion incentives and
local conditions that produce re-targeting may independently depress measured
TFP, and the paper itself links churn to leader promotion prospects [E1; E2].
Land-supply rank changes may mix policy re-targeting with market-driven parcel
demand; spatial spillovers can contaminate cross-city comparisons; the one-year
lag may mis-time exposure around leader turnover; and city TFP depends on
Malmquist aggregation choices [E2; analytical inference].

## Data Requirements

A reuse needs parcel-level industrial land transfer records with location and
year from the official land-market platform [E5], district administrative areas,
consistent 2008-2016 city and district identifiers, city-year outcomes from the
statistical yearbook and customs exports, SIPO manufacturing patent counts, and
firm inputs/outputs for the Malmquist construction [E2]. Dataset acquisition and
coverage belong in `Econ Data Know-How`; this record stores the treatment
contract the variation requires.

## Evidence Notes

E1 is the publisher/CrossRef record and establishes the article's identity and
the abstract-reported design and findings; it does not establish the full
specification. E2 is an author-team Chinese dissemination note inspected in
full; it reports the PC construction, data sources, specification, robustness,
and micro hot-zone results, but it is a secondary summary rather than the
article or appendix. E3 and E4 are verified official documents that establish
the development-zone cleanup regime and catalog churn; they do not establish
any city's land-supply behavior. E5 verifies the identity of the official parcel
data platform only. The record is grounded in institutional identity and the
official data source, while the assignment measure remains paper-reported and
its endogeneity is a first-order feature, not a solved problem.
