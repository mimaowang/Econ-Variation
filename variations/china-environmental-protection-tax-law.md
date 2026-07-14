---
schema_version: 2
id: china-environmental-protection-tax-law
name: China's Environmental Protection Tax Law (2018)
aliases:
- Environmental Protection Tax Law
- EPT Law
- 环境保护税法
- 环保税法
- China environmental protection tax reform
- Pigovian tax (China)

status: grounded
provenance:
  task_id: task-38a16e1723e2
scope:
  country: China
  regions:
  - All provincial-level administrative units
  domains:
  - environment
  - taxation
  - regulation
  - pollution
  - firm-behavior
  - public-finance
  - green-innovation
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: >
    The variation is a nationwide Chinese tax reform that directly changes the
    price of polluting emissions faced by enterprises and local governments.
    The 2018 effective date provides a common pre/post breakpoint, while
    province-level tax-rate choices create cross-sectional intensity variation,
    making it a China-specific empirical shock for environmental and industrial
    economics.
identity:
  instrument: National environmental protection tax levied on emissions of air
    pollutants, water pollutants, solid waste, and noise
  authority: Standing Committee of the National People's Congress (law); State
    Council (implementation regulations); provincial People's Congresses (rate
    setting within statutory ranges); tax and ecology authorities (collection
    and monitoring)
  legal_identifiers:
  - 中华人民共和国主席令 第六十一号 (2016-12-25)
  - 中华人民共和国环境保护税法 (passed 2016-12-25, effective 2018-01-01)
  - 中华人民共和国国务院令 第693号 (2017-12-25, effective 2018-01-01)
  implementation_regime: >
    The law replaced the earlier pollution-discharge fee system with a tax
    administered by tax departments, using emissions data shared by ecology
    authorities. Provincial governments set air- and water-pollutant tax rates
    within national minimum/maximum ranges. Firms receive a 75% tax reduction
    when emissions are at least 30% below standards and a 50% reduction when at
    least 50% below standards.
  assignment_mechanism: >
    All enterprises, public institutions, and other producers directly
    discharging taxable pollutants are taxpayers. Quasi-experimental variation
    comes from the national effective date interacted with cross-sectional
    exposure: heavy-polluting industries, high-emission firms, and provinces
    that chose higher tax rates face larger shocks. There is no individual-level
    randomization.
  parent: null
  related_variations:
  - china-central-environmental-protection-inspection
  - china-low-carbon-pilot-first-wave
  - china-pollution-information-disclosure
  - china-water-regulation-enforcement
  - china-water-quality-monitoring-rd
  - china-huai-river-heating-air-pollution
  - china-heating-policy-air-pollution-wtp
timeline:
  announcement: '2016-12-25'
  effective: '2018-01-01'
  implementation_start: 2018
  implementation_end: ongoing
  local_timing: >
    The Environmental Protection Tax Law was passed and promulgated by
    Presidential Order No. 61 on 25 December 2016 and took effect nationwide on
    1 January 2018. The State Council Implementation Regulations (Order No. 693)
    were issued on 25 December 2017 and also took effect on 1 January 2018.
    All provinces set their air- and water-pollutant tax rates before the
    effective date.
  anticipation: >
    The law and its effective date were publicly announced in December 2016,
    giving firms roughly one year to anticipate. Provincial rate consultations
    occurred during 2017. Because a discharge-fee system already existed, the
    reform was partly anticipated, especially by heavily polluting firms.
  last_verified: '2026-07-14'
assignment:
  unit: firm-year or province-year
  treated: >
    Enterprises and other producers directly discharging taxable pollutants.
    In reduced-form designs, heavily polluting listed firms or high-emission
    firms are treated from 2018 onward. Intensity is higher in provinces that
    set higher tax rates and for firms with higher baseline emissions.
  comparison_pool: >
    Firms or industries with low or no taxable emissions; the same firms before
    2018; provinces that chose lower tax rates; non-polluting firms within the
    same region.
  rule: >
    Code a unit as treated from 2018 onward if it directly emits taxable
    pollutants. In reduced-form work the treatment is a post-2018 indicator
    interacted with heavy-polluting-industry status. In intensity designs the
    treatment equals the applicable provincial tax rate multiplied by the
    firm's emission quantity.
  intensity: >
    Continuous (tax burden per unit emission) or binary
    (heavy-polluting industry × post-2018). Cross-sectional intensity comes
    from province-level rate choices; within-province intensity varies by
    pollutant type and by how far emissions are below the statutory standards.
  exemptions:
  - Agricultural production (excluding large-scale livestock breeding)
  - Mobile pollution sources (motor vehicles, ships, aircraft, etc.)
  - Emissions delivered to licensed centralized sewage or waste-treatment facilities
  - Tax reductions of 75% or 50% for emissions 30% or 50% below standards
  compliance: >
    Taxpayers declare emissions to tax authorities. Emissions are measured by
    automatic monitoring devices, monitoring-agency reports, or official
    coefficients. Ecology authorities share monitoring information with tax
    bureaus through a shared platform. Collection is more rigid than the
    previous fee system because it is backed by tax law.
  exposure_construction: >
    Build a firm-year panel with calendar year, province, and industry code.
    Add a post-2018 indicator and a heavy-polluting-industry indicator. For
    intensity designs, merge province-level air/water tax rates and firm-level
    emissions. Exclude exempt sectors and firms without direct emissions.
  required_identifiers:
  - firm or province identifier
  - calendar year
  - industry code
  - province code
  - taxable emissions (for intensity designs)
  spillovers: >
    Polluting activity may relocate to lower-rate provinces or to exempt
    sectors. Output-price and input-market effects can spill over to
    non-polluting firms through supply chains. Cross-border air and water
    pollution can create leakage.
research_compatibility:
  outcome_domains:
  - air pollution
  - water pollution
  - solid waste
  - corporate green innovation
  - firm environmental investment
  - total factor productivity
  - employment and green skills
  - firm performance
  - tax compliance
  - public finance
  affected_populations:
  - heavily polluting enterprises
  - manufacturing workers
  - local tax and ecology officials
  - residents in polluted regions
  - investors in green technology
  mechanism_channels:
  - emission-abatement investment
  - end-of-pipe treatment
  - process modification
  - green innovation
  - production relocation
  - tax compliance and enforcement
  - input substitution
  best_for:
  - Difference-in-differences designs exploiting the 2018 national cutoff
  - Intensity DID using provincial tax-rate variation
  - Studies linking firm-level emissions or green-patent data to tax exposure
  - Research on how Pigovian taxes affect corporate behavior in developing countries
  not_good_for:
  - Identifying effects for sectors exempt from the tax
  - Long-run general-equilibrium outcomes without a long post-reform window
  - Outcomes that cannot be linked to firm, industry, or province identifiers
  - Designs that cannot separate the tax from concurrent environmental campaigns
    such as central environmental inspections
design:
  claim_type: causal
  affordances:
  - single national effective date
  - province-level rate variation
  - pre-existing discharge-fee baseline
  - availability of listed-firm panel data
  - concentration-based tax reductions that create threshold variation
  candidate_designs:
  - difference-in-differences with a 2018 cutoff
  - event study around the implementation date
  - intensity difference-in-differences using provincial rates
  - triple-difference adding polluting versus non-polluting firms
  - regression discontinuity at emission-standard thresholds for tax reductions
  identifying_variation: >
    The national switch from pollution-discharge fees to environmental tax on
    1 January 2018, interacted with cross-sectional exposure from industry
    pollution intensity and province-level tax rates.
  primary_strategy: >
    Difference-in-differences on a firm-year panel: Post2018 ×
    HeavyPolluter, with firm and year fixed effects and standard errors
    clustered at the firm or province level.
  estimand: >
    The average effect of the environmental protection tax on outcomes for
    treated firms relative to untreated firms, under a parallel-trends
    assumption.
  treatment_variable: >
    A post-2018 indicator interacted with a heavy-polluting-industry indicator,
    or a continuous measure of expected tax burden based on province rates and
    firm emissions.
  comparison_logic: >
    Heavy-polluting firms after 2018 are compared with the same firms before
    2018 and with light-polluting or non-polluting firms over the same period.
  estimation_notes: >
    Include firm and year fixed effects; control for province or industry
    time-varying characteristics where needed; cluster at the province or firm
    level. For intensity designs merge provincial tax rates with firm-level
    emissions. Modern staggered-DID estimators are unnecessary for the national
    cutoff but become relevant if exploiting provincial rate-adoption timing.
  assumptions:
  - Parallel trends between heavy- and light-polluting firms absent the reform
  - Provincial rate choices are conditionally independent of unobserved firm
    emission trends
  - No other national policy changed differentially for heavy-polluting firms
    in 2018
  - Spillovers to untreated firms or regions are limited or can be modeled
  diagnostics:
  - Pre-trends in event-study plots
  - Placebo reform dates
  - Robustness to alternative heavy-polluting industry definitions
  - Sensitivity to provincial rate measures
  - Tests for emission leakage across provinces
threats:
- type: anticipation
  basis: documented
  condition: >
    The law and effective date were announced in December 2016, so firms could
    adjust during 2017 before the tax took effect.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Exclude 2017 from the pre-period
  - Test for 2017 placebo effects
  - Estimate dynamic event-study coefficients around 2018
- type: confounding-policies
  basis: inferred
  condition: >
    Concurrent environmental policies such as central environmental inspections,
    the Air Pollution Prevention and Control Action Plan, and carbon-trading
    pilots overlap with 2018 and may affect heavy polluters.
  evidence_refs:
  - E1
  - E3
  possible_diagnostics:
  - Control for central environmental inspection timing
  - Include province-by-year fixed effects where the design allows
  - Use non-target pollutants or exempt sectors as falsification tests
- type: endogenous-rate-setting
  basis: inferred
  condition: >
    Provinces that chose higher tax rates may differ from low-rate provinces in
    wealth, pollution severity, or enforcement capacity, biasing intensity
    estimates.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Control for province-level economic and pollution trends
  - Use pre-determined rate determinants as conditioning variables
  - Compare within-province variation across pollutants where possible
- type: spillovers-and-leakage
  basis: inferred
  condition: >
    Firms may shift production to lower-rate provinces or abroad, and
    output-market effects may affect non-polluting firms.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Estimate effects in border counties
  - Test for changes in neighboring low-rate provinces
  - Restrict the sample to firms with immobile production
- type: measurement-error
  basis: inferred
  condition: >
    Emission data may come from self-reporting or intermittent monitoring, and
    automatic monitoring is not universal; tax reductions depend on
    concentration thresholds that may be measured with error.
  evidence_refs:
  - E2
  - E3
  possible_diagnostics:
  - Use continuous emission monitoring subsamples where available
  - Sensitivity to alternative emission measures
  - Compare reported emissions with tax-revenue aggregates
- type: selective-compliance
  basis: inferred
  condition: >
    Firms may underreport emissions or engage in tax avoidance, especially in
    regions with weaker tax administration.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Compare tax payments with reported emissions
  - Test for bunching around reduction thresholds
  - Examine heterogeneous effects by regional enforcement capacity
empirical_requirements:
  contract_version: 1
  population: Chinese industrial enterprises, especially A-share listed firms or
    pollution-intensive firms, observed before and after 2018.
  observation_unit: firm-year or province-year
  geography_level: province or firm location
  time_start: 2008
  time_end: 2022
  minimum_frequency: annual
  minimum_pre_periods: 4
  minimum_post_periods: 3
  required_fields:
  - outcome (emissions, green patents, investment, productivity, etc.)
  - firm identifier
  - calendar year
  - industry classification
  - province code
  - taxable emissions or pollution intensity
  - firm financial controls
  required_identifiers:
  - firm identifier
  - year
  - province code
  treatment_key:
  - firm identifier
  - year
  treatment_source: >
    Primary legal sources are Presidential Order No. 61 and State Council Order
    No. 693; provincial tax-rate decisions are published by provincial People's
    Congresses. Firm data come from CSMAR/Wind; emissions from CSMAR
    environmental-disclosure files, pollution-permit platforms, or corporate
    reports; tax-revenue aggregates from the China Taxation Yearbook.
  measurement_risks:
  - Self-reported emissions may understate true pollution.
  - Provincial rate data must be manually compiled.
  - Industry classification codes change over time.
  - Firm relocation or exit may be correlated with treatment.
  - Concentration data needed for reduction thresholds can be sparse.
evidence:
- id: E1
  source_type: policy-document
  citation: >
    National People's Congress of China. 2016. "Presidential Order No. 61 of
    the People's Republic of China: Environmental Protection Tax Law."
  url: http://www.npc.gov.cn/zgrdw/npc/xinwen/2016-12/25/content_2005007.htm
  date: '2016-12-25'
  supports:
  - identity
  - timeline
  - scope
  verification_status: verified
  access_level: official-document
  locator: >
    Presidential Order No. 61, dated 25 December 2016; states that the
    Environmental Protection Tax Law was passed by the 12th NPC Standing
    Committee at its 25th session and takes effect on 1 January 2018.
- id: E2
  source_type: policy-document
  citation: >
    State Council of China. 2017. "Implementation Regulations of the
    Environmental Protection Tax Law" (State Council Order No. 693).
  url: https://30091820.s21i.faiusr.com/61/6/ABUIABA9GAAg1OjIqQYo2pv42AQ.pdf
  date: '2017-12-25'
  supports:
  - identity
  - timeline
  - assignment
  verification_status: verified
  access_level: official-document
  locator: >
    State Council Order No. 693, issued 25 December 2017 and effective
    1 January 2018; defines taxable pollutants, exemptions, tax reductions,
    monitoring methods, and provincial rate-setting authority.
- id: E3
  source_type: paper
  citation: >
    Yang, Xiaolei, Panbing Wan, and Mian Yang. 2026. "How polluting
    enterprises respond to Pigovian tax: Evidence from China's environmental
    protection tax law." China Economic Review 98: 102723.
  url: https://doi.org/10.1016/j.chieco.2026.102723
  date: 2026
  supports:
  - design_applications
  - design
  - assignment
  verification_status: reported
  access_level: abstract
  locator: >
    China Economic Review abstract; reports an A-share listed heavily
    polluting firm sample from 2008 to 2021, a DID design, and findings that
    the tax reduces emissions, especially wastewater, through green innovation.

design_applications:
- paper: How polluting enterprises respond to Pigovian tax
  doi: 10.1016/j.chieco.2026.102723
  journal: China Economic Review
  year: 2026
  research_question: >
    How do polluting enterprises in China adjust emissions and green innovation
    in response to the 2018 environmental protection tax?
  population: A-share listed enterprises in heavily polluting industries, 2008-2021
  outcome: Emissions (wastewater, waste gas, solid waste) and green innovation
  data_used:
  - CSMAR/Wind A-share firm financial and governance data
  - Firm pollution-emissions data
  - Heavy-polluting industry classification
  - 2018 Environmental Protection Tax Law implementation indicator
  treatment_encoding: Post-2018 indicator interacted with heavy-polluting-industry indicator
  comparison: Light-polluting or non-polluting listed firms over the same period
  empirical_design: Difference-in-differences with firm and year fixed effects
  assumptions:
  - Parallel trends between heavy- and light-polluting firms before 2018
  - No concurrent shock differentially affects heavy polluters in 2018
  - Industry classification captures exposure to the tax
  threats_addressed:
  - Parallel trends via event study
  - Mechanism analysis (source prevention, process modification, end-of-pipe treatment)
  - Robustness checks reported by the authors
  evidence_refs:
  - E3
readiness_blockers:
- >
  The exact province-by-pollutant tax-rate schedule has not been compiled from
  official provincial decisions inside this record.
- >
  Full replication materials for the CER paper have not been inspected; sample
  construction and treatment-coding details rely on the published abstract.
- >
  Firm-level environmental-protection tax payment data are not documented here.
method_transfer: null
---
## Institutional Background

China began pricing industrial pollution through a discharge-fee system in the
1980s, but fees were often negotiated, poorly enforced, and collected by
environmental agencies with limited leverage. The Environmental Protection Tax
Law of 2016 replaced that system with a tax collected by tax authorities and
backed by the Tax Collection and Administration Law. [E1]

## What Changed

On 1 January 2018 the Environmental Protection Tax took effect nationwide.
Taxable pollutants include air pollutants, water pollutants, solid waste, and
noise. Provincial governments set air- and water-pollutant rates within statutory
ranges, and firms receive lower tax bills when their emissions are well below
standards. The reform thus created a common post-2018 treatment date and
province-level variation in tax intensity. [E1; E2]

## Implementation and Assignment

The Standing Committee of the National People's Congress enacted the law, the
State Council issued implementation regulations, and provincial People's
Congresses chose rates. Tax bureaus collect the tax using emissions data shared
by ecology authorities. All enterprises directly discharging taxable pollutants
are taxpayers, but heavily polluting industries and high-emission firms bear the
largest burden. Assignment is therefore determined by the national effective
date, industry pollution intensity, and province-level rate choices. [E1; E2]

## Why This Creates Empirical Variation

The 2018 cutoff provides a clear before/after breakpoint for a
difference-in-differences design. Cross-sectional exposure comes from which
industries are heavy polluters and which provinces chose higher rates. This
variation can be used to estimate how Pigovian taxes affect emissions, abatement
investment, green innovation, firm performance, and labor demand. [E2; E3]

## Identification Risks

Firms may have anticipated the reform during 2017. Concurrent policies such as
central environmental inspections and air-pollution action plans overlap with
2018. Provinces that set higher tax rates may differ in wealth, enforcement
capacity, or baseline pollution. Firms can respond by relocating, underreporting
emissions, or shifting output to lower-rate provinces. [E1; E2; E3]

## Data Requirements

Researchers need a firm-year panel with firm identifiers, province, industry,
year, emissions, and outcome variables. Provincial tax-rate schedules must be
collected from official provincial documents. Firm financials are available from
CSMAR or Wind, and emissions data from corporate environmental disclosures,
pollution-permit platforms, or tax records. [E2; E3]

## Evidence Notes

E1 verifies the law's passage and effective date. E2 verifies the taxable
pollutants, exemptions, reductions, and provincial rate-setting rules. E3
reports a DID application using heavily polluting listed firms; its sample and
treatment coding have not been verified from replication materials.
