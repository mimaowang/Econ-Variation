---
schema_version: 2
id: china-sme-loan-access-saturation-experiment
name: China SME Loan-Access Encouragement and Market Saturation Experiment
aliases:
- Cai Szeidl indirect effects of access to finance
- China retail-market randomized credit encouragement
status: grounded
provenance:
  task_id: task-6f5c50006bfc
scope:
  country: China
  regions: [One unnamed prefecture-level city in southeastern mainland China]
  domains: [development-economics, firm-economics, regional-economics, industrial-organization, finance]
  variation_type: pilot-assignment
  knowledge_role: china-variation
  china_relevance: >
    Chinese firms in 78 local markets faced randomized offers of bank-officer
    information and application assistance for a new SME loan. Randomized
    market saturation allows the AER2024 application to study own-firm effects
    together with information diffusion and competitive spillovers. This is
    a Chinese credit intervention, not the separate Nanchang networking RCT.
identity:
  instrument: >
    A one-year loan-access encouragement intervention, nested within randomly
    assigned market saturation of zero, 50 or 80 percent. Loan officers visit
    assigned firms monthly to explain a new collateral-free loan and help
    with applications. Approval and actual borrowing are not randomized.
  authority: The investigators and an unnamed major Chinese commercial partner bank, working with local market offices.
  legal_identifiers:
  - AEARCTR-0009506; registry version DOI 10.1257/rct.9506-1.0
  - Internal bank intervention rather than a publicly identified national policy
  implementation_regime: >
    The bank offered the new product to firms in local markets in 2013.
    Untreated firms could apply independently. The bank screened all
    applications and assigned approved applicants a limit up to 30 percent
    of assessed net assets, capped at CNY500000. Assigned visits stopped once
    a firm decided to borrow; officers were not to visit untreated firms
    during the intervention year. The loan required monthly interest and
    repayment within two years, with subsequent borrowing possible.
  assignment_mechanism: >
    Computer randomization assigned 37 markets to 80 percent encouragement,
    10 to 50 percent, and 31 to pure control. Market assignment was stratified
    by county and above/below county-median market size, yielding 22 strata.
    Firms were then randomly assigned within above/below market-median
    employment strata. The intervention covered the underlying population
    of over 6000 firms; a randomly selected half formed the 3173-firm survey.
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 2013
  implementation_end: 2014
  local_timing: >
    The registry reports intervention dates August1,2013-August1,2014,
    within a study period July1,2013-September1,2020. The paper describes
    summer2013 baseline before intervention, summer2015 midline,
    summer2016 endline and summer2020 short follow-up. Exact dates come
    from retrospective registry fields, not inspected visit logs.
  anticipation: At baseline assigned firms did not yet know they would receive visits; all firms could subsequently learn about the product from peers or other sources.
  last_verified: '2026-10-04'
assignment:
  unit: Firm assignment nested in market saturation; outcomes measured by firm and survey wave.
  treated: Firms randomly assigned monthly information/application-assistance visits in 50 or 80 percent markets.
  comparison_pool: >
    Unassigned firms in those markets and firms in zero-saturation markets.
    The former can experience peer information and competition effects;
    they are not equivalent to pure-control firms or prohibited borrowers.
  rule: >
    Use the original market and firm assignment indicators and strata,
    not realized borrowing. For competition exposure define competitors
    as other firms in the same market selling the same specialized product
    category. Distinguish this share from all-market peer assignment share
    used for borrowing diffusion. Preserve assigned saturation and realized
    competitor shares separately because finite group sizes vary.
  intensity: Market saturation 0/0.5/0.8 and binary own assignment; realized competitor assignment share for spillover regressions.
  exemptions:
  - The random survey half is not the full population receiving assignment.
  - Approval remained subject to bank screening; neither assigned nor unassigned firms were guaranteed credit.
  compliance: >
    Actual take-up is endogenous. Endline bank data cover all3173 sampled
    firms, while survey-based other borrowing covers2658. Table2 reports
    an approximately28-percentage-point own-assignment effect on new-loan
    borrowing. Unassigned firms in treated markets also borrow more than
    pure controls. This is not perfect compliance or control exclusion.
  exposure_construction: >
    Join stable firm IDs to market IDs, specialized products, assignment
    strata and survey waves. Exclude the focal firm from its peer group.
    Construct the same-market same-product share assigned encouragement;
    interact own assignment and that share with post-baseline observations
    for Equation8. The printed paper does not establish whether every
    published share uses the full assignment roster or the surveyed half,
    nor exact handling of groups without competitors. Inspect loan_main.do
    and the assignment fields before exact coding rather than substituting
    nominal saturation or recomputing shares on outcome complete cases.
  required_identifiers: [firm_id, market_id, county_id, specialized_product_category, assignment_stratum, survey_wave]
  spillovers: >
    Spillovers are part of the design: information changes untreated peers'
    borrowing, treated competitors can steal demand, and nearby
    noncompetitors can receive demand spillovers. Nearby and nonlocal
    groups are different exposure definitions; no-interference firm-level
    RCT formulas would discard the experiment's identifying structure.
research_compatibility:
  outcome_domains: [firm revenue, profits, employment, borrowing, business practices, local competition, prices, consumer satisfaction]
  affected_populations: [Small firms in 78 government-defined local markets, Mainly retailers with service and manufacturing firms]
  mechanism_channels: [Reduced information and application costs, Additional borrowing, Business improvements, Information diffusion, Competitive demand reallocation]
  best_for:
  - Studying credit encouragement and competitive spillovers where firm assignment, market and product groups can be recovered.
  - Distinguishing firm growth from aggregate local-market development; own-firm gains need not imply net producer gains.
  not_good_for:
  - A nationwide bank-policy DID or a claim that loan approval was randomly allocated.
  - Applying these historical assignments to unrelated ASIF firms without a verified crosswalk.
  - Calling published model-based welfare estimates direct experimental measurements of social surplus.
design:
  claim_type: causal
  affordances: [Two-stage saturation randomization, Baseline and two long follow-ups, Bank take-up data, Explicit competitor exposure]
  candidate_designs: [Direct and spillover intention-to-treat analysis, Panel IV with own and competitor assignment instruments]
  identifying_variation: Randomized own encouragement and other firms' encouragement across markets of different assigned saturation, conditional on the documented strata and exposure definition.
  primary_strategy: >
    Equation8 regresses outcomes on Post times own assignment and Post
    times competitor assignment share, with firm effects and Post.
    Equation7 relates borrowing to own treatment and untreated times
    all-market peer treatment share. Equation9 instruments own borrowing
    and competitor borrowing share with the corresponding Post-assignment
    variables. These are distinct estimands within one intervention.
  estimand: >
    Direct and indirect effects of the encouragement in the reduced form.
    Interpreting IV coefficients as effects of borrowing, and converting
    them into welfare, requires additional exclusion and model assumptions.
  treatment_variable: Own randomized encouragement and same-market same-product competitor encouragement share, interacted with Post in the firm panel.
  comparison_logic: >
    Contrast assigned and unassigned firms while accounting for competitor
    exposure; pure-control markets supply a no-encouragement comparison.
    Information diffusion makes untreated-in-treated-market outcomes
    substantively different from outcomes in zero-saturation markets.
  estimation_notes: >
    The paper clusters standard errors at market level. There are78 markets,
    not3173 independent saturation assignments. Only10 markets have50-percent
    saturation. Equation8's linear share specification imposes structure
    across intensities; inspect treatment-arm alternatives and the original
    assignment strata before implementing inference. Post pools2015/2016;
    2020 retrospective prices and consumer responses are different measures.
  assumptions:
  - Randomization and exposure construction are preserved, including strata and integer constraints.
  - Relevant interference is adequately represented by the market/product and neighborhood exposure definitions.
  - Missing outcomes and shutdown do not create unaddressed treatment-dependent selection.
  - Borrowing IV additionally requires visits to affect the outcome through the modeled borrowing channels rather than an independent advisory effect.
  diagnostics:
  - Reproduce baseline balance for own and competitor exposure; inspect saturation-arm and wave-specific results.
  - Separate attrition from confirmed shutdown and assess treatment-dependent selection rather than relying only on survivor balance.
  - Check competitor denominator, focal-firm exclusion, missing groups and clustering against the replication code.
  - Compare survey sales with endline book-value sales and evaluate retrospective price recall and consumer-sample selection.
threats:
- type: treatment_take_up_confusion
  basis: documented
  condition: Assignment offers assistance, whereas approval and borrowing remain selective; unassigned firms can borrow and learn through peers.
  evidence_refs: [E1, E2]
  possible_diagnostics: [Separate ITT from borrowing IV, Inspect first stages and independent advisory channels]
- type: interference_and_exposure
  basis: reported
  condition: Competitive and information spillovers are substantive; an assumed no-spillover control or complete-case competitor denominator changes the comparison.
  evidence_refs: [E1, E3]
  possible_diagnostics: [Recover original peer construction, Compare nominal arms and realized shares, Examine alternative local/nonlocal groups]
- type: selection_and_measurement
  basis: reported
  condition: Shutdown differs in some arms and outcomes are missing for movers/nonresponders; 2020 prices recall2016 and consumer evaluations cover firms found open.
  evidence_refs: [E1, E3]
  possible_diagnostics: [Attrition/shutdown bounds and sensitivity, Book-sales comparison, Wave-specific sample accounting]
- type: registration_and_external_validity
  basis: documented
  condition: Registration was submitted in2022 after the2013-2020 study; neither the registry label nor AER publication establishes prospective analysis commitment or representativeness beyond the city.
  evidence_refs: [E2]
  possible_diagnostics: [Separate retrospective documentation from preregistration, Examine population and market differences before transfer]
empirical_requirements:
  contract_version: 1
  population: Sampled firms in the78 local markets, linked to the underlying assignment roster in the unnamed southeastern Chinese city.
  observation_unit: firm-survey-wave
  geography_level: market and specialized product group within county
  time_start: 2013
  time_end: 2016
  minimum_frequency: survey-wave
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - Original own-assignment, assigned market saturation and market/firm randomization strata.
  - Specialized product category and eligible peer assignment roster or documented deposited peer shares.
  - Baseline2013 and post2015/2016 outcomes, survey response, confirmed shutdown and firm tracking.
  - Bank product borrowing indicator/date/amount for the borrowing and IV applications.
  required_identifiers: [firm_id, market_id, county_id, specialized_product_category, assignment_stratum, survey_wave]
  treatment_key: [firm_id]
  treatment_source: Investigator/partner-bank assignment records; retrospective AEA registry documents the design, while ICPSR lists the deposited analysis files.
  measurement_risks:
  - ICPSR V1 lists loan_main.do, loanmain.dta and market.dta, but download led to login; contents, licensing and available roster fields were not inspected.
  - The current registry says public data unavailable, while the2024 deposit lists data files; that older registry field is not proof the deposit contains no usable data.
  - Survey sampling covered half of assigned firms; do not silently construct peer exposure only among surviving surveyed firms.
  - Province, city and bank are unnamed in the paper; do not invent a location or promise a link to external administrative datasets.
evidence:
- id: E1
  source_type: paper
  citation: Cai, Jing and Adam Szeidl. 2024. Indirect Effects of Access to Finance. AER114(8),2308-2351; final typeset author-hosted copy.
  url: https://adamszeidl.com/papers/indirect_effects.pdf
  date: '2024'
  supports: [identity.instrument, identity.implementation_regime, identity.assignment_mechanism, timeline.local_timing, timeline.anticipation, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.intensity, assignment.compliance, assignment.exposure_construction, assignment.spillovers, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.required_fields, empirical_requirements.measurement_risks, design_applications.data_used]
  verification_status: reported
  access_level: full-text
  locator: Direct in-memory PDF inspected2026-10-04, printed pp2313-2318 SectionI; pp2322-2326 SectionII.C equations7-9 and Table2; p2334 Table5 and its notes. Assignment is author-reported; registry independently documents two-stage randomization. No replication executed.
- id: E2
  source_type: archive
  citation: Investigator registration, Indirect Effects of Access to Finance, AEARCTR-0009506, version1.0; submitted May27,2022 and first published May30,2022.
  url: https://www.socialscienceregistry.org/trials/9506
  date: '2022-05-30'
  supports: [identity.instrument, identity.legal_identifiers, identity.assignment_mechanism, timeline.local_timing, assignment.unit, assignment.treated, assignment.intensity]
  verification_status: verified
  access_level: official-document
  locator: Complete registry HTML directly retrieved with urllib and parsed2026-10-04 after browser-tool HTTP403. General Information, initial/first-published dates, Interventions dates, Experimental Design, Randomization Method/Unit and sample arms; computer draws,78 markets,3173 survey firms,1436 treated survey firms. This verifies investigator registration, not independent visit compliance or a prospective analysis plan.
- id: E3
  source_type: appendix
  citation: Cai and Szeidl AER2024 online appendix.
  url: https://www.aeaweb.org/articles/materials/21389
  date: '2024'
  supports: [assignment.spillovers, design.diagnostics, empirical_requirements.measurement_risks]
  verification_status: reported
  access_level: appendix
  locator: Official34-page PDF inspected2026-10-04; pp17-18 discussion of TablesA1-A3 and survivor/exposure balance; p24 TableA10 notes distinguish local/nonlocal competitors, include no-peer indicators and label second-degree effects suggestive. Balance does not prove absence of selection.
- id: E4
  source_type: other
  citation: American Economic Association article identity and supplemental links.
  url: https://doi.org/10.1257/aer.20220711
  date: '2024-08'
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: Publisher title/authors, citation, volume114 issue8 pp2308-2351 and Additional Materials inspected2026-10-04 at https://www.aeaweb.org/articles?id=10.1257/aer.20220711; DOI linked here for identity, not used as method evidence.
- id: E5
  source_type: replication
  citation: Cai and Szeidl. Data and code for Indirect Effects of Access to Finance. OpenICPSR197302 V1, published July10,2024, DOI10.3886/E197302V1.
  url: https://www.openicpsr.org/openicpsr/project/197302/version/V1/view
  date: '2024-07-10'
  supports: [empirical_requirements.treatment_source, empirical_requirements.measurement_risks]
  verification_status: verified
  access_level: metadata
  locator: Project citation and Data-and-Do-file folder listing inspected2026-10-04; readme.pdf, loan_main.do, loanmain.dta, market.dta and welfare files listed. README download redirected to ICPSR login; file contents and access/license conditions not inspected. Metadata verification only.
design_applications:
- paper: Indirect Effects of Access to Finance
  doi: 10.1257/aer.20220711
  journal: American Economic Review
  year: 2024
  research_question: How do credit access and competition jointly affect small Chinese firms and local-market welfare?
  population: 3173 surveyed firms drawn from over6000 active firms in78 markets; mainly retail with other activities.
  outcome: Firm revenue, profits, employment, borrowing and business practices; separate follow-up prices and consumer evaluations.
  data_used: [Baseline2013 and follow-up2015/2016 firm surveys, Partner-bank product borrowing records, Market office firm lists and employment, Separate2020 market/firm/consumer surveys]
  treatment_encoding: Own encouragement and same-market same-product competitor assignment share times Post; all-market other-peer share for borrowing diffusion; borrowing variables instrumented in Equation9.
  comparison: Assigned/unassigned firms across 0/50/80-percent markets with firm effects and explicitly modeled peer exposure.
  empirical_design: Two-stage randomized encouragement saturation design; panel reduced form and supplementary borrowing IV.
  assumptions: [Preserved randomized assignment, Adequate interference mapping, Outcome selection accounted for, Additional exclusion/model assumptions for borrowing IV and welfare]
  threats_addressed: [Baseline and exposure balance, Survivor balance and wave-specific effects, Alternative business outcomes and book-value sales]
  evidence_refs: [E1, E2, E3, E4, E5]
method_transfer: null
readiness_blockers:
- Obtain lawful replication access and inspect loan_main.do, data labels and original or deposited peer shares; establish full-roster versus survey-sample denominators and zero-peer handling before coding.
- Preserve both randomization levels and original strata; choose inference appropriate to78 markets rather than treating firms as independent saturation draws.
- Address shutdown, nonresponse and interference for the proposed outcome; borrowing IV needs an exclusion argument beyond randomized encouragement.
- Do not claim prospective registration, exact visit compliance, named geographic joins or model-free welfare; those are not established by the inspected sources.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Collateral and application costs restricted credit access for small firms in
the study city. In2013 a large commercial bank introduced a collateral-free
product for firms organized in local markets. Market managers supplied
information that helped the bank screen and monitor applicants [E1, reported].
The city and bank remain unnamed; the mechanism should not be relabeled as a
known national lending reform.

## What Changed

Assigned firms received monthly information and help applying for the new
loan. The bank still decided whether to lend, and unassigned firms remained
free to apply [E1, E2]. The experimentally assigned change is therefore
encouragement, not credit receipt. This distinction determines whether a
researcher can interpret a coefficient as an assistance effect or must defend
an additional borrowing-IV exclusion restriction.

## Implementation and Assignment

The experiment first randomized market saturation, then firms within each
treated market. County and size strata matter at the market level; employment
strata matter within markets. Only half the underlying firm population was
surveyed [E1]. The registry independently records computer randomization,
the37/10/31 market arms and1436 treated firms in the3173-firm survey [E2].
It reports August2013-August2014 intervention dates retrospectively.

## Why This Creates Empirical Variation

Own encouragement shifts a firm's access to information and application
assistance. Other firms' encouragement shifts both information transmission
and competitive pressure. The paper defines competitors through market and
specialized product, not all nearby firms [E1]. Its reduced form keeps own
and competitor exposure together; treating unassigned firms in encouraged
markets as unaffected controls would erase the spillovers being studied.
Direct and spillover analyses belong to one variation, not separate countable
policy entries [analytical inference].

## Identification Risks

Observed borrowing reflects applications and bank screening. A successful
first stage alone cannot rule out independent effects of officer advice
[analytical inference; E1]. Attrition and confirmed shutdown are distinct;
survivor balance does not by itself eliminate selection. The2020 follow-up
adds recalled2016 prices and consumer evaluations of firms found open, rather
than another complete administrative panel [E1, E3]. Market producer gains
and consumer welfare also differ: model-based welfare is not a directly
observed experimental outcome.

## Data Requirements

Recover firm assignment, market saturation and strata, then link firm-wave
outcomes and bank borrowing by stable IDs. For competitor exposure, preserve
product groups and the original denominator; do not recalculate shares only
on firms with observed outcomes. The ICPSR deposit supplies a concrete
code/data lead, but this task inspected its directory rather than downloaded
files [E5]. External administrative joins need a separate verified geographic
or firm crosswalk; the unnamed study location cannot be inferred from another
paper by the same authors.

## Evidence Notes

The final typeset paper, official appendix and investigator registry were
inspected. The registry was submitted May27,2022, after the experiment and
follow-ups, despite its interface label; it is retrospective documentation
[E2]. Its older public-data field says no, while the2024 replication deposit
lists data files [E5]. Neither statement proves current file access or field
coverage. The record is grounded institutional knowledge with conditional
research use, not certified reproduction or unconditional exogeneity.
