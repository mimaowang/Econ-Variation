---
schema_version: 2
id: china-2010-fuel-efficient-car-catalog-subsidy
name: China 2010 Fuel-Efficient Passenger-Car Catalog Subsidy
aliases: [节能产品惠民工程节能汽车补贴, 2010 fuel-efficient vehicle subsidy, 2010节能汽车推广目录]
status: grounded
provenance:
  task_id: task-5103de97971d
scope:
  country: China
  regions: [Mainland China]
  domains: [industrial-economics, environmental-economics, development-economics, consumer-demand]
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: Certified passenger-car models sold in mainland China entered a national RMB 3000 buyer subsidy through successive official catalogs.
identity:
  instrument: National fuel-efficient passenger-car purchase subsidy assigned through model-specific promotion catalogs
  authority: Ministry of Finance, National Development and Reform Commission, Ministry of Industry and Information Technology
  legal_identifiers: [财建〔2010〕219号, 2010年第13号公告, 财办建〔2010〕75号, 财建〔2011〕754号, 2011年第26号公告]
  implementation_regime: The first six catalogs expanded the original program through September 2011; the October 2011 stricter-threshold seventh catalog replaced the first six and is a successor regime, not another ordinary addition.
  assignment_mechanism: Manufacturers applied; authorities checked vehicle attributes and listed approved model codes. Technical eligibility alone did not confer a subsidy before catalog listing.
  parent: null
  related_variations: []
timeline:
  announcement: '2010-06-18'
  effective: null
  implementation_start: 2010
  implementation_end: 2011
  local_timing: The original rules applied from June 1, 2010; the first catalog was signed June 18 but its NDRC webpage was published June 30. A later official payment notice says buyers qualify from catalog publication. The paper dates the first wave to June 18 and drops wave-start months in its main regressions. Preserve these clocks rather than asserting a single verified first-sale date. The stricter successor rule began October 1, 2011, while the seventh-catalog notice was signed October 17 and posted October 19.
  anticipation: The national subsidy policy preceded the first catalog, and the authors explicitly examine possible purchase postponement; wave sequence was not announced in advance.
  last_verified: '2026-10-03'
assignment:
  unit: Passenger-car model code by month, linked to province-model-month sales
  treated: Models appearing in one of the first six official subsidy catalogs during the paper's main study window
  comparison_pool: Never-listed models sold in the same months; the paper's preferred comparison is never-listed vehicles in the least fuel-efficient attribute quartile, chosen to reduce demand-substitution contamination.
  rule: Passenger cars with engine displacement at most 1.6 liters had to meet fuel-consumption limits conditional on curb weight, transmission and seating configuration, apply, pass official review and enter a published catalog. A listed buyer received a one-time RMB 3000 subsidy through the sales channel.
  intensity: Binary model-month catalog subsidy status; the RMB 3000 amount is fixed, but its percentage of model price varies.
  exemptions: [Models above 1.6 liters, Models not approved and listed, Seventh-catalog successor eligibility outside the first-six-wave baseline]
  compliance: Official rules require buyer receipt of a separate subsidy at sale; catalog listing does not independently prove every dealer paid it or that transaction prices were unchanged.
  exposure_construction: Link each official catalog's manufacturer and vehicle-model code to model attributes and province-model-month sales. Turn treatment on only for listed models after the relevant catalog event; preserve catalog signature, public-posting and paper-coded wave dates separately. Drop announcement months as the paper does unless daily eligibility can be reconciled.
  required_identifiers: [Manufacturer, Official vehicle-model code, Province, Month]
  spillovers: Buyers may switch from unsubsidized but similar efficient cars, postpone purchases, or respond to concurrent city-specific vehicle restrictions.
research_compatibility:
  outcome_domains: [Passenger-car sales, Vehicle mix, Fuel efficiency, Consumer substitution]
  affected_populations: [Car buyers, Automakers, Dealers]
  mechanism_channels: [Effective purchase price, Model choice, Timing of purchases]
  best_for: [Model-level analysis of catalog entry and car demand with explicit substitution controls]
  not_good_for: [Calling fuel-efficiency thresholds randomized, Treating all qualifying vehicles as subsidized, Using October 2011 as an unchanged seventh rollout, Assuming proprietary model-sales data are open]
design:
  claim_type: causal
  affordances: [Multiple catalog waves, Model-code lists, Fixed nominal buyer subsidy, Observable technical eligibility rules]
  candidate_designs: [Model-level difference-in-differences, Event study with substitution-aware comparison groups]
  identifying_variation: Within-model change when officially listed across the first six waves versus never-listed models observed in the same periods
  primary_strategy: Chen, Hu and Knittel, Sections 3–5 and equations 1–3 of the author-hosted full working-paper version; compare province-model-month sales before and after model subsidy with never-listed controls and inspect substitution among nearby models.
  estimand: Conditional response of listed models' sales to receipt of the subsidy, with separate displacement from other models; not a randomized threshold effect or an economy-wide net benefit from a simple treated-control coefficient.
  treatment_variable: Indicator that model j is receiving the catalog subsidy in month t
  comparison_logic: Never-subsidized models provide same-period trends; models too similar to treated cars may lose sales to them, so the authors also use a distant fourth fuel-inefficiency quartile and analyze effects on closer unsubsidized quartiles.
  estimation_notes: The authors use model, province and calendar-month fixed effects with product-life-cycle and category-trend controls; the baseline excludes Beijing, Shanghai, the seventh wave and wave-start months. Their final AEA appendix probes alternative distant control groups. These choices are design judgments, not proof of parallel trends or noninterference.
  assumptions:
  - Conditional sales trends for subsidized models and chosen never-listed controls would have been comparable without catalog entry.
  - Unmeasured changes in model quality, advertising or dealer pricing do not coincide with catalog entry in a way that explains the effect.
  - The distant control group has limited substitution from subsidized models, while substitution among close alternatives is measured separately.
  diagnostics: [Pre-event sales trajectories, Alternative control groups, Wave-month inclusion sensitivity, Beijing and Shanghai inclusion sensitivity, First-six versus seventh-wave separation]
threats:
- type: nonrandom-approval-and-timing
  basis: reported
  condition: Manufacturers applied, and the government did not reveal how it ordered the waves. Entry and timing may correlate with unobserved demand or product decisions.
  evidence_refs: [E3, E4]
  possible_diagnostics: [Pretrends, Manufacturer-specific trends, Application records if available]
- type: spillovers-and-anticipation
  basis: reported
  condition: Subsidized models can displace close unsubsidized models or shift purchase timing; a simple DID against close alternatives can overstate new demand.
  evidence_refs: [E3, E4]
  possible_diagnostics: [Attribute-quartile contrasts, Event-time analysis, Distant controls]
- type: policy-clock-and-successor
  basis: documented
  condition: First-list signature and website publication differ, while the official payment notice anchors eligibility to publication; the October 2011 seventh list replaced earlier catalogs under tighter standards.
  evidence_refs: [E1, E2, E5, E6]
  possible_diagnostics: [Retain three date fields, Exclude wave-start months, Re-estimate successor separately]
empirical_requirements:
  contract_version: 1
  population: Passenger-car models produced and sold in mainland China, as defined by the paper
  observation_unit: Province-model-month
  geography_level: Province
  time_start: 2009
  time_end: 2011
  minimum_frequency: monthly
  minimum_pre_periods: 3
  minimum_post_periods: 3
  required_fields: [Model-level monthly sales, Official catalog model code and entry wave, Engine displacement, Fuel consumption, Curb weight, Transmission, Seating configuration, Model price, Province, Calendar month]
  required_identifiers: [Manufacturer, Official vehicle-model code, Province, Month]
  treatment_key: [Official vehicle-model code, Month]
  treatment_source: NDRC, MIIT and MOF official promotion catalogs and adjustment notices
  measurement_risks: [Proprietary sales data, Catalog-to-sales code crosswalk, Signature-versus-publication dates, Dealer pass-through, Concurrent car ownership restrictions]
design_profiles: []
evidence:
- id: E1
  source_type: policy-document
  citation: NDRC, MIIT and MOF, 2010 No. 13 announcement, first fuel-efficient-car catalog
  url: https://www.ndrc.gov.cn/fggz/hjyzy/stwmjs/201006/t20100630_1160889.html
  date: '2010-06-18'
  supports: [identity.authority, identity.legal_identifiers, identity.assignment_mechanism, timeline.announcement, timeline.local_timing, assignment.exposure_construction]
  verification_status: verified
  access_level: official-document
  locator: Announcement body and official PDF attachment; signed June 18, webpage published June 30. Attachment identifies approved model codes.
- id: E2
  source_type: implementation-document
  citation: MOF, NDRC and MIIT offices, 财办建〔2010〕75号, subsidy disbursement notice
  url: https://www.ndrc.gov.cn/fggz/hjyzy/jnhnx/201009/t20100916_1134429.html
  date: '2010-09-02'
  supports: [timeline.local_timing, assignment.compliance, assignment.rule, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Items 1–3; subsidy from catalog publication, separate from dealer discounts, and monthly model-level reporting.
- id: E3
  source_type: paper
  citation: Chen, Hu and Knittel, Subsidizing Fuel Efficient Cars, MIT CEEPR full working-paper version, 2018
  url: https://ceepr.mit.edu/wp-content/uploads/2021/09/2018-003.pdf
  date: 2018
  supports: [assignment.comparison_pool, assignment.exposure_construction, timeline.anticipation, design.primary_strategy, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.required_fields, design_applications.data_used]
  verification_status: reported
  access_level: full-text
  locator: PDF pp. 8–17, Sections 2.2–4, equations 1–3; pp. 34–38, Tables 5–8. Working-paper version, not a verified copy of the final journal text.
- id: E4
  source_type: appendix
  citation: Chen, Hu and Knittel, AEJ Economic Policy online appendix, November 2020
  url: https://www.aeaweb.org/articles/materials/15631
  date: 2020
  supports: [design.estimation_notes, threats.condition, assignment.comparison_pool]
  verification_status: reported
  access_level: full-text
  locator: PDF pp. 1–2, Section B on unknown wave sequencing; pp. 8–12, Section D on alternative control groups.
- id: E5
  source_type: policy-document
  citation: MOF, NDRC and MIIT, 财建〔2011〕754号, adjusted subsidy policy
  url: https://zfxxgk.ndrc.gov.cn/web/iteminfo.jsp?id=1280
  date: '2011-09-07'
  supports: [identity.implementation_regime, timeline.local_timing, assignment.exemptions, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Items 1–2; original rule through September 30, new fuel-consumption limits and unchanged RMB 3000 amount from October 1.
- id: E6
  source_type: policy-document
  citation: NDRC, MIIT and MOF, 2011 No. 26 announcement, seventh catalog
  url: https://www.ndrc.gov.cn/xxgk/zcfb/gg/201110/t20111019_960997.html
  date: '2011-10-17'
  supports: [identity.implementation_regime, timeline.local_timing, assignment.exemptions, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Announcement body; seventh catalog implements from October 1 and cancels the first six lists; signed October 17, posted October 19.
- id: E7
  source_type: paper
  citation: Chen, Hu and Knittel 2021, American Economic Journal Economic Policy 13(4), 152–184
  url: https://doi.org/10.1257/pol.20170098
  date: 2021
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: Citation, abstract and links to replication package and online appendix. Published article PDF access-controlled; empirical detail is taken from E3 and E4.
design_applications:
- paper: "Subsidizing Fuel-Efficient Cars: Evidence from China's Automobile Industry"
  doi: 10.1257/pol.20170098
  journal: 'American Economic Journal: Economic Policy'
  year: 2021
  research_question: Did a national fuel-efficient-car buyer subsidy change model sales and displace sales of other cars?
  population: Passenger-car models sold in China during the paper's 2009–2011 main analysis window
  outcome: Province-model-month sales
  data_used: [Proprietary province-model-month passenger-car sales, Official model eligibility and fuel-consumption records, Public model attributes]
  treatment_encoding: Model-month indicator after entry into one of the first six subsidy catalogs
  comparison: Never-listed model sales, with distant fuel-inefficiency quartile as the preferred control and closer quartiles used to inspect substitution
  empirical_design: Multiple-wave DID and event-time analysis; the first six waves are baseline and the seventh is a separate robustness exercise
  assumptions: [Conditional parallel sales trends, Limited spillover to distant controls, No coincident unobserved model change]
  threats_addressed: [Alternative controls, Purchase-timing tests, Beijing and Shanghai exclusion, Seventh-wave sensitivity]
  evidence_refs: [E3, E4, E7]
method_transfer: null
readiness_blockers:
- "Conditional for direct reuse: the paper's province-model-month sales came from a private arrangement, and official catalog PDFs still require a careful model-code crosswalk."
- Do not infer the first buyer subsidy date solely from the June 18 signature; the public listing date and official disbursement instruction point to publication, while the paper codes June 18 and excludes wave-start months in its baseline.
---

## Institutional Background

This was a national buyer subsidy, not a provincial pilot or a general tax reduction. Manufacturers sought approval for individual passenger-car models. Technical limits constrained which models could apply, but the operative exposure came when a model entered an official promotion catalog [E1–E3].

## What Changed

Approved models offered buyers a separate RMB 3000 subsidy at sale [E2, E5]. The first six catalogs expanded the eligible set. In October 2011, stricter limits and a replacement catalog changed that regime [E5–E6]. A model's technical fuel efficiency, application, listing and actual buyer payment are related but different facts.

## Implementation and Assignment

Manufacturers applied for individual model codes, and authorities published approved codes in successive catalogs [E1, E3]. Entry into a catalog, rather than merely satisfying a technical threshold, defines the paper's subsidy indicator.

## Why This Creates Empirical Variation

The authors link catalog status and model attributes to monthly model sales in provinces. They compare each listed model after entry with its earlier sales and with never-listed models sold at the same time [E3]. Nearby unsubsidized cars may lose customers to subsidized cars, so the paper also uses relatively distant cars for a comparison and estimates displacement separately [E3–E4]. The waves are observed policy assignment, not random assignment.

## Identification Risks

The first catalog carries a June 18 signature but a June 30 web-publication date [E1]. The official disbursement instruction says benefits begin on publication [E2], whereas the working paper calls June 18 the first wave [E3]. Its baseline omits wave-start months. Retain both dates and verify transaction-level exposure before using daily treatment; do not smooth away the conflict. The published article's identity is verified by AEA, but its access-controlled main PDF was not used for detailed claims [E7].

## Data Requirements

A feasible extension needs lawful province-model-month sales, a stable crosswalk from official vehicle codes to sales models, and measured product attributes. Catalogs make assignment reconstructable but do not provide the proprietary sales panel. A new design must distinguish subsidy-induced new demand from substitution and account for concurrent car-registration restrictions in Beijing and Shanghai. No independent replication is claimed.

## Evidence Notes

Official notices establish the catalog and payment rules [E1–E2, E5–E6]. The full empirical description comes from an author-affiliated working-paper version and the journal's online appendix [E3–E4]; AEA metadata establishes the 2021 publication [E7]. The inaccessible final article text and private sales data were not represented as inspected.
