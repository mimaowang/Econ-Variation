---
schema_version: 2
id: china-2003-government-procurement-law-industry-reliance
name: China's2003 government procurement law and industry procurement-reliance exposure
aliases: [政府采购法与行业政府订单依赖, Hang-Zhan procurement regulation, procurement allocation and manufacturing productivity]
status: grounded
provenance:
  task_id: task-160278660df6
scope:
  country: China
  regions: [Mainland manufacturing industries; CICS2005 covers120 cities excluding Tibet]
  domains: [firm, industrial-economics, development, public-economics, resource-allocation]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: A national Chinese procurement reform is interacted with manufacturing industries' dependence on government sales. The baseline encodes dependence as an above-median binary group, not firm contract receipt or a city pilot.
identity:
  instrument: The2003 Government Procurement Law standardizes covered government purchasing procedures, differentiated empirically by industry procurement reliance.
  authority: National People's Congress Standing Committee adopted the law; fiscal departments supervise government procurement and competent central/provincial authorities determine catalogues and thresholds.
  legal_identifiers: [中华人民共和国政府采购法, 中华人民共和国主席令第68号]
  implementation_regime: Effective nationally on2003-01-01 after adoption on2002-06-29. Covered purchases use fiscal funds and fall within procurement catalogues or above applicable thresholds. Transparency, supplier competition, procurement procedures and complaints change together. Industry sales shares do not legally determine eligibility.
  assignment_mechanism: A common national reform interacts with heterogeneous industry demand from government. The paper constructs dependence from2005 CICS responses about2004 sales, aggregates with sales weights at two-digit manufacturing industry, divides at the median and maps to four-digit industries. This exposure is measured after reform and is not randomized or an administrative cutoff.
  parent: null
  related_variations: []
timeline:
  announcement: '2002-06-29'
  effective: '2003-01-01'
  implementation_start: 2003
  implementation_end: null
  local_timing: Baseline post equals1 from2003 onward for all sampled industries. Local catalogues and procurement thresholds differ, but the paper does not code their separate adoption dates. Its detailed methods, event study and Table7 specify1998–2007; the introduction's1998–2008 wording is inconsistent and should not extend the executable sample.
  anticipation: Adoption in June2002 allowed advance changes in procurement. Table5 adds an exposure-by2002 term; its insignificant estimate is reported evidence, not proof that anticipation was absent.
  last_verified: '2026-10-07'
assignment:
  unit: Four-digit manufacturing industry-year; exposure is shared within its two-digit parent industry.
  treated: Industries whose two-digit parent has an above-median government-sales share in the paper's CICS2005 construction.
  comparison_pool: Remaining lower-reliance manufacturing industries in the same years. They also face the law and can sell to government; the contrast is differential reform exposure, not covered versus legally exempt industries.
  rule: Compute each two-digit industry's sum of government sales divided by sum of sales using the2004 survey question; set gs=1 above the industry median and map through GB/T4754-2002. Interact gs with1(year>=2003). TableA1 lists30 two-digit industries; its first15 descending shares imply the high group, but verify the actual crosswalk before coding four-digit units.
  intensity: Baseline binary high versus low procurement reliance; the median is an analyst classification, not a legal eligibility threshold. Do not replace it with annual realized firm orders.
  exemptions: [Emergency procurement and state-security or secret procurement are outside Article85, Military procurement has separate rules under Article86, Public-works tendering is governed by the Tendering and Bidding Law under Article4, Ordinary SOE procurement is not the government's fiscal procurement covered here]
  compliance: The law changes processes, not guaranteed awards or payments to every supplier. The paper's industry proxy does not observe actual compliant procurement for each firm; local enforcement and supplier qualification can vary.
  exposure_construction: Use CICS2005 sales and government-sales percentage for2004, sales-weight aggregation by two-digit industry and the GB/T4754-2002 mapping. Join to annual ASIF manufacturing firm accounts and aggregate outcomes to four-digit industry-year. Keep government-sales and sales-to-SOEs questions separate. A2002 IO alternative uses PASO-sector purchases, not actual covered procurement contracts.
  required_identifiers: [firm_id, year, two_digit_industry_code, four_digit_industry_code, industry_crosswalk_version]
  spillovers: Government orders can be redistributed among firms and industries; low-reliance industries need not be unaffected. The estimate is relative industry reallocation, not total national welfare or the causal effect of one awarded contract.
research_compatibility:
  outcome_domains: [manufacturing allocative efficiency, firm size-productivity allocation, manufacturing firm sales and productivity]
  affected_populations: [mainland manufacturing firms, industries with heterogeneous government demand, covered government buyers]
  mechanism_channels: [procurement transparency, reduced favoritism, reallocation of orders and production factors]
  best_for: [differential manufacturing allocation responses to procurement regulation, government demand and industry reallocation with explicit survey-measurement assumptions]
  not_good_for: [a randomized government-contract award effect, city-specific procurement rollout, treating all SOE purchases as GPL exposure, assuming2004 shares are pre-reform, claiming a national welfare effect from relative industry DID]
design:
  claim_type: reduced-form
  affordances: [common reform by industry exposure interaction, industry-year DID, firm mechanism comparisons under additional assumptions]
  candidate_designs: [industry-year DID, exposure event study]
  identifying_variation: Differential changes after2003 between high- and low-government-sales industries, conditional on industry and year effects and controls.
  primary_strategy: Eq4 uses gs_i*post_t, four-digit industry and year fixed effects, and changing industry controls. Table3 reports four-digit industry-clustered standard errors. The event study uses1998 as base and1999–2007 exposure interactions. Treatment varies at the broader two-digit parent, so a new application should assess inference at that assignment level rather than blindly copy four-digit clustering.
  estimand: Relative post-reform change in the employment-share/log-productivity covariance for high versus low procurement-reliance manufacturing industries, under conditional parallel trends and stable exposure classification.
  treatment_variable: gs_i*1(year>=2003); gs_i is constructed from2004 sales in CICS2005, not measured treatment take-up.
  comparison_logic: Requires the industry distribution of government demand to represent persistent public-service needs rather than an endogenous response to reform. Concurrent WTO, ownership and industrial-policy changes must not generate the same differential trend.
  estimation_notes: Eq5 defines the sum of deviations of employment shares times deviations of log firm productivity within an industry-year, not a generic correlation coefficient. TFP uses Olley-Pakes, with Levinsohn-Petrin and interquartile dispersion checks. Table3 has4295 baseline observations and4180 after tariff controls. CICS2003 reports2002 shares only for six manufacturing sectors; the reported0.94 correlation with2004 at that coarse level is not a fine-industry pre-reform assignment proof. For IO exposure, p583 prose says positive PASO purchases whereas Table4 note says above median; do not silently choose one as the verified alternative algorithm.
  assumptions: [conditional parallel trends across exposure groups, post-reform survey shares preserve underlying demand ranking, consistent industry crosswalk and survey weights, comparable firm coverage and productivity measurement, no correlated concurrent reform]
  diagnostics: [1998-base event study, top versus bottom thirds excluding middle industries, pre-reform broad-sector share comparison, verify2002 IO exposure rule against code,2002 anticipation interaction, separate SOE-procurement interactions, ownership and tariff controls, domestic-firm-only and pharmaceutical-excluded samples, broader-level inference sensitivity]
threats:
  - type: post-treatment-exposure
    basis: documented
    condition: Main exposure uses2004 sales after the2003 law. Reform-induced order reallocation can alter measured treatment membership; the paper assumes industry demand is persistent and offers imperfect alternative measures.
    evidence_refs: [E1]
    possible_diagnostics: [recover pre-reform industry dependence, inspect ranking stability and crosswalk, do not overstate coarse-sector correlation]
  - type: concurrent-reform
    basis: documented
    condition: WTO tariff cuts, SOE reform, foreign entry and industry policies can produce heterogeneous productivity trends. Controls and pretrends do not establish that all such confounding is removed.
    evidence_refs: [E1]
    possible_diagnostics: [industry-specific pretrends, tariff and ownership sensitivity, procurement versus SOE-demand distinction]
  - type: assignment-level-inference
    basis: inferred
    condition: Exposure is common to two-digit parents but baseline standard errors cluster at four-digit industry; shared parent shocks can correlate finer clusters.
    evidence_refs: [E1]
    possible_diagnostics: [two-digit clustering or appropriate small-cluster inference, leave-parent-out sensitivity]
  - type: measurement-and-access
    basis: documented
    condition: CICS procurement shares and ASIF coverage/productivity need independent reconstruction; the authors explicitly lack permission to share data. Modern procurement-contract archives are not a substitute for the historical survey.
    evidence_refs: [E1, E2]
    possible_diagnostics: [verify authorized historical data and variable availability, preserve coverage thresholds, assess government versus SOE question coding]
empirical_requirements:
  contract_version: 1
  population: Mainland manufacturing firms in ASIF1998–2007, all SOEs and non-SOEs above RMB5million annual sales, with usable firm accounts. CICS2005 samples12400 firms across120 cities and all provinces except Tibet to measure industry dependence.
  observation_unit: Four-digit manufacturing industry-year.
  geography_level: National manufacturing industries; city/province identifiers are needed for survey coverage and geographic mechanism checks, not city assignment.
  time_start: 1998
  time_end: 2007
  minimum_frequency: annual
  minimum_pre_periods: 4
  minimum_post_periods: 1
  required_fields: [firm_id, year, industry codes and historical crosswalk, sales, government_sales_percentage_2004, employment, capital and investment inputs for productivity estimation, material inputs for robustness, ownership, industry tariff and policy controls]
  required_identifiers: [firm_id, year, two_digit_industry_code, four_digit_industry_code]
  treatment_key: [two_digit_industry_code, national reform year2003]
  treatment_source: CICS2005 question about2004 sales to government, sales-weighted into two-digit industry shares, then mapped to four-digit industries; President Order68 supplies the national legal clock.
  measurement_risks: [post-law measured dependence, survey representativeness and missing sales, historical industry crosswalk, ASIF entry-exit and size threshold, estimated revenue productivity versus physical efficiency, coarse industry exposure and cluster dependence]
evidence:
  - id: E1
    source_type: paper
    citation: 'Hang, Jing, and Chaoqun Zhan.2023. Government procurement and resource misallocation: Evidence from China. Journal of Economic Behavior & Organization216:568–589. DOI10.1016/j.jebo.2023.10.014.'
    url: https://doi.org/10.1016/j.jebo.2023.10.014
    date: 2023
    supports: [identity.instrument, identity.assignment_mechanism, timeline.local_timing, timeline.anticipation, assignment.rule, assignment.comparison_pool, assignment.exposure_construction, design.primary_strategy, design.estimand, design.estimation_notes, empirical_requirements.population, design_applications.empirical_design]
    verification_status: verified
    access_level: full-text
    locator: 'Author-linked final22-page PDF https://zhanchaoqun.github.io/files/government-procurement-misallocation-jebo2023.pdf read in memory; Section2 p571; Sections4.1–4.3 pp577–578 Eqs4–5; Tables2–5 and Sections5.1–5.3 pp579–584; Table7 and data-availability statement p586; AppendixA TableA1 p587. Research-page link inspected at https://zhanchaoqun.github.io/research.html. TableA3/A4 mentioned in prose were not recovered.'
  - id: E2
    source_type: implementation-document
    citation: 中华人民共和国政府采购法, 主席令第68号,2002-06-29; original law reproduced by Guangdong tax authority in2008.
    url: https://guangdong.chinatax.gov.cn/gdsw/dgsw_zfcgzd/2008-04/15/content_b831d7e1493e4ef787776965b7a16b3d.shtml
    date: 2002
    supports: [identity.instrument, identity.authority, identity.implementation_regime, timeline.announcement, timeline.effective, assignment.exemptions, assignment.compliance]
    verification_status: verified
    access_level: official-document
    locator: 'Actual official HTML: adoption/order header; Articles2–8 fiscal purchases, catalogues, construction tendering and thresholds; Articles22–27 supplier qualification and procurement methods; Articles84–88 special regimes and effective date. Original2008 reproduction, not a later amended-law eligibility rule.'
design_applications:
  - paper: 'Government procurement and resource misallocation: Evidence from China'
    doi: 10.1016/j.jebo.2023.10.014
    journal: Journal of Economic Behavior & Organization
    year: 2023
    research_question: Does regulated government procurement change production-factor allocation across manufacturing firms?
    population: Mainland manufacturing industries from ASIF1998–2007 with dependence assigned from CICS2005.
    outcome: Within-industry employment-share/log-productivity covariance; robustness uses productivity dispersion.
    data_used: [ASIF1998–2007, CICS2005 government-sales question for2004, WITS tariffs, CICS2003 shares for2002, China2002 IO table]
    treatment_encoding: Above-median two-digit procurement reliance assigned to four-digit industry and interacted with post2003.
    comparison: Lower-reliance manufacturing industries in the same years, under industry/year effects and controls.
    empirical_design: Exposure-group DID with event-study and alternative-measure diagnostics; not contract-award randomization.
    assumptions: [parallel conditional industry trends, persistent public-service demand ranking despite post-law measurement, correct survey-to-industry linkage]
    threats_addressed: [reported pretrends, exposure-measure alternatives, anticipation, SOE purchasing distinction, concurrent reforms, firm coverage and outcome definitions]
    evidence_refs: [E1, E2]
method_transfer: null
readiness_blockers:
  - Conditional use requires authorized ASIF and historical CICS data plus the industry crosswalk. The authors cannot share their data; no executable public replication package was verified.
  - Main treatment is reconstructable from published methods and TableA1, but its post-reform measurement is an identification risk. A new causal application must assess whether reform changed the demand ranking and consider assignment-level inference.
  - Use the explicitly documented1998–2007 methods clock, retaining the introduction's1998–2008 discrepancy. The IO alternative has conflicting positive-purchase versus above-median wording and missing TableA4; recover code or clarification before reproducing that variant.
superseded_by: null
deprecation_reason: null
---

## Institutional Background

The law changes how government buys, rather than awarding a subsidy to every
manufacturing firm. Fiscal procurement within catalogues or above thresholds
is covered; ordinary SOE purchasing is a separate demand source [E2]. The
paper asks whether fairer order allocation also reallocates production factors
across firms [E1, reported interpretation].

## What Changed

Adoption in June2002 precedes the common January2003 legal start. Procedures,
supplier competition, contracts and challenges change as a package, not an
isolated transparency treatment. Lower-reliance industries are exposed to the
same law, so the paper estimates a relative response [E1; E2].

## Implementation and Assignment

The legal scope and empirical exposure are different. Industry classification
comes from sales-weighted2004 survey shares, observed after reform. Map the
two-digit share to four-digit industry before constructing the national
post interaction; individual wins or annual procurement growth would answer
another question [E1].

## Why This Creates Empirical Variation

The comparison is high versus low government dependence over the same reform
clock. It is useful for industrial allocation questions if that ranking
reflects persistent public demand. The paper itself acknowledges the danger
of post-law measurement and checks coarse pre-reform shares and IO purchases;
these checks are not proof of fine-industry exogeneity [E1].

## Identification Risks

Ownership restructuring, trade liberalization and common parent-industry
shocks can change the comparison. Preserve the actual four-digit clustering
as what the paper did, while reconsidering two-digit shared exposure for a
new application. Firm-level sales/productivity mechanisms are reported support,
not a second variation or a contract-receipt causal estimate [E1].

## Data Requirements

Firm accounts build industry allocation; survey government-sales questions
build exposure. Their linkage is by historical industry, not an asserted
firm-to-contract match. The data-sharing restriction is explicit, so readiness
means a documented conditional research option, not an immediately executable
open-data design [E1].

## Evidence Notes

Read the final body and original-law reproduction, not only the abstract.
The body documents the main exposure despite minor sample-clock wording
inconsistency. Keep its IO alternative's contradictory rule unresolved rather
than invent missing appendix or code [E1; E2]. No copyrighted paper or
restricted dataset is stored here.
