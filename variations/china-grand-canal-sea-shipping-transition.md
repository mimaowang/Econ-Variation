---
schema_version: 2
id: china-grand-canal-sea-shipping-transition
name: Grand Canal Trade-Access Decline Following the 1826 Sea-Shipping Experiment
aliases: [Rebel on the Canal, Qing tribute-grain sea transportation, 大运河贸易通道衰退, 道光六年漕粮海运]
status: grounded
provenance:
  task_id: task-83135b77fc77
scope:
  country: China
  regions: [Zhili, Shandong, Henan, Anhui, Jiangsu, Zhejiang]
  domains: [regional-economics, urban-economics, development-economics, economic-history, transport-infrastructure, trade-access, social-conflict]
  variation_type: event-shock
  knowledge_role: china-variation
  china_relevance: Chinese historical counties experience different exposure to the decline of a domestic transport corridor; the published application links this exposure to social conflict and local market development.
identity:
  instrument: Tribute-grain sea-shipping experiment and subsequent decline of the Grand Canal trade corridor
  authority: Qing imperial government, with provincial shipping administration and Tianjin unloading authorities
  legal_identifiers: ['清宣宗成皇帝实录, volume 96, 道光六年三月甲申 sea-shipping directive; inspected digital transcription, not an original folio scan']
  implementation_regime: Temporary sea-shipping trial in 1826 followed by canal restoration and a longer transition; not a uniform permanent physical shutdown in 1826
  assignment_mechanism: Pre-existing adjacency to the canal crossed with the common 1826 transition date; adjacency is a researcher-constructed geographic exposure, not a randomly allocated county policy designation
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 1826
  implementation_end: null
  local_timing: The inspected imperial directive confirms sea shipments already being implemented in 1826. The paper dates the triggering breach to 1825, restoration to 1827, cessation of canal tribute-rice shipping after 1855 and formal closure announcement to 1901. Those later dates are paper-reported, not independently inspected decrees here. The regression post period includes 1826 through 1911.
  anticipation: The paper interprets the successful trial as changing expectations before final abandonment. Merchants' expectations and the timing of local trade losses are not directly observed or uniform.
  last_verified: '2026-09-28'
assignment:
  unit: Historical county-year
  treated: Counties bordering or containing the historical canal; the paper reports 73 of 575 geographic-sample counties, not 73 newly designated jurisdictions
  comparison_pool: Other counties in the same six-province inventory; population-normalized baseline regressions retain 536 counties overall
  rule: Spatially join the historical county geography and canal path, then interact the fixed AlongCanal indicator with a year indicator equal to one in and after 1826. Recover the paper's layer version and boundary-contact rule before reproducing county membership.
  intensity: Binary adjacency is the main encoding; canal length per 100 square kilometres, share of market towns within 10 km and distance to the canal are alternative measures of the same corridor exposure
  exemptions:
  - Southern canal sections remained relatively navigable; geographic adjacency does not mean equal realised trade disruption.
  - Counties without the population inputs are omitted from the normalized baseline, not assigned to a different treatment arm.
  compliance: The imperial directive records actual initial shipments and orders prompt Tianjin unloading and vessel return for a second shipment. It supports implemented sea transportation, not complete compliance with an immediate canal closure.
  exposure_construction: Join fixed geographic exposure to annual rebellion onsets by the paper-harmonised county identifier and year. Normalize onsets by imputed 1600 population and apply the inverse hyperbolic sine transformation for the baseline outcome. Keep the northern indicator based on the OLD Yellow River course separate from adjacency.
  required_identifiers: [Paper-harmonised county ID, Year, Historical prefecture ID, Historical province ID, Versioned canal geometry, County geometry, Old Yellow River course for north-south contrasts]
  spillovers: The paper estimates effects extending to about 150 km; baseline non-canal counties are not automatically unexposed. Its supplementary synthetic-control donor pool excludes counties closer than 150 km.
research_compatibility:
  outcome_domains: [Rebellion onsets, Historical market-town development, Trade-related urban livelihoods]
  affected_populations: [Historical counties along and away from the Grand Canal in six eastern Chinese provinces]
  mechanism_channels: [Regional trade-access loss, Shipping and commercial employment, Expectations about future canal use]
  best_for: [Historical local consequences of losing an established transport corridor, Spatial heterogeneity in trade-access disruption]
  not_good_for: [A modern county policy DID without historical crosswalks, An immediate nationwide canal shutdown in 1826, Separately identifying pure expectations from realised trade loss]
design:
  claim_type: reduced-form
  affordances: [Common historical transition date, Predetermined corridor adjacency, Long annual panel, North-south heterogeneity]
  candidate_designs: [County-year difference-in-differences, Decadal event study, Geographic intensity and distance gradients, Supplementary synthetic control]
  identifying_variation: Differential post-1826 outcome changes across counties with different pre-existing canal exposure; historical placement is not random and conditional parallel trends remain an assumption.
  primary_strategy: County and year fixed effects with AlongCanal interacted with Post; richer specifications include pretreatment rebelliousness interacted with years, province-year effects, prefecture trends and controls interacted with Post
  estimand: Relative change associated with the evolving canal-decline episode beginning at the trial date, not an isolated permanent one-year closure effect or a pure sea-shipping effect
  treatment_variable: AlongCanal multiplied by an indicator for year greater than or equal to 1826
  comparison_logic: Changes in canal-adjacent versus other counties in the six-province sample; north-south contrasts compare canal and non-canal counties within each side of the old Yellow River course
  estimation_notes: Baseline outcome is arcsinh of rebellion onsets per million imputed 1600 population. Decadal event-study reference pools years more than 50 years before 1826, not just the immediately preceding decade. County-clustered and supplementary spatial/serial Conley errors are reported; the 150-km synthetic-control restriction is not the baseline DID selection rule.
  assumptions: [Comparable conditional trends absent canal decline, No coincident corridor-specific changes driving the comparison, Faithful historical geocoding and outcome reporting, Spatial interference is accounted for in interpreting the contrast]
  diagnostics: [Pre-1826 trends, Decadal dynamics and restoration period, Alternative outcome normalization, Old-course north-south contrast, Other-route placebos, Opium War and Taiping exposures, Spatial donor restrictions]
threats:
- type: An evolving rather than instantaneous treatment
  basis: documented
  condition: The primary directive confirms a trial, while the paper describes restoration and later abandonment. A single post indicator averages different phases and cannot isolate each later step.
  evidence_refs: [E1, E2]
  possible_diagnostics: [Preserve the chronology, Inspect event-time dynamics, Use justified shorter windows without relabelling dates]
- type: Geographic comparability and concurrent disorder
  basis: reported
  condition: Historical canal counties may respond differently to nineteenth-century shocks; controls and route placebos are informative but do not prove the identifying assumption.
  evidence_refs: [E2]
  possible_diagnostics: [Pretrends, Alternative transport-route placebos, Province-year controls, War-exposure comparisons]
- type: Spatial interference and unequal navigation losses
  basis: reported
  condition: Non-canal counties may lose trade access too, and the southern corridor continued functioning relatively well; adjacency alone is not uniform treatment intensity.
  evidence_refs: [E2]
  possible_diagnostics: [Distance gradients, Donor restrictions, North-south contrast using the old river course]
- type: Historical reporting and geography reconstruction
  basis: inferred
  condition: Court-record rebellion onsets and reconstructed county geography may not measure identical populations throughout 1650-1911. The official V4 download inventory does not by itself establish the exact county-polygon layer used in the paper.
  evidence_refs: [E2, E3, E4]
  possible_diagnostics: [Audit onset coding and changing reporting, Reconcile county layers and identifiers, Compare normalization choices]
empirical_requirements:
  contract_version: 1
  population: Historical counties in the six-province canal study region, restricted by usable population inputs for the baseline
  observation_unit: Historical county-year
  geography_level: Paper-harmonised historical county, with province and prefecture crosswalks
  time_start: 1650
  time_end: 1911
  minimum_frequency: Annual; preserve sufficiently long pre-1826 and post-1826 windows for the intended specification
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields: [Rebellion onsets, Canal adjacency, Prefecture population in 1600, County households in 1546, Geographic exposure layers, Pretreatment rebelliousness, Specification-specific climate and agricultural controls]
  required_identifiers: [Historical county ID, Year, Prefecture ID, Province ID, Versioned geography]
  treatment_key: [Historical county ID, Year]
  treatment_source: Published spatial-join definition linked to historical geographic layers and replication deposit; the imperial trial is a timing anchor rather than a treated-county roster
  measurement_risks:
  - The 575-county geographic inventory differs from the 536-county normalized regression sample.
  - Population is imputed by allocating prefecture 1600 population using county 1546 household shares; it is not directly observed annual county population.
  - A modern county code or a 1911 time-slice polygon cannot silently substitute for the paper's harmonised geography.
  - Two pre/post observations are only a matching minimum, not replication of the published long-panel and event-study requirements.
evidence:
- id: E1
  source_type: archive
  citation: Qing imperial court. 清宣宗成皇帝实录, volume 96, 道光六年三月甲申 directive responding to Tao Shu's sea-shipping memorial.
  url: https://www.shidianguji.com/mid-page/7425368283639152691
  date: 1826
  supports: [identity.authority, identity.instrument, identity.legal_identifiers, timeline.implementation_start, assignment.compliance]
  verification_status: verified
  access_level: full-text
  locator: Inspected digital transcription, volume heading and the 甲申 imperial directive describing the year's initial sea-shipping trial, reported initial deliveries, Tianjin unloading and return for the second shipment. No original folio image or original trial-authorization decree was inspected; no Gregorian day conversion is asserted.
- id: E2
  source_type: paper
  citation: 'Cao, Yiming, and Shuo Chen. 2022. Rebel on the Canal: Disrupted Trade Access and Social Conflict in China, 1650-1911. American Economic Review 112(5):1555-1590. DOI 10.1257/aer.20201283.'
  url: https://doi.org/10.1257/aer.20201283
  date: 2022
  supports: [scope.china_relevance, identity.assignment_mechanism, timeline.local_timing, timeline.anticipation, assignment.rule, assignment.treated, assignment.comparison_pool, assignment.intensity, assignment.exposure_construction, assignment.spillovers, design.primary_strategy, design.estimand, design.estimation_notes, design_applications.data_used, design_applications.treatment_encoding, design_applications.empirical_design, threats.condition]
  verification_status: verified
  access_level: full-text
  locator: Published article at https://www.yimingcao.com/uploads/6/5/6/3/65630513/canal.pdf inspected 2026-09-28; pp.1560-1564 history/data, Tables 1-3 and equations 1-2 pp.1566-1570, distance gradients pp.1573-1574, SCM donor rule pp.1576-1577, old-course north-south contrast/Table 5 pp.1577-1579. Verification means inspection of the paper's actual design, not independent confirmation of all historical claims or a replicated estimate.
- id: E3
  source_type: official-data
  citation: Fudan University Center for Historical Geography. CHGIS Datasets V4 download documentation.
  url: https://yugong.fudan.edu.cn/CHGIS/sjxz.htm
  date: null
  supports: [empirical_requirements.treatment_source, empirical_requirements.measurement_risks]
  verification_status: verified
  access_level: official-document
  locator: 1820 and 1911 layer inventories and 1820 source description. Lists 1820 county seats, towns and rivers but not a nationwide 1820 county-boundary download; lists 1911 county boundaries. Provider documentation inspected, not underlying GIS files or the paper's crosswalk.
- id: E4
  source_type: official-data
  citation: Harvard CHGIS project. Intro to CHGIS.
  url: https://chgis.fas.harvard.edu/pages/intro/
  date: null
  supports: [assignment.required_identifiers, empirical_requirements.required_identifiers, empirical_requirements.measurement_risks]
  verification_status: verified
  access_level: official-document
  locator: Project description explains temporal-instance geocodes, historical units and 1911 single-year time-slice versus time-series overlap. Does not certify the exact paper's county classification or historical boundary stability.
- id: E5
  source_type: replication
  citation: Cao, Yiming, and Shuo Chen. 2022. Data and Code for Rebel on the Canal. openICPSR V1, DOI 10.3886/E157781V1.
  url: https://www.openicpsr.org/openicpsr/project/157781/version/V1/view
  date: '2022-04-19'
  supports: [scope.regions, empirical_requirements.population]
  verification_status: verified
  access_level: metadata
  locator: Project V1 landing page lists Data, Program, Results and Readme.pdf; geographic universe specifies six provinces as of 1820 and county-year unit. File previews/downloads did not expose usable content in this pass. Metadata establishes the deposit, not executed code or verified raw-data availability.
design_applications:
- paper: 'Rebel on the Canal: Disrupted Trade Access and Social Conflict in China, 1650-1911'
  doi: 10.1257/aer.20201283
  journal: American Economic Review
  year: 2022
  research_question: Did declining regional trade access increase social conflict in historical Chinese counties?
  population: Historical counties in six provinces around the Grand Canal; baseline normalized sample of 536 counties
  outcome: Inverse hyperbolic sine of rebellion onsets per million imputed 1600 population
  data_used: [Qing Shilu rebellion onsets, Historical geographic layers from Harvard Yenching and Fudan, Cao population reconstruction, Liang county households, Climate and agricultural historical controls]
  treatment_encoding: Fixed canal-adjacency indicator interacted with year greater than or equal to 1826; extensions use geographic intensity and distance
  comparison: Canal versus non-canal county outcome changes; north-south and alternative-route comparisons are supplementary diagnostics
  empirical_design: County-year DID and decadal event study, with supplementary CIC and synthetic control
  assumptions: [Conditional parallel trends, No unmodelled differential shocks, Historically comparable recording and geography]
  threats_addressed: [Pretreatment differences, Alternative transport routes, North-south navigation differences, Spatial spillovers, Major nineteenth-century wars]
  evidence_refs: [E2]
method_transfer: null
readiness_blockers:
- Recover replication README and code, exact canal and county layers, spatial-contact rule and sample crosswalk; the provider's V4 inventory is not proof of a ready-made 1820 county-polygon layer.
- Inspect original archive images or a scholarly critical edition for the transcribed directive before close historical quotation; independently locate later restoration and closure instruments if those dates become the research treatment.
- Audit rebellion-onset extraction, population imputation, missing counties and specification-specific historical controls before claiming numerical reproduction.
---

## Institutional Background

[E1, inspected primary-record transcription] Grain sea transportation was actually
being implemented in 1826: the imperial directive coordinates unloading and vessel
return, rather than merely proposing an alternative route. [E2, paper report]
The canal had supported both tribute shipping and private commerce. Shifting the
state's grain transport threatened the livelihoods and market access built around
that corridor, providing a regional and urban-development question.

## What Changed

The institutional object is a transition, not a switch turning off every canal
segment. The trial, restoration, subsequent shipping decline and final abandonment
belong to one episode here. Splitting its calendar milestones into several
independent variations would obscure the published counterfactual and inflate the
inventory. The dated archival directive confirms the trial but does not independently
prove all later closure dates or the paper's expectations mechanism.

## Implementation and Assignment

[E2, paper report] County exposure comes from geography established before the
trial. It is not a government list of newly treated counties. The northern contrast
uses the old Yellow River course; using its modern course would change assignment.
[E3-E4, provider documentation] Historical identifiers and dated layers exist, but
the inspected downloads do not close the exact county-polygon provenance. Preserve
that reconstruction gap rather than supplying a guessed map vintage.

## Why This Creates Empirical Variation

[Analytical inference] The same national transport transition can affect places
differently because some depend more on the canal. An observed pre-existing route
provides exposure, not automatic exogeneity. The post-1826 contrast becomes useful
only with a credible account of what otherwise would have happened to those counties.
The recorded application supplies such a research design; its assumptions remain
open to scrutiny for any new outcome.

## Identification Risks

[E2, paper report] Southern navigation remained relatively functional, and nearby
non-canal counties may share trade losses. Neither all treated counties nor all
controls have identical exposure. The long post period also contains major changes
beyond the temporary experiment. Negative placebo estimates and pretrend tests help
evaluate these concerns; they are not certificates of random assignment.

## Data Requirements

Build a historical county-year join, not a modern-city treatment list. Keep the
onset count, population denominator, transformation, fixed corridor exposure and
sample restrictions recoverable. A researcher using another outcome must establish
its own geographic and temporal comparability. Data assets and acquisition details
belong in the complementary data repository, linked by the application DOI, rather
than copied into another canonical assignment record.

## Evidence Notes

Task `task-83135b77fc77` reopens the historical access blockage recorded in
`candidate-2fcf8288fb5b`. Newly readable published design and a directly inspected
imperial-record transcription support grounded admission. Exact map reconstruction,
original archive scans and executable replication remain explicit conditions. This
is therefore a conditional research candidate, not design-documented readiness.
