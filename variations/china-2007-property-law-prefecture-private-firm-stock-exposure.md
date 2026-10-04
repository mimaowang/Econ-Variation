---
schema_version: 2
id: china-2007-property-law-prefecture-private-firm-stock-exposure
name: China 2007 Property Law and Predetermined Prefecture Private-Firm Stock Exposure
aliases:
- Cheng Gawande property protection and enterprise entry
- 物权法与改革前地级市私营企业存量占比
status: grounded
provenance:
  task_id: task-d099ce0e0b2b
scope:
  country: China
  regions: [Mainland China; prefecture-level application]
  domains: [development-economics, firm-entry, firm-dynamics, regional-economics, property-rights, institutions]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    A national property-rights framework is studied through differential
    enterprise entry and cohort survival across Chinese prefectures with
    different pre-reform private-firm shares. Exposure is a historical regional
    composition proxy, not a local pilot designation or observed enforcement.
identity:
  instrument: >
    The 2007 Property Law's national property-rights framework, including
    private-property and enterprise-asset protections, interacted with the
    2005 proportion of extant firms privately owned in a prefecture. The
    exposure captures a bundled legal reform, not an isolated collateral
    provision or a separately identified expropriation channel.
  authority: National People's Congress enacted the law; courts and other competent authorities apply the statutory remedies and procedures.
  legal_identifiers:
  - 中华人民共和国物权法, adopted 16 March 2007
  - Property Law Articles 4, 32-38, 42, 64-68 and 247
  implementation_regime: >
    National enactment and effectiveness in 2007, with the inspected author
    application allowing an anticipatory response from 2006. Legal protection
    is not an appointment of treated prefectures. This record documents the
    1998-2012 application window, not current law or later Civil Code changes.
  assignment_mechanism: >
    Common legal reform interacted with predetermined prefecture ownership
    composition. The authors interpret lower private-firm penetration as
    greater prior insecurity and therefore larger potential gains. Neither
    that interpretation nor the composition is a statutory assignment rule.
  parent: null
  related_variations: [china-2007-movable-collateral-menu-expansion]
timeline:
  announcement: '2007-03-16 (formal law adoption)'
  effective: '2007-10-01'
  implementation_start: '2007-10-01'
  implementation_end: null
  local_timing: >
    No staggered prefecture start is claimed. The January2021 manuscript's
    equation1 codes Post=1 from2006 and0 through2005. This is its anticipation
    encoding, not the law's effective date. Sample end2012 is not termination.
  anticipation: >
    Section2.1 and footnote3 explain the2006 contrast by drafting expectations.
    That account is source-reported. The2005 baseline and a national annual
    switch do not eliminate earlier anticipation or differential expectations.
  last_verified: '2026-10-04'
assignment:
  unit: Prefecture-year; entry and survival outcomes aggregate firm incorporation cohorts.
  treated: Prefectures with lower2005 private-firm shares have greater hypothesized reform exposure; there is no treated cutoff in the inspected main specification.
  comparison_pool: Higher-share prefectures under the same law, compared through within-prefecture changes and conditional regional trends; they are not legally untreated.
  rule: >
    For each prefecture i, count firms established by2005 that remained open
    as of2005. PFRatio_i is privately owned firms in that stock divided by
    all firms in the corresponding stock. Fix this share and interact it with
    1[year>=2006] in the inspected January2021 specification. Legal coverage
    and timing come from the law; the share and annual switch come from the
    authors. A smaller ratio means stronger hypothesized exposure, so do not
    reverse the coefficient interpretation or substitute a private-entry share.
  intensity: Continuous share in[0,1], used directly rather than a median split. It is a proxy for prior constraints, not measured property violations or a legal benefit amount.
  exemptions:
  - The law protects state and collective property as well; SOEs are not legally exempt or an automatically unaffected control group.
  - The draft excludes subsidiaries and observations lacking identifiable prefecture, industry, firm type or registration capital. These are research exclusions, not law exemptions.
  - The source covers broad industries; a non-agricultural research sample must be explicitly defined rather than attributed to the authors' full population.
  compliance: Statutory rights and remedies do not show actual local enforcement, court access or cessation of expropriation. The private-firm share does not measure take-up or compliance.
  exposure_construction: >
    Obtain a lawful historical registry extract including pre1998 establishments,
    establishment and closure histories, ownership types and prefecture/province
    identifiers. Reconstruct the complete2005 stock before constructing
    1998-2012 entry cohorts; a births-only1998-2012 extract is insufficient.
    Harmonize administrative boundaries across stock and cohorts, preserve
    private/SOE/foreign categories, and join the fixed ratio on prefecture ID.
    Establish a documented historical ownership coding if a current registry
    extract cannot recover2005 types. Do not silently recompute the share from
    current survivors or ASIF manufacturing firms.
  required_identifiers: [firm_id, prefecture_id, province_id, establishment_date, observation_year]
  spillovers: Firm relocation, product-market competition and ownership substitution can affect higher-share places and SOEs. A relative prefecture response is not a national net entry gain.
research_compatibility:
  outcome_domains: [Private firm incorporation, Entry-cohort survival counts, Shareholder composition, Enterprise development]
  affected_populations: [Mainland registered enterprises and their prefectures; surviving entry cohorts]
  mechanism_channels: [Property security, Enterprise asset control, Entry incentives, Reallocation and competition]
  best_for:
  - Regional enterprise-entry questions with a reconstructable pre-reform ownership stock and consistent registration cohorts.
  - Conditional differential reform responses rather than a national before-after effect or a pure single-channel estimate.
  not_good_for:
  - Treating the law as the first legal recognition of private property or as a constitutional amendment.
  - Calling the initial ownership share random or treating higher-share places as unexposed.
  - Identifying actual production, productivity or employment solely from incorporation and paid-in capital.
  - Measuring survival probabilities by using survivor counts without conditioning on cohort size.
design:
  claim_type: reduced-form
  affordances: [National legal dates, Predetermined regional composition, Repeated prefecture cohorts, Exposure-by-year diagnostics]
  candidate_designs: [Continuous-exposure difference-in-differences, Exposure-by-year event study]
  identifying_variation: Differential changes in prefecture enterprise outcomes associated with fixed2005 private-firm penetration around the reform and its anticipatory period.
  primary_strategy: >
    January2021 manuscript equation1 regresses prefecture-year outcomes on
    PFRatio_i times Post_t, prefecture and year effects, province-year effects,
    and trends interacted with log1p average new firms in2002-2005 and2000
    nighttime-light growth. Equation2 interacts the ratio with years, omitting2005.
  estimand: Conditional post-period change in an outcome per unit of baseline private-firm share; a negative entry coefficient means larger increases at lower shares. This is not an unconditional national average treatment effect.
  treatment_variable: PFRatio_i times1[year>=2006] in the inspected January2021 author version; effective-law dates remain separately recorded.
  comparison_logic: Compare within-prefecture changes across continuous baseline composition, controlling common and province-level time changes and specified baseline trends; both low- and high-share places face the same national statute.
  estimation_notes: >
    The draft reports341prefectures and4545prefecture-years,1998-2012; it
    clusters by prefecture and year. Entry and surviving-cohort outcomes use
    log1p counts. There are only15annual clusters, so inference merits
    sensitivity. Full final2024 methods and executable replication were not
    inspected; this record does not certify that every draft specification
    survived publication. Published appendix checks are attributed separately.
  assumptions:
  - Conditional counterfactual outcome trends do not vary with the baseline ownership share in the same way as the attributed reform response.
  - The baseline share is a defensible exposure proxy, not just industrial structure or a proxy for concurrent local reforms.
  - Incorporation, closure recording, ownership classification and prefecture mappings remain comparable over time.
  - Anticipation and inter-prefecture relocation do not invalidate the chosen contrast.
  diagnostics:
  - Inspect exposure-by-year coefficients before2006 and sensitivity to an explicit2006 anticipation period and2007 transition; label new timing specifications as adaptations.
  - Compare baseline-share definitions and common-support regions, without selecting the year that gives the strongest result.
  - Examine registration changes, ownership switching, cohort follow-up and reallocation to neighboring places.
  - Evaluate province-specific overlapping reforms and inference with few year clusters; nonrejection is not causal certification.
threats:
- type: endogenous_baseline_composition
  basis: reported
  condition: The draft recognizes historical political-economic determinants of private-firm penetration. Predetermination does not establish independence from later growth or reform shocks.
  evidence_refs: [E2]
  possible_diagnostics: [Exposure-specific pre-trends, Alternative baseline years, Industrial composition and common-support analysis]
- type: anticipation_and_bundled_legal_channels
  basis: documented
  condition: The application starts its post contrast in2006, before legal adoption/effectiveness. The law includes multiple rights and security-interest provisions; the regional proxy does not isolate a single channel.
  evidence_refs: [E1, E2]
  possible_diagnostics: [Separate anticipation from legal transition, Explicitly define the estimand, Avoid causal channel claims from the same interaction]
- type: concurrent_changes_and_spatial_reallocation
  basis: reported
  condition: Published appendix OA3 and OA5 examine selected confounders and neighboring exposure; those checks do not remove every correlated policy or relocation effect.
  evidence_refs: [E3]
  possible_diagnostics: [Outcome-relevant policy chronology, Neighbor and relocation sensitivity, Separate local entry from aggregate creation]
- type: registration_survival_and_historical_stock
  basis: documented
  condition: Incorporation is not verified operation. Survivor counts combine entry volume with persistence; retrospective registry types and incomplete closure histories can change both exposure and outcomes.
  evidence_refs: [E2]
  possible_diagnostics: [Document registry vintage, Fixed historical ownership crosswalk, Equal cohort follow-up, Compare conditional survival rates explicitly]
empirical_requirements:
  contract_version: 1
  population: Mainland prefectures and registered firms with consistent historical ownership, location and establishment information; identify any sector restriction separately.
  observation_unit: prefecture-year
  geography_level: prefecture
  time_start: 1998
  time_end: 2012
  minimum_frequency: annual
  minimum_pre_periods: 4
  minimum_post_periods: 3
  required_fields:
  - Firm establishment dates, closure history sufficient to reconstruct the extant2005 stock, historical private/SOE/foreign type, subsidiary status and paid-in-capital completeness.
  - Prefecture and province crosswalks valid for the baseline stock and annual entry cohorts.
  - Annual private-entry counts and baseline trend controls;2002-2005 entry counts and2000 nighttime-light growth for the inspected specification.
  required_identifiers: [firm_id, prefecture_id, province_id, observation_year]
  treatment_key: [prefecture_id, observation_year]
  treatment_source: Official2007 law supplies national legal coverage and dates; January2021 manuscript equation1 and footnote6 supply the fixed2005 stock ratio and anticipatory annual encoding.
  measurement_risks:
  - Lawful registry access and its historical vintage are necessary; this record does not provide restricted microdata or assert open access.
  - ASIF or a current-survivor registry cannot silently replace the denominator covering all extant firms in2005.
  - Firm registration and closure dates need not equal economic operation and shutdown; distinguish re-registration and relocation.
  - Employment is optional and unreliable in the inspected registry; the draft reports one-third missing and strong heaping.
design_profiles:
- id: cohort-survival
  label: Entry cohorts surviving beyond two or three years
  design_families: [Continuous-exposure difference-in-differences]
  when_to_use: Use when registry follow-up covers each entry cohort for the full survival horizon; counts are not conditional survival probabilities.
  outcome_domains: [Entry-cohort survival counts]
  requirements:
    population: Registered entry cohorts in mainland prefectures with complete two- or three-year closure follow-up and reconstructable2005 ownership stock.
    observation_unit: prefecture-by-entry-cohort-year
    geography_level: prefecture
    time_start: 1998
    time_end: 2012
    minimum_frequency: annual
    minimum_pre_periods: 4
    minimum_post_periods: 3
    required_fields: [Baseline ownership stock, Incorporation and closure dates, Common follow-up endpoint beyond2015 for the final cohort, Subsidiary/sample exclusions, Cohort size, Baseline trend controls]
    required_identifiers: [firm_id, prefecture_id, province_id, entry_cohort_year]
    treatment_key: [prefecture_id, entry_cohort_year]
evidence:
- id: E1
  source_type: policy-document
  citation: National People's Congress, 中华人民共和国物权法, original2007 text reproduced by the Beijing government.
  url: https://www.beijing.gov.cn/zhengce/zhengcefagui/qtwj/200710/t20071026_780682.html
  date: '2007-03-16'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.announcement, timeline.effective, timeline.implementation_start, assignment.rule, assignment.exemptions, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: Adoption heading; Articles4,32-38,42,64-68,247 inspected2026-10-04. Supports legal rights and national coverage/dates, not the paper's ownership-share proxy or observed enforcement.
- id: E2
  source_type: paper
  citation: Hua Cheng and Kishore Gawande, Live Capital in China - Property Rights Security and Firm Births, January31,2021 author manuscript,52PDFpages, CFRN deposit.
  url: https://www.cfrn.com.cn/uploads/fileupload/0bc0341ca76f4775a0d052f936ec152a/paper/1d2f1235c7b8445eb6610f565bd3b5ed.pdf
  date: '2021-01-31'
  supports: [identity.assignment_mechanism, timeline.local_timing, timeline.anticipation, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.intensity, assignment.exposure_construction, design.primary_strategy, design.treatment_variable, design.estimation_notes, empirical_requirements.treatment_source, empirical_requirements.measurement_risks, design_applications.treatment_encoding, design_applications.data_used]
  verification_status: reported
  access_level: full-text
  locator: Cover; Section2.1/footnote3 printedp5; Sections4.1-4.2 printedpp11-19, equation1 and footnote6 pp14-15; Section5.1/equation2 pp19-20. Inspected in memory; PDFp16 visually confirms equation1 and2006 post wording. Author2021 coding, not a verified final2024 replication.
- id: E3
  source_type: appendix
  citation: Cheng and Gawande, Bringing Dead Capital to Life - Property Rights Security in China, JLE67(2),2024, published Online Appendix.
  url: https://www.journals.uchicago.edu/doi/suppl/10.1086/727444/suppl_file/10532Appendix.pdf
  date: 2024
  supports: [design.diagnostics, threats.condition, assignment.spillovers, design_applications.threats_addressed]
  verification_status: reported
  access_level: appendix
  locator: OA1-5 and OA7, PDFpp2-5 inspected2026-10-04. Confounder, alternate baseline, neighboring and industry checks; not evidence that the linked replication ZIP or final main methods were inspected.
- id: E4
  source_type: policy-document
  citation: 中华人民共和国宪法修正案,14March2004, original text reproduced by Heyuan Yuancheng procuratorate from the NPC.
  url: https://www.ycqrmjcy.gov.cn/show-44-220.html
  date: '2004-03-14'
  supports: [identity.implementation_regime, timeline.anticipation, research_compatibility.not_good_for]
  verification_status: verified
  access_level: official-document
  locator: Adoption heading and amendment Articles21-22 inspected2026-10-04. Earlier nonpublic-sector/private-property protection; distinguishes2004 constitutional amendment from2007 statute.
- id: E5
  source_type: paper
  citation: Hua Cheng and Kishore Gawande, Bringing Dead Capital to Life - Property Rights Security in China, Journal of Law and Economics67(2),265-294,2024, publisher metadata.
  url: https://doi.org/10.1086/727444
  date: 2024
  supports: [design_applications.paper, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: Publisher heading, authors, volume67 issue2 and pages265-294 inspected2026-10-04; issue datedMay2024 and page postedJuly15,2024. No final main-body methods inspected.
design_applications:
- paper: Live Capital in China - Property Rights Security and Firm Births (January2021 manuscript; subsequently Bringing Dead Capital to Life - Property Rights Security in China)
  doi: 10.1086/727444
  journal: Journal of Law and Economics; final publication2024, detailed application here belongs to the inspected2021 precursor
  year: 2024
  research_question: Does national property-rights reform differentially change enterprise entry and entry-cohort persistence across prefectures with different pre-reform ownership composition?
  population: Author2021 registry sample1998-2012;341prefectures,4545prefecture-years after exclusions. Broad sectors, not only manufacturing or the owner's prospective non-agricultural restriction.
  outcome: Log1p private-entry counts, counts of entry-cohort firms surviving beyond two or three years, and shareholder-composition counts. Survivor counts are not survival rates.
  data_used: [SAIC enterprise registry with establishment/closure/ownership/shareholder histories, NOAA nighttime lights for the2000 baseline control, Prefecture and province mappings]
  treatment_encoding: January2021 equation1 and footnote6 use2005 extant private/all firm ratio times post2006; national legal start isOctober2007. Published OA checks are reported separately, not used to assert uninspected final treatment-year coding.
  comparison: Lower- versus higher-baseline-share prefectures through within-place changes, province-year effects and baseline outcome trends; all face the law.
  empirical_design: Continuous exposure DID and ratio-by-year diagnostics with2005 omitted; prefecture/year two-way clustering in the inspected author version.
  assumptions: [Conditional exposure-specific parallel trends, Defensible baseline-share proxy, Comparable registry histories, No confounding differential policy or anticipation response]
  threats_addressed: [Draft equation2 exposure-specific pre-trends, Published OA1 outlier exclusions, OA2 selected geographic balance, OA3 selected contemporary policies, OA4 alternative baseline years, OA5 neighboring exposure]
  evidence_refs: [E1, E2, E3, E4, E5]
method_transfer: null
readiness_blockers: []
---

## Institutional Background

Private property did not acquire legal protection for the first time in2007.
The2004 constitutional amendment already strengthened that protection [E4,
verified]. The2007 statute codified property rights and remedies, including
enterprise assets [E1, verified]. A claim that it amended the Constitution or
abolished every earlier protection would misdescribe the institution.

## What Changed

The law supplies one national legal framework. Cheng and Gawande study a
differential regional response using the pre-existing private-enterprise stock
[E2, reported]. This record concerns that exposure construction, not every
clause as a separate shock. It is related to, but not a copy of, the existing
movable-collateral case: that case uses firm inventories/receivables and a
specific security-interest opportunity; this one uses prefecture ownership
composition and enterprise cohorts. Neither separates every channel of the
same law [analytical inference].

## Implementation and Assignment

Reconstruct all firms open as of2005 and their historical types. The numerator
is private firms; the denominator includes the corresponding full firm stock.
Do not replace it with firms newly incorporated in2005. Fix this ratio, join
it to prefecture-year outcomes, and retain the author's2006 anticipation
contrast separately from March adoption and October2007 effectiveness [E1,
verified; E2, reported]. Higher-share places are comparators, not exempt places.

## Why This Creates Empirical Variation

The research interpretation is that lower private-sector penetration reflects
greater prior constraints and a larger potential response. It is not a
government-assigned intensity or proof of property insecurity. A negative
interaction coefficient implies larger increases in lower-share places under
the conditional comparison, not a negative effect of legal protection or an
unconditional national average effect [E2, reported; analytical inference].

## Identification Risks

Ownership composition embeds prior institutions and industrial structure.
Differential trends,2004 legal changes, anticipation and contemporary reforms
can mimic the attributed response. Reported diagnostics address selected
alternatives; they do not certify exogeneity [E2-E4; analytical inference].
The bundle also includes collateral-related channels, so a pure expropriation
mechanism cannot be inferred from the same coefficient.

## Data Requirements

The core connection is historical registry firms to consistent prefecture and
province IDs, then the fixed baseline share to annual cohorts. Access must
cover pre1998 establishments for the2005 stock. Closure histories beyond2015
are needed for the last cohort's full three-year follow-up [E2, reported].
Incorporation measures formal entry, not necessarily production. A count of
surviving entrants mixes cohort size with persistence; a conditional survival
rate is a different outcome. Employment, exports or assets require separate
measurement and cannot be recovered merely from registration capital.

## Evidence Notes

The legal framework is grounded in inspected official texts. Detailed coding
is explicitly the January2021 precursor; the accessible published2024 appendix
establishes the cited checks, not all final methods. The linked replication ZIP
returned403 and was not inspected. Thus this record supports conditional
research matching, not a claim of exact final-paper replication. Final-version
reconciliation is needed before reproducing its published estimates. Related
property-law candidates remain source-version-specific staging records; their
event/asset/bankruptcy contrasts must be reconciled here or against the existing
collateral case rather than generating duplicate ready entries.
