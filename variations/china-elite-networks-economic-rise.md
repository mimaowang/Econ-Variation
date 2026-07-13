---
schema_version: 2
id: china-elite-networks-economic-rise
name: Historical Elite Networks and Their Role in Shaping China's Post-1978 Economic Growth through Interregional Connectedness
aliases:
- Bai Jia Yang web of power China
- 精英网络 经济增长
- elite networks economic development China
- political elite connections regional growth

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - All provinces and prefectures
  domains:
  - political-economy
  - growth
  - networks
  - history
  - development
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: Variation in prefecture-level connectedness to China's national political elite network, driven by the historical
    presence of individuals from that prefecture in the Chinese Communist Party's revolutionary and early-governance networks
    (1920s–1949), which created persistent cross-prefecture differences in access to political power and economic resources
    in the post-1978 reform era
  authority: Historical patterns of CCP revolutionary recruitment and elite network formation
  legal_identifiers:
  - Historical CCP membership records
  - revolutionary base area documentation
  - post-1949 elite appointment records
  implementation_regime: The CCP elite network formed during the revolutionary period (1920s–1949) and early PRC governance
    (1949–1978); after the 1978 economic reforms, prefectures with stronger historical connections to this network received
    disproportionate economic benefits through policy favoritism, investment allocation, and infrastructure placement
  assignment_mechanism: A prefecture's connectedness to the elite network is determined by whether individuals born in that
    prefecture held senior positions in the CCP during the revolutionary and early governance periods; this is determined
    by historical revolutionary geography, not by the prefecture's post-1978 economic potential
  parent: null
  related_variations:
  - china-keju-abolition-elite-recruitment
  - china-political-connections-mortality
timeline:
  announcement: null
  effective: null
  implementation_start: 1978
  implementation_end: 2015
  local_timing: Elite network effects operate continuously throughout the reform period; connectedness is historically determined
    and changes slowly
  anticipation: Prefecture-level connectedness was determined historically before the reform era, making it exogenous to post-1978
    economic conditions
  last_verified: '2026-07-13'
assignment:
  unit: Prefecture
  treated: Prefectures with stronger historical connections to the national CCP elite network (more natives who held senior
    Party or government positions)
  comparison_pool: Prefectures with weaker or no elite network connections; within-prefecture comparison before and after
    the 1978 reforms (though all prefectures are treated after 1978, the intensity varies)
  rule: Connectedness is measured by the number and seniority of political elites historically originating from each prefecture;
    this connectedness is a stock variable determined by pre-1949 revolutionary history
  intensity: Continuous — measures of prefecture-level elite network centrality, number of Politburo members, Central Committee
    members, or provincial governors born in the prefecture
  compliance: Elite network effects operate through informal channels of influence, not formal policy mandates; the strength
    of actual resource flows may vary
  exemptions: []
  exposure_construction: Construct prefecture-level measures of historical elite connectedness (count of national-level political
    elites born in the prefecture, network centrality measures); interact with post-1978 indicator; use historical revolutionary
    geography (distance to revolutionary base areas, early CCP activity) as instruments
  required_identifiers:
  - prefecture code
  - year
  - elite connectedness measures
  - revolutionary history indicators
  spillovers: Economic benefits flowing to connected prefectures may create positive spillovers to neighboring areas through
    trade and labor market linkages; alternatively, resources may be diverted from non-connected to connected prefectures
    (zero-sum at national level)
research_compatibility:
  outcome_domains:
  - economic growth
  - GDP per capita
  - infrastructure investment
  - firm creation
  - industrial output
  - educational attainment
  - public goods
  affected_populations:
  - Residents of connected prefectures
  - residents of non-connected prefectures
  - political elites
  - local government officials
  mechanism_channels:
  - policy favoritism
  - infrastructure investment allocation
  - state-owned enterprise placement
  - educational resource allocation
  - intergovernmental transfers
  - regulatory preferences
  best_for:
  - Studying how informal elite networks affect economic development
  - understanding regional inequality in China
  - analyzing persistence of historical political structures
  not_good_for:
  - Individual-level outcomes
  - short-run fluctuations
  - identifying specific policy channels
  - cross-country comparisons
design:
  affordances:
  - historically determined elite networks predating reforms
  - cross-prefecture variation in connectedness
  - rich biographical data on political elites
  - long panel of regional economic outcomes
  candidate_designs:
  - cross-sectional and panel analysis of connectedness and growth
  - instrumental variables using revolutionary geography
  - difference-in-differences around leadership changes
  identifying_variation: Prefecture-level variation in historical elite connectedness (measured before 1978), interacted with
    the post-reform period; the key insight is that connectedness was determined by pre-1949 revolutionary history, not by
    post-1978 economic potential
  assumptions:
  - Historical elite connectedness is exogenous to post-1978 economic growth potential
  - revolutionary geography affects post-1978 outcomes only through elite networks
  - no differential pre-reform economic trends by connectedness
  diagnostics:
  - Test for pre-1978 economic differences by connectedness
  - examine whether effects concentrate after leadership changes
  - use distance to revolutionary base areas as instrument
  - test for spatial spillovers to neighboring prefectures
  primary_strategy: Panel analysis with prefecture and year fixed effects; IV using distance to revolutionary base areas;
    analysis of mechanism channels (infrastructure, SOE placement, fiscal transfers)
  estimand: The causal effect of the recorded exposure on GDP per capita, infrastructure investment, firm creation, industrial
    output, educational outcomes, conditional on the stated design assumptions.
  treatment_variable: Prefecture-level elite network centrality (count of national-level political elites born in the prefecture);
    interaction with post-1978 reform period
  comparison_logic: High-connectedness vs low-connectedness prefectures within the same province; pre-reform vs post-reform
    within prefectures
  estimation_notes: Panel analysis with prefecture and year fixed effects; IV using distance to revolutionary base areas;
    analysis of mechanism channels (infrastructure, SOE placement, fiscal transfers)
threats:
- type: omitted-geography
  basis: inferred
  condition: Prefectures that produced more revolutionary elites may have geographic characteristics (coastal access, soil
    quality, historical development) that independently promote post-1978 growth
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for geographic characteristics
  - use only revolutionary-base-area variation
  - compare prefectures with similar geography but different revolutionary histories
- type: reverse-causality
  basis: inferred
  condition: Post-1978 economic success may lead to more natives being appointed to elite positions (the network grows with
    economic importance), creating reverse causality
  evidence_refs:
  - E1
  possible_diagnostics:
  - use only pre-1978 elite measures
  - instrument with pre-1949 revolutionary history
  - test whether post-1978 elite appointments respond to economic growth
empirical_requirements:
  contract_version: 1
  population: Chinese prefectures, ~1978–2015
  observation_unit: Prefecture-year
  geography_level: Prefecture
  time_start: 1978
  time_end: 2015
  minimum_frequency: annual
  minimum_pre_periods: 5
  minimum_post_periods: 10
  required_fields:
  - prefecture code
  - year
  - GDP per capita
  - elite connectedness measures
  - geographic controls
  - revolutionary history indicators
  required_identifiers:
  - prefecture code
  - year
  treatment_key:
  - prefecture code
  - elite network centrality score
  - post-1978 indicator
  - elite × post-reform interaction
  treatment_source: Biographical database of Chinese political elites (Politburo, Central Committee, provincial leaders) with
    birthplace and career history; prefecture-level economic data from statistical yearbooks; GIS data on revolutionary base
    areas and early CCP activity
  measurement_risks:
  - elite birthplace vs actual connection (some elites may not favor their birthplace)
  - elite network measurement from incomplete biographical records
  - prefecture boundary changes over time
  - migration across prefectures
evidence:
- id: E1
  source_type: paper
  citation: 'Bai, Ying, Ruixue Jia, and David Y. Yang. 2023. "Web of Power: How Elite Networks Shaped China''s Economic Rise."
    Quarterly Journal of Economics 138 (2): 1029–1088.'
  url: https://doi.org/10.1093/qje/qjac041
  date: 2023
  supports:
  - identity
  - assignment
  - design
  - network analysis
  - regional growth analysis
  verification_status: verified
design_applications:
- paper: 'Web of Power: How Elite Networks Shaped China''s Economic Rise'
  doi: 10.1093/qje/qjac041
  journal: Quarterly Journal of Economics
  year: 2023
  research_question: How do historical elite networks affect regional economic development in China's post-1978 reform era?
  population: Chinese prefectures, 1978–2015
  outcome: GDP per capita, infrastructure investment, firm creation, industrial output, educational outcomes
  data_used:
  - Biographical database of Chinese political elites
  - Prefecture-level economic statistics
  - GIS data on revolutionary base areas
  - Historical CCP membership records
  treatment_encoding: Prefecture-level elite network centrality (count of national-level political elites born in the prefecture);
    interaction with post-1978 reform period
  comparison: High-connectedness vs low-connectedness prefectures within the same province; pre-reform vs post-reform within
    prefectures
  empirical_design: Panel analysis with prefecture and year fixed effects; IV using distance to revolutionary base areas;
    analysis of mechanism channels (infrastructure, SOE placement, fiscal transfers)
  assumptions:
  - elite connectedness historically predetermined
  - revolutionary geography is valid instrument
  - no differential pre-reform trends by connectedness level
  threats_addressed:
  - geographic confounds via controls and instruments
  - reverse causality via historical measures
  - spatial dependence via province fixed effects and spatial analysis
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
method_transfer: null
---
## Institutional Background
China's post-1978 economic miracle conceals enormous regional variation: some prefectures grew at double-digit rates for decades while others stagnated. Standard explanations (geography, policy, human capital) leave much variation unexplained. A growing literature points to political connections: prefectures whose natives held power in Beijing may have received preferential treatment in investment allocation, infrastructure placement, and regulatory decisions. [E1]

## What Changed
After 1978, economic decision-making was decentralized, giving political elites substantial discretion over resource allocation. Prefectures connected to powerful elites through birthplace ties could leverage these connections for economic advantage. The key empirical challenge is that connectedness may reflect pre-existing economic conditions — successful prefectures may produce more elites, rather than elites causing success. The paper addresses this by measuring connectedness using pre-reform elite networks rooted in revolutionary history. [E1]

## Implementation and Assignment
A prefecture's elite connectedness is measured by the number of national-level political leaders born there, with networks traced through shared revolutionary experiences. Since these networks were formed during the 1920s–1949 revolutionary period — decades before the economic reforms — they are predetermined with respect to post-1978 economic conditions. Revolutionary geography (distance to early CCP base areas) provides an instrument for connectedness. [E1]

## Why This Creates Empirical Variation
Prefectures differ dramatically in their historical connectedness to the national elite network, and this variation was largely determined before the reform era began. Comparing regions with different levels of historical connectedness, before and after the 1978 reforms, identifies the economic value of political connections in China's institutional environment. [E1; analytical inference]

## Identification Risks
Prefectures that produced revolutionary elites may have geographic or cultural characteristics that independently promote growth. The use of revolutionary-base-area distance as an instrument and extensive geographic controls helps address this concern. Additionally, post-1978 economic success may cause more natives to rise to elite positions, creating reverse causality — this is addressed by using only historically-determined measures of connectedness. [E1]

## Data Requirements
Comprehensive biographical database of Chinese political elites (national and provincial level) including birthplace, career history, and network ties. Prefecture-level economic data (GDP, investment, industry, education) from statistical yearbooks. GIS data on revolutionary base areas and early CCP activity for instrument construction. [E1]

## Evidence Notes
E1 provides systematic evidence that prefectures with stronger historical connections to the CCP elite network experienced significantly faster economic growth after 1978. The paper documents specific mechanism channels through which network connections translated into economic advantage, and uses the historical nature of network formation to address endogeneity concerns. The findings highlight the persistent influence of informal political structures on China's economic geography.
