# QJE China-related source sweep

Sweep goal: identify exogenous institutional variations or transferable identification methods from *Quarterly Journal of Economics* papers that are China-related and not yet represented in the repository.

Method: EconPapers/RePEc abstract search, IDEAS subject search, and web cross-check against existing `variations/*.md`. Crossref API was unavailable due to SSL errors, so bibliographic details were taken from publisher/EconPapers pages.

## Existing QJE records already in repository

| Citation | Knowledge role | File |
|---|---|---|
| Chen & Kung (2019, QJE) | china-variation | `variations/china-anti-corruption-land-market.md` |
| Bai, Jia & Yang (2023, QJE) | china-variation | `variations/china-social-ties-political-elite.md` |
| Adamopoulos et al. (2024, QJE) | china-variation | `variations/china-land-security-migration.md` |
| Qian (2008, QJE) | china-variation | `variations/china-missing-women-tea-price.md` |
| He, Wang & Zhang (2020, QJE) | china-variation | `variations/china-water-quality-monitoring-rd.md` |
| Angrist & Lavy (1999, QJE) | transferable-method | `variations/israel-maimonides-rule-class-size.md` |
| Wei & Zhang (2011, QJE) | china-variation | `variations/china-sex-ratio-competitive-savings.md` |

## New candidates (screening backlog)

| # | Citation | Tentative role | Why it may fit | Why it may be skipped |
|---|---|---|---|---|
| 1 | **Bloom, Liang, Roberts & Ying (2015, QJE)** — "Does Working from Home Work? Evidence from a Chinese Experiment" | `china-variation` | Ctrip Shanghai WFH eligibility assigned by a public draw selecting birthday parity. | **Grounded, conditional** as `variations/china-ctrip-work-from-home-experiment.md`. Original AEA trial 276 registration recovered 2026-10-03; retrospectively registered in 2017, not prospectively preregistered. |
| 2 | **Feenstra & Hanson (2005, QJE)** — "Ownership and Control in Outsourcing to China" | `china-variation` | Processing-trade ownership structures across Chinese sectors/regions. | **Resolved** as `variations/china-processing-trade-ownership-control.md`; treated as a structural `other` variation with customs-regime primary evidence. |
| 3 | **Hsieh & Klenow (2009, QJE)** — "Misallocation and Manufacturing TFP in China and India" | `transferable-method` | Canonical misallocation measurement; widely applied to Chinese plant data. | **Resolved** as `variations/hsieh-klenow-plant-misallocation-method.md`. |
| 4 | **Jin & Qian (1998, QJE)** — "Public Versus Private Ownership of Firms: Evidence from Rural China" | `china-variation` | Cross-province variation in TVE vs private ownership in rural China. | Older data; institutional assignment mechanism needs careful reconstruction. |
| 5 | **Che & Qian (1998, QJE)** — "Insecure Property Rights and Government Ownership of Firms" | `china-variation` | Property-rights shocks and government ownership in rural China. | Similar era/setting as #4; check for overlap. |
| 6 | **Groves, Hong, McMillan & Naughton (1994, QJE)** — "Autonomy and Incentives in Chinese State Enterprises" | `china-variation` | SOE autonomy reform and incentive contracts in China. | 1980s reform; assignment may be endogenous. |
| 7 | **Manova & Zhang (2012, QJE)** — "China's Exporters and Importers: Firms, Products and Trade Partners" | `global-china-variation` | Descriptive mapping of Chinese firm trade structure; useful for exposure instruments. | No exogenous shock; likely descriptive/structural. |
| 8 | **Bartling, Weber & Yao (2015, QJE)** — "Do Markets Erode Social Responsibility?" | skip | Lab experiment comparing market vs non-market allocation; includes Chinese subjects. | No Chinese institutional variation; not a China shock. |
| 9 | **Fajgelbaum & Khandelwal (2016, QJE)** — "Measuring the Unequal Gains from Trade" | `global-china-variation` / skip | Includes China welfare gains from trade; structural method. | No exogenous policy variation; structural estimation. |
| 10 | **Aghion, Burgess, Redding & Zilibotti (2008, QJE)** — "The Unequal Effects of Liberalization: Evidence from Dismantling the License Raj in India" | `transferable-method` | Staggered industrial de-licensing as a natural experiment; applicable to China's deregulation episodes. | India case; method transfer only. |
| 11 | **Donaldson & Hornbeck (2016, QJE)** — "Railroads and American Economic Growth: A Market Access Approach" | `transferable-method` | Historical U.S. railroad network as IV for market access; applicable to Chinese railway/highway infrastructure. | **Resolved** as `variations/us-railroad-market-access-method.md`. Note: the originally listed "Donaldson (2018, QJE) Railroads of the Raj" is actually AER 2018; the QJE railroad method is Donaldson & Hornbeck (2016). |
| 12 | **Donaldson & Hornbeck (2016, QJE)** — "Railroads and American Economic Growth" | `transferable-method` | Market-access instrument from railroad expansion; China railway application. | US historical setting; method transfer only. |
| 13 | **Dell (2010, Econometrica)** — "The Persistent Effects of Peru's Mining Mita" | `transferable-method` | Boundary discontinuity design; applicable to Chinese historical boundary policies. | In progress: resolving as a method-transfer record. Note: the originally listed "Dell (2010, QJE)" is actually Econometrica 2010. |
| 14 | **Ashraf & Galor (2013, QJE)** — "The 'Out of Africa' Hypothesis, Human Genetic Diversity, and Comparative Economic Development" | `transferable-method` | Genetic diversity instrument for development; China regional application. | Deep-history instrument; relevance to China needs justification. |
| 15 | **Putterman & Weil (2010, QJE)** — "Post-1500 Population Flows and the Long-Run Determinants of Economic Growth and Inequality" | `transferable-method` | Ancestry composition as instrument; China historical migration. | Long-run historical instrument; data construction heavy. |
| 16 | **Spolaore & Wacziarg (2009, QJE)** — "The Diffusion of Development" | `transferable-method` | Genetic distance to technological frontier; China regional development application. | Same concerns as #14. |
| 17 | **Nunn (2008, QJE)** — "The Long-Term Effects of Africa's Slave Trades" | `transferable-method` | Historical distance instruments; long-run development. | Africa; China application tenuous. |
| 18 | **Acemoglu, Johnson & Robinson (2001, QJE)** — "The Colonial Origins of Comparative Development" | `transferable-method` | Settler-mortality instrument for institutions; method reference. | Not China-specific. |
| 19 | **Klenow & Rodríguez-Clare (1997, QJE)** — "The Neoclassical Revival in Growth Economics" | skip | Growth accounting; no shock. | No exogenous variation. |
| 20 | **Easterly & Levine (2001, QJE)** — "What Have We Learned from a Decade of Empirical Research on Growth?" | skip | Growth synthesis; no shock. | No exogenous variation. |

## Immediate priority

The priority list below is historical. On 2026-10-03, audit task `task-52aecbc523a7`
recovered the original public AEA trial 276 history (`/trials/276/history/16533`,
DOI `10.1257/rct.276-1.0`) and re-inspected the published QJE article and author-hosted
replication script. The archive supports the Shanghai eligibility funnel, public parity
draw, 131/118 arms and December 6, 2010-August 14, 2011 intervention. Its first
registration was April 12, 2017; it is not a prospective protocol or an independent
lottery audit. The existing record, not a duplicate, now has conditional grounded
status. The audit also removes an invented November 1 announcement date, distinguishes
ITT from LATE, and narrows the default data contract to the paper's weekly performance
application. One lottery flipping birthday groups must not be represented as 249
independent draws; the separate 2021 hybrid-work experiment remains a different variation.

1. Resolve **Bloom et al. (2015)** first: the Ctrip WFH experiment offers a randomized, China-specific treatment with a well-documented assignment mechanism.
2. Then decide whether **Feenstra & Hanson (2005)** is better recorded as a `china-variation` or as a `transferable-method`.
3. Relegate purely structural/measurement papers (#3, #7, #9) to method-transfer or skip unless the user explicitly asks for them.

## Disposition update: 2026-08-11

The table above is a discovery ledger, not a live queue. The earlier immediate-priority items have already been reconciled: Bloom et al., Feenstra & Hanson, and Hsieh & Klenow are represented by the files named above; Jin & Qian, Che & Qian, and Groves et al. were screened and skipped because the papers do not expose a recoverable regional assignment under this campaign; and the Nanchang interfirm-network paper (`10.1093/qje/qjx049`) was screened and resolved as blocked because the independently inspected implementation and peer-construction records were not recoverable. The later JPE/QJE sweep also screened and skipped the Investor Memory field-survey paper (`10.1093/qje/qjaf035`), the U.S.–China trade-war structural paper (`10.1093/qje/qjae041`), and the Fractured-Land cross-country paper (`10.1093/qje/qjad003`). These outcomes live in the task and candidate ledgers; no item should be treated as “in progress” merely because its original discovery row still describes a possible fit.

For the Top-5 China regional/urban campaign, the QJE lane is audited through 2026-08-11. Future work should reopen a bounded task only when a new archive endpoint or inspectable source changes the evidence boundary; it should not promote the remaining method-transfer list into China variations by default.
