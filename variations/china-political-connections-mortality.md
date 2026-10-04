---
schema_version: 2
id: china-political-connections-mortality
name: Political Connections and Worker Safety Compliance in Chinese Listed Firms
aliases:
- Mortality cost of political connections
- Fisman Wang political connections China
- 政治关联与工人安全

status: contested
provenance:
  task_id: task-d76de82cefa8
scope:
  country: China
  regions:
  - Mainland China listed firms in nine hazardous industrial sectors
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
  instrument: Annual politically connected senior-executive status and its changes through executive turnover; not a politician death or illness shock
  authority: Firm executive appointments and departures; no external authority randomly assigns political connections
  legal_identifiers: []
  implementation_regime: The inspected study measures prior senior government employment of the chairman, vice-chairman, CEO and vice-CEOs of listed firms during2008-2013. Provincial safety-promotion rules are a separate moderator, not the executive-status assignment.
  assignment_mechanism: Firms acquire or lose connected executives through endogenous appointments and departures. Within-firm regressions use changes in this status; the authors explicitly caution that connections are not exogenously assigned.
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 2008
  implementation_end: 2013
  local_timing: Study observation window, not policy rollout. Status in year y uses executive employment on December31 of y-1, before the year's accidents.
  anticipation: Appointments and departures can respond to firm conditions; the inspected study does not establish unanticipated executive changes.
  last_verified: '2026-10-04'
assignment:
  unit: Firm-year
  treated: Firm-years with at least one qualifying connected senior executive at the preceding year-end
  comparison_pool: Unconnected firm-years under measured controls; within-firm specifications use status changes, including the subsample with variation in Connected
  rule: Connected equals1 if a qualifying executive formerly served as mayor or vice-mayor in the firm's city or held a provincial/central government post of equivalent or higher rank. It is not a politician-health event indicator.
  intensity: Binary connected executive status, not intensity of a health shock
  exemptions: []
  compliance: Not applicable — political connections are not a formal policy
  exposure_construction: Link annual firm identifiers to year-end senior-executive resumes and past government rank/location; lag status into the outcome year. Separately reconstruct fatalities and employment. Do not code arbitrary board membership or government ownership as equivalent to this status.
  required_identifiers:
  - firm ID
  - year
  - political connection indicator
  - executive identity, employment dates, past government rank and jurisdiction
  spillovers: Executive moves between firms and common local enforcement may connect observations; this is an analytical concern, not a studied politician-death spillover.
research_compatibility:
  outcome_domains:
  - workplace fatalities
  - worker safety
  - regulatory violations
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
  - Describing within-firm connection-status changes while explicitly retaining endogenous appointment and departure risks
  not_good_for:
  - Outcomes unrelated to regulation or enforcement
  - Politician death or illness event studies attributed to this paper
  - Treating ordinary executive turnover or provincial safety-rule adoption as random assignment
design:
  claim_type: descriptive
  affordances:
  - Within-firm executive-status changes
  - cross-sectional variation in connection status
  candidate_designs:
  - Firm fixed-effects association between Connected and annual workplace fatalities
  - Cross-sectional count and linear models with measured controls
  identifying_variation: Cross-firm and within-firm variation in connected executive status; executive turnover supplies the latter, without an exogenous assignment claim
  assumptions:
  - A causal interpretation would require time-varying firm conditions not to drive both executive choices and safety; the paper cautions that connections are endogenous
  diagnostics:
  - Compare full and executive-status-switcher samples and pre-existing firm characteristics
  - Distinguish departures following fatal accidents from antecedent status changes
  - Check fatality reporting sources and employment denominators
  primary_strategy: Negative-binomial count models and OLS fatalities/death-rate regressions; province, industry and year effects, with firm effects in selected specifications; firm-clustered standard errors
  estimand: Conditional association of connected executive status with fatalities and deaths per1000 employees; not a politician-health-shock causal effect
  treatment_variable: Connected at the previous December31, based on senior-executive employment history
  comparison_logic: Connected versus unconnected firm-years, and same-firm status changes with controls; executive selection remains unresolved
  estimation_notes: Inspected NBER June2015 version Section3.1.1 equation5. Fatal-accident stock-return events and subsequent executive departures are separate analyses, not health-shock identification.
threats:
- type: endogenous-connection-formation
  basis: documented
  condition: Firms that choose to form political connections may be systematically different from unconnected firms
  evidence_refs:
  - E2
  possible_diagnostics:
  - within-firm analysis eliminates time-invariant firm characteristics
  - compare connected and unconnected firms' pre-treatment trends
- type: concurrent-changes
  basis: inferred
  condition: Executive appointments may accompany changes in firm strategy or finances, while accidents can themselves trigger connected executives' departures; firm effects do not remove these time-varying channels
  evidence_refs:
  - E2
  possible_diagnostics:
  - Separate status before accidents from subsequent executive departures
  - compare with firms in different industries or regions
  - test for effects on placebo outcomes
empirical_requirements:
  contract_version: 1
  population: Listed Chinese firms in nine hazardous sectors during2008-2013; construction fatality data use a distinct ministry source
  observation_unit: Firm-year
  geography_level: National (firm-level)
  time_start: 2008
  time_end: 2013
  minimum_frequency: annual
  minimum_pre_periods: 1
  minimum_post_periods: 0
  required_fields:
  - firm political connections
  - preceding year-end executive roster and resumes with past government rank and location
  - workplace fatalities
  - employee count for deaths per1000 workers
  - regulatory violations
  - firm financial variables
  required_identifiers:
  - firm ID
  - year
  - political connection indicator
  treatment_key:
  - firm ID
  - year
  - preceding year-end qualifying executive-status indicator
  treatment_source: Executive resumes from Wind and annual reports; corporate disclosures and SAWS records for fatalities, proprietary housing/construction ministry records for construction, WiseSearch supplements; financial controls from CSMAR and employees from Resset in the inspected version
  measurement_risks:
  - underreporting of workplace fatalities
  - political connection measurement error
  - Midyear executive turnover and incomplete employment histories
  - Different coverage for construction contract workers and industrial employees
evidence:
- id: E1
  source_type: paper
  citation: 'Fisman, Raymond, and Yongxiang Wang. 2015. "The Mortality Cost of Political Connections." Review of Economic
    Studies 82 (4): 1346–1382.'
  url: https://doi.org/10.1093/restud/rdv020
  date: 2015
  supports:
  - design_applications.paper
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
  verification_status: reported
  access_level: abstract
  locator: Publisher metadata and abstract; published methods/typesetting not inspected in this audit
- id: E2
  source_type: paper
  citation: Fisman and Wang, The Mortality Cost of Political Connections, NBER Working Paper21266, June2015
  url: https://www.nber.org/system/files/working_papers/w21266/w21266.pdf
  date: 2015
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.rule
  - assignment.exposure_construction
  - design.primary_strategy
  - design.estimand
  - empirical_requirements.required_fields
  - design_applications.treatment_encoding
  verification_status: verified
  access_level: full-text
  locator: PDFp3/printed2 introduction; PDFpp10-14/printed9-13 Section1.4; PDFp19/printed18 Section3.1.1 equation5; PDFp24/printed23 equation6 and post-accident executive departures
design_applications:
- paper: The Mortality Cost of Political Connections
  doi: 10.1093/restud/rdv020
  journal: Review of Economic Studies
  year: 2015
  research_question: Do political connections allow firms to avoid safety compliance, and what are the mortality consequences?
  population: Hazardous-sector Chinese listed firms,2008-2013 in the inspected NBER version
  outcome: Workplace fatalities, regulatory violations for workplace safety
  data_used: [Wind executive resumes, Annual corporate reports and CSR disclosures, SAWS accident sources, Proprietary ministry construction accidents, WiseSearch news, CSMAR controls, Resset employees]
  treatment_encoding: Qualifying executive political experience at the previous year-end; the inspected version uses no politician death/illness instrument
  comparison: Connected/unconnected firm-years and within-firm executive-status changes
  empirical_design: Count/linear models with controls, selected firm-effects specifications and firm clustering; separate fatal-accident stock-return events
  assumptions:
  - Executive-status variation is not exogenously assigned; firm effects remove fixed attributes only
  threats_addressed:
  - Fixed firm differences examined through within-firm specifications, not a complete solution to executive selection
  - industry trends via controls
  evidence_refs:
  - E1
  - E2
readiness_blockers:
- Primary institutional evidence has not been independently verified; institutional and exposure grounding currently relies on the inspected research paper
- The inherited politician health-shock interpretation is contradicted by inspected methods; this contested record is not an exogenous-shock recommendation
- Final published methods and replication materials must be reconciled with the NBER version before further maturity review
- Provincial no-safety/no-promotion rules are a separate application requiring primary province-level assignment audit, not a silently merged exposure
method_transfer: null
---
## Institutional Background
This retained legacy case concerns political experience of senior executives and workplace safety in hazardous-sector listed firms. The inspected methods use executive arrivals and departures, not unexpected death or illness of an affiliated official. Its contested state concerns the inherited record's identification interpretation, not a claim that the published study itself is disputed. [E2]

## What Changed
Qualifying executive status changes when firms appoint or lose managers with prior senior government experience. The paper's data window is2008-2013. Political appointments and exits are choices, not independently assigned health events. [E2]

## Implementation and Assignment
The connected indicator uses the previous December31 roster and government employment history. Annual status precedes that year's accidents, while within-firm comparisons rely on executive turnover. Separate provincial safety-promotion laws moderate the connection relationship; their rules must not be folded into executive assignment. [E2]

## Why This Creates Empirical Variation
The variation supports descriptive analysis of executive status and regulatory outcomes. It does not supply a ready-made natural experiment: the authors explicitly caution that connections are not exogenously assigned. [E2]

## Identification Risks
Firm effects do not absorb changing management, strategies or enforcement. The paper separately studies connected executives leaving after fatal accidents, making it particularly important not to mistake subsequent departure for an antecedent external shock. Fatality reporting and construction-worker coverage also require source-specific reconstruction. [E2; analytical inference]

## Data Requirements
Use executive resumes, dated rosters, government rank and location, firm-year fatalities, employee denominators and financial controls. The inspected version combines corporate and safety-agency reports with commercial news supplements; construction uses proprietary ministry accidents. Raw-data accessibility and final-version reconciliation remain conditions. Politician-health data are not this application's treatment source. [E2]

## Evidence Notes
E1 verifies only the publication/abstract boundary. E2 is the inspected June2015 NBER version, not certified publisher typesetting. The audit preserves the existing file and DOI while replacing the unsupported health-shock story in both structured fields and narrative. No estimates were reproduced and no underlying microdata or PDF was stored.
