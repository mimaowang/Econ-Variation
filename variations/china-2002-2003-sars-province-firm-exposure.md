---
schema_version: 2
id: china-2002-2003-sars-province-firm-exposure
name: China 2002–2003 SARS provincial exposure and manufacturing redistribution
aliases: [非典省级企业暴露, SARS inventory and market power, Jiang Zhang SARS manufacturing]
status: grounded
provenance:
  task_id: task-63c2f1a4c4fc
scope:
  country: China
  regions: [Mainland China, Guangdong, Beijing, Shanxi, Inner Mongolia]
  domains: [firm-performance, industrial-economics, regional-economics, development, market-power, inventory]
  variation_type: event-shock
  knowledge_role: china-variation
  china_relevance: Mainland manufacturing firms face geographically unequal SARS disruption and associated responses. An actual REStat application compares firms in four heavily affected provinces with other mainland firms; health outcomes are not the focus of this case.
identity:
  instrument: The geographically unequal2002–2003 SARS epidemic and induced prevention responses, applied to mainland manufacturing firms through province location.
  authority: Epidemic spread is not assigned by an authority; Chinese national and local health authorities coordinate reporting and responses, with WHO receiving official reports.
  legal_identifiers: []
  implementation_regime: An epidemic beginning in Guangdong in November2002 spreads across provinces in2003. Infection, information, travel monitoring, prevention and firm/customer responses jointly change economic exposure. No single legal treatment date or isolated lockdown instrument is claimed.
  assignment_mechanism: Provincial location maps firms into different epidemic exposure; severity is realized through transmission and reporting rather than randomized assignment. The inspected application selects four heavily affected provinces and uses province-specific annual onset conventions. Its binary comparison is recoverable without endorsing unresolved manuscript case totals for a continuous dose.
  parent: null
  related_variations: [china-2020-2022-city-lockdown-truck-flow-exposure, china-covid19-community-infection-announcement-housing-market]
timeline:
  announcement: No single announcement starts infection or every firm's economic exposure; contemporary official reporting changes during spring2003.
  effective: WHO identifies Guangdong outbreak onset as2002-11-16; this is not a universal firm treatment date.
  implementation_start: 2002
  implementation_end: 2003
  local_timing: Baseline Eq14 sets the post indicator from2002 for Guangdong and2003 for other provinces; uniform2003 onset is robustness only. Persistent firm effects are studied through2007, not evidence of continuous epidemic transmission through2007.
  anticipation: Guangdong's late2002 exposure can contaminate an undifferentiated2002 pre-period. Markup detrending nevertheless fits1999–2002 under the authors' price-stickiness rationale; inventory and uncertainty detrending treat Guangdong differently.
  last_verified: '2026-10-07'
assignment:
  unit: Province-location exposure joined to firm-year observations.
  treated: Firms located in Beijing, Guangdong, Shanxi or Inner Mongolia under the paper's four-province application.
  comparison_pool: Firms in other mainland provinces and earlier observations; these provinces can have infections, national responses or market-redistribution gains, so they are not a verified zero-exposure population.
  rule: Treated=1 for the four named provinces; Post_jt=1 if Guangdong and year>=2002, or if another province and year>=2003. Treatment=Treated*Post. A fixed pre-shock location cohort is a separately declared robustness/new application rather than an undocumented replication convention.
  intensity: Baseline binary exposure. Eq16 additionally interacts provincial total cases in hundreds with post; the exact series behind manuscript counts is unresolved and is not certified for numerical reproduction. Alternative six-province treatment adds Hebei and Tianjin within the same regime.
  exemptions: [No universal legal exemption defines binary firm treatment, Firms outside the four provinces may still experience SARS or national responses, Hong Kong Macao and Taiwan are outside the mainland firm comparison]
  compliance: Location measures exposure, not observed infection, closure compliance or a particular restriction at a firm. Prevention and reporting intensity can differ across regions.
  exposure_construction: Harmonize firm-year province and city identifiers, assign the four-province flag and explicit annual post rule, and join to the declared outcome. Preserve observed relocation and survey entry/exit. A fixed initial province design must state its altered estimand. For continuous severity or border-defined neighbor comparisons, recover case definitions, vintage and province crosswalk rather than silently substituting official final counts for author counts.
  required_identifiers: [firm_id, year, province_code, city_code, industry_code]
  spillovers: The paper reports gains for low-case provinces bordering the four treated provinces; national demand, supply chains and travel measures also reach controls. The contrast is relative redistribution, not an aggregate national SARS effect.
research_compatibility:
  outcome_domains: [manufacturing markup, inventory, demand uncertainty, firm market share, firm performance]
  affected_populations: [mainland manufacturing firms, firms observed in the industrial survey]
  mechanism_channels: [customer demand disruption, inventory adjustment, uncertainty, production disruption, prevention and travel responses, interprovince competition]
  best_for: [Conditional regional comparisons of firm responses to epidemic disruption, Inventory and competition questions with firm accounts, Relative market redistribution with explicit spillover analysis]
  not_good_for: [Random provincial epidemic assignment, An isolated infection effect or single policy effect, Automatic pure demand-shock identification, National aggregate effects from the four-province contrast, Certified continuous-case replication without source reconciliation]
design:
  claim_type: reduced-form
  affordances: [unequal provincial exposure, Guangdong versus other-province onset timing, pre/post firm panel, neighbor spillover sensitivity]
  candidate_designs: [province-exposure DID with conditional detrending, outcome-specific event study, province-case intensity only after data reconciliation]
  identifying_variation: Changes in outcomes for firms in four heavily affected provinces relative to firms elsewhere, with earlier annual onset for Guangdong. Geography and epidemic severity are observational rather than randomized.
  primary_strategy: Eq14 includes firm controls, city GDP per capita/population density/export share and city/four-digit industry/year effects. Firm effects are Section8 robustness, not the baseline. Eq15 estimates event coefficients. Authors detrend outcomes before estimation because raw markup common trends are rejected.
  estimand: Conditional relative firm-outcome change from epidemic and induced responses, after the assumed continuation of province-group pre-trends; not the isolated effect of infection, a national average or separately identified inventory mediation.
  treatment_variable: Four-province indicator interacted with Guangdong post2002 or other-province post2003; alternative common2003 and six-province definitions are sensitivity specifications.
  comparison_logic: Assess treated-versus-other-province outcome trajectories while accounting for pre-trends, trade/industry composition and interference. Do not interpret untreated labeling as absence of exposure or recover causality from geographical distance alone.
  estimation_notes: ASIE1998–2007 covers all SOEs and non-SOEs with annual sales>=RMB5million. Table2 has1,237,304 firm-years and city-industry-year clustered errors; this does not settle province-level common-shock inference. Table3 province-PPI validation uses269 observations, firm-count weights and province-year clustering; that weighting should not be imported into baseline firm regressions without code. Preferred markup Eq10 adjusts output-value/variable-production-cost raw markup using industry-level probit non-stockout probability. AppendixA2 codes non-stockout=1 when finished-goods inventory>0, though baseline inventory ratios use total inventory. Demand uncertainty is city/two-digit-industry/year residual dispersion from Eq12, not an independently observed expectation measure.
  assumptions: [Outcome-specific counterfactual trends after declared adjustment, No remaining differential concurrent changes driving the comparison, Appropriate regional common-shock inference, Stable and explicit location/sample measurement, Interference consistent with a relative estimand, Model and accounting assumptions for generated outcomes]
  diagnostics: [Raw and adjusted event leads, Trend-continuation sensitivity, Guangdong2002 contamination and uniform2003 sensitivity, Firm effects and fixed-location cohort, Six-province and neighbor-control alternatives, Regional inference sensitivity, Entry exit and missing-account restrictions, Alternative observed outcomes and markup definitions]
threats:
  - type: rejected raw pre-trends and detrending assumption
    basis: reported
    condition: Raw markup common trends are rejected with F9.64 and p<0.001. AppendixB fits1999–2002 province-group slopes; markup retains Guangdong2002 under a price-stickiness rationale, whereas inventory and uncertainty separate its pre2002 slope. This is a counterfactual continuation assumption, not proof of original parallel trends or a certified sensitivity bound.
    evidence_refs: [E1, E4]
    possible_diagnostics: [raw and detrended results, alternative trend windows, leave Guangdong out, explicit sensitivity to post-trend deviations]
  - type: spillovers and relative redistribution
    basis: reported
    condition: Neighboring low-case provinces gain market share/markup. Other controls can have cases and nationwide responses, so stable-unit no-interference assumptions and national-effect interpretations are not automatic.
    evidence_refs: [E1, E4]
    possible_diagnostics: [border and trading-network exclusions, exposure mapping, declare relative rather than aggregate estimand]
  - type: epidemic selection and reporting vintage
    basis: documented
    condition: WHO records new nationwide electronic reporting and changing case definitions in March2003, and incomplete investigations in May. Mobility and prevention capacity can correlate with provincial firm trends. Author provincial counts remain unreconciled with official probable-case statistics.
    evidence_refs: [E2, E3, E5]
    possible_diagnostics: [reporting-vintage audit, case-definition sensitivity, baseline geographic composition controls, no random-dose interpretation]
  - type: common regional shocks and concurrent changes
    basis: inferred
    condition: Assignment is provincial while baseline errors cluster city-industry-year; many firm observations do not create independent province shocks. WTO exposure and contemporaneous restructuring may differ across regions despite controls.
    evidence_refs: [E1, E4]
    possible_diagnostics: [province-level inference and few-treated-region sensitivity, trade and ownership interactions, placebo years]
  - type: generated outcome and mediation
    basis: reported
    condition: Markup relies on cost/returns-to-scale and stockout measurement; uncertainty is generated from inventory residuals. Causal-steps inventory mediation and model decomposition are explicitly suggestive and involve endogenous components.
    evidence_refs: [E1, E4]
    possible_diagnostics: [sales versus production accounting audit, alternative markup and finished-inventory measures, avoid interpreting mediation as separately identified causal effects]
empirical_requirements:
  contract_version: 1
  population: Mainland manufacturing firms with recoverable province location and pre/post observations; industrial survey coverage is all SOEs and non-SOEs above the stated sales threshold.
  observation_unit: firm-year
  geography_level: Province exposure with city controls and firm identifiers.
  time_start: 1998
  time_end: 2007
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields: [declared firm outcome, firm location history, sales revenue and export status, capital stock, city GDP per capita population density and export share, ownership and firm age, survey inclusion and retention history]
  required_identifiers: [firm_id, year, province_code, city_code, industry_code]
  treatment_key: [province_code, year]
  treatment_source: Explicit four-province and annual onset convention in Eq14; WHO chronology and official Ministry briefing ground the epidemic regime but do not certify every author's numerical severity series.
  measurement_risks: [registration versus operating location, relocation, survey thresholds and attrition, Guangdong2002 exposure, generated outcome assumptions, unresolved provincial continuous-dose vintage]
evidence:
  - id: E1
    source_type: paper
    citation: Jiang Yating and Hongsong Zhang, How Do Large Epidemics Redistribute Market Power? Evidence from the2003 SARS Shock in China; June12,2025 author manuscript, linked to REStat online publication2026.
    url: https://hongsongzhang.weebly.com/uploads/1/3/4/7/13473383/sarsinventory_conditionalacceptance.pdf
    date: '2025-06-12'
    supports: [assignment.rule, assignment.treated, assignment.comparison_pool, assignment.intensity, assignment.spillovers, timeline.local_timing, design.primary_strategy, design.estimation_notes, empirical_requirements.required_fields, design_applications.treatment_encoding, design_applications.data_used]
    verification_status: reported
    access_level: full-text
    locator: '75-page PDF: main printedpp5–7 Sections2.1–2.2; pp13–18 Eq10–13 measurement; pp19–30 Eq14–16, pretrend discussion, geographic spillovers and robustness; footnotes3,15–17,22–28; Tables2–5 PDF42–45. Final typeset body and code not inspected.'
  - id: E2
    source_type: official-data
    citation: WHO Disease Outbreak News, SARS update13, March28,2003.
    url: https://www.who.int/emergencies/disease-outbreak-news/item/2003_03_28-en
    date: '2003-03-28'
    supports: [identity.instrument, identity.assignment_mechanism, timeline.effective, timeline.anticipation, assignment.compliance]
    verification_status: verified
    access_level: official-document
    locator: 'China joins WHO collaborative network paragraphs: Guangdong onset November16,2002; definitions compared, first Beijing/Shanxi reports and new nationwide Ministry-to-WHO electronic reporting. Does not verify author provincial total-case values or economic post indicators.'
  - id: E3
    source_type: implementation-document
    citation: Ministry of Health vice-minister Gao Qiang May30,2003 SARS briefing, official embassy reprint displayed May9,2004.
    url: https://is.china-embassy.gov.cn/chn/zbgx/200405/t20040509_10122097.htm
    date: '2003-05-30'
    supports: [identity.authority, identity.implementation_regime, assignment.exposure_construction, assignment.compliance, timeline.local_timing]
    verification_status: verified
    access_level: official-document
    locator: 'Sections1–2 read in full: Guangdong concentration January–March, northern spread April, six-province concentration May29, statutory reporting, coordinated local prevention and transport monitoring. Grounds location-dependent epidemic/response exposure, not the author exact four-province coding or a single firm closure rule.'
  - id: E4
    source_type: appendix
    citation: Jiang Zhang June2025 manuscript AppendicesB,E,F.
    url: https://hongsongzhang.weebly.com/uploads/1/3/4/7/13473383/sarsinventory_conditionalacceptance.pdf
    date: '2025-06-12'
    supports: [design.estimation_notes, design.diagnostics, timeline.anticipation, empirical_requirements.measurement_risks]
    verification_status: reported
    access_level: appendix
    locator: AppendixB printedpp3–4/PDF48–49 exact detrending window/Guangdong handling; E and TableA2 PDF57 stockout coding; TablesA4–A8 PDF59–62 alternative outcomes and neighbor exclusion; A4/A5 PDF68 map and original differential trends. Table2 footer separately inspected for clustering; executable cleaning and provider files not inspected.
  - id: E5
    source_type: official-data
    citation: WHO final probable SARS case summary, onset November2002–July2003, data as of December31,2003; web posting July24,2015.
    url: https://www.who.int/publications/m/item/summary-of-probable-sars-cases-with-onset-of-illness-from-1-november-2002-to-31-july-2003
    date: '2003-12-31'
    supports: [identity.implementation_regime, timeline.implementation_end, empirical_requirements.measurement_risks]
    verification_status: verified
    access_level: official-document
    locator: 'Full area table and footnotesa–e: mainland China5327 probable cases/349 deaths, global8096/774, separate HK/Macao/Taiwan rows, China first onset November16,2002 and last June3,2003. Inconsistent with manuscript claim that mainland accounts for87.5% of global cases/80% of deaths; those shares are not adopted here. No province-level author-series replication is claimed.'
  - id: E6
    source_type: other
    citation: Crossref publisher-deposited metadata for Jiang Zhang REStat article, DOI10.1162/rest.a.1769; Renmin University May21,2026 notice independently confirms online publication.
    url: https://doi.org/10.1162/rest.a.1769
    date: '2026-05-14'
    supports: [design_applications.paper, design_applications.journal, design_applications.year]
    verification_status: verified
    access_level: metadata
    locator: Crossref works endpoint read title, container-title and published-online date May14,2026; publisher DOI page inaccessible. University notice inspected separately. Metadata confirms publication only, not equality with the inspected2025 body or final methodological revisions.
design_applications:
  - paper: How Do Large Epidemics Redistribute Market Power? Evidence from the2003 SARS Shock in China
    journal: Review of Economics and Statistics
    year: 2026
    doi: 10.1162/rest.a.1769
    research_question: How does geographically uneven SARS disruption redistribute manufacturing market power, and how are inventory and uncertainty associated with it?
    population: Mainland manufacturing firms in ASIE1998–2007 under survey and accounting availability restrictions.
    outcome: Inventory-adjusted markup, raw/alternative markup, inventory ratio and generated city-industry-year demand uncertainty; market share and provincial PPI validate different aggregation margins.
    data_used: [ASIE firm accounts and annual geography, WHO-attributed epidemic chronology and provincial severity with unresolved exact case-series provenance, CEIC city controls, China Statistical Yearbook PPI for separate validation]
    treatment_encoding: Four named provinces times Guangdong post2002 or other-province post2003; six-province and uniform2003 sensitivity remain within the same case.
    comparison: Other mainland province firms before/after onset, after declared group detrending, with explicit neighbor spillover checks.
    empirical_design: Baseline city/industry/year effects, city-industry-year clustering; event study, firm-effect robustness and province-dose extension documented in inspected2025 version.
    assumptions: [province-group trend continuation, controlled concurrent regional changes, explicit interference estimand, regional inference, inventory/markup measurement validity]
    threats_addressed: [raw trend rejection and detrending, earlier Guangdong onset, six-province and cleaner-neighbor-control definitions, firm effects, alternate markup and finished inventory]
    evidence_refs: [E1, E4, E6]
method_transfer: null
readiness_blockers:
  - Conditional binary province exposure only. Reconcile provincial severity source and vintage before continuous-case or precise neighbor-threshold replication; manuscript counts and mainland/global shares must not be certified as official final statistics.
  - Assess outcome-specific trend continuation, Guangdong2002 contamination, regional common-shock uncertainty and interference. Paper detrending/clustering is documented, not an automatic causal guarantee for a new idea.
  - Exact markup replication additionally requires production value, labor/material costs, lagged total inventory, finished-goods inventory for stockout, capital/age/ownership and probit implementation; no executable code or complete cleaning protocol was inspected. A different observed firm outcome does not automatically require the markup model.
  - Published2026 metadata is verified but final body revisions remain unchecked. Preserve the2025 source-version boundary and audit location/sample selection before reproducing reported coefficients.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

SARS begins in Guangdong in November2002 and spreads to other mainland
regions in2003. Official reporting develops while the epidemic unfolds:
WHO describes a new national electronic reporting system in March, and the
Ministry briefing describes provincial spread, travel monitoring and coordinated
prevention [E2,E3]. A firm can lose customers or change production without
having an infected employee. The empirical object is epidemic-plus-response
economic exposure, not a single randomized policy or pure infection effect.

## What Changed

Manufacturing firms in heavily affected provinces face greater disruption
than firms elsewhere. The paper studies persistence through2007; that is
not a claim that the original epidemic continues throughout the panel. WHO's
final table separates mainland5327 probable cases from a global8096 and
records June2003 as mainland last onset [E5]. The manuscript's incompatible
mainland/global shares are not reproduced as institutional facts.

## Implementation and Assignment

Use the four-province flag for Beijing, Guangdong, Shanxi and Inner Mongolia
and multiply it by the annual post rule: Guangdong from2002, others from2003.
This is actual Eq14 encoding [E1,reported claim]. It is not interchangeable
with the uniform2003 robustness definition. Government reporting verifies the
unequal regional regime, not every manuscript numerical case count [E2,E3].
Continuous-case exposure remains conditional on recovering its source/vintage;
do not overwrite author counts with final official counts and call it replication.

## Why This Creates Empirical Variation

Different province groups experience different timing and intensity, allowing
within-panel relative comparisons. The paper connects these to manufacturing
markup, inventory and regional market shares [E1,reported claim]. Actual use
does not make realized provincial exposure randomized. Other provinces can
gain market share or face national disruption, so the intended contrast is
relative redistribution rather than the country's total economic loss.

## Identification Risks

Raw markup pre-trends fail; Guangdong drives the divergence. AppendixB
subtracts fitted group slopes and assumes continuation without SARS, with
outcome-specific treatment of2002 [E1,E4,reported claim]. A new outcome requires
its own diagnostic, not inherited parallel trends. Provincial common shocks
also demand inference beyond counting over a million firms; the paper's
city-industry-year clustering is a reported choice, not settled validation
[E1;analytical inference]. Inventory mediation is suggestive, and policy,
infection, customer demand and supply disruptions are not separately identified.

## Data Requirements

The default contract needs firm-year outcomes, historical province/city and
industry codes, firm controls and enough pre/post coverage. Record survey
entry, exit and location changes rather than assuming appearances are business
births. Preferred markup specifically needs output value rather than sales,
production costs, lagged inventory, and finished inventory to code non-stockout;
Eq10 adjusts raw markup using an estimated probability [E1,E4,reported claim].
These additional accounting/model inputs are needed for that outcome, not
every new firm-performance application. PPI weighting belongs to a separate
province-level validation and is not silently copied into firm regressions.

## Evidence Notes

The2025 author body and relevant appendix passages were inspected, while
Crossref metadata and the university notice establish2026 publication only.
Final typeset methods and code remain uninspected [E6]. Primary WHO and
Ministry sources establish chronology/reporting/response boundaries [E2,E3,E5];
they do not validate the author's exact continuous provincial series. The
conditional binary record preserves a usable comparison without hiding that
numerical-replication gap. Existing COVID lockdown/community records describe
different events and units; they are related, not duplicate SARS cases.
