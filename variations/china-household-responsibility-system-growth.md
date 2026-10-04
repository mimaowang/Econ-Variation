---
schema_version: 2
id: china-household-responsibility-system-growth
name: Province-Year Household Responsibility System Conversion Intensity in China's Agricultural Growth Accounting (1970–1987)
aliases:
- HRS agricultural growth Lin 1992
- 家庭联产承包责任制 农业增长
- decollectivization productivity China
- Lin rural reforms AER
- household responsibility system total factor productivity
- province-year HRS conversion share

status: extracted
provenance:
  task_id: task-4bb8995b2384
scope:
  country: China
  regions:
  - All provinces with agricultural sector (excluding Tibet)
  domains:
  - agriculture
  - development
  - productivity
  - land
  - structural-transformation
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: The staggered province-level adoption of the Household Responsibility System (HRS) between 1978 and 1984, which
    shifted agricultural production from collective farming to household-based farming, assigning land use rights to individual
    households and allowing them to retain residual output above procurement quotas
  authority: Chinese central government (State Council, Communist Party Central Committee), implemented at the provincial
    level under central authorization
  legal_identifiers:
  - Central Committee Document No. 1 (1982, 1983, 1984)
  - provincial HRS implementation directives
  - agricultural reform experimental zone approvals
  implementation_regime: '[E1, reported claim] A small number of production teams began household contracting near the end of 1978, initially against central prohibition; official acceptance followed in late 1981, after which adoption became nearly universal by end-1983.'
  assignment_mechanism: '[E1, reported claim] The paper uses province-year HRS intensity—the proportion of production teams converted to HRS—as a production-function regressor. It describes the institutional shift as largely spontaneous in response to underlying economic forces; it does not establish a random provincial assignment rule.'
  parent: null
  related_variations:
  - china-land-reform-sex-selection
  - china-land-property-rights-agricultural-efficiency
timeline:
  announcement: '1978-12-01'
  effective: null
  implementation_start: 1978
  implementation_end: 1984
  local_timing: '[E1, reported claim] The panel contains province-year HRS conversion shares from 1970-1987, except that the 1980 province observations are omitted because the number of converted teams by province was unavailable. National HRS prevalence rose from 1 percent in 1979 to 98 percent by end-1983.'
  anticipation: '[E1, reported claim] The paper reports initial local experimentation while household contracting was prohibited, subsequent central concession with a poor-region restriction, and full official acceptance in late 1981. It does not support a clean no-anticipation assumption.'
  last_verified: '2026-07-13'
assignment:
  unit: Province or province-year
  treated: '[E1, reported claim] There is no binary treated province in the paper''s baseline. Exposure is higher in province-years with a larger share of production teams converted to HRS.'
  comparison_pool: '[E1, reported claim] The production-function coefficient uses lower versus higher province-year conversion shares, within and across provinces conditional on province dummies and regressors; it is not a designated never-treated or not-yet-treated control group.'
  rule: '[E1, reported claim] The regression treatment is the share of a province''s production teams converted to HRS, not a clean province-level adoption date; it proxies institutional change from collective-team production to household contracts.'
  intensity: Continuous — the proportion of production teams or households within each province that had adopted HRS in each
    year, from 0 to 1
  exemptions: []
  compliance: '[E1, reported claim] HRS diffusion was initially local and later officially accepted; national adoption was about 98 percent of production teams by end-1983. The paper does not establish a uniform top-down compliance process.'
  exposure_construction: '[E1, reported claim] Use province-year production-team HRS conversion share in the production function. Exclude 1980 or separately source a defensible province-level HRS measure, because the paper omits that year for missing province conversion data.'
  required_identifiers:
  - province code
  - year
  - HRS adoption share (proportion of teams/households)
  spillovers: HRS adoption may have affected non-agricultural sectors through released labor, increased rural incomes, and
    demand for industrial inputs; cross-province spillovers through output prices and input markets
research_compatibility:
  outcome_domains:
  - agricultural output
  - total factor productivity in agriculture
  - input use (labor
  - fertilizer
  - machinery
  - land)
  - agricultural procurement
  - rural income
  - grain output
  affected_populations:
  - Rural agricultural households
  - agricultural labor force
  - state procurement agencies
  - rural non-agricultural enterprises
  mechanism_channels:
  - incentive effects of residual claimancy
  - labor effort intensification
  - improved input allocation
  - price response to procurement adjustments
  - productivity improvement from organizational change
  best_for:
  - Quantifying the productivity and output effects of decollectivization
  - understanding the contribution of institutional reform versus price reform to agricultural growth
  - analyzing the sources of China's rapid agricultural growth 1978–1984
  not_good_for:
  - Non-agricultural outcomes
  - post-1990 agricultural growth (the HRS effect was largely a one-time productivity improvement)
  - urban or industrial outcomes
design:
  claim_type: causal
  affordances:
  - province-year HRS conversion intensity
  - rich province-level panel data on agricultural inputs and outputs
  - pre-reform province panel for specification checks
  candidate_designs:
  - production function approach with HRS adoption share as a shift variable
  - decomposition of output growth into decollectivization effect
  - price effect
  - and input accumulation effect
  identifying_variation: '[E1, reported claim] Within the province panel, the HRS-team share changes rapidly during 1979-1983 and enters a production function alongside inputs, national price variables, crop-pattern and cropping-intensity measures, a trend, and province dummies. It is an observational production-function design, not randomized staggered adoption.'
  assumptions:
  - conditional on province effects and included controls, HRS intensity is not standing in for omitted province-year productivity shocks
  - the production-function specification separates institutional, price, input, crop-pattern, cropping-intensity, and trend effects sufficiently for the reported decomposition
  diagnostics:
  - assess sensitivity to alternative input and functional-form specifications reported by the paper
  - test sensitivity to excluded 1980 province observations and the very short diffusion window
  - inspect whether national price indices and unobserved contemporaneous changes remain separable from HRS intensity
  primary_strategy: '[E1, reported claim] Province-level Cobb-Douglas production-function estimation with province dummies, HRS team share, national price measures, crop-pattern and cropping-intensity measures, a time trend, and conventional inputs; the paper uses the fitted components for growth accounting.'
  estimand: The causal effect of the recorded exposure on Gross agricultural output value (constant prices), total factor
    productivity (TFP) in agriculture, output per unit of input, conditional on the stated design assumptions.
  treatment_variable: '[E1, reported claim] Province-year proportion of production teams converted to HRS; price controls are national price ratios rather than a simple post-1978 indicator.'
  comparison_logic: '[E1, reported claim] The coefficient is identified from within- and between-province variation in HRS team shares in the 1970-1987 panel (with 1980 omitted), conditional on province effects and included regressors; the paper is not framed as an early-versus-late DID.'
  estimation_notes: '[E1, reported claim] Province-level production function estimation with HRS conversion share as a shift variable; growth accounting decomposes fitted output growth into decollectivization, price, input, and residual components. It is not a staggered-DID estimator.'
threats:
- type: endogenous-adoption-timing
  basis: inferred
  condition: '[E1, reported claim] The paper describes local and largely spontaneous diffusion rather than random assignment. If province-specific conditions both speeded conversion and changed agricultural productivity, the HRS coefficient may combine institutional change with those shocks.'
  evidence_refs:
  - E1
  possible_diagnostics:
  - test sensitivity to province-specific trends or alternative modern designs where data permit
  - examine pre-reform province trajectories and documented adoption determinants
- type: concurrent-price-reforms
  basis: documented
  condition: '[E1, reported claim] National procurement and market price measures move during the same period as HRS diffusion. Separate regressors aid decomposition but cannot by themselves prove that simultaneous institutional and price changes are fully separable.'
  evidence_refs:
  - E1
  possible_diagnostics:
  - include input prices and procurement prices in the production function framework
  - test sensitivity to price specifications and crop composition controls
  - distinguish national price variation from province-specific HRS intensity in interpretation
- type: measurement-error
  basis: inferred
  condition: The share of production teams adopting HRS may be measured with error, particularly in provinces where adoption
    was gradual; official statistics may overstate adoption rates; input and output data from the early reform period may
    be unreliable
  evidence_refs:
  - E1
  possible_diagnostics:
  - use multiple measures of HRS adoption
  - test sensitivity to the treatment intensity specification
  - examine robustness to using binary adoption indicators rather than continuous shares
  - check consistency of official data with household-level survey data where available
empirical_requirements:
  contract_version: 1
  population: Chinese agricultural sector across 28 provinces, 1970–1987
  observation_unit: Province-year
  geography_level: Province
  time_start: 1970
  time_end: 1987
  minimum_frequency: annual
  minimum_pre_periods: 5
  minimum_post_periods: 3
  required_fields:
  - province code
  - year
  - gross agricultural output value
  - sown area
  - labor input (agricultural employment)
  - fertilizer use
  - mechanical power
  - draft animal power
  - HRS adoption share
  - agricultural procurement price index
  - weather indicators
  required_identifiers:
  - province code
  - year
  treatment_key:
  - province code
  - year
  - HRS adoption share (proportion of teams)
  treatment_source: '[E1, reported claim] Province conversion shares: Research Center for Rural Development of the State Council (1981–1982) and China Agricultural Yearbooks (1984/1985 volumes for 1983–1984). The paper treats 1979 as effectively zero and omits 1980 because province shares are unavailable; other agricultural series come from the cited statistical sources.'
  measurement_risks:
  - Provincial agricultural output data may be affected by changes in reporting standards during the reform period
  - input data quality may vary across provinces and over time
  - HRS adoption rate may not capture within-province heterogeneity in reform intensity
  - price data for agricultural inputs and outputs may be incomplete
evidence:
- id: E1
  source_type: paper
  citation: 'Lin, Justin Yifu. 1992. "Rural Reforms and Agricultural Growth in China." American Economic Review 82 (1): 34–51.'
  url: https://doi.org/10.2307/2117601
  date: 1992
  supports:
  - scope.china_relevance
  - identity.instrument
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.local_timing
  - timeline.anticipation
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.compliance
  - assignment.exposure_construction
  - design.claim_type
  - design.primary_strategy
  - design.identifying_variation
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - design.assumptions
  - design.diagnostics
  - threats.condition
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_key
  - empirical_requirements.treatment_source
  - empirical_requirements.measurement_risks
  - design_applications.paper
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
  - design_applications.research_question
  - design_applications.population
  - design_applications.outcome
  - design_applications.data_used
  - design_applications.treatment_encoding
  - design_applications.comparison
  - design_applications.empirical_design
  - design_applications.assumptions
  - design_applications.threats_addressed
  verification_status: verified
  access_level: full-text
  locator: 'Inspected full text: pp. 34-38 (institutional evolution and national HRS shares), pp. 40-42 (28-province 1970-1987 panel, omitted 1980 HRS observations, variables and production function), pp. 43-48 (estimates and decomposition).'
design_applications:
- paper: Rural Reforms and Agricultural Growth in China
  doi: 10.2307/2117601
  journal: American Economic Review
  year: 1992
  research_question: What are the relative contributions of decollectivization (HRS), price adjustments, and other reforms
    to China's agricultural output growth between 1978 and 1984?
  population: Chinese agricultural sector, 28 provinces, 1970–1987
  outcome: Gross agricultural output value (constant prices), total factor productivity (TFP) in agriculture, output per unit
    of input
  data_used:
  - China Statistical Yearbooks for provincial agricultural output and inputs
  - '[E1, reported claim] Research Center for Rural Development of the State Council (province conversion shares for 1981–1982) and China Agricultural Yearbooks (1984 and 1985 volumes, shares for 1983–1984)'
  - Provincial agricultural statistical compilations
  - Agricultural procurement price indices from State Price Bureau
  treatment_encoding: '[E1, reported claim] Province-year proportion of production teams converted to HRS; 1980 is excluded because province conversion shares were unavailable. National price ratios enter separately; there is no generic post-1978 treatment indicator.'
  comparison: '[E1, reported claim] Lower versus higher conversion intensity across the province-year panel, conditional on province effects and production-function controls; not early- versus late-adopter DID.'
  empirical_design: Province-level production function estimation with HRS adoption share as a shift variable; growth accounting
    decomposition of output growth into decollectivization effect, price effect, input growth, and residual TFP change
  assumptions:
  - '[E1, reported claim] Conditional on province effects and included regressors, HRS conversion intensity is not proxying for omitted province-year productivity shocks; the production function is sufficiently specified for the reported decomposition.'
  threats_addressed:
  - '[E1, reported claim] Province effects, national price measures, crop composition, cropping intensity, and conventional inputs enter the specification; these controls do not independently establish exogeneity of conversion intensity.'
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
method_transfer: null
---
## Institutional Background

[E1, reported claim] Before the reform, the production team was the basic farming unit. Near the end of 1978, some teams began contracting collectively owned land, resources, and output quotas to households despite central prohibition. The paper reports that official acceptance came in late 1981 and that 98 percent of production teams had adopted HRS by the end of 1983. This record has not independently inspected the central directives, so the institutional chronology remains paper-reported.

## What Changed

[E1, reported claim] Under HRS, collectively owned land was contracted to households for up to 15 years. In the paper's production-function decomposition, decollectivization accounts for about half of the reported 1978-1984 crop-output growth, while price adjustments also contribute through input response. This is a model-based decomposition, not a direct experimental estimate of a separately randomized policy shock.

## Implementation and Assignment

The paper uses 28-province annual observations from 1970-1987 and an HRS variable equal to the province's share of converted production teams. [E1, reported claim] The 1980 province observations are dropped because those conversion counts are unavailable. This is meaningful spatial and temporal intensity variation, but it does not supply a known external assignment rule; province dummies absorb time-invariant differences, while national price variables and a trend address only some concurrent changes.

## Why This Creates Empirical Variation

The coefficient is recovered from variation in provincial conversion shares after conditioning on inputs, province dummies, national price ratios, crop composition, cropping intensity, and trend. [E1, reported claim] It supports an evidence-bounded causal interpretation only if remaining province-year productivity shocks are not correlated with HRS conversion; the historical account of spontaneous diffusion makes that a substantive assumption, not an institutional fact.

## Identification Risks

The main identification challenge is endogenous diffusion: the paper describes HRS as evolving largely in response to underlying economic forces, so a province's conversion share can be correlated with unobserved province-year productivity conditions. [E1, reported claim] Province fixed effects remove time-invariant differences, but do not by themselves resolve time-varying selection. A second challenge is simultaneity with agricultural price reforms and other changes. The paper includes price measures and decomposes fitted output growth, which is useful accounting structure but does not turn the components into separately randomized shocks. [E1; analytical inference]

## Data Requirements

The analysis uses annual provincial panel data (1970–1987) for 28 Chinese provinces, covering gross agricultural output at constant prices, sown area, agricultural labor, fertilizer use, mechanical and draft-animal power, and the proportion of production teams adopting HRS. [E1, reported claim] The paper obtains province conversion shares for 1981–1982 from the State Council's Rural Development Research Center and for 1983–1984 from China Agricultural Yearbooks; it excludes 1980 because province-level conversion information was unavailable. A new application therefore needs a documented province-year intensity series rather than a generic post-reform dummy.

## Evidence Notes

E1 is the published AER article and directly documents its own production-function construction and growth-accounting decomposition. Its reported conclusion is that the fitted decollectivization component accounts for roughly half of 1978–1984 output growth. That number is a model-dependent decomposition, not a transportable treatment effect or independent confirmation that the conversion path was exogenous. The underlying central directives and full province conversion roster have not been independently reconstructed here.
