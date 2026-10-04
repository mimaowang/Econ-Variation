---
schema_version: 2
id: china-wto-accession-firm-performance
name: China's WTO-Accession-Era Industry Tariff Reductions and Manufacturing-Firm Performance
aliases:
- WTO accession China firm performance
- Brandt Van Biesebroeck Wang Zhang
- 中国加入WTO 企业绩效
- trade liberalization China

status: grounded
provenance:
  task_id: task-7d3ea6c12121
scope:
  country: China
  regions:
  - Mainland China
  domains:
  - trade
  - firm
  - productivity
  - industrial-organization
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: The application assigns annual industry tariff exposure to Chinese manufacturing firms and is usable for China-focused research.
identity:
  instrument: "[E1, reported claim] Annual 4-digit-industry output and input tariff changes during China's 1998-2007 trade-liberalization period, with the post-2001 WTO-agreement maximum allowable tariff used as an instrument for actual tariffs in the paper's IV specifications."
  authority: "[E2, verified] China became a WTO member on 11 December 2001. [E4, verified] Schedule CLII records China's goods concessions annexed to its accession protocol; E5 is the Ministry of Finance's account of implementing the reductions, not the annual legal notices themselves."
  legal_identifiers:
  - 'WT/ACC/CHN/49/Add.1, 1 October 2001: Schedule CLII, Part I (goods concessions) and Annex I staging matrix'
  implementation_regime: '[E4, verified] Product-specific bound rates at accession, final bound rates and implementation/staging columns define negotiated ceilings, not realized duties. [E5, reported claim] The Ministry of Finance reports annual reductions from 2002 and completion of all accession tariff commitments in 2010. [E1, reported claim] The application observes 1998-2007, including earlier liberalization; 2007 is its sample end, not the end of all commitments.'
  assignment_mechanism: '[E1, reported claim] A firm inherits its 4-digit industry''s lagged output-tariff and input-tariff exposure. Actual tariff choices may be endogenous; from 2001 onward, the paper instruments actual tariffs with the WTO agreement''s maximum allowable tariff.'
  parent: null
  related_variations:
  - china-trade-policy-uncertainty
  - china-mfa-quota-removal-textile-exporters
timeline:
  announcement: null
  effective: '2001-12-11'
  implementation_start: 1998
  implementation_end: 2007
  local_timing: '[E4, verified] Original staging rows assign product-specific annual ceilings rather than city rollout dates; inspected non-agricultural HS76061100 stages its ceiling across 2002-2004. [E1, reported claim] The application maps annual tariffs to industries over 1998-2007; post-2001 agreement ceilings instrument actual rates. Membership timing is distinct from those annual paths.'
  anticipation: '[E1, reported claim] The agreement''s maximum rates were mostly fixed by 1999, so negotiated commitments do not remove selection based on anticipated future industry performance.'
  last_verified: '2026-09-28'
assignment:
  unit: '[E1, reported claim] Manufacturing firm-year, inheriting 4-digit Chinese industry tariff measures.'
  treated: '[E1, reported claim] There is no untreated manufacturing group: firms face continuous lagged output-tariff and input-tariff levels, whose changes differ across industries and years.'
  comparison_pool: '[E1, reported claim] Within-firm changes over 1998-2007 and cross-industry differences in tariff paths, conditional on firm and year fixed effects; selected specifications additionally use sector-year effects.'
  rule: '[E1, reported claim] Map WITS HS8 import rates to 424 CIC4 manufacturing industries and take an unweighted product average for output tariffs. Weight industry tariffs by 2002 IO input shares for input tariffs, effectively at CIC3 detail. Account for HS2002 and CIC2003 changes. Output tariffs protect the firm''s final-good industry; they are not tariffs on Chinese exports.'
  intensity: '[E4, verified] Bound exposure varies by HS product and year in the original staging matrix. [E1, reported claim] The application separately measures continuous lagged industry output and input rates and instruments actual rates from 2001 onward with agreement ceilings. Industrial weights/concordances are paper constructions, not rules established by the schedule.'
  compliance: '[E1, reported claim] The tariff series records realized statutory trade protection; it does not establish firm-level compliance, take-up, or a uniform one-time treatment.'
  exemptions: []
  exposure_construction: '[E1, reported claim] Link firm-year industry code to lagged annual output and input tariffs. For the published IV robustness, use the agreement maximum allowable tariff from 2001 onward as the instrument; do not substitute a post-2001 dummy or append PNTR/MFA exposure without a separate paper and data construction.'
  required_identifiers:
  - firm ID
  - year
  - industry code (4-digit)
  - product-to-industry tariff concordance
  spillovers: '[E1, reported claim] Input tariffs transmit exposure through input-output links; entry, exit, and reallocation are part of the paper''s industry-performance decomposition, so own-industry tariff regressors need not isolate a no-spillover effect.'
research_compatibility:
  outcome_domains:
  - firm productivity
  - markups
  - prices
  - output
  - employment
  - entry
  - exit
  - product mix
  affected_populations:
  - Manufacturing firms
  - workers in trade-exposed industries
  - consumers
  mechanism_channels:
  - import competition
  - input tariff reduction
  - pro-competitive effects
  - markup compression
  - productivity improvement
  best_for:
  - Studying the effect of trade liberalization on firm-level productivity and market power
  - studying the distinct product-market and imported-input channels of tariff liberalization
  not_good_for:
  - A clean single-date WTO event study
  - US PNTR, export-market uncertainty, or MFA-quota effects without their separate exposure measures
design:
  claim_type: causal
  affordances:
  - annual industry tariff paths
  - distinct output and input tariff measures
  - rich firm-level panel data
  - pre-accession baseline period
  candidate_designs:
  - firm fixed-effects tariff regression
  - post-2001 allowable-tariff IV robustness
  identifying_variation: '[E1, reported claim] Firm/year-effects regressions use lagged CIC4 output tariffs and IO-weighted input tariffs, effectively CIC3, over 1998-2007. The IV variant instruments actual rates from 2001 onward with agreement maximum allowable rates. Industry tariffs are not firm-specific duties paid.'
  assumptions:
  - Conditional tariff changes, or the allowable-tariff instrument, are not correlated with unobserved firm-performance changes after the stated fixed effects and controls
  - Negotiated maximum allowable tariffs affect firm performance only through realized tariff protection in the IV application
  - Output-price and input-price deflators recover the intended markup and productivity objects under the paper's production-function assumptions
  diagnostics:
  - assess whether tariff changes correlate with pre-liberalization industry productivity and trends
  - report the first stage of agreement maximum tariffs for realized post-2001 tariffs
  - separately inspect output-tariff and input-tariff estimates and the corrigendum
  primary_strategy: '[E1, reported claim] Firm fixed-effects regressions of markup or estimated productivity on lagged output and input tariffs, with year effects and, in some specifications, sector-year effects; two-way clustering at industry-year and firm level. The paper also decomposes industry changes.'
  estimand: '[E1, reported claim] Under the application''s tariff-exogeneity or IV assumptions, the partial effect of a change in an industry''s output or input tariff on Chinese manufacturing-firm markups or productivity; it is not the total effect of WTO membership.'
  treatment_variable: '[E1, reported claim] One-year-lagged CIC4 output tariff and IO-weighted input tariff (effectively CIC3); negotiated maximum rates instrument actual tariffs from 2001 onward. Do not replace either exposure by a membership dummy or a contemporary CTS snapshot.'
  comparison_logic: '[E1, reported claim] Firm-years in industries with differently evolving continuous tariff measures, rather than a binary treated-versus-untreated post-accession comparison.'
  estimation_notes: '[E3, verified] Corrected Table 3 retains firm effects and restricts the sample to non-industry-switchers. The corrigendum preserves markup and input-tariff productivity conclusions but removes definitive firm-level output-tariff productivity evidence. Productivity is measured from deflated revenues, not observed physical output. [E1, reported claim] Its efficiency-effect interpretation relies on matching regression and industry-deflator weights.'
threats:
- type: concurrent-reforms
  basis: inferred
  condition: Industry-correlated reforms or demand shocks can move with tariff paths; a common WTO date does not itself separate these channels.
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for other reforms
  - retain industry-level controls and assess sensitivity to observed concurrent policy exposures
  - distinguish actual tariff effects from separate PNTR, quota-removal, and foreign-investment-policy designs
- type: anticipation-effects
  basis: inferred
  condition: Tariff negotiations and liberalization preceded 2001, and the paper reports that maximum rates were mostly fixed by 1999; a sharp post-membership interpretation is therefore vulnerable to anticipation.
  evidence_refs:
  - E1
  possible_diagnostics:
  - inspect year-specific tariff paths rather than imposing a single post-2001 break
  - test whether pre-period industry performance predicts later tariff changes
empirical_requirements:
  contract_version: 1
  population: '[E1, reported claim] Chinese manufacturing firms in the Annual Survey of Industrial Firms, 1998-2007, after the paper''s sample cleaning and industry-concordance restrictions.'
  observation_unit: Firm-year
  geography_level: National (firm-level) with industry variation
  time_start: 1998
  time_end: 2007
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 5
  required_fields:
  - firm output
  - inputs
  - value added
  - employment
  - capital stock
  - industry (4-digit)
  - ownership and entry/exit status
  - product/industry tariff concordances and input-output weights
  - price-deflator inputs needed for the paper's markup/productivity construction
  required_identifiers:
  - firm ID
  - year
  - industry code
  treatment_key:
  - industry code
  - lagged output tariff
  - lagged input tariff
  - post-2001 agreement maximum allowable tariff (IV variant)
  treatment_source: '[E1, reported claim] WITS HS8 import rates concorded to CIC4; input tariffs use 2002 IO weights. E4 provides original commitments, not the historical applied-rate panel. E7 links author protection measures, concordances, corrected deflators and the public replication deposit; linked data/code contents were not reconstructed in this audit.'
  measurement_risks:
  - matching tariff lines to industrial classification
  - firm-level output price vs industry-level deflator issues
  - tariff-to-industry and input-output concordance error
  - corrected input-price-deflator construction (see E3)
  - contemporaneous applied rates versus negotiated annual ceilings, preferential rates and processing-trade exemptions
  - latest CTS is a revised working database, not an unchanged historical accession panel (see E6)
evidence:
- id: E1
  source_type: paper
  citation: 'Brandt, Loren, Johannes Van Biesebroeck, Luhang Wang, and Yifan Zhang. 2017. "WTO Accession and Performance of
    Chinese Manufacturing Firms." American Economic Review 107 (9): 2784–2820.'
  url: https://doi.org/10.1257/aer.20121266
  date: 2017
  supports:
  - identity.instrument
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.implementation_start
  - timeline.implementation_end
  - timeline.local_timing
  - timeline.anticipation
  - assignment.unit
  - assignment.treated
  - assignment.comparison_pool
  - assignment.rule
  - assignment.intensity
  - assignment.compliance
  - assignment.exposure_construction
  - assignment.spillovers
  - design.claim_type
  - design.primary_strategy
  - design.identifying_variation
  - design.estimand
  - design.treatment_variable
  - design.comparison_logic
  - design.estimation_notes
  - design.assumptions
  - design.diagnostics
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
  locator: 'Published 37-page PDF linked at https://sites.google.com/view/jovb/chinese-data, https://drive.google.com/uc?export=download&id=1U-zx6OcO1TybLGQuHj5h4jnn1twQZN75. Inspected pp. 2789-2794 (WITS HS8, unweighted CIC4 output tariffs, IO-weighted input tariffs, concordance changes, negotiation/IV discussion and Table 1), p. 2795 equation (1), and pp. 2796-2798 (markup and revenue-productivity construction/weighting). Correction is independently inspected in E3.'
- id: E2
  source_type: other
  citation: 'World Trade Organization. "China and the WTO" member-information page.'
  url: https://www.wto.org/english/thewto_e/countries_e/china_e.htm
  date: 2026
  supports:
  - identity.authority
  - timeline.effective
  verification_status: verified
  access_level: official-document
  locator: 'Member-information page, opening membership statement: China has been a WTO member since 11 December 2001.'
- id: E3
  source_type: paper
  citation: 'Brandt, Loren, Johannes Van Biesebroeck, Luhang Wang, and Yifan Zhang. 2019. "WTO Accession and Performance of Chinese Manufacturing Firms: Corrigendum." American Economic Review 109 (4): 1616-1621.'
  url: https://www.aeaweb.org/content/file?id=8967
  date: 2019
  supports:
  - design.estimation_notes
  - empirical_requirements.measurement_risks
  - design_applications.empirical_design
  verification_status: verified
  access_level: full-text
  locator: 'AEA-hosted eight-page corrigendum manuscript: pp. 1-2 explain revised conclusions and the six-IO-sector input-deflator concordance offset; p. 4 corrected Table 3/notes (non-switchers, fixed effects, IV, clustering); pp. 5-7 revised Tables 4/7 and implications. Published correction DOI: 10.1257/aer.109.4.1616.'
- id: E4
  source_type: policy-document
  citation: 'World Trade Organization. 2001. WT/ACC/CHN/49/Add.1, Schedule CLII - People''s Republic of China, Part I: Schedule of Concessions and Commitments on Goods, with Annex I staging matrix.'
  url: https://goods-schedules.wto.org/browse-initial/1521
  date: '2001-10-01'
  supports:
  - identity.authority
  - identity.legal_identifiers
  - identity.implementation_regime
  - timeline.local_timing
  - assignment.intensity
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: official-document
  locator: 'Original accession attachment set fetched from https://goods-schedules.wto.org/download_all/42559 and inspected in memory. CHN49A1-00-en-fr-es.pdf cover identifies Schedule CLII as annexed to the protocol; CHN49A1-03-en.pdf PDF p. 1 (printed p. 79, HS25) displays accession/final bound rates and implementation columns; CHN49A1-18-en.pdf PDF p. 34 (printed p. 544, HS76-83) displays product-by-year staging, including HS76061100, and PDF p. 69 (printed p. 576) ends the matrix. No full tariff panel or industry concordance was reconstructed.'
- id: E5
  source_type: official-data
  citation: 'Yu Weiping, Vice Minister of Finance. 2021. 支持开放型经济高质量发展——加入世界贸易组织20年财政工作回顾. Ministry of Finance, Customs Department; originally Economic Daily, 11 December 2021, p. 3.'
  url: https://gss.mof.gov.cn/jhbd/202112/t20211217_3775859.htm
  date: '2021-12-17'
  supports:
  - identity.authority
  - identity.implementation_regime
  verification_status: verified
  access_level: official-document
  locator: 'Full official-hosted retrospective, first section (一) 履行入世降税承诺，统筹内外完善关税制度: annual reductions from 2002, all accession tariff commitments completed by 2010, subsequent autonomous reductions, periodic HS/tariff-line revisions and provisional rates. This is an agency implementation account, not inspection of each historical annual notice or rate.'
- id: E6
  source_type: other
  citation: 'World Trade Organization. Consolidated Tariff Schedules Database: contents, sources, transpositions and jargon definitions.'
  url: https://www.wto.org/english/tratop_e/tariffs_e/cts_e.htm
  date: 2026
  supports:
  - empirical_requirements.measurement_risks
  verification_status: verified
  access_level: official-document
  locator: 'Contents and latest-approved-schedules sections: bound maximum rates; working-tool status; continuous revisions and HS transpositions. Jargon definitions distinguish applied duties from ceilings and preferential tariffs. Inspected China CTS notes page https://ttd.wto.org/en/data/cts/china/schedule-notes/ labels HS2002 and update 20 February 2026; do not substitute it for original historical exposure.'
- id: E7
  source_type: replication
  citation: 'Johannes Van Biesebroeck. Chinese Data & Programs, author data page; AEA/openICPSR replication deposit 112892, version V1.'
  url: https://sites.google.com/view/jovb/chinese-data
  date: 2026
  supports:
  - empirical_requirements.treatment_source
  - empirical_requirements.measurement_risks
  verification_status: verified
  access_level: metadata
  locator: 'Author page lists industry/IO concordances, protection measures, and input_benchmark correction dated 15 November 2018. Its replication link resolves to https://doi.org/10.3886/E112892V1 (openICPSR version V1, 11 October 2019). Inspected listings only, not linked data/code contents, restricted firm data, or reproduction results.'
design_applications:
- paper: WTO Accession and Performance of Chinese Manufacturing Firms
  doi: 10.1257/aer.20121266
  journal: American Economic Review
  year: 2017
  research_question: '[E1, reported claim] How are changes in Chinese manufacturing firms'' markups and productivity related to output- and input-tariff liberalization during the WTO-accession era?'
  population: '[E1, reported claim] Chinese manufacturing firms in the 1998-2007 NBS Annual Survey of Industrial Firms sample, subject to the paper''s matching and industry-stability restrictions.'
  outcome: '[E1, reported claim] Estimated firm markups and productivity, plus industry-level decompositions of performance changes.'
  data_used:
  - '[E1, reported claim] NBS Annual Survey of Industrial Firms, 1998-2007; WITS HS8 import rates averaged into CIC4 output tariffs; 2002 IO-weighted input tariffs; and price-deflator inputs. Use the corrected input deflator identified by E3/E7.'
  treatment_encoding: '[E1, reported claim] Lagged output and input tariff levels by 4-digit industry-year; post-2001 agreement maximum allowable tariffs are instruments in the IV variant.'
  comparison: '[E1, reported claim] Within-firm and cross-industry comparisons across annual tariff paths, with firm and year fixed effects; not post-2001 firms versus an untreated group.'
  empirical_design: '[E1, reported claim] Firm fixed-effects tariff regressions with revenue-productivity/markup construction and an IV path. [E3, verified] Corrected Table 3 restricts to non-switchers; the corrigendum qualifies firm-level output-tariff productivity evidence.'
  assumptions:
  - conditional tariff paths or the allowable-tariff instrument are exogenous to unobserved firm-performance changes
  - production function correctly specified
  - markups identified from output elasticities and revenue shares
  threats_addressed:
  - actual-tariff endogeneity through the maximum-allowable-tariff IV specification after 2001
  - tariff-path correlation with initial industry performance through paper-reported tests
  - measurement correction through the 2019 corrigendum
  evidence_refs:
  - E1
  - E3
readiness_blockers:
- Reuse remains conditional on vintage-correct annual applied and bound tariff series, HS2002/CIC2003 concordances, IO weights, restricted firm-data access and corrected price-deflator/code versions. E4 closes the original commitment identity and staging boundary; E5 independently documents annual implementation, but this audit does not verify every historical applied-rate row or annual Chinese tariff notice. A contemporary CTS snapshot cannot fill that gap.
- This record serves the Brandt et al. tariff application only. It does not establish an exposure for US PNTR, MFA quota removal, export-market access, or a general one-time WTO shock; those require distinct records and sources.
method_transfer: null
---
## Institutional Background

[E2, verified] China became a WTO member on 11 December 2001. The Brandt et al. application is not a record of every consequence of that membership. It uses annual Chinese tariff measures during a longer 1998-2007 liberalization period. US permanent-normal-trade-relations policy and the textile-quota regime are related historical developments, but neither is this record's treatment variable. [E1, reported claim]

[E4, verified] The original Schedule CLII, dated 1 October 2001, records the negotiated goods commitments annexed to the accession protocol. Its bound rates are ceilings, not evidence that each firm paid that rate. The Ministry of Finance's retrospective reports annual reductions from 2002 and completion of all accession tariff commitments in 2010; it also describes subsequent autonomous reductions and tariff-line revisions. Thus the paper's 2007 endpoint is a sample boundary, not institutional completion. [E5, reported claim]

## What Changed
[E1, reported claim] The paper links its trade-liberalization setting to WTO accession and measures the relevant change as annual tariffs on final-good industries (output tariffs) and imported inputs (input tariffs). Those two measures have different economic channels and should remain separate. The paper also documents liberalization before 2001, so calling its design a one-date accession shock would erase the actual time structure.

[E4, verified] The original tariff tables distinguish accession ceilings, final ceilings and implementation, while the staging matrix sets out product-specific annual paths. This grounds the commitment underlying the IV; it does not replace the realized import-rate series. Applied rates can lie below bound rates, and the WTO's CTS is a continually revised working database. Its latest consolidated version should not be treated as an unchanged historical panel. [E6, verified]

## Implementation and Assignment
[E1, reported claim] Firm-year observations inherit lagged tariffs from their 4-digit industry. There is no completely unexposed manufacturing control group. The contrast is continuous: otherwise similar firm-years lie in industries whose output and input tariffs evolve differently. The paper instruments realized tariffs from 2001 onward with the agreement's maximum allowable tariff, recognizing that actual tariff setting can be endogenous. This is an application-specific strategy, not proof that all accession-related changes were exogenous.

[E1, reported claim] Product-to-industry mapping is part of the exposure, not clerical cleanup. The paper averages WITS HS8 import rates without trade weights into CIC4 output tariffs, then constructs input tariffs with 2002 IO shares, effectively at CIC3 resolution. HS2002 and CIC2003 revisions require concordances. The industry exposure describes protection, not a firm's observed duty payment; preferences and processing-trade exemptions prevent that interpretation. [Analytical inference] A new regional application would additionally need a justified local industry-composition mapping rather than assigning one nationwide post dummy to all locations.

## Why This Creates Empirical Variation
[E1, reported claim] The useful variation is the annual industry tariff path linked to firm outcomes, with firm and year fixed effects and a separate IV path. It can support a narrowly stated claim about tariff protection and the paper's markup/productivity measures, conditional on its measurement and exclusion assumptions. It cannot by itself identify the total effect of WTO membership, a US-market-access shock, or a textile-quota shock.

## Identification Risks
[E1, reported claim] The agreement's maximum rates were mostly fixed by 1999, while tariff reform also predates membership. Thus anticipation and industry-correlated reforms remain central risks, not footnotes. The IV helps only if negotiated maximum rates affect outcomes through realized tariffs rather than anticipated sector prospects. In addition, the 2019 corrigendum corrected the input-price deflator: its revised evidence preserves the markup findings and the input-tariff productivity effect, but no longer gives definitive firm-level evidence that output-tariff cuts raised productivity. [E3, verified]

[E3, verified] The correction fixes a six-position IO-concordance offset in assigning input deflators; corrected Table 3 also makes the non-industry-switching sample restriction explicit. [E1, reported claim] Productivity uses deflated revenues, not observed physical output. Interpreting estimated tariff effects as efficiency effects requires the paper's deflator/regression weighting argument; it does not recover each firm's physical productivity level.

## Data Requirements
[E1, reported claim] Reuse requires the 1998-2007 NBS Annual Survey of Industrial Firms, stable firm/industry identifiers, historical product-tariff concordances, IO weights and suitable price deflators. [E7, verified metadata] The author page links protection measures, concordances, corrected deflators and the replication deposit (DOI 10.3886/E112892V1). This audit inspected the listings, not the data/code contents or access to restricted firm data. E4 anchors the original commitments; annual applied rates and the full exposure merge still need reconstruction. Dataset access and reconstruction belong in the complementary data repository, linked by DOI rather than duplicated here.

## Evidence Notes
This audit upgrades the existing record to `grounded`: E4 supplies original commitment/staging evidence, E5 independently documents annual implementation, and E1/E3 establish the actual application and its correction. This is conditional decision-ready knowledge, not a certified replication. The inspected scan pages are named in E4; neither every tariff row nor each annual Chinese implementing notice was checked. E6 prevents a modern bound-rate database from being mistaken for historical applied protection. E7 records inspectable reuse routes without claiming their contents were reproduced. PNTR, MFA quotas and export-market policy remain outside this record's boundary. No new variation is counted merely for improving this existing record.
