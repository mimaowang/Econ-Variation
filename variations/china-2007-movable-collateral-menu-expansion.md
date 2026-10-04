---
schema_version: 2
id: china-2007-movable-collateral-menu-expansion
name: China 2007 Movable Collateral Menu Expansion and Predetermined Asset Exposure
aliases:
- Permissible collateral and access to finance
- Xu movable assets collateral reform
- 2007年物权法动产及应收账款担保范围扩展
status: grounded
provenance:
  task_id: task-ce568b433593
scope:
  country: China
  regions: [Mainland China; Shanghai and Shenzhen listed firms across 31 provincial-level jurisdictions in the inspected application]
  domains: [firm-economics, development-economics, finance, credit-allocation, industrial-organization]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    A national change in the legal framework for movable-property mortgages
    and receivable pledges differentially exposed Chinese enterprises according
    to their pre-reform asset composition. Xu studies this channel using
    nonfinancial firms eventually listed in Shanghai or Shenzhen. The serving
    object is collateral-menu exposure, not the entire Property Law or a claim
    that every part of it is an independent shock.
identity:
  instrument: >
    The 2007 explicit framework for existing and future production assets and
    receivable collateral, interacted with a firm's predetermined inventory
    and accounts-receivable intensity. Legal eligibility is nationwide; the
    paper's high/low asset classification is a research exposure proxy.
  authority: >
    National People's Congress enacts the Property Law. Its Article189 assigns
    floating-mortgage registration to the debtor-domicile industry-and-commerce
    authority, while Article228 requires receivable-pledge registration with
    the credit-reference institution. PBOC issued the accompanying receivable
    registration measures.
  legal_identifiers:
  - 中华人民共和国物权法, 主席令第六十二号, adopted 16 March 2007
  - Property Law Articles180-181,188-189,223(6),228 and247
  - 中国人民银行令〔2007〕第4号, 应收账款质押登记办法; issue/effect dates confirmed by PBOC's 2017 explanation, original full text not inspected
  implementation_regime: >
    Articles180-181 explicitly cover production equipment, raw materials,
    semi-finished goods and products, including existing and future property.
    Articles188-189 distinguish contract-based mortgage creation from
    registration needed against good-faith third parties. Article228 instead
    makes registration constitutive for receivable pledges. These routes are
    not one universal electronic registry. PBOC's retrospective confirms the
    2007 receivable measures became effective on 1 October2007. Operational
    registration practices and actual lending remain distinct from legal eligibility.
  assignment_mechanism: >
    All eligible firms face the same legal change, but the inspected paper
    compares firms with high and low predetermined shares of inventory plus
    accounts receivable. This composition predicts potential collateral-menu
    exposure, not realized secured borrowing or random treatment assignment.
  parent: null
  related_variations: []
timeline:
  announcement: '2007-03-16 (formal law adoption and promulgation)'
  effective: '2007-10-01'
  implementation_start: 2007
  implementation_end: null
  local_timing: >
    The inspected application uses 2001-2005 as pre-reform years, omits2006
    for anticipation, and codes2007-2011 as post-reform. This annual choice
    treats2007 as post although legal effectiveness began in October. The
    manuscript's December2006 draft news is not formal law enactment.
  anticipation: >
    The author argues passage and content were uncertain and omits2006.
    Predetermined exposure uses2001-2005 assets; that choice does not rule
    out earlier anticipation or inside information. Legal dates alone do
    not establish an unanticipated shock.
  last_verified: '2026-10-03'
assignment:
  unit: Firm-year with fixed pre-reform firm asset exposure.
  treated: Top third of firms ranked by their median2001-2005 inventory-plus-receivables share of total assets in the inspected application.
  comparison_pool: Bottom third under the same ranking; middle third omitted. Low-exposure firms still face the law and are not legally untreated.
  rule: >
    Compute Mov_it=(Inventory_it+AccountsReceivable_it)/TotalAssets_it.
    Take each firm's median over2001-2005; assign HighMov=1 to the top tertile
    and0 to the bottom tertile, omitting the middle. Interact fixed HighMov
    with Post=1 in2007-2011 and0 in2001-2005; exclude2006. The inspected text
    does not state a tie-breaking rule for exact tertile boundaries.
  intensity: >
    The underlying exposure is continuous predetermined asset composition.
    The main paper specification discretizes it into upper/lower tertiles;
    continuous exposure is reported as a robustness exercise available on request.
  exemptions:
  - Financial industries and observations missing total assets are excluded from the application.
  - Firms must have reports both before and after2006; this is sample selection, not a legal exemption.
  - The law also covers other eligible operators; agriculture-focused applications are outside this record's collection focus.
  compliance: >
    Book inventories and receivables do not show whether any asset was
    registered, pledged, appraised, or accepted by a lender. The inspected
    data lack detailed secured versus unsecured debt. The design estimates
    differential financial responses to legal opportunity, not compulsory take-up.
  exposure_construction: >
    Use WIND balance-sheet line items and fixed firm identifiers to construct
    the pre-reform ratio before joining yearly outcomes. Preserve the original
    industry, province, ownership and listing-history classifications. Do not
    substitute current asset mix for predetermined exposure, or silently replace
    inventory-plus-receivables with all current assets.
  required_identifiers: [firm_id, accounting_year, province_id, industry_id]
  spillovers: >
    Credit reallocation and product-market responses may affect low-exposure
    firms. The inspected application does not identify an aggregate credit
    supply effect; a relative high/low estimate need not equal a national net gain.
research_compatibility:
  outcome_domains: [leverage, debt maturity, firm investment, asset composition, profitability, credit allocation]
  affected_populations: [Mainland nonfinancial firms eventually listed in Shanghai or Shenzhen]
  mechanism_channels: [Expanded explicit collateral menu, receivable pledge registration, financing capacity, asset-debt maturity adjustment]
  best_for:
  - Firm financing and investment questions with long pre-reform asset histories and annual debt decomposition.
  - Comparing differential responses to nationwide legal change while separating formal collateral opportunity from observed loan use.
  not_good_for:
  - Treating low-inventory firms as unexposed to every Property Law provision.
  - Estimating the effect of actual registered collateral without registration or loan-level information.
  - Claiming nationwide welfare or bank screening effects from listed-firm debt balances alone.
design:
  claim_type: causal
  affordances: [National legal timing interacted with predetermined firm exposure, Upper versus lower asset-composition tertiles, Firm panel with industry-year and province-year controls]
  candidate_designs: [Exposure-based difference in differences]
  identifying_variation: >
    Differential pre/post changes among firms with high versus low pre-reform
    movable-asset intensity, conditional on firm, year, industry-year and
    province-year effects. Common legal timing alone supplies no untreated region.
  primary_strategy: >
    Regress annual outcomes on HighMov_i times Post_t with firm and time
    effects, industry-year and province-year interactions, and mostly lagged
    firm covariates. The BOFIT manuscript clusters standard errors by firm.
  estimand: >
    The differential response of high versus low predetermined movable-asset
    firms to the2007 legal regime under parallel-trend and channel-separation
    assumptions. It is not an effect per yuan of pledged collateral or a
    national average effect of the entire Property Law.
  treatment_variable: Fixed upper-tertile HighMov indicator times post2007; middle tertile and2006 observations omitted.
  comparison_logic: >
    Compare changes within firms between2001-2005 and2007-2011, then
    contrast high versus low baseline exposure. The low group also receives
    broader property/creditor protection, which must not have differential
    residual effects aligned with movable-asset intensity.
  estimation_notes: >
    Debt outcomes divide total, long-term or short-term debt by lagged total
    assets. Table2 main regressions use4559-6658 observations and750-835 firms,
    varying by outcome, not the full approximately1200-firm source panel.
    Data include reports before eventual listing; a listed-throughout sample
    is only a reported robustness exercise. Firm clustering does not by
    itself address every correlated industry or common exposure shock.
  assumptions:
  - High and low predetermined asset groups would have comparable conditional outcome trends without the legal change.
  - Other Property Law protections, concurrent reforms and macroeconomic shocks do not generate residual differential responses aligned with baseline movable assets.
  - Exposure and sample membership are not selectively adjusted in anticipation in ways that drive the comparison.
  diagnostics:
  - Reassess pre-trends and placebo reform years2003/2004; null placebo coefficients are not proof of parallel trends.
  - Contrast results excluding2007 or ending in2007, and discuss the short effective-period exposure in2007.
  - Compare industry-year/province-year controls and baseline tangibility, liquidity, profitability and debt interactions.
  - Examine changing sample composition, denominator effects, group cutoffs and common-shock inference.
threats:
- type: bundled_legal_channels
  basis: reported
  condition: The author explicitly acknowledges that expanded permissible collateral and stronger creditor rights are extremely difficult to disentangle fully (Section5.1.1 footnote12).
  evidence_refs: [E1]
  possible_diagnostics: [Baseline fixed-asset exposure interactions, Private/SOE comparisons, Outcome-specific channel evidence from registered loans]
- type: baseline_legal_overstatement
  basis: documented
  condition: The1995 Security Law already has nonpossessory mortgage and other-movable-property provisions; it does not establish a blanket pre2007 inventory prohibition.
  evidence_refs: [E3]
  possible_diagnostics: [Recover historical registration and court practice for the asset class, Distinguish explicit floating mortgages from existing fixed-property arrangements]
- type: concurrent_shocks_and_selection
  basis: inferred
  condition: Asset composition can predict differential responses to split-share and tax reforms, the2008 crisis/stimulus, or survival/listing; the reported checks reduce selected alternatives without certifying exogeneity.
  evidence_refs: [E1]
  possible_diagnostics: [Outcome-specific pre-trends, Predetermined characteristic interactions, Restricted windows and stable sample checks]
empirical_requirements:
  contract_version: 1
  population: Nonfinancial mainland firms with reports before and after2006, eventually listed in Shanghai or Shenzhen; upper/lower pre-reform asset-share thirds.
  observation_unit: Firm-year
  geography_level: Firm with province identifiers
  time_start: 2001
  time_end: 2011
  minimum_frequency: annual
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields: [inventory, accounts_receivable, total_assets, total_debt, long_term_debt, short_term_debt, firm_outcome, industry, province, fixed_assets, cash, profit, sales, incorporation_year, listing_history, controlling_owner, split_share_reform_completion]
  required_identifiers: [firm_id, accounting_year, province_id, industry_id]
  treatment_key: [firm_id, pre2006_median_movable_ratio, accounting_year]
  treatment_source: WIND inventory, accounts receivable and total assets over2001-2005; fixed tertile assignment and author-defined annual2007 post indicator, anchored to the legal enactment/effect dates.
  measurement_risks:
  - WIND access was not established; reconstructable financial line items do not imply public or unrestricted availability.
  - Bank loan status and secured/unsecured borrowing are not distinguished in the inspected source; balance-sheet debt is the measured outcome.
  - Tertile boundaries, ties and missing-year histories need explicit coding; no inspected replication code resolves them.
  - Exposure uses the2001-2005 window; the inspected text does not require all five observations for every firm. The minimum count is not sufficient to certify a reliable median or parallel trends; arbitrary single-year substitution is not baseline reproduction.
evidence:
- id: E1
  source_type: paper
  citation: 'Xu, Bing. Permissible collateral and access to finance: Evidence from a quasi-natural experiment. BOFIT Discussion Papers3/2018,31 January2018; independently identified subsequent CER2019 publication.'
  url: https://www.econstor.eu/bitstream/10419/212888/1/bofit-dp2018-003.pdf
  date: '2018-01-31'
  supports: [scope.china_relevance, identity.instrument, identity.assignment_mechanism, timeline.local_timing, timeline.anticipation, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.intensity, assignment.exemptions, assignment.compliance, assignment.exposure_construction, design.primary_strategy, design.identifying_variation, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, design.assumptions, design.diagnostics, threats.condition, empirical_requirements.population, empirical_requirements.required_fields, empirical_requirements.treatment_source, empirical_requirements.measurement_risks, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design]
  verification_status: reported
  access_level: full-text
  locator: >
    Complete42-page repository PDF fetched in memory2026-10-03; printed
    pp9-15 institutional/design/data Sections2-3; pp15-18 results; pp19-28
    robustness Sections5.1/5.2/5.3/5.4; printedpp33-34 Tables1-2 and footnotes7/12/25.
    PDF page=printed page+1 because repository cover and publication front matter.
    Key definitions and table sample inspected directly; not a claim to have
    inspected the final2019 publisher typeset text or on-request robustness files.
- id: E2
  source_type: policy-document
  citation: 中华人民共和国物权法; adopted and promulgated16 March2007, effective1 October2007; official Audit Office reproduction.
  url: https://www.audit.gov.cn/n7/n34/n58/c109665/content.html
  date: '2007-03-16'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.announcement, timeline.effective, timeline.implementation_start, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: >
    Official law text inspected directly2026-10-03: promulgation heading,
    Articles180-181 existing/future productive movables;188-189 mortgage creation,
    domicile registration and third-party rules;223(6)/228 receivable pledge;
    Article247 effective date. Does not establish actual registration or credit use.
- id: E3
  source_type: policy-document
  citation: 中华人民共和国担保法 (1995); official Zhengzhou State-owned Assets Supervision and Administration Commission reproduction.
  url: https://gzw.zhengzhou.gov.cn/zcfg/2995092.jhtml
  date: '1995-06-30'
  supports: [identity.implementation_regime, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: >
    Text inspected2026-10-03, Articles33-34 nonpossessory mortgage and
    broad property categories,41-43 registration and enterprise equipment/other
    movables,63-64 possessory pledge and75 rights pledge. No adjudication or
    registry practice inspected. Counters a blanket prohibition inference;
    does not independently settle the paper's practical inventory constraint.
- id: E4
  source_type: implementation-document
  citation: PBOC. 《应收账款质押登记办法》（2017年修订）修订说明, dated30 October2017, official China Government attachment.
  url: https://www.gov.cn/xinwen/2017-11/01/5236146/files/9c0d5df75a1e4913abbf20d2bb35b679.pdf
  date: '2017-10-30'
  supports: [identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.effective]
  verification_status: verified
  access_level: official-document
  locator: >
    Three-page official PDF inspected2026-10-03, p1 confirms30 September2007
    issuance and1 October2007 effective date of Order4, and pp2-3 explain later
    definition/transfer-registration changes. Used only for original dates
    and version boundary, not to backdate2017 rules to2007. Original2007
    registration texts remained inaccessible at inspected Ministry of Justice endpoints.
- id: E5
  source_type: other
  citation: Publisher-deposited Crossref metadata for Bing Xu, China Economic Review54 (April2019),237-255.
  url: https://doi.org/10.1016/j.chieco.2018.11.006
  date: '2019'
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: >
    Metadata directly inspected2026-10-03 through
    https://api.crossref.org/works/10.1016/j.chieco.2018.11.006:
    title, sole author BingXu, journal, volume54,237-255 and published[2019,4].
    DOI identity is linked here; final full text not inspected.
design_applications:
- paper: 'Permissible collateral and access to finance: Evidence from a quasi-natural experiment'
  doi: 10.1016/j.chieco.2018.11.006
  journal: China Economic Review
  year: 2019
  research_question: How expanded permissible collateral changes firm debt capacity, debt maturity, asset composition and allocation.
  population: Mainland nonfinancial firms eventually listed in Shanghai/Shenzhen,2001-2011 in the inspected BOFIT2018 version.
  outcome: Total/long-term/short-term debt over lagged assets; asset growth, fixed assets and profitability; predetermined-quality heterogeneity.
  data_used: [WIND firm financial statements, industry/province/ownership/listing classifications, pre-reform inventory and accounts receivable, national credit aggregates for selected checks]
  treatment_encoding: Fixed top versus bottom tercile of firm median2001-2005 movable ratio times2007-2011;2006/middle tercile omitted in the inspected version.
  comparison: Low baseline movable-intensity firms under the same national law; within-firm pre/post changes with time, industry-year and province-year controls.
  empirical_design: Exposure DID in independently identified BOFIT2018 precursor; final CER2019 specification not independently compared.
  assumptions: [Conditional parallel trends, No residual differential concurrent reforms, Predetermined exposure and stable measurement]
  threats_addressed: [Placebo2003/2004 reforms, Fixed-asset/ownership/connections checks, Split-share and tax checks, Credit/stimulus interactions and precrisis restriction]
  evidence_refs: [E1, E2, E3, E4, E5]
method_transfer: null
readiness_blockers:
- Compare final2019 methods or replication code before claiming exact published-version reproduction.
- Reconcile practical pre2007 inventory restrictions with the broader1995 statutory mortgage provisions; do not describe all inventory mortgages as newly legalized.
- Recover original registration procedures and enforcement evidence if the question concerns actual pledged collateral rather than balance-sheet exposure.
- Establish lawful WIND access and document exposure cutoffs, ties, missing-year treatment and estimation sample.
---

## Institutional Background

Chinese firms could mortgage equipment and other property before2007: the1995
Security Law already defined nonpossessory mortgages and listed enterprise
equipment and other movables among registration categories [E3, verified].
Xu describes practical limitations on changing inventories and receivables,
including fragmented registration and possessory arrangements [E1, reported
claim]. The inspected statute does not independently confirm those practical
limits. The useful distinction is an explicit expanded framework for future
productive assets and receivable pledges, not “no movable collateral before2007.”

## What Changed

The2007 law expressly provides for existing/future productive-property
mortgages and receivable pledges, with different creation and registration rules
[E2, verified]. PBOC's official retrospective dates the original receivable
registration measures to September/October2007 [E4, verified]. Neither confirms
universal lender acceptance. The record combines the inventory/receivable menu
as one empirical exposure, not two additional shocks to inflate the collection.

## Implementation and Assignment

The law applies nationally; a firm's upper/lower-tertile status is the author's
encoding, not government selection. Compute the median2001-2005 share of
inventory plus accounts receivable in assets, keep highest and lowest thirds,
exclude2006, and compare2007-2011 to2001-2005 [E1, reported claim]. Annual2007
post coding differs from the October legal effective date. Low-exposure firms
also benefit from the law's other protections. This is a differential exposure
comparison, not a treated-city rollout.

## Why This Creates Empirical Variation

An enlarged collateral menu could matter more to firms holding assets that were
previously difficult to pledge. Under conditional parallel trends, the high/low
comparison can isolate a relative financing response [analytical inference].
Xu reports higher total/long-term leverage but no corresponding profitability
improvement in the inspected version [E1, reported claim]. Balance-sheet debt
does not demonstrate registered collateral take-up, bank screening changes, or
a national allocation/welfare gain. The author explicitly notes difficulty
fully separating creditor protection from collateral-menu expansion.

## Identification Risks

Baseline asset structure is endogenous to industry, business model and finance.
Industry-year/province-year effects and2003/2004 placebo exercises address
selected alternatives, not all differential trends [E1, reported claim;
analytical inference]. Split-share, tax, crisis and stimulus changes overlap the
window. A small list of reported checks must not become blanket causal
certification. Reconsider anticipation, reporting/listing selection and exposure
cutoffs for a new outcome; recover enforcement evidence if that outcome requires
actual security interests rather than legal opportunity.

## Data Requirements

The core join is firm ID/accounting year, with pre2006 balance-sheet components,
annual outcomes and province/industry identifiers. WIND supplies the inspected
application; access is not established here. Firm debt is divided by lagged
assets; changing denominators and missing line items warrant care. The data do
not separate secured/unsecured debt. Registration/loan assets belong in the
separate data-asset repository if later recovered, linked by DOI rather than
duplicating profiles here [E1, reported claim; analytical inference].

## Evidence Notes

This record grounds the legal mechanism in official2007 and1995 texts and
PBOC's dated explanation, while attributing detailed empirical coding to an
actually inspected BOFIT2018 precursor. Final CER2019 identity is verified,
but its full methods were not compared. Related candidate-a88a045522ed concerns
a broader private-protection event, while candidate-88e7b08906ac bundles
property and bankruptcy reforms; both remain candidates, not parallel canonical
records of this same menu. Any later admission must resolve overlap rather
than count the statute again under another title. No paper or restricted data
was stored and no replication was claimed.
