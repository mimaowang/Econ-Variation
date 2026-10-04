---
schema_version: 2
id: china-industrial-parks-edge-city-spillovers
name: Chinese Industrial-Park Openings and Within-City Edge-City Spillovers (1998–2013)
aliases:
- Zheng Sun Wu Kahn edge cities China
- industrial parks policy local spillovers China
- 中国工业园区 边缘城市 溢出
status: grounded
provenance:
  task_id: task-93d2286f8e4a
scope:
  country: China
  regions:
  - Beijing
  - Shanghai
  - Shenzhen
  - Tianjin
  - Dalian
  - Wuhan
  - Xi'an
  - Chengdu
  domains:
  - urban
  - regional-economics
  - economic-geography
  - infrastructure
  - manufacturing
  - productivity
  - housing
  - trade
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    The case uses formal national- and provincial-level industrial-park openings in eight
    Chinese cities to study a distinctly within-city regional exposure: plants inside a
    park, incumbent plants near its boundary, and housing and retail grids near the new
    production sub-center. It is a place-based policy and spatial spillover design, not a
    claim that park locations were randomly assigned.
identity:
  instrument: >
    Staggered establishment of national- and provincial-level industrial parks and their
    geocoded boundaries in eight major Chinese cities. The paper's additional location IV
    uses pre-policy land development, historical population density, Communist/public land
    use, and terrain to instrument whether a within-city zone receives a park.
  authority: >
    Central and provincial governments formally approved qualifying parks; local governments
    assembled land and park administrative committees recruited firms. The NDRC/MNR/Construction
    Ministry 2006 directory and Ministry of Land and Resources boundary notices provide the
    institutional and spatial source, while the within-city IV is a research construction.
  legal_identifiers:
  - China Development Zone Review and Announcement Directory (2006 edition)
  - Ministry of Land and Resources official boundary announcements
  - National- and provincial-level industrial-park approval/establishment records
  implementation_regime: >
    The eight-city sample contains national- and provincial-level parks with preferential
    land, tax, credit, tariff, and regulatory arrangements. The study period overlaps the
    fourth park-building wave (1996–2008), while older parks remain in the panel to compare
    maturity and diminishing returns. Lower-level unapproved zones are not silently pooled
    with these qualifying parks.
  assignment_mechanism: >
    A plant is exposed when its zone or small-zone centroid lies within an official park
    boundary in a year when that park exists. Outside plants receive a continuous exposure
    through road-network distance to the closest existing park. For zone-park location
    selection, low historical land-conversion cost and flat terrain predict where local
    leaders can assemble a park; the exclusion restriction requires those cost shifters not
    to predict later productivity potential except through park placement.
  parent: null
  related_variations:
  - china-industrial-park-political-connection-rotation
  - china-expressway-market-access-walled-city-mst
timeline:
  announcement: null
  effective: null
  implementation_start: 1998
  implementation_end: 2013
  local_timing: >
    Manufacturing plants are observed annually from 1998–2007; park openings are coded by
    establishment year, with 27 parks established during 1998–2006 in the location models.
    Housing and retail outcomes run from 2006–2013. Parks established before 1996 are the
    old cohort and those established in or after 1996 are the new cohort. The published
    abstract reports 110 parks, whereas the inspectable working paper's data section and
    GIS construction report 120; retain both counts until the final article appendix or
    underlying list resolves the discrepancy.
  anticipation: >
    Mayors and firms could anticipate proposed park construction and recruitments. The
    authors inspect incumbent-plant pre-trends, but approval, land assembly, construction,
    and operation need not share one date. Use establishment year as the paper's treatment
    timing and preserve proposal or construction dates when recovered.
  last_verified: '2026-08-12'
assignment:
  unit: Plant-year, park-zone-year, and 2 km × 2 km city grid cell-month depending on outcome
  treated: >
    For plant outcomes, a plant is treated when its zone/small-zone centroid lies inside a
    park boundary after the park exists; an outside plant receives a continuous treatment
    according to road-network distance to the closest park and the city's other park
    employment. For housing and retail, a grid cell is more exposed when it lies closer to
    a park boundary or its workers' new consumption center after opening.
  comparison_pool: >
    Plants outside park boundaries in the same city, including incumbent plants before and
    after a nearby opening; grid cells farther from the closest park but comparable in
    distance to the CBD; and zone-park pairs within the same city for the site-selection
    model. Plants near other parks may be indirectly treated and should not be treated as
    universally clean controls.
  rule: >
    Geocode the official park boundary and plant address into a common city GIS. Set
    PARK_ij to one when plant i's small-zone (or zone) centroid falls inside park j's
    boundary, and AFTER_jt to one in years after park j exists. For outside plants compute
    road-network distance to the closest existing park and a separate global impact of all
    other parks. For housing and retail, assign observations to 2 km × 2 km grid cells and
    retain distance to the CBD, closest park, and park employment.
  intensity: >
    Binary inside-park exposure, log distance to the closest park, quadratic distance-decay
    weights for other parks' employment, park age/cohort, park human capital, FDI share,
    SOE share, size, and co-agglomeration. The location IVs are shares of developed land in
    1980, population density in 1982, Communist/public land in 1980, and flat land below
    15 degrees slope.
  exemptions:
  - Four waves before 1996 are grouped as old parks rather than a single opening cohort
  - Parks without a formal national/provincial listing or boundary are outside the canonical sample
  - Small zones without identifiers use zone centroids and have coarser spatial assignment
  - Shenzhen and Xi'an are omitted from specifications requiring 1982 population-density IV data
  compliance: >
    A formal park boundary does not ensure construction, firm entry, or operation on the
    establishment date. Park administrative committees negotiate incentives with entrants,
    so within-park firm composition is partly selected after treatment.
  exposure_construction: >
    Reconcile the official directory name/location/year to city park administrative committee
    boundary maps and land-use drawings. Geocode plants from ASIF addresses, village or
    township codes, and historical name crosswalks; merge plants to park polygons or
    centroid-based zones. Build annual park employment, human capital, FDI, SOE share, and
    industry co-agglomeration, then join housing-authority complexes and Dianping retail
    establishments to common 2 km grids.
  required_identifiers:
  - park directory code and name
  - park boundary polygon and centroid
  - city, district, zone, and small-zone codes
  - plant identifier and year
  - plant address or village/township code
  - housing complex or retail establishment coordinates and date
  spillovers: >
    Parks can attract firms from elsewhere in the city, raise local wages and employment,
    and induce nearby housing and retail. A close outside plant may benefit through
    agglomeration, while a distant area may lose activity; the design estimates local and
    network effects rather than a citywide total by default.
research_compatibility:
  outcome_domains:
  - plant TFP and survival
  - manufacturing employment and wages
  - housing transactions and prices
  - retail and restaurant entry
  - urban subcenter formation
  - agglomeration and regional productivity
  affected_populations:
  - manufacturing plants inside and near parks
  - workers and households near new production centers
  - housing developers and retail establishments
  - competing locations elsewhere in the city
  mechanism_channels:
  - input sharing and labor pooling
  - knowledge and technology spillovers
  - land assembly and preferential incentives
  - local wage and employment growth
  - residential and consumer-market response
  - industrial co-agglomeration
  best_for:
  - Within-city spatial spillovers of Chinese place-based industrial investment
  - Separating selection of productive firms into parks from incumbent-plant effects
  - Linking manufacturing shocks to housing and retail edge-city formation
  - Testing heterogeneous effects by park age, human capital, FDI, SOE share, and synergy
  not_good_for:
  - A national average treatment effect across all Chinese development zones
  - Treating a 2 km boundary or park centroid as an exogenous geographic cutoff
  - Ignoring park recruitment and residential/retail spillovers
  - Extending the 1998–2007/2006–2013 sample to later waves without a new park list
design:
  claim_type: causal
  affordances:
  - Staggered park openings with inside/outside and distance-to-park exposure
  - Plant fixed effects and district-year/industry-year controls
  - Historical land-cost and terrain instruments for within-city location
  - 2 km grid outcomes linking jobs, housing, and retail
  - Old/new park cohorts and park-level composition heterogeneity
  candidate_designs:
  - Plant-level DID of park×post exposure
  - Incumbent-plant fixed-effects distance-gradient design
  - Zone-park conditional-logit location model
  - Historical land-cost IV for park placement
  - Grid-cell event study for housing and retail near parks
  identifying_variation: >
    The main variation is the staggered appearance of a qualifying park in a precise city
    location, creating a boundary and distance gradient for incumbent plants and nearby
    grid cells. The location IV uses pre-policy land use, historical population density,
    Communist/public land, and slope to predict low-cost sites; its validity is conditional
    on those measures affecting later outcomes only through park placement.
  primary_strategy: >
    Estimate plant-level DID with park-inside and park-after indicators, plant fixed effects
    for incumbent plants, and district-year and industry-year controls. For outside plants,
    estimate the TFP gradient in distance to the closest park while controlling for distance
    to the CBD and global impact of other parks. Instrument park location with the historical
    land-cost variables in zone-park models and the within-park TFP specification. Use grid
    cell outcomes for housing and retail to trace the edge-city chain reaction.
  estimand: >
    The conditional local effect of a qualifying industrial-park opening on incumbent and
    nearby plant productivity, employment, housing, and retail outcomes in the eight-city
    sample, and the effect of moving a park to a lower historical land-cost location under
    the stated IV exclusion assumption.
  treatment_variable: >
    PARK_ij × AFTER_jt for inside plants; log road-network distance to the closest existing
    park and global park impact for outside plants; grid distance and park exposure for
    housing/retail; historical land-use, population, and terrain variables as location IVs.
  comparison_logic: >
    Inside-park comparisons use incumbent plants before and after an opening where possible;
    outside-plant comparisons use distance gradients and city/district/industry controls.
    The IV compares zones with different historical conversion costs within the same city,
    not parks randomly placed across China. Housing and retail comparisons are grid cells
    at different park distances after accounting for CBD distance and city trends.
  estimation_notes: >
    The paper reports a within-park TFP premium, a negative distance gradient for nearby
    plants, and housing/retail responses around parks; old parks have stronger spillovers
    than new parks. The working paper reports 120 parks, while the published abstract says
    110. Preserve the source-reported estimates and do not resolve the count by inference.
  assumptions:
  - Park establishment timing is measured consistently and pre-trends are not driven by
    unobserved local treatment anticipation
  - Plant fixed effects and spatial controls absorb selection into park locations sufficiently
  - Historical land and terrain variables predict location cost but not later productivity
    potential except through the park
  - Plant, boundary, housing, and retail geocoding is accurate enough for the chosen distance
  - Local spillovers and activity relocation are compatible with the estimand
  diagnostics:
  - incumbent-plant pre-trend and event-time plots
  - plant fixed effects and alternative zone/small-zone centroid definitions
  - first-stage strength and overidentification sensitivity for location IVs
  - alternative park cohorts, radii, distance metrics, and CBD controls
  - placebo openings and outcomes in areas too far from parks
  - separate firm entry, incumbent survival, housing, and retail margins
threats:
- type: endogenous-within-city-location
  basis: reported
  condition: >
    Mayors choose locations based on land costs, existing industry, infrastructure,
    university access, and expected future productivity. The IV exclusion requires more than
    a first stage: historical land use and slope must not proxy persistent productivity.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - historical outcome balance and pre-trends
  - city fixed effects and predetermined access controls
  - alternative IV sets and zone-park choice models
- type: recruitment-and-selection
  basis: reported
  condition: >
    Park administrative committees recruit productive firms and negotiate incentives, so a
    within-park premium mixes treatment with selective entry. Incumbent-plant fixed effects
    narrow the comparison but do not remove every location response.
  evidence_refs:
  - E2
  possible_diagnostics:
  - incumbent-only samples and plant fixed effects
  - firm entry/exit and pre-existing plant tests
  - separate inside, near, and far exposure
- type: timing-and-anticipation
  basis: documented
  condition: >
    The directory establishment year, construction, recruitment, and operation may differ;
    incumbent firms may adjust before the listed year. Housing and retail outcomes begin in
    2006, so they cover a different event window from manufacturing outcomes.
  evidence_refs:
  - E2
  - E3
  possible_diagnostics:
  - event-time leads and lags
  - local construction and approval notices
  - alternative start dates and old/new cohort windows
- type: spatial-reallocation-and-spillover
  basis: reported
  condition: >
    Nearby firms, workers, housing, and shops can be attracted from elsewhere in the city;
    near parks are not untreated and citywide totals may not rise one-for-one with local
    gains.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - distance bands and global park impact
  - citywide employment and firm relocation accounting
  - neighboring-grid and housing-market spillovers
- type: historical-geocode-error
  basis: documented
  condition: >
    Park boundaries and plant addresses are hand-geocoded; pre-2004 village/township codes
    are reconstructed and small-zone centroids are coarser than plant coordinates. The
    resulting assignment error matters most near park boundaries and at short distances.
  evidence_refs:
  - E2
  - E4
  possible_diagnostics:
  - boundary audit and precise-address subsamples
  - alternative centroid and distance definitions
  - stable historical administrative crosswalks
empirical_requirements:
  contract_version: 1
  population: Manufacturing plants, housing complexes, and retail establishments in eight Chinese cities linked to 120 listed national/provincial parks
  observation_unit: Plant-year, zone-park pair, or 2 km × 2 km grid-cell month
  geography_level: Park polygon, district/zone/small-zone, and city grid
  time_start: 1998
  time_end: 2013
  minimum_frequency: annual for plants and parks; monthly for housing and retail where available
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields:
  - park code, name, level, city, establishment year, and polygon
  - plant ID, address, zone/small-zone code, output, inputs, employment, and ownership
  - plant industry and firm-linking variables
  - road-network distance to CBD and closest park
  - park employment, human capital, FDI share, SOE share, size, and co-agglomeration
  - 1980 developed-land and Communist/public-land shares
  - 1982 zone population density and terrain slope
  - housing complex coordinates, monthly price/sales, and physical attributes
  - retail establishment coordinates, category, and opening date
  required_identifiers:
  - park code
  - city/district/zone/small-zone code
  - plant ID and year
  - grid-cell ID and month
  treatment_key:
  - park code and establishment year
  - plant or grid location
  - inside-park indicator or distance to closest park
  - park age and annual employment
  - historical land-cost IV values
  treatment_source: >
    NDRC/MNR/Construction Ministry 2006 development-zone directory and MLR boundary notices;
    park administrative committee maps; NBS Annual Survey of Industrial Firms 1998–2007;
    local housing-authority transaction files 2006–2013; Dianping retail openings; GIS
    road-network and historical land/population/terrain sources.
  measurement_risks:
  - published 110 versus working-paper 120 park count discrepancy
  - establishment versus construction/operation timing
  - incomplete boundary polygons and hand-geocoded plant addresses
  - coarse small-zone centroids and reconstructed pre-2004 codes
  - ASIF sales threshold and firm exit/relocation misclassification
  - location-IV exclusion may fail if historical land use predicts later productivity
design_profiles: []
evidence:
- id: E1
  source_type: paper
  citation: 'Zheng, Siqi, Weizeng Sun, Jianfeng Wu, and Matthew E. Kahn. 2017. "The birth of edge cities in China: Measuring the effects of industrial parks policy." Journal of Urban Economics 100:80–103. DOI: 10.1016/j.jue.2017.05.002.'
  url: https://doi.org/10.1016/j.jue.2017.05.002
  date: 2017
  supports:
  - identity.instrument
  - identity.implementation_regime
  - timeline.implementation_start
  - timeline.implementation_end
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design_applications.treatment_encoding
  - design_applications.comparison
  verification_status: verified
  access_level: abstract
  locator: 'ScienceDirect/IDEAS article metadata and abstract: 110 parks, eight cities, localized productivity/wage/employment spillovers, housing and retail responses, and published DOI.'
- id: E2
  source_type: paper
  citation: 'Zheng, Siqi, Weizeng Sun, Jianfeng Wu, and Matthew E. Kahn. 2015. "The Birth of Edge Cities in China: Measuring the Spillover Effects of Industrial Parks." NBER Working Paper 21378.'
  url: https://www.nber.org/system/files/working_papers/w21378/w21378.pdf
  date: 2015
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - identity.implementation_regime
  - timeline.local_timing
  - assignment.rule
  - assignment.intensity
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
  locator: 'NBER Working Paper 21378, pp. 13–25 and Sections 3–5: eight-city GIS data, 120-park list/boundaries, 1996 cohort split, ASIF 1998–2007, housing/retail 2006–2013, geocoding, DID, distance gradients, land-cost IVs, and spillover diagnostics.'
- id: E3
  source_type: policy-document
  citation: 'National Development and Reform Commission, Ministry of Land and Resources, and Ministry of Construction. 2007. China Development Zone Review and Announcement Directory (2006 edition), Announcement No. 18.'
  url: https://www.ndrc.gov.cn/xxgk/zcfb/gg/200704/t20070406_961289_ext.html
  date: 2007
  supports:
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.announcement
  - assignment.rule
  - assignment.exposure_construction
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: official-document
  locator: 'NDRC official announcement and linked 2006 directory: reviewed/approved development zones, four-boundary determination, and prohibition on unreviewed zones.'
- id: E4
  source_type: implementation-document
  citation: 'Ministry of Land and Resources. 2006. Announcement No. 17: Ninth batch of development zones implementing four-boundary ranges.'
  url: https://policy.mofcom.gov.cn/claw/clawContent.shtml?id=12338
  date: 2006
  supports:
  - identity.legal_identifiers
  - assignment.exposure_construction
  - assignment.required_identifiers
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_key
  verification_status: verified
  access_level: official-document
  locator: 'Boundary announcement reproduced in the Ministry of Commerce legal database: text, coordinate, area, and boundary-shape verification for 144 provincial development zones.'
design_applications:
- paper: 'The birth of edge cities in China: Measuring the effects of industrial parks policy'
  doi: 10.1016/j.jue.2017.05.002
  journal: Journal of Urban Economics
  year: 2017
  research_question: Do industrial-park openings generate localized production spillovers and new residential and consumption subcenters within Chinese cities?
  population: Manufacturing plants in eight cities, housing complexes and retail establishments in those cities, and 120 listed national/provincial parks in the working-paper data construction
  outcome: Plant TFP, employment, wages and survival; housing prices and sales; retail, restaurant and entertainment openings
  data_used:
  - National Bureau of Statistics Annual Survey of Industrial Firms, 1998–2007
  - Official 2006 development-zone directory and park committee boundary maps
  - Local housing-authority complex transactions, 2006–2013
  - Dianping retail establishment openings, 2006–2013
  - GIS road-network, land-use, population-density, and terrain data
  treatment_encoding: >
    PARK_ij × AFTER_jt for a plant whose zone/small-zone centroid is inside park j after
    establishment; log road-network distance to the closest existing park and a global
    park-impact measure for outside plants; 2 km grid-cell distance and park exposure for
    housing and retail; historical land, population, Communist/public land, and slope
    variables as park-location instruments.
  comparison: >
    Incumbent plants inside versus before/after park opening, outside plants at different
    distances to the closest park within a city, and grid cells at different park distances
    conditional on CBD distance and city/spatial controls. Zone-park location models compare
    all zones in the same city for each of 27 new parks.
  empirical_design: >
    Plant DID and fixed effects, distance-gradient regressions with global park impact,
    zone-park conditional-logit location models, land-cost IV estimates, cohort/park-power
    heterogeneity, and grid-cell housing/retail spillover analyses.
  assumptions:
  - no differential anticipation that invalidates park-after timing
  - incumbent fixed effects and spatial controls address firm/location selection
  - historical land/population/terrain shifters affect outcomes through park location
  - geocoded park and plant joins are sufficiently accurate
  - local spillovers are part of the estimand and are not mistaken for citywide net growth
  threats_addressed:
  - selection into parks through incumbent samples and plant fixed effects
  - within-city location endogeneity through historical cost IVs and choice models
  - CBD and other-park confounding through distance-to-CBD and global park impact
  - spatial reallocation through distance gradients, housing, and retail outcomes
  evidence_refs:
  - E1
  - E2
  - E3
  - E4
readiness_blockers:
- The official directory grounds qualifying park identity and approval information, but the final article's complete 110-versus-120 reconciliation and machine-readable GIS boundary file are not independently reproduced here.
- Park administrative committee maps and hand-geocoded plant addresses require a boundary-level audit before a new user treats a near-boundary estimate as exact.
- 'The location IVs rely on an exclusion assumption: historical land use, population density, and slope may predict later productivity or infrastructure even after controls.'
- Housing and retail outcomes begin in 2006 and cannot be read as a balanced extension of the 1998–2007 manufacturing panel.
method_transfer: null
superseded_by: null
deprecation_reason: null
---
## Institutional Background

Chinese industrial parks are geographically bounded production areas with a management committee and preferential land, tax, credit, tariff, or regulatory treatment. The national and provincial parks in this case went through formal approval, while lower-level zones were treated differently during the post-2003 clean-up. The official 2006 development-zone directory records approved areas and their four-boundary arrangements, and the Ministry of Land and Resources published boundary coordinates and shapes for reviewed zones [E3; E4].

The paper examines how these place-based investments reshape the internal geography of a city. It follows eight large cities—Beijing, Shanghai, Shenzhen, Tianjin, Dalian, Wuhan, Xi'an, and Chengdu—rather than claiming that the sample represents every Chinese city. Its working-paper data section reports 120 qualifying parks; the final article abstract reports 110. Both numbers are preserved because they describe different publication stages and the directory/GIS reconciliation has not been independently re-run [E1; E2].

## What Changed

When a park is established, land is assembled and an administrative committee can recruit firms with preferential terms. A park may therefore create a new production center, raise wages and employment, and generate demand for housing and retail nearby. The paper separates the older parks established before 1996 from new parks established in or after 1996; the fourth wave (1996–2008) overlaps the manufacturing panel [E2].

The treatment date in the empirical contract is the park's recorded establishment year. It is not automatically the date of approval, construction completion, first firm entry, or full operation. Those dates should remain separate if local notices or park records make them recoverable.

## Implementation and Assignment

The research team digitized park boundaries from the official list, park administrative committee maps, land-use drawings, and local contacts. It geocoded ASIF manufacturing plants using addresses and village/township identifiers, reconstructing earlier codes when necessary. A plant is inside a park when its small-zone or zone centroid falls within the park polygon; plants outside are assigned a road-network distance to the closest existing park. Housing complexes and retail establishments are geocoded to 2 km × 2 km grid cells [E2].

For the site-selection model, the paper studies 27 parks established from 1998–2006 and matches each park to all zones in its city. Four location shifters—developed-land share in 1980, population density in 1982, Communist/public land share in 1980, and flat land below 15 degrees slope—predict the cost of assembling a park. The IV is valid only if these historical cost measures do not also predict later productivity or infrastructure through another channel [E2; analytical inference].

## Why This Creates Empirical Variation

The staggered appearance of parks gives a plant-level before/after contrast, while the exact boundary and distance to the closest park create a within-city spatial gradient. Plant fixed effects narrow the comparison to incumbent plants; distance-to-CBD and a global impact of other parks distinguish the local gradient from the city's overall growth. The same production shock is then traced into housing prices/sales and retail entry on the 2 km grid [E1; E2].

The location IV provides a second, conditional comparison: zones with lower historical land-conversion costs are more likely to receive a park. It is useful for checking whether OLS location selection biases the local spillover estimate, but it is not a universal exogenous boundary or a policy lottery. Park recruitment, incumbent selection, and citywide reallocation remain part of the interpretation.

## Identification Risks

Mayors choose park locations based on land costs, infrastructure, universities, existing industry, and expected future growth. Administrative committees also recruit productive firms after the park is created, so an inside-park premium combines selection and treatment. The authors address this with incumbent plants, fixed effects, spatial controls, and land-cost instruments, but historical land and population measures may still proxy persistent productivity or later infrastructure [E2].

Timing is another boundary. Firms may anticipate a park before its listed establishment year, and construction or recruitment may lag approval. Small-zone centroids and reconstructed historical codes add spatial error near the boundary. Finally, nearby plants, housing, and shops can be attracted from other parts of the city; a positive local gradient need not imply the same-size citywide gain [E1; E2; analytical inference].

## Data Requirements

The minimum data contract is a park code/level/city/year and polygon; plant-level ASIF outputs, inputs, employment, ownership, industry, address and zone identifiers; road-network distances; park employment and composition; historical land/population/slope IVs; and geocoded housing and retail observations. The manufacturing panel runs 1998–2007, while housing and retail begin in 2006 and run through 2013. A new study should retain the original park count/version and use a boundary-quality flag rather than treating all GIS joins as equally precise [E2; E3; E4].

## Evidence Notes

E1 is the published JUE article record and establishes the final article's 110-park headline, eight-city setting, localized productivity/wage/employment effects, and housing/retail edge-city findings; it does not expose the park GIS file. E2 is the inspectable NBER working paper and establishes the 120-park data construction, official-list source, 1996 cohort split, 58,834-plant ASIF panel, geocoding procedures, 27 new parks, location IVs, and spatial models; it is an earlier version and does not by itself resolve the final article's count. E3 is the official NDRC/MNR/Construction Ministry announcement and establishes the reviewed directory and formal boundary process; it does not provide the authors' full plant-level join. E4 is an MLR boundary notice reproduced in the Ministry of Commerce legal database and establishes the publication of boundary text/coordinates; the original archive should be checked before serving a machine-readable polygon.

The record is grounded as a China place-based and within-city spatial exposure. It is especially useful for edge-city and spillover questions, provided that a downstream researcher states whether the estimand is a local effect, a displacement-adjusted city effect, or a location-IV effect under the historical-cost exclusion assumption.
