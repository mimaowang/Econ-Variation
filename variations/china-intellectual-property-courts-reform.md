---
schema_version: 2
id: china-intellectual-property-courts-reform
name: China's Intellectual Property Courts Reform (2014)
aliases:
- Intellectual Property Courts Reform
- IPC reform
- 知识产权法院改革
- Beijing-Shanghai-Guangzhou IP courts
- 知识产权法院
status: grounded
provenance:
  task_id: task-2c2448703f6f
scope:
  country: China
  regions:
  - Beijing
  - Shanghai
  - Guangdong (Guangzhou)
  - Later specialized IP tribunals in Nanjing, Suzhou, Wuhan, Chengdu, Hangzhou,
    Ningbo, Hefei, Fuzhou, Jinan, Qingdao, Shenzhen, Tianjin, Zhengzhou, Changsha,
    Xi'an, Nanchang, Lanzhou, Changchun, Urumqi, Haikou
  domains:
  - judicial-institutions
  - intellectual-property
  - innovation
  - firm-behavior
  - economic-growth
  - public-policy
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    The variation is a Chinese judicial-institution reform that created specialized
    intellectual property courts and tribunals, altering the local legal environment
    for patent enforcement. It assigns treatment to cities and firms by court
    jurisdiction, with direct relevance for innovation, patenting, and technology
    markets in China.
identity:
  instrument: >
    Establishment of specialized intellectual property courts in Beijing, Shanghai,
    and Guangzhou in late 2014, followed by specialized IP tribunals in additional
    cities from 2017 onward, centralizing and professionalizing adjudication of
    patent and other technology-related intellectual property disputes.
  authority: >
    Standing Committee of the National People's Congress; Supreme People's Court;
    Beijing, Shanghai, and Guangdong High People's Courts; later municipal
    intermediate people's courts with SPC approval.
  legal_identifiers:
  - 全国人民代表大会常务委员会关于在北京、上海、广州设立知识产权法院的决定（2014年8月31日）
  - 最高人民法院关于北京、上海、广州知识产权法院案件管辖的规定（法释〔2014〕12号）
  - Supreme People's Court jurisdiction regulation on Beijing, Shanghai and Guangzhou
    Intellectual Property Courts (Fa Shi [2014] No. 12)
  implementation_regime: >
    The NPC Standing Committee authorized the creation of three specialized IP
    courts in Beijing, Shanghai and Guangzhou in August 2014. The Supreme People's
    Court issued a jurisdiction regulation (effective 3 November 2014) specifying
    that the new courts would hear first-instance civil and administrative cases
    involving patents, plant varieties, integrated circuit layout designs, trade
    secrets and computer software, with Guangzhou IP Court exercising cross-regional
    jurisdiction inside Guangdong. The three courts opened between 6 November and
    28 December 2014. From 2017 the SPC approved specialized IP tribunals inside
    intermediate courts in additional cities, extending the reform's geographic
    coverage. [E1; E2]
  assignment_mechanism: >
    Cities (and firms located in them) become treated when an IP court or tribunal
    with jurisdiction over their technology-related IP disputes begins operation.
    The first treated cities are Beijing, Shanghai and Guangzhou in late 2014;
    additional cities enter in later waves. Treatment timing is determined by the
    central judicial reform schedule, not by individual firm or inventor choice.
    [E1; E2; E3, reported claim]
  parent: null
  related_variations:
  - china-rd-tax-notch
  - china-export-compulsory-inspection-deregulation
  - china-low-carbon-pilot-first-wave
timeline:
  announcement: '2013-11-01'
  effective: '2014-11-03'
  implementation_start: 2014
  implementation_end: null
  local_timing: >
    The Third Plenum of the 18th CPC Central Committee in November 2013 called for
    exploring the establishment of IP courts. The NPC Standing Committee passed the
    authorizing decision on 31 August 2014. The SPC jurisdiction regulation took
    effect on 3 November 2014. Beijing IP Court opened on 6 November 2014, Guangzhou
    IP Court on 16 December 2014, and Shanghai IP Court on 28 December 2014.
    Additional specialized tribunals began operating from 2017 onward. [E1; E2]
  anticipation: >
    The reform was publicly announced at the central level from late 2013 through
    August 2014, so some anticipation by late 2014 was possible. Empirical designs
    typically treat the first post-reform year as 2015 when the court opened after
    June, or as 2014 when it opened before July. [E3, reported claim]
  last_verified: '2026-07-14'
assignment:
  unit: city-year or firm-year
  treated: >
    Cities and firms located in jurisdictions covered by a newly established IP
    court or tribunal. In the main research application, treatment begins in the
    first year the IPC institution is available in the city.
  comparison_pool: >
    Cities and firms that had not yet obtained an IP court or tribunal during the
    sample period; the same cities before the local court opened.
  rule: >
    Code a city-year as treated from the first year an IP court or tribunal is
    available in that city. Following the source paper, if the establishment month
    is before July, the treatment year is the opening year; otherwise it is the
    following year. [E3, reported claim]
  intensity: >
    Binary at the city level (presence of an IPC institution); continuous proxies
    such as case duration or plaintiff win rate can be used for mechanism analysis.
  exemptions:
  - Intellectual property disputes outside the specialized courts' jurisdiction
    (e.g., ordinary copyright and trademark cases initially remained with local
    courts)
  - Cities without sufficient technology-case volume to receive a tribunal
  - Firms without patentable technologies
  compliance: >
    Institutional compliance is high because the reform created courts with
    mandatory jurisdiction. Take-up of the new judicial channel by plaintiffs
    depends on expected gains, case type and location; the reform nevertheless
    shifted the local judicial environment for eligible disputes. [E3, reported claim]
  exposure_construction: >
    Build a city-year panel of IP court/tribunal opening dates from official SPC
    approvals and court announcements. Merge with city-year patent data using city
    identifiers and with listed-firm data using firm location. Define treatment
    based on whether the city has an operating IPC institution in each year. [E3,
    reported claim]
  required_identifiers:
  - city code
  - calendar year
  - firm identifier (for firm-level designs)
  - patent application/grant identifier (for patent-level outcomes)
  spillovers: >
    Stronger IP enforcement in treated cities may attract inventors or firms from
    untreated neighboring cities, creating spatial spillovers. Patent transfers
    within business groups could also relocate patent registrations. Improved case
    outcomes in specialized courts may influence behavior in other jurisdictions
    through precedent or forum-shopping incentives.
research_compatibility:
  outcome_domains:
  - invention patenting
  - patent structure (invention vs utility vs design)
  - patent quality
  - research and development expenditure
  - firm innovation
  - technology commercialization
  - judicial efficiency
  - intellectual property litigation outcomes
  affected_populations:
  - inventors and firms in technology-intensive industries
  - manufacturing and information-technology firms
  - universities and research institutions
  - patent plaintiffs and defendants
  - cities with specialized IP courts or tribunals
  mechanism_channels:
  - stronger judicial protection of intellectual property
  - higher expected returns to patenting
  - shorter case duration
  - higher plaintiff win rates
  - shift from trade secrets to patents
  - knowledge spillovers from disclosed patents
  best_for:
  - Staggered difference-in-differences at the city-year or firm-year level
  - Event-study designs around local court opening dates
  - Mechanism analysis using case duration and plaintiff win rates
  - Heterogeneity analysis by education level and technology intensity
  not_good_for:
  - Identifying effects of specific patent legislation changes (the reform is
    judicial, not legislative)
  - Outcomes for non-technology intellectual property such as ordinary trademarks
    or copyrights, which were largely outside the new courts' jurisdiction
  - Causal claims that ignore spatial spillovers or selective migration of inventors
  - Settings where the outcome cannot be measured at the city or firm level
  - Short-term effects that cannot separate anticipation from post-treatment response
design:
  claim_type: causal
  affordances:
  - Clear staggered rollout driven by central authorization
  - Official opening dates for each city
  - City-level panel data from patent administrative records
  - Firm-level listed-company data for robustness
  - Mechanism variables from judgment documents and social satisfaction surveys
  candidate_designs:
  - City-level staggered difference-in-differences with city and year fixed effects
  - Firm-level staggered DID with firm and year fixed effects
  - Event-study using Callaway-Sant'Anna or Sun-Abraham estimators
  - Triple-difference interacting local human capital or technology intensity
  identifying_variation: >
    The staggered establishment of specialized IP courts and tribunals across
    Chinese cities from late 2014 onward, combined with jurisdiction rules that
    assign cities to treatment based on central decisions.
  primary_strategy: >
    Staggered difference-in-differences comparing innovation outcomes in cities
    that obtained an IP court or tribunal at different dates, with city fixed
    effects, year fixed effects, and baseline city characteristics interacted with
    a linear time trend. Cluster standard errors at the city level. [E3, reported claim]
  estimand: >
    The average effect of gaining access to a specialized IP court or tribunal on
    the number and structure of invention patents in the affected city, relative to
    cities that had not yet received the institution, under parallel-trends
    assumptions.
  treatment_variable: >
    City-year dummy equal to one when an IP court or tribunal is available in the
    city; at the firm level, a dummy for the city of firm location having an IPC
    institution.
  comparison_logic: >
    Cities that received the reform later or not at all provide the counterfactual
    trend for early adopters; the pre-reform period for each city provides the
    within-city baseline.
  estimation_notes: >
    Use a staggered DID estimator robust to heterogeneous treatment effects
    (Callaway-Sant'Anna) as the preferred specification. Control for baseline city
    characteristics including GDP per capita, population, education share, FDI,
    universities, hospitals, education spending and pre-reform patent stock. For
    firm-level analysis, add firm controls and cluster at the city level. [E3,
    reported claim]
  assumptions:
  - Parallel trends in patenting outcomes between treated and not-yet-treated cities
    absent the reform
  - The central timing of court establishment is not correlated with unobserved
    city-level innovation trends
  - Other innovation policies such as patent subsidies, MIC2025 and anti-corruption
    campaigns are controlled for or do not coincide differentially with IPC timing
  - Patent location proxies true innovative activity, or spatial transfers are
    explicitly tested
  diagnostics:
  - Event-study plots for pre-trends and dynamic effects
  - Callaway-Sant'Anna or Sun-Abraham staggered DID estimators
  - Robustness to 2-year, 4-year and unlimited patent windows
  - Exclusion of municipalities, provincial capitals and special economic zones
  - Controls for patent subsidies, MIC2025 and anti-corruption campaign
  - Tests for inter-region and intra-conglomerate patent transfers
  - Firm-level robustness in manufacturing and IT sub-samples
threats:
- type: spatial-spillovers-and-forum-shopping
  basis: inferred
  condition: >
    Inventors or firms in untreated cities may relocate patents or operations to
    treated cities to benefit from stronger protection, biasing city-level
    estimates upward.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Test for patent transfers across regions and within business groups
  - Use firm-level outcomes that are less mobile than patent counts
  - Control for neighboring-city treatment status
- type: confounding-policies
  basis: inferred
  condition: >
    Concurrent innovation policies such as patent subsidies, Made in China 2025,
    innovation-oriented city pilots and anti-corruption campaigns could affect
    patenting at the same time as the IPC reform.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Include controls for other innovation policies
  - Conduct subsample and sensitivity analyses
  - Use outcome variables less affected by subsidies (e.g., patent citations,
    though measurement is limited)
- type: patent-quality-vs-quantity
  basis: reported
  condition: >
    The reform increased the number and share of invention patents but did not
    significantly improve approval rates or citations per patent, suggesting the
    effect may partly reflect reclassification or disclosure strategy rather than
    higher-quality innovation. [E3, reported claim]
  evidence_refs:
  - E3
  possible_diagnostics:
  - Separate invention, utility and design patents
  - Examine approval rates and citation counts
  - Distinguish general effect from transformation effect
- type: anticipation
  basis: inferred
  condition: >
    The reform was announced in 2013-2014 before courts opened, so some patenting
    responses may have begun before the official treatment year.
  evidence_refs:
  - E2
  - E3
  possible_diagnostics:
  - Use event-study to check for pre-trends
  - Define treatment year conservatively based on opening month
- type: measurement-error
  basis: inferred
  condition: >
    City-level patent counts are aggregated by inventor or first patentee address,
    which may mismeasure the true location of innovative activity.
  evidence_refs:
  - E3
  possible_diagnostics:
  - Compare results using first, first-three and all patentee addresses
  - Validate against firm-level patent data for listed companies
empirical_requirements:
  contract_version: 1
  population: >
    Chinese cities and listed firms observed before and during the 2014-2020 IP
    courts reform.
  observation_unit: city-year or firm-year
  geography_level: city
  time_start: 2011
  time_end: 2020
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields:
  - number of invention patents (3-year window preferred)
  - number of utility and design patents
  - city code
  - calendar year
  - GDP per capita
  - resident population
  - highly educated population share
  - FDI
  - universities per capita
  - hospitals per capita
  - education expenditure
  - pre-reform patent stock
  - firm identifier and location (firm-level)
  - firm assets, size, leverage, cash flow (firm-level)
  required_identifiers:
  - city code
  - year
  - firm identifier (for firm-level analysis)
  treatment_key:
  - city code
  - year
  treatment_source: >
    City-level IP court/tribunal opening dates from Supreme People's Court
    approvals, court announcements and official reports; patent data from the China
    National Intellectual Property Administration via CnOpenData or similar
    databases; firm data from listed-firm databases; case-level data from China
    Judgments Online.
  measurement_risks:
  - Patent address may not reflect actual research location
  - The timing of tribunal openings for later-adopting cities may be less clearly
    documented than the first three IP courts
  - Case-level mechanism variables from judgment documents may be selective
  - 3-year patent windows delay measurement of contemporaneous effects

evidence:
- id: E1
  source_type: policy-document
  citation: >
    Supreme People's Court of China. 2014. "Provisions on the Jurisdiction of Cases
    of the Beijing, Shanghai and Guangzhou Intellectual Property Courts" (Fa Shi
    [2014] No. 12).
  url: http://gongbao.court.gov.cn/Details/b7a6d56264c13d9d6ff2a573d7f88d.html
  date: '2014-10-31'
  supports:
  - identity
  - assignment
  verification_status: verified
  access_level: official-document
  locator: >
    Official Supreme People's Court judicial interpretation dated 31 October 2014,
    effective 3 November 2014; defines the specialized jurisdiction of the three
    IP courts over patents, plant varieties, integrated circuit layouts, trade
    secrets and computer software, and Guangzhou's cross-regional jurisdiction.
- id: E2
  source_type: implementation-document
  citation: >
    Supreme People's Court of China. 2017. "Report on the Work of the Intellectual
    Property Courts" submitted to the Standing Committee of the National People's
    Congress on 29 August 2017.
  url: https://www.court.gov.cn/zixun/xiangqing/58142.html
  date: '2017-08-29'
  supports:
  - identity
  - timeline
  verification_status: verified
  access_level: official-document
  locator: >
    Official SPC report confirming the NPC Standing Committee decision of 31 August
    2014 and the opening of the Beijing, Shanghai and Guangzhou IP courts in
    November-December 2014.
- id: E3
  source_type: paper
  citation: >
    Wan, Liyang, Qian Wan, Zichao Yang, and Ying Zhao. 2026. "Judicial institution
    and innovation: Evidence from China's intellectual property courts reform."
    Journal of Development Economics 179: 103630.
  url: https://doi.org/10.1016/j.jdeveco.2025.103630
  date: 2026
  supports:
  - design_applications
  - design
  - assignment
  verification_status: reported
  access_level: abstract
  locator: >
    Journal of Development Economics abstract and published article; reports a
    staggered difference-in-differences analysis using city-year and firm-year
    panels, finding that the IP courts reform increased city-level invention
    patents by 22.6% and explores mechanisms through case duration and plaintiff
    win rates.

design_applications:
- paper: Judicial institution and innovation - Evidence from China's intellectual property courts reform
  doi: 10.1016/j.jdeveco.2025.103630
  journal: Journal of Development Economics
  year: 2026
  research_question: >
    How does the establishment of specialized intellectual property courts affect
    innovation in China?
  population: >
    Chinese cities and listed firms observed from 2011 to 2020, with city-level
    patent data from the China National Intellectual Property Administration.
  outcome: >
    Number of invention patents (3-year window), share of invention patents,
    patent approval rates, citations per patent, R&D investment, and technology
    expenditure.
  data_used:
  - CnOpenData patent database (city-year patent counts by type and address)
  - China Judgments Online (case duration and plaintiff win rates)
  - China Intellectual Property Protection Social Satisfaction Survey
  - 2011-2020 China City Statistical Yearbook
  - 2010 census education data
  - Listed-firm patent and financial data
  treatment_encoding: >
    City-year dummy IPCct equals one when an IP court or tribunal is available in
    the city; treatment year is the opening year if the establishment month is
    before July, otherwise the following year.
  comparison: >
    Cities and firms not yet covered by an IP court or tribunal, and the same
    cities before the local court opened.
  empirical_design: >
    Staggered difference-in-differences with city (or firm) fixed effects and year
    fixed effects; baseline city characteristics interacted with a linear time
    trend; Callaway-Sant'Anna estimator for heterogeneous treatment effects;
    clustered standard errors at the city level.
  assumptions:
  - Parallel trends in patenting between treated and not-yet-treated cities
  - Central reform timing is independent of unobserved city innovation trends
  - Other innovation policies are controlled or not differentially timed
  threats_addressed:
  - Pre-trends via event-study plots
  - Robustness to staggered DID estimators
  - Alternative patent window lengths
  - Exclusion of major cities and special economic zones
  - Controls for patent subsidies, MIC2025 and anti-corruption campaign
  - Tests for spatial and intra-conglomerate patent transfers
  evidence_refs:
  - E3

readiness_blockers:
- >
  A complete city-by-year panel of IP tribunal opening dates for the post-2017
  expansion has not been compiled into this record.
- >
  Replication materials for the JDE paper have not been inspected; treatment coding
  and sample construction rely on the published abstract and article text.
- >
  The distinction between the three standalone IP courts (2014) and later
  tribunals within intermediate courts has not been fully disaggregated into
  separate treatment intensities.

method_transfer: null
---

## Institutional Background

Before 2014, intellectual property disputes in China were handled primarily by
ordinary intermediate and basic-level courts, with uneven specialization and
local-protection concerns. The 2013 Third Plenum of the 18th CPC Central
Committee proposed exploring specialized IP courts. In August 2014 the NPC
Standing Committee authorized IP courts in Beijing, Shanghai and Guangzhou; the
SPC followed with jurisdiction rules in October 2014. [E1; E2]

## What Changed

Three specialized IP courts opened in late 2014, concentrating first-instance
jurisdiction over patents, plant varieties, integrated circuit layouts, trade
secrets and computer software. Guangzhou's court also exercised cross-regional
jurisdiction within Guangdong. From 2017 the SPC approved additional specialized
IP tribunals inside intermediate courts in other cities. The reform aimed to
raise judicial professionalism, shorten case duration, and strengthen IP
protection. [E1; E2]

## Implementation and Assignment

Treatment is assigned by city according to whether a specialized IP court or
tribunal with jurisdiction over local technology-related IP disputes is in
operation. Beijing, Shanghai and Guangzhou entered in late 2014; other cities
entered in later waves. The timing was determined by central authorization and
SPC approvals, not by local choice. [E1; E2; E3, reported claim]

## Why This Creates Empirical Variation

The reform created a staggered, city-level shock to the judicial enforcement of
intellectual property rights. Because the rollout was centrally planned and the
jurisdiction rules create a sharp division between treated and untreated cities,
researchers can use staggered difference-in-differences designs to estimate the
effect of specialized IP adjudication on innovation. [E1; E3, reported claim]

## Identification Risks

Inventors or firms may relocate patents to treated cities, causing spatial
spillovers. Concurrent innovation policies such as patent subsidies, Made in
China 2025 and anti-corruption campaigns may confound estimates. The reform may
increase patent quantity without improving quality, reflecting disclosure
strategy shifts rather than true innovation. Anticipation in 2014 and the use of
patent addresses as location proxies add further measurement and timing concerns.
[E3, reported claim]

## Data Requirements

Researchers need a city-year panel of IP court/tribunal opening dates, city-level
patent data by type and address, city socioeconomic controls from statistical
yearbooks, and ideally firm-level patent and financial data. Mechanism analysis
requires case-level information from China Judgments Online and survey measures
of judicial satisfaction. [E3, reported claim]

## Evidence Notes

E1 is the official SPC jurisdiction regulation that defines the specialized
subject-matter jurisdiction of the three IP courts. E2 is the SPC's 2017 report
to the NPC Standing Committee, which confirms the authorizing decision and the
late-2014 opening dates. E3 is the published Journal of Development Economics
article; its design details, sample construction and results are reported claims
that have not been independently verified from replication materials.
