---
schema_version: 2
id: china-2007-export-vat-rebate-product-cuts
name: China July2007 Export VAT Rebate Product Cuts and Predetermined Firm Exposure
aliases: [2007出口退税下调, 财税〔2007〕90号产品冲击, RebateCore2006, Export rebate cuts and firm pollution]
status: grounded
provenance:
  task_id: task-f3ce2621c91a
scope:
  country: China
  regions: [Mainland manufacturing firms in the application]
  domains: [firms, international-trade, environmental-economics, public-finance, financial-frictions, development-economics]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: Mainland manufacturing firms face different exposure to a national product-specific export rebate reduction through their fixed2006 export portfolios. The inspected paper actually studies their exports, output and pollution, not an overseas method proposed for China.
identity:
  instrument: July2007 product-specific export VAT rebate removal or reduction interacted with predetermined firm export-product exposure.
  authority: Ministry of Finance and State Administration of Taxation, with customs export dates and local tax administration.
  legal_identifiers: [财政部 国家税务总局关于调低部分商品出口退税率的通知, 财税〔2007〕90号, 财税〔2007〕97号补充通知]
  implementation_regime: >
    The original July2007 product adjustment and its July correction. Notice90
    separates removal, reduction and a third exemption category. Subsequent
    product-specific reversals and grandfathered contracts limit a permanent
    treatment interpretation. This is not the2004 central/local refund-financing
    reform or a universal VAT-rate reduction.
  assignment_mechanism: >
    Authorities target product categories, including pollution/resource concerns
    and trade friction; firms inherit exposure from their existing export basket.
    The paper fixes that basket in2006 rather than assigning firms randomly.
    Product targeting and prior specialization can generate differential trends.
  parent: null
  related_variations: [china-2004-export-vat-refund-local-financing]
timeline:
  announcement: '2007-06-19 public announcement; MOF explanation reports the joint decision on18June'
  effective: '2007-07-01'
  implementation_start: 2007
  implementation_end: null
  local_timing: >
    Notice90 uses the export date on the customs declaration. The application
    instead codes Post07=1 from2008, with2007 retained as the reference year.
    That is a full-year-post convention, not proof that2007 is untreated.
    Notice97 is dated10July2007. The2000-2013 study window is not a legal end
    date, and the entire package cannot be assumed unchanged throughout it.
  anticipation: Public notice precedes effect by about two weeks; prior environmental/trade policy signals can influence2006 specialization. Firm anticipation and partially treated2007 remain identification concerns.
  last_verified: '2026-10-03'
assignment:
  unit: Product-specific legal adjustment linked to a mainland firm through its fixed2006 export portfolio; annual firm outcomes.
  treated: Paper baseline firms with at least one of their top three2006 export-value products on its rebate-adjustment list.
  comparison_pool: Manufacturing firms without an affected core export product, including non-exporters and exporters without a qualifying core product; not a randomly selected or entirely unexposed group.
  rule: >
    Determine product membership in the removal/reduction schedules, keeping
    the exemption list distinct and applying Notice97 corrections. The tables
    specify new rates, not percentage-point cuts. Contract qualifications and
    customs export dates govern actual legal treatment; product membership
    alone predicts rather than observes a firm's refund loss.
  intensity: Baseline RebateCore is binary; RebateFull flags any affected export product and RebateShr is the2006 export-value-weighted affected share. These are alternative encodings of one product-policy exposure, not separate variations.
  exemptions:
  - Notice90 permits specified pre-July ship/export-contract and overseas-project contracts registered by20July2007 to retain previous rates; Notice97 clarifies categories and additional transactions retaining previous rates.
  - Conversion to exemption is legally distinct from an observed refund-rate cut; do not include that third schedule mechanically as a rebate reduction.
  - Paper scope is manufacturing; agricultural items in the broader legal schedules are not a new agricultural research application here.
  compliance: Statutory rates, exporter eligibility, contract grandfathering, approved refund and actual receipt differ. The paper's portfolio indicator does not measure refunds received or firm-level compliance.
  exposure_construction: >
    Aggregate2006 Customs export values by firm and product across destinations;
    harmonize the product vintage to the legal schedule before ranking. Set
    RebateCore_i=1 if any of the top three products by value is in the
    paper's rebate-cut list. Set RebateFull_i=1 for any affected export product;
    RebateShr_i=sum_p(export_value_ip2006 * affected_p)/total_exports_i2006.
    Interact each alternative with1(year>=2008) for the reported application.
    The share is value-weighted, not a fraction of product counts. Verify genuine
    non-exporters before assigning zero; unmatched or missing Customs records
    are not proof of no exports. Exact author list, HS aggregation and ties
    require reconciliation before numerical reproduction; no such code was inspected.
  required_identifiers: [firm_id, firm_name, year, product_code, city_id, industry_code]
  spillovers: Export-to-domestic-market substitution, supplier demand, competition and financing can transmit effects to nominal controls. Firm contrasts do not identify aggregate emissions, welfare or city-wide growth without additional structure.
research_compatibility:
  outcome_domains: [Firm export value and participation, Domestic sales share, Output, Revenue and profitability, SO2 and COD emissions and intensity, Productivity, Imported abatement equipment, Patents]
  affected_populations: [Matched mainland manufacturing firms, Exporters with pre-policy Customs portfolios, Polluting firms in the environmental survey]
  mechanism_channels: [Export-tax burden, Export demand and domestic substitution, Internal finance, Production scale, Abatement investment and productivity]
  best_for:
  - Studying manufacturing responses to a product-targeted trade/fiscal shock with observable pre-policy portfolios and an explicit counterfactual-trend assessment.
  - Separating production-scale changes from pollution-intensity changes using the same exposed firms, rather than interpreting lower total emissions as cleaner technology.
  not_good_for:
  - Treating pollution-targeted product selection as random or calling2007 a wholly untreated reference year.
  - Using the portfolio indicator as a direct bank-credit instrument; rebates also affect demand, prices and product mix.
  - Estimating a per-percentage-point tax effect from binary list membership without actual before/after rates.
  - Equating unmatched firms with non-exporters or extrapolating survey-surviving manufacturing firms to all firms or agriculture.
design:
  claim_type: causal
  affordances: [Predetermined product-portfolio exposure, National product-specific adjustment, Alternative binary and value-share encodings]
  candidate_designs: [Firm-panel difference-in-differences, Exposure-by-year event study, Conditional credit-access heterogeneity]
  identifying_variation: Relative post2007 changes of fixed2006 product-exposed and comparison firms, after stable firm differences and common annual factors. No random firm assignment is established.
  primary_strategy: >
    Lu Zhang Li2023 Eq4 estimates RebateCore_i x Post07_t with firm and year
    effects, firm controls and city-clustered errors; tables also list city
    effects. Eq5 interacts fixed exposure with year indicators, omitting2007.
    Table6 adds city-year or industry-year effects and1:10 nearest-neighbor
    propensity-score matching. These are reported sensitivity specifications,
    not a different legal shock or proof of conditional randomization.
  estimand: A conditional relative firm outcome change associated with predetermined exposure to the product policy under parallel-trend and interference assumptions; not the nationwide welfare effect or an isolated finance-channel effect.
  treatment_variable: Fixed2006 RebateCore membership interacted with year>=2008; alternative RebateFull and RebateShr do not measure realized rebate receipts.
  comparison_logic: Compare treated and comparison firms' annual changes over2000-2013; pre-policy portfolio differences and non-exporter composition must be addressed rather than erased by the national policy date.
  estimation_notes: >
    The environmental sample requires observations before and after reform:
    34,126 firms,1,725 treated and32,401 controls. Table3 has180,481
    firm-year observations; Table2 export regressions use different samples.
    Table3 reports coefficients -0.016 for total SO2 (insignificant), -0.047
    for total COD, +0.060/+0.030 for SO2/COD intensity and -0.077 for output.
    These are author estimates, not replication or unconditional percentage
    effects: exact log/zero/intensity transformations require code reconciliation.
    Green patent counts are insignificant in Table10; do not turn the proposed
    finance mechanism into a verified decrease in every innovation outcome.
  assumptions:
  - Exposed and comparison firms have comparable counterfactual trends after conditioning despite deliberately targeted products and prior export specialization.
  - Differential global-demand, exchange-rate and domestic regulation shocks do not drive the exposure-outcome relationship.
  - Product vintage, policy membership, exporter status, survey inclusion and firm joins are measured consistently across treatment and comparison firms.
  - Spillovers to controls and product substitution are compatible with the stated relative estimand rather than assumed absent by definition.
  diagnostics:
  - Inspect relative pre-trends and sensitivity to a partially treated2007 reference; distinguish legal effect from the author's post2008 convention.
  - Track subsequent product-rate changes and grandfathering rather than assuming all original cuts persist through2013.
  - Compare exporter-only and broader controls, matching attrition, survey thresholds and balanced versus unbalanced panels with explicit population changes.
  - Assess contemporaneous environmental targets, global-demand exposure and treatment-correlated firm controls, which can themselves be post-treatment outcomes.
threats:
- type: targeted_products_and_differential_trends
  basis: documented
  condition: Product targeting serves pollution/resource and trade-friction objectives. Existing specialization can correlate with later demand and regulation. Prior portfolios are predetermined, not automatically exogenous.
  evidence_refs: [E1, E2, E3]
  possible_diagnostics: [Product and destination-specific trends, Industry-year sensitivity, Untargeted exporter comparison, Concurrent-policy exposure]
- type: timing_persistence_and_contract_exceptions
  basis: documented
  condition: July2007 implementation makes the omitted2007 year partly treated. Notice97 corrections and grandfathered contracts separate legal membership from actual tax losses; later rate increases cannot be excluded for every original product.
  evidence_refs: [E1, E2, E3, E4]
  possible_diagnostics: [Historical rate panels, Contract and export-date checks, Transition-year sensitivity, Reversal-specific treatment paths]
- type: sample_selection_and_data_join
  basis: reported
  condition: Environmental-survey coverage favors major county polluters, ASIF coverage changes, and the baseline retains firms observed on both sides. The paper uses separate export and environmental matches; disappearance need not mean firm closure.
  evidence_refs: [E1, E5]
  possible_diagnostics: [Join coverage by exposure, True non-exporter verification, Entry and exit versus threshold crossing, Balanced-panel population comparison]
- type: confounding_and_mechanism_overinterpretation
  basis: inferred
  condition: Global crisis exposure, environmental enforcement and product demand can co-move with targeted exports. Conditioning on contemporaneous TFP or liquidity can change the estimand. Placebo label permutations do not establish the actual assignment's exogeneity, and credit-access heterogeneity is not random credit supply.
  evidence_refs: [E1]
  possible_diagnostics: [Predetermined-control sensitivity, Destination demand adjustment, Environmental-policy sensitivity, Explicit channel versus total-effect distinction]
empirical_requirements:
  contract_version: 1
  population: Mainland manufacturing firms with reliable2006 export portfolios and annual production data; baseline environmental profile additionally requires a valid AESPF match.
  observation_unit: Firm-year
  geography_level: firm
  time_start: 2000
  time_end: 2013
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields: [export_value_2006_by_product, corrected_policy_product_membership, annual_output, employment, fixed_assets, liquidity, leverage, tfp, so2_emissions, cod_emissions]
  required_identifiers: [firm_id, firm_name, year, product_code, city_id, industry_code]
  treatment_key: [firm_id, product_code, year]
  treatment_source: Notice90 rebate-removal/reduction lists with Notice97 corrections and historically reconciled2006 Customs portfolios; exact author list/code and contract exceptions must be recovered for reproduction.
  measurement_risks:
  - Export outcomes need Customs-ASIF matching; environmental outcomes need AESPF-ASIF matching plus the2006 Customs exposure link. Names, institutional numbers, addresses and contact information are not interchangeable universal IDs.
  - The paper describes top-three products by2006 value but does not provide an inspected machine-readable treatment list, product-code aggregation or tie-handling code. HS changes and multi-digit/range exceptions require historical reconciliation.
  - No public replication code or lawful access to cleaned Customs, ASIF or AESPF microdata was established. The published paper's availability is not permission or assurance of dataset access.
  - NBS states the2011 industrial threshold rose from5million to20million yuan. The paper prints11million and also describes all SOEs in a way that should not be projected unchanged across every sample year.
  - Tables and prose use different shorthand for logged variables and pollution intensity; preserve measured emissions/output and reconcile transformations and zeros before reproduction.
  - Exact membership in pollution-targeted versus other rate adjustments, later reversals and grandfathered contracts must be retained; the paper's persistence claim is not verified for all original goods.
  - Minimum periods are a recall floor for evaluating trends, not a claim that two pre/post observations reproduce the full2000-2013 application.
design_profiles:
- id: manufacturing-pollution
  label: Matched manufacturer pollution and output response
  design_families: [difference-in-differences, event-study]
  when_to_use: Use for SO2 or COD responses when production, environmental-survey and predetermined export exposure can be connected for the same firms.
  outcome_domains: [SO2 emissions and intensity, COD emissions and intensity, Output]
  requirements:
    population: ASIF-AESPF matched mainland manufacturing firms linked to reliable2006 Customs export exposure; non-exporter status must be established separately from missing joins.
    observation_unit: Firm-year
    geography_level: firm
    time_start: 2000
    time_end: 2013
    minimum_frequency: annual
    minimum_pre_periods: 2
    minimum_post_periods: 2
    required_fields: [export_value_2006_by_product, corrected_policy_product_membership, annual_output, so2_emissions, cod_emissions, employment, fixed_assets, liquidity, leverage, tfp]
    required_identifiers: [firm_id, firm_name, year, product_code, city_id, industry_code]
    treatment_key: [firm_id, product_code, year]
- id: manufacturing-exports
  label: Customs-linked manufacturer trade response
  design_families: [difference-in-differences, event-study]
  when_to_use: Use for trade and domestic-substitution outcomes when Customs-ASIF linkage and reliable fixed2006 export portfolios are available; pollution data are not required.
  outcome_domains: [Export value, Dirty-product exports, Domestic sales share, Export participation]
  requirements:
    population: Mainland manufacturing firms in the Customs-ASIF match with reliable2006 product exposure.
    observation_unit: Firm-year
    geography_level: firm
    time_start: 2000
    time_end: 2013
    minimum_frequency: annual
    minimum_pre_periods: 2
    minimum_post_periods: 2
    required_fields: [export_value_2006_by_product, corrected_policy_product_membership, annual_export_value, domestic_sales, employment, fixed_assets, liquidity, leverage, tfp]
    required_identifiers: [firm_id, firm_name, year, product_code, city_id, industry_code]
    treatment_key: [firm_id, product_code, year]
evidence:
- id: E1
  source_type: paper
  citation: 'Lu, Angdi; Jiang Zhang; Jie Li.2023. The impact of export VAT rebate reduction on firms pollution emissions: Evidence from Chinese enterprises. Energy Economics120,106630.'
  url: https://ae.ruc.edu.cn/docs/2023-05/baadc0cd801949d0ae821e1bfb12f04e.pdf
  date: '2023-03-15'
  supports: [scope.china_relevance, identity.instrument, identity.assignment_mechanism, timeline.local_timing, timeline.anticipation, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.intensity, assignment.exposure_construction, design.identifying_variation, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.population, empirical_requirements.time_start, empirical_requirements.time_end, empirical_requirements.required_fields, empirical_requirements.required_identifiers, empirical_requirements.treatment_source, empirical_requirements.measurement_risks, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design]
  verification_status: reported
  access_level: full-text
  locator: Published20-page university-hosted PDF inspected in memory3October2026; p3 Section2.1 policy; p5 Section3.1 top-three2006 construction, footnote4 share formula and Eq4 post2008; p6 Eq5, data and matches; p7 sample; p9 Tables2-3; pp10-13 figures and Tables4-6; pp14-17 channels/Table10; pp18-19 printed appendix. No code or microdata inspected. Legal timing and NBS threshold corrected by E2-E5; heterogeneity prose/table inconsistencies are not copied as verified results.
- id: E2
  source_type: policy-document
  citation: MOF and SAT, 财税〔2007〕90号, 财政部 国家税务总局关于调低部分商品出口退税率的通知, reproduced by MOFCOM.
  url: https://policy.mofcom.gov.cn/claw/clawContent.shtml?id=13441
  date: '2007-06-19'
  supports: [identity.authority, identity.legal_identifiers, identity.implementation_regime, identity.assignment_mechanism, timeline.effective, assignment.rule, assignment.exemptions, assignment.compliance, empirical_requirements.treatment_source]
  verification_status: verified
  access_level: official-document
  locator: >
    Legal text Articles1-4 and attachment inventory inspected3October2026;
    removal/reduction/exemption split, customs export-date clock, registered
    contract exceptions. First page of annex1 rows1-20 and annex2 rows1-19
    visually read from linked images: columns specify new rates, not cuts.
    Full schedule not transcribed or verified; reproduced page includes its
    own source disclaimer, and Notice97 corrections remain necessary.
- id: E3
  source_type: implementation-document
  citation: MOF/SAT, 财税〔2007〕97号, 关于调低部分商品出口退税率的补充通知,10July2007.
  url: https://shanghai.chinatax.gov.cn/zcfw/zcfgk/jckss/200707/t285763.html
  date: '2007-07-10'
  supports: [identity.legal_identifiers, identity.implementation_regime, timeline.local_timing, assignment.rule, assignment.exemptions, assignment.compliance, empirical_requirements.treatment_source, empirical_requirements.measurement_risks]
  verification_status: verified
  access_level: official-document
  locator: Full official tax-site HTML, Articles1-4, inspected3October2026; named code corrections, exclusion of schedules1/3 and already removed/exempt goods from schedule2, contract duration/chapter definitions and transactions retaining prior rates. No claim of empirical exception usage.
- id: E4
  source_type: implementation-document
  citation: MOF News Office, 我国将于7月1日调整部分商品出口退税政策,19June2007.
  url: https://www.mof.gov.cn/zhengwuxinxi/caizhengxinwen/200805/t20080519_26420.htm
  date: '2007-06-19'
  supports: [timeline.announcement, timeline.effective, timeline.anticipation, identity.assignment_mechanism, assignment.exemptions]
  verification_status: verified
  access_level: official-document
  locator: Original19June2007 date and explanatory paragraphs inspected3October2026 despite2008 URL migration; reports18June decision,2831-item package,553 removals/2268 reductions/10 exemptions, objectives and contract transition exceptions. Counts describe legal package, not the firm's empirical treatment list.
- id: E5
  source_type: official-data
  citation: NBS, 关于2011年工业经济效益指标发布情况的说明,27March2011.
  url: https://www.stats.gov.cn/xw/tjxw/tzgg/202302/t20230227_1918602.html
  date: '2011-03-27'
  supports: [empirical_requirements.measurement_risks, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Section3 of official HTML inspected3October2026; confirms2011 coverage threshold increase from5million to20million annual main-business revenue. This contradicts the source paper's p6 printed11million; it does not reveal the authors' implemented cleaning rule.
- id: E6
  source_type: other
  citation: Publisher-deposited Crossref metadata for Lu Zhang Li, Energy Economics120,106630, April2023 issue.
  url: https://doi.org/10.1016/j.eneco.2023.106630
  date: '2023-04'
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: Direct Crossref API inspected3October2026; author names, title, journal,volume120 and article106630 match the published PDF. Crossref issue April2023 differs from PDF online availability15March2023, not the legal2007 treatment date.
design_applications:
- paper: 'The impact of export VAT rebate reduction on firms pollution emissions: Evidence from Chinese enterprises'
  doi: 10.1016/j.eneco.2023.106630
  journal: Energy Economics
  year: 2023
  research_question: How product-targeted export rebate reductions change manufacturers' export, production and environmental outcomes, with conditional finance/technology channel assessment.
  population: Mainland manufacturing firms over2000-2013; Customs-ASIF export and AESPF-ASIF environmental samples are distinct, with baseline environmental firms observed before and after reform.
  outcome: Export value and domestic substitution; SO2/COD levels and emission per output; output, profitability and productivity; optional abatement imports and patents.
  data_used: [Chinese Customs Dataset, ASIF, Annual Environmental Survey of Polluting Firms, Chinese patent data for optional innovation outcomes, City statistical yearbooks for optional credit-access heterogeneity]
  treatment_encoding: Any affected top-three2006 export-value product x post2008; alternatives any affected product and2006 export-value-weighted affected share.
  comparison: Firms without an affected core product including verified non-exporters; exporter-only export results and broader environmental controls must not be treated as one identical population.
  empirical_design: Firm/year-effects DID with city-clustered errors; city effects listed in tables;2007-reference event study and alternative effects/matching in robustness.
  assumptions: [Parallel counterfactual firm trends conditional on observed differences, Comparable survey and matching coverage, Explicit legal and annual timing, No unmodeled differential crisis/regulation driving treatment]
  threats_addressed: [Reported event-study pre-trends,500 random-label placebos, Environmental-target and fee controls, Pre-policy US export share and trade/exchange exposures, Alternative treatment coding, Additional city-year/industry-year effects,1to10 matching, Balanced-panel appendix]
  evidence_refs: [E1, E2, E3, E4, E5, E6]
method_transfer: null
readiness_blockers:
- Establish lawful Customs/ASIF/AESPF access, reliable firm linkage and verified non-exporter status; no cleaned public replication deposit was inspected.
- Recover the actual author treatment list and HS-vintage/tie implementation, reconcile legal exceptions and subsequent rate changes, and distinguish full package from a persistent pollution-targeted subset.
- Reconcile partial2007 treatment, changing industrial coverage, outcome transformations and endogenous controls for the proposed outcome; the application is conditional research knowledge, not a ready-to-run causal guarantee.
---

## Institutional Background

Export VAT rebates return some domestic tax paid on exported goods. Reducing
them changes exporters' costs and cash flow, but also product demand and
domestic-market incentives. Lu, Zhang and Li use the2007 product adjustment
to study mainland manufacturers' trade, production and environmental
responses [E1, reported claim]. This is a product-policy case, separate from
the2004 allocation of refund-financing responsibility to local governments.

## What Changed

Notice90 removes or lowers rebates for listed products and separately
converts other goods to exemption. Its operative date is1July2007, using
the customs export date; specified registered contracts retain previous
rates [E2, verified]. Notice97 corrects codes and defines exceptions [E3,
verified]. The rate in a schedule is the new rate, not the size of its cut.
A researcher measuring tax intensity needs both earlier and later rates.

## Implementation and Assignment

The paper ranks each firm's2006 products by export value and defines
`RebateCore=1` if any of the top three is affected. Its continuous alternative
weights affected products by their2006 export values, not by their count
[E1, reported claim]. Do not substitute a firm's post-reform portfolio:
switching products is a potential response to treatment.

The comparison includes non-exporters and exporters without an affected
core product. An unaffected core does not imply no exposure through smaller
products or suppliers, and a failed Customs match does not prove non-exporter
status [analytical inference]. Product eligibility predicts exposure; it does
not observe a firm's actual refund loss or exemption usage. Exact author
membership, HS aggregation and code remain reproduction conditions.

## Why This Creates Empirical Variation

A common national reform changes costs differently across firms with
different prior product baskets. Eq4 uses fixed exposure interacted with
years2008 onward; Eq5 omits2007. The paper calls2007 the year before its
post period, but legal implementation already covers its second half. Keep
the legal clock distinct from the annual estimating convention [E1-E3].

The paper reports lower output and higher SO2/COD intensity, with a
significant reduction in total COD but an insignificant total-SO2 estimate
in Table3 [E1, reported claim]. A decrease in total emissions can coexist
with dirtier production per unit output. This decomposition is useful for
research decisions; it is not evidence that the policy improves every
environmental or economic outcome. The finance and innovation analyses
remain channels investigated under the same shock, not additional shocks.

## Identification Risks

Products were deliberately targeted. Prior export specialization can predict
later foreign demand, environmental enforcement and production trajectories.
Fixing it in2006 avoids mechanical post-treatment recoding but does not make
it random [E1-E4; analytical inference]. The authors examine pre-trends,
concurrent policies, crisis exposure and alternative specifications. Neither
insignificant pre-trends nor randomly permuting treatment labels establishes
that the actual assignment is exogenous.

Retaining firms observed before and after conditions on continued survey
presence. Coverage thresholds, exit and matching can affect that presence.
Contemporaneous TFP, liquidity and leverage can also be policy outcomes;
conditioning on them can change a total-effect interpretation [analytical
inference]. The national reform's spillovers and product substitution limit
an unaffected-control interpretation. Subsequent reversals must be tracked
rather than assuming every initial cut persists for the whole sample.

## Data Requirements

The export profile needs2006 product values and annual Customs-ASIF outcomes.
The environmental profile additionally needs a reliable AESPF-ASIF match and
its connection to Customs exposure. This distinction prevents pollution data
from becoming mandatory for an export-only query. The paper reports75,465
firms in the export pool and111,474 in the environmental pool; its baseline
environmental regression retains34,126 firms [E1, reported claim]. Those are
different populations, not interchangeable sample counts.

NBS confirms a2011 threshold increase from5million to20million yuan [E5,
verified]. The paper's printed11million is not the official rule. Its
industry and administrative-code harmonization, historic product membership,
log/zero transformations and precise matching implementation need recovery
before numerical reproduction. This record establishes the research-decision
chain and its limits; it does not provide restricted data or replicated results.

## Evidence Notes

E1 is a published full paper with a printed appendix, read from a university
host, not an abstract. E2-E4 ground the policy's legal timing and distinctions;
E5 corrects a material data-description error. Only the first scanned pages
of the two principal schedules were visually read; no complete cleaned legal
list or author code is claimed. Table A3 and its prose disagree on some
heterogeneity signs, so the record does not inherit a uniform industry claim.
Use the DOI to connect with a separate data-asset repository without copying
its canonical data-access records here.
