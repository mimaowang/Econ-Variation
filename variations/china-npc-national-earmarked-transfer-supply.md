---
schema_version: 2
id: china-npc-national-earmarked-transfer-supply
name: China National Earmarked-Transfer Supply Interacted with Fixed Poor-County Status
aliases:
- Guo Liu Ma local fiscal multiplier
- National Poor County fiscal-supply instrument
- 全国专项转移支付与国定贫困县身份交互工具变量
status: grounded
provenance:
  task_id: task-aa94e1439282
scope:
  country: China
  regions: [Mainland counties; Tibet and municipal districts excluded in the application]
  domains: [development-economics, regional-economics, public-finance, local-government, investment]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    The inspected Chinese county application uses national earmarked-transfer
    supply interacted with fixed2001 National Poor County status to instrument
    annual changes in county government spending. Its core question concerns
    local output and investment, not agricultural productivity or an overseas
    method merely proposed for China.
identity:
  instrument: Fixed2001 poor-county designation interacted with the annual log of aggregate earmarked transfers received by county governments.
  authority: Central fiscal and poverty agencies set funding and designation frameworks; provinces allocate projects and relay funds to counties.
  legal_identifiers:
  - 财政扶贫资金管理办法(试行), 财农字[2000]18号,30 May2000
  - 中国农村扶贫开发纲要(2001—2010年), 国发〔2001〕23号,13 June2001
  - 国家扶贫开发工作重点县管理办法,2001-2010 framework reproduced in official2010 poverty yearbook; exact promulgation date not recovered
  implementation_regime: >
    A2001-2009 empirical fiscal-supply interaction within the preferential
    county-funding regime. The2000 fiscal-fund rules and2001 outline establish
    project allocation and provincial responsibility. Poverty funds are only
    part of the paper's wider statistical earmarked-transfer aggregate; no
    inspected document sets each NPC's fixed share of that aggregate.
  assignment_mechanism: >
    Fixed NPC status predicts greater spending sensitivity to national
    earmarked-transfer supply. Designation and local project allocation are
    discretionary and poverty-related, not randomized. The paper exploits
    differential responses to annual common supply, not random designation,
    a single announcement date or an income-threshold RD.
  parent: null
  related_variations: [china-8-7-poverty-county-threshold]
timeline:
  announcement: '2001-06-13 outline notice; not the date of a surprise fiscal shock'
  effective: '2000-05-30 fund-management rules effective on promulgation;2001-2010 outline framework'
  implementation_start: 2001
  implementation_end: null
  local_timing: >
    Annual estimation runs2001-2009, with NPC status fixed to the classification
    labeled2001 by the paper. This is an analytical vintage, not an independently
    verified county-specific payment date. The original roster and reclassification
    notices were not inspected.2009 ends the sample, not the institution;
    the2000 fund rules were replaced from1 January2012.
  anticipation: Annual budgets and project approvals can be anticipated. This instrument does not require an unanticipated2001 treatment event, but anticipated or targeted supply responses matter for its identifying assumption.
  last_verified: '2026-10-03'
assignment:
  unit: County-year with a time-invariant2001 designation and common annual national supply series.
  treated: Counties coded as NPCs in2001 have the higher predicted fiscal response; this label denotes exposure, not an observed treatment onset in every county.
  comparison_pool: Non-NPC counties in the same usable mainland panel; they also receive earmarked transfers and are not an unfunded control group.
  rule: >
    The2000 rules direct food-for-work and newly added fiscal poverty funds to
    designated poor counties, while development funds can also support others.
    Allocation considers poverty, county numbers, natural conditions,
    infrastructure, local finances, income and fund effectiveness. The2001
    outline mainly favors key counties while allowing other poor areas.
    The county-management text describes provincial selection subject to
    central review and project-based support; this is not a mechanical grant
    formula or proof of exogenous NPC status.
  intensity: NPC_i2001 multiplied by log(E_t), where E_t is the national aggregate of earmarked transfers received by county governments in year t.
  exemptions:
  - Tibet is excluded for missing data and municipal districts for unavailable GDP and different fiscal regimes; these are paper sample restrictions, not legal funding exemptions.
  - Some fiscal poverty funds and assistance reach non-NPC poor areas; NPC status does not monopolize every transfer programme.
  compliance: National budget allocations pass through provinces and project procedures; allocated funds, actual transfers received and county expenditure are separate quantities. Fiscal matching and project performance can alter pass-through.
  exposure_construction: >
    Join a historically reconciled2001 NPC indicator to stable county IDs.
    For each year construct the natural log LEVEL of the national county
    earmarked-transfer aggregate, then interact it with that indicator.
    Instrument (G_it-G_i,t-1)/Y_i,t-1; the main outcome is
    (Y_it-Y_i,t-1)/Y_i,t-1. These are real annual changes scaled by lagged GDP,
    not spending/GDP levels, transfer growth rates or county-specific actual
    grants used directly as the instrument. Reconcile the aggregate's
    jurisdiction coverage and deflation with the paper before replication.
  required_identifiers: [county_id, year, province_id]
  spillovers: Intercounty purchases and factor movements can spread or displace effects. The paper cannot directly identify spillovers; its net-import interpretation is inferred without county import/export data.
research_compatibility:
  outcome_domains: [county GDP growth, investment, service-sector output, manufacturing output, retail sales]
  affected_populations: [Mainland non-district counties with usable annual fiscal and economic statistics]
  mechanism_channels: [Preferential fiscal pass-through, Local public spending, Investment demand, Nontradable production]
  best_for:
  - Studying short-run county output or investment responses to grant-induced expenditure, conditional on differential-trend and exclusion assumptions.
  - Separating a national fiscal-supply exposure from the effect of becoming a designated poor county.
  not_good_for:
  - Calling poverty status random or replacing this interaction with the1994 designation threshold.
  - Claiming an aggregate national multiplier, long-run growth effect or identified spatial spillover from the paper's local annual estimate.
  - Treating retail sales as complete consumption or extending the county sample automatically to municipal districts or individual firms.
design:
  claim_type: causal
  affordances: [Fixed geographic exposure to common fiscal supply, Differential county expenditure response]
  candidate_designs: [County and year fixed-effects panel 2SLS]
  identifying_variation: >
    NPC counties' expenditure responds more strongly to national earmarked
    transfers. After county and year fixed effects, that differential response
    supplies the first stage. Causal interpretation requires national supply
    not to react to NPC-specific relative economic conditions and requires
    exposure to affect output through the measured expenditure channel.
  primary_strategy: >
    Two-stage least squares for annual real GDP change/lagged GDP using
    NPC_i2001 x log(E_t) as the excluded instrument for annual real spending
    change/lagged GDP. Include county and year fixed effects; the controlled
    specification adds population growth, urbanization and primary/secondary
    pupils as a share of population. Reported robust errors cluster by county.
  estimand: A short-run relative local output response to expenditure induced by differential earmarked-transfer supply, under the application assumptions; not the total effect of poor-county designation or a nationwide fiscal expansion.
  treatment_variable: Annual real county-government expenditure change divided by prior-year real county GDP; fixed NPC status and national supply form the instrument, not this endogenous regressor.
  comparison_logic: Compare differential annual spending/output movements of fixed NPC and non-NPC counties net of common years and county baselines; non-NPC expenditure can respond to national supply too.
  estimation_notes: >
    Published Eq1-2 define expenditure CHANGES, although table-note shorthand
    refers to expenditures divided by lagged GDP. Table3 reports1768 counties,
    15561 observations without extra controls and15024 with them; first-stage
    F214.7/216.2 and output coefficients0.589/0.570. These are reported
    estimates, not replicated results or exogeneity tests. There are only nine
    annual national supply observations in2001-2009; county clustering alone
    does not settle inference for a common national-shock interaction.
  assumptions:
  - National earmarked-transfer supply does not respond to NPC versus non-NPC relative latent output shocks.
  - Designation-specific trends, other policies and differential macroeconomic responses do not drive the instrument-outcome relationship after conditioning.
  - Preferential assistance affects the proposed outcome through measured county expenditure rather than unmeasured loans, in-kind assistance or other channels.
  - County boundaries, fiscal categories, national aggregate coverage and real GDP/expenditure measurements are comparable across years.
  diagnostics:
  - Examine designation-group relative output and expenditure trajectories, including sensitivity to flexible trends and crisis years; identify any changed estimand.
  - Separate instrument relevance from exclusion and assess common-shock inference with the short annual series.
  - Reconstruct historical roster, administrative changes and fiscal matching/project allocation before using NPC exposure.
threats:
- type: discretionary_designation_and_funding
  basis: documented
  condition: Official allocation uses poverty and local fiscal/project conditions, with provincial discretion. Legal preference establishes relevance, not random designation or a fixed earmarked-transfer share.
  evidence_refs: [E2, E3, E4]
  possible_diagnostics: [Historical designation reconciliation, Allocation and matching histories, Relative trajectory comparisons]
- type: bundled_assistance_exclusion
  basis: documented
  condition: The2001 outline also provides preferential loans, infrastructure coordination and paired assistance; the county-management regime favors broader departmental resources. These can affect output outside the measured expenditure series.
  evidence_refs: [E3, E4]
  possible_diagnostics: [Budget versus loan separation, Concurrent assistance exposure, Proposed outcome-specific channel assessment]
- type: differential_national_shocks_and_few_years
  basis: inferred
  condition: National supply varies for only nine estimation years and NPCs can respond differently to the financial crisis or concurrent fiscal reforms. Similar average growth and high first-stage F do not remove this possibility or validate county-only inference.
  evidence_refs: [E1]
  possible_diagnostics: [Year sensitivity, Relative trends, Alternative common-shock inference with explicit short-series limitations]
- type: measurement_and_spatial_interference
  basis: reported
  condition: The paper lacks direct county consumption and trade data, excludes districts, and reports inconsistent raw-data year labels. Spillovers cannot be directly identified with its strategy.
  evidence_refs: [E1]
  possible_diagnostics: [Raw-series coverage reconciliation, Stable county crosswalk, Retail versus consumption distinction, Explicit spatial estimand]
empirical_requirements:
  contract_version: 1
  population: Mainland non-district counties with historical2001 NPC coding and usable fiscal/economic series; Tibet excluded in the application.
  observation_unit: County-year
  geography_level: county
  time_start: 2000
  time_end: 2009
  minimum_frequency: annual
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields: [county_gdp, county_government_expenditure, national_county_earmarked_transfer_aggregate, npc_status_2001, provincial_price_deflator, population_growth, urbanization_rate, primary_secondary_pupil_share]
  required_identifiers: [county_id, year, province_id]
  treatment_key: [county_id, year, npc_status_2001]
  treatment_source: Historical2001 NPC classification and National Prefecture and County Finance Statistics Yearbooks; national series must match Eq2's county-received earmarked-transfer aggregate.
  measurement_risks:
  - Data Section3 says2000-2009 raw coverage, while Table1 says1998-2009; Tables2-5 estimate2001-2009. Use2000-2009 as the stated lag-input envelope but reconcile the discrepancy before numerical reproduction.
  - One earlier/later observation is the minimum for an annual change, not a sufficient two-period policy experiment; the application needs the multi-year national series and relative county trajectories.
  - Paper reports deflation to1997 prices with provincial deflators and trimming key variables outside0.5/99.5 percentiles; exact aggregate deflation, trimming implementation and historical roster coding were not inspected in code.
  - Stable historical county/province codes and boundary crosswalks are required; a current592-county list cannot substitute for the2001 vintage.
  - Yearbook access and cleaned microdata are not established by paper citation. No replication data or code was inspected.
  - Investment, sector output and retail-sales applications require their own outcome fields. Retail excludes most services and cannot measure total consumption; these optional outcomes are not mandatory for GDP-only matching.
evidence:
- id: E1
  source_type: paper
  citation: 'Guo, Qingwang; Chang Liu; Guangrong Ma.2016. How large is the local fiscal multiplier? Evidence from Chinese counties. Journal of Comparative Economics44(2),343-352.'
  url: https://www.dropbox.com/s/7vjfc41ht26fk9m/How%20large%20is%20the%20local%20fiscal%20multiplier.pdf?dl=1
  date: '2016-05'
  supports: [scope.china_relevance, identity.instrument, identity.assignment_mechanism, timeline.local_timing, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.intensity, assignment.exemptions, assignment.exposure_construction, assignment.spillovers, design.identifying_variation, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.population, empirical_requirements.time_start, empirical_requirements.time_end, empirical_requirements.required_fields, empirical_requirements.treatment_source, empirical_requirements.measurement_risks, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design]
  verification_status: reported
  access_level: full-text
  locator: >
    Published10-page PDF linked by author Chang Liu research page
    https://changliuchina.weebly.com/research.html, inspected in memory3 October2026
    via the same public Dropbox file's dl.dropboxusercontent.com URL.
    Printedpp343-346 motivation/institution/Eq1;347 Eq2 exact log-level
    instrument;348 Section3 data/footnotes12-13;349 Table3;350-351
    Tables4-5 and inference limits. Table1 raw-year caption conflicts with
    Section3; equations take precedence over spending-level table shorthand.
- id: E2
  source_type: policy-document
  citation: MOF and partner agencies, 财农字[2000]18号,30 May2000, 财政扶贫资金管理办法(试行).
  url: https://www.mof.gov.cn/gkml/caizhengwengao/caizhengbuwengao2000/caizhengbuwengao20004/200805/t20080519_21529.htm
  date: '2000-05-30'
  supports: [identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.effective, assignment.rule, assignment.compliance, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Official MOF reproduction inspected3 October2026; heading original date versus2008 web date; attachment1 Articles3,5-8 fund scope/matching/eligibility,12-14 allocation/relay,17-19 project management,28 immediate effect. These rules cover specified fiscal poverty funds, not the entire statistical earmarked-transfer aggregate.
- id: E3
  source_type: policy-document
  citation: State Council, 国发〔2001〕23号,13 June2001, 中国农村扶贫开发纲要(2001—2010年), reproduced by FAOLEX.
  url: https://faolex.fao.org/docs/pdf/chn155364.pdf
  date: '2001-06-13'
  supports: [identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.announcement, assignment.rule, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Inspected10-page government-text reproduction3 October2026; PDFp1 notice number/date, p3 paragraph11 focus areas, pp6-7 paragraphs21-26 yearly funds/preference/provincial relay/loans/concurrent assistance, p8 paragraph29 provincial responsibility. Not an original roster or individual disbursement record.
- id: E4
  source_type: implementation-document
  citation: China International Poverty Reduction Center official2010 yearbook, 国家扶贫开发工作重点县管理办法.
  url: https://yearbook.iprcc.org.cn/zggjfpzxnj/2010njzw/flezyzcwjhbfpgzwj/382560.shtml
  date: null
  supports: [identity.authority, identity.legal_identifiers, identity.assignment_mechanism, assignment.rule, assignment.compliance, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Full HTML inspected3 October2026; Article1 criteria/provincial nomination/central review/adjustment;3 preferential projects and other poor villages;4 project database;7 performance rewards/penalties. Heading situates the2001-2010 framework but does not supply an exact promulgation date;2010 is yearbook vintage, not policy onset.
- id: E5
  source_type: policy-document
  citation: MOF, 财农[2011]412号,7 November2011, 财政专项扶贫资金管理办法.
  url: https://www.mof.gov.cn/gkml/caizhengwengao/2012wg/wg201201/201203/t20120331_640066.htm
  date: '2011-11-07'
  supports: [timeline.local_timing]
  verification_status: verified
  access_level: official-document
  locator: Official MOF reproduction inspected3 October2026, heading original date versus2012 web date and Article30 effect1 January2012 and repeal of财农字[2000]18号. Later allocation rules are not backdated into the2001-2009 application.
- id: E6
  source_type: other
  citation: Publisher-deposited Crossref metadata for Guo Liu Ma, JCE44(2),May2016,343-352.
  url: https://doi.org/10.1016/j.jce.2015.06.002
  date: '2016-05'
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: Direct https://api.crossref.org/works/10.1016/j.jce.2015.06.002 inspected3 October2026; three authors/title/journal/volume/issue/month/pages agree with published PDF front matter.2015 DOI acceptance metadata is not the2016 issue year.
design_applications:
- paper: 'How large is the local fiscal multiplier? Evidence from Chinese counties'
  doi: 10.1016/j.jce.2015.06.002
  journal: Journal of Comparative Economics
  year: 2016
  research_question: How much annual local output and investment respond to grant-induced county public spending.
  population: Annual2001-2009 mainland non-district county panel,1768 counties in Table3; Tibet excluded.
  outcome: Annual real GDP change divided by prior-year GDP; investment and sector-output changes use the same GDP normalization, and retail sales provide an incomplete consumption proxy.
  data_used: [National Prefecture and County Finance Statistics Yearbooks, Provincial Statistical Yearbooks, Provincial deflators from China Statistical Yearbook, Fixed2001 NPC designation reported by the paper]
  treatment_encoding: Instrument annual real expenditure change/lagged GDP with fixed2001 NPC dummy times log annual aggregate earmarked transfers received by county governments.
  comparison: Differential annual responses of fixed NPC and non-NPC counties after county/year effects; both groups can receive grants.
  empirical_design: Panel2SLS with county/year effects, optional demographic/urbanization/pupil controls and county-clustered robust errors; not designation RD or a one-date DID.
  assumptions: [National supply not responding to NPC relative output shocks, No unmeasured designation-specific channels correlated with supply, Comparable county fiscal/output measurement]
  threats_addressed: [County and year fixed effects, Time-varying observed controls, Strong reported first stage, Reported group average-growth comparison, Separate sector and expenditure-component outcomes]
  evidence_refs: [E1, E2, E3, E4, E5, E6]
method_transfer: null
readiness_blockers:
- Recover and reconcile the historical2001 NPC roster, original reclassification notices, county crosswalks and exact national earmarked-transfer series before reproduction.
- Establish lawful yearbook/data access and reconcile raw-year labels, real aggregate construction and trimming; no public replication package was inspected.
- Assess designation-specific trajectories, national-supply targeting, bundled assistance and inference with nine annual common supply observations for the proposed outcome.
---

## Institutional Background

China's counties finance spending with own revenues and transfers from higher
levels. Guo, Liu and Ma distinguish general grants from earmarked grants and
report that designated poor counties receive a larger marginal share of the
latter when national supply expands [E1, reported claim]. The relevant change
is annual fiscal supply acting on an existing geographic funding preference,
not a new poor-county label assigned at random.

The2000 fiscal poverty-fund rules establish project-based allocation and
provincial relay. They differentiate fund categories: some are confined to
designated counties, while development funds can support other areas [E2,
verified]. The2001 outline continues preferential support but also authorizes
broader assistance [E3, verified]. Neither text makes the statutory poverty-fund
budget identical to all earmarked transfers in the paper's finance statistics.

## What Changed and How Exposure Is Measured

The paper holds NPC status fixed to its2001 classification and interacts it
with the natural log of national earmarked transfers received by county
governments in each year [E1, reported claim]. A researcher needs that common
series and the historical designation, not just actual grants in each county.
The2001 outline date anchors the policy environment; it does not establish
an unanticipated June treatment or each county's first payment.

## Implementation and Assignment

NPC and non-NPC counties face different funding sensitivities, not universal
cash receipt versus zero support. Provincial selection, project management
and performance conditions govern actual allocation [E2-E4, verified].

This case differs from the related8-7 poverty-threshold record. That record
centers on1994 designation around1992 income cutoffs; this one centers on
annual fiscal-supply exposure in2001-2009. Substituting the old cutoff would
change both assignment and estimand. The2002 income-tax-sharing candidates
also remain separate: their reform-specific exposure is not this instrument.

## Why This Creates Empirical Variation

Eq1-2 relate real annual GDP change to real annual expenditure change, both
scaled by prior-year GDP. County and year fixed effects remove stable county
levels and common annual movements; the controlled specification adds
population growth, urbanization and pupil share [E1, reported claim]. It does
not compare funded NPCs against wholly unfunded counties, and it does not
estimate the causal effect of receiving designation.

The short-run output coefficient is0.570 in the controlled Table3
specification. Table5 reports an investment response of1.190 and an
insignificant retail-sales response of0.0263 [E1, reported claim]. These are
the authors' estimates, not independent replication. Retail omits most
services; inferred net imports and possible spillovers are not observed trade
effects. The paper expressly leaves long-run growth and direct spillover
identification outside its design.

## Identification Risks

The institutional documents explain a first stage, not exclusion. Poor-county
status also brings loans, coordinated infrastructure and other assistance,
and officials select counties and projects using economic circumstances
[E2-E4, verified]. Those channels can influence growth outside the measured
county budget. Similar average growth of NPCs and non-NPCs, cited by the
authors, does not establish comparable yearly counterfactual trajectories
[analytical inference].

Only nine annual supply observations underlie the national interaction.
Thousands of county observations do not create thousands of independent
national shocks. Common-shock inference and sensitivity to differential crisis
responses need attention in a new application [analytical inference]. This
record is grounded for conditional research matching, not a causal guarantee
or a ready-to-run replication deposit.

## Data Requirements

County finance yearbooks supply fiscal series; provincial statistical
yearbooks supply GDP and economic outcomes. County, province and year IDs
connect these to designation and price deflators. Section3 states2000-2009
raw coverage and1997 prices; Table1 instead labels1998-2009, whereas
estimation tables consistently use2001-2009 [E1, reported claim]. Preserve
that discrepancy for source reconciliation rather than silently expanding
the data contract. Exact roster and cleaning code remain unavailable here.

## Evidence Notes

The companion data repository can document access and reconstruction using
the DOI as the connection. This record stores the research-decision logic,
not a copied paper, microdata or a claim that all listed yearbooks are already
downloaded. The published methods and official fund texts support admission;
unresolved reproduction and identification conditions stay explicit.
