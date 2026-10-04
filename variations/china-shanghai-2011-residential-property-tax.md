---
schema_version: 2
id: china-shanghai-2011-residential-property-tax
name: Shanghai2011 New-Purchase Residential Property-Tax Regime
aliases: [Shanghai property-tax pilot, 上海个人住房房产税试点, 沪府发〔2011〕3号]
status: grounded
provenance:
  task_id: task-ba3daf6a8947
scope:
  country: China
  regions: [Shanghai, mainland China]
  domains: [urban, housing, public-finance, regional-economics]
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: Shanghai introduces recurring tax liability for specified newly purchased personal homes; an inspected working version of a published econometrics study uses the city's2011 pilot to construct counterfactual home prices.
identity:
  instrument: Shanghai's initial tax on specified personal homes newly purchased from January28,2011, conditioned on family residency, local housing ownership and exemptions. Not a universal tax on the existing housing stock or a purchase prohibition.
  authority: Shanghai Municipal People's Government; local tax authorities with municipal housing and related departments, under the State Council's136th executive-meeting authorization.
  legal_identifiers: [沪府发〔2011〕3号, 上海市开展对部分个人住房征收房产税试点的暂行办法]
  implementation_regime: Initial2011 rules during the study's short2011-2012 window. Later residency/exemption adjustments are outside this version. Chongqing's simultaneous pilot has a different property-type and price-based assignment and is a separate regime.
  assignment_mechanism: City-level introduction at a known date, with household-property statutory liability determined by new purchase, residency, owned housing and exemptions. The inspected price application estimates aggregate Shanghai exposure, not a micro eligibility RD or every household's realized tax.
  parent: null
  related_variations: [china-chongqing-2011-residential-property-tax, china-housing-purchase-limits-rent-tax-substitution]
timeline:
  announcement: '2011-01-27'
  effective: '2011-01-28'
  implementation_start: '2011-01-28'
  implementation_end: null
  local_timing: Purchase timing is online contract registration; tax liability is calculated from the month after acquisition of ownership. The inspected draft fits prices through January2011 and predicts February2011-March2012. January is an end-of-month transition, not a fully untreated month by law.
  anticipation: Pilot debate and related housing restrictions precede implementation; the one-day announcement-to-effective interval does not establish an unexpected policy.
  last_verified: '2026-10-04'
assignment:
  unit: Household-property for statutory liability; Shanghai municipality-month for the inspected price application.
  treated: Local-resident families' newly purchased second-or-later Shanghai homes and nonlocal-resident families' new Shanghai purchases, subject to the initial statutory exemptions. Aggregate city treatment includes equilibrium responses of exempt homes.
  comparison_pool: In the inspected2012 draft, Jiangsu, Zhejiang, Heilongjiang and Sichuan price series predict Shanghai. These are provincial comparators with different aggregation, not matched untaxed Shanghai households; Chongqing is not an untreated donor.
  rule: Initial coverage follows family residency and local property holdings, with new purchase defined by online contract filing from January28. The family's ownership count includes spouses and minor children; exemptions can remove or reduce actual liability.
  intensity: Taxable transaction value uses a70% base, nominal annual rate0.6%, reduced to0.4% when price per square meter is no greater than twice the previous year's municipal new-commercial-home average. These statutory rates/thresholds are not an RD used in the inspected paper.
  exemptions:
  - For local-resident families buying a second-plus home, combined Shanghai housing area up to60 square meters per person is exempt; tax applies to the new purchase's excess area, not automatically its entire area.
  - Selling the family's original sole home within one year of buying a replacement permits refund; qualifying adult-child marriage/sole-home purchases can be exempt.
  - Qualifying introduced talent and eligible residence-permit holders have sole-home exemptions; a holder below three years can later qualify for refund under the original conditions.
  compliance: Property registration requires the tax authority's liability determination based on family/housing information; assessment is not proof of payment. Liability begins next month, is annual and prorated for partial years. Actual property-level collection needs administrative evidence beyond a city-post flag.
  exposure_construction: >
    For the documented aggregate application, link Shanghai's historical
    administrative unit to monthly prices, flag the January28 reform and
    retain January as a transition. Fit the pre-period log price on the
    draft's provincial donor prices, intercept, post-November2008 dummy
    and optional trend; use donor outcomes to predict post-period prices.
    This is OLS counterfactual forecasting, not equal-weight DID or
    convex-weight synthetic control. Micro statutory exposure instead
    needs contemporaneous family residency, owned-home counts and total
    area, purchase/ownership dates, exemption history, transaction value
    and annual municipal threshold. Do not replace those inputs with
    current address, home size alone or the city's pilot label.
  required_identifiers: [historical_administrative_unit_id, calendar_month]
  spillovers: Exempt properties can respond to reallocated demand, and investors can substitute across cities; aggregate exposure does not mean every property pays tax. Donor regions may receive displaced investment.
research_compatibility:
  outcome_domains: [Housing prices, Housing demand, Wealth, Local public finance]
  affected_populations: [Shanghai home buyers and owners, including equilibrium-exposed exempt households]
  mechanism_channels: [Recurring ownership cost, Housing-demand substitution, Capitalization, Tax-financed housing provision]
  best_for: [Aggregate short-run housing-market responses with comparable historical price series and an explicit contemporaneous-policy counterfactual.]
  not_good_for:
  - A tax-only causal effect identified solely by Shanghai-by-post while purchase and credit rules change at the same time.
  - Coding all Shanghai households as tax-paying or using60 square meters of a single home as the full exemption rule.
  - Treating the rate threshold as a paper-used RD or tax collection as observed from city status.
design:
  claim_type: reduced-form
  affordances: [Known initial legal date, Recoverable household eligibility, Long monthly pre-period in inspected application]
  candidate_designs: [Single-city counterfactual forecasting with defended donor stability, Household-property liability analysis with additional data and selection assumptions]
  identifying_variation: Shanghai's aggregate post-pilot price divergence from a pre-fitted provincial comparison relation; causal tax attribution additionally requires separation of simultaneous local housing regulation and stable donors.
  primary_strategy: The inspected September2012 working version uses equation16 OLS on log prices and donor series with an intercept, post-November2008 dummy and optional trend, fitted March1998-January2011; post outcomes are compared with forecasts. Published metadata confirms the two-city counterfactual approach, not every draft specification.
  estimand: Aggregate Shanghai price gap against a model-predicted no-pilot path over the short post-period, not tax incidence on a legally liable home.
  treatment_variable: Shanghai reform timing, with the draft's forecast evaluation starting February2011; no household tax-rate or area-threshold coefficient is estimated in this inspected application.
  comparison_logic: Pre-period price comovement with selected provincial donors supplies a forecast relation. OLS weights may be negative and need not sum to one; donors must remain informative and unexposed to confounding local changes or spillovers.
  estimation_notes: Draft reports155 pre-months and14 post-months through March2012, donor selection by fit, withheld pre-period forecasting and annual-growth sensitivity. These are draft-specific, not a verified final2014 sample or executable replication. Good pre-fit alone does not establish causal attribution.
  assumptions:
  - The pre-period donor-price relation remains stable absent the reform, including common-factor loading and relevant time-series restrictions.
  - Local purchase/credit/tax/land changes do not create an unseparated Shanghai-specific post break.
  - Price-series geography, construction and transaction composition are comparable over time.
  - Donors are not materially affected by displaced investment or differently timed housing interventions.
  diagnostics: [Withheld pre-period forecasting and placebo dates, Donor and trend sensitivity with transparent selection, Concurrent-policy comparison, Consistent price-vintage and composition analysis]
threats:
- type: contemporaneous_housing_policy_bundle
  basis: documented
  condition: The municipal February1,2011 announcement describes purchase restrictions, second-home credit tightening, other taxes and land/housing measures alongside the pilot. A common macro factor or2008 dummy does not automatically remove this city-specific bundle.
  evidence_refs: [E4]
  possible_diagnostics: [Recover comparator policy timing, State bundled versus tax-only estimand, Seek defensible liability heterogeneity rather than assume tax isolation]
- type: selective_liability_and_equilibrium_prices
  basis: documented
  condition: Original exemptions depend on combined household housing and residency, not only home size. The aggregate price outcome includes exempt homes and transaction-composition changes, so its gap is not a per-taxpayer treatment effect.
  evidence_refs: [E1, E2]
  possible_diagnostics: [Separate statutory liability from market exposure, Link historical family/property data, Examine comparable property-type prices]
- type: forecast_stability_and_version_boundary
  basis: reported
  condition: Draft donor selection and time-series assumptions govern forecasting;14 post-months restrict inference. Final typeset methods, historical price micro-inputs and executable replication were not inspected.
  evidence_refs: [E2, E3]
  possible_diagnostics: [Recover final version before exact reproduction, Out-of-sample pre-fit, Donor/placebo and dependence-sensitive inference]
empirical_requirements:
  contract_version: 1
  population: Shanghai aggregate housing market and documented provincial donor series, with historical geographic coverage verified before analysis.
  observation_unit: administrative-unit-month
  geography_level: municipality and province; not automatically comparable urban-core samples
  time_start: '1998-03'
  time_end: '2012-03'
  minimum_frequency: monthly
  minimum_pre_periods: 155
  minimum_post_periods: 14
  required_fields: [Historical comparable monthly home prices for Shanghai and selected donors, Price definition and reporting coverage/vintage, Reform and concurrent housing-policy dates, Explicit donor-selection and trend specifications]
  required_identifiers: [historical_administrative_unit_id, calendar_month]
  treatment_key: [historical_administrative_unit_id, calendar_month]
  treatment_source: Original Shanghai2011 notice establishes city/date and household coverage; the inspected working version documents the aggregate counterfactual construction, not a realized tax-payment dataset.
  measurement_risks:
  - The draft attributes monthly provincial/municipal prices to NDRC and acknowledges Tsinghua China Data Center provision. Exact historical series, coverage and lawful reconstruction/access were not independently recovered.
  - The draft warns of a January2011 NBS series break; do not splice NBS indexes into the longer NDRC price panel without independent comparability evidence.
  - Municipality/province averages are not transaction-level prices; targeted liability and housing composition cannot be inferred from their unit IDs.
evidence:
- id: E1
  source_type: policy-document
  citation: Shanghai Municipal Government, 沪府发〔2011〕3号, initial personal-housing property-tax pilot rules.
  url: https://shanghai.chinatax.gov.cn/zcfw/zcfgk/dcs/201101/t305661.html
  date: '2011-01-27'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.announcement, timeline.effective, timeline.implementation_start, timeline.local_timing, assignment.unit, assignment.treated, assignment.rule, assignment.intensity, assignment.exemptions, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: Header, notice and PartsI-IX,XI inspected in full2026-10-04. Initial rule, not a certification that later exemptions or every household's collection remained unchanged.
- id: E2
  source_type: paper
  citation: Bai, ChongEn, Qi Li and Min Ouyang, September2012 working version of Property Taxes and Home Prices, institution-hosted manuscript; publication is the citation target.
  url: https://www.ckgsb.edu.cn/Userfiles/doc/9.24%20Property%20Taxes%20and%20Home%20Prices%20A%20Tale%20of%20Two%20Cities.pdf
  date: 2012
  supports: [assignment.comparison_pool, assignment.exposure_construction, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.required_fields, empirical_requirements.measurement_risks, design_applications.population, design_applications.outcome, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design]
  verification_status: reported
  access_level: full-text
  locator: Title/version and Sections2-5, especially printedpp10-16 equation16 and donor/sample discussion inspected2026-10-04. Version explicitly distinguishes draft from final; draft citation/circulation notice retained and PDF not redistributed. No final-method equivalence, data access or code execution claimed.
- id: E3
  source_type: paper
  citation: Bai, Li and Ouyang2014, Journal of Econometrics180(1),1-15, publication metadata and abstract supplied to RePEc.
  url: https://doi.org/10.1016/j.jeconom.2013.08.039
  date: 2014
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: reported
  access_level: abstract
  locator: IDEAS publication header, suggested citation and publisher-supplied abstract at ideas.repec.org/a/eee/econom/v180y2014i1p1-15.html inspected2026-10-04; confirms China pilot counterfactual application. Publisher direct open failed; final full-text specifications not inspected.
- id: E4
  source_type: implementation-document
  citation: Shanghai Municipal Government, implementation of 国办发〔2011〕1号 and 沪府办发〔2011〕6号.
  url: https://www.shanghai.gov.cn/nw9822/20200906/0001-9822_479593.html
  date: '2011-02-01'
  supports: [timeline.local_timing, research_compatibility.not_good_for, empirical_requirements.required_fields]
  verification_status: verified
  access_level: official-document
  locator: Dated heading and measures1-5 inspected2026-10-04; purchase eligibility, second-home credit, taxes, land supply and housing program overlap. Migrated URL date is not the2011 announcement date.
design_applications:
- paper: 'Property taxes and home prices: A tale of two cities'
  doi: 10.1016/j.jeconom.2013.08.039
  journal: Journal of Econometrics
  year: 2014
  research_question: How does the initial Shanghai pilot change aggregate home prices relative to a forecast no-pilot path?
  population: Published abstract describes31 Chinese provincial/municipal price series; inspected2012 draft uses March1998-March2012, with155 pre-months and14 post-months. Final sample details remain version-conditioned.
  outcome: Aggregate home price in log levels and annual-growth sensitivity in the inspected draft.
  data_used: [NDRC monthly provincial/municipal home prices as reported in draft, Post2011 NBS housing-size indexes for descriptive discussion]
  treatment_encoding: City intervention with draft post-forecast window February2011-March2012; not individual statutory liability.
  comparison: Draft Shanghai donors Jiangsu, Zhejiang, Heilongjiang and Sichuan, selected for pre-fit; negative OLS weights permitted.
  empirical_design: Separate-city HCW-style counterfactual forecasting; detailed specification comes from the inspected working version, not an independently inspected final-method section.
  assumptions: [Stable donor relation, No unseparated local-policy break, Comparable price measurement, Limited donor spillovers]
  threats_addressed: [Draft withheld pre-period forecast check, Trend and growth sensitivity; these do not certify tax-only attribution]
  evidence_refs: [E2, E3]
method_transfer: null
readiness_blockers:
- Recover lawful historical NDRC series and its geography/measurement vintage, and reconcile final2014 methods before exact reproduction.
- Separate contemporaneous purchase/credit and other housing measures, or explicitly estimate the bundled local response rather than call it a tax-only causal effect.
- Verify donor stability, displacement and transaction composition; individual liability requires family-property records beyond this aggregate contract.
---

## Institutional Background

The2011 pilot adds recurring liability to selected new personal-home
purchases, not all housing and not all property taxation in China [E1].
Its stated purposes include distribution, housing consumption and resource
allocation. Revenue funds housing-related expenditure. Those objectives
explain a selective base, but do not establish random selection of Shanghai.

## What Changed

The reform adds recurring ownership cost to covered new purchases while
retaining household exemptions [E1]. Purchase restrictions are a separate
instrument in the concurrent housing-policy environment [E4].

## Implementation and Assignment

A local family's second purchase can still be exempt when combined
housing area remains within the family allowance. Nonlocal families face
different residency/talent exemptions [E1]. The legal timing also has
three stages: January27 announcement, January28 qualifying purchases,
and liability from the month after ownership acquisition. An annual city
flag cannot identify a household's actual payment.

## Why This Creates Empirical Variation

Bai, Li and Ouyang's published abstract establishes a China pilot-price
application [E3]. The inspected working version shows how an aggregate
counterfactual is constructed from donor comovement [E2, reported]. That
answers a market-level question, not a statutory cutoff question. The
same-day Chongqing pilot is separate because its original property-type,
price and stock/new-purchase rules produce different liability. A new
Shanghai outcome under this same initial assignment belongs in this case.

## Identification Risks

Shanghai also announced a local housing-control package at the beginning
of February [E4]. A post price gap can reflect that bundle. Donor pre-fit
helps forecasting but cannot isolate a tax that shares its timing with
purchase restrictions and credit changes [analytical inference]. Exact
reproduction remains conditional on final-version reconciliation and
historical price access. Do not silently replace the long NDRC series
with a differently constructed NBS index or treat good fit as exogeneity.

## Data Requirements

The aggregate contract needs historically comparable monthly Shanghai
and donor prices, unit identifiers, coverage/vintage and policy dates.
Household-tax use needs linked family and property histories instead;
aggregate city prices do not reveal individual payment [E1; E2].

## Evidence Notes

Original tax rules govern assignment where the draft simplifies family
area or the price-ratio boundary [E1; E2]. Research specifications are
labelled as draft-derived, and no copyrighted PDF is stored here.
Conditional readiness concerns a documented research opportunity with
explicit data and counterfactual conditions, not a completed replication.
