---
schema_version: 2
id: china-urban-rail-line-launch-road-substitution
name: China Urban Rail Line Launches and Road-Substitution Exposure
aliases:
- Subways and Road Congestion
- Gu Jiang Zhang Zou urban rail openings
- 城市轨道交通开通 道路拥堵
status: grounded
provenance:
  task_id: task-585631affc57
scope:
  country: China
  regions: [mainland China]
  domains: [urban, regional-economics, transportation, infrastructure]
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: Actual urban rail launches in25 mainland cities during2016-2017 change the public-transport alternatives to selected road trips. The inspected application studies road-segment speed, not a hypothetical national subway instrument.
identity:
  instrument: Passenger access to a newly operating urban rail line or extension, mapped to roads that substitute for journeys using that line. This includes the Xijiao surface tram; it is not exclusively underground metro.
  authority: National construction-planning review, provincial project approval and municipal implementation/operating-readiness authorities; local operators provide passenger service.
  legal_identifiers: [国办发〔2003〕81号, 发改基础〔2015〕49号, Beijing Municipal Commission of Transport2017-12-29 opening announcement]
  implementation_regime: The2016-2017 line-launch cohort under the then applicable urban rail planning and approval framework. Construction approval, completed works, passenger testing and regular operation are different events; later approval reforms are outside this cohort.
  assignment_mechanism: Line-specific passenger-access dates interacted with road segments identified through substitution between public-transport and driving routes. Siting and opening are chosen, not randomized; random partitioning of comparison roads is an estimation construction only.
  parent: null
  related_variations: [china-beijing-subway-grid-pair-connectivity]
timeline:
  announcement: null
  effective: null
  implementation_start: '2016-08-01'
  implementation_end: null
  local_timing: >
    The paper's45 launches, including7 extensions, occur within August2016
    through December2017; the hourly observation window ends January2018.
    These are sample bounds, not a national reform date or service termination.
    Table1 reports official openings. AppendixA.1 advances timing to the first
    contiguous passenger-test day, but excludes detached passenger-test periods.
    Xijiao began public operation December30,2017 according to the official
    announcement. Its subsequent interrupted operation needs separate coding:
    AppendixA.1 and FigureB.6 give inconsistent January closure dates.
  anticipation: Planning and construction precede service; announced opening dates and passenger trials can affect behavior. Opening need not be an unexpected event.
  last_verified: '2026-10-04'
assignment:
  unit: Directed road segment linked to a particular line-launch event and an hourly observation, subsequently aggregated to event-relative weeks.
  treated: Sampled roads on driving alternatives to grid-pair trips whose best public-transport route uses the newly launched line, rather than every road in a treated city or every road near a station.
  comparison_pool: Sampled roads around existing or planned lines in17 cities with no new rail launch during the event sample. These cities are not necessarily without rail service. Control roads are randomly partitioned into45 groups and assigned to launch events.
  rule: Government planning/project review and local operating-readiness processes permit launches; empirical exposure is assigned by actual passenger access and route substitution. Official city eligibility requirements do not constitute a paper-used regression discontinuity.
  intensity: Baseline road-by-event access contrast; heterogeneous responses may depend on road class and trip substitution. Station distance alone is not the published exposure measure.
  exemptions:
  - Baseline excludes local streets, weekends and national holidays, and retains roads with the required balanced observations.
  - Detached passenger-test periods are excluded; empty-train equipment tests are not passenger access.
  - Provider-wide missing periods September1-10 and October10-November30,2016 are not valid speed observations.
  compliance: National approval or a planned opening does not establish actual access. Municipal readiness/acceptance is required; the Beijing announcement confirms selected public openings, not every cohort date. Interrupted service must remain visible rather than coding once-open as permanently operating.
  exposure_construction: >
    Recover city, line/extension identity, historical geometry, official opening
    and passenger-test dates from Table1 and AppendixA.1. Select5km rail
    stretches with2.5km buffers, adjusting overlaps as in the paper. Divide
    buffers into1km grids, find grid pairs whose best public-transport route
    uses the new line, and identify roads on their best driving alternatives
    under morning/evening rush conditions. Join directed segment IDs and
    geometry to historical hourly Baidu speeds and road classes. For each
    launch, assign a control-road group from a no-launch city pool and align
    both sides to the same calendar dates. Use six pre-weeks and up to48
    post-weeks, retaining the test-ride adjustments, missing intervals and
    service-interruption flags. Residualize log speed by segment-by-weekday-
    by-hour effects before event-week aggregation. Historical routing vintage,
    segment-ID crosswalk and operating continuity are reproduction conditions;
    querying today's routes or replacing substitution with proximity creates
    a different treatment and must be labelled accordingly.
  required_identifiers: [city_id, line_event_id, directed_road_segment_id, observation_datetime, event_relative_week]
  spillovers: New service changes driving routes and connected rail/bus trips beyond directly substitutable roads. Roads near old lines and other events can also respond; the buffer is not an interference boundary.
research_compatibility:
  outcome_domains: [Road speed, Local congestion, Travel-time reliability, Urban transport substitution]
  affected_populations: [Road users and passengers in sampled mainland urban corridors]
  mechanism_channels: [Public-transport substitution, Route redistribution, Feeder-network changes, Construction completion]
  best_for: [Short-run local transport responses when historical passenger access and directed-road routing/speed data can be recovered.]
  not_good_for:
  - A citywide congestion or welfare effect from selected downtown road buffers alone.
  - Firm entry or productivity effects without firm-location links and a separately defended exposure/lag model.
  - Treating project approval, planned station proximity or random control partitioning as randomized line openings.
design:
  claim_type: reduced-form
  affordances: [Line-specific launch timing, High-frequency pre/post road speeds, Explicit route-substitution definition, Same-calendar comparison events]
  candidate_designs: [Stacked road-segment event study, Event-cohort DID with defended comparison roads]
  identifying_variation: Changes in sampled road speed around passenger access to a substitutable rail route, relative to calendar-aligned no-launch-city roads, conditional on counterfactual trends and differential seasonality.
  primary_strategy: Equation1 residualizes hourly log speed by road-segment-by-weekday-by-hour effects. Equation2 uses a stacked event study with road-segment and event-group-by-event-week effects and calendar-week interactions with city log population and log GDP per capita.
  estimand: Event-time change in residual log speed on directly substitutable sampled roads relative to assigned controls; a local short-run operating response, not a whole-city average effect.
  treatment_variable: Treated road segment interacted with event weeks -6 through47, omitting week -1; the access date incorporates contiguous passenger-test rides.
  comparison_logic: Each treated line event shares actual calendar time with a randomly assigned comparison-road group. Both groups can have rail networks; the comparison city has no new launch in the event sample. Allocation of roads to event stacks is not allocation of infrastructure.
  estimation_notes: Baseline uses weekday7-9AM and17-19PM observations and event-group clustering. The paper reports alternative dependence/inference checks. Its treated-only equation3 uses later openings as comparisons and is a distinct robustness specification, not an automatic substitute for the stacked design.
  assumptions:
  - Selected treated and comparison roads would have comparable residual-speed trends after the specified calendar and city-seasonality controls.
  - Construction recovery and concurrent feeder/road changes do not produce the attributed rail-only response.
  - Historical routing, provider sampling and balanced-panel exclusions do not change differentially at access dates.
  - Service interruptions and spatial/network interference are represented adequately for the chosen estimand.
  diagnostics:
  - Inspect event pre-trends, placebo dates and city-specific seasonal patterns; six pre-weeks and nonrejection cannot establish parallel trends.
  - Compare road classes, buffer/routing definitions and alternative comparison cities without silently changing the estimand.
  - Map construction completion and concurrent road/bus changes; distinguish a bundled opening effect from rail-only substitution.
  - Recover operating continuity and code provenance, report cohort influence and dependence-sensitive inference.
threats:
- type: selected_openings_and_differential_seasonality
  basis: reported
  condition: Treated cities are larger/richer and many launches occur in December near the subsequent Spring Festival. Common time effects alone do not remove city-differential seasonal traffic patterns; a short clean pre-period offers limited reassurance.
  evidence_refs: [E3]
  possible_diagnostics: [Calendar-by-city-characteristic sensitivity, Placebo opening dates, Cohort-specific trend and influence plots]
- type: bundled_opening_and_construction_recovery
  basis: documented
  condition: Beijing's opening announcement also describes new access roads and adjusted bus routes. Readiness follows construction, so speed gains can combine rail access, road restoration and feeder changes rather than a pure rail-only channel.
  evidence_refs: [E1, E2, E3]
  possible_diagnostics: [Recover corridor construction dates, Map feeder/road interventions, State bundled versus rail-only estimand]
- type: passenger_test_and_interrupted_service
  basis: reported
  condition: AppendixA.1 distinguishes contiguous and detached tests. For Xijiao it reports a January1 incident/closure and February28 resumption, while FigureB.6 describes January4 closure and March1 reopening; the latter is outside the speed window. Exact daily operational extent and continuity are not independently resolved here.
  evidence_refs: [E2, E3]
  possible_diagnostics: [Recover operator logs and author coding, Flag uncertain service days, Report explicit Xijiao exclusion or censoring sensitivity]
- type: routing_vintage_and_network_interference
  basis: inferred
  condition: Current route results or road IDs need not reproduce2016-2017 substitution. Selection of downtown buffers and re-routing restrict external validity; directly affected and comparison roads can share network spillovers.
  evidence_refs: [E3]
  possible_diagnostics: [Historical geometry and ID crosswalk, Provider coverage audit, Alternative exposure and spillover analysis]
empirical_requirements:
  contract_version: 1
  population: Directed road segments sampled around urban rail corridors in25 launch cities and17 no-launch cities; not all roads or travelers in mainland China.
  observation_unit: road-segment-hour joined to line event, then aggregated to road-segment-event-week
  geography_level: urban corridor and directed road segment
  time_start: '2016-08-01'
  time_end: '2018-01-31'
  minimum_frequency: hourly raw speed with weekly event aggregation
  minimum_pre_periods: 6
  minimum_post_periods: 1
  required_fields:
  - Directed segment coordinates, length, road class and historical ID/name crosswalk; city and line-event identity.
  - Historical rail geometry, grid origins/destinations, route-query rules and rush-hour substitution mapping.
  - Opening, contiguous/detached passenger-test and interruption dates, including date uncertainty flags.
  - Hourly speeds, observation coverage, weekday/holiday/hour indicators and baseline balanced-panel filters.
  - City population/GDP per capita and explicit control-road allocation needed for published seasonality/stack construction.
  required_identifiers: [city_id, line_event_id, directed_road_segment_id, observation_datetime, event_relative_week]
  treatment_key: [line_event_id, directed_road_segment_id, observation_datetime]
  treatment_source: Publisher-linked Table1 and AppendixA.1 define the paper's roster and test adjustments; municipal/operator evidence must establish realized access for reuse. Exposure additionally requires historical route substitution, not just the date table.
  measurement_risks:
  - Baidu historical hourly road speeds require lawful access and provider-vintage coverage. No raw speed download, license or code execution was verified.
  - Replication-deposit metadata and a listed README do not prove public access to all raw data, historical route queries or author random partition seeds.
  - Six pre-weeks and up to48 post-weeks are the reported window; late2017 events have fewer observed post-weeks before the January2018 endpoint. One post-week suffices for a short-run query, not replication of long-horizon coefficients.
evidence:
- id: E1
  source_type: policy-document
  citation: NDRC, 关于加强城市轨道交通规划建设管理的通知, 发改基础〔2015〕49号.
  url: https://zfxxgk.ndrc.gov.cn/web/iteminfo.jsp?id=307
  date: '2015-01-12'
  supports: [identity.authority, identity.legal_identifiers, identity.implementation_regime, assignment.rule, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: SectionsII(2)-(5),III(1)-(2),IV(1)-(2) inspected2026-10-04; national planning review, provincial approval, funding and operating-readiness responsibilities. Not a list of actual45 launches.
- id: E2
  source_type: implementation-document
  citation: Beijing Municipal Commission of Transport, public opening announcement for Xijiao, Yanfang and S1, December29,2017.
  url: https://jtw.beijing.gov.cn/xxgk/xwfbh/201912/t20191209_1007565.html
  date: '2017-12-29'
  supports: [identity.instrument, timeline.local_timing, assignment.compliance, research_compatibility.mechanism_channels]
  verification_status: verified
  access_level: official-document
  locator: Opening paragraph, Xijiao section and final feeder-road/bus paragraphs inspected2026-10-04. December30 public operation; Xijiao is a9km surface modern tram. URL migration date is not the original announcement date. Confirms this example only, not all cohort dates or subsequent uninterrupted service.
- id: E3
  source_type: paper
  citation: Gu, Yizhen, Chang Jiang, Junfu Zhang and Ben Zou. Subways and Road Congestion, publisher-linked manuscript with appendix for AEJ Applied2021.
  url: https://www.aeaweb.org/articles/materials/14228
  date: 2021
  supports: [identity.assignment_mechanism, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.intensity, assignment.exemptions, assignment.exposure_construction, assignment.required_identifiers, timeline.local_timing, timeline.anticipation, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.population, empirical_requirements.required_fields, empirical_requirements.measurement_risks, design_applications.population, design_applications.outcome, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design]
  verification_status: reported
  access_level: full-text
  locator: 63-page publisher-linked manuscript; printed mainpp4-14 Sections2.1-3.1 equations1-3, Table1 printedp32, AppendixA.1 printedp8 and AppendixB.1 pp9-10 inspected2026-10-04. Table1 and A.1 visually inspected; FigureB.6 caption text inspected, not its plotted estimates. This is the supplemental manuscript, not an assertion that the access-restricted final typeset PDF was inspected or that author code was run.
- id: E4
  source_type: replication
  citation: OpenICPSR, replication deposit115681V1 linked by the AEA article.
  url: https://doi.org/10.3886/E115681V1
  date: 2020
  supports: [empirical_requirements.measurement_risks]
  verification_status: reported
  access_level: metadata
  locator: VersionV1 landing page and README file listing inspected2026-10-04. Download/preview did not provide an inspected README body; no raw-data availability, licensing, route vintage or executable replication claim.
- id: E5
  source_type: paper
  citation: AEA publisher record, AEJ Applied13(2)(2021),83-115.
  url: https://doi.org/10.1257/app.20190024
  date: 2021
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: reported
  access_level: metadata
  locator: Publisher header, authors, issue/page citation and supplemental links inspected2026-10-04. Final PDF link requires membership/institutional access.
- id: E6
  source_type: policy-document
  citation: 国务院办公厅关于加强城市快速轨道交通建设管理的通知, 国办发〔2003〕81号, government gazette reproduction.
  url: https://zfgb.fujian.gov.cn/6914
  date: 2003
  supports: [identity.legal_identifiers, identity.implementation_regime, assignment.rule]
  verification_status: verified
  access_level: official-document
  locator: PartsI-II inspected2026-10-04; fiscal, GDP, urban-population and passenger-demand conditions, planning review and financing requirements. They are not the paper's treatment cutoff or proof of realized service.
design_applications:
- paper: Subways and Road Congestion
  doi: 10.1257/app.20190024
  journal: 'American Economic Journal: Applied Economics'
  year: 2021
  research_question: How does new urban rail access affect speed on roads that substitute for the new public-transport journeys?
  population: 45 launches including7 extensions in25 mainland cities, plus roads in17 no-launch cities; selected corridor roads observed August2016-January2018.
  outcome: Residual log road speed during weekday morning/evening rush periods.
  data_used: [Baidu Maps hourly directed-road speeds, Rail opening and passenger-test chronologies, Grid-pair route queries and road geometry, City population and GDP per capita]
  treatment_encoding: Direct-road-substitution exposure around line-specific passenger access, with contiguous tests advancing dates and detached tests removed; service-interruption coding still requires author/operator reconciliation.
  comparison: No-launch-city sampled roads randomly partitioned into event comparison groups; not random rail assignment and not necessarily cities without rail.
  empirical_design: Hourly residualization followed by stacked weekly road-segment event-study DID, with event-group time effects and city-characteristic differential seasonality controls.
  assumptions: [Comparable conditional counterfactual speed trends, Adequate seasonal and opening-bundle separation, Stable provider/routing measurement, Defended network-interference interpretation]
  threats_addressed: [Reported seasonality and placebo analyses, Short pre-window to limit construction contamination, Road-sample and inference sensitivity]
  evidence_refs: [E3, E5]
method_transfer: null
readiness_blockers:
- Obtain lawful historical speed data, routing vintage and directed-road ID/geometry crosswalks; current map queries do not reproduce the historical treatment.
- Recover author allocation/code details and reconcile Xijiao's operating dates and partial/full service before exact reproduction. Explicit exclusion/censoring sensitivity is a new analysis, not a silently repaired original series.
- Defend counterfactual trends, seasonality, construction/feeder overlap and interference for the intended outcome; no intrinsically exogenous rail-opening claim is made.
---

## Institutional Background

Urban rail investment proceeds through planning, financing, project review,
construction and operating readiness. The2003 and2015 documents explain
why approval is selective and why approval dates cannot substitute for
passenger access [E1; E6]. The Beijing announcement supplies an actual
public-opening example, including the surface Xijiao tram [E2]. The
record preserves this broader urban rail identity instead of translating
all events into underground metro.

## What Changed

Passengers gained a new rail alternative on a particular date. Roads
that carry competing trips may then experience different demand. Gu et
al. measure that exposure by route substitution, not by treating every
road inside the city as affected [E3, reported]. A nearby station is not
sufficient: the relevant grid-pair public-transport route must use the
new line, and the road must appear on its driving alternative.

## Implementation and Assignment

Table1 identifies the launch sample; AppendixA.1 explains why passenger
tests matter [E3, reported]. For example, Zhengzhou Line2 has a reported
August10-19,2016 passenger trial contiguous with its August19 official
opening; the exposure starts at the first trial day. Xiamen Line1's
October6-11,2017 test is detached from its December31 opening and is
excluded instead. These are paper-reported dates, not an independently
verified nationwide operating roster.

The comparison pool comprises Changsha, Changzhou, Dongguan, Hohhot,
Jinan, Lanzhou, Luoyang, Nantong, Ningbo, Shaoxing, Shenyang, Shijiazhuang,
Taiyuan, Urumqi, Wuhu, Wuxi and Xuzhou [E3, Table1]. Their identifying
property is no new launch during the sample, not permanent absence of
rail. Future dates listed for planned lines are contemporary plans,
not a verified retrospective chronology. Randomly assigning their roads
to event stacks aligns comparisons; it does not randomize the investment.

## Why This Creates Empirical Variation

Access changes at different line-specific dates and has different
substitution relevance across roads. This gives a local event-time
contrast with calendar-aligned comparisons. The useful research object
is the exposure mechanism, not a generic claim that subways raise growth.
The existing Beijing grid-pair connectivity record instead follows
network connectivity between pairs for collaboration. It shares some
physical infrastructure but has a materially different primary
assignment and join structure; another outcome using this same
road-substitution exposure belongs here, not in a new variation record.

## Identification Risks

December openings, Spring Festival traffic and differences in city size
make seasonal counterfactuals important [E3, reported]. Road restoration
and feeder changes are also part of the opening environment: the Beijing
notice explicitly describes access-road and bus adjustments [E2]. A
bundled local opening response may be defensible while a rail-only
interpretation remains unsupported. Neither short nonrejected pre-trends
nor the publication venue removes that distinction.

Xijiao illustrates the difference between first opening and continuous
operation. AppendixA.1's February28,2018 entry is linked to recovery
after a January incident; it is not an ordinary pre-opening passenger
test. Its note and FigureB.6 caption disagree on January closure timing
[E3, reported]. The discrepancy concerns operating continuity, not the
independently established December30 first opening [E2]. A user needing
exact daily treatment must resolve it rather than assume all45 events
remain continuously active after first access.

## Data Requirements

Join event identity and dates to historical rail geometry and route
substitution, then to directed road segments and hourly speed. Preserve
provider missing dates, holidays and road-class exclusions. Weekly speed
outcomes need the preceding hour-level residualization if reproducing
the paper. The deposit exists, but its metadata does not establish that
the private speed inputs or historical queries are freely obtainable
[E4]. This is a conditional research opportunity, not turnkey data.

## Evidence Notes

Methods and date tables come from an inspected publisher-linked
manuscript and appendix [E3]; the final typeset full text was access
restricted [E5]. Official sources establish the institutional regime
and selected realized access, not every author date. The record leaves
historical input access and the specific continuity discrepancy visible
so an agent can recommend it conditionally without inventing a completed
replication or certifying rail openings as exogenous.
