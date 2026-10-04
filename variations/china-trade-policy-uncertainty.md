---
schema_version: 2
id: china-trade-policy-uncertainty
name: US PNTR for China and Product-Level Tariff-Threat Exposure
aliases:
- Handley-Limão trade policy uncertainty
- China WTO PNTR uncertainty
- 中国加入WTO贸易政策不确定性

status: grounded
provenance:
  task_id: task-d3a098a14272
scope:
  country: China
  regions:
  - All regions
  - with product-level variation in pre-WTO trade policy uncertainty
  domains:
  - trade
  - policy-uncertainty
  - welfare
  - firm-entry
  - industrial-organization
  - economic-growth
  - development-economics
  variation_type: continuous-exposure
  knowledge_role: global-china-variation
  china_relevance: US removal of annual NTR renewal exposes Chinese exports differently across products; this supports China-facing trade and development research, not an independently verified city-level treatment.
identity:
  instrument: '[E1, reported claim] The United States'' post-accession implementation of PNTR for China, which removed the risk that Chinese exports would later face higher US Column 2 tariffs; its empirical exposure is an HS-6 product''s 2000 Column-2-to-MFN tariff-factor ratio, not an observed fall in the applied tariff.'
  authority: US Congress authorises PNTR through Public Law 106-286; the President implements it through Proclamation 7516.
  legal_identifiers:
  - Public Law 106-286, signed 2000-10-10
  - Proclamation 7516, signed 2001-12-27, effective 2002-01-01
  - Chapter 1 of Title IV of the Trade Act of 1974, terminated for China by the proclamation
  implementation_regime: >
    Proclamation 7516 ends the annual-waiver regime and extends nondiscriminatory
    treatment to products of China from 2002-01-01. This removes one source of
    tariff uncertainty, not antidumping, safeguards, or all future trade-policy risk.
    China's other WTO commitments and later US tariff regimes are outside this case.
  assignment_mechanism: The reduction in trade policy uncertainty varied across products based on the gap between the NTR
    tariff rate (the low rate granted under annual renewal) and the non-NTR (Column 2) tariff rate (the high rate that would
    apply if NTR was revoked); products with a larger gap experienced a greater reduction in trade policy uncertainty, creating
    cross-product variation in the treatment intensity
  parent: null
  related_variations:
  - china-wto-accession-firm-performance
  - china-mfa-quota-removal-textile-exporters
timeline:
  announcement: '2000-10-10'
  effective: '2002-01-01'
  implementation_start: 2002
  implementation_end: null
  local_timing: >
    [E3, verified] The proclamation records WTO accession on 2001-12-11, was
    signed 2001-12-27, and expressly makes NTR extension effective 2002-01-01.
    The 2000 law is the authorisation, not the operational treatment date. The
    research window ends in 2005 or 2006 depending on specification; that is not
    a legal termination date.
  anticipation: '[E1, reported claim] The authors document remaining uncertainty in 2000 and a 2001 MFN-revocation vote; this is evidence against treating the October 2000 law alone as completed exposure, not proof of zero anticipation.'
  last_verified: '2026-09-28'
assignment:
  unit: Harmonised HS-6 product-industry; HS-10 trade lines support aggregation and variety measures
  treated: Products exported from China to the US that faced a positive gap between the non-NTR (Column 2) tariff and the
    NTR tariff rate before PNTR; the reduction in trade policy uncertainty is larger for products with a wider gap
  comparison_pool: Lower initial tariff-threat products within Chinese exports to the US; Taiwan-to-US and China-to-EU/Japan flows supply distinct demand or supply comparisons in robustness specifications.
  rule: >
    The common PNTR regime change is interacted with pre-existing product-specific
    tariff threats. Construct r_V=(1+t_Column2,V)/(1+t_MFN,V) using year-2000
    tariffs, not log of raw percentage rates. The published model-derived
    uncertainty regressor is 1-r_V^(-sigma), with sigma the elasticity of
    substitution (sigma=3 in the baseline OLS). Preserve the chosen transformation
    for the specification rather than treating every monotone ranking as an
    interchangeable quantitative regressor.
  intensity: Continuous initial tariff-threat exposure, transformed to potential profit loss in the model; neither observed applied-tariff cuts nor random product assignment
  exemptions: []
  compliance: The proclamation establishes NTR treatment for products of China; temporary trade barriers remain separately relevant, and a low threat gap is an exposure level rather than noncompliance.
  exposure_construction: Construct harmonised year-2000 tariff factors, their ratio and baseline potential-loss transform; compare HS-6 log export changes from 2000 to 2005 while retaining separate applied-tariff and transport-cost changes. The annual-panel and Taiwan specifications are distinct checks, not grounds to label this measure an IV.
  required_identifiers:
  - HS-6 code harmonised to the 1996 classification
  - Origin and destination country
  - year
  - HS-10 line crosswalk when constructing price or variety outcomes
  spillovers: Reduced trade policy uncertainty for China's exports to the US may have diverted Chinese exports from other
    markets toward the US; third countries competing with China in the US market may have been adversely affected
research_compatibility:
  outcome_domains:
  - export values
  - export prices
  - number of exporting firms
  - product variety
  - import prices
  - consumer welfare
  - real income
  - tariff pass-through
  - firm entry into exporting
  affected_populations:
  - Chinese exporters
  - US importers
  - US consumers
  - US industries competing with Chinese imports
  - foreign exporters competing with China in the US market
  mechanism_channels:
  - trade policy uncertainty reduction
  - sunk cost of exporting
  - firm entry and exit
  - price adjustment
  - product quality upgrading
  - investment in export capacity
  best_for:
  - Studying the effects of trade policy uncertainty on trade flows
  - firm entry into export markets
  - and consumer welfare; quantifying the value of trade agreements in reducing policy uncertainty
  not_good_for:
  - Studying domestic Chinese policy variations unrelated to trade; studying non-US export markets; analyzing tariff rate
    changes rather than uncertainty changes; short-run dynamics of adjustment at monthly frequency
design:
  claim_type: structural
  affordances:
  - Cross-product variation in the initial tariff threat
  - before-after comparison around PNTR/WTO accession
  - triple-difference using non-China trade flows as a control group
  - difference-in-differences over time and across products
  candidate_designs:
  - Difference-in-differences comparing products with high vs. low NTR gaps before and after PNTR
  - TPU-augmented gravity long-difference estimation
  - triple-difference with non-Chinese exporter trade flows to control for US demand shocks
  - gravity-model estimation with product fixed effects
  identifying_variation: Greater and smaller initial product-level tariff threats predict different China-US export changes after the annual renewal risk is removed, conditional on trade-cost and policy controls.
  assumptions:
  - Products with high and low NTR gaps would have had similar export trends absent PNTR; the NTR gap is not correlated with
    other determinants of export growth (such as US demand shocks or Chinese comparative advantage); no other policy changes
    differentially affected high and low NTR gap products at the same time
  diagnostics:
  - Test for pre-trends in high vs. low NTR gap products before PNTR; placebo tests assigning PNTR at different dates; compare
    results using alternative measures of trade policy uncertainty; include product-specific linear trends; control for MFN
    tariff reductions from the Uruguay Round
  primary_strategy: TPU-augmented gravity in 2000-2005 HS-6 long changes, followed by annual-panel checks and separate general-equilibrium structural quantification; not merely a binary high-gap DID.
  estimand: Conditional partial response of product exports or price/variety outcomes to removal of initial tariff-threat exposure; aggregate welfare and implied firm entry additionally depend on the structural model.
  treatment_variable: Initial tariff-factor ratio r_V and specification-specific 1-r_V^(-sigma), distinguished from an observed applied-tariff reduction
  comparison_logic: Within China-US product growth, compare different initial threats after conditioning on costs and sector effects; add Taiwan or non-US destinations only with the corresponding pooled specification.
  estimation_notes: >
    The baseline uses products traded in both 2000 and 2005 and principally ad
    valorem tariff lines; zero flows and specific tariffs require the paper's
    robustness handling. Annual levels checks use 1996-2006. Changes in applied
    tariffs and CIF/FOB transport costs are separate controls. Pooled comparisons
    use sector-country and HS-6 effects and cluster by HS-6 where specified.
    HS-10 variety entry is not observed entry of identifiable firms. Structural
    welfare counterfactuals are not additional randomised outcomes.
threats:
- type: confounding-trends
  basis: inferred
  condition: Products with high NTR gaps may have been on different growth trajectories than products with low NTR gaps for
    reasons unrelated to trade policy uncertainty (e.g., differential comparative advantage changes)
  evidence_refs:
  - E1
  possible_diagnostics:
  - Include product-specific linear trends
  - test for pre-existing trends
  - use triple-difference with non-China trade flows
  - employ stacked difference-in-differences with alternative control groups
- type: concurrent-policy-changes
  basis: inferred
  condition: China's WTO accession also involved MFN tariff reductions (applied to all WTO members), non-tariff barrier removals,
    and services liberalization, which may confound the effect of trade policy uncertainty reduction
  evidence_refs:
  - E1
  possible_diagnostics:
  - Control for MFN tariff changes in the same period
  - restrict sample to products where MFN tariffs did not change
  - Retain separate tariff, temporary-barrier and MFA controls; do not declare the threat measure a validated IV merely because it predates PNTR
- type: anticipation-effects
  basis: inferred
  condition: The reduction in trade policy uncertainty may have been anticipated before the actual PNTR vote, causing firms
    to adjust export behavior before 2000 and biasing the estimated treatment effect
  evidence_refs:
  - E1
  possible_diagnostics:
  - Examine dynamics of export growth around the PNTR vote
  - test for structural breaks at different dates
  - Distinguish announcement and legal operation in event-time tests rather than choosing a date to fit the result
  - control for pre-PNTR expectation measures
- type: measurement-error
  basis: inferred
  condition: The NTR gap may not perfectly measure trade policy uncertainty; other sources of trade policy uncertainty (such
    as antidumping investigations) may be correlated with the NTR gap but have different effects
  evidence_refs:
  - E1
  possible_diagnostics:
  - Use alternative measures of trade policy uncertainty
  - construct uncertainty measures from text analysis or option prices
  - include controls for antidumping activity
  - compare results across different measures
empirical_requirements:
  contract_version: 1
  population: Chinese products exported to the United States with linkable initial tariff threats and positive trade at both baseline endpoints
  observation_unit: Harmonised HS-6 product-industry long change
  geography_level: China-US bilateral product trade; not a local administrative unit
  time_start: 2000
  time_end: 2005
  minimum_frequency: Baseline endpoints 2000 and 2005; annual data required for timing and pre-trend checks
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - HS product code
  - year
  - Chinese export value to US
  - NTR tariff rate
  - non-NTR (Column 2) tariff rate
  - CIF and FOB trade values for transport-cost changes
  - Applied tariff changes and relevant temporary trade barrier and MFA measures
  required_identifiers:
  - HS product code
  - year
  treatment_key:
  - Harmonised HS-6 product code
  - Year-2000 tariff schedule
  treatment_source: TRAINS tariff schedules via WITS, harmonised to HS 1996; NBER HS-10 US import data aggregated to HS-6; COMTRADE for non-US export comparisons
  measurement_risks:
  - Concord HS 2002 to HS 1996; price and variety profiles additionally require longitudinal HS-10 matching, with ambiguous reassignments handled as in the paper.
  - The baseline excludes some zero-flow and specific-tariff lines; AVE construction uses fixed 1996 unit values and must not be silently replaced by current prices.
  - Firm IDs and proprietary Chinese Customs data are not required by this paper's product-level baseline. Local or firm exposure mapping is a further design, not already verified here.
  - A single baseline endpoint is not sufficient for an event-study pre-trend claim.
design_profiles:
- id: annual-product-timing-panel
  label: Annual product panel for timing and pre-accession trends
  design_families: [Product panel, Continuous exposure interacted with time]
  when_to_use: Use annual product trade data to examine differential timing rather than treating two endpoint observations as a full event study.
  outcome_domains: [Export values]
  requirements:
    population: Chinese products with harmonised trade and policy information
    observation_unit: HS-6 product-industry-year
    geography_level: Bilateral product trade
    time_start: 1996
    time_end: 2006
    minimum_frequency: Annual
    minimum_pre_periods: 5
    minimum_post_periods: 5
    required_fields: [Product export value, Initial MFN and Column 2 tariff factors, Applied tariff and transport-cost measures]
    required_identifiers: [HS-6 code harmonised to 1996, Origin country, Destination country, Year]
    treatment_key: [Harmonised HS-6 product code, Initial tariff schedule, Year]
evidence:
- id: E1
  source_type: paper
  citation: 'Handley, Kyle, and Nuno Limão. 2017. ''Policy Uncertainty, Trade, and Welfare: Theory and Evidence for China
    and the United States.'' American Economic Review 107 (9): 2731–2783.'
  url: https://doi.org/10.1257/aer.20141419
  date: 2017
  supports:
  - identity.instrument
  - identity.authority
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.effective
  - timeline.local_timing
  - timeline.anticipation
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.compliance
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
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_key
  - empirical_requirements.treatment_source
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
  locator: 'Published PDF at https://www.econ.umd.edu/sites/www.econ.umd.edu/files/pubs/aer.20141419.pdf reinspected 2026-09-28: section II.A-B, equations 11-13 and Tables 1-4 (printed 2744-2754), section II.D-E (pre-trends, annual panel, Taiwan and sunk-cost checks), Appendix B (2780-2781) for sources and concordances. Research design and data statements are paper-reported, not an independently executed replication.'
- id: E2
  source_type: policy-document
  citation: 'United States. Public Law 106-286, Normal Trade Relations for the People''s Republic of China, 10 October 2000.'
  url: https://www.govinfo.gov/content/pkg/PLAW-106publ286/pdf/PLAW-106publ286.pdf
  date: 2000
  supports:
  - identity.authority
  - identity.legal_identifiers
  - timeline.announcement
  verification_status: verified
  access_level: official-document
  locator: 'Act title/date and Division A, Title I sections 101-103, printed 114 Stat. 881-882 (PDF pages 3-4), reinspected 2026-09-28; section 102 prevents extension before accession, while section 103 separately preserves market-disruption relief. Congress.gov entry failed on this pass; the official GovInfo copy supplies the inspected text.'
- id: E3
  source_type: implementation-document
  citation: 'United States. Presidential Proclamation 7516 of December 27, 2001, To Extend Nondiscriminatory Treatment to the Products of the People''s Republic of China.'
  url: https://www.govinfo.gov/content/pkg/CFR-2002-title3-vol1/pdf/CFR-2002-title3-vol1-proc7516.pdf
  date: '2001-12-27'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.effective, timeline.implementation_start, timeline.local_timing, assignment.rule, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: CFR printed page 717 (PDF page 2), recitals 1 and 3-4, operative clauses 1-2 and signature. Verifies annual-waiver replacement, accession chronology and 2002-01-01 operation; product-specific tariff measures are established by E1, not by this proclamation.
design_applications:
- paper: 'Policy Uncertainty, Trade, and Welfare: Theory and Evidence for China and the United States'
  doi: 10.1257/aer.20141419
  journal: American Economic Review
  year: 2017
  research_question: How does trade policy uncertainty affect trade flows, firm entry, and consumer welfare, and what was
    the contribution of policy uncertainty reduction to China's export boom after WTO accession?
  population: Baseline 3,211 harmonised HS-6 industries with positive China-US trade at both 2000 and 2005 endpoints and principally ad valorem tariffs; price and variety samples differ
  outcome: HS-6 export growth, ideal import price index and traded HS-10 variety growth; model-based US welfare and implied firm-entry effects
  data_used:
  - NBER Harmonized System US imports at HS-10, concorded and aggregated to HS-6
  - TRAINS tariffs via WITS; COMTRADE unit values for specific-tariff ad valorem equivalents
  - COMTRADE Chinese exports to non-US destinations for supply comparisons
  - Temporary trade-barrier and textile-quota measures specified in Appendix B
  treatment_encoding: Year-2000 tariff-factor ratio and baseline 1-r^(-3) potential-loss measure; 2000-2005 long changes plus a separate 1996-2006 timing panel
  comparison: Products with high NTR gap vs. low NTR gap before and after PNTR; Chinese export growth vs. non-Chinese export
    growth for the same products
  empirical_design: TPU-augmented gravity long differences with tariff and transport controls; semiparametric functional-form checks, pooled bilateral robustness and separate structural general-equilibrium estimation
  assumptions:
  - Parallel trends across products with different NTR gaps before PNTR; NTR gap is exogenous conditional on product and year
    fixed effects; no other time-varying factors differentially affect high and low NTR gap products
  threats_addressed:
  - Pre-accession growth and annual timing checks; applied tariff, transport, NTB and MFA controls; Taiwan demand and non-US destination supply comparisons; sunk-cost heterogeneity
  evidence_refs:
  - E1
readiness_blockers:
- Recover and execute the precise tariff concordance, specific-duty AVE and zero-flow/sample handling before claiming numerical reproduction; this audit inspected publication and legal sources, not replication code.
- Price and variety applications require the online appendix's longitudinal HS-10 and ideal-index construction; variety counts are not firm counts.
- A regional or firm-level China application needs a separately justified pre-policy product-to-location or product-to-firm exposure mapping and counterfactual. The published product-level record does not itself establish that assignment.
method_transfer: null
---
## Institutional Background

[E3, verified] Chinese products received NTR through annual waivers before the
proclamation replaced that regime. [E1, paper report] The economically relevant
change is removal of a threat: firms deciding whether to incur export entry or
upgrading costs no longer face the same annual risk of losing low tariff treatment.
This is not evidence of a large contemporaneous cut in applied US tariffs.

## What Changed

[E2-E3, verified] Keep authorisation on 2000-10-10, WTO membership on 2001-12-11,
the implementing proclamation on 2001-12-27 and operation on 2002-01-01 separate.
The national regime change is common, but the exposure to the removed threat
differs by product. [E2] Section 103 also establishes market-disruption relief:
PNTR must not be described as ending every possible trade restriction.

## Implementation and Assignment

[E3] Legal operation is verified independently of the paper. [E1, paper report]
The empirical assignment requires the initial tariff schedule and harmonised
product identity. Use tariff factors including one, with rates converted from
percentages, before taking a ratio or its model-based transform. A product's
ranking by a threat gap is not the same object as its quantitative regressor.
Historical tariff schedules also do not make product assignment random.

## Why This Creates Empirical Variation

[E1, paper report] The main comparison is product export growth conditional on
applied tariffs, transport costs and sector trends. Taiwan-to-US comparisons help
address product-specific US demand; China-to-other-destination comparisons help
address Chinese supply. They serve different counterfactual purposes. Annual
timing tests provide another check, not a substitute for those assumptions.

[Analytical inference] A researcher can study China-facing development outcomes
with this exposure, but mapping it onto cities, employment or firms needs its own
pre-policy composition weights, joins and exclusion argument. The product-level
application does not establish that further spatial design by itself.

## Identification Risks

[Analytical inference] Correlated product trends, concurrent WTO commitments,
textile quotas and temporary barriers may undermine a threat-exposure comparison.
Control choices and pre-period diagnostics must address the application in hand.
[E1, paper report] Structural welfare conclusions further depend on demand,
entry, upgrading and general-equilibrium assumptions. A successful partial export
regression does not independently verify those assumptions. Do not describe
uninspected IV or firm-level specifications as robustness tests this paper performed.

## Data Requirements

[E1, Appendix B] The baseline is a product-level join, not a proprietary firm
panel. Tariffs and trade need consistent HS 1996 identities and endpoint years.
Use the annual profile for timing checks. Price and variety outcomes need finer
HS-10 construction, while structural welfare quantification needs additional
aggregate inputs. Keep these requirements separate rather than requiring every
possible data source for a simple export-growth application.

## Evidence Notes

Task `task-d3a098a14272` reinspected the published design and added the implementing
proclamation. It replaces contradictory timing and unsupported firm-data/IV
descriptions while preserving the existing record identity and its related cases.
Grounded status means the institutional core and actual application are traceable;
it is not a claim of executed replication or a ready-made regional instrument.
The two repositories can link through DOI without copying data-asset documentation.
