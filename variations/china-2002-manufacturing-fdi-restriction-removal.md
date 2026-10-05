---
schema_version: 2
id: china-2002-manufacturing-fdi-restriction-removal
name: China 2002 manufacturing FDI restriction removal using baseline firm products
aliases: [外商投资产业指导目录2002年修订, manufacturing foreign ownership liberalization, product-specific FDI restriction removal]
status: grounded
provenance:
  task_id: task-8e0378a6b66d
scope:
  country: China
  regions: [Mainland China]
  domains: [firm-economics, industrial-organization, development, foreign-direct-investment, trade, productivity]
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: Mainland manufacturing firms producing specified products faced different changes in foreign-investment restrictions in the2002 catalogue. An accepted ReStat paper uses baseline product descriptions to identify affected firms and study ownership and production.
identity:
  instrument: Removal of all catalogue FDI restrictions on a firm's pre-reform manufacturing products in the2002 revision.
  authority: State Development Planning Commission, State Economic and Trade Commission, and Ministry of Foreign Trade and Economic Cooperation, with State Council approval.
  legal_identifiers: [外商投资产业指导目录（1997年12月修订）, 三部门令第21号（2002）, 指导外商投资方向规定（国务院令第346号）]
  implementation_regime: Product-specific national investment approval and ownership conditions, including regional and export-related exceptions. This case serves the2002 removal contrast, not all WTO reforms, later catalogue waves, encouragement benefits alone, or realized acquisitions.
  assignment_mechanism: Baseline product activities determine whether a firm initially faces a restricted/prohibited category or explicit ownership condition and whether every such restriction disappears in2002. These provisions form one author-defined liberalization eligibility contrast; changes in outcomes or acquisition status do not create separate shocks.
  parent: null
  related_variations: [china-wto-accession-firm-performance, china-trade-policy-uncertainty, china-general-market-access-negative-list-provincial-pilot]
timeline:
  announcement: '2002-03-11'
  effective: '2002-04-01'
  implementation_start: 2002
  implementation_end: null
  local_timing: Order21 replaces the1997 catalogue from April1,2002. The paper assigns products observed in2001 and uses Post=1 for2002 onward in1998–2007. It reports a further minor revision effective2005; that is not another initial2002 cohort. Sector-specific accession commitments and project approvals can have different dates.
  anticipation: WTO accession in late2001 could affect preparations and product choice. The inspected paper uses2000 as its event-study reference and separately drops2001 or assigns2000 products; these are robustness choices, not a change in the formal2002 date.
  last_verified: '2026-10-05'
assignment:
  unit: Manufacturing product activity, inherited by a firm through its pre-reform product basket; annual firm outcomes.
  treated: Firms facing at least one catalogue restriction on products produced in2001 and for which all such restrictions disappear in2002. Encouraged status alone neither establishes nor excludes a binding ownership condition.
  comparison_pool: Ownership application compares initially restricted firms that remain restricted. Performance application instead compares liberalized firms with never-regulated firms, conditioning both groups on becoming fully foreign-owned after2001 and never being fully foreign-owned during1998–2001. These pools are not interchangeable.
  rule: Parse prohibited/restricted category and explicit JV, Chinese-control or relative-control provisions separately for each baseline product and location. Liberalized_i=1 only for an initially restricted firm with no remaining restriction on its baseline products under2002 rules. Interact this fixed status with I(year>=2002); preserve subsequent rule revisions separately.
  intensity: Binary author-defined removal of all restrictions. Foreign paid-in-capital share, full foreign ownership, majority ownership and share>=25percent are outcomes or application-specific conditions, not distinct policy shocks.
  exemptions: [Encouraged activities may retain ownership conditions, Relative Chinese control is not an aggregate50percent cap, Export-oriented projects may obtain approved relief, Central-western conditions may differ, Services and their phased opening schedules are outside this manufacturing case, Partly liberalized multiproduct firms are not automatically fully liberalized]
  compliance: Catalogue classification and project approval differ from observed foreign ownership. Article12 retains approval and filing procedures; formal relaxation does not establish immediate acquisition, compliance, or subsidy receipt.
  exposure_construction: Use up to three textual main-product descriptions from the firm survey, not a generic four-digit industry flag. Match descriptions to each historical catalogue within broad manufacturing sectors, preserve category and equity conditions, and apply manual product-list and location corrections. Freeze the baseline basket before calculating removal. Join stable firm identities across annual records; obtain HS6 links separately for WTO tariff and uncertainty controls.
  required_identifiers: [firm_id, year, baseline_product_description, catalogue_product_clause, province_or_location, historical_industry_code, HS6_for_trade_controls]
  spillovers: Liberalization can affect domestic rivals, suppliers and local markets. Still-restricted or never-regulated firms need not be indirectly unaffected; an own-firm ownership contrast is not a pure sector-wide welfare effect.
research_compatibility:
  outcome_domains: [foreign ownership share, full foreign ownership, firm output, total factor productivity, ownership restructuring, firm innovation, exporting]
  affected_populations: [mainland manufacturing firms in the industrial survey, initially restricted product producers, foreign-acquired manufacturers]
  mechanism_channels: [relaxing investment approval and ownership constraints, organizational restructuring, foreign investment entry, competitive spillovers]
  best_for: [firm-product-linked studies of foreign-investment liberalization, distinguishing permission changes from realized ownership, production effects with explicit acquisition selection]
  not_good_for: [generic WTO2001 dummy, encouragement treated as unrestricted ownership, four-digit industry treated as exact product exposure, city-average exposure without firm products, treating policy relaxation as an exclusion-valid IV by default, interpreting acquisition-selected results as an effect on every firm]
design:
  claim_type: reduced-form
  affordances: [common reform date with differential baseline product exposure, within-industry liberalized and comparison firms, explicit pre-reform product basket]
  candidate_designs: [firm-panel difference-in-differences, inverse-probability-weighted difference-in-differences, event study around the policy clock]
  identifying_variation: Some initially restricted baseline products lose all restrictions in2002 while others remain constrained; a second application changes the comparison and conditions on acquisition without changing the policy instrument.
  primary_strategy: The inspected accepted manuscript uses liberalized-by-Post DID for ownership with firm and two-digit sector-year effects. Its performance design uses acquired liberalized versus acquired never-regulated firms with firm and four-digit industry-year effects. Both apply pre-reform-covariate IPW and product-linked trade controls.
  estimand: Ownership application targets a conditional ATT of liberalization among initially restricted firms. Performance application targets the author's ownership-reoptimization contrast among subsequently acquired firms, not an unconditional policy ITT or an IV LATE; its causal interpretation additionally requires defensible acquisition selection.
  treatment_variable: Fixed liberalized_i from2001 products times I(year>=2002). The performance sample's treated_i uses the same removal rule but a never-regulated comparison and a post-policy full-acquisition restriction.
  comparison_logic: Preserve the ownership application's still-restricted control separately from the performance application's acquired never-regulated control. Both acquisition groups have ownership changes, but equivalent selection is an identifying claim, not an institutional fact.
  estimation_notes: Equation1 includes firm and two-digit sector-year effects; Equation2 uses firm and four-digit industry-year effects. Initial applied import tariffs1998 and US column2-minus-MFN tariff gaps1996 are linked to2001 products atHS6 and interacted with year effects. Logit IPW uses2000 log output/employment/wage, foreign share, age, export-sales share, import-input share and two-digit sector indicators; controls receive p/(1-p), off-support observations are excluded, and p is winsorized at its99th percentile. Import shares require a customs merge. Baseline standard errors cluster by firm. Table1 has94,817 observations; Table2 output9,671 and TFP8,811. These are accepted-manuscript sample counts, not promised counts for a new dataset.
  assumptions: [conditional counterfactual trends, sufficient common support, no residual product-targeted WTO or encouragement confounding, defensible baseline product and location assignment, outcome-specific spillover interpretation, additional selection assumptions for acquired-firm performance]
  diagnostics: [pre-reform leads and trend-sensitivity bounds, baseline2000 versus2001 basket, encouragement-by-year controls, detailed industry-year effects, matching-threshold and manual-correction audit, acquisition selection and attrition, restriction persistence and later revisions, product-level dependence in inference]
threats:
  - type: product-assignment-error
    basis: reported
    condition: AppendixA shows semantically similar descriptions can lie outside an exhaustive legal sublist. Industry coding also assigns different firms. A similarity threshold alone cannot certify exposure.
    evidence_refs: [E3]
    possible_diagnostics: [manual clause-level audit, separate unmatched from legally permitted, inspect regional exceptions, compare baseline baskets and matching cutoffs]
  - type: selected-liberalization-and-overlap
    basis: documented
    condition: Product selection is not random; encouragement can change concurrently and retained equity clauses occur within encouraged categories. WTO-related tariff changes and uncertainty reduction overlap the reform.
    evidence_refs: [E1, E3]
    possible_diagnostics: [encouragement interactions, product-linked tariff and uncertainty controls, support and pretrend checks, transparent selection covariates]
  - type: post-policy-acquisition-selection
    basis: inferred
    condition: Conditioning on future full foreign acquisition can change sample composition through the policy response. The paper's equally-selected-control argument and IPW on observables do not prove removal of unobserved or collider selection.
    evidence_refs: [E3]
    possible_diagnostics: [distinguish policy ITT from selected-acquirer ATT, pre-acquisition paths, survival and acquisition probabilities, initially foreign-owned subgroup, explicit selection sensitivity]
  - type: legal-versus-research-clock
    basis: reported
    condition: The paper cites an engine-equity commitment upon WTO accession while using the2002 catalogue clock; later2005 changes and project-level relief also complicate persistent exposure. This record does not verify every product's earliest legally effective opening.
    evidence_refs: [E1, E3, E4]
    possible_diagnostics: [retrieve specific accession and approval instruments for narrow products, omit2001, audit later-treated controls, compare actual ownership paths]
  - type: inference-and-interference
    basis: inferred
    condition: Many firms inherit the same product rule and can share shocks; firm clustering does not automatically capture product-level dependence or competitive spillovers.
    evidence_refs: [E3]
    possible_diagnostics: [product or policy-cell inference sensitivity, sector support, spillover-aware comparisons]
empirical_requirements:
  contract_version: 1
  population: Mainland manufacturing firms initially facing catalogue restrictions on their2001 products; the default application studies ownership without requiring subsequent acquisition.
  observation_unit: firm-year
  geography_level: mainland firm location with province-specific policy checks
  time_start: 1998
  time_end: 2007
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 2
  required_fields: [foreign paid-in-capital and total paid-in-capital, baseline main-product descriptions, historical catalogue category and ownership clauses, firm location, industry, year, baseline output employment wage age export-sales share and import-input share for published IPW, product-linked initial tariff and uncertainty controls]
  required_identifiers: [firm_id, year, baseline_product_description, province_or_location]
  treatment_key: [baseline_product_description, province_or_location, year]
  treatment_source: Official1997 and2002 catalogues plus the accepted manuscript AppendixA product matching and manual corrections. Author links a policy-data replication deposit at DOI10.7910/DVN/OXZ0SD; its contents were inaccessible in this audit, so it is a recovery route, not inspected code.
  measurement_risks: [firm-ID changes, incomplete or changing product strings, unmatched versus permitted coding, relative versus absolute control, conditional export and regional relief, acquisition and survey survival, post-policy recoding, later catalogue revisions]
design_profiles:
  - id: ownership
    label: Liberalization and foreign ownership among initially restricted firms
    outcome_domains: [foreign ownership share, full foreign ownership, majority foreign ownership]
    design_families: [difference-in-differences, event-study]
    when_to_use: The idea asks whether relaxed investment constraints change foreign ownership. Do not require or select firms on subsequent full acquisition for this profile.
    requirements:
      population: Mainland manufacturing firms restricted on at least one2001 product, with liberalized and still-restricted comparison firms.
      observation_unit: firm-year
      geography_level: mainland firm location
      time_start: 1998
      time_end: 2007
      minimum_frequency: annual
      minimum_pre_periods: 3
      minimum_post_periods: 2
      required_fields: [foreign paid-in-capital share, baseline product descriptions, pre-post catalogue restrictions, location, industry, year,2000 propensity covariates and product-level trade controls]
      required_identifiers: [firm_id, year, baseline_product_description, province_or_location]
      treatment_key: [baseline_product_description, province_or_location, year]
  - id: acquired-firm-performance
    label: Ownership reoptimization and performance among subsequently acquired firms
    outcome_domains: [firm output, total factor productivity, ownership restructuring]
    design_families: [difference-in-differences, event-study]
    when_to_use: The idea concerns production or productivity after ownership reoptimization and can explicitly defend selection into subsequent full acquisition. This profile does not estimate the effect for all producers.
    requirements:
      population: Firms never fully foreign-owned1998–2001 but fully foreign-owned after2001; liberalized firms compared with acquired firms never subject to any FDI policy over the sample.
      observation_unit: firm-year
      geography_level: mainland firm location
      time_start: 1998
      time_end: 2007
      minimum_frequency: annual
      minimum_pre_periods: 3
      minimum_post_periods: 2
      required_fields: [firm output or total factor productivity, annual foreign paid-in-capital share, baseline product descriptions, pre-post catalogue restrictions, all-year never-regulated status, location, four-digit industry, year,2000 propensity covariates and product-level trade controls, labor capital and material inputs plus deflators for the paper's TFP outcome]
      required_identifiers: [firm_id, year, baseline_product_description, province_or_location]
      treatment_key: [baseline_product_description, province_or_location, year]
evidence:
  - id: E1
    source_type: policy-document
    citation: Three ministries. Order21, 外商投资产业指导目录及附件, March11,2002.
    url: https://www.ndrc.gov.cn/xxgk/zcfb/fzggwl/200507/t20050707_960602_ext.html
    date: '2002-03-11'
    supports: [identity.instrument, identity.authority, identity.legal_identifiers, timeline.announcement, timeline.effective, assignment.rule, assignment.exemptions]
    verification_status: verified
    access_level: official-document
    locator: Promulgation paragraph; encouraged manufacturing sectionIII(18)1–5; restricted/prohibited manufacturing lists; attachment encouraged item5 on complete-vehicle50percent cap. Opening dates belong to2002, not the portal's2005 posting.
  - id: E2
    source_type: policy-document
    citation: SAT reproduction of 国发〔1997〕37号, Appendix1 外商投资产业指导目录（1997年12月修订）.
    url: https://fgk.chinatax.gov.cn/zcfgk/c102440/c5211626/content.html
    date: 1997
    supports: [identity.implementation_regime, assignment.treated, assignment.rule, assignment.exemptions]
    verification_status: verified
    access_level: official-document
    locator: Appendix1 complete encouraged/restrictedA/restrictedB/prohibited lists, especially restrictedB mechanical industry items1–2 whole vehicles and engines with Chinese control; encouraged mechanical item16's specific auto-component sublist. The accompanying import-equipment tax notice is a different instrument.
  - id: E3
    source_type: paper
    citation: Eppinger and Ma. Optimal Ownership and Firm Performance. CESifo10551, February20,2024 accepted peer-reviewed manuscript for ReStat108(3),817–832,2026; DOI10.1162/rest_a_01431.
    url: https://www.ifo.de/sites/default/files/docbase/docs/cesifo1_wp10551.pdf
    date: '2024-02-20'
    supports: [identity.assignment_mechanism, timeline.local_timing, timeline.anticipation, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.exposure_construction, design.primary_strategy, design.estimand, design.estimation_notes, empirical_requirements.required_fields, design_applications.treatment_encoding, design_applications.data_used]
    verification_status: reported
    access_level: full-text
    locator: Actual60-page PDF through web reader; titlep1 declares accepted peer-reviewed version; printedpp5–19 Sections2–4.3, Equations1–2, Tables1–2; AppendixA.1 ppI–V matching and TablesA.1–A.2; AppendixB.1–B.2 ppXII–XIV. Separate59-page EconStor2023 draft previously inspected is not relabeled the final source. Text and table rows inspected; screenshot rendering did not supply inspectable pixels.
  - id: E4
    source_type: policy-document
    citation: MOFCOM reproduction of 指导外商投资方向规定, State Council Order346.
    url: https://tfs.mofcom.gov.cn/swfg/dwtzhwstz/art/2011/art_5fbbb861c1a945a5b369838f683cdd7e.html
    date: '2002-04-01'
    supports: [identity.implementation_regime, assignment.rule, assignment.exemptions, assignment.compliance, timeline.effective]
    verification_status: verified
    access_level: official-document
    locator: Full body Articles1–17 read; Article4 categories, Article8 Chinese51percent and relative control, Articles10–11 approved export/central-western relief, Article12 approvals, Article16 HMT analogy, Article17 effectiveApril1. Reproduction metadata is not a separate2011 reform.
  - id: E5
    source_type: scholarship
    citation: Peter Eppinger author research list, ReStat publication and replication links.
    url: https://sites.google.com/site/petereppinger/research
    date: '2026-10-05'
    supports: [design_applications.doi, design_applications.journal, design_applications.year, empirical_requirements.treatment_source]
    verification_status: reported
    access_level: metadata
    locator: Journal Publications first entry gives108(3),817–832,2026 and links replication DOI10.7910/DVN/OXZ0SD. Deposit page/API and final Dropbox download inaccessible; no replication contents inspected or signed URL saved.
  - id: E6
    source_type: scholarship
    citation: ReStat article DOI linked from Eppinger's author publication list.
    url: https://doi.org/10.1162/rest_a_01431
    date: 2026
    supports: [design_applications.doi, design_applications.journal, design_applications.year]
    verification_status: reported
    access_level: metadata
    locator: Author research page Journal Publications first entry hyperlink explicitly targets this DOI and identifies the2026 volume/issue/pages. Direct DOI reader failed; evidence verifies citation identity, not an inspected publisher body.
design_applications:
  - paper: Optimal Ownership and Firm Performance An Analysis of China's FDI Liberalization
    doi: 10.1162/rest_a_01431
    journal: Review of Economics and Statistics
    year: 2026
    research_question: Does liberalization change foreign ownership, and how does ownership reoptimization relate to production and productivity?
    population: ASIP mainland manufacturers1998–2007; ownership analysis initially restricted firms, performance analysis subsequently fully foreign-acquired firms with distinct comparisons.
    outcome: Foreign ownership share and ownership-threshold indicators; log output and chain-linked Tornqvist TFP, plus reported supplementary outcomes.
    data_used: [NBS Annual Surveys of Industrial Production1998–2007, historical FDI catalogues, customs microdata for import-input shares, Imbert product-to-HS6 correspondence, Brandt output/input deflators, World Bank CPI, initial import tariffs and US tariff-gap data]
    treatment_encoding: All restrictions on the firm's2001 products removed in2002, interacted with a2002-onward indicator; separate acquisition-selected sample for performance, not an acquisition-date event clock.
    comparison: Ownership uses still-restricted firms; performance uses never-regulated firms also becoming fully foreign-owned after2001 and never fully foreign-owned before2002.
    empirical_design: IPW DID with firm and sector/industry-year effects, annual policy-clock interactions, product-linked trade controls and firm-clustered errors; accepted2024 manuscript inspected.
    assumptions: [conditional parallel trends, support and selection on observable baseline characteristics, additional acquisition-selection comparability for performance, valid product assignment and overlap controls]
    threats_addressed: [encouragement-by-year and detailed industry controls in ownership robustness,2000 baseline products and omission of2001, alternative similarity cutoffs, expanded propensity covariates, Rambachan-Roth relative-magnitude trend sensitivity in2024 Section4.3; none proves exclusion or eliminates acquisition selection]
    evidence_refs: [E1, E2, E3, E4, E5, E6]
method_transfer: null
readiness_blockers:
  - Conditional use requires the author-corrected product-policy lookup or an auditable reconstruction using both catalogues, exact product sublists and location exceptions. The replication DOI is known but its contents were not inspected; an industry-only flag is not an equivalent replacement.
  - Secure authorized industrial-survey/customs access and stable annual firm joins; retain missing products and unverified special approvals as uncertain instead of treating them as permitted.
  - Defend the selected-acquirer comparison before using the performance profile. The default ownership profile is different and must not inherit that selection silently.
  - Resolve earliest product-specific accession opening and later catalogue changes for precise timing or a new window; the served annual2002 proxy is not a certificate of every project's legal effective date.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

China's foreign-investment catalogue governed projects through detailed
activities, categories and ownership clauses. The1997 list restricted
vehicle and engine manufacture with Chinese control. The2002 list moves
engine manufacture into encouragement without that clause, while its
attachment retains a50percent foreign cap on complete vehicles [E1,E2].
This is an observable before/after institutional contrast; it is not
permission to label the entire transport-equipment industry liberalized.

Categories and equity provisions are separate. Encouraged investment can
remain JV-only or Chinese-controlled. Order346 defines aggregate Chinese
control as at least51percent and relative control by comparison with each
foreign investor, and allows certain approved export and regional relief
[E4]. Therefore, a paper's shorthand50percent ownership threshold is not
a universal translation of every control clause [E3,reported claim].

## What Changed

Order21 took effect on April1,2002 and replaced the1997 catalogue [E1].
The served variation is the paper's removal of all restrictions on baseline
manufacturing products, not encouragement alone, realized foreign purchase,
or a general WTO dummy. Restrictions, explicit caps and prohibitions are
checked jointly to establish that removal state [E3,reported claim].
Services opening schedules and subsequent revisions remain outside the
initial contrast. Different outcomes below count this mechanism once.

## Implementation and Assignment

Start with the products a firm made before the reform. For each product,
read the exact activity clause, any exhaustive sublist, ownership condition
and relevant location qualification in each catalogue. Check whether the
firm initially faced any restriction and whether all disappear. The
paper freezes2001 products and codes the post period from2002; it also
reports a2000-basket robustness check [E3,reported claim]. A multiproduct
firm still subject to one binding condition is not fully liberalized.

The appendix's semantic matching generates possible product-clause links;
it is not itself a legal interpretation. It uses Chinese word segmentation,
Tencent embeddings, within-sector comparisons and a preferred0.8 similarity
cutoff, followed by manual corrections applied across shared strings.
Car seats receive a high similarity score to key auto components but are
outside the enumerated list and are manually corrected to permitted.
Location-dependent clauses require location corrections too
[E3,reported claim]. Do not collapse an unmatched description into
verified permitted status. The public replication route is preserved,
but its corrected lookup has not been inspected [E5,reported claim].

## Why This Creates Empirical Variation

The ownership application compares initially restricted firms whose
products were liberalized with firms remaining restricted. Firm effects,
sector-year effects, product-linked trade controls and IPW condition that
contrast; they do not make policy selection random [E3,reported claim].

For output and productivity the paper asks a different question. It keeps
firms becoming fully foreign-owned after2001 and compares liberalized
acquirers with never-regulated acquirers in the same industries. This
seeks the effect of releasing constrained ownership rather than all
benefits of foreignness. Both groups face acquisition selection. The
policy clock remains2002 rather than each acquisition date
[E3,reported claim]. Use the separate profiles because their populations,
comparison firms and outcome requirements differ.

## Identification Risks

WTO-related tariffs, uncertainty and encouragement overlap liberalization.
The paper reports specific controls and ownership robustness, not proof
that every product-specific confound disappears [E3,reported claim].
Its2024 accepted version also applies relative-magnitude parallel-trend
sensitivity; this is additional evidence, not a guarantee for another
outcome or sample. The paper cites an engine commitment upon accession,
whereas its research clock uses2002. A narrowly dated engine study needs
that primary commitment and actual approval history, not a silent choice
between2001 and2002 [analytical inference].

Conditioning on future acquisition can select on a policy consequence.
The claim that acquired comparison firms remove cherry-picking remains an
identifying argument. IPW balances observed baseline characteristics but
does not settle unobserved selection [analytical inference]. Restricting
post-reform observations to firms still producing liberalized products is
also a selected robustness sample, not a cure for endogenous switching.
Firm-clustered errors and insignificant leads are not product-level
independence or causal certification.

## Data Requirements

The actual study uses mainland manufacturing firms from ASIP1998–2007,
covering SOEs and above-threshold other firms. Foreign paid-in-capital
includes Hong Kong, Macao and Taiwan investors; firms remain mainland
research objects [E3,reported claim]. Preserve that definition rather than
changing investor origin to fit the collection's geography.

Annual firm continuity, baseline product strings, location, historical
industry codes and capital shares are indispensable. Published IPW also
uses a customs merge for import shares and a separate product-to-HS6 bridge
for trade controls. Productivity needs inputs and deflators; the paper's
chain-linked index is not a direct physical-productivity measure. A city
panel or industry label alone cannot reconstruct this firm-product
contrast. Dataset access and reconstruction belong in a linked data
knowledge project; this record preserves the research requirements.

## Evidence Notes

Earlier work correctly blocked admission without the1997 list or a
recoverable assignment bridge. The SAT appendix now supplies that list,
and the accepted manuscript supplies a specific product-level mapping and
two explicit research comparisons. These close the institutional and
design knowledge chain sufficiently for conditional matching. They do not
deliver an inspected executable crosswalk, unrestricted microdata, or
verified earliest opening dates for every activity.

The2023 EconStor draft and2024 accepted version are distinct sources.
The latter explicitly identifies its peer-reviewed acceptance status;
the author lists the eventual2026 issue [E3,E5,reported claim]. Earlier
industry-level RIE export work remains in the source ledger: its
Sheng-Yang industry coding and entry definitions are not silently upgraded
to this product-level design. No copyrighted paper or firm observations
are redistributed here.
