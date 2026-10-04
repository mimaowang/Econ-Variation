---
schema_version: 2
id: china-firm-media-bias-competition
name: 2003 County-Party-Newspaper Closures and Prefectural Media Competition
aliases:
- Media Bias in China
- Qin Strömberg Wu county-daily reform
- 2003 县市报刊治理

status: design-documented
provenance:
  task_id: task-6eac2d84ffc6
scope:
  country: China
  regions:
  - Mainland Chinese prefectural newspaper markets observed in the paper
  domains:
  - media
  - political-economy
  - information
  - competition
  - urban-economics
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: A nationwide 2003 closure order removed county-level Party papers in mainland China; prefectural papers faced differential loss of competitors according to the number of county papers already present in their markets.
identity:
  instrument: The 2003 central newspaper-governance campaign required most county/city-district Party newspapers to cease publication, with narrow retention or upper-tier merger routes.
  authority: General Offices of the CCP Central Committee and State Council issued the notice; General Administration of Press and Publication coordinated approval and cancellation with local implementing authorities [E1; E2].
  legal_identifiers:
  - 中办发〔2003〕19号, 关于进一步治理党政部门报刊散滥和利用职权发行、减轻基层和农民负担的通知
  - 新闻出版总署 2003 implementation rules for 中办发〔2003〕19号
  implementation_regime: The July 2003 national order targeted county/city-district papers while exempting some pre-1949 Party titles and minority-language/autonomous-county papers and allowing reviewed mergers of large papers. Closures and transfers were to be processed in 2003, with contract/registration matters ending by December [E1; E2].
  assignment_mechanism: The legal closure rule applies to a newspaper's administrative rank and exceptions; the paper uses a prefecture's count of county papers in 2002 as predetermined intensity of lost newspaper competition after 2003. This is not a randomized closure or a generic commercial-newspaper-entry shock [E1; E3].
  parent: null
  related_variations: []
timeline:
  announcement: '2003-07-15'
  implementation_start: 2003
  implementation_end: 2003
  local_timing: The central notice was issued in July 2003; adjustment approvals were scheduled by September and merger/closure contracts could run through December. The paper codes all 2003 and later years as post, while its newspaper directory shows 325 county papers in 2002 and 75 in 2004 [E1–E3].
  effective: null
  anticipation: The July notice and subsequent approvals gave papers time to adjust within 2003; the paper's annual post-2003 indicator cannot establish zero anticipation or a common day of cessation [E1; E2].
  last_verified: '2026-10-02'
assignment:
  unit: Surviving prefectural newspaper-year, carrying the prefecture's 2002 county-paper count.
  treated: Prefectural Party and commercial papers in markets with more county-level newspapers before the national closure; exposure is continuous, not a binary list of selected prefectures.
  comparison_pool: Surviving prefectural papers in otherwise comparable markets with fewer or no county newspapers in 2002, observed before and after 2003. Party and commercial papers are estimated separately or interacted with exposure [E3].
  rule: Construct Reform_2003 = number of county-level papers in prefecture in 2002 × 1(year ≥ 2003). Actual closures reduced competition but were incomplete; do not substitute realized newspaper exits or contemporaneous market size for this baseline-exposure variable [E3, §IV.A].
  intensity: Number of county papers in 2002; the authors report a national decline from 325 in 2002 to 75 in 2004, not a one-for-one closure in every prefecture.
  exposure_construction: Join the author-compiled 1981–2011 newspaper directory to each observed surviving prefectural paper, retain its prefecture and Party/commercial type, attach the prefecture's 2002 county-paper count, then interact with a 2003+ year indicator and content outcomes from WiseNews [E3, §§II, IV].
  required_identifiers:
  - prefecture code
  - year
  - newspaper ID
  - administrative level and Party/commercial type
  exemptions:
  - Pre-1949 Party-founded county papers and papers in autonomous counties or minority languages could remain.
  - Selected large county papers could be absorbed by province/prefecture-level Party groups after review.
  compliance: Most but not all county papers closed; the order did not mechanically remove each baseline paper. The empirical intensity is intent-to-treat-style baseline exposure to the reform, not verified actual closures for each market [E1–E3].
  spillovers: Competition and product differentiation within the same newspaper market are the mechanism being studied; cross-prefecture readership or advertising spillovers remain possible [E3].
research_compatibility:
  outcome_domains:
  - political versus commercial newspaper content
  - media-market product differentiation
  - competition among government-owned newspapers
  affected_populations:
  - surviving prefectural Party and commercial newspapers
  - readers and advertisers in their local markets
  mechanism_channels:
  - loss of county-level Party-paper competitors
  - different product positioning by Party and commercial papers
  best_for:
  - Studying how the 2003 closure changed content of surviving prefectural papers by their baseline competitor count
  - Comparing Party-versus-commercial responses under the same local market shock
  not_good_for:
  - Treating voluntary commercial-paper entry as part of the closure assignment
  - Inferring effects on the closed county papers' own content, which WiseNews does not cover
  - Measuring citizen beliefs, voting, or readership directly from newspaper content
design:
  claim_type: causal
  affordances:
  - National closure rule crossed with predetermined prefecture exposure
  - Newspaper-by-year content before and after the 2003 campaign
  - Party/commercial type heterogeneity within markets
  candidate_designs:
  - Continuous-exposure difference-in-differences for surviving newspapers
  - Exposure-by-year event study and placebo 2002 reform
  identifying_variation: Differential 2003 loss of county-paper competition predicted by the number of county papers in the prefecture in 2002; not an instrument for HHI or a random newspaper-level closure [E3, §IV].
  assumptions:
  - Without the closure campaign, higher- and lower-baseline-county-paper markets would have had comparable trends in survivor-paper content, conditional on fixed effects and controls.
  - Other contemporaneous changes did not differentially affect prefectures in proportion to the 2002 county-paper count.
  diagnostics:
  - Paper Figure 5 exposure-by-year coefficients and Table 3 placebo-2002 test
  - Compare 16 theory-aligned markets with the broader 872 newspaper-year sample
  - Control for baseline market predictors interacted with post and assess concurrent media-group changes
  primary_strategy: Newspaper-year panel DID with newspaper and year fixed effects, prefecture-clustered errors, baseline county-paper count × 2003+ and its interaction with commercial-paper type [E3, Table 2].
  estimand: Differential change in surviving prefectural papers' content per additional county paper present locally in 2002, separately for Party and commercial papers.
  treatment_variable: Prefecture 2002 county-paper count × 1(year ≥ 2003), plus its interaction with the commercial-paper indicator.
  comparison_logic: Higher- versus lower-baseline-county-paper prefectures before and after 2003, preserving the paper-type interaction; the paper's Figure 6 median split is an illustration, not the main regression encoding.
  estimation_notes: The accepted article's Table 2 reports 872 newspaper-year observations in the full sample and identifies 16 theory-aligned markets (286 observations) for its main interpretation; it does not estimate an IV using closure as an instrument for current competition [E3, pp. 20–23].
threats:
- type: differential-baseline-trends
  basis: documented
  condition: Prefectures with more county papers in 2002 could have different post-2003 content trends even absent the order; one placebo year cannot prove the counterfactual [E3, §IV.C].
  evidence_refs: [E3]
  possible_diagnostics:
  - Exposure-by-year pre-trends and alternative baseline-market controls.
- type: exceptions-and-imperfect-exit
  basis: documented
  condition: Official rules exempt some titles and allow approved mergers, so 2002 count is predicted intensity rather than realized closure count [E1; E2].
  evidence_refs: [E1, E2, E3]
  possible_diagnostics:
  - Link each 2002 county paper to its 2004 license outcome when reconstructing a first stage.
- type: concurrent-policy-and-content-measurement
  basis: reported
  condition: Newspaper-group formation and changes in WiseNews coverage or text composition can correlate with baseline paper count; county-paper content is absent from WiseNews [E3, §§II, IV.C; E4].
  evidence_refs: [E3, E4]
  possible_diagnostics:
  - Reproduce paper's Wuhan/Hefei exclusions and appendix content-category checks.
empirical_requirements:
  contract_version: 1
  population: Surviving mainland Chinese prefectural Party and commercial newspapers in the paper's WiseNews content panel; directory covers about 1,000 general-interest titles.
  observation_unit: Newspaper-year
  geography_level: Prefectural newspaper market
  time_start: 1999
  time_end: 2010
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 2
  required_fields:
  - 2002 county-paper count by prefecture from historical directory
  - surviving newspaper ID, market, administrative level, Party/commercial type, year
  - annual article-topic shares and PCA bias measure from WiseNews
  - prefectural GDP, population, industrial share and FDI for reported controls
  required_identifiers:
  - newspaper ID
  - prefecture code
  - year
  treatment_key:
  - prefecture 2002 county-paper count
  - year ≥ 2003
  - commercial-paper type for heterogeneous effects
  treatment_source: Author-compiled 1981–2011 newspaper directory linked to the 2003 central reform; content outcomes from WiseNews 1999–2010 [E3; E4]. The original directory and licensed content are separate from the public policy notice.
  measurement_risks:
  - WiseNews has no county-paper content and incomplete early coverage
  - Baseline paper count requires stable prefecture/owner crosswalk
  - PCA content measure does not directly measure reader belief or censorship intensity
  - Exceptions and mergers make baseline exposure differ from actual closures
evidence:
- id: E1
  source_type: policy-document
  citation: 'CCP Central Committee General Office and State Council General Office, 关于进一步治理党政部门报刊散滥和利用职权发行、减轻基层和农民负担的通知, 中办发〔2003〕19号, reproduced in Zhejiang Provincial Gazette 2003 issue 24.'
  url: https://zjdy.zjdafw.gov.cn/zjzb/ZJZB-2003-24-11.pdf
  date: '2003-07-15'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, identity.assignment_mechanism, timeline.announcement, timeline.implementation_start, assignment.rule, assignment.exemptions, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: 'Zhejiang Provincial Gazette issue 24, notice section II.3: county/city-district newspapers generally cease, with upper-tier merger option for selected large papers; inspected 2026-10-02. This document sets the rule, not the paper’s measured prefecture-year exposure.'
- id: E2
  source_type: archive
  citation: 'Central Newspaper Governance Coordination Office, Q&A reported in People’s Daily, 2003-12-22, p. 2, archived newspaper scan/text.'
  url: https://cn.govopendata.com/renminribao/2003/12/22/2/
  date: '2003-12-22'
  supports: [identity.authority, identity.implementation_regime, timeline.local_timing, assignment.exemptions, assignment.compliance]
  verification_status: verified
  access_level: full-text
  locator: 'Q&A on county-paper closures: 262 county/city-district papers among 677 closures, 35 approved mergers, transfers/closure business ending December 2003, ceased papers barred from substitute publication; inspected 2026-10-02. The official answers are reproduced by a third-party archive, not independently checked against an original print copy.'
- id: E3
  source_type: paper
  citation: 'Qin, Bei, David Strömberg, and Yanhui Wu. 2018. "Media Bias in China." American Economic Review 108(9):2442–2476, DOI 10.1257/aer.20170947. Author-hosted accepted manuscript.'
  url: https://www.yanhuiwu.com/documents/newspaper_bias.pdf
  date: '2018'
  supports: [identity.assignment_mechanism, timeline.local_timing, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.intensity, assignment.exposure_construction, design.identifying_variation, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.population, empirical_requirements.observation_unit, empirical_requirements.required_fields, empirical_requirements.treatment_source, design_applications.data_used, design_applications.empirical_design]
  verification_status: verified
  access_level: full-text
  locator: 'Accepted AER manuscript, PDF pp. 1–3 for 117-paper content versus 1981–2011 directory, pp. 19–23 §IV for 2003 closure rule, 2002 count × post, 16-market/main and 872-observation/full samples, Tables 2–3 and Figures 5–6; inspected 2026-10-02. Reports author coding, not independent validation of every historic title.'
- id: E4
  source_type: appendix
  citation: 'Qin, Strömberg and Wu, Online Appendix to Media Bias in China, AEA materials.'
  url: https://www.aeaweb.org/articles/materials/9504
  date: '2018'
  supports: [design.diagnostics, empirical_requirements.measurement_risks, design_applications.threats_addressed]
  verification_status: verified
  access_level: appendix
  locator: 'Empirical Appendix Part 1 pp. 1–10, WiseNews sample description and additional tables; inspected 2026-10-02. Its theory appendix is not evidence that the policy mechanically randomized local paper counts.'
- id: E5
  source_type: paper
  citation: 'American Economic Association, Media Bias in China, American Economic Review 108(9), 2018, DOI 10.1257/aer.20170947.'
  url: https://doi.org/10.1257/aer.20170947
  date: '2018'
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: 'AEA article landing page bibliographic metadata; inspected 2026-10-02. Empirical specifics come from E3.'
design_applications:
- paper: Media Bias in China
  doi: 10.1257/aer.20170947
  journal: American Economic Review
  year: 2018
  research_question: How did the nationwide closure of county Party papers change content specialization of surviving prefectural Party and commercial newspapers?
  population: WiseNews-observed general-interest papers in mainland urban markets, 1999–2010; author directory tracks about 1,000 papers 1981–2011. Main theory-aligned sample covers 16 markets (286 newspaper-years); full empirical sample has 872 newspaper-years.
  outcome: Newspaper-year PCA index built from nine article-content categories, including leader/Xinhua references, sensitive/negative news, sports, crime and entertainment.
  data_used: [Author-compiled 1981–2011 newspaper directory with administrative rank and entry/exit, WiseNews 1999–2010 article content for 117 general-interest newspapers, prefectural GDP/population/industry/FDI controls]
  treatment_encoding: 2002 county-paper count in each prefecture × indicator for 2003 or later; interact again with commercial-paper type to estimate differential content response.
  comparison: Surviving prefectural newspapers in markets with different pre-reform county-paper counts, before versus after 2003; Party and commercial responses separated.
  empirical_design: Continuous-exposure DID at newspaper-year level with newspaper/year fixed effects and prefecture-clustered errors; placebo-2002 and event-time analyses.
  assumptions:
  - Conditional parallel trends in survivor-paper content by baseline county-paper count.
  - No concurrent shock correlated with that baseline count fully explains the type-specific post-2003 response.
  threats_addressed:
  - 2002 placebo and Figure 5 pre-reform coefficients
  - Controls for prefecture-level economic predictors and concurrent group-formation checks
  - Appendix content-category and alternative-sample analyses
  evidence_refs: [E1, E2, E3, E4, E5]
readiness_blockers: []
method_transfer: null
---
## Institutional Background

The 2003 campaign addressed the proliferation of party-government periodicals and compulsory subscriptions. The original notice generally stopped county and city-district papers, with explicit heritage/language exceptions and a reviewed merger path for some larger titles. The central coordination office later reported 262 such closures and 35 approved mergers. That institutional rule is narrower than the broad 1981–2011 commercialization of China's newspaper sector [E1; E2].

## What Changed

Prefectural Party and commercial papers lost varying numbers of county Party-paper competitors because their markets had different counts before the common national order. Qin, Strömberg and Wu use the 2002 county count crossed with a 2003+ indicator, not contemporaneous entry, realized exits, or a market HHI. Their author directory places county-paper counts at 325 nationally in 2002 and 75 in 2004, but official aggregate closure counts use a partly different all-periodicals boundary [E2; E3].

## Implementation and Assignment

The policy decided which lower-tier titles had to cease or could merge; it did not randomly assign prefectures. The paper observes content of surviving prefectural newspapers and compares type-specific changes between higher- and lower-exposure markets. Its theory-aligned analysis focuses on 16 markets with a Party and a commercial paper at the upper tier; the broader 872-observation panel is separate. County-paper content is unavailable in WiseNews, so the outcome is never the closed papers' own editorial change [E3, §IV; E4].

## Why This Creates Empirical Variation

The fixed 2002 county-paper count predates the national closure, so it predicts how much local newspaper competition the policy could remove. Identification still depends on parallel content trends by baseline count. The paper finds divergence in opposite directions: surviving Party dailies become more politically oriented while commercial papers become less so. The average effect across both paper types is near zero and should not be rewritten as one uniform bias change [E3, Tables 2–3].

## Identification Risks

Baseline county-paper density may reflect market size, local politics or urban development that also change newspaper content after 2003. Exemptions and mergers make the baseline count an imperfect proxy for actual lost competitors. The authors show year-by-exposure pre-patterns, a 2002 placebo, extra market controls and selected concurrent-media-policy checks; those diagnostics narrow but do not eliminate the parallel-trends condition. Newspaper content is not direct evidence about readers' beliefs or the closed county papers [E1–E4].

## Data Requirements

Recover newspaper IDs, prefecture, administrative tier and Party/commercial category from the historical directory; count county papers in each prefecture in 2002. Link surviving papers to annual WiseNews article categories for 1999–2010 and to local controls. The paper and appendix explain the coding but access to licensed WiseNews text and the historical directory or replication material is necessary for exact reconstruction [E3; E4].

## Evidence Notes

E1 is the contemporaneous notice as published in a provincial gazette; E2 reproduces contemporaneous answers from the central coordinating office. They establish the policy and exceptions, not the paper's prefecture-level treatment series. E3 is the author's accepted AER manuscript inspected for the actual empirical encoding and results, E4 the publisher appendix, and E5 bibliographic identity. The record is usable for the documented conditional DID design, not a general license to call Chinese newspaper competition exogenous.
