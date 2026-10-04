---
schema_version: 2
id: china-top1000-designated-firm-energy-regulation
name: China Top1000 Designated-Firm Energy Regulation
aliases: [千家企业节能行动, Top1000 energy conservation, Regulating Conglomerates]
status: grounded
provenance:
  task_id: task-351b383e709b
scope:
  country: China
  regions: [Mainland China]
  domains: [firms, environmental-economics, industrial-economics]
  variation_type: eligibility-threshold
  knowledge_role: china-variation
  china_relevance: Named Chinese enterprises faced energy regulation; the application compares their outcomes with other domestic enterprises.
identity:
  instrument: Designation under the2006 Top1000 energy programme
  authority: NDRC and four co-issuing national agencies, with provincial verification
  legal_identifiers: [发改环资〔2006〕571号]
  implementation_regime: The original designated-firm programme, not its later Top10000 expansion
  assignment_mechanism: Retrospective energy-use eligibility followed by administrative designation; neither lottery nor unexpected annual adoption
  parent: null
  related_variations: []
timeline:
  announcement: '2006-04-07'
  effective: null
  implementation_start: 2006
  implementation_end: null
  local_timing: The notice was signed April7 and posted April14. The research specification separates designation from assessment, using2006 as the reference and post2006 outcomes; the application does not supply daily firm enforcement dates.
  anticipation: A lagged eligibility measure does not establish absence of expectations or other firm-specific trends.
  last_verified: '2026-10-02'
assignment:
  unit: Independent-accounting enterprise
  treated: Enterprises on the original national designation list
  comparison_pool: Paper-defined later Top10000 firms not already regulated or linked to Top1000 firms
  rule: The notice specifies above-scale enterprises in nine energy-intensive industries with2004 comprehensive energy consumption at least180000 tonnes of standard coal;1008 were designated after provincial checking.
  intensity: Designation is binary; local energy quotas are a different, potentially endogenous intensity.
  exemptions: [Do not assign an entire corporate group merely because one member is designated]
  compliance: The published appendix describes implemented consumption quotas rather than treating reported savings as audited efficiency gains.
  exposure_construction: Join the designation roster to legal enterprise identities, then annual outcomes. Distinguish missing matches from untreated firms and maintain predecessor/successor identities. Encode the paper's post-assessment comparison separately from legal announcement timing.
  required_identifiers: [Enterprise legal ID, Enterprise name, Year, Industry, Province]
  spillovers: Related enterprises and market competitors can respond; unregulated does not mean unaffected.
research_compatibility:
  outcome_domains: [Energy use, Output, Efficiency, Firm adjustment]
  affected_populations: [Designated industrial enterprises, Unregulated competitors and affiliates]
  mechanism_channels: [Regulatory burden, Production substitution, Energy management]
  best_for: [Conditional firm-panel comparisons with explicit spillover interpretation]
  not_good_for: [Random assignment, Automatic RD from the threshold, Untreated corporate-group controls, Nationwide welfare effects inferred from DID alone]
design:
  claim_type: reduced-form
  affordances: [Pre-existing eligibility measure, Named designation, Firm-panel comparisons]
  candidate_designs: [DID with network-aware controls]
  identifying_variation: Differential exposure to the designated-firm regime, conditional on comparable counterfactual trends
  primary_strategy: Author manuscript SectionII equations1-2, firm-panel DID
  estimand: Relative change for designated firms against the specified comparison; not an isolated direct effect when controls experience market spillovers
  treatment_variable: Roster membership interacted with post2006
  comparison_logic: See assignment.comparison_pool; exclude ownership-linked controls and assess residual market exposure
  estimation_notes: The inspected author text uses firm fixed effects, industry-year and province-year adjustments, firm clustering and a2006 event-study reference. A threshold-based RD is not the documented application.
  assumptions:
  - Conditional counterfactual trends are comparable despite differences in firm size and energy use.
  - Concurrent policies and composition changes do not generate the contrast.
  - Spillovers are represented in the estimand rather than silently assumed absent.
  diagnostics:
  - Inspect pretrends and2004 energy-use mean reversion without treating insignificant coefficients as proof.
  - Test exclusions for overlapping policies, missing outcomes and ownership-linked controls.
  - Separate direct, affiliate and market exposure; reconsider post-policy network classification.
threats:
- type: selection-and-mean-reversion
  basis: inferred
  condition: Large initial energy users can have different trajectories; lagged selection alone does not justify causal attribution.
  evidence_refs: [E1, E2]
  possible_diagnostics: [Baseline energy trajectories, Alternative comparison samples, Concurrent-policy sensitivity]
- type: network-and-market-interference
  basis: documented
  condition: Ownership links are measured in2018, after regulation. A later link is not proof of baseline affiliation, while excluding affiliates still leaves market spillovers.
  evidence_refs: [E2, E3]
  possible_diagnostics: [Historical ownership reconstruction, Stable-link sensitivity, Explicit market-effect interpretation]
- type: outcome-coverage
  basis: inferred
  condition: Energy-reporting coverage and industrial-survey thresholds select observations. A measured efficiency ratio requires consistent energy and output definitions, not just matched firm names.
  evidence_refs: [E2, E3]
  possible_diagnostics: [Outcome-specific sample counts, Missingness by designation, Reporting-threshold sensitivity]
empirical_requirements:
  contract_version: 1
  population: Outcome-observed designated and eligible comparison industrial enterprises
  observation_unit: Firm-year
  geography_level: Enterprise with province identifier
  time_start: 2001
  time_end: 2010
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields: [Roster designation, Energy consumption by fuel, Output, Industry, Province, Ownership links for control exclusion, Baseline firm characteristics]
  required_identifiers: [Legal enterprise ID, Enterprise name crosswalk, Year]
  treatment_key: [Legal enterprise ID, Year]
  treatment_source: Original NDRC roster, not a threshold reconstructed solely from outcome-survey energy
  measurement_risks: [Firm renaming or restructuring, Fuel conversions, Electricity-intensive sample exclusions, Restricted microdata access]
design_profiles: []
evidence:
- id: E1
  source_type: policy-document
  citation: NDRC et al., 关于印发千家企业节能行动实施方案的通知,571号
  url: https://www.ndrc.gov.cn/xxgk/zcfb/tz/200604/t20060414_965934_ext.html
  date: '2006-04-07'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.assignment_mechanism, timeline.announcement, timeline.implementation_start, assignment.rule, assignment.treated]
  verification_status: verified
  access_level: official-document
  locator: Notice opening, item1 and signature; original attachments linked but not inspected. Establishes eligibility/designation and signing date, not daily enforcement or measured compliance.
- id: E2
  source_type: paper
  citation: Chen et al., Regulating Conglomerates, author-hosted AER-format manuscript
  url: https://jcsuarez.com/Files/Chen_et_al_conglomerates.pdf
  date: null
  supports: [identity.implementation_regime, timeline.local_timing, assignment.comparison_pool, assignment.spillovers, design.primary_strategy, design.treatment_variable, design.comparison_logic, design.estimand, design.estimation_notes, empirical_requirements.time_start, empirical_requirements.time_end, empirical_requirements.required_fields, design_applications.data_used, design_applications.empirical_design, design_applications.treatment_encoding]
  verification_status: reported
  access_level: full-text
  locator: 184-page author copy retrieved2026-10-02; pp8-14, SectionsI.A-C andII equations1-2. Undated, with volume/month placeholders, not confirmed publisher typesetting. Numerical estimates are not reproduced here.
- id: E3
  source_type: appendix
  citation: Chen et al., published AER Online Appendix
  url: https://www.aeaweb.org/articles/materials/22277
  date: 2025
  supports: [assignment.compliance, assignment.required_identifiers, empirical_requirements.required_identifiers, threats.condition]
  verification_status: reported
  access_level: appendix
  locator: AppendixA PDF pp3-8, AppendixC pp20-22; quota interpretation, name/legal-ID merging and2018 network measurement. Interviews are attributed research evidence, not independently inspected local quota documents.
- id: E4
  source_type: paper
  citation: AEA article metadata, American Economic Review115(2),408-447
  url: https://doi.org/10.1257/aer.20211455
  date: 2025
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: AEA article title, authors and February2025 issue; member-only main-paper route not inspected.
- id: E5
  source_type: replication
  citation: Data and Code for Regulating Conglomerates, openICPSR196012V1
  url: https://doi.org/10.3886/E196012V1
  date: '2025-04-15'
  supports: [empirical_requirements.measurement_risks]
  verification_status: reported
  access_level: metadata
  locator: Project description excludes confidential data. README listing inspected; download redirects to login. Neither README content nor estimation code was inspected or executed.
design_applications:
- paper: 'Regulating Conglomerates: Evidence from an Energy Conservation Program in China'
  doi: 10.1257/aer.20211455
  journal: American Economic Review
  year: 2025
  research_question: How does enterprise regulation affect production and resource use when firms can adjust through ownership networks?
  population: Mainland industrial enterprises
  outcome: Energy use and output; distinguish intensity ratios from engineering efficiency
  data_used: [CESD2001-2010, ASIF characteristics and outputs, CARD ownership, ATS robustness]
  treatment_encoding: Designation interacted with post2006 in the inspected author version
  comparison: Later-designated firms, excluding linked enterprises; market exposure remains
  empirical_design: Firm-panel DID, not automatic RD or a randomized energy quota
  assumptions: [Conditional trends, Correct identity joins, Explicit interference interpretation]
  threats_addressed: [Pretrend assessment, Alternative samples, Concurrent-policy sensitivity]
  evidence_refs: [E2, E3, E4]
method_transfer: null
readiness_blockers:
- Access to identified CESD/ASIF/CARD microdata and stable firm crosswalks is conditional; the public replication listing does not supply confidential inputs or demonstrate unrestricted access.
- Author-copy specifications and published appendix are inspectable; final publisher typesetting and the login-required README/code were not reconciled. Confirm exact source-version reproduction before replicating estimates.
---

## Institutional Background

This case records enterprise designation, not a general environmental-policy label. The original notice establishes a retrospective selection rule and administrative verification [E1]. That helps recover who was regulated, but does not make high-energy firms comparable to smaller firms without further reasoning. Energy management, environmental emissions and technical efficiency are related concepts, not interchangeable outcomes [analytical inference].

## What Changed

The original programme created a named regulatory population. Its later expansion defines a possible research comparison, not a second treatment embedded in this record. The published appendix distinguishes formal savings language from consumption quotas used in implementation [E3, reported claim]. A new study should verify local quota intensity separately rather than infer it from designation.

## Implementation and Assignment

Keep legal announcement, assessment timing and empirical coding separate. Reconstruct membership from the roster and legal identities; join years only after resolving firm continuity. Missing firm matches cannot become zero exposure. Corporate affiliation matters for comparison construction, but designation does not automatically apply to every affiliate [analytical inference].

## Why This Creates Empirical Variation

The paper compares firm trajectories under differential regulatory exposure [E2, reported claim]. Its relative effect can reflect changes in both treated and comparison firms. That remains informative for a suitably framed question; it is not a nationwide net-energy effect. A sharp formal eligibility rule does not establish a usable density of observations near its cutoff [analytical inference].

## Identification Risks

An apparent output decline can combine policy response, initial-scale mean reversion and changing reporting coverage. Network adjustment also complicates the untreated comparison. Treat2018 affiliation as an observed later relationship, not a predetermined instrument. The credible next step is to test whether the intended comparison survives these issues, not to add every available control indiscriminately [analytical inference].

## Data Requirements

The default contract concerns the direct firm-panel comparison. A separate spillover analysis requires a complete ownership history, an independently specified matching design and outcome-specific coverage; these are not silently added to every user's mandatory fields. Restricted microdata remain an access condition even when public designation is recoverable. This repository records the necessary joins; dataset acquisition belongs in the complementary data knowledge base.

## Evidence Notes

Task351b383e709b closes institutional identity, primary selection and the version-bounded research application. It does not certify replication or unrestricted data. The NBER July2021 version was also inspected for orientation, but the later author copy supplies the documented specification. Preserve the published appendix and author-copy distinction instead of presenting either as independently audited local enforcement. No paper or restricted dataset was saved.
