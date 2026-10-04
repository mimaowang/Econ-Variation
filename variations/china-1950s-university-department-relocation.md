---
schema_version: 2
id: china-1950s-university-department-relocation
name: China's 1950s University Department Relocation and County-Industry Exposure
aliases:
- China's 1952 higher-education department adjustment
- 1950s university department relocation in China
- 中国1950年代高校院系调整
status: grounded
provenance:
  task_id: task-45e31d5a9c60
scope:
  country: China
  regions:
  - Mainland China counties and cities receiving, losing, or reorganizing university departments
  domains:
  - regional-economics
  - urban
  - economic-geography
  - higher-education
  - industrial-development
  variation_type: cohort-rule
  knowledge_role: china-variation
  china_relevance: >
    This was a centrally directed reallocation of university departments that
    changed the spatial supply of specialized human capital in Chinese places.
    The research object is department-level receiving-county and industry
    exposure, not a claim that every university reform or every city received
    the same treatment.
identity:
  instrument: >
    The department-relocation component of China's higher-education adjustment
    program, implemented in phases from 1949 through 1957 and concentrated in
    the large 1952 reorganization. Departments were split, merged, cancelled, or
    moved among institutions and cities to build a specialized system.
  authority: >
    The Central People's Government Ministry of Higher Education and regional
    higher-education adjustment committees directed the program. Contemporaneous
    People's Daily reporting records the national adjustment and the Ministry's
    industrial-training objectives; the Ministry of Education preserves an
    official retrospective account.
  legal_identifiers:
  - 1951 national engineering-college adjustment discussions and the 1952 national higher-education adjustment plan
  - 1952-09-24 People's Daily report that the nationwide adjustment was substantially complete
  - Central Ministry of Higher Education and regional adjustment-committee implementation records
  implementation_regime: >
    The central program reorganized the national map of fields and institutions,
    while regional committees implemented moves, mergers, new specialist colleges,
    staff transfers, and changes in teaching units. The main 1952 wave focused on
    North and East China and was followed by adjustments in other regions through
    1957. Within-city moves, cross-city moves, and cancellations are distinct
    exposure states rather than one automatically interchangeable treatment.
  assignment_mechanism: >
    Central authorities assigned departments and their fields to receiving
    institutions and locations. In the regional application, a county's exposure
    is generated when a relocated department is located there and its field is
    technologically related to an industry in that county. The main contrast is
    within-county across industries, not treated city versus untreated city.
  parent: null
  related_variations: []
timeline:
  announcement: '1951-11'
  effective: '1952-05'
  implementation_start: 1949
  implementation_end: 1957
  local_timing: >
    The author presentation separates four phases: partial adjustments before
    the end of 1951; the North, East, and Northeast wave from June to September
    1952; a Middle-South wave in 1953; and remaining adjustments in 1955–1957.
    The September 1952 report says the nationwide work was basically complete
    while transfers were still underway. Exact department and receiving-county
    dates must come from the historical roster, not one national date.
  anticipation: >
    Plans, conferences, and regional preparation preceded moves, and the program
    overlapped with the First Five-Year Plan and other 1950s spatial investments.
    A national 1952 dummy therefore mixes anticipation and heterogeneous
    implementation and is not the preferred treatment encoding.
  last_verified: '2026-10-05'
assignment:
  unit: >
    County–industry cells for the long-run application, with department,
    institution, city, and receiving-county records as the treatment source.
  treated: >
    A county–industry cell is exposed when a relocated or newly established
    department in that county has a field linked to the industry's patent or
    industrial classification under the paper's department–industry crosswalk.
  comparison_pool: >
    Other industries in the same county with no related relocated department are
    the main comparison. Neighboring counties and industries linked through
    shared labor, input, or knowledge networks may not be clean controls.
  rule: >
    Reconstruct historical department changes, map receiving departments to
    counties and fields, and use the reported CNKI patent and IPC-to-National
    Industrial Classification links to code related county–industry exposure.
    The exact count, share, or indicator normalization remains to be audited.
  intensity: >
    Natural intensity measures are the number or share of related relocated
    departments and their field-specific capacity. The paper's exact normalization
    and treatment of all move types remain unresolved.
  exemptions:
  - Departments never relocated
  - Departments cancelled rather than received elsewhere
  - Within-city moves when the design isolates cross-city relocation
  - Industries with no defensible link under the audited crosswalk
  compliance: >
    The program was centrally directed, but implementation included mergers,
    institutional reorganization, and local execution. A recorded move establishes
    institutional exposure; it does not guarantee graduates, patents, or firms.
  exposure_construction: >
    Join a dated department-change roster to receiving institutions and stable
    county identifiers, classify fields, and merge them with industry observations
    through an inspected patent/industrial-code crosswalk. Keep cross-city,
    within-city, new, and cancelled departments separate until audited.
  required_identifiers:
  - stable county identifier and historical county crosswalk
  - receiving institution and city identifier
  - department or field identifier
  - industry classification and patent-class crosswalk
  - relocation or adjustment phase/date
  - industry observation year
  spillovers: >
    Universities can attract firms, graduates, patents, and collaborators beyond
    county borders. Neighboring counties and related industries may receive
    indirect exposure.
research_compatibility:
  outcome_domains:
  - county-industry employment
  - firm entry and firm counts
  - productivity and value added per worker
  - patents and innovation
  - industrial specialization and regional growth
  - human-capital composition
  affected_populations:
  - Manufacturing firms and workers in Chinese counties
  - University departments, students, and faculty moved by the program
  - Entrepreneurs and industries related to relocated fields
  mechanism_channels:
  - local knowledge spillovers
  - industry-specific talent-pool formation
  - university–industry matching
  - persistent agglomeration and path dependence
  best_for:
  - Long-run county–industry effects of specialized human-capital placement
  - Within-county comparisons that absorb common county shocks
  - Comparing human-capital and physical-capital place-based policies
  not_good_for:
  - Treating all 1950s university changes as one homogeneous city treatment
  - Inferring a clean 1952 cutoff without department-level dates
  - Ignoring the First Five-Year Plan, 156 Projects, Third Front, or transport
design:
  claim_type: causal
  affordances:
  - Centrally directed department relocation across institutions and places
  - Within-county cross-industry exposure after an inspected field link
  - Long-run historical outcomes and post-1978 market-reform comparisons
  - Department-level heterogeneity and knowledge-spillover mechanisms
  candidate_designs:
  - County fixed effects with within-county cross-industry comparisons
  - Historical exposure design using pre- and post-reform industrial observations
  - Heterogeneity by field, relocation type, and market-reform period
  - Spatial-spillover and neighboring-county designs
  identifying_variation: >
    The identifying contrast is the difference within a county between industries
    linked to relocated departments and industries not linked to them, conditional
    on the audited roster, industry link, and pre-program structure.
  primary_strategy: >
    The paper reports county-industry regressions with county fixed effects and
    department–industry relatedness from patent and industrial classifications.
    A replication should retain the within-county contrast, code phases separately,
    and account for other 1950s place-based investments.
  estimand: >
    The long-run effect of exposure to a relocated university department in a
    technologically related county–industry cell on employment, firm entry,
    productivity, or innovation relative to other industries in that county.
  treatment_variable: >
    A department–industry exposure indicator or intensity measure derived from
    relocated departments in the receiving county and an audited field–industry
    crosswalk; the paper's exact normalization is not yet independently reproduced.
  comparison_logic: >
    Compare related and unrelated industries within the same county, use
    pre-program industrial structure where available, and treat neighboring or
    network-connected counties as potentially contaminated.
  estimation_notes: >
    The December 2025 presentation's slide 19 equation uses log manufacturing
    outcome and IndustryRelatedRelocation at county–industry level, with both
    county and industry fixed effects. Slide 24, Table 3, clusters historical
    selection-check errors by county; this does not verify every final-paper
    specification or how zero outcomes enter logs.
    The paper reports weak or absent effects during the planned-economy period
    and stronger persistent effects after market reforms, with patent and human-
    capital mechanisms. These are source-reported findings, not independently
    replicated estimates here.
  assumptions:
  - Conditional on county and industry controls, department placement is not driven by unobserved future county–industry growth
  - The department-to-industry crosswalk captures technologically relevant exposure
  - Concurrent spatial policies and transport changes are controlled or do not explain the contrast
  - Relocated departments affect outcomes through human-capital and knowledge channels rather than an unrecorded direct subsidy
  - Spillovers and historical boundary changes are measured sufficiently
  diagnostics:
  - Reconstruct the department roster and receiving-county dates from historical and primary records
  - Plot pre-program county–industry differences using 1933 and 1953 information
  - Exclude counties affected by 156 Projects or Third Front construction
  - Vary the department–industry and patent-class mapping
  - Separate cross-city moves, within-city moves, cancellations, and new departments
  - Test neighboring-county and labor or knowledge-network spillovers
threats:
- type: nonrandom_department_location
  basis: reported
  condition: Central placement may reflect ideological, educational-equality, national-talent, political, or pre-existing industrial considerations correlated with later growth.
  evidence_refs:
  - E3
  - E4
  possible_diagnostics:
  - Pre-program county–industry balance and trends
  - Controls for historical industrial structure and competing spatial programs
  - Samples excluding strategically targeted regions
- type: concurrent_place_based_policies
  basis: reported
  condition: The First Five-Year Plan, 156 Projects, Third Front construction, and transport investments overlap the relocation period.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Explicit controls or exclusions for contemporaneous programs
  - Compare human-capital exposure with physical-capital exposure
  - Falsification on unrelated industries
- type: department_industry_measurement
  basis: reported
  condition: The patent and industrial-code mapping may be noisy or sensitive to the technology definition.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Rebuild the CNKI and IPC-to-industry crosswalk
  - Use alternative patent, input-output, and job-posting links
  - Report broad and narrow field definitions
- type: timing_and_phase_heterogeneity
  basis: reported
  condition: The program ran from 1949 to 1957 in several regional waves, so one 1952 date mixes anticipation and treatment.
  evidence_refs:
  - E1
  - E3
  possible_diagnostics:
  - Phase-specific dates and cohorts
  - Exclude transition years or estimate dynamic effects
  - Sensitivity to within-city and cross-city definitions
- type: spatial_and_network_spillovers
  basis: inferred
  condition: Departments, graduates, patents, and firms can affect neighboring counties and related industries.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Distance bands and neighboring-county exposure measures
  - Labor, patent, and input-output network tests
  - Exclude highly connected counties
empirical_requirements:
  contract_version: 1
  population: Chinese counties and manufacturing industries, with university departments and related firms or workers
  observation_unit: County-industry-year or county-industry historical census observation
  geography_level: County, city, and province with historical boundary crosswalks
  time_start: 1933
  time_end: 2017
  minimum_frequency: Irregular historical censuses with annual or event-time mechanism data where available
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - county and historical county identifier
  - industry code and field–industry relatedness measure
  - department relocation or adjustment status and phase/date
  - receiving institution and city
  - employment, firm count, productivity, or value-added outcome
  - pre-program industrial structure
  - patent or knowledge-spillover measure for mechanism work
  - indicators for 156 Projects, Third Front, and transport exposure when relevant
  required_identifiers:
  - county_id
  - historical_county_id
  - industry_code
  - department_id or field_code
  - institution_id
  - year
  treatment_key:
  - receiving_county_id
  - department_field_code
  - department_industry_link
  - relocation_phase_or_year
  treatment_source: >
    The paper reports tracing 1,847 pre-1952 departments primarily from Ji (1990),
    then linking fields to industries through CNKI patents and the CNIPA IPC-to-
    National Industrial Classification table. Its Mendeley replication record is
    published, but the public metadata query inspected on 2026-10-02 reports size 0;
    no roster, code, or usable file payload was verified. Do not treat the roster or
    exposure normalization as independently reproducible yet.
  measurement_risks:
  - incomplete or inconsistent historical department names and institution identifiers
  - county boundary changes between historical censuses
  - uncertainty over whether within-city moves count as exposure
  - noisy department–industry and patent-class mapping
  - selective survival and coverage in historical industrial data
  - overlapping physical-capital and transport policies
design_profiles: []
evidence:
- id: E1
  source_type: archive
  citation: 'People''s Daily. 1952-09-24. “全国高等学校院系调整基本完成” [Nationwide higher-education department adjustment basically complete].'
  url: https://cn.govopendata.com/renminribao/1952/9/24/1/?amp=1
  date: '1952-09-24'
  supports:
  - identity.authority
  - identity.implementation_regime
  - timeline.announcement
  - timeline.effective
  - timeline.implementation_start
  - timeline.local_timing
  - assignment.unit
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: 'Page 1, contemporaneous report on national adjustment, regional focus, specialist colleges, Ministry direction, and ongoing transfers.'
- id: E2
  source_type: implementation-document
  citation: 'Ministry of Education of the People''s Republic of China. 2009. “完成高校院系调整” [Completing the higher-education department adjustment].'
  url: https://www.moe.gov.cn/jyb_xwfb/xw_zt/moe_357/s3581/moe_2669/moe_2921/tnull_50924.html
  date: 2009
  supports:
  - identity.authority
  - identity.implementation_regime
  - timeline.effective
  - timeline.implementation_start
  - timeline.implementation_end
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: 'Official Ministry portal retrospective on industrial-training objectives, national scope, and the 1952–1957 context.'
- id: E3
  source_type: paper
  citation: 'Fan, Jianyong, Wei Tang, and Feng Zhang. 2025. “Persistent Effects of Universities on Local Industrial Growth: Evidence from China''s Policy-induced College Relocation in the 1950s.” Author presentation, December 2025.'
  url: https://voxdev.org/sites/default/files/2025-12/Persistent%20effects%20of%20universities%20on%20local%20industrial%20growth.pdf
  date: 2025
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.treated
  - assignment.comparison_pool
  - assignment.exposure_construction
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.estimation_notes
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_source
  verification_status: reported
  access_level: full-text
  locator: 'Author presentation slides 2–18 and 36–44: phases, data, mechanisms and competing policies. On 2026-10-05 the embedded equation on slide 19 and Table 3 on slide 24 were visually inspected through their PDF image objects: county/industry fixed effects and county-clustered historical selection checks. This is an author presentation, not visual verification of the final article or a recovered normalization formula.'
- id: E4
  source_type: paper
  citation: 'Fan, Jianyong, Wei Tang, and Feng Zhang. 2026. “Persistent Effects of Universities on Local Industrial Growth: Evidence from China''s Policy-induced College Relocation in the 1950s.” Journal of Development Economics 179:103628. DOI: 10.1016/j.jdeveco.2025.103628.'
  url: https://doi.org/10.1016/j.jdeveco.2025.103628
  date: 2026
  supports:
  - identity.instrument
  - assignment.treated
  - design.identifying_variation
  - design.estimand
  - design_applications.treatment_encoding
  - design_applications.comparison
  - design_applications.data_used
  - design_applications.empirical_design
  - design_applications.assumptions
  - design_applications.threats_addressed
  - empirical_requirements.observation_unit
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_source
  verification_status: reported
  access_level: full-text
  locator: 'ScienceDirect full-text HTML inspected: Historical background; Data; Baseline regressions; Mechanisms; and Further discussion sections. It describes the 1950s department reallocation, county-industry sample and within-county cross-industry specification, Ji (1990) roster source, CNKI/IPC-to-industry link, historical outcomes, mechanisms, and treatment of 156 Projects and Third Front as concurrent place-based policies.'
- id: E5
  source_type: replication
  citation: 'Fan, Jianyong, Wei Tang, and Feng Zhang. 2025. Replication data for “Persistent Effects of Universities on Local Economic Growth.” Mendeley Data, version 1. DOI: 10.17632/5pdtx4t4r3.1.'
  url: https://data.mendeley.com/api/datasets-v2/datasets/5pdtx4t4r3?fields=repository.*&version=1
  date: '2025-12-04'
  supports:
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: metadata
  locator: >
    Public dataset metadata and version page inspected on 2026-10-02. The record describes
    itself as the article's replication data and states a CC BY 4.0 licence; the public API
    metadata response reports size 0, and no roster, code, or file payload was available in
    the inspected response. This verifies the existence and current metadata state of the
    replication record, not that replication materials can be downloaded or run.
design_applications:
- paper: 'Persistent Effects of Universities on Local Industrial Growth: Evidence from China''s Policy-induced College Relocation in the 1950s'
  doi: 10.1016/j.jdeveco.2025.103628
  journal: Journal of Development Economics
  year: 2026
  research_question: How does centrally relocated university-department capacity affect long-run industrial growth in receiving Chinese counties?
  population: Chinese county–industry cells and firms observed in historical industrial surveys and later census or registry data
  outcome: Employment, firm counts, productivity or value added, patents, and human-capital mechanisms in related industries
  data_used:
  - Changes in Chinese Higher Education Institutions (Ji, 1990) and hand-collected department histories
  - 1933 industrial survey and 1953 population information
  - 1985 national industrial census and 1995/2004 economic censuses
  - Business registration, patent, and patent-citation data
  - CNKI patent data and IPC-to-National Industrial Classification reference table
  treatment_encoding: >
    County exposure to a relocated department is linked to an industry through
    the paper's department–patent–industry crosswalk; the presentation reports
    county fixed effects and within-county cross-industry variation. Exact
    normalization and treatment of all move types remain to be audited.
  comparison: >
    Industries in the same county without a related relocated department, with
    controls for historical industrial structure and sensitivity to concurrent
    place-based programs.
  empirical_design: County–industry contrasts with county and industry fixed effects in the inspected presentation equation; long-run outcomes and mechanism analyses
  assumptions:
  - Department placement is conditionally unrelated to future county–industry growth
  - The field–industry crosswalk measures relevant exposure
  - Concurrent spatial policies and boundary changes are accounted for
  - Spillovers do not invalidate the chosen within-county comparison
  threats_addressed:
  - Historical selection and location choice through pre-period controls and diagnostics
  - Concurrent 156 Projects, Third Front, and transportation exposure
  - Alternative department–industry links and spatial spillovers
  evidence_refs:
  - E3
  - E4
  - E5
method_transfer: null
readiness_blockers:
- The paper and author presentation report tracing 1,847 pre-1952 departments from Ji (1990), but the underlying roster, code, and exact exposure normalization have not been independently recovered or rerun. The linked Mendeley replication record currently reports zero bytes in its public API metadata; its page alone does not verify usable files.
- The 1952 adjustment plan and regional records should be linked to a machine-readable department–institution–county history before design-documented admission.
- Historical county boundaries, department names, and the CNKI/IPC-to-industry crosswalk may introduce material measurement error.
- Relocation overlaps the First Five-Year Plan, 156 Projects, Third Front construction, and transport changes; the program is not intrinsically exogenous.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

After 1949, the central government reorganized higher education to supply specialized personnel for planned industrialization and to replace the pre-1949 comprehensive-university structure with a more specialized system. The contemporaneous September 1952 report describes a nationwide adjustment led by the Ministry of Higher Education, regional concentration in North and East China, new specialist colleges, and transfers of staff and teaching units [E1]. The Ministry's official account explains the industrial-training and Soviet-model objectives and places the broader adjustment in the 1952–1957 period [E2].

## What Changed

The program changed the location and institutional home of university departments rather than simply adding the same university to every city. Departments were split, merged, cancelled, or transferred; engineering, geology, steel, aviation, water conservancy, agriculture, medicine, and teacher-training fields were reorganized into specialist institutions [E1; E2]. The canonical boundary is the department-relocation and receiving-location component. Later higher-education expansion, a university's overall reputation, and the separate 156 Projects or Third Front programs are related but not substitutes for this instrument.

## Implementation and Assignment

Exposure is not a national 1952 dummy. The program had several phases from 1949 through 1957, with a large North/East/Northeast wave in mid-1952, further regional adjustments in 1953, and remaining changes in 1955–1957 [E1; E3]. For the regional application, a receiving county becomes exposed to an industry when a relocated department there has a field linked to that industry through the inspected patent and industrial-code crosswalk [E3; E4]. The practical comparison is among industries within the same county, while neighboring counties, related fields, and later labor or knowledge flows may be indirectly treated.

## Why This Creates Empirical Variation

The design uses a centrally directed historical reallocation of specialized human capital to create county–industry differences. County fixed effects remove common local shocks, while the department–industry link allows industries in one county to receive different exposure. Its identifying content comes from the conditional cross-industry contrast and the quality of the historical roster, not from a claim that the central program was random [E3; analytical inference].

## Identification Risks

Departments may have been placed for ideological, educational-equality, national-talent, political, or industrial reasons that also predict later growth. The program overlaps with the First Five-Year Plan, 156 Projects, Third Front construction, and transport investments. A single 1952 date mixes anticipation and several regional waves. The department–industry crosswalk, historical county boundaries, surviving industrial observations, and university spillovers are additional risks [E3; E4; analytical inference].

## Data Requirements

At minimum, a study needs stable historical county identifiers, a dated department-to-institution and receiving-county roster, department fields, an inspected field–industry crosswalk, and county–industry outcomes. The application reports historical industrial and population sources for 1933, 1953, 1985, 1995, and 2004, plus business-registration, patent, and patent-citation data for later mechanisms [E3; E4]. Dataset acquisition and coverage belong in `Econ Data Know-How`; this record stores the treatment contract and joins it requires.

## Evidence Notes

E1 is a contemporaneous newspaper archive and establishes the national administrative action, regional focus, objectives, specialist-college creation, and continuing transfers; it does not provide the complete department roster or an exogenous-assignment guarantee. E2 is an official retrospective and establishes the broader 1952–1957 context; it does not establish each department's receiving county. E3 is an inspectable author presentation and reports the paper's phases, data sources, county–industry specification, and mechanisms; it is not the article's full appendix or raw roster. E4 is the inspected publisher full-text HTML and documents the paper's reported county-industry construction, historical sources, data links, and treatment of concurrent place-based policies; it still does not independently supply its roster, code, or an exogenous-assignment guarantee. E5 confirms that a public replication-data record exists, but its current metadata response reports zero bytes and does not expose a usable roster or code file. The record is grounded in institutional identity and core timing, while exact treatment construction and reproducibility remain explicit blockers.
