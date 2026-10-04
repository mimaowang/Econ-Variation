---
schema_version: 2
id: china-neighboring-capital-imports-spatial-spillover
name: Neighboring Capital Imports and Non-Importer Productivity in China (2000–2006)
aliases:
- Mo Zhang neighboring capital imports
- geocoded manufacturing firms China import spillover
- 邻近企业资本品进口 空间溢出
status: contested
provenance:
  task_id: task-b3d7c21b1d74
scope:
  country: China
  regions:
  - Chinese prefecture-level cities and the manufacturing firms located within them
  domains:
  - trade
  - urban
  - regional-economics
  - economic-geography
  - spatial-economics
  - manufacturing
  - productivity
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    The paper constructs a China-specific firm-to-firm spatial exposure: a non-importer's
    lagged exposure to capital-goods imports by nearby firms. It is useful for regional
    spillover and network research, but it is not an administratively assigned policy
    shock. Import decisions and firm locations are endogenous; the paper's causal
    interpretation is conditional on a local-spatial-exclusion IV assumption.
identity:
  instrument: >
    A constructed neighboring-import exposure based on Chinese manufacturing firms'
    capital-goods imports, with a baseline neighbor defined as a firm within 10 km and
    the same prefecture-level city as a non-importer. The paper instruments this exposure
    with capital-import density in 10–20 km and 20–30 km rings.
  authority: >
    The underlying observations come from China's National Bureau of Statistics Annual
    Survey of Industrial Enterprises and transaction-level customs records maintained by
    the General Administration of Customs. The 10 km network rule and IV are research
    constructions, not government eligibility rules.
  legal_identifiers:
  - Annual Survey of Industrial Enterprises (ASIE), 2000–2006
  - General Administration of Customs transaction-level customs data, 2000–2006
  - Broad Economic Categories (BEC) concordance with HS96/HS02
  implementation_regime: >
    The exposure is observed in an annual firm panel from 2000 to 2006. Firms that never
    imported during the sample are the target population; the paper studies whether their
    productivity evolves differently when nearby firms import capital or intermediate
    goods. This is a market-network process rather than a phased policy rollout.
  assignment_mechanism: >
    For each non-importer-year, geographic coordinates and prefecture-level city
    membership define concentric neighbor sets. Prior-year import activity of those
    neighbors is converted into a capital/intermediate import indicator or density. The
    assignment is therefore a measured spatial network exposure, not exogenous treatment
    assignment.
  parent: null
  related_variations:
  - china-trade-migration-productivity
  - china-expressway-market-access-walled-city-mst
timeline:
  announcement: null
  effective: null
  implementation_start: 2000
  implementation_end: 2006
  local_timing: >
    A neighbor's import in year t−1 enters the non-importer's exposure in year t. The
    baseline radius is less than 10 km within the same prefecture-level city; 0–5,
    10–20, and 20–30 km rings are used as alternatives and instruments.
  anticipation: >
    Firms may anticipate trade opportunities and choose both location and import status.
    The one-year lag is intended to allow spillovers to operate over time, not to create
    an exogenous adoption date.
  last_verified: '2026-08-12'
assignment:
  unit: Non-importing manufacturing firm-year
  treated: >
    A non-importer-year with at least one neighboring firm that imported capital goods in
    the preceding year, or with a positive lagged density of such neighbors. Capital and
    intermediate import exposures are coded separately.
  comparison_pool: >
    Non-importers with no prior-year capital-import neighbor, or with lower neighboring
    importer density, within the same observed firm panel. A zero-neighbor observation is
    not automatically a clean control because firms with no measured neighbors are
    excluded from the main sample and spatial sorting remains possible.
  rule: >
    Geocode each ASIE firm from company name and registration address; use a great-circle
    distance and retain neighbors within 10 km and the same prefecture-level city. Join
    annual GAC imports to ASIE firms, classify products through HS96/BEC before 2002 and
    HS02/BEC from 2002 onward, and lag the neighbor import measure one year. Alternative
    rings and the 10–20 km and 20–30 km densities are kept as separate variables.
  intensity: >
    Binary exposure or log density, ln(1 + 100 × neighboring importers / all measured
    neighbors), separately for capital and intermediate goods. Importer size, upstream or
    downstream position, and distance bands provide additional heterogeneity measures.
  exemptions:
  - Firms that import during any sample year are outside the never-importer target group
  - Firms with no measured neighbor within 10 km are excluded from the main analysis
  - Firms with longitude/latitude repeated at least 10 times are excluded as likely
    imprecisely geocoded
  compliance: >
    There is no policy compliance margin. Importing reflects firm choices, market access,
    productivity, and local conditions; the IV is intended to address part of this
    endogeneity, not to turn the exposure into a government-assigned treatment.
  exposure_construction: >
    Merge the ASIE firm-year panel with annualized GAC transactions, first by firm name
    and year and then using contact information such as telephone and postal code. Map
    ASIE registration addresses with Amap; retain a flag for precise versus city-centroid
    geocodes. Build firm-to-firm distances within prefecture-level cities, classify HS
    products with the UN BEC concordances, and create lagged neighbor indicators/densities
    and ring instruments. Keep encrypted replication identifiers distinct from original
    NBS/GAC identifiers.
  required_identifiers:
  - firm identifier
  - calendar year
  - prefecture-level city identifier
  - longitude and latitude or geocode-quality flag
  - ASIE product description and industry code
  - GAC firm match and HS product code
  - BEC concordance version
  spillovers: >
    The exposure is itself a spatial spillover. Upstream and downstream suppliers may
    transmit imported-input gains; neighboring firms can also share local shocks, labor,
    customers, and policy environments. Treating nearby firms as unaffected controls is
    therefore inappropriate.
research_compatibility:
  outcome_domains:
  - firm productivity
  - manufacturing growth
  - spatial spillovers
  - supply-chain linkages
  - technology adoption
  - regional productivity
  affected_populations:
  - Chinese manufacturing firms that never import in the sample
  - neighboring importing firms and their suppliers/customers
  - workers and local production networks around the firms
  mechanism_channels:
  - upstream supply-chain spillovers
  - downstream demand and quality spillovers
  - local learning and technology diffusion
  - spatial agglomeration
  - imported-capital embodied technology
  best_for:
  - Firm-level regional spillover designs with geocoded Chinese manufacturing data
  - Separating capital-input and intermediate-input spatial effects
  - Network and distance-decay diagnostics when the researcher can reproduce the joins
  - Studying how trade shocks propagate beyond direct importers
  not_good_for:
  - A clean policy-treatment or randomized-shock design
  - City-level treatment coding that ignores within-city firm locations
  - Designs that treat the 10 km boundary as a legal cutoff
  - Replication using only public aggregate trade data
design:
  claim_type: causal
  affordances:
  - Geocoded firm-to-firm exposure within prefecture-level cities
  - Separate capital and intermediate import measures
  - Lagged exposure and concentric-ring distance decay
  - Neighbors'-neighbors IV construction
  - Upstream/downstream supply-chain heterogeneity
  candidate_designs:
  - Production-function estimation with a productivity-evolution equation
  - Spatial spillover IV using 10–20 km and 20–30 km import rings
  - Distance-decay and placebo-ring tests
  - Supply-chain position and importer-size heterogeneity
  identifying_variation: >
    Conditional variation comes from differences across non-importing firms and years in
    the prior-year import activity of geographically nearby firms. The paper's IV uses
    more distant ring imports to predict within-10-km neighbor imports, relying on local
    rather than global spatial correlation of productivity shocks.
  primary_strategy: >
    Estimate production functions and a Markov productivity process for non-importers,
    then use lagged neighbor capital/intermediate import indicators or densities. The IV
    specification instruments the within-10-km density with 10–20 km and 20–30 km ring
    densities; it should be reported as conditional on the spatial exclusion assumption.
  estimand: >
    The conditional effect of a prior-year neighboring capital or intermediate import
    exposure on productivity of never-importing Chinese manufacturing firms, for exposure
    induced through the specified spatial network and under the stated IV assumptions.
  treatment_variable: >
    n^capital_{j,t−1} and n^intermediate_{j,t−1} indicators, or log neighbor-import
    densities within 10 km and the same prefecture-level city; ring densities are stored
    separately as instruments and diagnostics.
  comparison_logic: >
    Compare non-importers with different measured local network exposure while holding
    firm production inputs and observed characteristics in the production-function design.
    The comparison is not treated city versus untreated city and does not remove common
    local shocks by proximity alone.
  estimation_notes: >
    The published design uses alternative production-function estimators and a lagged
    productivity evolution process. It reports positive capital-import spillovers and no
    clear intermediate-import spillover, with distance decay beyond 10 km. Those are
    source-reported estimates, not a claim that importer choices are exogenous.
  assumptions:
  - Conditional on controls and lagging, neighboring import decisions are not driven by
    the target firm's current productivity shock
  - Productivity shocks are sufficiently local that 10–20 km and 20–30 km imports do not
    directly affect the target firm's productivity
  - Distant imports still predict nearby import decisions strongly enough for a first stage
  - ASIE–GAC matching, geocoding, prefecture boundaries, and BEC classification are valid
  - The production-function and productivity-transition specification is appropriate
  diagnostics:
  - Report first-stage strength and the quasi-first-stage checks
  - Plot distance decay and test 0–5, 10–20, and 20–30 km rings
  - Vary the repeated-coordinate exclusion threshold and geocode precision
  - Compare capital, intermediate, processing-trade, and placebo exposures
  - Test upstream/downstream and importer-size heterogeneity
  - Inspect pre-period productivity and local policy/technology shocks
threats:
- type: endogenous-importer-location-and-choice
  basis: reported
  condition: >
    Firms choose where to locate and whether to import. Local productivity, policy,
    infrastructure, and market access can jointly affect imports and non-importer outcomes.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - firm and industry controls and lagged exposure
  - pre-period balance and placebo exposures
  - alternative production-function estimators
- type: spatial-exclusion-IV
  basis: reported
  condition: >
    The ring IV assumes that productivity shocks are sufficiently local: imports 10–20 km
    or 20–30 km away may affect nearby importers but have no direct effect on the target
    non-importer. The paper motivates and tests this with distance decay, but the claim is
    not an institutional guarantee.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - ring-specific reduced forms and first stages
  - placebo outcomes and alternative ring widths
  - controls for local policy, industry, and spatial trends
- type: geocoding-and-boundary-measurement
  basis: reported
  condition: >
    Amap can return a city centroid when a precise address match fails; repeated coordinates
    are removed, and GCJ-02 offsets and changing prefecture boundaries can still misclassify
    10 km neighbors.
  evidence_refs:
  - E2
  possible_diagnostics:
  - geocode-quality flags and alternative duplicate thresholds
  - precise-coordinate subsamples
  - alternative radii and stable boundary crosswalks
- type: proprietary-data-and-match-selection
  basis: documented
  condition: >
    Original ASIE and GAC firm-level identifiers are proprietary. The replication package
    supplies anonymized IDs and essential variables, so a public user cannot independently
    re-create the original firm match or audit every excluded observation.
  evidence_refs:
  - E3
  - E4
  possible_diagnostics:
  - compare encrypted replication outputs with reported tables
  - document access approvals and matching validation when original data are obtained
  - retain a match-quality and sample-attrition report
empirical_requirements:
  contract_version: 1
  population: Chinese ASIE manufacturing firms, focusing on firms that never import during 2000–2006
  observation_unit: Firm-year
  geography_level: Firm location within prefecture-level city
  time_start: 2000
  time_end: 2006
  minimum_frequency: annual
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - firm output and value added
  - labor, capital, and intermediate inputs
  - ownership and two-digit industry
  - ASIE firm name, address, phone, postal code, and product descriptions
  - GAC annual import transactions, HS product codes, values, and trade mode
  - longitude, latitude, prefecture-level city, and geocode quality
  - HS96/BEC and HS02/BEC concordances
  required_identifiers:
  - firm ID
  - year
  - prefecture-level city ID
  - ASIE–GAC match key
  - longitude and latitude
  - HS/BEC product code
  treatment_key:
  - target firm ID
  - year t
  - neighbor firm IDs within 10 km and same prefecture-level city
  - neighbor import year t−1
  - capital/intermediate BEC class
  - 10–20 km and 20–30 km ring densities
  treatment_source: >
    ASIE maintained by NBS and transaction-level GAC customs data, joined as in the paper;
    UN HS–BEC concordance tables for product classification; Amap geocoding for firm
    coordinates; Mendeley replication materials for anonymized verification outputs.
  measurement_risks:
  - proprietary firm identifiers prevent a fully public match audit
  - city-centroid fallback and GCJ-02 coordinates affect short distances
  - repeated-location exclusions alter the target sample
  - ASIE coverage is limited to SOEs and non-SOEs above the sales threshold
  - HS96/HS02 concordance and NLP product matching may misclassify inputs
  - prefecture boundaries and firm legal entities can change over time
design_profiles: []
evidence:
- id: E1
  source_type: paper
  citation: 'Mo, Jiawei, and Zhe Zhang. 2024. "Neighboring capital imports and non-importer productivity: Evidence from geocoded manufacturing firms in China." Journal of Urban Economics 143:103692. DOI: 10.1016/j.jue.2024.103692.'
  url: https://doi.org/10.1016/j.jue.2024.103692
  date: 2024
  supports:
  - identity.instrument
  - identity.implementation_regime
  - timeline.implementation_start
  - timeline.implementation_end
  - timeline.local_timing
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design_applications.treatment_encoding
  - design_applications.comparison
  verification_status: verified
  access_level: abstract
  locator: 'ScienceDirect article page and abstract; article metadata, JEL codes, sample period, 10 km exposure, distant-firm IV, and reported 0.99% estimate.'
- id: E2
  source_type: paper
  citation: 'Mo, Jiawei, and Zhe Zhang. 2024. Author-available full text of "Neighboring capital imports and non-importer productivity: Evidence from geocoded manufacturing firms in China."'
  url: https://www.researchgate.net/publication/383497261_Neighboring_capital_imports_and_non-importer_productivity_Evidence_from_geocoded_manufacturing_firms_in_China
  date: 2024
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - assignment.rule
  - assignment.exposure_construction
  - assignment.required_identifiers
  - design.identifying_variation
  - design.primary_strategy
  - design.assumptions
  - design.diagnostics
  - threats.condition
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_key
  - design_applications.data_used
  - design_applications.treatment_encoding
  verification_status: verified
  access_level: full-text
  locator: 'Sections 2.1–2.2 (ASIE/GAC merge, Amap geocoding, distance and BEC rules); Section 3 (lagged exposure); Section 4.3 and Figure 2/Table 5 (ring IV and exclusion assumption); Sections 5–6 (mechanisms and quantification).'
- id: E3
  source_type: replication
  citation: 'Mo, Jiawei, and Zhe Zhang. 2024. Replication package for "Neighboring capital imports and non-importer productivity: Evidence from geocoded manufacturing firms in China." Mendeley Data, version 1. DOI: 10.17632/v7rgtb6kwc.1.'
  url: https://data.mendeley.com/datasets/v7rgtb6kwc/1
  date: 2024
  supports:
  - empirical_requirements.treatment_source
  - design_applications.data_used
  verification_status: verified
  access_level: replication
  locator: 'Mendeley Data landing page: version 1, 15 August 2024; package description says code and data reproduce the paper and appendix; categories include Urban Economics, International Trade, and Productivity.'
- id: E4
  source_type: replication
  citation: 'Mo, Jiawei, and Zhe Zhang. 2024. Replication README for "Neighboring capital imports and non-importer productivity: Evidence from geocoded manufacturing firms in China."'
  url: https://prod-dcd-datasets-public-files-eu-west-1.s3.eu-west-1.amazonaws.com/c6d371e3-73e1-4198-b392-e3b8a6392602
  date: 2024
  supports:
  - empirical_requirements.treatment_source
  - empirical_requirements.measurement_risks
  - design_applications.data_used
  - threats.condition
  verification_status: verified
  access_level: full-text
  locator: 'Replication README, pp. 1–2: ASIE and Customs data are proprietary; anonymized firm/city/province IDs and essential variables are shared; original data require NBS and GAC access; package structure and computational requirements.'
- id: E5
  source_type: policy-document
  citation: 'General Administration of Customs of the People''s Republic of China. Regulations of the People''s Republic of China on Customs Statistics, effective 1 March 2006.'
  url: https://english.customs.gov.cn/statics/55dd0995-11de-4e05-a7e3-0dd5c4364f27.html
  date: 2006
  supports:
  - identity.authority
  - assignment.required_identifiers
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  verification_status: verified
  access_level: official-document
  locator: 'Articles 2, 6–10 and 15–17: official customs statistical mandate, recorded product codes, values, trading enterprises, trade regime, dates, and domestic locations.'
- id: E6
  source_type: other
  citation: 'United Nations Statistics Division. Correspondence tables between HS and Broad Economic Categories.'
  url: https://unstats.un.org/unsd/trade/classifications/correspondence-tables.asp
  date: 2024
  supports:
  - assignment.rule
  - assignment.exposure_construction
  - empirical_requirements.required_fields
  verification_status: verified
  access_level: metadata
  locator: 'UN Statistics Division correspondence-table page cited by the paper for HS96/BEC and HS02/BEC product classification.'
design_applications:
- paper: 'Neighboring capital imports and non-importer productivity: Evidence from geocoded manufacturing firms in China'
  doi: 10.1016/j.jue.2024.103692
  journal: Journal of Urban Economics
  year: 2024
  research_question: How do nearby firms' capital and intermediate imports affect productivity of Chinese manufacturing firms that never import?
  population: 301,419 non-importing manufacturing firms and 928,789 observations in the 2000–2006 ASIE-based panel, after the paper's sample exclusions
  outcome: Revenue-based productivity, value added per worker, R&D participation, and productivity growth of non-importers
  data_used:
  - National Bureau of Statistics Annual Survey of Industrial Enterprises, 2000–2006
  - General Administration of Customs transaction-level data, 2000–2006
  - Amap company/address geocoding
  - UN HS–BEC correspondence tables
  - Mendeley replication package with anonymized identifiers and essential variables
  treatment_encoding: >
    A lagged dummy or log density of neighboring firms importing capital or intermediate
    goods within 10 km and the same prefecture-level city; 10–20 km and 20–30 km ring
    import densities serve as IVs for the within-10-km density.
  comparison: >
    Never-importing firms with different prior-year neighbor-import exposure, within the
    production-function and productivity-transition sample; not a city-level untreated
    comparison.
  empirical_design: >
    Production-function estimation with a productivity-evolution process, alternative
    estimators, distance-decay tests, supply-chain heterogeneity, and a neighbors'-neighbors
    IV specification.
  assumptions:
  - lagged neighbor imports are not driven by the target firm's current productivity shock
  - distant ring imports have no direct productivity effect on the target firm
  - distant imports predict nearby imports
  - data matching, geocoding, product classification, and production-function measures are valid
  threats_addressed:
  - local-spatial endogeneity through lagging and ring IVs
  - direct-distance spillovers through ring estimates and distance decay
  - input-classification concerns through HS/BEC concordances and alternative measures
  - supply-chain mechanisms through upstream/downstream interactions
  evidence_refs:
  - E1
  - E2
  - E3
  - E4
  - E6
readiness_blockers:
- This is a constructed, endogenous market-network exposure rather than an externally assigned policy shock; retain it as contested until the admissibility boundary for such exposures is explicitly accepted.
- The ring IV depends on a local spatial-exclusion assumption. Distance decay and placebo checks do not prove that 10–20 km or 20–30 km imports have no direct effect.
- Original ASIE and GAC firm identifiers and the exact matching process are proprietary; the public replication package uses anonymized IDs and cannot provide a complete external match audit.
- Amap city-centroid fallback, repeated-coordinate exclusions, GCJ-02 offsets, and historical prefecture boundaries can change 10 km neighbor assignment.
method_transfer: null
superseded_by: null
deprecation_reason: null
---
## Institutional Background

The paper studies a market network inside China's manufacturing sector, not a new legal program. The underlying panel is the National Bureau of Statistics Annual Survey of Industrial Enterprises (ASIE) from 2000–2006, merged with transaction-level customs data from the General Administration of Customs. ASIE covers state-owned enterprises and non-state-owned enterprises above the paper's sales threshold and includes addresses and product descriptions; customs transactions provide firm-level import products, values, and trade modes [E2]. The official customs framework establishes what customs statistics record, but it does not assign firms to the paper's neighbor treatment [E5].

## What Changed

Nothing changed by a common announcement date. Instead, a non-importing firm's local production network changes when nearby firms import capital or intermediate goods. The paper's baseline neighbor is within 10 km and the same prefecture-level city. It distinguishes capital goods (BEC 41 and 521) from intermediate goods and uses the HS96/BEC concordance before 2002 and HS02/BEC from 2002 onward [E2; E6].

## Implementation and Assignment

The research team geocodes ASIE firms using company name and registration address through Amap. A precise coordinate is used when available; otherwise the city center is returned, and firms with coordinates repeated at least ten times are excluded as likely imprecise [E2]. ASIE and customs observations are joined using firm names and then contact information such as postal codes and telephone numbers. For a non-importer j in year t, the exposure is the import activity of firms within 10 km and the same prefecture-level city in t−1. A binary indicator and a log density are both used; 10–20 km and 20–30 km rings remain separate rather than being silently folded into the baseline [E2].

This is a measured network exposure. Importers choose locations and import decisions, and local productivity shocks may affect both importers and non-importers. The comparison is consequently between non-importers with different measured neighbor exposure, not between cities assigned by a government rule. The public replication package preserves the code and anonymized variables but not the original firm-identifying data [E3; E4].

## Why This Creates Empirical Variation

The design exploits firm-level spatial variation in the lagged composition of nearby importers. The productivity equation allows capital and intermediate neighbor exposure to affect the transition of non-importer productivity, and the paper reports stronger effects for capital imports and for upstream or downstream neighbors. To address serially correlated local shocks, it instruments within-10-km neighbor import density with import density in the 10–20 km and 20–30 km rings [E1; E2].

The IV logic is conditional: distant firms may influence a nearby importer while not directly affecting the target non-importer. The paper motivates this with distance decay and reports ring results, but this is an identifying assumption rather than an institutional fact. The useful object for a new study is therefore the complete network exposure contract and its diagnostics, not an unsupported claim that neighboring imports are exogenous [E2; analytical inference].

## Identification Risks

Importer location, import participation, industry, and local policy are jointly selected. A city-centroid fallback can create false neighbors, while duplicate-coordinate exclusions alter the target sample. The ASIE–GAC match uses contact information and the original identifiers are proprietary, so selection and measurement cannot be fully audited from public files [E2; E4].

The central IV threat is direct spatial correlation beyond 10 km. A productivity or infrastructure shock can affect firms throughout a labor market, so the absence of a significant coefficient in an outer ring does not by itself prove exclusion. The outcome is revenue-based productivity, and supply-chain position, importer size, product matching, and prefecture boundaries can all change the interpretation [E1; E2; analytical inference].

## Data Requirements

Replication requires an annual firm panel with stable firm and prefecture identifiers, production inputs and outcomes, ASIE addresses and product descriptions, annual GAC transactions and HS codes, a documented ASIE–GAC match, geocodes with quality flags, and HS96/BEC and HS02/BEC concordances. The treatment key must retain target firm, year, neighbor firm set, lagged import class, distance band, and prefecture-level city. The Mendeley package is useful for checking code and anonymized outputs; the original NBS/GAC data are needed for a full identifier-level audit [E3; E4].

## Evidence Notes

E1 is the publisher article record and establishes the paper's China setting, 10 km exposure, distant-firm IV, headline estimates, and journal publication; its public page is an abstract/article-preview route and does not make the proprietary microdata open. E2 is the inspectable author-available full text and establishes the data merge, geocoding fallback, BEC coding, lagged rule, ring IV, and reported limitations; it does not turn the market exposure into an externally assigned shock. E3 establishes the existence and scope of the replication package. E4's README establishes that original ASIE and customs identifiers are proprietary and that the shared package is anonymized; it does not validate the original firm match. E5 grounds the official customs-data institution and recorded fields, but it does not establish the 10 km neighbor rule. E6 is the classification source cited by the paper and supports product-code conversion, not causal identification.

The record is therefore preserved as a contested China spatial-exposure case: it is valuable for regional/network spillover work and for a reproducible data contract, while its causal interpretation remains conditional and it must not be presented as a policy shock or a clean exogenous treatment.
