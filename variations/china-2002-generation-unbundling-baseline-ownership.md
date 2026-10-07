---
schema_version: 2
id: china-2002-generation-unbundling-baseline-ownership
name: China's2002 generation unbundling with baseline state-ownership exposure
aliases: [厂网分开2002, 国发〔2002〕5号发电企业重组, Gao-VanBiesebroeck generation restructuring]
status: grounded
provenance:
  task_id: task-d316b5fa447a
scope:
  country: China
  regions: [Mainland fossil-fuel electricity generation firms]
  domains: [firm, industrial-economics, development, electricity-generation]
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: Actual mainland generation firms face vertical unbundling and restructuring; the paper compares fixed2002 state-ownership categories with other generators. This is not an electricity-shortage instrument or an emissions-policy application.
identity:
  instrument: The2002 electricity restructuring regime separates generation from grid businesses and reorganizes State Power Company assets, with parallel requirements for local and other-department electricity enterprises.
  authority: State Council; electricity reform working group and implementing enterprises, with central-local coordination and the new electricity regulator.
  legal_identifiers: [国发〔2002〕5号, 发改能源〔2003〕1025号]
  implementation_regime: Generation/grid separation and company formation precede completion of competitive wholesale pricing. Geographic and asset-quality considerations guide portfolio formation; exceptions and transitional management remain. The paper's baseline is differential state-ownership exposure within this industry regime, not proof that each registered SOE underwent an identical asset transfer.
  assignment_mechanism: The legal restructuring applies to SPC generation/grid assets and relevant local or other-department enterprises. The paper fixes2002 registration types110 and151 as the more directly affected group; alternative Big Five affiliation and majority-state-capital definitions change the comparison and are sensitivity checks, not separate shocks.
  parent: null
  related_variations: []
timeline:
  announcement: '2002-02-10'
  effective: null
  implementation_start: 2002
  implementation_end: null
  local_timing: NEA reproduces the plan as issued2002-02-10, while the2003 coordination notice describes circulation in March2002. Neither establishes every firm's transfer date. By2003-08-25 the five generation groups and two grid companies were operating. The final paper explicitly defines its delayed-effect period as2004–2007; retain annual interactions and verify the inclusive boundary of its separate POST2002 specification from code before exact replication.
  anticipation: Earlier1985 entry and1997 regulatory separation already changed incentives. Formation and ownership adjustments continue through2002–2004; expectations of future competition can matter before any regional bidding market operates.
  last_verified: '2026-10-07'
assignment:
  unit: Fossil-fuel electricity generation firm-year.
  treated: Firms officially registered in2002 as state-owned type110 or state-solely-funded type151 in the benchmark application, fixed as exposed for the whole panel.
  comparison_pool: Firms with private, foreign, collective or mixed ownership in2002. They also face industry-wide regulatory and market changes; they are less directly exposed comparisons, not unaffected controls.
  rule: For the published benchmark set STATE0=1 when2002 registration is110 or151, otherwise0, and hold that group fixed. Interact it with annual indicators or the delayed2004–2007 period. Legal SPC asset affiliation is a separate variable and cannot be inferred solely from registration.
  intensity: Binary baseline-ownership exposure; no measured dose of asset divestiture, privatization or competitive electricity pricing.
  exemptions: [Legal grid companies may retain pumped-storage or selected emergency/peaking units, Pending generation reorganizations may remain temporarily grid-managed, Small self-supplying hydro areas separate when appropriate, Fossil-fuel CIC4411 application excludes hydro and nuclear generation, Foreign investment contracts can retain transitional arrangements]
  compliance: Official2003 notice confirms group operation and reiterates local unbundling duties, not uniform completion or competitive pricing at each generator. Actual transfers and affiliation require firm histories for an asset-level study.
  exposure_construction: Link NBS industrial firm accounts1998–2007, isolate CIC4411, recover2002 registration and freeze baseline group. Follow official IDs and check name/birthdate/postal-code continuity around reorganization. Aggregate manufacturing output and employment in the paper's six-digit diqu region to construct revenue instruments, separately from treatment.
  required_identifiers: [firm_id, year, registration_type_2002, industry_code, diqu_code, province_code]
  spillovers: Private and foreign generators respond to competition, demand and coal prices; year effects absorb common changes but not ownership-specific spillovers or shocks. Grid access and regionally constrained transmission can transmit exposure across firms.
research_compatibility:
  outcome_domains: [employment input demand, material expenditure, conditional operating efficiency]
  affected_populations: [Mainland fossil-fuel electricity generation firms, baseline state-owned generators]
  mechanism_channels: [separation of generation and grid control, managerial incentives, competitive pressure, adjustment of legacy labor and input use]
  best_for: [ownership-differential responses to generation restructuring, conditional input demand under regulated output prices, industrial organization of state enterprises]
  not_good_for: [universal privatization, immediate nationwide electricity price liberalization, random asset assignment, directly measured physical TFP, policy exposure for all manufacturing firms, environmental outcomes inferred from this paper]
design:
  claim_type: reduced-form
  affordances: [fixed-ownership-group DID, annual ownership interactions, delayed adjustment comparison]
  candidate_designs: [firm-panel DID, ownership-group event study]
  identifying_variation: Differential evolution of factor demand for baseline state-owned generators relative to other generators during one common restructuring regime.
  primary_strategy: Firm and year fixed-effects input-demand equations with price-heterogeneity controls; instrument firm revenue with regional manufacturing output and employment. STATE0 interacts with years or post periods. The preferred reported delayed specification uses2004–2007 and firm-clustered inference.
  estimand: Differential employment or material-expenditure adjustment conditional on revenue and modeled prices. It combines ownership-linked responses to the restructuring environment; it is not a randomized divestiture effect, unconditional employment effect or direct physical productivity measure.
  treatment_variable: Fixed2002 registration110/151 indicator interacted with annual indicators or the delayed2004–2007 post window.
  comparison_logic: Absent restructuring, baseline ownership groups must have comparable conditional input-demand trends after accounting for prices and demand. Industry-wide changes can affect both groups. Alternative affiliation definitions alter both treated firms and controls, so preserve the common-control exercise as well as full-sample comparisons.
  estimation_notes: TableII uses10792 observations. Its late-post labor/material coefficients are−0.072/−0.051; TableIV's Big Five labor coefficient is+0.077, not confirmation of the same effect. Revenue IV addresses endogenous output, not endogenous policy assignment. Local manufacturing demand must affect factor use through generator revenue rather than unmodeled input-price or labor-market channels. TableII reports strong first-stage and overidentification diagnostics; these do not prove exclusion or parallel trends. Randomized inference describes a resampling procedure, not randomized policy assignment.
  assumptions: [conditional ownership-group parallel trends, stable baseline grouping and firm continuity, adequate modeling of heterogeneous electricity and coal prices, valid regional-demand instruments for revenue, no remaining ownership-specific contemporaneous confounding]
  diagnostics: [annual pre/post interactions, alternative ownership definitions, common control set, Mahalanobis matching, price-control alternatives, firm-clustered and pooled pre/post inference, revenue-instrument sensitivity, entry/exit and ID-change audits, concurrent coal and SASAC reform assessment]
threats:
  - type: assignment-proxy
    basis: documented
    condition: Registration ownership is not literal SPC transfer status; the Big Five group overlaps only partly and its labor response changes sign. Capital-majority ownership produces weaker estimates.
    evidence_refs: [E1, E2]
    possible_diagnostics: [preserve exact2002 codes, reconcile affiliation and capital, common controls, obtain actual asset histories for transfer-specific claims]
  - type: concurrent-reforms
    basis: documented
    condition: Coal-market liberalization, coal-price pass-through, SASAC incentives and capacity expansion occur around the restructuring and can affect ownership groups differently.
    evidence_refs: [E1, E3]
    possible_diagnostics: [price and ownership interactions, regional/cohort comparisons, narrow estimand to the joint restructuring environment]
  - type: endogenous-output-and-prices
    basis: documented
    condition: Revenue and material expenditures are value measures with heterogeneous unobserved prices. Local manufacturing demand can influence factor costs as well as output; IV validity is not established by first-stage or Hansen tests alone.
    evidence_refs: [E1]
    possible_diagnostics: [physical quantities and prices where available, alternative revenue instruments, direct regional input-cost controls, compare instrumented and predetermined-output specifications]
  - type: panel-selection
    basis: documented
    condition: The paper reports23percent pre2002 firm exit,31percent of2002 firms absent in1998 and10percent experiencing an ID change during restructuring. Firm reporting units need not be individual plants.
    evidence_refs: [E1]
    possible_diagnostics: [name birthdate and postal crosswalk, entry/exit versus ID changes, survivor sensitivity, consistent firm-versus-plant unit]
empirical_requirements:
  contract_version: 1
  population: NBS industrial survey fossil-fuel electricity generators, CIC4411,1998–2007; all SOEs and other firms above RMB5million annual sales. The authors infer near-universe coverage from scale, not a verified census of physical plants.
  observation_unit: firm-year
  geography_level: Mainland firm and six-digit diqu region within province.
  time_start: 1998
  time_end: 2007
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 1
  required_fields: [employment, material expenditure including fuel and nonfuel, electricity revenue, total labor compensation, fixed assets, establishment year, state capital share, baseline2002 ownership registration, regional manufacturing output and employment]
  required_identifiers: [firm_id, year, industry_code, registration_type_2002, diqu_code, province_code]
  treatment_key: [firm_id, registration_type_2002, year]
  treatment_source: Final SectionIII(iii) registration lookup and TableIV alternatives; official2002 restructuring plan and2003 coordination notice establish the institutional regime, not a ready firm-transfer table.
  measurement_risks: [firm ID changes, legal versus registration exposure, missing baseline classification for entrants, firm versus plant aggregation, value versus physical inputs, regional code continuity, changing ownership and survival]
evidence:
  - id: E1
    source_type: paper
    citation: 'Gao, Hang and Johannes Van Biesebroeck.2014. Effects of Deregulation and Vertical Unbundling on the Performance of China’s Electricity Generation Sector. Journal of Industrial Economics62(1):41–76. DOI10.1111/joie.12034.'
    url: https://doi.org/10.1111/joie.12034
    date: 2014
    supports: [identity.assignment_mechanism, timeline.local_timing, timeline.anticipation, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.exposure_construction, design.primary_strategy, design.estimand, design.estimation_notes, empirical_requirements.population, design_applications.empirical_design]
    verification_status: verified
    access_level: full-text
    locator: 'Actual final HTML body at https://pmc.ncbi.nlm.nih.gov/articles/PMC4809436/: SectionII; III(ii) price differences, III(iii) treated definitions, III(iv) revenue instruments/inference; IV data and firm continuity; V(i) explicit2004–2007 period; V(ii) and TablesII–IV; footnotes20,23–24,30. Formula images not independently transcribed; no code inspected.'
  - id: E2
    source_type: policy-document
    citation: 国务院电力体制改革方案, 国发〔2002〕5号, reproduced by National Energy Administration.
    url: https://www.nea.gov.cn/2011-08/17/c_131054253.htm
    date: '2002-02-10'
    supports: [identity.instrument, identity.authority, identity.implementation_regime, timeline.announcement, timeline.implementation_start, assignment.rule, assignment.exemptions, assignment.compliance]
    verification_status: verified
    access_level: official-document
    locator: 'Actual official body header and Clauses7–12 on separation, portfolio assignment and grid exceptions;14–15 internal reform versus listing;17–22 staged markets/contracts;25 formation target.2011 reproduction date is not issuance. Supports legal assignment, not the paper’s ownership proxy.'
  - id: E3
    source_type: implementation-document
    citation: 国家发展改革委关于请地方政府综合经济管理部门做好电力体制改革工作中有关工作的通知, 发改能源〔2003〕1025号.
    url: https://www.nea.gov.cn/2011-08/17/c_131054259.htm
    date: '2003-08-25'
    supports: [identity.implementation_regime, timeline.local_timing, assignment.rule, assignment.compliance, assignment.spillovers]
    verification_status: verified
    access_level: official-document
    locator: 'Actual complete official reproduction: opening confirms five generation groups and two grid companies operating; SectionI extends unbundling to local enterprises; III–VI distinguish internal distribution accounts, regional price pilots and centrally approved direct trade.2011 portal date is not policy date.'
design_applications:
  - paper: Effects of Deregulation and Vertical Unbundling on the Performance of China's Electricity Generation Sector
    doi: 10.1111/joie.12034
    journal: Journal of Industrial Economics
    year: 2014
    research_question: Did generation restructuring change conditional labor and material demand more among baseline state-owned firms?
    population: Mainland fossil-fuel generators in NBS1998–2007 panel, classified using2002 ownership.
    outcome: Log employment and log material expenditure conditional on revenue and price controls.
    data_used: [NBS annual industrial firm surveys CIC4411, regional manufacturing output and employment, province and ownership fields, official restructuring context]
    treatment_encoding: Fixed2002 types110/151 times annual indicators or post; preferred delayed window2004–2007. Big Five and majority-state-capital alternatives are sensitivity definitions.
    comparison: Other2002 ownership categories, with matched and common-control alternatives; controls also face industry reforms.
    empirical_design: Firm/year DID input-demand equations with regional-demand IV for revenue, price-heterogeneity controls and firm-clustered inference.
    assumptions: [conditional group trends, valid demand-IV exclusion, adequate price controls, firm continuity and selection interpretation]
    threats_addressed: [alternative grouping and controls, heterogeneous prices, output simultaneity, serial correlation, observed covariate imbalance]
    evidence_refs: [E1, E2, E3]
method_transfer: null
readiness_blockers:
  - Obtain authorized NBS firm accounts and stable IDs; reconstruct2002 ownership and diqu manufacturing aggregates. Late entrants without observable2002 registration need the paper's executable sample/classification rule, not an invented ownership assignment.
  - Use the explicitly documented2004–2007 delayed comparison or annual interactions; recover code before exact POST2002 replication or deciding treatment of transition years in pooled estimation. Legal issuance, group operation and each firm's realized transfer are different clocks.
  - Baseline ownership is a policy-exposure proxy, not an asset-transfer roster. Asset-specific studies require actual affiliation/transfer histories. Interpret the conditional reduced form with concurrent reforms and materially different alternative-group results, not as a universal privatization productivity gain.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Generation entry expanded from1985 and regulator/business separation followed
in1997. The2002 regime separates grid control from generation and reorganizes
SPC assets; local government enterprises also face unbundling duties [E1;
E2; E3]. It does not turn every generator into a private firm or immediately
establish competitive electricity prices. The legal plan explicitly retains
grid exceptions, transitional contracts and locally staged markets [E2].

## What Changed

The legal change separates generation from grid businesses and reorganizes
their assets, finances and personnel. The2003 coordination notice confirms
operation of the new central groups while still requiring local implementation
and coordination [E2; E3]. This is a transition, not one universal transfer date.

## Implementation and Assignment

The plan forms generation portfolios according to asset quality and geography,
so affiliation is not randomly assigned [E2]. The published benchmark instead
fixes registration types110/151 at2002 and compares their subsequent input
demand with other ownership categories [E1, reported claim]. These categories
can be encoded from firm accounts but do not enumerate actual transfers.
Keep legal assignment and research exposure connected without equating them.

## Why This Creates Empirical Variation

The paper asks whether the more directly exposed ownership group adjusts
factor demand differently under the common restructuring regime. Its
preferred delayed comparison covers2004–2007 [E1, reported claim]. Instrumenting
revenue addresses output simultaneity, not selection into restructuring.
Employment and material coefficients concern conditional input use, rather
than an unconditional employment or directly measured physical TFP effect.

## Identification Risks

Alternative grouping is substantively important: Big Five affiliation changes
the labor estimate's sign, and using common controls changes the comparison
again [E1, reported claim]. Coal liberalization, price pass-through and SASAC
incentives occur alongside unbundling. A new research application must explain
which joint response it identifies; the word deregulation cannot isolate one
component [analytical inference].

## Data Requirements

The panel records firms, not necessarily individual plants, and value inputs,
not physical fuel quantities. Preserve baseline ownership and ID continuity:
the authors report10percent of firms changing IDs during reorganization [E1,
reported claim].

## Evidence Notes

Official sources establish the legal regime and operation of
new groups by August2003, but not each firm's transfer date [E2; E3]. Exact
early-post code and late-entrant classification remain conditional-use needs;
do not invent them from the policy year. No paper or restricted data is stored.
