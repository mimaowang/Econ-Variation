---
schema_version: 2
id: china-housing-purchase-limits-rent-tax-substitution
name: China Housing Purchase Limits and Rent-Tax Substitution
aliases:
- Housing Purchase Limits Policy (HPLP)
- China home-purchase restriction fiscal squeeze
- 中国住房限购与租税替代
- 住房限购政策
status: grounded
provenance:
  task_id: task-e6f648e1ff1b
scope:
  country: China
  regions:
  - City-level panels covering HPLP cities and comparison cities in the paper sample
  - The 46-city policy harmonization set reported in a related scholarly appendix
  domains:
  - regional-economics
  - urban-economics
  - housing
  - land
  - public-finance
  - firms
  - local-government
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    The variation is a city-specific housing-purchase restriction that changes the
    demand for residential property and, through local land finance, the revenue
    environment faced by city governments. Zhao and Zhang use the staggered policy
    exposure to study a rent-to-tax substitution in local revenue and the resulting
    tax burden, investment, employment, and wage outcomes of local firms. It is not
    the same object as a housing-price outcome, a land-supply reform, or a generic
    housing-market boom.
identity:
  instrument: >
    A city-level Housing Purchase Limits Policy (HPLP), implemented through local
    limits on the number of homes a household may buy and eligibility checks for
    non-local buyers. The national 2010 notice authorized cities with overheated
    housing markets to impose temporary purchase limits; local notices determined
    the household, property-count, tax, and social-insurance conditions. Beijing's
    2010 and 2011 notices provide a dated example, while other cities used different
    thresholds, dates, and later relaxation rules.
  authority: >
    The State Council set the 2010 national housing-market-control framework and
    allowed local governments to limit purchases. Municipal housing, construction,
    land, tax, and registration agencies translated that authorization into city
    rules and checked household qualifications. This is an administrative policy
    regime, not an assigned experiment; the paper's quasi-experimental leverage
    comes from differences in city adoption timing and the resulting fiscal squeeze.
  legal_identifiers:
  - State Council, Guofa [2010] No. 10, 2010-04-17 (国发〔2010〕10号)
  - Beijing municipal implementation notice, Jingzhengfa [2010] No. 13, 2010-04-30 (京政发〔2010〕13号)
  - Beijing housing-purchase qualification notice, Jingjianfa [2011] No. 65, 2011-02-16 (京建发〔2011〕65号)
  - City-specific HPLP notices and relaxation/abolition notices, to be archived per city
  implementation_regime: >
    The national framework did not give every city the same treatment. A local rule
    could restrict purchases by an existing homeowner, cap additional purchases,
    suspend sales to households with too many homes, or require non-local households
    to document local tax or social-insurance contributions. Housing developers,
    brokers, registration windows, housing departments, and sometimes banks enforced
    the rule. City adoption, effective dates, exemptions, and later relaxation must
    therefore be stored as a city-versioned policy table rather than inferred from a
    national post dummy.
  assignment_mechanism: >
    At the institutional level, a city enters treatment when its local HPLP becomes
    operative. At the paper level, a city-year is treated when the HPLP is active,
    and a firm is exposed through the city of its headquarters. The household-level
    eligibility rule is a separate layer: a treated city does not mean that every
    household, firm, land parcel, or transaction received the same restriction.
  parent: null
  related_variations:
  - china-city-county-merger-consolidation
  - china-misallocation-trade-liberalization
timeline:
  announcement: '2010-04-17'
  effective: null
  implementation_start: 2010
  implementation_end: null
  local_timing: >
    The State Council issued the national framework on 17 April 2010. Beijing's
    first city notice is dated 30 April 2010, and its detailed qualification notice
    began applying the purchase limit from 17 February 2011. A scholarly appendix
    reports 46 cities adopting between April 2010 and 2011, with many cities later
    relaxing or abolishing restrictions in 2014-2015 while several first-tier cities
    retained them. The paper studies 2008-2015, which is its observation window, not
    a claim that one identical rule existed throughout that period.
  anticipation: >
    Housing-market participants could anticipate a local restriction from national
    announcements, local drafting, public discussion, or housing-price pressure
    before the local notice. A city-year post indicator must not be interpreted as
    proof that no transactions or fiscal responses occurred between announcement,
    detailed implementation, and first full year. The paper's exact anticipation
    window and city-specific coding remain to be recovered.
  last_verified: '2026-08-13'
assignment:
  unit: >
    City-year for local-government revenue outcomes, with firm-year observations
    nested in the headquarters city for the firm outcomes. Household eligibility,
    property transactions, land auctions, and firm headquarters are distinct units
    and should not be collapsed into one treatment variable.
  treated: >
    A city-year is treated after that city's HPLP adoption/effective date; a firm is
    exposed when its headquarters city is treated in the relevant year. The policy
    rule itself applies to qualifying household purchases of residential property,
    not automatically to every firm, commercial parcel, or industrial-land market.
  comparison_pool: >
    Cities that had not yet adopted, or did not adopt within the paper's sample
    window, supply the natural comparison pool subject to the paper's sample and
    fixed-effect choices. The exact city sample and treatment coding are not exposed
    in the accessible abstract and must be checked against the full paper before a
    replication treats never-treated and not-yet-treated cities as interchangeable.
  rule: >
    Encode each city's dated local rule and its version. For example, Beijing's 2011
    notice allowed a local household with one home to buy one more, suspended sales
    to local households with two or more homes and to non-local households already
    owning a home, and required non-local households without local housing to show a
    valid residence permit plus five years of local tax or social-insurance records.
    These are an example of the assignment boundary, not a universal rule for all
    HPLP cities.
  intensity: >
    The paper's core exposure is a city HPLP indicator and adoption timing. Possible
    secondary margins are the number-of-home cap, non-local qualification duration,
    property types covered, enforcement intensity, and whether a city later relaxed
    the rule. No such intensity should be filled in without a dated local notice.
  exemptions:
  - Household hukou or local-residence categories can receive different treatment
  - Existing home count, first/second/additional home status, and household composition
  - Non-local households may need tax or social-insurance histories and may face stricter limits
  - Military, talent, or other locally specified categories may receive exceptions
  - Commercial and industrial land or non-residential transactions are not automatically covered
  compliance: >
    Developers, brokers, and registration windows collected household forms and
    ownership information; housing authorities checked eligibility and could block
    online signing or registration. The Beijing notice also requires cross-agency
    qualification checks and preserves the distinction between a city being under a
    rule and a particular household successfully taking up a purchase.
  exposure_construction: >
    Build a city-version policy table from local notices: announcement date, first
    enforceable date, rule version, covered purchase types, relaxation/abolition date,
    and source locator. Merge the dated city key to city-year revenue data and to
    firms through headquarters-city identifiers. Keep national announcement, local
    notice, first-full-year, and abolition clocks separate; do not replace them with
    a single 2010 dummy.
  required_identifiers:
  - Stable prefecture-level city code and historical administrative crosswalk
  - City-specific HPLP notice, effective date, rule version, and relaxation/abolition date
  - Local-government total revenue, land-lease revenue, tax revenue, and accounting definitions
  - Stable firm identifier, headquarters city, fiscal year, and firm ownership/industry fields
  - Firm tax burden, corporate income tax and business tax fields where used
  - Firm investment, employment, wages, land holdings, and relevant balance-sheet outcomes
  - Housing or land price series and local credit/policy controls for mechanism checks
  spillovers: >
    A purchase restriction can lower residential and commercial land demand, change
    local land-lease receipts, shift household and migrant location choices, and alter
    firms' collateral, credit, investment, hiring, and wage decisions. Households and
    firms can move across city borders, and land-price or tax-enforcement responses
    can reach untreated cities. These spillovers are part of the fiscal and urban
    equilibrium and must not be treated as absent merely because the policy is coded
    at city level.
research_compatibility:
  outcome_domains:
  - Local-government revenue composition and land-finance dependence
  - Corporate income-tax and business-tax burdens
  - Firm investment, employment, wages, innovation, and land holdings
  - Residential and commercial land prices and development activity
  - Housing demand, migration, household sorting, and urban expansion
  - Local fiscal capacity and public-finance responses to housing-market shocks
  affected_populations:
  - Households and migrants subject to city purchase eligibility rules
  - Local governments and agencies reliant on land-lease revenue
  - Firms headquartered in adopting and comparison cities
  - Developers, land sellers, brokers, and local tax authorities
  - Workers whose investment, employment, or wages respond to firm-level fiscal pressure
  mechanism_channels:
  - Reduced housing demand and land-lease revenue
  - Local-government substitution toward tax collection
  - Higher firm tax burdens and changed tax composition
  - Collateral, credit, and investment responses to land-price changes
  - Firm relocation, labor demand, and wage adjustment
  - Household and firm sorting across city borders
  best_for:
  - City-level studies of land finance and local tax enforcement
  - Firm-level responses to a housing-demand and fiscal-revenue shock
  - Staggered-policy event studies with explicit city-version coding
  - Research connecting urban housing regulation to firm investment and labor outcomes
  - Mechanism work that separately measures land-lease and tax channels
  not_good_for:
  - Treating HPLP adoption as random or identical across cities
  - Estimating a nationwide housing-price effect without city-specific policy histories
  - Calling household eligibility, firm headquarters, and property exposure the same treatment
  - Measuring tax enforcement or firm welfare without the underlying fiscal and firm records
  - Combining HPLP with land-supply, mortgage, or later housing reforms without an overlap audit
design:
  claim_type: causal
  affordances:
  - Staggered city adoption between 2010 and 2011 with later relaxation in many cities
  - Pre-policy city-year observations in the 2008-2015 study window
  - City revenue outcomes and firm outcomes linked through headquarters geography
  - Separate land-lease and tax-revenue channels
  - Housing and land-price mechanisms that can be checked before interpreting firm outcomes
  candidate_designs:
  - Staggered difference-in-differences or event study using city adoption dates
  - City fiscal-panel design for land-lease and tax-revenue shares
  - Firm-year design with headquarters-city HPLP exposure and firm fixed effects
  - Land-price first-stage followed by firm investment or employment outcomes
  - Triple differences by firm land holdings, ownership, or exposure to local tax enforcement
  - Cohort-specific or stacked designs that respect relaxation and first-tier exceptions
  identifying_variation: >
    The paper uses the timing of a city's HPLP as a housing-demand shock that reduces
    the land-lease-revenue base and changes the local government's revenue mix. The
    resulting city-year exposure is joined to local firms to study tax burden and
    real outcomes. The useful contrast is across cities and dates conditional on the
    paper's sample and controls, not a claim that national housing policy was
    externally assigned to cities.
  primary_strategy: >
    Zhao and Zhang describe a quasi-experimental HPLP variation over 2008-2015. A
    reconstruction should use the paper's exact city adoption table and estimator,
    then compare city fiscal outcomes and firm outcomes around each local adoption
    date. If a modern staggered-DID estimator is substituted, report that choice and
    preserve the paper's original timing definition rather than silently rewriting it.
  estimand: >
    The local effect of a city's HPLP adoption on its revenue composition and on the
    tax burden, investment, employment, and wages of firms linked to that city, over
    the paper's 2008-2015 window and comparison pool. This is not the general-
    equilibrium effect of all housing regulation on every Chinese city or a direct
    estimate of household welfare.
  treatment_variable: >
    City-year HPLP_active, constructed from the city-specific effective date and
    local rule version. Alternative specifications may use announcement, first
    full year, or abolition dates, but those clocks must remain separate. Firm
    exposure is HPLP_active merged by headquarters city and year.
  comparison_logic: >
    Compare adopting cities with cities not yet treated or not treated in the paper
    sample, using city and year fixed effects and the paper's additional controls.
    Validate the comparison with pre-trends, city-specific adoption predictors,
    alternative cohorts, and a clear treatment of cities that relaxed the policy.
    The exact original comparison logic remains a full-text recovery item.
  estimation_notes: >
    Keep revenue shares and levels separate, report land-lease and tax channels rather
    than treating total revenue as the only outcome, and distinguish city fiscal
    effects from firm-level pass-through. Do not infer tax enforcement from a firm tax
    burden coefficient alone without checking tax-base composition, firm entry/exit,
    relocation, and concurrent housing, credit, and land policies.
  assumptions:
  - Conditional city trends would not diverge exactly at HPLP adoption for reasons unrelated to the policy
  - City adoption dates and rule versions are measured from contemporaneous notices
  - Revenue accounting and firm identifiers are comparable over the study window
  - National and local housing, credit, land, and tax reforms do not explain the full contrast after audit
  - Headquarters-city exposure is a meaningful link for the firm outcomes being studied
  - Cross-city migration, firm relocation, and land-market spillovers are measured or interpreted as part of the estimand
  diagnostics:
  - Cohort-specific event-study leads and pre-trend plots
  - Alternative announcement, effective, first-full-year, and abolition clocks
  - City-level adoption predictors, policy-intensity versions, and leave-one-city-out checks
  - Separate land-lease revenue, tax revenue, total revenue, and fiscal-ratio outcomes
  - Residential, commercial, and industrial land-price placebo or mechanism series
  - Firm entry, exit, relocation, headquarters changes, ownership, and land-holding heterogeneity
  - Overlap audit for credit tightening, property-tax/land-tax enforcement, stimulus, and other local reforms
threats:
- type: endogenous-city-adoption
  basis: documented
  condition: >
    The national notice targeted overheated or high-pressure housing markets, and
    cities chose local timing and rule strength. Adopting cities may therefore have
    different housing trends, migration, fiscal stress, or political priorities before
    the notice.
  evidence_refs:
  - E1
  - E2
  - E5
  possible_diagnostics:
  - City-specific event-study leads and pre-policy housing/land trends
  - Adoption-predictor balance and alternative comparison pools
  - Cohort-specific estimates and leave-one-city-out checks
- type: anticipation-and-policy-versioning
  basis: reported
  condition: >
    National announcements, drafting, and local implementation preceded or followed
    one another, while city rules were relaxed at different dates. A single post-year
    can mix anticipation, active restriction, and partial relaxation.
  evidence_refs:
  - E2
  - E3
  - E5
  possible_diagnostics:
  - Separate announcement, effective, first-full-year, and abolition indicators
  - Lead coefficients and dated local-policy archive
  - Rule-version and exemption heterogeneity
- type: fiscal-channel-confounding
  basis: inferred
  condition: >
    The same housing pressure that motivated HPLP may change local land supply, credit,
    construction, investment, or tax enforcement through channels not captured by
    land-lease revenue. The rent-to-tax interpretation requires those channels to be
    measured rather than assumed away.
  evidence_refs:
  - E1
  - E4
  possible_diagnostics:
  - Land-price and land-transaction mechanism series
  - Commercial and industrial land placebos
  - City credit, construction, and other housing-policy controls
- type: firm-city-linkage-and-selection
  basis: reported
  condition: >
    A headquarters-city merge may miss branch activity, relocation, ownership changes,
    or selective firm exit. Firm tax burden and employment estimates can therefore
    reflect sample composition as well as local fiscal pressure.
  evidence_refs:
  - E4
  possible_diagnostics:
  - Stable firm-ID and headquarters crosswalks
  - Entry, exit, relocation, and ownership checks
  - Balanced panels and outcomes not dependent on tax reporting intensity
- type: spatial-spillover
  basis: inferred
  condition: >
    Households, firms, land demand, and tax bases can move to nearby cities. Untreated
    cities may therefore be affected, and a city-level comparison can measure a local
    equilibrium response rather than an isolated treatment effect.
  evidence_refs:
  - E4
  - E5
  possible_diagnostics:
  - Neighbor-city exposure and border-distance measures
  - Migration and firm-relocation outcomes
  - Wider comparison rings and spatially clustered uncertainty
- type: revenue-and-tax-measurement
  basis: reported
  condition: >
    Land-lease revenue, tax revenue, corporate income tax, business tax, and total
    revenue can be defined or recorded differently across cities and years. A share
    change can also arise from accounting or denominator changes rather than a real
    enforcement response.
  evidence_refs:
  - E4
  possible_diagnostics:
  - Archive accounting definitions and deflators
  - Levels, shares, and alternative revenue denominators
  - Tax composition, reporting, and missingness checks
empirical_requirements:
  contract_version: 1
  population: Chinese cities and firms observed during the HPLP adoption and comparison period
  observation_unit: City-year fiscal panel linked to firm-year observations by headquarters city
  geography_level: Prefecture-level city or equivalent historical city code, with firm headquarters and nearby-city crosswalks
  time_start: 2008
  time_end: 2015
  minimum_frequency: annual, with quarterly or monthly housing/land series where available
  minimum_pre_periods: 2
  minimum_post_periods: 2
  required_fields:
  - City code, historical boundary/crosswalk, and city-specific HPLP policy version
  - Announcement, effective, first-full-year, relaxation, and abolition dates where applicable
  - Total local revenue, land-lease revenue, tax revenue, and denominator definitions
  - Stable firm ID, headquarters city, year, ownership, industry, and firm entry/exit flags
  - Corporate income tax, business tax or successor tax fields, investment, employment, and wages
  - Land holdings, land transactions, residential/commercial/industrial land prices, and local credit controls
  required_identifiers:
  - historical_city_code
  - hplp_policy_version_id
  - policy_effective_date
  - stable_firm_id
  - headquarters_city_code
  - fiscal_year
  treatment_key:
  - hplp_active_city_year
  - hplp_announcement_date
  - hplp_effective_date
  - hplp_relaxation_or_abolition_date
  treatment_source: >
    State Council and municipal HPLP notices, a dated city-policy crosswalk, the
    paper's reported 2008-2015 application, city fiscal accounts, and the linked firm
    records. Data acquisition, restricted firm sources, and reproducible joins belong
    in Econ Data Know-How.
  measurement_risks:
  - National authorization and city enforcement dates are not interchangeable
  - City rule versions and relaxation dates differ and need contemporaneous notices
  - Land-lease and tax-revenue definitions may change across cities or years
  - Firm identifiers and headquarters locations may change through entry, exit, or relocation
  - Housing, credit, land, and tax policies overlap the HPLP window
  - Abstract-level access does not establish the original sample filters, clustering, or raw-variable definitions
design_profiles:
- id: city-fiscal-panel
  label: City fiscal revenue composition panel
  design_families:
  - staggered-did
  - event-study
  when_to_use: >
    Use when city accounts can separate land-lease revenue, tax revenue, and total
    revenue and when each city's HPLP dates and rule versions are archived.
  outcome_domains:
  - land-finance dependence
  - tax-revenue share
  - total local revenue
  requirements:
    population: Chinese adopting and comparison cities
    observation_unit: City-year
    geography_level: Historical prefecture-level city
    time_start: 2008
    time_end: 2015
    minimum_frequency: annual
    minimum_pre_periods: 2
    minimum_post_periods: 2
    required_fields:
    - City code and policy version
    - Total revenue, land-lease revenue, tax revenue, and definitions
    - Announcement/effective/relaxation dates
    required_identifiers:
    - historical_city_code
    - hplp_policy_version_id
    - fiscal_year
    treatment_key:
    - hplp_active_city_year
- id: firm-fiscal-pass-through
  label: Firm tax burden and real-outcome pass-through
  design_families:
  - firm-fixed-effects-did
  - triple-difference
  when_to_use: >
    Use when stable firm records can be linked to headquarters cities and tax burden,
    investment, employment, and wage definitions are reproducible.
  outcome_domains:
  - corporate tax burden
  - investment
  - employment
  - wages
  requirements:
    population: Firms with headquarters in HPLP and comparison cities
    observation_unit: Firm-year
    geography_level: Headquarters city and nearby-city crosswalk
    time_start: 2008
    time_end: 2015
    minimum_frequency: annual
    minimum_pre_periods: 2
    minimum_post_periods: 2
    required_fields:
    - Stable firm ID and headquarters city
    - Corporate income tax, business tax, investment, employment, and wages
    - Ownership, industry, entry/exit, relocation, and land-holding fields
    required_identifiers:
    - stable_firm_id
    - headquarters_city_code
    - fiscal_year
    treatment_key:
    - hplp_active_city_year
    - firm_headquarters_city
evidence:
- id: E1
  source_type: policy-document
  citation: State Council of the People's Republic of China. 2010-04-17. Notice on resolutely curbing excessively rapid housing-price increases in some cities, Guofa [2010] No. 10 (国发〔2010〕10号).
  url: https://jsj.yueyang.gov.cn/54027/54028/54042/content_1396075.html
  date: '2010-04-17'
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.announcement
  - assignment.rule
  - assignment.exemptions
  verification_status: verified
  access_level: official-document
  locator: >
    The official reproduction identifies Guofa [2010] No. 10 and its 17 April 2010
    date, assigns city governments responsibility for housing control, permits local
    governments to limit the number of homes purchased for a period, and discusses
    tax and land-market administration. It establishes the national authorization;
    it does not establish every city's eventual notice, effective date, or paper
    sample.
- id: E2
  source_type: policy-document
  citation: Beijing Municipal People's Government. 2010-04-30. Notice implementing the State Council housing-control document, Jingzhengfa [2010] No. 13 (京政发〔2010〕13号).
  url: https://www.beijing.gov.cn/zhengce/zfwj/zfwj/szfwj/201905/t20190523_72619.html
  date: '2010-04-30'
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.local_timing
  - assignment.rule
  verification_status: verified
  access_level: official-document
  locator: >
    Beijing's official notice is dated 30 April 2010, implements Guofa [2010] No. 10,
    temporarily limits additional purchases, and ties local purchase and lending
    administration to household housing and local tax/social-insurance information.
    It is a Beijing example and does not prove identical rules in other cities.
- id: E3
  source_type: implementation-document
  citation: Beijing Municipal Commission of Housing and Urban-Rural Development. 2011-02-16. Notice on implementing Beijing housing-purchase limits, Jingjianfa [2011] No. 65 (京建发〔2011〕65号).
  url: https://www.beijing.gov.cn/zhengce/zhengcefagui/201905/t20190522_57003.html
  date: '2011-02-16'
  supports:
  - identity.implementation_regime
  - timeline.local_timing
  - assignment.treated
  - assignment.rule
  - assignment.exemptions
  - assignment.compliance
  verification_status: verified
  access_level: official-document
  locator: >
    The official notice is dated 16 February 2011 and applies the detailed limit from
    17 February. It states the one-home/previous-home conditions, the five-year
    local tax or social-insurance requirement for the specified non-local households,
    document review, online-signing checks, and registration enforcement. It does
    not establish the rules or dates of the other HPLP cities.
- id: E4
  source_type: paper
  citation: 'Zhao, Renjie, and Jiakai Zhang. 2022. "Rent-tax substitution and its impact on firms: Evidence from housing purchase limits policy in China." Regional Science and Urban Economics 96:103804. DOI: 10.1016/j.regsciurbeco.2022.103804.'
  url: https://ideas.repec.org/a/eee/regeco/v96y2022ics0166046222000448.html
  date: 2022
  supports:
  - identity.instrument
  - identity.assignment_mechanism
  - timeline.implementation_start
  - timeline.implementation_end
  - assignment.unit
  - assignment.treated
  - assignment.exposure_construction
  - research_compatibility.outcome_domains
  - design.identifying_variation
  - design.estimand
  - design.treatment_variable
  - design.primary_strategy
  - design_applications.research_question
  - design_applications.outcome
  verification_status: verified
  access_level: abstract
  locator: >
    IDEAS/RePEc reproduces the publisher-indexed abstract: HPLP variation is used
    over 2008-2015; implementing cities experience a decline in land-lease revenue
    share and a rise in tax-revenue share; local firms face higher CIT/BT burdens and
    lower investment, employment, and wages. The page reports the DOI and journal
    identity but says the publisher full text is restricted, so exact city lists,
    samples, estimator, clustering, and raw data definitions remain unverified.
- id: E5
  source_type: scholarship
  citation: Related scholarly appendix, "Land investment and firm responses to housing purchase restriction," Appendix D, 2019 conference manuscript.
  url: https://cicm.pbcsf.tsinghua.edu.cn/cn2019/pdf/CICM2019-67.pdf
  date: 2019
  supports:
  - timeline.local_timing
  - assignment.treated
  - assignment.required_identifiers
  - assignment.rule
  verification_status: verified
  access_level: appendix
  locator: >
    Pages 26-27 describe Beijing's 30 April 2010 start, the 46-city expansion, later
    relaxation in many cities, and anticipation concerns. Appendix D on page 56 lists
    the city IDs and reported announcement/abolition dates. This is a secondary
    research appendix, not an official policy archive and not the replication package
    for Zhao and Zhang; use it as a harmonization lead until each local notice is
    archived.
- id: E6
  source_type: paper
  citation: DOI metadata for Zhao and Zhang, Regional Science and Urban Economics 96 (2022), article 103804.
  url: https://doi.org/10.1016/j.regsciurbeco.2022.103804
  date: 2022
  supports:
  - identity.instrument
  - design.primary_strategy
  - design.estimand
  - design_applications.doi
  verification_status: verified
  access_level: metadata
  locator: >
    DOI metadata establishes the article identity, authors, journal, year, volume,
    article number, and DOI. Substantive application claims are attributed to E4.
design_applications:
- paper: 'Rent-tax substitution and its impact on firms: Evidence from housing purchase limits policy in China'
  doi: 10.1016/j.regsciurbeco.2022.103804
  journal: Regional Science and Urban Economics
  year: 2022
  research_question: How does a city housing-purchase restriction change the local revenue mix and the tax burden and real outcomes of firms connected to that city?
  population: Chinese city fiscal observations and local firms in the paper's 2008-2015 application; exact sample frame remains to be recovered.
  outcome: Local total revenue, land-lease revenue share, tax-revenue share, firm corporate income tax and business tax burden, investment, employment, and wages as reported in the abstract.
  data_used:
  - City-level local-government revenue accounts with land-lease and tax components
  - Firm-level tax and accounting records linked to headquarters city
  - City HPLP adoption and policy-timing records
  - Housing or land-market and local-policy controls needed for channel checks
  treatment_encoding: City-year HPLP active after the city-specific local adoption date; firm exposure is the headquarters-city treatment merged by year. The exact original coding and treatment of partial-year exposure must be recovered from the paper.
  comparison: Cities outside or not yet inside the HPLP adoption set in the paper's sample, with exact never-treated, not-yet-treated, and relaxation handling pending full-text recovery.
  empirical_design: Quasi-experimental city-policy comparison over 2008-2015 with city fiscal outcomes and firm-level pass-through; reconstruct the paper's exact staggered-DID/event-study specification before replication.
  assumptions:
  - Conditional pre-trends and city adoption predictors are sufficiently comparable for the stated local estimand.
  - City policy dates and rule versions are measured from contemporaneous notices.
  - Revenue and firm records are consistently defined and linked across years.
  - Housing, land, credit, tax, and other local reforms do not explain the full reported contrast.
  - Firm headquarters exposure captures the relevant local fiscal environment for the outcomes studied.
  threats_addressed:
  - City and year fixed effects or equivalent panel controls, once recovered from the full paper
  - Event-study leads and alternative policy clocks
  - Separate land-lease and tax channels
  - Firm entry, exit, relocation, ownership, and land-holding checks
  - City-specific policy-version and relaxation audit
  evidence_refs:
  - E4
  - E6
method_transfer: null
readiness_blockers:
- The publisher full text and replication package were not accessible through the inspected route. Exact city sample, treatment table, estimator, clustering, weighting, sample filters, and raw-variable definitions remain to be recovered.
- The 46-city list and dates in E5 are a related scholarly appendix rather than the official city-by-city policy archive or the Zhao-Zhang replication. Archive each local notice and reconcile versions, partial-year exposure, and relaxation dates before treating the list as canonical.
- The national authorization and Beijing examples establish the institutional boundary, but they do not establish identical HPLP rules, exemptions, or enforcement in every city.
- City fiscal accounts and firm records, including stable firm IDs, headquarters crosswalks, tax definitions, and land-lease revenue fields, are not stored here; acquisition and data restrictions belong in Econ Data Know-How.
- Adoption responds to housing pressure, migration, fiscal conditions, and local priorities. Anticipation, land-price and credit channels, firm relocation, and nearby-city spillovers require explicit diagnostics and should not be described as removed by the policy label.
- The paper's 2008-2015 window is an observation period. It must not be converted into a claim that one uniform HPLP was active in every treated city for the entire window.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

China's national housing-control framework in April 2010 responded to rapid housing
and land-price growth. The State Council assigned local governments responsibility for
stabilizing housing markets and allowed a city facing especially high pressure to
temporarily limit the number of homes a household could buy [E1]. Beijing translated
that authorization into a city notice on 30 April 2010 and a detailed qualification
and registration procedure in February 2011 [E2; E3]. Other cities adopted their own
versions on different dates and later relaxed or abolished many of them [E5].

The policy matters for regional and urban research because local governments relied
heavily on land-lease revenue. A restriction on housing demand can therefore change
land prices, land transactions, and the fiscal base even when the legal text is aimed
at households. The firm application treats this fiscal channel as distinct from a
direct housing-price treatment: firms are linked through headquarters city, while the
legal purchase restriction is imposed on qualifying households [E1; E4].

## What Changed

The national announcement date is 17 April 2010, but the usable treatment clock is
city-specific. Beijing's first notice is dated 30 April 2010; its detailed procedure
began applying on 17 February 2011 and required documentary checks of household homes,
residence, tax, and social-insurance history [E2; E3]. A related scholarly appendix
reports 46 adopting cities by the end of 2011 and records later abolition dates for
many of them [E5]. Those dates are a research lead, not a substitute for each city's
official notice.

Zhao and Zhang study the 2008-2015 period. Their abstract reports that, in cities
implementing HPLP, the share of land-lease revenue in total revenue fell while the
tax-revenue share rose; it also reports higher local-firm CIT/BT burdens and lower
investment, employment, and wages [E4]. These are paper-reported outcomes. The record
does not claim that every city, firm, or household experienced the same change.

## Implementation and Assignment

The institutional treatment is a dated city rule. A city may limit additional home
purchases, suspend sales to households above a home-count threshold, or require
non-local households to document local tax or social-insurance contributions. Beijing's
2011 notice illustrates how eligibility was checked and how online signing and property
registration could be blocked when the documents did not match the rule [E3]. It is
important to preserve the household-level eligibility conditions separately from the
city-level policy indicator.

For the paper's application, the city-year is treated after the city's HPLP date, and
a firm is exposed through its headquarters city. The comparison is therefore a panel
comparison across adoption dates, not a comparison of households that did and did not
successfully buy a home. The exact city sample, treatment of partial-year adoption,
and handling of cities that relaxed the policy must be recovered from the full paper.

## Why This Creates Empirical Variation

The policy supplies a staggered urban-policy shock to housing demand. If a city loses
part of its land-lease base after adopting HPLP, its fiscal response can be observed
in the composition of local revenue. A firm panel can then ask whether firms in the
city face higher tax burdens and adjust investment, employment, or wages. Land prices,
commercial land, credit, and firm land holdings help separate the fiscal channel from
other consequences of a housing slowdown [E4; E5].

This variation is useful precisely because it has multiple layers. The legal rule is
household purchase eligibility; the urban-market margin is housing and land demand;
the fiscal margin is land-lease versus tax revenue; and the firm margin is the local
business environment. A usable replication must join those layers without treating a
city label as proof of household compliance or firm-level tax enforcement.

## Identification Risks

Cities adopted HPLP because of housing pressure, migration, land prices, and local
priorities, so adoption timing can correlate with pre-existing trends [E1; E5]. National
and local announcements also allow anticipation, and later relaxation creates a second
timing margin. The 46-city appendix explicitly notes that public expectations about
adoption and reversal matter for land-price responses [E5].

The fiscal interpretation has its own risks. A restriction can affect credit,
construction, land supply, household sorting, and firm relocation at the same time as
it changes land-lease receipts. Firm tax burdens may also reflect entry, exit,
reporting, headquarters changes, or a changing tax base. Neighboring cities can absorb
households and firms, so an untreated comparison may carry part of the policy response.
These are conditions for diagnostics and interpretation, not reasons to erase the
variation.

## Data Requirements

The minimum city contract needs historical city codes, local notices, announcement and
effective dates, rule versions, and relaxation/abolition dates. Fiscal data must define
total revenue, land-lease revenue, and tax revenue in comparable units. The firm
contract needs stable IDs, headquarters city, year, ownership and industry, tax
burden components, investment, employment, wages, land holdings, and entry/exit or
relocation markers. Housing and land-price series plus local credit and policy records
are valuable mechanism and overlap checks.

The firm and fiscal data acquisition problem belongs in `Econ Data Know-How`; this
record preserves the institutional treatment and the join contract that data work
must satisfy. A future agent should recover the paper's exact filters and estimator
before labeling a replication as ready.

## Evidence Notes

E1 is the national State Council notice. It establishes the 17 April 2010 framework,
local responsibility, the permission for temporary city purchase limits, and related
tax/land administration. It does not establish every local adoption date or the paper
sample. E2 is Beijing's official 30 April 2010 implementation notice; it establishes
one city example and its purchase-control mechanics, not a national uniform rule. E3
is Beijing's official February 2011 qualification and enforcement notice; it establishes
the household documents, home-count conditions, local tax/social-insurance rule, and
registration checks for Beijing, not other cities.

E4 is the accessible IDEAS/RePEc record of the Zhao-Zhang paper. It establishes the
paper identity, 2008-2015 study window, land-lease/tax revenue findings, and reported
firm outcomes, but the publisher route did not expose the full sample, city table,
estimator, clustering, or raw-variable definitions. E5 is a related scholarly
appendix with a 46-city list and dates; it is useful for discovery and crosswalk work,
but it is neither an official policy archive nor the Zhao-Zhang replication. E6 is DOI
metadata only and establishes article identity, not substantive findings.

The soft recency marker for this application is 2022: it can help a future agent order
newer papers during collection, but it cannot replace city-level policy evidence,
data joins, or the evidence boundary. The paper remains useful even if an older or
newer application has a different outcome, because its distinct variation is the
housing-demand-to-land-finance-to-firm-tax channel.
