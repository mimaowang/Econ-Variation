---
schema_version: 2
id: china-arrival-young-talent-send-down
name: County Exposure to Received Send-Down Youth, 1968–1977
aliases:
- Arrival of Young Talent
- 上山下乡知青县域接收强度
- SDY rural education exposure
status: contested
provenance:
  task_id: task-9bb70167b880
scope:
  country: China
  regions:
  - Mainland rural counties; the AER core sample excludes Beijing, Tianjin, Shanghai and city-governed districts
  domains: [development-economics, education, historical-migration, human-capital]
  variation_type: continuous-exposure
  knowledge_role: china-variation
  china_relevance: >
    Urban Chinese youths were sent to mainland rural counties. The AER study
    compares recorded county reception intensity across school-age cohorts.
    The exposure is real; the sign of its schooling effect is disputed.
identity:
  instrument: >
    County totals of urban educated youths received in rural villages and
    collective farms in 1968–1977. This is not an observed county quota,
    individual teacher assignment, or the full historical movement.
  authority: >
    Mao's December 1968 instruction and central/local implementation.
    The cited retrospective official history documents national mobilization,
    not a uniform county allocation formula.
  legal_identifiers:
  - 1968-12-22 People's Daily publication of Mao's instruction on educated youths going to the countryside
  implementation_regime: >
    Urban youths moved to rural communities; county gazetteers recorded local
    reception. State-farm placements are outside the paper's county-gazetteer
    measure. Its 1968–1977 window is narrower than the whole movement.
  assignment_mechanism: >
    Counties received different numbers, but no inspected source establishes
    a single exogenous county-allocation rule. The paper interacts historical
    county reception with affected cohorts; it does not randomize placement.
  parent: null
  related_variations: []
timeline:
  announcement: '1968-12-22 national mass-mobilization instruction; earlier send-down activity existed'
  effective: null
  implementation_start: 1968
  implementation_end: 1977
  local_timing: The paper counts 1968–1977 county arrivals; this is a study window, not the whole policy duration.
  anticipation: County-specific anticipation has not been established.
  last_verified: '2026-10-02'
assignment:
  unit: Rural county of reception × resident birth cohort for the outcome design
  treated: Higher county received-youth density, interacting with cohorts born 1956–1969
  comparison_pool: Lower-density counties and 1946–1955 cohorts in the baseline
  rule: >
    The authors divide county received-youth totals by 1964 county population
    and classify cohorts by primary-school overlap with the mass movement.
    The measured density is not a statutory threshold.
  intensity: County received youths in 1968–1977 / 1964 total county population
  exemptions: []
  compliance: Individual compliance is not measured; received rather than assigned youths enter the variable.
  exposure_construction: >
    Join 1968–1977 county reception totals to 1964 county population and
    interact density with a 1956–1969 birth-cohort indicator. The appendix
    tests alternative windows and overlap years. Do not substitute a per-child
    denominator or 1966–1978 window as the published baseline.
  required_identifiers:
  - harmonized historical county ID
  - 1964 county population
  - 1968–1977 received-youth total
  - rural resident birth cohort and schooling outcome
  spillovers: County migration and school catchments may matter; negligible spillovers are not established here.
research_compatibility:
  outcome_domains: [rural schooling, human capital]
  affected_populations: [rural residents born 1946–1969 in the paper's comparison]
  mechanism_channels: [educated-person arrival, possible teaching and aspiration effects]
  best_for:
  - Studying historical county exposure to relocated urban youths after adjudicating the outcome-coding dispute
  not_good_for:
  - Claiming randomized county placement or an instrument for every later development outcome
  - Concluding the movement increased net welfare or growth from a rural-schooling coefficient
  - Treating every received youth as a teacher
design:
  claim_type: reduced-form
  affordances:
  - county-level historical reception counts
  - birth-cohort variation in school-age overlap
  candidate_designs:
  - county-density × affected-cohort DID with explicit schooling-measure sensitivity
  identifying_variation: >
    Higher versus lower county received-youth density, compared across
    1956–1969 affected and earlier birth cohorts. County and province-cohort
    fixed effects make identification conditional, not random.
  primary_strategy: >
    AER appendix Table A1 reports rural-individual 1990-census years-of-
    education regressions on density × affected cohort, with county,
    province-cohort and baseline-education-by-cohort effects, gender and
    ethnicity controls, and county-clustered standard errors.
  estimand: >
    Differential rural schooling attainment of affected versus older
    cohorts per unit of county youth-reception density, conditional on
    outcome coding and DID assumptions; not an individual youth effect.
  treatment_variable: County received youths / 1964 population × affected-cohort indicator
  comparison_logic: Affected and earlier rural cohorts within counties of differing historical intensity
  estimation_notes: >
    Final appendix Table A1 and Appendix D verify measure and cohort
    definitions. Table B1 gives 1,773 core counties after exclusions.
    No geographic IV is documented in the verified baseline.
  assumptions:
  - Without arrivals, cohort schooling gaps would not systematically vary with county reception density after controls
  - Gazetteer omissions and historical geography do not induce material treatment-linked bias
  - Schooling-years coding is comparable across changing education systems
  diagnostics:
  - Reproduce both historical school-length codings on common data
  - Check cohort-window and county-sample sensitivity
  - Audit state-farm exclusions and historical county boundaries
threats:
- type: outcome-coding-dispute
  basis: documented
  condition: >
    Gong et al. argue that Cultural Revolution school-length coding makes
    the positive result negative and insignificant. Chen et al. dispute
    this and defend the baseline in two replies. Not independently
    adjudicated here.
  evidence_refs: [E4, E5, E6]
  possible_diagnostics:
  - Reproduce both codings and schooling-level outcomes on the same microdata
- type: nonrandom-county-reception
  basis: inferred
  condition: >
    County reception could covary with contemporaneous school expansion
    or disruption. National policy origin alone does not grant exogeneity.
  evidence_refs: [E2]
  possible_diagnostics: [Inspect cohort patterns and local school expansion]
- type: gazetteer-coverage
  basis: documented
  condition: >
    County totals cover 1968–1977 and exclude state farms; some counties
    lack reception or 1964 population data.
  evidence_refs: [E2]
  possible_diagnostics: [Report exclusions and compare province aggregates]
empirical_requirements:
  contract_version: 1
  population: Rural residents in the 1990 census comparison, born 1946–1969
  observation_unit: Rural individual × county × birth cohort
  geography_level: County
  time_start: 1964
  time_end: 1990
  minimum_frequency: Birth cohort, with cumulative 1968–1977 exposure
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields:
  - historical county ID
  - 1964 county population
  - 1968–1977 youth-reception total
  - birth year, rural residence, education attainment and coding
  required_identifiers: [historical county ID, birth cohort]
  treatment_key: [historical county ID, birth cohort]
  treatment_source: >
    Authors' county-gazetteer compilation; their county dataset is catalogued
    at PKU DOI 10.18170/DVN/MDIN00, but all files are restricted under
    access terms. This repository does not copy it.
  measurement_risks:
  - historical county harmonization and missing 1964 denominators
  - exclusion of state-farm placements
  - disputed schooling-level to years conversion
evidence:
- id: E1
  source_type: archive
  citation: Beijing Party Organization Department, historical note on 1968-12-22 send-down instruction
  url: https://www.bjdj.gov.cn/article/35162.html
  date: 2021
  supports: [identity.instrument, identity.authority, identity.legal_identifiers, timeline.announcement]
  verification_status: verified
  access_level: full-text
  locator: '党史日历·上山下乡: 1968-12-22 People’s Daily conveyed the instruction; retrospective summary, not original newspaper scan.'
- id: E2
  source_type: paper
  citation: Chen et al. 2020, Arrival of Young Talent, AER online appendix
  url: https://www.aeaweb.org/articles/materials/13570
  date: 2020
  supports:
  - identity.implementation_regime
  - identity.assignment_mechanism
  - timeline.implementation_start
  - timeline.implementation_end
  - assignment.rule
  - assignment.intensity
  - assignment.exposure_construction
  - design.identifying_variation
  - design.primary_strategy
  - design.treatment_variable
  - design.estimation_notes
  - empirical_requirements.treatment_source
  verification_status: verified
  access_level: full-text
  locator: 'Table A1 p.3; Table B1 p.7; Appendix C pp.9–11; Appendix D pp.12–13, inspected 2026-10-02.'
- id: E3
  source_type: paper
  citation: Chen, Fan, Gu, Zhou. 2020. Arrival of Young Talent. American Economic Review 110(11):3393–3430. DOI 10.1257/aer.20191414
  url: https://doi.org/10.1257/aer.20191414
  date: 2020
  supports: [identity.instrument, design.estimand]
  verification_status: verified
  access_level: abstract
  locator: 'AEA bibliographic page and abstract; final article full text not directly inspected.'
- id: E4
  source_type: paper
  citation: Gong, Liu, Lu, Wen, Zhou. 2021. Was China’s Send-down Movement Really a Blessing? ShanghaiTech SEM WP 2020-012
  url: https://sem.shanghaitech.edu.cn/2021/0629/c3558a66929/page.htm
  date: 2021
  supports: [threats]
  verification_status: verified
  access_level: abstract
  locator: 'ShanghaiTech working-paper abstract; asserts negative insignificant estimate under revised school-years coding.'
- id: E5
  source_type: paper
  citation: Chen, Fan, Gu, Zhou. 2021. Arrival of Young Talent, Reply. SSRN 3787288
  url: https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID3787288_code2884684.pdf?abstractid=3787288
  date: 2021
  supports: [threats]
  verification_status: verified
  access_level: abstract
  locator: 'SSRN abstract; authors reject the critique and report additional evidence.'
- id: E6
  source_type: paper
  citation: Chen, Fan, Gu, Zhou. 2021. Arrival of Young Talent, Further Reply. SSRN 3917492
  url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3917492
  date: 2021
  supports: [threats]
  verification_status: verified
  access_level: abstract
  locator: 'SSRN further-reply abstract documents continuing outcome-coding disagreement.'
- id: E7
  source_type: official-data
  citation: Chen, Fan, Gu, Zhou. 2024. County-Level Sent-down Youth Dataset of China. PKU Open Research Data Platform V1, DOI 10.18170/DVN/MDIN00
  url: https://opendata.pku.edu.cn/dataset.xhtml?persistentId=doi%3A10.18170%2FDVN%2FMDIN00&version=1.0
  date: 2024
  supports: [empirical_requirements.treatment_source]
  verification_status: verified
  access_level: metadata
  locator: 'Dataset description covers 1968–1977 county counts; three files restricted. No data file accessed.'
design_applications:
- paper: 'Arrival of Young Talent: The Send-Down Movement and Rural Education in China'
  doi: 10.1257/aer.20191414
  journal: American Economic Review
  year: 2020
  research_question: Did local youth reception change schooling for rural school-age cohorts?
  population: Rural residents in the core county sample, born 1946–1969
  outcome: Years of education in 1990 census; coding disputed
  data_used: [1990 rural census sample, county-gazetteer received-youth totals, 1964 county population]
  treatment_encoding: County reception density × 1956–1969 birth-cohort indicator
  comparison: Earlier cohorts in the same county and cohorts across counties of differing intensity
  empirical_design: Cohort-by-county-density DID with county and province-cohort fixed effects
  assumptions: [Conditional parallel differences, comparable schooling-years coding]
  threats_addressed: [Appendix cohort-window and denominator sensitivity; coding dispute not resolved here]
  evidence_refs: [E2, E3]
readiness_blockers:
- Public critique and replies contest the schooling-effect sign and magnitude; do not recommend it without adjudicating outcome coding on common data.
- PKU county data files require authorized access or independent gazetteer reconstruction.
method_transfer: null
---
## Institutional Background

The 1968 national push moved urban educated youths to rural communities.
The paper measures historical reception from county gazetteers, not quotas.
[E1; E2]

## What Changed

The real research object is county received-youth density during 1968–1977,
interacted with school-age birth cohorts. [E2]

## Implementation and Assignment

The final AER appendix divides received youths by 1964 county population;
state-farm placements are omitted. The affected cohorts are 1956–1969.
The inspected sources do not establish random county allocation. [E2]

## Why This Creates Empirical Variation

The paper compares education gaps between older and school-age cohorts
across counties with different historical reception densities. This is
conditional cohort DID, not a simple policy-onset comparison. [E2]

## Identification Risks

This is a useful lead, not an automatically clean instrument. County reception
was not verified as random, state farms are omitted, and school systems changed.
A public critique disputes the paper's schooling-year coding and the authors
replied twice. Without adjudicating that dispute on common data, this record
stays contested and cannot be recommended as a ready causal estimate.
[E2; E3; E4; E5; E6]

## Data Requirements

The county dataset has a DOI, but the files require authorization. The former
record overstated a 1966 directive, a 1966–1978 study window, a geographic IV,
and a 1982–2005 outcome panel as verified baseline facts; these are withdrawn.
[E2; E7]

## Evidence Notes

E1 is a retrospective official historical summary, not the original
1968 newspaper. E2 is the final paper's online appendix, E3 its publisher
abstract, E4 the critical working paper, E5–E6 the authors' replies, and
E7 restricted dataset metadata. The published full article and restricted
microdata were not directly inspected here. [E1; E2; E3; E4; E5; E6; E7]
