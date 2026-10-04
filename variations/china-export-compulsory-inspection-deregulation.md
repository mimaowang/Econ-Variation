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
  task_id: task-cd44ea2bed2a
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
    Legal exposure is assigned to listed product codes. Translating this
    into a firm contrast requires a baseline export basket and explicit
    multiproduct rules. Firms exporting retained codes are a proposed
    comparison, not a verified author comparison pool. Predetermined
    export shares can measure exposure, but actual paper weights are unknown.
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
    1 August 2013 to 31 December 2013 under a separate fiscal instrument;
    MOF/NDRC continued the waiver for calendar2014. Inspection removal and
    fee relief must not be treated as the same assignment.
  anticipation: >
    The reform was announced two weeks before it took effect. Firms could
    anticipate the removal of inspection requirements and the temporary fee
    waiver, but the exact product list was determined by the announcement.
  last_verified: '2026-10-04'
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
    firm's exposure using a stated baseline basket or another justified
    rule; a pre-reform treated-product share is one possible construction,
    not a verified encoding from the2026 paper. Annual2013 coding needs
    explicit partial-year handling rather than silently applying full treatment.
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
    Export commodity inspection ceased for the specified codes, but the87
    retained animal/plant quarantine codes and dangerous-goods packaging
    controls must not be coded as complete withdrawal of border oversight.
    Operational clearance-document changes require their own implementation
    source; the legal removal does not establish every port's practice.
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
    within a firm. A contemporaneous treated-product share can itself
    respond to deregulation; do not silently use it as predetermined exposure.
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
    The authors' institution reports a firm-level DID application mapping
    ten-digit HS codes to firm identifiers. Exact fixed effects, sample
    window, standard-error clustering and multiproduct assignment have not
    been inspected. Product-level DID is a possible application of the legal
    list, not a verified description of that paper.
  estimand: >
    The average effect of being removed from compulsory export inspection on
    export outcomes, relative to products that remained under inspection,
    under a parallel-trends assumption.
  treatment_variable: >
    An indicator for an HS code (or a firm's export bundle) being removed
    from compulsory export inspection after 15 August 2013; alternatively,
    the share of exports in removed HS codes.
  comparison_logic: >
    An analytical application compares removed codes before/after the reform
    with codes remaining under inspection, conditional on a credible common
    trend. The published paper's actual firm comparison, eligibility rules
    and mixed-product treatment remain to be recovered from methods.
  estimation_notes: >
    Use HS-code and year fixed effects; include product-level controls for
    initial inspection intensity, export value, and sector. Cluster at the
    HS-code or firm level. For firm-level outcomes, use lagged export-share
    weights to reduce endogenous product-mix responses. These are analytical
    design suggestions, not inspected author specifications. The legal date
    does not dictate whether2013 is a fully treated annual observation.
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
    A separate export-inspection fee waiver overlapped the2013 removal.
    MOF/NDRC document2014 No.6 continued relief through31 December2014 for
    all covered outbound goods and other statutory inspection objects, with
    exceptions. Waiting until January2014 does not remove this confound.
  evidence_refs:
  - E3
  - E5
  possible_diagnostics:
  - Compare pre-reform fee burdens and their changes across product groups
  - Separate inspection obligations from statutory fees and commercial testing
  - Verify successor fee rules before choosing a supposedly fee-free comparison
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
  - E4
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
  - E4
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
    AQSIQ/GAC2013 No.109 annex1 for1,420 removed codes and annex3 for87 codes
    retaining exit animal/plant quarantine. Recover original codes, their
    historical concordance and baseline inspection obligations. The author's
    institution reports four micro-databases linked through ten-digit HS and
    firm identifiers, but does not name all four or establish their merge
    coverage. Customs outcomes and firm patent data are possible inputs;
    CSMAR, particular patent sources and quality-estimation procedures are
    not confirmed paper-used sources. The2010-2016 contract and minimum
    pre/post periods are planning requirements, not verified paper dates.
  measurement_risks:
  - HS-code reclassifications may shift codes in and out of the treatment list
  - Export-quality proxies based on unit values are noisy
  - Original annex code tables and their version concordance remain uninspected
  - Overlapping fee relief continued through2014; its later path needs verification
  - Product switching within firms can alter intensity measures
evidence:
- id: E1
  source_type: policy-document
  citation: >
    General Administration of Quality Supervision, Inspection and Quarantine
    and General Administration of Customs. 2013. "Announcement on Adjusting
    the Catalogue of Entry-Exit Commodities Subject to Inspection and
    Quarantine" (Joint Announcement No. 109).
  url: https://m.cqn.com.cn/zj/content/2013-08/01/content_1903720.htm
  date: '2013-08-01'
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.announcement
  - timeline.effective
  - assignment.rule
  - assignment.exemptions
  verification_status: verified
  access_level: official-document
  locator: >
    Full AQSIQ/GAC announcement reproduced by China Quality News, inspected
    October4,2026: heading/date, paragraph1, paragraph2, commencement sentence
    and annex labels. Paragraph1 distinguishes1,420 removed codes from87
    retaining exit animal/plant quarantine and preserves specified industrial
    inspection and dangerous-goods packaging requirements. Paragraph2 adds
    two import lignite codes, outside this export case. Annex1/3 links404;
    individual codes were not inspected. Earlier Kunshan source timed out
    on this audit; its prior inspection is not presented as current access.
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
  - design_applications.paper
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
  verification_status: verified
  access_level: metadata
  locator: >
    Crossref DOI metadata read directly October4,2026 confirms four authors,
    JDE183, article103873, September2026 issue. Publisher full text was not
    recovered; SSRN5531502 delivery returned403. The earlier record blended
    an8,799-observation working-summary claim with this final DOI. That
    number and a positive quality effect are not retained as final findings.
- id: E3
  source_type: policy-document
  citation: MOF and NDRC.2014. 关于2014年继续免收出口商品检验检疫费的通知, 财综[2014]6号.
  url: https://zhs.mof.gov.cn/zhengcefabu/201402/t20140212_1042453.htm
  date: '2014-01-27'
  supports: [timeline.local_timing, threats.condition, empirical_requirements.measurement_risks]
  verification_status: verified
  access_level: official-document
  locator: >
    Full ministry text inspected October4,2026, title/legal identifier,
    paragraph1 and signature. Calendar2014 relief covers outbound goods,
    transport, containers and other statutory objects, with specified
    personal-health, commercial voluntary-testing and quarantine-treatment
    exceptions. Signed January27; web publication February12. This source
    establishes2014 continuation, not the fee regime after2014.
- id: E4
  source_type: other
  citation: HUST School of Public Administration.2026. 公管学院杨芷晴团队关于政府监管的研究获进展.
  url: https://cpa.hust.edu.cn/info/1602/14419.htm
  date: '2026-07-19'
  supports: [design.primary_strategy, design_applications.population, design_applications.outcome, design_applications.data_used, design_applications.empirical_design]
  verification_status: reported
  access_level: full-text
  locator: >
    Full author-institution research announcement inspected October4,2026,
    research summary paragraph (after the policy-background paragraph):
    reports8,700 observations, ten-digit HS-to-firm linkage, four micro-data
    sources and DID. Reports positive export and innovation effects, without
    a significant quality decline measured by willingness to pay. This is
    not paper methods: no database names, exposure weights, comparison,
    sample dates, fixed effects or diagnostics are recovered.
- id: E5
  source_type: policy-document
  citation: MOF and NDRC.2013. 关于免收出口商品检验检疫费等有关问题的通知, 财综[2013]85号.
  url: https://czt.fujian.gov.cn/ztzl/xzsyxsfmlqd/201309/P020180317410507938327.tif
  date: '2013-08-15'
  supports: [timeline.local_timing, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: >
    Two-page original stamped MOF/NDRC scan linked from Fujian Finance's
    September1,2013 forwarding entry. Both frames read visually in memory
    October4,2026. Page1 title/identifier and paragraph1 specify August1 to
    December31,2013 relief for all outbound goods, transport, containers and
    other statutory objects. Page2 completes personal-health/commercial
    voluntary-testing/quarantine-treatment exceptions; paragraph2 preserves
    agency statutory functions through central budget funding. Signed
    August15; printed August19. Fee relief does not abolish inspection duties.
design_applications:
- paper: The effectiveness of entry deregulation
  doi: 10.1016/j.jdeveco.2026.103873
  journal: Journal of Development Economics
  year: 2026
  research_question: >
    How does removing compulsory export inspection affect export volume,
    export quality, and firm innovation?
  population: Chinese exporting firms; author-institution summary reports8,700 firm-level observations, not8,700 unique firms
  outcome: Exports, willingness-to-pay-based quality and innovation; no significant quality decline is not evidence of a positive quality effect
  data_used:
  - Ten-digit HS-to-firm linkage is reported; original code mapping uninspected
  - Four micro-databases are reported; complete names and joins await methods
  treatment_encoding: >
    The legal exposure follows listed ten-digit HS codes from15 August2013.
    The paper's baseline firm mapping, multiproduct eligibility, weights and
    annual2013 treatment convention remain uninspected.
  comparison: Published firm comparison and exclusions remain uninspected; retained-inspection products are an analytical comparison proposal
  empirical_design: Firm-level DID reported by the author's institution; specification uninspected
  assumptions:
  - Parallel trends between treated and control products
  - No concurrent shock differentially affects removed products in 2013
  - Product removal is exogenous to firm-level innovation shocks
  threats_addressed:
  - Not verified; using DID alone does not establish parallel trends
  evidence_refs:
  - E2
  - E4
readiness_blockers:
- >
  Original annex1/3 code tables have not been inspected; current reproduction
  links return404. Recover both the1,420-code and87-code components and HS
  version concordances before encoding treatment.
- >
  Full paper methods and replication materials have not been inspected.
  Exact paper-used firm assignment, baseline shares, mixed-product rules,
  comparison pool, four data sources, sample dates, quality construction
  and diagnostics remain unresolved. An institution's research summary is
  not a substitute for these details.
- >
  The separate fee relief, including its2014 continuation, has not been
  disentangled from inspection removal in inspected paper methods.
method_transfer: null
---
## Institutional Background

The pre-reform catalogue imposed export commodity inspection on designated
products. AQSIQ/GAC adjusted that catalogue in response to the government's
export-growth and restructuring agenda; neither that objective nor the broad
scale of withdrawal makes the selected products randomly assigned. [E1]

## What Changed

Announcement109, signed1 August2013 and effective15 August, ended export
commodity inspection for1,507 codes. Only1,420 left the catalogue altogether;
87 retained exit animal/plant quarantine. Industrial exclusions and dangerous
goods packaging controls remained. The same notice's two import lignite
codes are outside this export-removal case. [E1]

## Implementation and Assignment

Legal assignment is code-specific, but the original annex tables still need
inspection. A firm can export removed, retained and never-inspected products
simultaneously. Its binary status or baseline-share intensity is therefore a
second mapping decision, not something determined by the reform's name.
The published application's exact mapping remains uninspected. [E1; E4,
reported claim; analytical inference]

## Why This Creates Empirical Variation

A product contrast follows from the code list and date. The author's
institution reports a firm DID application with8,700 observations assembled
from four micro-databases. It reports export and innovation gains without
a significant decline in willingness-to-pay-based quality. That last finding
is not a positive quality effect; neither8,700 observations nor the DID label
reveals the number of unique firms or proves parallel trends. [E4, reported
claim] A baseline exposure can avoid mechanically incorporating later product
switching, but this is design reasoning, not inspected author code.
[analytical inference]

## Identification Risks

Removed and retained products can differ in risk and growth, and firms can
anticipate or change their product mix. Those concerns require outcome-specific
diagnostics rather than assuming the code list is exogenous. [analytical
inference] Separate fee relief continued through calendar2014, so treating
2014 as automatically free of the fee confound would be wrong. Examine whether
baseline fees and their reductions differed across the comparison groups;
do not replace this question with a common-year dummy. [E3; analytical inference]

## Data Requirements

Start with the two export annexes, historical code concordances, firm-product
identifiers and pre-reform inspection status. Outcome panels must distinguish
regulatory assignment from product switching. Patent/R&D joins and demand-based
quality construction need separate verification; the institutional summary
does not identify all four micro-databases or their merge attrition. The default
time contract above is a planning window, not the paper's established sample.
[E1; E4, reported claim; analytical inference]

## Evidence Notes

E1 is the inspected legal text, not the missing code-table contents. E2 verifies
publication metadata only; E4 preserves the author's institution's reported
application with its narrower access boundary. The former record mixed an
8,799-observation working summary and a positive quality claim into the2026
publication. This audit corrects that attribution without claiming to have read
the final methods. E3 establishes2014 fee continuation. Original annexes,
paper methods and replication remain explicit blockers; status stays grounded
with conditional use, not design-documented or replication-verified.
