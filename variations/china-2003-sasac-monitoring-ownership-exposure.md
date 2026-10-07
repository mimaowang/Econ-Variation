---
schema_version: 2
id: china-2003-sasac-monitoring-ownership-exposure
name: China SASAC monitoring reform and ownership-based exposure from 2004
aliases: [国资委监管体制改革所有制暴露, Li Zhang external government monitoring of SOEs]
status: grounded
provenance:
  task_id: task-1c021e8ec230
scope:
  country: China
  regions: [Mainland China]
  domains: [firm-performance, industrial-economics, development, state-owned-enterprises, regional-monitoring-costs]
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: An Economic Journal paper compares Chinese manufacturing firms classified by state ownership before and after the SASAC regime, with oversight-distance heterogeneity. The empirical annual ownership proxy is distinguished from actual legal supervision and local agency opening dates.
identity:
  instrument: The 2003 reform establishing authorized state-asset supervision and investor-responsibility institutions, encoded in the paper as ownership-based exposure from 2004.
  authority: State Council and provincial/prefecture governments; their authorized state-asset supervision bodies perform investor responsibilities for designated enterprises.
  legal_identifiers: [国务院令第378号]
  implementation_regime: State assets remain state-owned; authorized central and local bodies exercise investor responsibilities and organize supervision, executive assessment and governance. Legal scope includes assets in state-owned, state-controlled and state-participating enterprises but excludes financial institutions. Supervisory responsibilities follow designated enterprises and corporate rights, not a universal 30-percent ownership cutoff.
  assignment_mechanism: The paper interacts annual state ownership above30% with a common post2004 indicator. This is an observational proxy for differential exposure to national governance reform, not random ownership, a statutory threshold experiment, or a verified enterprise-level agency-adoption series.
  parent: null
  related_variations: [china-soe-decentralization]
timeline:
  announcement: The national body is established in2003; State Council Decree378 is signed and promulgated2003-05-27.
  effective: Decree378 takes effect upon promulgation on2003-05-27; this does not establish operational supervision for every local firm on that date.
  implementation_start: 2003
  implementation_end: null
  local_timing: Eq22 of the inspected July2021 author version sets Post=1 from2004. Its early2004 provincial-completion wording differs from the official NDRC retrospective, which states all31 provincial bodies plus Xinjiang Production and Construction Corps were formed by June2004. The2007 report describes prefecture establishment as then largely completed, not complete everywhere in2004. Annual2004 is the paper's proxy, not a monthly or firm-specific implementation date.
  anticipation: National institutional changes during2003 and ongoing SOE reforms can affect pre2004 outcomes; the paper explicitly treats2003 as transition and tests excluding it.
  last_verified: '2026-10-07'
assignment:
  unit: Firm-year ownership exposure; additional spatial heterogeneity uses firm-to-affiliated-government distance.
  treated: Observed manufacturing firm-years with state ownership share strictly above30% in and after2004 under the inspected application.
  comparison_pool: Firm-years not meeting that ownership definition and earlier observations. Non-SOEs are not necessarily wholly private or legally unexposed to every state-asset rule; supplier/market spillovers also reach them.
  rule: Code SOE_jt=1 if annual state ownership share exceeds0.30 and Post_t=1 if year>=2004; treatment is their product. Do not replace annual status with initial status while claiming to reproduce Eq22. For a new design, separately declare a fixed pre-reform cohort or stable-ownership restriction and its estimand.
  intensity: Binary ownership-by-post exposure. Eq25 and related specifications interact this same regime with logged spherical oversight distance; distance is a monitoring-cost proxy, not a new policy or excluded instrument.
  exemptions: [Financial institutions excluded from Decree378, Prefectures with few state assets may be authorized not to establish a separate body, Actual supervised-enterprise lists and shareholding governance differ from the empirical30% classification]
  compliance: Investor rights and designated-enterprise supervision ground the institution. Ownership share alone does not verify an inspection, supervisory board dispatch, effective monitoring strength or agency compliance for each sampled firm.
  exposure_construction: Harmonize annual firm identifiers and capital ownership components to recover state share and year. Join the declared firm-year outcome to SOE*Post without imputing missing state share as private. If using distance, recover annual registration affiliation and firm/government geography, assign central/provincial/prefecture seats, map county/township affiliations to prefecture as the paper does, and exclude ambiguous other affiliations. The provider's coordinate and zero-distance implementation was not recovered from code; geographic extensions require those choices rather than an invented formula.
  required_identifiers: [firm_id, year, industry_code, province_code, registration_affiliation_type]
  spillovers: Changes in SOE input/output prices can affect private trading partners. The comparison identifies relative outcomes, not the total national reform effect.
research_compatibility:
  outcome_domains: [firm productivity, quality-adjusted material input prices, manufacturing performance, corporate governance]
  affected_populations: [surveyed mainland manufacturing SOEs and non-SOEs]
  mechanism_channels: [external monitoring, managerial effort and procurement behavior, executive assessment, corporate governance]
  best_for: [Conditional ownership-group comparisons of national governance reform, Firm performance panels with state-capital histories, Monitoring-distance heterogeneity after a separate geography audit]
  not_good_for: [Random ownership assignment or RDD at30% state share, Verified inspection treatment without supervisory records, Directly observed procurement corruption or physical productivity from accounting data alone, A uniform exact-day local rollout, Isolating monitoring from every companion governance measure]
design:
  claim_type: reduced-form
  affordances: [national regime change, state-ownership comparison, ownership-history restrictions, oversight-distance heterogeneity]
  candidate_designs: [ownership-by-post DID-style comparison, ownership-group event study, oversight-distance triple interaction]
  identifying_variation: Changes in outcomes of firms with greater state ownership relative to other firms from2004, and differences in that relative change across oversight distance for geographic extensions.
  primary_strategy: Inspected Eq22 regresses the outcome on SOE, SOE*Post, firm controls and industry/province/year effects; Table3 also includes registration-affiliation effects and firm-clustered errors. Firm fixed effects appear in AppendixG12 robustness, not the stated Eq22 baseline. A new causal application should evaluate firm effects, ownership switching, group trends and effective assignment-level uncertainty rather than copy the baseline mechanically.
  estimand: Conditional relative change in sampled SOE outcomes under the governance package compared with non-SOEs; not an effect of actual inspections or a national aggregate treatment effect.
  treatment_variable: Annual SOE_jt*1(year>=2004), with SOE_jt based on state share>30%. Geographic specification additionally includes SOE*Post*log(oversight distance) and lower-order terms.
  comparison_logic: Compare pre/post ownership-group trajectories conditional on controls and sample coverage. National law alone cannot eliminate differential restructuring, WTO exposure or ownership selection.
  estimation_notes: ASIP1998–2007 covers all surveyed SOEs and non-state firms above RMB5million annual sales; reported data include326,294 firms across19 two-digit manufacturing industries. Full-control Table3 uses873,414 firm-years versus1,196,053 without R&D/capital-intensity controls. Material prices and productivity are estimated industry by industry using CES production, demand, input-quality and dynamic-process assumptions; they are not directly observed prices or physical TFP. Default inputs include revenues, workers, wages, materials and capital. Oversight-distance regressions use a different affiliation-filtered sample. The road extension uses a2009 network, not a sample-period road-opening series.
  assumptions: [Comparable ownership-group counterfactual trends after controls, No differential concurrent reforms driving the intended comparison, Ownership proxy and sample histories appropriate to the estimand, Defensible industry-specific structural measurement for the paper's outcomes, Spillovers bounded and inference appropriate to common ownership-group shocks]
  diagnostics: [Event leads and outcome-specific pre-trends, Exclude2003 transition and inspect local timing, Stable ownership and fixed pre-policy ownership sensitivity, Firm effects and industry-specific trends, Actual supervisor roster versus ownership proxy validation, Balanced coverage without equating survey entry to business creation, Structural-outcome and alternative observed-outcome checks, Distance changes and geography audit before spatial extension]
threats:
  - type: legal scope versus ownership proxy
    basis: documented
    condition: Decree378 covers designated enterprise assets and investor rights, including state-participating enterprises. The paper's30% cutoff does not identify each firm's legal supervisor or actual monitoring onset.
    evidence_refs: [E1, E2]
    possible_diagnostics: [supervised-enterprise roster linkage, ownership-definition alternatives, fixed pre-reform classification]
  - type: phase-in and anticipation
    basis: documented
    condition: Reform starts during2003, provincial formation is complete by June2004 in official reporting, and local organization continues thereafter. The paper's common2004 dummy approximates a gradual regime.
    evidence_refs: [E1, E3]
    possible_diagnostics: [transition exclusion, timing sensitivity by supervising tier, original local histories for a rollout design]
  - type: differential productivity pretrend
    basis: reported
    condition: The main paper documents a slight narrowing of the productivity gap before treatment. AppendixG6 detrends using separate pre2003 group slopes, which assumes those counterfactual slopes would continue; it does not establish parallel trends for every outcome.
    evidence_refs: [E1, E4]
    possible_diagnostics: [outcome-specific event study, detrending sensitivity, alternate comparison populations]
  - type: endogenous ownership and structural change
    basis: reported
    condition: Privatization, restructuring, entry barriers and WTO exposure can differ by ownership. Annual ownership and surviving samples can respond to reform; dropping switchers changes the population rather than randomizing it.
    evidence_refs: [E1, E4]
    possible_diagnostics: [stable-ownership sample, pre-policy cohort, industry and trade exposure checks, sample attrition assessment]
  - type: generated outcome and monitoring inference
    basis: reported
    condition: Estimated input prices and productivity depend on optimal input choice, quality adjustment and industry normalization. High prices can also reflect transport, bargaining or other distortions; they are not direct proof of corrupt payments.
    evidence_refs: [E1]
    possible_diagnostics: [recover structural implementation and uncertainty, alternative outcomes, measurement-assumption sensitivity]
  - type: geographic selection and changing distance
    basis: reported
    condition: Firms can relocate or change affiliation; distance also reflects agglomeration and input markets. Ambiguous affiliations are dropped and road distance is measured after the sample.
    evidence_refs: [E1]
    possible_diagnostics: [fixed initial geography, unchanged-distance sample, non-oversight city comparison, do not use2009 roads as predetermined opening treatment]
empirical_requirements:
  contract_version: 1
  population: Mainland manufacturing firms observed in the1998–2007 industrial survey; private-firm sales thresholds and ownership-dependent coverage require explicit handling.
  observation_unit: firm-year
  geography_level: Province for the default comparison; firm and affiliated-government geography additionally needed for distance heterogeneity.
  time_start: 1998
  time_end: 2007
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields: [state capital and total capital for annual ownership share, declared annual performance outcome, sales revenue, workers, wage expenditure, material expenditure, book capital stock and deflators for published structural outcomes, firm age, lagged R&D indicator, capital intensity, registration affiliation and sample-retention history]
  required_identifiers: [firm_id, year, industry_code, province_code, registration_affiliation_type]
  treatment_key: [firm_id, year]
  treatment_source: Annual survey ownership plus the paper's post2004 convention; Decree378 and official formation history ground the regime, not a firm-specific adoption roster.
  measurement_risks: [annual ownership switching, state-participating firms below cutoff, registration versus actual supervision, above-scale survey coverage, structural outcome normalization and missing controls, incomplete local phase-in]
evidence:
  - id: E1
    source_type: paper
    citation: 'Li, Shengyu and Hongsong Zhang. Does External Monitoring from the Government Improve the Performance of State-Owned Enterprises? Economic Journal132(642),2022,675–708. Inspected author version July8,2021.'
    url: https://hongsongzhang.weebly.com/uploads/1/3/4/7/13473383/external_monitoring.pdf
    date: '2021-07-08'
    supports: [assignment.rule, assignment.intensity, assignment.exposure_construction, timeline.local_timing, design.primary_strategy, design.estimation_notes, empirical_requirements.required_fields, design_applications.treatment_encoding, design_applications.data_used]
    verification_status: reported
    access_level: full-text
    locator: '78-page author PDF, main printedpp7–17 institutional/data/structural sections, pp19/21/23–25 Eq21–22/Table3, pp27–29 Eq24/Table4/footnotes24–26, pp31–34 road and non-oversight distance methods. Version-linked publisher DOI10.1093/ej/ueab048 metadata establishes publication; final typeset body and implementation code not inspected. Table3 footer documents affiliation effects and firm clustering.'
  - id: E2
    source_type: policy-document
    citation: Original enterprise state-asset supervision interim regulation, State Council Decree378, promulgated2003-05-27; official Suzhou SASAC reprint attributed to State Council.
    url: https://guozw.suzhou.gov.cn/gzw/gzjgdcc/200505/26b33174290840d8af7b59f6d7f504b0.shtml
    date: '2003-05-27'
    supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, identity.assignment_mechanism, timeline.effective, assignment.exemptions, assignment.compliance]
    verification_status: verified
    access_level: official-document
    locator: Full47-article original text and promulgation inspected; Arts2,4–7,10–14,17–18,22,34–37,47. Financial exception, designated enterprises, authorized investor responsibilities, local organization, governance and reporting duties; no30% statistical cutoff. Reprint display2005 is not legal effective date, and later revised online versions were not substituted.
  - id: E3
    source_type: other
    citation: NDRC institutional-reform department, state-asset management framework progress,2007-02-27, attributed to SASAC website.
    url: https://www.ndrc.gov.cn/fggz/tzgg/ggkx/200702/t20070227_1032347_ext.html
    date: '2007-02-27'
    supports: [timeline.local_timing, identity.implementation_regime]
    verification_status: verified
    access_level: official-document
    locator: Entire progress paragraph read; states provincial bodies plus XPCC complete by June2004 and prefecture organization largely complete at reporting time. Does not supply city-by-city dates or supervised-firm rosters.
  - id: E4
    source_type: appendix
    citation: Li and Zhang July2021 author-version online appendix.
    url: https://hongsongzhang.weebly.com/uploads/1/3/4/7/13473383/external_monitoring.pdf
    date: '2021-07-08'
    supports: [design.estimation_notes, design.diagnostics, assignment.rule, timeline.anticipation, empirical_requirements.measurement_risks]
    verification_status: reported
    access_level: appendix
    locator: AppendixA pp1–3/PDF43–45; G1 p18/PDF60 and G6–G12 pp22–25/PDF64–67, including stable ownership, detrending, survey entry/exit definition, WTO, alternative ownership, transition-year exclusion and firm-FE Eq47–48. Linked code and remaining cleaning implementation not inspected; appendix narrative does not independently verify every historical supervisory practice.
  - id: E5
    source_type: other
    citation: Oxford Academic publisher bibliographic record for Li and Zhang, Economic Journal132(642),2022,675–708.
    url: https://doi.org/10.1093/ej/ueab048
    date: '2022-02'
    supports: [design_applications.paper, design_applications.journal, design_applications.year]
    verification_status: verified
    access_level: metadata
    locator: Publisher title, authors, issue year/pages, DOI and online publication2021-06-08. Metadata confirms published identity only; it does not verify methods or establish equality of final typeset text and inspected author version.
design_applications:
  - paper: Does External Monitoring from the Government Improve the Performance of State-Owned Enterprises?
    journal: Economic Journal
    year: 2022
    doi: 10.1093/ej/ueab048
    research_question: Does strengthened government monitoring improve Chinese SOEs' estimated input prices and productivity relative to non-SOEs, and does oversight distance moderate that change?
    population: Manufacturing firms in ASIP1998–2007, with ownership and sample-definition restrictions varying by specification.
    outcome: Structurally estimated quality-adjusted material prices and productivity; traditional LP productivity as an alternative.
    data_used: [ASIP1998–2007 firm accounts and capital ownership, Firm registration affiliation and geography for spatial extension, Industry deflators and structural production/demand estimation, 2009 road network only for road-distance sensitivity]
    treatment_encoding: Annual state share>30% interacted with year>=2004; the same exposure is interacted with logged oversight distance in the spatial extension.
    comparison: SOE versus non-SOE outcome changes before/after2004; different oversight distances within this ownership-group comparison.
    empirical_design: DID-style ownership interaction with baseline industry/province/year/affiliation effects and firm clustering; event coefficients and appendix firm-effect/stable-ownership alternatives.
    assumptions: [conditional ownership-group trends, valid regime proxy, structural outcome assumptions, controlled differential reforms and bounded interference]
    threats_addressed: [stable ownership and balanced panel checks, explicit productivity detrending, exclusion of2003, alternative ownership definition, WTO and trade sensitivity, firm effects and distance alternatives]
    evidence_refs: [E1, E4, E5]
method_transfer: null
readiness_blockers:
  - Conditional national ownership-proxy use only; obtain actual supervisor histories and designated-enterprise rosters before claiming firm-level monitoring receipt or precise staggered local treatment. Official June2004 completion and continuing prefecture formation limit the paper's early2004 narrative.
  - Annual ownership switching, differential trends, concurrent restructuring and indirect input-output effects must be assessed for the proposed outcome. The30% cutoff is not random or statutory assignment and baseline firm clustering cannot alone settle common group-shock uncertainty.
  - Exact published outcomes require structural estimation, normalization, deflators and cleaning implementation; no author code or provider files were inspected. Spatial use additionally needs validated affiliation/geography, distance units and zero-distance handling; no executable geocoding convention is certified here.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

The reform reorganizes how the state acts as an investor and supervises enterprise
assets. It gives authorized central and local bodies clearer responsibilities
for governance, executive assessment, reporting and asset preservation. Assets
remain state-owned; a supervisory body is not the legal owner of every firm's
assets in its own right [E2]. This matters because the paper's monitoring channel
is only one part of a wider governance package.

## What Changed

The institution begins in2003, while the paper codes a common annual post period
from2004 [E1, reported claim]. Official reporting puts complete provincial
formation in June2004 and describes prefecture organization as largely complete
only at its2007 reporting date [E3]. Consequently,2004 is a usable documented
application convention, not a verified simultaneous opening date. A fine-grained
rollout design would need different historical evidence.

## Implementation and Assignment

The basic construction is annual state capital divided by total capital,
classified strictly above30%, interacted with year>=2004. Keep missing capital
information distinct from zero state ownership. This classification is the
paper's empirical proxy [E1, reported claim], not the law's assignment cutoff:
the regulation covers state assets in designated and participating enterprises
and allocates responsibilities through government authorization [E2]. Use actual
rosters if the question concerns verified supervision rather than this proxy.

Oversight distance provides heterogeneity within the same reform. The paper maps
lower-tier affiliations to prefecture supervision and excludes ambiguous other
affiliations; distance can change through relocation or transfers [E1, reported
claim]. Existing SOE decentralization records concern those actual transfers,
not the introduction of this monitoring regime. Do not count distance and
ownership regressions as separate shocks.

## Why This Creates Empirical Variation

State-associated and other firms can respond differently to governance reform,
creating a before/after group comparison. Greater distance can moderate the
monitoring channel, but also captures market access and agglomeration. Eq22 and
its spatial extensions document actual paper use; neither ownership nor distance
is randomized [E1, reported claim; analytical inference]. The estimand is relative
firm performance, not a total national effect or a measured corruption incidence.

## Identification Risks

The paper acknowledges a pre-treatment productivity trend and uses separate
group detrending under a continuation assumption [E1, E4, reported claim].
Ownership switching, sample selection, privatization and WTO-related competition
can also produce differential changes. Stable-ownership and balanced-panel checks
help diagnose these issues but restrict the population. Survey appearance is not
necessarily actual business creation, and omission of2003 does not verify local
implementation in2004 [E4; analytical inference].

## Data Requirements

The default join is firm identifier and year, with annual ownership and a
defensible outcome. The paper's preferred outcomes additionally require
industry-specific structural estimation from revenue, materials, labor, wages
and capital. They are estimated quality-adjusted measures, not invoice prices
or directly observed physical efficiency [E1, reported claim]. A researcher
studying another outcome need not collect roads or firm coordinates merely
because the paper has geographic extensions; using those extensions requires
the extra affiliation and geography audit. A2009 road network cannot supply a
predetermined1998–2007 transport-opening treatment.

## Evidence Notes

This record is grounded for conditional idea matching. Official original legal
text and formation history establish the regime; inspected author methods and
appendix establish the ownership-year construction and its limits. Exact author
code, local supervisory rosters, geocoding and final typeset version were not
inspected. Preserve these implementation conditions instead of treating the
publication's causal language as a guarantee for a new research question.
