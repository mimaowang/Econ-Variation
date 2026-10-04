---
schema_version: 2
id: china-minimum-wage-county-border-new-business-entry
name: County-Border Minimum-Wage Differentials and New Business Entry in China
aliases:
- Li Shi Zhou minimum wage border design
- China county minimum wage new firm entry
- minimum wage spatial border approach China
status: grounded
provenance:
  task_id: task-e6f648e1ff1b
scope:
  country: China
  regions:
  - Adjacent county-level units within the same Chinese prefecture
  - 317 prefecture-level areas represented in the 1997-2012 research sample
  domains:
  - regional-economics
  - urban-economics
  - labor-economics
  - firm-dynamics
  - spatial-economics
  variation_type: boundary-discontinuity
  knowledge_role: china-variation
  china_relevance: >
    This record captures a paper-used local design built from statutory minimum-wage
    differences across contiguous Chinese county-level units. It is not a generic
    national minimum-wage indicator: exposure is assigned to geocoded new business
    registrations close to a same-prefecture county border, with the opposite side
    of that border supplying the local comparison.
identity:
  instrument: >
    County- and district-level statutory minimum-wage schedules operating under
    China's Labor Law and the 2004 Minimum Wage Regulations. The empirical object is
    the cross-border difference in the schedule faced by adjacent county-level units,
    not a single nationwide wage reform.
  authority: >
    The national labor-law framework and Ministry of Labor and Social Security rules
    set the determination and enforcement framework; provincial labor authorities
    established several wage tiers, and county-level administrations selected or
    applied local levels within that framework. The paper reports that local
    adjustment dates and levels differed across counties.
  legal_identifiers:
  - Labor Law of the People's Republic of China, passed 1994-07-05 and effective 1995-01-01
  - Minimum Wage Regulations, Ministry of Labor and Social Security Order No. 21, issued 2004-01-20 and effective 2004-03-01
  - Province- and county-level minimum-wage adjustment notices used to construct local schedules
  implementation_regime: >
    Provinces commonly set several minimum-wage tiers and permitted counties,
    county-level cities, and municipal districts to choose levels according to local
    conditions. Adjustment dates were not synchronized. The 2023 application keeps
    only contiguous county pairs in the same prefecture, requires a wage schedule for
    both sides, and restricts registration observations to narrow GIS bands.
  assignment_mechanism: >
    For each eligible border pair and year, a county side receives the higher or lower
    statutory minimum wage recorded for that locality. The paper's primary exposure is
    the cross-border wage difference, assigned to new registrations geocoded within one
    kilometre of the shared border; it also uses industry wage and skill exposure and
    a shareholder-link rule to examine relocation.
  parent: null
  related_variations:
  - china-minimum-wage-firm-competitive-shocks
timeline:
  announcement: null
  effective: null
  implementation_start: 1997
  implementation_end: 2012
  local_timing: >
    The legal system predates the sample, while county schedules changed at different
    local dates. The paper's main panel is annual from 1997 through 2012; a downstream
    replication must recover each local schedule's effective date rather than assign a
    common national start.
  anticipation: >
    Local wage notices could be published before the effective date, and employers may
    anticipate routine adjustments. The paper's annual schedule does not by itself
    identify the day of announcement, so short-window event timing is not implied.
  last_verified: '2026-08-13'
assignment:
  unit: County-border side-year, with new business registrations as the outcome unit
  treated: >
    The side of a contiguous same-prefecture county border with the higher statutory
    minimum wage in a given year, measured through the local wage differential rather
    than a binary national reform indicator.
  comparison_pool: >
    The opposite side of the same county border in the same year, within the matched
    border-pair sample; broader-band and county-total estimates are secondary checks,
    not interchangeable comparisons.
  rule: >
    Keep adjacent county-level units in one prefecture, require both sides to have a
    wage schedule and business entries, geocode registrations, and compare observations
    inside the corresponding one-kilometre bands on each side of the border.
  intensity: >
    Continuous cross-border minimum-wage difference, usually expressed as a log wage
    gap; the reported baseline interprets a 10 percent increase in the local wage as a
    2.69 percent change in new entries.
  exemptions:
  - Counties without a complete schedule for the sample window or without an observed entry are excluded from the baseline pair panel.
  - Registrations outside the selected narrow border band are not part of the local-border estimand.
  - Informal activity and businesses absent from the registration system are not observed.
  compliance: >
    The treatment is the statutory schedule, not verified payment by each employer.
    The paper studies formal registrations and reports robustness and relocation checks,
    but neither the regulation nor the registration data proves uniform compliance.
  exposure_construction: >
    Join each geocoded registration to its county and incorporation year, assign the
    county's statutory wage, and retain the one-kilometre side of a contiguous
    same-prefecture border. Construct the pair-year wage gap and, where needed, an
    industry exposure measure from low-salary or low-skill shares. Define a possible
    relocation entry using a shareholder who also owns a pre-existing establishment on
    the other side.
  required_identifiers:
  - Business registration identifier and incorporation date
  - County or district code and historical county-border polygon/version
  - Same-prefecture border-pair identifier and signed distance to the border
  - Local minimum-wage schedule, effective date, and wage tier
  - One-digit industry code and shareholder identifiers when testing relocation
  spillovers: >
    Workers, customers, and firms may cross the border; new registrations may relocate
    rather than represent new productive activity; neighboring local policies can move
    together. Treat the border estimate as a local equilibrium response and report the
    shareholder-link proxy's limits.
research_compatibility:
  outcome_domains:
  - business entry and entrepreneurship
  - firm location
  - formalization
  - employment and wages
  - industrial composition
  - local economic activity
  affected_populations:
  - Newly registered Chinese businesses
  - Low-salary and low-skill industries
  - Workers and firms near county borders
  - Local governments setting or applying wage tiers
  mechanism_channels:
  - labor-cost and entry-margin channel
  - industry selection by wage exposure
  - local relocation and border sorting
  - formal-registration channel
  best_for:
  - Estimating a narrow local response of new formal business entry to statutory wage differences
  - Comparing entry responses by low-wage or low-skill industry exposure
  - Studying whether apparent entry changes reflect relocation across nearby county borders
  not_good_for:
  - Treating the national minimum-wage system as randomly assigned
  - Measuring informal businesses missing from registration records
  - Inferring long-run aggregate employment or welfare from the one-kilometre border sample
  - Replacing the broad firm-level competitive-shock design in the related 2020 record
design:
  claim_type: causal
  affordances:
  - Same-prefecture adjacent counties provide a geographically local comparison
  - One-kilometre bands limit differences in local amenities and trends, subject to continuity assumptions
  - Continuous wage gaps support intensity and industry-exposure heterogeneity
  - Shareholder links permit a direct, though incomplete, relocation diagnostic
  candidate_designs:
  - Spatial difference-in-differences or border-pair regression with county-pair and year fixed effects
  - Industry-by-border design contrasting low-salary or low-skill exposure
  - Wider-band and county-total estimates as diagnostics for local comparability and policy endogeneity
  identifying_variation: >
    Identification comes from year-to-year and cross-side differences in statutory
    minimum wages between contiguous counties in the same prefecture, applied to
    registrations within one kilometre of the shared border. The local comparison is
    informative only if time-varying shocks do not change discontinuously across the
    border in ways correlated with the wage gap.
  primary_strategy: >
    The paper's baseline compares new-entry counts on the two sides of the same border
    in a 1-km band, using pair and year fixed effects and controls for cross-border
    differences in pre-existing establishments. It reports wider bands and a county-total
    specification as diagnostic contrasts; the latter should not be treated as the same
    local design.
  estimand: >
    The local effect of a statutory cross-border minimum-wage differential on the number
    of newly registered businesses near the border during 1997-2012, with heterogeneity
    by industry wage or skill exposure. This is not an estimate of the national effect
    of every minimum-wage adjustment.
  treatment_variable: >
    Pair-year log minimum-wage difference, assigned to the county side and geocoded
    1-km border-band registration count; secondary specifications use industry exposure
    to low salaries or low skills.
  comparison_logic: >
    Compare the higher-wage and lower-wage sides of the same contiguous county pair in
    the same year, holding pair-specific geography fixed. Use broader bands, artificial
    contrasts, and county-total results only to test whether the narrow comparison is
    behaving as expected.
  estimation_notes: >
    The paper reports a baseline coefficient of -0.269, implying a 2.69 percent decline
    in entries for a 10 percent wage increase. Wider 2-, 3-, and 4-km bands attenuate
    the estimate, while the positive county-total coefficient is consistent with local
    wage setting responding to economic conditions. Preserve these as reported results,
    not as a guarantee for new data.
  assumptions:
  - Local economic and policy shocks are sufficiently smooth across the narrow border after pair and year controls.
  - The recorded statutory wage is measured with the correct county, tier, and effective date.
  - The two sides have comparable registration coverage and geocoding near the border.
  - Industry exposure measures are not themselves generated by the post-treatment entry response.
  - Shareholder links capture enough relocation to interpret the mobility diagnostic without treating it as a complete census.
  diagnostics:
  - Pre-period entry trends and border-side balance
  - 1-km versus 2-, 3-, and 4-km bands
  - County-total estimate as an endogeneity warning, not a preferred specification
  - Low-salary and low-skill industry heterogeneity
  - Shareholder-link relocation counts and coefficients
  - Separate pre-2004 and post-2004 policy-period estimates
threats:
- type: endogenous-local-wage-setting
  basis: documented
  condition: >
    Counties may adjust minimum wages in response to local growth, labor demand, or
    fiscal conditions that also change business entry. The paper's positive county-total
    estimate is a warning that a broad comparison can be confounded.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Pair and year fixed effects with pre-existing-establishment controls
  - Narrow-band estimates and pre-trend tests
  - County-total result reported only as a contrast
  - Excluding high-growth or policy-intensive pairs
- type: border-continuity-and-concurrent-policy
  basis: inferred
  condition: >
    A county boundary can coincide with different infrastructure, zoning, tax, or
    enforcement changes. Narrow distance reduces but does not remove discontinuous local
    interventions or sorting at the line.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Boundary-side balance and placebo outcomes
  - Inventory of local policies and infrastructure by pair-year
  - Alternative bands and leave-one-border-out estimates
- type: schedule-and-boundary-measurement
  basis: reported
  condition: >
    County reorganizations, historical polygons, tier changes, and effective dates can
    misassign a registration to a wage schedule or border side.
  evidence_refs:
  - E1
  - E3
  possible_diagnostics:
  - Archive every local wage notice and effective date
  - Version historical county crosswalks and GIS polygons
  - Re-run with incorporation date and alternative schedule clocks
- type: relocation-and-spillover
  basis: reported
  condition: >
    Fewer registrations on the high-wage side may reflect movement across the nearby
    border rather than destruction of entry. Shareholder links observe only a subset of
    such moves and can also capture owner expansion.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Shareholder-linked relocation measure
  - Entry and exit flows on both sides
  - Wider spatial rings and incumbent-firm outcomes
- type: registration-coverage-and-composition
  basis: inferred
  condition: >
    NECIPS records formal registrations and may change coverage or geocoding quality over
    time; industry mix and unregistered activity can therefore change independently of
    the statutory wage.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Coverage and missing-address audits
  - Industry-specific entry counts and capital thresholds
  - Cross-checks against official business-registration totals
empirical_requirements:
  contract_version: 1
  population: New formal business registrations in Chinese county-level units, 1997-2012
  observation_unit: County-border-side-year, with business-entry microdata for geospatial filtering
  geography_level: Historical county or district border and same-prefecture border pair
  time_start: 1997
  time_end: 2012
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields:
  - Registration ID and incorporation date
  - Geocoded address or latitude and longitude
  - Historical county or district code and border-pair membership
  - Statutory minimum wage, wage tier, and effective date
  - One-digit industry code
  - Shareholder identifiers and linked prior establishments for relocation analysis
  - Counts of pre-existing establishments by broad industry and county side
  required_identifiers:
  - registration_id
  - county_code_versioned
  - prefecture_code
  - border_pair_id
  - incorporation_date
  - min_wage_schedule_id
  - shareholder_id where available
  treatment_key:
  - county-pair-year log minimum-wage difference
  - county-side indicator within the 1-km border band
  treatment_source: >
    Archived provincial and county minimum-wage notices linked to historical county
    boundaries; business entries and shareholder fields from the National Enterprise
    Credit Information Publicity System or an equivalent auditable source.
  measurement_risks:
  - Local notices may state announcement and effective dates separately
  - County reorganizations can break historical codes and border polygons
  - Address geocoding may place an entry on the wrong side or outside the true band
  - Registration coverage excludes informal activity and may change across years
  - Shareholder links do not identify every relocation or productive activity shift
evidence:
- id: E1
  source_type: policy-document
  citation: Ministry of Labor and Social Security. 2004-01-20. Minimum Wage Regulations, Order No. 21.
  url: https://www.mohrss.gov.cn/xxgk2020/gzk/gz/202112/t20211228_431587.html?eqid=969b02cd00006c970000000264675adc
  date: '2004-01-20'
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - assignment.rule
  - assignment.compliance
  - timeline.implementation_start
  verification_status: verified
  access_level: official-document
  locator: >
    The official Ministry page identifies Order No. 21, its 2004-03-01 effective date,
    covered employers, provincial determination procedure, adjustment requirements,
    and enforcement provisions. It establishes the legal framework, not the paper's
    complete county schedule or border sample.
- id: E2
  source_type: policy-document
  citation: National Health Commission. 1994-07-05. Labor Law of the People's Republic of China.
  url: https://www.nhc.gov.cn/zwgk/falv/201304/01b30f4945da4088a44c0c0cc0507751.shtml
  date: '1994-07-05'
  supports:
  - identity.legal_identifiers
  - identity.authority
  - timeline.implementation_start
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: >
    The official text records passage on 1994-07-05, effectiveness on 1995-01-01,
    and the statutory minimum-wage provision. It establishes the national legal basis,
    not local compliance or the empirical border coding.
- id: E3
  source_type: paper
  citation: 'Li, Shi, and Zhou. 2023. "The Minimum Wage and the Locations of New Business Entries in China: Estimates Based on a Refined Border Approach." Regional Science and Urban Economics 99:103876. DOI: 10.1016/j.regsciurbeco.2023.103876.'
  url: https://faculty.xmu.edu.cn/_resources/group1/M00/00/04/rBtL9GWeTVCATNsdABbXXMHBQNk823.pdf
  date: 2023
  supports:
  - identity.implementation_regime
  - identity.assignment_mechanism
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
  locator: >
    Author-hosted full text: abstract; institutional background; minimum-wage schedule
    discussion; data and sample construction; spatial-difference empirical strategy;
    baseline and wider-band tables; industry heterogeneity; policy-period split; and
    shareholder-link relocation section. It establishes the paper's application and
    reported estimates, not independent verification of every local notice.
- id: E4
  source_type: paper
  citation: DOI metadata for Li, Shi, and Zhou, Regional Science and Urban Economics 99 (2023), article 103876.
  url: https://doi.org/10.1016/j.regsciurbeco.2023.103876
  date: 2023
  supports:
  - identity.instrument
  - design.primary_strategy
  - design.estimand
  verification_status: verified
  access_level: metadata
  locator: DOI metadata establishes the article identity, journal, year, volume, article number, and DOI; substantive design claims come from E1-E3.
design_applications:
- paper: 'The Minimum Wage and the Locations of New Business Entries in China: Estimates Based on a Refined Border Approach'
  doi: 10.1016/j.regsciurbeco.2023.103876
  journal: Regional Science and Urban Economics
  year: 2023
  research_question: How do local statutory minimum-wage differences affect the location and composition of new business entries near Chinese county borders?
  population: New business registrations in 2,526 county-level units forming 7,384 contiguous same-prefecture border pairs, 1997-2012.
  outcome: Annual counts of new registrations near each side of the county border, with industry-specific entry and shareholder-linked relocation measures.
  data_used:
  - National Enterprise Credit Information Publicity System business registrations and shareholder fields
  - Geocoded registration addresses and historical county-border GIS data
  - County-level minimum-wage schedules and local effective dates
  - CEIC wage data and census or IPUMS education measures for industry exposure
  - County-side pre-existing-establishment counts for baseline controls
  treatment_encoding: Pair-year log minimum-wage difference assigned to the higher- and lower-wage county sides within one-kilometre bands; secondary specifications use industry low-salary or low-skill exposure.
  comparison: The two sides of the same contiguous county border within the same prefecture and year, with wider bands and county-total estimates retained as diagnostic contrasts.
  empirical_design: Spatial difference-in-differences or border-pair regressions with pair and year fixed effects, narrow GIS bands, industry heterogeneity, and a shareholder-link relocation test.
  assumptions:
  - Time-varying shocks are sufficiently smooth across the narrow border conditional on pair and year controls.
  - County schedules, boundaries, and registration geocodes are correctly joined.
  - Registration coverage is comparable across sides and years.
  - The relocation proxy captures enough movement to interpret the entry response without treating it as exhaustive.
  threats_addressed:
  - Same-prefecture border-pair and year fixed effects
  - 1-km baseline and wider-band sensitivity
  - County-total contrast exposing local wage-setting endogeneity
  - Industry exposure heterogeneity
  - Shareholder-linked relocation analysis
  evidence_refs:
  - E3
  - E4
method_transfer: null
readiness_blockers:
- The paper's complete local minimum-wage schedule files, effective-date archive, and historical county-border crosswalk are not stored in this repository; recover them before constructing a replication-ready treatment panel.
- NECIPS microdata, geocoding provenance, and shareholder-link identifiers are not archived here. Acquisition, licensing, and deduplication belong in Econ Data Know-How.
- The legal sources establish the wage-setting framework but not every county's compliance, announcement date, or concurrent policy; do not convert the paper's annual schedule into a universal daily treatment clock.
- The narrow-border design requires continuity and limited cross-border sorting. The relocation proxy is incomplete, and the paper's reported coefficient should remain attributed to its sample and specification.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

China's Labor Law established a statutory minimum-wage floor, and the 2004 Minimum
Wage Regulations specified how provincial authorities should determine, adjust, and
enforce local levels. Provinces commonly maintained several tiers and allowed
county-level units to select levels according to local conditions. The result was a
shared legal framework with non-synchronous local schedules rather than one national
wage treatment [E1; E2].

The 2023 paper studies that local schedule as a spatial research object. It is related
to the repository's broader 2020 firm-competitive-shock record, but it asks a narrower
question: what happens to formal new business entry on either side of a nearby county
border when the two statutory schedules differ? The distinction is important because
the treatment, comparison, outcome, and join keys are all different.

## What Changed

There is no single reform date in this record. Between 1997 and 2012, neighboring
county-level units changed their statutory wage levels at different local dates and
by different amounts. A replication must therefore retain each notice's effective date
and tier, while treating the paper's annual pair-year schedule as a reported coding
choice [E1; E3].

The paper reports that a 10 percent local wage increase is associated with a 2.69
percent decline in new entries in the one-kilometre baseline. It also reports stronger
responses in low-salary or low-skill industries, weak relocation responses under its
shareholder-link definition, and different estimates after 2004. These are application
results, not universal properties of every county schedule [E3].

## Implementation and Assignment

The legal framework covers enterprises and other formal employers, but the empirical
assignment is not individual wage compliance. For a given year, the higher-wage side
of an eligible same-prefecture border is treated relative to the lower-wage side. The
paper keeps registrations within one kilometre of the shared line, geocodes addresses,
and compares the two sides of the same border pair. It requires both sides to have a
usable schedule and at least one observed entry [E3].

The shareholder-link exercise labels a registration as potentially relocated when an
owner also appears in a pre-existing establishment across the border. The authors note
that the rule can include owner expansion or production shifts and that registrations
do not directly report relocation. It is therefore a diagnostic for the mechanism,
not a complete mobility census [E3].

## Why This Creates Empirical Variation

Adjacent counties in one prefecture share much of the surrounding market while their
administrations can apply different wage tiers. A border-pair and year comparison in a
narrow band can absorb fixed geographic differences and limit broad local trends. The
continuous wage gap also makes it possible to study entry responses by industry wage
exposure. The design is useful precisely because it makes the comparison and join
explicit; it is not useful as a claim that local wage-setting is random [E3; analytical
inference].

The existing `china-minimum-wage-firm-competitive-shocks` record should remain linked
but separate. That record covers a broader county-level exposure for manufacturing
firms in 2002-2008, while this one covers formal new entries in narrow border bands
from 1997-2012. They can be compared or jointly studied only after their schedule
crosswalks and samples are harmonized.

## Identification Risks

Local governments may raise wages when entry and growth are already changing. The
paper's county-total contrast is a useful warning that a broad cross-sectional design
can pick up this selection. The narrow band reduces geographic distance but does not
remove a policy, infrastructure, zoning, or enforcement change that happens at the
same county line [E3; analytical inference].

Historical county reorganizations, changing wage tiers, announcement anticipation,
and geocoding errors can misassign treatment. Formal registration coverage can change
over time and misses informal activity. Finally, fewer registrations on the high-wage
side can be offset by nearby relocation, and shareholder links observe only part of
that process. These are reasons to preserve the paper's exact sample and diagnostics,
not reasons to label the variation unusable.

## Data Requirements

The minimum contract needs versioned county polygons and border pairs, local wage
notices with effective dates, registration IDs and incorporation dates, geocoded
addresses, industry codes, and pre-existing establishment counts. A relocation study
additionally needs shareholder identifiers and a defensible historical link rule.
Registration acquisition, licensing, geocoding, and cross-database joins belong in
`Econ Data Know-How`; this record keeps the institutional and design contract visible.

## Evidence Notes

E1 is the official 2004 regulation. It establishes the covered employers, provincial
determination process, adjustment and enforcement framework, but not the paper's full
county schedule archive. E2 is the official Labor Law text establishing the statutory
minimum-wage basis and dates; it does not prove local compliance. E3 is the inspected
author-hosted full paper and establishes the border sample, one-kilometre bands,
registration data, estimation strategy, heterogeneity, policy-period split, and
relocation definition as reported by the authors. E4 is metadata confirming the paper's
identity and DOI, not an additional source for local implementation.

The soft recency marker is 2023: it may help a later agent order recent applications,
but it cannot replace an archived assignment rule or move this record ahead of a more
distinct older variation merely because it is newer.
