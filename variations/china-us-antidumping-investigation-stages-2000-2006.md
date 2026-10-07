---
schema_version: 2
id: china-us-antidumping-investigation-stages-2000-2006
name: US Antidumping Investigation Stages Faced by Chinese Exporters, 2000–2006
aliases:
- Lu Tao Zhang antidumping investigations
- US antidumping Chinese exporters
- 美国反倾销调查阶段
- 中国出口企业反倾销冲击
status: grounded
provenance:
  task_id: task-d49671cd452b
scope:
  country: China
  regions: [Mainland Chinese exporters to the United States]
  domains: [international-trade, firm-dynamics, industrial-organization, development]
  variation_type: event-shock
  knowledge_role: global-china-variation
  china_relevance: US product-specific investigations change market access and uncertainty faced by mainland Chinese exporters. This is a firm and industrial-development application, not a US domestic-outcome or overseas-method record.
identity:
  instrument: US antidumping investigation proceedings against Chinese exports initiated during 2000–2006, represented as one investigation-stage mechanism rather than separate records for each stage or outcome.
  authority: US Department of Commerce determines dumping; US International Trade Commission determines injury. Both final determinations must be affirmative for an antidumping order.
  legal_identifiers:
  - Tariff Act of 1930, Title VII, sections 733, 735 and 736
  - 19 USC 1673b, 1673d and 1673e, 2006 edition
  - A-570-890 / 731-TA-1058, wooden bedroom furniture, inspected implementation example only
  implementation_regime: Product and exporter-specific US trade-remedy proceedings, with preliminary and final decisions, possible termination, provisional security and definitive duties. This is not a uniform national tariff change or a later administrative-review shock.
  assignment_mechanism: An investigated China-origin product enters dated proceeding stages. The paper maps US HS10 products to HS6 and joins Chinese HS8 shipments at HS6; its main sample selects cases with affirmative final ITC decisions after endpoint and overlap exclusions. Selection and duty intensity are not random.
  parent: null
  related_variations: [china-trade-policy-uncertainty]
timeline:
  announcement: null
  effective: null
  implementation_start: 2000
  implementation_end: 2006
  local_timing: The application's observation window is monthly 2000–2006, not a common legal effective date. Its three boundaries are initiation month, preliminary ITC injury month and final ITC injury month. Commerce preliminary measures and the order have separate dates; some initiated cases end after the panel window.
  anticipation: Petitions and investigation initiation can change orders before deposits begin. The first investigation interval is itself an uncertainty exposure, not an untreated pre-period.
  last_verified: '2026-10-07'
assignment:
  unit: HS6 product-month, or Chinese exporter-HS6 product-month, for exports to the United States.
  treated: Chinese shipments mapped to products investigated by the United States; the main application uses 28 successful cases after the reported sample exclusions.
  comparison_pool: Unaffected HS6 products and their exporters within the treated products' HS4 categories; an alternative pool retains unaffected products above a fitted investigation-probability cutoff.
  rule: The application assigns disjoint intervals [initiation, preliminary ITC), [preliminary ITC, final ITC), and [final ITC, panel end]. Only the first is a binary investigated-product interaction; the latter two interact their intervals with preliminary and final duties respectively.
  intensity: Equation 1 uses preliminary product duties and final product duties; firm-product regressions replace final duties with firm-product duties. Footnote 4 reports no within-product across-firm preliminary-duty variation. The paper does not make duty assignment an instrument for random treatment.
  exemptions:
  - Negative injury or dumping decisions can terminate proceedings; provisional security may be refunded.
  - Case scope and exporter exclusions matter. The inspected furniture order excludes Markor Tianjin with a de minimis margin; treating its published 0.83 percent margin as an operative positive duty would be wrong.
  compliance: Legal exposure is determined by written merchandise scope, exporter-specific rates and entry timing, not HS6 membership alone. The paper's HS6 aggregation measures a broader exposure proxy rather than proving every shipment owes the duty.
  exposure_construction: Preserve case ID and all agency dates; pad HS codes to their declared precision, map US HS10 and Chinese HS8 to a harmonized HS6, aggregate monthly customs outcomes, and flag repeated or overlapping case exposure. Construct the paper's ITC-stage intervals separately from Commerce measure dates. Reconstruct product duty aggregation and exporter-rate matching before running the intensity regression; do not substitute a countrywide rate for all firms.
  required_identifiers: [case ID, HS6 product code, calendar month, exporter ID, exporter name, destination country]
  spillovers: Exports may move to other products or destinations, and intermediaries can redirect purchases. Unaffected products in the same HS4 may therefore be affected indirectly.
research_compatibility:
  outcome_domains: [export volume, export value, export unit value, exporter count, product-market exit, destination diversion, firm allocation]
  affected_populations: [Chinese manufacturing exporters, trading intermediaries, direct exporters, single-product exporters, multiproduct exporters]
  mechanism_channels: [market-access costs, investigation uncertainty, exporter selection, trade intermediation, product and destination reallocation]
  best_for: [monthly exporter responses to trade-remedy proceedings, firm heterogeneity in foreign market-access shocks, industrial export reallocation]
  not_good_for: [automatic exogenous duty instrument, domestic firm closure inferred from export exit, measured TFP inferred only from export size, city treatment without a predetermined exposure bridge, finance or environmental-policy collection]
design:
  claim_type: reduced-form
  affordances: [dated investigation stages, product-level contrasts, duty intensity, exporter heterogeneity]
  candidate_designs: [monthly product difference-in-differences, monthly firm-product difference-in-differences, event-time diagnostic]
  identifying_variation: Changes across disjoint investigation intervals for investigated Chinese products relative to unaffected products, with preliminary and final duty interactions and product and calendar-month fixed effects.
  primary_strategy: The inspected October 2013 manuscript's equations 1–5 combine investigation-stage DID with product-level or firm-product outcomes. Standard errors are clustered at HS6 product level.
  estimand: Differential export responses during initiation, preliminary-ITC-to-final-ITC and final-ITC intervals in the selected successful-case population, with duty-scaled responses in the latter two intervals. This is not the unconditional effect of all petitions or a pure effect of starting cash deposits.
  treatment_variable: Treatment_p × Post1_pt; PreliminaryDuties_pt × Post2_pt; FinalDuties_pt × Post3_pt. Post1 is [t0,t1), Post2 is [t1,t2), Post3 is t>=t2, where t0 is initiation, t1 preliminary ITC, and t2 final ITC month. Firm-product analysis uses firm-product final duties.
  comparison_logic: Control 1 consists of unaffected products within HS4. Control 2 consists of unaffected products whose fitted investigation probability is at least the 75th percentile of the treated products' fitted probabilities, using import value, US GDP growth, exchange-rate index, past investigations and HS4 indicators. This is not nearest-neighbor propensity matching.
  estimation_notes: Keep the three intervals disjoint rather than cumulative post dummies. The selected case window and overlap exclusions must be reproduced; retain negative/withdrawn cases as distinct robustness samples. Contemporary estimators should examine heterogeneous timing effects rather than interpreting the original fixed-effects specification as universally unbiased.
  assumptions:
  - Absent investigation exposure, treated and chosen control products would have comparable outcome changes after fixed effects and stated controls.
  - Petition selection, final success and duty intensity do not introduce unaddressed outcome-specific differential trends.
  - Harmonized HS6 and exporter links represent the relevant product and rate exposure adequately.
  - Other trade remedies and export diversion do not invalidate the chosen controls.
  diagnostics:
  - Pre-initiation leads and product-specific trends, with explicit support around each event.
  - Compare the two control pools and examine their propensity support.
  - Compare the 28 successful cases with unsuccessful and withdrawn-case samples.
  - Examine concurrent foreign antidumping cases, US safeguards and China's WTO tariff changes.
  - Compare HS6 products by constituent HS10 scope coverage; separately check excluded exporters.
  - Recompute intervals using Commerce measure dates when the research question concerns actual deposits rather than investigation stages.
threats:
- type: endogenous-investigation-selection
  basis: documented
  condition: The paper selects successful proceedings and predicts investigation probability using imports and other covariates. Neither petition selection nor realized success is random.
  evidence_refs: [E1]
  possible_diagnostics: [pretrend checks, alternative control pool, include unsuccessful and withdrawn cases, report the selected-case estimand]
- type: stage-versus-legal-treatment-timing
  basis: documented
  condition: ITC injury dates differ from Commerce security and order dates. Furniture has a January 2004 preliminary ITC month but June 2004 preliminary security, a December 2004 final injury month and a January 2005 order, with a provisional-measure lapse and an exporter exclusion.
  evidence_refs: [E1, E2, E3, E4, E5, E6]
  possible_diagnostics: [preserve all dates, inspect notices and scope, distinguish investigation and deposit estimands]
- type: aggregation-and-rate-measurement
  basis: documented
  condition: HS6 contains narrower legally covered products and potentially exempt exporters. The archive has countrywide and firm rates, but the original product aggregation and name-rate bridge were not reconstructed.
  evidence_refs: [E1, E5, E6]
  possible_diagnostics: [scope-aware product crosswalk, exporter exclusion audit, product rate aggregation documentation, manual review of ambiguous firm names]
- type: spillovers-and-concurrent-shocks
  basis: documented
  condition: The authors examine foreign cases, US safeguards, China's WTO tariff changes and processing trade; these checks do not establish absence of all diversion or concurrent shocks.
  evidence_refs: [E1]
  possible_diagnostics: [third-country export outcomes, exclude concurrent cases, ordinary-trade subsample, alternative comparison products]
- type: exporter-classification-and-productivity-proxy
  basis: documented
  condition: Intermediaries are inferred from name strings and productivity from export volume in the baseline; the manufacturing-survey match is a limited validation subset. Export-market exit is not domestic firm death.
  evidence_refs: [E1]
  possible_diagnostics: [validate names against business activities, distinguish US-only and worldwide single-product status, avoid direct TFP or closure interpretation]
empirical_requirements:
  contract_version: 1
  population: Mainland Chinese exporters of investigated and comparison products to the United States; non-agricultural applications should explicitly select industrial cases rather than silently calling the paper's entire mixed sample non-agricultural.
  observation_unit: Exporter-HS6-product-month
  geography_level: Mainland China exporters linked to US destination exposure
  time_start: 2000
  time_end: 2006
  minimum_frequency: monthly
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields: [export value, export quantity, destination country, case outcome, initiation date, preliminary ITC date, final ITC date, preliminary duty, final product duty, exporter-specific final duty]
  required_identifiers: [exporter ID, exporter name, Chinese HS8 code, US HS10 code, harmonized HS6 code, case ID, calendar month]
  treatment_key: [case ID, harmonized HS6 code, calendar month, exporter-rate link]
  treatment_source: The paper uses Chinese Customs monthly transactions and Bown's 2010 GAD. A later public GAD USA workbook supplies case, product and foreign-firm sheets, but is not the original estimation file. Agency notices establish legal scope and measure timing.
  measurement_risks:
  - One pre and post month is only a minimum dimensional contract, not adequate trend support; inspect longer leads and case-specific stage lengths.
  - Access to firm-level Customs and usable identifiers must be lawful; publication does not establish public microdata availability.
  - Confirm original rate units and product aggregation; do not average unrelated exporter rates or apply a PRC-wide rate to exempt respondents.
  - Pad product codes before truncation and reconcile HS revisions and narrower written scope.
  - Preserve exporter groups and aliases in named respondent lists instead of assuming an exact customs-name join.
  - Preserve 2010 versus 2016 archive vintage; later case outcomes and inconsistent dates need original-notice review.
  - Baseline needs no complete Customs-to-manufacturing-survey merge; the paper uses that match only to validate its export-size proxy.
  - Intermediary and product-diversity analyses additionally need name strings, pre-event product portfolios and other destinations.
evidence:
- id: E1
  source_type: paper
  citation: Lu, Yi, Zhigang Tao and Yan Zhang. How Do Exporters Respond to Antidumping Investigations? HKIMR Working Paper 19/2013, October 2013; associated JIE article 91(2), 290–300.
  url: https://www.aof.org.hk/uploads/publication/364/wp-no-19_2013-final-.pdf
  date: '2013-10'
  supports: [scope.china_relevance, identity.instrument, identity.assignment_mechanism, timeline.local_timing, timeline.anticipation, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.intensity, assignment.exposure_construction, assignment.required_identifiers, assignment.spillovers, design.identifying_variation, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, design.assumptions, design.diagnostics, threats.condition, empirical_requirements.population, empirical_requirements.observation_unit, empirical_requirements.time_start, empirical_requirements.time_end, empirical_requirements.required_fields, empirical_requirements.required_identifiers, empirical_requirements.treatment_key, empirical_requirements.treatment_source, empirical_requirements.measurement_risks, design_applications.research_question, design_applications.population, design_applications.outcome, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design, design_applications.threats_addressed]
  verification_status: verified
  access_level: full-text
  locator: Institutional 47-page PDF inspected 2026-10-07, printed pp.3–8, 15–17 and Appendix Table A2 p.31; equation 1 on printed p.5 visually inspected. These are PDF pp.6–11, 18–20 and 34. This is an October 2013 full manuscript, not the publisher's typeset article or replication code. Assertions about data and robustness remain author-reported.
- id: E2
  source_type: policy-document
  citation: United States Code, 2006 edition, title 19, section 1673b, preliminary determinations.
  url: https://www.govinfo.gov/content/pkg/USCODE-2006-title19/html/USCODE-2006-title19-chap4-subtitleIV-partII-sec1673b.htm
  date: 2006
  supports: [identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.local_timing, assignment.compliance, assignment.exemptions, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Actual historical statute text inspected, subsections (a)–(e), especially (d) affirmative Commerce preliminary determination, security, suspension and four/six-month limit, and (e) critical-circumstance retroactivity. ITC preliminary injury alone is not the security trigger.
- id: E3
  source_type: policy-document
  citation: United States Code, 2006 edition, title 19, section 1673d, final determinations.
  url: https://www.govinfo.gov/content/pkg/USCODE-2006-title19/html/USCODE-2006-title19-chap4-subtitleIV-partII-sec1673d.htm
  date: 2006
  supports: [identity.authority, identity.legal_identifiers, identity.implementation_regime, assignment.exemptions, assignment.compliance, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Historical text subsections (a), (b) and (c), including separate Commerce dumping and ITC injury decisions and (c)(2) negative determination termination and refund. Inspected 2026-10-07.
- id: E4
  source_type: policy-document
  citation: United States Code, 2006 edition, title 19, section 1673e, assessment of duty.
  url: https://www.govinfo.gov/content/pkg/USCODE-2006-title19/html/USCODE-2006-title19-chap4-subtitleIV-partII-sec1673e.htm
  date: 2006
  supports: [identity.legal_identifiers, identity.implementation_regime, timeline.local_timing, assignment.compliance, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Historical text subsections (a)–(c), order publication after affirmative injury notification, written merchandise description, deposits pending liquidation and special injury provisions. Inspected 2026-10-07; does not verify every case's actual implementation date.
- id: E5
  source_type: implementation-document
  citation: Department of Commerce. Wooden Bedroom Furniture from the People's Republic of China, amended final determination and antidumping duty order. Federal Register 70, 329–333, January 4, 2005, E4-3926, A-570-890.
  url: https://www.govinfo.gov/content/pkg/FR-2005-01-04/html/E4-3926.htm
  date: '2005-01-04'
  supports: [identity.legal_identifiers, timeline.local_timing, assignment.exemptions, assignment.compliance, threats.condition, empirical_requirements.measurement_risks]
  verification_status: verified
  access_level: official-document
  locator: Full notice read, effective-date header, amended determination, antidumping duty order pp.329–332, scope and suspension pp.332–333. Identifies June 24 preliminary measure, December 23 ITC notification, December 21 provisional-limit endpoint, excluded Markor, company rates and dispositive written scope. One industrial case, not verification of all cases.
- id: E6
  source_type: archive
  citation: Bown, Chad P. Temporary Trade Barriers Database, June 2016 public archive, GAD USA workbook through 2015Q4.
  url: https://www.chadpbown.com/wp-content/uploads/2019/02/TTBD_2016.zip
  date: 2016
  supports: [assignment.exposure_construction, assignment.required_identifiers, threats.condition, empirical_requirements.treatment_source, empirical_requirements.measurement_risks]
  verification_status: verified
  access_level: dataset
  locator: In-memory inspection of GAD/GAD-USA.xls sheets AD-USA-Master, AD-USA-Products and AD-USA-Foreign-Firms, columns and China 2000–2006 case rows, especially USA-AD-1058. Separate ITC, dumping and measure dates; HS_DIGITS; CASE_ID; named final-rate rows. Later archive is not the authors' 2010 vintage or verified Customs-rate matching.
- id: E7
  source_type: paper
  citation: IDEAS publication metadata, Lu, Tao and Zhang, Journal of International Economics 91(2), 290–300, 2013.
  url: https://ideas.repec.org/a/eee/inecon/v91y2013i2p290-300.html
  date: 2013
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: Publication entry inspected during screen task-41d2316467a8; identifies DOI 10.1016/j.jinteco.2013.08.005 and journal publication. Metadata is not evidence for treatment coding.
- id: E8
  source_type: paper
  citation: Lu, Tao and Zhang, 2013, JIE article DOI identifier.
  url: https://doi.org/10.1016/j.jinteco.2013.08.005
  date: 2013
  supports: [design_applications.doi]
  verification_status: reported
  access_level: metadata
  locator: DOI identified through the inspected IDEAS publication entry E7; identifier only, not publisher full-text access or substantive coding evidence.
design_applications:
- paper: How do exporters respond to antidumping investigations?
  doi: 10.1016/j.jinteco.2013.08.005
  journal: Journal of International Economics
  year: 2013
  research_question: How do Chinese exporters respond to US investigation stages, and how do responses differ by intermediary status and product diversification?
  population: Chinese exporters and HS6 products to the United States, monthly 2000–2006; main sample of 28 successful cases after the reported five endpoint/overlap exclusions from 47 initial cases.
  outcome: Export volume, exporter counts, unit values, non-US exports and product-market exit. Export size is a productivity proxy, not directly measured baseline TFP.
  data_used: [Chinese Customs monthly HS8 transactions 2000–2006, Bown 2010 Global Antidumping Database US cases and duties, limited manufacturing-survey match for export-size proxy validation]
  treatment_encoding: October 2013 manuscript equations 1–4 use the three disjoint ITC-based intervals, with preliminary and final duty intensity; final intensity becomes firm-product-specific in firm regressions. May 2012 manuscript's simpler specification is not substituted.
  comparison: Unaffected HS6 products within HS4, or unaffected products above the treated-probability 75th-percentile cutoff. Retain the alternative pools separately.
  empirical_design: Product and firm-product monthly DID with fixed effects and HS6-clustered errors; stage response and exporter-heterogeneity analysis.
  assumptions: [comparable counterfactual changes, no unaddressed differential contemporaneous shocks, appropriate stage and duty measurement, sufficiently unaffected comparison products]
  threats_addressed: [pre-initiation trends, product trends, unsuccessful and withdrawn cases, concurrent foreign antidumping, processing trade, foreign ownership, HS aggregation, safeguards and WTO tariff changes, worldwide single-product definition]
  evidence_refs: [E1, E7, E8]
method_transfer: null
readiness_blockers:
- Obtain lawful Customs access and recover case-to-HS6 and named-exporter-rate joins, original product-duty aggregation and rate units. The paper explains the contrast; a ready-to-run treatment matrix was not inspected.
- Reconcile the 2010 estimation vintage and exact 28-case/81-HS6 selection before replication. The 2016 workbook contains dates inconsistent with chronological order and later outcomes; never silently repair them or treat it as an identical estimation file.
- The full October 2013 manuscript, not the publisher's typeset article or estimation code, supports the application. Verify final-version differences if exact published replication is required.
- Industrial-only research must declare exclusions from the paper's mixed sample, which also contains honey and shrimp. A regional application requires a separately justified predetermined local export-exposure bridge and spillover analysis.
- Treat stage effects as investigation responses, not pure legally operative duty effects. Case notices must close security lapses, de minimis exclusions and narrow product scope for a deposit-timing question.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

US antidumping is a two-agency proceeding, not a tariff assigned uniformly to
Chinese firms. Commerce determines dumping and the ITC determines injury;
negative decisions can terminate a case. Affirmative Commerce preliminary
decisions trigger security and suspension, while definitive orders depend on
both final decisions. Historical statutory provisions establish this separation.
[E2–E4, verified]

Lu, Tao and Zhang study the mainland-exporter side of this process. Different
products enter investigations at different dates, allowing a monthly comparison
with unaffected products. The relevant economic channels include uncertainty,
import costs, exporter selection and diversion. These are conditional research
opportunities: investigation and final success are selected, not random.
[E1, reported application; analytical inference]

## What Changed

The paper follows initiation, preliminary ITC injury and final ITC injury
intervals. Its October 2013 specification attaches preliminary and final duties
to the latter intervals. Saving only three binary post indicators would lose
the inspected application's intensity dimension. These stages belong in one
record because they describe one proceeding mechanism, not three independent
policy experiments. [E1, equations 1–4]

## Implementation and Assignment

For an investigated product, define t0 as initiation month, t1 as preliminary
ITC month and t2 as final ITC month. Encode mutually exclusive Post1=[t0,t1),
Post2=[t1,t2) and Post3>=t2. Join Chinese HS8 shipments and US case HS10 products
at harmonized HS6, preserving case and exporter identifiers. The paper drops
two endpoint cases and three overlapping cases, then uses 28 successful cases
in its baseline. Its appendix lists 47 initial cases, not the fully constructed
estimation matrix. [E1, reported application]

The furniture example makes the institutional distinction concrete. Its
preliminary ITC month is January 2004, but provisional security begins in June.
The January 2005 order reports December injury notification, a provisional
measure lapse and an excluded exporter. Thus the paper's monthly intervals
are encodable, but their labels cannot establish continuous duty liability.
Written scope controls coverage even where a tariff code is listed for
convenience. [E1 Table A2; E5, verified]

## Why This Creates Empirical Variation

The first contrast measures an investigation interval; the next two scale stage
exposure by duties. Controls are unaffected products within HS4 or a high-fitted-
probability pool, not a generic sample of all exporters. Identification depends
on comparable counterfactual changes and defensible scope/rate measurement.
The authors' pretrend and sample checks inform that judgment without proving
exogeneity for a new outcome. [E1, reported application; analytical inference]

## Identification Risks

Successful-case selection, endogenous petitioning and unequal rates are central,
not peripheral, concerns. Nearby products can absorb diverted demand; exporters
can redirect trade elsewhere. HS6 may mix covered and uncovered goods, while
rate schedules distinguish named firms and exclusions. The inspected furniture
notice independently demonstrates why a common PRC rate cannot be imposed on
every exporter. [E1; E5; analytical inference]

The paper identifies intermediaries through names containing 进出口, 经贸 or
贸易, and defines its baseline single-product category from pre-initiation
exports to the US. Worldwide diversification is a separate robustness check.
Neither name classification nor export size certifies business type or TFP;
ceasing a product's exports is not firm closure. [E1, reported definitions]

## Data Requirements

Use monthly Customs transactions with product, exporter ID/name, destination,
value and quantity, plus dated cases, outcomes and applicable duties. Keep the
case-product bridge separate from the respondent-name-rate bridge. Product
aggregates need no complete manufacturing-survey merge; that additional survey
is used only for proxy validation in the inspected application. [E1]

The public later GAD has useful relational sheets, but access is not an exact
replication certificate. Preserve its vintage and inspect original notices for
inconsistent dates and altered outcomes. The knowledge contract states the
needed joins; it does not claim to supply restricted microdata or the authors'
uninspected estimation file. [E6; analytical inference]

## Evidence Notes

The May 2012 manuscript was a screening lead. The full October 2013 manuscript
now supports the duty-interacted specification, while publication metadata
links it to the JIE article. No publisher typeset text or estimation code was
inspected. Statutes support the legal process; one furniture order verifies an
industrial implementation example, not every case. Grounded status preserves
a recoverable institutional and empirical decision chain with explicit
reconstruction conditions, not a completed treatment-data deposit.
