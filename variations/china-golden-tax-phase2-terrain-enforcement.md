---
schema_version: 2
id: china-golden-tax-phase2-terrain-enforcement
name: Golden Tax Phase II Invoice Enforcement Interacted with County Terrain Ruggedness in China
aliases: [Golden Tax county ruggedness, 金税二期地形征管冲击, Liu Zhao fiscal capacity and capital misallocation]
status: grounded
provenance:
  task_id: task-9cd88f48e4da
scope:
  country: China
  regions: [Mainland Chinese counties]
  domains: [digital-economy, public-finance, firm, institutions, regional-economics]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: National computer-assisted VAT invoice enforcement changes the importance of physical inspection costs in Chinese counties. A mainland industrial-firm application compares outcomes across pre-existing terrain ruggedness, linking fiscal capacity to firm investment and spatial capital allocation.
identity:
  instrument: Golden Tax Phase II anti-counterfeit special VAT invoicing and computerized invoice cross-checking, with phased mandatory use by general VAT taxpayers
  authority: State Council General Office and State Administration of Taxation; implementation by local state tax offices
  legal_identifiers: [国办发〔2000〕12号, 国税发〔2000〕183号, 国税函〔2003〕139号]
  implementation_regime: National phased conversion from handwritten special VAT invoices; major-invoice requirements in 2002 and general-taxpayer completion rules in 2003. This is not the later Golden Tax Phase III rollout or the 2009 equipment-input-credit reform.
  assignment_mechanism: The paper interacts a common post-2002 period with pre-existing county terrain ruggedness, which proxies the cost of physical tax inspections before computerized invoice matching. Rugged counties are predicted to experience a larger enforcement improvement; ruggedness is not a legal eligibility criterion or a randomly allocated tax rate.
  parent: null
  related_variations: [china-vat-reform-investment, china-wto-accession-firm-performance]
timeline:
  announcement: '2000-02-12'
  effective: '2002-01-01'
  implementation_start: 2000
  implementation_end: null
  local_timing: Notice183 mandates system issuance of special invoices above RMB10000 from January2002 and removes handwritten ten-thousand-version input-credit eligibility from April2002. Notice139 later sets July2003 general-taxpayer issuance and October2003 handwritten-credit deadlines. The paper codes Post=1 from2002; this annual coding is not a verified date of full adoption in every county.
  anticipation: National authorization in February2000 and the November2000 phase-in notice predate2002; equipment installation and network connection may change behavior earlier. The paper reports nationwide network connection in2001. Inspect transition-year dynamics rather than assume an unannounced January2002 shock.
  last_verified: '2026-09-29'
assignment:
  unit: County exposure assigned to firms through county location; county-year aggregates are a separate outcome panel
  treated: More rugged mainland counties and firms located there experience greater predicted reductions in inspection-related enforcement costs after2002
  comparison_pool: Less rugged counties and their firms in the same national reform; they are lower-intensity exposed units, not untreated counties
  rule: General VAT taxpayers must install and use the anti-counterfeit system under notices12/183/139. The statutory mandate is national and phased; the empirical intensity is the paper's county geography proxy, not county designation or local adoption chosen by the researcher.
  intensity: Log standard deviation of ground elevation across GTOPO30 cells in each county, standardized to mean zero and SD one; interact with the indicator year>=2002
  exemptions: [Small-scale taxpayers are not covered by the general-taxpayer installation mandate in the same way, Notice139 allows tax offices to continue issuing handwritten special invoices on behalf of small-scale taxpayers, Transitional handwritten invoices have different issuance and deduction deadlines]
  compliance: Installation and authentication obligations are statutory; paper exposure predicts enforcement costs and does not observe individual adoption dates or administrative firm-level remittances. Do not assume the project eliminated every physical audit or every opportunity for evasion.
  exposure_construction: Overlay GTOPO30 30-arcsecond elevation cells on harmonized county polygons, compute log elevation SD and standardize using a documented county sample. Join county exposure to annual firm locations and set Post=1 in2002-2007, zero in1998-2001. Baseline firm analysis removes changing county IDs; county outcomes require separate stable-geography aggregation. Preserve the paper's phased timing rather than invent staggered pilot cohorts.
  required_identifiers: [Harmonized county code and polygon, Firm panel ID, Firm county location, Year, Four-digit industry code]
  spillovers: Capital can shift between counties and entrants can select different locations. A relative high/low-ruggedness contrast includes spatial reallocation and does not identify the nationwide total effect without further assumptions.
research_compatibility:
  outcome_domains: [Effective VAT burden, Firm capital, Firm entry and exit, Spatial capital allocation, Productivity and MRPK dispersion]
  affected_populations: [Mainland industrial firms in ASIF, County-level industrial establishments, Registered firms for the separate SAIC entry check]
  mechanism_channels: [Lower invoice-matching costs, Reduced dependence on physical tax inspections, More uniform enforcement, Investment and location adjustment]
  best_for: [Testing heterogeneous digital enforcement effects with a long pre/post industrial panel, Studying whether tax enforcement changes spatial capital allocation]
  not_good_for: [Estimating Golden Tax Phase III city-pilot effects, Treating terrain as an unconditional instrument for any firm outcome, Inferring a national average effect from a relative-intensity coefficient, Treating ASIF appearance as legal business creation]
design:
  claim_type: reduced-form
  affordances: [Predetermined geographic exposure, Common phased national reform, Firm and county panels with pre-reform observations]
  candidate_designs: [Continuous-exposure difference-in-differences, Ruggedness-by-year event study, Supplementary IV for effective VAT rates under a stronger exclusion restriction]
  identifying_variation: Differential pre/post changes across counties with different terrain-related pre-reform inspection costs; county ruggedness itself can affect firms through many non-tax channels
  primary_strategy: Firm-year or county-year continuous-exposure DID using standardized ruggedness x Post2002
  estimand: Relative change in the specified outcome associated with one SD higher county ruggedness after the reform, conditional on comparable counterfactual trends; not the average national treatment effect or an unconditional effect of fiscal capacity
  treatment_variable: Standardized county log elevation SD x indicator(year>=2002)
  comparison_logic: Compare changes in more-rugged and less-rugged counties, all subject to national reform; year interactions use2001 as the reference in the inspected application
  estimation_notes: Manuscript equations2-3 use firm or county fixed effects, year effects and baseline county export intensity/population density/log GDP per capita interacted with year. Cluster at county level. Table3 additionally instruments county effective VAT rate with ruggedness x Post; first stage is differential effective-rate growth, exclusion requires no other terrain-correlated reform effect on capital, and its F statistics are reported rather than independently replicated.
  assumptions:
  - Without the reform, outcome trends across geographic exposure would be comparable after the specified baseline controls.
  - WTO changes, state-sector restructuring and infrastructure or digital expansion do not independently create a coincident ruggedness-related break.
  - County polygons and firm locations encode stable exposure; outcome reporting and sample entry do not mechanically generate the contrast.
  - Supplementary IV needs the stronger condition that exposure affects capital only through the instrumented effective VAT burden; reduced-form DID alone does not establish it.
  diagnostics:
  - Estimate ruggedness-by-year coefficients with2001 reference; check1998-2001 and transitional2002-2003 separately.
  - Compare VAT credits/payments with inputs/domestic sales and administrative county revenue; do not equate self-report agreement with validated remittance.
  - Inspect non-exporter and domestic-private samples, trade-exposure controls and industry-year effects.
  - Compare ASIF entry with SAIC registrations and examine sample-threshold crossing and county changes.
  - Inspect infrastructure controls and continuous-treatment assumptions; the manuscript reports an available-on-request binary-exposure check, not inspected replication output.
threats:
- type: terrain-correlated-concurrent-shocks
  basis: documented
  condition: WTO accession, SOE restructuring and infrastructure growth overlap the reform and can affect rugged/flat counties differently. Manuscript robustness checks address specific channels but do not prove the absence of all confounding breaks.
  evidence_refs: [E3]
  possible_diagnostics: [Trade-exposure-by-year controls, Domestic-private and non-exporter samples, Infrastructure trends and spending, Within-county distance contrast with a separately reconstructed data contract]
- type: phased-compliance-and-anticipation
  basis: documented
  condition: Published mandates precede2002 and general-taxpayer conversion continues in2003. One annual Post dummy cannot represent every firm's actual installation or first enforceable invoice.
  evidence_refs: [E1, E2, E3]
  possible_diagnostics: [Transition-year exclusions, Event coefficients, Recover actual installation or invoice-size exposure if the new question requires them]
- type: self-report-and-survey-selection
  basis: documented
  condition: ASIF VAT and sales are self-reported; its non-state sales threshold can change observed entry and capital composition. The paper explicitly distinguishes this from administrative remittances and uses registered-entry and county-revenue checks.
  evidence_refs: [E3]
  possible_diagnostics: [Alternative effective-rate denominators, County revenue evidence, Registered-entry counts, Threshold and balanced-panel sensitivity]
- type: geographic-sorting-and-spatial-displacement
  basis: inferred
  condition: Excluding changing county IDs does not identify every relocation or remove changing entrant composition. Capital moving between comparison counties means relative effects cannot be added as independent national effects.
  evidence_refs: [E3]
  possible_diagnostics: [Stable boundary crosswalk, Distinguish continuing firms from entrants, Registration location histories, Alternative spatial aggregation]
empirical_requirements:
  contract_version: 1
  population: ASIF state industrial firms and non-state industrial firms with annual sales above RMB5million in mining/manufacturing/power,1998-2007; baseline excludes firms whose county IDs change
  observation_unit: Firm-year
  geography_level: County exposure linked to firms
  time_start: 1998
  time_end: 2007
  minimum_frequency: annual
  minimum_pre_periods: 4
  minimum_post_periods: 6
  required_fields: [VAT reported by firm, Total sales, Firm capital and relevant price deflator for investment outcomes, Firm county, Industry, Ownership and exports, County elevation SD, Baseline2000 county export intensity population density and GDP per capita]
  required_identifiers: [Firm panel ID, Year, Harmonized county code and polygon, Four-digit industry code]
  treatment_key: [County standardized ruggedness, Post2002]
  treatment_source: GTOPO30 elevation raster over historical/harmonized county polygons; national invoice mandates establish phased timing. The paper's empirical Post2002 is an annual application choice, not an observed county adoption table.
  measurement_risks: [ASIF VAT/sales is not an administrative payment rate or the statutory VAT rate, County boundary vintage and elevation-grid weights must be recovered, Log elevation SD requires a documented convention for flat or missing cells, Sales-threshold crossing can mimic entry or exit, Restricted firm identifiers and incomplete survey linkage, Standardization sample changes the numerical one-SD interpretation]
design_profiles:
- id: county-capital-entry
  label: County-level capital and firm-entry application
  design_families: [Continuous-exposure DID]
  when_to_use: The question concerns county aggregate capital or formal entry rather than continuing-firm outcomes
  requirements:
    population: Industrial capital aggregated from ASIF; legal new-registration counts from SAIC are a separate outcome definition
    observation_unit: County-year
    geography_level: County
    time_start: 1998
    time_end: 2007
    minimum_frequency: annual
    minimum_pre_periods: 4
    minimum_post_periods: 6
    required_fields: [County aggregate deflated net fixed assets or registration counts for the chosen outcome, County elevation SD, Baseline2000 county export intensity population density and GDP per capita]
    required_identifiers: [Harmonized county code and polygon, Year, Registration ID and incorporation date when constructing legal entry]
    treatment_key: [County standardized ruggedness, Post2002]
evidence:
- id: E1
  source_type: policy-document
  citation: State Administration of Taxation. 关于推行增值税防伪税控系统若干问题的通知, 国税发〔2000〕183号,2000-11-09; attachment reproduces 国办发〔2000〕12号,2000-02-12.
  url: https://shanghai.chinatax.gov.cn/zcfw/zcfgk/zzs/200803/t287439.html
  date: '2000-11-09'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.announcement, timeline.effective, timeline.local_timing, timeline.anticipation, assignment.rule, assignment.compliance, assignment.exemptions]
  verification_status: verified
  access_level: official-document
  locator: Inspected2026-09-29; notice sectionI(1)-(2) on2002/2003 planned issuance/deduction deadlines and attachment1 sectionsI-III on installation and authentication. Web upload2008 is not legal issue date; archived validity annotations do not replace the historical text. Later2003 rules modify completion timing.
- id: E2
  source_type: implementation-document
  citation: State Administration of Taxation. 关于进一步明确推行防伪税控系统和金税工程二期完善与拓展有关工作的通知, 国税函〔2003〕139号,2003-02-14.
  url: https://zhejiang.chinatax.gov.cn/art/2003/2/14/art_8409_15252.html
  date: '2003-02-14'
  supports: [identity.legal_identifiers, identity.implementation_regime, timeline.local_timing, assignment.rule, assignment.exemptions, assignment.compliance, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Inspected2026-09-29; sectionI general-taxpayer July issuance/October deduction deadlines and tax-office small-scale exception; sectionsII-III shared issuance and software deployment. This is a national SAT notice reproduced by Zhejiang, not a Zhejiang pilot rule.
- id: E3
  source_type: paper
  citation: Liu,Yu and Xiaoxue Zhao.2026. Fiscal capacity and capital misallocation - the economic costs of tax evasion. Journal of Public Economics255,105581. Inspected author manuscript dated2025-11-24.
  url: https://drive.google.com/file/d/1e63eAJBxT2D2xGcA0jGNtUyJk7vfqVdH/view
  date: '2025-11-24'
  supports: [scope.china_relevance, identity.assignment_mechanism, assignment.treated, assignment.comparison_pool, assignment.intensity, assignment.exposure_construction, assignment.spillovers, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, design.assumptions, design.diagnostics, empirical_requirements.population, empirical_requirements.required_fields, empirical_requirements.measurement_risks, design_applications.data_used, design_applications.treatment_encoding, threats.condition]
  verification_status: reported
  access_level: full-text
  locator: Author research page links this88-page PDF. Inspected2026-09-29 PDFpp1-18 (printedpp1-17),20-21,26-30,39-40,47-49,54-55,58; sections2,4,5,6.1/6.2,7; equations2-3; Tables2-3,A.1-A.2,A.5; Figures1-3 captions. Nov2025 manuscript, not certified typeset2026 article or executed replication. Core sample and instrument construction are source-reported.
- id: E4
  source_type: scholarship
  citation: Xiaoxue Zhao, Research publications page; lists the paper under Journal of Public Economics255,March2026,105581 and links author manuscript and publisher DOI.
  url: https://sites.google.com/site/xiaoxuezhao/research
  date: '2026-09-29'
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: Publications entry Fiscal Capacity and Capital Misallocation inspected2026-09-29; verifies manuscript/publication association, not final-version equality.
- id: E5
  source_type: scholarship
  citation: Crossref publisher-deposited metadata for Liu and Zhao, Fiscal capacity and capital misallocation, Journal of Public Economics 255 (March 2026), article 105581.
  url: https://doi.org/10.1016/j.jpubeco.2026.105581
  date: '2026-09-29'
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: Inspected Crossref /works/10.1016/j.jpubeco.2026.105581 response on 2026-09-29; title, authors, container-title, volume, article-number, published date and DOI fields. Metadata establishes publication identity only; DOI landing page was inaccessible and does not supply inspected final full text.
design_applications:
- paper: Liu and Zhao - Fiscal capacity and capital misallocation, author manuscript2025-11-24
  doi: 10.1016/j.jpubeco.2026.105581
  journal: Journal of Public Economics
  year: 2026
  research_question: Does heterogeneous fiscal capacity distort firm location and capital allocation, and does computerized invoice enforcement reduce those distortions?
  population: Mainland industrial firms in ASIF1998-2007; separate county aggregate and registered-entry applications
  outcome: VAT/sales, firm and county capital, entry/exit, MRPK and productivity distributions
  data_used: [ASIF1998-2007 with longitudinal firm matching, GTOPO30 elevation and county polygons, SAIC registration records for legal-entry check, Baseline county statistics, TRAINS tariff and VAT export-rebate controls, NBS physical-product quantities2000-2006 for a restricted TFPQ application]
  treatment_encoding: Standardized log county elevation SD x Post2002; event-year interactions reference2001. Ruggedness remains continuous in baseline; no median pilot assignment.
  comparison: Relative outcome changes in more/less-rugged counties, conditional on firm/county and year effects and baseline-characteristic-by-year controls
  empirical_design: Reduced-form continuous DID; supplementary Table3 2SLS instruments effective VAT burden with the same interaction, with stronger exclusion requirements
  assumptions: [Comparable counterfactual exposure trends, No concurrent terrain-correlated break driving the result, Stable county and firm matching, Reporting and survey-entry responses distinguished from real capital changes]
  threats_addressed: [Year-specific exposure coefficients, Alternative VAT denominators and county revenue, Non-exporter and domestic-private restrictions, WTO tariff/uncertainty/rebate controls, Infrastructure and SOE reform controls, Registration-based entry check, Supplementary within-county fastest-route-distance exposure]
  evidence_refs: [E3, E4, E5]
method_transfer: null
readiness_blockers:
- Reconcile the linked November2025 manuscript with final2026 paper and replication inputs before reproducing estimates; no final-version equality or executed replication is claimed.
- Recover county polygon vintage, firm/county crosswalk and exposure standardization sample; obtain lawful ASIF or registration access appropriate to the selected profile.
- For a new outcome establish its own terrain-related counterfactual trends and phased compliance exposure; do not infer identification from the existing paper's robustness exercises.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

The object is digital invoice enforcement, not a tax-rate cut. General VAT
taxpayers issue special invoices that give purchasers evidence for input credits.
When those invoices are handwritten and difficult to match across tax offices,
the formal rate alone does not determine the burden actually enforced. The
government authorized national use of anti-counterfeit invoicing, requiring
installation and authentication; the project also imposed equipment and service
costs. These legal obligations are verified, not proof of universal compliance
[E1]. The paper's mechanism is that computer matching reduces reliance on costly
physical visits, especially in rugged counties [E3, reported claim].

## What Changed

The mandate has several clocks. Notice183 sets January2002 system issuance and
April2002 loss of handwritten-credit eligibility for the ten-thousand invoice
version. Its planned later completion dates must not be substituted for the
subsequent July/October2003 deadlines in notice139. The latter preserves the
tax-office-issued small-scale exception [E1; E2]. The empirical application uses
2002 as its annual break while recognizing continued conversion. It is not a
county adoption table, a PhaseIII staggered rollout, or the2009 equipment-credit
reform [E3, reported claim].

## Implementation and Assignment

Build county ruggedness from elevation cells and historical county polygons,
then attach it to firm locations. The paper uses log elevation SD, standardized
within its sample, interacted with Post2002. Flatter counties are a lower-dose
comparison, not legally untreated units. The firm specification studies changes
among observed firms; county aggregation serves a different question about local
capital and entry [E3, reported claim]. Actual taxpayer status or installation
dates become necessary if a new question concerns individual compliance rather
than the paper's geographic exposure [analytical inference].

## Why This Creates Empirical Variation

The reform changes an administrative friction predicted to matter differently
across geography. That supports an exposure-by-time comparison if competing
terrain-related trends are adequately addressed; geography does not become
exogenous to every economic outcome. The inspected application uses firm/county
and year effects, baseline county characteristics interacted with year, and
county-clustered inference [E3, reported claim].

Table3 additionally uses this interaction as an instrument for effective VAT
rates. That is a stronger interpretation: the first stage is exposure-related
VAT-burden growth, while exclusion requires capital to respond only through the
instrumented burden. Other digital, transport or regulatory channels could
violate it even if the reduced-form comparison remains informative. Keep the
reduced-form and IV claims separate [E3, reported claim; analytical inference].

## Identification Risks

WTO accession, restructuring and infrastructure development occur nearby in
time. The paper examines these channels, but they remain relevant to any new
outcome. Pre-period event coefficients cannot certify parallel trends outside
the observed sample. A nationwide reform also permits capital displacement:
relative gains and losses between counties do not by themselves reveal the
national net effect [E3, reported claim; analytical inference].

The paper explicitly notes that firm VAT and sales are self-reported. VAT/sales
is neither the statutory rate nor a direct administrative payment measure.
ASIF appearance can reflect crossing its sales threshold rather than business
creation; registration counts are the distinct check. Excluding changing county
IDs preserves a baseline sample but may omit relocators and cannot fix boundary
or matching errors [E3, reported claim].

## Data Requirements

Use the firm-year contract for within-firm outcomes and the county profile for
aggregate capital or entry. Neither requires patent data. Physical product
quantities are needed only for the paper's restricted TFPQ application, not for
the basic enforcement contrast. The supplementary distance exercise requires
firm addresses, county tax-office coordinates and a terrain-based fastest-route
construction; it is not an observed historical-road-distance series [E3,
reported claim]. Dataset acquisition belongs in the companion data catalog;
this record preserves the design and joins without storing restricted data.
The county profile uses the same elevation-based exposure and invoice mandates
as the default contract. County aggregation needs stable boundaries; ASIF entry
is not legal registration, and SAIC registrations do not capture informal entry
[E3, reported claim; analytical inference].

## Evidence Notes

E1-E2 establish legal identity, taxpayer boundary and phased rules. They do not
verify county completion dates or measured enforcement gains. E3 is the
author-linked November2025 manuscript, including its appendix; E4 establishes
its association with the2026 journal publication. No equality with final
typesetting or executed replication is asserted. The historical regime and the
paper-used core comparison are sufficiently grounded to serve a conditional
research decision; geographic crosswalks, data access and outcome-specific
identification still require the stated checks. Publication year2026 is a light
recency marker, not an evidence upgrade.
