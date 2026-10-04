---
schema_version: 2
id: china-industrial-land-minimum-investment-intensity
name: China Industrial Land Minimum Investment Intensity
aliases:
- Industrial land fixed-investment density requirement
- China MII land regulation
- 工业用地投资强度下限
status: grounded
provenance:
  task_id: task-1be84f6d483d
scope:
  country: China
  regions:
  - Mainland China under the 2008 national industrial-project land-use controls
  domains: [regional-economics, urban-economics, industrial-organization, development-economics]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    Chinese industrial projects face location-and-industry-specific minimum
    investment per land area. The recorded institutional core is the 2008 national
    regime; the research application studies additional local tightening rather
    than assuming a single uniform national treatment.
identity:
  instrument: Minimum fixed-asset investment per unit of industrial-project land under the 2008 land-use control indicators
  authority: Ministry of Land and Resources with provincial and local land authorities
  legal_identifiers:
  - 国土资发〔2008〕24号, issued and effective 2008-01-31
  - Predecessor trial indicators 国土资发〔2004〕232号, superseded by the 2008 notice
  implementation_regime: >
    Land-supply approval and contracts attach investment-density conditions, with
    completion acceptance and contractual liability. Local standards can supplement
    the national controls. This record does not establish the paper's entire local
    schedule or treat every local government as adopting on the national date.
  assignment_mechanism: >
    Project location determines its land-grade category, and industry determines
    its applicable investment requirement. Assignment depends on the standard in
    force when the project is accepted and contracted, including applicable local
    requirements, not simply the firm's year of observation.
  parent: null
  related_variations: []
timeline:
  announcement: '2008-01-31'
  effective: '2008-01-31'
  implementation_start: 2008
  implementation_end: 2023
  local_timing: >
    These dates bound the 2008 national regime, not the first introduction of MII
    or all local changes. The 2023 replacement changes investment intensity into
    a nationally recommended indicator with local control values; already accepted
    projects retain their acceptance-time requirements. [E5, verified] Yunnan's
    forwarding notice states that the revised land grades under
    国土资发〔2008〕308号 apply to both investment controls and minimum land prices
    from 2009-01-01. Its tables and the national revision were not inspected.
  anticipation: Local announcement, negotiation and project acceptance can precede purchase or observed production; align these clocks before an event study.
  last_verified: '2026-10-04'
assignment:
  unit: Industrial project or parcel, connected to firm-year observations
  treated: New industrial projects subject to a binding investment-density requirement; locally tightened projects require separate historical coding
  comparison_pool: >
    The paper compares higher and lower requirements, including neighbouring
    jurisdictions and industries unaffected by local tightening. Legal eligibility
    alone does not establish comparable firms.
  rule: >
    Join historical project location to land grade and GB/T4754-2002 industry,
    then recover the applicable national and local contract requirements. The
    statutory investment numerator includes buildings, equipment and land payments;
    it is not a minimum price paid for land.
  intensity: Applicable required fixed-asset investment per land area, with historical units retained
  exemptions:
  - Under the 2008 document, renovation and expansion projects may refer to the standards rather than automatically having identical new-project treatment.
  - Reasoned and approved exceptional projects can depart from controls; preserve their approval status.
  compliance: Contractual acceptance requirements are not evidence that every firm met or was inspected under the same threshold.
  exposure_construction: >
    Recover a versioned location-industry standard at project acceptance or contract
    time; connect parcels to firms without confusing repeated firm-years with new
    policy assignments. Retain national, provincial and municipal components
    separately until the applicable legal hierarchy is documented. [E1, verified]
    Table 1 supplies seven location classes: grades 1-4, 5-6, 7-8, 9-10,
    11-12, 13-14 and 15. Requirements are in ten-thousand yuan per hectare;
    industry 40 ranges from 4400 in class 1 to 440 in class 7. Annex 2 gives
    historical place names, not numeric county codes. [E5, verified] Do not carry
    that original grade roster unchanged beyond the 2009 revision or substitute
    a current geography classification for the project's historical rule.
  required_identifiers: [Historical county code, Industry code and classification version, Project acceptance or contract date, Parcel and purchaser identifiers, Stable firm identifier and year]
  spillovers: Firms may choose the other side of a border or alter parcel size and capital mix; sorting can itself respond to tightening.
research_compatibility:
  outcome_domains: [Industrial land allocation, Capital-land mix, Firm productivity, Manufacturing location]
  affected_populations: [Industrial entrants, Relocating manufacturers, Land-supplying local governments]
  mechanism_channels: [Constrained input substitution, Project admission, Location selection]
  best_for:
  - Assessing whether spatially differentiated investment requirements constrain industrial land use
  not_good_for:
  - Calling cross-sectional land grades random or treating all post-2008 firms as equally treated
  - Substituting minimum industrial land prices or development-zone designation for MII
design:
  claim_type: reduced-form
  affordances: [Location-industry thresholds, Local changes over time, Administrative-border comparisons]
  candidate_designs: [Local-change panel comparisons, Border comparisons within industry]
  identifying_variation: The paper exploits local changes and border differences in MII requirements; these contrasts still require a defensible counterfactual.
  primary_strategy: >
    Relate requirements to the gap between estimated marginal land productivity
    and land user cost, with local-change and border specifications. This is not
    an instrument that establishes exogeneity merely because its inputs are legal.
  estimand: Conditional relationship between required investment density and estimated industrial land misallocation in the observed manufacturing sample
  treatment_variable: Applicable MII requirement, distinguished from realised capital-to-land ratio
  comparison_logic: Compare exposure contrasts within the relevant local, industry, time and border structure; do not compare selected entrants to all incumbent firms without adjustment.
  estimation_notes: >
    Preserve each paper specification and its clustering when reconstructing the
    design. The computed productivity gap depends on production-function and
    user-cost assumptions, not only the policy coding.
  assumptions:
  - Local tightening is not wholly explained by unobserved changes in land scarcity or industrial composition.
  - Border-side sorting and other policy discontinuities do not account for the comparison.
  - Estimated production inputs and annualised land cost measure the intended quantities.
  diagnostics: [Local pre-trends where observed, Unaffected-industry comparisons, Border balance and sorting, Alternative land-cost and production-function assumptions]
threats:
- type: Measurement definition
  basis: documented
  condition: The legal investment numerator includes land payments; a machinery-and-building capital measure is not automatically the same regulated quantity.
  evidence_refs: [E1]
  possible_diagnostics: [Reconcile legal numerator to paper code before interpreting bindingness]
- type: Endogenous location and policy choice
  basis: inferred
  condition: Governments can tighten in response to scarcity and firms can sort across jurisdictions; geographic exposure is not random assignment.
  evidence_refs: [E1, E2]
  possible_diagnostics: [Compare border-side composition and concurrent policies, Examine announcement-time entry and parcel size]
- type: Bundled local instruments
  basis: documented
  condition: A local notice can jointly alter project admission, investment, output and pricing; isolate the encoded measure rather than naming the bundle MII alone.
  evidence_refs: [E3]
  possible_diagnostics: [Construct a local instrument chronology, Separate controls and enforcement changes]
- type: Historical land-grade revision
  basis: documented
  condition: '[E5, verified] The 2009 change applies revised grades to investment controls as well as minimum land prices. A fixed original grade map can miscode exposure; the forwarding text does not recover every revised numeric grade or prove the paper used that map.'
  evidence_refs: [E1, E5]
  possible_diagnostics: [Recover the revision and jurisdiction tables, Align rule versions with project dates and historical county codes]
empirical_requirements:
  contract_version: 1
  population: Newly established or relocating Chinese manufacturers with linkable industrial parcels
  observation_unit: Firm-year with project-level policy exposure
  geography_level: Historical county and relevant administrative border
  time_start: 2007
  time_end: 2014
  minimum_frequency: Annual firm observations plus dated project contracts
  minimum_pre_periods: 0
  minimum_post_periods: 1
  required_fields: [Applicable MII requirement, Parcel area, Fixed investment components, Output and factor inputs, Land price and user-cost construction]
  required_identifiers: [Firm identifier, Parcel purchaser and contract identifier, County code, Two-digit industry, Year, Border-pair identifier where used]
  treatment_key: [Historical location, Industry, Applicable rule version, Project acceptance or contract date]
  treatment_source: National Table 1 and Annex 2 reproduced in E1, subsequent grade revisions including E5, plus exact local schedules and project contracts; the original national table alone cannot supply the paper's full local exposure panel
  measurement_risks:
  - Zero minimum pre-periods describes a level or border comparison, not permission to run an event study without pre-treatment outcomes.
  - Administrative mergers and industry recoding can create spurious threshold changes.
  - Keep hectares, mu and square metres explicit when joining policy and parcel data.
evidence:
- id: E1
  source_type: policy-document
  citation: Ministry of Land and Resources. 2008. Industrial Project Construction Land Control Indicators, 国土资发〔2008〕24号; full reproduction in the Ministry of Commerce legal database, credited there to Pkulaw.
  url: https://policy.mofcom.gov.cn/claw/clawContent.shtml?id=4038
  date: '2008-01-31'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, identity.assignment_mechanism, timeline.announcement, timeline.effective, timeline.implementation_start, assignment.rule, assignment.exemptions, assignment.compliance, assignment.exposure_construction, empirical_requirements.treatment_source]
  verification_status: verified
  access_level: official-document
  locator: Notice paragraphs 1-3 and supersession sentence; indicators II, III, VI and VII; application notes I and II(1); Annex 2 land grades and Table 1 including headers, units and industry 40 row inspected 2026-10-04. Original numeric table is accessible HTML, not the paper's full local schedule or a verified county-code crosswalk.
- id: E2
  source_type: paper
  citation: 'Zhao, Aidong, Huub Ploegmakers, Jan Rouwendal, and Xianlei Ma. 2025. Land investment regulation and allocative efficiency: evidence from the Chinese manufacturing sector. Journal of Economic Geography 25(2):151-174. Online publication 2024-08-01. DOI 10.1093/jeg/lbae024.'
  url: https://doi.org/10.1093/jeg/lbae024
  date: 2025
  supports: [scope.china_relevance, assignment.comparison_pool, design.identifying_variation, design.primary_strategy, design.estimand, empirical_requirements.time_start, empirical_requirements.time_end, design_applications.data_used, design_applications.treatment_encoding, design_applications.empirical_design]
  verification_status: verified
  access_level: full-text
  locator: Publisher open-access HTML at https://academic.oup.com/joeg/article/25/2/151/7725676 inspected 2026-09-28; sections 2, 5 and 7, local-change Table 1 and regression Table 6. Later fetch attempts intermittently failed; no replication package was inspected.
- id: E3
  source_type: implementation-document
  citation: Wuxi Municipal Government. Further Promoting Economical and Intensive Land Use to Promote Industrial Transformation and Upgrading; signed 2011-10-27, page published 2012-01-04.
  url: https://www.wuxi.gov.cn/doc/2012/01/04/4178774.shtml
  date: '2011-10-27'
  supports: [threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Section III(4)-(5) combines investment-density admission, output, pricing and acceptance requirements. Contextual evidence of bundled implementation; not a claimed paper treatment event or a substitute for Jiangsu's 2010 schedule.
- id: E4
  source_type: policy-document
  citation: Ministry of Natural Resources. 2023. Notice issuing revised Industrial Project Construction Land Control Indicators, signed 2023-05-11; State Council republication dated 2023-06-26.
  url: https://app.www.gov.cn/govdata/gov/202306/26/504692/article.html
  date: '2023-05-11'
  supports: [timeline.implementation_end, timeline.local_timing]
  verification_status: verified
  access_level: official-document
  locator: Sections I-II distinguish recommended investment intensity and preserve acceptance-time standards; final paragraph repeals 国土资发〔2008〕24号 from publication. Signature is 2023-05-11 and this republication is 2023-06-26; exact original publication day is not verified, so the record bounds the ending only to 2023.
- id: E5
  source_type: implementation-document
  citation: Yunnan Provincial Land and Resources Department. Forwarding the Ministry's documents adjusting land grades; official historical reproduction on the Yunnan Natural Resources Department website.
  url: https://dnr.yn.gov.cn/html/2009/dijiaxinxi_0323/57.html
  date: '2009-03-23'
  supports: [timeline.local_timing, assignment.exposure_construction, empirical_requirements.treatment_source, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Full forwarding text inspected 2026-10-04, especially the sentence specifying 2009-01-01 application to both investment controls and minimum land prices. URL dates the webpage; displayed publication-date field is blank, and the local signature date is not verified. National notice is explicitly omitted; linked DOC tables were not inspected.
design_applications:
- paper: 'Land investment regulation and allocative efficiency: evidence from the Chinese manufacturing sector'
  doi: 10.1093/jeg/lbae024
  journal: Journal of Economic Geography
  year: 2025
  research_question: Do minimum investment requirements distort industrial land allocation?
  population: 20,205 newly established or relocating manufacturing firms, 2007-2014
  outcome: Estimated marginal land productivity minus land user cost
  data_used: [Industrial land lease records linked to the annual manufacturing survey]
  treatment_encoding: County-industry MII requirements and local increases
  comparison: Lower-requirement and neighbouring jurisdictions; industries unaffected by local increases
  empirical_design: Production-function construction followed by local-change and border regressions
  assumptions: [Comparable conditional counterfactuals, Credible production-function and land-cost measurement]
  threats_addressed: [Border specifications, Unaffected-industry checks]
  evidence_refs: [E2]
method_transfer: null
readiness_blockers:
- Original national numeric Table 1 and historical Annex 2 are now inspected; recover subsequent grade revisions, a historical county-code crosswalk and full local county-industry-time schedules before constructing the paper's treatment panel.
- Reconcile the statutory fixed-investment numerator, which includes land payments, with the paper's analytical capital definition and replication code.
- Recover parcel-to-survey matching rules, duplicate handling, sample filters and production-function code; no replication package or private microdata access was verified.
---

## Institutional Background

[E1, verified] This is an industrial-project development condition, not the price
floor for buying industrial land. Its research relevance is that a required input
mix can constrain a firm's choice of land even where land is auctioned.

## What Changed

The 2008 national notice revised an earlier regime. [E2, verified paper report]
Local tightening supplies the research application's contrasts. Neither statement
makes the nationwide revision a uniform binary shock. [E4, verified] The 2023
replacement also prevents extending the historical regime unchanged to today.

## Implementation and Assignment

Treat rule versions as project-level conditions. A firm's survey year does not
establish which condition governed its parcel. The original blocked candidate
`candidate-4b19c33aad81` remains a historical account of the earlier unresolved
local-schedule investigation; this record does not silently resolve that gap.

## Why This Creates Empirical Variation

Location, industry and local rule changes create observable exposure differences.
Whether those differences support causal interpretation depends on policy choice,
firm selection and the counterfactual, rather than on the existence of a statute.

## Identification Risks

Do not translate statutory intensity directly into a firm's realised capital-land
ratio. [E1] The legal numerator includes land payments. The analytical capital
measure and compliance proxy need an explicit reconciliation. [E3] Wuxi illustrates
why a local land-policy bundle cannot automatically be coded as MII alone; its
notice is contextual, not newly established paper-used variation.

## Data Requirements

Before empirical reuse, obtain historical rule schedules and a reproducible
project-to-firm join. A DOI link can lead to the complementary data repository;
this record does not duplicate data-asset documentation or promise access.

## Evidence Notes

The core legal mechanism and research use are inspected, supporting grounded
status. Exact exposure reconstruction remains conditional, as the blockers make
explicit. No primary local timetable or executable reproduction is claimed.
