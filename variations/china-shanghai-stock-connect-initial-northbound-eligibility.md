---
schema_version: 2
id: china-shanghai-stock-connect-initial-northbound-eligibility
name: Shanghai2014 Stock Connect Initial Northbound Eligibility and Launch Confirmation
aliases:
- Shanghai Stock Connect initial A-share eligibility
- 2014沪股通初始纳入资格
status: grounded
provenance:
  task_id: task-c01c354b428e
scope:
  country: China
  regions: [mainland China, Shanghai-listed A-shares]
  domains: [finance, investment, firm-behavior]
  variation_type: event-shock
  knowledge_role: china-variation
  china_relevance: Mainland-listed A-shares receive differentiated access to investors trading through Hong Kong; the recorded application studies those A-share prices, not Hong Kong stock outcomes.
identity:
  instrument: Initial Shanghai Stock Connect northbound stock eligibility, used around the November10,2014 confirmation of the launch date.
  authority: CSRC and Hong Kong SFC approve the link; SSE, SEHK, ChinaClear and HKSCC implement trading and clearing.
  legal_identifiers: [中国证券监督管理委员会、香港证券及期货事务监察委员会联合公告（2014年4月10日）, 中国证券监督管理委员会、香港证券及期货事务监察委员会联合公告（2014年11月10日）, 上证发〔2014〕60号, 上海证券交易所沪港通试点办法]
  implementation_regime: Initial2014 northbound Shanghai pilot. Southbound Hong Kong stocks, Shenzhen2016 eligibility, later index-driven entries and subsequent scope/quota reforms are outside this case's empirical boundary.
  assignment_mechanism: Initial inclusion through SSE180/SSE380 constituent status or Shanghai A/H dual listing, subject to original exclusions and the announced eligible list. Stocks are selected by market characteristics rather than randomized.
  parent: null
  related_variations: []
timeline:
  announcement: '2014-04-10'
  effective: '2014-11-17'
  implementation_start: '2014-11-17'
  implementation_end: null
  local_timing: April10 approval in principle; September26 SSE pilot rules effective on publication; November10 final launch confirmation is the paper's event day; November17 trading begins. No treatment is assigned to actual foreign trades before launch.
  anticipation: The broad eligibility rule was public in April and detailed exchange rules in September. The November event resolves launch uncertainty, not first-ever knowledge of the program; the paper also acknowledges early market reactions.
  last_verified: '2026-10-04'
assignment:
  unit: Shanghai-listed A-share security in the initial eligibility regime; outcomes are stock-event observations built from dated return series.
  treated: Initial northbound-eligible Shanghai A-shares; the paper retains440 eligible stocks with valid matched controls.
  comparison_pool: Unconnected mainland A-shares from Shanghai and Shenzhen, selected by the paper's propensity matching; not Hong Kong shares or all mainland firms.
  rule: Article16 includes SSE180 and SSE380 constituents and SSE-listed A-shares of A/H companies. Risk-alert-board securities, foreign-currency B-shares and other SSE-designated special cases are excluded. Article19 makes list-entry and exit effective at the times announced by the SEHK securities trading service company.
  intensity: Eligibility is a binary access/announcement contrast, not realized holdings or an equal stock-level cash inflow. Initial northbound net-buy quotas were13billionRMB daily and300billionRMB aggregate, constraining total access rather than defining a firm-size cutoff.
  exemptions:
  - Original Article16 excludes ST,*ST and delisting-period securities on the risk-alert board, B-shares and designated special circumstances.
  - Article24 allows sales but not new purchases after removal where the security remains SSE-listed; sell-only status is not buy eligibility.
  - The500,000RMB mainland individual-investor threshold concerns southbound participation, not this northbound stock treatment.
  compliance: Eligibility permits access through prescribed broker/order-routing and clearing arrangements. Buy acceptance depends on quotas and operational rules; foreign holding limits and issuer disclosure obligations continue to apply. Eligibility does not establish participation by each investor or actual purchases of each stock.
  exposure_construction: >
    Obtain the initial2014 eligible roster with its announcement/effective
    vintage, preserve six-digit mainland security codes together with exchange,
    and link it to dated A-share prices and issuer accounting IDs. Set CONNECT=1
    for initially eligible Shanghai stocks and0 for the unconnected A-share
    comparison pool. Validate roster exceptions against historical index,
    A/H and risk-alert status if reconstructing instead of obtaining the list.
    Do not backfill2014 from current eligible stocks or code later entry as
    initial treatment. Anchor the paper's event time to November10 on the
    mainland trading calendar, retaining November17 as the trading launch.
    For its application estimate a logit on SIZE,BM,ROA,Shanghai beta and total
    volatility, then nearest-neighbor match without replacement and caliper0.20.
    The paper reports568 eligible,519 data-valid and440 matched treated stocks;
    controls include77 Shanghai and363 Shenzhen stocks. The roster and match
    have not been independently reconstructed here.
  required_identifiers: [security_code, exchange, trading_date, issuer_id, eligibility_vintage]
  spillovers: Marketwide reform news, domestic portfolio reallocation and expected future inclusion can affect unconnected stocks. A/H issuers already have another investor-access channel; they are not identical to A-only issuers.
research_compatibility:
  outcome_domains: [Announcement abnormal returns, Trading turnover, Return volatility, Financial-market integration]
  affected_populations: [Mainland A-share issuers and their investors]
  mechanism_channels: [Expected investor demand, Speculative trading, Risk sharing, Information and disclosure, Investor access]
  best_for: [Differential short-window A-share revaluation around launch confirmation with dated initial eligibility and a credible matched comparison.]
  not_good_for:
  - Treating any foreign-ownership increase as randomly assigned by eligibility.
  - A nationwide average reform effect from a before-after comparison with no cross-sectional contrast.
  - Annual firm innovation or growth effects presented as established by this asset-pricing paper.
  - Combining Shanghai2014 and Shenzhen2016 without resolving their separate eligibility rules and event clocks.
design:
  claim_type: reduced-form
  affordances: [Dated launch confirmation, Cross-stock eligibility contrast, Pre-event market and accounting histories]
  candidate_designs: [Matched cross-sectional announcement event study, Eligibility-by-predetermined-beta interaction]
  identifying_variation: Initial eligible versus propensity-matched unconnected A-shares around November10,2014; beta interactions examine differential price sensitivity within that contrast.
  primary_strategy: Equation1 regresses announcement CAR on CONNECT and controls; Equation2 adds CONNECT times Shanghai beta and the beta main effect. Equations3-4 use normalized turnover and volatility changes instead of CAR. These are not an annual staggered DID or an eligibility RD.
  estimand: Conditional eligible-minus-matched-unconnected announcement revaluation, and its slope difference with respect to pre-event Shanghai beta. A pure demand or speculation effect requires separating other reform channels and selection.
  treatment_variable: Binary initial CONNECT and, for the heterogeneity specification, CONNECT multiplied by Shanghai market beta.
  comparison_logic: Match eligible Shanghai stocks to unconnected Shanghai/Shenzhen A-shares with similar observed characteristics; estimate differential announcement responses, not eligible-stock returns alone.
  estimation_notes: Main sample440pairs/880stocks; nearest-neighbor matching without replacement, caliper0.20. Tables3-7 report industry-clustered robust errors. CAR windows use trading days(-1,+1),(-2,+2),(-3,+3). Market-model CAR estimates coefficients on a250-day pre-event window, requires at least30 valid return days, and leaves a30-day gap before the event window. SIZE is October2014 market capitalization; beta and liquidity variables use November2013-October2014; BM,ROA andLEV use2013 accounts. Appendix definitions must take precedence over a generic October matching description.
  assumptions:
  - Absent launch-confirmation news, matched groups would have comparable abnormal returns conditional on benchmarks and observed characteristics.
  - No other simultaneous news differentially affects eligible stocks or high-beta eligible stocks in the same event window.
  - Initial roster selection, missing data and unmatched-stock exclusion do not generate the attributed announcement contrast.
  - Portfolio spillovers and differing April-November expectations are understood when interpreting the comparator and estimand.
  diagnostics:
  - Inspect pre-event differential returns, April-November run-up and alternative windows; do not equate insignificant tests with random selection.
  - Show match balance, common support and exclusions; the79 unmatched eligible stocks are larger and have higher book-to-market in the paper.
  - Examine exchange-specific shocks and A/H exclusions; most matched controls are Shenzhen stocks.
  - Test beta estimation excluding April-October2014 and baseline turnover/volatility using March2014, as reported in Sections5.5-5.6.
  - Assess common-event and cross-stock dependence rather than assuming industry clustering resolves every inference concern.
threats:
- type: eligibility_selection_and_match_support
  basis: documented
  condition: Index membership and A/H status select stocks;79 data-valid eligible stocks fail the main caliper match. Covariate balance cannot eliminate unobserved selection or extend results to excluded stocks.
  evidence_refs: [E1, E4]
  possible_diagnostics: [Inspect common support and exclusions, Report Shanghai-only controls and exchange sensitivity, Distinguish matched-population estimand]
- type: anticipation_and_event_clock
  basis: documented
  condition: April approval and September rules preceded November confirmation. Paper Section5.7 acknowledges early reactions in both groups; November10 is neither initial policy revelation nor November17 realized trading.
  evidence_refs: [E1, E2, E3, E4]
  possible_diagnostics: [Plot run-up returns, Separate announcement and launch clocks, Use pre-April beta/baselines and alternative windows]
- type: multiple_channels_and_issuer_obligations
  basis: documented
  condition: Access can change demand, risk sharing and information; November10 SSE notice70 also specifies eligible issuers' disclosure and shareholder-management obligations. Eligibility alone does not isolate a pure foreign-capital-demand channel.
  evidence_refs: [E4, E5]
  possible_diagnostics: [Separate reduced-form access from mechanism claims, Examine cash-flow and risk-sharing alternatives, Avoid an exclusion-restriction claim from eligibility alone]
- type: control_spillovers_and_common_event_dependence
  basis: inferred
  condition: Unconnected stocks may react to reform news and domestic reallocation. An event shared by many stocks creates dependence not guaranteed to vanish under industry-clustered errors.
  evidence_refs: [E3, E4]
  possible_diagnostics: [Inspect comparator reactions and exchange exposure, Use event-appropriate dependence sensitivity, Check A/H sensitivity]
empirical_requirements:
  contract_version: 1
  population: Initially eligible Shanghai A-shares and mainland unconnected A-shares with pre-event return/accounting data and overlap for matching.
  observation_unit: stock-event
  geography_level: mainland listed security and exchange, not issuer locality
  time_start: 2013
  time_end: 2014
  minimum_frequency: daily
  minimum_pre_periods: 30
  minimum_post_periods: 3
  required_fields:
  - Initial2014 eligible roster and dated buy/sell-only status; historical SSE180/SSE380,A/H,risk-alert and exception flags if independently reconstructing eligibility.
  - Exchange-qualified security code, stable issuer-accounting crosswalk, mainland trading calendar, adjusted daily returns and trading/suspension histories.
  - Chosen abnormal-return benchmark; market-model CAR needs a250-trading-day estimation span,30-day gap and at least30 valid returns, not just30 calendar days before announcement.
  - Matching covariates with their actual vintages; twelve-month daily histories for beta,total/idiosyncratic volatility,turnover and illiquidity;2013 accounts and October2014 capitalization.
  - Trading value, share volume and historical free-float shares for turnover/liquidity applications;5-minute returns are additionally required for the volatility application, not baseline CAR.
  - Industry classification for the paper's clustering and exchange identity for comparison sensitivity.
  required_identifiers: [security_code, exchange, trading_date, issuer_id, eligibility_vintage]
  treatment_key: [security_code, exchange, eligibility_vintage]
  treatment_source: Original2014 SSE rules define eligibility; Article19 designates the SEHK trading service company's dated list as operational authority. Recover the launch-vintage list from exchange archives or a documented historical provider, then reconcile to the paper's reported568 initial stocks.
  measurement_risks:
  - The current HKEX page shows September2026 changes and current buy/sell versus sell-only lists; it is not inspected evidence of every2014 eligible issuer. No historical568-row roster or executable replication was acquired here.
  - CSMAR access, adjustment conventions, missing-return handling, accounting merges and the exact realized propensity matches must be verified in a new implementation.
  - Exchange-qualified stock codes are not geography identifiers; joining to city outcomes needs a separate issuer-location and aggregation design not used in this paper.
evidence:
- id: E1
  source_type: policy-document
  citation: SSE, original2014 上海证券交易所沪港通试点办法, issued with 上证发〔2014〕60号.
  url: https://www.sse.com.cn/aboutus/mediacenter/hotandd/c/c_20150912_3988783.shtml
  date: '2014-09-26'
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, identity.implementation_regime, identity.assignment_mechanism, timeline.local_timing, assignment.unit, assignment.rule, assignment.exemptions, assignment.compliance, assignment.exposure_construction, empirical_requirements.treatment_source]
  verification_status: verified
  access_level: official-document
  locator: Original publication preamble and Articles16-24,38-49 inspected2026-10-04; excludes later revised eligibility. Article19 establishes list/effective-date authority, not the recovered2014 roster.
- id: E2
  source_type: policy-document
  citation: CSRC and SFC, joint announcement approving Stock Connect in principle.
  url: https://apps.sfc.hk/edistributionWeb/api/news/list-content?lang=EN&refNo=14PR41
  date: '2014-04-10'
  supports: [identity.authority, timeline.announcement, timeline.anticipation, assignment.rule, assignment.intensity, assignment.exemptions]
  verification_status: verified
  access_level: official-document
  locator: Opening approval, SectionIII(c)-(e) and final preparation/launch paragraphs inspected2026-10-04. Proposed access, quotas and southbound investor threshold; not realized capital flows.
- id: E3
  source_type: policy-document
  citation: CSRC and SFC, final launch joint announcement.
  url: https://apps.sfc.hk/edistributionWeb/api/news/list-content?lang=EN&refNo=14PR136
  date: '2014-11-10'
  supports: [identity.instrument, timeline.effective, timeline.implementation_start, timeline.local_timing, assignment.compliance]
  verification_status: verified
  access_level: official-document
  locator: Entire joint announcement inspected2026-10-04; opening approval and November17 commencement, finalized arrangements and preparation since April10. Does not supply stock-level roster or demand estimates.
- id: E4
  source_type: paper
  citation: Liu, Clark, Shujing Wang and K.C. John Wei. JBF126(2021),106102, published article.
  url: https://eng.pbcsf.tsinghua.edu.cn/__local/0/98/51/0E581842B130DF4BF1F09F6E843_E0FE23E6_109117.pdf?e=.pdf
  date: 2021
  supports: [assignment.treated, assignment.comparison_pool, assignment.exposure_construction, assignment.spillovers, timeline.anticipation, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.required_fields, empirical_requirements.measurement_risks, design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year, design_applications.population, design_applications.data_used, design_applications.treatment_encoding, design_applications.comparison, design_applications.empirical_design]
  verification_status: reported
  access_level: full-text
  locator: Printedpp3-9 Sections2,4.1-4.2 and Tables1-4; pp11-13 Equations2-4/Tables5-7; p18 Sections5.4-5.5/Table13; pp21-23 Table15,Section5.7,Section6 and variable appendix inspected in memory2026-10-04. No separate Internet Appendix inspection, roster reconstruction or code execution; PDF text rather than visual verification.
- id: E5
  source_type: implementation-document
  citation: SSE 上证发〔2014〕70号, 关于加强沪港通业务中上海证券交易所上市公司信息披露工作及相关事项的通知.
  url: https://www.sse.com.cn/lawandrules/sselawsrules/repeal/rules/c/c_20141110_10776215.shtml
  date: '2014-11-10'
  supports: [assignment.compliance, research_compatibility.mechanism_channels, identity.implementation_regime]
  verification_status: verified
  access_level: official-document
  locator: Preamble and clauses1-11 inspected2026-10-04; original eligible-issuer disclosure, investor relations and voting arrangements effective at pilot launch. Archive labels later expiry; not a claim of present applicability.
- id: E6
  source_type: official-data
  citation: HKEX, View All Eligible Securities, current page.
  url: https://www.hkex.com.hk/Mutual-Market/Stock-Connect/Eligible-Stocks/View-All-Eligible-Securities?sc_lang=en
  date: '2026-09-30'
  supports: [empirical_requirements.measurement_risks]
  verification_status: verified
  access_level: official-document
  locator: Current Shanghai northbound links distinguish buy/sell and sell-only lists; page updatedSeptember30,2026 inspectedOctober4. Current page only; current spreadsheet and historical2014 rows were not inspected.
- id: E7
  source_type: paper
  citation: Publisher-deposited Crossref metadata and the published PDF title page for Liu,Wang and Wei2021.
  url: https://doi.org/10.1016/j.jbankfin.2021.106102
  date: 2021
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: reported
  access_level: metadata
  locator: Crossref works API DOI,title,authors,volume126,article106102 and May2021 issue inspected2026-10-04; institutional published PDF title page also identifies onlineMarch8,2021. Metadata only, not methods support.
design_applications:
- paper: 'Demand shock, speculative beta, and asset prices: Evidence from the Shanghai-Hong Kong Stock Connect program'
  doi: 10.1016/j.jbankfin.2021.106102
  journal: Journal of Banking and Finance
  year: 2021
  research_question: Does expected investor demand at launch confirmation revalue eligible mainland stocks, especially those with high speculative beta?
  population: Initial Shanghai northbound stocks and matched unconnected mainland A-shares;568 initially eligible,519 data-valid,440 matched treatment/control pairs.
  outcome: Announcement CARs and normalized changes in turnover and intraday return volatility.
  data_used: [Exchange eligible-stock lists, CSMAR returns and financial accounts, Exchange investor holding data, Market and factor benchmarks]
  treatment_encoding: Initial CONNECT at the November10,2014 event, plus CONNECT times pre-event Shanghai beta; turnover/volatility use(0,+10) averages relative to recent-month baselines.
  comparison: Propensity-matched unconnected A-shares;77 Shanghai and363 Shenzhen controls in the main sample.
  empirical_design: Matched stock-level event study and cross-sectional beta interactions; industry-clustered inference. Section6 Shenzhen2016 test is not part of this canonical case.
  assumptions: [Comparable conditional announcement counterfactuals, No overlapping eligible-stock-specific news, Defended anticipation and comparator interpretation]
  threats_addressed: [Reported balance and window checks, A/H exclusion, Alternative beta and turnover baselines, Cash-flow and risk-sharing alternatives, Placebo dates]
  evidence_refs: [E4, E7]
method_transfer: null
readiness_blockers:
- Obtain and verify a dated2014 initial roster or an auditable historical reconstruction; current stock lists cannot serve as treatment history. The paper's568-stock count is reported, not independently reproduced.
- Secure lawful daily/accounting data and benchmark definitions, reproduce matching and inspect code or Internet Appendix for exact implementation before claiming a replication.
- Defend event-specific counterfactuals, selection, anticipation, overlapping disclosure/access channels and common-event inference for the intended outcome. Access eligibility alone does not validate a pure-demand instrument or long-run corporate effect.
---

## Institutional Background

The April2014 joint announcement proposed mutual stock-market access while
preserving each market's trading and clearing framework [E2]. For mainland
issuers, the northbound link offered an additional route through Hong Kong
brokers. It did not make all foreign investment newly possible or turn Hong
Kong-account investors into a single nationality. The paper describes earlier
B-share and QFII channels [E4, reported claim].

## What Changed

November10 confirmed that the prepared link would start trading November17
[E3]. Initial eligibility differentiated Shanghai securities through specified
index membership and A/H listing rules [E1]. The recorded paper studies price
reactions to launch confirmation: investors can respond to expected access
before the first northbound trade occurs [E4, reported claim]. April approval,
November confirmation and November trading are therefore separate clocks,
not three independently counted variations.

## Implementation and Assignment

Article16 defines the eligible universe and exclusions; Article19 assigns
operational list and effective-date publication to the SEHK securities trading
service company [E1]. Later index changes can alter access, and removal can
leave sell-only rights [E1]. Those later changes should not be silently folded
into the initial CONNECT flag. The paper links initial eligibility to CSMAR,
then matches440 eligible stocks to440 mainland unconnected stocks using five
observed characteristics [E4, reported claim]. Neither matching nor the quota
rule makes initial index membership random.

## Why This Creates Empirical Variation

Eligible and unconnected A-shares face different expected access at a common
announcement. The paper compares their benchmark-adjusted event returns and
interacts eligibility with pre-event beta [E4, reported claim]. The useful
research object is this conditional access contrast, not an observed amount
of exogenous foreign capital. Turnover and volatility provide additional
outcomes under the same assignment. Extending to firm investment, innovation
or city growth would require a new application, appropriate data links and
defended timing and mechanisms [analytical inference].

## Identification Risks

Selection into indices, early expectations and the predominance of Shenzhen
controls complicate counterfactual interpretation [E1; E4, reported claim].
The launch-era disclosure notice also requires equal information access,
investor relations and shareholder participation for eligible issuers [E5].
Consequently a reduced-form eligibility response need not isolate demand
[analytical inference]. Section5.7 acknowledges run-up reactions in both
groups. Placebo prose must be read alongside Table13, which contains some
significant standalone CONNECT coefficients; it does not establish universal
insignificance or absence of selection [E4, reported claim].

## Data Requirements

Recover the initial eligible list with exchange-qualified security codes and
vintage, not today's list [E1; E6]. Join to the mainland trading calendar,
returns, issuer accounts and chosen benchmarks. The Appendix specifies the
market-model CAR estimation span and gap, while p8 and Section4.1 specify
covariate vintages and matching [E4, reported claim]. Five-minute returns are
needed for the intraday-volatility outcome, not every use of this case. No
restricted data or paper PDF is stored here; the companion data knowledge
repository can document acquisition and limitations through the DOI.

## Evidence Notes

Original regulator announcements and exchange rules ground identity, timing,
assignment and operational authority [E1; E2; E3]. The published institutional PDF
grounds the traceable application as reported research, not independent
replication [E4]. Its separate2016 Shenzhen application has a market-value
condition and another announcement clock; only its boundary was inspected
here. Grounded status leaves historical-roster acquisition and new causal
use conditional. No executable replication, separate Internet Appendix or
2014 stock-by-stock roster has been independently inspected.
