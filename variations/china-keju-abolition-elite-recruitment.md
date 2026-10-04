---
schema_version: 2
id: china-keju-abolition-elite-recruitment
name: The 1905 Abolition of China's Civil Service Examination (Keju) as a Shock to Elite Recruitment and Political Stability
aliases:
- Keju abolition 1905
- Bai Jia civil service exam
- 科举废除 精英选拔
- imperial examination abolition

status: grounded
provenance:
  task_id: task-60966e340c79
scope:
  country: China
  regions:
  - 262 prefectures across China
  domains:
  - political-economy
  - history
  - education
  - institutions
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: A national Chinese education and recruitment reform changes historical prefectures' exposure according to their pre-existing entry-exam quotas; the actual application concerns regional political mobilization and the loss of mobility opportunities.
identity:
  instrument: The 1905 abolition of the keju (科举), China's 1,300-year-old civil service examination system, which eliminated
    the primary channel for elite recruitment and created a sudden loss of upward mobility prospects for educated elites across
    all prefectures
  authority: Qing imperial court under Guangxu; the paper reports endorsement by Empress Dowager Cixi
  legal_identifiers:
  - '光绪三十一年八月初四日停罢科举上谕; inspected digital transcription, not original edict image'
  implementation_regime: The abolition was a single national event in 1905, affecting all prefectures simultaneously; however,
    prefectures had different historical quotas (quotas) for entry-level exam candidates, creating cross-sectional variation
    in the intensity of the shock
  assignment_mechanism: Common abolition timing interacted with predetermined entry-level quota exposure. The paper uses late-Qing quotas fixed over 1873-1904, not an unchanged centuries-old quota; county quotas plus a shared prefecture quota generate a lumpy regional allocation.
  parent: null
  related_variations: []
timeline:
  announcement: '1905-09-02'
  effective: null
  implementation_start: 1905
  implementation_end: null
  local_timing: Announced 1905-09-02. The transcribed edict cancels provincial and metropolitan exams beginning with the 1906 cycle and also stops provincial annual/periodic exams. The yearly application nevertheless codes both 1905 and 1906 as post; the separate 1905 monthly exercise uses the September transition.
  anticipation: The paper reports a 1904 plan for gradual abolition within about a decade, followed by accelerated abolition in 1905. Earlier reform expectations and the August 1905 formation of the Revolutionary Alliance complicate an unanticipated-shock interpretation.
  last_verified: '2026-09-28'
assignment:
  unit: Prefecture
  treated: All 262 prefectures face abolition; exposure differs with pre-existing entry-exam quotas. There is no legally untreated prefecture arm.
  comparison_pool: Higher versus lower quota-exposure prefectures before versus after abolition; baseline annual sample is 1900-1906
  rule: Recover the late-Qing county quotas and shared prefecture quota from Kun et al. (1899), aggregate to the paper's prefecture, and combine with population in 1880. The main regression uses log quota interacted with Post and separately controls log population interacted with Post, equivalent to a log quota-per-capita specification with population controls.
  intensity: Logged entry-exam quota relative to population, not the raw quota-per-capita value and not the observed number of exam takers
  compliance: The edict removes the traditional examination route but instructs authorities to arrange alternative paths for existing degree holders and expand schools. It does not establish universal compliance or the elimination of all later examinations or recruitment channels.
  exposure_construction: For the 1900-1906 panel set Post=1 for 1905 and 1906 and multiply by log late-Qing quota. Preserve log 1880 population and other baseline characteristics interacted with Post, prefecture/year effects and province-year effects. Do not apply a September day cutoff to annual observations. IV is supplementary and not required to construct baseline exposure.
  required_identifiers:
  - prefecture code
  - year
  - historical keju quota
  - historical prefecture population in 1880
  exemptions: [Existing degree holders are explicitly promised alternative arrangements; their prospects need not equal those of would-be entrants]
  spillovers: Elites from high-quota prefectures who lost examination prospects may have migrated or mobilized politically,
    affecting neighboring areas
research_compatibility:
  outcome_domains:
  - political participation
  - revolution
  - elite mobility
  - education
  - modernization
  - political stability
  affected_populations:
  - Educated elites
  - examination candidates
  - gentry class
  - local political organizations
  mechanism_channels:
  - blocked upward mobility
  - elite grievances
  - human capital reallocation
  - political mobilization
  - revolutionary participation
  best_for:
  - Studying how institutional changes affecting elite recruitment influence political stability
  - historical natural experiments
  not_good_for:
  - A modern regional panel without historical exposure links
  - Estimating an individual exam candidate's treatment effect from prefecture aggregates
  - Treating the 1911 cross-sectional uprising association as another pre-post DID
design:
  claim_type: causal
  affordances:
  - Common 1905 announcement, with distinct annual and monthly encodings
  - cross-prefecture variation in historical quotas
  - pre/post abolition comparison
  - IV using river geography
  candidate_designs:
  - difference-in-differences (quota × post-1905)
  - instrumental variables using small rivers
  identifying_variation: Regional variation in log entry-exam quotas interacted with abolition timing, conditional on population and other characteristics; the supplement uses normalized small-river counts and pre-quota-system exam-performance changes as alternative instruments, not exam-hall capacity.
  assumptions:
  - Higher- and lower-quota prefectures have comparable conditional trends absent abolition.
  - For IV only, normalized small-river geography affects participation through quota exposure rather than transport, agriculture, administration or other time-varying channels.
  - For the second IV only, pre-1425 short-run changes in exam success have no direct differential post-1905 effect after controlling initial performance and other covariates.
  diagnostics:
  - Test for relationship between quotas and pre-1905 outcomes
  - examine IV first stage and validity
  - compare with alternative historical instruments
  - test for other concurrent reforms
  primary_strategy: Prefecture-year linear probability DID with log quota multiplied by Post; separate monthly, county and IV exercises diagnose the main comparison
  estimand: Differential change in the probability of any registered revolutionary originating from a prefecture by log quota exposure, conditional on population and identifying assumptions; not an average effect of abolition against an unaffected China
  treatment_variable: Log late-Qing entry-exam quota multiplied by an indicator for 1905 or 1906; log population multiplied by Post is separately controlled
  comparison_logic: High-quota vs low-quota prefectures; pre-1905 vs post-1905
  estimation_notes: Prefecture-clustered errors; baseline includes prefecture/year and province-year effects. IV1 is small-river count divided by total river length, interacted with Post, with log river length interacted with Post controlled. Its rationale runs through county formation and stepwise county quota aggregation. IV2 is the difference in log(1+jinshi count) between 1368-1398 and 1399-1425, interacted with Post, with initial performance controlled. The 1911 uprising outcome is a separate cross-sectional association. River thresholds and GIS segmentation need replication-code recovery, not invented cutoffs.
threats:
- type: other-concurrent-reforms
  basis: inferred
  condition: The late Qing period saw multiple modernization reforms (New Policies, constitutional movement); the keju abolition
    was part of a broader reform package
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - control for other reforms
  - use cross-prefecture variation that isolates keju-specific effects
  - compare timing of different reforms
- type: Geography exclusion and quota endogeneity
  basis: reported
  condition: Small-river geography and historical exam performance could affect later development or political networks outside quotas; relevance and placebo results do not prove exclusion. Late quotas also incorporate the Taiping-era revision.
  evidence_refs: [E1]
  possible_diagnostics: [Transport and crop suitability placebos, Climate and basin controls, Early versus late quota robustness, Separate first stages and overidentification diagnostics]
- type: Recorded membership versus all participation
  basis: reported
  condition: Registered revolutionaries have identifiable origins and joining times, but missing lists, organization formation and differential recording may change the measured outcome; origins are not necessarily places of activity.
  evidence_refs: [E1]
  possible_diagnostics: [Monthly Alliance analysis, Guangdong longer-window analysis, Outcome count versus presence, Newspaper coverage for 1911 outcome]
empirical_requirements:
  contract_version: 1
  population: 262 historical prefectures in the paper's main membership panel
  observation_unit: Prefecture-year
  geography_level: Paper-harmonised historical prefecture, with origin-county crosswalk
  time_start: 1900
  time_end: 1906
  minimum_frequency: Annual; published baseline has five pre years and two post-coded years
  minimum_pre_periods: 5
  minimum_post_periods: 2
  required_fields:
  - prefecture code
  - year
  - historical keju quota
  - population in 1880
  - registered revolutionary presence or counts by origin and joining year
  - specification-specific baseline geography and urbanization controls
  required_identifiers:
  - Paper-harmonised historical prefecture code
  - Year
  - Historical province code
  treatment_key:
  - Paper-harmonised historical prefecture code
  - Year
  treatment_source: Kun et al. (1899) quota tables linked to historical prefectures; paper's actual quota and population construction. River geography is required only for the supplementary IV, not the baseline.
  measurement_risks:
  - historical data quality and completeness
  - prefecture boundary changes over time
  - quota measurement accuracy
  - Membership originates from Chang (1982) supplemented by Luo (1958), not a census of all revolutionaries or observed exam candidates.
  - Population reference year 1880 is a denominator vintage, not the beginning of the main outcome panel.
  - Separate 1905 monthly, Guangdong 1894-1906 county and 1911 cross-sectional outcomes cannot be unioned into a national 1880-1912 annual panel.
evidence:
- id: E1
  source_type: paper
  citation: 'Bai, Ying, and Ruixue Jia. 2016. "Elite Recruitment and Political Stability: The Impact of the Abolition of China''s
    Civil Service Exam." Econometrica 84 (2): 677–733.'
  url: https://doi.org/10.3982/ECTA13448
  date: 2016
  supports:
  - scope.china_relevance
  - identity.assignment_mechanism
  - timeline.local_timing
  - timeline.anticipation
  - assignment.rule
  - assignment.intensity
  - assignment.exposure_construction
  - assignment.comparison_pool
  - design.primary_strategy
  - design.estimand
  - design.estimation_notes
  - empirical_requirements.required_fields
  - empirical_requirements.measurement_risks
  - design_applications.data_used
  - design_applications.treatment_encoding
  - design_applications.empirical_design
  - threats.condition
  verification_status: verified
  access_level: full-text
  locator: Published article and appended supplement at https://www.ruixuejia.com/uploads/4/6/3/3/46339953/exam_ecma__1_.pdf inspected 2026-09-28. Sections 2.1-2.4 pp.683-694, equation 1 pp.696-697, monthly and 1911 contrasts pp.701-703, section 3.4 pp.706-713, Tables IV-V and appended Table A.VII. Inspection verifies the reported construction, not raw archive transcription, GIS replication or causal assumptions.
- id: E2
  source_type: archive
  citation: Qing imperial court. 光绪三十一年八月初四日停罢科举上谕, reproduced as 停罢科举诏 on Wikisource.
  url: https://zh.wikisource.org/w/index.php?title=停罷科舉詔&oldid=970721
  date: '1905-09-02'
  supports: [identity.authority, identity.instrument, identity.legal_identifiers, timeline.announcement, timeline.local_timing, assignment.exemptions, assignment.compliance]
  verification_status: verified
  access_level: full-text
  locator: Dated heading and full edict transcription inspected 2026-09-28, including cancellation from 丙午科, stopping provincial annual/periodic exams, alternatives for existing 举贡生员 and expansion of schools. This is a digital primary-text reproduction, not an original archive scan or independently collated critical edition; the Gregorian heading is corroborated by the published paper.
design_applications:
- paper: 'Elite Recruitment and Political Stability: The Impact of the Abolition of China''s Civil Service Exam'
  doi: 10.3982/ECTA13448
  journal: Econometrica
  year: 2016
  research_question: How did the abolition of the keju examination system affect political stability in late Qing China?
  population: 262 historical prefectures, annual baseline 1900-1906 with 1,834 prefecture-year observations
  outcome: Indicator for any registered revolutionary originating from a prefecture in a year; count variants are supplementary
  data_used: [Kun et al. (1899) imperial entry-exam quota tables, Chang (1982) revolutionary organization membership, Luo (1958) Alliance records, Ge (2000) population in 1880, Harvard Yenching historical geography, Treaty-port and city-rank controls]
  treatment_encoding: Log late-Qing quota multiplied by Post=1 in 1905 and 1906, controlling log 1880 population multiplied by Post; supplementary IVs use normalized small rivers and short-run pre-1425 exam-performance changes
  comparison: High-quota vs low-quota prefectures; pre-1905 vs post-1905
  empirical_design: Prefecture-year linear probability DID; prefecture-month Alliance and Guangdong county panels are separate robustness designs, while 1911 uprising incidence is cross-sectional
  assumptions:
  - Conditional parallel trends in revolutionary participation across quota exposures
  - For supplementary IVs, no direct differential post-abolition effects outside quota exposure
  threats_addressed:
  - quota endogeneity examined using two alternative instruments and placebo tests, not proven absent
  - concurrent reforms via prefecture-level controls and timing analysis
  - spatial spillovers via geographic controls
  evidence_refs:
  - E1
readiness_blockers:
- Collate the digital edict reproduction with an original archive image or authoritative critical edition before detailed historical quotation; uniform compliance is not established by the edict.
- Recover quota tables, origin-county-to-prefecture crosswalk and executable replication code, including missing membership records and monthly sample restrictions.
- For IV replication recover river-network provenance, segmentation, precise small-river definition and both instrument construction scripts. Instrument diagnostics do not establish exclusion for a new outcome.
method_transfer: null
---
## Institutional Background
[E1, inspected paper report] The entry examination governed admission to the
lower gentry, with opportunities beyond holding government office. Its licensing
exam was held twice every three years, not an annual allocation of degrees. County
quotas and a shared prefecture quota constrained success at this entry stage.
The paper uses late-Qing quotas stable during 1873-1904 and checks earlier quotas;
the Taiping-era revision prevents describing them as unchanged for centuries.

## What Changed
[E2, inspected primary-text reproduction] The court ordered traditional
examinations stopped, promoted schools, and promised alternative arrangements
for existing degree holders. The change removed a particular recruitment and
status route; it did not abolish all education, all examinations or every possible
career. [E1, paper report] Accelerated abolition departed from an earlier gradual
reform plan. The institutional motivation and the disappointment of would-be
entrants are connected, but the paper does not observe every entrant's lost income.

## Implementation and Assignment
[E1-E2] National abolition supplies common timing, not a randomly chosen group
of prefectures. The quota measure proxies opportunities under the old institution;
there is no regional count of all exam takers. Keep announcement, cancelled exam
cycle and the paper's annual Post definition distinct. [E1, paper report] Small
rivers enter an additional IV comparison because geography helps explain county
formation and the aggregation of stepwise quotas. Exam-hall transport capacity
is not the published first-stage explanation.

## Why This Creates Empirical Variation
[Analytical inference] Places with different pre-existing access to elite status
may respond differently to removal of that access. The useful contrast is this
differential response, not the total national effect of abolition. [E1, paper
report] Population controls and fixed effects make the actual comparison
recoverable. Neither predetermined quotas nor statistically relevant instruments
make parallel trends or exclusion automatic.

## Identification Risks
[E1, paper report] The Alliance's establishment and the Russo-Japanese War
occurred close to abolition. Monthly variation and event/placebo comparisons
address timing concerns without proving that no concurrent channel remains.
Membership data record origins of identified participants, not necessarily where
their activities occurred. The separate 1911 uprising map cannot provide a
pre-post outcome panel. [Analytical inference] River geography has plausible
economic and administrative channels that must be reconsidered for any new use.
## Data Requirements

[E1, paper report] Link quotas and fixed 1880 population to revolutionary
membership by historical origin prefecture and joining year. The baseline
1900-1906 panel does not require ten pre years or five post years; those previously
listed requirements were unsupported. The 1905 Alliance monthly analysis needs
joining dates, while the Guangdong extension needs county identifiers and its
own sample. River and early jinshi data are additional IV inputs, not missing
fields that should disqualify the baseline design. Data-asset acquisition belongs
in the complementary repository with a DOI link.

## Evidence Notes

Task `task-60966e340c79` audits the existing record rather than creating another
case. E1 now has inspected published construction and precise evidence paths;
E2 independently exposes the abolition directive as a primary-text reproduction.
The paper's mechanism interpretation is attributed, not a verified fact about
every participant. Original archive collation, crosswalks and executable
reproduction remain conditions, so admission is grounded and conditional rather
than design-documented.
