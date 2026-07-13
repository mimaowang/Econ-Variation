---
schema_version: 2
id: china-firm-media-bias-competition
name: Market Competition Reform and Newspaper Exits in China's State-Owned Media Market (1981–2011)
aliases:
- Media Bias in China
- Qin Stromberg Wu newspaper competition
- 中国媒体偏向 市场竞争

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - All provinces with newspaper markets
  domains:
  - media
  - political-economy
  - information
  - competition
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: A government reform that forced underperforming newspapers to exit or merge, combined with the expansion of
    market-oriented non-party newspapers ("commercial newspapers"), creating variation in market competition across Chinese
    cities and over time
  authority: Chinese government (newspaper restructuring and exit policies)
  legal_identifiers:
  - Newspaper restructuring regulations
  - exit/merger policies for government-owned newspapers
  implementation_regime: Between 1981 and 2011, the Chinese newspaper market shifted from purely propaganda outlets to a mixed
    market with commercial non-party newspapers competing alongside party organs; a reform forced exits of underperforming
    newspapers, creating exogenous variation in market competition
  assignment_mechanism: Variation in newspaper entry and exit across cities and over time, driven by both market forces and
    government restructuring policies; the exit reform provides a plausibly exogenous source of competition change
  parent: null
  related_variations:
  - china-media-censorship-vpn-experiment
timeline:
  implementation_start: 1981
  implementation_end: 2011
  local_timing: Newspaper entries and exits occur at different times in different cities
  announcement: null
  effective: null
  anticipation: The newspaper exit reform was not anticipated at the individual newspaper level
  last_verified: '2026-07-13'
assignment:
  unit: Newspaper-city-year
  treated: Newspaper markets after increased competition from non-party commercial newspapers or after forced exits of competing
    newspapers
  comparison_pool: Markets with less competition or pre-reform periods
  rule: Competition intensity varies with the number and type of newspapers in a city; the forced-exit reform creates exogenous
    reductions in competition
  intensity: Continuous — number of competing newspapers in a city
  exposure_construction: Code city-year-level newspaper market structure (count of party vs commercial newspapers, HHI); use
    reform-induced exits as instrument for competition change
  required_identifiers:
  - city code
  - year
  - newspaper ID
  - newspaper type (party/commercial)
  exemptions: []
  compliance: Not applicable — universal coverage
  spillovers: Changes in one newspaper's bias may affect the editorial decisions of competing newspapers in the same market
research_compatibility:
  outcome_domains:
  - media bias
  - news content
  - political coverage
  - corruption reporting
  - advertising
  - readership
  affected_populations:
  - Newspaper readers
  - journalists
  - local officials
  - advertisers
  mechanism_channels:
  - market competition
  - advertising revenue
  - reader demand
  - political control
  - self-censorship
  best_for:
  - Studying how market forces interact with political control in media markets
  - how competition affects content bias
  not_good_for:
  - Direct effects on citizen attitudes (content analysis
  - not individual-level outcomes)
design:
  affordances:
  - exogenous exits due to government restructuring
  - expansion of commercial newspapers over time
  - newspaper-level content data
  candidate_designs:
  - difference-in-differences
  - event study around newspaper exits
  - instrumental variables using reform exits
  identifying_variation: Government-mandated newspaper exits and the expansion of commercial non-party newspapers as sources
    of variation in market competition
  assumptions:
  - Reform exits are not driven by newspaper quality that independently affects bias
  - commercial newspaper entry timing is conditionally exogenous
  diagnostics:
  - Test for pre-trends in bias before exits
  - compare party vs commercial newspapers
  - distinguish demand-driven vs supply-driven bias changes
  primary_strategy: Panel analysis with city and year fixed effects; IV using government-mandated newspaper exits; analysis
    of content bias changes with competition
  estimand: The causal effect of the recorded exposure on Measures of media bias (coverage of corruption, sensitive events,
    politically favorable vs unfavorable reporting), conditional on the stated design assumptions.
  treatment_variable: City-year-level competition intensity; reform-induced newspaper exits as instrument
  comparison_logic: Higher vs lower competition markets; pre vs post exit reform
  estimation_notes: Panel analysis with city and year fixed effects; IV using government-mandated newspaper exits; analysis
    of content bias changes with competition
threats:
- type: endogenous-exits
  basis: inferred
  condition: Newspapers selected for forced exit may be systematically different from survivors; if bias affects exit probability,
    the comparison is confounded
  evidence_refs:
  - E1
  possible_diagnostics:
  - examine exit selection criteria
  - compare pre-exit characteristics
  - use only plausibly exogenous policy-driven exits
empirical_requirements:
  contract_version: 1
  population: Chinese newspapers across 120+ cities, 1981–2011
  observation_unit: Newspaper-article or newspaper-city-year
  geography_level: City
  time_start: 1981
  time_end: 2011
  minimum_frequency: annual
  minimum_pre_periods: 5
  minimum_post_periods: 5
  required_fields:
  - newspaper content (bias measures)
  - newspaper type
  - city market structure
  - exit/entry events
  - advertising revenue
  - circulation
  required_identifiers:
  - newspaper ID
  - city code
  - year
  treatment_key:
  - city code
  - year
  - competition index
  - exit reform indicator
  treatment_source: Newspaper content via text analysis; newspaper market data from government and industry sources; exit
    reform documentation
  measurement_risks:
  - content analysis measurement error
  - classifying bias systematically
  - missing informal/underground publications
evidence:
- id: E1
  source_type: paper
  citation: 'Qin, Bei, David Strömberg, and Yanhui Wu. 2018. "Media Bias in China." American Economic Review 108 (9): 2442–2476.'
  url: https://doi.org/10.1257/aer.20170947
  date: 2018
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - competition-bias analysis
  verification_status: verified
design_applications:
- paper: Media Bias in China
  doi: 10.1257/aer.20170947
  journal: American Economic Review
  year: 2018
  research_question: How does market competition affect media bias in a state-controlled media system?
  population: Chinese newspapers across 120+ cities, 1981–2011
  outcome: Measures of media bias (coverage of corruption, sensitive events, politically favorable vs unfavorable reporting)
  data_used: []
  treatment_encoding: City-year-level competition intensity; reform-induced newspaper exits as instrument
  comparison: Higher vs lower competition markets; pre vs post exit reform
  empirical_design: Panel analysis with city and year fixed effects; IV using government-mandated newspaper exits; analysis
    of content bias changes with competition
  assumptions:
  - Reform exits are exogenous to newspaper quality
  - content coding accurately reflects bias
  - market structure measured without error
  threats_addressed:
  - endogenous exits via IV
  - demand-side confounds via advertiser and reader controls
  - alternative mechanisms via content-type analysis
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
---
## Institutional Background
China's newspaper market operates under government ownership and censorship, but since the 1980s has included both traditional party organs and commercially oriented non-party newspapers. The government tolerates commercial newspapers because they generate revenue and attract readers, but maintains ultimate editorial control. A key reform forced underperforming newspapers to exit, creating exogenous variation in competition. [E1]

## What Changed
As commercial newspapers entered markets and some party organs were forced to exit, local competition intensity changed. The key question is whether more competition reduces or increases bias: competition for readers may push newspapers toward more critical, independent reporting (reader-demand channel), while competition for advertising and fear of political repercussions may push in the opposite direction. [E1]

## Why This Creates Empirical Variation
Government-mandated newspaper exits create plausibly exogenous variation in market structure. When a newspaper is forced to close, remaining newspapers face a changed competitive environment for reasons unrelated to their own editorial choices. This allows identification of the causal effect of competition on content bias. [E1; analytical inference]

## Identification Risks
Newspapers selected for forced exit may have different characteristics (including content bias) from survivors. If systematically more critical newspapers are targeted, the estimated effect of competition on bias is confounded. The paper addresses this using both cross-sectional and time-series variation. [E1]
## Implementation and Assignment

The reform created variation in newspaper market competition across cities and over time through two channels: the government-mandated exit of underperforming newspapers (removing competitors) and the entry of commercially oriented non-party newspapers (adding competitors). The exit reform provides a particularly clean source of variation because exits were determined by government policy rather than market forces.[E1]

## Data Requirements

Newspaper-level content data (text analysis of ~120 newspapers for bias measurement), city-level newspaper market structure data (entry, exit, party vs. commercial classification), advertising revenue, circulation, and readership demographics. The content analysis requires systematic coding of political bias from a large corpus of Chinese-language newspaper articles.[E1]

## Evidence Notes

E1 is the published AER article. It documents that increased competition from commercial newspapers reduced political bias in content, driven by reader demand for less biased reporting, and that government-mandated exits had the opposite effect by reducing competitive pressure.
