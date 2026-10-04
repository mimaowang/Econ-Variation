---
schema_version: 2
id: china-2007-pollution-cadre-accountability-subsidy-exposure
name: China's 2007 Pollution-Target Cadre Accountability and Pre-Reform Firm Subsidy Exposure
aliases: [2007 national pollution control reform, pollutant targets in cadre evaluation, 节能减排一票否决, 国发2007年15号]
status: grounded
provenance:
  task_id: task-33bf3bb7fb2a
scope:
  country: China
  regions: [Mainland China, prefecture-level jurisdictions, industrial firms]
  domains: [environmental-economics, development-economics, firm-economics, regional-economics, political-economy]
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: >
    A mainland-wide change in local officials' pollution-control incentives can
    be studied through firms' different pre-existing relationships with local
    government. The paper's exposure is not a staggered local policy rollout:
    firms with and without pre-2007 subsidies face a common 2007 reform but
    potentially respond differently.
identity:
  instrument: >
    State Council 2007 energy-conservation and pollution-reduction work plan,
    especially binding SO2 and COD reduction targets incorporated into local
    government and cadre performance assessment with a one-vote veto.
  authority: State Council; local governments implement and are assessed through the central-local administrative hierarchy.
  legal_identifiers: ['国发〔2007〕15号, 国务院关于印发节能减排综合性工作方案的通知']
  implementation_regime: >
    The Eleventh Five-Year Plan had already set 2010 national reduction goals.
    The 2007 work plan made local responsibility, target decomposition,
    assessment and cadre consequences explicit. It instructed provinces to
    submit implementation plans by 2007-06-30. The plan also includes many
    regulatory and industrial measures; the research design cannot isolate
    cadre evaluation from every simultaneous environmental policy.
  assignment_mechanism: >
    The national change applies to local governments, not to firms selected by
    a lottery. Luo, Nian and Zhang use whether a firm received any government
    subsidy during 2001-2006 as a predetermined marker of a prior
    firm-government relationship, interacted with the post-2007 period.
    Subsidy receipt was discretionary and nonrandom; the policy did not assign
    reform eligibility according to that receipt.
  parent: null
  related_variations: []
timeline:
  announcement: '2007-06'
  effective: '2007'
  implementation_start: '2007'
  implementation_end: null
  local_timing: >
    The inspected State Council notice is dated by its 2007 document number and
    June 2007 publication; it orders local implementation plans by 2007-06-30.
    The paper codes 2007 onward as post-reform, but no firm-specific or city-
    specific implementation dates were recovered from these sources.
  anticipation: >
    The 2006-2010 pollution reduction goals predated the 2007 accountability
    strengthening. Firms or officials could anticipate stronger implementation;
    a 2007 post indicator is the paper's empirical convention, not proof of no
    earlier behavioral response.
  last_verified: '2026-10-04'
assignment:
  unit: Mainland industrial firm by year; the institutional incentive changes at local-government level.
  treated: Firms receiving at least one government subsidy in 2001-2006, observed after 2007.
  comparison_pool: Firms with no recorded subsidy in 2001-2006, observed in the same before/after window.
  rule: >
    Define firm_i treated from any positive pre-reform subsidy during 2001-2006
    in the Annual Survey of Industrial Firms; post_t is year >= 2007. Compare
    their interaction against never-subsidized firms, retaining the paper's
    sample exclusions and fixed-effects structure. Do not recode subsidy as a
    statutory eligibility rule or treat post-2007 subsidy receipt as baseline
    assignment.
  intensity: The paper checks pre-2007 subsidy frequency and amount as alternative exposure intensities; the baseline is any receipt.
  exemptions:
  - Four provincial-level municipalities are excluded from the paper's baseline sample because of different governance structure; this is a research-sample choice, not a formal exemption from the national policy.
  - Firms without any observed pre- or post-reform period are excluded from its within-firm comparison.
  compliance: >
    Formal local target accountability does not demonstrate identical enforcement
    in each city or firm. The paper studies differential response to incentives,
    not verified compliance by every local official.
  exposure_construction: >
    Merge Environmental Statistics firm-year emissions to ASIF firm-year
    subsidy and baseline characteristics, first by firm identifier-year and
    then by name-year where needed, deduplicating joins. Freeze subsidy status
    using 2001-2006 and interact it with year >= 2007. Preserve prefecture,
    industry, ownership and pre-reform covariates for the identification audit.
  required_identifiers: [firm identifier, firm name for secondary matching, year, prefecture, industry, pre-2007 subsidy receipt]
  spillovers: >
    A local government may pressure subsidized and unsubsidized firms, or firms
    may shift activity across jurisdictions. Relative firm-level contrasts can
    then differ from total citywide pollution changes.
research_compatibility:
  outcome_domains: [SO2 emissions, COD emissions, abatement, industrial production, local pollution concentrations]
  affected_populations: [industrial polluters, local governments, residents exposed to pollution]
  mechanism_channels: [cadre incentives, local pollution enforcement, prior government-firm reciprocity, abatement investment]
  best_for:
  - Testing heterogeneous firm responses to a common government-incentive change when pre-reform subsidy histories and pollution outcomes can be linked.
  - Studying local pollution consequences while separately measuring city-level exposure and recognizing that the firm DID is relative.
  not_good_for:
  - Claiming subsidy receipt itself was randomly assigned or mandated by the 2007 plan.
  - Reading the firm DID coefficient as the absolute pollution effect of the national reform.
  - Inferring city-specific treatment dates or statutory subsidy-based eligibility from the national document.
design:
  claim_type: causal
  affordances: [common national policy timing, predetermined heterogeneous firm exposure, firm-year pollution panel]
  candidate_designs: [firm-level difference-in-differences, event study of differential pre/post emissions, city-level exposure-share analysis]
  identifying_variation: >
    A common 2007 accountability change intersects with heterogeneous
    government-firm relationships measured before it. Identification of the
    interaction requires comparable counterfactual changes between firms with
    and without pre-reform subsidies, conditional on the controls, not merely
    that the central reform was national.
  primary_strategy: >
    Luo, Nian and Zhang compare SO2 and COD emissions of subsidized versus
    unsubsidized firms before and after 2007 in a 2001-2010 firm-year panel,
    with firm and two-digit-industry-by-year fixed effects plus pre-reform
    characteristics interacted with year. Their separate regional analysis
    aggregates pre-subsidized-firm exposure to cities and considers pollution
    concentrations; this is a different estimand and data join.
  estimand: Differential post-2007 emission change for previously subsidized versus unsubsidized firms in the matched industrial sample.
  treatment_variable: Indicator(any subsidy in 2001-2006) multiplied by indicator(year >= 2007).
  comparison_logic: Within-firm before/after change contrasted across predetermined subsidy groups; not a treated-city versus untreated-city rollout.
  estimation_notes: >
    The inspected author manuscript uses inverse-hyperbolic-sine emissions in
    its baseline, firm and two-digit-industry-by-year fixed effects, baseline
    covariates by year, and firm-clustered standard errors. It reports
    event-study, alternative inference and city-year robustness checks. Regional
    equations10-11 use a simple city mean of the frozen firm treatment indicator,
    interacted with year >=2007, city effects and province-year effects, and
    city-clustered errors. Pre-reform economic averages interact with year;
    weather controls use quantile-day shares except annual mean precipitation.
    SO2 is logged. Equation11 prints log COD but Table6 and TableA13 describe
    averaged COD without a log; that transformation needs code or final-version
    reconciliation before interpreting water coefficients as percentages.
  assumptions:
  - Without the reform, conditional emission trends for the two firm groups would have been comparable.
  - Differential contemporaneous policies, industry shocks, selection and reporting changes do not explain the interaction.
  - The pre-2007 subsidy marker captures the intended prior government relationship sufficiently for this contrast.
  diagnostics: [differential pre-trends, baseline covariate balance, alternative exposure intensity, non-targeted pollutants, city-year and finer-industry-year sensitivity, emissions-reporting sensitivity]
threats:
- type: nonrandom-subsidy-history
  basis: documented
  condition: Local governments had discretion over subsidies, and pre-subsidized firms differ in size, ownership or productivity; fixed effects do not remove different time-varying trends.
  evidence_refs: [E2]
  possible_diagnostics: [pre-trends, baseline-covariate-by-year interactions, matched or reweighted comparisons]
- type: bundled-environmental-policies
  basis: documented
  condition: The 2007 State Council plan contains other environmental enforcement, project-approval and industrial measures, so the cadre channel is not separately assigned.
  evidence_refs: [E1]
  possible_diagnostics: [mechanism outcomes, city-level policy controls, alternative pollutants]
- type: coverage-and-reporting
  basis: reported
  condition: Environmental Statistics covers major industrial polluters and relies on firm-reported emissions; matched data cannot represent every firm or directly measure ambient exposure.
  evidence_refs: [E2]
  possible_diagnostics: [sample-composition checks, monitoring-station or satellite corroboration]
- type: regional-outcome-and-linkage
  basis: reported
  condition: >
    Regional exposure is a sampled-firm share, not a statutory city rollout or
    the share of city emissions from treated firms. MERRA-2 is a reanalysis,
    not a set of direct city SO2 monitor readings. Sparse water stations and
    an elevation/distance-based downstream join can mix other cities' sources;
    the manuscript's COD transformation differs between equation and table notes.
  evidence_refs: [E4, E5]
  possible_diagnostics: [firm-size-weighted exposure, upstream COD placebo, unweighted COD, industrial SO2 emissions, actual river connectivity, exact outcome transformation]
empirical_requirements:
  contract_version: 1
  population: Mainland industrial firms in the paper's matched CESD-ASIF sample, excluding four provincial-level municipalities in its baseline.
  observation_unit: firm-year
  geography_level: prefecture linked to firm
  time_start: 2001
  time_end: 2010
  minimum_frequency: annual
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields: [firm-level SO2 or COD emissions, 2001-2006 subsidy amount or receipt, firm characteristics before 2007, industry, year, location]
  required_identifiers: [firm identifier or validated name join, year, industry, prefecture]
  treatment_key: [firm identifier, year, pre-2007 subsidy status]
  treatment_source: ASIF pre-2007 subsidy fields joined to CESD emissions, as described in the inspected author manuscript.
  measurement_risks: [nonrandom subsidy allocation, missing post-2007 ASIF subsidy values, firm ID/name matching errors, changing industrial survey coverage, self-reported emissions]
design_profiles:
- id: city-air-quality
  label: City SO2 concentration response to pre-subsidy firm share
  design_families: [continuous-exposure difference-in-differences, event study]
  when_to_use: >
    For the paper's regional air analysis, not its firm emission estimand. A
    lawful frozen firm sample supplies the city treatment share; inspect exact
    MERRA-2 variable, units and grid-to-city weights before reconstruction.
    Public gridded outcomes alone do not supply the restricted exposure inputs.
  outcome_domains: [City SO2 concentration]
  requirements:
    population: Mainland prefecture cities represented by the paper's firm sample and regional outcome joins
    observation_unit: city-year
    geography_level: prefecture city linked to province
    time_start: 2001
    time_end: 2010
    minimum_frequency: annual
    minimum_pre_periods: 6
    minimum_post_periods: 4
    required_fields: [Pre-2007 firm subsidy indicator, Firm-to-city membership and sample eligibility, Monthly MERRA-2 SO2 field and units, City boundaries and grid overlap, Province, Year, Pre-reform GDP per capita and fiscal revenue and population and industrial production, Weather controls for adjusted specifications]
    required_identifiers: [Firm identifier for exposure aggregation, Historical city/province crosswalk, Grid coordinates, Year]
    treatment_key: [City, Frozen pre-reform firm share, Year]
- id: city-downstream-water-quality
  label: Downstream COD response to pre-subsidy firm share
  design_families: [continuous-exposure difference-in-differences, event study]
  when_to_use: >
    For the regional water analysis using2004-2010 station readings, not a
    firm-COD panel or a station policy rollout. Reconcile logged versus level
    COD, exact downstream classification and missing-station treatment before
    replication; retain shared-station dependence and hydrological spillovers.
  outcome_domains: [Downstream COD concentration]
  requirements:
    population: Sample-linked cities with eligible downstream water stations within100km
    observation_unit: city-year constructed from station readings
    geography_level: city centroid linked to water stations and province
    time_start: 2004
    time_end: 2010
    minimum_frequency: annual
    minimum_pre_periods: 3
    minimum_post_periods: 4
    required_fields: [Frozen city pre-subsidy firm share, Station-year COD readings and units, Station coordinates, City centroid, Distance and downstream classification, Province, Year, Pre-reform economic averages, Weather controls for adjusted specifications]
    required_identifiers: [Historical city/province crosswalk, Water station identifier, Station coordinates, Year]
    treatment_key: [City, Frozen pre-reform firm share, Year]
evidence:
- id: E1
  source_type: policy-document
  citation: State Council. 2007. 国务院关于印发节能减排综合性工作方案的通知, 国发〔2007〕15号; NDRC official reproduction.
  url: https://www.ndrc.gov.cn/xxgk/zcfb/qt/200706/t20070604_967718_ext.html
  date: '2007-06'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.announcement, timeline.local_timing, assignment.compliance, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: 'Notice paragraphs II and final implementation paragraph; attached plan sections I(1), VI(22)-(24): binding targets, local target decomposition, cadre one-vote veto, and June 30 local-plan deadline; inspected 2026-10-02.'
- id: E2
  source_type: paper
  citation: 'Luo, Nian and Zhang. 2025-08-07. "Reciprocity and State Capacity: Evidence from a National Pollution Control Reform in China." Author manuscript, later published in Journal of Development Economics.'
  url: https://econ.pku.edu.cn/docs/2025-12/854e00b1d10d472a822e2088691e3118.pdf
  date: '2025-08-07'
  supports: [identity.assignment_mechanism, timeline.effective, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.intensity, assignment.exemptions, assignment.exposure_construction, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.population, empirical_requirements.observation_unit, empirical_requirements.time_start, empirical_requirements.time_end, empirical_requirements.required_fields, empirical_requirements.treatment_source, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design]
  verification_status: verified
  access_level: full-text
  locator: '79-page manuscript pp. 9-16, Sections 2.2-4.2: 2007 reform, subsidy exposure, CESD/ASIF join, exclusions, 2001-2010 sample, DID specification and identification risks; inspected 2026-10-02. Not compared against publisher typesetting.'
- id: E3
  source_type: other
  citation: Crossref DOI registration for Luo, Nian and Zhang, Journal of Development Economics, DOI 10.1016/j.jdeveco.2026.103905.
  url: https://doi.org/10.1016/j.jdeveco.2026.103905
  date: '2026'
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: 'Crossref work metadata retrieved 2026-10-02: title, authors, journal, DOI; 2027-01 volume/issue assignment is not the online publication year. Bibliographic identity only.'
- id: E4
  source_type: paper
  citation: Luo, Nian and Zhang, August7,2025 author manuscript, Section7 Aggregate Impacts
  url: https://econ.pku.edu.cn/docs/2025-12/854e00b1d10d472a822e2088691e3118.pdf
  date: '2025-08-07'
  supports: [assignment.intensity, design.estimation_notes, design.comparison_logic, threats.condition, design_applications.data_used]
  verification_status: reported
  access_level: full-text
  locator: >
    PDFpp32-35/printedpp31-34 Sections7.1-7.2 and footnotes51-56;
    PDFp59 Table6 and PDFp79 TableA13 read. PDFpp33-34 equations10-11 and
    PDFp59 Table6 visually inspected2026-10-04. Air2001-2010, water2004-2010;
    city treatment simple mean, baseline water inverse-distance downstream
    stations within100km. Table6 baseline counts2710 air and666 water city-years;
    fully controlled counts2653 and631, not counts of unique cities. No code inspected.
- id: E5
  source_type: official-data
  citation: NASA GMAO, MERRA-2 overview and system characteristics
  url: https://gmao.gsfc.nasa.gov/gmao-products/merra-2/
  date: null
  supports: [threats.condition, empirical_requirements.measurement_risks, design_applications.data_used]
  verification_status: verified
  access_level: official-document
  locator: >
    Overview paragraphs1-3 and linked system-characteristics page Configuration
    and Analysis system read2026-10-04. Reanalysis incorporates observations
    through a model/assimilation system;0.625degree longitude by0.5degree
    latitude, beginning1980. Does not verify the paper's chosen variable or
    spatial aggregation code.
design_applications:
- paper: 'Reciprocity and State Capacity: Evidence from a National Pollution Control Reform in China'
  doi: 10.1016/j.jdeveco.2026.103905
  journal: Journal of Development Economics
  year: 2026
  research_question: Did stronger pollution targets for local officials elicit different emission reductions from firms with prior government subsidy relationships?
  population: Mainland industrial firms in a matched Environmental Statistics and ASIF panel, excluding four provincial-level municipalities in the baseline.
  outcome: Firm-year SO2 and COD emissions; separate city-level pollution-concentration outcomes.
  data_used: [China Environmental Statistics Database, Annual Survey of Industrial Firms, NASA MERRA-2 M2TMNXAER regional SO2 as identified in the manuscript, China Environmental Yearbooks station COD2004-2010, City Statistical Yearbooks, NOAA weather station readings]
  treatment_encoding: Any subsidy receipt during 2001-2006 interacted with year >= 2007; alternative pre-subsidy frequency or amount.
  comparison: Previously unsubsidized firms over the same years, conditional on firm and industry-by-year fixed effects and baseline-covariate trends.
  empirical_design: 2001-2010 firm-year difference-in-differences, with a separate city-level exposure-share analysis.
  assumptions: [conditional parallel trends, stable and correctly linked pre-policy subsidy histories, no differential concurrent shock fully explaining the contrast]
  threats_addressed: [pre-trend event study, covariate-by-year adjustment, alternative inference and exposure checks, non-targeted pollutants and regional analysis]
  evidence_refs: [E1, E2, E3, E4, E5]
method_transfer: null
readiness_blockers: []
superseded_by: null
deprecation_reason: null
---

## Institutional Background

China's 2006-2010 plan retained a national goal of reducing major pollutants, but the author manuscript explains that earlier target setting had not sufficiently changed local officials' incentives [E2, reported claim]. The State Council's 2007 work plan explicitly makes local governments responsible for target completion, requires target decomposition to cities, counties and key enterprises, and links completion to cadre evaluation and a one-vote veto [E1]. The substantive shock is therefore to local-government accountability, not the creation of a firm-subsidy program.

## What Changed

The plan combines cadre consequences with monitoring, approval and industrial-policy measures [E1]. It names SO2 and COD as the main pollutant targets and calls for local implementation plans by June 30, 2007 [E1]. The paper's 2007 post indicator represents that national tightening. Neither the official notice nor the paper establishes that every local enforcement action started on the same day [E1, E2].

## Implementation and Assignment

Luo, Nian and Zhang compare firms that received any government subsidy in 2001-2006 with firms without recorded subsidies, before versus after 2007 [E2]. Local governments had discretion in allocating those pre-reform subsidies; they were not a legal assignment rule for the later reform [E2]. The analysis freezes subsidy exposure before the shock, merges firm-year pollution and industrial-survey records by identifier and then name, and excludes the four provincial-level municipalities and firms without observations on both sides of the reform in the baseline [E2]. This is a national-policy-by-prior-relationship contrast, not staggered city adoption.

## Why This Creates Empirical Variation

The common government-incentive shift could make officials ask more of firms with which they already had support relationships. A differential change in those firms' SO2 or COD emissions supplies the empirical variation [E2, reported interpretation]. The coefficient is relative to unsubsidized firms; it cannot alone measure the national policy's total pollution effect. The authors separately aggregate firm exposure to cities and examine concentration outcomes for a regional question [E2].

## Identification Risks

The central reform may be plausibly external to a particular firm's subsidy history, but subsidy histories are selected, and groups could have different counterfactual trends [E2]. The 2007 plan also bundles several policy instruments, so a clean cadre-only mechanism is not assigned [E1]. Survey coverage, reporting and name-based matching may shift the analytic sample [E2]. Pre-trends, baseline-covariate-by-year adjustments, alternative pollutants and city-level evidence can probe these problems but do not make subsidy assignment random [E2; analytical inference].

## Data Requirements

A replication needs a firm-year panel from 2001-2010 with pre-2007 subsidy histories and SO2 or COD emissions, valid firm identifier/name joins, industry and prefecture, and sufficient observations on both sides of 2007. The inspected manuscript reports 23,609 firms and 143,524 firm-year observations after its exclusions [E2]. That is its matched sample, not a promise that CESD/ASIF access or the same join is available to a new researcher. Keep the separate regional pollution data and city exposure-share construction distinct from the firm-level requirement.

The regional analysis takes the simple average of the frozen firm treatment indicator within a city, not an emissions-weighted share. A pre-reform firm-size-weighted version is a robustness check. City air outcomes span2001-2010; the MERRA-2 monthly product is aggregated to city-year and logged in equation10 [E4, reported claim]. NASA describes MERRA-2 as reanalysis that assimilates observations, not direct city monitor measurements [E5]. Exact field, units and grid-to-boundary weights remain reconstruction conditions; substituting an arbitrary satellite series would not reproduce the paper.

Water outcomes have a shorter2004-2010 window. The paper averages readings from downstream stations within100km of the city centroid using inverse-distance weights; upstream readings and unweighted downstream averages are checks [E4, reported claim]. A station can represent upstream sources from more than one city, so city-clustered errors do not by themselves remove all shared hydrological dependence [analytical inference]. Equally important, equation11 prints log COD while Table6's note describes the averaged COD level. This record preserves the discrepancy instead of assigning percentage effects to a transformation that has not been reconciled [E4].

## Evidence Notes

The official State Council document establishes the national target, local accountability mechanism and 2007 implementation direction [E1]. The inspected 2025 author manuscript establishes the actual paper-used treatment, comparison, sample and design [E2]. Crossref establishes the later Journal of Development Economics DOI and bibliographic identity [E3]; its issue is assigned to January 2027, while the online article was reported in 2026. The publisher's final typeset methods were not inspected, so substantive claims remain explicitly tied to the author manuscript, and no city-specific implementation roster is implied.

Audit `task-33bf3bb7fb2a` added the two regional data contracts after reading Section7 and visually checking its equations and Table6 [E4]. They are applications of the same policy-by-prior-relationship variation, not extra cases. Public pollution measurements do not eliminate the need for lawful firm exposure data. No paper PDF or restricted data were stored, and no estimates were reproduced.
