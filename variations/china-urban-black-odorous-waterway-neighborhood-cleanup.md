---
schema_version: 2
id: china-urban-black-odorous-waterway-neighborhood-cleanup
name: Urban Black-and-Odorous Waterway Cleanup and Neighborhood Proximity Exposure
aliases: [城市黑臭水体整治, BOW neighborhood cleanup, Black-and-Smelly Water Program]
status: grounded
provenance:
  task_id: task-434d470f72d1
scope:
  country: China
  regions: [Beijing, Chengdu, Nanjing, Shanghai, Shenzhen, Tianjin]
  domains: [urban-economics, housing, neighborhood-development, environmental-economics]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: Mainland urban neighborhoods inherit exposure from proximity to designated waterway segments; the application studies housing and business responses, not agricultural production.
identity:
  instrument: Urban black-and-odorous waterbody remediation under the2015 Water Pollution Action Plan
  authority: State Council; housing and environmental authorities; city governments
  legal_identifiers: [国发〔2015〕17号, 城市黑臭水体整治工作指南2015]
  implementation_regime: Built-up-area inventory, locally organized engineering, assessment and subsequent maintenance; metropolitan2017 target distinct from the broader2020 target.
  assignment_mechanism: Locally designated polluted waterway geometry generates neighborhood proximity exposure; neither the designation nor housing distance was randomized.
  parent: null
  related_variations: []
timeline:
  announcement: '2015-04-16'
  effective: '2015'
  implementation_start: 2016
  implementation_end: null
  local_timing: Legal2017 basic-elimination target is not a common completion date. The inspected author application starts post at January2016 list disclosure; project-specific implementation starts are unobserved.
  anticipation: The public2015 policy and local inventories precede the application clock; examine2015 leads rather than declaring no anticipation.
  last_verified: '2026-10-04'
assignment:
  unit: Designated waterway segment and nearby property location
  treated: Addresses inside the union of one-mile buffers around designated segments
  comparison_pool: Addresses one-to-two miles from any designated segment in the same sample cities
  rule: Use historical designation geometry, not modern water quality or current clean-water status; distance is the paper's exposure definition, not statutory eligibility.
  intensity: Distance and baseline severity; realized cleanup quality is not random dose.
  exemptions: [Outside built-up areas is outside this implementation boundary; later nationwide and rural extensions are not this case.]
  compliance: Official rules require evaluation and maintenance. Formal targets do not establish realized compliance for every segment.
  exposure_construction: Spatially join property geocodes to the designated segment-buffer union and interact near exposure with the disclosed program period. Overlapping buffers do not duplicate properties.
  required_identifiers: [Historical waterbody identifier and segment geometry, Property address/geocode, City and neighborhood code, Transaction date]
  spillovers: Downstream improvements and relocation of economic activity can affect the comparison ring; citywide capitalization is not captured by a local contrast.
research_compatibility:
  outcome_domains: [housing-prices, real-estate-development, local-business]
  affected_populations: [Urban properties and nearby businesses in the six application cities]
  mechanism_channels: [Remediation and riverbank amenities, Residential demand, Endogenous commercial response]
  best_for: [Conditional neighborhood capitalization comparisons with dated site geometry and pre-policy transactions]
  not_good_for: [Pure drinking-water health effects, Randomized chemical-threshold RD, Site-specific engineering completion effects without completion dates]
design:
  claim_type: reduced-form
  affordances: [spatial-exposure, difference-in-differences, event-study]
  candidate_designs: [Near-versus-ring DID, Event study with alternative buffers]
  identifying_variation: Differential proximity within cities before and after the application information clock
  primary_strategy: difference-in-differences
  estimand: Conditional relative capitalization of bundled cleanup exposure, not isolated chemical improvement or total welfare.
  treatment_variable: Near indicator times post disclosure
  comparison_logic: Compare price changes for near addresses against the outer ring, not across randomized municipalities.
  estimation_notes: The author specification uses location and city-time controls and property characteristics; retain the inspected version boundary rather than asserting replication of the final publication.
  assumptions: [Parallel untreated neighborhood trends, Limited anticipation, No correlated neighborhood interventions, Comparable transaction composition, Limited comparison contamination]
  diagnostics: [Pre-period event coefficients, Alternative rings and downstream exclusions, Composition stability, Concurrent redevelopment checks, Parallel-trend sensitivity]
threats:
- type: endogenous designation and redevelopment
  basis: inferred
  condition: Complaints, pollution and local engineering priorities can track neighborhood trajectories; associated amenities are bundled treatment.
  evidence_refs: [E2, E3]
  possible_diagnostics: [Historical inventories, Pre-trends, Dated redevelopment controls]
- type: timing and spillovers
  basis: reported
  condition: Disclosure is not completion; downstream and broader housing-market responses can contaminate controls.
  evidence_refs: [E3]
  possible_diagnostics: [Separate information and completion estimands, Downstream exclusion, Alternative buffers]
- type: transaction composition
  basis: reported
  condition: Repeated cross-sections do not have a stable apartment repeat-sales identifier.
  evidence_refs: [E3]
  possible_diagnostics: [Property-characteristic balance over time, Stable agency coverage, Neighborhood reweighting]
empirical_requirements:
  contract_version: 1
  population: Pre-owned housing transactions near historical designated urban segments
  observation_unit: Property transaction
  geography_level: Geocoded address and waterway segment within city
  time_start: 2012
  time_end: 2020
  minimum_frequency: Dated transactions with at least annual estimation bins
  minimum_pre_periods: 3
  minimum_post_periods: 2
  required_fields: [Transaction price, Transaction date, Property characteristics, Distance to designated segment, Historical designation, City/neighborhood, Program period]
  required_identifiers: [Property geocode, Historical waterbody identifier and geometry, City/neighborhood code]
  treatment_key: [Historical waterbody identifier, Segment geometry, Disclosure period]
  treatment_source: Dated official inventories and IPE historical segment information; reconcile geometry before spatial joining.
  measurement_risks: [Coordinate-system mismatch, Current versus historical geometry, Incomplete agency coverage, Selection of transacted properties]
design_profiles: []
evidence:
- id: E1
  source_type: policy-document
  citation: State Council Water Pollution Action Plan2015
  url: https://www.ndrc.gov.cn/xxgk/zcfb/qt/201504/t20150416_967871.html
  date: '2015-04-16'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.announcement, timeline.local_timing, assignment.unit, assignment.rule]
  verification_status: verified
  access_level: official-document
  locator: Header signature/publication distinction and VIII(27), inspected4 October2026; inventories/disclosure, municipal/provincial-capital/separately-planned-city built-up-area2017 target versus broader2020 target. No ranked economic selection or realized completion certified.
- id: E2
  source_type: implementation-document
  citation: Cities' Black-and-Odorous Waterbody Remediation Work Guide2015, official Wuhan Water Bureau reproduction
  url: https://swj.wuhan.gov.cn/szy/202004/P020200506380692667954.pdf
  date: '2015'
  supports: [identity.assignment_mechanism, assignment.rule, assignment.compliance, assignment.exemptions, identity.implementation_regime, timeline.local_timing]
  verification_status: verified
  access_level: official-document
  locator: Printed pp2-7 Sections1.2-1.5,2.2-2.4; pp21-23 Sections5.1-5.3. Identification uses preassessment/public input; chemical grading includes shallow-water adjustment and contiguous-point rules. Acceptance combines public assessment, monitoring and implementation records.2015 guide, not2020 upload-date implementation.
- id: E3
  source_type: paper
  citation: Yue Yu and Qianyang Zhang, The Value of Cleaner Waterways, February1,2025 author manuscript with appendix
  url: https://drive.google.com/file/d/1ht0UmrpIT4guvSTpTC7il87U9fJhbIw7/view
  date: '2025-02-01'
  supports: [assignment.treated, assignment.comparison_pool, assignment.exposure_construction, timeline.local_timing, design.primary_strategy, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.required_fields, empirical_requirements.required_identifiers, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison]
  verification_status: reported
  access_level: full-text
  locator: Author link from ABFER draft first page; public Drive download read in memory.58pages, printed pp7-16 Sections2-4, Eq1-2 footnotes12,31-35; pp43-45 AppendixA.1-A.3. This is not the final typeset JEEM article or executed code.
- id: E4
  source_type: other
  citation: Qianyang Zhang author publication page and JEEM bibliographic identity
  url: https://doi.org/10.1016/j.jeem.2025.103159
  date: '2025'
  supports: [design_applications.paper, design_applications.journal, design_applications.doi, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: Author publications entry linked to DOI; direct Crossref publisher-deposited metadata inspected4 October2026 for title/authors/journal/volume/publication. JEEM132 June2025; title variants are the same paper, not separate shocks.
design_applications:
- paper: The value of cleaner waterways - Evidence from the Black-and-Odorous water program
  doi: 10.1016/j.jeem.2025.103159
  journal: Journal of Environmental Economics and Management
  year: 2025
  research_question: Local housing capitalization and neighborhood business response
  population: Six mainland cities;292 segments in February2025 author version
  outcome: Housing prices and development; business locations
  data_used: [Brokerage transaction compilation2012-2020, Historical IPE waterway information, CREIS2010-2020, Gaode2015/2019 snapshots]
  treatment_encoding: One-mile buffer union times post January2016; neither actual completion nor a randomized chemical cutoff
  comparison: One-to-two-mile ring; distance-bin diagnostics use a different reference area
  empirical_design: DID, urban-neighborhood and city-year effects, property controls, double clustering at neighborhood and city-year
  assumptions: [Parallel trends, Limited anticipation, Stable composition, No differential concurrent changes]
  threats_addressed: [Event study, Alternative buffers, Downstream exclusions, More granular location-time controls, Parallel-trend sensitivity]
  evidence_refs: [E1, E2, E3, E4]
method_transfer: null
readiness_blockers:
- Recover the exact dated292-segment inventory, original geometry, coordinate reference and geocoding procedure for application; no raw-data or code replication was inspected.
- Reconcile February2025 author methods against final article/appendix before claiming exact replication; do not substitute the March2023 draft's304 segments.
- Audit local public disclosure and concurrent redevelopment for a new outcome; January2016 is the author information clock, not universally verified site disclosure or completion.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

The2015 action plan made urban black-and-odorous-waterbody remediation a
local-government obligation. Its accelerated target follows administrative
city categories, not a ranking of the richest36 cities [E1]. Engineering,
evaluation and continuing maintenance constitute one implementation regime;
later rural extensions are outside this case.

## What Changed

Previously polluted urban waterways became designated remediation projects,
with local engineering and assessment obligations [E1; E2]. Announcement is
not proof of completion. The recorded contrast follows addresses near those
historical segments rather than treating an entire city as equally exposed.

## Implementation and Assignment

Use the historical designated segment as the institutional anchor. Official
identification includes preassessment and public input; chemical measurements
also grade severity, and shallow-water and contiguous-point provisions matter
[E2]. Rebuilding a list from four simple cutoffs would not faithfully recreate
the institution. A research distance buffer is another layer: it maps designated
segments to addresses, rather than deciding which segments government treats.

## Why This Creates Empirical Variation

The author's2025 application compares nearer and outer-ring addresses after
disclosure, preserving overlapping buffers as a union [E3, reported claim].
It measures relative exposure to a cleanup package, including riverbank
amenities. Distinct business and housing outcomes do not warrant separate
canonical cases. A local contrast is not proof of an overall welfare gain
[analytical inference].

## Identification Risks

Disclosure, engineering and assessment are different clocks. A price response
to expected amenities can precede physical completion. Pollution selection,
redevelopment, sorting and downstream benefits can generate differential trends
or contaminate controls; diagnostics inform these assumptions rather than
proving that the policy is intrinsically exogenous [E2; E3; analytical inference].

## Data Requirements

Join dated designation geometry to property locations using a reconciled
coordinate system, then connect transaction time, characteristics and stable
neighborhood identifiers. This is a repeated-cross-section contract, not a
requirement for unavailable repeat-sales IDs. Dataset acquisition belongs in
the companion data catalog via the DOI.

## Evidence Notes

The institutional mechanism and author-used comparison are grounded; this is
a conditional research candidate, not a reproduced final-paper design. E2's
official contiguous severe-point rule differs from E3's simplified appendix
description. Retain the actual designated roster instead of silently choosing
one reconstruction. Neither source verifies universal site compliance.
