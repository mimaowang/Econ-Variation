---
schema_version: 2
id: china-golden-tax-iii-jurisdiction-rollout
name: China Golden Tax III First Core-System Deployment by Tax Jurisdiction
aliases:
- 金税三期分税收辖区上线
- Golden Tax Project III firm-location exposure
status: grounded
provenance:
  task_id: task-29da473f69b0
scope:
  country: China
  regions: [Mainland provincial and independently administered municipal tax jurisdictions]
  domains: [firms, public-finance, taxation, governance, digital, industry, regional-economics]
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: Chinese firms inherit exposure to a new integrated tax-administration platform through the jurisdiction administering them; a published mainland listed-firm study encodes its staggered deployment.
identity:
  instrument: First deployment of the Golden Tax III core tax-administration system across tax jurisdictions, including initial pilots and subsequent optimized-version rollout.
  authority: State Administration of Taxation, with provincial and independently administered municipal State and Local Tax Bureaux implementing deployment.
  legal_identifiers: [Guangdong joint tax-bureau announcement2014 No19, Shanghai joint tax-bureau announcement2016 No8, Zhejiang LTB and PBC Hangzhou announcement2016 No15, Guangdong STB letter2015 No9]
  implementation_regime: Replacement of local core tax-administration applications with a standardized integrated platform. Original pilot and optimized versions differ; this case records first core-system exposure, not subsequent upgrades, the earlier Golden Tax II invoice regime or the2018 bureau merger.
  assignment_mechanism: Centrally organized, staggered jurisdiction deployment changes firms' administrative exposure according to their tax location. Timing is not randomized and a company address is only a proxy for the jurisdiction administering all its establishments.
  parent: null
  related_variations: [china-golden-tax-phase2-terrain-enforcement]
timeline:
  announcement: null
  effective: null
  implementation_start: 2013
  implementation_end: 2016
  local_timing: The published roster reports first launches from February2013 to October2016; annual exposure starts in the launch year for January-June and the next year for July-December. Verified notices specify Guangdong January8,2015 and Shanghai July8,2016; Guangxi reports actual external service September8,2015 rather than its planned September1. These checks do not independently verify every roster row.
  anticipation: Deployment announcements, staff training and dual-track trials precede formal external use; firms can adjust before the annual treatment year.
  last_verified: '2026-10-04'
assignment:
  unit: Tax jurisdiction and deployment cohort; listed firms inherit the paper's region-level exposure.
  treated: Firms located in a jurisdiction with the core system deployed; the published annual TD becomes1 permanently from the paper-defined annual start.
  comparison_pool: Firms in other launch cohorts before their annual exposure begins. The published interaction also contrasts low-tax-burden or high-related-party-transaction firms with their respective reference groups; those groups are not legally untreated firms.
  rule: Attach a jurisdiction's first formal deployment month to firm location, respecting independent-city boundaries. For the published annual application set g to launch year if month<=6, otherwise year+1, and TD_it=1(year>=g). Separately code Qingdao and Shenzhen rather than inherit Shandong and Guangdong dates.
  intensity: Binary administrative availability, not an observed inspection, actual enforcement dose, tax rate or proof of tax evasion. Pre-deployment firm tax characteristics are effect modifiers.
  exemptions:
  - Qingdao is excluded from the paper's Shandong2013 row and enters its separate July2016 row.
  - Shenzhen is excluded from the Guangdong January2015 row and enters separately in October2016.
  - Dalian, Xiamen and Ningbo are also independent rollout jurisdictions in official planning; their exact dates cannot be inferred from a province-only table.
  compliance: Formal system availability does not establish identical enforcement across firms, successful data matching, or uniform use of every module. Separate administrative availability from realized scrutiny and tax outcomes.
  exposure_construction: Use the reported roster below as an attributed application table, retain raw launch month and derived annual g, and join historical firm province/city identifiers. Verify administering jurisdiction and address changes for a new panel; distinguish head office from subsidiaries and operating establishments. Do not recode later pilot-version upgrades as first exposure.
  required_identifiers: [firm_id, year, province_id, city_id, tax_jurisdiction_id, formal_launch_year_month]
  spillovers: Group-company links, interjurisdiction transactions and shared information can transmit enforcement effects beyond the head-office jurisdiction; national invoice-system changes can reach nominally not-yet-treated firms.
research_compatibility:
  outcome_domains: [corporate reporting, tax compliance, firm investment, financing, productivity]
  affected_populations: [Mainland taxpayers, Mainland A-share nonfinancial firms in the published application]
  mechanism_channels: [information integration, tax-risk detection, standardized processing, lower filing costs]
  best_for:
  - Firm panels with historical locations, several pre-periods and supported not-yet-treated comparisons during rollout.
  - Conditional reduced-form studies of integrated tax administration, distinguishing reporting responses from real behavior.
  not_good_for:
  - A post2017 panel lacking pre-deployment variation or a perpetual never-treated mainland control group.
  - Calling every low-tax-burden firm an evader or an unaffected high-tax-burden firm a statutory control.
  - Identifying a pure tax-rate, inspection or bureau-merger effect from this availability indicator.
design:
  claim_type: reduced-form
  affordances: [Staggered jurisdiction deployment, Predetermined firm-characteristic interactions]
  candidate_designs: [Cohort-aware DID, Event study with supported comparisons, Differential exposure by pre-deployment firm characteristics]
  identifying_variation: The same platform becomes available in different jurisdictions at different times; the published study additionally interacts deployment with pre-deployment tax-burden and related-party-transaction classifications.
  primary_strategy: Zhu, Pan and Hu2021 equation7 includes TD and TD times GROUP, controls, firm/year/industry effects. Preserve the common deployment term and differential interaction rather than describe GROUP as a separate rollout mechanism.
  estimand: Conditional reduced-form deployment effects and differences between predetermined firm groups in the selected listed-firm population; not an effect per inspection or a causal effect of tax noncompliance itself.
  treatment_variable: Annual absorbing TD constructed using the January-June versus July-December convention; GROUP uses pre-deployment tax burden below, or related-party transactions above, the region-industry mean.
  comparison_logic: Adoption timing supplies cross-cohort before/after comparisons; the interaction measures differential changes across firm groups. For a new design use explicit not-yet-treated comparisons and report support. By the final annual cohort in2017 no never-treated mainland group remains; post-adoption group contrasts need their own differential-trend assumptions.
  estimation_notes: The published2008-2018 sample has17,669 firm-year observations, excludes financial firms, negative equity, late first reports and missing variables, and winsorizes continuous fields at1/99. Tables4-7 report firm-clustered t statistics. Equation9 omits event year minus1. The exact pre-deployment averaging window and historical address treatment are not specified in the inspected passages; no code was inspected. Firm clustering alone need not capture shared jurisdiction shocks.
  assumptions:
  - Conditional cohort parallel trends and limited anticipation for the chosen outcome and comparison window.
  - Pre-deployment group classifications are fixed without post-treatment leakage and have comparable untreated trends.
  - Location identifies the relevant tax jurisdiction and system exposure consistently.
  - Concurrent tax and reporting reforms do not produce the same differential changes being attributed to deployment.
  diagnostics:
  - Inspect cohort pre-trends, comparison support and alternative launch-year conventions.
  - Freeze group construction before deployment and disclose its lookback window.
  - Check independent-city treatment, movers and group-company exposure.
  - Assess jurisdiction-level clustered inference and cohort heterogeneity.
  - Separate2015 invoice/reporting changes,2016 VAT expansion and2018 bureau merger where the study window includes them.
threats:
- type: trial-formal-and-version-timing
  basis: documented
  condition: Formal external use follows preparation or trials; original pilots and optimized-version upgrades need not be the same first-treatment event. The paper's narrative and table also use different dates for the second pilot wave.
  evidence_refs: [E1, E2, E3, E4, E6]
  possible_diagnostics: [Retain raw dated notices and paper coding separately, Compare formal-service and anticipation windows, Distinguish first adoption from upgrades]
- type: jurisdiction-and-establishment-mapping
  basis: documented
  condition: Zhejiang's notice explicitly excludes Ningbo and official planning lists all five independent cities, whereas the paper separately lists only Qingdao and Shenzhen. Headquarters assignment can mismeasure other establishments.
  evidence_refs: [E1, E5, E7]
  possible_diagnostics: [Verify independent-city dates for the selected sample, Inspect administering bureaus and historical locations, Restrict stable-location single-jurisdiction firms]
- type: concurrent-reporting-and-administration
  basis: documented
  condition: Guangdong enables a new annual income-tax return with the core system and Zhejiang simultaneously changes electronic tax payment; the platform bundles information and service changes rather than isolating scrutiny.
  evidence_refs: [E5, E6]
  possible_diagnostics: [Examine affected tax categories and filing measures, Model overlapping reform exposure, Distinguish real outcomes from measurement changes]
- type: selected-cohorts-and-finite-controls
  basis: inferred
  condition: A centrally organized rollout can still select jurisdictions on administrative capacity or growth. Nationwide adoption exhausts not-yet-treated comparisons, and conventional TWFE can mix heterogeneous cohort effects.
  evidence_refs: [E1, E7]
  possible_diagnostics: [Cohort-aware estimation and calendar support, Pre-trends and administrative-capacity checks, Restrict horizons with credible controls]
- type: subgroup-and-shared-shock-inference
  basis: inferred
  condition: Low tax burden need not be unlawful avoidance; pre-group windows, selective sample retention and jurisdiction-shared errors can change the differential estimand and uncertainty.
  evidence_refs: [E1]
  possible_diagnostics: [Alternative fixed pre-group definitions, Report exclusions and panel retention, Jurisdiction-level inference sensitivity]
empirical_requirements:
  contract_version: 1
  population: Mainland A-share nonfinancial firms for the documented application; broader taxpayers require a separately justified data and location contract.
  observation_unit: firm-year
  geography_level: firm tax jurisdiction with province and independently administered city identifiers
  time_start: 2008
  time_end: 2018
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 1
  required_fields:
  - Chosen firm outcome and historical firm location
  - Jurisdiction first formal deployment month and source status
  - Pre-deployment taxes paid, tax refunds and sales for the low-tax-burden interaction
  - Industry and predetermined grouping window; related-party transaction amounts and denominators for that alternative grouping
  - Assets, working-capital changes and lag/current/lead operating cash flow if reconstructing the paper's accrual residual
  - Production, sales and discretionary-expense fields if reconstructing real earnings management
  required_identifiers: [firm_id, province_id, city_id, tax_jurisdiction_id, industry_id, year]
  treatment_key: [tax_jurisdiction_id, year]
  treatment_source: Published Table1 monthly roster and section4 annual conversion, with selected original tax-bureau notices verifying formal-service dates and jurisdiction limits.
  measurement_risks:
  - CSMAR access and accounting definitions must be obtained lawfully; no restricted observations are redistributed here.
  - The record does not supply a fully independently verified nationwide monthly deployment dataset.
  - New samples need historical location and administering-jurisdiction reconciliation, especially independent cities and multiregion groups.
  - GROUP lookback and missing-value treatment need an explicit pre-deployment rule; low tax burden is not proof of evasion.
  - Two pre-periods are only a matching minimum, not sufficient evidence of parallel trends.
evidence:
- id: E1
  source_type: paper
  citation: 'Zhu Kai, Pan Shuxin and Hu Mengmeng.2021. 智能化监管与企业盈余管理选择——基于金税三期的自然实验. Journal of Finance and Economics47(10):140-155. DOI10.16538/j.cnki.jfe.20210716.101.'
  url: https://qks.sufe.edu.cn/J/PDFFull/2b8bf226-3125-4910-91be-c555e6a170f0.pdf
  date: 2021
  supports: [identity.instrument, identity.assignment_mechanism, timeline.local_timing, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.exposure_construction, design.primary_strategy, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.required_fields, empirical_requirements.treatment_source, design_applications.treatment_encoding, design_applications.data_used]
  verification_status: verified
  access_level: full-text
  locator: 'Publisher final16-page PDF: first-page publication/DOI; Table1 printed142; section4 printed145-146 including equation7, TD and GROUP; Tables4-7 printed147-149. Table1 and equation7/TD page visually inspected. Source reports its national roster; independent verification is limited to the notices below. No replication code inspected.'
- id: E2
  source_type: implementation-document
  citation: 'Shanghai tax agency.2016-04-25. 金税三期工程介绍, sections1-2.'
  url: https://shanghai.chinatax.gov.cn/hktax/tzgg/qtgg/201604/t423764.html
  date: 2016
  supports: [identity.instrument, identity.authority, identity.implementation_regime, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: 'Sections1-2 distinguish VAT-focused Golden Tax II from the broader integrated core system and national/provincial processing; July2016 is a Shanghai plan here, not actual-use evidence.'
- id: E3
  source_type: policy-document
  citation: 'Guangdong State and Local Tax Bureaux.2014-12-24. Joint announcement2014 No19 on optimized core-system launch and switching.'
  url: https://guangdong.chinatax.gov.cn/gdsw/ssfggds/2014-12/24/content_a5870d4579fb41faad4e53a6f917f9ff.shtml
  date: 2014
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, timeline.local_timing, assignment.rule]
  verification_status: verified
  access_level: official-document
  locator: 'Opening and item2: respective provincial bureau systems switch to formal service January8,2015 at08:30. Archived notice was repealed in2018; historical date remains its subject. Does not itself establish Shenzhen timing.'
- id: E4
  source_type: policy-document
  citation: 'Shanghai State and Local Tax Bureaux.2016-06-01. Joint announcement2016 No8, 关于金税三期系统上线有关事项的公告.'
  url: https://shanghai.chinatax.gov.cn/xhtax/tzgg/tzl/201606/t424746.html
  date: 2016
  supports: [timeline.local_timing, assignment.rule, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: 'Opening and items1-2: July2016 formal deployment, June28-July7 switching and July8 at08:30 restoration of external services; this is not the earlier dual-track trial.'
- id: E5
  source_type: policy-document
  citation: 'Zhejiang Local Tax Bureau and PBC Hangzhou.2016-09-13. Joint announcement2016 No15 on electronic tax payment.'
  url: https://zhejiang.chinatax.gov.cn/art/2016/9/13/art_8410_12294.html
  date: 2016
  supports: [identity.legal_identifiers, timeline.local_timing, assignment.rule, assignment.exemptions]
  verification_status: verified
  access_level: official-document
  locator: 'Main paragraph explicitly excludes Ningbo and sets October8,2016 core-system and electronic-payment rollout. It does not establish Ningbo launch.'
- id: E6
  source_type: policy-document
  citation: 'Guangdong State Tax Bureau.2015-01-05. 粤国税函〔2015〕9号, forwarding the revised annual corporate income-tax return notice.'
  url: https://guangdong.chinatax.gov.cn/gdsw/ssfggds/201501/d5c4b371ce1c42f59a9ecbe0dffed54b.shtml
  date: 2015
  supports: [timeline.local_timing, identity.implementation_regime]
  verification_status: verified
  access_level: official-document
  locator: 'Provincial item4: January8,2015 single-track core system and new return formally enabled together; national forwarded item4 distinguishes existing CTAIS/Golden Tax users and national software upgrades.'
- id: E7
  source_type: policy-document
  citation: 'MOF, SAT and PBC.2016-04-07. 财库〔2016〕66号,2016 tax-treasury-bank electronic network work notice; MOFCOM-hosted legal-text republication.'
  url: https://policy.mofcom.gov.cn/claw/clawContent.shtml?id=51235
  date: 2016
  supports: [identity.authority, identity.implementation_regime, assignment.exemptions]
  verification_status: reported
  access_level: official-document
  locator: 'Item2(6) lists Dalian, Qingdao, Xiamen, Ningbo and Shenzhen separately among planned2016 launches. Source credit is a legal-text provider, not the issuing copy; original MOF endpoint could not be opened. Plan is not proof of individual actual dates.'
- id: E8
  source_type: implementation-document
  citation: 'Guangxi State Tax Bureau.2015-09-14. 广西金税三期优化版正式上线启动, official CAC republication.'
  url: https://www.cac.gov.cn/2015-09/14/c_1116553396.htm
  date: 2015
  supports: [timeline.local_timing, assignment.rule, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: 'Opening, preparation paragraph and actual-service paragraph: September1 planned single-track launch, July-August dual entry while old system handles external business, September8 actual external use throughout14 prefectures.'
- id: E9
  source_type: paper
  citation: 'China DOI resolution metadata for Zhu, Pan and Hu, 智能化监管与企业盈余管理选择——基于金税三期的自然实验.'
  url: https://doi.org/10.16538/j.cnki.jfe.20210716.101
  date: 2021
  supports: [design_applications.paper]
  verification_status: verified
  access_level: metadata
  locator: 'DOI resolver title, three authors and DOI; October12,2021 registration. Methods and journal pagination come from the final publisher PDF, not this metadata page.'
design_applications:
- paper: 'Intelligent Supervision and Earnings Management Choice: A Natural Experiment Based on Golden Tax-III'
  doi: 10.16538/j.cnki.jfe.20210716.101
  journal: Journal of Finance and Economics
  year: 2021
  research_question: Whether integrated tax administration changes the choice between accrual and real earnings management, differentially by pre-deployment tax characteristics.
  population: Mainland A-share firms retained in the2008-2018 nonfinancial sample;17,669 firm-year observations.
  outcome: Accrual residual and real earnings-management measures; tax burden in mechanism checks.
  data_used: [CSMAR accounting and firm characteristics, Annual reports for ultimate controller, Jurisdiction deployment roster]
  treatment_encoding: TD follows launch region and the half-year annual conversion; Qingdao and Shenzhen separately coded. GROUP is a fixed pre-deployment below-mean tax-burden or above-mean related-party-transaction classification at region-industry level, with exact lookback unresolved.
  comparison: Deployment cohorts and interaction differences relative to each tax-characteristic reference group, not a permanent non-treated sector.
  empirical_design: TD and TD times GROUP with firm/year/industry effects; firm-clustered inference and dynamic interaction event-time checks.
  assumptions: [Cohort and group parallel trends, Predetermined classification, No confounded deployment or measurement changes]
  threats_addressed: [Dynamic pre-period interaction checks, Alternative accrual measures, Alternative tax-burden and related-party definitions]
  evidence_refs: [E1, E9]
method_transfer: null
readiness_blockers:
- Verify the new panel's historical tax-jurisdiction and independent-city dates before applying the reported roster; monthly or quarterly work requires more date resolution than the annual application.
- Set and disclose the pre-deployment GROUP lookback if using the interaction; the paper passages do not establish its exact code.
- Establish outcome-specific cohort comparisons, overlapping-reform treatment and shared-jurisdiction inference; formal deployment is not an exogeneity certificate.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Golden Tax II concentrated on VAT-invoice monitoring. Golden Tax III extended the core platform across taxes and administrative processes, with national/provincial data handling and more standardized information flows [E2]. This matters to firms through both scrutiny and service costs. The recorded object is first core-system deployment, not a higher statutory tax rate, an observed audit, or the later organizational merger.

## What Changed

Jurisdictions replaced their operating applications at different times. Guangdong's notice schedules formal use for January8,2015 [E3]; Shanghai's formal-service date is July8,2016 [E4]. Preparation is not exposure to a fully operational new system: Guangxi describes dual entry while the old system still served taxpayers, followed by September8,2015 external use [E8]. Original pilot and optimized versions are not assumed to supply identical enforcement doses.

## Implementation and Assignment

The application maps firm region to first launch and converts a second-half launch to the next annual treatment year [E1]. Preserve the underlying month as well as this analytical convention. The following table transcribes the published Table1, not a newly verified nationwide administrative dataset [E1, reported roster].

| Reported launch | Jurisdictions in published Table1 | Annual TD starts |
|---|---|---|
|2013-02|Chongqing|2013|
|2013-10|Shandong excluding Qingdao; Shanxi|2014|
|2015-01|Guangdong excluding Shenzhen; Henan; Inner Mongolia|2015|
|2015-07|Ningxia|2016|
|2015-09|Hebei; Tibet; Guizhou; Guangxi; Yunnan|2016|
|2015-10|Hunan; Qinghai; Hainan; Gansu|2016|
|2016-01|Anhui; Xinjiang; Sichuan; Jilin|2016|
|2016-07|Liaoning; Jiangxi; Fujian; Shanghai; Qingdao|2017|
|2016-08|Beijing; Tianjin; Heilongjiang; Hubei; Shaanxi|2017|
|2016-10|Jiangsu; Zhejiang; Shenzhen|2017|

The table explicitly separates Qingdao and Shenzhen but has no separate Dalian, Xiamen or Ningbo rows. Zhejiang's original notice excludes Ningbo, while national planning names all five independent cities [E5,E7]. Do not infer monthly exposure for those cities from a province row. The paper says firm region, not a documented historical tax-bureau join; stable headquarters location can be a usable proxy only after checking the new sample's tax location and multiregion structure [analytical inference].

## Why This Creates Empirical Variation

Different deployment cohorts create temporal contrasts. The published specification combines TD with an interaction for pre-deployment firm characteristics, so its interaction is a differential response rather than the total deployment effect [E1]. Low-tax-burden firms are classified below the region-industry mean; high-related-party firms are classified above it. These classifications do not create another institutional assignment or certify evasion.

A new application can use supported not-yet-treated comparisons rather than inherit the paper's conventional specification. Once the final annual cohort starts in2017, all included rollout cohorts are treated. Longer outcome panels do not restore untreated comparisons; late effects or group interactions need explicit support and assumptions [analytical inference].

## Identification Risks

Pilot sequencing can reflect administrative capacity or development even when individual firms do not choose it. Firm-level clustering can understate uncertainty from common jurisdiction shocks [analytical inference]. Non-significant event leads are diagnostics, not proof of parallel trends. Guangdong couples deployment with a new corporate income-tax return, and Zhejiang couples it with electronic-payment changes [E5,E6]. Reporting outcomes can change because measurement and filing change, while real outcomes can reflect service improvements as well as enforcement.

## Data Requirements

Retain firm, province, city, administering jurisdiction and calendar identifiers alongside raw launch month and annual treatment year. The documented application uses CSMAR and manually collected controller information [E1]. Group interactions require a fixed pre-deployment lookback and region-industry reference values; do not calculate them with post-treatment observations. Accrual-residual construction needs lag and lead cash flows, so the outcome period alone does not delimit raw accounting-data coverage. Other firm outcomes do not automatically require every earnings-management field.

## Evidence Notes

The publisher PDF identifies the final2021 journal paper and its DOI. Table1 and section4 were inspected, including a visual check of the deployment table and equation7/TD definition. Its institutional narrative dates the second pilot wave to October2014, while Table1 gives January2015. The annual half-year rule yields2015 either way for that wave, but this does not make the monthly histories interchangeable. Guangdong's original formal-service notice supports January2015 [E1,E3]. Other roster dates remain attributed to the paper unless individually checked.

The CCER2023 manuscript that led to this candidate remains a working paper; its investment cash-flow construction and prose/table sign inconsistency are preserved in the source map, not imported as verified published results. Li, Wang and Wu's2020 Economic Modelling application has publication/abstract confirmation but its full methods were not recovered in this task; no coding is imputed to it. The separately inspected2021 published application supplies the traceable research use here. No source PDF, code or restricted firm observations are redistributed.
