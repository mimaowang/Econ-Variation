---
schema_version: 2
id: china-2017-industrial-transformation-demonstration-first-cohort
name: China first-cohort industrial transformation demonstration-zone city exposure
aliases: [首批产业转型升级示范区, old-industrial and resource-city transformation pilots]
status: grounded
provenance:
  task_id: task-2bbde75956b0
scope:
  country: China
  regions: [Mainland China]
  domains: [regional-economics, urban-economics, industrial-economics, development, industrial-upgrading, innovation]
  variation_type: pilot-assignment
  knowledge_role: china-variation
  china_relevance: A mainland regional industrial-policy designation is actually used in a published economics paper to study city industrial upgrading. The record serves that first-cohort city exposure, not a generic environmental or financial policy.
identity:
  instrument: First-cohort national industrial transformation/upgrading demonstration-zone designation in2017.
  authority: NDRC and four cooperating departments; provincial coordination and locally implemented plans.
  legal_identifiers: [发改振兴〔2017〕671号]
  implementation_regime: Administrative recognition with locally differentiated implementation; this case is limited to the first cohort and its city-level research application through2018. Later cohorts and project awards are outside the served assignment.
  assignment_mechanism: Provincial recommendations and national administrative selection favor previously capable old-industrial/resource cities; the published application maps designated economic regions to21 prefecture-level units. That mapping is a reported aggregate proxy, not a legal expansion of special territories.
  parent: null
  related_variations: [china-industrial-transfer-policy-inland-city-status]
timeline:
  announcement: Notice signed2017-04-13 and publicly posted2017-04-21.
  effective: Recognition date is distinct from local-plan approval or individual project operation; exact local operative dates are not inspected.
  implementation_start: 2017
  implementation_end: null
  local_timing: The inspected city application turns exposure on in2017 and ends its panel in2018. The endpoint is a sample restriction, not policy abolition. Its discussion names a later2019 cohort but that cohort is not served here.
  anticipation: Prior industrial-city plans and preparation can affect trends before national recognition; policy selection explicitly rewards prior progress.
  last_verified: '2026-10-05'
assignment:
  unit: National city/economic-region designation; prefecture-level city-year proxy in the inspected application.
  treated: The paper's21 cities are Shenyang, Anshan, Fushun, Changchun, Jilin, Songyuan, Baotou, Ordos, Zhuzhou, Xiangtan, Loudi, Shizuishan, Wuzhong, Yinchuan, Tangshan, Changzhi, Zibo, Tongling, Huangshi, Chongqing and Zigong. See the boundary distinction in the prose.
  comparison_pool: The published paper uses138 other sampled old-industrial/resource prefectures, plus pre2017 observations. This is not a comparison with every Chinese city; later-treated places may be controls only within the2018 endpoint.
  rule: For the reported first-cohort application set did_ct =1 for a listed city and year>=2017, otherwise0, restricted to the2003–2018 study window. Preserve this proxy separately from the official economic-region boundary.
  intensity: Binary city recognition exposure; not a firm's received subsidy, project completion, park membership or actual implementation intensity.
  exemptions: [No whole-province exposure, Later designation cohorts are not first-cohort treatment, Industrial transfer demonstration zones and industrialization bases are distinct programs]
  compliance: Recognition does not imply equal local activity or support to every firm. Actual take-up requires local/project evidence.
  exposure_construction: Store the21-city author mapping with historical city codes and cohort2017; join city_id/year to city outcomes. Retain a separate official-territory variable for sensitivity, especially Ningdong and the Chongqing surrounding urban area. Do not assign every firm within a mapped city direct project receipt. Registered/operating-address exposure and corporate-group joins require their own documented convention.
  required_identifiers: [city_id, year, historical_city_name, boundary_version]
  spillovers: Multi-city clusters coordinate activities and can affect nearby untreated cities through industry links and investment. City clustering need not capture dependence within a jointly assigned economic region.
research_compatibility:
  outcome_domains: [industrial structure upgrading, industrial structure rationalization, city innovation, regional investment]
  affected_populations: [mainland old-industrial and resource cities]
  mechanism_channels: [industrial coordination, innovation platforms, investment, local implementation]
  best_for: [annual city-level first-cohort recognition exposure, industrial upgrading in comparable old-industrial/resource cities]
  not_good_for: [exact park boundary effects without local maps, direct subsidy receipt, all-China random policy allocation, long-run effects with a2018 endpoint, ready firm-level exposure without an address convention]
design:
  claim_type: reduced-form
  affordances: [selected first-cohort cities versus other old-industrial/resource cities before and after2017]
  candidate_designs: [city-year difference-in-differences, event-study with boundary sensitivity]
  identifying_variation: One common2017 recognition onset for the paper's21-city first cohort within a159-city sample; the national label alone is not the comparison.
  primary_strategy: The2021 paper estimates city and year fixed-effects DID with lagged controls; city-level clustered standard errors are reported.
  estimand: Conditional average change in the paper's city industrial-structure measures associated with first-cohort recognition, not a pure effect of one component subsidy or verified direct treatment of all territory.
  treatment_variable: did_ct = first_cohort_author_city_c times indicator(year>=2017), through2018.
  comparison_logic: Require comparable counterfactual trends within the selected old-industrial/resource-city pool; account for preparation and co-assigned clusters. Differences in levels need not invalidate DID but selection on trends does.
  estimation_notes: The paper reports159 cities over2003–2018. Table2 has2462 observations without controls and1959/1937 for controlled upgrading/rationalization. Outcome construction uses sector value added and employment, with normalized sector labor productivity for upgrading and a negative weighted productivity-deviation measure for rationalization. There are only two post years. Do not label this a staggered-cohort estimator or extend its controls through later entry.
  assumptions: [conditional parallel outcome trends, no unmodeled preparation effects, defensible aggregate city exposure, no unhandled policy overlap or spatial interference, comparable sector measurement]
  diagnostics: [pre2017 event leads and power, omit transition2017, exclude broad Chongqing exposure, narrow Ningdong mapping sensitivity, economic-region dependence, nearby-city exclusion, concurrent-policy checks, missingness by treatment]
threats:
  - type: selection
    basis: documented
    condition: Selection favors prior reform achievements and foundations, so firm-level inability to choose designation is not an exogeneity argument.
    evidence_refs: [E3]
    possible_diagnostics: [prepolicy trend comparison, comparable old-industrial/resource controls, predetermined covariate trends]
  - type: geographic-measurement
    basis: documented
    condition: Official special territories are mapped to entire prefectures in the author footnote; preserve rather than silently reconcile the difference.
    evidence_refs: [E1, E2]
    possible_diagnostics: [narrow territory sensitivity, drop Wuzhong and Yinchuan, omit Chongqing, explain aggregate intention-to-treat estimand]
  - type: inference-and-spillovers
    basis: inferred
    condition: Joint economic-region assignment and spatial coordination can correlate city outcomes across nominal clusters.
    evidence_refs: [E1, E2]
    possible_diagnostics: [region-level dependence sensitivity, spatially robust inference, assignment-level resampling with justified exchangeability]
  - type: policy-overlap
    basis: reported
    condition: The paper reports controls for industrial-transfer and low-carbon pilots but does not display their robustness results; this does not independently validate overlap adjustment.
    evidence_refs: [E1]
    possible_diagnostics: [recover omitted tables, audit concurrent policies for the chosen outcome]
empirical_requirements:
  contract_version: 1
  population: Mainland prefecture-level old-industrial/resource cities comparable to the paper's159-city pool.
  observation_unit: city-year
  geography_level: prefecture-level city
  time_start: 2003
  time_end: 2018
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 2
  required_fields: [city-year research outcome, first_cohort_author_city, historical city boundary, sector value added and employment for paper industrial-structure measures, price deflators for monetary fields, population GDP budget expenditure utilized FDI retail sales highway length and area for published controls]
  required_identifiers: [city_id, year]
  treatment_key: [city_id, year]
  treatment_source: Official2017 notice identifies recognition; Peng and Jin2021 SectionIII and footnote6 supply the explicit21-city annual proxy.
  measurement_risks: [special-territory aggregation, normalization not fully reproducible without author code, missing outcome-specific city rows, registered versus operating firm location, only two post years]
evidence:
  - id: E1
    source_type: paper
    citation: '彭飞、金慧晴 (2021). 区域产业政策有效性评估——基于中国资源型和老工业城市的证据. 产业经济研究 (3):99–111. DOI10.13269/j.cnki.ier.2021.03.008.'
    url: https://doi.org/10.13269/j.cnki.ier.2021.03.008
    date: 2021
    supports: [assignment.treated, assignment.rule, assignment.comparison_pool, design.primary_strategy, design.estimation_notes, empirical_requirements.required_fields, design_applications.treatment_encoding, design_applications.data_used]
    verification_status: reported
    access_level: full-text
    locator: 'Actual13-page publisher PDF https://bjb.nufe.edu.cn/dfiles/1/20210308.pdf accessed in memory: printedpp99–109, SectionIII equation1 and outcome equations2–3, SectionIV Tables2 and6, SectionV robustness and footnotes6–9. Printedp109/footnote6 visually inspected. Publication year/issue verified; exact issue day not established.'
  - id: E2
    source_type: policy-document
    citation: NDRC joint first-cohort designation notice, 发改振兴〔2017〕671号.
    url: https://www.ndrc.gov.cn/xxgk/zcfb/tz/201704/t20170421_962949.html
    date: '2017-04-13'
    supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.announcement, assignment.unit, assignment.compliance]
    verification_status: verified
    access_level: official-document
    locator: Opening12-region designation; SectionsI–IV local coordination, provincial-plan approval, support and evaluation; signature2017-04-13 and website date2017-04-21. Linked attachment not inspected.
  - id: E3
    source_type: policy-document
    citation: NDRC contemporaneous explanation of first-cohort selection.
    url: https://www.ndrc.gov.cn/fzggw/jgsj/zxs/sjdt/201704/t20170421_1193676.html
    date: '2017-04-21'
    supports: [identity.assignment_mechanism, assignment.rule, timeline.anticipation]
    verification_status: verified
    access_level: official-document
    locator: Selection paragraph explicitly describes provincial recommendations from old-industrial/resource-city plans, strong foundations and prior achievements; it supports selective designation, not the author's enlarged city crosswalk.
design_applications:
  - paper: Regional industrial-policy effectiveness in resource and old-industrial cities
    journal: 产业经济研究 / Industrial Economics Research
    year: 2021
    research_question: Does first-cohort designation change city industrial upgrading and rationalization?
    population: 159 mainland old-industrial/resource prefecture-level cities.
    doi: 10.13269/j.cnki.ier.2021.03.008
    outcome: Sector-weighted normalized labor-productivity upgrading and negative weighted productivity-deviation rationalization.
    data_used: [EPS, China City Statistical Yearbook, municipal yearbooks and bulletins for missing data]
    treatment_encoding: Author21-city mapping interacted with2017-or-later, in2003–2018;21 treated and138 comparison cities before missingness.
    comparison: City/year effects with one-year-lagged controls within the old-industrial/resource-city pool.
    empirical_design: Common-onset DID with city clustering; reported event study, PSM caliper0.05, placebo and bootstrap1000 sensitivity.
    assumptions: [conditional parallel trends, valid aggregate proxy, no unhandled spatial interference]
    threats_addressed: [displayed pretrend exercise, reported Chongqing exclusion, displayed PSM and bootstrap sensitivity, undisplayed overlap controls]
    evidence_refs: [E1]
method_transfer: null
readiness_blockers:
  - Conditional use is the documented21-city annual recognition proxy. Exact-territory or direct-firm/project treatment requires local maps and an explicit location/receipt convention; it cannot inherit this city contract.
  - Audit selective assignment, economic-region dependence and spillovers for the chosen outcome. PSM or insignificant leads are not proof of valid counterfactual trends.
  - Exact reconstruction of normalized industrial-structure outcomes needs the normalization/code; omitted overlap tables and the BMJ2022 firm-innovation methods remain unavailable. Those gaps do not erase the inspected city application but prevent offering the separate firm application as ready.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

This is a regional industrial-transition program for old-industrial and
resource-city settings, not a universal subsidy or a claim that every city
industrial park changed policy in2017. Selection reflects prior progress
and provincial recommendations [E3]. Its empirical usefulness must therefore
come from a credible comparison, not from the label “quasi-natural experiment.”

## What Changed

The first cohort received national recognition under a locally implemented
regime [E2]. This record follows the recognition mechanism, not later cohorts,
specific grants or industrial-transfer designation. Recognition, construction
plan approval and project operation are separate timing objects.

## Implementation and Assignment

The paper makes its proxy reconstructible [E1, reported claim]:

| Author group | City mapping |
|---|---|
| Liaoning central | 沈阳、鞍山、抚顺 |
| Jilin central | 长春、吉林、松原 |
| Inner Mongolia western | 包头、鄂尔多斯 |
| Hunan central | 株洲、湘潭、娄底 |
| Ningxia northeastern | 石嘴山、吴忠、银川 |
| Other author-mapped units | 唐山、长治、淄博、铜陵、黄石、重庆、自贡 |

Footnote6 explicitly includes Wuzhong and Yinchuan and uses whole Chongqing.
The official notice instead names Shizuishan–Ningdong and Chongqing's surrounding
urban area [E2]. Those are not interchangeable geographies. Preserve both layers:
the table reproduces an actual city application, while exact-territory exposure
requires more detailed maps. An aggregate recognition-environment question can
use the proxy conditionally; a park-boundary or direct-subsidy question cannot.

## Why This Creates Empirical Variation

The observed comparison is21 author-mapped cities versus138 other cities before
and after2017, ending in2018 [E1, reported claim]. City and year effects do not
remove changing advantages that helped win designation. Evaluate pre-trend power,
preparation and regional trajectories for the new outcome [analytical inference].

## Identification Risks

Jointly assigned economic regions complicate city-level inference and controls
may receive spillovers [analytical inference]. Only2017–2018 are post years in
the inspected application [E1, reported claim]. Its broader firm-mechanism table
does not supply a ready historical-address contract. Do not silently translate
city recognition into a firm's received treatment or add later cohorts without
an audited roster and comparison redesign.

## Data Requirements

Join historical city codes and year to the explicit first-cohort proxy. For the
published outcomes, sector value added and employment are essential; for another
city outcome, do not require patents merely because innovation is a proposed
channel. Retain the study's old-industrial/resource-city population rather than
substituting a nationwide sample without explaining comparability.

## Evidence Notes

The2021 full methods resolve a city application despite the unavailable BMJ2022
body. The latter remains a source lead, not an inspected firm-innovation design.
Grounded admission preserves the conditional city proxy; it does not certify
precise territory, author-code replication or causal validity for every idea.
