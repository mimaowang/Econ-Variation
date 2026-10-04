---
schema_version: 2
id: china-beijing-2008-private-car-driving-restriction-subway-premium
name: Beijing 2008 Weekday Driving Restriction and the Rising Subway Housing Premium
aliases:
- 北京2008年尾号限行
- Beijing one-day-per-week driving restriction 2008
- 车牌尾号每周停驶一天
- Beijing CDR 2008 subway capitalization
status: grounded
provenance:
  task_id: task-e6f648e1ff1b
scope:
  country: China
  regions:
  - 'Beijing (restricted area: within the 5th Ring Road, including the ring road)'
  domains:
  - urban-economics
  - transportation
  - housing
  - environmental-economics
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: >
    Beijing's weekday driving restriction by license-plate tail number, announced
    2008-09-28 and effective 2008-10-11, reduced private-car use on one weekday
    per week within the 5th Ring Road. The paper application uses the sharp start
    of the restriction as an exogenous shock to transportation mode choice and
    measures the rise in the housing-price premium for subway proximity
    (pseudo-repeat-sale design on Beijing second-hand transactions), with spatial
    heterogeneity by subway-versus-car travel-time substitutability.
identity:
  instrument: >
    Beijing's weekday driving restriction by license-plate tail number (按车牌尾号
    每周停驶一天), announced in the Beijing Municipal People's Government notice
    《关于实施交通管理措施的通告》 of 2008-09-28 and effective 2008-10-11: each
    non-official vehicle is banned from driving on one weekday
    per week, determined by the last digit of its plate, within the 5th Ring Road
    (including the ring road), 6:00-21:00. The five tail-number groups rotate
    their assigned weekdays on a schedule announced in advance by the traffic
    management bureau. The trial period ran 2008-10-11 to 2009-04-10 and the
    scheme was subsequently extended. The Olympic-period odd-even scheme
    (July-September 2008, reported dates 2008-07-20 to 09-20) is a separate,
    prior measure and not part of this instrument.
  authority: >
    Beijing Municipal People's Government (北京市人民政府), notice of 2008-09-28,
    implemented by the Beijing traffic management bureau; the notice also ordered
    official vehicles off the road one weekday per week (all roads, 0:00-24:00,
    with 30% of official cars sealed) from 2008-10-01 and, in a companion notice,
    staggered work hours (错时上下班) from 2008-10-11.
  legal_identifiers:
  - 'Beijing Municipal People''s Government notice of 2008-09-28 on implementing traffic management measures (北京市人民政府关于实施交通管理措施的通告)'
  - 'Trial period 2008-10-11 to 2009-04-10; subsequently extended by further notices'
  implementation_regime: >
    A fixed-date rolling weekly scheme: within the 5th Ring Road (including the
    ring road), 6:00-21:00 on weekdays (legal holidays and rest days excluded),
    one weekday stop per plate per week; first assignment Monday 1 and 6,
    Tuesday 2 and 7, Wednesday 3 and 8, Thursday 4 and 9, Friday 5 and 0
    (temporary plates included; plates ending in a letter managed as 0); the
    five groups rotate their stop days on a schedule announced in advance by the
    traffic management bureau. Vehicles stopped by the scheme received a
    one-month reduction in road maintenance fee and vehicle tax.
  assignment_mechanism: >
    Assignment is by plate tail number and weekday within the restricted area and
    hours, so which households are treated rotates mechanically; exposure for the
    housing-market application is spatial and household-level: households whose
    driving option is restricted attach higher value to subway access, so the
    policy shock interacts with distance to the nearest subway station. The
    paper compares price changes of housing units near versus far from subway
    stations before and after 2008-10-11.
  parent: null
  related_variations: []
timeline:
  announcement: '2008-09-28'
  effective: '2008-10-11'
  implementation_start: 2008
  implementation_end: 2009
  local_timing: >
    Notice published 2008-09-28; official-vehicle restrictions from 2008-10-01;
    social-vehicle scheme from 2008-10-11 (10-11 and 10-12 fell on the weekend,
    so the first restricted weekday was Monday 2008-10-13); staggered work hours
    from 2008-10-11; trial period through 2009-04-10, thereafter renewed. The
    Olympic odd-even scheme ended in late September 2008 (reported 09-20),
    about three weeks before this scheme began.
  anticipation: >
    The notice was published on 2008-09-28, thirteen days before the scheme took
    effect; the Olympic odd-even scheme had just ended, so the regime and its
    enforcement were familiar. Households could re-time transactions or adjust
    mode choice in anticipation; the paper's handling of anticipation was not
    inspected.
  last_verified: '2026-08-14'
assignment:
  unit: Housing transaction (WoAiWoJia second-hand transactions inside the 5th Ring Road); treated dimension is proximity to the nearest subway station interacted with the policy start
  treated: >
    Housing units near subway stations (paper-reported cutoffs: within 2 km
    for the 1.8 percentage-point premium increase, within 3 km for the 2.7
    percentage-point increase) whose prices capitalize the post-policy rise in
    demand for subway access.
  comparison_pool: >
    Housing units farther from subway stations inside the 5th Ring Road, in the
    pre-policy window (6 months before, extended to 12 months) versus the
    post-policy window; the pseudo-repeat-sale pairing of the same or similar
    units over time is the paper's comparison construction.
  rule: >
    Restriction status applies city-wide within the 5th Ring Road, so the
    assignment margin used by the paper is not restricted versus unrestricted
    locations but near-versus-far subway proximity interacted with the policy
    date; the paper's matching algorithm and the coding of the window extension
    to 12 months were not inspected beyond the screen and abstract-level text.
  intensity: >
    Distance to the nearest subway station (near/far); and a subway-versus-car
    travel-time substitution index computed with GAODE navigation to the CBD,
    along which the premium increase is heterogeneous.
  exemptions:
  - Police, fire, ambulance, and engineering rescue vehicles.
  - Public buses and trolleybuses, inter-provincial long-distance coaches, large buses, taxis (excluding rental vehicles), minibuses, postal vehicles, licensed tourist coaches, approved employer shuttles and school buses.
  - Marked enforcement and tow vehicles; sanitation, landscaping, road-maintenance, and funeral vehicles.
  - Vehicles with diplomatic ("使") plates and approved temporary-entry vehicles.
  compliance: >
    The verified 2008-09-28 notice specifies the scheme, area, hours, tail-number
    groups, exemptions, and a one-month reduction in road maintenance fee and
    vehicle tax for stopped vehicles, but does not itself state penalties.
    Companion official-media coverage at the launch (reported, not re-inspected
    this round) described a one-week grace period with warnings only, followed
    by 100-yuan fines enforced electronically via video monitoring and
    license-plate recognition.
  exposure_construction: >
    WoAiWoJia second-hand housing transactions within the 5th Ring Road, cleaned
    to 24,104 records; prices matched to subway distance and travel times (GAODE
    navigation), with a pseudo-repeat-sale approach pairing price changes of
    units over time around the policy date; the exact geocoding, cleaning, and
    pairing rules were not inspected.
  required_identifiers:
  - Unit location (within 5th Ring Road) and transaction date
  - Distance to nearest subway station
  - Subway-versus-car travel time to the CBD (substitution index)
  - Unit characteristics for price controls
  spillovers: >
    Price effects may spill from near-subway to far-subway units (re-optimization
    of mode choice at the margin); buyers may substitute between units or
    neighborhoods within the window; subway-supply responses and new station
    openings outside the window (e.g., Line 4 opened 2009-09-28) limit the
    interpretation of persistence.
research_compatibility:
  outcome_domains:
  - housing prices and capitalization of transport access
  - willingness to pay for subway proximity
  - transportation mode choice under driving restrictions
  affected_populations:
  - Beijing households inside the 5th Ring Road, especially car owners
  - Buyers and sellers in the Beijing second-hand housing market
  - Households whose commute can be served by subway
  mechanism_channels:
  - mode-shift channel (restriction raises the value of subway access)
  - travel-time substitution channel (premium rises where subway matches car travel time)
  - capitalization channel (short-run inelastic housing supply converts demand shift into prices)
  best_for:
  - Event-style designs around the 2008-10-11 policy start with near-versus-far subway comparisons
  - Capitalization studies of transport access with an exogenous demand shock
  - Studies of driving restrictions' behavioral consequences beyond pollution
  not_good_for:
  - "Treating the restriction as covering all of Beijing at all hours: it applies weekdays 6:00-21:00 inside the 5th Ring Road only"
  - "Merging with the Olympic odd-even scheme (July-September 2008) or later Beijing restriction rounds: separate regimes and dates"
  - "Recovering long-run sorting effects: the paper itself notes it cannot fully control for residential sorting"
  - "Attributing post-2008 price movements to the restriction alone: national housing stimulus and later Beijing purchase-lottery policies (from 2011-01) are concurrent regime changes"
design:
  claim_type: causal
  affordances:
  - Sharp, announced-in-advance policy start (2008-10-11) exogenous to housing market conditions
  - Within-city spatial margin (near versus far subway) holding city-level shocks constant
  - Short window (6 months, extended to 12) limiting omitted variables in repeat-sale price changes
  - Spatial heterogeneity dimension via travel-time substitutability (GAODE navigation)
  candidate_designs:
  - "Pseudo-repeat-sale DID: price changes near versus far subway stations around 2008-10-11"
  - Hedonic regressions with the policy shock interacted with subway distance
  - Heterogeneity analysis along subway-versus-car travel-time substitution
  - Persistence analysis over 12-24 months after the policy
  identifying_variation: >
    The 2008-10-11 policy start is an exogenous shock to private-car use within
    the 5th Ring Road; combined with the spatial gradient of subway access, it
    differentially raises the value of subway-proximate housing. The pseudo-repeat
    sale approach over a short window mitigates omitted-variable problems common
    in subway capitalization studies.
  primary_strategy: >
    Pseudo-repeat-sale approach on WoAiWoJia second-hand transactions inside the
    5th Ring Road (24,104 cleaned records), comparing housing price changes near
    versus far from subway stations in a 6-month window (extended to 12 months)
    around the 2008-10-11 policy, with heterogeneity by subway-versus-car travel
    time substitution (GAODE navigation) and persistence checks.
  estimand: >
    The policy-induced increase in the housing-price premium for subway
    proximity: 1.8 percentage points for units within 2 km and 2.7
    percentage points within 3 km of a subway station, roughly 36% to 60%
    of the initial subway premium (paper-reported), mainly from the change in
    transportation mode; the premium increase persists over time with initial
    overshooting (paper-reported).
  treatment_variable: >
    Proximity to the nearest subway station (near/far, distance to station)
    interacted with the post-2008-10-11 indicator; heterogeneity index = relative
    subway-versus-car travel time to the CBD.
  comparison_logic: >
    Near-subway versus far-subway units inside the 5th Ring Road, before versus
    after 2008-10-11; the pseudo-repeat-sale pairing removes unit-level
    unobservables; short-window supply inelasticity supports price capitalization.
  estimation_notes: >
    The inspected sources establish the policy identity and dates, the data
    source (WoAiWoJia, 24,104 cleaned transactions inside the 5th Ring Road),
    the pseudo-repeat-sale design with 6-month windows extended to 12 months,
    the headline premium increases (1.8/2.7 pp at 2 km/3 km cutoffs), the
    travel-time substitution heterogeneity, and persistence. The exact matching
    and geocoding rules, specification, and robustness tests were not inspected.
  assumptions:
  - The 2008-10-11 restriction start is exogenous to housing price trends.
  - Near and far units would have followed parallel price trends absent the policy.
  - Short-run housing supply is sufficiently inelastic for demand shifts to capitalize.
  - No systematic sorting into near-subway units within the window (paper reports it cannot fully control for sorting).
  - No differential measurement of prices near versus far subway over the window.
  diagnostics:
  - Persistence checks over 12-24 months after the policy
  - Heterogeneity by travel-time substitution index (GAODE)
  - Pseudo-repeat-sale robustness to window length (6 vs 12 months)
  - Placebo dates before the announcement
threats:
- type: concurrent-policies
  basis: documented
  condition: >
    The Olympic odd-even restriction (July-September 2008) falls inside or near
    the paper's pre-window (April-October 2008), so pre-period price dynamics
    near subway may already reflect restriction-related mode shifts; the
    2008-10-01 official-vehicle restrictions and the 2008-10-11 staggered work
    hours are simultaneous traffic-demand measures; and national housing-policy
    stimulus in October 2008 (mortgage rate and down-payment adjustments) is a
    city-wide housing demand shock whose interaction with subway proximity is
    not separated in the inspected material.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Exclude or dummy the Olympic period in the pre-window
  - Control for transaction-month effects and national policy dates
  - Compare with cities without restrictions using the same data source
- type: anticipation-and-behavioral-response
  basis: documented
  condition: >
    The scheme was announced on 2008-09-28, before the effective date, and the
    Olympic odd-even regime had just ended, so buyers and sellers could
    anticipate the mode-shift and re-time transactions; sellers near subway may
    hold or list strategically around the policy date.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Volume and listing-activity checks around the announcement
  - Robustness to excluding the announcement-to-effective window
- type: sorting-and-selection
  basis: reported
  condition: >
    The paper itself notes it cannot fully control for residential sorting; if
    car owners disproportionately move near subway after the restriction, the
    premium change mixes capitalization with composition.
  evidence_refs:
  - E4
  possible_diagnostics:
  - Buyer-type and car-ownership information where available
  - Short-window estimates versus longer-window persistence
- type: measurement-and-data-coverage
  basis: inferred
  condition: >
    WoAiWoJia listings are not the full Beijing market; geocoding and
    station-distance measurement error, and the pseudo-repeat-sale pairing rules
    (24,104 cleaned records), were not inspected; subway station openings just
    outside the window (e.g., Line 4 opened 2009-09-28) complicate the
    persistence interpretation.
  evidence_refs:
  - E4
  possible_diagnostics:
  - Sensitivity of results to distance cutoffs
  - Robustness of station-distance measurement (straight-line vs network)
- type: spillovers-and-general-equilibrium
  basis: inferred
  condition: >
    Near-subway price increases may spill over to far-subway units as buyers
    re-optimize, biasing the near-far comparison downward; conversely, far units
    may gain from bus-mode substitution, biasing it upward; the restriction
    itself raises driving costs city-wide within the 5th Ring Road.
  evidence_refs:
  - E4
  possible_diagnostics:
  - Distance-gradient analysis rather than discrete near/far
  - Ring-based and boundary-distance robustness
empirical_requirements:
  contract_version: 1
  population: Beijing housing units inside the 5th Ring Road and their transactions around 2008-2010
  observation_unit: Housing transaction; unit-day and unit-month price changes
  geography_level: Unit location (inside 5th Ring Road); distance to nearest subway station
  time_start: '2008-04-01'
  time_end: '2010-12-31'
  minimum_frequency: Daily
  minimum_pre_periods: 60
  minimum_post_periods: 60
  required_fields:
  - Transaction price and date (WoAiWoJia or equivalent Beijing second-hand data)
  - Unit location and distance to nearest subway station
  - Subway-versus-car travel time to CBD (navigation-based substitution index)
  - Unit characteristics (size, floor, age, orientation, etc.)
  - Restriction indicator (post 2008-10-11)
  required_identifiers:
  - Unit identifier for repeat-sale pairing
  - Transaction date
  - Station identifier for nearest-subway distance
  treatment_key:
  - distance to nearest subway station interacted with post-2008-10-11 indicator
  - travel-time substitution index
  treatment_source: >
    Beijing Municipal People's Government notice of 2008-09-28 (published on the
    Beijing traffic management bureau website, jtgl.beijing.gov.cn): scheme,
    dates, area, hours, tail-number assignment, exemptions, and fee reduction.
  measurement_risks:
  - Listing versus transaction price differences in WoAiWoJia data
  - Geocoding and station-distance measurement error
  - Repeat-sale pairing selectivity (24,104 cleaned records)
  - Concurrent national housing stimulus (October 2008) and later Beijing policies (2011 purchase lottery)
  - Subway supply changes (station openings) near the window
  - Seasonal and holiday effects in a short window
design_profiles: []
evidence:
- id: E1
  source_type: policy-document
  citation: 'Beijing Municipal People''s Government. 2008-09-28. Notice on implementing traffic management measures (北京市人民政府关于实施交通管理措施的通告).'
  url: https://jtgl.beijing.gov.cn/jgj/jgxx/94246/95332/123949/index.html
  date: '2008-09-28'
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.announcement
  - timeline.effective
  - timeline.local_timing
  - timeline.anticipation
  - assignment.rule
  - assignment.exemptions
  - assignment.compliance
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: official-document
  locator: >
    Official notice text retrieved from the Beijing traffic management bureau
    website (jtgl.beijing.gov.cn), re-inspected 2026-08-14: published
    2008-09-28; official vehicles of party and government organs stop one
    weekday per week from 2008-10-01 (all roads, 0:00-24:00, with 30% of
    official cars sealed); all other vehicles (including out-of-province
    vehicles with long-term city passes) stop one weekday per week within the
    5th Ring Road (including the ring road), 6:00-21:00, legal holidays and
    rest days excluded, trial period 2008-10-11 to 2009-04-10; five tail-number
    groups rotate stop days on a schedule announced in advance by the traffic
    management bureau; first assignment Monday 1 and 6, Tuesday 2 and 7,
    Wednesday 3 and 8, Thursday 4 and 9, Friday 5 and 0 (temporary plates
    included, letters managed as 0); exemptions (police, fire, ambulance,
    engineering rescue, public buses/trolleybuses, inter-provincial coaches,
    taxis excluding rentals, minibuses, postal, licensed tourist coaches,
    approved employer shuttles and school buses, marked enforcement and tow
    vehicles, sanitation/landscaping/road-maintenance/funeral vehicles,
    diplomatic "使" plates, approved temporary-entry vehicles); stopped
    vehicles receive a one-month reduction in road maintenance fee and vehicle
    tax; companion notice on the same page orders staggered work hours from
    2008-10-11. The notice does not state penalties; the grace week and
    100-yuan fine mentioned in this record come from companion official-media
    coverage reported at launch and were not re-inspected this round.
- id: E2
  source_type: paper
  citation: 'Xu, Yangfei, Qinghua Zhang, and Siqi Zheng. 2015. "The rising demand for subway after private driving restriction: Evidence from Beijing''s housing market." Regional Science and Urban Economics 54:28-37.'
  url: https://www.sciencedirect.com/science/article/abs/pii/S0166046215000538
  date: '2015'
  supports:
  - identity.assignment_mechanism
  - assignment.treated
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - design.assumptions
  - design_applications.research_question
  - design_applications.population
  - design_applications.outcome
  - design_applications.empirical_design
  - design_applications.treatment_encoding
  - empirical_requirements.population
  verification_status: reported
  access_level: abstract
  locator: >
    ScienceDirect abstract and introduction excerpts (inspected 2026-08-14):
    the Beijing city government imposed restrictions on private driving in
    October 2008; the pseudo-repeat-sale approach focuses on a short window of
    6 months before and after the policy during which there were no other
    shocks to Beijing's transportation system; the price premium for subway
    proximity increased by 1.8 percentage points for units within 2 km and 2.7
    percentage points within 3 km of a subway station after the restriction;
    locations are differentiated by a subway-versus-private-car travel-time
    substitution index built from GAODE online navigation travel times to the
    CBD; willingness to pay rises more where the subway better substitutes for
    driving; the short window and assumed low housing-supply elasticity support
    capitalization into prices. The working-paper abstract (same authors and
    title, indexed on RePEc) additionally reports the increase as roughly 36%
    to 60% of the initial subway premium, mainly due to the change in
    transportation mode, and persistence of the premium increase over time.
- id: E3
  source_type: other
  citation: 'OpenAlex bibliographic record W811274678 for DOI 10.1016/j.regsciurbeco.2015.06.004 (title, authors Yangfei Xu, Qinghua Zhang, Siqi Zheng, year 2015, RSUE 54:28-37).'
  url: https://api.openalex.org/works/W811274678
  date: '2015'
  supports:
  - design_applications.paper
  - design_applications.journal
  - design_applications.doi
  - design_applications.year
  verification_status: verified
  access_level: metadata
  locator: >
    OpenAlex record W811274678 (re-inspected 2026-08-14) resolves DOI
    10.1016/j.regsciurbeco.2015.06.004 to the article in Regional Science and
    Urban Economics, volume 54, pages 28-37, 2015, authors Yangfei Xu
    (Tsinghua University), Qinghua Zhang (Peking University), and Siqi Zheng
    (Tsinghua University, corresponding), cited by 66 works as of the
    inspection date.
- id: E4
  source_type: paper
  citation: 'Screen-task inspection record (task-ab4db2cd27d6) of the ScienceDirect page for Xu, Zhang, and Zheng 2015, as preserved in candidate-a4cd4961d59c.'
  url: https://doi.org/10.1016/j.regsciurbeco.2015.06.004
  date: '2015'
  supports:
  - assignment.unit
  - assignment.comparison_pool
  - assignment.intensity
  - assignment.exposure_construction
  - empirical_requirements.required_fields
  - empirical_requirements.measurement_risks
  verification_status: reported
  access_level: abstract
  locator: >
    The candidate provenance records that the ScienceDirect page confirms: the
    restriction from 2008-10-11 by plate tail number (one non-holiday weekday
    per private car per week, with rotating restricted weekdays); the WoAiWoJia
    second-hand transaction sample inside the 5th Ring Road cleaned to 24,104
    records; the pseudo-repeat-sale construction over 6 months before and after
    the policy, extended to 12 months; the near-versus-far subway station price
    comparison; the spatial heterogeneity by the degree of subway-versus-car
    travel time substitution; and the explicit caveat that residential sorting
    cannot be fully controlled. Exact matching, geocoding, and specification
    details were not recovered.
design_applications:
- paper: Yangfei Xu, Qinghua Zhang, and Siqi Zheng
  year: 2015
  journal: Regional Science and Urban Economics
  doi: 10.1016/j.regsciurbeco.2015.06.004
  research_question: To what extent did demand for subway access rise after Beijing imposed weekday driving restrictions in October 2008?
  population: Beijing second-hand housing transactions inside the 5th Ring Road around 2008-2010 (WoAiWoJia, 24,104 cleaned records)
  outcome: Housing prices and the capitalized premium for subway proximity
  empirical_design: 'Pseudo-repeat-sale approach comparing price changes near versus far from subway stations in a 6-month window (extended to 12 months) around the 2008-10-11 restriction, with heterogeneity by subway-versus-car travel-time substitution (GAODE navigation) and persistence checks'
  treatment_encoding: Proximity to nearest subway station (near/far and distance) interacted with the post-2008-10-11 indicator; travel-time substitution index for heterogeneity
  comparison: Housing units farther from subway stations inside the 5th Ring Road, and the pre-policy window
  data_used:
  - WoAiWoJia second-hand housing transactions inside the 5th Ring Road (24,104 cleaned records)
  - Distance to nearest subway station and GAODE navigation travel times
  - Beijing Municipal People's Government notice of 2008-09-28
  assumptions:
  - The 2008-10-11 restriction start is exogenous to housing price trends
  - Parallel near-far price trends absent the policy and inelastic short-run supply
  - No systematic sorting within the short window (paper reports it cannot fully control for sorting)
  threats_addressed:
  - Pseudo-repeat-sale pairing removes unit-level omitted variables
  - Short window limits sorting and major housing-market changes
  - Travel-time substitution index provides a spatial heterogeneity margin
  - Persistence analysis checks whether the premium increase is transitory
  evidence_refs:
  - E2
  - E4
method_transfer: null
readiness_blockers:
- The paper's matching and geocoding rules, the pseudo-repeat-sale pairing algorithm, and the 24,104-record cleaning steps were not inspected.
- The paper's treatment of the Olympic odd-even period inside or near the pre-window and of the October 2008 national housing stimulus was not inspected.
- Parallel-trends, placebo, and robustness evidence were not inspected.
- The official 2008 notice provides for advance-announced rotation of tail-number groups; the rotation cadence used in the paper's coding (companion official-media coverage reportedly describes monthly rotation, while the candidate brief described three-monthly rotation) was not resolved.
- The launch-time grace week and 100-yuan fine come from companion official-media coverage reported at launch and were not re-inspected against a primary source this round.
- Whether the paper's 6-month pre-window (April-October 2008) overlaps the Olympic restriction was not resolved.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Beijing restricted private-car driving by license-plate tail number from 2008-10-11: each non-official vehicle stopped one weekday per week within the 5th Ring Road (including the ring road), 6:00-21:00, under the Beijing Municipal People's Government notice of 2008-09-28 [E1]. The scheme followed the Olympic-period odd-even restriction (July-September 2008), and the same notice restricted official vehicles from 2008-10-01 while a companion notice introduced staggered work hours from 2008-10-11 [E1]. The paper studies the demand-side consequence: the mode shift raises the value of subway access, and the housing premium for subway proximity rose after the policy [E2, E4].

## What Changed

From 2008-10-11, driving within the 5th Ring Road on the assigned weekday was banned for each plate group (first assignment Monday 1 and 6, Tuesday 2 and 7, Wednesday 3 and 8, Thursday 4 and 9, Friday 5 and 0; letters managed as 0; groups rotate on an advance-announced schedule), 6:00-21:00 on weekdays with legal holidays and rest days excluded, with listed exemptions [E1]. Stopped vehicles received a one-month reduction in road maintenance fee and vehicle tax [E1]; launch-time official-media coverage additionally reported a one-week grace period with warnings only and 100-yuan fines thereafter [E1, reported claim]. The paper measures the resulting increase in the housing-price premium for subway proximity: 1.8 percentage points within 2 km and 2.7 within 3 km of a station, roughly 36%-60% of the initial premium [E2, reported claim].

## Implementation and Assignment

Assignment to the weekly stop is mechanical by plate tail number and weekday, so the treatment margin used by the paper is not restricted versus unrestricted locations but proximity to subway interacted with the policy date: near-subway housing gains from the demand shift, far-subway housing serves as the comparison [E2, E4]. The paper uses WoAiWoJia second-hand transactions inside the 5th Ring Road (24,104 cleaned records), pseudo-repeat-sale pairing over 6 months before and after the policy (extended to 12), and a GAODE navigation travel-time substitution index for spatial heterogeneity [E2, E4]. The exact matching and geocoding rules were not inspected [E4].

## Why This Creates Empirical Variation

The restriction's start date was announced on 2008-09-28 and fixed by the government, exogenous to housing market conditions, and it differentially raised the value of subway access within the city [E1, E2]. Because the scheme applies city-wide inside the 5th Ring Road, the identifying variation is the interaction of the policy shock with the spatial gradient of subway access: near-versus-far price changes before versus after the policy, within a short window that limits omitted variables and sorting [E2, E4]. The travel-time substitution index provides an additional heterogeneity margin predicted by the mode-shift mechanism [E2].

## Identification Risks

The leading risks are concurrent policies and composition: the Olympic odd-even scheme sits inside or near the paper's pre-window, the October 2008 national housing stimulus coincides with the post-window, and the official-vehicle restrictions and staggered work hours are simultaneous [E1, analytical inference]. Anticipation is possible given the 2008-09-28 announcement and the just-ended Olympic regime [E1, analytical inference]. The paper itself notes it cannot fully control for residential sorting [E4]. Measurement risk comes from listing data, geocoding, and pairing rules not inspected, and subway supply changes near the window complicate persistence [E4, analytical inference].

## Data Requirements

The design needs Beijing second-hand transaction data inside the 5th Ring Road (WoAiWoJia or equivalent), transaction prices and dates, unit location with distance to the nearest subway station, navigation-based subway-versus-car travel times (substitution index), unit characteristics for controls, and the restriction calendar [E2, E4]. The 2008-09-28 notice provides the policy dates and rules [E1]. Data acquisition belongs in `Econ Data Know-How`; this record preserves the policy identity, the assignment margin, and the evidence boundary.

## Evidence Notes

E1 is the official Beijing notice of 2008-09-28, verified on the Beijing traffic management bureau website (re-inspected 2026-08-14), establishing the scheme, area, hours, tail-number assignment, exemptions, fee reduction, and the companion staggered-work-hours measure; the launch-time grace week and 100-yuan fine remain a companion official-media reported claim, not re-inspected this round. E2 is the paper's ScienceDirect abstract and introduction excerpts (inspected 2026-08-14), establishing the pseudo-repeat-sale design, the 1.8/2.7 percentage-point premium increases at the 2 km/3 km cutoffs, the GAODE travel-time heterogeneity index, and persistence; E2's claims are paper-reported, not independently verified. E3 is the OpenAlex bibliographic record (RSUE 54:28-37, 2015), verified at metadata level. E4 is the screen task's ScienceDirect inspection, establishing the data source, sample (24,104 transactions), windows (6 extended to 12 months), and the sorting caveat. The exact matching and pairing algorithm, Olympic-period and housing-stimulus controls, rotation cadence, and robustness tests were not recovered and are recorded as readiness blockers rather than assumed.
