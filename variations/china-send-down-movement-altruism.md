---
schema_version: 2
id: china-send-down-movement-altruism
name: China's Mass Send-Down Movement as a Natural Experiment in Intrafamily Resource Allocation under Forced Separation (1968–1978)
aliases:
- Li Rosenzweig Zhang send-down altruism
- 上山下乡 家庭资源配置
- Sophies choice China
- send-down movement family allocation

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - Urban areas sending youth to rural areas; rural receiving areas
  domains:
  - family-economics
  - education
  - political-economy
  - altruism
  variation_type: event-shock
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: China's State-enforced Send-Down Movement (上山下乡, 1968–1978), during which approximately 17 million urban middle
    and high school graduates were required to relocate to rural areas for manual labor; the forced nature and specific timing
    of the movement create exogenous variation in which children left the household and which remained, revealing parental
    preferences over children
  authority: Chinese Communist Party (Mao Zedong's directive of 1968)
  legal_identifiers:
  - Mao's December 1968 directive
  - Go to the countryside and be re-educated by the peasants
  - local Revolutionary Committee implementation orders
  implementation_regime: Urban youth (primarily middle and high school graduates) were required to go to the countryside;
    in many families with multiple age-eligible children, parents could decide which child to send and which to keep (if any
    exemption was available), creating a "Sophie's Choice" setting that reveals parental favoritism
  assignment_mechanism: The policy was coercive and universal in urban areas, but families with multiple eligible children
    could influence which specific child was sent; the variation reveals how parents allocate opportunities (staying in the
    city, access to education) among children when forced to choose
  parent: null
  related_variations:
  - china-keju-abolition-elite-recruitment
  - china-one-child-policy-twins-iv
timeline:
  announcement: '1968-12-22'
  effective: '1968-12-22'
  implementation_start: 1968
  implementation_end: 1978
  local_timing: The movement was launched nationally in December 1968; implementation varied slightly by city but was uniformly
    enforced
  anticipation: The movement was announced suddenly in December 1968; there was no household-level anticipation of which specific
    children would be sent
  last_verified: '2026-07-13'
assignment:
  unit: Individual (child) and household
  treated: Children sent to the countryside (negative shock to education and urban opportunities); children kept in the city
    (positive selection for parental favoritism)
  comparison_pool: 'Within-family comparison: which child was sent vs which child was kept, conditional on number of age-eligible
    children'
  rule: The policy forced at least one child per family to relocate; for families with multiple eligible children, parental
    allocation of this burden reveals preferences (altruism, favoritism, guilt) over children
  intensity: Binary — sent vs not sent; intensity varies with the number of eligible children and number of children required
    to go
  compliance: The policy was coercive — essentially full compliance — but families could influence which specific child was
    sent
  exemptions: []
  exposure_construction: Construct indicators for whether a child was sent-down based on historical records and retrospective
    surveys; compare outcomes (education, earnings, marriage, health) of sent-down children to non-sent siblings and to pre/post-policy
    cohorts
  required_identifiers:
  - household ID
  - child ID
  - birth year
  - send-down indicator
  - sibling set
  spillovers: The absence of one child from the household affects resource allocation to remaining children; return migration
    after the policy ended creates additional variation
research_compatibility:
  outcome_domains:
  - education
  - earnings
  - health
  - marriage
  - intra-household allocation
  - altruism
  - parental favoritism
  affected_populations:
  - Sent-down youth (知青)
  - their siblings who stayed in cities
  - their parents
  - rural communities receiving sent-down youth
  mechanism_channels:
  - parental altruism and favoritism
  - interrupted education
  - rural labor experience
  - human capital loss
  - guilt and compensation
  - within-family resource allocation
  best_for:
  - Testing models of intra-household allocation under extreme constraints
  - studying the long-run effects of forced migration and interrupted education
  - understanding revealed preference in family decisions
  not_good_for:
  - Estimating the aggregate effects of the Cultural Revolution
  - studying rural receiving communities
  - cross-country comparisons of forced migration
design:
  affordances:
  - forced nature of the policy
  - within-family variation in which child is sent
  - sharp start and end dates
  - large-scale population affected (17 million)
  - rich retrospective survey data
  candidate_designs:
  - within-family difference in outcomes between sent and non-sent siblings
  - cohort comparison (pre-policy
  - during-policy
  - post-policy)
  - differences-in-differences across cities with different implementation intensity
  identifying_variation: Within-family variation in which child was sent-down, exploiting the forced nature of the policy
    at the household level but parental choice over which specific child
  assumptions:
  - The policy was binding at the household level (at least one child must go)
  - parental choice over which child to send reveals underlying preferences
  - the policy affects outcomes only through the forced relocation and not through other channels
  diagnostics:
  - Compare sent vs non-sent siblings within the same family
  - test for systematic differences between sent and non-sent children on pre-determined characteristics
  - compare with families where no choice was involved (only one eligible child)
  primary_strategy: Within-family fixed effects comparing sent and non-sent siblings; cohort analysis comparing affected and
    unaffected cohorts; structural estimation of parental preference parameters
  estimand: The causal effect of the recorded exposure on Educational attainment, earnings, health, marital outcomes of sent-down
    children vs non-sent siblings, conditional on the stated design assumptions.
  treatment_variable: Within-family indicator for which child was sent-down; comparison of outcomes between sent and non-sent
    siblings
  comparison_logic: 'Within-family: sent-down child vs non-sent sibling; between-family: families with choice (multiple eligible
    children) vs no-choice families (one eligible child)'
  estimation_notes: Within-family fixed effects comparing sent and non-sent siblings; cohort analysis comparing affected and
    unaffected cohorts; structural estimation of parental preference parameters
threats:
- type: selection-bias
  basis: documented
  condition: Within families, parents chose which child to send; if this choice was based on unobserved child characteristics
    that independently affect later-life outcomes, within-family comparisons may be biased
  evidence_refs:
  - E1
  possible_diagnostics:
  - test for pre-sending differences between sent and non-sent siblings
  - compare with families where choice was constrained (single-child families)
  - instrument using age-based eligibility rules
  - control for birth order and pre-existing health
- type: measurement-error
  basis: inferred
  condition: Retrospective data on send-down experiences may contain recall error; some aspects of the experience (duration,
    location quality) are measured imprecisely
  evidence_refs:
  - E1
  possible_diagnostics:
  - validate against administrative records where possible
  - test for systematic recall bias by current outcomes
  - use multiple survey waves
empirical_requirements:
  contract_version: 1
  population: Urban-born Chinese cohorts affected by the Send-Down Movement (born ~1948–1960), their siblings, and comparison
    cohorts
  observation_unit: Individual
  geography_level: National (urban-origin individuals)
  time_start: 1968
  time_end: 1978
  minimum_frequency: retrospective cross-section or longitudinal follow-up
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields:
  - birth year
  - sibling composition
  - send-down indicator
  - send-down duration
  - education
  - earnings
  - health
  - marital status
  - parental characteristics
  required_identifiers:
  - household/sibling group ID
  - individual ID
  - birth year
  - send-down indicator
  treatment_key:
  - send-down indicator
  - number of siblings sent
  - within-family send-down allocation
  treatment_source: Retrospective surveys (Chinese General Social Survey, China Family Panel Studies, urban household surveys
    with send-down history modules); historical records of send-down quotas by city
  measurement_risks:
  - recall error on exact dates and duration
  - selective mortality of sent-down cohort
  - incomplete enumeration of all siblings
  - migration after return complicates tracking
evidence:
- id: E1
  source_type: paper
  citation: 'Li, Hongbin, Mark R. Rosenzweig, and Junsen Zhang. 2010. "Altruism, Favoritism, and Guilt in the Allocation of
    Family Resources: Sophie''s Choice in Mao''s Mass Send-Down Movement." Journal of Political Economy 118 (1): 1–38.'
  url: https://doi.org/10.1086/650315
  date: 2010
  supports:
  - identity
  - assignment
  - design
  - altruism analysis
  - intra-household allocation
  - long-run outcomes
  verification_status: verified
design_applications:
- paper: 'Altruism, Favoritism, and Guilt in the Allocation of Family Resources: Sophie''s Choice in Mao''s Mass Send-Down
    Movement'
  doi: 10.1086/650315
  journal: Journal of Political Economy
  year: 2010
  research_question: Under extreme constraints, how do parents allocate burdens and opportunities among children, and what
    does this reveal about altruism, favoritism, and guilt?
  population: Urban Chinese families with children eligible for the Send-Down Movement, 1968–1978
  outcome: Educational attainment, earnings, health, marital outcomes of sent-down children vs non-sent siblings
  data_used: []
  treatment_encoding: Within-family indicator for which child was sent-down; comparison of outcomes between sent and non-sent
    siblings
  comparison: 'Within-family: sent-down child vs non-sent sibling; between-family: families with choice (multiple eligible
    children) vs no-choice families (one eligible child)'
  empirical_design: Within-family fixed effects comparing sent and non-sent siblings; cohort analysis comparing affected and
    unaffected cohorts; structural estimation of parental preference parameters
  assumptions:
  - within-family allocation reveals true parental preferences
  - pre-existing child differences are observable and controllable
  - no general equilibrium effects on non-sent children through changed urban conditions
  threats_addressed:
  - parental selection via within-family comparison
  - cohort effects via pre/post-policy comparisons
  - omitted child characteristics via sibling fixed effects
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
---
## Institutional Background
In December 1968, Mao Zedong issued the directive that "educated youth must go to the countryside to be re-educated by the poor and lower-middle peasants." This launched the largest forced urban-to-rural relocation in human history — the Send-Down Movement (上山下乡). Between 1968 and 1978, approximately 17 million urban middle and high school graduates were sent to rural areas, often to remote villages, for years of manual agricultural labor. The policy was coercive: urban families had little choice but to comply. [E1]

## What Changed
For urban families, the Send-Down Movement meant losing at least one child to the countryside, where they would lose access to education, urban amenities, and family support for years. Crucially, families with multiple age-eligible children could influence which specific child was sent. This created a "Sophie's Choice" — a forced decision that reveals deep parental preferences over children. The paper uses this variation to test models of altruism, favoritism, and guilt in family resource allocation. [E1]

## Implementation and Assignment
The policy specified that at least one child per urban household must go. Parents of multi-child families had to choose. This created two types of variation: (1) at the household level — some families were forced to send a child while exempt families were not; and (2) within the household — which child was sent versus kept. By comparing sent to non-sent siblings, the paper controls for all family-level confounds. [E1]

## Why This Creates Empirical Variation
The forced nature of the send-down decision at the household level, combined with parental discretion over which specific child to send, creates a unique setting for studying intra-household allocation. Unlike standard settings where parents allocate resources (money, food, education spending) among children, the Send-Down Movement forced parents to allocate a severe negative shock. This reveals whether parents equalize outcomes among children (altruism) or favor some children over others (favoritism). [E1; analytical inference]

## Identification Risks
The primary concern is that within-family allocation was not random — parents chose which child to send based on child characteristics that also affect later-life outcomes. The paper's within-family comparisons control for family-level factors but not for child-specific selection. The paper addresses this by examining pre-send-down differences between sent and non-sent children and by comparing choice-constrained families (one child) to choice families (multiple children). [E1]

## Data Requirements
Retrospective survey data with complete sibling histories including birth year, sex, birth order, send-down participation, send-down duration and location, post-send-down education, earnings, health, and marital status. Parental characteristics (education, occupation, political status) for understanding selection. Large sample sizes to identify within-family variation across sibling sets of different sizes. [E1]

## Evidence Notes
E1 finds evidence of both altruism and favoritism in parental allocation of the send-down burden. The paper provides structural estimates of parental preference parameters, finding that parents care about all children but also exhibit favoritism toward certain children (e.g., sons over daughters in some specifications). The paper also documents long-run consequences: sent-down children experienced permanently lower educational attainment and earnings decades after the policy ended, with some evidence of compensatory behavior (guilt) by parents toward sent-down children after their return.
