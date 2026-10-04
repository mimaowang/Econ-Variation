---
schema_version: 2
id: china-csrc-final-ipo-review-near-miss-exporters
name: China CSRC Final-Review IPO Approval among Exporting Applicants
aliases:
- 发审委最终审核通过与未通过的出口企业比较
- China IPO final-review near misses
status: grounded
provenance:
  task_id: task-eb432f797bac
scope:
  country: China
  regions: [Mainland manufacturing exporters that reached CSRC IPO final-review meetings]
  domains: [trade, corporate-finance, firm-dynamics, development-economics]
  variation_type: other
  knowledge_role: china-variation
  china_relevance: >
    The historical Chinese approval system made a final CSRC review-meeting
    decision consequential for domestic IPO applicants. Gong, Li, Sun and Wei
    compare mainland manufacturing exporters that passed this final review with
    exporters rejected at the same stage and link their decisions to customs
    transactions. The empirical exposure is a firm's review outcome, not the
    decision to apply, the initial application date, or an automatic IPO listing.
identity:
  instrument: Final public-offering application review by the CSRC issuance examination committee under the pre-registration approval regime
  authority: China Securities Regulatory Commission and its issuance examination committee (发审委)
  legal_identifiers:
  - CSRC Order No. 31, 中国证券监督管理委员会发行审核委员会办法, effective 2006-05-09; amended in 2009 and 2017
  - CSRC Order No. 134, 2017 revision of the committee rules, effective on publication
  implementation_regime: >
    Applicants first enter an intensive screening process; firms reaching the
    ordinary public-offering review meeting face a seven-member committee and
    a five-vote passage rule. The committee returns a review result and the CSRC
    subsequently decides whether to approve issuance. Follow-up review or
    suspension can intervene before a listing. The paper studies committee
    approval as its treatment, not a legal guarantee of immediate equity proceeds.
  assignment_mechanism: >
    After self-selection into an IPO application and earlier screening, the final
    committee judges each application. The empirical contrast is approved versus
    rejected manufacturers that reached final meetings in comparable review-year
    cohorts. The result is not random: judgments can reflect unobserved expected
    profitability, governance and export prospects; the paper excludes some
    profit/revenue-related rejections in a restricted comparison.
  parent: null
  related_variations: []
timeline:
  announcement: null
  effective: null
  implementation_start: 2006
  implementation_end: 2016
  local_timing: >
    These dates bound the paper's relevant pre-registration review and customs
    observation era, not the lifespan of the committee system. Event time is each
    firm's final review meeting year; approved firms may list later. The 2023
    nationwide registration reform does not retroactively change historical
    treatment; registration pilots started earlier on specific boards.
  anticipation: Application, prescreening and prospectus preparation precede the meeting, so investment and export plans may change before the recorded approval decision.
  last_verified: '2026-10-02'
assignment:
  unit: IPO-applicant manufacturing firm at its final CSRC review meeting
  treated: Firm whose public-offering application passed the final committee review
  comparison_pool: Firm whose application reached the same final-review stage but was rejected, compared within review meeting year; a restricted analysis removes rejection reasons tied to future revenue or profitability
  rule: >
    Use the final meeting's public-offering vote/result, not filing, eventual
    listing, IPO proceeds or all applicants. Under the inspected CSRC ordinary
    procedure seven members vote and at least five affirmative votes pass;
    subsequent CSRC authorization is a separate decision.
  intensity: Binary committee passage; realized listing, amount raised and issuance delay are downstream or compliance variables, not treatment assignment.
  exemptions:
  - Earlier withdrawn applicants and applications never reaching the final meeting are outside this paper's near-miss comparison.
  - Registered offerings on later pilot boards and the post-2023 registration regime require separate institutional handling.
  compliance: Passing committee review does not prove that every firm promptly obtained the same amount of public equity; investigate later authorization, delay, withdrawal and listing.
  exposure_construction: >
    Recover applicant legal identity, board, final meeting date, vote outcome and
    rejection clauses from the historical review records; join these firms to
    annual Chinese customs-export records. Define event time by review year,
    keep approvals and rejections within that risk set, and reproduce the
    paper's restricted sample excluding revenue/profitability-related rejections.
  required_identifiers: [Applicant legal name and registration identifier, Review meeting date/result, Board, Rejection clause, Customs firm identifier, Export year]
  spillovers: IPO outcomes may affect competitors, supply-chain partners or the distribution of scarce investor funds; applicant firms can reapply after rejection.
research_compatibility:
  outcome_domains: [Firm exports, Product-destination market entry, Export diversification, Intangible investment]
  affected_populations: [Chinese manufacturing exporters that reach final IPO review]
  mechanism_channels: [Access to public equity, Risk-bearing capital, Intangible investment, Export-market experimentation]
  best_for:
  - Contrasting export paths after final-stage IPO approval versus a near-miss rejection among already screened applicants
  not_good_for:
  - Treating committee approval as randomly assigned or applying the estimate to ordinary nonapplicant firms
  - Treating approval, CSRC issuance authorization, actual listing and cash proceeds as the same event
design:
  claim_type: reduced-form
  affordances: [Final-stage near-miss comparison, Review-cohort event time, Rejection-clause restricted sample]
  candidate_designs: [Cohort-based firm-year difference-in-differences/event study]
  identifying_variation: >
    Firms on both sides passed earlier IPO screening and appeared before the final
    committee; the meeting's approval outcome changes the chance of subsequent
    public equity access. Compared with all firms or all applicants, this narrows
    selection, but final-stage votes remain judgmental and potentially related
    to otherwise unobserved export prospects.
  primary_strategy: >
    Compare annual exports of approved and rejected manufacturing exporters
    within final-review-year cohorts. The author presentation specifies firm,
    review-cohort-by-year, HS2-sector-by-year and board-by-year effects, with
    event-time indicators for four pre- and six post-meeting years; the published
    abstract also confirms a cohort-based DID and restricted rejection screen.
  estimand: Conditional difference in post-review export trajectories for approved versus final-stage rejected applicant exporters, not an average effect for all potential IPO candidates
  treatment_variable: Indicator that the applicant passed the final CSRC committee review, interacted with post-review or event time
  comparison_logic: Approved and rejected applicants reaching the same meeting-year risk set; remove rejections citing forward-looking profit/revenue problems and examine pre-review export balance and trends.
  estimation_notes: >
    The inspected author slides give 2000-2016 for customs outcomes and 2000-2020
    for the broader Wind review database, but do not alone establish the final
    paper's exact IPO-cohort endpoints or all firm-join rules. Do not infer a full
    six-year post-window for every cohort. The reported export response is an
    application result, not a fixed property of approval for other outcomes.
  assumptions:
  - Absent approval, approved and restricted rejected firms would have followed comparable export trajectories conditional on review cohort, sector and board.
  - Remaining rejection reasons are not proxies for export-relevant unobserved weakness or different expected product-market opportunities.
  - Pre-meeting investment and differential survival or customs matching do not account for the apparent post-review divergence.
  diagnostics: [Pre-review export trends, Rejection-clause exclusions, Applicant balance, Actual issuance and listing delays, IPO suspension sensitivity, Reapplication and customs-link attrition]
threats:
- type: Endogenous committee judgment
  basis: documented
  condition: The committee evaluates substantive applicant qualities; rejections mentioning future revenue or profitability can directly predict export outcomes, and excluding those clauses does not prove the remaining vote is random.
  evidence_refs: [E1, E2, E4]
  possible_diagnostics: [Reproduce clause exclusions, Compare pre-review exports and planned fundraising, Inspect remaining rejection text and trends]
- type: Approval versus realized equity
  basis: documented
  condition: A passing committee vote precedes separate CSRC authorization and possible post-meeting review; an approval indicator is not cash received or a guaranteed listing.
  evidence_refs: [E1]
  possible_diagnostics: [Track authorization, listing date, proceeds and withdrawals separately]
- type: Selected population and linkage
  basis: inferred
  condition: IPO applicants that survive prescreening and match to customs data are a small selected set; results need not transport to startups, nonexporters, or all manufacturers.
  evidence_refs: [E2]
  possible_diagnostics: [Report application and customs-match attrition, Compare applicant and exporter coverage]
empirical_requirements:
  contract_version: 1
  population: Chinese manufacturing exporters whose IPO applications reached a final CSRC review meeting during the historical approval regime
  observation_unit: Applicant firm-year, with optional firm-destination-product-year export outcomes
  geography_level: Mainland firm, matched to national customs records
  time_start: 2000
  time_end: 2016
  minimum_frequency: Annual outcomes and dated review-meeting decisions
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields: [Final committee outcome and date, Board, Rejection reasons, Firm annual export value, Destination-product export markets, Customs applicant join, Actual listing or authorization status where available]
  required_identifiers: [Applicant identity, Review meeting identifier and year, Board, Customs firm identity, Firm-year]
  treatment_key: [Applicant identity, Final review meeting year, Committee pass or fail]
  treatment_source: Historical CSRC committee results and rejection records linked to Wind IPO Examination Database, then matched to Chinese Customs Trade Statistics
  measurement_risks: [Name changes and corporate restructuring in customs joins, Missing or selectively published rejection clauses, Suspended IPO periods, Different meeting and listing dates, Later registration boards mixed with approval-system observations]
evidence:
- id: E1
  source_type: policy-document
  citation: CSRC Order No. 31, 中国证券监督管理委员会发行审核委员会办法, effective 2006-05-09, official CSRC text; 2009 and 2017 amendments existed.
  url: https://www.csrc.gov.cn/csrc/c100028/c1002945/content.shtml
  date: '2006-05-09'
  supports: [identity.instrument, identity.authority, identity.implementation_regime, identity.assignment_mechanism, timeline.implementation_start, assignment.rule, assignment.compliance, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: Articles 3, 19-23, 27-32 on committee vote, seven-member/five-vote ordinary procedure, publication of result and separate CSRC authorization.
- id: E2
  source_type: scholarship
  citation: Gong, Robin Kaiji, Yao Amber Li, Stephen Teng Sun and Shang-Jin Wei, author presentation, International Seminar on Trade, World Bank, May 2025.
  url: https://thedocs.worldbank.org/en/doc/6216a61c882dd66395f98067e707107a-0050022025/related/S2-2-sides-ISoT-RobinKaijiGong.pdf
  date: '2025-05'
  supports: [scope.china_relevance, identity.assignment_mechanism, timeline.local_timing, assignment.treated, assignment.comparison_pool, assignment.exposure_construction, design.identifying_variation, design.primary_strategy, design.estimation_notes, empirical_requirements.time_start, empirical_requirements.time_end, design_applications.data_used, design_applications.treatment_encoding, design_applications.empirical_design]
  verification_status: verified
  access_level: full-text
  locator: Presentation pp.15-26 (committee process, Wind/customs data, cohort specification, restricted-sample rationale); pp.27-30 balance and export event-study plots; pp.73-82 sample and robustness tables. This is an author slide deck, not the final article or a replication archive.
- id: E3
  source_type: policy-document
  citation: CSRC, 关于修改《中国证券监督管理委员会发行审核委员会办法》的决定, Order No. 134, 2017 revision, official regional CSRC republication.
  url: https://www.csrc.gov.cn/heilongjiang/c105404/c1268891/content.shtml
  date: '2017-07-07'
  supports: [identity.legal_identifiers, identity.implementation_regime, assignment.rule]
  verification_status: verified
  access_level: official-document
  locator: Amendment text and republished rules, especially articles 3 and 28-31. Context for rule continuity; not evidence that the paper includes 2017 cohorts.
- id: E4
  source_type: paper
  citation: 'Gong, Robin Kaiji, Yao Amber Li, Stephen Teng Sun and Shang-Jin Wei. 2026. Equity Financing and Exports: Evidence from IPO Approvals in China. Journal of International Economics 162:104292. DOI 10.1016/j.jinteco.2026.104292.'
  url: https://doi.org/10.1016/j.jinteco.2026.104292
  date: '2026-08'
  supports: [design_applications.doi, design_applications.journal, design_applications.year, design_applications.research_question, design_applications.outcome]
  verification_status: reported
  access_level: abstract
  locator: Publisher-indexed article abstract and introduction, and CityUHK publication metadata (online 2026-06-13); published full text/appendix not independently inspected.
- id: E5
  source_type: policy-document
  citation: CSRC, nationwide registration-rule publication, 2023-02-17.
  url: https://www.csrc.gov.cn/csrc/c100028/c7123213/content.shtml
  date: '2023-02-17'
  supports: [timeline.local_timing, assignment.exemptions]
  verification_status: verified
  access_level: official-document
  locator: Opening paragraphs announcing nationwide registration and effective date; not a statement that every board retained approval rules until this day.
design_applications:
- paper: 'Equity Financing and Exports: Evidence from IPO Approvals in China'
  doi: 10.1016/j.jinteco.2026.104292
  journal: Journal of International Economics
  year: 2026
  research_question: Does final-stage IPO approval change the subsequent exports of Chinese manufacturing applicants relative to near-miss rejections?
  population: Mainland manufacturing exporters reaching a CSRC final review meeting, linked to annual customs records
  outcome: Annual export value and product-destination extensive margin
  data_used: [Wind IPO Examination Database and committee meeting records, Chinese Customs Trade Statistics, restricted rejection-clause coding]
  treatment_encoding: Final committee approval versus rejection in the review year; restricted analysis excludes forward-looking revenue/profitability rejections
  comparison: Same review-meeting-year approved and final-stage rejected exporting applicants
  empirical_design: Cohort-based firm-year DID and event study with review-cohort-year, sector-year and board-year effects
  assumptions: [Conditional parallel export trends, Rejection-clause filter addresses prognostic selection, Credible applicant-to-customs linkage]
  threats_addressed: [Pre-review export balance, Restricted rejection reasons, Board and sector effects, IPO suspension sensitivity]
  evidence_refs: [E2, E4]
method_transfer: null
readiness_blockers:
- Inspect the 2026 published full text or current NBER manuscript before claiming exact final-version IPO cohort years, exclusions, firm-to-customs matching algorithm or published coefficient replication.
- Obtain meeting-level vote/result, rejection-clause and post-meeting listing records before treating a new firm's exposure as directly constructible; Wind and customs microdata access was not verified.
---

## Institutional Background

For the paper's historical setting, Chinese firms seeking a public offering entered an approval process that screened applicants before a final CSRC committee meeting. The ordinary public-offering committee vote required five affirmative votes among seven members [E1]. The regulator, not the vote itself, made the later formal issuance-authorization decision; a passing vote therefore should not be relabeled realized equity finance [E1]. Subsequent registration reforms, eventually nationwide in 2023, are outside this paper's historical comparison [E5].

## What Changed

The variation is firm-specific final-review passage or rejection inside an ongoing institution, not a policy launch on a single calendar date. Both sides applied and survived earlier screening. What differs is the meeting outcome and hence the prospect of listing and raising public equity. The authors' question is whether that approval changes firms' export expansion, especially entry into new product-destination markets [E2; E4, reported publication description].

## Implementation and Assignment

The paper uses the committee meeting year as event time, maps its pass/fail result to applicant identity, and links those firms to customs-export histories [E2]. Rejected applicants are meaningful near misses only among firms that reached the final meeting; withdrawn or early-rejected applications are not equivalent controls. Revenue- or profitability-related rejection reasons may forecast exports, so the paper excludes such rejections for a restricted comparison [E2]. Committee members exercised judgment, so this is not a lottery or a clean 5-vote regression discontinuity: the available materials do not establish a running variable or near-threshold vote sample.

## Why This Creates Empirical Variation

A final pass substantially changes expected access to public equity after similar earlier screening. The author presentation specifies a cohort-based event study that compares approved and rejected exporters around their respective review meetings [E2]. The published abstract reports larger subsequent exports, primarily through more destination-product markets [E4, reported claim]. Those estimates apply to the selected near-miss population and depend on parallel untreated export paths; they are not a universal effect of IPOs for all Chinese firms.

## Identification Risks

The committee may have information about future sales and profitability not observed by the researcher. Removing explicit profit/revenue rejections narrows but cannot eliminate that concern [E2]. Applicants may change strategy during prescreening, rejected firms may reapply, and approved firms may list with different delays or proceeds [E1; analytical inference]. Board-level rule changes, IPO suspensions, and firm-to-customs matching can also affect cohort comparability. Pre-event balance and trends are diagnostics, not proof of random assignment.

## Data Requirements

Implementation requires dated CSRC final-meeting outcomes and rejection clauses, stable applicant identities, board and review cohort, and an auditable join to customs exporter-year and product-destination transactions. The inspected presentation identifies Wind review data for 2000-2020 and customs transactions for 2000-2016 [E2]. Those are source coverage dates, not a claim that every review cohort contributes equal pre/post years. The exact final-paper cohort selection and join algorithm remain a specific blocked reproduction step, not a detail to guess.

## Evidence Notes

The primary CSRC rule verifies the committee and separate issuance decision [E1]; the 2017 revision confirms rule continuity but not the paper's sample endpoint [E3]. The author-hosted conference presentation verifies the empirical comparison and data architecture [E2]. Publisher and university metadata confirm the 2026 JIE identity, while the final typeset article and its appendix were not fully inspected [E4]. Grounded status denotes a usable, source-traceable institutional and research case with explicit replication conditions; it does not certify a random vote, actual financing of every approved firm, or access to restricted applicant and customs microdata.
