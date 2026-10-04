---
schema_version: 2
id: china-migrants-firms-evidence
name: Origin Crop-Price Shocks, Historical Migration Links, and Urban Firm Exposure in China (2000–2005)
aliases:
- Imbert Seror Zhang Zylberberg migrants firms China
- 农民工 企业
- migration shock firm productivity
- rural-urban migration China
status: grounded
provenance:
  task_id: task-1afa87e08bde
scope:
  country: China
  regions:
  - Mainland rural origin prefectures and urban destination prefectures in the paper's sample
  domains:
  - regional-economics
  - urban-economics
  - development
  - labor
  - firms
  - innovation
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    Chinese urban manufacturing establishments share a destination-prefecture
    migrant-labor supply exposure. Origin-prefecture crop portfolios and
    overseas crop-price innovations predict differential inflows to those
    destinations through pre-2000 migration networks.
identity:
  instrument: >
    The paper's destination-prefecture shift-share instrument sums shocks
    to potential agricultural revenue in rural origin prefectures, weighted
    by each origin's pre-2000 settlement shares across urban destinations.
    Its raw price input is FAOSTAT annual producer prices outside China,
    not observed weather disasters or a hukou-policy rollout.
  authority: >
    No government assigned this shock. International producer-price changes
    and fixed crop potential enter the authors' constructed instrument;
    the Chinese National Bureau of Statistics collected the population
    and firm sources used to measure the first stage and outcomes.
  legal_identifiers:
  - FAOSTAT Agricultural Producer Prices (underlying price-series family)
  - FAO-IIASA GAEZ v3 potential-yield family (underlying fixed suitability input)
  - 2000 China Population Census and 2005 1% Population Sample Survey (migration measurement)
  implementation_regime: >
    This is a market-price and inherited-network exposure, not an enacted
    policy. The authors combine crop-specific international farm-gate
    price innovations with origin crop potential, then map origin shocks
    to destination prefectures using pre-2000 rural-to-urban settlement
    patterns. Hukou restrictions form background context, not treatment.
  assignment_mechanism: >
    Destination d receives z_d = sum over other origin prefectures o of
    lambda_od times s_o. Here lambda_od is the pre-2000 fraction of
    migrants from origin o settling in d, and s_o aggregates 2000–2005
    crop-price innovations weighted by o's fixed potential crop revenue.
    All firms in the same destination inherit the same instrument value;
    the baseline design does not assign firm-specific migrant-origin shares.
  parent: null
  related_variations:
  - china-2014-hukou-local-implementation
timeline:
  announcement: null
  effective: null
  implementation_start: 2000
  implementation_end: 2005
  local_timing: >
    Price innovations and reconstructed rural-to-urban flows cover
    2000–2005. Historical origin-destination settlement shares come from
    the 2000 census; the 2005 sample survey retrospectively measures
    migration spells. Baseline firm outcomes are differenced from 2000
    to 2006. Annual raw series do not make the main estimate an annual
    firm-panel event study.
  anticipation: >
    Price innovations are residual changes after the paper's AR(1)
    specification, not events with public announcement and effective
    dates. Their conditional unpredictability and exclusion from
    urban production must be evaluated, not presumed.
  last_verified: '2026-10-02'
assignment:
  unit: Destination prefecture for instrument; firm within that prefecture for outcome
  treated: >
    A destination with larger predicted rural-migrant inflow under the
    paper's origin crop-revenue and historical-network construction;
    exposure is continuous rather than binary.
  comparison_pool: >
    Manufacturing establishments in other destination prefectures with
    different predicted inflows, using their 2000-to-2006 outcome changes.
    Firms within one destination do not supply independent instrument
    variation in the baseline specification.
  rule: >
    For each of 21 crops, take FAOSTAT producer prices across countries
    other than China, weighted by baseline export shares, and extract
    crop-year log-price innovations using an AR(1) with crop and year
    effects. Weight these innovations by an origin prefecture's fixed
    potential crop-revenue portfolio from baseline harvested area and
    GAEZ yield; aggregate 2000–2005 shocks. Weight origin shocks by
    pre-2000 destination settlement shares to obtain each destination's
    instrument. The exact original data vintage and code still matter.
  intensity: Predicted immigration rate induced by origin crop-price shocks and historical settlement shares
  compliance: >
    The first stage is migration behavior, not regulatory compliance.
    The accepted manuscript reports a negative first-stage coefficient
    because a negative origin income shock raises outmigration; actual
    migration is inferred from survey histories with a return-migration
    correction.
  exposure_construction: >
    Instrument actual destination immigration rate over 2000–2005
    (inter-prefecture rural-to-urban migrants divided by the destination's
    2000 non-migrant resident population) with the destination-level
    shift-share. Match every 2000–2006 manufacturing establishment to
    a historically consistent destination prefecture. Do not call the
    instrument a firm's measured migrant-worker share.
  required_identifiers:
  - origin and destination prefecture crosswalk
  - crop, country, year, and pre-period export-share keys for price inputs
  - origin-by-crop harvested area and potential yield
  - pre-2000 origin-destination migrant stock
  - 2005 survey origin, destination, migration year, hukou type, and weights
  - firm ID and destination prefecture
  exemptions:
  - Tobacco is excluded from the 21-crop price basket because China may influence its international price
  - Within-prefecture movement is not the baseline inter-prefecture migration contrast
  spillovers: >
    Agricultural price changes could affect urban firms through traded
    intermediate inputs or demand, not only migration. Labor-market
    and product-market responses can also propagate across destinations.
research_compatibility:
  outcome_domains:
  - firm labor cost and employment
  - capital-to-labor ratio and value added per worker
  - product mix and patenting
  - destination manufacturing structure
  affected_populations:
  - urban manufacturing establishments in the ASIF/NBS survey
  - rural migrants and destination workers
  mechanism_channels:
  - origin-income-induced rural outmigration
  - destination labor-supply changes
  - input mix, product choice, and innovation adjustment
  best_for:
  - Urban firm outcomes linked to stable prefectures and the paper's multi-year migration exposure
  - Assessing long-horizon production responses to rural-to-urban labor supply
  not_good_for:
  - Firm-specific migrant-sourcing claims absent employee-origin data
  - Interpreting the design as a hukou reform or weather-shock experiment
  - Annual event studies reconstructed from the paper's aggregate IV alone
  - Agricultural outcomes as the main destination research object
design:
  claim_type: causal
  affordances:
  - Price innovations interact with fixed origin crop portfolios
  - Earlier origin-destination settlement links transmit shocks unevenly
  - Prefecture-level instrument joins to an establishment outcome panel
  candidate_designs:
  - Baseline 2000-to-2006 first-difference firm-outcome IV
  - Origin-level shift-equivalent IV and pretrend diagnostics
  identifying_variation: >
    Across-destination differences in exposure to 2000–2005 origin
    agricultural-income shocks through historical settlement links.
    Historical shares may be endogenous to urban demand; the paper's
    identifying claim rests primarily on quasi-random, sufficiently
    independent origin shifts and the exclusion restriction.
  primary_strategy: >
    In the balanced ASIF/NBS sample, regress each firm's 2000-to-2006
    change in an outcome on its destination's 2000–2005 immigration
    rate, instrumented by destination z_d. Baseline regressions weight
    firms by 2000 employment and cluster at destination prefecture.
    Origin-shift equivalents and shift-share-robust inference are checks.
  estimand: >
    Conditional effect of a higher rural-migrant inflow rate on
    2000-to-2006 outcomes for above-scale manufacturing
    establishments represented in the instrument-induced contrast.
    It is not a firm-specific treatment effect or an aggregate effect
    on every Chinese worker.
  treatment_variable: Actual destination immigration rate in 2000–2005; instrument is historical settlement shares times origin potential-crop-revenue price shocks
  comparison_logic: >
    Compare 2000-to-2006 changes across firms located in destinations
    with differently predicted rural inflows. The same-prefecture
    establishments share treatment and instrument, so inference must
    respect the prefecture-level exposure.
  estimation_notes: >
    The accepted manuscript's Table 3 has 31,886 balanced-panel firms.
    Table 4 checks prefecture-by-sector aggregates and an unbalanced
    sample. The price basket has only 21 crops and geography can
    correlate origin shocks; the authors explicitly discuss this.
  assumptions:
  - Crop-price innovations are plausibly exogenous to destination manufacturing potential outcomes
  - Origin shocks influence destination manufacturing mainly through migration, conditional on tested channels
  - A few correlated crops or geographically clustered origins do not dominate effective identifying variation
  - Historical links affect outcomes only through permitted pathways once current and lagged exposures are handled
  diagnostics:
  - Origin-level shift-equivalent specification and 1998–2000 pretrend test
  - Exclude agricultural-input-processing industries and nearby origin-destination flows
  - Control for neighboring shocks, market access, and baseline immigrant stock
  - Examine lagged 1993–1998 shocks and shift-share-robust standard errors
  - Compare balanced with unbalanced establishment samples
threats:
- type: exclusion-through-goods-markets
  basis: documented
  condition: Crop-price shocks could affect city manufacturing through input costs or rural demand rather than only migrant labor.
  evidence_refs: [E1, E2]
  possible_diagnostics: [exclude processors of agricultural goods, control neighboring income shocks, restrict to exporters, omit short-distance origin links]
- type: correlated-shifts-and-history
  basis: documented
  condition: Crop portfolios are spatially correlated and only 21 crops supply price innovations; historical migration shares may encode persistent urban demand.
  evidence_refs: [E1, E2]
  possible_diagnostics: [origin-level analysis, effective-shift concentration, lagged-shock placebo, shift-share-robust inference]
- type: survey-flow-and-firm-selection
  basis: documented
  condition: The 2005 retrospective survey misses return or step migration and the main balanced ASIF sample omits entry, exit, and small firms.
  evidence_refs: [E1, E2]
  possible_diagnostics: [return-migration correction sensitivity, alternative flow definitions, unbalanced-sample comparison]
empirical_requirements:
  contract_version: 1
  population: Mainland above-scale industrial establishments in covered urban destination prefectures
  observation_unit: Establishment outcome change from 2000 to 2006
  geography_level: Destination prefecture; origin prefecture for instrument construction
  time_start: 2000
  time_end: 2006
  minimum_frequency: two endpoint outcomes plus annual price histories and migration-spell years
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - 2000 and 2006 firm compensation, employment, fixed assets, value added, and location
  - 2000 origin-destination migrant stock and destination resident population
  - 2005 retrospective migration origins, destinations, years, and survey weights
  - baseline origin-by-crop harvested area, potential yield, and world producer-price series
  - 2000 export-share weights for crop price aggregation
  required_identifiers: [firm ID, destination prefecture, origin prefecture, crop, country, year]
  treatment_key: [destination prefecture, origin prefecture, crop, year]
  treatment_source: >
    Paper's constructed IV draws on FAOSTAT Agricultural Producer Prices,
    FAO harvested-area mapping, FAO-IIASA GAEZ potential yield, 2000
    census migration stocks, and 2005 1% Population Sample Survey
    retrospective flows. Firm outcomes come from the NBS Annual Survey
    of Industrial Firms. These are source identities, not a claim that
    all restricted microdata are open.
  measurement_risks:
  - Return migration requires an author-modeled correction; intermediate stops are not fully observed
  - Current FAO data revisions and newer GAEZ versions need not reproduce the paper's original vintage
  - Firms are legal units, many small firms are outside ASIF, and stable IDs require matching
  - Prefecture boundary changes require a consistent origin-destination-firm crosswalk
  - Actual migrant share in each firm is not observed from the destination flow measure
evidence:
- id: E1
  source_type: paper
  citation: 'Imbert, Clément, Marlon Seror, Yifan Zhang, and Yanos Zylberberg. 2022. "Migrants and Firms: Evidence from China." Author accepted manuscript of American Economic Review 112(6):1885–1914, DOI 10.1257/aer.20191234.'
  url: https://wrap.warwick.ac.uk/id/eprint/163520/1/WRAP-Migrants-firms-evidence-China-2022.pdf
  date: 2022
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - identity.implementation_regime
  - timeline.local_timing
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.exposure_construction
  - assignment.required_identifiers
  - design.identifying_variation
  - design.primary_strategy
  - design.treatment_variable
  - design.comparison_logic
  - empirical_requirements.population
  - empirical_requirements.treatment_source
  - design_applications.treatment_encoding
  - design_applications.empirical_design
  verification_status: verified
  access_level: full-text
  locator: '39-page Warwick author accepted manuscript: pp.6–16 (paper §I, data, Equations 1–5, Table 2); pp.17–23 (Table 3 and identification checks); pp.26–29 (product and patent results). Inspected 2026-10-02; final AEA PDF was not accessed.'
- id: E2
  source_type: appendix
  citation: 'Imbert et al. 2022. Online Appendix to "Migrants and Firms: Evidence from China." American Economic Association.'
  url: https://www.aeaweb.org/articles/materials/16850
  date: 2022
  supports:
  - identity.assignment_mechanism
  - assignment.exposure_construction
  - design.assumptions
  - design.diagnostics
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: full-text
  locator: '56-page publisher-hosted online appendix, Appendix A.1 pp.2–5, B.2 pp.11–14, C.1–C.3 pp.19–29 and F pp.48–55; inspected 2026-10-02. Verifies author construction and limits, not independent raw-data replication.'
- id: E3
  source_type: official-data
  citation: 'FAO. FAOSTAT Agricultural Producer Prices dataset and price-domain explanation.'
  url: https://www.fao.org/prices/en
  date: 2026
  supports:
  - identity.legal_identifiers
  - identity.instrument
  - timeline.local_timing
  - assignment.required_identifiers
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: official-document
  locator: 'FAO prices page inspected 2026-10-02 identifies official national annual farm-gate producer prices by commodity, the raw price-series family. It does not verify the authors’ 21-crop selection, historical vintage, weights, residuals, or destination IV.'
- id: E4
  source_type: official-data
  citation: 'FAO and IIASA. Global Agro-Ecological Zones, official FAO database overview.'
  url: https://www.fao.org/land-water/resources/tools/databases/gaez/en
  date: 2026
  supports:
  - identity.legal_identifiers
  - identity.implementation_regime
  - assignment.required_identifiers
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: official-document
  locator: 'FAO GAEZ overview inspected 2026-10-02 confirms crop potential-yield and suitability data under different input/management scenarios. It describes the dataset family, not the authors’ exact 2012 v3 extraction or prefecture overlays.'
- id: E5
  source_type: official-data
  citation: 'National Bureau of Statistics of China. 2006. 2005年全国1%人口抽样调查主要数据公报.'
  url: https://www.stats.gov.cn/sj/tjgb/rkpcgb/qgrkpcgb/202302/t20230206_1901996.html
  date: 2006
  supports:
  - identity.legal_identifiers
  - identity.authority
  - timeline.local_timing
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: official-document
  locator: 'NBS communique dated 2006-03-16, survey description and notes: 2005 national 1% sample, mainland population, 2005-11-01 reference date, and aggregate floating-population figures. It does not expose prefecture-level individual migration histories used in the paper.'
- id: E6
  source_type: paper
  citation: 'American Economic Association. 2022. AER article page for Imbert et al., vol.112 no.6, pp.1885–1914.'
  url: https://doi.org/10.1257/aer.20191234
  date: 2022
  supports: [design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: 'AEA article page identifies paper, DOI, year, journal, pages, and supplemental appendix. Only metadata and abstract were accessible at publisher page; substantive design comes from E1–E2. Inspected 2026-10-02.'
design_applications:
- paper: 'Migrants and Firms: Evidence from China'
  doi: 10.1257/aer.20191234
  journal: American Economic Review
  year: 2022
  research_question: How do origin-income-driven rural migrant inflows alter urban manufacturing firms' labor costs, input use, products, and innovation?
  population: 31,886 balanced-panel above-scale establishments observed 2000–2006 in the baseline; alternative aggregates include the unbalanced sample
  outcome: Changes in compensation per worker, employment, capital/labor, and value added/worker; product choice and patent outcomes in extensions
  data_used:
  - NBS Annual Survey of Industrial Firms / above-scale manufacturing census, 2000–2006
  - 2000 Population Census baseline settlement patterns and 2005 1% Population Sample Survey migration histories
  - FAOSTAT producer prices, FAO harvested-area map, and FAO-IIASA GAEZ potential yields
  - Product descriptions and matched patent applications for secondary outcomes
  treatment_encoding: Destination prefecture immigration rate 2000–2005 instrumented with the pre-2000 origin-destination shares times 2000–2005 origin crop-price-revenue shocks
  comparison: Baseline-to-2006 outcome change of firms in destination prefectures with differing instrument-predicted migrant inflows
  empirical_design: Employment-weighted establishment first-difference 2SLS with prefecture-clustered inference; origin-level and shift-share checks
  assumptions:
  - Price-based origin shifts plausibly exogenous to urban manufacturing outcomes
  - Origin shocks affect destinations through migration rather than input-cost or product-demand channels
  - Historical shares and spatially correlated crop portfolios are handled sufficiently for the stated contrast
  threats_addressed: [goods-market exclusion, correlated shifts and pre-existing links, missed return migration, ASIF selection]
  evidence_refs: [E1, E2, E3, E4, E5, E6]
method_transfer: null
readiness_blockers:
- The paper's 2000 census and 2005 mini-census microdata, original FAO vintage, 2012 GAEZ v3 extraction, and crop-by-origin constructed exposure were not independently reproduced; current official pages verify source families only.
- The accessible full text is the author accepted manuscript plus publisher appendix, not a page-by-page comparison with the final AER version.
- The main estimate spans 2000-to-2006 firm changes and 2000–2005 migration, not annual causal responses; new use requires the original input vintages and a stable prefecture crosswalk.
- Crop-price shocks may also affect input costs and rural demand; the paper tests these channels, but the exclusion restriction remains an assumption.
superseded_by: null
deprecation_reason: null
---
## Institutional Background

The object is not a hukou reform and not an agricultural-outcome study. Rural workers move between Chinese prefectures, and urban manufacturing firms face changing local labor supply. Hukou rules affect migration costs and welfare but do not assign this paper's instrument [E1, reported context]. The 2005 NBS survey exists and records national floating-population aggregates [E5, verified]; the paper uses restricted individual migration histories rather than those public aggregate tables [E1–E2, reported construction].

## What Changed

Different international crop prices changed potential agricultural revenue in different rural origin prefectures because their baseline crop portfolios differed. The authors isolate innovations in crop prices outside China, weight them by potential crop revenue, and aggregate them over 2000–2005 [E1, §I.B; E2, Appendix C]. FAO confirms the annual farm-gate price and potential-yield data families, but the precise historical dataset vintages and author transforms were not recreated here [E3–E4, verified source identities].

## Implementation and Assignment

Earlier rural migrants from each origin had settled in different destination prefectures. The paper uses those pre-2000 shares to transmit origin income shocks to a destination-level predictor of migrant inflow. Every manufacturing establishment in a destination inherits the same predictor; firms are **not** assigned exposure by their own historical employee origins [E1, Equations 1–5]. Actual migrant inflows come from the 2005 survey's retrospective histories, corrected for missed return migration under an explicit model [E2, Appendix B.2]. The shock is therefore a constructed source of variation, not an observed policy date or directly measured firm-worker mix.

## Why This Creates Empirical Variation

The paper compares how firms in cities with different predicted inflows changed between 2000 and 2006, using the predictor as an instrument for actual destination immigration rates. Its baseline 2SLS weights by initial employment and clusters by destination prefecture [E1, Equation 5 and Table 3]. The study reports more labor-intensive production, lower value added per worker, and changes in product and patenting patterns. Those are paper estimates for its sample and assumptions, not universal consequences of rural migration.

## Identification Risks

The paper explicitly does **not** rely on historical settlement shares being random. It relies on origin shifts being plausibly exogenous and sufficiently dispersed, plus a restriction that crop-price shocks reach urban manufacturing principally through migration. Crops and origin geographies can be correlated, and crop prices can also change manufacturers' input costs or the purchasing power of rural customers. The authors test pretrends, old shocks, nearby routes, processors, market access, and alternative inference, but these checks do not turn the IV into a law of nature [E1, §§I.C, II.C; E2, Appendix C/F].

## Data Requirements

A faithful reuse needs the 2000 census's origin-destination migrant stocks, the 2005 survey's residence/registration/departure-year microdata and weights, the original price and crop-potential vintages, a stable prefecture crosswalk, and firm outcomes at both endpoints. Public NBS and FAO pages verify the existence of source families, not unrestricted access to the individual records or a ready-made instrument. Annual firm data alone cannot recreate the authors' destination-level exposure [E1–E5].

## Evidence Notes

This audit corrected three old distortions: the baseline instrument is destination-level rather than firm-specific; the origin shock uses international crop-price innovations rather than generic weather or pests; and the paper's main causal comparison is a 2000-to-2006 first difference, not an annual firm event study. Grounded means the identity, source families, treatment, join, comparison, and limits are recoverable. It does **not** certify the exact raw-data reconstruction or the IV exclusion restriction.
