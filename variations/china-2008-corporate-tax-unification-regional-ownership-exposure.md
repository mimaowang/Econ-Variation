---
schema_version: 2
id: china-2008-corporate-tax-unification-regional-ownership-exposure
name: China 2008 Corporate Tax Unification Regional-Ownership Exposure
aliases: [两税合并区域所有制差异, 2008 corporate-tax ownership-region exposure]
status: grounded
provenance:
  task_id: task-10cf7d4c8af5
scope:
  country: China
  regions: [Mainland China]
  domains: [regional-economics, public-finance, firm-economics, international-trade]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: The national corporate-income-tax unification changes mainland enterprises' exposure according to their preceding tax status and continuing preferences; regional ownership contrasts supply one actual empirical use.
identity:
  instrument: Differential corporate-income-tax exposure under the 2008 unification and grandfathered transition, retaining continuing Western Development qualifications
  authority: National People's Congress, State Council, Ministry of Finance and State Administration of Taxation
  legal_identifiers: [中华人民共和国企业所得税法（2007年）, 国发〔2007〕39号, 财税〔2008〕21号, 财税〔2001〕202号, 财税〔2011〕58号]
  implementation_regime: One national unification effective in 2008 with an explicit transition for existing low-rate and holiday beneficiaries. Western preferences qualify the comparison; this record does not represent the entire Western Development package or a separate industry-eligibility threshold design.
  assignment_mechanism: Exposure depends on pre-reform statutory status, grandfathering and continuing eligibility, not simply foreign ownership. The regional-ownership application uses differences in realized tax changes rather than assigning every firm the national headline rate.
  parent: null
  related_variations: [china-western-development-program-boundary-exposure]
timeline:
  announcement: '2007-03-16'
  effective: '2008-01-01'
  implementation_start: 2008
  implementation_end: 2013
  local_timing: The law takes effect nationwide in 2008. Old qualifying 15% rates transition through 18%, 20%, 22%, 24% and 25% in 2008–2012; old24% rates become25% in2008. Holidays continue within their prescribed term. The2013 endpoint belongs to the research window, not expiry of the unified law.
  anticipation: The law was announced in March2007 and transition arrangements in December2007; entry, accounting and location responses before effective treatment cannot be ruled out.
  last_verified: '2026-10-04'
assignment:
  unit: Taxpaying enterprise-year; aggregate exposure can be compared across ownership-region-year cells
  treated: Enterprises whose previous rate or benefit changes under unification; the sign and timing of exposure depend on prior qualification
  comparison_pool: Other ownership-region cells whose net tax position changes differently, conditional on continuing preferences; not a universally untreated western population
  rule: Apply the2007 law and transition to the enterprise's old benefit and establishment date. Maintain Western Development qualification separately from geographic location. Use measured effective tax rates for the regional application rather than substituting statutory rates.
  intensity: Change in measured net-of-effective-tax income retention, with the statutory schedule explaining exposure but not equaling realized intensity
  exemptions: [Continuing qualified Western Development preferences, Grandfathered fixed-term tax holidays, New-law qualified high-technology and small-profit preferences, Nonresident withholding outside the resident-enterprise application]
  compliance: Tax payable, accounting profit and legally taxable income differ. A nominal rate is not proof of paid tax or benefit receipt.
  exposure_construction: Preserve firm identifiers, ownership and location; distinguish registration from production. Build region-year ownership cells from consistently selected firms, sum revenue and construct a declared effective-rate aggregate. Join legal transition and western eligibility without assigning a uniform15% rate to all western firms.
  required_identifiers: [Firm legal-unit identifier, Ownership category, Production province, Registration province, Year]
  spillovers: Production relocation and domestic-foreign competition can affect comparison cells; aggregate changes need not measure movement of existing plants alone.
research_compatibility:
  outcome_domains: [Regional production, Firm location, Tax burden, Enterprise investment]
  affected_populations: [Mainland manufacturing legal units, Domestic enterprises, Foreign-invested enterprises]
  mechanism_channels: [After-tax returns, Location incentives, Entry and exit, Accounting and compliance]
  best_for: [Regional ownership comparisons with observed corporate-tax and production data]
  not_good_for: [Assigning one tax change to every foreign firm, Treating western location as sufficient for15% eligibility, Attributing every2008 output change to tax, Counting a new outcome as another variation]
design:
  claim_type: causal
  affordances: [National reform clock, Predetermined benefit history, Explicit transition, Continuing geographically qualified preferences]
  candidate_designs: [Regional-ownership triple-difference instrumental variables, Exposure-based event study]
  identifying_variation: Differential post2007 net-tax changes across ownership and western-region groups
  primary_strategy: The inspected author application specifies its instrument and outcome below. Reuse requires an independently defended first stage and exclusion restriction.
  estimand: Response of regional enterprise production to reform-induced net-tax retention under the chosen aggregation and valid instrument; not an unrestricted effect of foreign ownership
  treatment_variable: Log of one minus the effective corporate tax rate
  comparison_logic: Ownership contrasts within regions are differenced across regional eligibility groups and time. Region-year and ownership-year shocks can be absorbed, but ownership-specific western shocks remain a threat.
  estimation_notes: Keep effective rates below one for the log transform, disclose denominator and loss-firm handling, and distinguish a ratio of sums from a mean of firm ratios. Use inference that tolerates a weak first stage; count independent regional clusters rather than firm observations.
  assumptions: [Differential shocks do not jointly drive the instrument and production outside the tax channel, Measured tax retention responds to the reform, Ownership and sampling changes do not manufacture the contrast]
  diagnostics: [First-stage event trajectories, Weak-IV robust confidence intervals, Stable reporting-threshold sample, Alternative ownership coding, Crisis and stimulus exposure controls, Registered-versus-production geography reconciliation]
threats:
- type: legal-eligibility-versus-geographic-proxy
  basis: documented
  condition: Western tax benefits require encouraged activities and revenue-share qualification; comparable treatment also exists in three eastern autonomous prefectures. A province dummy is not individual legal eligibility.
  evidence_refs: [E3, E4]
  possible_diagnostics: [Qualified-industry restriction, Autonomous-prefecture sensitivity, Observed benefit records]
- type: concurrent-reform-and-crisis
  basis: inferred
  condition: Differential export collapse, credit allocation or investment policy can move foreign production in western regions after2007 independently of corporate tax.
  evidence_refs: [E5]
  possible_diagnostics: [Predetermined export and credit exposure, Placebo years, Ownership-specific regional trends]
- type: tax-measurement-and-survey-composition
  basis: inferred
  condition: Losses, missing taxes, changing survey thresholds and entry/exit can change average effective rates even when legal rates are known.
  evidence_refs: [E1, E5]
  possible_diagnostics: [Matched sample and common revenue threshold, Report missingness by ownership-region-year, Separate extensive and intensive margins]
empirical_requirements:
  contract_version: 1
  population: Manufacturing legal units in mainland China with defensible ownership, geography and corporate-tax measurements
  observation_unit: Ownership-province-year
  geography_level: Province
  time_start: 2005
  time_end: 2013
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields: [Enterprise revenue, Corporate income tax payable, Accounting pre-tax profit, Ownership category, Production province, Registration province, Year, Survey reporting threshold, Missing-tax flag, Western-region classification]
  required_identifiers: [Firm legal-unit identifier, Ownership category, Province code, Year]
  treatment_key: [Ownership category, Province code, Year]
  treatment_source: Original law and transition notices, western qualification documents, plus a transparently constructed observed tax panel
  measurement_risks: [Restricted firm microdata, Loss-profit denominators, Accounting versus taxable profit, Sample-threshold changes, Ownership switching, Local preferences within nonwestern provinces]
design_profiles: []
evidence:
- id: E1
  source_type: policy-document
  citation: Original2007 Enterprise Income Tax Law, MOF publication
  url: https://www.mof.gov.cn/zhengwuxinxi/zhengcefabu/2007zcfb/200805/t20080519_26016.htm
  date: '2007-03-16'
  supports: [identity.instrument, identity.authority, timeline.announcement, timeline.effective, assignment.rule, assignment.exemptions, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: Articles1–5,21–22,28,50,57 and60; original law, not a later consolidated amendment.
- id: E2
  source_type: implementation-document
  citation: State Council 国发〔2007〕39号 and MOF/STA 财税〔2008〕21号
  url: https://www.mof.gov.cn/gkml/caizhengwengao/caizhengbuwengao2008/caizhengbuwengao20084/200807/t20080701_55430.htm
  date: '2008-02-04'
  supports: [identity.implementation_regime, identity.assignment_mechanism, timeline.local_timing, assignment.rule, assignment.exemptions]
  verification_status: verified
  access_level: official-document
  locator: Main noticeII and attachment1 sectionsI–III; establishment cutoff, transition rates, holiday continuation, western continuation and prohibition on stacking preferences. Gazette postingJuly1 is not effective date.
- id: E3
  source_type: policy-document
  citation: MOF/STA/Customs 财税〔2001〕202号
  url: https://www.mof.gov.cn/gkml/caizhengwengao/caizhengbuwengao2002/caizhengbuwengao20024/200805/t20080519_21081.htm
  date: '2001-12-30'
  supports: [assignment.rule, assignment.exemptions, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: SectionsI,II(1) andIV; twelve western jurisdictions, analogous three eastern prefectures, encouraged-industry activity and70% revenue share; effective2001 despite later web posting.
- id: E4
  source_type: policy-document
  citation: MOF/Customs/STA 财税〔2011〕58号
  url: https://fgk.chinatax.gov.cn/zcfgk/c102416/c5204164/content.html
  date: '2011-07-27'
  supports: [assignment.rule, assignment.exemptions, identity.implementation_regime, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: ItemsII–V;2011–2020 qualified15% rule,70% share, geographic scope and replacement of earlier notices from2011.
- id: E5
  source_type: paper
  citation: Deng, Liu, Wang and Zi, author manuscript dated February12,2025
  url: https://sophie-yuanzi.github.io/papers/tax_dlwz.pdf
  date: '2025-02-12'
  supports: [design.identifying_variation, design.treatment_variable, design_applications.treatment_encoding, design_applications.empirical_design, design_applications.data_used, empirical_requirements.time_start, empirical_requirements.time_end]
  verification_status: reported
  access_level: full-text
  locator: Sections2.1–2.4 and4.2, appendixC.1 andE; PDFpp7–12,29–30,66–72,94–97. Working version inspected; final publisher PDF returned403.
- id: E6
  source_type: other
  citation: Crossref publisher-deposited REStat metadata
  url: https://doi.org/10.1162/rest.a.279
  date: '2025-09-09'
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: Title, publisher, container-title and published date-parts inspected through https://api.crossref.org/works/10.1162/rest.a.279; DOI also linked from the author homepage. Final publication text was not accessible.
design_applications:
- paper: Local Corporate Taxes and the Geography of Foreign Multinationals
  doi: 10.1162/rest.a.279
  journal: Review of Economics and Statistics
  year: 2025
  research_question: How does corporate tax affect regional production?
  population: Domestic and foreign manufacturing cells in30 provinces, excluding Tibet
  outcome: Log aggregate revenue
  data_used: [ASIF2005–2009 and2013, Firm registration records, Statistical yearbooks, Industry catalogs]
  treatment_encoding: Foreign times West times Post07 instruments log net-of-effective-tax rate; baseline rate averages firm tax-payable/pre-tax-profit ratios.
  comparison: Domestic versus foreign cells across western and other provinces before/after2007
  empirical_design: 2SLS with region-year, ownership-year and ownership-west effects; provincial clustering. First-stage, Anderson-Rubin, city-level and common-threshold checks are reported.
  assumptions: [Tax-channel exclusion, First-stage relevance, Comparable differential trends]
  threats_addressed: [Crisis and stimulus, Anticipation, Survey composition, FDI catalog changes]
  evidence_refs: [E5, E6]
method_transfer: null
readiness_blockers:
- Conditional reuse requires lawful ASIF access and explicit ownership coding, including the treatment of Hong Kong/Macao/Taiwan investment; the inspected manuscript does not provide a complete executable reconstruction.
- Preserve the working-version boundary. Empirical tax estimation retains missing values, whereas its quantitative2013 exercise substitutes zeros; neither convention is a general missing-data rule.
- Reconstruct western membership and the three eastern autonomous-prefecture exceptions. Geographic instruments need a first stage, not a claim that every western enterprise receives15% treatment.
---

## Institutional Background

The2007 law replaces the previously separate domestic and foreign enterprise tax systems with a common framework [E1]. The change does not eliminate all preferences. A reader needs the preceding benefit, establishment date and continuing qualification to understand a firm's tax exposure [E2–E4].

## What Changed

The national reform begins in2008, but previously qualified enterprises follow a transition rather than jumping to one rate immediately [E1–E2]. Thus the empirical object is differential exposure under unification, not a new western program. The existing Western Development boundary record represents a broader place-based package; this record should not be substituted for it.

## Implementation and Assignment

Establishment before March16,2007 and the prescribed prior benefit govern grandfathering [E2]. Western qualification requires an encouraged main activity and a revenue-share condition; it is not conferred on every enterprise by provincial location [E3–E4]. The latter distinction matters when translating a regional comparison into an individual firm's treatment.

## Why This Creates Empirical Variation

The actual research application is specified in `design_applications` [E5, reported claim]. [Analytical inference] A common national clock can produce differential exposure without random assignment. A regional-ownership instrument is useful only if it shifts observed net tax retention and does not proxy for a different ownership-specific regional shock.

## Identification Risks

[Analytical inference] Financial crisis, export demand and stimulus may affect the same comparison cells. Legal continuity of a preference does not establish continuity of the tax base, enforcement or survey composition. Nor does a statistically informative first stage prove exclusion. Entry across a reporting threshold must not be described automatically as physical plant relocation.

## Data Requirements

The default contract supports a regional production question, not every conceivable firm outcome. Preserve underlying legal-unit identifiers so changes in ownership, reporting eligibility and location can be distinguished. Tax payable over accounting profit is a measurement choice, not a statutory tax rate [E1; E5, reported claim]. An extension must define loss firms, outliers and missing values before constructing regional averages.

## Evidence Notes

Original law and transition notices establish institutional identity and timing [E1–E4]. Publisher-deposited metadata establishes publication identity [E6]. The accessible author manuscript supplies the research application [E5, reported claim]; no independent replication or inspection of the final typeset body is claimed. The earlier CER effective-rate-group candidate is related unification evidence, not authority to count another record for a different outcome.
