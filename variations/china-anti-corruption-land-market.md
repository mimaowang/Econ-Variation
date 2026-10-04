---
schema_version: 2
id: china-anti-corruption-land-market
name: China's 2012 Anti-Corruption Campaign Shock on Politically Connected Land Transactions
aliases:
- Busting the Princelings
- Xi Jinping anti-corruption land market
- 反腐运动 土地市场

status: contested
provenance:
  task_id: task-76b362e96ad9
scope:
  country: China
  regions:
  - All provinces
  domains:
  - political-economy
  - land
  - corruption
  - firm
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: Xi Jinping's anti-corruption campaign (2012–2016), specifically the staggered arrival of central inspection
    teams across provinces and the replacement of provincial party secretaries with Xi loyalists
  authority: Central Commission for Discipline Inspection (CCDI), CPC Central Committee
  legal_identifiers:
  - Eight-Point Regulation (2012)
  - Central Inspection Team institutionalization (2013–2016)
  implementation_regime: The anti-corruption campaign was implemented through rotating central inspection teams dispatched
    to different provinces at staggered times; provincial party secretaries were gradually replaced across provinces
  assignment_mechanism: The staggered timing of central inspection team arrivals and provincial leadership turnover creates
    temporal and cross-province variation in anti-corruption enforcement intensity
  parent: null
  related_variations: []
timeline:
  announcement: '2012-12-04'
  effective: null
  implementation_start: 2013
  implementation_end: 2016
  local_timing: Central inspection teams arrived at different provinces on a staggered schedule between 2013–2016; leadership
    replacements also occurred asynchronously
  anticipation: The campaign was announced at the 18th Party Congress in late 2012; early effects may have preceded formal
    inspection arrivals
  last_verified: '2026-07-13'
assignment:
  unit: Land transaction (firm-local government pair)
  treated: Land transactions involving politically connected firms ("princelings" — firms connected to Politburo members),
    after the anti-corruption campaign intensifies in their province
  comparison_pool: Land transactions involving unconnected firms; transactions in provinces not yet inspected; pre-campaign
    transactions by connected firms
  rule: A land transaction is treated if (a) the buyer is a firm politically connected to a Politburo member AND (b) the transaction
    occurs after the anti-corruption campaign reaches the relevant province through inspections or leadership change
  intensity: Connected firms experienced a 42.6% reduction in price discounts in provinces targeted by central inspections
  exemptions: []
  compliance: Enforcement was real but incomplete; connected firms retained some advantages even during the campaign
  exposure_construction: For each land transaction, code whether the buyer has a political connection to a Politburo member;
    interact with post-campaign timing indicators at the province-year level, with variation by inspection team arrival and
    leadership change
  required_identifiers:
  - land transaction ID
  - firm political connection indicator
  - province
  - year
  - inspection arrival date
  - provincial leader identity
  spillovers: The anti-corruption campaign may have shifted corrupt transactions to less-monitored sectors or to firms with
    different types of connections
research_compatibility:
  outcome_domains:
  - land prices
  - corruption
  - political connections
  - firm value
  - official promotions
  - local public finance
  affected_populations:
  - politically connected firms
  - local government officials
  - land market participants
  mechanism_channels:
  - reduced corruption
  - increased enforcement
  - reduced political protection
  - promotion incentive changes
  - land market transparency
  best_for:
  - Studying how top-down political campaigns affect firm-political relationships
  - staggered treatment designs with leadership changes
  not_good_for:
  - Long-run equilibrium effects after the campaign
  - outcomes in non-land sectors
design:
  claim_type: causal
  affordances:
  - staggered inspection team arrivals
  - provincial leader replacements
  - firm-level political connection data
  - detailed land transaction records
  candidate_designs:
  - staggered difference-in-differences
  - triple differences (connected × inspected province × post-campaign)
  identifying_variation: The interaction of pre-existing firm political connections with the staggered timing of anti-corruption
    enforcement across provinces
  assumptions:
  - Inspection timing is unrelated to pre-existing land market conditions
  - connected and unconnected firms would have had parallel trends absent the campaign
  - connections are correctly measured
  diagnostics:
  - Test for pre-trends in land price discounts
  - compare provinces with different inspection timing
  - test for spatial spillovers using nearby untreated provinces
  - verify balance of connected/unconnected firm characteristics
  primary_strategy: Triple differences; staggered DID; spatial matched sample (within 500m radius of land parcels)
  estimand: The causal effect of the recorded exposure on Land transaction price discounts, provincial party secretary promotion
    probability, conditional on the stated design assumptions.
  treatment_variable: Triple interaction — firm connected to Politburo member × province inspected or leadership changed ×
    post-2012
  comparison_logic: Connected vs unconnected firms; inspected vs not-yet-inspected provinces; pre- vs post-campaign
  estimation_notes: Triple differences; staggered DID; spatial matched sample (within 500m radius of land parcels)
threats:
- type: endogenous-inspection-timing
  basis: inferred
  condition: Provinces were not randomly selected for inspection; those with more visible corruption may have been targeted
    earlier
  evidence_refs:
  - E1
  possible_diagnostics:
  - test for pre-trends by inspection timing
  - use within-province variation in connection intensity
  - examine selection criteria for inspection scheduling
- type: measurement-of-connections
  basis: inferred
  condition: Political connections are difficult to measure comprehensively; connections through family ties, former colleagues,
    or lower-level officials may be missed
  evidence_refs:
  - E1
  possible_diagnostics:
  - use multiple connection measures
  - test robustness to alternative definitions
  - focus on the most clearly identifiable connections
- type: replication-data-integrity
  basis: reported
  condition: A later replication reports apparent duplicate parcel rows and a discrepancy between the paper's description and code for the area variable. Its alternative cleaning and outcome transformations leave some princeling differences but make the timing and causal interpretation of the campaign materially less stable.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Inspect transaction identifiers and distinguish legitimate identical parcels from duplicated rows before estimation
  - Reproduce the analysis with documented duplicate rules and transaction-level audit samples
  - Re-estimate quantity outcomes with correctly specified transformations and transparent extensive-margin handling
  - Report sensitivity of campaign interactions to the pre-2012 trend and outcome definition
empirical_requirements:
  contract_version: 1
  population: Land transactions in urban China, 2004–2016, matched to firm political connection data
  observation_unit: Land transaction
  geography_level: Province and city
  time_start: 2004
  time_end: 2016
  minimum_frequency: annual
  minimum_pre_periods: 5
  minimum_post_periods: 3
  required_fields:
  - land transaction price
  - location
  - buyer identity
  - seller (local government)
  - transaction date
  - firm political connections
  - province inspection dates
  required_identifiers:
  - transaction ID
  - firm ID
  - province code
  - year
  treatment_key:
  - firm political connection indicator
  - province inspection or leadership change indicator
  - post-2012 indicator
  treatment_source: Land transaction records from China Land Market Network; firm connection data from annual reports and
    public records; inspection and leadership data from official CCDI and party announcements
  measurement_risks:
  - political connections may be incomplete
  - land price reporting accuracy
  - inspection intensity measurement
  - confounding local economic conditions
evidence:
- id: E1
  source_type: paper
  citation: 'Chen, Ting, and James Kai-sing Kung. 2019. "Busting the ''Princelings'': The Campaign Against Corruption in China''s
    Primary Land Market." Quarterly Journal of Economics 134 (1): 185–226.'
  url: https://doi.org/10.1093/qje/qjy027
  date: 2019
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.announcement
  - timeline.implementation_start
  - timeline.local_timing
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.exposure_construction
  - assignment.required_identifiers
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - design.assumptions
  - design.diagnostics
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_source
  - design_applications.paper
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
  - design_applications.research_question
  - design_applications.population
  - design_applications.outcome
  - design_applications.treatment_encoding
  - design_applications.comparison
  - design_applications.empirical_design
  - design_applications.assumptions
  - design_applications.threats_addressed
  verification_status: reported
  access_level: abstract
  locator: QJE citation and author publication page identify the paper, journal, issue, pages, DOI, and accompanying download/replication-file links; the original article full text was not independently inspected in this audit.
- id: E2
  source_type: scholarship
  citation: 'Manso, Julia. 2026. "Are Princelings Truly Busted? Evaluating Transaction Discounts in China''s Land Market." Journal of Applied Econometrics 41(2): 384-403. DOI: 10.1002/jae.70060.'
  url: https://onlinelibrary.wiley.com/doi/10.1002/jae.70060
  date: 2026
  supports:
  - threats.condition
  - threats.possible_diagnostics
  - empirical_requirements.measurement_risks
  verification_status: verified
  access_level: full-text
  locator: 'Sections 1-4 and appendix: audit of 1,208,621 original transaction rows, duplicate-row patterns, the area-variable code/text discrepancy, and sensitivity of the campaign interpretation to duplicate removal and alternative outcome construction.'
design_applications:
- paper: 'Busting the ''Princelings'': The Campaign Against Corruption in China''s Primary Land Market'
  doi: 10.1093/qje/qjy027
  journal: Quarterly Journal of Economics
  year: 2019
  research_question: Did the anti-corruption campaign reduce land price discounts to politically connected firms, and what
    were the consequences for official promotions?
  population: ~1 million land transactions across Chinese cities, 2004–2016
  outcome: Land transaction price discounts, provincial party secretary promotion probability
  data_used:
  - China Land Market Network / Land Transaction Monitoring System parcel transaction records
  - Firm political-connection coding from public biographical and corporate sources, as reported by the paper
  - Province inspection and provincial-party-secretary appointment timing, as reported by the paper
  treatment_encoding: Triple interaction — firm connected to Politburo member × province inspected or leadership changed ×
    post-2012
  comparison: Connected vs unconnected firms; inspected vs not-yet-inspected provinces; pre- vs post-campaign
  empirical_design: Triple differences; staggered DID; spatial matched sample (within 500m radius of land parcels)
  assumptions:
  - parallel trends across connected/unconnected firms
  - inspection timing exogenous
  - connection measurement accurate
  threats_addressed:
  - endogenous inspection timing via staggered design
  - measurement error via multiple connection definitions
  - spatial confounding via matched-sample analysis
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
---
## Institutional Background
Before Xi Jinping's anti-corruption campaign, politically connected firms — particularly those tied to Politburo members ("princelings") — received massive discounts on land purchases from local governments. These discounts served as quid pro quo: local officials provided cheap land in exchange for political support or promotion consideration from higher-level patrons. [E1]

## What Changed
The paper treats the post-2012 anti-corruption campaign, staggered central inspections, and provincial party-secretary replacement as related enforcement signals. It reports that these signals coincided with smaller discounts for politically connected firms; that is a paper-reported empirical result, not a finding independently reproduced in this record. [E1]

## Implementation and Assignment
Central inspection teams arrived in different provinces at different times (2013–2016), creating staggered treatment timing. Provincial leadership replacements added another source of variation. The key identification comes from comparing connected-firm land transactions before vs. after the campaign reaches their province, relative to unconnected firms in the same market. [E1]

## Why This Creates Empirical Variation
The paper's empirical design treats pre-existing political connections interacted with post-2012 and province-level enforcement signals as the source of contrast. Its identifying content therefore depends on the timing of inspections and leadership changes, comparability of connected and unconnected firms, parcel-data integrity, and the absence of differential pre-trends; staggered timing alone does not establish exogeneity. [E1; analytical inference]

## Identification Risks
Provinces were not randomly selected for inspection; those with more visible corruption may have been targeted earlier. Political connections may also be measured with error, particularly informal or indirect connections. In addition, a later replication identifies apparent duplicate parcel rows and an area-variable code/text mismatch; it finds that the timing evidence is substantially less clean under alternative data cleaning and transformations. The original result is therefore not a plug-in causal shock without a fresh data audit. [E1; E2; analytical inference]

## Data Requirements
The reported application combines parcel-level land transactions, firm political-connection coding, province-level inspection and leadership-change dates, and provincial controls. A new use also needs transaction identifiers and raw fields sufficient to audit duplicate records, a documented area transformation, and a pre-specified rule for any deduplication. [E1; E2]

## Evidence Notes
E1 is the original QJE study, retained here as the source of the reported design, coding, and findings; this audit did not independently inspect its full text or reproduce its estimates. E2 is a subsequent full-text replication audit. It reports apparent duplicates in roughly one-third of the original transaction rows, especially among princeling parcels, and a mismatch between the text and code for an area outcome. Although some original associations persist under one deduplication exercise, the replication finds the campaign timing evidence less stable under alternative outcome construction. This record is consequently **contested**: it is a valuable land-market research lead, but a new study must audit the raw parcel data and re-establish identification before relying on the reported campaign effect.
