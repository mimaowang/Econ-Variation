---
schema_version: 2
id: china-nanchang-interfirm-network-meetings-randomization
name: Nanchang Randomized Interfirm Business Meetings
aliases: [Nanchang SME business-association experiment, China monthly manager network meetings, 南昌企业经理交流实验]
status: grounded
provenance:
  task_id: task-4466ef9ce2cd
scope:
  country: China
  regions: [Nanchang, Jiangxi]
  domains: [development-economics, urban-economics, regional-economics, firm-networks, industrial-organization]
  variation_type: other
  knowledge_role: china-variation
  china_relevance: >
    This is an implemented Chinese firm-level networking experiment, not a foreign
    method or city-wide policy rollout. It offers a local test of information and
    partnership frictions relevant to urban firm networks, without identifying
    the aggregate benefits of city size or agglomeration.
identity:
  instrument: Randomized invitation to a year of monthly business meetings for young firms
  authority: Jing Cai and Adam Szeidl in collaboration with Nanchang's Commission of Industry and Information Technology (CIIT)
  legal_identifiers: [AEARCTR-0001859, 'Trial registration DOI 10.1257/rct.1859-1.0; initially registered 2017-01-09']
  implementation_regime: Researcher-organized experimental business associations facilitated by CIIT; this is not a compulsory national regulation
  assignment_mechanism: >
    Firms in the recruited experimental sample receive a randomized invitation or
    no-meetings assignment. Group-composition, information-seeding and cross-group
    meeting randomizations are additional mechanisms, outside this record's main
    invitation-versus-control boundary.
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: '2013-08'
  implementation_end: '2014-08'
  local_timing: Summer 2013 recruitment and baseline; meetings from August 2013 for one year; follow-ups in summers 2014 and 2015. Registry intervention window is 2013-08-01 to 2014-08-31, not exact meeting dates for each group.
  anticipation: Invitation and willingness to participate precede allocation; baseline and invitation dates should be retained separately from the first meeting.
  last_verified: '2026-09-28'
assignment:
  unit: Firm, with managers participating in assigned meeting groups
  treated: Randomized invitation to regular meetings; use the final paper's 1,500 assigned firms, not a retrospective attendance threshold
  comparison_pool: Final paper's 1,320 no-meetings firms from the same recruited sample
  rule: Retain experimental invitation assignment; measure attendance separately. Registry documents firm-level size-and-industry stratified randomization, while peer composition has its own subregion-conditioned allocation.
  intensity: Binary invitation for the main intention-to-treat contrast; realised attendance is not itself randomized
  exemptions:
  - Nonresponders to recruitment and firms outside the site or recruitment cohort are outside the experimental estimand.
  - Do not replace the no-meetings comparison with all firms in Nanchang.
  compliance: J-PAL describes a certificate conditional on at least ten of twelve meetings; the paper also documents survey-linked certificates for controls. Keep assignment, attendance and certification separate.
  exposure_construction: Merge the experimental invitation indicator, assigned group and survey wave by stable firm identifier; retain assignment even for low attendance and analyse missing outcomes explicitly.
  required_identifiers: [Experimental firm identifier, Invitation assignment, Assigned group identifier, Survey wave, Baseline size and sector strata, Subregion where required]
  spillovers: Information or partnerships can spread beyond assigned groups; controls may interact with treated firms. Such contamination changes the contrast relative to no exposure anywhere.
research_compatibility:
  outcome_domains: [Revenue and profit, Employment and inputs, Business partnerships, Borrowing, Management practices]
  affected_populations: [Young SMEs willing to participate in business associations]
  mechanism_channels: [Learning from managers, Supplier-client matching, Trust formation]
  best_for: [Studying the effect of offering an organized local business-network program to interested young firms]
  not_good_for:
  - Estimating a representative China-wide firm effect or a city-wide agglomeration effect
  - Treating actual attendance or realised peer quality as unconditional random assignment
design:
  claim_type: causal
  affordances: [Randomized invitation, Baseline and two follow-ups, Assigned meeting groups]
  candidate_designs: [Invitation intention-to-treat by follow-up wave]
  identifying_variation: Random invitation among recruited firms supplies the main counterfactual; voluntary recruitment limits the population to which that counterfactual applies.
  primary_strategy: Firm fixed effects with invitation interacted with midline and endline indicators; preserve the experimental contrast rather than seeking a new observational policy control group
  estimand: Effect of the invitation package on recruited firms at the two follow-ups, not an attendance effect or a representative-city effect
  treatment_variable: Randomized meetings invitation indicator
  comparison_logic: Outcome changes of invited firms versus no-meetings firms from the experimental sample, with group-linked dependence and attrition treated explicitly
  estimation_notes: The paper clusters at meeting-group level for treated firms and firm level for controls. Firm-level allocation and correlated group-level outcomes are different issues.
  assumptions:
  - Allocation and outcome construction remain faithful to the experiment.
  - Differential missingness does not drive the estimated contrast.
  - Interpretation accounts for certificates, information interventions and cross-arm spillovers.
  diagnostics: [Baseline balance, Attrition and closure by arm, Assignment versus attendance, Survey versus book revenue, Cross-arm connections and concurrent interventions]
threats:
- type: Recruitment selection
  basis: reported
  condition: Interested participants differ from recruitment nonresponders; randomization within the sample does not remove that external-validity limit.
  evidence_refs: [E2, E3]
  possible_diagnostics: [Compare the sampled nonresponders to participants, State the recruited-population estimand]
- type: Treatment package
  basis: documented
  condition: Invitations combine organized contact with participation incentives; separating pure network contact from certificates requires additional evidence.
  evidence_refs: [E1, E2, E3]
  possible_diagnostics: [Retain certificate conditions by arm, Inspect government-service and funding channels]
- type: Different sample versions
  basis: documented
  condition: Registry and J-PAL counts are 2,800 with 1,480 invited; final paper counts are 2,820 with 1,500 invited. Neither the registry's final respondents nor summary counts define every paper regression sample.
  evidence_refs: [E1, E2, E3]
  possible_diagnostics: [Reconcile assignment and survey rosters with final analysis code before reproducing]
- type: Spillover and post-assignment participation
  basis: inferred
  condition: Conditioning on attendance selects a post-assignment outcome, while cross-arm information exchange can attenuate the invitation contrast.
  evidence_refs: [E1, E2]
  possible_diagnostics: [Use invitation ITT, Examine connections to other arms, Report attendance without replacing assignment]
empirical_requirements:
  contract_version: 1
  population: Recruited young firms in Nanchang's experiment
  observation_unit: Firm-survey wave
  geography_level: Experimental site and subregion; stable firm linkage is essential
  time_start: 2013
  time_end: 2015
  minimum_frequency: Baseline and summer follow-up waves with explicit outcome recall windows
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields: [Invitation indicator, Outcome and recall window, Baseline covariates, Response and closure flags, Attendance and other intervention flags]
  required_identifiers: [Firm ID, Group ID, Wave, Assignment strata and subregion where required]
  treatment_key: [Experimental firm ID]
  treatment_source: Experimental assignment roster and final analysis code, not a public city policy list
  measurement_risks:
  - Survey year and the accounting period recalled by respondents are not interchangeable.
  - Closure and nonresponse are different states; neither should automatically be coded zero revenue.
  - An ordinary commercial firm panel cannot recreate the experiment without its assignment identifiers.
evidence:
- id: E1
  source_type: archive
  citation: Cai, Jing, and Adam Szeidl. 2017. Interfirm Relationships and Business Performance. AEA RCT Registry, AEARCTR-0001859, DOI 10.1257/rct.1859-1.0.
  url: https://www.socialscienceregistry.org/trials/1859
  date: '2017-01-09'
  supports: [identity.instrument, identity.legal_identifiers, identity.assignment_mechanism, timeline.implementation_start, timeline.implementation_end, assignment.unit, assignment.rule, assignment.intensity, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Author-submitted registry HTML inspected via direct HTTP on 2026-09-28; intervention dates, experimental design, firm randomization unit, stratification, arm sizes and initial registration. Retrospective registration, not an ex-ante plan or independent assignment audit.
- id: E2
  source_type: implementation-document
  citation: J-PAL. Interfirm Relationships and Business Performance in China. Evaluation documentation naming CIIT as partner.
  url: https://www.povertyactionlab.org/evaluation/interfirm-relationships-and-business-performance-china
  date: null
  supports: [identity.authority, identity.implementation_regime, timeline.local_timing, assignment.compliance, research_compatibility.mechanism_channels, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Context of the evaluation and Details of the intervention; site, implementing partner, August 2013 first meetings and follow-ups. Institutional research-summary evidence, not a CIIT administrative order; summary sample counts differ from the final paper.
- id: E3
  source_type: paper
  citation: 'Cai, Jing, and Adam Szeidl. 2018. Interfirm Relationships and Business Performance. Quarterly Journal of Economics 133(3):1229-1282. DOI 10.1093/qje/qjx049.'
  url: https://doi.org/10.1093/qje/qjx049
  date: 2018
  supports: [assignment.treated, assignment.comparison_pool, assignment.required_identifiers, design.primary_strategy, design.estimation_notes, design_applications.population, design_applications.data_used, design_applications.empirical_design, threats.condition]
  verification_status: verified
  access_level: full-text
  locator: Open publisher HTML https://academic.oup.com/qje/article/133/3/1229/4768295; II.B-D and III.A(2), Tables I-II. Final allocation, additional experiments, survey population, selection, ITT equation and clustering inspected 2026-09-28.
- id: E4
  source_type: replication
  citation: 'Replication Data for Interfirm Relationships and Business Performance. Harvard Dataverse DOI 10.7910/DVN/5ZX8ZI; CEU research catalog entry.'
  url: https://research.ceu.edu/en/datasets/replication-data-for-interfirm-relationships-and-business-perform/
  date: '2017-12-11'
  supports: [empirical_requirements.treatment_source]
  verification_status: reported
  access_level: metadata
  locator: University catalog identifies the replication deposit and README; archive landing page was reachable but its API and file contents were not inspected. Existence of a deposit is not verification of variables or an executed reproduction.
design_applications:
- paper: Interfirm Relationships and Business Performance
  doi: 10.1093/qje/qjx049
  journal: Quarterly Journal of Economics
  year: 2018
  research_question: Do organized meetings improve firms' performance?
  population: Final paper's 2,820 firms; 1,500 invited and 1,320 controls
  outcome: Revenue, profits, inputs and partnerships
  data_used: [Experimental assignment and firm surveys in 2013, 2014 and 2015]
  treatment_encoding: Random invitation interacted with follow-up waves
  comparison: No-meetings experimental controls
  empirical_design: Firm fixed effects and wave-specific ITT, with treated meeting-group and control-firm clustering
  assumptions: [Valid allocation and comparable response, Interpretation includes the invitation package]
  threats_addressed: [Baseline balance, Attrition, Selection, Government-access channels]
  evidence_refs: [E3]
method_transfer: null
readiness_blockers:
- Replication file contents were not inspected; reconcile final assignment counts and variable names before executable reuse. Preserve the registry and J-PAL count discrepancy rather than silently replacing either source.
- Additional peer-composition, information-seeding and one-time cross-group assignments need separate resolved records if collected as distinct variations; they are not included in this record's main estimand.
---

## Institutional Background

[E1-E3] The implemented object is a deliberately created local business-network
program, not merely the existence of business associations. Firms' willingness to
join precedes allocation. Randomization therefore gives a comparison among
participants, not among every enterprise in the city.

## What Changed

Some sampled firms were offered organized repeated contact; others were not.
This binary offer is the record's boundary. Other interventions help study
mechanisms, but their assignment rules are not interchangeable with the offer.

## Implementation and Assignment

[E1, verified registry] Firm allocation is distinct from meeting-group dependence.
The registry was submitted in 2017, after the program, and cannot establish
preregistration. [E2-E3] Source sample versions differ. Use the final paper for its
own analysis sample without erasing the earlier documentation.

## Why This Creates Empirical Variation

[Analytical inference] The invitation contrast can inform research on local
information and matching frictions. It does not provide an existing shock for
an arbitrary city panel: without experimental firm identifiers, a researcher
cannot join its assignment to new outcomes.

## Identification Risks

Preserve the invitation package as the estimand. Attendance is a choice made after
assignment, and improved access to other participants is not necessarily the only
component. A new application must address spillovers, missing outcomes and
sample selection rather than inheriting validity from the word randomized.

## Data Requirements

Join the experimental roster to observations by firm, not simply by city-year.
Survey recall windows and closure status need explicit treatment. Peer analyses
would also need the separate conditional group allocation and its identifiers;
the primary offer record does not silently supply them.

## Evidence Notes

The original blocked candidate `candidate-215698fb2245` retains the history of the
earlier missing implementation evidence. [E1] The now-inspected author registry
provides primary experimental documentation; [E2] institutional evaluation notes
corroborate implementation. Neither is a government audit of randomization.
[E4, reported metadata] The replication deposit is a useful next source, not a
claim that its code has been inspected or successfully run.
