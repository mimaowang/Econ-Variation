---
schema_version: 2
id: china-shipbuilding-industrial-subsidies
name: Model-Implied Operating-Cost Support for Chinese Handysize Shipyards after 2006
aliases:
- Kalouptsidi Chinese shipbuilding subsidies
- Chinese shipbuilding industry cost wedge
- 中国造船业产业支持与成本楔子
status: grounded
provenance:
  task_id: task-7a479c3cf171
scope:
  country: China
  regions:
  - Mainland Chinese shipyards in a world Handysize bulk-carrier market
  - Japan, South Korea, and Europe are model comparison producers, not Chinese treatment units
  domains:
  - industrial-policy
  - international-trade
  - firm-dynamics
  - industrial-organization
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    The policy bundle targeted Chinese shipbuilding, and the published paper
    estimates a post-2006 cost wedge for Chinese Handysize bulk-carrier yards
    relative to foreign yards. The wedge is China-facing, but is inferred from
    a structural model rather than observed firm-level subsidy payments.
identity:
  instrument: >
    China-specific post-2006 reduction in Handysize bulk-carrier shipyard
    operating costs, interpreted by Kalouptsidi (2018) as consistent with
    industrial subsidies. The empirical object is a model-implied production-
    cost wedge, not a documented grant, loan, or subsidy entitlement for each
    yard. New Chinese yard capacity is a separate intervention in the same
    paper's counterfactual and must not be collapsed into the operating-cost wedge.
  authority: >
    State Council-approved shipbuilding development plan, drafted by NDRC and
    COSTIND, with sector support implemented through relevant fiscal, financial,
    tax, insurance and local bodies. The study does not observe which authority
    paid an operating subsidy to each sampled yard.
  legal_identifiers:
  - 船舶工业中长期发展规划（2006-2015年）, State Council approved in August 2006; NDRC public edition
  - 船舶工业调整和振兴规划, NDRC 2009-06-09, a crisis-era successor package rather than the paper's 2006 breakpoint
  implementation_regime: >
    The 2006-2015 plan set shipbuilding capacity and product goals, prioritized
    the Bohai, Yangtze-mouth, and Pearl-mouth bases, specified project approval,
    and called for fiscal, financial, tax, leasing, insurance, working-capital
    credit and export-financing support. These instruments were not one common
    measurable transfer. The separate 2009-2011 revitalization plan increased
    financing and restructuring support while curbing new dock approvals.
    The paper treats an aggregate Chinese cost shift from 2006 and a surge of
    new facilities as two modeled interventions; it does not identify the
    causal effect or receipt of any individual policy instrument.
  assignment_mechanism: >
    The official 2006 plan names priority facilities and types of support,
    with approved projects and qualified enterprises selectively eligible.
    Actual operating-cost assistance is not observed at yard level. The
    published model assigns a China x post-2006 cost-function term to Chinese
    yards in the studied Handysize market and estimates its magnitude from
    prices, orders, production choices, capacity and industry dynamics.
    This is an empirical measurement convention, not a legal subsidy rule.
  parent: null
  related_variations: []
timeline:
  announcement: '2006-08 (State Council approval of the medium- and long-term plan; exact day not established here)'
  effective: null
  implementation_start: 2006
  implementation_end: 2012
  local_timing: >
    The model divides the industry into pre-2006 and post-2006 regimes and
    observes quarterly yard production from Q1 2001 to Q3 2012. The inferred
    cost wedge covers 2006-2012; this end date is the analysis window, not a
    verified policy expiry. The paper examines regional onset proxied by first
    new dock/berth operation precisely because official local subsidy dates
    were unavailable. The 2009 plan is a later, different policy package.
  anticipation: >
    The structural model assumes an unexpected, one-shot, immediate and
    permanent change in industry expectations at 2006. The plan and prior
    investment buildup make this a modeling assumption rather than a verified
    fact about shipyards or buyers.
  last_verified: '2026-10-02'
assignment:
  unit: Chinese shipyard-quarter in the world Handysize bulk-carrier market
  treated: >
    Chinese Handysize-producing yards in the model's post-2006 regime,
    including entrants and incumbents. This denotes modeled exposure to a
    China-specific cost shift; observed subsidy receipt by yard is unknown.
  comparison_pool: >
    Pre-2006 Chinese cost choices and contemporaneous Japan, South Korea
    and Europe yards in the same Handysize market, conditional on the model's
    demand, state variables and country cost terms. Foreign yards are not
    untreated units in a published DID design.
  rule: >
    For the paper's cost function, China-yard indicator times post-2006
    indicator enters the linear operating-cost term. The plan's project
    approval and support provisions do not assign the estimated percentage
    cost reduction uniformly to all yards or distinguish recipients.
  intensity: >
    Estimated rather than observed: a 13-20% Chinese operating-cost
    reduction across specifications, corresponding to US$1.5-4.5 billion
    over 2006-2012 at observed production. The study does not give a
    yard-level subsidy rate suitable for direct microdata merging.
  exemptions:
  - The empirical cost estimates focus on Handysize bulk carriers; other vessel types appear in descriptive shares, not the same estimated treatment
  compliance: >
    Neither payment take-up nor compliance with each finance and support
    instrument is observed. The paper's inferred wedge must not be read as
    universal receipt by every Chinese shipyard.
  exposure_construction: >
    Reproduce the published object only with a world Handysize yard-quarter
    panel, new and used ship prices, shipowner-demand states, steel prices,
    backlogs, capacity and production. Estimate the dynamic demand and
    shipyard cost system with a China x post-2006 cost term; simulate a
    no-cost-support counterfactual separately from a no-new-entrants
    counterfactual. A simple China x post indicator alone is not the
    paper's causal estimator.
  required_identifiers:
  - shipyard ID and country
  - quarter
  - ship type restricted to Handysize bulk carriers for the estimated model
  - ship/vessel ID and age for price transactions
  spillovers: >
    Global substitution is intrinsic to the model: Chinese cost reductions
    and entry alter ship production, ship prices, Japanese market share,
    freight rates and cargo-shipper surplus. Foreign yards are affected
    competitors, not insulated no-interference controls.
research_compatibility:
  outcome_domains:
  - shipyard production and global market share
  - prices, industry costs, and shipper surplus in structural counterfactuals
  - strategic industrial support and capacity expansion
  affected_populations:
  - Chinese Handysize shipyards
  - foreign competing Handysize shipyards
  - shipowners and cargo shippers through the estimated market equilibrium
  mechanism_channels:
  - inferred operating-cost support
  - new Chinese yard entry and capacity expansion, separately modeled
  - production reallocation through dynamic shipbuilding and shipping demand
  best_for:
  - Model-based evaluation of the aggregate operating-cost wedge and capacity expansion associated with China's 2006 shipbuilding push
  - Studying global reallocation and welfare under an explicit dynamic world-market model
  not_good_for:
  - Treating the plan as a randomized or staggered firm-level subsidy grant
  - A China-versus-foreign-yard DID that ignores shared world prices and demand shocks
  - Inferring which individual Chinese shipyard received a loan, cash transfer, or 13-20% cost reduction
  - Treating 2009 credit and capacity controls as the same 2006 intervention
design:
  claim_type: structural
  affordances:
  - China-specific 2006 break in modeled Handysize production costs
  - Quarterly yard choices, capacity, backlogs, and world new/used ship prices
  - Separate counterfactual removal of cost support and new yard entry
  candidate_designs:
  - Dynamic demand-and-supply estimation of a China x post-2006 cost term
  - Structural counterfactuals with versus without the inferred cost wedge and new entrants
  identifying_variation: >
    Production decisions and new/used ship prices before and after 2006
    across China and foreign producers, conditional on shipyard capacity,
    backlog, time-to-build, steel prices and estimated shipping-demand
    states. The China-post coefficient represents a residual cost shift
    consistent with subsidies, not a directly randomized policy contrast.
  primary_strategy: >
    Estimate shipowner willingness to pay from new and used ship prices,
    recover yard cost parameters from observed ordered production choices
    and dynamic optimality conditions, test the China x post-2006 cost term,
    then simulate market equilibria under no entrants and no interventions.
    No published firm-level DID or event-study subsidy effect is used.
  estimand: >
    Model-implied post-2006 differential change in Chinese Handysize yard
    operating costs and simulated effects of that cost wedge plus capacity
    entry on production, prices, costs and shipper surplus, conditional on
    the structural model and its counterfactual assumptions.
  treatment_variable: >
    China x post-2006 term in the estimated cost function; its coefficient
    is interpreted as an inferred operating-cost reduction. New yard entry
    is a distinct counterfactual component.
  comparison_logic: >
    Chinese pre/post cost function relative to other producer countries
    within the same world market, after fitting demand and dynamic production
    choices. The paper's counterfactual holds observed demand and steel
    states and changes Chinese cost and entry assumptions.
  estimation_notes: >
    Main production panel: 192 Handysize yards, including 119 Chinese,
    Q1 2001-Q3 2012; the cost sample with capacity data has 4,741
    yard-quarter observations. Table 6 reports a dynamic China-post
    cost coefficient; Table 7 separately contrasts baseline, no entrants,
    and no interventions. Other ship types enter descriptive Table 1 only.
  assumptions:
  - The structural demand, production cost, expectation and state-transition specifications are adequate for recovering latent costs
  - Competing China-specific technology or productivity shifts around 2006 do not fully explain the recovered cost break
  - The model's unexpected one-shot regime change and counterfactual treatment of entrants approximate actual industry expectations
  - Global demand and steel-price states capture major contemporaneous shocks, including the financial-crisis period
  diagnostics:
  - Inspect China-year cost coefficients and Japan-post placebo
  - Check alternative cost curvature, year trends, state transitions and LASSO approximations
  - Compare baseline simulated production with observed production
  - Separate existing-yard results from new-entry effects
threats:
- type: latent-policy-measure
  basis: documented
  condition: >
    The 13-20% wedge is estimated from behavior and prices, not from observed
    subsidy transactions; technology, learning or omitted cost changes could
    partly produce the same pattern.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Compare alternative cost functions, timing and placebo country breaks
- type: simultaneous-capacity-expansion
  basis: documented
  condition: >
    New Chinese docks and entrants grew sharply around 2005-2006; confusing
    capacity support with marginal operating-cost support would distort the
    mechanism and welfare counterfactual.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Report no-entrants and no-interventions counterfactuals separately
- type: demand-and-crisis
  basis: documented
  condition: >
    World shipping demand and steel prices shifted over the 2001-2012
    window, and 2009 introduced a separate crisis response. A simple
    before/after comparison would confound these changes.
  evidence_refs:
  - E1
  - E3
  possible_diagnostics:
  - Model shipping-demand and steel-price states; examine alternative time specifications
empirical_requirements:
  contract_version: 1
  population: World Handysize bulk-carrier shipyards, including Chinese, Japanese, South Korean and European yards
  observation_unit: Shipyard-quarter, linked to new/used ship transaction and world-market quarter data
  geography_level: Shipyard country in a global market
  time_start: 2001
  time_end: 2012
  minimum_frequency: quarterly
  minimum_pre_periods: 5
  minimum_post_periods: 6
  required_fields:
  - shipyard ID, country, quarter and Handysize vessel type
  - yard orders or quarterly production, backlog and delivery time
  - yard entry date, dock/berth count and maximum dock length
  - new-ship contract dates and prices
  - used-ship transaction date, price, age and origin
  - fleet age distribution, shipping demand and steel-plate prices
  required_identifiers:
  - shipyard ID and country
  - quarter
  - ship or contract ID for prices
  treatment_key:
  - Chinese yard x post-2006 model term
  - separate post-2005 Chinese entrant classification
  treatment_source: >
    Clarksons Research world shipbuilding, contracts, transactions, yard
    characteristics and fleet series; Japanese steel-plate price. The
    official plans establish sector policy context but supply no
    yard-level cost-subsidy amount.
  measurement_risks:
  - Most new-ship contract prices are missing, motivating used-ship price data
  - Yard capacity snapshots and entry timing require reconstruction
  - The estimated subsidy wedge is model-dependent and not a directly joinable field
  - The paper's 2012 endpoint is sample coverage, not a policy sunset
evidence:
- id: E1
  source_type: paper
  citation: 'Kalouptsidi, Myrto. 2018. "Detection and Impact of Industrial Subsidies: The Case of Chinese Shipbuilding." Review of Economic Studies 85(2): 1111-1158. DOI 10.1093/restud/rdx050.'
  url: https://doi.org/10.1093/restud/rdx050
  date: 2018
  supports:
  - scope.china_relevance
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.intensity
  - assignment.exemptions
  - assignment.exposure_construction
  - design.claim_type
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_source
  - design_applications.empirical_design
  - design_applications.data_used
  verification_status: verified
  access_level: full-text
  locator: 'Published OUP typeset PDF inspected from author research page https://sites.google.com/site/myrtokaloup/research (myrtosubsidies.pdf): pp. 1111-1118 (scope and policy context), 1124-1126 (model and Clarksons data), 1131-1139 (cost estimation and robustness), 1139-1141 (counterfactuals), Tables 1, 2, 4, 6 and 7; publisher DOI metadata verified separately.'
- id: E2
  source_type: policy-document
  citation: 国家发展改革委、国防科工委, 船舶工业中长期发展规划（2006-2015年）, public edition, State Council approved August 2006.
  url: https://www.ndrc.gov.cn/fggz/fzzlgh/gjjzxgh/200710/P020191104623363865929.pdf
  date: 2006
  supports:
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.announcement
  - timeline.implementation_start
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: 'NDRC public PDF pp. 1, 8-12: plan period and three bases; clauses 25-29 priority capacity projects, 33-40 approval/eligibility and fiscal-financial support, 44-47 working-capital and export credit. It supports policy scope and selective project rules, not actual subsidy receipt or 13-20% yard cost reductions. State Council approval month corroborated by NDRC 2007-12-03 base-progress notice.'
- id: E3
  source_type: policy-document
  citation: 国家发展改革委, 船舶工业调整和振兴规划, issued 2009-06-09.
  url: https://zfxxgk.ndrc.gov.cn/web/iteminfo.jsp?id=251
  date: '2009-06-09'
  supports:
  - identity.implementation_regime
  - timeline.local_timing
  - research_compatibility.not_good_for
  verification_status: verified
  access_level: official-document
  locator: 'NDRC webpage header and sections I, IV(1)-(2), IV(6): crisis response for 2009-2011, credit/export buyer financing and temporary bar on new dock approvals outside the earlier plan; successor package, not the observed 2006 cost-shift assignment.'
design_applications:
- paper: 'Detection and Impact of Industrial Subsidies: The Case of Chinese Shipbuilding'
  doi: 10.1093/restud/rdx050
  journal: Review of Economic Studies
  year: 2018
  research_question: Is a China-specific operating-cost decline consistent with industrial subsidies after 2006, and how much did inferred cost support and new capacity change world shipbuilding outcomes?
  population: 192 world Handysize bulk-carrier yards, 119 in China; production observed Q1 2001-Q3 2012
  outcome: Estimated shipyard operating costs and simulated production shares, ship prices, profits, freight rates and cargo-shipper surplus
  data_used:
  - Clarksons Research yard-quarter Handysize orders, backlog and delivery times
  - Clarksons new-ship and second-hand ship contract prices, vessel age and origin
  - Clarksons yard capacity, entry and industry fleet/order series
  - Japanese steel-plate price series
  treatment_encoding: China x post-2006 term in estimated cost function; newly entered yards removed separately in counterfactuals
  comparison: Chinese pre/post modeled costs relative to other producer countries in the same world market, not an observed subsidy-recipient versus nonrecipient DID
  empirical_design: Dynamic industry demand-and-supply estimation; estimate Chinese cost shift from yard choices and ship prices, then simulate no-entrant and no-intervention counterfactuals
  assumptions:
  - Demand and yard dynamic optimization adequately recover unobserved costs
  - No unmodeled China-specific technological break fully mimics the 2006 cost change
  - Industry participants' expectations and counterfactual states are adequately approximated
  threats_addressed:
  - Alternative cost curvature, time controls and Japan-post placebo
  - Separate role of new yard entry and operating-cost support
  - Sensitivity to state transitions, existing-yard sample and dynamic approximation
  evidence_refs:
  - E1
readiness_blockers:
- Actual yard-by-yard subsidy receipt, transfer amount and local start dates are unobserved. The conditional research use is the published structural China-post cost wedge, not a direct policy-exposure file for firm DID or event studies.
- The paper models an unexpected immediate 2006 regime shift; the official plan and contemporaneous capacity expansion do not independently establish that expectation timing or isolate the cost effect of one named financing instrument.
method_transfer: null
---
## Institutional Background

The 2006-2015 development plan sought to expand Chinese shipbuilding, especially
three coastal bases, through prioritized capacity projects and a menu of fiscal,
financial, tax, credit and insurance support. The plan sets conditions for large
projects and preferential categories; it does not publish a national list of
shipyard operating subsidies or a universal cost reduction. A separate 2009
crisis-era plan changed finance support and restricted new capacity approvals.
Those are institutional facts, not the same thing as the paper's estimated
cost wedge. [E2; E3]

## What Changed

Kalouptsidi's world-market analysis focuses on Handysize bulk carriers. Chinese
yard entry and docks expanded sharply around 2005-2006. After 2006 the estimated
cost function of Chinese yards falls relative to its pre-period and other
producer countries, by 13-20% across reported specifications. The author
interprets this as strong evidence consistent with operating-cost subsidies;
the amount is inferred from behavior and prices, not read from government
ledgers. New facilities are a second, separately modeled intervention. [E1]

## Implementation and Assignment

The official plan offers differentiated support to approved projects and
qualified enterprises, but actual beneficiaries and payment dates are not
recoverable from the inspected documents. In the paper's model every Chinese
Handysize yard in the post-2006 regime shares a country-period cost term; this
is a measurement convention. The paper tests regional onset using the first
new dock/berth operation as a proxy because official local implementation
dates were unavailable. That proxy cannot certify a subsidy date for a
particular yard. [E1; E2]

## Why This Creates Empirical Variation

The study combines production decisions at 192 Handysize yards with new and
used ship prices, backlogs, capacity, steel prices and shipping-demand states.
It uses dynamic optimization to infer latent costs, tests the China-post-2006
cost term, then simulates what world production and welfare would look like
without new Chinese yards and without both modeled interventions. This is
a structural market-equilibrium comparison; a simple China-versus-Japan DID
would not reproduce it and would treat an affected competitor as an unaffected
control. [E1]

## Identification Risks

A China-specific productivity or technology change could also lower recovered
costs; the author tests time trends, other-country breaks, cost curvature and
existing-yard samples but does not observe subsidy payments. The structural
counterfactual also depends on demand, cost, dynamic expectations, entry and
the assumed 2006 regime shift. The 2009 financial-crisis response overlaps the
later sample years. These limits matter whenever the result is reused outside
its Handysize market and model. [E1; E3]

## Data Requirements

The published calculation needs quarterly global Handysize yard orders
(Q1 2001-Q3 2012), backlog, entry and capacity, 417 reported new-ship
contracts, 2,016 used-ship sale contracts, fleet and demand states, and
steel-plate prices. Clarksons Research is the main source. It is not
enough to merge a public policy-date column into firm accounts; reproducing
the estimated wedge requires the structural system and commercial market
data. [E1]

## Evidence Notes

E1 is the published article, inspected in the author-hosted publisher PDF.
E2 independently establishes the 2006 plan's scope and support menu; E3
establishes the distinct 2009 successor package. None of these sources
observes a complete recipient roster, firm-specific subsidy amount, or
local operating-subsidy start date. The 13-20% estimate is therefore a
model-based interpretation under stated alternatives, not an official
subsidy rate. [E1-E3]
