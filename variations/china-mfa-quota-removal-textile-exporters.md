---
schema_version: 2
id: china-mfa-quota-removal-textile-exporters
name: MFA Quota Removal and Trade Liberalization's Effect on Chinese Textile and Clothing Exporters
aliases:
- Khandelwal Schott Wei MFA China
- Chinese textile export quota removal
- embedded institutional reform AER

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - China (exporting firms) and major import markets (United States
  - European Union)
  domains:
  - international-trade
  - firm-dynamics
  - productivity
  - industrial-organization
  - development
  variation_type: staggered-rollout
  knowledge_role: global-china-variation
  china_relevance: A global or foreign policy change directly alters the treatment environment faced by Chinese units.
identity:
  instrument: The elimination of externally imposed export quotas on Chinese textile and clothing products under the Agreement
    on Textiles and Clothing (ATC), which phased out the Multifiber Arrangement (MFA) quota system between 1995 and 2005
  authority: World Trade Organization (WTO) through the Agreement on Textiles and Clothing; quotas were imposed by importing
    countries (US, EU, Canada, etc.) on Chinese exports
  legal_identifiers:
  - Agreement on Textiles and Clothing (ATC
  - 1995–2005)
  - Multifiber Arrangement (MFA
  - 1974–1994)
  - China WTO Accession (December 2001)
  - US-China bilateral textile agreements
  implementation_regime: The MFA phase-out removed export quotas on textile and clothing products in four stages (1995, 1998,
    2002, 2005); however, China only became a WTO member in December 2001, so the quota removals relevant to China were those
    in the final stage (2002 and especially 2005)
  assignment_mechanism: The timing of quota removal was determined by the product category's integration schedule under the
    ATC; some product categories had quotas removed earlier (2002) while others retained quotas until 2005; this creates variation
    across product categories in the timing of trade liberalization
  parent: null
  related_variations: []
timeline:
  announcement: '1994-12-31'
  effective: '1995-01-01'
  implementation_start: 1995
  implementation_end: 2005
  local_timing: The ATC phase-out applied globally, but for China, the binding removals occurred in stages 3 (2002) and 4
    (2005) because China was not a WTO member before 2001; the US and EU also maintained separate quotas on China through
    bilateral agreements that were eliminated in 2005
  anticipation: The ATC phase-out schedule was announced in 1994, providing advance notice of quota removals; however, the
    magnitude of China's export surge and the degree of resource misallocation under quotas were not fully anticipated
  last_verified: '2026-07-13'
assignment:
  unit: Product category (HS or MFA category)
  treated: Textile and clothing product categories whose quotas were removed (either in 2002 or 2005)
  comparison_pool: Product categories that were never subject to quotas (always unrestricted); variation across categories
    in the timing of quota removal (2002 vs. 2005) provides staggered treatment
  rule: Products subject to binding quotas before liberalization experienced a surge in exports from China after quota removal;
    the allocation of quotas before liberalization was based on historical export performance and administrative decisions,
    not necessarily firm productivity
  intensity: Binary at the product-category level (quota removed or not), but continuous at the product-category level in
    terms of how binding the pre-removal quota was (quota utilization rate)
  compliance: Complete removal of quotas as scheduled under the ATC; no non-compliance by importing countries
  exposure_construction: Code product categories as treated after the year in which their quotas were removed; use pre-liberalization
    quota bindingness (quota utilization rate) as a measure of treatment intensity; construct firm-level exposure based on
    their product mix before liberalization
  required_identifiers:
  - firm ID
  - year
  - product code (HS)
  - MFA category
  - quota status
  - quota level
  exemptions: []
  spillovers: Quota removal on one product category may affect exports in related categories as firms redirect production
    capacity; general equilibrium effects on wages, exchange rates, and export prices across the textile and clothing sector
research_compatibility:
  outcome_domains:
  - export volume
  - export prices
  - firm entry and exit
  - firm-level productivity
  - resource allocation
  - product quality
  affected_populations:
  - Chinese textile and clothing exporters
  - importing firms in the US and EU
  - workers in the textile and clothing industry
  - competing exporters from other countries
  mechanism_channels:
  - quota removal channel
  - resource reallocation channel
  - firm entry channel
  - rent dissipation
  - productivity improvement through reallocation
  best_for:
  - Studying how trade liberalization affects resource allocation across firms
  - analyzing misallocation from quantitative restrictions
  - estimating productivity gains from trade reform
  not_good_for:
  - Non-traded sectors
  - periods outside the phase-out window
  - outcomes not affected by export conditions
  - settings without binding quotas before liberalization
design:
  affordances:
  - staggered quota removal across product categories
  - variation in pre-reform quota bindingness
  - variation across firms in quota exposure
  - comparison with never-quota products
  candidate_designs:
  - staggered difference-in-differences across product categories
  - event study around quota removal
  - cross-sectional comparison of quota-bound vs. unbound products after removal
  - firm-level analysis using product mix exposure
  identifying_variation: Variation across textile product categories in the timing of quota removal (2002 vs. 2005) and in
    the bindingness of pre-removal quotas; variation across firms in their pre-liberalization product mix and thus in their
    exposure to quota removal
  assumptions:
  - The timing of quota removal is exogenous to firm-level productivity within the phase-out schedule
  - no other major trade policy changes differentially affect quota-bound products at the same time
  - firms cannot fully anticipate the magnitude of post-removal changes
  diagnostics:
  - event-study plots around quota removal
  - compare characteristics of early vs. late quota removers
  - test for pre-trends in export volumes and prices
  - placebo tests using unaffected time periods
  primary_strategy: Staggered difference-in-differences across product categories with year fixed effects; firm-level analysis
    using product mix exposure
  estimand: The causal effect of the recorded exposure on Export volume, export prices, number of exporting firms, firm entry
    and exit, productivity distribution, conditional on the stated design assumptions.
  treatment_variable: Binary indicator for whether product category's quota has been removed; continuous measure using pre-removal
    quota utilization rate (bindingness)
  comparison_logic: Quota-bound vs. unbound product categories; early (2002) vs. late (2005) quota removal; quota-bound products
    after removal vs. before removal
  estimation_notes: Staggered difference-in-differences across product categories with year fixed effects; firm-level analysis
    using product mix exposure
threats:
- type: selection-into-quota-removal-timing
  basis: documented
  condition: The ATC phase-out schedule was negotiated and products may have been sequenced based on political economy considerations,
    potentially correlating with product characteristics
  evidence_refs:
  - E1
  possible_diagnostics:
  - compare characteristics of early vs. late removed products
  - test sensitivity to controlling for product characteristics
  - use within-product variation over time
  - examine robustness to restricting to 2005 removal only
- type: china-specific-policies
  basis: inferred
  condition: China's WTO accession in 2001 coincided with broader trade liberalization (tariff reductions, removal of non-tariff
    barriers) that independently affected Chinese exports at the same time as quota removals
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for China's MFN tariff reductions
  - compare quota-bound vs. unbound products to difference out common WTO effects
  - use product-level variation to isolate quota effects
- type: general-equilibrium-effects
  basis: inferred
  condition: Quota removal on Chinese exports affected world prices, which in turn affected export patterns of other countries
    and potentially input prices, creating general equilibrium feedback
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for world market conditions
  - examine third-country export responses
  - use firm-level analysis to isolate micro effects
  - sensitivity to global demand controls
empirical_requirements:
  contract_version: 1
  population: Chinese textile and clothing exporting firms, 2000–2006
  observation_unit: Firm-year or product-year
  geography_level: National (firm-level) with product-level disaggregation
  time_start: 2000
  time_end: 2006
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields:
  - firm ID
  - year
  - product code
  - export value
  - export quantity
  - destination country
  - MFA quota status
  required_identifiers:
  - firm ID
  - year
  - product code (HS 8- or 10-digit)
  - MFA category code
  treatment_key:
  - product category code
  - post-quota-removal indicator
  - pre-removal quota utilization rate
  treatment_source: Chinese Customs Trade Statistics (firm-level export transactions); MFA quota schedules from the WTO and
    US/EU trade authorities; US ITC and EU Trade DG data on quota levels and utilization
  measurement_risks:
  - firm-level export data may not cover all export channels (processing trade reporting issues)
  - product code harmonization across datasets
  - quota utilization rates may be measured with error
  - firm entry and exit around quota removal may reflect strategic behavior
evidence:
- id: E1
  source_type: paper
  citation: 'Khandelwal, Amit K., Peter K. Schott, and Shang-Jin Wei. 2013. "Trade Liberalization and Embedded Institutional
    Reform: Evidence from Chinese Exporters." American Economic Review 103 (6): 2169–2195.'
  url: https://doi.org/10.1257/aer.103.6.2169
  date: 2013
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - resource misallocation
  - productivity gains
  - firm entry
  - export surge
  verification_status: verified
design_applications:
- paper: 'Trade Liberalization and Embedded Institutional Reform: Evidence from Chinese Exporters'
  doi: 10.1257/aer.103.6.2169
  journal: American Economic Review
  year: 2013
  research_question: How did the removal of externally imposed export quotas affect Chinese textile and clothing exports,
    and what does the pattern of export expansion reveal about resource misallocation under the quota regime?
  population: Chinese textile and clothing exporters, 2000–2006
  outcome: Export volume, export prices, number of exporting firms, firm entry and exit, productivity distribution
  data_used:
  - Chinese Customs Trade Statistics (firm-level export transactions)
  - MFA quota schedules from WTO, United States, and European Union trade authorities
  - Chinese Industrial Enterprises Database for firm characteristics and productivity
  treatment_encoding: Binary indicator for whether product category's quota has been removed; continuous measure using pre-removal
    quota utilization rate (bindingness)
  comparison: Quota-bound vs. unbound product categories; early (2002) vs. late (2005) quota removal; quota-bound products
    after removal vs. before removal
  empirical_design: Staggered difference-in-differences across product categories with year fixed effects; firm-level analysis
    using product mix exposure
  assumptions:
  - Timing of quota removal is exogenous to product-level productivity trends
  - no other simultaneous trade policy changes differentially affect quota-bound products
  threats_addressed:
  - selection into quota removal timing via product fixed effects and event-study pre-trends
  - WTO accession confounding via comparing quota vs. non-quota products
  - anticipation via robustness checks
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
method_transfer: null
---
## Institutional Background

Under the Multifiber Arrangement (MFA), importing countries (primarily the US and EU) imposed quantitative restrictions (quotas) on textile and clothing exports from developing countries, including China. These quotas were product-specific, limiting the quantity of each product category that could be exported. The quotas created artificial scarcity and rents: firms with quota allocations could earn rents from restricted market access, while more productive firms that could not obtain quota allocations were prevented from expanding. This system of quantitative restrictions created misallocation by decoupling production from productivity. [E1]

## What Changed

The Agreement on Textiles and Clothing (ATC), signed during the Uruguay Round, mandated the phase-out of all MFA quotas in four stages between 1995 and 2005. For China, the key quota removals occurred when it joined the WTO in December 2001: some product quotas were removed immediately in 2002 (Stage 3), while others were removed in January 2005 (Stage 4). The quota removal eliminated quantitative restrictions on Chinese textile and clothing exports, allowing market forces rather than administrative allocation to determine which firms exported and how much. [E1]

## Implementation and Assignment

Quota removal followed a pre-announced schedule defined at the product-category level. Product categories in stages 1 and 2 (1995, 1998) had their quotas removed before China joined the WTO; for China, stages 3 (2002) and 4 (2005) were the relevant liberalization events. The analysis exploits variation across product categories in the timing of quota removal and in the bindingness of quotas before removal (measured by quota utilization rates). Firm-level exposure varies based on each firm's pre-liberalization product mix. [E1]

## Why This Creates Empirical Variation

The staggered removal of quotas across product categories generates variation in liberalization timing that identifies the effects of removing quantitative restrictions. Product categories whose quotas were more binding (higher utilization rates) before removal experienced larger export surges and greater resource reallocation after removal. The paper uses this variation to test for resource misallocation: under the quota regime, export expansion after removal should occur disproportionately through net entry of new firms (rather than expansion by incumbents) if quotas were allocated inefficiently. [E1; analytical inference]

## Identification Risks

The timing of quota removal was not random but negotiated under the ATC, potentially correlating with product characteristics. However, the staggered nature of the phase-out and the use of product fixed effects addresses time-invariant product heterogeneity. A more significant concern is that China's WTO accession in 2001 coincided with tariff reductions and other trade reforms that may independently affect textile and clothing exports. The paper addresses this by comparing quota-bound and never-bound products to difference out common WTO effects. [E1; analytical inference]

## Data Requirements

Product-category-level data on quota levels and utilization rates from WTO, US, and EU trade authorities; firm-level customs data tracking exports by product, value, quantity, and destination; firm registration and characteristics data to track entry, exit, and productivity. The analysis requires concordance between MFA product categories and the Harmonized System (HS) codes used in Chinese customs data. [E1]

## Evidence Notes

E1 finds that both the surge in export volumes and the decline in export prices after quota removal were driven primarily by net entry of new firms, not by expansion of incumbent exporters. This pattern is inconsistent with the efficient allocation of quotas under the MFA regime, suggesting that quotas were allocated based on non-productivity criteria (such as historical market share, political connections, or administrative decisions). The paper estimates that removing this misallocation accounts for a substantial share of the productivity gains associated with quota removal.
