# Top-5 China regional and urban variation coverage

This is the working map for the collection campaign requested by the project owner. It is a map of what has been searched and decided, not a claim that a journal's prestige makes a design credible. The object to collect is the variation a paper actually uses: the institutional change or assignment rule, the unit and timing it reaches, and the comparison that makes a research design possible.

## What belongs in this campaign

The journal set is the American Economic Review, Econometrica, Journal of Political Economy, Quarterly Journal of Economics, and Review of Economic Studies. The time window is all publication years available in the journal indexes, with a coverage date recorded for each sweep. A paper belongs in the campaign when China is part of the institution, sample, historical setting, or exposure, and when the paper studies a geographic, regional, urban, infrastructure, migration, land, housing, environmental, labor-market, or other place-based mechanism. A paper may be retained even if its title does not say “China”; the institutional section and design determine the decision.

The campaign is about reusable variation, not about collecting every China paper. A descriptive or purely structural paper can be logged as a skip or method lead when it does not provide an assignment or exposure that a researcher could encode. A non-China paper is retained only in the separate `transferable-method` lane when its identification construction is genuinely useful for a Chinese application. A China paper that merely mentions Chinese data without a recoverable treatment, comparison, or exposure is not promoted to a canonical variation.

## How an agent should work

Start with one journal and one bounded source inventory. Use the journal's own archive or search, Crossref/EconPapers metadata, and a second independent lane such as references, citations, or subject indexes. Search both direct China terms (China, Chinese, province, county, city names) and regional/urban design terms (urban, regional, transport, market access, migration, land, housing, pollution, infrastructure, local government). These terms are recall aids, not evidence. Inspect the paper or an accessible working-paper version before deciding whether the variation is real.

Each identified source receives one durable decision: `candidate` if the variation looks recoverable but needs resolution, `skip` if it is outside scope or has no usable assignment, or `blocked` if the paper or institutional source cannot be inspected. A retained source gets its own screen task and then a linked resolve/ground task. The screen task never writes a canonical record. Uncertainty stays in the candidate ledger; only a grounded or design-documented record enters `variations/`.

When two papers use the same policy, do not create two records merely because the outcomes differ. First ask whether the institution, assignment mechanism, and treatment encoding are the same. Keep one variation with multiple design applications when they are the same; split when the policy, exposure construction, or primary assignment mechanism differs. This is especially important for China infrastructure and policy waves, where a national plan, a local implementation rule, and an instrument can look similar but imply different estimands.

## When the campaign is complete

“Complete” means complete relative to a dated, auditable search boundary, not that no future paper can ever appear. For each of the five journals, the inventory must record the archive/index endpoints searched, query date, publication-year coverage, and the disposition of every China regional/urban lead returned by the two discovery lanes. The campaign can close only after:

1. the journal archive/metadata sweep and the independent citation or subject sweep have both been reviewed;
2. every retained source is canonical, queued as a candidate with a documented next step, or explicitly blocked/skipped with a reason;
3. duplicate policies and split cases have been reconciled; and
4. a repeat search produces no new unreviewed source in that journal's covered years.

The agent should then write a short coverage note naming the remaining blind spots (for example, inaccessible backfiles or ambiguous working-paper versions). A new publication or a materially better index reopens only the affected journal lane; it does not silently change the meaning of “complete.”

## Journal lanes

| Journal | Primary archive/index | Independent recall lane | Status |
|---|---|---|---|
| American Economic Review | AEA archive + Crossref ISSN `0002-8282` | EconPapers/IDEAS and citation snowball | audited through 2026-08-11; repeat search found no new unreviewed source |
| Econometrica | Wiley archive + Crossref ISSN `0012-9682` | EconPapers/IDEAS and citation snowball | audited through 2026-08-11; repeat search found no new unreviewed source |
| Journal of Political Economy | University of Chicago archive + Crossref ISSN `0022-3808` | EconPapers/IDEAS and citation snowball | audited through 2026-08-11; repeat search found no new unreviewed source |
| Quarterly Journal of Economics | Oxford Academic archive + Crossref ISSN `0033-5533` | `sources/qje-china-discovery.md` plus citation snowball | audited through 2026-08-11; repeat search found no new unreviewed source |
| Review of Economic Studies | Oxford Academic archive + Crossref ISSN `0034-6527` | EconPapers/IDEAS and citation snowball | audited through 2026-08-11; repeat search found no new unreviewed source |

The records already in `variations/` are seed coverage only. They are useful for de-duplication and query expansion, but they do not by themselves certify that a journal lane is complete. The queue and this map should move together: a journal is not marked complete merely because several familiar papers have been recorded.

## AER discovery snapshot: 2026-08-10

The AEA archive's China search and issue pages were used as the primary recall lane, then individual article pages and DOI metadata were checked. The search returns many China papers that are descriptive, structural, or published in another AEA journal; those are not silently treated as AER variation. The following AER sources were retained for one-source-per-task screen:

| DOI | Source | Initial reason for screen |
|---|---|---|
| `10.1257/aer.20201283` | Cao & Chen, “Rebel on the Canal” (2022) | Grand Canal abandonment creates a county-level trade-access break and a clear regional comparison. |
| `10.1257/aer.101.5.2081` | Wang, “State Misallocation and Housing Prices” (2011) | China’s housing privatization is a place-based urban housing regime whose assignment and timing need reconstruction. |
| `10.1257/aer.20181249` | Martinez-Bravo et al., “The Rise and Fall of Local Elections” (2022) | Staggered village-election exposure is directly regional and may reconcile or correct the legacy village-election record. |
| `10.1257/000282802762024575` | Jacoby, Li & Rozelle, “Hazards of Expropriation” (2002) | Village land reallocation creates plot-level tenure insecurity; screen must decide whether this is a recoverable institutional variation or an observational exposure. |
| `10.1257/000282802762024566` | Shiue, “Transport Costs and the Geography of Arbitrage” (2002) | Historical transport-cost and market-integration variation is regional, but its assignment is not assumed to be causal until inspected. |
| `10.1257/aer.90.2.389` | McElroy & Yang, “Carrots and Sticks” (2000) | China population-policy incentives and penalties may contain regional policy variation; the short paper requires a conservative screen. |
| `10.1257/aer.20211455` | Chen et al., “Regulating Conglomerates” (2025) | A national energy program has sharp size-based exposure and network spillovers; screen will test whether its variation is materially regional/urban or belongs outside this campaign. |

The archive also surfaced AER papers already represented by canonical records (for example, the Huai River heating case, send-down education, and migrants/firms). These were reconciled by DOI rather than duplicated. AEA Papers and Proceedings and American Economic Journal records surfaced in the same AEA search (including carbon-trading, tail-pipe standards, and e-commerce) remain outside this Top-5 lane; they can be collected in a later, separately named campaign. At the 2026-08-11 boundary, all retained AER sources are canonical or have explicit blocked/skip outcomes, and the repeat AEA/Crossref search found no new unreviewed China regional/urban source.

### AER independent metadata and subject pass: 2026-08-11

The Crossref ISSN inventory (`0002-8282`, query terms China/Chinese and regional/urban/migration/land/infrastructure) was compared with the AEA article pages and an independent subject search. Near-scope returns not already in the screen table were dispositioned as follows: Rozelle, Taylor & deBrauw (`10.1257/aer.89.2.287`) and Zhao (`10.1257/aer.89.2.281`) describe rural-to-urban migration and remittances but provide no policy or geographic assignment; Auffhammer & Wolfram (`10.1257/aer.104.5.575`) is province-level descriptive demand evidence; Cheremukhin et al. (`10.1257/aer.20220249`) is a national political-cycle model rather than a regional treatment; Ebenstein et al. (`10.1257/aer.p20151094`) uses city first differences for pollution and life expectancy without an assignment; Tombe & Zhu (`10.1257/aer.20150811`) is a quantitative trade/migration model; and de Janvry et al. (`10.1257/aer.20211207`) is a firm/worker experiment without a place-based treatment. These are logged as scope skips, not hidden leads. Crossref hits already represented by the canonical DOI set (including migrants/firms, media bias, SOE decentralization, and citizen appeals) were reconciled without duplication. After these targeted dispositions, a repeat AEA/Crossref query on the same date returned no additional unreviewed AER source with a recoverable China regional/urban assignment beyond the screen table.

## Econometrica discovery snapshot: 2026-08-10

The Wiley/Econometric Society records and an independent metadata/citation search identified four sources needing an explicit screen. Two directly China-based designs are already canonical and are therefore not duplicated: the abolition of the civil service exam (`10.3982/ECTA13448`) and the Chinese R&D/innovation paper (`10.3982/ECTA18586`). The new screen queue is:

| DOI | Source | Initial reason for screen |
|---|---|---|
| `10.3982/ECTA20146` | Qin, Strömberg & Wu, “Social Media and Collective Action in China” (2024) | A city panel uses changing cross-city social-media connections to study the geographic spread of protests and strikes; resolve must separate a network exposure from a policy assignment. |
| `10.3982/ECTA19699` | Gai et al., “Rural Pensions, Labor Reallocation, and Aggregate Income” (2025) | The rural pension rollout affects labor allocation and migration across rural and urban places; screen must recover the actual rollout and comparison rather than infer it from the structural counterfactual. |
| `10.3982/ECTA13758` | Caliendo, Dvorkin & Parro, “Trade and Labor Market Dynamics” (2019) | The China trade shock is a global-China exposure that varies across local labor markets; screen must decide whether it belongs in the `global-china-variation` lane rather than the direct-China lane. |
| `10.3982/ECTA16598` | Adamopoulos et al., “Misallocation, Selection, and Productivity” (2022) | Chinese village/farm land institutions are central, but the paper may be measurement and structural counterfactual rather than an inspectable quasi-experimental variation. |
| `10.3982/ECTA19367` | Borusyak & Hull, “Nonrandom Exposure to Exogenous Shocks” (2023) | The paper's empirical application uses 2007–2016 Chinese high-speed-rail construction to estimate prefecture market-access effects; the screen must keep the China HSR variation distinct from the NTHS highway record and reconstruct the recentered exposure. |

The structural paper is not promoted merely because it uses Chinese regional data. At the 2026-08-11 boundary, the retained screens, the independent subject/citation pass, and the targeted repeat search are closed; the remaining blocked candidates preserve their evidence gaps in the ledger.

### Econometrica independent metadata and subject pass: 2026-08-11

The Crossref ISSN inventory (`0012-9682`) and an independent EconPapers/subject search first returned the four sources above; a targeted repeat search then surfaced Borusyak & Hull (`10.3982/ECTA19367`). Its screen and resolve tasks created `variations/china-high-speed-rail-recentered-market-access.md`, a separate grounded HSR market-access record with the observed, expected, and recentered exposures kept distinct. The remaining China hit is a historical statistics handbook (`10.2307/1909254`), not an empirical assignment. The five retained screens now have explicit outcomes: rural pensions and social media remain blocked candidates; the China-trade structural exposure and misallocation measurement paper are skipped for this narrower regional/urban variation lane; and the HSR application is grounded with line-level archive and replication crosswalk blockers preserved. A repeat Wiley/Crossref search after that disposition produced no additional unreviewed China regional/urban source.

## Journal of Political Economy discovery snapshot: 2026-08-10

The University of Chicago archive and Crossref title/subject recall were checked, with a second pass through the JPE issue pages and citation-facing metadata. Existing canonical records were matched by DOI before adding work. Four borderline or potentially useful sources were retained for one-source-per-task screen; the screen is deliberately allowed to end in an explicit skip.

| DOI | Source | Initial reason for screen |
|---|---|---|
| `10.1086/734873` | Wang & Yang, “Policy Experimentation in China: The Political Economy of Policy Learning” (2025) | China’s local policy experiments may provide a reusable regional assignment, but the screen must recover the experiment-selection rule and treatment geography rather than treating every pilot as causal variation. |
| `10.1086/733420` | Alessandria et al., “Trade Policy Dynamics: Evidence from 60 Years of US-China Trade” (2025) | China-linked trade-policy exposure is plausibly regional through industry employment, but the paper is primarily structural and may belong only in the global-China lane. |
| `10.1086/738344` | Rodríguez-Clare, Ulate & Vásquez, “Trade with Nominal Rigidities: Understanding the Unemployment and Welfare Effects of the China Shock” (2026) | The China shock is mapped to US states and migration; screen must determine whether the paper contributes an inspectable exposure or only a model counterfactual. |
| `10.1086/726237` | “Investing with the Government: A Field Experiment in China” (2024) | A randomized China field experiment is a useful boundary case, but it is retained only if its design has a material place-based component. |
| `10.1086/739256` | Heckman & Zhou, “A Study of the Microdynamics of Early-Childhood Learning” (2026) | China REACH uses a paired-village randomized home-visiting intervention in rural Gansu; the canonical record separates the JPE treated-arm skill dynamics from the linked treatment-effect application. |

The archive also surfaced already represented JPE sources, including land reform and sex selection (`10.1086/701030`), competitive saving (`10.1086/660887`), clean-air willingness to pay (`10.1086/705554`), and the send-down movement (`10.1086/650315`); those are reconciliation targets, not duplicate records. Macro, tax-evasion, and purely structural China papers remain outside the regional/urban variation lane unless the screen finds a recoverable geographic exposure. At the 2026-08-11 boundary, the retained screens, independent citation/subject pass, and repeat Chicago/Crossref search are closed with no new unreviewed source.

### JPE independent metadata and subject pass: 2026-08-11

The Crossref ISSN inventory (`0022-3808`) was checked against the University of Chicago archive, issue pages, and an independent title/subject search. Besides the four original screens, the targeted archive search found Heckman & Zhou (`10.1086/739256`), whose China REACH paper documents a paired-village randomized home-visiting intervention; its resolve task created `china-reach-rural-home-visiting-rct` with the JPE dynamic-skill estimand kept separate from the linked treatment-effect application. Other recent China hits were either already canonical (land reform, competitive saving, clean-air willingness to pay, and send-down) or structural/non-place papers (including `10.1086/733420`, which was skipped as a US–China trade-policy model). Historical China book notices and macro papers were excluded from the regional/urban lane. After this disposition, the repeat Chicago/Crossref query returned no additional unreviewed JPE source with a recoverable China geographic assignment.

## Quarterly Journal of Economics discovery snapshot: 2026-08-10

The existing QJE seed inventory was re-read against Oxford Academic issue/article pages and a new search for China, city, rural, migration, and regional mechanisms. Existing records (including Ctrip work-from-home, land security and mobility, anti-corruption and land markets, water-quality monitoring, and the social-ties study) were treated as DOI reconciliation targets. Four sources were retained for explicit screens because their abstracts expose either a local-government/rural institutional comparison or a randomized intervention inside a Chinese city:

| DOI | Source | Initial reason for screen |
|---|---|---|
| `10.1162/003355398555748` | Jin & Qian, “Public Versus Private Ownership of Firms: Evidence from Rural China” (1998) | Provincial and local-government differences in township-village enterprise ownership may be useful, but the screen must separate descriptive correlations from an assignment that can be encoded. |
| `10.1162/003355398555658` | Che & Qian, “Insecure Property Rights and Government Ownership of Firms” (1998) | Local-government ownership is tied to China’s transition and place-specific public-good/revenue institutions; the paper may instead be a theory-led interpretation without a standalone shock. |
| `10.2307/2118432` | Groves et al., “Autonomy and Incentives in Chinese State Enterprises” (1994) | State-enterprise autonomy and incentive reform are China institutional changes, but the screen must verify whether there is timing or geographic contrast rather than a firm-level reform description. |
| `10.1093/qje/qjx049` | Cai & Szeidl, “Interfirm Relationships and Business Performance” (2018) | A randomized business-network intervention was run in Nanchang and stratified across 26 subregions; this is a strong city-boundary candidate, subject to reconstructing treatment, peer, and subregion assignment. |

The seed list also contains method-transfer and descriptive leads; those remain visible in `sources/qje-china-discovery.md` but are not silently promoted into this narrower campaign. At the 2026-08-11 boundary, the QJE screens, second citation/subject pass, and repeat Oxford/Crossref search are reconciled with explicit skip, blocked, or canonical outcomes.

### QJE independent metadata and subject pass: 2026-08-11

The Crossref ISSN inventory (`0033-5533`) was checked against Oxford issue/article pages, the QJE China source sweep, and an independent citation/subject search. `10.1093/qje/qjaf035` (Investor Memory and Biased Beliefs) was reviewed as a China field survey with randomized recall prompts, but it has no regional or urban treatment and is recorded as a scope skip. `10.1093/qje/qjae041` (U.S.–China trade-war model) and `10.1093/qje/qjad003` (Fractured-Land Hypothesis, with China as a comparative example) are structural or cross-country applications without a China regional assignment and are also skipped. `10.1093/qje/qjaa024` was reconciled to the existing water-monitoring records; the four older screens have explicit skip or blocked/candidate outcomes. A repeat Oxford/Crossref query on the same date returned no additional unreviewed QJE source with a recoverable China regional/urban assignment.

## Review of Economic Studies discovery snapshot: 2026-08-10

The Oxford Academic archive, advance-article list, recent issue pages, and an independent title/abstract recall were checked. The search is especially important for this lane because a new 2026 article uses a China-wide industrial siting design that would be invisible in older seed files. Existing canonical records were reconciled by DOI before adding work. Four sources were retained for explicit screens:

| DOI | Source | Initial reason for screen |
|---|---|---|
| `10.1093/restud/rdag078` | Heblich, Seror, Xu & Zylberberg, “Large Industrial Clusters in the Long Run: Evidence from Million-Rouble Plants in China” (2026) | Soviet-allied plant siting and allied/enemy airbase geography supply a county-level exposure with a clear control group; screen must recover the siting rule, plant boundary, and long-run outcome joins. |
| `10.1093/restud/rdag047` | “Technology Transfer and Early Industrial Development: Evidence from the Sino-Soviet Alliance” (2026) | Delayed Soviet transfers create three plant-level treatment states; screen must decide whether this is the same underlying 156 Projects variation as the cluster paper or a distinct treatment/estimand that should be split. |
| `10.1093/restud/rdaf011` | Barwick et al., “Industrial Policy Implementation: Empirical Evidence from China’s Shipbuilding Industry” (2025) | A China industrial-policy implementation paper may contain local/firm exposure distinct from the legacy shipbuilding subsidy record; screen will reconcile policy identity before any new record. |
| `10.1093/restud/rdac020` | Galle, Rodríguez-Clare & Yi, “Slicing the Pie: Quantifying the Aggregate and Distributional Effects of Trade” (2023) | The rise of China is mapped to US commuting zones; this is a boundary screen for the global-China lane, not presumed direct-China variation. |
| `10.1093/restud/rdaf029` | Brandt, Kambourov & Storesletten, “Barriers to Entry and Regional Economic Growth in China” (2026) | The official abstract reports prefecture-level regional convergence and entry barriers linked to state-sector size; screen must determine whether the geographic variation is an inspectable assignment or only a structural wedge/counterfactual. |

The archive also surfaced the already canonical property-rights land reform (`10.1093/restud/rdaa072`), VAT reform (`10.1093/restud/rdac027`), Great Famine (`10.1093/restud/rdv016`), highway expansion, firm dynamics, and other China records. Courtroom gender and other China-data papers without a geographic assignment are logged as scope skips rather than variation. At the 2026-08-11 boundary, the second advance-article/JEL search, independent citation/subject pass, retained screens, and repeat Oxford/Crossref search are reconciled with no additional unreviewed ReStud source.

### ReStud independent metadata and subject pass: 2026-08-11

The Crossref ISSN inventory (`0034-6527`) was compared with Oxford advance articles/issues, EconPapers/IDEAS citation metadata, and a second title/subject search. The pass added `10.1093/restud/rdac056` (AI firms and prefecture data-rich public-security contracts); its screen and resolve are explicitly `blocked` because the paper's constructed surveillance-capacity comparison is not an independently verified policy assignment. A targeted Oxford search then surfaced Au & Henderson, `10.1111/j.1467-937X.2006.00387.x` (“Are Chinese Cities Too Small?”); its screen is `skipped` because it estimates an urban agglomeration model on cross-sectional city data and treats hukou restrictions as a national context, not a dated city assignment. `10.1093/restud/rdv008` (quid pro quo technology transfer) is a structural global policy model without a regional treatment, while `10.1093/restud/rdy016` (pollution and health-insurance demand) is a daily behavioral study with no China regional assignment; both are scope skips. The two 2026 plant papers and `rdaf029` have explicit blocked outcomes, and the shipbuilding/trade screens are reconciled. A repeat Oxford/Crossref query after these dispositions returned no further unreviewed ReStud source with a recoverable China regional/urban assignment.

## Campaign closure note: 2026-08-11

The five journal lanes are closed relative to the dated archive and metadata boundary described above. Each lane has a primary journal/archive sweep, an independent metadata or subject/citation sweep, a repeat search, DOI-level reconciliation against existing canonical records, and a durable disposition for every retained lead. The serving layer gained two records during the final pass: the JPE China REACH paired-village intervention and the Econometrica HSR recentered market-access application. The remaining high-value leads are not silently discarded: blocked candidates retain their source, reason, and next evidence step in `state/candidates.jsonl`, while explicit skips record why the paper is outside this regional/urban variation boundary.

This closure is not a claim that future publications or inaccessible backfiles do not exist. It is an auditable stopping point for the five journals and the search lanes named in this file. A later agent should reopen only the affected journal lane when a new archive endpoint, full text, replication archive, or materially better index supplies new evidence; it should not manufacture a second canonical record from a title or abstract alone.
