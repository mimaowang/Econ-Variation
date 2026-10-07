---
schema_version: 2
id: china-2002-income-tax-sharing-county-dependence
name: China 2002 Income-Tax Sharing and County Fiscal Dependence
aliases: [2002所得税分享改革县级财政暴露, Pre-reform income-tax dependence]
status: grounded
provenance:
  task_id: task-4649ac178487
scope:
  country: China
  regions: [Mainland China]
  domains: [regional-economics, development-economics, public-finance, local-government]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: A national revenue-sharing change altered Chinese county governments' fiscal resources with heterogeneous exposure inherited from their prior revenue structure.
identity:
  instrument: Central-local sharing of enterprise and personal income-tax revenue from2002, with a protected2001 local base and provincial adjustment of subprovincial arrangements
  authority: State Council, Ministry of Finance and provincial fiscal authorities
  legal_identifiers: [国发〔2001〕37号]
  implementation_regime: National sharing and base settlement, not a firm statutory-rate cut or the temporary2001 base-inflation response. County pass-through depends on subprovincial arrangements.
  assignment_mechanism: Common national onset interacted with predetermined county income-tax dependence; dependence is a paper-defined proxy, not legal random assignment or a binary county pilot.
  parent: null
  related_variations: [china-2001-income-tax-protected-base-incentive, china-2004-2005-fiscal-province-managing-county-rollout]
timeline:
  announcement: '2001-12-31'
  effective: '2002-01-01'
  implementation_start: 2002
  implementation_end: null
  local_timing: The national scheme specifies50/50 central-local sharing in2002 and60/40 in2003. The paper sets post=1 from2002; actual county retained shares and transfers are not a uniform50percent county revenue loss.
  anticipation: The formal notice is not proof of first revelation. The related2001 base-incentive record documents earlier communication and responses; test anticipation rather than assuming surprise.
  last_verified: '2026-10-07'
assignment:
  unit: County fiscal jurisdiction by year
  treated: Nationwide county jurisdictions, with relatively larger measured exposure where the pre-reform corporate-revenue/expenditure proxy is higher
  comparison_pool: Lower-dependence counties before and after the common reform, not untreated provinces; the reported sample excludes urban districts, changed county boundaries, Tibet and the four direct-controlled municipalities.
  rule: The legal national allocation changes how covered taxes are shared; the paper exploits cross-county fiscal dependence rather than claiming that every county retains the same local share. Preserve provincial discretion and base settlement.
  intensity: Arithmetic mean of four annual ratios1994-1997 of corporate revenue to annual government expenditure, interacted with1(year>=2002). Corporate revenue combines corporate income tax and SOE remitted profits; it is not total income tax including personal tax.
  exemptions: [Specified railway/post/bank and offshore oil-gas income taxes remain central revenue under the original scheme, Cross-regional centralized payments require separate allocation rules, Protected-base settlement and subprovincial arrangements alter realized county exposure]
  compliance: The dependence index predicts differential fiscal imbalance; no county-by-county legal retained-share schedule or actual treatment-receipt roster was inspected.
  exposure_construction: Join comparable1994-1997 corporate-revenue and expenditure categories by historical county code; calculate each annual ratio before averaging, then attach that fixed mean to1997-2007 county-year data. Keep percentage versus fraction scaling explicit. Do not substitute mean income-tax/total-revenue or a ratio of four-year sums.
  required_identifiers: [county_id, prefecture_id, province_id, year]
  spillovers: Fiscal transfers and neighboring demand can change comparison outcomes; low measured dependence does not establish no effect.
research_compatibility:
  outcome_domains: [County vertical fiscal imbalance, Local fiscal capacity, Regional economic volatility]
  affected_populations: [County and county-level-city governments]
  mechanism_channels: [Revenue recentralization, Intergovernmental transfer dependence, Local stabilization capacity]
  best_for: [Conditional county-panel exposure contrasts with historical fiscal categories and explicit provincial pass-through]
  not_good_for: [A county pilot rollout, Firm income-tax-rate treatment, Automatic exogeneity of fiscal dependence, Uniform permanent county revenue loss]
design:
  claim_type: reduced-form
  affordances: [Common policy onset, Predetermined fiscal dependence, County/year fixed effects, Separate legal and measured fiscal exposure]
  candidate_designs: [Continuous-exposure difference-in-differences]
  identifying_variation: Differential county change after2002 by fixed pre-reform dependence. Identification requires counterfactual trends comparable across fiscal structures, not just a common national policy date.
  primary_strategy: JRS12700 Section5.1.1/Table6 regresses VFI on post2002 times1994-1997 dependence with county/year effects and prefecture-clustered errors.
  estimand: Conditional relative change in county VFI per unit of pre-reform proxy exposure, not an independently measured county-specific tax-share elasticity.
  treatment_variable: 1(year>=2002) times mean1994-1997 corporate-revenue/annual-expenditure ratio
  comparison_logic: Compare higher and lower fixed fiscal dependence over time; both face the national reform. County industry/SOE structure and provincial allocation can generate differential trends.
  estimation_notes: VFI=(annual expenditure-annual own revenue)/annual expenditure, not gross transfers/total revenue. Table6 reports9531 observations/1682 counties without full controls and9239/1674 with them. Missingness and sample exclusions differ from the stabilization regressions.
  assumptions: [Comparable exposure-specific counterfactual trends, Consistent historical fiscal categories and geography, No dominant exposure-correlated concurrent policy, Provincial pass-through and transfer spillovers considered]
  diagnostics: [Exposure-specific pretrends, Alternative fiscal proxies, Provincial allocation chronology,2001 anticipation sensitivity, SOE/industry composition and concurrent rural fiscal reform]
threats:
- type: proxy-and-pass-through
  basis: reported
  condition: Corporate revenue includes SOE profits and excludes personal tax. The authors lack detailed province-to-county sharing schedules; inherited fiscal structure is not randomly assigned.
  evidence_refs: [E1, E2]
  possible_diagnostics: [Fiscal-account concordance, Province-specific sharing documents, Predetermined industrial composition, Realized own-revenue and transfer changes]
- type: national-concurrent-change
  basis: documented
  condition: The sharing package also changes new-enterprise collection responsibility and prohibits unauthorized tax concessions. Together with2001 anticipation and concurrent rural fiscal reforms, these can affect outcomes outside a pure transfer-dependence channel.
  evidence_refs: [E1, E2]
  possible_diagnostics: [Outcome-specific institutional chronology, Alternative transition windows, Separate collection and fiscal-allocation mechanisms]
- type: stabilization-iv-and-window
  basis: reported
  condition: The volatility application additionally instruments government size with spatially weighted imputed spending. Neighboring fiscal demand can directly affect local volatility; lack of reverse causality does not establish exclusion. Three-year centered outcomes overlap across years and cross the reform boundary.
  evidence_refs: [E2]
  possible_diagnostics: [Weak-IV-robust inference, Spatial spillover sensitivity, Exact denominator and interaction-instrument reconstruction, Nonoverlapping or alternative outcome windows]
empirical_requirements:
  contract_version: 1
  population: Historically stable counties and county-level cities with comparable fiscal series
  observation_unit: county-year
  geography_level: county
  time_start: 1994
  time_end: 2007
  minimum_frequency: annual
  minimum_pre_periods: 4
  minimum_post_periods: 4
  required_fields: [Corporate revenue1994-1997 including original SOE-profit category, Annual fiscal expenditure, Annual own revenue, Year, Province/prefecture membership, Historical boundary changes, County and provincial controls for the reported controlled specification]
  required_identifiers: [county_id, prefecture_id, province_id, year]
  treatment_key: [county_id, year]
  treatment_source: National sharing document and paper Section5.1.1's fixed fiscal dependence construction
  measurement_risks: [Combined historical tax/profit accounts, Fraction versus percent scaling, Mean ratios versus ratio of sums, Local pass-through, Historical county exclusions]
design_profiles:
- id: county-output-volatility
  label: Fiscal dependence and government-size stabilization
  design_families: [Continuous-exposure DID-IV]
  when_to_use: For the published stabilization question only after reconstructing the government-size IV and instruments for its interaction; the baseline fiscal-imbalance contrast does not require this additional IV.
  outcome_domains: [Regional economic volatility]
  requirements:
    population: Stable sample counties and county-level cities, excluding urban districts/Tibet/direct-controlled municipalities
    observation_unit: county-year with centered growth windows
    geography_level: county
    time_start: 1994
    time_end: 2007
    minimum_frequency: annual
    minimum_pre_periods: 4
    minimum_post_periods: 4
    required_fields: [Fixed1994-1997 fiscal dependence, Annual real GDP and population with adjacent-year coverage, Annual fiscal expenditure,1997 county expenditure, Annual and1997 province-wide government expenditure, County centroids and pairwise distance, County/prefecture/province crosswalk, Openness/urbanization/specialization/inflation-volatility controls]
    required_identifiers: [county_id, prefecture_id, province_id, year]
    treatment_key: [county_id, year]
evidence:
- id: E1
  source_type: policy-document
  citation: State Council, 国务院关于印发所得税收入分享改革方案的通知, 国发〔2001〕37号,2001-12-31
  url: https://www.mof.gov.cn/gkml/caizhengwengao/caizhengbuwengao2002/caizhengbuwengao20024/200805/t20080519_21080.htm
  date: '2001-12-31'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, identity.assignment_mechanism, timeline.announcement, timeline.effective, timeline.implementation_start, timeline.local_timing, assignment.rule, assignment.exemptions, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: MOF gazette reproduction re-read2026-10-07 in full, attachmentIII(1-4),IV,V(1-4),VI. Verifies national sharing, scope/base protection and subprovincial adjustment, not random county dependence or a uniform county retention schedule. Portal2008 upload date is not the legal onset.
- id: E2
  source_type: paper
  citation: 'Jia, Junxue, Rong Li, Chang Liu and Jing Ning.2024. Local information and the stabilization role of local government: Evidence from a natural experiment in China. Journal of Regional Science64(4):1265-1286. DOI10.1111/jors.12700; firstonline2024-03-27.'
  url: https://doi.org/10.1111/jors.12700
  date: 2024
  supports: [assignment.unit, assignment.treated, assignment.comparison_pool, assignment.intensity, assignment.compliance, assignment.exposure_construction, assignment.required_identifiers, design.primary_strategy, design.identifying_variation, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, design.diagnostics, empirical_requirements.population, empirical_requirements.time_start, empirical_requirements.time_end, empirical_requirements.required_fields, empirical_requirements.treatment_source, empirical_requirements.measurement_risks, design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year, design_applications.population, design_applications.outcome, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design, threats.condition]
  verification_status: reported
  access_level: full-text
  locator: Publisher https://onlinelibrary.wiley.com/doi/full/10.1111/jors.12700 inspected2026-10-07, Sections2-3,4.1-4.2,5.1.1-5.2.2, Tables6-9 and endnotes8/11-16. Section5.1.1 independently read in full. Supporting appendix and author-request data/code not inspected; no executable replication claimed.
design_applications:
- paper: 'Local information and the stabilization role of local government: Evidence from a natural experiment in China'
  doi: 10.1111/jors.12700
  journal: Journal of Regional Science
  year: 2024
  research_question: Does revenue-sharing exposure weaken the economic stabilization associated with local government size?
  population: County panel1997-2007 with1994-1997 exposure inputs; Table7 full-control sample9244 observations/1671 counties
  outcome: Log standard deviation of real per-capita GDP growth over centered t-1 through t+1, with supplementary county VFI response
  data_used: [Prefecture City and County Public Finance Statistical Yearbook, Provincial statistical yearbooks, County GIS centroids]
  treatment_encoding: Fixed mean1994-1997 corporate-revenue/expenditure ratio times post2002; stabilization specification additionally interacts this exposure with government spending/GDP
  comparison: Higher versus lower inherited fiscal dependence, within county/year-effects design
  empirical_design: Table6 continuous-exposure FE-OLS; Equation2/Table7 DID-IV for government size and its stabilization interaction, with prefecture clusters
  assumptions: [Exposure-specific trends, Correct IV reconstruction and exclusion, Comparable fiscal categories, Centered outcome windows handled explicitly]
  threats_addressed: [Alternative volatility windows, Event diagnostics, Provincial-capital distance heterogeneity and economic-center placebo]
  evidence_refs: [E1, E2]
method_transfer: null
readiness_blockers:
- Conditional use requires historical category/geography reconstruction and consideration of provincial pass-through; predetermined dependence is not inherently exogenous.
- Stabilization use additionally needs the unpublished exact interaction-instrument specification. Section4.2's IV denominator prose says GDP per capita, whereas government size uses spending/GDP; resolve scaling from appendix/code before replication. Do not silently invent an instrument set.
- Supporting appendix and request-only data were not inspected; author claims of local information are proxy interpretations, not directly observed information flows.
---

## Institutional Background

The2002 reform replaces affiliation-based allocation with revenue sharing,
protects a2001 base and leaves provinces to adjust lower-level arrangements
[E1]. This is a fiscal-resource change, not a statutory company tax-rate cut.
It follows, rather than duplicates, the existing short-lived2001 base incentive.

## What Changed

Covered revenue moves into central-local sharing from January2002. Base returns
and transfers mean county fiscal effects are not simply half of all income
taxes. The legal framework supports heterogeneous exposure, but the paper's
dependence measure is an empirical proxy [E1; E2, reported claim].

## Implementation and Assignment

Compute the average of annual corporate-revenue/expenditure ratios from
1994 through1997, then interact it with post2002. Corporate revenue contains
SOE remitted profits as well as corporate tax. Do not relabel it as all income
taxes, normalize by revenue, or use2001 as its baseline [E2, reported claim].

## Why This Creates Empirical Variation

All counties encounter the reform; their inherited fiscal structures differ.
The contrast needs exposure-specific counterfactual trends. Provincial fiscal
discretion and correlated industrial structure remain substantive conditions
[E1; E2, reported claim; analytical inference].

## Identification Risks

The fiscal-imbalance response and the government-size stabilization question
are different applications of the same reform. The latter adds a spatially
weighted instrument: other counties'1997 expenditure is grown by their
province's aggregate expenditure ratio, divided by a GDP measure and averaged
with normalized inverse-squared distances, excluding the focal county
[E2, reported claim]. Spillovers can violate exclusion even if reverse
causality from one small county is unlikely [analytical inference].

Centered volatility crosses policy years. The event diagnostic excludes2001
and2002, uses2000 as a reference and reports a1999 lead; it is not a long
pretrend certificate. Table8 first-stage statistics near7 warrant weak-IV
attention despite Table7 values near19. Distance to the provincial capital
is a heterogeneity proxy, not a separately assigned shock [E2, reported claim].

## Data Requirements

Retain original fiscal-account definitions and historical county keys. The
default VFI contract does not demand the cross-county IV inputs; the volatility
profile does. Table7 has fewer observations than the raw panel, so joining
without sample and window checks does not reproduce its estimand. Data asset
access and reconstruction belong in Econ Data Know-How, linked by DOI.

## Evidence Notes

This task recovers candidate-ca0a107d2ee3's body-access gap without erasing its
blocked history. Original national policy grounds the institution; the paper
grounds the reported exposure and applications. Precise subprovincial schedules,
supporting appendix and executable instruments remain outside the inspection.
