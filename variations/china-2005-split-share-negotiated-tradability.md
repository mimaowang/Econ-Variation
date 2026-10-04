---
schema_version: 2
id: china-2005-split-share-negotiated-tradability
name: China 2005 Negotiated Split-Share Tradability Conversion and SOE Exposure
aliases:
- Split-Share Structure Reform
- Liao Liu Wang secondary privatization
- 股权分置改革与国企经营表现
status: grounded
provenance:
  task_id: task-ca1e06b9d69b
scope:
  country: China
  regions: [Mainland China; Shanghai and Shenzhen A-share listed firms]
  domains: [firm-economics, industrial-organization, development-economics, finance, corporate-governance]
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: >
    Chinese listed firms negotiated conversion of previously nontradable
    A shares into shares eligible for future exchange trading. The inspected
    JFE application compares operating changes of state-controlled and
    non-state-controlled reform completers. This is a corporate ownership
    and incentive exposure, not a regional pilot or an automatic transfer
    of state ownership to private owners.
identity:
  instrument: Negotiated elimination of the A-share tradability divide, with shareholder consideration, firm implementation dates and resale restrictions.
  authority: CSRC supervises and coordinates; stock exchanges administer implementation and continuing oversight; required state-asset approvals remain separate.
  legal_identifiers:
  - 关于上市公司股权分置改革试点有关问题的通知, 证监发[2005]32号, signed29 April2005
  - 上市公司股权分置改革管理办法, 证监发[2005]86号, issued4 September2005
  implementation_regime: >
    The April pilot selected companies following shareholder intentions and
    sponsor recommendations. September measures replaced the pilot notices
    and retained negotiated consideration, dual shareholder voting and
    staged resale restrictions while setting a general exchange-administered
    procedure. The paper pools2005-2007 completers; it does not identify a
    separate pilot-selection effect. This record serves the shared conversion
    mechanism, not a claim that administrative entry rules stayed identical.
  assignment_mechanism: >
    Reform completion is a firm-specific negotiated event. State control
    supplies the paper's differential exposure to prospective privatization
    and state-agent incentives, while non-SOEs also gain tradability. Neither
    completion timing nor state ownership is randomly allocated.
  parent: null
  related_variations: []
timeline:
  announcement: '2005-04-29 (signed pilot notice; SZSE page and paper date it30 April)'
  effective: '2005-04-29 pilot notice;2005-09-04 replacement management measures'
  implementation_start: 2005
  implementation_end: null
  local_timing: >
    Firm proposal, shareholder approval, implementation and lockup expiry
    are different dates. The paper retains1032 nonfinancial firms completing
    reform in2005-2007;2007 is a sample cutoff, not a verified nationwide end.
    September Article27 anchors the12-month lockup to plan implementation.
    Use firm disclosures to reconcile the database completion field before
    constructing annual event time; do not assign all firms the national date.
  anticipation: >
    Pilot intentions, disclosed plans, negotiations and voting precede
    implementation. The authors' expected-privatization interpretation can
    operate before actual state-share sales. The notice does not establish
    that markets or managers were surprised.
  last_verified: '2026-10-03'
assignment:
  unit: Listed firm with firm-specific conversion date, ownership exposure and annual operating outcomes.
  treated: Reform-completing state-controlled firms in the paper's633-SOE subsample; all original nontradable shareholders receive the legal conversion opportunity subject to restrictions.
  comparison_pool: Reform-completing non-SOEs,399 in the inspected sample; matching portfolios constructed by size-industry or size-market-to-book. They are reform-exposed, not untreated firms.
  rule: >
    A general-regime motion normally requires all nontradable shareholders'
    consent, or holders of at least two thirds of nontradable shares.
    Passage separately requires at least two thirds of participating voting
    rights overall AND of participating tradable-share voting rights.
    State-asset approval is required where applicable. The exchange agrees
    implementation timing. The paper classifies SOEs by ultimate state control,
    including voting/control rights, rather than requiring a majority equity stake.
  intensity: >
    State-owned shares divided by total shares is an alternative continuous
    exposure in the paper, alongside ultimate-controller classification and
    state-share groups. Negotiated consideration and future share sales are
    endogenous terms or mechanisms, not independent randomized treatments.
  exemptions:
  - Paper excludes228 firms from1260 completers because of delisting, financial industry membership or incomplete information; legal eligibility is not this sample restriction.
  - Management measures Article19 sets conditions for firms with investigations or other abnormal situations; Article20 confines A/H/B companies' conversion to the A-share market.
  compliance: >
    Conversion does not imply immediate resale. Original nontradable shares
    cannot trade or transfer during the first12 months after implementation.
    For original holders above5% of total shares, exchange sales after that
    lockup cannot exceed5% of total company shares in12 months or10% in24
    months. Extra plan promises can bind further. Announcement, tradability,
    lockup release and actual ownership transfer must remain distinct.
  exposure_construction: >
    Join firm-specific completion/implementation dates to annual accounts,
    ultimate controllers, state-share ratios and original nontradable holdings.
    Build non-SOE5x5 size-industry benchmark portfolios and the alternative
    size-market-to-book portfolios. Subtract each matched portfolio's median
    change from the SOE change. Table5 defines operating revenue/profit
    changes using the values three years before and after reform, normalized
    by the pre-reform value; do not replace endpoints with three-year window
    averages. Exact date-to-accounting-year mapping and portfolio formation
    coding require source reconciliation before numerical reproduction.
  required_identifiers: [firm_id, accounting_year, reform_date, industry_id]
  spillovers: >
    A market-wide supply and governance reform can affect both ownership
    groups. Competition and state-parent asset transfers link firms further.
    A relative SOE estimate need not equal the economy-wide growth effect.
research_compatibility:
  outcome_domains: [operating revenue, operating profit, employment, investment, corporate governance]
  affected_populations: [Mainland nonfinancial A-share reform completers, State-controlled listed enterprises, Comparable non-state-controlled listed enterprises]
  mechanism_channels: [Prospective privatization, Tradability and market discipline, State-agent incentives, Asset injection and fundraising]
  best_for:
  - Studying differential operating and governance responses of SOEs versus reform-exposed non-SOEs with harmonized accounts and ownership histories.
  - Distinguishing changed privatization opportunity from observed state ownership transfer.
  not_good_for:
  - Treating private firms as wholly untreated by the reform or conversion timing as randomly assigned.
  - Interpreting acquired employment or parent-company assets as aggregate job creation or new productive capacity.
  - Extrapolating a listed-firm contrast to all mainland firms or an economy-wide welfare effect.
design:
  claim_type: causal
  affordances: [Firm-specific negotiated conversion timing, State versus non-state ownership exposure, Matched reform-exposed benchmark portfolios]
  candidate_designs: [Benchmark-adjusted before-after comparison, Cross-sectional quantile regressions of operating changes]
  identifying_variation: >
    The paper attributes larger post-conversion operating changes among SOEs
    relative to comparable non-SOE completers to an additional privatization
    channel. Its causal interpretation requires common non-privatization
    effects and comparable counterfactual changes; neither follows from
    the legal conversion rule or portfolio matching alone.
  primary_strategy: >
    Compare operating changes three years before and after conversion and
    report group medians and Wilcoxon tests. For SOEs, subtract the median
    change of a matched5x5 non-SOE benchmark portfolio. Regress firm changes
    on state ownership and covariates using25th,50th and75th quantile
    regressions, with2005/2006 completion-year indicators. This is the paper's
    DID-style contrast, not a documented annual staggered TWFE event study.
  estimand: >
    A relative operating response associated with state ownership among
    selected conversion completers, interpreted by the authors as an additional
    privatization effect under their comparison assumptions. It is not the
    average effect of converting tradability for all firms, nor the effect
    of a completed state-to-private ownership sale.
  treatment_variable: Firm-specific reform event plus SOE classification or state-share ratio; negotiated compensation and asset injection enter mechanism exercises, not baseline exogenous assignment.
  comparison_logic: >
    Non-SOEs undergo the same tradability reform but lack the hypothesized
    additional state-agent privatization channel. Matched ownership-group
    changes aim to net out common reform and economic effects. Unobserved
    SOE-specific shocks or different completion selection can violate that logic.
  estimation_notes: >
    Published Table5 defines normalized revenue/profit endpoint changes at
    a three-year horizon. Medians across firms and benchmark portfolios must
    not be confused with taking a median over a firm's annual window.
    Table6 includes market capitalization, nontradable/tradable ratio,
    regulated-industry and H/B-share indicators and completion-year controls.
    Printed t-statistics do not establish an inspected clustering procedure.
    Section4.1.3 uses CPI-adjusted operating revenue/profit, headcount for
    employment and (change in gross property/plant/equipment plus change in
    intangible assets) divided by operating revenue for capital expenditure.
    The latter is a reported accounting proxy, not direct new capital formation.
    The stock-return application uses different daily-data requirements and
    is not part of this operating-outcome data contract.
  assumptions:
  - Matched ownership groups would have comparable operating changes absent the additional SOE channel.
  - Reform timing, completion and ownership classification do not select differential latent operating trajectories after conditioning.
  - Harmonized accounts isolate operating changes rather than accounting redefinition or changes in consolidation boundaries.
  diagnostics:
  - Examine pre-reform trajectories, completion selection and ownership transitions; these are proposed checks, not all reported paper tests.
  - Compare size-industry and size-market-to-book benchmarks and overlap within portfolio cells.
  - Separate asset-injection or parent-to-listed-firm transfers from new investment and employment creation.
  - Test sensitivity to crisis-period exposure and the2007 accounting transition with harmonized line items.
threats:
- type: negotiated_timing_and_ownership_selection
  basis: documented
  condition: Official rules select pilot firms through intentions and sponsor recommendation and set negotiated/voted company implementation; no random allocation of state control or timing is established.
  evidence_refs: [E2, E3]
  possible_diagnostics: [Pre-event trajectory comparisons, Completion and survival selection analysis, Baseline ownership histories, Portfolio common support]
- type: accounting_and_consolidation_changes
  basis: reported
  condition: Paper Section4.1.3 identifies January2007 accounting changes and manually recovers older operating revenue/profit; the conclusion cautions employment growth can include employees transferred with injected parent assets.
  evidence_refs: [E1]
  possible_diagnostics: [Harmonized annual-report definitions, Consolidation boundary tracking, New versus transferred jobs, Asset-injection sensitivity]
- type: differential_concurrent_shocks
  basis: inferred
  condition: Three-year post horizons for2005-2007 completers overlap the financial crisis and other reforms; common portfolio adjustment need not remove ownership-specific responses.
  evidence_refs: [E1]
  possible_diagnostics: [Completion-cohort sensitivity, Industry and ownership-specific trends, Restricted horizons with explicit changed estimand]
empirical_requirements:
  contract_version: 1
  population: Nonfinancial mainland A-share firms completing conversion in2005-2007, including SOEs and matched non-SOEs with usable before/after reports.
  observation_unit: Firm-year inputs collapsed to firm-level three-year-horizon changes and benchmark portfolio medians.
  geography_level: Mainland listed firm
  time_start: 2002
  time_end: 2010
  minimum_frequency: annual
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields: [operating_revenue, operating_profit, consumer_price_index, employment, firm_outcome, ultimate_controller, state_share_ratio, nontradable_share_count, tradable_share_count, market_capitalization, market_to_book, industry, regulated_industry, cross_listing, accounting_definition, consolidation_boundary]
  required_identifiers: [firm_id, accounting_year, reform_date, industry_id]
  treatment_key: [firm_id, reform_date, ultimate_controller, state_share_ratio]
  treatment_source: Firm reform disclosures and CSMAR/WIND records reported by the paper; historical annual reports for ultimate control, share structure and harmonized operating accounts.
  measurement_risks:
  - Calendar coverage2002-2010 is an inferred envelope for2005-2007 events plus/minus three years, not an independently verified balanced source panel.
  - The one-pre/one-post minimum refers to endpoint availability three years apart from the event; adjacent annual observations are not baseline reproduction or a sufficient pretrend history.
  - Current controller labels cannot replace historical ones; inspected text does not close every classification date or ownership-switcher rule.
  - Database access, exact event-date/year mapping,25-cell formation/ties and missing endpoint handling need recovery before reproduction; no replication code was inspected.
  - Revenue/profit definitions must be harmonized across2007; asset injection changes reporting perimeter and employment counts.
  - Deflate operating outcomes consistently with Section4.1.3; exact CPI base and implementation were not closed by inspected replication code. If using investment, also recover gross property/plant/equipment and intangible-asset changes for the paper's proxy; those fields are not mandatory for a revenue-only question.
evidence:
- id: E1
  source_type: paper
  citation: 'Liao, Li; Bibo Liu; Hao Wang.2014. China''s secondary privatization: Perspectives from the Split-Share Structure Reform. Journal of Financial Economics113(3),500-518.'
  url: https://eng.pbcsf.tsinghua.edu.cn/__local/2/8D/BF/5B2906725D8247333002A83695D_77ECA550_E3FB9.pdf?e=.pdf
  date: '2014-09'
  supports: [scope.china_relevance, identity.assignment_mechanism, timeline.local_timing, timeline.anticipation, assignment.unit, assignment.treated, assignment.comparison_pool, assignment.intensity, assignment.exemptions, assignment.exposure_construction, assignment.spillovers, design.identifying_variation, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, threats.condition, empirical_requirements.population, empirical_requirements.required_fields, empirical_requirements.treatment_source, empirical_requirements.measurement_risks, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design]
  verification_status: reported
  access_level: full-text
  locator: >
    Published19-page PDF on Tsinghua PBC School of Finance site inspected in
    memory2026-10-03; printedpp504-505 regime;506-509 Sections4.1-4.4
    ownership, comparison, accounts, sample and regressions;510-514 Tables2-8;
    p512 Table5 endpoint-change definition;516 conclusion employment caveat.
    Printed page=PDF page+499. No replication code or exact cell-membership
    table inspected. Reported privatization interpretation is not independent
    certification of causal validity.
- id: E2
  source_type: policy-document
  citation: CSRC pilot notice证监发[2005]32号, signed29 April2005; full text hosted by Shenzhen Stock Exchange with30 April page date.
  url: https://www.szse.cn/marketServices/deal/reform/t20050608_519253.html
  date: '2005-04-29'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.announcement, timeline.effective, assignment.rule, assignment.compliance, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Full notice inspected2026-10-03; heading and signature distinguish page/signature dates; I pilot selection; III dual voting thresholds; V lockup and above5%-holder sale restrictions; VI required approvals; VII exchange implementation/oversight; XI immediate effect.
- id: E3
  source_type: policy-document
  citation: CSRC上市公司股权分置改革管理办法,证监发[2005]86号,4 September2005; official Zhengzhou SASAC reproduction dated22 October2009.
  url: https://gzw.zhengzhou.gov.cn/zcfg/2974776.jhtml
  date: '2005-09-04'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.effective, timeline.local_timing, assignment.rule, assignment.exemptions, assignment.compliance, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: >
    Inspected2026-10-03: heading86/date; Articles2-5 negotiation/exchange/motion;
    8-11 timing/disclosure;15-17 state-asset approval/dual vote/implementation;
    19-20 abnormal and A/H/B cases;23-27 promises, restructuring and lockups;
    35-38 disclosures;55 immediate effect and repeal of pilot notices32/42.
    Official reproduction omits most of Article12; that article is not used.
    No original scanned CSRC gazette or firm-specific implementation plan
    is claimed inspected.
- id: E4
  source_type: other
  citation: Publisher-deposited Crossref metadata for Liao Liu Wang, JFE113(3),September2014,500-518.
  url: https://doi.org/10.1016/j.jfineco.2014.05.007
  date: '2014'
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: Direct API metadata inspected2026-10-03 at https://api.crossref.org/works/10.1016/j.jfineco.2014.05.007; title, three authors, journal, volume, issue, publication month and pages agree with inspected published PDF front matter.
design_applications:
- paper: 'China''s secondary privatization: Perspectives from the Split-Share Structure Reform'
  doi: 10.1016/j.jfineco.2014.05.007
  journal: Journal of Financial Economics
  year: 2014
  research_question: Whether tradability conversion generates additional operating improvements and governance incentives in SOEs relative to non-SOE completers.
  population: '1032 nonfinancial2005-2007 reform completers:633 SOEs and399 non-SOEs after228 exclusions from1260 completers.'
  outcome: CPI-adjusted operating revenue/profit, employee headcount and capital-expenditure proxy over operating revenue; governance and stock returns are additional paper outcomes with distinct measurement demands.
  data_used: [CSMAR financial and reform data cross-checked with WIND, Manually collected pre2007 annual-report operating revenue/profit, CPI adjustment reported in Section4.1.3, Ultimate-controller and state-share records, Reform consideration and asset-injection information]
  treatment_encoding: Firm-specific conversion event with state-control or state-share exposure; normalized operating changes three years before/after, benchmarked to matched non-SOE portfolio medians.
  comparison: Converted non-SOEs matched in5x5 size-industry or size-market-to-book portfolios, not legally unexposed companies.
  empirical_design: Median before-after comparisons and benchmark-adjusted ownership contrast plus cross-sectional quantile regressions; no annual staggered TWFE specification inferred.
  assumptions: [Comparable ownership-group counterfactual changes, Common non-privatization reform effects, Selection and accounting changes not driving differences]
  threats_addressed: [Alternative ownership measures, Two benchmark constructions, Accounting-definition harmonization, Completion-year and observed firm covariates]
  evidence_refs: [E1, E2, E3, E4]
method_transfer: null
readiness_blockers:
- Recover exact firm event dates, ownership classification dates and portfolio formation rules before numerical reproduction.
- Establish lawful CSMAR/WIND access and harmonized annual reports; no public replication package was inspected.
- Support counterfactual ownership-group trends and selection assumptions for the proposed outcome; legal grounding does not certify exogeneity.
- Trace consolidation and parent-to-listed-firm transfers before interpreting operating or employment growth as net economic development.
---

## Institutional Background

Chinese A-share companies had both tradable and nontradable shares with
different transfer rights. State ownership was often concentrated in the latter,
but privately held nontradable shares existed too. Liao, Liu and Wang study
the removal of that divide, arguing that the prospect of deeper privatization
changes state-agent incentives [E1, reported claim]. Their title does not mean
every SOE became privately owned.

## What Changed

The pilot notice was signed29 April2005; its SZSE page is dated30 April,
which is also the date used in the paper [E2, verified; E1, reported claim].
September management measures replaced the pilot notices with a general
procedure. Both require negotiated plans and two shareholder voting thresholds
[E2/E3, verified]. The pilot's administrative selection is not a randomized
rollout, and a paper pooling completers does not identify its separate effect.

Conversion grants a route to future exchange trading, not immediate free sale.
The September measures impose12 months of restrictions from implementation
and further sale caps on original holders above5% [E3, verified]. The official
rules also separate exchange procedures from required state-asset approvals;
the paper's shorthand about final CSRC approval should not become a universal
firm-level assignment rule.

## Implementation and Assignment

The application uses1032 nonfinancial2005-2007 completers, including633 SOEs
and399 non-SOEs. State control can arise through voting and control rights,
not only majority equity ownership [E1, reported claim]. A fresh study needs
historical controllers and firm implementation dates. Proposal, vote, registered
conversion, release from restrictions and actual sales answer different questions.

The non-SOE comparison also experiences conversion. The authors construct
5x5 non-SOE size-industry portfolios, with size-market-to-book portfolios as an
alternative, and subtract matched median changes from SOE changes. Table5
defines revenue/profit growth from values three years before and after reform,
normalized by the earlier value [E1, reported claim]. Medians across firms are
not permission to substitute a firm's three-year moving average.

## Why This Creates Empirical Variation

The useful contrast is whether SOEs respond differently to a shared tradability
change. The authors interpret the difference as an additional privatization
channel, including incentives and asset injection [E1, reported claim]. This
interpretation needs common counterfactual changes after matching. The legal
documents establish the conversion mechanism, not that ownership-group
differences are causally attributable to it [analytical inference].

## Identification Risks

Negotiations, completion selection and state control can correlate with future
performance. Portfolio matching does not remove all such differences. The
three-year horizons overlap the financial crisis, and ownership groups need
not react identically [analytical inference]. Quantile regression describes
heterogeneity; it does not repair assignment endogeneity.

Accounting and organizational boundaries are equally substantive. The authors
manually harmonize older operating accounts because Chinese GAAP changed
in January2007 and use CPI-adjusted revenue/profit, not nominal growth.
Their investment proxy combines gross fixed-property and intangible-asset
changes relative to operating revenue; it is not a direct count of new plants.
They caution that asset injection can move workers from a parent
into the listed company [E1, reported claim]. More recorded employment is not
necessarily new employment; larger revenue is not necessarily organic growth.

## Data Requirements

Firm IDs join reform records, annual reports and historical share/control
structure. Preserve date meanings, pre-event definitions and portfolio
membership. The2002-2010 envelope follows mechanically from2005-2007 events
plus/minus three years; it does not certify a balanced panel [analytical
inference]. CSMAR/WIND access and exact coding remain reproduction conditions.
Daily stock returns and factor construction are unnecessary for the core
operating-outcome contrast. Data access and asset reconstruction belong in the
companion data repository, linked through the DOI rather than copied here.

## Evidence Notes

Published methods and tables, not the abstract, support this application.
Official pilot and management texts ground the institutional mechanism while
preserving their procedural transition. The serving object is negotiated
tradability conversion with ownership exposure; generic SOE restructuring,
decentralization or later actual ownership sales are not additional records
of the same event. No restricted dataset, copyrighted paper or replication
result has been deposited or claimed.
