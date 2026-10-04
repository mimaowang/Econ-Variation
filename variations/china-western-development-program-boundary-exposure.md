---
schema_version: 2
id: china-western-development-program-boundary-exposure
name: China Great Western Development Program Eligibility Boundary Exposure
aliases:
- Western Development Program
- Great Western Development Program
- 西部大开发
- 国发〔2000〕33号
status: grounded
provenance:
  task_id: task-e6f648e1ff1b
scope:
  country: China
  regions:
  - Chongqing
  - Sichuan
  - Guizhou
  - Yunnan
  - Tibet
  - Shaanxi
  - Gansu
  - Ningxia
  - Qinghai
  - Xinjiang
  - Inner Mongolia
  - Guangxi
  domains:
  - regional-economics
  - development
  - place-based-policy
  - infrastructure
  - public-finance
  - urban-rural
  variation_type: boundary-discontinuity
  knowledge_role: china-variation
  china_relevance: The State Council's Western Development policy package assigned special fiscal, investment, infrastructure, and tax support to a defined set of western Chinese provincial jurisdictions. The usable exposure is a locality's program eligibility, particularly near the policy boundary, rather than a generic west-versus-east comparison.
identity:
  instrument: Eligibility for the Great Western Development Program's special policy package, determined by inclusion in the State Council-defined western-region jurisdiction set and implemented through fiscal transfers, investment, infrastructure priorities, and sector-qualified tax policies.
  authority: State Council of the People's Republic of China; State Council Western Region Development Leading Group Office; National Development and Reform Commission and participating ministries.
  legal_identifiers:
  - 国务院关于实施西部大开发若干政策措施的通知（国发〔2000〕33号，2000年12月26日）
  - 国务院办公厅转发国务院西部开发办关于西部大开发若干政策措施实施意见的通知（国办发〔2001〕73号，2001年9月29日）
  implementation_regime: The 2000-2001 policy package applied to Chongqing, Sichuan, Guizhou, Yunnan, Tibet, Shaanxi, Gansu, Ningxia, Qinghai, Xinjiang, Inner Mongolia, and Guangxi. It combined central construction funding, infrastructure and industrial priorities, transfer payments, and qualified tax concessions; it was not one identical project delivered to every eligible locality. The 2001 implementation opinion states that the listed twelve jurisdictions are the policy scope and that three eastern ethnic autonomous prefectures receive analogous consideration.
  assignment_mechanism: Administrative geographic eligibility. A township or county inherits program exposure from its location inside a listed western provincial-level jurisdiction. The Regional Studies application compares localities just inside and outside the resulting policy boundary; it does not claim that individual projects, transfers, or firms were randomly assigned.
  parent: null
  related_variations:
  - china-industrial-transfer-policy-inland-city-status
timeline:
  announcement: '2000-01'
  effective: '2001-01-01'
  implementation_start: 2000
  implementation_end: 2010
  local_timing: The paper codes the program as beginning in 2000 and estimates post-2000 border effects. The formal State Council policy notice is dated 2000-12-26, while its stated policy window is 2001-2010 and the detailed implementation opinion was issued in September 2001. A replication should therefore report sensitivity to alternative start dates rather than silently treating all components as effective on one day.
  anticipation: National planning and the leadership group preceded the detailed policy notice. Border localities, firms, and governments may have anticipated projects and incentives before the formal 2001 implementation opinion.
  last_verified: '2026-09-28'
assignment:
  unit: Township-year for the spatial-regression-discontinuity application; county-year or county-industry-year where a later application can reconstruct a compatible boundary exposure.
  treated: Localities located inside the twelve-jurisdiction western policy scope, especially townships within an audited bandwidth of the western eligibility boundary after the program start.
  comparison_pool: Localities on the non-western side of the same policy boundary within a pre-specified geographic bandwidth. Comparisons farther from the boundary are descriptive unless a separate design justifies them.
  rule: Overlay stable township or county centroids and boundaries on the official western-policy jurisdiction boundary. Code eligibility from the listed jurisdictions, preserve the three separately mentioned eastern ethnic autonomous prefectures, and define signed distance to the boundary before selecting an RD bandwidth.
  intensity: Baseline treatment is binary eligibility interacted with post-program time. Intensity may additionally be measured with observed transfers, qualifying-sector tax treatment, or infrastructure investment, but those measures are policy components or mediators and should not be substituted for geographic assignment without a design-specific argument.
  exemptions:
  - Yanbian Korean Autonomous Prefecture
  - Enshi Tujia and Miao Autonomous Prefecture
  - Xiangxi Tujia and Miao Autonomous Prefecture
  compliance: Geographic eligibility does not guarantee equal receipt of transfers, projects, tax concessions, or firm participation. The paper reports heterogeneous effects by baseline local endowments despite broadly similar aggregate fiscal and credit support.
  exposure_construction: Construct an audited township/county boundary crosswalk; assign western eligibility from the twelve-jurisdiction rule; calculate signed distance to the nearest policy boundary; restrict to a declared bandwidth; interact eligibility with post-period or year indicators. Keep distance, eligibility, and realized transfers/infrastructure separate variables.
  required_identifiers:
  - stable township or county identifier
  - township/county centroid or polygon
  - province-level policy eligibility
  - year
  - signed distance to policy boundary
  spillovers: Infrastructure, migration, fiscal redistribution, and firm relocation can cross the boundary. The paper reports tests for nearby control-side effects but explicitly cannot rule out spillovers that are not distance-dependent.
research_compatibility:
  outcome_domains:
  - regional-output
  - nighttime-lights
  - local-public-finance
  - firm-entry
  - population-density
  - inequality
  - infrastructure
  affected_populations:
  - townships and counties near the western policy boundary
  - firms and workers in eligible western jurisdictions
  - local governments receiving program resources
  mechanism_channels:
  - fiscal transfers
  - credit support
  - infrastructure investment
  - sector-qualified tax concessions
  - migration and agglomeration
  best_for:
  - Spatial RD studies of a broad place-based policy at the western eligibility boundary
  - Event-time studies that distinguish policy eligibility from realized support intensity
  - Research on heterogeneous regional effects of fiscal and infrastructure support
  not_good_for:
  - A generic west-versus-east comparison without a boundary restriction
  - Attribution to one component such as a railway or tax concession without component-level data
  - Claims that program eligibility randomized local development potential
design:
  claim_type: causal
  affordances:
  - A published, explicit administrative eligibility scope
  - A long north-south policy boundary crossing multiple provinces
  - Township-level nighttime-light panel and county socioeconomic data in the documented application
  - Pre-program years for border event-time diagnostics
  candidate_designs:
  - Spatial regression discontinuity at the western eligibility boundary
  - Boundary difference-in-differences with township and year fixed effects
  - Heterogeneity analysis by pre-program population density, industrialization, and rail access
  identifying_variation: Geographic discontinuity in eligibility for the western policy package at an administrative boundary, compared locally before and after program implementation.
  primary_strategy: Zhu, Wang, and Lin report spatial RD with geographic controls and a border-by-year event-time specification using townships near the policy boundary.
  estimand: A local average difference in post-program outcomes for localities immediately inside versus outside the policy boundary, conditional on continuity and absence of discontinuous confounders at that boundary.
  treatment_variable: Western-eligibility indicator interacted with post-program or individual year indicators; signed distance to the boundary enters the reported spatial RD specifications.
  comparison_logic: Compare immediately adjacent eligible and noneligible localities within a declared bandwidth, verify smoothness of observed geographic and socioeconomic characteristics, and inspect pre-2000 border-year coefficients.
  estimation_notes: The reported application uses annual DMSP nighttime lights for 1992-2012, VIIRS lights for 2012-2019, geographic controls, alternative bandwidths, and county-level data for outcomes and mechanisms. The paper's post-2000 coding should be checked against legal-policy effective-date alternatives.
  assumptions:
  - Potential outcomes and predetermined covariates vary smoothly at the policy boundary absent eligibility.
  - Boundary-side differences after the program are not driven by other policies discontinuously assigned at the same border.
  - Township geometry, boundary assignment, and distance calculations are accurate.
  - Cross-boundary spillovers do not invalidate the local comparison or are explicitly modeled.
  - The chosen program-start convention does not generate spurious pre-trends.
  diagnostics:
  - Covariate and geographic balance at the boundary
  - Pre-2000 border-by-year coefficients and placebo start years
  - Multiple bandwidths and spatial-control specifications
  - Alternative treatment start dates reflecting 2000 launch and 2001 policy implementation
  - Tests for distance-dependent control-side spillovers
  - Separate realized transfers, infrastructure, and tax-policy channels from eligibility
threats:
- type: boundary-noncomparability
  basis: reported
  condition: The administrative boundary can coincide with unobserved geography, provincial institutions, ethnic composition, or prior development programs that change discontinuously at the same location.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Covariate continuity and geographic balance tests
  - Narrower bandwidths and province-segment fixed effects
  - Placebo boundaries and pre-program outcomes
- type: bundled-policy-treatment
  basis: documented
  condition: Eligibility bundles transfers, infrastructure, industrial priorities, and tax incentives, so a boundary effect does not identify a single policy component.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Measure components separately where administrative data permit
  - Avoid labeling the estimand as a pure infrastructure or tax effect
- type: start-date-and-anticipation
  basis: reported
  condition: The paper's 2000 treatment coding precedes the formal 2000-12 notice and 2001 implementation detail; planning and early projects may also precede either date.
  evidence_refs:
  - E1
  - E3
  possible_diagnostics:
  - Event-time plots and alternative post definitions
  - Document project-specific announcement and completion dates
- type: cross-boundary-spillovers
  basis: reported
  condition: Migration, market access, and fiscal redistribution may affect noneligible neighbors beyond a simple distance-decay pattern.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Distance-band and network spillover tests
  - Exclude or separately model boundary segments with major transport links
- type: measurement-and-boundary-error
  basis: reported
  condition: Historical township boundaries, centroid assignments, night-light harmonization, and the treatment of the three analogous eastern ethnic prefectures can materially alter local RD classification.
  evidence_refs:
  - E2
  - E3
  possible_diagnostics:
  - Archive boundary shapefiles and crosswalk versions
  - Recompute distances from polygons and centroids
  - Report results with and without analogous prefectures
empirical_requirements:
  contract_version: 1
  population: Townships or counties near the formal western-policy boundary, observed before and after program implementation.
  observation_unit: Township-year for light-based outcomes; county-year for socioeconomic outcomes.
  geography_level: Township and county, linked to stable provincial eligibility and an audited boundary geometry.
  time_start: 1992
  time_end: 2019
  minimum_frequency: annual
  minimum_pre_periods: 5
  minimum_post_periods: 5
  required_fields:
  - township or county identifier
  - year
  - longitude and latitude or polygon geometry
  - western-policy eligibility
  - signed distance to eligibility boundary
  - nighttime-light outcome or socioeconomic outcome
  - pre-program population density, industrialization, and infrastructure measures
  - program-component measures when attributing mechanisms
  required_identifiers:
  - stable_township_or_county_id
  - province_id
  - year
  - boundary_version
  treatment_key:
  - stable_township_or_county_id
  - western_eligibility
  - signed_distance_to_boundary
  - year
  treatment_source: State Council policy-scope documents plus a reproducible GIS boundary derived from the twelve named provincial jurisdictions and documented treatment of analogous ethnic prefectures.
  measurement_risks:
  - township boundary changes and centroid misclassification
  - DMSP/VIIRS light-series harmonization
  - incomplete measurement of transfers and infrastructure components
  - ambiguity between 2000 launch and 2001 formal policy-window timing
  - policy-boundary segments that coincide with other provincial discontinuities
evidence:
- id: E1
  source_type: policy-document
  citation: 国务院. 2000. 《国务院关于实施西部大开发若干政策措施的通知》（国发〔2000〕33号，2000年12月26日）.
  url: https://www.moe.gov.cn/jyb_xxgk/gk_gbgg/moe_0/moe_7/moe_445/tnull_5921.html
  date: '2000-12-26'
  supports:
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.effective
  - timeline.implementation_end
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: Ministry of Education government-portal reproduction of Guofa [2000] No. 33; notice text identifies the western-development policy package and states that the measures mainly apply during 2001-2010.
- id: E2
  source_type: implementation-document
  citation: 国务院办公厅. 2001. 《国务院办公厅转发国务院西部开发办关于西部大开发若干政策措施实施意见的通知》（国办发〔2001〕73号）.
  url: https://www.ndrc.gov.cn/xxgk/zcfb/qt/200507/t20050709_967918.html
  date: '2001-09-29'
  supports:
  - identity.authority
  - identity.implementation_regime
  - timeline.implementation_start
  - assignment.rule
  - assignment.exemptions
  - assignment.intensity
  verification_status: verified
  access_level: official-document
  locator: 'NDRC official page, sections I-II and VII: the twelve-jurisdiction scope, three analogous eastern ethnic prefectures, construction and transfer support, and qualified tax policies.'
- id: E3
  source_type: paper
  citation: 'Zhu, Pengyu, Yulin Wang, and Yatang Lin. 2025. "Unravelling regional inequality: the heterogeneous impact of China''s Great Western Development Program." Regional Studies 59(1): 2438319. DOI: 10.1080/00343404.2024.2438319.'
  url: https://doi.org/10.1080/00343404.2024.2438319
  date: 2025
  supports:
  - scope.china_relevance
  - identity.instrument
  - timeline.local_timing
  - timeline.anticipation
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.exposure_construction
  - assignment.spillovers
  - design.primary_strategy
  - design.identifying_variation
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - design.assumptions
  - design.diagnostics
  - threats.condition
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.geography_level
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_key
  - empirical_requirements.measurement_risks
  - design_applications.paper
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
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
  locator: 'Inspected author manuscript (https://pengyuzhu.com/wp-content/uploads/2025/07/manuscript_for_regional_study_sep27_ver2-zhu_lin-changes-accepted.pdf), pp. 1-16 and appendix: policy-boundary RD, 1992-2019 lights, township/county data, geographic controls, pre-trend and bandwidth checks, heterogeneity, and stated spillover limits.'
design_applications:
- paper: 'Unravelling regional inequality: the heterogeneous impact of China''s Great Western Development Program'
  doi: 10.1080/00343404.2024.2438319
  journal: Regional Studies
  year: 2025
  research_question: Does eligibility for China's Great Western Development Program change local output growth and inequality, and are effects heterogeneous by pre-program local endowments?
  population: Townships near the western eligibility boundary and counties supplying socioeconomic outcomes.
  outcome: Township night-light intensity; county GDP and industrial indicators; population density, firm entry, public-service, and welfare measures.
  data_used:
  - DMSP annual nighttime lights, 1992-2012
  - VIIRS nighttime lights, 2012-2019
  - China County Statistical Yearbook, 1999-2018
  - China Population Census, 2000 and 2010
  - WorldPop township population density
  - SRTM elevation and slope, plus railway and road GIS data
  treatment_encoding: Western-side eligibility indicator interacted with post-2000 or year indicators, with signed distance to the policy boundary in spatial RD specifications.
  comparison: Townships immediately outside the western-program boundary within specified bandwidths; annual border contrasts before and after 2000.
  empirical_design: Spatial regression discontinuity with geographic controls, bandwidth robustness, and border-by-year difference-in-differences/event-time estimates.
  assumptions:
  - Localities immediately on either side of the boundary are comparable conditional on distance and geographic controls.
  - Other discontinuities at the boundary do not explain post-program changes.
  - Night-light and administrative data are consistently linked across time and boundaries.
  threats_addressed:
  - Covariate balance and pre-program event-time checks
  - Alternative bandwidths and spatial controls
  - Heterogeneity by baseline endowments
  - Distance-dependent spillover checks, with remaining non-distance spillovers acknowledged
  evidence_refs:
  - E3
method_transfer: null
readiness_blockers:
- The canonical policy boundary must be implemented from an archived GIS version and stable township/county crosswalk; this record does not distribute a shapefile.
- The author manuscript documents the application but no inspected replication package was found; exact code, bandwidth choices, and light-series harmonization should be reproduced before treating estimates as final.
- The policy is a bundle; component-specific causal claims require separate administrative measures rather than eligibility alone.
---
---
## Institutional Background

The Great Western Development Program was a central place-based policy directed at a defined western set of provincial jurisdictions. The formal 2000 policy notice set out a package rather than one intervention. The 2001 implementation opinion identifies the twelve covered jurisdictions and describes construction funding, infrastructure priorities, transfer payments, and qualified tax policies [E1; E2].

## What Changed

The research-relevant change is eligibility for this policy package. The program was launched politically in 2000, while the detailed policy notice dates from December 2000 and identifies 2001-2010 as the main policy window. This difference matters: the paper's post-2000 coding is a reported empirical convention, not proof that every component began simultaneously in January 2000 [E1; E3].

## Implementation and Assignment

Assignment follows geography. A locality inherits eligibility from its location in a listed western jurisdiction, while three eastern ethnic autonomous prefectures receive analogous consideration under the implementation opinion. The reported application constructs a spatial comparison across the western eligibility boundary. It does not treat realized transfers, tax concessions, infrastructure projects, or firm participation as randomly assigned [E2; E3].

## Why This Creates Empirical Variation

Townships near opposite sides of the administrative eligibility boundary can have different policy status after implementation. Zhu, Wang, and Lin use that contrast in a spatial RD and event-time design. Its identifying force depends on local continuity at the boundary and on the absence of other discontinuous border-side changes, rather than on a claim that western places were randomly selected [E3; analytical inference].

## Identification Risks

The program bundles multiple channels, borders can coincide with provincial institutions or geography, and migration or investment can spill across the boundary. Start-date choice, historical boundary crosswalks, and night-light harmonization also matter. The paper reports balance, pre-period, bandwidth, and distance-spillover checks, but notes that it cannot exclude all non-distance-dependent spillovers [E2; E3].

## Data Requirements

A usable replication needs an archived policy-boundary GIS layer, stable township/county identifiers, centroids or polygons, annual outcomes, and pre-program covariates. The documented application links DMSP/VIIRS lights, county statistical-yearbook outcomes, censuses, WorldPop, SRTM, and transport GIS data [E3]. Dataset acquisition and version management belong in `Econ Data Know-How`; this record preserves the treatment and joining contract.

## Evidence Notes

E1 and E2 are official sources for the policy identity, scope, and implementation regime. E3 is an inspected author-produced peer-reviewed manuscript for the 2025 *Regional Studies* paper and supports the reported spatial RD application. It does not independently establish that the boundary is exogenous, that all program components started together, or that its local estimates generalize across the whole West. The blocked JRS local-tax-effort candidate uses the same institutional policy family but a different application; it should be linked to this record only after its closed-access boundary and fiscal-data details are recoverable.
