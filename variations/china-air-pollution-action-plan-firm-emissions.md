---
schema_version: 2
id: china-air-pollution-action-plan-firm-emissions
name: 2013 China Air Pollution Action Plan and Firm Emission Intensity
aliases:
- Action Plan for Air Pollution Prevention and Control firm design
- APPCAP manufacturing-firm emissions China
- 大气污染防治行动计划企业排放
status: grounded
provenance:
  task_id: task-e6f648e1ff1b
scope:
  country: China
  regions:
  - Beijing-Tianjin-Hebei target area
  - Yangtze River Delta target area
  - Pearl River Delta target area
  - Seven target provincial-level units used in the paper application
  domains:
  - regional-economics
  - urban-economics
  - environmental-economics
  - firm-dynamics
  - industrial-organization
  - energy
  variation_type: event-shock
  knowledge_role: china-variation
  china_relevance: >
    This record captures the firm-level application of China's 2013 Air Pollution
    Prevention and Control Action Plan. The policy was a multi-instrument national
    program, but the paper's usable treatment is a target-province by post-2013
    exposure interacted with each manufacturer's pre-treatment waste-gas intensity.
    It is distinct from low-carbon pilot designation, real-time pollution disclosure,
    and later central environmental inspections.
identity:
  instrument: >
    State Council Air Pollution Prevention and Control Action Plan (the 2013 national
    clean-air action plan, often called the Ten Measures for Air Pollution Control),
    as applied to manufacturing firms in its three priority regions.
  authority: >
    The State Council issued the plan. The Ministry of Environmental Protection and
    other central departments translated it into regional and provincial targets,
    while provincial and local governments prepared annual implementation plans and
    assigned tasks to cities, counties, departments, and enterprises.
  legal_identifiers:
  - State Council, 国发〔2013〕37号, Action Plan for Air Pollution Prevention and Control, issued 2013-09-10
  - MEP and ministries, 环发〔2013〕104号, Beijing-Tianjin-Hebei implementation rules, issued 2013-09-17
  - State Council General Office, 国办发〔2014〕21号, implementation assessment measures, issued 2014-04-30
  - Provincial and local implementation plans and air-quality target responsibility contracts
  implementation_regime: >
    The plan combined national targets with region-specific air-quality goals,
    industrial emission standards, coal and boiler controls, capacity retirement,
    fuel and vehicle measures, and a responsibility-and-assessment chain. The three
    priority regions received stronger PM2.5 targets and a denser package of tasks.
    In the paper application, the target indicator covers seven provincial-level units:
    Beijing, Tianjin, Hebei, Shanghai, Jiangsu, Zhejiang, and Guangdong.
  assignment_mechanism: >
    A manufacturer is exposed when it is located in one of the seven target provincial
    units after the plan's first full implementation year, with exposure intensity
    measured by its 2013 waste-gas emissions per unit of value added. The paper's
    treatment is therefore target province x post-2013 x baseline emission intensity,
    not a binary claim that every firm faced the same enforcement.
  parent: null
  related_variations:
  - china-low-carbon-pilot-first-wave
  - china-pollution-information-disclosure
  - china-central-environmental-protection-inspection
timeline:
  announcement: '2013-09-10'
  effective: '2013-09-10'
  implementation_start: 2014
  implementation_end: 2017
  local_timing: >
    The formal plan was issued in September 2013 and the national assessment rules
    were issued in April 2014. The paper codes post as 2014 onward, which is an annual
    empirical clock rather than proof that every firm received a new requirement on
    1 January 2014.
  anticipation: >
    Severe pollution, the January 2013 episode, the public September plan, and local
    preparatory work could affect firms before the paper's post indicator. A 2013
    baseline emission-intensity measure may also include partial announcement-period
    responses and must not be treated as automatically pre-policy.
  last_verified: '2026-08-13'
assignment:
  unit: Manufacturing firm-year, linked to province and industry
  treated: >
    Manufacturers in Beijing, Tianjin, Hebei, Shanghai, Jiangsu, Zhejiang, or
    Guangdong in 2014 and later, with a larger value of the pre-period waste-gas
    emission-intensity measure receiving a stronger paper-defined exposure.
  comparison_pool: >
    Low-intensity manufacturers in the target provinces and manufacturers in the same
    broad industries outside the seven target provincial units, using firm and
    province-industry-year controls as specified by the application.
  rule: >
    Code the interaction of target-province membership, post-2013 annual exposure, and
    log 2013 waste-gas emissions per unit of value added. Keep the seven-unit target
    list separate from the plan's broader national responsibility system and from later
    inspections or pilots.
  intensity: >
    Continuous baseline emission intensity, measured as 2013 waste-gas emissions per
    unit of value added and used in logs; the application interprets a one-percent
    increase in baseline intensity as a stronger regulatory exposure.
  exemptions:
  - Non-manufacturing observations are outside the paper's main population.
  - Firms with fewer than eight employees, invalid or negative accounting fields, or missing or implausible waste-gas observations are excluded by the reported sample construction.
  - Firms outside the National Tax Statistics Database coverage are not observed.
  compliance: >
    The plan assigns responsibility and provides enforcement tools, but the official
    documents do not establish identical firm-level compliance. The paper observes
    emissions and operations and reports stronger responses for high-intensity firms;
    it does not turn the statutory target list into a direct inspection roster.
  exposure_construction: >
    Merge a manufacturing firm-year panel to a province target indicator and a post-2013
    indicator. Interact both with log 2013 waste-gas emissions per value added. Keep
    firm fixed effects and province-industry-year controls, and preserve the paper's
    alternative regional, ownership, political, and mechanism specifications.
  required_identifiers:
  - Stable firm identifier and year
  - Province or provincial-level municipality code
  - Industry code and province-industry-year cell
  - 2013 baseline waste-gas emissions and value added
  - Firm ownership and city identifier where heterogeneity is studied
  spillovers: >
    Pollution travels across provincial borders; firms can relocate, change suppliers,
    or alter reported emissions. The plan also changed monitoring, coal use, vehicle
    standards, and local industrial policy at the same time. A target-province design
    must therefore report spatial spillovers and overlapping policy exposure.
research_compatibility:
  outcome_domains:
  - waste-gas emissions
  - sulfur dioxide and nitrogen oxides
  - coal consumption
  - output and employment
  - input composition
  - production technology
  - environmental investment
  - firm survival and relocation
  affected_populations:
  - Chinese manufacturing firms
  - high-emission-intensity firms
  - industrial workers and local residents
  - firms in the three priority air-quality regions
  mechanism_channels:
  - pollution-abatement and compliance channel
  - coal substitution and input replacement
  - production-scale channel
  - product-composition channel
  - technology and technique channel
  - cross-border relocation and pollution displacement
  best_for:
  - Studying how targeted air-quality regulation changes emissions conditional on firm baseline intensity
  - Separating scale, composition, and technique responses in manufacturing
  - Testing regional, ownership, political, and industry heterogeneity in environmental regulation
  not_good_for:
  - Treating the Action Plan as a single uniform firm inspection or a randomized shock
  - Measuring effects on informal firms absent from the tax survey
  - Estimating a clean national welfare effect without accounting for other 2013-2015 policies and spillovers
  - Substituting this plan for the separate low-carbon-pilot, disclosure, or inspection records
design:
  claim_type: causal
  affordances:
  - Target-province and post-period policy timing
  - Continuous firm-level baseline emission-intensity exposure
  - Manufacturing panel with emissions, output, energy, and input fields
  - Mechanism tests for scale, composition, coal, and material substitution
  candidate_designs:
  - Triple-difference or continuous-intensity difference-in-differences with firm and province-industry-year fixed effects
  - Event study by target-province and baseline intensity groups
  - Mechanism designs for scale, product composition, coal use, and input substitution
  - Regional and ownership heterogeneity designs
  identifying_variation: >
    The application compares changes after 2013 between high- and low-intensity firms,
    separately by whether their province is one of the seven target units. Its identifying
    restriction is that, conditional on firm effects, province-industry-year effects,
    and observed firm controls, high- versus low-intensity firms in target and non-target
    provinces would otherwise have followed comparable paths.
  primary_strategy: >
    A firm-panel intensity design based on target province x post-2013 x log 2013
    waste-gas intensity, with firm fixed effects and time-varying province-industry-year
    controls. Event-study and placebo specifications check pre-policy trends; region
    and ownership splits describe implementation heterogeneity.
  estimand: >
    The local change in manufacturing-firm waste-gas emissions associated with the
    Action Plan among higher-intensity firms in the seven target provincial units after
    2013, relative to the stated lower-intensity and non-target comparisons. Mechanism
    estimates concern output, coal, materials, and technique responses rather than a
    single aggregate welfare effect.
  treatment_variable: >
    TargetProvince_p multiplied by Post2013_t and log 2013 waste-gas emissions per
    value added, with alternative models using target-region indicators and policy-period
    interactions.
  comparison_logic: >
    Use high- versus low-intensity firms within target provinces and compare the same
    intensity contrast in non-target provinces, while absorbing firm and
    province-industry-year differences. The target list, baseline intensity, and post
    clock must be kept visible in every application.
  estimation_notes: >
    The reported summary describes a large National Tax Statistics Database panel for
    2007-2015 and a negative response for high-intensity regulated firms, with no
    detectable output decline and evidence consistent with reduced coal use and input
    substitution. Exact sample filters, weighting, standard-error clustering, and
    replication code remain to be recovered from the paper or data materials.
  assumptions:
  - 2013 baseline intensity is not materially altered by announcement-period behavior or measurement changes.
  - Conditional pre-trends are comparable across intensity groups and target status.
  - Province-industry-year fixed effects absorb broad local and sector shocks without absorbing the treatment of interest.
  - Emission reports and value added are measured consistently across firms and years.
  - Cross-border displacement and overlapping programs do not fully account for the observed response.
  - The seven-province target list is coded from the plan and its responsibility documents, not inferred from pollution levels alone.
  diagnostics:
  - Event-study leads and pre-2013 intensity-trend tests
  - Alternative baseline intensity years, if legally and statistically defensible
  - Exclusion of firms in carbon-trading pilots, Top-10k energy programs, or other overlapping interventions
  - Separate waste-gas, sulfur-dioxide, nitrogen-oxide, coal, output, and employment outcomes
  - Region, ownership, city-leader, and industry heterogeneity
  - Spatial spillover, relocation, and treatment of target-province boundary firms
  - Placebo target lists and fake post years
threats:
- type: endogenous-target-selection
  basis: documented
  condition: >
    The target regions were chosen because of severe pollution and policy priorities,
    not by a lottery. They may have different industrial trends, administrative capacity,
    or concurrent programs even after fixed effects.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Pre-trend event studies by baseline intensity
  - Province-industry-year effects and firm controls
  - Reweighting or matched target and non-target provinces
  - Report target-region selection as part of the estimand
- type: announcement-anticipation-and-baseline-contamination
  basis: inferred
  condition: >
    The September 2013 announcement and earlier pollution episodes could change firm
    behavior before 2014, while the 2013 intensity measure may be partly post-announcement.
  evidence_refs:
  - E1
  - E3
  possible_diagnostics:
  - Alternative 2012 or earlier intensity baselines
  - Leads in the event study
  - Separate announcement and first-full-year clocks
  - Audit accounting and emission reporting changes in 2013
- type: concurrent-environmental-policies
  basis: reported
  condition: >
    The Twelfth Five-Year Plan, regional carbon-trading pilots, Top-10k energy-saving
    program, new standards, and later inspections overlapped the 2013-2015 window.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Exclude or separately code overlapping policy units
  - Interact controls with target status and baseline intensity
  - Use policy-specific placebo years and alternative samples
- type: spatial-relocation-and-pollution-displacement
  basis: inferred
  condition: >
    Firms or emissions may move across provincial borders, and pollution can travel from
    regulated regions to nearby areas. A firm-panel decline need not equal a regional
    reduction in total emissions.
  evidence_refs:
  - E1
  - E3
  possible_diagnostics:
  - Neighboring-province outcomes and border buffers
  - Firm entry, exit, and relocation tracking
  - Regional mass-balance or satellite pollution checks
- type: emissions-data-coverage-and-reporting
  basis: reported
  condition: >
    The National Tax Statistics Database is a large survey rather than a census, and
    reported waste gas, coal, value added, and facility costs can contain missing values,
    coding changes, or strategic reporting.
  evidence_refs:
  - E4
  possible_diagnostics:
  - Reproduce the paper's sample filters and missingness rules
  - Compare alternative pollutants and intensity definitions
  - Cross-check against official industrial and emissions aggregates
  - Test sensitivity to firm entry and exit
empirical_requirements:
  contract_version: 1
  population: Chinese manufacturing firms in the National Tax Statistics Database, approximately 2007-2015
  observation_unit: Firm-year
  geography_level: Province or provincial-level municipality, with city identifier where needed
  time_start: 2007
  time_end: 2015
  minimum_frequency: annual
  minimum_pre_periods: 4
  minimum_post_periods: 2
  required_fields:
  - Firm identifier and year
  - Province and city codes
  - Industry code and province-industry-year cell
  - Waste-gas emissions and 2013 baseline value
  - Value added or output for intensity construction
  - Coal, electricity, material, and intermediate inputs
  - Employment, ownership, exports, and product information
  - Environmental facility costs or investment where mechanism outcomes are used
  required_identifiers:
  - stable_firm_id
  - province_code
  - city_code
  - industry_code
  - calendar_year
  - baseline_intensity_year
  treatment_key:
  - target_province_indicator
  - post_2013_indicator
  - log_2013_waste_gas_intensity
  treatment_source: >
    State Council Action Plan and provincial target responsibility or implementation
    documents, joined to the National Tax Statistics Database and its firm-level
    emissions and operations fields.
  measurement_risks:
  - 2013 baseline may overlap announcement and preparation
  - Tax-survey sampling and firm identifiers may change across years
  - Waste-gas definitions and reporting quality can vary by province and industry
  - Province-industry-year fixed effects do not remove firm relocation or local spillovers
  - Exact target list and local implementation dates must be archived separately
evidence:
- id: E1
  source_type: policy-document
  citation: State Council of the People's Republic of China. 2013-09-10. Action Plan for Air Pollution Prevention and Control, 国发〔2013〕37号.
  url: https://www.mee.gov.cn/zcwj/gwywj/201811/t20181129_676555.shtml
  date: '2013-09-10'
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.announcement
  - timeline.effective
  - timeline.implementation_start
  verification_status: verified
  access_level: official-document
  locator: >
    Official plan: issue date and document number; national five-year objective;
    quantitative PM2.5 targets for the three priority regions; industrial emission,
    coal, capacity, fuel, and monitoring measures; and provisions making local
    governments responsible and enterprises the pollution-control actors. It does not
    establish firm-level compliance or the paper's sample filters.
- id: E2
  source_type: implementation-document
  citation: State Council General Office. 2014-04-30. Measures for Assessing Implementation of the Air Pollution Prevention and Control Action Plan, 国办发〔2014〕21号; and MEP notice on provincial target responsibility contracts, 2014-01-07.
  url: https://www.mee.gov.cn/zcwj/gwywj/201811/t20181129_676566.shtml
  date: '2014-04-30'
  supports:
  - identity.implementation_regime
  - timeline.local_timing
  - timeline.implementation_start
  - assignment.compliance
  verification_status: verified
  access_level: official-document
  locator: >
    The official assessment rules cover all provincial governments, distinguish
    Beijing--Tianjin--Hebei and surrounding areas, the Yangtze River Delta, the nine
    Pearl River Delta cities, and Chongqing for PM2.5 assessment, and require
    implementation through subnational responsibility. They establish the
    administrative chain, not the paper's seven-unit estimation indicator or identical
    firm enforcement.
- id: E3
  source_type: paper
  citation: 'Mao, Jie, Chunhua Wang, and Haitao Yin. 2023. "Corporate responses to air quality regulation: Evidence from a regional environmental policy in China." Regional Science and Urban Economics 98:103851. DOI: 10.1016/j.regsciurbeco.2022.103851.'
  url: https://www.sciencedirect.com/science/article/pii/S0166046222000898
  date: 2023
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.announcement
  - timeline.implementation_start
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.exemptions
  - assignment.exposure_construction
  - assignment.required_identifiers
  - assignment.spillovers
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  verification_status: verified
  access_level: abstract
  locator: >
    Publisher and IDEAS/RePEc abstract and indexed article sections identify the 2013
    Action Plan, its three-region objective, high-emission-intensity regulated firms,
    waste-gas outcome, no reported output decline, and coal or input-substitution
    mechanism. Full text and replication materials were not available through the
    inspected publisher route, so exact sample and coding details remain attributed.
- id: E4
  source_type: scholarship
  citation: 'Camphor Economics Academic Circle summary of Mao, Wang, and Yin (2023), "Corporate responses to air quality regulation," 2023-06-29.'
  url: https://cec.blog.caixin.com/archives/266741
  date: '2023-06-29'
  supports:
  - design.primary_strategy
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  verification_status: reported
  access_level: full-text
  locator: >
    The inspected Chinese summary reports the National Tax Statistics Database panel
    for approximately 2007-2015, about 700,000 firms per year, the paper's seven-unit
    provincial-level coding, the target x post x log-2013-intensity specification,
    sample filters, province-industry-year and firm controls, event study, and
    exclusions for overlapping programs. It is a secondary account of the paper, not
    the raw data or an official target-list archive. In particular, the seven-unit
    coding is an application choice and must not be relabelled as the national plan's
    full statutory coverage.
- id: E5
  source_type: paper
  citation: DOI metadata for Mao, Wang, and Yin, Regional Science and Urban Economics 98 (2023), article 103851.
  url: https://doi.org/10.1016/j.regsciurbeco.2022.103851
  date: 2023
  supports:
  - identity.instrument
  - design.primary_strategy
  - design.estimand
  verification_status: verified
  access_level: metadata
  locator: DOI metadata establishes article identity, journal, year, volume, article number, and DOI; substantive application claims come from E1-E4.
design_applications:
- paper: 'Corporate responses to air quality regulation: Evidence from a regional environmental policy in China'
  doi: 10.1016/j.regsciurbeco.2022.103851
  journal: Regional Science and Urban Economics
  year: 2023
  research_question: How did the 2013 Action Plan change emissions and production choices of Chinese manufacturing firms with different baseline emission intensity?
  population: Manufacturing firms in the National Tax Statistics Database, approximately 2007-2015, with the seven target provincial units and non-target comparison provinces.
  outcome: Waste-gas emissions, sulfur dioxide and nitrogen oxides where available, output, employment, coal use, materials, product composition, and environmental facility outcomes.
  data_used:
  - National Tax Statistics Database firm-level accounting, production, energy, and pollution fields
  - State Council Action Plan and provincial target responsibility documents
  - Industry input price indexes and province or city policy controls reported by the application
  - Carbon-trading, Top-10k, and other overlapping-policy indicators for robustness exclusions
  treatment_encoding: TargetProvince multiplied by Post2013 and log 2013 waste-gas emissions per unit of value added; target provinces are Beijing, Tianjin, Hebei, Shanghai, Jiangsu, Zhejiang, and Guangdong.
  comparison: High- versus low-intensity firms in target provinces, with the same intensity contrast in non-target provinces and province-industry-year and firm controls.
  empirical_design: Firm-panel triple-difference or continuous-intensity DID with firm and province-industry-year fixed effects, event-study leads, mechanism tests, and region or ownership heterogeneity.
  assumptions:
  - Conditional intensity trends are comparable before the plan.
  - The baseline intensity measure is not materially contaminated by announcement-period responses.
  - Target-province assignment and local implementation are correctly joined.
  - Overlapping policies, relocation, and reporting changes do not explain the full estimate.
  threats_addressed:
  - Province-industry-year and firm fixed effects
  - Event-study pre-trends and placebo years
  - Alternative pollution outcomes and baseline-intensity definitions
  - Exclusion or coding of carbon-trading and Top-10k firms
  - Regional, ownership, and political heterogeneity
  evidence_refs:
  - E3
  - E4
  - E5
method_transfer: null
readiness_blockers:
- The publisher full text and replication package were not accessible in the inspected route. Exact sample construction, weighting, clustering, and raw-variable definitions remain reported through the paper abstract and an independent summary.
- The paper's seven-unit target indicator is recoverable from the inspected secondary
  summary, whereas the official plan and assessment documents define a broader and
  differently shaped geographic regime. A machine-readable archive of the paper's
  coding decision, every provincial implementation plan, and local effective date is
  not stored here.
- The paper uses 2013 emission intensity as the baseline even though the plan was announced in September 2013; recover earlier baselines and accounting-change checks before treating it as fully pre-policy.
- The National Tax Statistics Database is not archived here, and its firm identifiers, sampling frame, emissions definitions, and access conditions belong in Econ Data Know-How.
- Target selection, concurrent environmental policies, firm relocation, and cross-border pollution mean the design is a conditional local comparison, not an intrinsically exogenous national experiment.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

After severe air-pollution episodes, the State Council issued the 2013 Air Pollution
Prevention and Control Action Plan. It set national and regional targets, but its most
specific targets and industrial measures concentrated on the Beijing-Tianjin-Hebei,
Yangtze River Delta, and Pearl River Delta areas. The plan combined emission standards,
coal and boiler changes, capacity retirement, vehicle and fuel rules, monitoring, and
administrative accountability rather than one isolated technology mandate [E1].

The follow-up responsibility and assessment documents made provincial governments the
implementation owners and required them to decompose tasks to cities, counties,
departments, and enterprises. That chain explains why a firm-level application can use
target-province membership, but it also explains why a province indicator is not the
same thing as a firm inspection record [E2].

## What Changed

The plan was issued on 10 September 2013. The paper's annual post clock begins in 2014,
after provincial responsibility contracts and implementation planning were in place.
This distinction matters: the formal announcement, preparation, first full year, and
later assessment are separate dates, not interchangeable treatment variables [E1; E2].

In the paper application, the target indicator covers seven provincial-level units:
Beijing, Tianjin, Hebei, Shanghai, Jiangsu, Zhejiang, and Guangdong. A firm's exposure
also depends on its 2013 waste-gas emissions per unit of value added. The reported
application finds a reduction in waste-gas emissions among higher-intensity regulated
firms without a corresponding output decline, with results consistent with coal and
input substitution [E3; E4].

## Implementation and Assignment

The useful treatment is a three-way interaction. First, the firm must be in one of the
seven target provincial units. Second, the observation must be in the paper's post-2013
period. Third, the firm carries a continuous intensity value based on its 2013 waste-gas
emissions relative to value added. The lower-intensity firms in target provinces and
the analogous intensity contrast in non-target provinces supply the comparisons [E3;
E4].

The plan's legal responsibility applies broadly to local governments and enterprises,
but the application observes manufacturing-firm emissions and operations in the
National Tax Statistics Database. The record therefore treats statutory target status,
baseline intensity, and observed compliance as separate layers. It does not infer that
every high-intensity firm was inspected or that every reported emission change was a
direct abatement response [E1; E3].

## Why This Creates Empirical Variation

The design combines a regional policy boundary with pre-existing differences in how
emission-intensive firms are. Firm fixed effects remove stable firm differences, while
province-industry-year controls absorb many broad local-sector shocks. The intensity
gradient then asks whether the same policy timing had a larger effect where the baseline
pollution burden was higher. This is useful for a mechanism question about firm
adaptation, not a universal estimate of the plan's total effect on Chinese air quality
[E3; E4; analytical inference].

The case must remain separate from the repository's low-carbon pilot, real-time
monitoring disclosure, and central inspection records. Those records change planning
designation, information availability, and inspection exposure respectively. The Action
Plan application instead uses a target-region responsibility regime and a firm-level
emission-intensity gradient. The programs overlap in time, so a combined study needs
explicit crosswalks rather than treating them as interchangeable treatments.

## Identification Risks

Target provinces were chosen because they were polluted and politically prioritized,
so the comparison is not random. The plan was announced in 2013, making the 2013
intensity baseline potentially contaminated by preparation or accounting changes. Other
environmental programs, including carbon-trading pilots and energy-saving campaigns,
overlap the same window. Pollution can move across provincial borders, and firms may
relocate or change reported inputs. These risks limit what the firm estimate can say
about aggregate regional emissions or welfare [E1; E3; E4].

The paper's event study and robustness exercises are useful diagnostics, but they do not
turn a selected target list into a random assignment. A new user should recover the
exact data filters and local implementation documents before extending the result to a
different firm sample or post-period.

## Data Requirements

The minimum panel needs stable firm IDs, annual observations, province and industry
codes, waste-gas emissions, value added or output, employment, coal and material inputs,
ownership, and the 2013 baseline intensity. A serious replication also needs the target
province archive, local responsibility plans, overlapping-policy indicators, and a way
to check firm entry, exit, and relocation. The National Tax Statistics Database and
related firm-data acquisition belong in `Econ Data Know-How`; this record preserves the
join and interpretation contract.

## Evidence Notes

E1 is the official State Council plan. It establishes the instrument, issue date,
priority regions, industrial measures, and government-enterprise responsibility, but
not firm-level compliance. E2 is the official implementation and assessment evidence;
it establishes regional targets, task decomposition, and accountability while leaving
local timing heterogeneous. E3 is the publisher and IDEAS/RePEc paper abstract and
indexed text; it establishes the paper's research question and headline findings but
the inspected publisher route did not expose the full article. E4 is a detailed Chinese
scholarly summary that reports the seven-province indicator, National Tax Statistics
Database panel, specification, and robustness work; those details remain attributed
until the original paper or replication materials are recovered. E5 is metadata only.

The soft recency marker is 2023: it can help a future agent order newer applications,
but it cannot replace the target list, baseline construction, or evidence boundary.
