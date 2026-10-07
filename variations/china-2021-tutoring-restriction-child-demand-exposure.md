---
schema_version: 2
id: china-2021-tutoring-restriction-child-demand-exposure
name: China's2021 tutoring restriction with baseline city child-demand exposure
aliases: [双减学科培训限制, Double Reduction firm dynamics, Huang-Liu-Ma-Yang tutoring restriction]
status: grounded
provenance:
  task_id: task-e45281b8cd16
scope:
  country: China
  regions: [Mainland cities and their education-service businesses]
  domains: [firm, industrial-economics, regional-economics, education-services]
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: A national restriction changes mainland academic tutoring businesses' permissible organization and operation. The paper uses predetermined city child population as differential demand exposure to study firm entry/cancellation and recruitment, not exam performance or a financial-market shock.
identity:
  instrument: The2021 national Double Reduction regime restricts approval, profit organization and operating times of academic off-campus tutoring, while expanding in-school support.
  authority: CPC Central Committee General Office and State Council General Office; education and other designated departments and local authorities implement the rules.
  legal_identifiers: [关于进一步减轻义务教育阶段学生作业负担和校外培训负担的意见]
  implementation_regime: Nationwide academic-training governance under Clauses13–15 and22 coexists with additional pilots under23–26. Compulsory-education academic institutions face halted new approvals and nonprofit registration. Preschool and high-school training have additional provisions in the closing paragraph. Nonacademic training remains subject to classification/approval rather than being automatically exempt from all regulation.
  assignment_mechanism: Legal exposure follows business activity and student stage under the national regime, not a city child-count cutoff. The paper constructs continuous city demand exposure from2020 census children aged5–14 interacted with the national post period; larger child populations proxy a larger affected customer base. The nine named pilot cities are not its treatment group.
  parent: null
  related_variations: []
timeline:
  announcement: '2021-07-24'
  effective: null
  implementation_start: 2021
  implementation_end: null
  local_timing: National text was published July24; local conversion, approval reviews and monitoring unfold afterwards. Section5.1 assigns post from August2021, with July not in the baseline treated period. Verify whether July is retained as pre or omitted in executable code before replication. This common research clock is not proof of simultaneous firm closure.
  anticipation: The paper documents market responses around May2021 and reports an alternative May clock. The national package also changes school-side services; anticipation and these demand changes belong to the interpretation, not an assumption of a perfectly isolated surprise.
  last_verified: '2026-10-07'
assignment:
  unit: City-month outcomes aggregated from firm registrations or recruitment records.
  treated: Cities have continuous exposure equal to their fixed2020 census children aged5–14, in thousands, interacted with the post period; within cities academic tutoring businesses are the directly restricted activity.
  comparison_pool: Lower-child-population cities provide a lower-intensity contrast under the same national policy. No city is legally untreated by the national regime. Arts/sports and other tutoring categories support spillover analyses, not automatically unexposed controls.
  rule: Match2020 census age5–14 child counts to stable city identifiers; define exposure=children/1000 and multiply by the policy indicator after July2021. Classify business outcomes separately from this city exposure. Legal restrictions are established by national Clauses13–15, not by the exposure proxy.
  intensity: Absolute baseline child count, not child share, actual tutoring enrollment, enforcement intensity or a legal eligibility threshold. A coefficient per1000 children must be multiplied by10 to discuss10000-child exposure.
  exemptions: [Arts sports and other nonacademic activities are not the same academic-training target but face approval standards and spillovers, Adult vocational and examination preparation are separate business categories, Closing policy paragraph separately governs preschool and ordinary-high-school training, Nine-city pilot enhancements do not define the nationwide baseline contrast]
  compliance: Nonprofit conversion or altered business scope is not necessarily economic exit; cancellation records miss businesses that stop operating without deregistration. National duties do not establish each firm's approval or conversion date.
  exposure_construction: Aggregate newly registered and cancelled education-service entities, including branches/subsidiaries, by city and month; join fixed2020 census children and city-month COVID cases. Preserve business names/scopes and a documented classification dictionary. Match city geography consistently and distinguish parent firms from establishments; ownership links are needed only for the separate entrepreneur/spillover application.
  required_identifiers: [city_id, year_month, firm_or_branch_id, registration_date, cancellation_date]
  spillovers: Untargeted arts/sports businesses show reported declines and share owners with academic tutors. School after-service expansion and customer substitution also change demand, so a sector difference is not a clean restriction-only effect.
research_compatibility:
  outcome_domains: [firm entry, firm cancellation, net registrations, recruitment vacancies]
  affected_populations: [education-service businesses and their branches, cities with different baseline tutoring demand]
  mechanism_channels: [restriction of commercial academic tutoring, organizational conversion and exit, customer-demand contraction, shared-ownership spillovers]
  best_for: [firm dynamics under restrictive industry regulation, city-demand exposure to national sector policy, spillovers across related service activities]
  not_good_for: [nine-city pilot DID, all tutoring businesses legally banned, observed layoffs inferred from vacancies, compulsory-education eligibility inferred directly from age5–14 counts, direct effect on exam scores, pure enforcement intensity from child population]
design:
  claim_type: reduced-form
  affordances: [national-post by predetermined-demand interaction, city-month continuous-exposure event study]
  candidate_designs: [continuous-exposure DID, demand-gradient event study]
  identifying_variation: After a common national policy, firm dynamics change differentially across cities with higher versus lower baseline child demand.
  primary_strategy: Section5.1 Eq1 uses post times2020 city child counts, city and year-month effects, city-calendar-month seasonality effects and city-month confirmed COVID cases. Eq2 interacts exposure with each year-month and normalizes June2021. Outcomes are levels rather than log transforms.
  estimand: Differential monthly business response per additional1000 baseline children under conditional common trends. It is an exposure-gradient reduced form of the national package, not the average nationwide effect from a legally untreated group.
  treatment_variable: Fixed2020 city children aged5–14 divided by1000 times post after July2021.
  comparison_logic: Higher-demand and lower-demand cities must have comparable untreated changes after conditioning on fixed effects and COVID cases. Absolute child counts also track city size, education markets and urban development; being predetermined does not make them random.
  estimation_notes: Table6 uses28008 observations for registration outcomes; job-posting Table3 uses23720. Table notes do not specify the standard-error clustering level, so recover code or final supplement before relying on nominal significance. A Table6 all-education coefficient−0.0394 per1000 children implies−0.394 registrations per10000-child increment, not a national50percent causal decline. Descriptive percentages, regression gradients and nationwide extrapolations are different objects. Main recruitment counts impute one opening when an advertisement lacks the number; advertisement-count robustness is separate.
  assumptions: [conditional exposure-gradient parallel trends, stable child and city coding, no child-count-correlated contemporaneous shock left uncontrolled, consistent industry dictionary and observation coverage, interpretable registration versus economic activity]
  diagnostics: [June2021-normalized event study, May anticipation and July inclusion clocks, baseline industry-scale and log-child exposure alternatives, advertisement versus recruitment counts, overall labor-market outcomes, through2021 registry restriction for COVID sensitivity, city-size and pilot-status sensitivity, city-level dependence-aware inference]
threats:
  - type: population-scale-exposure
    basis: documented
    condition: Absolute child count correlates with city scale and prepolicy education-industry size. The paper reports alternative proxies, but these do not create random assignment or guarantee comparable trends.
    evidence_refs: [E1]
    possible_diagnostics: [inspect exposure alternatives and support, size-conditioned trends, levels versus shares without silently changing the estimand]
  - type: bundled-national-policy
    basis: documented
    condition: School services and national business restrictions change together, with additional pilot measures and local execution. A national post interaction does not isolate each regulatory lever.
    evidence_refs: [E1, E2]
    possible_diagnostics: [pilot-status interactions, local implementation histories, separate direct activity and demand-substitution interpretation]
  - type: outcome-measurement
    basis: documented
    condition: Vacancies are not realized employment or layoffs; cancellations miss business pivots and informal cessation. Branch/subsidiary registrations are not one-to-one distinct enterprises.
    evidence_refs: [E1]
    possible_diagnostics: [advertisement-count sensitivity, observed employment if available, scope changes and branch consolidation, cancellation versus operational status]
  - type: spillovers-and-anticipation
    basis: documented
    condition: May expectations and cross-business ownership connections precede or transmit exposure. Nonacademic services can respond despite not being the direct legal target.
    evidence_refs: [E1, E2]
    possible_diagnostics: [alternative policy clocks, ownership-linked outcome classification, avoid nonacademic controls assumed untouched]
empirical_requirements:
  contract_version: 1
  population: Education-service entities and branches in mainland cities; default contract serves registration dynamics aggregated to city-month, not individual child or household outcomes.
  observation_unit: city-month
  geography_level: Mainland city matched to2020 census geography.
  time_start: 2016
  time_end: 2022
  minimum_frequency: monthly
  minimum_pre_periods: 12
  minimum_post_periods: 4
  required_fields: [2020 census children ages5–14, firm business names and scopes, registration and cancellation status/dates, branch or subsidiary flag, monthly city COVID cases, documented education-subtype dictionary]
  required_identifiers: [city_id, year_month, firm_or_branch_id]
  treatment_key: [city_id, baseline2020 child count, year_month]
  treatment_source: National July24 text verifies restricted business activities; published Eq1 defines continuous child-demand exposure and post. Census city identifiers must match the outcome geography.
  measurement_risks: [absolute child population versus share, student-stage versus census age bins, branch versus firm counts, dictionary changes and scope pivots, delayed cancellations, city boundary matching]
evidence:
  - id: E1
    source_type: paper
    citation: 'Huang, Zibin, Yinan Liu, Mingming Ma and Leo Yang Yang.2025. Biting the hand that teaches: Unraveling the economic impact of banning private tutoring in China. Journal of Comparative Economics53:954–976. DOI10.1016/j.jce.2025.07.002.'
    url: https://doi.org/10.1016/j.jce.2025.07.002
    date: 2025
    supports: [identity.assignment_mechanism, timeline.local_timing, timeline.anticipation, assignment.rule, assignment.intensity, assignment.comparison_pool, assignment.exposure_construction, assignment.spillovers, design.primary_strategy, design.estimand, design.estimation_notes, empirical_requirements.population, design_applications.empirical_design]
    verification_status: verified
    access_level: full-text
    locator: 'Actual23-page final author PDF https://www.zibinhuang.com/_files/ugd/b5c11e_dad268f2842549bfb7563d01c0f81f3d.pdf read in memory: pp957–959 Sections2.3/3;962–967 Sections5.1–5.4 Tables3–8;971–973 spillovers, owners and robustness;974 extrapolation; footnotes8,10,11–15. Figure captions, not visual coefficient plots, inspected. Final supplement/code not inspected.'
  - id: E2
    source_type: policy-document
    citation: 中共中央办公厅、国务院办公厅关于进一步减轻义务教育阶段学生作业负担和校外培训负担的意见, July24,2021 official full publication.
    url: https://www.gov.cn/zhengce/2021-07/24/content_5627132.htm
    date: '2021-07-24'
    supports: [identity.instrument, identity.authority, identity.implementation_regime, timeline.announcement, timeline.implementation_start, assignment.rule, assignment.exemptions, assignment.compliance, assignment.spillovers]
    verification_status: verified
    access_level: official-document
    locator: 'Actual government full body read: Clauses9–12 school services,13–15 national approval/nonprofit/operation restrictions,22 advertisements,23–26 nine-city pilot enhancements,27–30 administration and closing preschool/high-school provisions. Confirms legal activity exposure, not a statutory child-count rule. MOE endpoint403 replaced with government full text.'
design_applications:
  - paper: 'Biting the hand that teaches: Unraveling the economic impact of banning private tutoring in China'
    doi: 10.1016/j.jce.2025.07.002
    journal: Journal of Comparative Economics
    year: 2025
    research_question: How does restrictive academic-tutoring regulation change education-service business entry and cancellation across demand-exposed cities?
    population: Mainland education-service firms and branches aggregated by city/month,2016–2022 registration analysis.
    outcome: Levels of firm entry, cancellation, net entry and active registrations; recruitment is a separate outcome/data application.
    data_used: [Tianyancha registration histories and scopes,2020 population census city child counts, city-month COVID cases]
    treatment_encoding: Post after July2021 times city2020 children aged5–14 in thousands; national activity restrictions and pilot enhancements remain separate.
    comparison: Lower versus higher continuous city exposure, not cities legally outside the policy.
    empirical_design: Continuous-exposure city/month DID and annual-month interactions with June2021 base; city, year-month and city-calendar-month effects.
    assumptions: [conditional gradient trends, valid baseline exposure and city joins, stable classified outcomes, no remaining correlated contemporary shocks]
    threats_addressed: [event-study diagnostics, reported anticipation and July clocks, alternative exposure measures, reported COVID and noneducation checks]
    evidence_refs: [E1, E2]
method_transfer: null
readiness_blockers:
  - Obtain lawful registration data and the authors' final classification dictionary, sample city list and code; verify July handling and inference. Main method is recoverable but exact replication is not certified. The2024 author draft has different appendix labels/results and is not the final supplement.
  - Census age5–14 is a demand proxy, not an exact legal student-stage roster. Check city boundaries, size-dependent counterfactual trends, local/pilot implementation and contemporaneous COVID restrictions for the new question.
  - Default contract is firm registration dynamics. Recruitment use additionally requires platform deduplication, dates, city, business classification and openings versus ads; missing openings are imputed one in the paper. Later2022–2025 recruitment sources are not directly comparable. Neither source directly establishes layoffs or realized employment.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

The national package combines school-side support with restrictions on commercial
academic training. Clause13 halts new compulsory-education academic institutions,
requires nonprofit registration and restricts capitalization; nonacademic services
instead receive category-specific approval standards [E2]. This is not a ban on
every business called education or training.

## What Changed

Published July24,2021, the national duties apply beyond the nine named pilot cities.
Clauses23–26 designate extra experiments; using those cities as the paper's treated
group would change its design [E2]. The paper's common post clock begins after July,
while actual local organizational conversion and closure need their own dates [E1,
reported claim].

## Implementation and Assignment

The law assigns restrictions through activities and student stage. The study uses
a different empirical bridge: city2020 children aged5–14 in thousands proxy baseline
demand and interact with post [E1, reported claim]. This continuous gradient connects
the national change to regional business responses, without creating legally
untreated cities or a child-population threshold.

## Why This Creates Empirical Variation

With city, year-month and city-calendar-month effects, the comparison asks whether
higher-demand cities' business dynamics change more after the package. It requires
conditional common trends in that gradient, not merely prepolicy measurement of
children. The reported event study uses June2021 as base [E1, reported claim].

## Identification Risks

Child counts also reflect city size and economic conditions. School provision,
local execution, COVID restrictions and business connections can produce different
responses across cities. Arts/sports businesses are reported to experience spillovers,
so they are not automatically unaffected controls [E1; E2]. Insignificant leads and
alternative exposure proxies do not by themselves resolve these concerns
[analytical inference].

## Data Requirements

Join city-month registrations to fixed census demand and preserve business scope,
dates and branch status. Registrations and cancellations measure recorded entity
dynamics, not every operating firm's birth or death [E1, reported claim]. For a
recruitment question use the separate platform data contract, not an artificial
requirement that every registry study also possess job advertisements.

## Evidence Notes

The final paper and full official text close the institution, baseline exposure
and firm-dynamics application. The final dictionary, sample crosswalk, executable
July handling and clustering still require recovery for exact replication. The
March2024 draft was inspected as a version check; its changed appendix numbering
and estimates are not silently imported. The national job-loss extrapolation is
based on recruitment counterfactuals, not individually observed layoffs [E1]. No
copyrighted PDF, platform records or personal ownership data is redistributed.
