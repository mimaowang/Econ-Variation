---
schema_version: 2
id: china-textbook-curriculum-reform
name: China's 2004–2010 Provincial High-School Politics Curriculum Entry-Cohort Reform
aliases:
- Cantoni Chen Yang Yuchtman Zhang curriculum ideology China
- 教科书改革 政治意识形态
- Chinese textbook reform political content
- education ideology China

status: grounded
provenance:
  task_id: task-95e65e4bd5cf
scope:
  country: China
  regions:
  - Mainland provinces other than Shanghai in the paper's 2004–2010 adoption schedule
  domains:
  - education
  - political-economy
  - ideology
  - attitudes
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: Incoming high-school cohorts in mainland provinces encountered the new Politics curriculum when their province entered the senior-high curriculum experiment; Cantoni et al. (2017) use this province-by-entry-cohort exposure to study the political attitudes of Peking University undergraduates. Shanghai used a separate Politics curriculum and is outside this paper's common-textbook comparison.
identity:
  instrument: Staggered entry of provinces into the eighth senior-high curriculum reform, beginning with Guangdong, Shandong, Hainan, and Ningxia in autumn 2004 and extending to the remaining non-Shanghai provinces by 2010. The paper's treatment is the new Politics textbook for an incoming high-school cohort, not an overall fall in ideological content or a change in years of schooling.
  authority: The Ministry of Education issued the 2001 basic-education framework and the 2003 senior-high experiment notice; the latter selected the four first-wave provinces after voluntary applications and left later entry to preparation and subsequent decisions [E2; E3].
  legal_identifiers:
  - 教基〔2001〕17号, 基础教育课程改革纲要（试行）
  - 教基〔2003〕21号, 教育部关于开展普通高中新课程实验工作的通知
  - 普通高中课程方案（实验） and senior-high subject standards issued in 2003, as referenced in 教基〔2003〕21号
  implementation_regime: The 2003 notice designated four first-wave provinces for incoming students in autumn 2004 and proposed a wider rollout, but its 2007 nationwide target was a plan, not observed completion [E3]. The accepted paper documents later provincial entry through 2010 and treats Shanghai as a separate curriculum [E1, reported claim]. Its Politics-textbook comparison finds stronger emphasis on selected government-desired political and economic ideas, including socialist democracy, rule of law, and skepticism of unconstrained markets; it does not find a generic depoliticization [E1].
  assignment_mechanism: In the paper, a student's province of high-school attendance and high-school entry cohort determine whether the old or new Politics curriculum was taught for the three-year high-school spell. Provincial entry dates were not randomized; teacher preparation and provincial adoption decisions can correlate with other trends [E1; E3].
  parent: null
  related_variations:
  - china-keju-abolition-elite-recruitment
  - china-media-censorship-vpn-experiment
timeline:
  announcement: '2003-12-15'
  effective: null
  implementation_start: 2004
  implementation_end: 2010
  local_timing: The 2001 framework set general objectives, and the 15 December 2003 notice formally named Guangdong, Shandong, Hainan, and Ningxia for the autumn 2004 entering class [E2; E3]. The paper's province-level schedule runs from 2004 to 2010; 2007 nationwide entry was an unfulfilled forecast in the 2003 notice, not the paper's treatment date [E1; E3].
  anticipation: The national framework and first-wave notice were public before implementation, but the paper does not demonstrate zero student or provincial anticipation. It contrasts adjacent entry cohorts whose gaokao frameworks and three-year curricula differ, not a surprise announcement [E1].
  last_verified: '2026-10-02'
assignment:
  unit: Individual undergraduate, inheriting province-of-high-school-attendance by high-school-entry-cohort exposure.
  treated: Surveyed Peking University undergraduates whose high-school entry cohort was the first or a later cohort assigned to the new Politics curriculum in their high-school province [E1].
  comparison_pool: Surveyed undergraduates from earlier entry cohorts in the same province and contemporaneous cohorts from other provinces, conditional on province and cohort fixed effects; Shanghai's separate curriculum is outside the common-textbook exposure [E1].
  rule: NewCurriculum_cp equals one when high-school entry cohort c is at or after province p's first new-curriculum entry cohort, using the province of high-school attendance rather than current residence. The incoming cohort studies the new three-year curriculum; an older cohort remains on the old curriculum, so the baseline is not a 1–2-year partial-dose design [E1].
  intensity: Binary old-versus-new curriculum assignment in the paper's main design; textbook word-frequency changes describe content, not treatment dosage [E1].
  compliance: The accepted manuscript reports that nearly 95 percent of surveyed students identified the predicted old/new textbook cover, supporting but not proving perfect individual compliance; within-province school implementation was not independently audited [E1].
  exemptions: []
  exposure_construction: Join each surveyed student's reported high-school province and entry cohort to the paper's provincial first-entry schedule (Appendix B, Table B.1). Code exposure once per province-entry cohort; keep the 2013 survey outcome separate from curriculum timing and do not substitute current university province [E1].
  required_identifiers:
  - student ID
  - province code
  - high school entry year (cohort)
  - provincial first-entry cohort from the reform schedule
  spillovers: The paper notes that older and younger high-school cohorts may interact, and later university peers may share attitudes; cross-cohort contamination could attenuate the estimated contrast, not establish an uncontaminated direct effect [E1].
research_compatibility:
  outcome_domains:
  - attitudes toward Chinese governance, democratic institutions, and political participation
  - trust in government officials and views of bribery
  - skepticism of unconstrained free markets
  - stated identity and environmental attitudes, with weaker or mixed results
  - self-reported political and investment behavior, with mixed evidence
  affected_populations:
  - Peking University undergraduates surveyed in 2013 who attended high school in mainland provinces under the paper's curriculum schedule
  - other high-school entry cohorts in adopting mainland provinces only as a proposed reuse population, not the paper's observed sample
  mechanism_channels:
  - revised Politics textbooks and matching gaokao frameworks conveying government-desired views of governance and economic institutions
  - cohort-level exposure to different material within the same province
  best_for:
  - Studying how a specific state-directed curriculum change shaped beliefs of comparable Chinese high-school cohorts
  - Questions with a known high-school province and entry year, and outcomes measured after schooling
  not_good_for:
  - A generic decrease in political content, critical-thinking treatment, or education-quantity shock
  - Inferring national effects from the selective Peking University survey without new representative outcome data
  - Annual province policy DID using the 2007 planned national completion date as actual treatment
design:
  claim_type: causal
  affordances:
  - Sharp old/new curriculum boundary for incoming high-school cohorts within province
  - Officially designated 2004 first wave and paper-documented later provincial entry through 2010
  - Textbook, gaokao-framework, and survey-outcome comparison tied to specific messages rather than a generic ideology score
  candidate_designs:
  - Individual-level generalized difference-in-differences with province and high-school-entry-cohort fixed effects
  - Relative-entry-cohort contrasts around the first treated cohort as a pretrend and sharpness diagnostic
  identifying_variation: The paper compares undergraduates whose high-school province introduced the new Politics curriculum for their entering class with adjacent classes in that province and same-year classes elsewhere; timing was administratively chosen, not randomized [E1; E3].
  assumptions:
  - Absent reform, province-by-entry-cohort attitudes in the surveyed population would not jump at the adoption boundary after province and cohort fixed effects.
  - Student selection into Peking University and survey response does not change discontinuously with province-by-cohort exposure in ways that drive outcomes.
  - Reported high-school province and entry year correctly classify the curriculum and are not chosen in response to the reform.
  diagnostics:
  - Textbook-cover recall against predicted assignment (roughly 95 percent agreement in the accepted manuscript)
  - Relative-cohort coefficients before entry, province-specific cohort trends, and province-level or two-way clustered inference
  - Balance and response-rate checks using Peking University enrollment counts by province-cohort
  - Alternative outcome indices and multiple-testing adjustments; reported behavioral evidence remains mixed
  primary_strategy: Individual-level generalized difference-in-differences on the authors' April–May 2013 Peking University survey; regress each attitude measure on NewCurriculum_cp plus high-school province and entry-cohort fixed effects, clustering at province-by-cohort level [E1, Eq. 1, §§3–5].
  estimand: The effect of assignment to the new Politics curriculum on surveyed Peking University students' later stated attitudes under the conditional parallel-cohort and selection assumptions; this is not an estimate for all Chinese students [E1].
  treatment_variable: Binary first-or-later high-school entry under the province's new Politics curriculum, not years of partial exposure or a generic decline in ideological instruction [E1].
  comparison_logic: Within-province adjacent entry cohorts across the introduction boundary, net of nationwide entry-cohort shifts identified across provinces. Provincial adoption order is not randomly assigned [E1].
  estimation_notes: The paper's core outcome data are one 2013 cross-section, not an annual student panel; the accepted manuscript uses 1,954 surveyed students in descriptive Table 2 and outcome-specific samples in Tables 3–5. Some provinces enter the sample only under one curriculum, so within-province transition evidence is most transparent in the 13 provinces with both old and new cohorts in the survey [E1].
threats:
- type: endogenous-adoption-timing
  basis: reported
  condition: Provinces volunteered or prepared for entry, and the paper expressly states rollout was not randomized. Province fixed effects remove fixed differences, not province-by-cohort shocks or endogenous preparation trends [E1; E3].
  evidence_refs:
  - E1
  - E3
  possible_diagnostics:
  - Inspect relative-cohort pretrends and province-specific cohort trends.
  - Check policy-concurrent shocks in early versus late adopting provinces.
- type: cohort-confounds
  basis: reported
  condition: Cohort-specific national shocks are absorbed by cohort effects, but a provincial shock that affects adjacent entry cohorts differently near reform can mimic the treatment effect; the paper discusses this explicitly [E1, §4.2].
  evidence_refs:
  - E1
  possible_diagnostics:
  - Estimate relative-cohort contrasts before adoption.
  - Compare outcomes robust to province-specific cohort trends and local shocks.
- type: selective-university-and-survey-sample
  basis: documented
  condition: The paper surveys Peking University undergraduates in 2013, with an 18.6 percent online response rate. The authors check conditional balance and response rates, but the sample is neither all high-school students nor a nationally representative panel [E1, §§3–4].
  evidence_refs:
  - E1
  possible_diagnostics:
  - Reproduce province-cohort enrollment and response-rate checks.
  - Use representative outcome data before generalizing beyond the surveyed university population.
empirical_requirements:
  contract_version: 1
  population: Peking University undergraduate survey respondents in April–May 2013 who reported their mainland high-school province and cohort; a new application requires its own comparably linked outcome population.
  observation_unit: Individual in a 2013 cross-section, assigned province-by-high-school-entry-cohort treatment.
  geography_level: Province of high-school attendance, excluding Shanghai's separate Politics curriculum in the paper's common-textbook comparison.
  time_start: 2013
  time_end: 2013
  minimum_frequency: cross-sectional
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields:
  - province of high-school attendance
  - high-school entry cohort (or reliable graduation cohort with a three-year conversion)
  - province's first new-curriculum entry cohort
  - post-schooling political-attitude outcomes from the author's 2013 survey or a comparable source
  - survey respondent and eligible enrollment counts by province-cohort to assess selection
  required_identifiers:
  - respondent ID
  - high-school province code
  - high-school entry cohort
  treatment_key:
  - high-school province code
  - high-school entry cohort
  treatment_source: The official 2003 Ministry notice verifies first-wave assignment; the paper's Appendix B, Table B.1 compiles later province entry years from provincial documents. Outcomes come from the authors' 2013 Peking University survey, not CGSS or CFPS [E1; E3].
  measurement_risks:
  - political-attitude answers may reflect social desirability or survey framing, although the paper examines response distributions and private completion
  - observed survey coverage and Peking University selection limit external validity
  - province-level timing does not independently certify school-level delivery, and textbook-cover recall is below perfect
  - Shanghai's distinct Politics curriculum is not interchangeable with the common old/new textbook comparison
evidence:
- id: E1
  source_type: paper
  citation: 'Cantoni, Davide, Yuyu Chen, David Y. Yang, Noam Yuchtman, and Y. Jane Zhang. "Curriculum and Ideology." Final accepted manuscript dated October 7, 2015, deposited at LSE Research Online; published Journal of Political Economy 125(2): 338–392 (2017), DOI 10.1086/690951.'
  url: https://eprints.lse.ac.uk/91515/1/Yuchtman_Curriculum-and-ideology.pdf
  date: 2015
  supports:
  - scope.china_relevance
  - identity.instrument
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.local_timing
  - timeline.anticipation
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.compliance
  - assignment.exposure_construction
  - assignment.spillovers
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - design.assumptions
  - design.diagnostics
  - threats.condition
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_source
  - design_applications.paper
  - design_applications.research_question
  - design_applications.population
  - design_applications.outcome
  - design_applications.data_used
  - design_applications.treatment_encoding
  - design_applications.comparison
  - design_applications.empirical_design
  - design_applications.assumptions
  - design_applications.threats_addressed
  verification_status: verified
  access_level: full-text
  locator: 'LSE-hosted 117-page final accepted manuscript read 2026-10-02: pp. 2, 6–13 (reform and textbook/gaokao content); pp. 13–23 (§§3–4 and Eq. 1: 2013 Peking University survey, province-by-entry-cohort assignment, selection and controls); pp. 29–35 (§5 diagnostics and limits); Table 1 (word frequencies), Table 2 (1,954 respondents), Tables 3–6 (outcomes and checks), Appendix B Table B.1 (province schedule and cited local sources). This is author-accepted, not publisher typesetting, and later provincial implementation remains attributed to the paper.'
- id: E2
  source_type: policy-document
  citation: 'Ministry of Education. 2001. 教育部关于印发《基础教育课程改革纲要（试行）》的通知, 教基〔2001〕17号.'
  url: https://www.moe.gov.cn/srcsite/A26/jcj_kcjcgh/200106/t20010608_167343.html
  date: '2001-06-08'
  supports:
  - identity.authority
  - identity.legal_identifiers
  - timeline.local_timing
  verification_status: verified
  access_level: official-document
  locator: 'Original Ministry text fetched 2026-10-02 (HTTP 200 after redirect). Notice number and curriculum objectives inspected: patriotic, collectivist and socialist education, socialist rule-of-law awareness, moral development and innovation/practical capacities. This framework does not assign the senior-high first-wave provinces.'
- id: E3
  source_type: implementation-document
  citation: 'Ministry of Education. 2003. 教育部关于开展普通高中新课程实验工作的通知, 教基〔2003〕21号, December 15.'
  url: https://www.moe.gov.cn/srcsite/A06/s3732/200312/t20031215_167347.html
  date: '2003-12-15'
  supports:
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.announcement
  - timeline.implementation_start
  - timeline.local_timing
  - assignment.rule
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: official-document
  locator: 'Original Ministry notice fetched and inspected 2026-10-02 (HTTP 200 after redirect): first paragraph names Guangdong, Shandong, Hainan and Ningxia after provincial voluntary applications, beginning with autumn 2004 incoming classes; next paragraph gives 2005–07 expansion projections, not observed dates; final paragraph instructs other provinces to prepare and choose entry timing. It does not certify the paper’s later province list or school-level compliance.'
- id: E4
  source_type: paper
  citation: 'Cantoni et al. 2017. "Curriculum and Ideology." Journal of Political Economy 125(2): 338–392. DOI 10.1086/690951.'
  url: https://doi.org/10.1086/690951
  date: 2017
  supports:
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
  verification_status: verified
  access_level: metadata
  locator: 'Publisher DOI page inspected 2026-10-02: bibliographic identity, 2017 publication and abstract; full journal text requires access, so substantive design details rely on E1 final accepted manuscript.'
design_applications:
- paper: Curriculum and Ideology
  doi: 10.1086/690951
  journal: Journal of Political Economy
  year: 2017
  research_question: Did China's new high-school Politics curriculum change the political and economic attitudes of students who studied under it?
  population: 1,954 Peking University undergraduates responding to the authors' April–May 2013 survey, with outcomes analyzed on item-specific subsamples; high-school provinces and entry cohorts determine exposure.
  outcome: Stated trust in government officials, perceptions of Chinese democracy and political participation, skepticism toward unconstrained free markets, identity and environmental attitudes; behavioral evidence is mixed.
  data_used:
  - Author-conducted 2013 Peking University web survey (respondent attitude items, high-school province/cohort, demographics and textbook-cover recall)
  - Peking University enrollment counts by province-cohort for survey-response diagnostics
  - Provincial first-entry schedule compiled in the paper's Appendix B, Table B.1 from official provincial sources
  - Old/new Politics textbooks and gaokao-framework content comparisons to identify government-desired message changes
  treatment_encoding: Binary NewCurriculum_cp for a respondent whose high-school entry cohort is at or after province p's first new-curriculum cohort; Shanghai's separate Politics textbooks are outside the paper's common-textbook comparison.
  comparison: Adjacent old-versus-new high-school entry cohorts within province, net of cohort fixed effects that use cross-province timing variation.
  empirical_design: Generalized difference-in-differences on a 2013 individual survey with high-school province and entry-cohort fixed effects and province-by-cohort clustered errors; relative-cohort, selection, trend and inference checks.
  assumptions:
  - Province-by-entry-cohort attitude trends would not jump at adoption absent the new curriculum.
  - Selection into Peking University and survey response does not differentially induce the observed effect.
  - Reported high-school province and entry year accurately encode curriculum exposure.
  threats_addressed:
  - Nonrandom provincial rollout partly addressed by province and cohort fixed effects, province-specific trends and relative-cohort checks; these do not prove exclusion.
  - Selective sampling examined through province-cohort enrollment/response rates and observed balance.
  - Possible differential reporting considered through survey design and response-distribution checks; behavior findings are not uniformly strong.
  evidence_refs:
  - E1
  - E3
  - E4
readiness_blockers:
- Only the 2004 first-wave provincial assignment and national framework were independently checked against Ministry documents. The paper's Appendix B compiles the later 2005–10 province schedule and cites local documents, but those later source documents were not independently inspected in this audit.
- The paper's reported effect is for a selective 2013 Peking University survey, not an all-China student effect; another population needs its own outcomes and selection checks.
method_transfer: null
---
## Institutional Background
The Ministry of Education's 2001 basic-education framework combined academic and practical objectives with explicit patriotic, collectivist, socialist and moral-education aims [E2]. The Ministry's December 2003 notice then organized a senior-high experiment: Guangdong, Shandong, Hainan and Ningxia applied and were selected as the first entrants for autumn 2004, while other provinces were told to prepare teachers and materials and determine later entry [E3]. Cantoni et al. study the Politics textbooks within this broader reform, not a generic schooling expansion [E1].

## What Changed
Incoming high-school cohorts in adopting provinces studied revised Politics textbooks and a corresponding gaokao framework; earlier cohorts stayed on the old curriculum during their three-year spell [E1]. The authors compare the old and new Economic Life and Political Life books and find stronger coverage of specific government-desired messages about Chinese socialist democracy, governance, rule of law and economic institutions. In their word-frequency comparison, “market economy” declines while “socialism with Chinese characteristics” rises [E1, §2.3 and Table 1]. The old record's claim that this was a general reduction in political content reverses the paper's account. The Ministry's 2007 nationwide entry target was a projection; the authors document provincial entry continuing through 2010 [E1; E3].

## Implementation and Assignment
The paper codes exposure from the province of high-school attendance and the student's entry cohort, using the province-specific first new-curriculum cohort compiled in Appendix B, Table B.1 [E1]. Its empirical sample is not all pupils: 1,954 respondents to a 2013 Peking University undergraduate survey appear in descriptive Table 2, and item-level sample sizes vary [E1]. Within that sample, a treated respondent belongs to a cohort entering high school at or after the provincial switch; the comparison is an earlier cohort in the same province and same-year cohorts elsewhere. The authors report nearly 95 percent agreement when students identify the expected textbook cover. They do not claim that adoption timing was randomized or that every school implemented identically [E1; E3].

## Why This Creates Empirical Variation
The sharp entry-cohort boundary lets the authors compare students who attended high school in the same province one cohort apart yet used different curricula. Province fixed effects absorb stable provincial differences; entry-cohort effects absorb common national changes. The paper's generalized difference-in-differences coefficient is informative if other province-by-cohort determinants of later attitudes do not jump at the same boundary and if selection into university and the survey is not treatment-related [E1, Eq. 1 and §4]. The documented outcomes are more positive views of Chinese governance and greater skepticism of free markets; evidence on behavior and some other attitudes is mixed [E1; E4].

## Identification Risks
Provincial rollout was nonrandom: preparation and voluntary application could track economic, political or educational trends [E1; E3]. The accepted manuscript tests relative-cohort patterns, province-specific cohort trends, student balance, enrollment-cell response rates and textbook-cover recall, but none proves the identifying restriction. The 18.6 percent online response rate and elite-university sampling especially constrain population claims. Political-attitude responses may also differ from behavior; the paper reports mixed behavioral evidence rather than a uniformly persuasive effect [E1, §§3–5].

## Data Requirements
Reusing this assignment requires the high-school province and entry cohort, the provincial first-entry schedule, and outcomes measured after exposure. Reproducing the paper also requires its 2013 Peking University survey, province-cohort enrollment denominators for response-rate checks, and the old/new textbooks and gaokao frameworks for interpreting mechanisms [E1; E3]. CGSS and CFPS were not the data used in the paper; substituting either would be a new application needing its own exposure and selection audit.

## Evidence Notes
E1 is the LSE-hosted final accepted manuscript, read directly, and establishes the authors' treatment coding, data, content analysis, results and stated diagnostics as paper claims. E2 and E3 are the original Ministry texts, read directly; they establish the national framework and 2004 first-wave assignment but not every later province's implementation. E4 verifies the final publication identity and abstract, not the paywalled final typesetting. The record is grounded on the first-wave primary document and paper-documented later schedule; the latter remains attributed rather than independently certified. No paper or restricted microdata was stored.
