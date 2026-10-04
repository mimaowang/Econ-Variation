---
schema_version: 2
id: china-industrial-land-public-sale-transparency
name: China Industrial Land Public-Sale Transparency and Local Specialization Exposure
aliases: [Industrial land public-sale reform, Tian Wang Zhang land allocation and agglomeration, 工业用地招拍挂出让制度]
status: grounded
provenance:
  task_id: task-65fc3d2df567
scope:
  country: China
  regions: [Mainland China; inspected manuscript excludes Zhejiang from its main manufacturing sample]
  domains: [regional-economics, urban-economics, industrial-organization, development-economics]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: Chinese manufacturing establishments face a national industrial-land public-sale requirement with heterogeneous local implementation; the inspected application examines whether entry becomes more aligned with initial county-industry specialization.
identity:
  instrument: Public tender, auction and listing requirements for government-supplied industrial land, with a finite transition for eligible negotiated projects; not the minimum-price schedule.
  authority: State Council, Ministry of Land and Resources and Ministry of Supervision; municipal/county land departments administer supply and provincial departments supervise implementation.
  legal_identifiers:
  - 国发〔2006〕31号, dated 2006-08-31, provision V
  - 国土资发〔2007〕78号, dated 2007-04-04, provisions II-IV
  - 深府办〔2007〕80号, dated 2007-05-24, official local forwarding and reproduction of the national notice
  implementation_regime: >
    The 2006 State Council notice already requires industrial-land public sales.
    The April2007 implementing notice covers public sale or lease and permits
    qualifying legacy projects to sign negotiated contracts only through June30.
    It specifies pre-applications, industrial requirements, reserve prices,
    contract obligations and enforcement. July2007 is the end of this transition,
    not the first national announcement. Public format does not establish
    competitive bidding or eliminate administrative screening.
  assignment_mechanism: >
    Industrial use, government supply and project approval/contract history
    determine legal coverage and transition eligibility. The application's
    county-industry exposure instead combines initial specialization with
    measured prefecture implementation; it is not a legal random assignment.
  parent: null
  related_variations: [china-industrial-land-minimum-investment-intensity, china-county-industry-industrial-land-discount-border]
timeline:
  announcement: '2006-08-31'
  effective: '2007-04-04 implementing notice; public-sale mandate predates it'
  implementation_start: 2006
  implementation_end: null
  local_timing: >
    Qualifying negotiated contracts must be signed by2007-06-30. The inspected
    manuscript codes Post07=1 for all years2007-2010 and0 for2005-2006;
    this annual coding mixes transition and post-transition transactions in2007.
    Shenzhen's forwarding date is not every city's implementation date.
  anticipation: The2006 mandate and finite transition allow advance responses; omitting or separating2007 is a proposed sensitivity check, not a verified author specification.
  last_verified: '2026-10-04'
assignment:
  unit: County-industry-year; legal transaction coverage operates at project/parcel level.
  treated: Legally covered industrial parcels; analytically, county-industry pairs with greater initial specialization in prefectures with higher measured public-sale shares after reform.
  comparison_pool: Differently specialized pairs and differently implementing prefectures before/after2007. Lower public-sale share does not mean legal exemption or no exposure.
  rule: >
    For the legal rule, eligible legacy projects require a pre-2006-notice
    investment agreement fixing scope and price plus completed conversion and
    acquisition approvals; negotiated contracts must meet disclosure and June30
    deadline conditions. For the inspected design, Specialization_kj is the2004
    industry employment share within county k divided by the corresponding
    national share. Stringency_c is the standardized share of2008-2010
    industrial-land transactions sold publicly in supervising prefecture c.
    Interact Specialization with Post07 and Stringency, retaining lower-order
    specialization terms and the stated fixed effects.
  intensity: Continuous specialization-by-post-by-standardized-implementation exposure; implementation is measured after reform, not fixed before it.
  exemptions: [Qualifying legacy negotiated projects only through the prescribed transition, Original allocated-land conversions or use changes are handled under applicable land law, Zhejiang excluded by the manuscript as an early implementer rather than legally exempted]
  compliance: Observed sale-format shares measure implementation, not bidder counts or compliance with every screening/contract requirement. The manuscript describes negotiated pre-screening prices within public listing procedures.
  exposure_construction: >
    Aggregate2004 Census employment by stable county and industry to form the
    relative share. Classify industrial transactions by actual sale format and
    year, compute prefecture transaction-count public shares in2008-2010,
    standardize across the retained prefecture sample, and join counties to
    supervising prefectures. Establish a reproducible format dictionary,
    missing-format treatment and geographic/industry crosswalk before execution;
    the inspected text alone does not supply executable cleaning code.
  required_identifiers: [county code, supervising prefecture code, industry classification, year, land transaction identifier and sale format]
  spillovers: Entry can relocate between counties or industries; the main contrast concerns alignment of observed entrants, not net national creation of firms.
research_compatibility:
  outcome_domains: [manufacturing entry, industrial agglomeration, entrant employment, local economic development]
  affected_populations: [manufacturing establishments, county-industry groups, industrial land users]
  mechanism_channels: [public information about land supply, applicant screening, matching entrants to local specialization]
  best_for: [Studying changes in industrial location matching under transparent land supply, Comparing specialization-entry slopes across local implementation environments]
  not_good_for: [Treating implementation shares as randomly assigned, Estimating entry of all Chinese firms from an above-scale industrial survey, Interpreting a public listing as proof of a highest-bid competitive auction]
design:
  claim_type: reduced-form
  affordances: [National transition with heterogeneous implementation, Predetermined county-industry employment specialization]
  candidate_designs: [Continuous triple-interaction panel comparison]
  identifying_variation: Change in the specialization-entry relationship after2007 across prefectures with different measured implementation, conditional on the manuscript's fixed effects and controls.
  primary_strategy: County-industry-year panel regression with specialization, specialization-by-stringency, specialization-by-post and their triple interaction.
  estimand: Conditional change in the specialization-entry slope per standard-deviation increase in implementation; causal interpretation requires differential counterfactual trends and valid implementation measurement, not simply a national law.
  treatment_variable: Specialization_kj * Post07_t * standardized public-sale share_c.
  comparison_logic: Compare pre/post specialization-entry slopes across implementation environments; there is no randomly untreated China.
  estimation_notes: >
    The October2023 manuscript uses2005-2010, county-year and prefecture-industry-year
    effects, initial county-industry log employment, prefecture/industry two-way
    clustering and prefecture2008-2010 industrial-parcel-count weights.
    These are version-specific choices, not certified final-publication code.
  assumptions:
  - No omitted county-industry shocks jointly related to specialization, implementation and post-reform entry after controls.
  - Measured implementation is not itself driven by the outcome changes being attributed to reform.
  - Survey coverage and survivor-selection restrictions do not generate the estimated slope change.
  diagnostics:
  - Inspect pre-policy specialization-by-implementation slopes; non-rejection alone does not prove parallel trends.
  - Compare leave-one-county-out implementation and alternative sale windows described in manuscript section4.2.2.
  - Assess simultaneous minimum-price policy, stimulus credit and export-crisis exposure with appropriately interacted controls.
  - Test sensitivity to2007 transition coding, sample selection and weighting; these additional checks are proposals where not stated as performed.
threats:
- type: post-treatment-implementation
  basis: documented
  condition: Stringency is constructed from2008-2010 transactions; industrial development and policy compliance can jointly determine it. Prefecture aggregation or leave-one-out construction reduces mechanical overlap but does not establish exogeneity.
  evidence_refs: [E3]
  possible_diagnostics: [Inspect implementation determinants, Compare alternative windows and leave-one-county-out shares, Separate assignment from actual take-up]
- type: concurrent-policy-and-anticipation
  basis: documented
  condition: The2006 mandate predates Post07, minimum-price regulation overlaps, and the financial crisis/stimulus affect the post period. Their different exposures can survive aggregate fixed effects.
  evidence_refs: [E1, E2, E3]
  possible_diagnostics: [Respect legal and transaction clocks, Inspect interacted minimum-price and credit/export controls, Separate transition-year observations]
- type: selected-establishment-risk-set
  basis: documented
  condition: The manuscript retains county-industry cells with establishments in every year2005-2010, excludes Zhejiang, and relies on ASIF coverage thresholds. Reported founding year, especially2009 inferred from2010, is not simply first appearance in the survey.
  evidence_refs: [E3]
  possible_diagnostics: [Rebuild founding-year and survey-entry distinctions, Assess cells excluded by future survival, Do not generalize to below-threshold firms without data]
empirical_requirements:
  contract_version: 1
  population: Version-specific mainland manufacturing county-industry cells observed throughout2005-2010, excluding Zhejiang; not all newly registered businesses.
  observation_unit: County-industry-year
  geography_level: County nested in prefecture
  time_start: 2004
  time_end: 2010
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 3
  required_fields: [2004 county-industry and national employment, firm founding year, establishment location, manufacturing industry, annual establishment employment, industrial parcel sale format and transaction year, prefecture industrial transaction count, initial county-industry employment]
  required_identifiers: [stable county code, supervising prefecture code, harmonized industry code, establishment identifier, transaction identifier, year]
  treatment_key: [county-industry2004 specialization, prefecture2008-2010 public-sale share, observation year]
  treatment_source: National legal texts establish coverage; the inspected manuscript reconstructs exposure from2004 Economic Census, ASIF2005-2010 and landchina industrial transactions. Microdata and code require lawful access and reconstruction.
  measurement_risks: [Administrative/industry crosswalks, Post-reform public-sale denominator and missing-format coding, ASIF sales threshold and founding-year errors, Survivor-selection sample, Final-version coding not reconciled]
evidence:
- id: E1
  source_type: policy-document
  citation: State Council. 国务院关于加强土地调控有关问题的通知, 国发〔2006〕31号, dated2006-08-31; Heilongjiang government gazette reproduction.
  url: https://www.hlj.gov.cn/hlj/c108288/200708/c00_30642402.shtml
  date: '2006-08-31'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.announcement, timeline.implementation_start, timeline.anticipation]
  verification_status: verified
  access_level: official-document
  locator: Provision V and text signature2006-08-31; the web posting date2007-08-17 is not the instrument date. Public-sale and minimum-price requirements are both present.
- id: E2
  source_type: policy-document
  citation: Ministry of Land and Resources and Ministry of Supervision. 国土资发〔2007〕78号, dated2007-04-04; reproduced in Shenzhen government gazette alongside 深府办〔2007〕80号.
  url: https://www.sz.gov.cn/zfgb/2007/gb551/content/post_4983478.html
  date: '2007-04-04'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, identity.assignment_mechanism, timeline.effective, timeline.local_timing, assignment.treated, assignment.rule, assignment.exemptions, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: National notice II(1)-(3), III(3)-(9), IV and signature; transition eligibility and2007-06-30 deadline in II(2). Shenzhen forwarding datedMay24, with local provisions II-IV. Ministry commercial-law database separately reproduces the notice but credits a third-party legal provider; this gazette is the primary administrative reproduction.
- id: E3
  source_type: paper
  citation: Tian, Wenjia, Zhi Wang and Qinghua Zhang. Land Allocation and Industrial Agglomeration, manuscript dated October17,2023,74pages; later published as JDE171(2024),103351.
  url: https://www.cfrn.com.cn/uploads/master/file/20240423/662727d9e8270.pdf
  date: '2023-10-17'
  supports: [scope.china_relevance, identity.assignment_mechanism, timeline.local_timing, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.intensity, assignment.exemptions, assignment.compliance, assignment.exposure_construction, assignment.required_identifiers, assignment.spillovers, research_compatibility.outcome_domains, research_compatibility.affected_populations, research_compatibility.mechanism_channels, design.claim_type, design.affordances, design.candidate_designs, design.identifying_variation, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, design.assumptions, design.diagnostics, empirical_requirements.population, empirical_requirements.observation_unit, empirical_requirements.geography_level, empirical_requirements.time_start, empirical_requirements.time_end, empirical_requirements.minimum_frequency, empirical_requirements.minimum_pre_periods, empirical_requirements.minimum_post_periods, empirical_requirements.required_fields, empirical_requirements.required_identifiers, empirical_requirements.treatment_key, empirical_requirements.treatment_source, empirical_requirements.measurement_risks, design_applications.population, design_applications.outcome, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design, design_applications.assumptions, design_applications.threats_addressed]
  verification_status: verified
  access_level: full-text
  locator: Dated74page manuscript read directly in memory; sections2-4.2.3, pp9-26; equation1 pp16-17, equation2 pp21-22, sampling footnotes27-28 and38-42. Not final publisher typesetting. Interpretation of endogeneity and proposed additional diagnostics are analytical inference, not claimed author findings.
- id: E4
  source_type: paper
  citation: Zhi Wang author publication list, Tian Wang Zhang JDE171(2024)103351.
  url: https://zhiwang2013brownecon.weebly.com/publication.html
  date: 2024
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: Author publication entry with three authors, journal volume/year and article number; linked DOI10.1016/j.jdeveco.2024.103351. Does not verify final empirical coding.
- id: E5
  source_type: paper
  citation: Tian, Wang and Zhang (2024), Journal of Development Economics171,103351, DOI identifier linked by the inspected coauthor publication list.
  url: https://doi.org/10.1016/j.jdeveco.2024.103351
  date: 2024
  supports: [design_applications.doi]
  verification_status: reported
  access_level: metadata
  locator: DOI observed in the author publication hyperlink; direct DOI retrieval failed. Publication identity corroborated by E4, not final full-text access.
design_applications:
- paper: 'Land allocation and industrial agglomeration: Evidence from the 2007 reform in China'
  doi: 10.1016/j.jdeveco.2024.103351
  journal: Journal of Development Economics
  year: 2024
  research_question: Does transparent industrial-land supply change the alignment of new manufacturing establishments with local specialization?
  population: October2023 manuscript sample of2143counties in305prefecture/province-level cities, excluding Zhejiang; not independently reconciled to final publication.
  outcome: Any newly founded manufacturing establishment and log of entrant employment plus one, by county-industry-year.
  data_used: [2004 Economic Census employment, ASIF2005-2010 establishment information, Industrial land transactions from landchina]
  treatment_encoding: Initial specialization crossed with Post07 and standardized prefecture2008-2010 public-sale share; definitions attributed to the inspected manuscript.
  comparison: Changes in specialization-entry slopes across implementation environments, not untreated versus treated cities.
  empirical_design: Manuscript continuous triple-interaction panel regression with county-year and prefecture-industry-year effects.
  assumptions: [Conditional differential trends, No outcome-driven implementation measure, Comparable survey coverage and sample selection]
  threats_addressed: [Pre-policy slope checks, Minimum-price and stimulus/export interacted controls, Alternative implementation windows and leave-one-county-out shares]
  evidence_refs: [E3, E4, E5]
method_transfer: null
readiness_blockers:
- Conditional institutional/application lead, not turnkey causal identification; post-reform implementation must be justified for the new question.
- Final published methods and supplement remain uninspected; all numeric sample and coding choices here are expressly attributed to October2023 manuscript and require reconciliation for final-paper replication.
- Rebuild lawful microdata access, sale-format/missingness dictionary and stable county-industry joins; do not substitute registration addresses for establishment locations or survey appearance for founding year.
---

## Institutional Background

The institutional core is independently grounded: industrial land supplied by
government must use public procedures, with a time-limited exception for
qualified old projects [E1-E2]. This creates a land-information and allocation
mechanism distinct from minimum investment density and minimum-price schedules.
Those requirements coexist; separating records does not establish that their
effects can always be separated econometrically.

## What Changed

The2006 mandate precedes the April2007 transition notice. June30 closes the
qualified legacy-contract window; it is not the date all industrial projects
first faced regulation [E1-E2].

## Implementation and Assignment

Public listing also need not mean an unconstrained highest-bid auction. The
national notice specifies pre-applications and industry conditions [E2]; the
manuscript describes administrative screening and negotiated prices within
listing procedures [E3]. Preserve this distinction when interpreting competition
or productivity channels.

## Why This Creates Empirical Variation

The inspected manuscript asks whether new establishments become better aligned
with a county's existing industrial specialization, not whether all firms gain
equally from a national reform [E3]. Its execution-intensity measure is an
observed post-reform choice. The informative comparison is a change in the
specialization-entry slope across implementation environments, not a national
treated-versus-untreated experiment.

## Identification Risks

Differential industrial shocks can drive both compliance and entry. Neither an
insignificant pre-trend test nor province-level implementation aggregation rules
out that problem. The annual2007 treatment also mixes legally different
transaction windows. Assess these conditions before claiming a causal reform
effect [E1-E3; analytical inference].

## Data Requirements

Reconstruct relative employment shares from2004 Census and founding-year entry
from ASIF, then join actual transaction formats through stable county-prefecture
geography. Census/ASIF access is provider-controlled. Missing formats, founding
year corrections and the all-years-present industry restriction change the risk
set; a business-registration panel is not an automatic substitute [E3].

## Evidence Notes

This task inspected the national texts in official gazettes and the full dated
manuscript. Publication identity is confirmed by the coauthor's list [E4]. The
PKU final-PDF lead failed web retrieval and local TLS; indexed excerpts are not
substituted for final methods. Grounded refers to the institution and recoverable
version-specific comparison, not verified final replication or random exposure.
No paper, restricted microdata or credentials were stored.
