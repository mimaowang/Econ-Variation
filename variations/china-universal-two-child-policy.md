---
schema_version: 2
id: china-universal-two-child-policy
name: China's Universal Two-Child Policy (2016)
aliases:
- Universal Two-Child Policy
- 全面两孩政策
- 普遍二孩政策
- UTC policy
- Two-Child Policy
status: grounded
provenance:
  task_id: task-a35333f94eeb
scope:
  country: China
  regions:
  - National
  domains:
  - demography
  - family-economics
  - labor-economics
  - public-policy
  - fertility
  variation_type: single-date-reform
  knowledge_role: china-variation
  china_relevance: >
    The variation is a nationwide Chinese population-policy reform that abruptly
    relaxed birth quotas from the one-child and "single-only" two-child regimes to
    a universal two-child rule. It assigns treatment by legal eligibility and is
    widely used to study fertility, household behavior, labor supply, and human
    capital in China.
identity:
  instrument: >
    Nationwide relaxation of birth quotas allowing all married couples to have up
    to two children, replacing the prior regime in which a second child was
    permitted only for narrowly eligible couples.
  authority: >
    Standing Committee of the National People's Congress (NPC); State Council;
    National Health and Family Planning Commission; provincial people's
    congresses.
  legal_identifiers:
  - 全国人民代表大会常务委员会关于修改《中华人民共和国人口与计划生育法》的决定（主席令第四十一号）
  - Decision of the Standing Committee of the National People's Congress on Amending
    the Population and Family Planning Law of the People's Republic of China
    (Presidential Order No. 41)
  - 中华人民共和国人口与计划生育法（2015年修正）
  implementation_regime: >
    The NPC Standing Committee amended the national Population and Family Planning
    Law on 27 December 2015; the amendment took effect on 1 January 2016. Article 18
    was revised to state that the state advocates that every married couple have
    two children, while leaving detailed implementing measures to provincial-level
    people's congresses. The prior "single-only" two-child policy, which allowed a
    second child only when at least one spouse was an only child, was superseded
    for all couples nationwide. [E1]
  assignment_mechanism: >
    Treatment is legal eligibility to bear a second child under the new universal
    rule but not under the preceding Single-Only Two-Child Policy. In the primary
    research application, a woman is coded as treated if she was eligible for a
    second child under the UTC policy but not under the Single-Only policy as of
    December 2015. Counties are treated according to the local share of such newly
    eligible women. [E1; E2, reported claim]
  parent: null
  related_variations:
  - china-one-child-policy-twins-iv
timeline:
  announcement: '2015-10-29'
  effective: '2016-01-01'
  implementation_start: 2016
  implementation_end: null
  local_timing: >
    The Fifth Plenary Session of the 18th CPC Central Committee announced the policy
    direction on 29 October 2015. The NPC Standing Committee passed the legal
    amendment on 27 December 2015 and the presidential order was promulgated the
    same day. The revised law became effective nationwide on 1 January 2016.
    Provincial-level people's congresses subsequently issued local implementing
    regulations and birth-registration procedures. [E1]
  anticipation: >
    The policy was announced in October 2015 and legally enacted in December 2015,
    so some anticipation in late 2015 was possible. Conception-to-birth lags mean
    that fertility responses observed from 2016 onward are the relevant post-period
    outcomes, and empirical designs typically exclude births conceived before the
    legal change. [E2, reported claim]
  last_verified: '2026-07-14'
assignment:
  unit: woman-year or county-year
  treated: >
    Married women of fertile age who became legally eligible for a second child
    under the universal rule but would not have been eligible under the
    Single-Only Two-Child Policy; alternatively, counties with a higher share of
    such newly eligible women.
  comparison_pool: >
    Women who were already eligible for a second child under the Single-Only
    policy and therefore unaffected by the further relaxation; women before the
    policy change; counties with a low share of newly eligible women.
  rule: >
    At the individual level, code a woman as treated from 2016 onward if she had
    one living child in December 2015 and neither she nor her husband qualified
    for a second birth under the Single-Only rules. At the county level, use the
    share of women meeting that definition as a continuous treatment intensity.
    [E2, reported claim]
  intensity: >
    Binary eligibility at the individual level; continuous share of newly eligible
    women at the county level.
  exemptions:
  - Couples already permitted more than one child under ethnic-minority or rural
    exceptions that predated the Single-Only reform
  - Women beyond fertile age
  - Unmarried women and couples not seeking a second child
  compliance: >
    Legal compliance is high because the reform removed a binding quota rather
    than imposing an obligation. Behavioral uptake is partial: only women who
    desired at least two children responded, and aggregate fertility rose by a
    modest amount. [E2, reported claim]
  exposure_construction: >
    Construct a woman-level eligibility indicator from survey questions on parity,
    spouse-only-child status, and hukou/ethnic rules in force before 2016. Merge
    with annual birth histories to form a woman-year panel. For county-level
    analysis, compute the 2015 share of newly eligible women using a pre-reform
    fertility survey and merge with county population data. [E2, reported claim]
  required_identifiers:
  - woman identifier
  - calendar year
  - parity
  - birth history
  - county code
  - husband only-child status
  - urban/rural hukou status
  - ethnicity
  spillovers: >
    General-equilibrium effects may shift childcare markets, maternity-leave
    norms, and grandparent child-care supply. Fertility responses by treated
    women can affect untreated households through social interactions or local
    service prices.
research_compatibility:
  outcome_domains:
  - fertility and birth timing
  - household consumption and savings
  - female labor supply
  - maternal health
  - child human capital
  - marriage and divorce
  - fertility desires and intentions
  affected_populations:
  - married women of fertile age
  - couples with one child
  - only children and their spouses
  - urban Han households previously constrained by the one-child rule
  - rural and ethnic-minority households with partial prior exemptions
  mechanism_channels:
  - removal of a binding legal quota
  - fertility desire heterogeneity
  - intergenerational transfers and child-care constraints
  - labor-market and career costs of childbearing
  best_for:
  - Difference-in-differences comparing newly eligible women before and after 2016
  - County-level DID using exposure share
  - Triple-difference designs interacting eligibility with fertility desire
  - Event-study designs around the January 2016 effective date
  not_good_for:
  - Estimating the effect of the one-child policy itself, which requires a different
    source of variation
  - Outcomes that cannot be linked to individual fertility histories or county
    identifiers
  - Designs that ignore the preceding Single-Only Two-Child Policy and treat all
    women as equally constrained before 2016
  - Studying the 2021 three-child policy, which is a separate reform
  - Outcomes measured only after fertility desires themselves may have adjusted
    to the new regime
design:
  claim_type: causal
  affordances:
  - Sharp nationwide policy change with a known legal effective date
  - Individual-level eligibility variation based on pre-reform family structure
  - County-level variation in treatment intensity derived from the same rule
  - Fertility-desire heterogeneity that can be used in triple-difference designs
  candidate_designs:
  - Individual-level DID with woman fixed effects and province-by-year fixed effects
  - County-level DID with county fixed effects and province-by-year fixed effects
  - Triple-difference DID using high versus low fertility desire
  - Event-study specification around the 2016 reform
  identifying_variation: >
    The abrupt expansion of second-child eligibility from the Single-Only rule to
    all couples on 1 January 2016, combined with cross-sectional differences in
    whether a woman would have been ineligible under the old rule.
  primary_strategy: >
    Difference-in-differences comparing birth outcomes of newly eligible women in
    2016-2017 to those of already-eligible women, with individual fixed effects,
    province-by-year fixed effects, and controls for age, education, ethnicity,
    work-unit type, and hukou status interacted with year dummies. [E2, reported claim]
  estimand: >
    The average effect of becoming eligible for a second child under the UTC policy
    on the number of births per eligible woman, relative to remaining under the
    Single-Only rule, conditional on parallel trends.
  treatment_variable: >
    An indicator for being newly eligible for a second child under the UTC policy,
    interacted with a post-2016 indicator; or a county's share of newly eligible
    women interacted with a post-2016 indicator.
  comparison_logic: >
    Already-eligible women provide the counterfactual trend for newly eligible
    women, under the assumption that the two groups would have followed parallel
    fertility paths absent the universal relaxation. The pre-reform period
    (2012-2015) captures common trends.
  estimation_notes: >
    Cluster standard errors at the county level. Weight regressions by survey
    sampling weights for national representativeness. Exclude births conceived
    before the reform to avoid contamination by the Single-Only policy. Verify
    pre-trends in an event-study specification. [E2, reported claim]
  assumptions:
  - Parallel trends in fertility outcomes between newly eligible and already-eligible
    women absent the UTC reform
  - The Single-Only Two-Child Policy did not itself create differential fertility
    responses that confound the post-2016 period
  - Fertility desire is measured before or independently of the policy response
  - No other national reform coincided with January 2016 and differentially affected
    newly eligible women
  diagnostics:
  - Event-study plots for pre-trends and dynamic treatment effects
  - Robustness to excluding women whose first birth occurred in 2014-2015
  - Robustness to using pregnancies rather than live births as the outcome
  - Sensitivity to county-by-year fixed effects
  - Heterogeneity analysis by stated fertility desire
  - County-level analysis using 2020 census fertility rates
threats:
- type: confounding-by-prior-relaxation
  basis: inferred
  condition: >
    The 2013 Single-Only Two-Child Policy already relaxed quotas for some couples,
    so the UTC comparison mixes a treated group (newly eligible) with a control
    group (already eligible) that itself experienced a prior policy change.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Exclude births conceived during the Single-Only window
  - Use placebo tests with 2013-2015 as a pseudo-reform period
  - Compare effect sizes across cohorts with different prior eligibility
- type: anticipation-and-leakage
  basis: inferred
  condition: >
    The October 2015 announcement and December 2015 enactment allowed some couples
    to time conceptions around the reform, blurring the exact treatment date.
  evidence_refs:
  - E1
  - E2
  possible_diagnostics:
  - Use conception dates rather than birth dates where available
  - Drop births in the first months of 2016
  - Test for bunching in late-2015 conceptions
- type: selective-response
  basis: reported
  condition: >
    The fertility response was concentrated among women who already desired at
    least two children; women with low desired fertility showed almost no response,
    implying ITT estimates average over a highly selected subpopulation. [E2, reported claim]
  evidence_refs:
  - E2
  possible_diagnostics:
  - Report treatment-effect heterogeneity by desired fertility
  - Estimate local average treatment effects if compliance can be modelled
- type: measurement-error
  basis: inferred
  condition: >
    Live-birth histories may miss stillbirths, abortions, or short-spacing births,
    and survey-reported desired fertility may be affected by the policy itself.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Use pregnancy histories as an alternative outcome
  - Use pre-reform measures of desired fertility where possible
  - Validate age and parity against administrative records
- type: general-equilibrium-spillovers
  basis: inferred
  condition: >
    A broad fertility rebound could affect labor markets, childcare prices, and
    social norms, which in turn may influence untreated households.
  evidence_refs:
  - E2
  possible_diagnostics:
  - Estimate effects on placebo outcomes among already-eligible women
  - Control for local service-price trends
  - Test for spatial correlation across counties
empirical_requirements:
  contract_version: 1
  population: >
    Married women of fertile age in China observed before and after the January
    2016 reform, ideally with parity and spouse information.
  observation_unit: woman-year or county-year
  geography_level: county
  time_start: 2012
  time_end: 2020
  minimum_frequency: annual
  minimum_pre_periods: 3
  minimum_post_periods: 2
  required_fields:
  - number of births in year
  - parity as of December 2015
  - woman age
  - education
  - ethnicity
  - urban/rural hukou
  - work-unit type
  - husband characteristics
  - county code
  - year
  required_identifiers:
  - woman identifier
  - year
  - county code
  treatment_key:
  - woman identifier
  - year
  treatment_source: >
    Individual eligibility is constructed from the 2017 China Fertility Survey or
    similar fertility surveys with detailed birth and marital histories. County
    exposure shares can be computed from the same survey or from 2020 census
    fertility rates.
  measurement_risks:
  - Survey birth histories may underreport short-spacing or non-marital births
  - Fertility desire may be measured after the reform and thus be endogenous
  - County-level exposure is an aggregate of individual eligibility and may
    capture compositional differences
  - Local implementing regulations varied at the province level
  - The 2017 China Fertility Survey has restricted access

evidence:
- id: E1
  source_type: policy-document
  citation: >
    Standing Committee of the National People's Congress of China. 2015. "Decision
    of the Standing Committee of the National People's Congress on Amending the
    Population and Family Planning Law of the People's Republic of China"
    (Presidential Order No. 41).
  url: https://www.gov.cn/zhengce/2015-12/28/content_5029897.htm
  date: '2015-12-27'
  supports:
  - identity
  - timeline
  - assignment
  verification_status: verified
  access_level: official-document
  locator: >
    Official NPC Standing Committee decision and amended Population and Family
    Planning Law dated 27 December 2015; states that Article 18 was revised to
    advocate two children per couple, effective 1 January 2016, with provincial
    implementing measures.
- id: E2
  source_type: paper
  citation: >
    Fang, Hanming, and Chang Liu. 2026. "Desired fertility, realized fertility and
    the effects of China's Universal Two-Child Policy." Journal of Development
    Economics 182: 103796.
  url: https://doi.org/10.1016/j.jdeveco.2026.103796
  date: 2026
  supports:
  - design_applications
  - design
  - assignment
  verification_status: reported
  access_level: abstract
  locator: >
    Journal of Development Economics abstract and published article; reports a
    difference-in-differences design using the 2017 China Fertility Survey and
    2020 census county-level data, exploiting eligibility variation created by
    the UTC policy.

design_applications:
- paper: Desired fertility, realized fertility and the effects of China's Universal Two-Child Policy
  doi: 10.1016/j.jdeveco.2026.103796
  journal: Journal of Development Economics
  year: 2026
  research_question: >
    How did China's Universal Two-Child Policy affect realized fertility, and to
    what extent did fertility desires shape the response?
  population: >
    Married women aged 20-40 in China, and county-level fertile-age populations,
    observed around the 2016 reform.
  outcome: >
    Number of live births per woman (2016-2017) and county-level fertility rates
    (2016-2020).
  data_used:
  - 2017 China Fertility Survey
  - 2020 China Population Census
  - 2015 mini-census population counts
  - County-level GDP, housing price, and private-tutoring density data
  treatment_encoding: >
    Individual-level: indicator Eligible_i x Post_t, where Eligible equals one if
    the woman was eligible under UTC but not under the Single-Only Two-Child
    Policy as of December 2015, and Post equals one in 2016-2017. County-level:
    share of newly eligible women in 2015 interacted with Post_t.
  comparison: >
    Already-eligible women under the Single-Only policy and the pre-reform period
    serve as the counterfactual for newly eligible women; low-eligibility counties
    serve as the counterfactual for high-eligibility counties.
  empirical_design: >
    Difference-in-differences with individual fixed effects and province-by-year
    fixed effects; triple-difference interacting high fertility desire; county-level
    DID with county and province-by-year fixed effects; event-study specifications.
  assumptions:
  - Parallel trends between newly eligible and already-eligible women
  - Fertility desire is a stable, pre-determined characteristic or measured independently
  - County-level desired fertility reflects long-standing regional differences
  threats_addressed:
  - Pre-trends via event-study plots
  - Robustness to excluding women with first births in 2014-2015
  - Alternative outcome using pregnancies instead of live births
  - County-by-year fixed effects
  - Exclusion of ethnic minorities
  evidence_refs:
  - E2

readiness_blockers:
- >
  The full text of the JDE paper and its replication materials have not been
  inspected; design details rely on the abstract and published article summary.
- >
  Provincial implementing regulations and local birth-registration procedures
  have not been compiled into this record.
- >
  County-level exposure shares and pre-reform fertility-desire measures have not
  been extracted into a reusable dataset here.

method_transfer: null
---

## Institutional Background

From 1979 onward China restricted most couples to one child, with gradually
expanding exemptions for rural families whose first child was a girl, ethnic
minorities, and couples in which both spouses were only children. In 2013 the
"Single-Only" Two-Child Policy allowed a second child if at least one spouse was
an only child. Concerns about population aging and a shrinking labor force led
the Fifth Plenary Session of the 18th CPC Central Committee to announce a further
universal relaxation in October 2015. [E1]

## What Changed

The NPC Standing Committee amended the Population and Family Planning Law on
27 December 2015, and the revised law took effect on 1 January 2016. Article 18
was changed to advocate that every married couple have two children. Provincial
people's congresses were authorized to issue detailed implementation rules. The
change was nationwide and simultaneous, but its bite differed across households
depending on whether they had already been eligible under the 2013 Single-Only
rule. [E1]

## Implementation and Assignment

A couple is treated as newly exposed to the reform if it was allowed a second
child only after the universal rule took effect. In practice this means couples
in which neither spouse was an only child and who did not fall under other
pre-existing exemptions. The primary research design therefore compares women
who became newly eligible in 2016 with women who were already eligible before
2016, using birth histories from 2012-2017. Counties with larger shares of
newly eligible women experience a higher treatment intensity. [E1; E2, reported claim]

## Why This Creates Empirical Variation

The reform created a sharp, nationwide change in the legal right to bear a second
child. Because the pre-reform eligibility rule depended on family structure,
cross-sectional differences in only-child status generate variation in exposure
to the relaxation. Combined with the known effective date, this supports
difference-in-differences and event-study designs at both the individual and
county levels. [E1; E2, reported claim]

## Identification Risks

The 2013 Single-Only relaxation means the control group of already-eligible women
itself experienced a prior treatment, which can confound the post-2016 trend.
Anticipation of the 2016 reform may have shifted conception timing around the
effective date. Fertility responses are highly heterogeneous by desired fertility,
so average effects may not generalize. Measurement error in birth histories and
the endogeneity of reported fertility desires can bias estimated effects. Local
service markets and social norms may generate spillovers to untreated households.
[E2, reported claim]

## Data Requirements

Researchers need individual-level fertility histories with parity, spouse
only-child status, age, education, ethnicity, hukou, and work-unit information,
typically from the China Fertility Survey or large household panels such as
CFPS and CHFS. County-level analysis requires the share of newly eligible women,
which can be estimated from the 2017 China Fertility Survey or 2020 census, plus
controls for economic conditions and local service markets. [E1; E2, reported claim]

## Evidence Notes

E1 is the official NPC Standing Committee decision and the amended national law;
it verifies the legal content, effective date, and delegation to provincial
implementation. E2 is the published Journal of Development Economics article;
its design details, sample construction, and results are reported claims that
have not been independently verified from replication materials.
