---
schema_version: 2
id: china-airport-network-incidental-county-access
name: China Airport Network Expansion and Incidental County Access
aliases:
- Incidental county access to China's expanding domestic airport network
- 中国机场网络扩张与非机场县可达性
status: grounded
provenance:
  task_id: task-5d62ec8c635b
scope:
  country: China
  regions: [Mainland Chinese counties in the paper's harmonised geography]
  domains: [regional-economics, urban-economics, transport-infrastructure, development-economics]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: County exposure to China's domestic airport expansion is linked to Chinese industrial activity and local GDP; the comparison focuses on incidental beneficiaries rather than airport host locations.
identity:
  instrument: Expansion of the operational domestic civil airport network
  authority: Civil Aviation Administration of China and airport-development authorities
  legal_identifiers:
  - 全国民用机场布局规划, approval reported by CAAC on 2008-01-25
  - CAAC 2009 and 2010 annual airport production statistical bulletins
  implementation_regime: >
    Operational availability of airport nodes during 2000-2009 changes potential
    domestic access. The 2008 national plan provides institutional context, not
    a common effective date or the sole authorisation for every observed opening.
  assignment_mechanism: >
    New nodes alter the geometric relation of counties to nearby origin airports
    and domestic destinations. The research restricts counties to buffers between
    initially available and newly available airports, then uses continuous changes
    in a potential-access index; it does not randomise airport siting.
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 2000
  implementation_end: 2009
  local_timing: >
    These years bound the research's airport-access window, not the institutional
    lifetime of airport expansion. Use each node's operational year, not the
    plan's publication year or a statistical bulletin's publication date.
  anticipation: Planned airports may influence activity before operation; the paper's future-airport placebo does not rule out every anticipatory response.
  last_verified: '2026-09-28'
assignment:
  unit: Historical county-period, with county-industry outcomes in the principal application
  treated: Counties with greater increases in potential domestic airport access within the incidental-beneficiary sample
  comparison_pool: >
    Less-exposed counties in the same restricted geography and initial-airport
    groups, including counties retaining their old nearest airport. These are
    not necessarily unexposed because the destination network also expands.
  rule: >
    For each interval retain counties satisfying abs(d_old-d_new)/d_old < 0.60,
    where d_old is distance to the nearest initially available airport and d_new
    distance to the nearest airport newly available during the interval. This
    symmetric buffer excludes locations close to either airport and distant
    locations; it is a sample restriction, not a legal eligibility threshold.
  intensity: Change in log potential airport-access index, with airport pairs and population weights fixed apart from node availability
  exemptions: [International destinations are outside the constructed domestic-access index]
  compliance: A licensed airport, an operating airport, a regular-service city and a paper-defined node are different objects; actual route frequency is not the treatment.
  exposure_construction: >
    At sampled points within each county compute air_it = sum over the five
    nearest available origin airports j of [(sum over eligible domestic destination
    airports k of pop_k/airtime_jk)/landtime_ij], then average across county points.
    Destination weights are fixed 2000 populations of airport-containing counties.
    Appendix A uses landtime=sqrt(2)*distance/65 km per hour and airtime=distance/800
    km per hour plus one hour; omit airport pairs closer than 200 km. County sampling
    is area-proportional, with 3-200 points. Do not replace this construction with
    a nearest-airport dummy, a centroid measure, or observed passenger traffic.
  required_identifiers: [Harmonised county polygon and code, Airport node and coordinates, Operational year, County-industry-year]
  spillovers: Network expansion can improve access without changing a county's nearest airport; airport-host effects and actual route decisions are outside the isolated contrast.
research_compatibility:
  outcome_domains: [Industrial productivity, Industrial output, Value added, County GDP]
  affected_populations: [Manufacturing in incidental-beneficiary counties, Local economies outside airport host locations]
  mechanism_channels: [Potential domestic travel-time reduction, Access to other markets and knowledge]
  best_for: [Testing local economic responses to potential airport-network access where historical geography and network availability can be reconstructed]
  not_good_for:
  - Estimating the effect of airport passenger traffic without a separate traffic identification design
  - Treating all airport-host cities or all counties after 2008 as randomly treated
design:
  claim_type: reduced-form
  affordances: [Continuous exposure, Geographic incidental-beneficiary comparison, Long differences]
  candidate_designs: [County-industry long-difference regression, County GDP long-difference regression]
  identifying_variation: Differential access changes within buffers and groups sharing an initially nearest airport, not the national airport trend alone
  primary_strategy: >
    Relate long changes in outcomes to lagged log-access changes in the restricted
    sample, controlling for initial access and group-period and industry effects.
    This is not a sharp boundary RDD or random assignment of airport locations.
  estimand: Outcome response to potential domestic access expansion among incidental-beneficiary counties, conditional on comparable counterfactual trends
  treatment_variable: Delta log of the geometrically constructed domestic potential-access index
  comparison_logic: Compare greater and smaller continuous exposure changes among geographically neighbouring counties, conditional on initially nearest airport and interval.
  estimation_notes: >
    Main industrial observations are 2001, 2005 and 2009, matched to access in
    2000, 2004 and 2008, yielding two four-year changes. Employment and fixed assets
    enter the productivity specification through quadratic log-input controls.
    Preserve initial-access trend controls, industry effects and initial-airport
    grouping; standard errors are clustered by nearest airport. After 2007 firm
    identifiers are unavailable in the reported source, so the application uses
    county-by-two-digit-industry aggregates, not firm fixed effects.
  assumptions:
  - Conditional outcome trends within the buffer are not driven by unobserved spatial development shocks correlated with new airport geometry.
  - Historical county harmonisation and airport-node coding do not mechanically create access or outcome changes.
  - The potential-access index is the intended exposure; realised travel and traffic require additional interpretation.
  diagnostics: [Initial characteristics and 1990-2000 population trends, Alternative buffer widths, Alternative speeds and destination weights, Future planned-airport placebo, Concurrent road and rail controls]
threats:
- type: Endogenous airport development
  basis: documented
  condition: National planning incorporates economic and transport development objectives; spatial buffers mitigate direct targeting but do not prove conditional exogeneity.
  evidence_refs: [E1, E4]
  possible_diagnostics: [Compare pre-trends within initial-airport groups, Audit concurrent transport and place-based investments]
- type: Potential versus realised access
  basis: reported
  condition: Index changes encode feasible connections, not complete observed routes or their frequency; interpret them as infrastructure-access exposure rather than actual travel treatment.
  evidence_refs: [E4]
  possible_diagnostics: [Separate route availability and traffic mechanisms from the assignment measure]
- type: Node and administrative harmonisation
  basis: documented
  condition: Official airport and service-city counts differ, and the paper combines nearby airports in Beijing and Shanghai. A generic airport list or current county geography cannot reproduce the paper's exposure.
  evidence_refs: [E2, E3, E4]
  possible_diagnostics: [Recover the exact node crosswalk, Audit openings versus resumptions and relocations, Reconcile outcomes to harmonised county units]
empirical_requirements:
  contract_version: 1
  population: Chinese manufacturing represented in the annual industrial survey and the incidental county sample
  observation_unit: County-by-two-digit-industry at long-difference endpoints
  geography_level: Harmonised 2004 county geography including the paper's urban-district aggregations
  time_start: 2000
  time_end: 2009
  minimum_frequency: Outcome endpoints 2001, 2005, 2009 and preceding-year airport access
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields: [Gross industrial output, Employment, Total fixed assets, Airport coordinates and operational years, Fixed 2000 destination population, County polygons, Initial airport distance and access]
  required_identifiers: [Harmonised county code, Two-digit industry code, Year, Airport node identifier, Initial-nearest-airport group]
  treatment_key: [Harmonised county, Access year]
  treatment_source: Historical CAAC airport availability reconciled to the paper's nodes and GIS construction; the inspected annual bulletins are primary anchors, not a complete recovered panel
  measurement_risks:
  - Stable firm identifiers are not a requirement for the published county-industry design; recover aggregation and sample rules instead.
  - The county point draw, airport merging, closure and resumption rules must be recovered before claiming numerical replication.
  - One initial endpoint describes a long-difference comparison, not sufficient pre-trend data for a new event study.
design_profiles:
- id: county-gdp-long-difference
  label: County GDP response to potential airport access
  design_families: [Long differences, Continuous geographic exposure]
  when_to_use: County GDP is available but firm-survey aggregates are not; this is the paper's distinct outcome-data application of the same assignment.
  outcome_domains: [County GDP]
  requirements:
    population: Counties with linkable county GDP and historical airport exposure
    observation_unit: County at long-difference endpoints
    geography_level: Paper-harmonised county geography
    time_start: 2001
    time_end: 2010
    minimum_frequency: GDP endpoints 2002, 2006, 2010 matched to access 2001, 2005, 2009
    minimum_pre_periods: 1
    minimum_post_periods: 1
    required_fields: [County GDP, Airport coordinates and operational years, Fixed 2000 destination population, County polygons, Initial airport distance and access]
    required_identifiers: [Harmonised county code, Year, Airport node identifier, Initial-nearest-airport group]
    treatment_key: [Harmonised county, Access year]
evidence:
- id: E1
  source_type: policy-document
  citation: CAAC. 2008. 全国民用机场布局规划获得国务院批准.
  url: https://www.caac.gov.cn/XWZX/MHYW/200801/t20080125_11773.html
  date: '2008-01-25'
  supports: [identity.authority, identity.legal_identifiers, identity.implementation_regime, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Approval report and planning objectives; 2006 baseline, 2020 target and planning process. Publication reports approval already granted, not an inspected signed approval date or a universal airport-opening date.
- id: E2
  source_type: official-data
  citation: CAAC. 2009年全国机场生产统计公报, published 2010-02-05.
  url: https://www.caac.gov.cn/XXGK/XXGK/TJSJ/201511/t20151102_8735.html
  date: '2010-02-05'
  supports: [identity.instrument, identity.legal_identifiers, timeline.local_timing, assignment.compliance, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Section I reports 166 licensed airports, 165 regular-service airports and 163 service cities for 2009, naming new service cities and Guangyuan's resumption. The attached spreadsheet was not inspected.
- id: E3
  source_type: official-data
  citation: CAAC. 2010年全国机场生产统计公报, published 2011-03-15.
  url: https://www.caac.gov.cn/XXGK/XXGK/TJSJ/201511/t20151102_8763.html
  date: '2011-03-15'
  supports: [identity.instrument, timeline.local_timing, assignment.compliance, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Section I reports 175 licensed and regular-service airports, 172 service cities, and newly served cities. This is a primary endpoint check, not proof of the paper's precise 172-node roster.
- id: E4
  source_type: paper
  citation: 'Gibbons, Stephen, and Wenjie Wu. 2020. Airports, access and local economic performance: evidence from China. Journal of Economic Geography 20(4):903-937. Online 2019-12-31. DOI 10.1093/jeg/lbz021.'
  url: https://doi.org/10.1093/jeg/lbz021
  date: 2020
  supports: [scope.china_relevance, identity.assignment_mechanism, timeline.implementation_start, timeline.implementation_end, assignment.rule, assignment.comparison_pool, assignment.exposure_construction, design.primary_strategy, design.estimand, design.estimation_notes, empirical_requirements.required_fields, empirical_requirements.required_identifiers, design_applications.data_used, design_applications.treatment_encoding, design_applications.empirical_design, threats.condition]
  verification_status: verified
  access_level: full-text
  locator: Publisher HTML at https://academic.oup.com/joeg/article/20/4/903/5692238 and redirected https://oup.silverchair-cdn.com/article-minimal/5692238, inspected 2026-09-28; sections 3.1-3.3, equation 3.2, sample restriction around Figure 1, section 4, Appendix A and footnote 9. Paper-reported design and data were inspected; replication files and raw microdata were not.
design_applications:
- paper: 'Airports, access and local economic performance: evidence from China'
  doi: 10.1093/jeg/lbz021
  journal: Journal of Economic Geography
  year: 2020
  research_question: How does improved domestic airport access affect manufacturing performance and county economic activity?
  population: Chinese county-industry aggregates and county economies in incidental-beneficiary buffers
  outcome: Industrial output and productivity, value added and county GDP
  data_used: [Annual Survey of Industrial Firms, County statistical yearbooks, CAAC airport information, 2004 county boundaries, 2000 and 1990 population census information]
  treatment_encoding: Lagged long changes in log potential airport access, with fixed distances, assumed speeds and baseline population weights
  comparison: Greater and smaller access gains within the incidental buffer, conditional on initial-airport grouping and baseline access
  empirical_design: County-industry and county GDP long-difference regressions; value-added availability yields a separate 2001-2007 outcome interval with access 2000-2006
  assumptions: [Comparable conditional trends despite endogenous airport siting, Faithful geographic and aggregate-outcome construction]
  threats_addressed: [Initial balance and population trends, Buffer and index sensitivity, Future airport placebo, Concurrent transport controls]
  evidence_refs: [E4]
method_transfer: null
readiness_blockers:
- Recover the complete historical node roster, operational dates and merging, resumption, closure and relocation rules; the inspected primary bulletins do not independently verify every airport-year used by the paper.
- Obtain GIS construction and county crosswalks, point sampling and exposure code before claiming exact treatment replication; official counts cannot substitute for paper nodes.
- Confirm industrial survey access, aggregation filters and yearbook harmonisation. No raw-data access or executable reproduction was verified.
---

## Institutional Background

[E1-E3, verified] Airport expansion is a national infrastructure process with
local operational events. Economic development enters its planning, so an
official plan does not make airport placement exogenous. The empirical object
here is access gained by other counties, not the return to hosting an airport.

## What Changed

An additional airport can shorten ground access, extend domestic destination
access, or do both. [E4, inspected paper report] The index isolates this change in
potential infrastructure access. It intentionally does not absorb demand-driven
route frequency or contemporaneous improvements in road travel speed.

## Implementation and Assignment

Keep calendar dates and units distinct. [E2] A city regaining regular service is
not necessarily a newly built airport. [E3-E4] An official airport count, service
city count and merged paper-node count are not interchangeable. Footnote 9 explains
the paper's Beijing/Shanghai merging but does not establish the complete crosswalk.

## Why This Creates Empirical Variation

[E4, inspected paper report] Restricting attention to counties between old and new
airport catchments avoids the most directly targeted places. Neighbouring counties
can nevertheless receive different access gains. This motivates a comparison;
it does not turn the buffer into a legal cutoff or an unconditionally random
experiment. Counties keeping their nearest airport may still gain destinations.

## Identification Risks

[Analytical inference] Geographic proximity helps only if relevant economic
trends and co-investments remain comparable after controls. [E4, paper report]
The historical military-airport IV exercise is supplementary and weak, not the
main identification strategy; do not relabel this record an established IV.
Potential travel access also cannot independently identify which realised travel,
market or knowledge channel caused the estimated outcome response.

## Data Requirements

Build the county-access panel first, then join by harmonised county and access
year, with the paper's one-year lag to outcomes. County-industry aggregation avoids
inventing stable post-2007 firm identifiers. Use the separate GDP profile when
that is the outcome data actually available. The complementary data repository
should document assets and acquisition paths through the DOI rather than duplicate
this assignment record.

## Evidence Notes

The primary institutional anchors and actual published construction justify a
grounded conditional record. Historical candidate `candidate-38c462868273` remains
the provenance of the earlier access blockage; the new task records the changed
source accessibility. This admission does not claim numerical replication,
verified access to proprietary microdata, or design-documented readiness.
