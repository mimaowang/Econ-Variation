---
schema_version: 2
id: china-export-slowdown-shift-share-land-supply
name: China City Export-Slowdown Shift-Share Exposure and the Local Land-Supply Fiscal Response (Wang-Wu-Wu 2025 JUE)
aliases:
- Wang Wu Wu 2025 Export slowdown and increasing land supply JUE
- Falling export and rising land supply CES 2024 conference version
- export shock Bartik IV residential land supply China fiscal consolidation
- 中国城市出口放缓 shift-share 暴露与地方政府土地供应财政反应
status: grounded
provenance:
  task_id: task-1caed0a89490
scope:
  country: China
  regions:
  - Prefecture-level Chinese cities; the published version reports 320 cities over 2008-2022, and the inspected 2024 conference version uses 326 cities over 2007-2017 with a 2019-2020 COVID-19 extension
  domains:
  - trade-globalization
  - public-finance
  - infrastructure-urban
  - governance-politics
  variation_type: continuous-exposure
  knowledge_role: global-china-variation
  china_relevance: >
    The shock originates outside China - year-to-year changes in national
    (leave-one-out) export demand by product chapter, plausibly driven by
    world trade conditions after the 2008 global financial crisis, the
    2012-2019 weak trade recovery, and COVID-19 - but exposure is assigned
    to Chinese prefecture-level cities through their base-period export
    composition, and the studied response is a distinctly Chinese
    institution: city governments monetize their monopoly over urban land
    supply to offset export-driven tax-revenue losses. The regional/urban
    content is central: differential city exposure, residential land supply,
    urban expansion, and commuting costs.
identity:
  instrument: >
    A city-level export-demand shift-share (Bartik) instrument. The
    endogenous regressor is the log-difference of city i's total export
    value between year t-1 and t (from General Administration of Customs of
    China firm-level customs records collapsed to city-year by exporter
    location). The instrument sums, over 97 HS two-digit chapters k, the
    leave-one-out national export change in chapter k in year t (all cities
    except i) multiplied by city i's base-period share of national exports
    in chapter k, divided by city i's base-period total exports; the
    baseline base period is the 2006-2007 average, with 2005-2007 and 2007
    alternatives as robustness.
  authority: >
    No policy authority assigns treatment. The underlying measurements are
    produced by the General Administration of Customs of China (GACC)
    firm-level export records and the Ministry of Natural Resources
    landchina.com parcel records; the shock construction (chapter
    aggregation, leave-one-out shifts, base-period shares) is the authors',
    following Bartik (1991), Autor et al. (2013), Goldsmith-Pinkham et al.
    (2020), and Campante et al. (2021).
  legal_identifiers:
  - 'Wang, Qiuyi, Jing Wu, and Shuping Wu. 2025. "Export slowdown and increasing land supply: Local government''s responses to export shocks in China." Journal of Urban Economics 149: 103796. DOI: 10.1016/j.jue.2025.103796'
  - 'RePEc:eee:juecon:v:149:y:2025:i:c:s0094119025000610 (EconPapers bibliographic record and official abstract)'
  - 'Wang, Qiuyi, Jing Wu, and Shuping Wu. 2024. "Falling Export and Rising Land Supply: Local Government''s Responses to Export Shock in China." Chinese Economists Society conference version, open full text (56 pages including appendices)'
  implementation_regime: >
    External demand realization, not an administrative regime. National
    export growth by HS chapter fluctuates with world trade conditions
    (post-2008 GFC slowdown, weak 2012-2019 recovery, 2020 COVID-19
    disruption); each city inherits a weighted average of these national
    chapter-level shifts with fixed base-period weights reflecting its
    pre-sample export specialization. There is no rollout, threshold, or
    eligibility rule.
  assignment_mechanism: >
    Shift-share interaction: exposure intensity equals the covariance
    between a city's fixed base-period (2006-2007) export composition
    across HS chapters and the national leave-one-out export growth of
    those chapters in year t. Identification relies on the exogeneity of
    the national chapter-level shifts (Borusyak et al. 2022), not of the
    shares, which the authors acknowledge may be endogenous to cities'
    comparative advantage; balance tests regress HS-level shocks on
    exposure-weighted baseline city characteristics and find no correlation.
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 2008
  implementation_end: 2022
  local_timing: >
    The published version (JUE 2025) reports a 2008-2022 panel of 320
    prefecture-level cities. The inspected 2024 conference version uses
    GACC city-chapter export data for 2007-2017 (326 cities), NTSD tax data
    for 2008-2015 (tax regressions estimated 2009-2015 because variables
    are log-differenced), landchina.com parcel records for 2007-2017 (land
    regressions 2008-2017), and an analogous-construction COVID-19
    extension for 2019-2020. How the published version extends the
    city-chapter export panel to 2022 and reduces the sample to 320 cities
    is not verified in the inspected sources. The 320-city figure comes
    from publisher/RePEc-derived screening text and was not re-verified in
    the abstract inspected here.
  anticipation: >
    National chapter-level export shifts are world-demand realizations that
    a single Chinese city cannot anticipate or manipulate; city governments
    respond within the same year by adjusting land supply. The 2008-2009
    fiscal stimulus is a documented co-occurring national response that may
    mute downstream price effects (the paper notes stimulus likely offset
    housing-price declines); year and province-by-year fixed effects absorb
    the common component but not any city-differential stimulus allocation.
  last_verified: '2026-08-15'
assignment:
  unit: >
    City-year: prefecture-level cities (326 in the inspected conference
    version; 320 reported for the published version), observed annually.
  treated: >
    All cities are continuously treated; there is no untreated group.
    Treatment intensity is the city's realized export growth (log-difference
    of total export value), instrumented by the shift-share predicted
    export shock.
  comparison_pool: >
    Other cities in the same year: year fixed effects absorb national
    shocks, city fixed effects absorb time-invariant specialization, and
    province-by-year fixed effects restrict the comparison to cities within
    the same province and year, which matters because coastal provinces
    combine high export exposure with scarce developable land.
  rule: >
    Construct the shift-share instrument from GACC customs data: aggregate
    firm-level exports to city-year values for each of 97 HS two-digit
    chapters (HS-8 codes collapsed by first two digits); compute the
    leave-one-out national chapter export change; weight by the city's
    2006-2007 average share of national exports in that chapter; divide by
    the city's 2006-2007 average total exports. Regress the log-difference
    of local tax revenue or of residential land supply (revenue, area,
    price) on the log-difference of city exports by 2SLS, with city, year,
    and province-by-year fixed effects, city-clustered standard errors, and
    5 percent winsorization of all variables.
  intensity: >
    Continuous. In the inspected conference version, a ten-percentage-point
    decrease in export growth reduces local tax revenues by 2.17 percent
    and increases revenue-oriented residential land supply revenues by
    9.78 percent (2009-2015 sample); the implied land-revenue increase
    (about USD 20.3 billion against USD 8.7 billion of tax losses, with
    about 36 percent of land revenue becoming profit) yields a roughly
    0.84-to-one profit substitution. The published abstract reports that
    additional land-supply profits offset approximately 94 percent of
    tax-revenue losses over 2008-2022.
  exemptions:
  - Chapter 77 of the HS classification has no export value and is dropped, leaving 97 chapters
  - NTSD 2007 is excluded because corporate income tax information is missing, so the tax-revenue panel starts in 2008 and the log-differenced tax regression in 2009
  - Land parcels that failed to sell (no bid above the price floor) are not in the supply data
  - The 2019-2020 COVID-19 analysis uses an analogous rather than identical shock construction because the city-chapter export panel was unavailable
  compliance: >
    Exposure is measured from customs records, not chosen, but exporter
    location determines the city assignment of exports; intermediary-firm
    exports may not reflect local production shocks (a concern addressed in
    the related Campante et al. design by excluding intermediaries; the
    inspected text does not document such an exclusion here). Land supply is
    the government's choice variable, and the design estimates that
    behavioral response rather than treating it as assigned.
  exposure_construction: >
    Author construction from three administrative micro-datasets: GACC
    firm-level customs records (exporter location to city, HS-8 product,
    USD values deflated to 2007=100); SAT-MOF National Tax Survey Database
    (about 680 thousand firms per year, 2008-2015) aggregated to city-year
    local tax revenue using statutory provincial share ratios and estimated
    within-province city share ratios; and Ministry of Natural Resources
    landchina.com parcel-level primary-market land transfers (279,534
    residential parcels sold by tender, English auction, or two-stage
    auction in 326 cities, 2007-2017), collapsed to city-year area, price,
    and revenue.
  required_identifiers:
  - stable prefecture-city identifier linking customs exporters, NTSD firms, and landchina parcels over 2007-2022
  - HS chapter (two-digit) for each export record
  - land parcel transaction method (tender / English auction / two-stage auction versus administrative allocation or negotiation) to separate revenue-oriented supply
  - tax type and statutory sharing ratios to compute the local-government share of NTSD tax payments
  spillovers: >
    The leave-one-out construction removes a city's own contribution from
    its shifts, but spatially correlated demand conditions across cities
    remain possible; the paper reports robustness to province-level
    clustering and to Adao et al. (2019) AKM/AKM0 shift-share inference.
    General-equilibrium channels are acknowledged rather than modeled: the
    2008-2009 national stimulus may have offset housing-price declines, and
    land oversupply spills into housing markets with a development lag
    (three-year-lagged export shocks raise housing stock and supply but not
    sales).
research_compatibility:
  outcome_domains:
  - local government fiscal behavior and fiscal consolidation through land revenue
  - urban residential land supply (area, price, revenue) and land-finance sustainability
  - urban spatial expansion, housing-market oversupply risk, and commuting costs
  - local tax revenue responses to external trade shocks
  affected_populations:
  - Prefecture-level city governments and their fiscal budgets, 2008-2022
  - Urban residents affected by induced land oversupply, excessive built-up expansion, and commuting costs
  mechanism_channels:
  - export slowdown reducing local tax revenues, inducing revenue-oriented residential land supply as fiscal consolidation
  - area-margin expansion with stable land prices as the operative land-supply margin
  - developable-land availability (Saiz-style slope constraint) and base-period housing prices conditioning the feasibility of the response
  - land oversupply converting into housing stock with a development lag, amplifying oversupply risk and commuting costs
  best_for:
  - Designs that need a plausibly exogenous city-level external demand shock in post-2008 China with a fully documented shift-share construction (base shares, leave-one-out shifts, balance tests, AKM inference)
  - Studies of Chinese land finance, local fiscal consolidation, and urban land supply responses to trade exposure
  - Analyses linking trade shocks to urban spatial expansion and housing-market risk
  not_good_for:
  - Questions that need a domestic policy instrument; the variation is an external demand shock and its land-supply response is a behavioral outcome, not an assigned treatment
  - Designs requiring the exact published 2008-2022 construction; only the 2007-2017 conference-version construction (plus a 2019-2020 analogous COVID extension) is fully inspected, and the extension of the city-chapter export panel past 2017 is unverified
  - Studies needing firm- or individual-level outcomes; the identifying variation and outcomes are city-level aggregates
design:
  claim_type: causal
  affordances:
  - A fully specified shift-share instrument with named base period (2006-2007 average; 2005-2007 and 2007 robustness), 97 HS two-digit chapters, and leave-one-out national shifts
  - "Placebo structure from China's land-supply institutions: non-revenue-oriented residential supply (administrative allocation, negotiation) and revenue-oriented industrial land supply should not respond to a fiscal-consolidation motive"
  - "A secondary-market residential land transaction placebo that separates the government-supply channel from a confounded housing-price boom"
  - "Administrative micro-data on both sides of the mechanism: NTSD tax survey for the revenue loss and parcel-level MNR records for the land response"
  candidate_designs:
  - 2SLS first-difference panel of city tax revenue or land supply on export growth instrumented by the shift-share shock, with city, year, and province-by-year fixed effects
  - Reduced-form (IV-OLS) regression of land-supply changes directly on the shift-share shock
  - IV regression of land-supply revenue on tax revenue instrumented by the shift-share shock to estimate the fiscal substitution rate
  - Heterogeneity by developable-land ratio and base-period housing prices; asymmetry between negative and positive shocks
  identifying_variation: >
    Cross-city differences in base-period export composition interacted
    with year-by-year national chapter-level export demand shifts,
    restricted within province-year cells; identification comes from the
    exogeneity of national chapter shifts, not from the shares.
  primary_strategy: >
    Two-stage least squares (paper Equations 5 and 6). First stage: city
    export log-growth on the shift-share instrument (coefficient about
    0.54-0.61, Kleibergen-Paap F about 30-40). Second stage:
    log-differences of local tax revenue (2009-2015) and of
    revenue-oriented residential land supply revenue, area, and price
    (2008-2017) on instrumented export growth, with city, year, and
    province-by-year fixed effects, city clustering, and 5 percent
    winsorization.
  estimand: >
    The causal effect of a city-level export growth change on (a) local
    government tax revenue growth and (b) revenue-oriented residential land
    supply growth (revenue, area, price), for prefecture-level Chinese
    cities in the post-2008 period; and the implied fiscal substitution
    rate between land-supply profits and export-driven tax losses.
  treatment_variable: >
    Log-difference of city total export value (USD, 2007=100) between t-1
    and t, instrumented by the base-period-weighted leave-one-out national
    chapter export change (the Bartik variable).
  comparison_logic: >
    Within province-year, cities whose base-period export mix was
    concentrated in chapters with weak national demand are compared with
    cities specialized in stronger chapters. The comparison fails if
    national chapter shocks correlate with exposure-weighted baseline city
    characteristics (balance-tested), if city-specific confounders
    correlated with the export mix drive land supply (addressed by
    base-year values of GDP per capita, FDI, fiscal revenue, built-up area,
    secondary-industry share, and housing price interacted with year fixed
    effects), or if domestic output and import shocks confound the export
    channel (directly controlled following Campante et al. 2021).
  estimation_notes: >
    Inspected conference-version results: 2SLS coefficient of export growth
    on tax-revenue growth 0.217 (2009-2015, KP F 30.7); on land-supply
    revenue growth -1.128 (2008-2017, KP F 32.5) and -0.978 on the matched
    2009-2015 sample. Effects run through the area margin: land supply area
    increases while prices stay stable, consistent with revenue
    maximization through volume. The response is asymmetric (stronger for
    below-median shocks) and stronger in fiscally stressed and
    export-dependent cities. A ten-percentage-point export decline maps to
    about USD 20.3 billion additional land revenue against USD 8.7 billion
    tax losses (about 0.84-to-one in profits at a 36 percent profit share);
    the published abstract reports a 94 percent offset over 2008-2022.
    Unintended-cost exercises: negative export shocks significantly raise
    excessive built-up-area expansion (four prediction scenarios), raise
    housing stock and supply (not sales) at a three-year lag, and imply
    RMB 0.664 billion per year of added commuting costs per percentage
    point of export decline in the conference version (the published
    abstract reports USD 124 million per year per percentage point).
  assumptions:
  - National HS-chapter export shifts are exogenous to city-level determinants of land supply conditional on city, year, and province-by-year fixed effects (Borusyak et al. 2022 shifts-exogeneity); the shares are acknowledged as potentially endogenous
  - The export shock affects land supply through local tax-revenue losses (fiscal consolidation), not through a housing-price demand channel (placebo evidence reported against the price channel)
  - Exporter location in customs data assigns export exposure to the correct city
  - NTSD-based tax revenues proxy total local tax revenues (about 63 percent of Finance Yearbook totals) without shock-correlated coverage bias
  diagnostics:
  - Balance tests of HS-level export shocks against exposure-weighted baseline city characteristics (GDP per capita, fiscal revenue per capita, non-hukou population share, manufacturing employment share, export-to-GDP ratio, college-educated share) showing no correlation
  - Alternative base periods (2005-2007, 2007) and alternative winsorization (1, 2 percent) leaving estimates comparable
  - Adao et al. (2019) AKM and AKM0 confidence intervals and province-level clustering leaving inference intact
  - "Placebo outcomes: non-revenue-oriented residential supply, revenue-oriented industrial land supply, and secondary-market residential transactions show no matching response"
  - Direct controls for city domestic output shocks and import shocks (Campante et al. 2021 style) leave the export coefficient stable
threats:
- type: shift_share_share_endogeneity
  basis: documented
  condition: The base-period export shares reflect cities' comparative advantage and could correlate with unobserved land-supply determinants; the authors acknowledge this and rest validity on shifts-exogeneity with balance tests, following Goldsmith-Pinkham et al. (2020) and Borusyak et al. (2022).
  evidence_refs:
  - E1
  possible_diagnostics:
  - Re-estimate with shock-level instruments or leave-one-industry-out variants
  - Test pretrends in land supply against future shift-share shocks
- type: co_occurring_stimulus_and_policy_confounding
  basis: reported
  condition: The 2008-2009 national fiscal stimulus coincided with the largest export decline and may have been allocated differentially across cities; year and province-by-year fixed effects absorb only the common component. The paper notes the stimulus likely offset housing-price declines but does not isolate city-differential stimulus.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Control for city-level stimulus allocation or credit growth where data allow
  - Restrict to post-stimulus years and compare
- type: housing_price_channel_confounding
  basis: reported
  condition: Rising housing prices over 2007-2017 could independently drive land supply and correlate with export performance; the paper reports no significant export-shock effect on housing-price changes, robustness to controlling housing-price changes, and a secondary-market placebo that rejects the price-driven story, but the housing boom remains a background condition of the whole period.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Interact the shock with base-period housing-price levels and test stability
  - Replicate on the post-2017 fang-zhu-bu-chao regime where prices stagnated
- type: exporter_location_measurement
  basis: inferred
  condition: City assignment of exports follows exporter location; intermediary trading firms can register exports far from production, and the inspected text does not document an intermediary exclusion, so measured city exposure may differ from local production exposure.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Exclude intermediary-firm exports following Campante et al. (2021) and compare
  - Cross-check city export exposure against industrial-survey production locations
- type: published_version_construction_unverified
  basis: inferred
  condition: The published 2008-2022, 320-city version extends the city-chapter export panel beyond the 2017 boundary of the inspected conference version and changes the city count; the extension procedure, sample selection, and the 94 percent offset figure rest on the abstract and screening text rather than inspected full text.
  evidence_refs:
  - E2
  - E4
  possible_diagnostics:
  - Obtain the published article or its appendix and verify the post-2017 export panel construction and the 320-city sample rule
- type: tax_coverage_and_rebate_bias
  basis: reported
  condition: NTSD covers about 63 percent of local tax revenue and omits some tax types; export tax rebates are centrally funded (100 percent since 2015), so measured local tax losses may misstate true fiscal exposure if coverage correlates with export intensity.
  evidence_refs:
  - E1
  possible_diagnostics:
  - Recompute with Finance Yearbook totals at the city level and compare the first-stage-to-tax link
empirical_requirements:
  contract_version: 1
  population: Prefecture-level Chinese cities (326 in the inspected conference version; 320 reported for the published version)
  observation_unit: city-year
  geography_level: prefecture-level city, nested in province (province-by-year fixed effects)
  time_start: 2008
  time_end: 2022
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 0
  required_fields:
  - city-year export value by HS two-digit chapter (GACC customs, firm location; base-period 2006-2007 values for shares)
  - city-year local tax revenue by tax type with statutory sharing ratios (NTSD or Finance Yearbook)
  - parcel-level residential land transfers with transaction method, area, price, and revenue (landchina.com)
  - "city controls: GDP per capita, FDI, fiscal revenue per capita, built-up area, secondary-industry share, housing price (base-period values for interactions)"
  - city developable-land ratio and base-period average housing price for heterogeneity
  required_identifiers:
  - city_id
  - year
  - hs_chapter
  - parcel transaction method and parcel_id for aggregation
  treatment_key:
  - city_id
  - year
  treatment_source: >
    Author-constructed shift-share export shock: leave-one-out national
    HS-chapter export changes weighted by 2006-2007 city export shares,
    built from GACC customs micro-data; land-supply outcomes aggregated
    from MNR landchina.com parcel records (revenue-oriented methods only).
  measurement_risks:
  - exporter-location assignment may not match production location (intermediary firms)
  - NTSD sampling frame and 63 percent coverage of local tax revenue
  - city boundary and code changes over 2007-2022 are not verified in this record
  - the published version's post-2017 export panel construction is not inspected
  - landchina parcel records exclude parcels that failed to sell, so supply is measured conditional on successful transactions
design_profiles:
- id: ntsd-tax-revenue-subdesign
  label: NTSD tax-revenue fiscal-link subdesign
  design_families:
  - shift-share IV panel
  when_to_use: Use when the question concerns the export-to-local-tax-revenue link itself rather than the land response; bounded by NTSD availability (2008-2015, log-differenced regressions from 2009).
  outcome_domains:
  - local government tax revenue responses to external trade shocks
  requirements:
    population: Prefecture-level cities covered by the NTSD (about 680 thousand firms per year), 326 cities
    observation_unit: city-year
    geography_level: prefecture-level city
    time_start: 2009
    time_end: 2015
    minimum_frequency: annual
    minimum_pre_periods: 0
    minimum_post_periods: 0
    required_fields:
    - firm-level tax payments by tax type from the NTSD with statutory provincial share ratios and estimated within-province city share ratios
    - city-year export value by HS chapter for the instrument
    required_identifiers:
    - city_id
    - year
    - tax_type
    treatment_key:
    - city_id
    - year
evidence:
- id: E1
  source_type: paper
  citation: 'Wang, Qiuyi, Jing Wu, and Shuping Wu. 2024. "Falling Export and Rising Land Supply: Local Government''s Responses to Export Shock in China." Chinese Economists Society conference version (open full text, 56 pages including Appendices A-E; earlier version of the Journal of Urban Economics article).'
  url: https://www.china-ces.org/Files/3055abstract/202401241534361470.pdf
  date: 2024
  supports:
  - identity.instrument
  - identity.authority
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.local_timing
  - timeline.anticipation
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.exemptions
  - assignment.compliance
  - assignment.exposure_construction
  - assignment.required_identifiers
  - assignment.spillovers
  - design.identifying_variation
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - design.assumptions
  - design.diagnostics
  - empirical_requirements.population
  - empirical_requirements.required_fields
  - empirical_requirements.treatment_source
  - design_applications.paper
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
  locator: >
    Open conference-version PDF downloaded and text-extracted on
    2026-08-15 (56 pages). Inspected passages: Abstract; Sections 1-2
    (motivation, institutional background on land finance, Figure 1 export
    and tax-revenue growth 2007-2019); Section 3.1 (GACC customs data,
    97 HS two-digit chapters from HS-8, city-year panel 2007-2017 with
    326 cities, Equation 1 export shock, Equation 2 Bartik construction
    with leave-one-out national shifts and 2006-2007 base-period shares,
    footnote 10 formulas, 2005-2007 and 2007 alternative base years);
    Section 3.2 (NTSD 2008-2015, SAT-MOF, about 680 thousand firms,
    three-step local tax revenue construction, 63 percent coverage of
    Finance Yearbook totals); Section 3.3 (MNR landchina.com parcel data,
    279,534 residential parcels via tender/English auction/two-stage
    auction in 326 cities 2007-2017, revenue-oriented versus
    non-revenue-oriented and industrial placebos, successful transactions
    only); Section 3.4 (Equations 5-6, city/year/province-by-year fixed
    effects, city clustering, 5 percent winsorization); Section 4.1 and
    Table 1 (2SLS: tax 0.217, land revenue -1.128 and -0.978, first-stage
    coefficients 0.535-0.606, KP F 30.7-32.5, USD 20.3 billion land
    revenue versus USD 8.7 billion tax loss, 0.84-to-one profit
    substitution, IV substitution-rate coefficient -4.5); Section 4.4
    (housing-price channel rejection, secondary-market placebo, confounder
    interactions with base-year values, Borusyak-style balance tests,
    Adao et al. AKM/AKM0 inference, province clustering); Section 4.5
    (COVID-19 2019-2020 analogous construction); Section 5 (excessive
    expansion Table 5, three-year-lagged housing stock/supply/sales, RMB
    0.664 billion commuting cost per percentage point, developable-land
    and housing-price interactions). Establishes the design, data
    construction, results, and diagnostics of the conference version; it
    does not independently verify the underlying restricted datasets
    (GACC, NTSD, MNR) and it predates the published 2008-2022 version.
- id: E2
  source_type: paper
  citation: 'Wang, Qiuyi, Jing Wu, and Shuping Wu. 2025. "Export slowdown and increasing land supply: Local government''s responses to export shocks in China." Journal of Urban Economics 149: 103796. DOI: 10.1016/j.jue.2025.103796 (EconPapers/RePEc bibliographic record with official abstract).'
  url: https://econpapers.repec.org/article/eeejuecon/v_3a149_3ay_3a2025_3ai_3ac_3as0094119025000610.htm
  date: 2025
  supports:
  - identity.legal_identifiers
  - timeline.implementation_start
  - timeline.implementation_end
  - assignment.intensity
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
  verification_status: verified
  access_level: abstract
  locator: >
    EconPapers item page for RePEc:eee:juecon:v:149:y:2025:i:c:
    s0094119025000610 fetched and read 2026-08-15. Establishes the
    published identity (authors, Journal of Urban Economics volume 149,
    article 103796, DOI 10.1016/j.jue.2025.103796, keywords, JEL F14 F63
    H71 R52) and the official abstract: shift-share (Bartik) IV, robust
    negative effect of export shocks on residential land supply in China
    during 2008-2022, revenue-based fiscal consolidation, land-supply
    profits offsetting approximately 94 percent of tax-revenue losses,
    area expansion with stable prices, excessive urban expansion and
    housing-market risk, USD 124 million yearly commuting costs per
    percentage-point export-growth drop, and declining sustainability of
    the measure. The ScienceDirect full text is subscriber-only
    (unpaywall reports no open-access location on 2026-08-15), so all
    2008-2022 and 320-city details rest on this abstract plus screening
    text, not on inspected full text.
- id: E3
  source_type: official-data
  citation: '自然资源部不动产登记中心 (Ministry of Natural Resources Real Estate Registration Center). "中国土地市场网" (landchina.com), official national land-market disclosure and monitoring portal, guided by the MNR Department of Natural Resources Development and Utilization (自然资源部自然资源开发利用司).'
  url: https://www.landchina.com/
  date: '2026-08-15'
  supports:
  - identity.authority
  - identity.instrument
  - timeline.local_timing
  - assignment.exposure_construction
  - assignment.compliance
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: official-document
  locator: >
    landchina.com homepage fetched and read 2026-08-15. The site footer
    states that the portal is operated by the MNR Real Estate Registration
    Center (自然资源部不动产登记中心, also styled the MNR Legal Affairs
    Center), under the guidance of the MNR Department of Natural Resources
    Development and Utilization (自然资源部自然资源开发利用司), and
    references the national land-market dynamic monitoring and regulation
    system (土地市场动态监测与监管系统). This establishes landchina.com
    as the official MNR platform publishing primary-market land transfer
    (土地出让) records - the parcel-level source the paper names for land
    supply area, price, and revenue. It does not verify the paper's
    specific extraction of 279,534 residential parcels or the city-year
    aggregation.
- id: E4
  source_type: paper
  citation: 'Wang, Qiuyi, Jing Wu, and Shuping Wu. 2025. Journal of Urban Economics 149: 103796, DOI landing page (ScienceDirect), subscriber-only.'
  url: https://doi.org/10.1016/j.jue.2025.103796
  date: 2025
  supports:
  - identity.legal_identifiers
  - design_applications.doi
  verification_status: blocked
  access_level: metadata
  locator: >
    DOI resolution and the ScienceDirect article page (PII
    S0094119025000610) were attempted on 2026-08-15 and returned no
    extractable content (HTTP 400 on the abstract page); Unpaywall
    reports no open-access location for this DOI on 2026-08-15. The DOI
    record is retained for bibliographic matching only; all design
    content rests on E1 and the official abstract in E2.
design_applications:
- paper: "Export slowdown and increasing land supply: Local government's responses to export shocks in China"
  doi: 10.1016/j.jue.2025.103796
  journal: Journal of Urban Economics
  year: 2025
  research_question: Do Chinese city governments respond to negative export shocks by expanding revenue-oriented residential land supply to offset export-driven tax-revenue losses, and what are the urban-spatial costs of this fiscal-consolidation strategy?
  population: Prefecture-level Chinese cities, 2008-2022 (published; 326 cities 2007-2017 plus 2019-2020 COVID extension in the inspected conference version)
  outcome: Local tax revenue growth; revenue-oriented residential land supply revenue, area, and price growth; excessive built-up-area expansion; housing stock/supply/sales; commuting costs
  data_used:
  - GACC firm-level customs export records aggregated to city-year by HS two-digit chapter
  - SAT-MOF National Tax Survey Database 2008-2015 (about 680 thousand firms per year)
  - MNR landchina.com parcel-level land transfer records (279,534 revenue-oriented residential parcels, 2007-2017 in the conference version)
  - Ministry of Housing and Urban-Rural Development housing stock/supply/sale data; NBS built-up area and population
  treatment_encoding: Log-difference of city export value instrumented by the shift-share (leave-one-out national HS-chapter shifts, 2006-2007 base-period shares); city, year, and province-by-year fixed effects; city clustering; 5 percent winsorization
  comparison: Within province-year across cities with different base-period export composition; placebo land categories (non-revenue residential, industrial, secondary-market) isolate the fiscal-consolidation channel
  empirical_design: 2SLS shift-share IV first-difference panel with reduced-form, substitution-rate IV, asymmetry, heterogeneity, and unintended-cost exercises
  assumptions:
  - National HS-chapter export shifts are exogenous to city land-supply determinants conditional on the fixed effects (shifts-exogeneity)
  - The transmission runs through local tax-revenue losses rather than housing prices
  - NTSD tax coverage is representative enough to proxy local fiscal exposure
  threats_addressed:
  - Endogeneity of realized export growth via the shift-share instrument with leave-one-out shifts
  - Share endogeneity acknowledged; addressed through shifts-exogeneity balance tests
  - Housing-price confounding via controls and a secondary-market placebo
  - Domestic output and import shock confounding via direct controls
  - Shift-share inference via Adao et al. (2019) AKM/AKM0 intervals and province clustering
  evidence_refs:
  - E1
  - E2
  - E3
  - E4
method_transfer: null
readiness_blockers:
- The published JUE full text is subscriber-only (no open-access location per Unpaywall on 2026-08-15); the 2008-2022 period, the 320-city sample rule, the 94 percent offset figure, and the published commuting-cost estimate rest on the official abstract and screening text, not inspected full text. The fully inspected construction is the 2024 CES conference version (2007-2017, 326 cities, plus a 2019-2020 analogous COVID extension).
- The 320-city figure and the published panel span derive from publisher/RePEc-derived screening text; the EconPapers abstract verifies 2008-2022 but does not state the city count.
- GACC customs micro-data, the NTSD, and MNR parcel records are access-restricted or require scraping; the record stores the treatment contract, not acquisition paths (those belong in the companion data repository). Institutional grounding of the land-supply platform is verified through the MNR landchina.com portal (E3), but no official document independent of the paper was inspected for the customs and tax data constructions.
- Exporter-location assignment of customs exports and the 63 percent NTSD coverage of local tax revenue are measurement risks that any reuse must re-examine.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Chinese city governments rely on two revenue pillars: local tax revenue
shared with higher levels under the tax-sharing system, and revenue from
selling urban land use rights, over which they hold a local monopoly
[E1]. Residential land sold through revenue-oriented methods (tender,
English auction, two-stage auction) generates the bulk of land revenue -
according to the China Land and Resources Statistical Yearbook cited in
the paper, 97 percent of urban land supply revenue in 2017 came through
these methods [E1]. After the 2008 global financial crisis, China's
export growth - about 18 percent per year on average over 1992-2008 -
dropped sharply and stayed weak through the 2012-2019 slow-trade period
and the 2020 COVID-19 disruption, eroding the tax base of
export-exposed cities [E1]. Land supply revenue was RMB 1.03 trillion
in 2008, equivalent to 44 percent of local tax revenue, giving city
governments a margin on which to compensate [E1].

## What Changed

No domestic policy changed: the variation is the year-to-year
realization of national export demand by HS two-digit product chapter,
transmitted to cities through their fixed pre-sample export composition
[E1]. The canonical boundary of this record is the shift-share export
shock as constructed and used by Wang, Wu, and Wu (2025 JUE; 2024 CES
conference version): leave-one-out national chapter export changes
weighted by 2006-2007 city export shares, applied to city-level fiscal
and land-supply outcomes [E1, E2]. Related but distinct objects - the
US-China trade war tariff exposure designs, the Campante et al. (2021)
export-slowdown shift-share for labor unrest, and domestic land-quota or
housing-regulation policies - are outside this boundary even though the
paper builds on the same instrument family [E1; analytical inference on
the boundary].

## Implementation and Assignment

Each city inherits a predicted export shock equal to the weighted sum of
national chapter-level export changes, with weights fixed at the city's
2006-2007 export shares (alternatives: 2005-2007 and 2007) [E1]. The
endogenous regressor is realized city export growth from GACC customs
records; the instrument isolates the component driven by national
demand in the city's pre-sample export mix, and identification rests on
the exogeneity of the national shifts, supported by balance tests
against exposure-weighted baseline city characteristics [E1]. The
behavioral chain is then estimated in two 2SLS equations: export growth
raises local tax revenue growth (coefficient 0.217, 2009-2015) and
lowers revenue-oriented residential land supply revenue growth
(coefficient about -1.0 to -1.1, 2008-2017), with the land response
operating on the area margin at stable prices [E1]. The implied fiscal
substitution is near one-for-one in profits in the conference version
and approximately 94 percent of tax losses in the published abstract
[E1, E2].

## Why This Creates Empirical Variation

Chinese cities differ sharply in pre-sample export specialization, and
national chapter-level demand fluctuated violently after 2008, so the
shift-share interaction generates continuous, plausibly exogenous
city-year exposure variation within province-year cells [E1]. China's
land institutions give the design its placebo structure: if the response
were driven by a generic economic downturn or a housing-price boom
rather than fiscal consolidation, non-revenue-oriented residential
supply, industrial land supply, and secondary-market transactions should
move the same way - and they do not [E1]. The asymmetry of the response
(stronger for below-median shocks) further matches a
fiscal-consolidation motive rather than a symmetric demand channel [E1].

## Identification Risks

Identification rests on Borusyak et al. (2022) shifts-exogeneity, not on
any claim that export demand is intrinsically exogenous; the shares are
acknowledged as potentially endogenous [E1]. The main risks are
confounding by the 2008-2009 stimulus and other co-occurring national
policies beyond what province-by-year fixed effects absorb, the
decade-long housing boom as a background condition, exporter-location
measurement error in the customs data (intermediary firms), the 63
percent NTSD coverage of local tax revenue, and the unverified
extension of the construction to 2008-2022 and 320 cities in the
published version [E1, E2; the exporter-location and published-version
risks are analytical inference]. Inference is protected by city
clustering with province-clustering robustness and Adao et al. (2019)
AKM/AKM0 shift-share intervals [E1].

## Data Requirements

Reuse requires GACC firm-level customs records (exporter city, HS-8
product, USD value) to rebuild city-chapter export panels and the
leave-one-out instrument with 2006-2007 base shares; NTSD 2008-2015 (or
Finance Yearbook aggregates) for local tax revenue with statutory
sharing ratios; and MNR landchina.com parcel records with transaction
method, area, price, and revenue to construct revenue-oriented
residential land supply and the placebo categories [E1]. Housing and
built-up-area series are needed only for the unintended-cost exercises
[E1]. Dataset acquisition paths belong in the companion data
repository; this record stores only the treatment contract.

## Evidence Notes

E1 is the open 2024 Chinese Economists Society conference version, a
56-page full text with appendices, downloaded and read on 2026-08-15;
it establishes the instrument formula, base period, data construction,
fixed-effects structure, first-stage strength, results, placebos,
balance tests, and inference procedures for the 2007-2017 sample plus a
2019-2020 analogous COVID extension, but not the underlying restricted
datasets. E2 is the EconPapers/RePEc record with the official abstract
of the published JUE 2025 version, read directly on 2026-08-15; it
establishes publication identity and the 2008-2022 headline findings
(94 percent offset, USD 124 million commuting costs) but no
construction detail, and the ScienceDirect full text remained
subscriber-only with no open-access location. E3 is the MNR
landchina.com portal footer, read directly on 2026-08-15; it establishes
that the parcel-level land transfer source the paper names is the
official MNR land-market disclosure and monitoring platform, but not
the paper's specific extraction. E4 is the DOI landing record, retained
for bibliographic matching after the ScienceDirect page failed to yield
content. The 320-city sample count
comes from screening text and is recorded as reported, not verified. No
evidence in this record was built from search snippets, and nothing
here certifies the shock as exogenous beyond the paper's stated
shifts-exogeneity assumption.
