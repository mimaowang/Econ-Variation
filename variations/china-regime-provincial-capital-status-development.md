---
schema_version: 2
id: china-regime-provincial-capital-status-development
name: Regime-Driven Provincial-Capital Status Changes and Regional Development in Historical China
aliases:
- historical Chinese provincial-capital gains and losses
- Bai-Jia political hierarchy 1000-2000
- 历代省会地位变迁
status: design-documented
provenance:
  task_id: task-62b2b2793910
scope:
  country: China
  regions:
  - China proper in the paper's historical 261-prefecture harmonization; this is not a panel of all territory in today's mainland China
  domains: [regional-economics, urban-economics, development-economics, political-economy, economic-history]
  variation_type: other
  knowledge_role: china-variation
  china_relevance: >
    Bai and Jia study Chinese prefectures whose provincial administrative-center
    status changed across dynastic and modern regimes. This is a historical
    China-facing assignment, not a modern place-based program and not a claim
    that every national-capital move is a separate treatment.
identity:
  instrument: >
    Gaining or losing the seat of a provincial-level government as national
    regimes changed provincial boundaries, national capitals and provincial
    administrative centers. The empirical treatment is provincial-capital
    status of a location, not the regime change itself or distance to Beijing.
  authority: >
    The governing court or national government of each regime established
    provincial jurisdictions and their administrative seats. These were
    political choices, not randomized assignments; the paper models their
    geographical logic rather than claiming they were automatically exogenous.
  legal_identifiers: []
  implementation_regime: >
    The paper follows the Northern Song, Ming, Qing and People's Republic
    observation regimes; it omits the Yuan and Republic from its baseline
    population panel because of shorter duration and weaker prefectural data.
    The Song could have separate seats for fiscal and judicial/welfare affairs,
    both counted as provincial capitals in the baseline. Provincial-capital
    status must therefore be read by regime and office function, not assigned
    using today's provincial capital list.
  assignment_mechanism: >
    A historical prefecture becomes exposed when the geocoded seat of a
    provincial administration falls inside it, and ceases to be exposed when
    that seat moves or the relevant jurisdiction changes. The paper maps those
    historically dated seats and boundaries to fixed year-2000 prefectures;
    its separate hierarchical-distance index predicts status using within-
    province geography and distance to the national capital, but is an
    empirical instrument, not a statutory selection rule.
  parent: null
  related_variations: [china-ming-capital-relocation-population-distribution]
timeline:
  announcement: null
  effective: null
  implementation_start: 980
  implementation_end: 2000
  local_timing: >
    CHGIS represents administrative units, parent jurisdictions and seat
    locations with historical begin/end years [E1]. Bai and Jia observe
    population at 980, 1078, 1102, 1393, 1580, 1776, 1820, 1851, 1910,
    1964 and 2000, coding capital status at each observation; these sparse
    measurement years are not eleven reform dates [E2; E3]. Historical seat
    changes can fall between observations, so event time is interval-censored.
  anticipation: >
    Regime transitions, war and administrative preparation may precede the
    recorded capital-seat change. Neither a dynasty boundary nor a census
    year proves an unanticipated treatment date.
  last_verified: '2026-10-02'
assignment:
  unit: Harmonized year-2000 Chinese prefecture by historical observation year
  treated: >
    A prefecture-period whose fixed polygon contains a geocoded provincial
    capital seat for that historical regime. Gaining and losing that status
    are opposite transitions in one binary mechanism, not two records.
  comparison_pool: >
    Other prefectures in the 261-unit China-proper panel, including never-
    capitals and not-yet or formerly capital prefectures. The paper also
    examines 63 ever-capital prefectures to narrow the comparison, and allows
    geography, crop suitability and macroregion to have period-specific effects.
  rule: >
    Use CHGIS's dated provincial-seat points, administrative hierarchy and
    historical boundaries, plus the paper's digitization of Song geography,
    to determine whether each fixed year-2000 prefecture contains a relevant
    seat in each observed period [E1; E2; E3]. Do not label every prefecture
    near a national capital as treated; proximity enters the separate IV.
  intensity: Binary provincial-capital status in the main DID; gain and loss indicators in appendix change-on-change specifications.
  exemptions:
  - Yuan and Republican periods are omitted from the baseline because of shorter duration and data availability, not because their administrations lacked capitals.
  - China-proper coverage excludes historical peripheral regions with incomplete or changing governance and archival coverage.
  compliance: >
    The formal administrative seat and measured capital status are observable
    historical geography. The sources do not establish when each public office,
    infrastructure investment or market response became effective locally.
  exposure_construction: >
    Harmonize historical population and administrative geography to the 261
    year-2000 prefectures. The main outcome crosswalk allocates historical
    prefecture population to overlaps in proportion to area, then divides by
    fixed prefecture area. Geocode provincial seats and intersect them with
    the fixed polygon in each observed period. Retain historical and fixed
    IDs separately; the paper tests 1- and 2-degree grids as alternatives.
  required_identifiers: [historical administrative-unit identifier, historical validity year, provincial-seat point, historical boundary polygon, year-2000 prefecture identifier, observation year]
  spillovers: >
    A capital may redirect offices, roads, tax flows and migration across a
    whole province. Neighboring non-capitals can benefit from improved access,
    so the DID contrasts relative location effects, not aggregate national gains.
research_compatibility:
  outcome_domains: [historical population density, urbanization, spatial concentration, public employment, transport-network centrality]
  affected_populations: [residents of historical Chinese prefectures, provincial administrators, neighboring prefectures on administrative and transport routes]
  mechanism_channels: [location of public offices, fiscal and information routing, state transport investment, regional market access]
  best_for:
  - Questions about how provincial political status redirects Chinese population and urban development over long periods.
  - Designs able to reconstruct regime-specific seats, boundaries and sparse historical population measurements.
  not_good_for:
  - Treating provincial-capital designation as a randomly assigned modern policy or an annual rollout.
  - Reusing the paper's historical effect as a contemporary city-growth elasticity without checking period and population fit.
  - Treating the hierarchical-distance IV as valid for outcomes directly shaped by national-capital proximity or boundary changes.
design:
  claim_type: causal
  affordances: [within-prefecture status changes across regimes, both gains and losses, geographical predictor of capital selection]
  candidate_designs: [historical prefecture-period DID, gain-versus-loss change model, hierarchical-distance IV]
  identifying_variation: >
    Regime changes shifted national capitals and provincial boundaries, altering
    which prefectures held provincial administrative seats. The paper uses
    actual status changes in DID, then uses the regime-specific rank of a
    geography-only hierarchical-distance measure to predict status in an IV.
  primary_strategy: >
    Bai and Jia regress log population density or urbanization on capital
    status with fixed prefecture and observation-year effects, interacting
    geography, crop suitability and nine macroregions with years. Their IV
    first stage predicts status with log rank in hierarchical distance, built
    from area-weighted distances to other prefectures in the province plus a
    regime-weighted distance to the national capital. The second stage replaces
    actual status with the predicted component [E2, pp. 632-638; E3, B.2].
  estimand: >
    DID: conditional difference in prefectural population density or
    urbanization associated with holding provincial-capital status in this
    historical panel. IV: a local effect for prefectures whose status responds
    to the paper's hierarchical-distance predictor, conditional on its
    exclusion restriction; it need not equal the DID estimand.
  treatment_variable: >
    Capital_it equals one when the fixed prefecture contains a provincial
    capital seat in observation period t. The IV is log rank in hierarchical
    distance within the contemporaneous province, not the treatment itself.
  comparison_logic: >
    Compare a prefecture's outcomes when it does and does not hold status,
    net of common time shocks, against other prefectures in the harmonized
    panel. Gain/loss and ever-capital analyses test whether the pooled
    contrast depends on permanently different cities [E2; E3].
  estimation_notes: >
    The baseline has 261 prefectures and 2,871 prefecture-period observations;
    urbanization uses only 1580, 1820, 1964 and 2000. The paper clusters
    standard errors by prefecture, tests spatial inference, excludes four
    extra census years from the baseline to limit uneven gaps, and checks
    grid-level mappings. Its reported magnitudes are conditional historical
    estimates, not an invariant policy effect [E2, Tables 2-3; E3, B.1].
  assumptions:
  - Absent status changes, conditional population trends of changing and comparison prefectures would be comparable.
  - Regime-induced hierarchical distance changes predict status but do not directly alter local development through other channels after controls.
  - Historical population and administrative boundaries can be mapped to fixed units without differential error driving the result.
  - Population displacement and neighbor spillovers are interpreted as part of a spatial reallocation, not as independent national growth.
  diagnostics: [pre-status-change trends, ever-capital-only sample, gain and loss symmetry, alternate grid harmonization, placebo hierarchical distance, national-capital and boundary sensitivity, spatial standard errors]
threats:
- type: endogenous-capital-selection
  basis: documented
  condition: Rulers selected administrative centers for political and geographic reasons; successful or strategically important places could also be selected.
  evidence_refs: [E2, E3]
  possible_diagnostics: [ever-capital sample, pretrends, gain and loss contrasts]
- type: iv-exclusion
  basis: documented
  condition: Changes in national-capital location and provincial boundaries can alter market access, defense or trade even without changing a prefecture's capital status. The hierarchical-distance rank is not automatically excluded from outcomes.
  evidence_refs: [E2, E3]
  possible_diagnostics: [never-capital reduced form, component controls, alternative market-center distances]
- type: historical-crosswalk
  basis: documented
  condition: Area-proportional redistribution assumes population was uniform within a historical prefecture; changing boundaries and sparse censuses can blur exposure and outcomes.
  evidence_refs: [E2, E3]
  possible_diagnostics: [1- and 2-degree grid alternatives, boundary-specific sensitivity, census-period subsets]
- type: bundled-regime-change
  basis: inferred
  condition: War, migration, taxation and transport-policy changes accompanying a new regime may affect the same prefectures, so status is not the only consequence of regime change.
  evidence_refs: [E2]
  possible_diagnostics: [regime-specific patterns, mechanism data, geographic and region-by-period controls]
empirical_requirements:
  contract_version: 1
  population: Historical China-proper prefectures in the paper's 261-unit harmonized panel.
  observation_unit: fixed-prefecture by irregular historical observation period
  geography_level: historical provincial and prefectural geography harmonized to year-2000 prefectures
  time_start: 980
  time_end: 2000
  minimum_frequency: irregular historical censuses, not annual
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields: [historical provincial-seat geocode and validity years, historical province and prefecture boundaries, fixed year-2000 prefecture polygons, prefecture population by historical census, geography and macroregion controls]
  required_identifiers: [historical prefecture ID, historical province ID, validity year, seat point ID, fixed prefecture ID, observation year]
  treatment_key: [fixed prefecture ID, observation year, capital status]
  treatment_source: CHGIS historical seats and boundaries with the paper's digitized Song supplement; replication dataset DOI 10.7910/DVN/ZQDPTB is a source lead, not an independently audited substitute for historical records.
  measurement_risks: [interval-censored reform timing, historical boundary interpolation, nonuniform population inside polygons, source coverage differences across dynasties]
design_profiles: []
evidence:
- id: E1
  source_type: official-data
  citation: Harvard China Historical GIS, database design and temporal administrative-unit documentation.
  url: https://chgis.fas.harvard.edu/pages/database/
  date: null
  supports: [identity.instrument, identity.implementation_regime, timeline.local_timing, assignment.rule, assignment.required_identifiers]
  verification_status: verified
  access_level: dataset
  locator: 'Database Design §§1-3.3: historical administrative-unit validity spans, province/prefecture polygons, provincial administrative-seat points, parent jurisdictions and source-note links; inspected 2026-10-02. Supports CHGIS data structure, not every capital transition coded by the paper.'
- id: E2
  source_type: paper
  citation: 'Bai, Ying, and Ruixue Jia. 2023. The Economic Consequences of Political Hierarchy: Evidence from Regime Changes in China, 1000–2000 C.E. Review of Economics and Statistics 105(3):626-645. DOI 10.1162/rest_a_01058.'
  url: https://cbdb.hsites.harvard.edu/sites/g/files/omnuum3101/files/cbdb/files/the_economic_consequences_of_political_hierarchy_evidence_from_regime_changes_in_china_1000-2000_c.e.pdf
  date: '2023'
  supports: [identity.assignment_mechanism, identity.implementation_regime, timeline.local_timing, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.exposure_construction, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.population, empirical_requirements.time_start, empirical_requirements.time_end, design_applications.empirical_design, design_applications.data_used]
  verification_status: verified
  access_level: full-text
  locator: 'Published PDF pp. 626-638, especially §II.B, §III, §V.A and Tables 1-3: regime and status coding, 261-unit crosswalk, DID/IV, outcome periods, comparator and diagnostics; inspected 2026-10-02.'
- id: E3
  source_type: appendix
  citation: Bai and Jia, Online Appendix to The Economic Consequences of Political Hierarchy, NBER-hosted version.
  url: https://back.nber.org/appendix/w26652/HierarchyAppendix191231.pdf
  date: '2019-12-31'
  supports: [assignment.exposure_construction, design.treatment_variable, design.diagnostics, empirical_requirements.required_fields, empirical_requirements.measurement_risks, design_applications.treatment_encoding, design_applications.comparison]
  verification_status: verified
  access_level: appendix
  locator: 'Appendix pp. A-4 to A-6 §§B.1-B.2 and pp. A-10 to A-18 §§D-E: area-weighted population crosswalk, seat geocoding, hierarchical distance and gain/loss, pretrend and IV checks; inspected 2026-10-02. Appendix predates final typesetting; use final article for headline sample and results.'
- id: E4
  source_type: other
  citation: MIT Press, Review of Economics and Statistics publication DOI registration for Bai and Jia 2023.
  url: https://doi.org/10.1162/rest_a_01058
  date: '2023'
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: 'DOI and published citation printed on the inspected article first page; DOI landing identity checked 2026-10-02. Bibliographic support only.'
design_applications:
- paper: 'The Economic Consequences of Political Hierarchy: Evidence from Regime Changes in China, 1000–2000 C.E.'
  doi: 10.1162/rest_a_01058
  journal: Review of Economics and Statistics
  year: 2023
  research_question: How do gains and losses of provincial administrative-center status reshape Chinese regional population and urbanization over long periods?
  population: 261 harmonized China-proper prefectures over eleven irregular observation dates, 980-2000.
  outcome: Log population density; urbanization and public employment/transport as secondary outcomes.
  data_used: [CHGIS regime-specific boundaries and seat points, digitized Song provincial seats, historical prefecture census counts, 1964 and 2000 censuses, geography and macroregion controls]
  treatment_encoding: Indicator that a fixed year-2000 prefecture contains a regime-specific provincial seat; appendix also separates gains from losses.
  comparison: Within-prefecture status changes against other harmonized prefectures, with year fixed effects and differentiated geographic trends; 63 ever-capital prefectures provide a narrower comparison.
  empirical_design: Historical prefecture-period DID and hierarchical-distance IV; the latter uses regime-induced geography to predict capital status and requires an exclusion restriction.
  assumptions: [conditional counterfactual trends, no direct effect of IV geography apart from status, valid historical boundary harmonization]
  threats_addressed: [pretrends, status selection, boundary harmonization, IV alternative channels, spatial dependence]
  evidence_refs: [E2, E3, E4]
method_transfer: null
readiness_blockers: []
---

## Institutional Background

The change here is **which Chinese prefecture housed a provincial government**, not a generic dynasty dummy. Under successive regimes, rulers redrew provinces and located their seats partly in relation to other prefectures and the national center. A prefecture could gain, retain, or lose this administrative role; Song fiscal and judicial seats complicate any one-capital-per-province shortcut. CHGIS preserves dated administrative units and seat locations, while Bai and Jia geocode the status into a stable prefectural panel [E1; E2]. The separate Ming move of the national capital is related background, not this record's treatment.

## What Changed

Holding the provincial seat changed a place's position in the administrative hierarchy and its access to offices and state-directed connections [E2, reported interpretation]. Its exact political and economic content varied across regimes; the record follows the common seat-status assignment, not a claim that all regimes transferred identical powers.

## Implementation and Assignment

The paper observes 261 fixed year-2000 prefectures at eleven unevenly spaced dates from 980 to 2000. It reconstructs older population counts on those fixed polygons using area-overlap weights and marks whether a period's provincial seat lies inside each polygon [E2, reported application; E3, reported crosswalk]. The treatment variable is therefore encodable, but neither the census year nor the dynasty label is an exact date at which every office or economic channel moved. Historical boundary changes and sparse observations are part of the research design, not clerical details.

## Why This Creates Empirical Variation

In the published application, a prefecture's periods with capital status are compared with its other periods and with contemporaneous non-capital prefectures. The authors supplement this DID with an IV based on the rank of an area-weighted distance to fellow prefectures plus distance to the national capital; regime changes alter that geography and predict capital placement [E2; E3, reported application]. The DID comparison and IV prediction are complementary, but they rest on different assumptions and need not estimate the same effect.

## Identification Risks

This setting is useful for studying population density and urbanization, conditional on pretrend comparability and on the IV not affecting development by routes other than capital status. The sources do **not** make provincial-capital selection automatically exogenous. Neighboring places may gain transport access even without holding the seat, and the historical series cannot support an annual event-study clock [analytical inference]. The paper's gain/loss, ever-capital, grid and IV checks reduce specific concerns without proving every regime shock was otherwise inert [E2; E3].

## Data Requirements

The starting point is a dated capital-seat and boundary panel, then a documented historical-to-fixed-prefecture overlay, not a contemporary city-year table. The article and appendix specify the 261-unit geography, irregular population observations, four urbanization dates and hierarchical-distance ingredients [E2; E3]. The Harvard Dataverse replication DOI is a retrieval lead; this record does not claim to have independently rebuilt its files.

## Evidence Notes

CHGIS documentation verifies how historical seat, parent-jurisdiction and validity-year data are organized [E1]. The published paper and appendix report the actual analysis, sample construction and diagnostics [E2; E3]. Neither source licenses treating every reconstructed historical status or outcome as error-free; the crosswalk and political selection remain substantive conditions.
