---
schema_version: 2
id: china-chongqing-2011-residential-property-tax
name: Chongqing2011 Selected-Property Residential Tax Regime
aliases: [Chongqing property-tax pilot, 重庆个人住房房产税试点, 重庆市人民政府令第247号]
status: grounded
provenance:
  task_id: task-ba3daf6a8947
scope:
  country: China
  regions: [Chongqing main urban nine districts, mainland China]
  domains: [urban, housing, public-finance, regional-economics]
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: The initial Chongqing pilot taxes specified detached/high-price homes and defined nonlocal purchases within nine urban districts; a published Chinese price study uses the pilot, with detailed counterfactual methods inspected in its working version.
identity:
  instrument: Initial2011 personal-home property tax on defined dwelling/buyer categories within Chongqing's main urban nine districts. Includes existing detached commercial homes, new high-price homes and specified new ordinary homes; not an all-municipality universal housing tax.
  authority: Chongqing Municipal People's Government under State Council136th executive-meeting authorization; property-location tax authorities and cooperating housing/household/business/labour departments.
  legal_identifiers: [重庆市人民政府令第247号, 重庆市关于开展对部分个人住房征收房产税改革试点的暂行办法, 重庆市个人住房房产税征收管理实施细则]
  implementation_regime: Original January2011 regime. Later2017 buyer-category expansion and2023/2024 amendments are not backcast into the2011-2012 application.
  assignment_mechanism: City-area intervention with statutory property-type, transaction-price and buyer-status eligibility. The inspected price application uses aggregate Chongqing outcomes rather than a randomized tax designation or a transaction-threshold RD.
  parent: null
  related_variations: [china-shanghai-2011-residential-property-tax]
timeline:
  announcement: '2011-01-27'
  effective: '2011-01-28'
  implementation_start: '2011-01-28'
  implementation_end: null
  local_timing: Original rule effective January28; liability begins the month following acquisition, with registration-date clarification in Article14. New-built purchase timing follows contract submission to the registration centre; existing-home purchases use transfer/change registration. The inspected draft predicts February2011-March2012 after fitting through January.
  anticipation: Housing-policy debate and announcement can affect expectations and transactions; first formal liability does not eliminate advance purchasing or price anticipation.
  last_verified: '2026-10-04'
assignment:
  unit: Property-owner/family for liability inside the nine-district pilot; aggregate Chongqing administrative-unit-month in the inspected application.
  treated: Personally owned detached commercial homes, newly bought high-price homes at least twice the previous two years' main-nine-district average price per square meter, and new second-plus ordinary homes bought by people simultaneously without Chongqing hukou, enterprise or employment, subject to the original exemptions.
  comparison_pool: Inspected draft aggregate price donors are Jiangsu, Zhejiang, Beijing and Sichuan. They are provincial/municipal forecasting comparators, not untreated low-price Chongqing dwellings; Shanghai is itself a simultaneous pilot.
  rule: Initial geographic boundary is Yuzhong, Jiangbei, Shapingba, Jiulongpo, Dadukou, Nanan, Beibei, Yubei and Banan, including specified development areas. Eligibility distinguishes detached stock, new high-price purchases and defined nonlocal second-plus purchases.
  intensity: Initial transaction-value base after exempt area; detached/high-price homes below three times the reference average use0.5%, three-to-below-four times1%, and at least four times1.2%. Defined nonlocal ordinary homes use0.5%. Two times determines high-price eligibility, not the first tax-rate step; these thresholds are not an RD used by the inspected paper.
  exemptions:
  - A family may deduct exempt area for one taxable home; pre-rule detached stock has180 square meters, newly bought detached/high-price homes100 square meters. New and old detached homes do not share a blanket180-square-meter allowance.
  - The defined no-hukou/no-enterprise/no-job buyer category receives no area deduction; satisfying any one status condition later permits ordinary-home exemption/refund for that year.
  - Original rule exempts self-built homestead housing and permits specified hardship/force-majeure relief; this urban-tax application is not an agriculture study.
  compliance: Tax authorities use housing/status information, annual payments prorated by months and transfer clearance. Once a detached/high-price home enters coverage, absent new rules its taxable status and assigned transaction value/rate persist through ownership transfer. City status alone does not establish collection.
  exposure_construction: >
    For aggregate price analysis, align Chongqing's historical geographic
    price coverage with the original nine-district pilot, mark January28
    and use the draft's February post-forecast window. Fit pre-period
    log prices on Jiangsu, Zhejiang, Beijing and Sichuan donor prices,
    intercept, post-November2008 indicator and optional trend. For actual
    liability, join property location/type, new-versus-existing status,
    relevant purchase/ownership dates, price per square meter, the
    contemporaneous two-year reference average, household area-deduction
    history and the buyer's simultaneous status conditions. The paper's
    aggregate forecast is not a property-level threshold estimate. Do
    not treat the whole Chongqing municipality as legally covered or use
    later amended rules to impute2011 liability.
  required_identifiers: [historical_administrative_unit_id, calendar_month]
  spillovers: Demand can shift from taxed high-price/detached homes into exempt segments, and across districts/cities. Aggregate price changes can reflect both relative prices and transaction mix; donor markets can also be affected.
research_compatibility:
  outcome_domains: [Housing prices, Housing-demand composition, Wealth, Local public finance]
  affected_populations: [Home owners/buyers in the original nine-district pilot and connected housing markets]
  mechanism_channels: [Recurring ownership cost, Property-segment substitution, Tax capitalization, Public-rental-housing funding]
  best_for: [Housing-market responses to a selective tax when geographic coverage and property composition can be made explicit.]
  not_good_for:
  - Uniform tax incidence on every Chongqing resident or home.
  - Calling a high-end-to-low-end spillover causally identified from post-only price charts.
  - A paper-used price-threshold RD inferred solely from the statutory threshold.
design:
  claim_type: reduced-form
  affordances: [Known initial legal date, Explicit nine-district boundary, Distinct stock/new and property/buyer eligibility]
  candidate_designs: [Single-unit counterfactual forecasting with defended coverage, Property-liability comparison only with additional selection and continuity evidence]
  identifying_variation: Aggregate Chongqing price divergence from a fitted donor-price relation after a selective tax introduction, conditional on geographic alignment, stable counterfactual relation and concurrent-policy separation.
  primary_strategy: Inspected September2012 working version uses equation16 separate-city OLS with donor log prices, intercept, post-November2008 dummy and optional trend; fitting March1998-January2011 and forecasting February2011-March2012. Publication metadata confirms the counterfactual framework, not all draft specifications.
  estimand: Short-post-period aggregate price gap against a predicted no-pilot path, combining taxed and exempt-market responses within the outcome's actual coverage.
  treatment_variable: Chongqing intervention date in an aggregate forecast design; property eligibility, price-ratio thresholds and rates are institution details, not estimated RD treatment in the inspected application.
  comparison_logic: The pre-fitted provincial/municipal donor relation predicts a counterfactual. OLS donor weights can be negative and are not convex SCM weights; regional shocks or spillovers can invalidate extrapolation.
  estimation_notes: The draft reports155 pre-months and14 post-months, fitting/trend and growth sensitivity. Housing-size NBS series begin at treatment and supply suggestive patterns only; the draft explicitly says they do not test the proposed spillover. Final2014 methods and code were not inspected.
  assumptions: [Stable pre-fitted donor relation and defended time-series restrictions, Comparable outcome geography/measurement, No unseparated local housing-policy break, Limited donor spillovers and composition artifacts]
  diagnostics: [Withheld pre-period forecasts, Donor/trend/placebo sensitivity, Nine-district versus outcome-coverage audit, Comparable property-type pre/post prices with an actual counterfactual]
threats:
- type: selective_tax_and_geographic_aggregation
  basis: documented
  condition: Legal assignment covers specific homes/buyers in nine urban districts; aggregate Chongqing data can include different geographic/property coverage. An aggregate gap is not a per-taxpayer effect or proof of municipality-wide legal treatment.
  evidence_refs: [E1, E2]
  possible_diagnostics: [Recover historical geographic reporting coverage, Distinguish liability from equilibrium exposure, Examine composition-stable prices]
- type: statutory_simplification_and_version_drift
  basis: documented
  condition: The draft simplifies coverage as high-end homes and treats detached-home area generically. Original rules also include the defined nonlocal ordinary-home category and distinguish180-square-meter old stock from100-square-meter new purchases. Later consolidated rules are not the2011 text.
  evidence_refs: [E1, E2]
  possible_diagnostics: [Use original legal version, Recover property/buyer histories, Do not infer2011 eligibility from current summaries]
- type: forecast_and_spillover_attribution
  basis: reported
  condition: Donor forecasts rely on stable relations; post-only size indexes do not identify segment substitution. Pilot selection, concurrent housing/credit measures and regional shocks can produce aggregate breaks. Publication metadata does not verify final code or data availability.
  evidence_refs: [E2, E3]
  possible_diagnostics: [Out-of-sample forecasting, Comparator policy chronology, Final-version reconciliation, Segment-specific pre-period and counterfactual evidence]
empirical_requirements:
  contract_version: 1
  population: Aggregate Chongqing housing-price coverage must be reconciled with the original nine-district tax boundary; documented donor provincial/municipal markets.
  observation_unit: administrative-unit-month
  geography_level: municipality/province price series versus urban nine-district legal assignment
  time_start: '1998-03'
  time_end: '2012-03'
  minimum_frequency: monthly
  minimum_pre_periods: 155
  minimum_post_periods: 14
  required_fields: [Comparable historical monthly Chongqing and donor prices, Reporting geography/property composition and vintage, Initial pilot and concurrent housing-policy dates, Explicit donor-selection/trend specifications]
  required_identifiers: [historical_administrative_unit_id, calendar_month]
  treatment_key: [historical_administrative_unit_id, calendar_month]
  treatment_source: Original Order247 establishes legal boundary, eligibility and timing; the inspected draft supplies aggregate price forecasting, not a property-tax payment panel.
  measurement_risks:
  - Historical NDRC price-series access and precise geographic coverage were not independently recovered; author-provided data provenance is reported, not a public-download assurance.
  - The draft flags the January2011 NBS measurement break; post-only size series cannot supply the missing pre-treatment segment counterfactual.
  - Property-level extension requires IDs, price/reference-year ratios, dates, family exemptions and buyer status; aggregate city IDs alone cannot construct liability.
evidence:
- id: E1
  source_type: policy-document
  citation: Original Chongqing Municipal Government Order247, January27,2011, pilot temporary rules and implementing details.
  url: https://cq.gov.cn/zwgk/zfxxgkml/szfwj/fzhsxgz/fzhsxzfgz/201101/W020210205087116420790.pdf
  date: '2011-01-27'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.announcement, timeline.effective, timeline.implementation_start, timeline.local_timing, assignment.unit, assignment.treated, assignment.rule, assignment.intensity, assignment.exemptions, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: Nine-page original government PDF, temporary-rule PartsI-XII and implementing Articles3-14 inspected2026-10-04. Header Order247 and original second-plus nonlocal category distinguish this text from later amendments; HTML access timed out but original PDF was readable.
- id: E2
  source_type: paper
  citation: Bai, ChongEn, Qi Li and Min Ouyang, September2012 working version of Property Taxes and Home Prices, institution-hosted; publication is the citation target.
  url: https://www.ckgsb.edu.cn/Userfiles/doc/9.24%20Property%20Taxes%20and%20Home%20Prices%20A%20Tale%20of%20Two%20Cities.pdf
  date: 2012
  supports: [assignment.comparison_pool, assignment.exposure_construction, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.required_fields, empirical_requirements.measurement_risks, design_applications.population, design_applications.outcome, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design]
  verification_status: reported
  access_level: full-text
  locator: Version header and Sections2-5, especially printedpp10-16 equation16, donors and Section5 spillover limits inspected2026-10-04. Draft-specific information; no final-method equivalence or executable replication claim. PDF circulation/citation notice retained; file not redistributed.
- id: E3
  source_type: paper
  citation: Bai, Li and Ouyang2014, Journal of Econometrics180(1),1-15; publication metadata and abstract supplied to RePEc.
  url: https://doi.org/10.1016/j.jeconom.2013.08.039
  date: 2014
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: reported
  access_level: abstract
  locator: IDEAS publication header, suggested citation and publisher-supplied abstract at ideas.repec.org/a/eee/econom/v180y2014i1p1-15.html inspected2026-10-04. Confirms actual Chongqing pilot-price application; final methods not inspected after publisher open failed.
design_applications:
- paper: 'Property taxes and home prices: A tale of two cities'
  doi: 10.1016/j.jeconom.2013.08.039
  journal: Journal of Econometrics
  year: 2014
  research_question: How does Chongqing's selective personal-housing tax change aggregate home prices relative to a predicted no-pilot path?
  population: Published abstract describes31 Chinese provincial/municipal price series; inspected draft uses March1998-March2012 with155 pre-months and14 post-months. Tax boundary and price coverage must be reconciled.
  outcome: Aggregate log home prices and annual-growth sensitivity; housing-size indexes used descriptively in draft.
  data_used: [NDRC monthly provincial/municipal home prices as reported in draft, Post2011 NBS size-specific housing-price indexes]
  treatment_encoding: Draft aggregate forecast intervention starting February2011 after the January28 legal introduction; not a measured property-level tax bill.
  comparison: Draft Chongqing donors Jiangsu, Zhejiang, Beijing and Sichuan, selected for pre-fit; Shanghai excluded as a simultaneous pilot.
  empirical_design: Separate-city HCW-style counterfactual forecasting; draft-derived specifications explicitly distinguished from the published abstract and uninspected final methods.
  assumptions: [Stable donor relation, Aligned geography and measurement, Concurrent-policy separation, Limited donor spillovers]
  threats_addressed: [Draft withheld pre-period forecast and trend/growth checks; post-only size patterns explicitly not a causal spillover test]
  evidence_refs: [E2, E3]
method_transfer: null
readiness_blockers:
- Recover lawful historical price inputs and geographic coverage; reconcile final2014 methods before exact reproduction.
- Defend donor stability and separate contemporaneous local housing/credit changes or state a bundled-response estimand.
- A selective-tax mechanism requires original-version liability data and comparable segment counterfactuals; post-only price patterns are insufficient.
---

## Institutional Background

Chongqing's pilot sought to guide housing consumption and distribution;
tax proceeds fund public rental housing [E1]. Its original base differs
from Shanghai: detached commercial housing includes old stock, while
high-price and defined nonlocal ordinary-home rules target new purchases.
This difference changes exposure, exemptions and joins and warrants a
separate regime, not another record for each rate bracket.

## What Changed

Covered properties acquire recurring tax obligations under the initial
nine-district rules, distinguishing existing detached stock, new high-price
homes and specified nonlocal ordinary-home purchases [E1]. Connected
exempt-market responses do not make every home legally taxable.

## Implementation and Assignment

The pilot begins in nine main urban districts rather than the whole
municipality [E1]. A high-price eligibility threshold uses two times the
previous two years' district-area reference average; tax-rate thresholds
are three and four times. Existing detached stock receives a180-square-
meter allowance, new detached/high-price purchases100, and the defined
nonlocal ordinary category none. These original details correct the
draft's simplified high-end-only account [E1; E2].

## Why This Creates Empirical Variation

The published study uses the city pilot for a price counterfactual [E3].
Its inspected draft explains separate-city forecasting with selected
provincial/municipal donors [E2, reported]. Market exposure reaches exempt
homes through demand substitution, but the original paper's post-only
size-price patterns do not identify that spillover. A statutory price
threshold is not automatically an estimated RD or a valid new design.

## Identification Risks

An aggregate municipal price series need not match the nine-district
tax boundary. A price gap can combine changing transaction composition,
concurrent housing measures and selective liability [analytical inference].
Exact reproduction needs final-method reconciliation, the historical
NDRC series and a defensible donor relation. Future micro analysis needs
property/buyer histories, not current labels or later revised tax rules.

## Data Requirements

Recover historical price inputs and geographic/property coverage before
joining municipality-month reform timing. Property-level use additionally
needs dwelling IDs/types, reference-price ratios, purchase dates, family
deductions and buyer status; the legal rule supplies definitions, not
those microdata [E1; E2].

## Evidence Notes

The original official PDF was readable even though its HTML page timed
out [E1]. The research version inspected is September2012, while2014
publication metadata establishes the final study's existence and broad
application [E2; E3]. Neither unrestricted raw data nor final code
execution is claimed. The regime is grounded; research use remains
conditional on these specific data and identification conditions.
