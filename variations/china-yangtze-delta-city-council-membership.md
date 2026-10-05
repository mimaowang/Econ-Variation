---
schema_version: 2
id: china-yangtze-delta-city-council-membership
name: China Yangtze River Delta city council membership and intercity cooperation exposure
aliases: [长三角城市经济协调会, 长江三角洲城市经济协调会, council membership market integration]
status: grounded
provenance:
  task_id: task-21bf3d5f9591
scope:
  country: China
  regions: [Shanghai, Jiangsu, Zhejiang, Anhui]
  domains: [regional-economics, urban-economics, development, firm-innovation, market-integration, intercity-cooperation]
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: Mainland municipalities enter a regional coordination organization at different dates; a published economics paper actually uses their membership to study intercity firm innovation partnerships.
identity:
  instrument: Membership in the Yangtze River Delta city economic coordination council.
  authority: Participating municipal governments and their mayoral coordination meetings.
  legal_identifiers: [长江三角洲城市经济协调会章程]
  implementation_regime: Voluntary municipal coordination with evolving thematic cooperation and locally dependent implementation; membership is an institutional participation proxy, not a statutory entitlement to a uniform enterprise subsidy.
  assignment_mechanism: Municipal admission to the council changes membership status. The inspected research assigns cities by reported admission cohorts and constructs exposure for pairs with both or exactly one endpoint belonging; these are two states of one membership mechanism.
  parent: null
  related_variations: []
timeline:
  announcement: The paper reports1992 departmental coordination,1997 mayoral-council formation and subsequent admissions; founding narratives differ in counts and preparatory dates.
  effective: Yancheng's municipal account directly confirms entry in March2010. Other historical cohort dates below are author-reported; membership does not date each cooperation project's operation.
  implementation_start: 1997
  implementation_end: null
  local_timing: Reported cohorts are1997 fifteen founders, August2003 Zhejiang Taizhou, March2010 six cities and April2013 eight cities. In the2000–2015 patent application, both/one membership indicators are lagged two years;1997 founders are already members before the panel starts.2018/2019 expansions are outside that application.
  anticipation: Cooperation predates formal admission; cities may prepare and coordinate while seeking membership. The two-year patent lag is a research convention, not an independently verified universal implementation delay.
  last_verified: '2026-10-05'
assignment:
  unit: Municipality membership; two-city pair-year exposure in the served application.
  treated: See the author-reported cohort table in the prose. Both endpoints belong for Both; exactly one belongs for One. Jiangsu Taizhou泰州 and Zhejiang Taizhou台州 are different cities.
  comparison_pool: Pair-years in the paper's Jiangsu-Zhejiang-Anhui-Shanghai sample with neither endpoint a member form the omitted membership state, while Both and One enter jointly. Pre-entry states contribute variation; a pair can change from neither to One to Both.
  rule: Let M_c,t =1 from the reported admission year onward. Both_ij,t = M_i,t*M_j,t; One_ij,t = M_i,t*(1-M_j,t)+(1-M_i,t)*M_j,t. Baseline uses Both_ij,t-2 and One_ij,t-2 jointly with contemporary controls, endpoint fixed effects and year effects.
  intensity: Binary institutional membership and paired membership states; not measured market integration, patent support receipt or project implementation intensity.
  exemptions: [Regional planning inclusion is not council admission, Observers are not automatically members,2018 and2019 entrants are not treated events in the2000–2015 application]
  compliance: The municipality participates in cooperation, but actual projects and enterprise take-up differ. Municipal evidence describes admission separately from future integration plans.
  exposure_construction: Build a city-year cohort lookup retaining source and reported-versus-verified status; join it independently to both city endpoints before calculating paired indicators and lagging. Join patent publication numbers and distinct co-owners to cleaned firm names and checked addresses, assign owners to historical cities, then aggregate joint grants by city pair and grant year. Do not replace co-owned grants with generic patent counts or silently freeze all annual firm locations at2008.
  required_identifiers: [city_i, city_j, year, firm_owner_id, patent_publication_number, historical_city_code]
  spillovers: Cooperation can divert partnerships from nonmembers and spill across neighboring municipalities. Different pairs sharing one city can have correlated outcomes despite pair-level clustering.
research_compatibility:
  outcome_domains: [intercity collaborative innovation, joint invention patent grants, innovation partner matching, regional market integration]
  affected_populations: [firms with matched patent co-ownership and census information in the sampled mainland cities]
  mechanism_channels: [municipal coordination, intercity information and innovation platforms, reduced cooperation barriers, partner diversion]
  best_for: [annual intercity joint-patent and partner-network outcomes with explicit endpoint membership, studying institutional cooperation rather than one subsidy]
  not_good_for: [random admission assumptions, nationwide region labels, direct firm subsidy receipt, generic patent totals without ownership pairs, treating founding as a2000 event, a ready employment application without resolving its control window]
design:
  claim_type: reduced-form
  affordances: [admissions change endpoint membership at different dates, one-member and two-member pairs distinguish partnership states]
  candidate_designs: [paired-city panel comparisons, admission-cohort event studies with interference assessment]
  identifying_variation: Changes in one or both endpoint membership, lagged two years, compared with other membership states and calendar-time variation in the reported2000–2015 city-pair panel.
  primary_strategy: Li-Cheng-Wu2022 jointly estimate Both and One with city-endpoint and year fixed effects; endpoint-by-year effects and negative-binomial alternatives are separately reported. Standard errors cluster by city pair.
  estimand: Conditional association interpreted by the paper as creation/diversion of intercity collaborative innovation following membership. A new causal interpretation requires an outcome-specific counterfactual, interference treatment and admission-selection assessment.
  treatment_variable: Both_ij,t-2 and One_ij,t-2, not a single city-level dummy nor two different policies.
  comparison_logic: Recover changes across membership states without assuming One is untreated. Baseline endpoint effects are not pair fixed effects; do not silently describe the published model as a conventional pair-FE DID.
  estimation_notes: Main outcomes are log(1+joint grants), log(1+active firm partnerships) and log(1+average grants per active partnership). Table3 reports23,698 observations. City controls include road passengers and airports; pair controls combine GDP per capita, population, education spending, FDI and fixed investment, with patent scale and direct high-speed-rail links. Patent-scale prose says grants whereas Table2 says applications; exact reproduction requires clarification. The intensive-margin zero/no-partnership convention and pairs with more than two patent owners require author-code clarification, not invented rules.
  assumptions: [credible counterfactual trends conditional on the chosen specification, no unhandled anticipation or concurrent regional policies, comparable patent and owner measurement, explicit spillover estimand, defensible historical city exposure]
  diagnostics: [cohort-specific leads with power assessment, founder-only sensitivity, state-transition risk sets, admission-selection covariates, shared-city or dyadic dependence sensitivity, geographic spillovers, grant-versus-application timing, matched-owner attrition]
threats:
  - type: selection-and-anticipation
    basis: inferred
    condition: Voluntary coordination and preparation can precede selected admission; membership is not random and insignificant pretrend estimates do not prove parallel trends.
    evidence_refs: [E1, E3]
    possible_diagnostics: [pre-admission cooperation histories, cohort-specific trends, credible comparison risk sets]
  - type: implementation-and-overlap
    basis: documented
    condition: Entry, regional planning and individual cooperation projects are different events; the municipal source describes prospective integration activity after admission.
    evidence_refs: [E3, E4]
    possible_diagnostics: [separate planning and project dates, outcome-specific overlapping policies]
  - type: network-interference-and-inference
    basis: inferred
    condition: One-member pairs can be affected and pairs sharing an endpoint need not be independent. Pair clustering alone does not address this dependence.
    evidence_refs: [E1]
    possible_diagnostics: [dyadic dependence sensitivity, spillover-aware estimands, state-specific comparisons]
  - type: owner-and-location-measurement
    basis: reported
    condition: Matching uses a single2008 census and cleaned names with address checking. Historical relocation, suffix collisions, unmatched firms and multi-owner pair weighting are not resolved by the published matching description alone.
    evidence_refs: [E1, E2]
    possible_diagnostics: [stable-address subset, match-quality audit, explicit co-owner weighting, firm coverage by cohort]
empirical_requirements:
  contract_version: 1
  population: Firms in the reported Jiangsu-Zhejiang-Anhui-Shanghai city-pair sample with matched patent co-owner and2008 census information.
  observation_unit: city-pair-year
  geography_level: pair of prefecture-level municipalities
  time_start: 2000
  time_end: 2015
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 2
  required_fields: [city-pair research outcome, council entry cohort for both endpoints, patent publication number and distinct corporate co-owners for published innovation outcomes, grant year, firm names and checked addresses, census industry and ownership for extensions, historical location convention, city controls and pair transport links for published specification]
  required_identifiers: [city_i, city_j, year, firm_owner_id, patent_publication_number]
  treatment_key: [city_i, city_j, year]
  treatment_source: JWE2022 supplement Table1 provides reported cohorts; municipal Yancheng entry and Xuancheng membership snapshot independently support bounded institutional facts, not every historical admission date.
  measurement_risks: [historical city changes, single-census survivorship and relocation, multi-owner weighting, intensive-margin zero convention, application-versus-grant control discrepancy]
evidence:
  - id: E1
    source_type: paper
    citation: '李建成、程玲、吴明琴 (2022). 政府协调下的市场整合与企业创新伙伴选择. 世界经济45(4):187–216.'
    url: https://sjjj.magtech.com.cn/CN/PDF/782
    date: 2022
    supports: [identity.assignment_mechanism, timeline.local_timing, assignment.rule, assignment.comparison_pool, assignment.exposure_construction, design.primary_strategy, design.estimation_notes, empirical_requirements.required_fields, design_applications.data_used, design_applications.treatment_encoding]
    verification_status: reported
    access_level: full-text
    locator: Actual30-page publisher PDF inspected in memory; printedpp191–198 SectionsIII–V, Equations1–3 and Tables1–3; p195 equations visually inspected in source screen. Printedp202 event-study section also inspected. DOI not established.
  - id: E2
    source_type: appendix
    citation: Li-Cheng-Wu2022 publisher supplementary matching instructions and tables.
    url: https://sjjj.magtech.com.cn/fileup/1002-9621/SUPPL/20220418013040.pdf
    date: 2022
    supports: [assignment.treated, assignment.exposure_construction, timeline.local_timing, empirical_requirements.measurement_risks]
    verification_status: reported
    access_level: appendix
    locator: Actual four-page PDF HTTP200, all pages inspected; AppendixA,p1 firm-name/address matching and ownership pairs; AppendixC,Table1,p3 cohorts; Table2,p3 and Tables3/5,p4 alternative samples. Public attachment component articleId782 yielded the real URL; no code or individual observations included.
  - id: E3
    source_type: implementation-document
    citation: Yancheng municipal policy explanation, 十二五规划解读之：抢抓战略机遇 打造发展新引擎.
    url: https://wap.yancheng.gov.cn/art/2011/12/7/art_25892_3599873.html
    date: '2011-12-07'
    supports: [identity.instrument, timeline.effective, assignment.compliance]
    verification_status: verified
    access_level: official-document
    locator: Full section 全面融入长三角; its preceding-year March entry means March2010 for Yancheng. Separate2008 national inclusion and prospective integration plans; does not certify other cities' entry dates.
  - id: E4
    source_type: archive
    citation: Xuancheng municipal meeting account, 安徽宣城等四市加入长三角.
    url: https://www.xuancheng.gov.cn/News/show/249438.html
    date: '2018-04-13'
    supports: [identity.authority, identity.instrument, assignment.unit, assignment.treated]
    verification_status: verified
    access_level: official-document
    locator: Attendance paragraph lists30 existing members; April12 internal mayoral meeting paragraph reports approved admission proposals for4 additional cities. Supports2018 snapshot and municipal admission procedure, not earlier cohort dates or2000–2015 effects.
design_applications:
  - paper: 政府协调下的市场整合与企业创新伙伴选择
    doi: null
    journal: 世界经济 / The Journal of World Economy
    year: 2022
    research_question: Does city-government coordination change firms' intercity innovation partner matching and collaborative output?
    population: Matched corporate patent owners aggregated to city pairs in Jiangsu, Zhejiang, Anhui and Shanghai.
    outcome: Joint invention-patent grants, collaborating firm-pair count and average grants per active firm pair, each logged after adding one.
    data_used: [CNIPA patent ownership and grant information2000–2015, second Economic Census2008, China City Statistical Yearbook, NBS city patent totals, author-collected airport and direct high-speed-rail data]
    treatment_encoding: Reported city entry cohorts determine Both and One membership states; both indicators lagged two years in baseline.
    comparison: Both and One enter jointly against neither-member pairs with city-endpoint and year effects; not a permanent untouched One group.
    empirical_design: Paired-city panel regression and event study; endpoint-by-year effects and negative-binomial models separately reported; baseline clusters by city pair.
    assumptions: [defensible counterfactual trends, explicit membership-state interference, stable outcome and historical-location measurement]
    threats_addressed: [reported event leads, displayed alternative controls and sample checks, supplementary reset comparisons, none proves random admission or complete dyadic independence]
    evidence_refs: [E1, E2]
method_transfer: null
readiness_blockers:
  - Conditional use serves the inspected author's annual membership proxy. All historical admission instruments and founding-count discrepancies are not independently resolved; do not offer precise founding-event or legally effective component treatment from this record.
  - Census access and historical firm/city joins must be secured; report owner-match attrition, relocation and multi-owner weighting rather than assuming a complete annual firm history.
  - Assess selected admission, staggered effects, state transitions, overlap and shared-city dependence for the new outcome; published clustering and pretrends are not causal certification.
  - The2017 county productivity and2025 firm employment papers concern the same council. They are not separate ready shocks or substitutes for the patent contract; the2025 baseline control-window gap remains blocked in the candidate ledger.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

This council organizes cooperation between municipal governments. Membership
opens a coordination relationship, not a common subsidy paid to all firms.
Yancheng's own explanation distinguishes joining in March2010 from inclusion
under a national regional policy and from plans to deepen cooperation [E3].
The municipal meeting record confirms actual membership and admission by
mayoral discussion [E4]. These primary facts ground the institution; they do
not independently verify every date in the research cohort table.

## What Changed

The paper uses cities' entry into this organization as a proxy for market
integration [E1, reported claim]. Its1992 precursor,1997 upgrade and2004
procedural changes are not interchangeable onset dates. Older historical
accounts give inconsistent founding counts. The served2000–2015 application
uses an explicit reported roster with founders already treated before the
sample; it does not identify a1997 founding effect. Exact founding-event
questions remain outside the ready application.

## Implementation and Assignment

The following is the inspected author table, not a newly verified official
admission list [E2, reported claim]:

| Reported admission | Municipalities |
|---|---|
|1997 | 上海、无锡、宁波、舟山、苏州、扬州、杭州、绍兴、南京、南通、泰州、常州、湖州、嘉兴、镇江 |
| August2003 | 台州 |
| March2010 | 合肥、盐城、马鞍山、金华、淮安、衢州 |
| April2013 | 徐州、芜湖、滁州、淮南、丽水、温州、宿迁、连云港 |

The accumulated thirty names agree with the independently inspected2018
municipal snapshot [E4]; Yancheng's entry month has direct municipal support
[E3]. Agreement on names does not independently establish the other dates.
Later2018 and2019 entries in the attachment are outside the patent panel.

## Why This Creates Empirical Variation

For a city pair, admission can change neither-member exposure to One and
then Both. The two indicators belong in one membership-state model, not two
canonical shocks [E1, reported claim]. One is an affected state: partner
diversion is part of the paper's question. A reader must not call every pair
without Both an untreated comparison. The two-year lag reflects the paper's
innovation timing choice, not an institution-wide effective-date rule.

## Identification Risks

Cities choose cooperation and admission can track growth or innovation
capacity. Earlier coordination, regional plans and later projects can alter
the counterfactual [analytical inference]. Pair-level clusters leave open
dependence across pairs sharing a city. The pair-state design also permits
interference: a change in membership can affect outside partners rather
than only the newly admitted city. An appropriate new application needs
these judgments, not just the paper's DID label.

## Data Requirements

Construct joint grants from patent numbers and distinct corporate owners,
match firm names with address checks, and aggregate owner pairs to historical
city pairs and grant years [E1,E2, reported claim]. Do not aggregate all
subsidiary patents to a parent or treat the2008 census as annual firm data.
The appendix supplies a matching procedure, but no executable code, match
error rate or complete historical-location crosswalk. A new dataset can
answer this question only after its coverage, permissions and location
convention are established. Generic patent counts cannot measure partner
matching; alternative city outcomes require their own data contract.

## Evidence Notes

Earlier resolve tasks correctly retained uncertainty before the supplement
and municipal bodies were recovered. Grounded admission now rests on a
reconstructible research proxy plus directly observed institutional facts;
it preserves the remaining gaps as conditions instead of claiming a fully
verified historical charter. The source ledger retains the2017 county and
2025 employment designs, including their different lags and comparison
windows. This file counts the shared membership mechanism once and does
not promote the unresolved employment application.
