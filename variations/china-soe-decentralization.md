---
schema_version: 2
id: china-soe-decentralization
name: Changes in Government Oversight of Chinese Industrial SOEs, 1999-2007
aliases:
- Huang-Li-Ma-Xu SOE decentralization
- Hayek local information and commanding heights
- 国有企业隶属关系下放
status: grounded
provenance:
  task_id: task-d629af30d033
scope:
  country: China
  regions:
  - Mainland China; the paper's industrial SOE sample spans provincial jurisdictions
  domains:
  - firm
  - industrial-organization
  - political-economy
  - regional-economics
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    Chinese industrial SOEs changed their supervising government from a higher
    administrative tier to a lower one at different firm-years. The paper
    observes these changes in China and studies which firms were selected for
    transfer. This is a real China-facing institutional variation, but the
    published paper does not estimate its causal effect on firm performance.
identity:
  instrument: >
    Downward reassignment of an industrial SOE's government affiliation or
    oversight authority (隶属关系) among central, provincial, municipal, and
    county tiers. This is an administrative control-rights change, not
    necessarily privatization, a change of firm location, or a universal
    nationwide policy activated on one date.
  authority: >
    The government or state-asset authority with incumbent oversight, with
    receiving lower-level government and applicable approval procedures.
    Specific central and provincial transfer programs had different issuing
    authorities; there is no single assignment authority for all 1,516
    observed transfers.
  legal_identifiers:
  - 国发〔1998〕22号; State Council central coal-mine transfer to provinces, an illustrative sector-specific program
  - 鲁政发〔2003〕62号; Shandong provincial SOE reform opinion, reproduced in the published paper's appendix
  - 陕政办发〔2005〕108号; Shaanxi provincial SOE territorial-management notice, reproduced in the appendix
  implementation_regime: >
    Separate central and local decisions reassigned SOEs down the government
    hierarchy during the observed 1999-2007 window. The 1998 State Council
    coal notice transferred named central mines to provincial management.
    Shandong's 2003 opinion made downward transfer one option for suitable
    provincial SOEs, especially dispersed small or medium enterprises difficult
    for the province to supervise. These are examples of heterogeneous
    implementation, not a common rule automatically assigning every sample firm.
  assignment_mechanism: >
    Government-selected firm-specific transfer. The incumbent authority and
    local reform programs weighed strategic importance, firm attributes, and
    manageability. The paper finds that firms farther from their initial
    overseeing government were more likely to be transferred, especially where
    local information mattered, while strategically important firms were less
    subject to that pattern. Distance is an observed predictor, not a legal
    cutoff, randomized assignment, or instrument used by this paper.
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 1999
  implementation_end: 2007
  local_timing: >
    In the paper's annual industrial panel, first downward oversight changes
    occur between 1999 and 2007; the paper reports 1,516 transfers in its
    analysis sample. The State Council coal example was issued in 1998, and
    provincial decisions such as Shandong 2003 and Shaanxi 2005 occurred at
    different times. A national reform announcement date would misstate the
    institution; firm-year timing must be read from oversight affiliation.
  anticipation: >
    Reform proposals and local notices may precede the recorded affiliation
    change. The published selection analysis does not establish an
    unanticipated shock for firm-outcome research.
  last_verified: '2026-10-02'
assignment:
  unit: Industrial state-owned enterprise-year, initially supervised above the county tier
  treated: >
    A sample SOE in the first year its recorded oversight level moves from a
    higher to a lower government tier, including central-to-provincial and
    provincial-to-municipal or county transfers. A firm that was already
    county-supervised at entry has no lower tier in the paper's studied hierarchy.
  comparison_pool: >
    At-risk SOEs that have not yet experienced a downward transfer in that
    year. The published paper drops post-transfer observations from the hazard
    sample; its comparison is not a DID control group for post-transfer outcomes.
  rule: >
    Code the first year in which the firm's observed oversight government is
    lower in the administrative hierarchy than in the preceding year. The
    paper's sample construction removes firms initially at county or lower,
    observations without three consecutive years, and anomalous reversals.
    Specific policy notices identify certain batches, but do not provide a
    complete firm-level treatment roster for the national sample.
  intensity: Binary first transfer in the paper; size of administrative-tier jump may vary but is not the principal treatment measure
  exemptions:
  - Firms initially overseen at county or lower levels are outside the paper's at-risk sample
  - Strategically important central SOEs were more likely to remain centrally supervised; this is selection, not a categorical exemption list
  compliance: >
    Oversight reassignment is an administrative decision. The published panel
    records affiliation changes, not independent firm-level implementation
    files for every transfer; apparent reversals are removed from its sample.
  exposure_construction: >
    Harmonize firm identifiers and annual oversight-government tiers in the
    Annual Survey of Industrial Firms (1998-2007), retain eligible initially
    above-county SOEs, and mark the first downward change. For the paper's
    selection model, measure log(1 + distance in km) from firm location to
    the initial supervising government's seat and lag firm covariates.
  required_identifiers:
  - stable firm identifier
  - year
  - initial and annual oversight government level and identity
  - firm location
  - initial oversight-government seat
  - industry and ownership classification
  spillovers: >
    Transfer may change local government incentives, competition, and
    neighboring firms' environment. Those effects are plausible future
    research questions, not estimates supplied by this paper.
research_compatibility:
  outcome_domains:
  - selection into lower-tier SOE oversight
  - firm performance or productivity as a future, separately identified question
  - local government-firm relations as a future question
  affected_populations:
  - industrial SOEs with above-county initial oversight
  - receiving and relinquishing governments
  - workers and local markets potentially affected by transferred SOEs
  mechanism_channels:
  - local information and monitoring costs
  - state strategic control over commanding-heights firms
  - government selection on firm scale and performance
  best_for:
  - Studying determinants and timing of which Chinese industrial SOEs changed supervising government
  - Developing a firm-year administrative-transfer exposure with explicit attention to government selection
  not_good_for:
  - Treating the published paper as evidence that decentralization caused productivity, profitability, or innovation changes
  - Using distance as a ready-made valid instrument for transfer effects on firm outcomes
  - Assuming every transfer was central-to-provincial or arose from one nationwide rollout
design:
  claim_type: descriptive
  affordances:
  - Observed firm-year affiliation changes across tiers in a national industrial panel
  - Initial firm-to-supervisor distance and industry heterogeneity allow analysis of selection
  candidate_designs:
  - Annual probit or hazard model of first downward oversight change, as in the paper
  - A future firm-outcome design only after separately establishing comparable risk sets, event timing, pre-trends, and concurrent-reform controls
  identifying_variation: >
    Among still-at-risk SOEs, the paper compares the probability of a first
    downward transfer across initial distance to oversight government and other
    pre-transfer firm and industry characteristics. This is variation in
    government selection, not an exogenous assignment of the transfer.
  primary_strategy: >
    Published application: annual probit hazard for transfer occurrence with
    lagged firm characteristics, three-digit industry, year, and initial
    oversight-government indicators; standard errors clustered by initial
    overseeing government. Alternative hazard and competing-reform analyses
    probe the selection pattern.
  estimand: >
    Conditional association between initial distance and the annual
    probability that an at-risk SOE is transferred to a lower government.
    The paper does not identify the causal effect of transfer on firm outcomes.
  treatment_variable: >
    In the published regression, first downward transfer is the dependent
    event; initial log(1 + km to supervising government) is the key explanatory
    variable, not an instrumented treatment.
  comparison_logic: >
    Farther versus nearer at-risk firms under observed controls and initial
    oversight-government, industry, and year indicators; strategically
    important firms show a weaker distance relationship.
  estimation_notes: >
    The paper reports a 1-standard-deviation increase in log distance is
    associated with about 1.3 percentage points higher transfer probability
    in its pooled baseline, not the 10.5-point effect formerly stated here.
    This magnitude is a model result, not a policy assignment probability.
  assumptions:
  - Interpreting coefficients as determinants depends on observed controls adequately describing government selection; they do not turn distance into random assignment
  diagnostics:
  - Compare transferred and still-supervised SOEs on pre-transfer size, profitability, productivity, and industry
  - Check alternative government tiers, competing restructuring events, and hazard specifications
  - For any future outcome study, inspect pre-transfer trends and coincident ownership or restructuring changes rather than importing the paper's selection model as a causal design
threats:
- type: endogenous-selection
  basis: documented
  condition: >
    Governments selected SOEs for transfer. The appendix shows transferred
    firms differ in pre-transfer size, profitability, and productivity; distance
    is also related to location and market access.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Reconstruct at-risk cohorts and compare pre-transfer characteristics
  - In an outcome study, test pre-trends and sensitivity to local economic conditions
- type: concurrent-reform
  basis: documented
  condition: >
    SOE restructuring, privatization, and ownership changes occurred during
    the same period; the paper examines alternative restructuring events while
    estimating transfer selection.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Track separate ownership and restructuring events by firm-year
- type: heterogeneous-authority
  basis: documented
  condition: >
    National coal, provincial, and municipal transfer programs differ in
    authority, eligible firms, and effective timing. One notice cannot be
    generalized to the entire national affiliation-change sample.
  evidence_refs:
  - E2
  - E3
  possible_diagnostics:
  - Match identified transfer batches to their actual issuing notice
empirical_requirements:
  contract_version: 1
  population: >
    Chinese industrial SOEs in the 1998-2007 Annual Survey of Industrial
    Firms, initially above county supervision and with consecutive observations;
    the paper's final risk sample contains 17,546 firms and 1,516 transfers.
  observation_unit: Firm-year
  geography_level: Firm location and initial overseeing-government seat
  time_start: 1998
  time_end: 2007
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 0
  required_fields:
  - stable firm ID and year
  - annual oversight government level and initial oversight government
  - SOE classification and state ownership share
  - firm location and government-seat coordinates
  - industry code
  - assets, sales, profits and other pre-transfer firm controls
  required_identifiers:
  - stable firm ID
  - year
  - initial oversight government and tier
  treatment_key:
  - first year of downward oversight-tier change
  treatment_source: >
    Annual Survey of Industrial Firms oversight-affiliation field, joined to
    firm and government-seat geography. The cited official notices document
    implementation examples but are not a complete national transfer roster.
  measurement_risks:
  - changing firm identifiers or missing three-year runs
  - inconsistent or reversed oversight-tier coding
  - state-share threshold and SOE definition
  - firm relocation or wrong government-seat geocoding
  - loss of post-transfer observations in the paper's risk model
evidence:
- id: E1
  source_type: paper
  citation: >
    Huang, Zhangkai, Lixing Li, Guangrong Ma, and Lixin Colin Xu. 2017.
    "Hayek, Local Information, and Commanding Heights: Decentralizing
    State-Owned Enterprises in China." American Economic Review 107 (8):
    2455-2478. DOI 10.1257/aer.20150592.
  url: https://doi.org/10.1257/aer.20150592
  date: 2017
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.rule
  - design.primary_strategy
  - design.estimand
  - design_applications.empirical_design
  verification_status: verified
  access_level: full-text
  locator: 'Published AER text pp. 2456-2466, institutional background and data, eq. (1), Tables 1-3; conclusion pp. 2474-2475; full-text copy https://documents.worldbank.org/curated/en/825361515675016563/pdf/122574-JRN-PUBLIC-Hayek-Local-Information.pdf'
- id: E2
  source_type: appendix
  citation: Huang et al. 2017, online appendix to AER 107(8), Appendix A-C.
  url: https://swlb2.aeaweb.org/articles/materials/7628
  date: 2017
  supports:
  - empirical_requirements.population
  - timeline.local_timing
  - assignment.comparison_pool
  - design.diagnostics
  - identity.implementation_regime
  verification_status: verified
  access_level: appendix
  locator: 'Appendix A pp. 1-7, especially Table A3; Appendix B Table B3; Appendix C pp. 7-13, Shandong 鲁政发〔2003〕62号 and Shaanxi 陕政办发〔2005〕108号 excerpts'
- id: E3
  source_type: implementation-document
  citation: 国务院关于改革国有重点煤矿管理体制的通知, 国发〔1998〕22号.
  url: https://www.nea.gov.cn/2011-08/17/c_131055778.htm
  date: 1998
  supports:
  - identity.instrument
  - identity.authority
  - identity.implementation_regime
  - timeline.local_timing
  - assignment.treated
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: 'Opening transfer directive and attached list of 94 central mines; issued 1998-07-03'
design_applications:
- paper: 'Hayek, Local Information, and Commanding Heights: Decentralizing State-Owned Enterprises in China'
  doi: 10.1257/aer.20150592
  journal: American Economic Review
  year: 2017
  research_question: Which Chinese industrial SOEs are selected for lower-tier government oversight, and is that selection consistent with local-information versus strategic-control considerations?
  population: 17,546 initially above-county industrial SOEs in a 1998-2007 panel; 1,516 first downward transfers
  outcome: Annual first downward oversight transfer
  data_used:
  - Annual Survey of Industrial Firms 1998-2007, including annual oversight tier and firm accounts
  - Firm locations and initial overseeing-government seats for geographic distance
  - Government documents on selected transfer programs, summarized in the online appendix
  treatment_encoding: First observed downward oversight transfer is the modeled event; log(1 + initial firm-to-overseer distance in km) is a predictor
  comparison: Still-at-risk SOEs farther versus nearer their initial overseeing government, conditional on lagged firm covariates and government, industry, and year indicators
  empirical_design: Annual probit hazard of first transfer; complementary Cox hazard and competing-reform specifications
  assumptions:
  - Selection interpretation is conditional on measured firm and government characteristics, not randomized exposure
  threats_addressed:
  - Strategic-sector retention and correlated firm characteristics examined in heterogeneity and robustness analysis
  - Alternative restructuring outcomes examined separately from decentralization
  evidence_refs:
  - E1
  - E2
readiness_blockers: []
method_transfer: null
---
## Institutional Background

This record documents an actual change in which tier of Chinese government
supervised an industrial SOE. Its strongest published use is to understand
selection into that change. A researcher can use it to ask why distant firms
were more likely to be delegated to nearer governments, while nationally
strategic firms remained under higher-tier control. It is not a ready-made
causal estimate of what delegation did to productivity or profits. [E1; E2]

## What Changed

Oversight may move down more than one rung of the central-provincial-municipal-
county hierarchy. No single national date assigned all firms: for example,
the 1998 State Council coal notice named central mines moving to provinces,
whereas the Shandong 2003 opinion treated transfer of suitable provincial SOEs
to municipalities as one reform option. The latter explicitly considered
dispersed, hard-to-manage small and medium firms. These examples explain why
distance might matter, but do not identify the policy file of every firm in
the national panel. The paper records first downward moves in 1999-2007. [E1-E3]

## Implementation and Assignment

The authors construct a risk set of initially above-county SOEs with at least
three consecutive years of survey information. Their outcome is the first
observed move to a lower supervising tier. They estimate its annual
probability against lagged firm characteristics and initial distance to the
supervising government, with government, industry and year indicators. A
one-standard-deviation distance increase corresponds to roughly 1.3 percentage
points greater transfer probability in the reported pooled baseline. This is
evidence about government selection, not a distance-IV or a DID of
post-transfer firm outcomes. [E1; E2]

## Why This Creates Empirical Variation

Firms differ in initial supervising tier, distance to the supervising seat,
and year of first downward transfer. This is useful for studying selection into
delegation, but it is not by itself random exposure to a policy. [E1; E2]

## Identification Risks

For a new causal question about the effect of oversight transfer, first
reconstruct the exact firm-year transfer and appropriate at-risk comparison
pool, then verify pre-transfer trends and separate privatization,
restructuring, and local economic changes. Distance is not automatically
exogenous to firm outcomes: location shapes market access and economic
conditions. The official notices establish real transfer mechanisms, but
their named batches cannot be silently treated as the complete national
assignment rule. [E1-E3]

## Data Requirements

The published selection analysis needs annual firm identifiers and oversight
tiers, at least three consecutive years, initial supervision above county,
initial firm and government-seat locations, and lagged firm controls. The
1998-2007 survey panel supplies these fields in the published application;
official notices are examples of implementation, not a substitute for the
national firm-year affiliation series. [E1-E3]

## Evidence Notes

E1 is the published paper, with the full text available from the linked
World Bank copy in its locator. E2 is its online appendix and reproduces
selected provincial notices; E3 is an independently accessible State Council
notice for the coal-sector subset. No source inspected here provides an
independent administrative roster for all 1,516 observed transfers.
