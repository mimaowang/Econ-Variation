---
schema_version: 2
id: china-political-connections-mortality
name: Political Connections and Worker Safety Compliance in Chinese Listed Firms
aliases:
- Mortality cost of political connections
- Fisman Wang political connections China
- 政治关联与工人安全

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - All China
  domains:
  - political-economy
  - labor
  - health
  - firm
  - regulation
  variation_type: other
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: Within-firm variation in the value of political connections driven by the unexpected death or serious illness
    of connected politicians, combined with cross-sectional variation in which firms have political ties
  authority: Not applicable — political connections are informal; the identifying variation comes from exogenous health shocks
    to connected officials
  legal_identifiers: []
  implementation_regime: Chinese listed firms form and maintain political connections through executives, board members, and
    ownership ties to government officials; regulatory enforcement of workplace safety standards is subject to political influence
  assignment_mechanism: Political connections are endogenously formed, but their value changes exogenously when connected
    politicians unexpectedly die or become seriously ill; this within-firm, over-time variation identifies the effect of connections
    on workplace safety compliance
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 2002
  implementation_end: 2012
  local_timing: Connected politicians die or become ill at unpredictable times; the shock is firm-specific and temporally
    staggered
  anticipation: Death and serious illness of politicians are largely unanticipated events; firms cannot perfectly prepare
    for the loss of political protection
  last_verified: '2026-07-13'
assignment:
  unit: Firm-year
  treated: Firm-year observations after the death or serious illness of a politically connected official
  comparison_pool: The same firm before the death/illness event; firms without political connections; firms whose connected
    politicians remain healthy
  rule: The value of political connection decreases when the connected politician dies or becomes seriously ill; the timing
    is driven by health shocks rather than firm decisions
  intensity: Binary — connected politician death or serious illness; the intensity varies with the importance of the specific
    politician
  exemptions: []
  compliance: Not applicable — political connections are not a formal policy
  exposure_construction: Code firm-year observations as "post-shock" if a connected politician has recently died or become
    seriously ill; identify political connections through board members, executives, and ownership records; compare within-firm
    changes in workplace fatalities and regulatory violations
  required_identifiers:
  - firm ID
  - year
  - political connection indicator
  - connected politician health/death status
  spillovers: When a connected politician dies, affected firms may be replaced in their protected position by other connected
    firms; the death may have broader political implications beyond the individual firm
research_compatibility:
  outcome_domains:
  - workplace fatalities
  - worker safety
  - regulatory violations
  - firm productivity
  - corruption
  affected_populations:
  - workers at politically connected firms
  - particularly in dangerous industries like mining and construction
  mechanism_channels:
  - regulatory enforcement avoidance
  - safety compliance reduction
  - political protection
  - corruption
  - regulatory capture
  best_for:
  - Studying the real costs of political connections through regulatory enforcement
  - within-firm designs exploiting exogenous connection-value changes
  not_good_for:
  - Outcomes unrelated to regulation or enforcement
  - short panels without sufficient health-shock events
design:
  affordances:
  - exogenous politician health shocks
  - within-firm pre/post comparison
  - cross-sectional variation in connection status
  candidate_designs:
  - difference-in-differences with firm fixed effects
  - event study around politician death/illness
  identifying_variation: Within-firm changes in workplace safety outcomes following the unexpected death or serious illness
    of politically connected officials
  assumptions:
  - Politician health shocks are exogenous to firm safety outcomes
  - no concurrent changes at the firm that coincide with health shocks
  - the effect runs from reduced connection value → reduced safety compliance → increased fatalities
  diagnostics:
  - Test for differential pre-trends before health shocks
  - compare with firms whose connected politicians remain healthy
  - examine alternative explanations (industry-wide trends
  - economic conditions)
  primary_strategy: Difference-in-differences with firm fixed effects; event study around politician death/illness; cross-sectional
    comparison of connected vs unconnected firms
  estimand: The causal effect of the recorded exposure on Workplace fatalities, regulatory violations for workplace safety,
    conditional on the stated design assumptions.
  treatment_variable: Interaction of pre-existing political connections with politician health shock (death/serious illness)
  comparison_logic: Within-firm changes after connected politician health shocks; between connected and unconnected firms
  estimation_notes: Difference-in-differences with firm fixed effects; event study around politician death/illness; cross-sectional
    comparison of connected vs unconnected firms
threats:
- type: endogenous-connection-formation
  basis: documented
  condition: Firms that choose to form political connections may be systematically different from unconnected firms
  evidence_refs:
  - E1
  possible_diagnostics:
  - within-firm analysis eliminates time-invariant firm characteristics
  - compare connected and unconnected firms' pre-treatment trends
- type: concurrent-changes
  basis: inferred
  condition: The death of a politician may coincide with other changes (industry policy, local economic shocks) that independently
    affect workplace safety
  evidence_refs:
  - E1
  possible_diagnostics:
  - use narrow windows around health shocks
  - compare with firms in different industries or regions
  - test for effects on placebo outcomes
empirical_requirements:
  contract_version: 1
  population: Chinese listed firms, approximately 2002–2012
  observation_unit: Firm-year
  geography_level: National (firm-level)
  time_start: 2002
  time_end: 2012
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields:
  - firm political connections
  - connected politician health/death data
  - workplace fatalities
  - regulatory violations
  - firm financial variables
  required_identifiers:
  - firm ID
  - year
  - political connection indicator
  treatment_key:
  - firm ID
  - year
  - connected politician death indicator
  treatment_source: Firm annual reports, CSMAR database, politician biographical data, workplace safety administrative records
  measurement_risks:
  - underreporting of workplace fatalities
  - political connection measurement error
  - politician health information availability
evidence:
- id: E1
  source_type: paper
  citation: 'Fisman, Raymond, and Yongxiang Wang. 2015. "The Mortality Cost of Political Connections." Review of Economic
    Studies 82 (4): 1346–1382.'
  url: https://doi.org/10.1093/restud/rdv020
  date: 2015
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - mechanism analysis
  verification_status: verified
design_applications:
- paper: The Mortality Cost of Political Connections
  doi: 10.1093/restud/rdv020
  journal: Review of Economic Studies
  year: 2015
  research_question: Do political connections allow firms to avoid safety compliance, and what are the mortality consequences?
  population: Chinese listed firms, ~2002–2012
  outcome: Workplace fatalities, regulatory violations for workplace safety
  data_used: []
  treatment_encoding: Interaction of pre-existing political connections with politician health shock (death/serious illness)
  comparison: Within-firm changes after connected politician health shocks; between connected and unconnected firms
  empirical_design: Difference-in-differences with firm fixed effects; event study around politician death/illness; cross-sectional
    comparison of connected vs unconnected firms
  assumptions:
  - health shocks exogenous
  - within-firm identification addresses selection
  - no other concurrent changes
  threats_addressed:
  - endogenous connections via within-firm design
  - confounding trends via narrow event windows
  - industry trends via controls
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
---
## Institutional Background
Political connections are pervasive in Chinese business. Firms with politically connected executives or board members may receive favorable regulatory treatment, access to credit, government contracts, and protection from enforcement actions. The flip side of this relationship is that politically protected firms may face weaker incentives to comply with costly regulations — including workplace safety standards. [E1]

## What Changed
When a politically connected official unexpectedly dies or becomes seriously ill, the value of the firm's political connection drops. This creates a within-firm shock: the same firm, before and after losing political protection, faces different regulatory enforcement regimes. [E1]

## Implementation and Assignment
The identifying variation comes from two sources: (1) cross-sectional — some firms have political connections and others do not; and (2) temporal — the value of connections changes exogenously when connected politicians die or fall ill. The key assumption is that politician health shocks are not caused by firm characteristics and do not coincide with other changes that independently affect workplace safety. [E1]

## Why This Creates Empirical Variation
The design exploits a natural experiment in the value of political connections. Death and serious illness are largely random from the firm's perspective and create plausibly exogenous variation in the protection that political connections provide. The within-firm estimator controls for all time-invariant differences between connected and unconnected firms. [E1]

## Identification Risks
Firms do not randomly acquire political connections — connected and unconnected firms differ systematically. While the within-firm design addresses time-invariant selection, it does not address the possibility that firms lose connections precisely when other things are changing. The paper addresses this by using narrow time windows around health shocks and by comparing different types of outcomes. [E1; analytical inference]

## Data Requirements
Firm-level data on political connections (board members, executives, ownership), politician biographical data including health and death information, firm-level workplace fatality and regulatory violation records, and standard firm financial variables. [E1]

## Evidence Notes
E1 documents that worker death rates at politically connected firms are 2–3 times higher than at unconnected firms, and that the effect operates through reduced safety compliance rather than reduced regulatory response after accidents occur. The finding implies a literal "mortality cost" of the political connection system.
