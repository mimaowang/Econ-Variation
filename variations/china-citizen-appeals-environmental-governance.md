---
schema_version: 2
id: china-citizen-appeals-environmental-governance
name: Randomized Public and Private Pollution Appeals to Chinese CEMS Firms, 2020
aliases:
- Buntaine Greenstone He Liu Wang Zhang squeaky wheel
- China citizen appeals experiment
- 中国污染举报随机实验
status: design-documented
provenance:
  task_id: task-41ea678ac598
scope:
  country: China
  regions:
  - 333 mainland Chinese prefectures with CEMS-monitored firms in the paper's experimental frame
  domains:
  - environmental-economics
  - political-economy
  - public-economics
  - regulation
  variation_type: other
  knowledge_role: china-variation
  china_relevance: The research team randomly assigned appeal channels to mainland Chinese plants monitored by the Ministry of Ecology and Environment; these are actual China-based firm exposures, not an overseas method analogy.
identity:
  instrument: Research-team assignment of eligible CEMS plants to no research-team appeal, private appeal, or public Weibo appeal after a verified emissions-standard violation during May–December 2020.
  authority: The researchers and volunteer citizens recruited through three environmental NGOs assigned and filed the experimental appeals. Local ecology and environment bureaus received them through existing channels; they did not randomize or run the intervention [E1].
  legal_identifiers:
  - 环境保护部令第35号, 环境保护公众参与办法, effective 2015-09-01; authorizes citizen reporting and official response channels, not this experiment's randomization
  - 环发〔2013〕74号, 关于加强污染源环境监管信息公开工作的通知; public monitoring-information context
  - AEA RCT Registry AEARCTR-0005601; planned intervention, not proof of exact realized dates or counts
  implementation_regime: The paper's frame is 24,620 CEMS-monitored plants in 333 prefectures as of January 2020. The experiment ran 2020-05-06 to 2020-12-31. Research volunteers filed appeals only after daily violations were verified; ordinary government enforcement continued independently [E1, §III].
  assignment_mechanism: Firm-level randomization placed CEMS firms in control, private-appeal or public-Weibo-appeal arms. At a second level, 60% of prefectures were assigned 95% treated firms and 40% were assigned 70% treated firms; this saturation randomization tests spillovers [E1, §III.A].
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: '2020-05-06'
  implementation_end: '2020-12-31'
  local_timing: Assignment preceded the field period. Each day the team checked the previous 24 hours of CEMS readings; verified violations by treated firms triggered a scripted appeal, except repeat violations within a week. A small implementation pilot occurred in April 2020 [E1, §III.B].
  anticipation: Exact appeals followed violations and were not scheduled to firms in advance, but firms may have known public CEMS reporting and citizen-complaint channels already existed. The paper does not prove zero anticipation or zero independent complaints.
  last_verified: '2026-10-02'
assignment:
  unit: CEMS firm for the main assignment; prefecture for randomized treatment saturation; individual Weibo appeal for the visibility subexperiment
  treated: CEMS firms preassigned to one of the research team's private or public appeal arms. An actual appeal is filed only following a verified standard violation; assigned but nonviolating firms remain in their arm for intention-to-treat comparisons.
  comparison_pool: CEMS firms assigned no research-team appeal. For spillover analysis compare like-assigned firms across 95%-treated versus 70%-treated prefectures; other citizen complaints can occur in any arm.
  rule: The researchers randomize CEMS firms, not pollution-violation incidents, to control, private or public appeal arms. After a verified violation, volunteers use the assigned channel. The 2015 public-participation rule recognizes hotline and website reporting, but does not specify the experimental allocation [E1; E3].
  intensity: Roughly 1/7 of firms are control, 5/7 private and 1/7 public in the broad design; prefectures receive 70% or 95% treated saturation. Private subchannels include Weibo direct message, 12369 website/hotline and phone call to firm; half of public Weibo appeals receive extra likes/shares at the appeal level [E1, §III.A].
  compliance: The paper reports 2,941 filed appeals out of 5,366 verified violations during the experiment; remaining events include control-firm violations and repeated violations within a week. Filing does not guarantee a regulatory response; 1,161 formal responses were observed [E1, §III.B].
  exposure_construction: Join preassigned firm arm and prefecture saturation to CEMS firm identifiers and daily readings. Model broad-arm assignment interacted with post-2020-05-06 for daily violations and pollution; use appeal-level randomization only to compare boosted versus unboosted Weibo visibility among public appeals [E1, §§III–IV].
  required_identifiers:
  - CEMS firm identity or social credit code
  - prefecture code
  - randomized firm arm and prefecture saturation
  - daily timestamp and pollutant monitoring point
  - appeal event ID for actual filing and visibility subexperiment
  exemptions:
  - Plants outside the January 2020 CEMS frame are not in the experiment, even if locally polluting.
  - CEMS spikes from production shutdown or monitor malfunction were screened out before appeals; repeated violations within a week did not trigger a new appeal.
  spillovers: Prefecture saturation is randomized precisely to test whether extra appeals change enforcement or pollution at control firms or assigned but nonviolating firms. The paper does not find treated-firm reductions offset by control firms; that is an empirical finding, not a design assumption [E1, §§III.A, V].
research_compatibility:
  outcome_domains:
  - CEMS emissions concentrations and standards violations
  - ambient pollution
  - regulator responses to citizen appeals
  affected_populations:
  - CEMS-monitored mainland Chinese plants
  - local environmental regulators
  mechanism_channels:
  - private regulatory notice
  - public visibility and regulator responsiveness
  best_for:
  - Comparing the intention-to-treat effects of private and public citizen appeals on monitored plants
  - Testing within-prefecture spillovers through randomized treatment saturation
  - Studying whether experimentally boosted public visibility changes responses to Weibo appeals
  not_good_for:
  - Treating actual complaint receipt as randomly assigned among firms conditional on a post-assignment violation
  - Extrapolating to unmonitored plants or long-run industrial relocation
  - Interpreting existing complaint law as the experiment's assigning authority
design:
  claim_type: causal
  affordances:
  - Preassigned firm arms before subsequent violation-based appeal triggers
  - Randomized 70%-versus-95% prefecture treatment saturation
  - Appeal-level boosted-versus-unboosted Weibo visibility among public appeals
  candidate_designs:
  - Firm-arm intention-to-treat analysis using pre/post CEMS panel
  - Prefecture-saturation spillover analysis
  - Within-public-appeal visibility experiment for regulator responses
  identifying_variation: Firm assignment precedes violations and determines which channel is used if a verified violation occurs; prefecture assignment changes the fraction of firms eligible for appeals; half of filed public Weibo posts were separately randomized to boosted visibility [E1, §III].
  assumptions:
  - Firm-arm comparisons retain originally assigned firms, including those without violations or appeals.
  - Prefecture spillovers are estimated, not assumed absent.
  - Public-appeal visibility comparisons are limited to their randomized appeal-level population.
  diagnostics:
  - Paper Table 2 pre-treatment arm balance
  - Paper Tables 3 and 7 plus appendix robustness and pre-period patterns
  - CEMS mechanical-spike and production-stop screening
  primary_strategy: Multi-level randomized field experiment; daily firm-arm intention-to-treat estimates and separate prefecture-saturation and appeal-visibility contrasts [E1, §§III–VI].
  estimand: Effects of assignment to private or public appeal eligibility on monitored firms' daily violation and emission outcomes; separate saturation spillover and public-post visibility effects.
  treatment_variable: Firm private-arm × post and public-arm × post; randomized high-intensity prefecture × post; separately randomized Weibo like/share boost for response outcomes.
  comparison_logic: Preserve assigned control, private and public firm arms regardless of subsequent violations; compare 95% versus 70% prefectures for indirect effects, and boosted versus unboosted public posts for appeal response.
  estimation_notes: The main daily CEMS regressions use firm and day or province-by-day fixed effects, with two-way prefecture and week clustering [E1, §IV and Table 3]. A comparison of broad arms conditional on post-assignment violations would select on an affected outcome [E1, §III.A n.13].
threats:
- type: triggered-treatment-versus-assignment
  basis: documented
  condition: An appeal follows only a verified violation and at most once per firm within a week. Comparing appealed firms with unappealed firms or conditioning broad-arm response comparisons on subsequent violations loses the clean firm randomization [E1, §III.A n.13 and §III.B].
  evidence_refs: [E1]
  possible_diagnostics:
  - Retain original assigned denominator for firm-level ITT.
  - Tabulate verified violations, appeals filed and responses by arm.
- type: spillovers
  basis: documented
  condition: Regulators may shift attention to or away from untreated firms within a prefecture; the design deliberately varies treatment saturation to detect this [E1, §§III.A, VI].
  evidence_refs: [E1]
  possible_diagnostics:
  - Compare control-firm outcomes by randomized 95% versus 70% prefecture saturation.
- type: measurement-and-external-complaints
  basis: documented
  condition: CEMS readings can spike during shutdowns or monitor malfunctions; unrelated citizens also filed complaints in all arms [E1, §§III.B–D].
  evidence_refs: [E1]
  possible_diagnostics:
  - Recreate verification filters and examine daily flows alongside concentrations.
  - Separate research-team filings from MEE records of other citizens' appeals.
empirical_requirements:
  contract_version: 1
  population: The paper's 24,620 CEMS-monitored firms in 333 mainland Chinese prefectures as of January 2020; not all Chinese firms.
  observation_unit: Firm-day for primary CEMS outcomes; firm/appeal-event for complaint responses; prefecture-day or week for saturation and ambient pollution.
  geography_level: Firm and prefecture
  time_start: 2020
  time_end: 2020
  minimum_frequency: Daily for the primary CEMS outcomes
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - hourly or daily SO2/COD concentrations and firm-specific emission standards
  - gas/water flows and production-status indicators for false-positive screening
  - firm assigned arm, prefecture assigned saturation and experiment start date
  - verified violation dates, research-team appeal events, channel and formal responses
  required_identifiers:
  - CEMS firm ID or social credit code
  - prefecture code
  - observation date and pollutant/monitoring point
  - appeal event ID for appeal-level tests
  treatment_key:
  - preassigned firm control/private/public arm
  - prefecture 70%-or-95% assigned saturation
  - post-2020-05-06 indicator
  - randomized public-post boost for response subexperiment
  treatment_source: Research team's nonpublic randomization and appeal logs linked to MEE CEMS and citizen-appeal records by firm identifiers [E1, §III.D]. The public article documents the design but does not make raw assignment keys reconstructible from law or CEMS alone.
  measurement_risks:
  - CEMS false-positive spikes during production stoppage or monitor faults
  - Other citizens' appeals mistaken for research-team appeals
  - Post-assignment violation selection when estimating regulator response
evidence:
- id: E1
  source_type: paper
  citation: 'Buntaine, Mark T., Michael Greenstone, Guojun He, Mengdi Liu, Shaoda Wang, and Bing Zhang. 2024. "Does the Squeaky Wheel Get More Grease? The Direct and Indirect Effects of Citizen Participation on Environmental Governance in China." American Economic Review 114(3): 815–850. DOI 10.1257/aer.20221215. Author-hosted final manuscript.'
  url: https://www.sdwang.org/uploads/4/4/8/5/44856715/pollution_appeals_final.pdf
  date: '2024'
  supports: [identity.instrument, identity.authority, identity.implementation_regime, identity.assignment_mechanism, timeline.implementation_start, timeline.implementation_end, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.intensity, assignment.compliance, assignment.exposure_construction, assignment.spillovers, design.identifying_variation, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.population, empirical_requirements.observation_unit, empirical_requirements.required_fields, empirical_requirements.treatment_source, design_applications.data_used, design_applications.empirical_design]
  verification_status: verified
  access_level: full-text
  locator: '§III.A–D, PDF pp. 10–17, especially p. 14 field dates and verified-violation appeal trigger, p. 16 CEMS and registry joins; §IV, PDF pp. 17–20, firm-arm ITT; §VI, PDF pp. 24–27, saturation spillovers; Table 1, PDF pp. 40–41, sample/appeal counts. Inspected 2026-10-02. Reports realized design, unlike the registry’s planned dates.'
- id: E2
  source_type: archive
  citation: 'AEA RCT Registry, AEARCTR-0005601, "Citizen Participation and Government Accountability: Experimental Evidence from Environmental Complaints in China," registered before fieldwork.'
  url: https://www.socialscienceregistry.org/trials/5601
  date: '2020'
  supports: [identity.legal_identifiers, identity.assignment_mechanism, timeline.local_timing, assignment.rule]
  verification_status: verified
  access_level: metadata
  locator: 'Registry study overview and intervention/design fields, inspected 2026-10-02: intended firm/city double randomization and seven arms, planned 2020-04-13 start and 2021-05-01 end. These planned dates and sample are NOT substituted for realized 2020-05-06 to 2020-12-31 and 24,620 firms in E1.'
- id: E3
  source_type: policy-document
  citation: 'Ministry of Environmental Protection, 环境保护公众参与办法, Order No. 35, issued 2015-07-13, effective 2015-09-01.'
  url: https://www.mee.gov.cn/gzk/gz/202112/t20211211_963794.shtml
  date: '2015-07-13'
  supports: [identity.legal_identifiers, identity.implementation_regime, assignment.rule]
  verification_status: verified
  access_level: official-document
  locator: 'Articles 10–13 authorize citizens to report environmental violations through 12369, government websites and related channels and describe receipt, investigation and response; inspected 2026-10-02. Does not authorize or document the research randomization.'
- id: E4
  source_type: implementation-document
  citation: 'Ministry of Environmental Protection, 关于加强污染源环境监管信息公开工作的通知, 环发〔2013〕74号, 2013-07-12.'
  url: https://www.mee.gov.cn/gkml/hbb/bwj/201307/t20130717_255667.htm
  date: '2013-07-12'
  supports: [identity.legal_identifiers, identity.implementation_regime]
  verification_status: verified
  access_level: official-document
  locator: 'Notice on publication of pollution-source regulatory and monitoring information; inspected 2026-10-02. Background for publicly visible monitoring, not evidence of the study’s exact firm sample or appeal assignments.'
- id: E5
  source_type: appendix
  citation: 'Buntaine et al., AER 2024 online appendix and supplementary materials for DOI 10.1257/aer.20221215.'
  url: https://www.aeaweb.org/articles/materials/20362
  date: '2024'
  supports: [design.diagnostics, empirical_requirements.measurement_risks, design_applications.threats_addressed]
  verification_status: verified
  access_level: appendix
  locator: 'AEA article materials page linking online appendix; appendix Table A2 and A3 robustness and Appendix B violation-screening protocol; inspected 2026-10-02.'
- id: E6
  source_type: paper
  citation: 'American Economic Association, publication landing page for Buntaine et al., American Economic Review 114(3), 2024, DOI 10.1257/aer.20221215.'
  url: https://doi.org/10.1257/aer.20221215
  date: '2024'
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: 'Publisher bibliographic identity, title, authors, journal, year and DOI only; inspected 2026-10-02. Empirical details come from E1.'
design_applications:
- paper: Does the Squeaky Wheel Get More Grease? The Direct and Indirect Effects of Citizen Participation on Environmental
    Governance in China
  doi: 10.1257/aer.20221215
  journal: American Economic Review
  year: 2024
  research_question: Do private or public citizen appeals after observed standard violations reduce Chinese firms' emissions, and do appeals displace enforcement from other firms?
  population: 24,620 CEMS-monitored firms across 333 prefectures in the January 2020 frame; research appeals filed 2020-05-06 through 2020-12-31.
  outcome: Daily CEMS emission-standard violations and SO2/COD concentrations or emission amounts; regulator response to filed appeals; ambient pollution and control-firm outcomes for spillover analyses.
  data_used: [MEE CEMS hourly firm pollution and flow records, research-team firm assignments and filed-appeal/response logs, MEE records of all citizens' 2020 appeals, Ministry of Commerce firm-registration data linked by social credit code, national ambient-air monitoring data for spillover tests]
  treatment_encoding: Preassigned control/private/public firm arms interacted with post period; 95%- versus 70%-treated prefecture assignment; separately randomized like/share boost among public Weibo appeals.
  comparison: All preassigned private and public firms versus control regardless of later violations; high- versus lower-saturation prefectures for spillovers; boosted versus unboosted public posts for response.
  empirical_design: Multi-level randomized field experiment. Main daily firm ITT specifications include firm and day or province-by-day fixed effects; separate saturation and visibility analyses.
  assumptions:
  - Assigned firm groups are comparable before treatment, assessed in Table 2.
  - Post-assignment violation status is not conditioned on when comparing broad firm arms.
  - Within-prefecture interference is investigated via randomized saturation, not ruled out by assumption.
  threats_addressed:
  - Baseline imbalance using reported balance tests
  - CEMS false-positive violations through blinded manual screening and appendix robustness
  - Control-firm displacement using randomized prefecture saturation
  - Other-citizen complaints using separate MEE administrative records
  evidence_refs: [E1, E2, E3, E4, E5, E6]
readiness_blockers: []
method_transfer: null
---
## Institutional Background

Chinese CEMS plants' emissions were observable in near-real time, and citizens already had routes to report apparent violations. The 2015 participation rule explains why a private complaint to the 12369 system could reach an official; it did not create the paper's experimental assignments. This is a research-team intervention embedded in existing monitoring and complaint institutions, not a rollout of a new government policy [E1; E3; E4].

## What Changed

Before the May–December 2020 field period, the researchers randomly assigned firms in a 24,620-plant, 333-prefecture CEMS frame to no research appeal, a private appeal channel, or a public Weibo appeal channel. Volunteers filed appeals only when a treated firm subsequently had a verified violation. A separate prefecture assignment made either 70% or 95% of firms eligible for treatment; a further randomization boosted visibility for half of public Weibo appeals [E1, §III and Table 1; E2 records the earlier plan].

## Implementation and Assignment

The private treatment was not just a hotline: it included Weibo direct messages to regulators, the 12369 website and hotline, and calls to firms. The researchers screened daily CEMS breaches and excluded apparent shutdown or monitoring artifacts before volunteers filed. Of 5,366 verified violations, 2,941 generated research-team appeals; control firms and repeat violations within a week account for the remainder. The published end date and realized counts supersede the registry's proposed schedule [E1, §III and Table 1; E2].

## Why This Creates Empirical Variation

The clean firm comparison is assignment to an appeal channel, not whether an appeal happened: an appeal requires a later violation, which the earlier assignment itself can affect. Daily firm outcomes therefore retain the originally assigned denominator. Random saturation offers a separate test of spillovers onto control firms, while boosted-versus-unboosted public posts isolate how visibility affects regulator response among those posts. These are three related but distinct estimands [E1, §§III–VI].

## Identification Risks

Existing complaints by other citizens could reach any firm, so the control group means no *research-team* appeal, not no complaint. Spillovers across firms are a measured possibility, not a violation assumed away. The paper explicitly warns that broad-arm comparisons of regulator response conditional on a later violation are selected; only the appeal-level visibility contrast remains randomized for that question. CEMS errors and shutdown spikes also require the documented screening protocol [E1, §III.A n.13, §§III.B–D].

## Data Requirements

Reproduction needs the preassigned firm and prefecture keys, research appeal/boost logs, MEE CEMS hourly readings and standards joined by firm ID or social credit code, and dates. The paper also links MEE records of other citizens' complaints and Ministry of Commerce registration data; ambient air monitors support a separate spillover test. The first ten 2020 CEMS weeks are excluded for COVID shutdowns. The published paper identifies these inputs but does not itself expose the firm-level randomization keys, so an independent researcher must obtain authorized experimental records to replicate the exact treatment variable [E1, §III.D].

## Evidence Notes

The paper finds larger reductions under public than private appeal assignment and no evidence that control-firm emissions offset treated-firm gains. Its explanation that publicity redirects regulator incentives is an interpretation supported by the visibility experiment and other tests, not a directly observed change in an official's objective. E3–E4 establish the preexisting reporting and information regime; E2 preserves what was planned; E1 establishes what the researchers actually did. The distinction matters whenever this record is used to design new research [E1–E5].
