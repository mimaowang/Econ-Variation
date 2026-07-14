---
schema_version: 2
id: china-export-compulsory-inspection-deregulation
name: China's Export Compulsory Inspection Deregulation (2013)
aliases:
- Export statutory inspection deregulation
- 出口法检取消
- 2013 AQSIQ-GAC Announcement No. 109
- 出入境检验检疫机构实施检验检疫的进出境商品目录调整

status: grounded
provenance:
  task_id: task-308a9748f356
scope:
  country: China
  regions:
  - All customs districts
  domains:
  - trade
  - regulation
  - exports
  - firm-behavior
  - innovation
  - governance
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: >
    The variation is a product-level Chinese trade-regulation reform that
    removed statutory export inspection requirements for 1,507 ten-digit HS
    codes. Exposure is assigned to Chinese exporting firms and products,
    creating a domestic deregulation shock suitable for studying export
    performance, quality upgrading, and innovation.
identity:
  instrument: Removal of compulsory export commodity inspection for 1,507 HS
    codes of general industrial products
  authority: General Administration of Quality Supervision, Inspection and
    Quarantine (AQSIQ) and General Administration of Customs (GAC)
  legal_identifiers:
  - 质检总局、海关总署联合公告2013年第109号
  - Announcement on Adjusting the Catalogue of Entry-Exit Commodities Subject
    to Inspection and Quarantine (2013 No. 109)
  - Based on the Law on Import and Export Commodity Inspection and its
    implementation regulations
  implementation_regime: >
    AQSIQ and GAC jointly announced a one-time adjustment to the inspection
    catalogue. Products under 1,507 HS codes were no longer subject to
    statutory export inspection; 1,420 codes were removed from the export
    inspection catalogue, while 87 codes remained only for exit animal/plant
    quarantine. Hazardous chemicals, fireworks, lighters, toys and strollers,
    food-contact products, automobiles, and rare earths continued to be
    inspected.
  assignment_mechanism: >
    Treatment is assigned at the product level by HS code. Firms exporting
    products whose HS codes were removed from the compulsory export
    inspection list became treated; firms exporting products that remained in
    the list formed the control group. Intensity can be measured by a firm's
    export share in deregulated products.
  parent: null
  related_variations:
  - china-mfa-quota-removal-textile-exporters
  - china-trade-policy-uncertainty
  - china-vat-reform-investment
  - china-wto-accession-firm-performance
timeline:
  announcement: '2013-08-01'
  effective: '2013-08-15'
  implementation_start: 2013
  implementation_end: ongoing
  local_timing: >
    AQSIQ and GAC issued Joint Announcement No. 109 on 1 August 2013. The
    removal of export statutory inspection for 1,507 HS codes took effect on
    15 August 2013. Concurrently, export inspection fees were waived from
    1 August 2013 to 31 December 2013.
  anticipation: >
    The reform was announced two weeks before it took effect. Firms could
    anticipate the removal of inspection requirements and the temporary fee
    waiver, but the exact product list was determined by the announcement.
  last_verified: '2026-07-14'
assignment:
  unit: product-year or firm-year
  treated: >
    Ten-digit HS codes removed from the export compulsory inspection
    catalogue on 15 August 2013, and the firms that exported those products.
  comparison_pool: >
    HS codes that remained subject to export compulsory inspection, and firms
    that exported those products. The same products or firms before 15 August
    2013 provide a pre-period counterfactual.
  rule: >
    Code an HS code as treated from 15 August 2013 onward if it was among the
    1,507 codes removed from the export statutory inspection list. Code a
    firm as treated in a year if it exported treated products; intensity can
    be the share of exports in treated HS codes.
  intensity: >
    Binary at the HS-code level; continuous at the firm-year level (share of
    exports in deregulated HS codes). Some designs may distinguish products
    removed completely from those shifted to animal/plant quarantine only.
  exemptions:
  - Products remaining subject to export inspection (hazardous chemicals,
    fireworks, lighters, toys and strollers, food-contact products,
    automobiles, rare earths)
  - Products subject only to exit animal/plant quarantine (87 HS codes)
  - Non-exporting firms and products outside the catalogue
  compliance: >
    Exporters of treated products no longer needed to obtain an exit cargo
    customs clearance form from inspection and quarantine agencies for
    statutory inspection. Customs continued to monitor excluded products.
  exposure_construction: >
    Merge a firm-product-year export panel with the pre- and post-2013
    inspection catalogue. Assign treated codes based on the 1,507 HS codes
    listed in Announcement No. 109. Construct firm-level intensity as the
    lagged export share in treated codes if using a continuous measure.
  required_identifiers:
  - ten-digit HS code
  - firm identifier
  - calendar year or month
  - export value or quantity
  spillovers: >
    Firms may shift export composition toward treated products. Input-output
    linkages can transmit effects from treated exporters to upstream
    suppliers. Quality or certification reputations may spill across products
    within a firm.
research_compatibility:
  outcome_domains:
  - export volume
  - export quality
  - export extensive margin
  - firm innovation
  - total factor productivity
  - governance efficiency
  - customs clearance time
  - trade costs
  affected_populations:
  - Chinese exporting firms
  - export intermediaries
  - manufacturers in deregulated sectors
  - customs and inspection agencies
  mechanism_channels:
  - reduction of regulatory compliance costs
  - faster customs clearance
  - reallocation of managerial resources
  - quality upgrading
  - innovation response
  - input substitution
  best_for:
  - Product-level or firm-level difference-in-differences designs
  - Studies linking customs transaction data to regulatory catalogues
  - Research on deregulation and export performance in China
  not_good_for:
  - Identifying effects for exempt products that remained under inspection
  - Outcomes that cannot be matched to HS codes or firm identifiers
  - Designs that cannot separate the inspection removal from the concurrent
    fee waiver or other 2013 trade-facilitation measures
design:
  claim_type: causal
  affordances:
  - sharp product-level treatment defined by an official HS-code list
  - large one-time removal covering about 70% of export inspection codes
  - availability of Chinese customs transaction data
  - pre-existing statutory inspection regime provides a clear baseline
  - can be combined with firm financial and patent data
  candidate_designs:
  - difference-in-differences at the HS-code level
  - difference-in-differences at the firm-year level with share-based intensity
  - triple-difference exploiting heterogeneous pre-reform inspection intensity
  - event study around August 2013
  identifying_variation: >
    The removal of 1,507 HS codes from the compulsory export inspection
    catalogue on 15 August 2013, while other codes remained subject to
    inspection.
  primary_strategy: >
    Difference-in-differences comparing treated and control HS codes (or
    firms) before and after 15 August 2013, with product and time fixed
    effects and clustered standard errors.
  estimand: >
    The average effect of being removed from compulsory export inspection on
    export outcomes, relative to products that remained under inspection,
    under a parallel-trends assumption.
  treatment_variable: >
    An indicator for an HS code (or a firm's export bundle) being removed
    from compulsory export inspection after 15 August 2013; alternatively,
    the share of exports in removed HS codes.
  comparison_logic: >
    Removed HS codes after August 2013 are compared with the same codes
    before removal and with HS codes that were never removed.
  estimation_notes: >
    Use HS-code and year fixed effects; include product-level controls for
    initial inspection intensity, export value, and sector. Cluster at the
    HS-code or firm level. For firm-level outcomes, use lagged export-share
    weights to reduce endogenous product-mix responses.
  assumptions:
  - Parallel trends for treated and control HS codes absent the reform
  - The reform is not systematically correlated with pre-existing export
    trends of removed products
  - Concurrent fee waiver and trade-facilitation measures do not
    differentially affect treated and control products
  - Product reclassification does not drive the results
  diagnostics:
  - Pre-trends in event-study plots
  - Placebo reform dates
  - Robustness to alternative control groups
  - Sensitivity to continuous vs. binary treatment
  - Tests for product switching within firms
threats:
- type: selection-into-treatment
  basis: inferred
  condition: >
    The 1,507 removed HS codes may have been selected because they were
    low-risk, low-inspection-intensity, or had stronger export trends,
    creating baseline differences with remaining codes.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Test for pre-trends in export outcomes
  - Match on pre-reform inspection intensity and export characteristics
  - Control for sector-specific trends
- type: confounding-policies
  basis: documented
  condition: >
    A temporary waiver of export inspection fees ran from 1 August 2013 to
    31 December 2013, and the State Council's broader trade-facilitation
    package was announced in late July 2013.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Control for fee-waiver period
  - Compare effects after the fee waiver ended
  - Include month fixed effects and policy-package controls
- type: anticipation
  basis: inferred
  condition: >
    The announcement was made two weeks before implementation; firms may have
    delayed or advanced shipments.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Examine monthly export patterns around July-August 2013
  - Exclude a short window around the announcement
- type: product-switching
  basis: inferred
  condition: >
    Firms may shift exports toward deregulated products, biasing intent-to-
    treat estimates and changing product composition.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Use lagged export-share weights
  - Estimate effects on the extensive margin separately
  - Test for changes in firm product mix
- type: measurement-error
  basis: inferred
  condition: >
    Export quality is inferred from unit values or other proxies, and HS-code
    reclassifications may affect treatment assignment.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Sensitivity to quality measures
  - Use stable HS codes across years
  - Compare results at different levels of aggregation
empirical_requirements:
  contract_version: 1
  population: Chinese exporting firms and their ten-digit HS-code products
    observed before and after August 2013.
  observation_unit: product-year or firm-year
  geography_level: national customs data
  time_start: 2010
  time_end: 2016
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields:
  - outcome (export value, quantity, quality proxy, innovation measure)
  - ten-digit HS code
  - firm identifier
  - calendar year or month
  - pre-reform inspection status
  - firm/product controls
  required_identifiers:
  - HS code
  - firm identifier
  - year
  treatment_key:
  - HS code
  - year
  treatment_source: >
    The list of 1,507 removed HS codes from AQSIQ/GAC Joint Announcement
    No. 109 (2013). Export transaction data come from Chinese customs
    records; firm financials and patents from CSMAR or the National
    Intellectual Property Administration; quality proxies from customs unit
    values.
  measurement_risks:
  - HS-code reclassifications may shift codes in and out of the treatment list
  - Export-quality proxies based on unit values are noisy
  - Inspection catalogue attachments must be manually digitized
  - Temporary fee waiver may confound short-run estimates
  - Product switching within firms can alter intensity measures
evidence:
- id: E1
  source_type: policy-document
  citation: >
    General Administration of Quality Supervision, Inspection and Quarantine
    and General Administration of Customs. 2013. "Announcement on Adjusting
    the Catalogue of Entry-Exit Commodities Subject to Inspection and
    Quarantine" (Joint Announcement No. 109).
  url: https://www.ks.gov.cn/kss/cpzl/201308/ce438f67154d41eeaaebabed0505c2c5.shtml
  date: '2013-08-01'
  supports:
  - identity
  - timeline
  - assignment
  verification_status: verified
  access_level: official-document
  locator: >
    Kunshan government reproduction of AQSIQ/GAC Joint Announcement No. 109;
    states that 1,507 HS codes of general industrial products are removed
    from export statutory inspection, effective 15 August 2013, and lists
    products that remain under inspection.
- id: E2
  source_type: paper
  citation: >
    Yang, Zhiqing, Zhiyuan Zhu, Peiyao Liu, and Lianfa Luo. 2026. "The
    effectiveness of entry deregulation: Quasi-experimental evidence from
    China's export compulsory inspection deregulation." Journal of
    Development Economics 103873.
  url: https://doi.org/10.1016/j.jdeveco.2026.103873
  date: 2026
  supports:
  - design_applications
  - design
  - assignment
  verification_status: reported
  access_level: abstract
  locator: >
    Published abstract and SSRN working-paper summary; reports 8,799
    firm-level observations from matched customs and other data sources, a
    DID design, and findings that deregulation increased export volume,
    export quality, and firm innovation.
design_applications:
- paper: The effectiveness of entry deregulation
  doi: 10.1016/j.jdeveco.2026.103873
  journal: Journal of Development Economics
  year: 2026
  research_question: >
    How does removing compulsory export inspection affect export volume,
    export quality, and firm innovation?
  population: Chinese exporting firms, 8,799 firm-level observations
  outcome: Export volume, export quality, and firm innovation
  data_used:
  - Chinese customs transaction data
  - Export compulsory inspection catalogue
  - Ten-digit HS code concordance
  - Firm financial or patent data
  - Four matched data sources
  treatment_encoding: HS code removed from compulsory export inspection list
    after 15 August 2013
  comparison: Firms/products that remained subject to compulsory export
    inspection
  empirical_design: Difference-in-differences at the firm or product level
  assumptions:
  - Parallel trends between treated and control products
  - No concurrent shock differentially affects removed products in 2013
  - Product removal is exogenous to firm-level innovation shocks
  threats_addressed:
  - Parallel trends via DID
  - Mechanism analysis on innovation capacity
  - Robustness checks reported by authors
  evidence_refs:
  - E2
readiness_blockers:
- >
  The exact list of 1,507 ten-digit HS codes has not been digitized from the
  announcement attachments inside this record.
- >
  Full replication materials have not been inspected; treatment coding and
  sample construction details rely on the published abstract.
- >
  The temporary fee waiver from August to December 2013 has not been
  separately controlled for in this record.
method_transfer: null
---
## Institutional Background

China's export compulsory inspection system required exporters of designated
products to obtain an exit cargo customs clearance form from inspection and
quarantine agencies before shipment. The system covered a broad catalogue of
industrial products and was administered by AQSIQ and GAC. [E1]

## What Changed

On 15 August 2013, AQSIQ and GAC removed 1,507 ten-digit HS codes of general
industrial products from the compulsory export inspection catalogue. About
70% of the codes previously subject to export inspection were deregulated,
while hazardous chemicals, fireworks, lighters, toys and strollers,
food-contact products, automobiles, and rare earths remained under
inspection. [E1]

## Implementation and Assignment

The reform assigned treatment at the product level by HS code. Exporters of
deregulated products no longer needed statutory inspection; exporters of
remaining products continued to face inspection requirements. Assignment was
not randomized: the removed codes were selected by regulators, but the large,
official list provides a clear treatment-control split. [E1]

## Why This Creates Empirical Variation

The removal created a sharp, product-level deregulation shock. Researchers can
compare export outcomes for treated and control HS codes before and after
August 2013, exploiting the fact that the reform affected a large share of
export inspection codes at a single date. [E1; E2]

## Identification Risks

Removed products may differ systematically from retained products in baseline
risk or export trends. The concurrent waiver of inspection fees and the
State Council's trade-facilitation package may confound short-run estimates.
Firms may anticipate the announcement or shift exports toward deregulated
products. [E1; E2]

## Data Requirements

Researchers need the official list of removed HS codes, Chinese customs
transaction data with firm and HS-code identifiers, and outcome measures such
as export value, quantity, and quality proxies. Firm-level innovation data
require matching with patent or R&D records. [E1; E2]

## Evidence Notes

E1 verifies the announcement, effective date, scope, and exceptions of the
export inspection deregulation. E2 reports a DID application using matched
customs and firm data; its treatment coding and sample construction have not
been verified from replication materials.
