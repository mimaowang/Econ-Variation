---
schema_version: 2
id: china-two-control-zones-1998
name: China's 1998 Two Control Zones sulfur-dioxide and acid-rain regulation
aliases:
- Two Control Zones (TCZ)
- Acid Rain Control Zones and Sulfur Dioxide Pollution Control Zones
- 两控区
- 酸雨控制区和二氧化硫污染控制区
status: design-documented
provenance:
  task_id: task-37f78c6b6d4d
scope:
  country: China
  regions:
  - Prefectures containing listed acid-rain-control cities or listed sulfur-dioxide-control counties and districts
  - 27 provincial-level jurisdictions and 175 cities/areas in the official 2006 Ministry summary
  domains:
  - environmental-economics
  - regional-economics
  - firm-dynamics
  - industrial-economics
  - economic-development
  variation_type: event-shock
  knowledge_role: china-variation
  china_relevance: >
    The State Council approved mainland China's two pollution-control-zone designations
    in January 1998. The assignment is tied to Chinese prefectures and their listed
    constituent places; the principal inspected application studies industrial firms.
identity:
  instrument: >
    The State Council's 1998 approval of the Acid Rain Control Zones and Sulfur Dioxide
    Pollution Control Zones plan, commonly called the Two Control Zones (TCZ) regulation.
  authority: >
    The State Council approved the zones and national targets; the then-State Environmental
    Protection Administration published the delineation plan, while local governments and
    environmental, coal, and power authorities carried out implementation and enforcement.
  legal_identifiers:
  - State Council, 国函〔1998〕5号, 1998-01-12, on the Acid Rain Control Zones and Sulfur Dioxide Pollution Control Zones
  - State Environmental Protection Administration request 环发〔1997〕634号, identified in the State Council reply
  implementation_regime: >
    The official annex contains two related but geographically different schedules. Acid-rain
    control areas are generally named at city or prefecture level; sulfur-dioxide control areas
    include named districts and counties. The reply sets 2000 compliance and total-emissions
    targets and a 2010 ceiling tied to 2000 emissions. It also specifies measures for sulfur
    coal, power plants, and heavily polluting industries. A Ministry of Environmental Protection
    retrospective reports 175 cities/areas across 27 provincial-level jurisdictions. The program
    is not a uniform citywide dose: the applicable schedule and local enforcement matter.
  assignment_mechanism: >
    Authorities selected places using prior pollution and geography, not random assignment.
    Lu and Pless report criteria based on sulfur-dioxide concentrations and emissions for SO2
    zones and on precipitation acidity, sulfate deposition, and emissions for acid-rain zones.
    In their firm application, a prefecture is coded as regulated if it contains a listed TCZ
    district or county, accommodating administrative-boundary changes; firms inherit exposure
    from their recorded location. This aggregation is the paper's operational choice, not a
    separately verified rule of uniform enforcement across the whole prefecture.
  parent: null
  related_variations:
  - china-air-pollution-action-plan-firm-emissions
  - china-low-carbon-pilot-first-wave
timeline:
  announcement: '1998-01-12'
  effective: '1998-01-12'
  implementation_start: null
  implementation_end: null
  local_timing: >
    The State Council approval is dated 1998-01-12. In the January 2026 author manuscript,
    Lu and Pless treat 1998 as pre-policy and set Post=1 from 1999, explaining that local
    implementation lagged the central announcement. That is the paper's annual coding clock,
    not evidence that every listed place first enforced the policy in 1999. The reply names
    2000 and 2010 targets; later plans and accountability changes are not recoded here as
    separate onset dates or as a staggered rollout.
  anticipation: >
    The 1995 revision of the Air Pollution Prevention and Control Law had already introduced
    region-specific controls, and the 1998 designation followed a planning process. Local
    preparation may therefore predate the paper's 1999 post indicator. Researchers should
    inspect earlier policy exposure and pre-trends rather than assume 1996-1998 is an untouched
    baseline.
  last_verified: '2026-10-02'
assignment:
  unit: Industrial firm-year in the main application; prefecture-month in the paper's auxiliary SO2 validation profile
  treated: >
    In the main firm application, firms whose recorded address maps to a prefecture containing
    a listed TCZ place are treated from the paper's 1999 post period onward. The TCZ-by-post
    term is the geographic policy exposure. A separate industry indicator interacts with it to
    describe heterogeneous regulatory burden; it is not the zone-assignment rule itself.
  comparison_pool: >
    Firms in prefectures outside the official TCZ schedules provide the geographic comparison.
    Within regulated prefectures, the paper also compares firms in more versus less
    pollution-intensive industries; those contrasts answer different parts of its heterogeneous
    design and should not be collapsed into a single treated-versus-control coefficient.
  rule: >
    Reconstruct the two 1998 annexes, preserve their city-versus-county/district granularity,
    and map named historical places to the prefecture and firm-location codes used in the data.
    For the inspected paper, code TCZ_p x Post_1999. Do not infer assignment from contemporary
    pollution, a prefecture centroid, or the paper's reported result. The official acid-rain
    annex notes an exclusion for designated state-supported poverty counties; do not generalize
    that footnote to the separate SO2 annex without checking its entries.
  intensity: >
    The main geographic assignment is binary. Lu and Pless add a higher-pollution-industry
    indicator in TCZ x Post x Dirtier. Their manuscript describes ten more pollution-intensive
    industries using industry-level SO2 and coal shares, but its main-text note and Appendix A
    give different years for the underlying industry data (2002 versus 2001). Treat that
    interaction as a version-specific reported construction until reconciled with the final
    published article and supplement.
  exemptions:
  - Places not included in the relevant official annex are not treated merely because their prefecture is polluted.
  - The acid-rain-control annex contains a state-supported-poverty-county exclusion; its scope should not be applied to the SO2-control schedule by assumption.
  compliance: >
    The reply prescribes targets and measures, including sulfur-content restrictions, plant
    desulfurization or other controls, and industrial waste-gas treatment. Local governments
    retained implementation and enforcement responsibilities. The designation does not prove
    identical inspections, compliance, or treatment intensity for every firm.
  exposure_construction: >
    Join the archived 1998 annex to historical county/district and city boundaries, derive the
    paper's containing-prefecture indicator, then join firms by historical location and year.
    Keep the policy clock (Post from 1999) separate from the legal approval date. For the
    JPubE application, the geographic DID includes TCZ x Post; an additional triple interaction
    uses industry pollution intensity to compare effects within the regulated geography.
  required_identifiers:
  - Historical city, county, and district names or codes from the 1998 annex
  - Historical prefecture code and boundary crosswalk for 1996-2006
  - Stable firm identifier, recorded address/location code, and year
  - Two-digit Chinese Industrial Classification code
  - Industry SO2-emissions and coal-consumption shares for the heterogeneity application
  spillovers: >
    Pollution crosses administrative borders; regulated firms may relocate, shift suppliers,
    or affect competitors and labor markets outside treated prefectures. These effects can
    contaminate non-TCZ comparisons in either direction. Later national industrial and trade
    changes also differentially affected historically polluted, more industrialized places.
research_compatibility:
  outcome_domains:
  - Industrial-firm total factor productivity and factor use
  - Firm exit, sales, employment, capital, and intermediate inputs
  - Sulfur-dioxide emissions, removal, intensity, and ambient concentration
  - Environmental compliance and industrial upgrading
  affected_populations:
  - Chinese industrial firms in designated and non-designated prefectures
  - Workers in covered firms and industries
  - Residents of regulated and neighboring areas, when using area-level pollution outcomes
  mechanism_channels:
  - Pollution-abatement investment and compliance costs
  - Production-process upgrading and input efficiency
  - Firm exit, selection, and reallocation
  - Fuel substitution and sulfur-dioxide reduction
  - Local labor-market and competitor spillovers
  best_for:
  - Studying historical place-based environmental regulation and industrial-firm adjustment
  - Comparing regulated and non-regulated prefectures with explicit historical geography and timing
  - Examining whether industry pollution exposure changes the response to the same geographic regulation
  - Testing environmental enforcement with separate firm-pollution or prefecture-SO2 data
  not_good_for:
  - Treating designation as random or calling all 1998 approval areas uniformly enforced
  - Assuming a clean 1998 treatment year or a uniform 1999 local implementation date
  - Measuring current pollution effects from the 1996-2006 firm application
  - Estimating entry or small-firm effects from the listed-firm-survey panel alone
  - Using the paper's industry-intensity interaction before reconciling its baseline-year discrepancy
design:
  claim_type: reduced-form
  affordances:
  - One national designation date with geographically selected regulated places
  - A paper-used annual post period beginning in 1999
  - Firm-panel comparisons across designated prefectures and industries
  - A separate prefecture-month satellite SO2 validation application
  candidate_designs:
  - Firm-level geographic difference-in-differences with firm and industry-year fixed effects and prefecture-specific trends
  - A heterogeneous DID adding TCZ x Post x industry pollution intensity, with the stated version caveat
  - Prefecture-level DID for sulfur-dioxide concentration using a distinct monthly satellite-data profile
  - Event studies and sensitivity checks around the paper's annual implementation clock
  identifying_variation: >
    The paper compares changes after its 1999 implementation clock in firms located in listed
    TCZ prefectures with changes in firms outside those prefectures, conditional on fixed
    effects, prefecture-specific trends, and controls. The location choice was based on
    pollution and geography, so identification depends on conditional trends rather than
    random designation. Industry pollution intensity supplies a further heterogeneity contrast,
    not a second policy assignment.
  primary_strategy: >
    Lu and Pless estimate log firm outcomes on TCZ_p x Post_t and TCZ_p x Post_t x Dirtier_s,
    with firm fixed effects, industry-year effects, prefecture-specific linear trends, and a
    control for differential TCZ exposure after China's WTO entry; standard errors are clustered
    by firm. The reported coefficient on TCZ x Post is the change for less pollution-intensive
    firms relative to non-TCZ firms. The additional triple-interaction coefficient is the extra
    change for more pollution-intensive firms relative to less-intensive firms within TCZ areas;
    the total contrast for dirtier firms versus non-TCZ firms is the sum of both coefficients.
  estimand: >
    A conditional change in the outcomes of firms assigned to a TCZ prefecture after the
    paper's 1999 annual cutoff, relative to the specified non-TCZ comparison. The estimate is
    application- and population-specific; it is not the average effect of all environmental
    regulation or a national welfare effect.
  treatment_variable: TCZ prefecture x Post_1999; optional interaction with the paper's Dirtier industry indicator
  comparison_logic: >
    For the main coefficient, compare less-pollution-intensive firms in TCZ prefectures with
    firms in non-TCZ prefectures. The triple interaction asks whether dirtier industries change
    additionally relative to cleaner industries within the TCZ geography. Keep β1, β2, and
    β1+β2 interpretations distinct.
  estimation_notes: >
    The author manuscript reports an unbalanced panel of 127,699 industrial firms in 40
    two-digit industries over 1996-2006. CIED includes SOEs and private firms above the annual
    sales threshold; the main within-firm productivity sample requires observations on both
    sides of implementation. Exit is analyzed separately, with firms' last observed year used
    to construct an exit indicator and a panel balanced from 1998 onward. The manuscript also
    uses prefecture-level SO2 outcomes and NASA MERRA-2 concentration data. The checked paper
    source is the January 2026 author manuscript; its final journal identity is confirmed, but
    the published full text was not independently compared.
  assumptions:
  - Conditional on firm effects, industry-year effects, prefecture trends, and reported controls, treated and comparison firms would otherwise have followed comparable trends.
  - The historical annex is mapped to the correct prefecture and firm-location codes without using post-treatment pollution to assign treatment.
  - The paper's 1999 annual post indicator is a useful application clock despite unobserved local implementation differences.
  - The industry-intensity split is measured from a genuinely pre-policy distribution; the author-manuscript year discrepancy must be resolved before relying on this dimension.
  - Spatial spillovers, relocation, and concurrent industrial or trade shocks do not explain the full comparison.
  - Changes in survey coverage, firm identification, and outcome reporting do not generate the result.
  diagnostics:
  - Plot event-study leads around the 1999 annual cutoff and inspect 1996-1998 separately, recognizing that early CIED years are pilot data.
  - Compare specifications with prefecture-specific trends, alternative fixed effects, and the paper's WTO-by-TCZ control.
  - Rebuild the treatment crosswalk from the official annex and historical boundaries; report unmatched units.
  - For industry heterogeneity, verify the final publication's pollution-share year and reproduce both the 2001/2002 source discrepancy and the 1997 comparison.
  - Separate survivor productivity estimates from the paper's exit sample and test sensitivity to the private-firm sales threshold.
  - Compare China Environmental Yearbook measures with the paper's satellite SO2 profile and test neighboring-prefecture spillovers.
threats:
- type: endogenous-pollution-based-selection
  basis: documented
  condition: >
    The government selected zones because of pre-existing pollution and geography. The paper
    reports that treated prefectures were already more industrialized and had higher GDP per
    capita, population, and SO2 emissions. Prefecture trends mitigate some differential growth
    but do not make the assignment random or remove all changing local confounders.
  evidence_refs:
  - E1
  - E2
  - E4
  possible_diagnostics:
  - Pre-policy event-study leads and placebo timing
  - Alternative comparison groups and matching or reweighting with pre-policy covariates
  - Report the pollution-selected estimand and avoid extrapolating to cleaner regions
- type: administrative-crosswalk-and-treatment-timing
  basis: reported
  condition: >
    The legal schedules mix prefecture-level cities with county- and district-level locations,
    and boundaries changed during the application period. The paper aggregates listed counties
    or districts to their containing prefecture and uses 1999 as the first post year, but the
    crosswalk and local enforcement dates have not been independently reconstructed here.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Preserve the original listed units and document every historical boundary mapping
  - Compare prefecture aggregation with finer county/district exposure where data allow
  - Separate 1998 announcement, 1999 paper coding, and locally documented implementation dates
- type: industry-exposure-version-and-baseline
  basis: reported
  condition: >
    In the January 2026 author manuscript, a Section 3.1 note refers to 2002 as the initial
    industry-pollution data year while Appendix A refers to 2001 and compares it with 1997.
    Both are after the 1998 designation, so Dirtier may not be a clean pre-treatment intensity
    measure. This threatens the triple-interaction interpretation, not the existence of the
    underlying geographic TCZ assignment.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Reconcile the final journal text and appendix before coding Dirtier
  - Reconstruct industry shares from 1997 or earlier data where consistently available
  - Treat the geographic TCZ x Post contrast separately from the additional industry interaction
- type: industrialization-wto-and-concurrent-policy-trends
  basis: reported
  condition: >
    Historically polluted prefectures may respond differently to WTO accession, industrial
    restructuring, privatization, and later environmental plans. The paper controls for a
    TCZ-by-post-WTO term and local trends and discusses a 2003 productivity shift, but these
    controls do not prove that all concurrent place-based changes are removed.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Inspect 2001-2006 policy overlap and the 2003 shift in event-study results
  - Test alternative periods and exclude or separately model later environmental programs
  - Compare industry-, region-, and ownership-specific outcomes
- type: survey-selection-and-firm-location
  basis: reported
  condition: >
    CIED excludes private firms below its annual-sales threshold and has smaller pilot-year
    samples; the main within-firm productivity sample requires observations both before and
    after implementation. Reported addresses may not identify all production sites. These
    limits affect small firms, entrants, exit interpretation, and location-based exposure.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Analyze exit separately from incumbent productivity and test the sales-threshold sensitivity
  - Drop 1996-1997 pilot years and report how composition changes
  - Check firm-code, city-code, and address changes; compare multiple-site or relocation cases
- type: interference-and-pollution-spillovers
  basis: reported
  condition: >
    Pollution transport, competitor substitution, labor movement, and relocation can transmit
    the policy to nominally untreated prefectures. The paper explicitly identifies no-spillover
    exposure as an assumption and tests several consequences, but local and cross-border effects
    remain part of the interpretation.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Estimate neighboring-prefecture and distance-band effects
  - Compare firm outcomes with prefecture-level satellite pollution outcomes
  - Track relocation or border-firm sensitivity where identifiers permit
empirical_requirements:
  contract_version: 1
  population: Industrial firms covered by the China Industrial Enterprise Database (CIED), with the inspected paper's survey limits
  observation_unit: Firm-year
  geography_level: Historical county/district-to-prefecture mapping and firm location
  time_start: 1996
  time_end: 2006
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields:
  - Stable firm identifier, annual year, and location/address or city code
  - Historical county/district and prefecture identifiers or an auditable geographic crosswalk
  - Two-digit industry code and industry-year classification
  - Labor, capital, output or value added, and intermediate-input measures
  - Ownership and firm-survey inclusion/sales-threshold fields
  - Industry SO2-emissions and coal-consumption shares if using the pollution-intensity interaction
  required_identifiers:
  - firm_id
  - year
  - historical_prefecture_code
  - historical_county_or_district_code
  - industry_code
  treatment_key:
  - official_1998_TCZ_schedule
  - historical_place_to_prefecture_crosswalk
  - Post_1999_paper_clock
  - optional_Dirtier_industry_indicator
  treatment_source: >
    State Council Reply Guohan [1998] 5 and its two official zone annexes, combined with the
    paper's stated containing-prefecture rule and a documented historical boundary crosswalk.
  measurement_risks:
  - The annex includes different administrative levels; current administrative codes may misclassify historical exposure.
  - The paper's annual 1999 clock is not a uniform local implementation date.
  - Private-firm survey coverage excludes firms below the sales threshold; pilot-year coverage is smaller and more SOE-heavy.
  - Main within-firm productivity results do not represent entry and all exits; the paper constructs a separate exit sample.
  - The pollution-intensity baseline year is inconsistent in the inspected author manuscript.
design_profiles:
- id: prefecture-satellite-sulfur-dioxide
  label: Prefecture-month satellite SO2 outcome and enforcement check
  design_families:
  - difference-in-differences
  when_to_use: >
    Use when the outcome is ambient prefecture-level sulfur-dioxide concentration rather
    than firm productivity. This is the paper's separate validation design and has a different
    unit, frequency, time span, and data join; do not combine its requirements with CIED.
  outcome_domains:
  - ambient sulfur-dioxide concentration
  - environmental enforcement
  requirements:
    population: Mainland China prefectures with usable satellite SO2 and boundary data
    observation_unit: Prefecture-month
    geography_level: Prefecture, created from 60-by-50-kilometer satellite grid cells by nearest-neighbor remapping
    time_start: 1988
    time_end: 2008
    minimum_frequency: monthly
    minimum_pre_periods: 24
    minimum_post_periods: 24
    required_fields:
    - SO2 Surface Mass Concentration from MERRA-2
    - TCZ prefecture indicator and paper-coded post-1999 year
    - Prefecture identifier and month/year
    - Weather fields for the paper's weather-controlled specification
    required_identifiers:
    - prefecture_code
    - year_month
    - satellite_grid_cell
    treatment_key:
    - TCZ_prefecture
    - Post_1999
evidence:
- id: E1
  source_type: policy-document
  citation: State Council. 1998-01-12. Official Reply Concerning Acid Rain Control Zones and Sulfur Dioxide Pollution Control Zones, 国函〔1998〕5号.
  url: https://www.mee.gov.cn/zcwj/gwywj/201811/t20181129_676362.shtml
  date: '1998-01-12'
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.announcement
  - timeline.effective
  - assignment.rule
  - assignment.exemptions
  - assignment.compliance
  verification_status: verified
  access_level: official-document
  locator: >
    MEE's official reproduction: header and State Council reply paragraphs 1-7, including
    approval of the two-zone delimitation and attachments; attachment 1's area table and
    attachment 2's separate SO2-control-area schedule. Paragraphs 2-5 state 2000/2010
    targets and controls concerning sulfur coal, power plants, industrial waste gas, and
    implementation responsibilities. The schedules mix administrative levels and do not
    themselves provide a modern prefecture-code crosswalk.
- id: E2
  source_type: paper
  citation: >
    Lu, Yangsiyu, and Jacquelyn Pless. 2026. Greening to Grow: Evidence from Environmental
    Regulation and Industrial Firm Productivity in China. January 28, 2026 author manuscript,
    84 pages; subsequently published in Journal of Public Economics 256, 105596.
    DOI: 10.1016/j.jpubeco.2026.105596.
  url: https://jacquelynpless.com/wp-content/uploads/2026/01/LuPless_EnviroRegProd_28jan2026.pdf
  date: '2026-01-28'
  supports:
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
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
  - empirical_requirements.observation_unit
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - design_applications.paper
  - design_applications.research_question
  - design_applications.treatment_encoding
  - design_applications.empirical_design
  verification_status: verified
  access_level: full-text
  locator: >
    Author-hosted manuscript inspected in memory: pp. 7-8 (TCZ background and criteria),
    pp. 11-15 (Eq. 1, 1999 post clock, comparison, data, TCZ status and industry exposure),
    pp. 25-30 (spillover, trend and exit discussion), pp. 55-61 (main figures and online
    data-preparation appendix, including firm linkage and industry-intensity timing). The
    geographic treatment and paper's own caveats are source-reported; the underlying CIED
    construction and administrative crosswalk were not independently reproduced.
- id: E3
  source_type: paper
  citation: Jacquelyn Pless, Publications, listing Lu and Pless (2026), Journal of Public Economics, with published-version and working-paper links.
  url: https://jacquelynpless.com/research/
  date: 2026
  supports:
  - design_applications.paper
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
  verification_status: verified
  access_level: metadata
  locator: >
    Author publications page, lines 19-23: title, coauthor, 2026 Journal of Public Economics publication,
    publisher link, and separate working-paper link. It verifies bibliographic identity, not equivalence
    of the author manuscript and final article.
- id: E4
  source_type: official-data
  citation: Ministry of Environmental Protection. 2006-06-07. 中国的环境保护, section “两控区污染防治”.
  url: https://www.mee.gov.cn/home/ztbd/sjhjr/2006hjr/xgbd/200606/t20060607_77198.shtml
  date: '2006-06-07'
  supports:
  - identity.implementation_regime
  - scope.regions
  verification_status: verified
  access_level: official-document
  locator: >
    Section III, paragraph “两控区污染防治”: reports the 1998 approval, 27 provincial-level
    jurisdictions, 175 cities/areas, approximate area, and 2005 SO2-control-zone air-quality
    comparisons. It is an official retrospective, not a machine-readable treatment roster.
- id: E5
  source_type: scholarship
  citation: Lu, Yangsiyu, and Jacquelyn Pless. 2026. Greening to Grow. Journal of Public Economics 256, 105596.
  url: https://doi.org/10.1016/j.jpubeco.2026.105596
  date: 2026
  supports:
  - design_applications.doi
  verification_status: verified
  access_level: metadata
  locator: >
    DOI and bibliographic metadata cross-checked against the author's publication listing and
    the University of Oxford INET publication record. The publisher landing page returned 403
    during this inspection, so this source establishes publication identity only, not the final
    article's design details.
design_applications:
- paper: "Greening to Grow: Evidence from Environmental Regulation and Industrial Firm Productivity in China"
  doi: 10.1016/j.jpubeco.2026.105596
  journal: Journal of Public Economics
  year: 2026
  research_question: How did the 1998 Two Control Zones regulation affect industrial-firm productivity and adjustment, and did responses differ with pollution intensity and ownership?
  population: >
    The author manuscript reports an unbalanced panel of 127,699 firms in 40 two-digit
    industries, 1996-2006. CIED includes state-owned firms and private firms above the annual
    sales threshold; the within-firm productivity sample requires observations before and
    after the policy. Exit is analyzed with a separately constructed panel.
  outcome: >
    Firm TFP and single-factor productivity, exit, output, sales, labor, capital, intermediate
    inputs, wages, and pollution measures; area-level SO2 is used for a separate enforcement
    validation.
  data_used:
  - China Industrial Enterprise Database / Annual Survey of Industrial Firms (CIED), 1996-2006
  - State Council 1998 zone schedules and historical firm location information
  - China Statistical Yearbook industry emissions and coal-consumption data for the paper's industry split
  - China Environmental Yearbook and China Environmental Statistics Dataset for pollution measures
  - NASA MERRA-2 monthly SO2 concentration data for prefecture-level validation
  treatment_encoding: >
    TCZ prefecture x Post, with Post beginning in 1999 and 1998 treated as pre; add TCZ x
    Post x Dirtier for the paper's heterogeneity estimate. The Jan 2026 manuscript differs
    on whether the industry-intensity source year is 2001 or 2002; do not silently choose one.
  comparison: >
    Non-TCZ prefectures form the geographic comparison. The main TCZ x Post coefficient
    describes less-pollution-intensive firms relative to non-TCZ firms; the triple interaction
    describes the additional change for dirtier versus cleaner industries in TCZ areas.
  empirical_design: >
    A single-date geographic DID with an industry-heterogeneity interaction, firm fixed effects,
    industry-year effects, prefecture-specific linear trends, a WTO-by-TCZ control, and
    firm-clustered standard errors. This is not a staggered city adoption design.
  assumptions:
  - Conditional outcome trends would be comparable between TCZ and non-TCZ places absent the regulation.
  - The 1999 annual application clock captures the relevant local implementation period.
  - Historical TCZ schedules are accurately joined to firm prefectures and locations.
  - Industry-intensity classification is not materially altered by the policy; the author manuscript's 2001/2002 source-year discrepancy limits interpretation of the triple interaction, not the core geographic TCZ x Post term.
  - Spatial spillovers and later trade or industrial changes do not explain the full contrast.
  threats_addressed:
  - Firm and industry-year fixed effects and prefecture-specific trends
  - WTO-by-TCZ control and discussion of the post-2003 shift
  - Event-study leads, alternative fixed effects, and omission of CIED pilot years
  - Satellite-based SO2 checks alongside administrative emissions data
  - Separate exit analysis and sensitivity to the private-firm sales threshold
  evidence_refs:
  - E1
  - E2
  - E3
  - E4
  - E5
method_transfer: null
readiness_blockers: []
superseded_by: null
deprecation_reason: null
---

## Institutional Background

By the 1990s, sulfur-dioxide emissions and acid deposition had become regionally concentrated
problems. The 1995 amendment to China's Air Pollution Prevention and Control Law allowed
stronger rules in designated pollution regions. On 12 January 1998, the State Council approved
the plan delimiting Acid Rain Control Zones and Sulfur Dioxide Pollution Control Zones
(国函〔1998〕5号). Its annexes name the covered places, while the reply sets emissions and air-quality
targets for 2000 and 2010 and describes controls on high-sulfur coal, power plants, and industrial
waste gas [E1]. A later Ministry retrospective reports 175 cities or areas across 27 provincial-level
jurisdictions; that count describes the program's reach, not a ready-made modern prefecture panel
[E4].

The two schedules should remain distinguishable. The acid-rain list is largely city- or
prefecture-oriented; the SO2 list includes sub-prefecture counties and districts. The State Council
approved named geography, not an experiment in which otherwise similar places were randomly
assigned. Places entered because of pollution conditions, so covered areas were already more
industrial and economically different. The program's legal designation is real and useful; its
designation is not proof that local enforcement began on one common date or had the same strength
everywhere.

## What Changed

The 1998 reply connected air-quality goals to administrative responsibilities and industrial
adjustment. It restricted high-sulfur coal, required controls for certain power plants and heavily
polluting industries, and instructed local authorities and relevant departments to prepare plans and
ensure implementation [E1]. This makes the policy relevant to environmental economics, industrial
development, and firm dynamics—not just ambient pollution. But a firm may face a different burden
depending on its location, industry, technology, state ownership, and local government's enforcement.

Keep this 1998 designation separate from later plans, assessments, and broader clean-air policies.
Those may affect the same places, but they do not turn the original TCZ schedule into a later
staggered rollout. The JPubE paper uses 1999 as its first post year and expressly treats 1998 as
pre because local implementation followed the central announcement [E2]. That is a defensible
paper-specific annual clock to study, not a verified common local start date.

## Implementation and Assignment

In Lu and Pless's 2026 author manuscript, the firm-level rule begins with the official list. A firm
is exposed if its recorded location maps to a regulated prefecture; for the SO2 schedule, the authors
count a prefecture as regulated when it contains a listed TCZ district or county, partly to handle
administrative-division changes. They then code the post period from 1999 [E2]. The historical list
and this aggregation rule are the assignment bridge. Do not substitute today's boundaries, use
current pollution to infer treatment, or assume that every firm inside a large prefecture received
the same inspection.

The paper's main regression uses `TCZ × Post`; the additional `TCZ × Post × Dirtier` term asks
whether more pollution-intensive industries responded differently within the same geography.
That industry classification is not a second policy assignment. The manuscript's main-text note
and its online appendix name different source years for the industrial pollution shares (2002 and
2001); until the final version is reconciled, treat that dimension as unresolved rather than
pretending its baseline status is settled [E2].

## Why This Creates Empirical Variation

The paper combines a fixed geographic designation with a before/after comparison. It reports 127,699
industrial firms in an unbalanced 1996–2006 panel, using CIED data, firm fixed effects, industry-year
effects, prefecture-specific trends, and a control for different TCZ exposure after WTO accession
[E2]. Its main TCZ coefficient is the change for less-pollution-intensive firms relative to firms
outside TCZ prefectures; the triple-interaction coefficient is the additional change for dirtier
industries relative to cleaner ones in regulated areas. The sum, not the interaction alone, is the
reported contrast for dirtier firms against the outside comparison group.

This is a conditional difference-in-differences design, not randomized placement. The authors
explicitly note selection by historical pollution and the accompanying differences in
industrialization; they add prefecture trends and other controls, but those adjustments do not prove
that all differential changes have been removed [E2]. The paper also studies a separate
prefecture-month SO2 outcome using satellite observations. That outcome has a different data
contract, so it is separated in `design_profiles` rather than mixed into the firm-year requirements.

## Identification Risks

Three interpretation boundaries matter most. First, the designated locations were pollution-selected
and were already more industrialized; the design needs credible conditional trends, not a claim that
the policy was exogenous by construction [E2]. Second, the paper's 1999 indicator compresses local
implementation into an annual clock. The annex also mixes administrative levels, so an incorrect
historical crosswalk can misassign firms even when the policy document itself is clear [E1, E2].

Third, the comparison can be affected by WTO-era demand, restructuring, later pollution policy,
pollution transport, firm movement, and labor or competitor spillovers. The paper discusses these
issues and uses several controls and checks, but the resulting coefficient remains tied to its sample
and model [E2]. Its CIED productivity panel also does not stand in for every firm: small private
firms fall below the survey threshold, early years are pilot observations, and the within-firm
productivity sample differs from the separate exit analysis. The paper does not credibly estimate
entry from that panel [E2].

## Data Requirements

A firm-level study needs the official schedules, historical county/district and prefecture boundaries,
firm identifiers and addresses, industry codes, annual outcomes, and enough pre- and post-period
observations to inspect trends. Productivity work additionally needs labor, capital, output or value
added, and intermediate inputs; a heterogeneous exposure study needs the industry-pollution source
and its reference year. The record does not store CIED or recreate its firm joins. The companion
data repository is the place for lawful access routes and data-specific reconstruction limits.

For area-level pollution, use the separate satellite profile: prefecture-month SO2 mass
concentration, grid-to-prefecture assignment, and weather data over the paper's 1988–2008 window.
This can help check whether the regulatory contrast is visible in pollution measures, but it is not a
substitute for reconstructing firm exposure or establishing the exclusion of other local shocks.

## Evidence Notes

E1 is the official State Council reply reproduced by the Ministry of Ecology and Environment; its
annexes establish the named-zone boundary source and the reply establishes the formal targets and
measures. E4 is an official retrospective that summarizes the number and geographic reach of
designated areas. E2 is the inspected 84-page January 2026 author manuscript; it establishes what
that version reports about assignment, sample, models, and limitations, not independent reproduction
of CIED or the historical crosswalk. E3 confirms the 2026 Journal of Public Economics publication
identity through the author's publication page. The final publisher full text was not compared with
the author version, and the industry-intensity year discrepancy remains open. Recency is a light
sorting signal only; the underlying variation is the 1998 policy, not a 2026 intervention.
