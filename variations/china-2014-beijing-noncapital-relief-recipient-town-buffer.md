---
schema_version: 2
id: china-2014-beijing-noncapital-relief-recipient-town-buffer
name: Beijing Noncapital Function Relief and Nearby Recipient-Town Exposure
aliases: [NCFR recipient-town buffer, 北京非首都功能疏解与周边乡镇承接暴露]
status: grounded
provenance:
  task_id: task-1d505b0cda43
scope:
  country: China
  regions: [Hebei, Tianjin, Liaoning, Inner Mongolia, Shanxi, Henan, Shandong]
  domains: [regional-economics, urban-economics, development, firm-entry, industrial-relocation]
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: A Beijing dispersion policy is studied through growth and firm entry in nearby mainland recipient towns outside Beijing, relative to towns outside the wider Beijing-Tianjin-Hebei region.
identity:
  instrument: Noncapital function relief through restrictions on new activities in Beijing, reduction or relocation of existing functions, and support for regional recipients; paper-defined exposure is proximity outside Beijing rather than designation of each recipient town.
  authority: Central coordination of Beijing-Tianjin-Hebei development; Beijing municipal authorities and relevant registration/project departments, with Tianjin and Hebei recipient governments.
  legal_identifiers: [北京市新增产业的禁止和限制目录（2014年版）, 北京市新增产业的禁止和限制目录（2015年版）京政办发〔2015〕42号]
  implementation_regime: A policy bundle pursued since2014, with revised industry restrictions in2015 and later years. The2015 notice distinguishes citywide and functional-area restrictions, new activity from in-process or upgrading projects, and specific exceptions. These rules restrict Beijing entry; they do not legally grant uniform benefits to every town within20kilometres outside Beijing.
  assignment_mechanism: The authors select Hebei/Tianjin town polygons intersecting the20km outward buffer of Beijing as exposed recipients. Controls intersect a20km outward buffer of the entire Beijing-Tianjin-Hebei region and are in other provinces. This is a spatially selected two-region DID, not opposite sides of a single local cutoff, random recipient assignment or a firm-level relocation mandate.
  parent: null
  related_variations: [china-2015-tongzhou-subcenter-announcement-district-exposure, china-industrial-transfer-policy-inland-city-status]
timeline:
  announcement: '2014-02 (paper proposal chronology)'
  effective: null
  implementation_start: 2014
  implementation_end: null
  local_timing: >
    Section3.2 anchors the policy year to2014 and the panel to2010-2019. Section2.2 separately describes formal implementation one year after theFebruary2014 proposal. Preserve that distinction: the annual proposal-based contrast is not proof that all2015 catalogue restrictions operated throughout2014. Exact author post syntax remains a replication detail; report sensitivity to2014 transition versus2015 implementation.
  anticipation: Announcement, catalogue revisions and actual relocations are sequential. Firms and local governments can adjust before particular approvals or project completions.
  last_verified: '2026-10-07'
assignment:
  unit: Town-level administrative polygon by year, including street, town and township types.
  treated: Hebei/Tianjin towns intersecting the20km buffer outside Beijing's administrative boundary, under the authors' recipient-exposure interpretation.
  comparison_pool: Towns in Liaoning, Inner Mongolia, Shanxi, Henan and Shandong intersecting the20km buffer outside the Beijing-Tianjin-Hebei region. Beijing itself is not a control because the policy also changes its activities.
  rule: Official restrictions apply within Beijing according to catalogue jurisdiction and industry conditions. For the reported recipient application, separately dissolve Beijing and Beijing-Tianjin-Hebei boundaries, construct outward buffers, intersect town polygons, and assign the two sample groups. Twenty kilometres is an analytical sampling rule, not a legal eligibility threshold. Preserve polygon-intersection selection rather than replacing it with centroid distance.
  intensity: Binary membership in the near-Beijing recipient sample interacted with the paper's annual policy period. Alternative buffer widths vary sample selection, not legally assigned intensity.
  exemptions:
  - The2015 catalogue exempts in-process and upgrading projects and preserves specified special-policy areas and other legal provisions; foreign investment follows its own catalogue.
  - The recipient sample does not imply that all industries or existing firms in Beijing were prohibited.
  compliance: Town proximity predicts access to potential displaced activity, not observed receipt or verified firm moves. New registration can arise locally and need not identify origin in Beijing.
  exposure_construction: Archive town geometry, province/county affiliations and both dissolved regional borders in a metric coordinate system. Select intersecting outward-buffer polygons, retain stable town/year keys, and join annual mean light and county controls. For firm entry, geocode registered addresses and aggregate incorporation counts to the same polygons; an individual firm's current address is not a historical operating-site history.
  required_identifiers: [town_id, county_id, province_id, year, town_polygon_version]
  spillovers: Beijing is intentionally affected. The distant outer-region controls may still receive wider industrial or market spillovers; geographic separation reduces direct contact but does not prove no interference.
research_compatibility:
  outcome_domains: [Town nighttime-light intensity, New firm registration, Regional development, Population distribution]
  affected_populations: [Recipient and comparison towns near the two distinct regional boundaries]
  mechanism_channels: [Restricted Beijing entry, Industrial relocation, Infrastructure support, Population redistribution]
  best_for: [Conditional recipient-region growth and firm-entry contrasts with reproducible town buffers and explicit concurrent-policy chronology]
  not_good_for: [A sharp geographic RD at one shared border, Firm-specific compulsory relocation effects, National net welfare or productivity gains from local light growth, Uniform industry prohibition]
design:
  claim_type: reduced-form
  affordances: [Reconstructable geographic sample rule, Annual before/after outcomes, Alternative widths, Separate institution and recipient-exposure definitions]
  candidate_designs: [Two-region town-panel difference-in-differences, Exposure-by-year diagnostics]
  identifying_variation: Differential post-policy change in near-Beijing recipient towns versus outside-JingJinJi border towns. Those groups occupy different boundaries, so local continuity at one border does not establish their counterfactual comparability.
  primary_strategy: Equation1 includes town/year fixed effects and time-varying county GDP, wage, fiscal expenditure and investment controls. Table2 reports6530 town-years, town clusters and a Conley-error alternative.
  estimand: Conditional relative change in observed recipient-town outcomes under the dispersion bundle, not the national average effect of an isolated catalogue provision.
  treatment_variable: Recipient-town group times common annual post, anchored to the paper's2014 policy convention; verify its exact annual switch before reproducing coefficients.
  comparison_logic: Use outer-JingJinJi towns instead of Beijing to avoid deliberately affected metropolitan controls. Assess group-specific pretrends and baseline structure because the two buffers are not adjacent treated/control sides of one discontinuity.
  estimation_notes: Outcome is log annual mean PANDA nighttime-light intensity, not GDP growth itself. Table2's6530 observations over10years are consistent with653 towns but no roster was inspected. Time-varying fiscal/investment controls may be policy channels. Exact GIS vintage, Conley bandwidth and log-zero handling require reproduction documentation.
  assumptions: [Conditional comparable counterfactual trends across the two geographic samples, No differential concurrent regional shocks dominating the contrast, Stable polygons and outcome measures, Control-region interference explicitly considered]
  diagnostics: [Pre-policy exposure-year coefficients, Alternative5-100km buffers, Placebo assignment/time exercises, Town-area and administrative-type subsets, Concurrent infrastructure and regional-policy chronology, Spatially correlated inference]
threats:
- type: two-boundary-counterfactual
  basis: documented
  condition: Recipient and control samples sit at different geographic borders. Closeness to their own border does not make them locally exchangeable with each other; the paper's boundary-DID label should not imply sharp-RD identification.
  evidence_refs: [E1]
  possible_diagnostics: [Baseline structure and pretrends, Alternative justified control groups, Region-specific shocks]
- type: bundled-policy-and-clock
  basis: documented
  condition: The2014 proposal contrast spans2015 industry restrictions and other coordinated development projects. Official restrictions are heterogeneous and revised, not one uniform date or industry rule. Infrastructure changes can affect lights independently of productive activity.
  evidence_refs: [E1, E2, E3]
  possible_diagnostics: [Alternative transition coding, Component chronology, Outcome-specific policy controls without mechanically conditioning on mediators]
- type: registration-and-raster-measurement
  basis: reported
  condition: Newly registered firms do not reveal their origin, actual production or relocation. PANDA is a model-extended light series and LandScan is gridded population, not direct town GDP or migration histories. Table1 labels Manu_Entry foreign-invested while Sections3.2.2/5.1 call it manufacturing; do not silently resolve the classification conflict.
  evidence_refs: [E1]
  possible_diagnostics: [Historical address/classification checks, Registry log-zero convention, Alternative light measures, Census-unit reconciliation]
empirical_requirements:
  contract_version: 1
  population: Recipient towns outside Beijing and comparison towns outside Beijing-Tianjin-Hebei selected by polygon-buffer intersection.
  observation_unit: town-year
  geography_level: township-level polygons
  time_start: 2010
  time_end: 2019
  minimum_frequency: annual
  minimum_pre_periods: 4
  minimum_post_periods: 4
  required_fields: [Town geometry and stable IDs, Both regional boundaries and buffer membership, Year, Annual mean nighttime-light intensity, County GDP/wage/fiscal-expenditure/fixed-investment controls for the reported controlled specification]
  required_identifiers: [town_id, county_id, province_id, year, town_polygon_version]
  treatment_key: [town_id, year]
  treatment_source: Official Beijing restriction framework plus paper Section3.1's recipient and control buffer construction;2014 is the reported policy-period convention, not a uniform operative industry restriction.
  measurement_risks: [Geometry version and administrative changes, Model-derived light comparability, Light/log-zero handling, Policy timing convention and post-treatment controls]
design_profiles:
- id: town-firm-entry
  label: New firm registration in recipient towns
  design_families: [Two-region town-panel difference-in-differences]
  when_to_use: Use for formal enterprise incorporation, not verified relocation or production; manufacturing-specific results require clarification of the paper's inconsistent category label.
  outcome_domains: [New firm registration]
  requirements:
    population: The same recipient/control town groups with comparable historical incorporation coverage.
    observation_unit: town-year
    geography_level: township-level polygons
    time_start: 2010
    time_end: 2019
    minimum_frequency: annual
    minimum_pre_periods: 4
    minimum_post_periods: 4
    required_fields: [Baseline buffer membership, Firm incorporation year, Historical registration address and geocode, Annual new-firm counts and log-zero convention, County controls for controlled specification]
    required_identifiers: [firm_id, town_id, county_id, province_id, year]
    treatment_key: [town_id, year]
evidence:
- id: E1
  source_type: paper
  citation: 'Yuan, Bo, Kecen Jing, and Yuhai Liu.2024. From agglomeration to dispersion: How does China''s noncapital functions'' relief affect regional development? Journal of Regional Science64(3):595-620. DOI10.1111/jors.12684; firstonline2024-01-23.'
  url: https://doi.org/10.1111/jors.12684
  date: 2024
  supports: [identity.assignment_mechanism, timeline.announcement, timeline.local_timing, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.intensity, assignment.exposure_construction, assignment.spillovers, design.primary_strategy, design.identifying_variation, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, design.diagnostics, threats.condition, empirical_requirements.population, empirical_requirements.observation_unit, empirical_requirements.time_start, empirical_requirements.time_end, empirical_requirements.required_fields, empirical_requirements.treatment_source, empirical_requirements.measurement_risks, design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year, design_applications.research_question, design_applications.population, design_applications.outcome, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design, design_applications.assumptions, design_applications.threats_addressed]
  verification_status: reported
  access_level: full-text
  locator: Publisher HTML https://onlinelibrary.wiley.com/doi/full/10.1111/jors.12684 inspected2026-10-07, Sections2.2/3.1-3.2/4.1-4.2/5-6, Tables1-8 and endnotes1-4. Figure captions inspected, not digitized. Section3.1 specifies polygon intersections at two different outer borders;3.2 anchors2014. Author-request data/code not inspected.
- id: E2
  source_type: policy-document
  citation: 北京市人民政府办公厅,北京市新增产业的禁止和限制目录（2015年版）,京政办发〔2015〕42号,2015-08-17.
  url: https://www.beijing.gov.cn/zhengce/zhengcefagui/201905/t20190522_58709.html
  date: '2015-08-17'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, assignment.rule, assignment.exemptions, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Notice signature, replacement of2014 version, explanatory SectionsI-III and project/function-area definitions inspected2026-10-07. Legal Beijing scope and exceptions verified; attached industry tables not inspected and no exhaustive industry eligibility is claimed. Does not legally assign the20km recipient buffer.
- id: E3
  source_type: implementation-document
  citation: 国家发展改革委,关于政协十三届全国委员会第四次会议第0148号提案答复的函,2021.
  url: https://www.ndrc.gov.cn/xxgk/jianyitianfuwen/qgzxwytafwgk/202112/t20211220_1308660.html
  date: 2021
  supports: [identity.instrument, identity.authority, identity.implementation_regime, timeline.implementation_start, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: Opening response and paragraph stating policy activity since2014, inspected2026-10-07. Grounds the coordinated dispersion bundle, not each recipient town's actual treatment receipt or the paper's post syntax.
design_applications:
- paper: 'From agglomeration to dispersion: How does China''s noncapital functions'' relief affect regional development?'
  doi: 10.1111/jors.12684
  journal: Journal of Regional Science
  year: 2024
  research_question: Does Beijing dispersion change regional activity and entry in nearby recipient towns?
  population: 2010-2019 town panel in the two distinct20km outer buffers;6530 observations in Table2.
  outcome: Log mean nighttime lights; town new registrations and gridded population as supplementary outcomes. Firm TFP2010-2015 is a different short panel, not proof of long-run null productivity effects.
  data_used: [PANDA annual nighttime lights, Business Registration Enterprises Database geocoded to towns, County regional-economy/urban-construction yearbooks, LandScan and2010/2020 census for supplementary population analysis]
  treatment_encoding: Near-Beijing recipient polygons versus outside-JingJinJi control polygons times paper's annual2014 policy convention;buffer selection is intersection, not centroid cutoff.
  comparison: Different outer regional borders;Beijing excluded because directly affected.
  empirical_design: Town/year DID, county controls, town clusters and reported Conley alternative;event diagnostics omitT-1, width and subset checks.
  assumptions: [Comparable counterfactual trends, Explicit bundle/clock interpretation, Stable spatial joins and measured outcomes, No dominating control spillovers]
  threats_addressed: [Reported leads, Random-placebo exercises,5-100km width alternatives, Town-area and type subsets, Spatial-error alternative]
  evidence_refs: [E1, E2, E3]
method_transfer: null
readiness_blockers:
- Conditional use requires reproducible historical polygon intersections, annual policy coding and spatially appropriate inference; no author roster or code is distributed here.
- Recipient entry is not verified movement from Beijing. Isolating catalogue enforcement rather than the regional bundle needs industry-specific legal tables and a separate design.
---

## Institutional Background

Beijing sought to disperse activities inconsistent with its capital functions,
using entry restrictions, relocation and regional support. Official sources
confirm action since2014 and a revised2015 catalogue [E2-E3]. The recipient
application is not the Tongzhou district housing announcement: it concerns
towns outside Beijing and a different comparison geography.

## What Changed

The institutional bundle could make nearby locations more attractive to
activities constrained in Beijing. Legal restrictions varied by industry,
function area and project status [E2]. No official20km benefit entitlement
is established. The paper's proximity rule represents hypothesized exposure
to displaced demand and activity, not observed treatment receipt [E1, reported].

## Implementation and Assignment

Construct two outward buffers. Treated town polygons intersect the Beijing
buffer in Hebei/Tianjin; controls intersect the outer JingJinJi buffer in
other provinces. Keep the complete polygons selected by intersection rather
than silently clipping their outcome to the buffer or selecting centroids
[E1, reported]. The annual2014 convention and later catalogue implementation
are separate clocks.

## Why This Creates Empirical Variation

The DID compares changes across two samples, not continuity across one shared
boundary. Its credibility depends on comparable counterfactual trends despite
different provincial settings [analytical inference]. Reported checks and a
spatial-error alternative inform that judgment but do not prove exogeneity.

## Identification Risks

Regional infrastructure and other policies can affect recipients at the same
time. Increased lights or incorporation may reflect reallocation, construction
or measurement rather than net welfare gains. A nonsignificant short firm-TFP
result is not proof that productivity never changes [E1, reported; analytical
inference]. Preserve the manufacturing/foreign-invested label conflict and
avoid claiming that registrations identify actual migrant enterprises.

## Data Requirements

Join historical town geometry to policy buffers and town/year outcomes, then
county/year controls. The entry profile replaces the light outcome with
geocoded incorporation counts; it does not require unrelated population or
firm-TFP inputs. Geometry and registry vintages belong in the empirical
implementation, with data-acquisition detail in Econ Data Know-How.

## Evidence Notes

Publisher methods recovered candidate-5b11b69d9c74's access gap. Its blocked
history is retained. Legal sources establish Beijing restrictions and the
dispersion institution; the inspected paper supplies the recipient buffer
and reported application. Author-request data are not a public replication
package, and no exact industry table, roster or executable code is claimed.
