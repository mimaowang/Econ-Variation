---
schema_version: 2
id: china-bankruptcy-tribunal-city-access
name: China City Access to Specialized Bankruptcy Tribunals and Local Capital Reallocation
aliases: [Going Bankrupt in China city adoption, 清算与破产审判庭城市暴露]
status: grounded
provenance:
  task_id: task-567263a02a79
scope:
  country: China
  regions: [Mainland prefecture-level cities]
  domains: [regional-economics, firm-dynamics, corporate-finance, institutional-economics]
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: The application uses differential timing of bankruptcy tribunal availability across Chinese cities to study local industrial capital productivity and resource reallocation in 2011-2017.
identity:
  instrument: City access to a specialized liquidation and bankruptcy tribunal within an existing people's court
  authority: Supreme People's Court guidance, provincial high courts and local court/establishment authorities
  legal_identifiers: [法〔2016〕169号, 2016-06-21 work plan on liquidation and bankruptcy tribunals in intermediate people's courts]
  implementation_regime: >
    Specialized adjudication within existing courts, including earlier local
    initiatives and the 2016 national acceleration. The 2011-2017 application
    excludes the later 2019-2020 named bankruptcy tribunals and personal bankruptcy.
    It does not represent a change to the nationwide substantive bankruptcy law.
  assignment_mechanism: >
    A city-year is exposed from its first specialized tribunal introduction year
    in the author's inventory, including that year. Adoption reflects administrative
    priorities and local circumstances, not a random allocation. Institutional
    availability is distinct from which court handles a particular firm's case.
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: null
  implementation_end: null
  local_timing: >
    Author inventory dates range from 2007-01-01 to 2017-12-30 for 97 tribunal
    rows. These are reported research dates, not proof that specialization began
    nationally in 2007. Shenzhen's row is 2007-01-01 while official court history
    dates its first tribunal to 1993; either date makes it already exposed throughout
    2011-2017. The May 6,2016 notice and June 21 work plan accelerated later adoption;
    deadlines do not establish actual opening dates. Exact daily timing needs local checks.
  anticipation: Local planning can precede inauguration; the city application uses annual availability, not unexpected daily shocks.
  last_verified: '2026-10-02'
assignment:
  unit: Prefecture-level city-year
  treated: Cities in years at or after their first author-listed specialized tribunal date during the 2011-2017 outcome panel
  comparison_pool: Cities before introduction and cities without an introduction in the study window; this is the paper's two-way fixed-effect comparison, not random untreated cities
  rule: >
    Compute the earliest introduction year among tribunal records with a valid
    prefecture city and code Post=1 from that year. The official 2016 program
    prioritized provincial capitals/subprovincial cities and allowed other courts
    to respond to local needs. Do not treat its deadlines as observed dates or
    use the later specialized_courts_dates file as a new adoption in this window.
  intensity: Binary city-level availability, not the fraction of bankruptcies actually handled professionally
  exemptions:
  - Provincial high-court rows with blank city in the public file are not automatically treatment for every city in that province.
  - The 2019-2020 named bankruptcy tribunals are outside this regional application's outcome window.
  - Tribunal presence does not transfer all local cases into the specialized institution.
  compliance: The official plan specifies functions and jurisdiction; the paper reports that specialized and traditional courts coexist. Availability therefore does not certify every firm received specialized adjudication.
  exposure_construction: >
    Retrieve the author's specialized_tribunals_dates.dta, retain court and city
    identities and intro_date, resolve name-to-prefecture codes and court reorganizations,
    then derive first city exposure and join annual yearbook outcomes. Preserve
    already-treated cities separately from new adopters; do not interpret their
    historical dates as within-panel transitions. Use documented city crosswalks
    rather than propagating high-court entries to all prefectures.
  required_identifiers: [Court name, Source city name, Harmonized prefecture code, Introduction date/year, Outcome year]
  spillovers: Liquidation can reallocate labor and capital across cities; the regional estimand can include local spillovers while cross-city effects threaten the comparison.
research_compatibility:
  outcome_domains: [Average industrial capital productivity, Average profitability, Labor allocation across industries]
  affected_populations: [Local industrial firms above the yearbook reporting threshold, Urban labor markets]
  mechanism_channels: [Insolvency resolution capacity, Exit and reallocation, Judge specialization, Local political influence]
  best_for: [Conditional regional research on professional insolvency adjudication and industrial resource allocation]
  not_good_for: [Random case assignment, All-firm bankruptcy probabilities, Personal bankruptcy reform, Effects of a 2019 independent court, Firm-level TFP inferred from city accounting ratios]
design:
  claim_type: reduced-form
  affordances: [Staggered city availability, Public author court-date inventory, Annual city accounting outcomes]
  candidate_designs: [City-year adoption comparison with conditional parallel trends]
  identifying_variation: Differential timing of the first author-listed specialized tribunal across cities in a 2011-2017 regional panel
  primary_strategy: Equation 3 city and year fixed-effect regression with time-varying city controls
  estimand: Conditional change in city industrial capital productivity/profitability associated with tribunal availability, not a random reform effect or individual case-duration effect
  treatment_variable: PostSpecialization_city_year, including the introduction year
  comparison_logic: Compare city outcomes before/after introduction against other cities, including never adopters; already-treated cities require separate handling in a new staggered-adoption analysis
  estimation_notes: >
    Table9 PanelB uses 2011-2017 city data, baseline-2011 firm-count weights and
    city-clustered standard errors. Its log(Output/Capital) is an aggregate
    value-added/tangible-asset ratio, not firm TFP; log(ROA) is aggregate profits/
    total assets. The short event study includes only eventual adopters, omits
    adoption year k=0, and spans k=-2 to2; it has no pure never-treated control.
    Court-by-case regressions in equations1-2 identify a different assignment
    and are not admitted as an interchangeable design profile here.
  assumptions:
  - City capital-productivity trends would have been comparable conditional on controls without specialization.
  - Concurrent local credit, insolvency and industrial policies do not drive both timing and outcomes.
  - Author-listed availability and harmonized city identifiers adequately measure the intended exposure.
  - Baseline weights, reporting thresholds and accounting definitions do not generate treatment-correlated composition changes.
  - Cross-city resource movements do not invalidate the specified comparison.
  diagnostics:
  - Separate never-treated, not-yet-treated and already-treated cities; examine cohort-specific estimates rather than assuming homogeneous TWFE effects
  - Replicate the Table8 timing hazard and pre-outcome checks without treating them as proof against unobserved selection
  - Sensitivity to exact local inauguration sources, January1 date precision and historical already-treated cities
  - Exposure-name crosswalk and blank high-court row audit
  - Preserve Table9 outcome units and baseline weights; do not convert aggregate capital ratios into firm TFP
threats:
- type: endogenous-adoption
  basis: reported
  condition: The paper explicitly recognizes that economic conditions can drive specialization timing. Hazard tests of observable trends and controls do not eliminate time-varying unobservables.
  evidence_refs: [E3]
  possible_diagnostics: [Cohort-specific pretrends, Concurrent-policy controls, Adoption timing sensitivity]
- type: historical-date-and-institution-boundary
  basis: documented
  condition: The author's Shenzhen tribunal date is2007 while official history says1993. Both precede this outcome panel, but the discrepancy prevents treating the inventory as a universal history or using2007 as a verified inauguration.
  evidence_refs: [E4, E5]
  possible_diagnostics: [Keep Shenzhen as already-treated, Resolve reorganization records for historical extensions, Verify any new within-panel date against local sources]
- type: city-accounting-composition
  basis: inferred
  condition: City industrial aggregates cover firms above a reporting threshold and can change composition through entry/exit or statistical coverage. Their productivity ratio is not an individual firm's technical efficiency.
  evidence_refs: [E3]
  possible_diagnostics: [Threshold-consistent panels, Firm-level decompositions where obtainable, Alternative baseline weights]
empirical_requirements:
  contract_version: 1
  population: Yearbook-covered industrial firms with annual sales above RMB20million, aggregated to prefecture cities
  observation_unit: City-year
  geography_level: Prefecture-level city
  time_start: 2011
  time_end: 2017
  minimum_frequency: annual
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields: [Tribunal introduction date, Industrial value added, Tangible assets, Profits, Total assets, Firm count, Average firm employment, City GDP per capita, Manufacturing employment share, Baseline2011 firm count]
  required_identifiers: [Court name and source city, Prefecture code, Year]
  treatment_key: [Prefecture code, Year]
  treatment_source: Author public97-row tribunal-date inventory linked from research page, with original2016 legal priority rules and local history kept distinct
  measurement_risks: [Exact local-date precision, Blank high-court cities, Historical boundary and court-name changes, Industrial reporting threshold, Log ratios require positive values and source filtering]
design_profiles: []
evidence:
- id: E1
  source_type: policy-document
  citation: Supreme People's Court 法〔2016〕169号, notice on enterprise rescue and liquidation
  url: https://www.court.gov.cn/fabu/xiangqing/37392.html
  date: '2016-05-06'
  supports: [identity.legal_identifiers, identity.authority, identity.implementation_regime, assignment.rule, assignment.compliance, timeline.local_timing]
  verification_status: verified
  access_level: official-document
  locator: Signed May6, page published May25; SectionII specialization priority, duties and reporting deadline; SectionIII coordination. Not a court-specific opening roster.
- id: E2
  source_type: implementation-document
  citation: Supreme People's Court Civil Division2 explanation of June21,2016 intermediate-court work plan
  url: https://pccz.court.gov.cn/pcajxxw/pcnews/newsxq?id=73A45D14EA34555EF0F3BC3587CA92D1
  date: '2016-06-21'
  supports: [identity.legal_identifiers, identity.implementation_regime, assignment.rule, timeline.local_timing]
  verification_status: verified
  access_level: official-document
  locator: Official explanation published October11; issue date paragraph, July/December implementation deadlines and intermediate-court jurisdiction/functions; not full original plan or local adoption list.
- id: E3
  source_type: paper
  citation: Li and Ponticelli (2022), Going Bankrupt in China, Review of Finance26(3),449-486
  url: https://doi.org/10.1093/rof/rfab023
  date: 2022
  supports: [identity.assignment_mechanism, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.compliance, assignment.exposure_construction, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.population, empirical_requirements.required_fields, design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year, design_applications.research_question, design_applications.population, design_applications.outcome, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design]
  verification_status: reported
  access_level: full-text
  locator: AuthorFebruary14,2022 manuscript at https://jacopoponticelli.com/papers/Ponticelli_03_GoingBankruptInChina_RF.pdf,55pages; pp10-22,28-32,54-55 inspected, Sections2.2,3-3.2,4.1,4.4, Eq1-4, Table9 and appendixA1-A2. Publisher typesetting not inspected.
- id: E4
  source_type: replication
  citation: Author-linked Court Introduction Data, ChinaBankruptcy_Data.zip
  url: https://www.dropbox.com/s/tn7cwf3w3zadw2b/ChinaBankruptcy_Data.zip?raw=1
  date: null
  supports: [timeline.local_timing, assignment.exposure_construction, assignment.required_identifiers, empirical_requirements.treatment_source]
  verification_status: reported
  access_level: replication
  locator: Research page https://jacopoponticelli.com/research.html publication6 links archive; inspected both Stata files in memory. specialized_tribunals_dates has97rows and court/city/intro_date columns; specialized_courts_dates has9rows dated2019-2020. No estimation code or case/outcome panel in archive.
- id: E5
  source_type: archive
  citation: Supreme People's Court2016 report of Shenzhen bankruptcy information platform and historical tribunal
  url: https://www.court.gov.cn/zixun/xiangqing/16641.html
  date: '2016-02-15'
  supports: [timeline.local_timing]
  verification_status: verified
  access_level: official-document
  locator: Opening paragraph explicitly dates Shenzhen intermediate court's bankruptcy tribunal to1993; no evidence that author2007date represents first historical establishment.
design_applications:
- paper: Going Bankrupt in China
  doi: 10.1093/rof/rfab023
  journal: Review of Finance
  year: 2022
  research_question: Does specialized insolvency adjudication availability change local resource allocation and industrial capital productivity?
  population: Prefecture-city industrial aggregates in2011-2017
  outcome: log industrial value-added/tangible-assets ratio and log aggregate profits/total-assets ratio
  data_used: [Author court introduction inventory, China Statistical Yearbooks city aggregates]
  treatment_encoding: Post from first city specialization year including adoption year, Eq3; within2011-2017 this concerns earlier tribunals rather than2019new institutions
  comparison: City outcomes over time against other cities including never-adopters, with city/year FE and controls
  empirical_design: Table9PanelB weighted city-year TWFE, baseline2011 firm weights and city clustering; short eventual-adopter event study as sensitivity
  assumptions: [Conditional counterfactual city trends, No endogenous unobserved timing shocks, Reliable city-date joins and aggregate outcomes]
  threats_addressed: [Observable adoption hazard, City controls, Short pre-outcome event study]
  evidence_refs: [E3, E4]
method_transfer: null
readiness_blockers:
- Conditional regional comparison, not certified exogenous timing; cohort and spillover assumptions require a new application's own checks.
- Public archive contains dates only; code, city crosswalk and complete outcome panel were not inspected. Do not claim a turnkey replication or exact coding of blank high-court entries.
- Historical first establishment and author inventory dates differ for Shenzhen; daily precision and outside-window historical extensions need separate evidence. Do not silently overwrite the source date.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

Professional adjudication was intended to improve firm rescue and exit. The
2016 notice prioritizes specialized staffing while also requiring coordination
with local government [E1]. Institutional reform therefore does not itself
prove that political influence disappeared.

## What Changed

Cities gained access to specialized adjudication capacity at different times.
The regional application studies2011-2017, before the later named bankruptcy
tribunals. It is not a2019 reform or the national2007 bankruptcy-law change
[E3, reported claim]. The2016 plan's deadlines are implementation targets,
not observed inauguration dates [E2].

## Implementation and Assignment

Use the earliest relevant tribunal date within each prefecture, then code annual
availability. The public archive preserves court, city and date fields but lacks
a city crosswalk and analysis code [E4, reported claim]. Blank-city provincial
high-court rows cannot simply treat every city. Already-exposed cities are not
new adopters during the panel.

Shenzhen illustrates why the exposure and history must remain separate. Its
author row is January1,2007; official history dates its tribunal to1993 [E4;
E5]. Both imply availability throughout2011-2017. This discrepancy does not
create a within-panel treatment switch, but it rules out calling2007 a verified
first inauguration [analytical inference]. The2019 Shenzhen named tribunal is
listed among the intermediate court's internal institutions on its current
[official organization page](https://www.szcourt.gov.cn/nsjg/index.html);
do not translate the paper's new-court wording into an independently constituted
court without historical organizational evidence.

## Why This Creates Empirical Variation

Equation3 compares city outcomes around the first specialization year with other
cities. Table9PanelB weights by baseline firm counts and clusters by city.
The accounting outcomes measure aggregate average capital product and profitability,
not firm TFP. The result can reflect reallocation and composition as well as
changes within surviving firms [E3, reported claim; analytical inference].

The case-duration comparison is different. Equation2 compares courts within
the same city and case-acceptance year. Geography predicts case allocation but
does not make it random. The case platform also selects earlier cases surviving
to its2016 launch and omits many asset-poor short cases; in-progress cases are
censored atDecember2020 [E3, reported claim]. Those selection problems must not
be silently imported into—or claimed solved by—the city availability design.

## Identification Risks

Local economic circumstances can drive adoption. A hazard model with observable
trends does not remove unobserved shocks. The event study uses only eventual
adopters and a short two-year window; its absence of a never-treated group and
omitted adoption-year reference limit the interpretation [E3, reported claim].
A new study should examine treatment cohorts, already-treated cities and parallel
trends rather than assume all TWFE comparisons estimate the same effect.

## Data Requirements

The main contract joins annual industrial accounting aggregates to prefecture
availability. It does not require personal judge or creditor information. The
paper's separate zombie-industry labor measure first classifies listed firms
using discounted borrowing and below-sector-medianTFP, then maps64CSMAR industries
to20yearbook sectors. A decline in that employment share is not an observed
exit rate for all zombie firms [E3, reported claim]. That construction remains
a documented secondary application, not a mandatory union of data requirements.

## Evidence Notes

The court-date archive and author manuscript were inspected in memory; neither
is stored here. The original2014 guidance and full2016 work plan were not
inspected; E1 is an original notice and E2 an official plan explanation. The
primary policy supports the regime, while the author inventory supports reported
local exposure. Admission is conditional on a2011-2017 regional application;
it is not an exhaustive historical roster, replication certificate or assertion
that a specialized label establishes uniform actual court capability.
