---
schema_version: 2
id: china-citizen-appeals-environmental-governance
name: Nationwide Field Experiment on Citizen Participation in Environmental Governance through Pollution Appeals in China
aliases:
- Buntaine Greenstone He Liu Wang Zhang squeaky wheel
- China citizen appeals experiment

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - 294 prefectures across China
  domains:
  - environmental-economics
  - political-economy
  - public-economics
  - regulation
  variation_type: pilot-assignment
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: A nationwide field experiment that randomly assigned citizen appeals (public via social media or private via
    government hotline) against manufacturing firms violating pollution standards, creating exogenous variation in the type
    of citizen participation in environmental enforcement
  authority: Research team in partnership with local environmental protection bureaus (EPBs); the experiment randomized the
    routing of citizen complaints about pollution violations by firms
  legal_identifiers:
  - China Environmental Protection Law (2014 revision)
  - Ambient Air Quality Standards (GB 3095-2012)
  implementation_regime: The experiment was conducted across 294 prefectures, with citizen appeals randomly assigned to either
    public (social media) or private (government hotline) channels; the proportion of treated firms within each prefecture
    was also randomly varied
  assignment_mechanism: Random assignment of citizen appeals to public vs. private channels; random variation in the proportion
    of treated firms (10%, 25%, 50%, or 75%) at the prefecture level
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 2017
  implementation_end: 2019
  local_timing: The experiment was conducted over 2017–2019 with multiple waves of appeal assignments
  anticipation: No anticipation possible because appeals were randomly assigned after violations were detected; firms could
    not predict whether a citizen appeal would be made or through which channel
  last_verified: '2026-07-13'
assignment:
  unit: Firm
  treated: Firms assigned to receive citizen appeals (either public or private) after violating pollution standards
  comparison_pool: Firms in the same prefecture that were not assigned any citizen appeal (control group); variation across
    prefectures in the proportion of treated firms
  rule: Firms violating pollution standards were randomly assigned to either public appeal (via social media), private appeal
    (via government hotline), or no appeal (control); at the prefecture level, the fraction of violating firms receiving appeals
    was randomly varied
  intensity: Binary at the firm level (appeal or no appeal), with type of appeal (public vs. private) providing additional
    cross-cutting variation; prefecture-level treatment proportion varies from 10% to 75%
  compliance: High compliance; citizen appeals were executed as designed and regulators responded to assigned appeals
  exposure_construction: Code firms as treated if a citizen appeal was submitted against them; distinguish between public
    and private appeal types; use prefecture-level treatment proportion as an additional source of variation for indirect
    effects
  required_identifiers:
  - firm ID
  - prefecture code
  - appeal assignment
  - appeal type
  - violation date
  exemptions: []
  spillovers: The experiment was designed to test for spillovers through random variation in the prefecture-level proportion
    of treated firms, enabling estimation of general equilibrium effects on untreated firms within the same regulatory environment
research_compatibility:
  outcome_domains:
  - pollution emissions
  - environmental compliance
  - regulatory behavior
  - firm behavior
  - citizen participation
  - government accountability
  affected_populations:
  - Polluting manufacturing firms
  - local environmental regulators
  - citizens in polluted areas
  mechanism_channels:
  - regulatory attention channel
  - public pressure channel
  - reputation concerns
  - government accountability
  - avoidance of public unrest
  best_for:
  - Studying how different forms of citizen participation affect environmental enforcement
  - estimating direct and indirect effects of public appeals
  - understanding regulator response to public pressure
  not_good_for:
  - Outcomes not related to environmental enforcement
  - long-run structural changes
  - non-China contexts
  - variation across different institutional environments
design:
  affordances:
  - random assignment of appeals
  - variation in appeal type (public vs. private)
  - prefecture-level variation in treatment proportion
  - panel structure with multiple waves
  candidate_designs:
  - randomized controlled trial comparing public vs. private appeals
  - difference-in-differences
  - indirect effect estimation through variation in regional treatment intensity
  identifying_variation: Exogenous variation in whether a citizen appeal is submitted against a violating firm and through
    which channel (public vs. private), generated by random assignment; prefecture-level variation in the share of violating
    firms receiving appeals identifies spillover effects on untreated firms
  assumptions:
  - random assignment successfully balanced firm characteristics across treatment arms
  - no contamination across treatment arms within prefectures
  - regulators did not systematically alter behavior across prefectures based on treatment proportions
  diagnostics:
  - balance checks across treatment arms
  - manipulation checks on randomization
  - tests for selective attrition
  - tests for cross-prefecture spillovers
  primary_strategy: Multi-level randomized controlled trial with firm-level and prefecture-level randomization
  estimand: The causal effect of the recorded exposure on Firm-level pollution emissions, violation rates, regulator inspection
    frequency and enforcement actions, conditional on the stated design assumptions.
  treatment_variable: Binary indicator for any appeal assignment; separate indicators for public (social media) vs. private
    (hotline) appeal type; prefecture-level share of treated firms
  comparison_logic: Firms receiving public appeals vs. private appeals vs. no appeals; prefectures with different treatment
    proportions
  estimation_notes: Multi-level randomized controlled trial with firm-level and prefecture-level randomization
threats:
- type: non-compliance-with-assignment
  basis: documented
  condition: Citizen appeals may not have been executed exactly as assigned, or regulators may not have responded uniformly
    across treatment arms
  evidence_refs:
  - E1
  possible_diagnostics:
  - compliance checks on appeal execution
  - comparison of assigned vs. actual appeal type
  - regulator response audits
- type: spillovers
  basis: documented
  condition: Treatment effects on firms in the same prefecture may affect control firms through regulatory channel, labor
    market, or product market spillovers
  evidence_refs:
  - E1
  possible_diagnostics:
  - compare outcomes across prefectures with different treatment proportions
  - test for spillovers in outcomes of untreated firms
- type: hawthorne-effects
  basis: inferred
  condition: Firms or regulators may have altered behavior due to awareness of being studied, independent of the treatment
    itself
  evidence_refs:
  - E1
  possible_diagnostics:
  - compare to external administrative data not linked to the experiment
  - examine whether effects persist after experiment ends
empirical_requirements:
  contract_version: 1
  population: Polluting manufacturing firms and local environmental regulators in 294 Chinese prefectures
  observation_unit: Firm-wave or prefecture-wave
  geography_level: Prefecture
  time_start: 2017
  time_end: 2019
  minimum_frequency: wave-level (multiple waves over the study period)
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - firm ID
  - prefecture code
  - pollution emissions
  - violation status
  - appeal assignment
  - appeal type
  - firm characteristics
  required_identifiers:
  - firm ID
  - prefecture code
  - wave identifier
  treatment_key:
  - appeal assignment indicator
  - appeal type indicator
  - prefecture-level treatment proportion
  treatment_source: Experiment administrative records; pollution violation data from environmental protection bureaus; citizen
    appeal records from social media and government hotline platforms
  measurement_risks:
  - measurement error in emissions data
  - selective reporting of violations
  - attrition of firms from the sample over waves
  - regulator gaming of reported outcomes
evidence:
- id: E1
  source_type: paper
  citation: 'Buntaine, Mark T., Michael Greenstone, Guojun He, Mengdi Liu, Shaoda Wang, and Bing Zhang. 2024. "Does the Squeaky
    Wheel Get More Grease? The Direct and Indirect Effects of Citizen Participation on Environmental Governance in China."
    American Economic Review 114 (3): 815–850.'
  url: https://doi.org/10.1257/aer.20221215
  date: 2024
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - direct effects
  - indirect effects
  - spillover analysis
  - regulator behavior
  verification_status: verified
design_applications:
- paper: Does the Squeaky Wheel Get More Grease? The Direct and Indirect Effects of Citizen Participation on Environmental
    Governance in China
  doi: 10.1257/aer.20221215
  journal: American Economic Review
  year: 2024
  research_question: What are the direct and indirect effects of different forms of citizen participation (public vs. private
    appeals) on environmental governance outcomes in China?
  population: Polluting manufacturing firms and local regulators in 294 Chinese prefectures, 2017–2019
  outcome: Firm-level pollution emissions, violation rates, regulator inspection frequency and enforcement actions
  data_used: []
  treatment_encoding: Binary indicator for any appeal assignment; separate indicators for public (social media) vs. private
    (hotline) appeal type; prefecture-level share of treated firms
  comparison: Firms receiving public appeals vs. private appeals vs. no appeals; prefectures with different treatment proportions
  empirical_design: Multi-level randomized controlled trial with firm-level and prefecture-level randomization
  assumptions:
  - Random assignment ensures comparability across treatment arms
  - no interference between treatment arms within prefectures
  - regulators do not systematically compensate or adjust behavior across prefectures
  threats_addressed:
  - confounding via randomization
  - spillovers via prefecture-level randomization of treatment proportion
  - experimenter demand effects via comparison with administrative data
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
---
## Institutional Background

China's environmental enforcement system relies on local Environmental Protection Bureaus (EPBs) that monitor firm compliance with pollution standards. While citizens can report violations through official government hotlines and, increasingly, through social media platforms, the effectiveness of these channels in actually reducing pollution had not been causally established. The institutional setting creates a tension between EPBs' dual mandates of facilitating economic growth and enforcing environmental regulations. [E1]

## What Changed

The research team conducted a nationwide field experiment across 294 prefectures in China. When manufacturing firms were detected violating pollution standards, citizen appeals against those firms were randomly assigned to one of three arms: (1) public appeals via social media, (2) private appeals via the government hotline, or (3) no appeal (control group). Additionally, the proportion of violating firms receiving appeals within each prefecture was randomly varied (10%, 25%, 50%, or 75%) to identify general equilibrium effects. [E1]

## Implementation and Assignment

Assignment occurred at two levels. First, at the firm level, violating firms were randomly assigned to public appeal, private appeal, or control. Second, at the prefecture level, the share of violating firms receiving any appeal was randomly varied. This dual randomization allows identification of both the direct effect of appeals on targeted firms and the indirect (spillover) effects on untreated firms within the same regulatory environment. Appeals were implemented through existing citizen complaint channels (social media for public, government hotline for private). [E1]

## Why This Creates Empirical Variation

The random assignment of appeals across violating firms generates exogenous variation in whether a firm faces citizen pressure and through which channel. The prefecture-level randomization of treatment share creates additional variation that identifies general equilibrium effects—for example, whether regulators reallocate enforcement effort away from control firms when many firms are targeted. This design allows estimation of both the direct treatment effect on targeted firms and the spillover effects on untargeted firms within the same regulatory jurisdiction. [E1; analytical inference]

## Identification Risks

The experiment relies on the integrity of random assignment and the ability to prevent contamination across treatment arms. If regulators in high-treatment-proportion prefectures systematically altered their behavior across all firms (not just targeted ones), the estimated spillover effects could be confounded with regulatory responses to treatment intensity. Additionally, firms or regulators may have altered behavior due to awareness of being studied (Hawthorne effects), though the comparison with routine administrative data provides a check. [E1; analytical inference]

## Data Requirements

Firm-level panel data on pollution emissions and violation status from China's continuous emissions monitoring system; administrative records of citizen appeals through social media and government hotline platforms; environmental inspection and enforcement records from local EPBs; firm characteristics from administrative registration data. [E1]

## Evidence Notes

E1 reports that public appeals via social media substantially reduced violations and emissions, while private appeals via government hotline had more modest effects. Public appeals shifted regulators' focus from economic growth toward avoiding pollution-induced public unrest. The prefecture-level randomization of treatment proportion reveals that pollution reductions by treated firms were not offset by increases from control firms, indicating that the overall environmental improvement was not zero-sum. The paper provides one of the first causal estimates of how different citizen participation channels affect both targeted firms and the broader regulatory environment.
