---
schema_version: 2
id: china-wwi-textile-import-disruption-port-access
name: WWI textile import disruption and mainland China's prewar port-access exposure
aliases: [一战纺织品进口中断, WWI Chinese textile industry, wartime import competition and port accessibility]
status: grounded
provenance:
  task_id: task-534839cd5ae0
scope:
  country: China
  regions: [Historical mainland Chinese counties in the published textile-industry panel]
  domains: [development, regional-economics, industrial-economics, firm-dynamics, international-trade, economic-history]
  variation_type: continuous-exposure
  knowledge_role: global-china-variation
  china_relevance: An external war disrupted imports actually faced by mainland textile producers; the paper interacts the shock with prewar county access to Chinese ports. This is not a Chinese port-opening policy or the1929 tariff reform.
identity:
  instrument: WWI-induced disruption of imported cotton textiles and machinery, differentiated by prewar county travel time to ports.
  authority: Foreign belligerents' production and shipping decisions, vessel requisitioning and disruption of commercial routes; China Maritime Customs recorded Chinese trade. No Chinese authority randomly assigned county exposure.
  legal_identifiers: [No common domestic policy eligibility instrument; wartime shipping restrictions and requisitions documented in contemporary consular trade reports]
  implementation_regime: External trade disruption interacts with an already established domestic transport network. Domestic producers face reduced import competition alongside delayed imported machinery, changing export demand and other wartime conditions. Shipping routes can be replaced; disruption is not universal closure.
  assignment_mechanism: Geography and prewar transport connections determine continuous proximity to import markets. The empirical exposure is log(1+shortest travel days to a port), interacted with national war/postwar windows or the national cotton-yarn import unit-value series. Port access is not randomly assigned.
  parent: null
  related_variations: []
timeline:
  announcement: No single domestic announcement defines county eligibility; the external war begins in1914.
  effective: The paper codes WWI_t=1 in1914–1919 and PostWWI_t=1 in1920–1925, with1907–1913 as the preperiod. The empirical war window includes1919 and must not be rewritten to end in1918.
  implementation_start: 1914
  implementation_end: 1919
  local_timing: Fixed prewar accessibility is interacted with common annual shock measures. Railways are restricted to1913 availability; Table2 labels the travel-cost measure1914. Military hostilities ending in1918 do not set the paper's recovery clock.
  anticipation: Early1914 observations precede the war; annual treatment aggregates within-year exposure. Machinery orders, delivery and operation can occur in different years, so investment and operating-mill responses can be delayed.
  last_verified: '2026-10-07'
assignment:
  unit: Historical county-year.
  treated: Continuously exposed mainland textile-industry counties, not a binary list of war-treated counties. The paper reports1789 counties and33991 county-years in1907–1925; a Shanghai-excluded alternative has1788 counties and33972 observations. Firms of different ownership can operate in the mainland sample.
  comparison_pool: Counties with different prewar travel times, observed before, during and after the shock. Inland counties are less directly connected, not unaffected controls; county and year effects absorb fixed location differences and common annual shocks.
  rule: Construct tau_i=log(1+minimum prewar travel days from county i to a port). Estimate separate WWI_t*tau_i and PostWWI_t*tau_i terms. Port-containing counties have tau_i=0. A price specification substitutes log(national yarn import value/quantity)*tau_i.
  intensity: Larger tau means weaker port access, not greater treatment dosage. A negative interaction can mean that the positive response is smaller inland; it is not an absolute national effect of war or a negative treatment effect for every county.
  exemptions: [No binary untreated group guaranteed, No whole-province exposure rule, Do not use foreign production locations as Chinese sample units]
  compliance: Route replacement, changes in foreign supply and machinery delivery make the realized shock heterogeneous. Contemporary Swatow reporting documents substitution of shipping routes and smaller vessels after wartime requisitioning; this corroborates imperfect disruption rather than uniform implementation.
  exposure_construction: Combine CHGISv6 rivers and historical courier roads with digitized rail routes available in1913, adding direct access links for unconnected counties. Assign rail/river/major-road/access-road speeds of1200/150/75/40km per day; minimize travel time to ports and apply log(1+days). An alternative minimizes to six yarn ports—Jiaozhou, Shanghai, Hankou, Chongqing, Guangzhou and Mengzi. Do not substitute the different six-port set in the later JCE tariff paper. Recover county identities and firm locations from the underlying historical joins rather than modern county codes.
  required_identifiers: [historical_county_id, province_id, year, mill_id, historical_port_id, transport_segment_id]
  spillovers: Domestic distribution and substitution transmit import conditions inland; neighboring counties and ports share routes. Spatial spillovers and exposure measurement limit a simple treated-versus-unaffected interpretation.
research_compatibility:
  outcome_domains: [operating textile mills, textile industrial expansion, initial capital of new textile firms]
  affected_populations: [mainland historical textile producers, industrial counties with different access to international trade]
  mechanism_channels: [reduced import competition, imported machinery delivery constraints, spatial market access, local industrial complements]
  best_for: [historical trade disruption and industrial development, heterogeneous responses by preexisting transport access]
  not_good_for: [random port placement, pure competition-only effects, modern firm effects without a historical bridge, new-firm entry inferred from operating stock alone, causal effects of bank placement]
design:
  claim_type: reduced-form
  affordances: [common external shock interacted with fixed spatial exposure, national import-unit-value interaction, annual exposure event study]
  candidate_designs: [continuous-exposure DID, event-study, county-year fixed-effects interaction]
  identifying_variation: Changes in operating-mill counts across counties with different prewar port access during1914–1919 and1920–1925; an alternative uses fluctuations in national yarn import unit values.
  primary_strategy: Eq1 regresses log(1+operating mills_it) on WWI_t*tau_i and PostWWI_t*tau_i with county and year fixed effects. Eq2 uses the logged national yarn import unit value interacted with tau_i. Inference clusters by province; these equations are not2SLS.
  estimand: Differential change in logged operating-mill counts along the prewar travel-cost gradient, conditional on the comparison assumptions. Year effects absorb the common shock; the interaction alone does not identify the national average effect of the war.
  treatment_variable: WWI_t*tau_i and PostWWI_t*tau_i, with tau_i=log(1+travel days). Price_t*tau_i is the paper's alternative encoding of the same trade disruption, not a second independent shock.
  comparison_logic: Requires that counties with different port access would have comparable conditional changes absent the trade shock, and that other changing determinants do not produce the same geographic gradient. Flat reported pretrends do not establish random geography or rule out every wartime channel.
  estimation_notes: Eq1 and Table3 are onpp267–269; Eq2 and Table4 onpp270–272. Yan2011 records99 mills' operation, acquisition, merger and exit, yielding a stock outcome. Du1991's109-firm initial-capital series omits exits and is a distinct robustness outcome. The national price construction in text differs from Table4's loose port-level wording; retain this discrepancy for code verification. Unit values can reflect quality and composition. Financial-complement interactions onpp276–277 are explicitly suggestive, not a separately identified bank reform. Replication DOI10.3886/E115822V1 is cited, but its package was not inspected.
  assumptions: [conditional parallel trends across port-access gradients, stable prewar network measurement, correct historical geography and operating dates, no omitted differential contemporaneous shocks, adequate spatial support and inference]
  diagnostics: [year-by-travel-cost pretrends and postpaths, Shanghai-excluded results, major-port and transport-speed sensitivity, alternative mill histories and capital outcomes, domestic conflict and concession gradients, yarn quality and currency sensitivity, spatial dependence and province-cluster adequacy]
threats:
  - type: selective-port-access
    basis: documented
    condition: Ports and concessions were industrial centers with distinctive institutions and inputs before the war; fixed effects alone do not absorb differential subsequent trajectories.
    evidence_refs: [E1]
    possible_diagnostics: [pretrend power, Shanghai exclusion, historical industrial-center controls, alternative port definitions]
  - type: bundled-external-shock
    basis: documented
    condition: Imported machinery was delayed while foreign competition changed. Currency, export demand and domestic political events also changed; the contrast is not a clean competition-only intervention.
    evidence_refs: [E1, E3]
    possible_diagnostics: [order-versus-delivery histories, national-shock and local-conflict interactions, outcome-specific channel analysis]
  - type: exposure-measurement
    basis: reported
    condition: Network speeds partly proxy passenger rather than commodity travel; historical courier roads proxy later major roads. National import unit values are not a pure external price instrument.
    evidence_refs: [E1, E2]
    possible_diagnostics: [alternative speeds and ports, transport-network reconstruction, quality-specific yarn prices, inspect author price aggregation]
  - type: outcome-and-historical-join
    basis: documented
    condition: Sparse historical mill histories require consistent operation, merger and exit definitions. Initial-capital flows and operating stocks are not interchangeable, and current administrative codes cannot reproduce historical county joins.
    evidence_refs: [E1]
    possible_diagnostics: [firm-life-history audit, ownership and Shanghai sensitivity, historical county membership crosswalk]
empirical_requirements:
  contract_version: 1
  population: Mainland historical counties linked to the paper's operating-mill panel; retrieve the actual1789-county membership rather than assuming every modern Chinese county belongs.
  observation_unit: county-year
  geography_level: historical county
  time_start: 1907
  time_end: 1925
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields: [annual operating textile-mill count, mill founding and actual operation dates, mill merger acquisition and exit histories, fixed prewar travel days to ports, historical county sample membership and crosswalk, province identifier, year, domestic conflict and concession measures for diagnostics]
  required_identifiers: [historical_county_id, province_id, year]
  treatment_key: [historical_county_id, year]
  treatment_source: Author's CHGISv6/prewar transport construction and Eq1 in Liu2020; reconstruct travel times from documented routes and speeds or obtain the cited replication package. CMC quantities/values provide the optional national price series.
  measurement_risks: [historical names and boundary mapping, operating stock versus entry flow, transport speed approximation, sample membership, sparse counts and log(1+x), import-unit-value composition and currency]
evidence:
  - id: E1
    source_type: paper
    citation: 'Liu, Cong (2020). The Effects of World War I on the Chinese Textile Industry: Was the World’s Trouble China’s Opportunity? Journal of Economic History80(1):246–285.'
    url: https://doi.org/10.1017/S0022050719000858
    date: 2020
    supports: [identity.instrument, identity.implementation_regime, identity.assignment_mechanism, timeline.effective, timeline.local_timing, timeline.anticipation, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.intensity, assignment.exposure_construction, assignment.spillovers, design.primary_strategy, design.treatment_variable, design.estimation_notes, empirical_requirements.required_fields, design_applications.empirical_design, design_applications.data_used]
    verification_status: reported
    access_level: full-text
    locator: Final40-page journal PDF Liu_WWIFinal.pdf linked on https://sites.google.com/view/congliu/research; inspected cover and printedpp253–277, especiallypp256–262 data, Eqs1–2 onpp267/270, Tables3–5 and machinery discussionpp272–275. Journal80(1) and246–285 on actual final body; online2019-12-26. Results not independently rerun.
  - id: E2
    source_type: appendix
    citation: Liu2020 author-linked Online Appendix, Liu_WWI_OnlineAppendix.docx.
    url: https://sites.google.com/view/congliu/research
    date: 2020
    supports: [assignment.exposure_construction, design.estimation_notes]
    verification_status: reported
    access_level: appendix
    locator: Author-linked Dropbox appendix's paragraph text inspected in memory; AppendixA transport assumptions and AppendixB financial-institution typology, alternate-outcome/price figure descriptions. Math objects were not reconstructed; appendix table layout and code were not independently verified.
  - id: E3
    source_type: archive
    citation: US Bureau of Foreign and Domestic Commerce, Supplement to Commerce Reports, Annual Series52c, China,1915-06-10.
    url: https://archive.org/details/supplementto52191510unit
    date: '1915-06-10'
    supports: [identity.instrument, identity.implementation_regime, timeline.local_timing, assignment.compliance]
    verification_status: verified
    access_level: official-document
    locator: Original32-page government scan read atpp1–2 and27–28, p27 visually inspected. Shanghai account describes1914 war-related trade disruption and local-yarn substitution; Swatow account records interrupted German routes, replacement shipping and British vessel requisitioning. Corroborates local shock realization, not all county travel weights or a pure causal estimate.
design_applications:
  - paper: The Effects of World War I on the Chinese Textile Industry
    doi: 10.1017/S0022050719000858
    journal: Journal of Economic History
    year: 2020
    research_question: Did wartime import disruption foster Chinese textile-industry expansion, and how did prewar trade access shape its geography and timing?
    population: Published1789-county historical Chinese panel in1907–1925; operating textile mills including Chinese and foreign ownership, with Shanghai-excluded alternatives.
    outcome: log(1+annual operating textile mills); alternative initial capital invested by new textile firms.
    data_used: [Yan2011 mill histories, Du1991 initial-capital entry data, CMC trade reports and Hsiao1974, CHGISv6 rivers courier roads and county geography, CIA1954 railway map with Zhang1997 construction dates, prewar local characteristics and domestic conflict sources]
    treatment_encoding: War and postwar dummies interacted with log(1+prewar port travel days); alternative logged national import unit value interacted with the same travel measure.
    comparison: Across county port-access gradients with county/year fixed effects and province-clustered inference; annual interactions check pretrends.
    empirical_design: Continuous-exposure DID and fixed-effects price interaction; not an IV estimate or randomized port assignment.
    assumptions: [conditional parallel trends, no confounding changing geographic gradient, credible historical exposure and outcome measurement]
    threats_addressed: [reported pretrends, Shanghai exclusion, major-port alternative, separate initial-capital source, ownership splits, suggestive machinery-delay evidence]
    evidence_refs: [E1, E2]
method_transfer: null
readiness_blockers:
  - Conditional use requires the original historical county membership and mill-to-county join plus prewar transport weights; modern county names or straight-line distance alone do not reproduce the treatment.
  - The cited public replication deposit was not read. Eq2's text specifies national import unit values while Table4 describes port-level prices; inspect actual aggregation before reproducing the price variant. Eq1's war-window specification does not require silently resolving that discrepancy.
  - A new outcome requires reassessing port selection, multiple wartime channels, spatial propagation and the1919 recovery clock. The reported result is not a universal exogeneity certificate or a national welfare estimate.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

The external war changed the conditions under which mainland textile producers
competed and obtained machinery [E1, reported claim]. Preexisting ports and
transport links determined market access, not random domestic eligibility.
Contemporary consular reporting corroborates mainland shipping disruption and
route replacement [E3]. This case is therefore China-facing global variation,
not an overseas method imported merely because it seems transferable.

## What Changed

Imported cotton products became less available while machinery deliveries also
slowed. The paper examines the resulting spatial pattern of industrial expansion,
not an isolated competition channel [E1, reported claim]. A delayed operating-mill
response can follow earlier investment without implying a late local policy start.

## Implementation and Assignment

Use fixed prewar shortest travel days, then apply the specified log transformation
and common annual windows. The paper's1914–1919 window is deliberate and differs
from military hostilities ending in1918. More distant counties have larger tau;
calling them more intensively treated would reverse the interpretation [E1].
The historic network, mill identities and county membership must be preserved
when constructing an executable panel.

## Why This Creates Empirical Variation

County and year effects leave differential changes by prewar port access.
The main contrast compares those gradients over time; inland places need not be
unaffected. The price interaction describes the same institutional shock using
another national time series, so it should not inflate the variation count [E1].
Neither specification uses port distance as a2SLS instrument.

## Identification Risks

Ports, concessions and industrial centers can evolve differently for reasons
other than import competition. Machinery shortages and domestic political
changes are substantive channels or confounders, depending on the question
[E1, reported claim; analytical inference]. A flat pretrend or a robustness result
does not resolve these risks for a new outcome. The paper labels its local
financial-complement evidence suggestive; bank geography is not another causal
policy experiment.

## Data Requirements and Evidence Boundary

Yan's baseline counts mills in operation, including their exits and mergers.
Du's initial-capital series concerns new firms and cannot substitute for that
stock without changing the outcome [E1]. Recover historical geography and the
prewar network before estimation. The replication DOI is a concrete access lead,
not a claim that its files or results have been inspected.

## Evidence Notes

The actual final journal body supplies the estimating equations, windows,
sample counts and outcome definitions. Author-linked appendix paragraphs explain
the transport approximations, but extracted prose is not verification of every
math object or table. The original government report corroborates shock
realization, not the author's complete exposure vector. This record supports a
conditional research decision; it is not a completed independent replication.
