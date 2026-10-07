---
schema_version: 2
id: china-pilot-ftz-preexisting-production-location-exposure
name: China pilot FTZ rollout exposure of pre-existing production establishments
aliases: [自贸试验区设立, pilot free trade zone establishment, FTZ production-location exposure]
status: grounded
provenance:
  task_id: task-7d09473e1860
scope:
  country: China
  regions: [Mainland China]
  domains: [regional-economics, urban-economics, development, firm-performance, industrial-economics, trade]
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: National pilot FTZ designation changes the institutional environment of mainland production establishments. A published firm study uses pre-implementation physical operations inside designated subzones, rather than a province-wide or host-city indicator.
identity:
  instrument: State Council pilot free-trade-zone designation and geographically specified expansion,2013–2020.
  authority: State Council designation; provincial and zone authorities implement differentiated reforms.
  legal_identifiers: [国发〔2013〕38号, 上海市人民政府令第7号, 国发〔2020〕10号]
  implementation_regime: Designated subzones receive a bundle of administrative and trade-investment reforms. This record serves the first exposure of existing production locations, including later-added territory; it is not a universal tax exemption or the nationwide general market-access negative list.
  assignment_mechanism: Central administrative choice of designated territory and rollout date; the firm application freezes production presence one year before local implementation and excludes post2012 in-movers. Neither central selection nor a firm's inability to choose designation establishes random assignment.
  parent: null
  related_variations: [china-general-market-access-negative-list-provincial-pilot]
timeline:
  announcement: Shanghai overall plan signed2013-09-18; later author cohorts and expansions are documented in Appendix TableA1. Approval, announcement and operation are distinct dates.
  effective: Shanghai management measures effective2013-10-01. The2020 new-zone/expansion notice is signed2020-08-30; author TableA1 labels its cohort September2020. Do not replace all local operative dates with notice dates.
  implementation_start: 2013
  implementation_end: null
  local_timing: Author TableA1 lists Shanghai September2013; Tianjin/Fujian/Guangdong and Shanghai expansion April2015; seven zones April2017; Hainan October2018; Shanghai Lingang July2019; six new zones August2019; Beijing/Hunan/Anhui and Zhejiang expansion September2020. These months are author-reported, not independently verified legal onsets for every parcel. For annual use preserve the first relevant territory's cohort year; expansion does not reset old-territory treatment.
  anticipation: Approval and preparation can precede the author's cohort year. Restricting movers does not eliminate anticipation by incumbents or governments.
  last_verified: '2026-10-07'
assignment:
  unit: Official FTZ subzone territory; pre-existing production-establishment presence mapped to a firm in the inspected application.
  treated: Firms with operational production presence inside the relevant designated subzone one year before its local implementation. The paper reports4707 treated firms; ownership or political connection is a heterogeneity attribute, not assignment to a separate shock.
  comparison_pool: First application matches4707 firms never receiving FTZ treatment in the sample, within the same or adjacent provinces. Second application retains only4707 eventual beneficiaries and uses timing differences; later-treated firms supply untreated comparisons only before their own onset.
  rule: For a documented historical production location in a designated territory, freeze eligibility at local cohort year minus1 and turn FTZ exposure on from that cohort year. Apply the reported post2012 in-mover exclusion separately; do not substitute current headquarters or province membership.
  intensity: Binary institutional-environment exposure. This is not actual receipt of a grant or each component's legal eligibility, and multiple facilities can require an explicit aggregation convention.
  exemptions: [Outside-zone firms do not inherit direct treatment merely from host-city or province membership, Original bonded-zone status is not pilot FTZ treatment, General market-access and foreign-investment negative lists are separate instruments, Post2022 expansions are outside the inspected firm panel]
  compliance: Actual benefits and enforcement vary by firm and measure. Physical presence is the author's exposure proxy; specific legal benefits may require registered-in-zone status or other eligibility.
  exposure_construction: Build a subzone-version/cohort table from the identified plans and TableA1; link dated production addresses to its territory, then firm_id/year to outcomes. Preserve expansion parcel onset and original parcel onset separately. The author reports manual address verification but supplies no inspected geocoder or multi-establishment tie-breaking rule. Require these conventions for a new implementation rather than assuming headquarters identifies all plants.
  required_identifiers: [firm_id, establishment_id, year, historical_production_address, address_reference_year, subzone_id, boundary_version, cohort_year]
  spillovers: Outside-zone firms can be exposed indirectly through supply chains, workers and investment. Same/adjacent-province matching does not guarantee an unexposed comparison.
research_compatibility:
  outcome_domains: [firm productivity, firm profitability, exports, firm investment, industrial upgrading]
  affected_populations: [mainland incumbent firms with recoverable production locations]
  mechanism_channels: [administrative reform, investment facilitation, trade logistics, resource access]
  best_for: [annual incumbent-firm outcomes with historical production-location evidence, comparing designated and credibly unexposed territory]
  not_good_for: [whole-province FTZ exposure, postpolicy entrants without the incumbent-address contract, exact component tax effects, quarterly effects without reconciled data frequency, treating political connection as randomly assigned]
design:
  claim_type: reduced-form
  affordances: [staggered first exposure across designated territories, matched never-treated firms, not-yet-treated comparisons]
  candidate_designs: [cohort-specific difference-in-differences, event study, matched-panel difference-in-differences]
  identifying_variation: Different onset years for pre-existing firms physically located within designated subzones; the policy name, political connection and province membership are not the identifying contrast.
  primary_strategy: Zhang and Zhao2026 estimate firm-panel fixed-effects DID and interactions with prepolicy ownership/connection, comparing a fixed matched sample and an eventual-beneficiary-only sample.
  estimand: Conditional change in outcomes of eligible pre-existing firms associated with the FTZ institutional bundle; not a pure effect of one subsidy or the causal effect of acquiring political connections.
  treatment_variable: pre_local_year_operational_presence_in_relevant_zone times indicator(year>=local_cohort_year), subject to the reported mover exclusions.
  comparison_logic: Require comparable untreated outcome paths after conditioning on prepolicy characteristics. Stop using a later cohort as an untreated control at its own onset; do not interpret a generic TWFE coefficient as an automatically clean cohort average.
  estimation_notes: Matched9414 firms and117886 firm-year observations; industrial-enterprise data1998–2015 and listed-firm statements1998–2022 have different support. Matching is once at2012 or the nearest prelocal year using Mahalanobis distance. Firm clustering is reported; designation-level dependence requires separate assessment. AppendixA3 header says quarters but its note says yearly effects; no quarterly data contract is served.
  assumptions: [conditional parallel untreated trends, adequate overlap, faithful historical location mapping, no outcome-selected relocation exclusions, no unhandled spatial interference, cohort-consistent outcome support]
  diagnostics: [inspect outcome-specific pretrends rather than accept blanket prose, reconcile annual versus quarterly event index using author code, assess overlap and fixed matches, use heterogeneity-robust cohort estimates, zone-level inference sensitivity, map expansion separately, test address and mover definitions]
threats:
  - type: selection-and-anticipation
    basis: documented
    condition: Administrative selection and predesignation preparation remain relevant. AppendixA2 contains significant pre-treatment associations despite the body's blanket no-significance statement; it is a selection regression rather than proof of parallel trends.
    evidence_refs: [E3, E4]
    possible_diagnostics: [outcome-specific event leads, joint tests and power, inspect province selection, cohort-specific counterfactuals]
  - type: location-and-eligibility
    basis: documented
    condition: The author operational-presence proxy differs from registered-in-zone eligibility for some legal measures. Multi-plant and post2012 mover handling need an explicit convention; misclassification need not attenuate effects toward zero.
    evidence_refs: [E1, E3]
    possible_diagnostics: [historical plant-address audit, registration-versus-production sensitivity, single-establishment sample, freeze before anticipation]
  - type: frequency-and-support
    basis: documented
    condition: AppendixA3 labels quarters while its note labels years; annual industrial outcomes stop2015 and cannot independently estimate later cohorts. Firm counts do not imply a balanced annual panel.
    evidence_refs: [E3, E4]
    possible_diagnostics: [recover author event-index code, show cohort-by-source coverage, separate listed and industrial samples, disclose missingness]
  - type: inference-and-overlap
    basis: inferred
    condition: Zone-level designation can correlate firm errors, and geographically close controls can receive spillovers. TWFE decomposition does not by itself resolve heterogeneous-effect bias.
    evidence_refs: [E3, E4]
    possible_diagnostics: [assignment-level clustering sensitivity, distance exclusions, modern cohort estimators, overlap and matching-year audit]
empirical_requirements:
  contract_version: 1
  population: Mainland pre-existing firms with historically verifiable production presence in designated territory and credible comparison observations.
  observation_unit: firm-year
  geography_level: establishment coordinates or historical address matched to FTZ subzone boundary
  time_start: 1998
  time_end: 2022
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 2
  required_fields: [firm-year research outcome, dated production address, local subzone first-exposure year, boundary version, relocation history, prepolicy industry and firm characteristics for matching]
  required_identifiers: [firm_id, year, establishment_id, subzone_id]
  treatment_key: [firm_id, year]
  treatment_source: Author AppendixA1 territory/cohort table and official plan boundaries; body Sections3.1 and4.1 define frozen production-presence exposure. Exact polygons and plant aggregation must be supplied for implementation.
  measurement_risks: [historical address versus current headquarters, multiple plants and mergers, post2012 mover exclusion, expansion backdating, cohort-specific source support, event-frequency inconsistency]
evidence:
  - id: E1
    source_type: policy-document
    citation: State Council Shanghai overall plan 国发〔2013〕38号, reproduced on MOFCOM legal-information portal.
    url: https://policy.mofcom.gov.cn/claw/clawContent.shtml?id=63285
    date: '2013-09-18'
    supports: [identity.instrument, identity.authority, identity.legal_identifiers, timeline.announcement, assignment.unit, assignment.compliance]
    verification_status: verified
    access_level: official-document
    locator: Actual text SectionI(3) four customs areas; SectionII administrative/investment reforms and temporary approval adjustment from2013-10-01; appendix note confines opening measures to registered-in-zone firms. Portal attributes reproduction to a third-party legal provider; maps and appendix images not inspected.
  - id: E2
    source_type: policy-document
    citation: State Council 国发〔2020〕10号 new-zone plans and Zhejiang expansion, reproduced by MOFCOM from China Government Network.
    url: https://www.mofcom.gov.cn/zcfb/zgdwjjmywg/art/2020/art_87e8466e0c334e66a7e235d04925597a.html
    date: '2020-08-30'
    supports: [identity.legal_identifiers, timeline.effective, assignment.exposure_construction, assignment.exemptions]
    verification_status: verified
    access_level: official-document
    locator: Actual full text notification/signature; Zhejiang SectionII(1) Ningbo46km2, Hangzhou37.51km2 and Jinyi35.99km2; Beijing/Anhui/Hunan each designate specific subareas. Notice signature differs from webpage2020-10-30 posting.
  - id: E3
    source_type: paper
    citation: 'Zhang, Qi and Bin Zhao (2026). Free market initiatives: Benefits and distortions from political power. Economic Inquiry64(3):931–954. DOI10.1111/ecin.70062; first published2026-04-18.'
    url: https://doi.org/10.1111/ecin.70062
    date: 2026
    supports: [assignment.treated, assignment.rule, assignment.comparison_pool, assignment.exposure_construction, design.primary_strategy, design.estimation_notes, empirical_requirements.required_fields, design_applications.treatment_encoding, design_applications.data_used]
    verification_status: reported
    access_level: full-text
    locator: Actual browser-rendered full body at https://onlinelibrary.wiley.com/doi/full/10.1111/ecin.70062 Sections3.1–3.3, Table1 note, Sections4.1.1–4.1.2 and5.5, Introduction mover exclusion, endnotes7–8 and data availability. Equations' math also present in AX; no code rerun or archive file inspection claimed.
  - id: E4
    source_type: appendix
    citation: Zhang and Zhao2026 Supporting Information S2, ecin70062-sup-0002-Appendix.pdf.
    url: https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1111%2Fecin.70062&file=ecin70062-sup-0002-Appendix.pdf
    date: 2026
    supports: [timeline.local_timing, design.diagnostics, design.estimation_notes, assignment.treated]
    verification_status: reported
    access_level: appendix
    locator: Actual14-page publisher supplement downloaded through its visible link. Printedp2/TableA1 cohorts and subareas; p3/TableA2 correlations; p4/TableA3 dynamics visually inspected. Other appendix tables/code not claimed inspected.
design_applications:
  - paper: Free market initiatives — firm performance and political-power heterogeneity
    doi: 10.1111/ecin.70062
    journal: Economic Inquiry
    year: 2026
    research_question: How does FTZ rollout affect incumbent firm performance and vary by prepolicy political power?
    population: 9414 matched mainland firms; eventual-beneficiary-only comparison uses4707 treated firms. Political-connection measures cover709 listed firms rather than all industrial firms.
    outcome: ROA, production-function TFP and asinh exports; accounting cost measures are channels rather than independent assigned shocks.
    data_used: [Shanghai and Shenzhen listed-firm financial statements1998–2022, China industrial enterprises database1998–2015, historical business-address disclosures and manual checks]
    treatment_encoding: Operational presence within the relevant official territory one year before local implementation; local cohort post indicator and reported post2012 in-mover exclusion.
    comparison: Fixed Mahalanobis matched never-treated firms in same/adjacent provinces, and timing comparison within eventual beneficiaries.
    empirical_design: Annual firm fixed-effects staggered DID with reported firm clustering; prepolicy ownership/connection interactions describe heterogeneous effects, not an independent randomized treatment.
    assumptions: [conditional parallel trends, comparable source coverage, no unhandled sorting or interference]
    threats_addressed: [reported address/mover checks, fixed matching, displayed appendix selection tests with contrary significant cells, reported decomposition and concurrent-policy controls]
    evidence_refs: [E3, E4]
method_transfer: null
readiness_blockers:
  - Conditional use requires dated production addresses, official boundary versions and local onset; a city/province-only dataset does not satisfy this contract. Generalized legal benefit receipt is not verified by operational presence.
  - Preserve the observed diagnostics conflict and assess counterfactual trends for the new outcome. The source paper is not a certification of causal validity; do not promise zero misclassification bias or clean TWFE weighting.
  - Annual applications only until author event-index code resolves AppendixA3 quarter/year inconsistency. Exact author reproduction, multi-plant aggregation and post2012 mover filtering remain code-level follow-ups; openICPSR DOI10.3886/E239716V7 lists materials but files have not been inspected.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Pilot FTZs create selected territorial laboratories for trade, investment and
administrative reform. The2013 Shanghai plan starts from four existing customs
areas; designation changes their institutional regime, not simply their name
or bonded status [E1]. Different measures can have different eligibility.
Presence in the host city does not make an enterprise legally eligible for
every inside-zone benefit.

## What Changed

Designation spreads across territories and later expands existing zones.
The2020 Zhejiang instrument adds Ningbo, Hangzhou and Jinyi territory [E2].
An old Shanghai parcel and a newly added Shanghai parcel can therefore have
different first-exposure years. Neither an expansion date nor the province's
original designation should overwrite each parcel's actual onset.

## Implementation and Assignment

The inspected firm application freezes operational presence one year before
local designation and excludes post2012 in-movers [E3, reported claim]. Join
historical establishments to the relevant boundary version, then aggregate
exposure to firms using a declared convention. Keep registered eligibility
separate from physical operations: the paper measures a broader institutional
environment and does not prove receipt of each legal advantage.

TableA1 names subareas and their cohorts [E4, reported claim]. It is sufficient
to recover the assignment concept and expansion sequence, not a ready GIS
polygon layer. Obtain the relevant official boundary description for the
researcher's locations. Do not silently correct spellings such as the table's
Shanghai high-tech-area label when reproducing the author's mapping.

## Why This Creates Empirical Variation

The useful contrast is outcomes before and after each relevant territory's
rollout relative to credible untreated firms. The paper uses two comparisons:
fixed matched never-treated firms and eventual beneficiaries treated at
different times [E3, reported claim]. They share one institutional assignment,
so they are not two variations. Prepolicy ownership and political ties are
heterogeneity dimensions, not new policy shocks.

## Identification Risks

Actual inspection changes how the diagnostics should be described. TableA2
reports export-association p-values0.016,0.020 and0.007 at four, six and seven
years before exposure, contrary to the body's blanket no-significance claim
[E3, E4]. TableA3 displays a negative export pre-event interval at−4 and
negative TFP intervals at−3 and−1 [E4]. These are reasons to reassess the
comparison, not to erase the policy from the knowledge base or endorse its
published causal interpretation. Its header says quarters while its note says
yearly effects; this record serves annual data only pending code clarification.

Production addresses can misclassify treatment, and the direction of bias is
not established merely by asserting attenuation [analytical inference].
Selection, anticipation, shared zone shocks and spillovers need query-specific
assessment. Decomposition and placebo exercises cannot prove these absent.

## Data Requirements

For a new firm outcome, the essential bridge is firm_id/year plus dated
production-establishment identity, subzone boundary/version and local cohort.
Add outcome-specific variables rather than requiring every published channel.
TFP needs production inputs; ROA needs net profit and assets; exports need a
documented unit and transformation. Industrial data ending2015 cannot supply
postperiods for later designation cohorts, even though listed statements reach
2022 [E3, reported claim]. Data-asset acquisition belongs in Econ Data Know-How;
the paper DOI connects the projects without copying assets here.

## Evidence Notes

This record admits a grounded, conditional territorial-exposure mechanism,
not a validated replication or unrestricted recommendation. The2025 ROIE
host-prefecture entry paper remains candidate48e99f9e05e7: its aggregate
exposure and unresolved51-prefecture crosswalk are not silently substituted
for this plant-location contract. Historical blocked candidate2bc5cc93f059
remains preserved; task7d09473e1860 supersedes its old Abstract-only access
limitation with actual body and appendix inspection.
