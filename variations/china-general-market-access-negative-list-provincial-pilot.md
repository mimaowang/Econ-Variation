---
schema_version: 2
id: china-general-market-access-negative-list-provincial-pilot
name: China general market-access negative-list provincial pilot exposure
aliases: [市场准入负面清单制度试点, general market-access negative-list pilot]
status: grounded
provenance:
  task_id: task-73769b07dae2
scope:
  country: China
  regions: [Mainland China]
  domains: [firm-behavior, industrial-economics, development, regional-market-integration, market-entry]
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: Mainland firms receive location-based exposure to the 2016 and 2017 provincial general market-access pilots. A published Chinese economics-journal paper actually uses this exposure to study firm capacity overhang. This is not an overseas shock or a foreign-investor-only list.
identity:
  instrument: Provincial piloting of the general market-access negative-list draft before nationwide implementation in late December 2018.
  authority: State Council approval; NDRC and Ministry of Commerce coordination; provincial governments propose and implement approved plans.
  legal_identifiers: [国发〔2015〕55号, 发改经体〔2016〕442号, 发改经体〔2018〕1892号]
  implementation_regime: A common national draft is tested in four provinces or municipalities in 2016 and eleven additional provinces or municipalities in June 2017. Provincial plans require State Council approval. Prohibited and restricted entry remain inside the list; entry outside it is open under the general framework. National implementation supersedes the pilot-versus-nonpilot boundary in late 2018.
  assignment_mechanism: Administratively selected provincial cohorts, with firms inheriting pilot exposure through registered province in the inspected application. No random selection, threshold or lottery is established; individual firms' actual relief depends on their activities and pre-existing restrictions.
  parent: null
  related_variations: []
timeline:
  announcement: Framework signed 2015-10-02; pilot notice signed 2016-03-02 and posted 2016-04-11.
  effective: The 2016 draft takes effect upon State Council approval of a province's pilot plan, not automatically on its national website posting date.
  implementation_start: 2016
  implementation_end: 2018
  local_timing: NDRC's 2017-08-31 contemporaneous reply verifies the initial four started in 2016 and the eleven additions joined in June 2017. Exact provincial approval days are not inspected. The 2021 firm application assigns annual exposure from 2016 and 2017, respectively, through its 2018 endpoint. The national notice is signed 2018-12-21 and posted 2018-12-28; this endpoint is a regime transition, not abolition of negative lists.
  anticipation: The October 2015 framework and provincial preparation can change expectations before the annual pilot indicator turns on; some prior local entry reforms may already operate.
  last_verified: '2026-10-05'
assignment:
  unit: Province-level pilot assignment; firm-year registered-province exposure in the published application.
  treated: Firms registered in Tianjin, Shanghai, Fujian or Guangdong from 2016; firms registered in Liaoning, Jilin, Heilongjiang, Zhejiang, Henan, Hubei, Hunan, Chongqing, Sichuan, Guizhou or Shaanxi from 2017.
  comparison_pool: Firms in other mainland provinces and pre-pilot years, subject to comparable trends and overlapping reform checks. Later cohorts are not-yet-treated before entry. Already-treated firms in the published TWFE are not automatically valid controls. Nonpilot provinces are not permanently unexposed after the late-2018 nationwide transition.
  rule: Set Open_it to one when registered province is in the first cohort and year is at least 2016, or in the second cohort and year is at least 2017, otherwise zero, for the published 2014–2018 pilot-exposure application. This annual intention-to-treat proxy is explicitly reported by the 2021 paper, not a verified measure of each firm's industry-specific deregulation or a daily effective-date series.
  intensity: Binary exposure to the provincial institutional package; neither the number of removed restrictions nor individual compliance intensity is measured by this indicator.
  exemptions: [Foreign-investment and free-trade-zone negative lists are separate instruments, General business registration simplification is not identical to this pilot, List inclusion can retain prohibition or permission requirements rather than deregulate every activity]
  compliance: Approved provincial implementation and firm location establish program exposure, not uniform administrative compliance or an actual newly available investment opportunity for every firm.
  exposure_construction: Build the two-cohort province table below, join historical registered province to firm_id and year, and preserve relocation conventions. Distinguish registered from operating location. For annual outcomes evaluate exclusion of 2018, transition-year coding or a clearly explained late-year exposure convention; do not extend an untreated nonpilot comparison into 2019. A new monthly design needs original provincial approval dates and cannot reuse these annual onsets as exact days.
  required_identifiers: [firm_id, year, registered_province_id, operating_province_id for location sensitivity, industry_code]
  spillovers: Entry, competition, supplier links and investment can cross provincial borders; a firm in a nonpilot province can be affected through treated partners or markets.
research_compatibility:
  outcome_domains: [firm capacity overhang, firm investment, diversification, market entry, productivity]
  affected_populations: [mainland listed nonfinancial firms, firms operating in selected provinces]
  mechanism_channels: [entry transparency and approval constraints, competition, resource allocation, investment opportunities]
  best_for: [Firm outcome panels with historical provincial geography and pre/post pilot years, Reduced-form evaluation of a regional market-access governance package]
  not_good_for: [An isolated industry-specific deregulation effect without before/after restriction mapping, Foreign-investment-only treatment or a free-trade-zone designation effect, A permanent pilot/nonpilot contrast after nationwide implementation]
design:
  claim_type: reduced-form
  affordances: [two provincial pilot cohorts, public cohort roster, registered-firm exposure before national rollout]
  candidate_designs: [cohort-specific DID, event study, published firm-and-year-FE DID]
  identifying_variation: Differences in pilot onset across provinces interacted with firms' registered locations and before/after outcome changes.
  primary_strategy: The inspected 2021 application regresses capacity overhang on Open and controls with firm and year fixed effects and firm-clustered errors. New work should use cohort-appropriate comparisons and inference at the province assignment level rather than treating firms as independent policy assignments.
  estimand: Conditional reduced-form effect of exposure to a provincial entry-governance pilot on sampled firms' outcomes; not a treatment-on-the-treated effect of a particular restriction removal.
  treatment_variable: Open_it is the registered-province annual pilot indicator with first-cohort onset 2016 and second-cohort onset 2017, retained through 2018 in the published application.
  comparison_logic: Compare outcome changes for sampled firms in pilot provinces with comparable firms in provinces not yet piloting during the relevant window. Selection, national transition and concurrent reforms limit this interpretation.
  estimation_notes: The published baseline retains 11,872 firm-years in 2014–2018 from CSMAR and Wind, excluding financial, B-share, ST and missing-data observations and winsorizing continuous variables at 1/99 percent. Its three capacity-overhang proxies use stochastic-frontier estimation with installed capital measured as fixed plus intangible assets, fixed assets, or total assets. Optimal capacity depends on sales, operating and nonoperating costs, volatility, systematic risk and the risk-free rate, with industry effects and nonnegative overhang. Exact frontier specification, distributions and implementation code were not inspected; these proxies are not directly observed physical utilization. The event-study sample starts in 2010 and contains 17,396 observations, unlike the baseline.
  assumptions: [Conditional parallel outcome trends absent the pilot, No unhandled anticipation or province-specific coincident reforms, Valid historical location exposure and comparable sample retention, Cross-province interference addressed or bounded, Appropriate outcome construction and province-level inference]
  diagnostics: [Cohort-specific leads and pre-policy trends, Omit 2018 and compare explicit transition conventions, Province-level inference with small-cluster sensitivity, Registered versus operating and fixed pre-policy location checks, Audit overlapping FTZ and supply-side reforms, Separate actual restriction changes from general pilot exposure]
threats:
  - type: administrative pilot selection
    basis: reported
    condition: The paper acknowledges uncertain selection criteria and possible omitted factors; added covariates and reassigned-placebo results do not establish random selection.
    evidence_refs: [E1, E2]
    possible_diagnostics: [pre-policy province trends, cohort-specific comparisons, overlapping-reform dates]
  - type: exposure is not actual deregulation
    basis: reported
    condition: The paper explicitly cannot identify which industries or firms experienced a before/after restriction change; a provincial dummy therefore represents a policy-environment exposure.
    evidence_refs: [E1]
    possible_diagnostics: [activity-specific restriction mapping if claiming actual deregulation, intention-to-treat labeling, entry versus incumbent outcomes]
  - type: late-2018 nationwide transition
    basis: documented
    condition: The signed national notice applies to all provinces in late December 2018 while the published pilot indicator remains cohort-specific through 2018.
    evidence_refs: [E1, E4]
    possible_diagnostics: [exclude 2018, monthly outcome sensitivity where dates are recovered, do not retain nonpilot controls after national rollout]
  - type: firm clustering versus province assignment
    basis: reported
    condition: The baseline clusters by firm although assignment is provincial; the text reports other clustering checks, but their tables are available on request and no standalone province clustering is established by those reports.
    evidence_refs: [E1]
    possible_diagnostics: [province clustering, wild-cluster or suitable small-sample inference, assignment-level effective sample size]
  - type: capacity measurement and geographic sorting
    basis: reported
    condition: Model-based overhang depends on the installed-capital proxy and frontier assumptions; registered and operating locations can differ. Total assets can include assets unused in production.
    evidence_refs: [E1]
    possible_diagnostics: [recover frontier implementation before reproducing published outcomes, compare independently constructed outcome measures, location histories and operating-location checks]
  - type: market spillovers and policy bundles
    basis: inferred
    condition: Regional competition and investment can affect nonpilot firms, while contemporaneous FTZ and supply-side reforms can covary with pilot assignment.
    evidence_refs: [E2, E3]
    possible_diagnostics: [partner and neighbor exposure, concurrent-policy controls and restricted windows]
empirical_requirements:
  contract_version: 1
  population: Mainland nonfinancial listed firms for the inspected application; other firm populations require their own coverage and selection assessment.
  observation_unit: firm-year
  geography_level: Historical registered province or directly administered municipality.
  time_start: 2014
  time_end: 2018
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields: [historical registered province, cohort onset year, firm capacity-overhang outcome or inputs and documented construction, fixed assets and intangible assets and total assets for published proxy alternatives, sales and operating/nonoperating costs and volatility and systematic risk and risk-free rate for frontier reconstruction, firm listing/industry/ST status, firm size leverage profitability age ownership analyst attention largest-shareholder share and productivity for published controls, provincial marketization control]
  required_identifiers: [firm_id, year, registered_province_id, industry_code]
  treatment_key: [registered_province_id, year]
  treatment_source: Official 2016 notice and contemporaneous NDRC 2017 reply establish the two cohorts; the 2021 paper supplies the annual registered-firm coding convention.
  measurement_risks: [registered versus operating locations, year-end national transition, actual industry restrictions versus program exposure, model-dependent capacity measures, post-reform location changes, province-level assignment with many firm observations]
evidence:
  - id: E1
    source_type: paper
    citation: '张韩、王雄元、张琳琅 (2021). 市场准入管制放松与供给侧去产能——基于负面清单制度试点的准自然实验. 财经研究 47(7):93–107.'
    url: https://doi.org/10.16538/j.cnki.jfe.20210416.403
    date: '2021-07-03'
    supports: [assignment.rule, assignment.treated, design.primary_strategy, design.treatment_variable, design.estimation_notes, empirical_requirements.required_fields, design_applications.treatment_encoding, design_applications.data_used]
    verification_status: reported
    access_level: full-text
    locator: 'Publisher full HTML https://qks.sufe.edu.cn/mv_html/j00001/202107/a17542be-e520-46c2-a756-c00d96823898_WEB.htm: Section III sample, variables and equation1; Section IV(1), Tables3–4; IV(2) exposure-identification discussion, selection and other robustness subsections; footnotes2–3. These passages were read, not inferred from the abstract. Auxiliary robustness tables and frontier code were not inspected.'
  - id: E2
    source_type: policy-document
    citation: State Council general market-access negative-list framework, 国发〔2015〕55号, signed 2015-10-02.
    url: https://www.mof.gov.cn/zhengwuxinxi/zhengcefabu/201510/t20151019_1510192.htm
    date: '2015-10-02'
    supports: [identity.instrument, identity.authority, identity.assignment_mechanism, identity.implementation_regime, timeline.anticipation, assignment.exemptions]
    verification_status: verified
    access_level: official-document
    locator: Paragraphs1,6,8,10–11; national pilot-selection/approval process and general-versus-foreign-investor list distinction. Planned 2015–2017 window is not observed provincial onset.
  - id: E3
    source_type: policy-document
    citation: NDRC and Ministry of Commerce pilot draft notice, 发改经体〔2016〕442号, signed 2016-03-02.
    url: https://www.ndrc.gov.cn/xxgk/zcfb/tz/201604/t20160411_963018.html
    date: '2016-03-02'
    supports: [identity.instrument, identity.legal_identifiers, identity.implementation_regime, assignment.treated, assignment.rule, timeline.effective]
    verification_status: verified
    access_level: official-document
    locator: Opening and paragraphs1–7, especially first four provinces, provincial proposals/State Council approval and effect from approval. Notice read; linked list attachment not independently inspected.
  - id: E4
    source_type: policy-document
    citation: NDRC and Ministry of Commerce nationwide notice, 发改经体〔2018〕1892号, signed 2018-12-21.
    url: https://www.ndrc.gov.cn/xxgk/zcfb/tz/201812/t20181228_962356_ext.html
    date: '2018-12-21'
    supports: [timeline.implementation_end, identity.implementation_regime, assignment.comparison_pool]
    verification_status: verified
    access_level: official-document
    locator: Addressees, opening approval paragraph, SectionII(1)–(2), signature; read full notice, not linked list attachment. Website posting is 2018-12-28.
  - id: E5
    source_type: policy-document
    citation: NDRC reply to CPPCC proposal0517, index000013039-2017-00554, dated 2017-08-31.
    url: https://zfxxgk.ndrc.gov.cn/web/iteminfo.jsp?id=15459
    date: '2017-08-31'
    supports: [timeline.implementation_start, timeline.local_timing, assignment.treated, assignment.rule, identity.implementation_regime]
    verification_status: verified
    access_level: official-document
    locator: SectionI(4) explicitly identifies first four starts in2016, June2017 eleven additions by name and15 current pilot regions. Other mixed-ownership/PPP passages do not define this variation.
design_applications:
  - paper: Deregulation of market access and de-capacity of supply side
    journal: 财经研究 / Journal of Finance and Economics
    year: 2021
    research_question: Does provincial general market-access pilot exposure reduce listed firms' model-based capacity overhang?
    population: Mainland listed nonfinancial firms after B-share/ST/missing-data exclusions.
    doi: 10.16538/j.cnki.jfe.20210416.403
    outcome: Model-based firm capacity overhang under three installed-capital proxies.
    data_used:
      - 'CSMAR and Wind listed-firm data with 2014–2018 baseline 11,872 observations'
      - Provincial marketization index
      - Frontier-estimated capacity outcomes
      - 'Event-study sample extended to2010 with 17,396 observations'
    treatment_encoding: Registered first-cohort province from2016 or second-cohort province from2017, otherwise zero; absorbing annual pilot exposure through2018.
    comparison: Other sampled firms and pre-pilot observations with firm/year effects; later national implementation requires an explicit transition sensitivity.
    empirical_design: Multi-period TWFE DID with baseline firm clustering; event leads/lags and extra diagnostics reported in the inspected passages.
    assumptions: [conditional parallel trends, no unhandled province-specific confounding or spillovers, valid geographic assignment, defensible frontier-based outcome measurement]
    threats_addressed: [displayed expanded-window event study, displayed diversification check, reported operating-location substitution, reported PSM and clustering alternatives with tables on request]
    evidence_refs: [E1]
method_transfer: null
readiness_blockers:
  - Conditional use concerns annual pilot intention-to-treat exposure, not exact-day implementation or verified firm-specific restriction removal; obtain provincial approval histories for finer timing and before/after activity rules for the latter estimand.
  - Audit the late-2018 national transition, selective cohorts and province-level inference for the user's outcome; the published absorbing indicator cannot supply untreated post-2018 provinces.
  - Exact replication of capacity overhang requires the frontier specification, inputs and code; the inspected article documents proxy choices and determinants but not a complete reproducible estimator. Auxiliary robustness tables are available on request, not independently verified.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

The reform organizes entry restrictions into an explicit general list rather
than treating every business activity as presumptively requiring discretionary
permission. Prohibited and restricted activities remain regulated; outside-list
entry is open. It covers domestic and foreign investors, unlike the separate
foreign-investment list [E2]. It is not a blanket abolition of approvals.

## What Changed

Provincial pilots tested a common national draft under approved local plans
[E3]. Their useful empirical contrast is earlier exposure to this governance
package, not the nationwide institution's existence. By late December2018 the
national notice applies across provinces and forbids independent local entry
lists [E4]. Extending the pilot comparison beyond that transition changes the
research question to earlier-versus-later exposure.

## Implementation and Assignment

The contemporaneous NDRC reply supplies a recoverable annual cohort roster
[E5]:

| Pilot onset | Provinces and directly administered municipalities |
|---|---|
| 2016 | 天津、上海、福建、广东 |
| June2017 | 辽宁、吉林、黑龙江、浙江、河南、湖北、湖南、重庆、四川、贵州、陕西 |

Join this province table to historical firm registration and year. The published
firm application makes the indicator absorbing within2014–2018 [E1, reported
claim]. The official roster verifies entry into the pilot, while exact operative
days depend on provincial-plan approval [E3]. Reported daily dates in the paper
have not been independently authenticated and should not drive a monthly design.

## Why This Creates Empirical Variation

Staggered provincial entry generates a before/after comparison for firms, but
administrative selection can correlate with their outcome trends. The inspected
application studies capacity overhang. Investment, entry or productivity are
possible research questions, not claims that this paper estimates those effects.
The provincial proxy captures a policy environment: the paper itself cannot
identify every firm's actual restriction change [E1, reported claim].

## Identification Risks

National rollout is not merely another year fixed effect if one continues to
label former nonpilot firms untreated. For annual2018 outcomes, specify why a
late-year national event does or does not affect measurement and compare a
window ending in2017 [E4; analytical inference]. Province-assignment inference,
preparation, relocation, overlapping FTZ/supply-side reforms and market spillovers
also need outcome-specific treatment. The paper's insignificant pre-policy leads
do not prove parallel trends; reported robustness results are not independent
validation [E1, reported claim].

## Data Requirements

A firm-year outcome panel must carry historical province, firm identifier and
industry, with adequate pre-policy years. Registered-location exposure and
operating-location exposure answer different geographic questions. Capacity
overhang is estimated, not directly read from fixed assets: exact reproduction
requires the stated frontier inputs and the missing implementation details.
Researchers with another well-measured firm outcome need not invent a capacity
proxy to use this provincial assignment [E1; analytical inference].

## Evidence Notes

This grounded record admits the annual provincial mechanism with explicit
conditions, not an exact replication certificate. The blocked2025 province-pair
market-integration application remains in the source ledger: its final price-
dispersion transformation and2018 coding have not been closed. Its unilateral
and bilateral comparisons are applications of this same mechanism, not two
additional variations. Do not offer that application as ready merely because
the institutional roster is now grounded.
