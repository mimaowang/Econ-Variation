---
schema_version: 2
id: china-1994-public-housing-tenant-purchase-opportunity
name: China 1994 Public-Housing Tenant Purchase Opportunity
aliases: [1994公房出售改革, 单位住房产权改革, Public housing privatization and entrepreneurship]
status: grounded
provenance:
  task_id: task-02bf4b23efa8
scope:
  country: China
  regions: [Mainland China]
  domains: [urban-economics, development-economics, labor-economics, household-finance, entrepreneurship]
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: Urban mainland public-housing tenants face a purchase opportunity under national reform with local implementation; baseline residence supplies an actual research exposure proxy.
identity:
  instrument: Tenant purchase opportunity under the 1994 national public-housing sale framework
  authority: State Council and implementing provincial and city/county governments
  legal_identifiers: [国发〔1994〕43号, 国务院关于深化城镇住房制度改革的决定]
  implementation_regime: National framework permitting voluntary public-housing sales under locally approved prices and plans. This is not the 1998 termination of welfare housing allocation, an earlier city experiment, or a later title top-up.
  assignment_mechanism: Existing public-housing residence creates differential purchase exposure, subject to sale suitability and local implementation. The research proxy combines prereform residence and couple-level state employment, rather than observed purchase or a city adoption instrument.
  parent: null
  related_variations: []
timeline:
  announcement: '1994-07-18'
  effective: '1994-07-18'
  implementation_start: 1994
  implementation_end: null
  local_timing: National decision effective on publication. Local approval governs implementation; the paper reports sample areas implemented by 1997. The survey gap prevents identifying regional adoption dates.
  anticipation: Earlier reform experiments and the decision's harmonization of sales since January 1994 preclude assuming no anticipation.
  last_verified: '2026-10-07'
assignment:
  unit: Prereform resident couple, inherited by each eligible individual's survey observations
  treated: Public-housing heads and spouses with at least one state-employed partner at baseline; a proxy for purchase opportunity, not verified receipt
  comparison_pool: Separately other state-employed couples outside public housing and nonstate private homeowners, fixed at baseline
  rule: National articles14–22 permit voluntary sales, locally set prices and differentiated title rights. The empirical application below uses residence and employment instead of verifying an individual offer.
  intensity: Binary baseline exposure interacted with post-reform survey waves; no measured universal subsidy amount
  exemptions: [Housing deemed unsuitable for sale by city/county government, Household area limits and one-time below-market purchase entitlement, Military housing subject to separate approval]
  compliance: Purchase is voluntary. Cost-price and standard-price titles have different disposition rights; neither the law nor residence alone proves purchase, resale freedom or entrepreneurial collateral access.
  exposure_construction: Link baseline housing, employment and spouses within household; retain baseline wave and carry classification through the individual panel. Join outcomes by longitudinal person ID and wave, preserving changing household membership and survey retention.
  required_identifiers: [Longitudinal person ID, Household ID, Couple relationship, Survey wave, Community ID]
  spillovers: Housing-market adjustment and employment changes can affect comparison residents; their lack of a direct tenant offer does not imply no equilibrium exposure.
research_compatibility:
  outcome_domains: [Entrepreneurship, Labor mobility, Household productive capital]
  affected_populations: [Urban public-housing tenants, State-employed couples, Urban working-age household heads and spouses]
  mechanism_channels: [Separation of housing from employment, Access to housing value, Changed rent and purchase costs]
  best_for: [Urban individual panels with prereform housing and couple employment]
  not_good_for: [Coding all state workers as treated, Treating voluntary purchasers as randomly assigned, Assuming unrestricted mortgage rights, Substituting a 1998 policy clock]
design:
  claim_type: causal
  affordances: [Predetermined residence contrast, Common national reform clock, Two distinct comparison populations]
  candidate_designs: [Baseline-exposure panel difference-in-differences, Wave-interaction diagnostic]
  identifying_variation: Differential outcome changes across baseline housing-employment groups around the reform
  primary_strategy: Fixed-effects logit DID in the inspected application
  estimand: Conditional log-odds contrast for exposure to the purchase opportunity, not an average probability effect or treatment-on-purchasers estimate
  treatment_variable: State_Resident89 multiplied by Post
  comparison_logic: Compare each baseline group over time and estimate the tenant contrast separately against each control population.
  estimation_notes: Age quadratic; individual effects; household clustering. Conditional logit omits outcome-invariant individuals, so report the estimating sample. Probability effects require additional assumptions.
  assumptions: [Comparable untreated outcome evolution on the specified model scale, No differential concurrent shock that explains the exposure contrast, Defensible handling of survey retention and baseline missingness]
  diagnostics: [Prereform group trajectories, Separate control estimates, Baseline-wave sensitivity, Attrition by group and wave, Stable occupation-question coding, Concurrent state-sector reform exposure]
threats:
- type: nonrandom-baseline-housing
  basis: reported
  condition: Public housing and state employment reflect earlier allocation and household selection. Individual effects do not absorb changing returns to education or connections.
  evidence_refs: [E2]
  possible_diagnostics: [Group-specific pretrends, Covariate-time interactions, Alternative state-sector control]
- type: selective-attrition
  basis: reported
  condition: Differential mobility can remove treated people from the survey. The paper's IPW correction assumes selection on observed variables and does not resolve unobserved selection.
  evidence_refs: [E2]
  possible_diagnostics: [Retention panel, Observable-selection weights, Sensitivity to unobserved selection]
- type: offer-proxy-and-local-title
  basis: documented
  condition: Residence does not establish an actual offer; national rules permit non-sale exceptions and distinguish partial title from cost-price ownership with market-entry limits.
  evidence_refs: [E1, E2]
  possible_diagnostics: [Purchase and title validation where available, Local sale-rule reconstruction, Separate eligibility from take-up]
- type: concurrent-state-restructuring
  basis: reported
  condition: Layoff expectations and other state-sector reforms may change entrepreneurship differently across tenant and nontenant households; unemployment is not a complete layoff history.
  evidence_refs: [E2]
  possible_diagnostics: [Predetermined employer restructuring exposure, Employment transitions, Alternative windows]
empirical_requirements:
  contract_version: 1
  population: Urban working-age household heads and spouses with prereform residence and employment history
  observation_unit: Individual-wave
  geography_level: Urban survey community
  time_start: 1989
  time_end: 2004
  minimum_frequency: irregular-panel
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields: [Housing ownership or tenancy, Employment sector, Head-spouse relationship, Primary occupation, Age, Student status, Retirement status, Urban registration composition, Survey wave, Baseline wave, Retention indicator]
  required_identifiers: [Longitudinal person ID, Household ID, Community ID, Survey wave]
  treatment_key: [Longitudinal person ID, Survey wave]
  treatment_source: Prereform household and employment survey linked to the national1994 decision; local rules required for verified offer or title measures
  measurement_risks: [Baseline missingness, Spouse matching, Household changes, Restricted or changed identifiers, Nonrandom attrition, Offer versus purchase, No intervening annual observations, Related housing-price application requires a separately estimated province-level mismatch measure rather than this default tenant-employment treatment]
design_profiles: []
evidence:
- id: E1
  source_type: policy-document
  citation: State Council national1994 decision reproduced in an official Beijing government notice
  url: https://www.beijing.gov.cn/zhengce/zfwj/zfwj/szfwj/201905/t20190523_71836.html
  date: '1994-07-18'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, assignment.rule, assignment.exemptions, assignment.compliance, timeline.announcement, timeline.effective, timeline.anticipation, timeline.local_timing, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: National attachment 国发〔1994〕43号, articles14–22,27,31,36–37 and July18 signature. The preceding Beijing notice is dated December23; that is not the national reform date.
- id: E2
  source_type: paper
  citation: Shing-Yi Wang, published REStat94(2),532–551
  url: https://nyudri.wordpress.com/wp-content/uploads/2012/04/creditconstraintsjobmobilityandentrepreneurship.pdf
  date: '2012-05-01'
  supports: [assignment.treated, assignment.comparison_pool, assignment.exposure_construction, design.primary_strategy, design.estimation_notes, design_applications.treatment_encoding, design_applications.empirical_design, design_applications.data_used, empirical_requirements.time_start, empirical_requirements.time_end, threats.condition]
  verification_status: reported
  access_level: full-text
  locator: IIpp534–535; IVApp538–539; IVBpp538–539 and notes15–17; VApp540–541 equation8,table2; VB–Cpp541–543,table4 and attrition/IPW discussion. Published20-page body inspected; no independent replication.
- id: E3
  source_type: other
  citation: Crossref publisher-deposited publication metadata
  url: https://doi.org/10.1162/rest_a_00160
  date: '2012-05-01'
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: Crossref works endpoint title, container-title, volume94, issue2, pages532–551 and publication date2012May; published PDF first-page imprint agrees.
- id: E4
  source_type: paper
  citation: Shing-Yi Wang, State Misallocation and Housing Prices, September2010 author manuscript hosted by AEA
  url: https://www.aeaweb.org/conference/2011/retrieve.php?pdfid=142
  date: '2010-09-01'
  supports: [assignment.spillovers, empirical_requirements.measurement_risks]
  verification_status: reported
  access_level: full-text
  locator: 37-page manuscript, Section3.1 pp13-14, Section3.2 equation12 pp16-19, Section3.3.3 equation17 and Table6 pp26-29. Table6 p28 rendered and visually inspected; final AER2011 text and deposited code not inspected. September is the cover month, not a verified day.
design_applications:
- paper: 'Credit Constraints, Job Mobility, and Entrepreneurship: Evidence from a Property Reform in China'
  doi: 10.1162/rest_a_00160
  journal: Review of Economics and Statistics
  year: 2012
  research_question: Does housing privatization change entrepreneurship?
  population: Urban heads/spouses aged18–60, excluding students and retirees
  outcome: Primary-job self-employment
  data_used: [CHNS1989/1991/1993/1997/2000/2004]
  treatment_encoding: Couple public residence plus state employment in1989; earliest available1991/1993 substitutes. Post comprises1997/2000/2004.
  comparison: Baseline other state employees and nonstate private homeowners, separately
  empirical_design: Individual-FE logit DID, age quadratic, household clustering; wave interactions and observable-selection IPW checks
  assumptions: [Parallel untreated evolution, Ignorable attrition conditional on weighting variables]
  threats_addressed: [Pretrends, Observable group differences, Attrition, Serial correlation, Concurrent reforms]
  evidence_refs: [E2, E3]
method_transfer: null
readiness_blockers:
- Conditional reuse requires lawful CHNS access and harmonized longitudinal and spouse keys; no raw microdata or executable reconstruction was inspected.
- Actual offers and entrepreneurial borrowing are unobserved in the inspected application. Additional title and local sale records are needed for those narrower mechanisms, not silently imputed from residence.
---

## Institutional Background

The national decision seeks to replace unit-provided housing with shared financing and a housing market. Sales are one component alongside rents and housing funds [E1]. This record isolates tenant purchase exposure, not every reform component.

## What Changed

Eligible public housing can be sold voluntarily, with locally approved prices and household limits [E1]. National authorization is not a verified offer to every resident. Earlier experiments and later allocation reform remain outside this case.

## Implementation and Assignment

Cost-price purchase conveys ownership but normally delays market entry for five years. Standard-price purchase conveys partial rights and shared proceeds; certificates must state the title fraction [E1]. A subsidized purchase cannot be described as immediately unrestricted collateral. Local sale and title records would resolve that stronger claim.

## Why This Creates Empirical Variation

The inspected application is encoded above [E2, reported claim]. [Analytical inference] Baseline tenancy links a national change to individual exposure without making earlier housing allocation random. Keep eligibility fixed rather than selecting successful purchasers after the reform.

## Identification Risks

[Analytical inference] Mobility is both an outcome and a source of missing observations. Observable-selection weighting cannot certify unbiased retention. State-sector controls help separate shared changes, but do not eliminate tenant-specific restructuring or changing selection.

## Data Requirements

[Analytical inference] Resolve the couple before constructing the person panel: otherwise a nonstate spouse can be misclassified. Preserve baseline-wave choice, household changes and missingness. Irregular waves are not annual policy observations; a regional rollout design needs additional timing and observations.

## Evidence Notes

Institutional facts use the national attachment, not Beijing's separate implementation date [E1]. The published paper supplies reported coding and methods [E2]; metadata supplies publication identity [E3]. The blocked AER candidate `candidate-19670874707c` is related housing-reform evidence, not a second ready variation merely because it studies prices. CHNS provider links attempted during resolution were inaccessible; neither their questionnaires nor current download conditions are certified.

The October7 follow-up inspected the September2010 AEA-hosted manuscript
behind that AER paper [E4, reported claim]. Its housing-price test uses
prereform province-average mismatch interacted with post-reform waves, among
households privately housed in1993. Mismatch is predicted minus observed log
market rental value, fitted on prereform private households; the province
average includes both housing groups. Equation17/Table6 uses household effects,
housing-quality controls and province-clustered bootstrap inference. These
private households face market spillovers, not direct tenant purchase exposure.
[Analytical inference] This application needs a separate household/province-wave
contract, generated-regressor uncertainty and credible differential trends;
the default entrepreneurship treatment and person-level contract cannot be
reused unchanged. It remains a bounded related application, not an admitted
design profile. The final publisher text and replication code remain unread.
The manuscript's unrestricted full-title resale claim on p5 must not override
the national decision's normal five-year market-entry condition [E1; E4].
