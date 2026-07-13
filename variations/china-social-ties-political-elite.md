---
schema_version: 2
id: china-social-ties-political-elite
name: Social Ties and the Selection of China's Political Elite
aliases:
- Politburo social ties selection
- Fisman Shi Wang Wu elite ties
- elite network selection CCP

status: contested
provenance:
  task_id: task-e9b64f33e231
scope:
  country: China
  regions:
  - Chinese Communist Party Politburo
  domains:
  - political-economy
  - institutions
  - elite-selection
  variation_type: other
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: Social ties (shared hometown and shared college alumni connections) between Politburo incumbent members and
    candidate members, creating within-group variation in the probability of candidate selection for the Politburo
  authority: Chinese Communist Party (CCP) — Politburo and Central Committee selection processes
  legal_identifiers:
  - CCP Constitution Articles governing Central Committee and Politburo selection
  implementation_regime: The selection of new Politburo members operates through an internal CCP process at each National
    Congress; the presence of social ties with incumbent members is not a formal rule but an empirically documented pattern
    that generates quasi-random variation within candidate pools
  assignment_mechanism: Within a given candidate pool for Politburo membership, connections to incumbent members are distributed
    unevenly across candidates; variation is driven by the historical distribution of hometown origins and college attendance
    among political elites
  parent: null
  related_variations:
  - china-keju-abolition-elite-recruitment
timeline:
  announcement: null
  effective: null
  implementation_start: 1992
  implementation_end: 2017
  local_timing: Politburo selections occur at each five-year National Congress of the CCP (1992, 1997, 2002, 2007, 2012, 2017)
  anticipation: Candidates cannot fully anticipate the social-tie landscape at future congresses because incumbent composition
    changes at each congress
  last_verified: '2026-07-13'
assignment:
  unit: Individual candidate for Politburo membership (CCP elite member)
  treated: Candidates who share a hometown connection or college alumni connection with at least one incumbent Politburo member
    at the time of selection
  comparison_pool: Candidates for Politburo membership who do not share social ties with incumbent members, within the same
    selection cycle
  rule: Treatment is defined by the presence of any shared tie (same birth county or same university) between a candidate
    and an incumbent full or alternate Politburo member; the study also constructs a continuous measure of the number and
    strength of ties
  intensity: Continuous — number of shared ties, number of connected incumbents, and strength-of-ties measures based on hierarchical
    closeness
  exemptions: []
  compliance: Social ties are a relational characteristic, not a policy; compliance is not applicable — the treatment is a
    measure of connectedness
  exposure_construction: For each candidate at each congress, construct indicator variables for same-county tie (candidate
    and incumbent share birth county) and same-college tie (candidate and incumbent attended same university); also construct
    count variables for number of tie-connected incumbents
  required_identifiers:
  - candidate name
  - candidate birth county
  - candidate university attended
  - incumbent members list
  - incumbent birth county
  - incumbent university attended
  spillovers: Candidates connected to the same incumbent may compete against each other; ties to one incumbent may affect
    relationships with other incumbents in factional politics
research_compatibility:
  outcome_domains:
  - elite selection
  - political promotion
  - factional politics
  - leadership transitions
  - political networks
  affected_populations:
  - CCP Central Committee members
  - Politburo candidates
  - CCP political elite
  mechanism_channels:
  - social networks
  - alumni connections
  - hometown ties
  - patronage
  - factional alignment
  best_for:
  - Studying the role of informal social networks in elite political selection
  - fixed-effects analysis within selection cycles
  - testing network-based theories of authoritarian politics
  not_good_for:
  - Causal effects of individual policy positions
  - mass-level political outcomes
  - generalizing to non-authoritarian political systems
design:
  affordances:
  - within-congress variation in candidate ties
  - fixed effects for selection cycle
  - fixed effects for candidate birth province and factional background
  - continuous tie-intensity measures
  candidate_designs:
  - linear probability model with congress fixed effects and candidate background controls
  - conditional logit with congress fixed effects
  - within-candidate variation across sequential selection rounds
  identifying_variation: Conditional on congress-year fixed effects (which absorb common shocks to all candidates in a given
    selection cycle), variation in the presence and intensity of social ties across candidates within the same candidate pool
    identifies the effect of ties on selection probability
  assumptions:
  - No unobserved candidate characteristics correlated with both ties and selection likelihood conditional on controls
  - ties are not systematically allocated to candidates based on unobserved ability
  - the distribution of hometowns and universities across incumbents is not driven by selection-cycle-specific factors
  diagnostics:
  - Compare observable characteristics of tied and non-tied candidates
  - test whether ties predict pre-selection career outcomes
  - examine sensitivity to inclusion of province and faction fixed effects
  - placebo tests with non-selection outcomes
  primary_strategy: linear probability model with congress fixed effects and candidate background controls
  estimand: The causal effect of the recorded exposure on the outcome defined by the research application, conditional on
    the stated design assumptions.
  treatment_variable: For each candidate at each congress, construct indicator variables for same-county tie (candidate and
    incumbent share birth county) and same-college tie (candidate and incumbent attended same university); also construct
    count variables for number of tie-connected incumbents
  comparison_logic: Candidates for Politburo membership who do not share social ties with incumbent members, within the same
    selection cycle
  estimation_notes: linear probability model with congress fixed effects and candidate background controls; conditional logit
    with congress fixed effects; within-candidate variation across sequential selection rounds
threats:
- type: omitted-variable
  basis: inferred
  condition: Candidates with social ties may also be more qualified or better connected through other unobserved channels
    (e.g., factional membership, work history, patronage relations) that independently affect selection
  evidence_refs:
  - E1
  possible_diagnostics:
  - Include candidate fixed effects where possible
  - control for candidate rank in prior Central Committee
  - control for factional membership
  - test robustness to alternative tie definitions
- type: reverse-causality
  basis: inferred
  condition: Incumbents may cultivate ties with promising candidates rather than ties causing selection; or selection outcomes
    may be rationalized post-hoc through social-tie narratives
  evidence_refs:
  - E1
  possible_diagnostics:
  - Use pre-determined ties from before candidates entered elite circles
  - examine ties formed during university (exogenous to later selection)
  - test timing of tie formation relative to candidate emergence
- type: measurement
  basis: documented
  condition: Social ties are measured using publicly available biographical data which may be incomplete or inaccurate; college
    ties may miss important educational connections (e.g., party school attendance) and hometown ties may be misclassified
    at the county level
  evidence_refs:
  - E1
  possible_diagnostics:
  - Cross-validate with independent biographical sources
  - test sensitivity to alternative geographic granularity (prefecture vs county)
  - examine robustness to excluding potentially misclassified ties
empirical_requirements:
  contract_version: 1
  population: Candidates for the CCP Politburo (both full and alternate members) observed at each five-year National Congress
    from 1992 to 2017, along with the incumbent Politburo members at each congress
  observation_unit: Candidate-congress (each candidate observed at each selection cycle they are in the candidate pool)
  geography_level: Individual candidate (with county and province geocoding for hometown origin; university institution for
    education)
  time_start: 1992
  time_end: 2017
  minimum_frequency: quinquennial (every five years at each Party Congress)
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - candidate name
  - candidate birth county
  - candidate university attended
  - Politburo membership status
  - selection congress year
  - incumbent member names
  - incumbent birth counties
  - incumbent universities
  required_identifiers:
  - candidate identifier
  - congress year
  - birth county code
  - institution code for university
  treatment_key:
  - candidate-congress indicator
  - same-county tie dummy
  - same-college tie dummy
  - number of connected incumbents
  - total tie count
  treatment_source: Biographical data from Baidu Baike, official CCP biographical directories, and Chinese government biographical
    databases
  measurement_risks:
  - Incomplete biographical records for some candidates
  - ambiguous county-level geographic assignments (birth vs ancestral home)
  - missing or incomplete university information
  - difficulty distinguishing multiple types of informal ties
  - changing administrative boundaries over time
evidence:
- id: E1
  source_type: paper
  citation: 'Fisman, Raymond, Jing Shi, Yongxiang Wang, and Weixing Wu. 2020. "Social Ties and the Selection of China''s Political
    Elite." American Economic Review 110 (6): 1752–1781.'
  url: https://doi.org/10.1257/aer.20180841
  date: 2020
  supports:
  - identity
  - assignment
  - design
  - threats
  - empirical_requirements
  verification_status: verified
design_applications: []
readiness_blockers:
- "Admissibility audit (task-e9b64f33e231, 2026-07-13): The paper (Fisman, Shi, Wang, Wu 2020 AER) is an observational study
  of social ties and Politburo selection. The treatment (hometown/college ties with incumbents) is an endogenous personal
  characteristic, not an externally assigned variation. The record's framing also needs correction: the paper finds a connections
  PENALTY (5-9 pp lower selection probability), not a positive selection effect. No instrument, threshold, boundary, or randomization
  is present. Kept contested as a low-priority lead; do not invest in grounding."
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
method_transfer: null
---
## Institutional Background

The Chinese Communist Party (CCP) Politburo is the highest decision-making body in China's political system. Its members are selected from the broader Central Committee at the five-yearly National Congress of the CCP. The selection process is internal and non-transparent, but substantial biographical information about members and candidates is publicly available. Informal social ties — shared hometown origins and shared university attendance — have long been understood to play a role in elite politics in China, where guanxi (relationship-based) networks are culturally and institutionally important. [E1]

## What Changed

This is not a study of an institutional reform or policy change. The paper studies the association between sharing a hometown or alma mater with an incumbent Politburo member and selection as a new member. It is an observational candidate-cycle comparison, not an externally assigned treatment. [E1, reported claim]

## Implementation and Assignment

In each selection cycle (at each National Congress from 1992 to 2017), there is a pool of candidates who are eligible for Politburo membership, typically comprising Central Committee members. Among these candidates, some share social ties with incumbent Politburo members — either by birth county or by attended university. These ties are measured using publicly available biographical data from Baidu Baike and official sources. The key identifying assumption is that, conditional on congress-year fixed effects and observable background characteristics, the distribution of ties across candidates is plausibly exogenous to selection outcomes. [E1]

## Why This Creates Empirical Variation

Variation arises from the distribution of social ties within each candidate pool at each congress. Not all candidates have ties to incumbents, and the number and strength of ties vary across candidates. Because the composition of the Politburo changes at each congress (through retirements, promotions, and demotions), the tie landscape shifts across selection cycles, providing within-candidate variation for those observed in multiple cycles. The inclusion of congress-year fixed effects removes common shocks and secular trends, isolating the within-cycle effect of ties. [E1; analytical inference]

## Identification Risks

The primary identification risk is omitted variable bias: candidates with social ties may systematically differ from those without ties in ways that independently predict selection. For example, candidates from politically important provinces or elite universities may be more qualified and also more likely to be connected. The paper addresses this through province and university fixed effects, but residual confounding from unobserved dimensions of candidate quality or factional alignment remains a concern. Reverse causality is also possible — incumbents may seek ties with promising candidates rather than ties causing selection. Additionally, publicly available biographical data may contain measurement error that attenuates estimated effects or introduces bias if non-randomly missing. [E1; analytical inference]

## Data Requirements

The analysis requires detailed biographical information for both Politburo candidates and incumbent members over multiple congress cycles (1992–2017). Data fields include name, birth county, university attended, career history, Politburo membership status at each congress, and factional or patronage relationships. The main sources are Baidu Baike entries and official CCP biographical directories. Data must be structured at the candidate-congress level, with each candidate appearing in each cycle they were in the candidate pool. [E1]

## Evidence Notes

E1 is the published American Economic Review article by Fisman, Shi, Wang, and Wu. Its abstract reports a connections penalty: hometown or college connections are associated with a 5–9 percentage-point lower probability of Politburo selection, not a positive selection effect. Because the comparison is observational and the selection process is opaque, this record is contested and must not be used as assignment-generating variation without a new admissibility audit.
