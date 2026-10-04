---
schema_version: 2
id: china-mic25-pilot-city-high-tech-clusters
name: China Made in China 2025 Pilot-City High-Tech Cluster Rollout
aliases:
- MIC25 pilot-city clusters
- Made in China 2025 city pilot
- 中国制造2025试点示范城市
- MIC25 high-tech cluster policy
status: grounded
provenance:
  task_id: task-17607a3a90bc
scope:
  country: China
  regions:
  - Mainland China prefecture-level and province-level cities in the 30-city MIC25 pilot
  domains:
  - regional-economics
  - urban-economics
  - labor
  - industrial-policy
  - technological-change
  - housing
  - economic-geography
  variation_type: pilot-assignment
  knowledge_role: china-variation
  china_relevance: >
    The record captures the staggered city-level implementation of the Made in China
    2025 high-tech-cluster pilots, not the national strategy in the abstract. Thirty
    cities were selected between 2016 and 2017 and then published city-specific
    development blueprints. Those blueprints attached local fiscal, land, talent,
    regulatory, and industrial-support packages to selected high-tech sectors, creating
    a dated place-based exposure for city labor, housing, and firm outcomes.
identity:
  instrument: >
    The MIC25 pilot-city high-tech-cluster designation and the associated city
    development blueprint. The treatment object is the pilot-city implementation
    package and its city-specific starting quarter; the broad 2015 national strategy,
    later National Demonstration Zone upgrade, individual subsidies, and subsequent
    technology outcomes are related but not interchangeable objects.
  authority: >
    The State Council issued Made in China 2025 (Guofa [2015] No. 28). The Ministry
    of Industry and Information Technology and other central bodies selected and
    supported pilot cities, while each selected city published and implemented its
    own blueprint. The central selection process was not fully disclosed, so the
    authority of the designation does not imply random assignment.
  legal_identifiers:
  - State Council, Made in China 2025, Guofa [2015] No. 28 (2015-05-08)
  - MIIT approval of Ningbo as the first MIC25 pilot demonstration city (2016-08-18)
  - City-specific MIC25 development blueprints and implementation notices for the 30 pilot cities
  - 2018 upgrade of pilot cities to National Demonstration Zones, treated as a later related regime
  implementation_regime: >
    The national plan named ten priority manufacturing areas and encouraged local
    experimentation. Ningbo was the first approved pilot in August 2016; the other
    29 cities were selected through the end of 2017. A city became exposed in the
    paper's main coding when it published its own MIC25 development plan, usually a
    few months after central approval. The plans did not require every city to build
    every priority industry: each city emphasized its existing comparative industries.
    In 2018 the pilot cities were upgraded to National Demonstration Zones with
    additional support; that later upgrade is outside this record's primary treatment
    clock.
  assignment_mechanism: >
    Local governments applied and the central government selected 30 cities after
    considering industrial and regional characteristics, but the rejected applicant
    list and a complete selection formula were not published. The research application
    therefore uses propensity-score matching on pre-policy city size, employment,
    GDP per capita, land area, industrial-firm count, tax income, primary-sector share,
    and their 2010-2015 growth rates. Matching makes the comparison more transparent;
    it does not turn policy selection into a random draw.
  parent: null
  related_variations:
  - china-industrial-park-political-connection-rotation
  - china-industrial-parks-edge-city-spillovers
  - china-industrial-transfer-policy-inland-city-status
  - china-from-imitation-to-innovation
timeline:
  announcement: '2016-08'
  effective: null
  implementation_start: 2016
  implementation_end: 2017
  local_timing: >
    The paper's Table 1 codes the starting date as the quarter in which a city
    published its own MIC25 development plan: 2016Q2 Ningbo; 2017Q1 Shenyang,
    Changchun, Nanjing, Wuxi, Changzhou, Suzhou, Zhenjiang, and Quanzhou; 2017Q2
    Huzhou, Zhengzhou, Luoyang, Xinxiang, Changsha, Zhuzhou, Xiangtan, Hengyang,
    Zhuhai, Foshan, Jiangmen, Zhaoqing, Yangjiang, Zhongshan, and Chengdu; 2017Q3
    Hefei, Wuhan, and Wuzhong; and 2017Q4 Ganzhou, Qingdao, and Guangzhou. These
    cohorts sum to 30 cities. The paper distinguishes this blueprint date from the
    central approval date and from the 2018 National Demonstration Zone upgrade.
    The official notice dates Ningbo's first approval to 2016-08-18, which does not
    line up mechanically with the paper's 2016Q2 cohort label; preserve both fields
    and resolve the underlying Ningbo plan date before treating the quarter as an
    administrative effective date.
  anticipation: >
    The national 2015 plan, local applications, and preparation of city blueprints
    could generate expectations before the paper's coded quarter. The blueprint date
    is an administrative exposure clock, not proof that firms, workers, or housing
    markets changed only after that date. The paper's event-time leads and pre-period
    balance checks are therefore part of the design rather than evidence that
    anticipation was impossible.
  last_verified: '2026-08-12'
assignment:
  unit: >
    A city-quarter for aggregate housing and labor outcomes; a city-industry-quarter
    for job openings and offered wages; and a city-year or firm-year for registered
    firms and migrant mechanisms. Neighboring-city observations are kept as a
    separate spatial exposure rather than folded into the pilot-city treatment.
  treated: >
    One for a city in the 30-city pilot list from the quarter in which that city
    published its MIC25 blueprint onward. For industry applications, retain the
    city-by-industry cell and distinguish the four paper groupings (IT, science,
    manufacturing, and business) and routine versus non-routine occupations where
    those classifications are available.
  comparison_pool: >
    The primary comparison is a propensity-score-matched non-pilot city selected from
    the 335-city universe using 2015 levels and 2010-2015 growth rates of the listed
    city characteristics. The broader non-pilot pool excludes cities adjacent to pilot
    cities when used for the main comparison. A matched city is a design choice, not
    automatically an untreated counterfactual.
  rule: >
    Join the paper's 30-city cohort table to stable prefecture or municipality codes,
    expand each cohort from its blueprint quarter, and construct event time in
    quarters. Keep central selection, city blueprint, targeted industry, occupation,
    matched-control status, and neighboring status as separate fields. Do not code a
    city as treated merely because it adopted a generic industrial policy or because
    it was later included in a National Demonstration Zone.
  intensity: >
    The primary exposure is the binary pilot designation and event time. Useful
    secondary dimensions are the city's selected industries, routine versus
    non-routine job type, years since blueprint, and the separate five-nearest-neighbor
    exposure. Actual subsidy amounts, project counts, and take-up are not uniformly
    observed and must not be imputed from the designation.
  exemptions:
  - The 2018 National Demonstration Zone upgrade when the research question is the initial pilot rollout
  - Cities adjacent to both a pilot and a matched control city in the paper's spillover sample
  - Generic MIC25-related local policies in non-pilot cities, unless they are independently coded as contamination
  - City-industry cells for sectors not represented in the local blueprint or the job-posting classification
  compliance: >
    Pilot status created eligibility for substantial fiscal, credit, land, talent,
    and regulatory support, but the policy package was locally tailored. A pilot city
    could emphasize only its advantageous sectors, and designation does not establish
    that every firm received a subsidy or that every worker was exposed.
  exposure_construction: >
    Build a dated city cohort table from the paper's blueprint publication dates and
    official notices, then merge it to quarterly MetroData job postings, city-level
    Anjuke housing-price indices, firm-registration records, and any migrant survey
    outcomes. For the spillover design, identify the five closest cities that are
    neither pilot nor matched-control cities for each focal city, and remove cities
    adjacent to both sides to avoid double counting. Preserve the paper's cohort date
    and the later 2018 upgrade as separate variables.
  required_identifiers:
  - Stable prefecture-level or municipality city code
  - MIC25 pilot cohort and blueprint publication quarter
  - Matched control city and propensity score or matching identifier
  - Neighboring-city membership and focal pilot/control city
  - Calendar quarter and year
  - Industry and occupation or routine-status code for job postings
  - Job-posting identifier or city-industry-quarter aggregation key
  - City-level housing-price index and firm identifier where mechanisms are studied
  spillovers: >
    The paper explicitly studies the five closest non-pilot, non-control cities. Pilot
    cities can attract firms and workers from those neighbors, reduce short-run job
    openings and wages there, and later generate positive diffusion. Cities shared by
    pilot and control neighborhoods are excluded in the paper's spillover sample;
    migration restrictions, land supply, other industrial programs, and overlapping
    city clusters can still transmit exposure beyond the recorded neighbor set.
research_compatibility:
  outcome_domains:
  - online job openings and labor demand
  - offered monthly wages
  - routine versus non-routine occupational inequality
  - city housing prices and living costs
  - firm entry, employment, and hiring
  - migration and population changes
  - industrial upgrading and technology adoption
  - regional inequality and spatial spillovers
  affected_populations:
  - Workers and job seekers in pilot and neighboring cities
  - Firms in the ten MIC25 priority areas and related local industries
  - Households facing changes in wages, migration opportunities, and housing costs
  - Non-pilot cities used as matched controls or neighboring comparisons
  mechanism_channels:
  - fiscal subsidies, low-interest finance, and tax support
  - land allocation, regulatory assistance, and intellectual-property protection
  - attraction and entry of high-tech firms
  - demand for non-routine versus routine labor
  - worker and firm relocation across city boundaries
  - housing-supply constraints and local housing-cost capitalization
  best_for:
  - Staggered city-level evaluation of place-based industrial policy
  - Labor-demand and wage effects by industry or occupation
  - Housing-cost responses to high-tech-cluster development
  - Spatial displacement and later spillovers into nearby cities
  - Studies that can reproduce the cohort table and matched-city construction
  not_good_for:
  - Treating MIC25 as one nationwide single-date treatment
  - Treating pilot selection as random or the matched city as automatically valid
  - Inferring a uniform subsidy, firm take-up, or actual robot adoption from status alone
  - Combining the initial pilots with the 2018 National Demonstration Zone upgrade
  - Designs that cannot separate neighboring spillovers from untreated exposure
design:
  claim_type: causal
  affordances:
  - Thirty city cohorts with blueprint dates from 2016Q2 through 2017Q4
  - Pre-policy city characteristics for transparent propensity matching
  - Quarterly job-posting data with industry, occupation, wage, and employer detail
  - Separate pilot, matched-control, and five-nearest-neighbor comparisons
  - City-level housing and firm-registration mechanisms
  candidate_designs:
  - Propensity-matched staggered difference-in-differences or event study
  - Callaway-Sant'Anna group-time ATT by pilot cohort
  - City-industry-quarter labor-demand design with industry-time and industry-city fixed effects
  - Pilot-versus-neighbor spillover design using five nearest eligible cities
  - City-level housing-price event study and firm-entry mechanism analysis
  identifying_variation: >
    The paper compares outcomes in cities whose MIC25 blueprints begin in different
    quarters with outcomes in propensity-similar non-pilot cities, using the cohort
    timing as the exposure clock. The identifying comparison is conditional on the
    matching variables, city and time structure, and the assumption that unobserved
    outcome trends do not jointly determine selection and post-selection changes.
    Neighbor estimates use the analogous five-nearest-city contrast and should be
    interpreted as spatial spillover effects, not as a clean untreated group.
  primary_strategy: >
    Estimate cohort-specific and average treatment effects following the paper's
    Callaway-Sant'Anna implementation. Job-opening and wage specifications use
    industry-by-time and industry-by-city fixed effects and weight city-industry cells
    by 2015 postings; the housing specification uses city and time fixed effects and
    weights by 2015 GRDP. The paper reports both fourteen post-quarter and first-four-
    quarter windows.
  estimand: >
    The conditional average effect of beginning a MIC25 high-tech-cluster blueprint
    in a selected city on job openings, offered wages, housing prices, and related
    mechanisms, relative to the matched non-pilot city under the stated selection,
    timing, and spillover assumptions.
  treatment_variable: >
    A city-quarter indicator equal to one from the city's blueprint publication
    quarter, together with cohort-specific event-time indicators. For labor outcomes,
    interact or stratify this exposure by industry and routine status; for spatial
    analyses, retain a separate neighbor-of-pilot or neighbor-of-control indicator.
  comparison_logic: >
    Compare each pilot city with its propensity-similar non-pilot counterpart before
    and after its cohort quarter, while estimating the five-nearest-neighbor sample
    against the corresponding neighbors of matched controls. The paper's controls
    are conditional comparisons; broad non-pilot cities can differ in size, prosperity,
    industrial base, and other policies.
  estimation_notes: >
    The paper reports approximately 30% more job openings and 4% higher offered wages
    in pilot cities over fourteen post quarters, an 11.5% housing-price increase in
    the same window, and short-run adverse neighbor effects that later attenuate or
    turn positive. These are reported estimates, not a guarantee for every outcome or
    city. Reproduction must use the paper's cohort date (city blueprint publication),
    matching variables, weights, fixed effects, and alternative first-year window.
  assumptions:
  - Matching on observed 2015 levels and 2010-2015 growth rates captures the main selection differences relevant to post-period trends.
  - Pilot and matched cities would have followed comparable outcome trends absent the blueprint.
  - Blueprint publication quarters and city identifiers are measured consistently.
  - Local MIC25 packages and targeted industries do not vary so much that one binary treatment hides unrelated regimes.
  - Neighboring cities are not simultaneously exposed to another policy that explains the same outcome movement.
  - Online job postings and Anjuke price indices measure the intended labor and housing margins without differential platform changes.
  diagnostics:
  - Reproduce propensity-score overlap, covariate balance, and growth-rate balance before matching.
  - Plot event-study leads for pilot and matched cities and test alternative pre-period windows.
  - Reconstruct all 30 blueprint dates from official notices and retain approval versus blueprint dates separately.
  - Exclude or separately code cities adjacent to both pilot and control cities and test alternative neighbor counts.
  - Test robustness to cohort-heterogeneous DID estimators, weighting, industry groups, and the four-quarter window.
  - Audit concurrent industrial, high-tech-zone, smart-city, environmental, and National Demonstration Zone policies.
  - Check whether firm entry, migration, and housing supply move in the timing required by the proposed mechanisms.
threats:
- type: endogenous-pilot-selection
  basis: documented
  condition: The central government did not disclose the complete selection process or rejected applicant list; pilot cities were selected after local applications and had stronger industrial foundations on some baseline measures.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Reproduce the paper's propensity model and common-support restriction
  - Report balance in levels and pre-policy growth rates
  - Use alternative matching specifications and plausible rejected-city samples
- type: blueprint-versus-approval-timing
  basis: documented
  condition: The paper dates treatment by a city blueprint publication, which can occur months after central approval and may follow local preparation or anticipation.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Keep approval, blueprint, and first local implementation dates as separate variables
  - Test leads and alternative treatment clocks
- type: local-policy-heterogeneity
  basis: documented
  condition: Pilot cities selected advantageous industries and used different fiscal, land, talent, and regulatory packages; a binary pilot indicator may pool materially different interventions.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Code city-specific industries and policy components
  - Estimate cohort and industry heterogeneity
  - Exclude cities with no recoverable local blueprint detail
- type: spatial-spillover-and-contamination
  basis: documented
  condition: Firms and workers can move from adjacent cities, while cities can be adjacent to both pilot and control cities or share wider urban clusters.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Reproduce the five-nearest-neighbor construction and dual-adjacency exclusion
  - Estimate spillovers and direct effects jointly
  - Test alternative distance and administrative-neighbor definitions
- type: concurrent-industrial-policy
  basis: inferred
  condition: High-tech zones, industrial parks, smart-city programs, local subsidies, and the 2018 National Demonstration Zone upgrade may overlap the pilot rollout.
  evidence_refs:
  - E1
  - E3
  possible_diagnostics:
  - Build a city-year policy overlap inventory
  - Separate the initial pilot from later demonstration-zone exposure
  - Use placebo policies and leave-one-cohort-out estimates
- type: platform-and-price-measurement
  basis: documented
  condition: MetroData aggregates six job platforms and Anjuke constructs city-level price indices; changes in coverage, duplicate removal, listings, or composition can mimic treatment effects.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Audit platform coverage and duplicate rules over time
  - Compare alternative labor or housing sources where available
  - Report composition and weighting sensitivity
- type: migration-and-housing-equilibrium
  basis: inferred
  condition: Hukou restrictions, inelastic land supply, firm entry, and worker relocation can change both treated and neighboring outcomes, so local estimates need not equal a national welfare effect.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Track firm registration, migrant survey, population, and housing-supply mechanisms
  - Estimate direct and neighboring effects together
  - Avoid interpreting a local price increase as a welfare gain without accounting for wages and displacement
empirical_requirements:
  contract_version: 1
  population: Workers, job seekers, firms, and households in Chinese cities observed around the 2016-2017 MIC25 pilot rollout
  observation_unit: City-quarter, city-industry-quarter, city-year, or firm-year linked to the MIC25 city cohort
  geography_level: Prefecture-level or province-level city, with separate neighboring-city links
  time_start: 2015
  time_end: 2020
  minimum_frequency: quarterly
  minimum_pre_periods: 4
  minimum_post_periods: 4
  required_fields:
  - outcome and outcome definition
  - stable city code and province code
  - calendar quarter and year
  - MIC25 cohort and blueprint publication quarter
  - matched-control identifier and propensity score
  - neighboring-city membership and focal city
  - industry and occupation or routine-status code for labor outcomes
  - job-opening count and offered wage, or a documented city housing-price index
  - firm identifier and registration year for firm mechanisms
  required_identifiers:
  - city code
  - province code
  - MIC25 cohort quarter
  - matched city code
  - focal pilot/control city code for neighbor links
  - industry and occupation code
  - calendar quarter
  treatment_key:
  - city code
  - calendar quarter
  - MIC25 cohort quarter
  treatment_source: Paper Table 1 plus city blueprint and MIIT/State Council implementation notices; do not substitute a generic MIC25 keyword or the later 2018 upgrade
  measurement_risks:
  - central approval date versus city blueprint date
  - incomplete or inconsistent city-code and boundary crosswalks
  - nonrandom pilot selection and imperfect propensity matching
  - local policy-package and industry heterogeneity
  - contamination from adjacent cities and overlapping policies
  - job-platform coverage, duplicate removal, and occupation classification
  - city-level housing index composition and listing or transaction coverage
design_profiles:
- id: labor-demand
  label: City-industry-quarter labor-demand and wage design
  design_families:
  - staggered difference-in-differences
  - event study
  when_to_use: Use when job-posting records contain city, industry, occupation, quarter, offered wage, and a stable employer or posting key.
  outcome_domains:
  - job openings
  - offered wages
  - routine versus non-routine labor demand
  requirements:
    population: Workers and employers represented in Chinese online job postings
    observation_unit: City-industry-quarter or posting-level record aggregated to city-industry-quarter
    geography_level: Prefecture-level or province-level city
    time_start: 2015
    time_end: 2020
    minimum_frequency: quarterly
    minimum_pre_periods: 4
    minimum_post_periods: 4
    required_fields:
    - job-opening count
    - offered wage
    - city code
    - industry and occupation code
    - calendar quarter
    - MIC25 cohort quarter
    required_identifiers:
    - city code
    - industry code
    - occupation or routine-status code
    - calendar quarter
    - posting or employer identifier
    treatment_key:
    - city code
    - calendar quarter
- id: housing-cost
  label: City-quarter housing-cost response
  design_families:
  - city-level event study
  - staggered difference-in-differences
  when_to_use: Use when a city-level transaction or price index can be linked to the MIC25 cohort and the researcher can separate housing costs from wage and migration mechanisms.
  outcome_domains:
  - housing prices
  - living costs
  - housing-supply capitalization
  requirements:
    population: Households and workers in Chinese pilot, matched, and neighboring cities
    observation_unit: City-quarter
    geography_level: Prefecture-level or province-level city
    time_start: 2015
    time_end: 2020
    minimum_frequency: quarterly
    minimum_pre_periods: 4
    minimum_post_periods: 4
    required_fields:
    - city housing-price or transaction index
    - city code
    - calendar quarter
    - MIC25 cohort quarter
    required_identifiers:
    - city code
    - calendar quarter
    treatment_key:
    - city code
    - calendar quarter
evidence:
- id: E1
  source_type: policy-document
  citation: 'State Council. 2015-05-08. 《中国制造2025》, Guofa [2015] No. 28.'
  url: https://www.ndrc.gov.cn/xxgk/zcfb/qt/201505/t20150520_967388.html
  date: '2015-05-08'
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  verification_status: verified
  access_level: official-document
  locator: 'The official notice identifies Made in China 2025 as the national manufacturing-upgrading action plan and sets the strategic goals and priority technology/manufacturing directions; it does not establish the later city cohort dates.'
- id: E2
  source_type: implementation-document
  citation: 'Xinhua / State Council Information Office. 2016-08-18. MIIT approved Ningbo as the first Made in China 2025 pilot demonstration city.'
  url: https://www.gov.cn/xinwen/2016-08/18/content_5100482.htm
  date: '2016-08-18'
  supports:
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - assignment.rule
  - assignment.treated
  - timeline.announcement
  verification_status: verified
  access_level: official-document
  locator: 'The official report records the formal launch of the city-pilot work and Ningbo as the first approved pilot, while describing city-specific development and support rather than a uniform nationwide package.'
- id: E3
  source_type: paper
  citation: 'Mane, Klint, Geunyong Park, and Ande Shen. 2025. “High-tech clusters, labor demand, and inequality: Evidence from Made in China 2025.” Regional Science and Urban Economics 115:104142. DOI: 10.1016/j.regsciurbeco.2025.104142.'
  url: https://geunyongpark.com/files/mic25.pdf
  date: 2025
  supports:
  - identity.instrument
  - identity.implementation_regime
  - identity.assignment_mechanism
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
  verification_status: verified
  access_level: full-text
  locator: 'Author-hosted full-text PDF: policy background and Table 1 (pilot cohorts and blueprint starting quarters); Sections 3-4 (MetroData job postings, city yearbooks, Anjuke housing index, firm registration, migration survey, propensity matching and event-study design); Section 5 (pilot, neighbor, housing, and mechanism results).'
- id: E4
  source_type: paper
  citation: 'IDEAS/RePEc bibliographic record for Mane, Park, and Shen, Regional Science and Urban Economics 115 (2025), article 104142.'
  url: https://ideas.repec.org/a/eee/regeco/v115y2025ics0166046225000596.html
  date: 2025
  supports:
  - identity.instrument
  - design.primary_strategy
  - design.estimand
  verification_status: verified
  access_level: metadata
  locator: 'The record confirms the journal article identity, DOI, publication year, and JEL coverage; substantive cohort and design claims are taken from E3, not from metadata alone.'
- id: E5
  source_type: paper
  citation: 'Publisher DOI record for Mane, Park, and Shen, “High-tech clusters, labor demand, and inequality: Evidence from Made in China 2025.”'
  url: https://doi.org/10.1016/j.regsciurbeco.2025.104142
  date: 2025
  supports:
  - identity.instrument
  - design.primary_strategy
  - design.estimand
  verification_status: verified
  access_level: metadata
  locator: 'The DOI record establishes the publication identity and article DOI; the paper-specific cohort, data, and estimates are established by E3.'
design_applications:
- paper: 'High-tech clusters, labor demand, and inequality: Evidence from Made in China 2025'
  doi: 10.1016/j.regsciurbeco.2025.104142
  journal: Regional Science and Urban Economics
  year: 2025
  research_question: How did the staggered construction of MIC25 high-tech clusters change labor demand, offered wages, housing costs, and inequality across pilot and neighboring Chinese cities?
  population: Workers, job seekers, firms, migrants, and households in 30 MIC25 pilot cities, matched non-pilot cities, and their neighboring cities.
  outcome: Quarterly online job openings and offered wages by city-industry and occupation; city-level housing prices; firm entry and hiring; population and migrant mechanisms.
  data_used:
  - MetroData postings from six Chinese job-search platforms, 2015-2020
  - City-level statistical yearbooks
  - Anjuke monthly city housing-price index aggregated to quarters
  - China Administrative Registration Database firm records
  - China Migrants Dynamic Survey for a welfare mechanism check
  treatment_encoding: City equals one from the quarter in which its MIC25 development blueprint was published; cohorts are Ningbo in 2016Q2, eight cities in 2017Q1, fifteen in 2017Q2, three in 2017Q3, and three in 2017Q4.
  comparison: Propensity-score-matched non-pilot cities using 2015 levels and 2010-2015 growth rates; spillover estimates compare five nearest eligible neighbors of pilot cities with five nearest neighbors of matched controls.
  empirical_design: Cohort-heterogeneous event-study and Callaway-Sant'Anna ATT estimates with city/time or industry-city and industry-time fixed effects, the paper's weights, and separate fourteen-quarter and four-quarter post windows.
  assumptions:
  - Selection on observed pre-policy city characteristics is sufficient for the matched comparison.
  - Pilot and matched cities have comparable counterfactual trends after matching.
  - Blueprint quarters are measured consistently and do not simply proxy for earlier local implementation.
  - Neighbor and control samples are not differentially contaminated by overlapping policies.
  - The job and housing data measure the intended margins over the study window.
  threats_addressed:
  - Pre-policy balance and event-study leads
  - Propensity-score matching and alternative outcome windows
  - Five-nearest-neighbor spillover construction and dual-adjacency exclusion
  - Industry and occupation heterogeneity
  - Firm-entry, migration, and housing-cost mechanism checks
  evidence_refs:
  - E3
  - E4
  - E5
method_transfer: null
readiness_blockers: []
---

## Institutional Background

Made in China 2025 was a national manufacturing-upgrading plan, but this record is
not a national post-2015 dummy. It follows the later city-pilot layer: central
approval created a pilot designation and each selected city prepared a blueprint
for a locally emphasized set of high-tech industries. The official plan establishes
the national policy and its direction; it does not by itself establish the later
city list, local take-up, or a common subsidy amount [E1].

## What Changed

The empirical object is the staggered start of the 30 pilot-city blueprints. The
paper's Table 1 reports one Ningbo cohort in 2016Q2 and four cohorts in 2017. An
official notice places Ningbo's first approval on 2016-08-18. That apparent mismatch
is retained rather than smoothed away: the paper cohort quarter and the official
approval date are different source fields until the underlying local plan is
checked [E2; E3]. The 2018 National Demonstration Zone upgrade is a later regime and
must not be folded into the initial-pilot treatment.

## Implementation and Assignment

For a replication, join the paper's cohort table to stable city identifiers and
expand the paper's coded quarter forward. Keep the central approval, city blueprint
publication, selected industry, matched-control status, and neighboring status in
separate columns. The paper's comparison uses propensity scores based on 2015 city
levels and 2010-2015 growth rates, then removes cities adjacent to pilot cities from
the broader control pool and constructs five-nearest-city spillover samples [E3].

The selection process is not documented as a public threshold or random draw. Local
applications and central selection reflect industrial and regional characteristics,
and the rejected-applicant list was not available in the inspected paper. Matching is
therefore a transparent comparison device, not proof that the assignment is
exogenous [E1; E3].

## Why This Creates Empirical Variation

The dated city exposure can be connected to quarterly job postings and wages,
city-level housing prices, firm registrations, and migrant outcomes. It supports a
conditional staggered-treatment question: what changed after a selected city's
blueprint began, relative to its matched non-pilot counterpart, under the paper's
trend and spillover assumptions? The nearby-city estimates answer a different
question about displacement or diffusion; they are not a clean untreated group.

The paper reports approximately 30 percent more job openings and 4 percent higher
offered wages in pilot cities over fourteen post-quarters, alongside an 11.5 percent
housing-price increase and short-run negative neighbor effects. These are reported
applications, not universal effects of every local MIC25 measure [E3].

## Identification Risks

The national plan, local applications, preparation of blueprints, and later
demonstration-zone support can create anticipation before the coded quarter. Pilot
cities can differ in unobserved growth prospects, local industrial policy, and
housing supply; matching and event-study leads reduce but do not eliminate those
concerns. The five-nearest-neighbor construction also leaves room for migration,
firm relocation, and overlapping policies to transmit treatment beyond the recorded
boundary [E3].

The Ningbo quarter/date discrepancy is a measurement risk, not a reason to choose
whichever clock gives a preferred estimate. A careful design should reproduce the
paper's coding, test the official approval and local-plan clocks separately, and
state which estimand each supports.

## Data Requirements

The minimum data contract is a city-quarter panel with stable prefecture or
municipality codes, the 30-city cohort table, matched-control and neighbor
identifiers, industry and occupation codes, and outcome-specific joins. The paper
uses MetroData job postings from six platforms (2015-2020, analyzed quarterly over
the shorter pre/post window), Anjuke monthly housing indices, city yearbooks, firm
registration records, and the China Migrants Dynamic Survey [E3]. A reproduction
must preserve source dates, platform coverage, city-boundary changes, and the
distinction between blueprint publication and central approval.

## Evidence Notes

E1 is the official national plan. It establishes the policy's national purpose and
priority directions, but not the later city cohort or actual implementation. E2 is
the official report of Ningbo's first approval on 2016-08-18 and the city-specific
pilot framework; it does not establish the complete 30-city table. E3 is the
author-hosted full-text paper used for Table 1, data construction, matching,
neighbor definition, estimators, and reported results; its cohort quarter is a
paper-reported coding choice and should not be mistaken for an independently
verified legal effective date. E4 and E5 establish article metadata and the DOI;
they are not substitutes for the paper's full-text evidence. No source inspected
here proves random selection, universal firm take-up, or absence of anticipation.

The record is therefore grounded as a Chinese place-based pilot assignment with an
explicit paper application and a preserved timing conflict. It is useful for
conditional regional, urban, labor, housing, and spatial-spillover designs, but
should not be presented as a nationally uniform or intrinsically exogenous shock.
