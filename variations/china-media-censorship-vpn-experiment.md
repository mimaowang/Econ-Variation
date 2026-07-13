---
schema_version: 2
id: china-media-censorship-vpn-experiment
name: Field Experiment Providing Uncensored Internet Access via VPN to Chinese Citizens (2018–2019)
aliases:
- Media censorship China field experiment
- Chen Yang 1984 or Brave New World
- VPN experiment China
- 网络审查 VPN实验

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - Beijing
  - Shanghai
  domains:
  - media
  - political-economy
  - information
  - attitudes
  variation_type: pilot-assignment
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: An 18-month randomized field experiment providing free VPN access (and in one treatment arm, temporary financial
    incentives) to Chinese university students to study the causal effect of uncensored internet access on knowledge, beliefs,
    attitudes, and behaviors
  authority: Academic researchers (Chen and Yang, Peking University and Harvard)
  legal_identifiers: []
  implementation_regime: Participants at two elite Chinese universities were randomly assigned to receive free VPN access
    to uncensored internet; some also received small financial incentives to visit foreign news sites for current-events questions
  assignment_mechanism: Random assignment at the individual level; the experimental treatment arms are (1) free VPN access
    only, (2) free VPN access + temporary financial encouragement to consume foreign news
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 2018
  implementation_end: 2019
  local_timing: Treatment was administered continuously during the 18-month experiment
  anticipation: VPN access was provided at the start of the experiment; there was no subject-level anticipation
  last_verified: '2026-07-13'
assignment:
  unit: Individual (university student)
  treated: Students randomly assigned to receive free VPN access (and some also financial encouragement)
  comparison_pool: Students randomly assigned to the control group (no VPN access provided)
  rule: Random assignment via lottery
  intensity: Binary at first stage (VPN provided or not); encouragement arm provides additional financial incentive; actual
    treatment take-up varies (only ~50% used the VPN)
  compliance: Take-up was approximately 50% in the access-only arm, higher in the encouragement arm
  exposure_construction: Binary treatment indicator; continuous measure of actual VPN usage and foreign news consumption
  required_identifiers:
  - subject ID
  - treatment arm
  - university
  - baseline survey responses
  exemptions: []
  spillovers: Subjects may share uncensored information with peers in their social networks; the paper measures (and finds
    limited) social transmission
research_compatibility:
  outcome_domains:
  - political attitudes
  - government trust
  - knowledge
  - emigration intentions
  - media consumption
  - beliefs
  affected_populations:
  - Chinese university students
  - educated urban youth
  mechanism_channels:
  - access to uncensored information
  - demand for information
  - social transmission
  - belief updating
  best_for:
  - Studying causal effects of censorship on political attitudes
  - understanding demand for uncensored information
  - field experiments on media
  not_good_for:
  - General population effects (subjects are elite university students)
  - long-run societal effects of censorship removal
design:
  affordances:
  - random assignment of VPN access
  - within-subject pre/post measurement
  - financial encouragement variation
  candidate_designs:
  - randomized controlled trial with multiple arms
  - encouragement design
  - ITT and IV analysis
  identifying_variation: Random assignment of VPN access and financial encouragement to consume foreign news
  assumptions:
  - Random assignment is successful
  - no differential attrition
  - no Hawthorne effects contaminating long-run outcomes
  - the encouragement affects outcomes only through information acquisition
  diagnostics:
  - Baseline balance checks
  - attrition analysis
  - first-stage take-up rates
  - comparison of ITT and IV estimates
  primary_strategy: RCT with multiple treatment arms; encouragement design; ITT and LATE estimation
  estimand: The causal effect of the recorded exposure on Knowledge of censored news, political attitudes, government trust,
    emigration intentions, media consumption, conditional on the stated design assumptions.
  treatment_variable: Random assignment to free VPN access; encouragement arm adds financial incentive for visiting foreign
    news sites
  comparison_logic: Control group vs VPN-only vs VPN+encouragement
  estimation_notes: RCT with multiple treatment arms; encouragement design; ITT and LATE estimation
threats:
- type: limited-generalizability
  basis: documented
  condition: Subjects are students at two elite universities; they are not representative of the broader Chinese population
  evidence_refs:
  - E1
  possible_diagnostics:
  - report demographics
  - discuss external validity
  - compare with survey data on broader populations
- type: experimenter-demand-effects
  basis: inferred
  condition: Providing VPN access combined with survey questions about political attitudes may create demand effects
  evidence_refs:
  - E1
  possible_diagnostics:
  - use unobtrusive behavioral measures
  - compare with non-survey outcomes where possible
empirical_requirements:
  contract_version: 1
  population: Approximately 1,200 university students at two elite Chinese universities, 2018–2019
  observation_unit: Individual survey wave
  geography_level: Individual (Beijing and Shanghai)
  time_start: 2018
  time_end: 2019
  minimum_frequency: wave-based (baseline, midline, endline)
  minimum_pre_periods: 0
  minimum_post_periods: 2
  required_fields:
  - treatment assignment
  - VPN usage
  - foreign news consumption
  - political attitudes
  - knowledge
  - trust
  - emigration intentions
  required_identifiers:
  - subject ID
  - survey wave
  - treatment arm
  treatment_key:
  - subject ID
  - treatment arm indicator
  - encouragement indicator
  treatment_source: Experimental data collected by the authors; administrative data on VPN usage
  measurement_risks:
  - self-reported outcomes may be subject to social desirability bias
  - VPN usage measurement accuracy
  - survey attrition
evidence:
- id: E1
  source_type: paper
  citation: 'Chen, Yuyu, and David Y. Yang. 2019. "The Impact of Media Censorship: 1984 or Brave New World?" American Economic
    Review 109 (6): 2294–2332.'
  url: https://doi.org/10.1257/aer.20171765
  date: 2019
  supports:
  - identity
  - assignment
  - design
  - main results
  - mechanism analysis
  - social transmission analysis
  verification_status: verified
design_applications:
- paper: 'The Impact of Media Censorship: 1984 or Brave New World?'
  doi: 10.1257/aer.20171765
  journal: American Economic Review
  year: 2019
  research_question: Does providing access to uncensored internet change Chinese citizens' knowledge, beliefs, and political
    attitudes?
  population: ~1,200 university students at two elite Chinese universities, 18-month experiment
  outcome: Knowledge of censored news, political attitudes, government trust, emigration intentions, media consumption
  data_used: []
  treatment_encoding: Random assignment to free VPN access; encouragement arm adds financial incentive for visiting foreign
    news sites
  comparison: Control group vs VPN-only vs VPN+encouragement
  empirical_design: RCT with multiple treatment arms; encouragement design; ITT and LATE estimation
  assumptions:
  - random assignment successful
  - no differential attrition
  - encouragement exclusion restriction
  threats_addressed:
  - selection into information via random assignment
  - low take-up via encouragement design
  - social desirability via behavioral measures
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
---
## Institutional Background
China operates the world's most extensive internet censorship system (the "Great Firewall"), blocking access to foreign news sites and politically sensitive content. Whether this censorship shapes citizens' political attitudes — or whether citizens would voluntarily seek uncensored information given access — is a central question. [E1]

## What Changed
The experiment randomly provided a subset of students with VPN access to bypass the firewall. In the encouragement arm, students were paid small amounts ($1–3) to correctly answer current-events questions whose answers required visiting foreign news sites. This temporary nudge created persistent changes in information-seeking behavior. [E1]

## Implementation and Assignment
Random assignment ensures that treatment and control groups are comparable at baseline. The key finding: free access alone did not induce most students to seek uncensored information (only ~50% even tried the VPN). However, temporary encouragement produced persistent increases in information acquisition that lasted months after the incentives ended. [E1]

## Why This Creates Empirical Variation
Random assignment addresses the fundamental endogeneity problem: people who seek uncensored information are systematically different from those who do not. The experiment shows that censorship operates partly through supply restriction (the firewall) and partly through demand suppression (years of censorship shapes habits and preferences against seeking political information). [E1]

## Identification Risks
The subjects are elite university students, limiting external validity to the broader Chinese population. Survey-based outcome measures may be affected by social desirability bias in an authoritarian context. The experiment cannot estimate the general equilibrium effects of universal censorship removal. [E1; analytical inference]
## Data Requirements

Individual-level experimental data: treatment assignment, VPN usage logs, survey responses (baseline, midline, endline), incentivized current-events quiz responses, and administrative data on subject demographics. The key outcome variables are self-reported political attitudes, knowledge of censored events, and behavioral measures.[E1]

## Evidence Notes

E1 documents that free VPN access alone had little effect (low endogenous demand for uncensored information), but financial encouragement created persistent increases in information acquisition, and that acquiring uncensored information significantly changed political attitudes. The paper's title reflects the finding that censorship operates through both supply restriction (1984) and demand suppression (Brave New World).
