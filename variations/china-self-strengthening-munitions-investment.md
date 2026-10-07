---
schema_version: 2
id: china-self-strengthening-munitions-investment
name: China self-strengthening munitions-factory investment and civilian industrial development
aliases: [洋务运动军工投资, Self-Strengthening Movement military factories, late Qing arsenal placement]
status: grounded
provenance:
  task_id: task-9c88d6b229ad
scope:
  country: China
  regions: [Mainland historical counties in the paper's core-province sample]
  domains: [development, regional-economics, industrial-economics, industrial-development, economic-history]
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: Mainland military-factory placement and investment are actually used to study civilian industrial entry and output; the historical national roster is broader than the served mainland research sample.
identity:
  instrument: County exposure to state munitions factories and military shipyards established during the1861–1894 Self-Strengthening Movement.
  authority: Qing provincial governors and viceroys proposed and financed establishments with imperial approval; individual factories were supervised by state officials.
  legal_identifiers: [Factory-specific memorials to the throne reproduced in the1993 Second Historical Archives collection, Fujian shipbuilding memorial of1866-06-25 and imperial approval of1866-07-14]
  implementation_regime: Decentralized military modernization funded and implemented by provincial officials, involving imported machinery and technicians. This is not a single uniform nationwide civilian subsidy. Factories and shipyards were established at different dates;1894 is the investment window endpoint, not a universal closure date.
  assignment_mechanism: Provincial political support interacted with defense needs, waterways, mineral access, capitals and foreign machinery access. Placement was selective. The paper compares historical host counties with nonhost counties and separately instruments accumulated investment with preprogram correspondence ties and governor-residence distance.
  parent: null
  related_variations: []
timeline:
  announcement: Factory-specific proposals and approvals; no common national announcement assigns all counties in1861.
  effective: Establishment years in Appendix TableA1 are the paper's exposure clock, distinct from a first output or full-capacity date.
  implementation_start: 1861
  implementation_end: 1894
  local_timing: The national narrative begins1861; the starred factory rows in the inspected sample run1865–1890. Jiangnan is dated1865; Fujian shipbuilding is dated1866.1895 deregulation of private entry and subsequent New Policies change the response environment, not the factory's first-treatment year.
  anticipation: Proposals, fundraising and procurement precede establishment. Governors sometimes moved machinery between provinces. Audit founding versus relocation and operational timing for any new outcome.
  last_verified: '2026-10-07'
assignment:
  unit: Historical county-year for establishment exposure; historical county for accumulated investment.
  treated: The published sample contains16 military-host counties among1432 counties matched to1911 boundaries in15 core provinces. TableA1 stars23 factories in the sampled provinces; factories are not23 independent county treatments. Taiwan and Tainan rows are unstarred and are outside the served mainland sample.
  comparison_pool: Other1416 sampled counties and pretreatment host-county years in1858–1937. CEM alternatives retain31 or317 counties depending on binning; these are alternative comparison populations, not the full national set of untreated places.
  rule: Set host_ct=1 from the first sampled munitions-factory establishment in county c onward;0 before or for nonhosts. For the1933 application aggregate documented military investment over1861–1894 by1911 county and use log(1+investment).
  intensity: Binary establishment onset in the panel; accumulated investment in taels in the cross section. These encode the same program with different estimands, not separate policy records.
  exemptions: [Unsampled provinces, Taiwan and Tainan, Civilian firms are outcomes rather than military-factory treatment, No automatic whole-province exposure]
  compliance: Establishment is not equal investment or performance. State supervision and poor efficiency make exposure distinct from successful modernization.
  exposure_construction: Recover Fan2003 factory histories and AppendixA1, deduplicate factories within counties, retain first establishment year and aggregate investment. Match factory and civilian-firm locations to CHGISv6 county records for1911 before county-year aggregation. Resolve historical names and relocations rather than applying current county codes. TableA1's Shandong location is not itself a county identifier; retrieve the underlying history or author crosswalk for that row.
  required_identifiers: [factory_name, historical_county_id_1911, prefecture_id, province_id, establishment_year, observation_year]
  spillovers: Procurement, technical skills and shared inputs can spread outside host counties. Paper prefecture and neighboring-county exercises do not establish absence of spillovers for every outcome or later period.
research_compatibility:
  outcome_domains: [civilian industrial firm entry, civilian industrial output, industrial agglomeration, industrial input-output linkages]
  affected_populations: [mainland historical industrial counties, civilian industrial entrants]
  mechanism_channels: [local intermediate-input demand, technical human capital, supporting institutions, private-entry deregulation]
  best_for: [historical place-based military investment and civilian industrial development, industrial-policy complementarities with market entry]
  not_good_for: [modern firm effects without a historical bridge, random placement claims, all34 factories as mainland sample treatment, universal welfare returns to military investment]
design:
  claim_type: reduced-form
  affordances: [staggered county establishment exposure, historical investment intensity with a political-network instrument]
  candidate_designs: [county-year DID and event study, county cross-sectional2SLS]
  identifying_variation: First military-factory establishment at different dates across sampled counties; accumulated investment varies with pre1861 political ties and subsequent governor postings weighted by residence distance.
  primary_strategy: The panel regresses log(1+new civilian firms) on absorbing establishment exposure with county/year effects, prefecture trends and cross-sectional controls interacted with decades; standard errors cluster by prefecture. The1933 application instruments log(1+military investment) in a prefecture-FE cross-sectional regression.
  estimand: Conditional host-county change in civilian entry in the panel; investment-induced change in log(1+1933 civilian output) under the instrument's identifying assumptions in the cross section. Neither is automatically an average national industrial-policy effect.
  treatment_variable: host_ct in the panel; log(1+county military investment in taels) in1933 cross-sectional analysis. IV_c=sum_j(pre1861 movement-related letters for governor j serving c during1861–1894)/(distance to governor residence+1), following Eq4.4 and AppendixC.
  comparison_logic: Panel identification requires counterfactual trends conditional on selective placement and changing controls. Cross-sectional2SLS requires relevance and no direct effect of political ties or weighted administrative proximity on civilian output except through military investment; central appointments and rotation are the paper's argument, not proof.
  estimation_notes: Table3 reports114560 county-years. Table5 reports1432 counties and prefecture-clustered inference. AppendixC searches2238 letters from1841–1860, restricting to subsequent governors and classifying277 as movement-related with nine keywords. Both xunfu and zongdu count. Matched comparisons and insignificant pretrends do not eliminate selection. Log(1+x) coefficients with zeros are not universal percentage elasticities. Data are available on request, not a verified public replication deposit.
  assumptions: [conditional parallel trends, correct first-treatment clock and historical joins, adequate comparison support, instrument relevance and exclusion, no unhandled spatial interference, stable outcome coverage]
  diagnostics: [pretrend power and cohort sensitivity, matched-sample support, relocation and founding-date sensitivity, prefecture dependence with few treated counties, governor-distance direct paths, placebo correspondence and instrument relevance, historically measured outcome missingness]
threats:
  - type: selective-placement
    basis: documented
    condition: Geography and provincial political support influence assignment; balance differences remain on some political and economic measures.
    evidence_refs: [E1, E2]
    possible_diagnostics: [selection covariates and trends, CEM support, alternative historical controls]
  - type: exclusion-restriction
    basis: inferred
    condition: Governor ties and proximity can affect other investment or governance; historical rotation and placebo results do not rule out every direct path.
    evidence_refs: [E1, E2]
    possible_diagnostics: [residence-distance controls, other public investment paths, post1872 subset, placebo-letter instrument]
  - type: historical-geography-and-timing
    basis: documented
    condition: Multiple factories share counties, some factories relocate, and the national roster extends beyond the mainland sample. The Shandong row needs a historical county crosswalk.
    evidence_refs: [E1, E2]
    possible_diagnostics: [audited1911 joins, preserve unsampled flag, relocation alternatives, distinguish proposal construction and operation]
  - type: outcome-selection
    basis: reported
    condition: Entry sources cover capital-qualified firms and lack annual exits; the1933 census excludes some sectors and small workshops. These are different populations, not interchangeable measures of all firms or welfare.
    evidence_refs: [E1, E2]
    possible_diagnostics: [coverage by county and sector, source overlap, monetary comparability, avoid interpreting entry as net firm stock]
empirical_requirements:
  contract_version: 1
  population: Mainland historical counties in the paper's1432-county15-province risk set; use author sample membership rather than every location on the national factory roster.
  observation_unit: county-year
  geography_level: historical county on1911 boundaries
  time_start: 1858
  time_end: 1937
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields: [civilian firm establishment year and location, civilian firm capital and ownership for coverage definition, factory establishment year and location, sample membership, historical county boundary crosswalk, geographic and political selection covariates for conditional comparisons]
  required_identifiers: [historical_county_id_1911, prefecture_id, year]
  treatment_key: [historical_county_id_1911, year]
  treatment_source: Fan2003 and published AppendixA1; historical factory histories resolve first establishment and relocation. Author data are on request.
  measurement_risks: [historical location ambiguity, firm source thresholds and omissions, missing exit dates, relocation clocks, posttreatment controls, sparse pretreatment entries]
design_profiles:
  - id: county-entry-panel
    label: Historical civilian firm-entry panel
    design_families: [DID, event-study]
    when_to_use: For annual civilian entry following factory establishment, with the1858–1937 historical county-year data and audited first-treatment dates.
    outcome_domains: [civilian industrial firm entry]
    requirements:
      population: Mainland1432-county historical risk set or an explicitly justified comparable subset.
      observation_unit: county-year
      geography_level: historical county on1911 boundaries
      time_start: 1858
      time_end: 1937
      minimum_frequency: annual
      minimum_pre_periods: 3
      minimum_post_periods: 3
      required_fields: [annual civilian firm entry, first factory establishment year, sample membership, historical county crosswalk, selection covariates]
      required_identifiers: [historical_county_id_1911, prefecture_id, year]
      treatment_key: [historical_county_id_1911, year]
  - id: county-output-1933-iv
    label: Historical investment and1933 civilian industrial output
    design_families: [IV, cross-section]
    when_to_use: For the long-run output application, with accumulated investment and the exact governor-correspondence instrument; annual entry is not a substitute for output.
    outcome_domains: [civilian industrial output]
    requirements:
      population: Mainland1432 counties linked to the1933 industrial census and1911 boundaries.
      observation_unit: county
      geography_level: historical county on1911 boundaries
      time_start: 1933
      time_end: 1933
      minimum_frequency: cross-sectional
      minimum_pre_periods: 0
      minimum_post_periods: 1
      required_fields: [1933 civilian industrial output,1861–1894 accumulated factory investment in taels,1841–1860 classified governor correspondence,1861–1894 governor appointment and jurisdiction, governor residence distance, selection covariates, historical county crosswalk]
      required_identifiers: [historical_county_id_1911, prefecture_id, governor_id]
      treatment_key: [historical_county_id_1911]
evidence:
  - id: E1
    source_type: paper
    citation: 'Bo, Liu and Zhou (2023). Military investment and the rise of industrial clusters: Evidence from China’s self-strengthening movement. Journal of Development Economics161:103015.'
    url: https://doi.org/10.1016/j.jdeveco.2022.103015
    date: 2023
    supports: [identity.assignment_mechanism, identity.implementation_regime, timeline.local_timing, timeline.anticipation, assignment.treated, assignment.comparison_pool, assignment.rule, assignment.compliance, assignment.exposure_construction, design.primary_strategy, design.treatment_variable, design.estimation_notes, empirical_requirements.population, design_applications.empirical_design]
    verification_status: reported
    access_level: full-text
    locator: Final19-page journal PDF linked by Cong Liu's research page, public Dropbox file BoLiuZhou_SSM_Final.pdf; inspectedpp2–12 and16–17, Sections2–4, Eqs4.1–4.4, Tables1–5 and data-availability statement. Online date2022-11-29, journal year2023. Not an independently rerun result.
  - id: E2
    source_type: appendix
    citation: Publisher online appendix to Bo, Liu and Zhou JDE103015.
    url: https://ars.els-cdn.com/content/image/1-s2.0-S0304387822001572-mmc1.pdf
    date: 2023
    supports: [identity.legal_identifiers, identity.assignment_mechanism, timeline.effective, assignment.treated, assignment.rule, assignment.intensity, assignment.exposure_construction, design.treatment_variable, empirical_requirements.required_fields, empirical_requirements.treatment_source, design_applications.data_used]
    verification_status: reported
    access_level: appendix
    locator: Inspected17-page supplement PDFpp1–8/printed54–61; AppendixA translated Grand Council memorial excerpts, B1 firm-entry/census coverage, B2 investment source, C exact correspondence construction, TableA1 complete roster visually inspected atPDFp8. Earlier title preserved in the appendix, same publisher PII. Original archive books and author code not inspected.
  - id: E3
    source_type: archive
    citation: National Museum of China collection account, 江南制造局在1865-1885年间所造船只清单.
    url: https://www.chnmuseum.cn/zp/zpml/gmww/202104/t20210406_249554.shtml
    date: '2021-04-06'
    supports: [identity.instrument, identity.authority, identity.implementation_regime, timeline.local_timing]
    verification_status: verified
    access_level: official-document
    locator: Complete collection description verifies Jiangnan's1865 Shanghai establishment, Zeng/Li role and military production/imported machinery. Supports that example, not independent verification of every roster row.
  - id: E4
    source_type: archive
    citation: Fuzhou local gazetteer commission, 船政创办的历史背景和发展过程, extract from 船政志.
    url: https://www.fuzhou.gov.cn/zgfzzt/zjrc/mdfc/lswh/201809/t20180928_2624963.htm
    date: '2018-09-28'
    supports: [identity.instrument, identity.authority, identity.legal_identifiers, timeline.effective, timeline.anticipation, assignment.compliance]
    verification_status: verified
    access_level: official-document
    locator: Memorial1866-06-25, approval1866-07-14, leadership transfer and construction start1866-12-23; factory/school expansion under Shen illustrates differentiated implementation. This corroborates the Fujian example, not every host or investment amount; approval/construction are not first output.
design_applications:
  - paper: Military investment and the rise of industrial clusters
    doi: 10.1016/j.jdeveco.2022.103015
    journal: Journal of Development Economics
    year: 2023
    research_question: Did military modernization investment generate civilian industrial development?
    population: Mainland1432 historical counties,16 treated county hosts; narrower matched alternatives.
    outcome: Annual civilian industrial firm entry and1933 civilian industrial output.
    data_used: [Du1991 and2019 firm histories, Fan2003 military factories and investment, Liu1937 industrial census, CHGISv6, Zeng2011 correspondence, Wei2013 governor appointments]
    treatment_encoding: Absorbing first establishment for entry; log(1+accumulated military investment) for output, instrumented with governor ties weighted by residence distance.
    comparison: County/year FE and prefecture trends for entry; prefecture FE and selection covariates for1933 output; prefecture-clustered inference.
    empirical_design: Panel DID/event-study with CEM alternatives and cross-sectional2SLS.
    assumptions: [conditional parallel trends, exclusion and relevance, stable historical geography and coverage]
    threats_addressed: [reported matched comparisons and pretrends, reported distance controls and placebo correspondence, reported post1872 and prefecture sensitivities]
    evidence_refs: [E1, E2]
method_transfer: null
readiness_blockers:
  - Conditional historical use requires the underlying roster-to1911 county join, especially the Shandong row and relocated factories; a current county-name merge is not adequate. The decision contract is documented, not a ready-to-download replication dataset.
  - For the IV application recover the actual letter classification and governor posting aggregation before estimation; generic ties or distance alone do not reproduce Eq4.4. Exclusion must be defended for the chosen outcome.
  - New outcomes or later periods require reassessing private-entry deregulation, war disruption, policy overlap and spillovers; the published diagnostics do not certify those extensions.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

The change was a geographically uneven effort to build military manufacturing,
not an intrinsically exogenous industrial policy. Provincial officials proposed
factories, mobilized funds and chose sites; defense concerns and machinery access
also mattered [E1, E2, reported claim]. The National Museum verifies the1865
Jiangnan example [E3]. Fujian's gazetteer separates the1866 proposal, imperial
approval and construction dates [E4]. These examples corroborate the regime
without pretending to independently verify all factory histories.

## What Changed

Military factories brought machinery, technical workers and manufacturing
facilities to selected places. The empirical treatment is establishment or
investment, not successful production, equal local support or one common
national switch [E1, E2, reported claim].

## Implementation and Assignment

Use AppendixA1's sampled-province flag, not every national roster row. It includes
Taiwan and Tainan, which are not in the served mainland sample. Several factories
share a county; the paper reports16 host counties rather than34 independent
treatments [E1, E2, reported claim]. The broad1861 program start must not overwrite
county establishment dates. The Shandong location label needs the underlying
historical join before an executable treatment vector can be reconstructed.

## Why This Creates Empirical Variation

The entry panel follows first military establishment; the output application
follows accumulated investment. They belong in one institutional case with two
data contracts. Do not require correspondence data for a panel-entry question,
or accept entry data as a replacement for1933 output in the IV question. The
instrument combines preprogram letters with later governor assignments and
residence distance [E1, E2, reported claim]. Political connections are not another
standalone shock and are not automatically valid instruments for unrelated outcomes.

## Identification Risks

The paper's own chronology points to private-entry deregulation as a complement
to military investment [E1, reported claim]. A delayed entry response need not be
an implementation delay. Matching narrows support, while the governor network
could affect other local policies [analytical inference]. Review those paths,
the small number of host counties and historical control measurement rather
than inheriting the paper's causal language.

## Data Requirements and Evidence Boundary

Entry records have capital thresholds and lack annual exits; the census covers
selected powered factories with more than30 workers and excludes munitions
factories and several other sectors [E2, reported claim]. Thus the outcome does
not merely count the original military establishments, but it also does not
measure every civilian enterprise. Locations are harmonized to1911 boundaries
[E1, reported claim]. Author data are available on request; no public replication
package was verified. The record supports a conditional research decision, not
a claim of completed independent replication.

## Evidence Notes

The final journal body and publisher appendix close the actual application
and measurement definitions. Historical official sources corroborate two
establishments and the distinction between approval and implementation.
Uninspected archival books and unavailable author microdata remain named
reconstruction needs, not independently verified facts. No paper or sensitive
data is deposited in this repository.
