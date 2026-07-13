---
schema_version: 2
id: china-trade-policy-uncertainty
name: Reduction in Trade Policy Uncertainty from China's WTO Accession and US Granting of Permanent Normal Trade Relations
  (2000–2001)
aliases:
- Handley-Limão trade policy uncertainty
- China WTO PNTR uncertainty
- 中国加入WTO贸易政策不确定性

status: extracted
provenance:
  task_id: legacy-untracked
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
  variation_type: single-date-reform
  knowledge_role: global-china-variation
  china_relevance: A global or foreign policy change directly alters the treatment environment faced by Chinese units.
identity:
  instrument: The US granting of Permanent Normal Trade Relations (PNTR) to China in October 2000 (effective when China joined
    the WTO in December 2001), which eliminated the threat of annual tariff revocations and created a discrete, permanent
    reduction in trade policy uncertainty facing Chinese exporters to the US market
  authority: United States Congress (granting PNTR to China), World Trade Organization (China's accession), State Council
    of China (WTO accession agreement)
  legal_identifiers:
  - US-China Trade Relations Act of 2000 (PNTR)
  - China's WTO Accession Protocol (2001)
  - Jackson-Vanik amendment waiver
  - US MFN/NTR tariff schedules
  - Section 301 provisions
  implementation_regime: Before China's WTO accession, the US renewed China's Normal Trade Relations (NTR) status annually
    through a presidential waiver of the Jackson-Vanik amendment, subjecting Chinese exports to the threat of tariff increases
    to Smoot-Hawley (Column 2) levels; PNTR eliminated this annual renewal requirement, making the low NTR tariff rates permanent
    and reducing trade policy uncertainty for Chinese exporters
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
  effective: '2001-12-11'
  implementation_start: 2000
  implementation_end: 2001
  local_timing: The US Congress granted PNTR to China in October 2000, and the policy took effect when China formally joined
    the WTO on December 11, 2001; the reduction in trade policy uncertainty was immediately effective upon WTO accession
  anticipation: The PNTR legislation was debated in Congress throughout 2000, so markets partially anticipated the reduction
    in trade policy uncertainty before the final vote; however, the exact timing and outcome were uncertain until the vote
    passed
  last_verified: '2026-07-13'
assignment:
  unit: Product (HS tariff line) and firm (Chinese exporter)
  treated: Products exported from China to the US that faced a positive gap between the non-NTR (Column 2) tariff and the
    NTR tariff rate before PNTR; the reduction in trade policy uncertainty is larger for products with a wider gap
  comparison_pool: Products with zero or small NTR/non-NTR gaps (where PNTR had little effect on trade policy uncertainty);
    products not affected by US tariff policy
  rule: A product is treated when the US grants China PNTR, eliminating the annual threat that tariffs on Chinese exports
    could rise from NTR to non-NTR (Column 2) levels; treatment intensity is the log difference between the non-NTR and NTR
    tariff rates
  intensity: Continuous — the NTR gap (log difference between non-NTR and NTR tariff rates); alternative specifications use
    the tariff risk premium, the probability of a trade war scenario, or a binary indicator for products that faced positive
    trade policy uncertainty
  exemptions: []
  compliance: The PNTR policy was binding on all US imports from China; no exemptions existed once PNTR was implemented
  exposure_construction: The NTR gap (ln(1 + τ_non_NTR) − ln(1 + τ_NTR)) for each product at the HS tariff line level, interacted
    with the post-PNTR period; the instrument uses this cross-product variation in the magnitude of the uncertainty reduction
  required_identifiers:
  - HS product code
  - NTR tariff rate
  - non-NTR (Column 2) tariff rate
  - year
  - Chinese export value to US
  - Chinese export value to other countries
  - US import value from China
  - firm-level export data (for firm-level analysis)
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
  affordances:
  - Cross-product variation in the NTR gap
  - before-after comparison around PNTR/WTO accession
  - triple-difference using non-China trade flows as a control group
  - difference-in-differences over time and across products
  candidate_designs:
  - Difference-in-differences comparing products with high vs. low NTR gaps before and after PNTR
  - instrumental variables using the NTR gap as a shifter of Chinese exports
  - triple-difference with non-Chinese exporter trade flows to control for US demand shocks
  - gravity-model estimation with product fixed effects
  identifying_variation: Cross-product variation in the NTR gap (the difference between non-NTR and NTR tariff rates) interacted
    with the post-PNTR period; the identifying assumption is that products with larger and smaller NTR gaps would have followed
    similar trade trends in the absence of PNTR
  assumptions:
  - Products with high and low NTR gaps would have had similar export trends absent PNTR; the NTR gap is not correlated with
    other determinants of export growth (such as US demand shocks or Chinese comparative advantage); no other policy changes
    differentially affected high and low NTR gap products at the same time
  diagnostics:
  - Test for pre-trends in high vs. low NTR gap products before PNTR; placebo tests assigning PNTR at different dates; compare
    results using alternative measures of trade policy uncertainty; include product-specific linear trends; control for MFN
    tariff reductions from the Uruguay Round
  primary_strategy: Difference-in-differences comparing product-level Chinese export growth for products with varying NTR
    gaps, before and after PNTR; structural estimation of a general equilibrium trade model with policy uncertainty
  estimand: The causal effect of the recorded exposure on Chinese export values and prices to the United States, number of
    Chinese exporters, US import prices, US consumer welfare, conditional on the stated design assumptions.
  treatment_variable: NTR gap = ln(1 + τ_non_NTR) − ln(1 + τ_NTR), interacted with post-PNTR indicator; binary indicator for
    products with a positive NTR gap
  comparison_logic: Products with high NTR gap vs. low NTR gap before and after PNTR; Chinese export growth vs. non-Chinese
    export growth for the same products
  estimation_notes: Difference-in-differences comparing product-level Chinese export growth for products with varying NTR
    gaps, before and after PNTR; structural estimation of a general equilibrium trade model with policy uncertainty
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
  - use the NTR gap as an instrument for trade policy uncertainty while controlling for other WTO-related changes
- type: anticipation-effects
  basis: inferred
  condition: The reduction in trade policy uncertainty may have been anticipated before the actual PNTR vote, causing firms
    to adjust export behavior before 2000 and biasing the estimated treatment effect
  evidence_refs:
  - E1
  possible_diagnostics:
  - Examine dynamics of export growth around the PNTR vote
  - test for structural breaks at different dates
  - use announcement date rather than effective date
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
  population: Chinese exports to the United States at the product (HS) level, 1995–2005
  observation_unit: Product (HS tariff line)-year; firm-product-year (for firm-level analysis)
  geography_level: Product (HS) level for trade flows; firm level for exporter analysis
  time_start: 1995
  time_end: 2005
  minimum_frequency: annual
  minimum_pre_periods: 5
  minimum_post_periods: 4
  required_fields:
  - HS product code
  - year
  - Chinese export value to US
  - Chinese export quantity to US
  - NTR tariff rate
  - non-NTR (Column 2) tariff rate
  - Chinese export value to other countries
  - US import value from all countries
  - firm identifiers (for firm-level analysis)
  required_identifiers:
  - HS product code
  - year
  treatment_key:
  - NTR gap (ln(1 + τ_non_NTR) − ln(1 + τ_NTR))
  - post-PNTR indicator
  - interaction
  treatment_source: US International Trade Commission (USITC) Tariff Database for tariff rates; US Census Bureau for US import
    data; Chinese Customs Statistics for Chinese export data
  measurement_risks:
  - NTR gap may be endogenous if tariffs are correlated with product characteristics or political determinants; product-level
    aggregation may mask firm-level heterogeneity; US import data includes re-exports through third countries; processing
    trade may respond differently to policy uncertainty than ordinary trade
evidence:
- id: E1
  source_type: paper
  citation: 'Handley, Kyle, and Nuno Limão. 2017. ''Policy Uncertainty, Trade, and Welfare: Theory and Evidence for China
    and the United States.'' American Economic Review 107 (9): 2731–2783.'
  url: https://doi.org/10.1257/aer.20141419
  date: 2017
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - theory framework
  - welfare quantification
  - firm entry analysis
  verification_status: verified
design_applications:
- paper: 'Policy Uncertainty, Trade, and Welfare: Theory and Evidence for China and the United States'
  doi: 10.1257/aer.20141419
  journal: American Economic Review
  year: 2017
  research_question: How does trade policy uncertainty affect trade flows, firm entry, and consumer welfare, and what was
    the contribution of policy uncertainty reduction to China's export boom after WTO accession?
  population: Chinese exports to the United States at the product level (approximately 5,000 HS tariff lines, 1995–2005)
  outcome: Chinese export values and prices to the United States, number of Chinese exporters, US import prices, US consumer
    welfare
  data_used:
  - US ITC tariff data (NTR and non-NTR rates)
  - US Census trade data
  - Chinese Customs trade data
  - Chinese Customs firm-level export data
  treatment_encoding: NTR gap = ln(1 + τ_non_NTR) − ln(1 + τ_NTR), interacted with post-PNTR indicator; binary indicator for
    products with a positive NTR gap
  comparison: Products with high NTR gap vs. low NTR gap before and after PNTR; Chinese export growth vs. non-Chinese export
    growth for the same products
  empirical_design: Difference-in-differences comparing product-level Chinese export growth for products with varying NTR
    gaps, before and after PNTR; structural estimation of a general equilibrium trade model with policy uncertainty
  assumptions:
  - Parallel trends across products with different NTR gaps before PNTR; NTR gap is exogenous conditional on product and year
    fixed effects; no other time-varying factors differentially affect high and low NTR gap products
  threats_addressed:
  - Confounding trends via product fixed effects and pre-trend tests; other WTO changes via controlling for MFN tariff reductions;
    anticipation via event study dynamics; endogeneity via instrumenting for the NTR gap using product characteristics
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
method_transfer: null
---
## Institutional Background

Before China's accession to the World Trade Organization (WTO) in December 2001, United States trade policy toward China was governed by the Jackson-Vanik amendment to the Trade Act of 1974. This provision required the US President to renew China's Normal Trade Relations (NTR) status annually, subject to a determination that China satisfied certain conditions regarding emigration rights. This annual renewal process created significant trade policy uncertainty: if NTR status was revoked, US tariffs on Chinese imports would revert to the much higher Smoot-Hawley tariff rates (the "Column 2" rates), which averaged approximately 35% compared to NTR rates averaging about 4%. The granting of Permanent Normal Trade Relations (PNTR) to China in October 2000 (effective December 2001) eliminated this annual uncertainty, making the low NTR tariff rates permanent and removing the threat of a tariff increase on Chinese exports. [E1]

## What Changed

The US Congress passed PNTR legislation in October 2000, and the policy became effective when China joined the WTO on December 11, 2001. This policy change eliminated the annual review of China's NTR status, making the low NTR tariff rates permanent. Critically, the magnitude of the uncertainty reduction varied across products: products with a large gap between the non-NTR (Column 2) rate and the NTR rate faced a large reduction in trade policy uncertainty, while products where the two rates were similar faced little change in uncertainty. This cross-product variation in the "NTR gap" provides the identifying variation for estimating the effects of trade policy uncertainty on Chinese exports and US welfare. [E1]

## Implementation and Assignment

The PNTR policy was implemented through an act of the US Congress signed into law by President Clinton in October 2000, taking effect upon China's WTO accession in December 2001. The policy change applied to all Chinese exports to the US, but its impact varied across products based on the pre-existing gap between NTR and non-NTR tariff rates. The identification strategy exploits this product-level variation in treatment intensity: the NTR gap measures the magnitude of the trade policy uncertainty reduction for each product. Products with larger NTR gaps experienced a greater reduction in uncertainty about future US tariff policy, generating cross-product variation in the incentive for Chinese firms to enter the US export market. [E1]

## Why This Creates Empirical Variation

The NTR gap varies across products based on historically determined tariff schedules that are plausibly exogenous to contemporaneous Chinese export supply conditions. Before PNTR, Chinese exporters faced the risk that tariffs on their products could rise from low NTR rates to high non-NTR rates if NTR status was revoked. PNTR eliminated this risk permanently. The identification compares the change in Chinese export outcomes (values, prices, firm entry) for products with high NTR gaps (large uncertainty reduction) to products with low NTR gaps (small uncertainty reduction), before and after the PNTR/WTO policy change. Handley and Limão (2017) find that this reduction in trade policy uncertainty accounts for over one-third of China's export growth to the US between 2000 and 2005, and that the reduction in uncertainty is equivalent to a 13-percentage-point permanent tariff reduction in terms of its effect on US consumer welfare. [E1; analytical inference]

## Identification Risks

The primary identification concern is that products with high and low NTR gaps may have differed in other dimensions that affected their export growth even without PNTR. For example, products in which China had rapidly growing comparative advantage may have been systematically different from products with stagnant export growth. The paper addresses this through product fixed effects, pre-trend tests, and controlling for other WTO-related changes (such as MFN tariff reductions). Additional concerns include: anticipation effects (firms may have adjusted before the policy change was certain), concurrent changes in Chinese trade policy (WTO accession involved multiple liberalization measures), and measurement error in the NTR gap as a proxy for policy uncertainty. The authors address these through event-study dynamics, triple-difference comparisons with non-Chinese exporters to control for US demand shocks, and robustness checks using alternative uncertainty measures. [E1; analytical inference]

## Data Requirements

Product-level trade data from the US Census Bureau (US imports from China and other countries) and Chinese Customs Statistics (Chinese exports by product and destination). Tariff data from the US International Trade Commission (USITC) providing both NTR (Column 1) and non-NTR (Column 2) tariff rates at the HS tariff line level for the pre-PNTR period. For firm-level analysis, Chinese Customs firm-level export data covering the universe of Chinese exporters with product-destination information. The key variables are the NTR gap for each HS product, Chinese export values and quantities, and US import data. [E1]

## Evidence Notes

E1 is the published AER article. It develops a general equilibrium model of trade with policy uncertainty and firms' export entry decisions, and estimates the model using product-level trade data. The paper's central finding is that the elimination of trade policy uncertainty via PNTR accounted for more than one-third of the increase in Chinese exports to the US during 2000–2005 (a period when Chinese manufacturing exports to the US more than doubled). The welfare analysis shows that the reduction in trade policy uncertainty lowered US import prices and increased US consumers' real income by an amount equivalent to a 13-percentage-point reduction in permanent tariffs. The paper also provides evidence that the effect operates through the extensive margin (entry of new Chinese exporters and new products) rather than primarily through the intensive margin (increased exports by existing exporters).
