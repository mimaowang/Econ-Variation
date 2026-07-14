---
schema_version: 2
id: example-variation-case
name: Exact Variation Case Name
aliases: []
status: extracted
provenance:
  task_id: task-required
scope:
  country: China
  regions: []
  domains: []
  variation_type: other
  knowledge_role: china-variation # china-variation / global-china-variation / transferable-method
  china_relevance: Explain why this belongs in a China-focused research knowledge base.
identity:
  instrument:
  authority:
  legal_identifiers: []
  implementation_regime:
  assignment_mechanism:
  parent:
  related_variations: []
timeline:
  announcement:
  effective:
  implementation_start:
  implementation_end:
  local_timing:
  anticipation:
  last_verified: "YYYY-MM-DD"
assignment:
  unit:
  treated:
  comparison_pool:
  rule:
  intensity:
  exemptions: []
  compliance:
  exposure_construction:
  required_identifiers: []
  spillovers:
research_compatibility:
  outcome_domains: []
  affected_populations: []
  mechanism_channels: []
  best_for: []
  not_good_for: []
design:
  claim_type: # causal / reduced-form / structural / descriptive / method-pattern
  affordances: []
  candidate_designs: []
  identifying_variation:
  primary_strategy:
  estimand:
  treatment_variable:
  comparison_logic:
  estimation_notes:
  assumptions: []
  diagnostics: []
threats:
  - type:
    basis: inferred
    condition:
    evidence_refs: []
    possible_diagnostics: []
empirical_requirements:
  contract_version: 1
  population:
  observation_unit:
  geography_level:
  time_start:
  time_end:
  minimum_frequency:
  minimum_pre_periods: 0
  minimum_post_periods: 0
  required_fields: []
  required_identifiers: []
  treatment_key: []
  treatment_source:
  measurement_risks: []
design_profiles: [] # Optional alternatives; each profile supplies one coherent design-specific requirements contract.
evidence:
  - id: E1
    source_type: policy-document
    citation:
    url:
    date:
    supports: []
    verification_status: lead-only
    access_level: # metadata / abstract / full-text / appendix / replication / official-document / dataset
    locator: # page, section, table, article, or dataset location actually inspected
design_applications: []
method_transfer: # Must be null for China/global-China variation; required mapping for transferable-method.
readiness_blockers: []
superseded_by: # Deprecated redirects use a canonical record ID; otherwise leave null.
deprecation_reason: # Deprecated records without a replacement must explain why they are terminal.
---

## Institutional Background

Explain the pre-change institution, the economic or political pressure behind the change, and how this case fits the wider institutional system. Cite verified facts with `[E1]`, source-attributed statements with `[E2, reported claim]`, and the agent's own implications with `[analytical inference]`.

## What Changed

Explain the substantive change, affected actors, formal rule, implementation regime, phase-in, discretion, and exceptions.

## Implementation and Assignment

Explain how units become treated, when exposure begins, which comparison pool exists, how intensity or compliance varies, and how a researcher can encode treatment.

## Why This Creates Empirical Variation

Explain the assignment-generating feature and the conditional designs it may support. A design name alone is insufficient.

## Identification Risks

Explain endogenous adoption, anticipation, contemporaneous reforms, spillovers, sorting, measurement error, and other case-specific threats. Distinguish documented evidence, reported claims, and inference.

## Data Requirements

Translate the design into observable population, unit, geography, time, frequency, fields, identifiers, and treatment-source requirements. Do not duplicate dataset profiles.

## Evidence Notes

Explain conflicts, blocked sources, uncertain dates, or limits on what each source establishes.

<!--
For a non-China paper retained as transferable-method, replace method_transfer: null with:
method_transfer:
  source_context:
  strategy_family:
  reusable_logic:
  construction_steps: []
  source_treatment_or_endogenous_variable:
  source_instrument_or_assignment:
  first_stage_or_contrast:
  identifying_assumptions: []
  diagnostics: []
  china_use_cases: []
  china_data_requirements: []
  transfer_limits: []
Do not fully catalog the foreign policy unless its institutional details are necessary to understand the method.
-->
