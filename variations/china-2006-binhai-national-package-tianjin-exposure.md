---
schema_version: 2
id: china-2006-binhai-national-package-tianjin-exposure
name: China 2006 Binhai national development package and Tianjin aggregate exposure
aliases: [滨海新区开发开放国家战略, 国发2006年20号天津省级暴露, Tianjin Binhai counterfactual growth]
status: grounded
provenance:
  task_id: task-b75376fd84be
scope:
  country: China
  regions: [Mainland China, Tianjin, Tianjin Binhai New Area]
  domains: [regional-economics, urban-economics, development, industrial-economics, place-based-policy]
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: An actual economics publication evaluates mainland Tianjin aggregate growth around the2006 Binhai national development package. This is one municipality-level regional exposure, not direct eligibility of every Tianjin firm.
identity:
  instrument: National authorization of the Binhai comprehensive reform and development package under国发〔2006〕20号.
  authority: State Council authorization; Tianjin and responsible ministries implement specific measures.
  legal_identifiers: [国发〔2006〕20号]
  implementation_regime: A national package for an already developed submunicipal territory, requiring subsequent implementation plans. The served application treats Tianjin's province-equivalent economy as exposed; the package is not an isolated tax change or the2013 pilot FTZ regime.
  assignment_mechanism: Administrative selection of Binhai as a development/reform pilot. The published application compares one exposed municipality with an outcome-specific combination of other provincial economies. Selection is purposeful, not random.
  parent: null
  related_variations: [china-pilot-ftz-preexisting-production-location-exposure]
timeline:
  announcement: Official document dated2006-05-26; the inspected authority webpage was uploaded2015-07-27.
  effective: Authorization is dated May26,2006; SectionIV requires further measures. It does not establish one simultaneous operational start for every component.
  implementation_start: 2006
  implementation_end: null
  local_timing: Served GDP application fits2000Q1–2006Q2 and evaluates2006Q3–2012Q2, following Section4.1 and Table2. Section3 instead calls2006Q2 the first treated quarter; that conflict is retained, not silently reconciled.
  anticipation: National-plan preparation and earlier Binhai development can affect the fitted preperiod. The paper retains2006Q2 in GDP estimation despite the May authorization; assess a transition-quarter exclusion.
  last_verified: '2026-10-07'
assignment:
  unit: Binhai administrative pilot designation with a Tianjin province-equivalent quarterly outcome application.
  treated: Tianjin aggregate economy; direct institutional territory remains narrower than the municipality.
  comparison_pool: Paper footnote15 lists Shanxi, Jilin, Heilongjiang, Inner Mongolia, Shanghai, Jiangsu, Anhui, Fujian, Jiangxi, Henan, Hunan, Hubei, Guangxi, Hainan, Guizhou, Yunnan, Shaanxi, Gansu, Qinghai and Ningxia. GDP selection retains Shanxi, Jilin, Jiangsu, Fujian, Hubei and Hainan.
  rule: Official assignment designates Binhai under the2006 package. For the served GDP application, exposure is Tianjin times quarter>=2006Q3 within2000Q1–2012Q2; this is the Table2 evaluation clock, not a verified direct-benefit rule for firms or all policy components.
  intensity: One treated regional aggregate and a post-period contrast; no observed firm subsidy receipt or component-specific dose is identified.
  exemptions: [Non-Binhai Tianjin firms are not universally eligible for package benefits, Other provincial outcomes need not be unaffected by national development or spillovers, Later FTZ designation is outside this package application]
  compliance: Authorization and aggregate exposure do not measure implementation of particular projects, tax take-up or reform compliance.
  exposure_construction: Preserve province_id and quarter; harmonize the Tianjin aggregate and donor series by period and statistical vintage. Build outcome-specific prepolicy regression using the reported donor pool, select through adjusted-R2 and AICC, freeze coefficients, and predict Tianjin after2006Q2. For GDP, Table1 includes an intercept and unrestricted signed weights; this is not a convex synthetic control. Keep Binhai legal geography separate from the macro exposure flag.
  required_identifiers: [province_id, quarter, series_id, statistical_vintage]
  spillovers: Bohai neighbours are excluded for expected direct effects, but wider trade/investment links can still contaminate retained donors. The estimate is a relative Tianjin effect, not China's net development gain.
research_compatibility:
  outcome_domains: [provincial real GDP growth, regional investment growth, regional employment growth, provincial export growth, provincial import growth]
  affected_populations: [Tianjin aggregate economy, mainland provincial donor economies]
  mechanism_channels: [regional reform environment, development coordination, investment attraction, openness]
  best_for: [single-treated regional development package, quarterly Tianjin GDP counterfactual within the inspected window]
  not_good_for: [direct firm tax eligibility, isolated package-component effects, all-China random assignment, national net welfare, automatic annual city DID, unrestricted extension past2012]
design:
  claim_type: reduced-form
  affordances: [single treated regional aggregate before and after a national development designation]
  candidate_designs: [factor-based panel counterfactual, outcome-specific donor sensitivity]
  identifying_variation: Tianjin's post2006 aggregate growth relative to a preperiod-fitted relationship with selected other provincial economies.
  primary_strategy: Du-Ge-Li-Pei-Zhou2025 applies the Du-Yin-Zhang panel counterfactual procedure. For each donor-count m it selects the subset maximizing adjusted-R2, stops when the best fit no longer improves, then selects among retained models by corrected AIC. An intercept and donor coefficients are estimated by preperiod OLS and held fixed afterward.
  estimand: Difference between actual Tianjin year-on-year real GDP growth and the predicted no-package path, conditional on the maintained donor relationship; it cannot separate components or establish the national total effect.
  treatment_variable: Tianjin exposure from2006Q3 for the documented GDP evaluation, with May2006 authorization retained separately.
  comparison_logic: Donor economies must remain sufficiently unexposed and the prepolicy common-factor relationship must continue absent the package. Prepolicy fit alone does not exclude a coincident Tianjin-specific shock or a postperiod structural break.
  estimation_notes: CEIC supplies provincial nominal outcomes and CPI. Section4 says nominal variables are converted using province CPI. GDP levels begin1999Q1; year-on-year growth loses the first year. Section4.1 explicitly gives2000Q1–2006Q2 fitting and Table2 ends2012Q2, despite a nearby sentence saying end2012. Table1 GDP weights are Shanxi0.3465, Jilin0.1453, Jiangsu0.5743, Fujian-0.3970, Hubei0.1347 and Hainan0.1907 with intercept-0.0070 and reported R2=0.9871. Tables and significance are reported, not reproduced. Investment uses monthly observations and other outcomes have different periods/donors; they are not interchangeable contracts.
  assumptions: [stable counterfactual factor relationship, no coincident Tianjin-specific confounding, defensible transition-quarter handling, sufficiently unexposed donors, comparable outcome definitions and statistical vintages, valid prediction uncertainty after model selection]
  diagnostics: [holdout prepolicy prediction, omit2006Q2 transition quarter, alternative preperiod endpoints, donor leave-one-out and contaminated-donor exclusions, regional placebo with justified comparability, serially dependent prediction uncertainty, GDP-vintage and deflator sensitivity]
threats:
  - type: selective-designation
    basis: documented
    condition: Binhai was selected as an existing regional growth pole; national authorization is not a lottery and prior development may predict subsequent growth.
    evidence_refs: [E1, E2]
    possible_diagnostics: [preperiod holdout, preparation-timing sensitivity, comparable regional trajectories]
  - type: geographic-aggregation
    basis: documented
    condition: The official pilot territory is narrower than the Tianjin aggregate. An aggregate response can include indirect effects and dilution; it is not direct firm-level eligibility.
    evidence_refs: [E1, E2]
    possible_diagnostics: [state aggregate estimand, recover separate Binhai outcomes for a new design, avoid assigning benefits from municipal address alone]
  - type: timing-and-reporting
    basis: documented
    condition: Section3 names2006Q2 as onset while Section4.1 and Table2 begin GDP evaluation2006Q3; the GDP endpoint sentence also differs from Table2. Employment prose says Guangzhou while Table5 says Guizhou, which is already in the donor pool. These are source discrepancies, not agent corrections.
    evidence_refs: [E2]
    possible_diagnostics: [Table2-based GDP encoding, transition exclusion, recover author code before exact replication of conflicting specifications]
  - type: donor-contamination-and-structural-change
    basis: reported
    condition: The authors exclude Bohai neighbours, provinces with similar policies and Sichuan; other national reforms, the2008 crisis and region-specific changes may still alter the fitted relationship.
    evidence_refs: [E2]
    possible_diagnostics: [audit retained donor reforms, sensitivity around2008, holdout prediction, alternate donor sets]
  - type: inference-and-measurement
    basis: inferred
    condition: High in-sample fit and donor coefficient significance do not validate prediction uncertainty after donor selection. Province CPI is not necessarily an appropriate GDP or investment deflator, and revised series can change historical growth.
    evidence_refs: [E2]
    possible_diagnostics: [serial-dependence-aware inference, selection-aware resampling, official real-growth sensitivity, document vintages and deflation]
empirical_requirements:
  contract_version: 1
  population: Tianjin province-equivalent aggregate and the documented20 mainland donor economies; GDP application only by default.
  observation_unit: province-quarter
  geography_level: province
  time_start: 1999
  time_end: 2012
  minimum_frequency: quarterly
  minimum_pre_periods: 25
  minimum_post_periods: 24
  required_fields: [quarterly nominal provincial GDP, corresponding provincial CPI, province identifiers, quarter, statistical vintage, GDP year-on-year growth, donor eligibility and exclusions, Tianjin exposure flag]
  required_identifiers: [province_id, quarter]
  treatment_key: [province_id, quarter]
  treatment_source: Official国发〔2006〕20号 and the inspected paper Section4.1/Table2 GDP clock; donor pool from Section4.1 and footnote15.
  measurement_risks: [CPI versus GDP deflator, quarterly versus cumulative provider series, statistical revisions,2006Q2 transition contamination, package geography versus aggregate outcome, unrestricted negative donor weights]
evidence:
  - id: E1
    source_type: policy-document
    citation: State Council opinion on Binhai development and opening, 国发〔2006〕20号; Dongjiang authority reproduction.
    url: https://www.dongjiang.gov.cn/contents/26/4462.html
    date: '2006-05-26'
    supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, identity.assignment_mechanism, timeline.announcement, timeline.effective, assignment.unit, assignment.rule, assignment.compliance]
    verification_status: verified
    access_level: official-document
    locator: Full official reproduction inspected, metadata/signature and SectionsI–IV. I specifies Binhai territory; III authorizes the reform pilot; IV requires subsequent plans/measures. The2015 page date is not the2006 instrument date. Does not verify the paper's aggregate counterfactual or common implementation of every component.
  - id: E2
    source_type: paper
    citation: 'Du, Zaichao; Ge, Linnan; Li, Bing; Pei, Pei; Zhou, Lei (2025). Special Economic Zone and Local Economic Performance in China: Evidence From Tianjin. The World Economy48(5):1060–1071. DOI10.1111/twec.13669.'
    url: https://doi.org/10.1111/twec.13669
    date: '2025-02-21'
    supports: [assignment.treated, assignment.comparison_pool, assignment.exposure_construction, timeline.local_timing, timeline.anticipation, design.primary_strategy, design.estimation_notes, design.comparison_logic, empirical_requirements.required_fields, design_applications.treatment_encoding, design_applications.data_used, design_applications.year]
    verification_status: reported
    access_level: full-text
    locator: Actual browser-rendered publisher body https://onlinelibrary.wiley.com/doi/full/10.1111/twec.13669 inspected Sections1–4.4, Tables1–10, endnotes7–17 and Data Availability Statement. Table1 signed GDP weights and Table2 quarterly rows inspected as HTML tables, not figure images. Section3/Q2 versus Section4.1/Q3, GDP endpoint and employment province-name discrepancies retained. Figure captions only; no author code or numeric rerun inspected.
design_applications:
  - paper: 'Special Economic Zone and Local Economic Performance in China: Evidence From Tianjin'
    journal: The World Economy
    year: 2025
    doi: 10.1111/twec.13669
    research_question: How does the2006 Binhai national package change Tianjin aggregate economic performance?
    population: Tianjin municipality and outcome-specific selected provincial donors.
    outcome: Year-on-year real provincial GDP growth; monthly investment and quarterly employment/export/import are additional reported outcomes with separate periods and selected donors.
    data_used: [CEIC provincial nominal macroeconomic series, CEIC province CPI]
    treatment_encoding: For served GDP use2000Q1–2006Q2 fitting and2006Q3–2012Q2 evaluation per Section4.1/Table2; not a direct inside-zone firm policy flag.
    comparison: Selected signed-weight provincial counterfactual with intercept; the full eligible pool and exclusions remain visible.
    empirical_design: Preperiod adjusted-R2 donor search and AICC selection followed by fixed-coefficient prediction; not TWFE DID or convex synthetic control.
    assumptions: [stable no-policy prediction relationship, sufficiently unexposed donors, no unmodeled coincident Tianjin shock]
    threats_addressed: [Bohai-neighbour exclusion, similar-policy exclusions, Sichuan earthquake exclusion, reported alternative inclusion of Sichuan Tibet and Xinjiang]
    evidence_refs: [E2]
method_transfer: null
readiness_blockers:
  - Conditional macro GDP use only. State2006Q3 as the Table2 evaluation convention and assess the May2006 transition; recover code before claiming exact replication of the conflicting Section3 onset or extending the reported GDP endpoint.
  - Obtain appropriate quarterly GDP/CPI definitions and vintages, audit cumulative versus single-quarter series, and justify the counterfactual relationship and inference for the new outcome. No public code/data inspection or reproduced coefficient is claimed.
  - Firm eligibility and isolated component effects require separate operative rules and historical territory joins. Monthly investment and other reported applications cannot silently reuse the GDP frequency, donor weights or sample contract.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Binhai was already a developed territory when the2006 national package
authorized further reform. The official instrument defines a narrower area
than Tianjin and requires later implementation measures [E1]. Consequently
this case records a development-package exposure, not creation of an empty
zone or one simultaneous operative change for every benefit.

## What Changed

National authorization changes the regional development environment. The
paper asks about the resulting Tianjin macroeconomic path, not whether each
firm receives a particular benefit [E2, reported claim]. It is distinct from
the later pilot FTZ plant-location mechanism; different macro outcomes here
remain applications of one package rather than extra variation counts.

## Implementation and Assignment

The legal designation concerns Binhai, whereas the paper observes Tianjin
as a province-equivalent unit. Preserve that bridge: an aggregate impact can
contain indirect effects outside the designated territory without making
those firms directly eligible [E1,E2; analytical inference].

For GDP, the recoverable coding follows Section4.1 and Table2: fit through
2006Q2, then evaluate2006Q3–2012Q2. Section3 says the second quarter instead;
the May26 authorization falls within the retained preperiod. A transition
exclusion is therefore a substantive sensitivity, not a cosmetic date fix.
The sentence about cutting at end2012 also differs from the displayed GDP
endpoint. These conflicts prevent claiming code-exact reproduction but do
not erase the explicitly displayed GDP contrast [E2, reported claim].

## Why This Creates Empirical Variation

One region receives the package while selected other provincial economies
provide a predicted no-package path. The procedure estimates an intercept
and unrestricted weights from the preperiod, including a negative Fujian
weight. It must not be described as a convex synthetic control. The served
GDP donor subset is Shanxi, Jilin, Jiangsu, Fujian, Hubei and Hainan; another
outcome needs its own fitted relationship [E2, reported claim].

## Identification Risks

A close preperiod fit is evidence of prediction within that period, not proof
that Tianjin would retain the relationship afterward. Deliberate growth-pole
selection, anticipatory activity, wider spillovers and contemporaneous shocks
can change it. The paper excludes Beijing, Liaoning, Hebei and Shandong for
Bohai links; Chongqing, Zhejiang and Guangdong for similar policies; and
Sichuan for its earthquake, with Tibet and Xinjiang omitted from the displayed
pool [E2, reported claim]. Those exclusions do not certify the retained donors
as unaffected [analytical inference].

The reported GDP R2=0.9871 does not settle selection-aware prediction
uncertainty. Likewise, the employment prose's Guangzhou conflicts with
Table5's Guizhou; do not silently replace one with the other and offer that
application as code-verified. The GDP contract avoids that separate ambiguity.

## Data Requirements

Use historical province identifiers and quarter to join Tianjin with the
documented donor pool. GDP levels must extend back to1999Q1 to construct
the2000Q1 first year-on-year growth observation. The fitted period has25
quarters and the displayed evaluation has24. Retain provider series units,
deflation and revision vintage; establish whether quarterly observations are
single-quarter or cumulative before computing growth [E2; analytical inference].
CEIC access or author-request microfiles need not be public to describe this
variation, but filenames or metadata cannot establish a successful replication.

## Evidence Notes

The actual publisher body, HTML tables and endnotes now resolve the earlier
Abstract-only access limitation of candidate-b8acaf4118fd. New task
task-b75376fd84be supplies provenance; the prior blocked history is preserved.
Official designation, paper aggregate coding and analytical identification
conditions stay separate. No figure image, executable code or numeric result
was independently reproduced. Grounded conditional use is appropriate for
the documented regional GDP exposure, not a blanket endorsement of the paper's
causal estimates or a ready firm-level policy contract.
