---
schema_version: 2
id: china-mfa-quota-removal-textile-exporters
name: MFA Quota Removal and Trade Liberalization's Effect on Chinese Textile and Clothing Exporters
aliases:
- Khandelwal Schott Wei MFA China
- Chinese textile export quota removal
- embedded institutional reform AER
- 纺织服装出口配额取消
- MFA配额取消

status: grounded
provenance:
  task_id: task-653f2a948cfb
scope:
  country: China
  regions:
  - Mainland Chinese exporters; destination exposure in United States, European Union and Canada
  domains:
  - international-trade
  - firm-dynamics
  - productivity
  - industrial-organization
  - development
  variation_type: single-date-reform
  knowledge_role: global-china-variation
  china_relevance: Import-market quota expiry changes mainland Chinese textile and apparel firms' product-destination opportunities. This is a non-agricultural industrial-development and firm-allocation variation, not an overseas-method-only record or a Chinese local-policy experiment.
identity:
  instrument: '[E1, verified] The 1 January 2005 removal of pre-existing importing-market textile and clothing quotas on Chinese exports, as encoded by Khandelwal, Schott, and Wei at the HS-product-by-destination level. This record is not a generic China WTO-accession or phased product-rollout variation.'
  authority: '[E2, verified] The WTO Agreement on Textiles and Clothing (ATC) ended its special quota regime on 1 January 2005. [E1, verified] The paper''s exposure is the subset of US, EU, and Canadian product-destination pairs that were quota-bound through 2004.'
  legal_identifiers:
  - Agreement on Textiles and Clothing (ATC), Article 9 final expiry; Article 2 transition
  - Multifiber Arrangement (MFA), predecessor regime; paper uses MFA terminology for the final quotas
  implementation_regime: '[E2, verified] The ATC was a 1995-2005 transition, but its remaining restrictions terminated on 1 January 2005. [E1, verified] The paper deliberately focuses on that final common date, not on an event-study across ATC stages.'
  assignment_mechanism: '[E1, verified] For each HS product and destination among the United States, European Union, and Canada, the paper defines exposure by whether that destination imposed a quota through 2004. It retains only HS products that are bound in at least one of those destinations and quota-free in at least one other; hence the within-product comparison is across destinations, and the policy change is common in 2005.'
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: '2005-01-01'
  implementation_start: 2005
  implementation_end: 2005
  local_timing: Final ATC quotas expire on 2005-01-01. The paper holds 2004 product-destination quota status fixed and compares annual changes ending in 2004 and 2005; 2005 safeguards affect a subset, so the encoded annual post variable is not proof of a full year without quantitative restraints.
  anticipation: '[E2, verified] The ATC transition was announced years before expiry, so the paper does not supply a no-anticipation design. [E1, verified] Its identification instead compares the 2004-2005 differential change for bound versus free destinations with the corresponding 2003-2004 differential.'
  last_verified: '2026-09-28'
assignment:
  unit: '[E1, verified] Chinese firm-HS8-product-destination-year shipment, aggregated where needed to HS-product-destination-year.'
  treated: '[E1, verified] A retained HS product exported to a US, EU, or Canadian destination that imposed a quota through 2004; it is exposed when those remaining quotas terminate in 2005.'
  comparison_pool: '[E1, verified] The same retained HS products exported quota-free to another one of the three destination markets. Products bound in all three destinations are excluded; the resulting sample contains 359 HS categories.'
  rule: '[E1, verified] The treatment indicator is a pre-2005 quota status at the product-destination level, not a Chinese product''s ATC integration stage or a firm''s product-mix score.'
  intensity: '[E1, verified] Primary treatment is binary quota-bound status through 2004 interacted with the 2005 period. The inspected core design does not require a quota-utilization-rate intensity measure.'
  compliance: The ATC restrictions end legally on January 1; replacement safeguards are not ATC continuation. The paper reports unchanged results excluding US products under 2005 safeguards, but could not identify affected EU products. Actual quota status within 2005 therefore differs across products and destinations; no blanket complete-liberalization claim is warranted.
  exposure_construction: Link Chinese Customs firm-year-HS8-destination shipments to 2004 destination-specific MFA quota status. Aggregate EU destinations into the paper's single market block; retain only HS products both quota-bound and quota-free across US/EU/Canada. Form outcome changes ending in 2004 and 2005 and regress on a 2005 indicator, quota-bound indicator and interaction. Recover the exact EU membership aggregation and HS concordance before replication; do not use Chinese regions as the original assignment unit.
  required_identifiers:
  - firm ID
  - year
  - product code (HS)
  - MFA category
  - quota status
  - destination-specific 2004 quota status
  - destination country to EU market-block crosswalk
  exemptions: []
  spillovers: '[E1, verified] Firm entry and reallocation are part of the paper''s mechanism, so a shipment-level estimate is not a no-interference effect for an isolated firm. Destination demand, Chinese domestic reforms, and post-expiry safeguards can also change the contrast.'
research_compatibility:
  outcome_domains:
  - export volume
  - export prices
  - firm entry and exit
  - firm-level productivity
  - resource allocation
  - product quality
  affected_populations:
  - Chinese textile and clothing exporters
  - importing firms in the US and EU
  - workers in the textile and clothing industry
  - competing exporters from other countries
  mechanism_channels:
  - quota removal channel
  - resource reallocation channel
  - firm entry channel
  - rent dissipation
  - productivity improvement through reallocation
  best_for:
  - Studying how trade liberalization affects resource allocation across firms
  - analyzing misallocation from quantitative restrictions
  - estimating productivity gains from trade reform
  not_good_for:
  - Non-traded sectors
  - periods outside the phase-out window
  - outcomes not affected by export conditions
  - settings without binding quotas before liberalization
design:
  claim_type: causal
  affordances:
  - common 2005 removal of destination-specific quota constraints
  - within-HS-product contrast between quota-bound and quota-free destinations
  - firm entry and ownership composition within product-destination markets
  candidate_designs:
  - difference-in-differences at the HS-product-destination level with a 2003-2004 benchmark
  - decomposition of product-destination export change into incumbent and entrant margins
  identifying_variation: '[E1, verified] The identifying contrast is the change from 2004 to 2005 for quota-bound product-destination pairs, net of the contemporaneous change for quota-free destinations of the same retained HS products and net of the analogous 2003-2004 difference. It is not staggered rollout across Chinese product categories.'
  assumptions:
  - conditional on the within-product destination comparison and the prior-year differential, quota-bound and quota-free destination pairs would not have had different 2004-2005 changes absent quota expiry
  - no contemporaneous destination-specific shock differentially affects the previously constrained pairs relative to the comparison pairs
  - the 2003-2004 differential is informative about the relevant pre-2005 differential, despite the pre-announced multilateral transition
  diagnostics:
  - reproduce the actual pre-reform placebo contrasting 2002-2003 with 2003-2004; 2003-2004 is also the baseline benchmark
  - inspect balance and ownership composition across the quota-bound and quota-free product-destination cells before expiry
  - distinguish extensive-margin entry from incumbents' intensive-margin response
  - test sensitivity to the paper's restricted within-product destination sample
  primary_strategy: '[E1, verified] Product-destination difference-in-differences comparing the 2004-2005 change for pre-2005 quota-bound pairs with the corresponding quota-free pairs, using 2003-2004 as a pre-change difference; the paper then decomposes the response by firm margin and ownership.'
  estimand: The change in product-destination outcome changes for previously quota-constrained exports relative to quota-free exports after removing the analogous prior-year differential, under the identifying assumptions. Quota-bound means covered by a quota, not necessarily a proven binding fill rate. The paper studies prices and quantity-share reallocation by firm margin/ownership and model-based productivity implications, not direct TFP effects for every exporter or a national WTO-accession effect.
  treatment_variable: '[E1, verified] Pre-2005 quota-bound HS-product-destination indicator interacted with the 2005 period.'
  comparison_logic: '[E1, verified] For a product exported to more than one of the US, EU, and Canada, compare a destination that maintained a quota through 2004 to one that did not; use their 2003-2004 differential to discipline the 2004-2005 comparison.'
  estimation_notes: Published equation 3 regresses changes on 2005, quota-bound and their interaction for change-years 2004 and 2005, clustering by HS product; variants add product-destination fixed effects. The sample contains 359 HS8 categories after excluding 188 covered in all three markets. Table 3 separately decomposes quantity shares into incumbents, adders, new exporters and exiters; a firm can enter one product-market and remain incumbent in another. Unit values are nominal FOB value divided by quantity, not observed physical productivity. Quality adjustment in equation 7 infers demand residuals using elasticity 4 and product/country-year effects; it remains model-dependent.
threats:
- type: destination-specific-confounding
  basis: documented
  condition: '[E1, verified] The application depends on quota-bound and quota-free destinations for the same HS product being a valid counterfactual after their prior differential is netted out. Demand, trade-policy, or market-access shocks that change differentially in 2005 would threaten that comparison.'
  evidence_refs:
  - E1
  possible_diagnostics:
  - reproduce the 2002-2003 versus 2003-2004 pre-reform placebo
  - inspect destination-specific contemporaneous policy and demand changes
  - retain the paper's within-product, mixed-destination sample restriction
- type: post-expiry-restrictions
  basis: documented
  condition: US and EU reimposed restrictions on a subset within 2005, not only after the paper's window. The paper's US-exclusion robustness does not establish absence of EU contamination; expectations of renewed allocation can also affect the 2005 export surge. CITA's official notice dates successive US limits to May 23, May 27 and August 31 and documents staged entry of overshipments.
  evidence_refs:
  - E1
  - E5
  possible_diagnostics:
  - document the destination-product policy path rather than carrying the 2005 indicator forward mechanically
  - separate the paper's 2003-2005 window from later outcomes
  - reproduce the US safeguard exclusion and recover EU 2005 category-to-HS mapping before assuming an uncontaminated annual contrast
- type: general-equilibrium-effects
  basis: inferred
  condition: Quota removal on Chinese exports affected world prices, which in turn affected export patterns of other countries
    and potentially input prices, creating general equilibrium feedback
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for world market conditions
  - examine third-country export responses
  - use firm-level analysis to isolate micro effects
  - sensitivity to global demand controls
empirical_requirements:
  contract_version: 1
  population: '[E1, verified] Chinese exporters of the retained textile and clothing HS products to the United States, European Union, and Canada, observed around 2003-2005.'
  observation_unit: '[E1, verified] Firm-HS8-product-destination-year shipment, with product-destination aggregates for the principal contrast.'
  geography_level: National exporter data linked to foreign destination markets
  time_start: 2003
  time_end: 2005
  minimum_frequency: annual
  minimum_pre_periods: 2
  minimum_post_periods: 1
  required_fields:
  - firm ID
  - year
  - product code
  - export value
  - export quantity
  - destination country
  - destination-specific 2004 MFA quota status
  - firm ownership category for ownership decompositions
  required_identifiers:
  - firm ID
  - year
  - HS8 product code or a documented exact conversion to the paper's HS8 classification
  - destination market code
  - destination country to EU market-block crosswalk
  treatment_key:
  - HS8 product code
  - destination market code
  - pre-2005 quota-bound indicator
  - 2005 period indicator
  treatment_source: '[E1, verified] Chinese Customs firm-level export transactions linked to an HS-to-MFA concordance identifying which destinations imposed quotas in 2004; the paper cites a concordance made available by the Embassy of China''s Economic and Commercial Affairs office. [E2, verified] WTO material verifies only the common 1 January 2005 expiry of the ATC regime, not the paper''s product-destination coding.'
  measurement_risks:
  - firm-level export data may not cover all export channels (processing trade reporting issues)
  - product code harmonization across datasets
  - the restricted sample excludes products quota-bound in all three destinations and therefore does not describe all Chinese textile exports
  - HS/MFA concordance and destination-specific 2004 status must be reproduced exactly; a national product indicator changes the design
  - observed net entry is a mechanism/outcome margin, not proof by itself that China''s licensing rule was inefficient
  - baseline needs 2003-2005; the separate pre-reform placebo also needs 2002, while descriptive exports extend back to 2000
  - FOB unit values mix efficiency, quality and markups; quantity units differ across products
  - Customs-to-NBS producer matching is incomplete and particularly weak for SOEs; it is not needed for the default export comparison
evidence:
- id: E1
  source_type: paper
  citation: 'Khandelwal, Amit K., Peter K. Schott, and Shang-Jin Wei. 2013. "Trade Liberalization and Embedded Institutional
    Reform: Evidence from Chinese Exporters." American Economic Review 103 (6): 2169–2195.'
  url: https://sompks4.github.io/public/mfa_aer.pdf
  date: 2013
  supports:
  - scope.china_relevance
  - identity.instrument
  - identity.authority
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.local_timing
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.compliance
  - assignment.exposure_construction
  - assignment.spillovers
  - design.identifying_variation
  - design.assumptions
  - design.diagnostics
  - design.primary_strategy
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - threats.condition
  - empirical_requirements.population
  - empirical_requirements.observation_unit
  - empirical_requirements.time_start
  - empirical_requirements.time_end
  - empirical_requirements.required_fields
  - empirical_requirements.required_identifiers
  - empirical_requirements.treatment_key
  - empirical_requirements.treatment_source
  - empirical_requirements.measurement_risks
  - design_applications.paper
  - design_applications.doi
  - design_applications.journal
  - design_applications.year
  - design_applications.research_question
  - design_applications.population
  - design_applications.outcome
  - design_applications.data_used
  - design_applications.treatment_encoding
  - design_applications.comparison
  - design_applications.empirical_design
  - design_applications.assumptions
  - design_applications.threats_addressed
  verification_status: verified
  access_level: full-text
  locator: Published author-hosted AER PDF inspected again 2026-09-28. Pages 2169-2171 distinguish allocation inference from an observed allocation rule; p.2175 footnotes 9-11 document within-2005 safeguards, export-licensing overlap and unknown auction selection; pp.2176-2179 define Customs units, EU aggregation, 359 HS8 products, equation 3 and HS clustering; pp.2180-2185 and Table 3 distinguish firm-product-market entry and the true pre-reform placebo; pp.2187-2188 equation 7 define quality adjustment. NBS comparison and limited firm-name matching are separate, not the baseline dataset.
- id: E2
  source_type: policy-document
  citation: 'World Trade Organization. "Textiles" and "Agreement on Textiles and Clothing" overview.'
  url: https://www.wto.org/english/tratop_e/texti_e/texti_e.htm
  date: 2005
  supports:
  - identity.authority
  - identity.implementation_regime
  - timeline.effective
  - timeline.anticipation
  - assignment.compliance
  - threats.condition
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: official-document
  locator: WTO overview header inspected again 2026-09-28 states that the ATC and all restrictions under it terminated January 1, 2005 and that the sector thereafter returned to general multilateral rules. This establishes the common endpoint, not a promise of no replacement safeguards or a paper-specific HS-destination concordance.
- id: E3
  source_type: paper
  citation: 'American Economic Association. "Trade Liberalization and Embedded Institutional Reform: Evidence from Chinese Exporters" article metadata and supplementary-material listing.'
  url: https://www.aeaweb.org/articles?id=10.1257/aer.103.6.2169
  date: 2013
  supports:
  - design_applications.doi
  verification_status: verified
  access_level: metadata
  locator: 'AEA article page confirms the DOI, journal, volume, pages, and availability of a replication package and supplemental appendix; substantive application claims are supported by the inspected author-hosted article [E1].'
- id: E4
  source_type: paper
  citation: 'Khandelwal, Amit K., Peter K. Schott, and Shang-Jin Wei. 2013. "Trade Liberalization and Embedded Institutional Reform: Evidence from Chinese Exporters." DOI identifier.'
  url: https://doi.org/10.1257/aer.103.6.2169
  date: 2013
  supports:
  - design_applications.doi
  verification_status: reported
  access_level: metadata
  locator: 'Canonical DOI identifier for the published AER article; it is used only for bibliographic identity because substantive fields are supported by the inspected author-hosted full text [E1].'
- id: E5
  source_type: implementation-document
  citation: Committee for the Implementation of Textile Agreements. Entry of Shipments of Cotton, Wool and Man-Made Fiber Textiles and Apparel in Excess of China Textile Safeguard Limits. Directive dated November 29, 2005, Federal Register 70, 72427, December 5, 2005, FR Doc. E5-6842.
  url: https://www.govinfo.gov/content/pkg/FR-2005-12-05/pdf/E5-6799.pdf
  date: '2005-11-29'
  supports: [timeline.local_timing, assignment.compliance, threats.condition, empirical_requirements.measurement_risks]
  verification_status: verified
  access_level: official-document
  locator: Official scanned PDF p.72427 inspected 2026-09-28. The first notice is E5-6842 despite this two-page PDF's filename E5-6799, which refers to a different notice on p.72428. Lists May 23 limits for 338/339, 347/348 and 352/652; May 27 limits for 638/639, 647/648, 301 and 340/640; August 31 limits for 349/649 and 620; all through December 31, with delayed staged entry. Its directive paragraph truncates 340/640 to 40/640, while the explanatory paragraph and table give 340/640. It does not provide the paper's Chinese HS8 concordance or EU categories.
- id: E6
  source_type: policy-document
  citation: World Trade Organization. Agreement on Textiles and Clothing, Articles 1-2 and 9.
  url: https://www.wto.org/english/docs_e/legal_e/16-tex_e.htm
  date: 1994
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.effective, timeline.anticipation]
  verification_status: verified
  access_level: official-document
  locator: WTO legal text inspected 2026-09-28, Article 9 terminates the agreement and restrictions on the first day of the 121st WTO month and forbids extension; page header gives January 1, 2005. The transition is not a no-anticipation experiment. The Annex uses HS6 and cannot substitute for the paper's destination-specific HS8 quota concordance.
design_applications:
- paper: 'Trade Liberalization and Embedded Institutional Reform: Evidence from Chinese Exporters'
  doi: 10.1257/aer.103.6.2169
  journal: American Economic Review
  year: 2013
  research_question: How did the removal of externally imposed export quotas affect Chinese textile and clothing exports,
    and what does the pattern of export expansion reveal about resource misallocation under the quota regime?
  population: '[E1, verified] Chinese textile and clothing exporters in the retained 359-HS-product sample, exporting to the United States, European Union, or Canada during 2003-2005.'
  outcome: '[E1, verified] Product-destination export value, quantity, unit price, firm entry/exit margins, and ownership composition; the paper uses these responses to assess the allocation of quota licenses.'
  data_used:
  - Chinese Customs Trade Statistics (firm-level export transactions)
  - '[E1, verified] Destination-specific 2004 quota-status concordance for US, EU, and Canadian markets.'
  - Separate NBS Annual Survey of Manufacturing 2005 ownership-group productivity comparison; not a complete Customs producer match or a default treatment join
  treatment_encoding: '[E1, verified] A product-destination pair is quota-bound if that destination imposed a quota through 2004; the treatment is its interaction with the 2005 period. The paper does not use a 2002-versus-2005 staggered treatment encoding in its principal application.'
  comparison: '[E1, verified] Within the same retained HS product, compare destinations that were quota-bound through 2004 with destinations that were quota-free, and compare their 2004-2005 differential with the same differential from 2003-2004. Products bound in all three destinations are excluded.'
  empirical_design: '[E1, verified] Product-destination difference-in-differences over 2003-2005, followed by decomposition of the 2004-2005 response into intensive and extensive margins and ownership groups.'
  assumptions:
  - the quota-free destination cells provide a valid within-product counterfactual for the bound cells after their prior differential is netted out
  - no 2005 destination-specific demand or policy shock differentially changes bound and free cells beyond the quota expiry
  threats_addressed:
  - product composition through a within-HS, mixed-destination sample
  - common changes through the 2003-2004 differential benchmark
  - allocation mechanism through entry and ownership decompositions rather than an assumption that quota licenses were randomly allocated
  - reported US safeguard-product exclusion; EU safeguard exclusion remains unresolved in the paper
  evidence_refs:
  - E1
  - E4
readiness_blockers:
- The record fits mainland non-agricultural development and firm allocation, but is not an original regional/urban assignment. A local-outcome application needs a separately justified predetermined regional export exposure and must address trade reallocation and spillovers; the published firm-product-destination design does not itself validate such a regional design.
- The exact published replication package and original quota-license allocation records were not inspected; claims about the Chinese licensing mechanism remain bounded to the paper's tested inference rather than independently verified administrative reality.
- Recover the original HS8-by-destination 2004 quota concordance, EU market aggregation and legal Customs access before reconstruction. The WTO treaty establishes expiry, not the exact 359-product cells.
- Map the 2005 US safeguard categories and obtain an inspected EU primary instrument and HS correspondence. Regulation (EC) 1084/2005 is a concrete EU lead, but EUR-Lex retrieval returned a redirect/empty HTTP 202 on 2026-09-28; search snippets were not admitted as verified legal evidence. Paper footnote 9 reports EU restrictions without identifying their product list.
method_transfer: null
---
## Institutional Background

[E2, verified] The WTO's Agreement on Textiles and Clothing (ATC) was a transition away from the earlier special textile quota regime, and its remaining restrictions terminated on 1 January 2005. The historical policy was imposed by importing markets, not by a Chinese city or province. [E1, verified] Khandelwal, Schott, and Wei study how that external market-access change interacted with the Chinese allocation of export quota licenses; the paper's findings about misallocation are evidence about this application, not a direct administrative archive of every licensing decision.

## What Changed

[E2, verified] The common legal boundary relevant here is 1 January 2005, when the ATC special regime ended. [E1, verified] Although the wider ATC transition had earlier stages, the published application focuses on the final expiry and asks how Chinese exports to destinations that had maintained quotas through 2004 changed relative to exports of the same products to destinations that had not. It should therefore not be recoded as a staggered 2002-versus-2005 Chinese liberalization.

## Implementation and Assignment

[E1, verified] The application joins Chinese Customs shipments by firm, HS8 product, destination, and year to a destination-specific pre-2005 quota classification. It begins with 547 HS products subject to a quota in at least one of the United States, European Union, or Canada, removes the 188 bound in all three, and works with 359 products that have both a bound and a free destination. A product may thus be treated for exports to one destination and control for exports to another. This construction is the heart of the record; a product-only treatment variable loses the comparison that makes the paper usable.

EU countries are aggregated into one quota market. The word "bound" here denotes
quota coverage, not proof that each cell exhausted its quota. Firm entry is also
market-specific: an exporter can add a previously constrained product-destination
pair while remaining an incumbent elsewhere. Do not turn that change into a claim
that an entirely new producer was established. [E1, sections III-IV]

## Why This Creates Empirical Variation

[E1, verified] The paper compares the quota-bound/free difference in the 2004-to-2005 change with the analogous 2003-to-2004 difference. It reports that export growth and price decline after expiry are driven by net entry. The authors use the entry and ownership patterns to evaluate whether the preceding Chinese quota-license allocation was productivity based. This is a carefully bounded inference about allocation under the quota regime, not proof that a quota label is intrinsically exogenous or that every later Chinese textile outcome follows the same mechanism.

Equation 3 uses outcome changes, with change-years 2004 and 2005 and errors
clustered by HS product; variants add product-destination effects. Its separate
pre-reform placebo compares 2002-2003 with 2003-2004. The default 2003-2005 panel
therefore provides two pre years and one post year, not two post observations.
This distinction determines whether a later dataset can implement the design
without silently inventing a longer treatment path. [E1, equation 3 and Table 3]

## Identification Risks

The critical identifying question is not whether 2005 was random: expiry was an
announced multilateral change. It is whether the differential change for previously
constrained and quota-free markets would have remained comparable absent expiry.
The first-difference comparison does not eliminate destination-specific demand or
policy shocks. A future regional application needs additional exposure construction
and assumptions; the current paper does not assign treatment to Chinese cities.
[E1; E6; analytical inference]

Safeguards are a within-window issue. The paper reports that excluding US products
restricted in 2005 leaves its results unchanged, but it could not identify the EU
product list. CITA's official notice independently confirms US limits beginning
in May and August, and later staged admission of excess shipments. Thus the paper
identifies a transition using initial quota status, not a universally unrestricted
2005. Expectations of replacement quota allocations are another interpretation
explicitly considered in its footnote 9. [E1, reported checks; E5, verified dates]

## Data Requirements

A replication needs Chinese Customs transactions with firm ID, HS8 product, destination, year, value, and quantity; the paper's destination-specific 2004 quota concordance; and a stable HS/MFA crosswalk. It also needs the sample rule excluding products bound in all three destinations. A general WTO timeline establishes the legal endpoint but cannot replace the product-destination exposure crosswalk. [E1, verified; E2, verified]

Ownership enters the allocation decomposition. Customs unit values are nominal
FOB value divided by product-specific quantity units; they are not direct TFP.
The NBS ownership-group TFP comparison is separate: producer-exporter name matching
is limited, especially for SOEs using trading divisions. Do not require a complete
NBS merge for the export baseline or advertise one as already available. [E1,
section III, footnotes 14-15 and section IV.C]

## Evidence Notes

[E1, verified] The paper finds that the export response and price decline are principally accounted for by net entry, and uses that pattern in its allocation analysis. The record deliberately does not add unsupported specifics—such as a verified nationwide licensing rule, a quota-utilization-rate treatment, or a staggered Chinese rollout. The paper's counterfactual calculation and claims about the productivity contribution of allocation remain paper-reported results, not independently reconstructed administrative facts.

This audit adds the treaty's exact expiry clause and a primary US implementation
notice, while leaving the EU legal-category crosswalk and original replication
construction unresolved. Grounded status recognises a traceable mainland-facing
development variation with a recoverable comparison, not a finished data deposit
or a certified regional causal design.
