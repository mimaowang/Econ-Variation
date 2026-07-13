---
schema_version: 2
id: china-textbook-curriculum-reform
name: China's 2004–2010 High School Textbook Reform as a Shock to Political Ideology Content in Education
aliases:
- Cantoni Chen Yang Yuchtman Zhang curriculum ideology China
- 教科书改革 政治意识形态
- Chinese textbook reform political content
- education ideology China

status: extracted
provenance:
  task_id: legacy-untracked
scope:
  country: China
  regions:
  - Provinces that adopted new textbooks under the staggered reform
  domains:
  - education
  - political-economy
  - ideology
  - attitudes
  variation_type: staggered-rollout
  knowledge_role: china-variation
  china_relevance: The variation occurs in China, assigns exposure to Chinese units, and supports China-focused empirical
    research.
identity:
  instrument: China's staggered provincial adoption of new high school textbooks between 2004 and 2010 as part of a national
    curriculum reform (New Curriculum Reform), which altered the ideological and political content taught to students; the
    staggered provincial rollout creates variation in the timing of exposure to the reformed curriculum
  authority: Chinese Ministry of Education
  legal_identifiers:
  - New Curriculum Reform (基础教育课程改革纲要)
  - provincial textbook adoption regulations
  - textbook content standards
  implementation_regime: The central government mandated the curriculum reform but allowed provinces to adopt the new textbooks
    on a staggered schedule between 2004 and 2010; the new textbooks included a substantial reduction in explicitly political
    and ideological content compared to the pre-reform curriculum
  assignment_mechanism: Provincial adoption timing provides temporal variation; within provinces, which cohorts are exposed
    to new versus old textbooks depends on their year of high school entry, creating a cohort-based difference-in-differences
    design
  parent: null
  related_variations:
  - china-keju-abolition-elite-recruitment
  - china-media-censorship-vpn-experiment
timeline:
  announcement: '2001-06-01'
  effective: null
  implementation_start: 2004
  implementation_end: 2010
  local_timing: Provinces adopted the new curriculum on a staggered schedule between 2004 and 2010, with the first cohort
    of students exposed varying by province
  anticipation: The reform was announced in 2001 but implementation was staggered; individual students did not choose which
    curriculum they were exposed to
  last_verified: '2026-07-13'
assignment:
  unit: Individual (student) and province-cohort
  treated: Students who entered high school in a province after the new curriculum was adopted, and thus were exposed to textbooks
    with reduced political/ideological content
  comparison_pool: Students in the same province who entered high school before the new curriculum adoption; students in provinces
    that had not yet adopted the new curriculum in the same year
  rule: Exposure is determined by the interaction of provincial adoption year and student cohort (year of high school entry);
    students are treated if their province had adopted the new textbooks by the time they entered high school
  intensity: Binary at the individual level (exposed to new curriculum or not); intensity varies by the number of years of
    exposure (students exposed for all 3 years of high school vs only 1-2 years) and by the degree of content change
  compliance: Curriculum adoption was mandatory within each province once adopted; all schools in the province used the new
    textbooks — essentially full compliance
  exemptions: []
  exposure_construction: Code student i from province p in cohort c as treated if province p adopted the new curriculum on
    or before cohort c entered high school; construct measures of exposure intensity based on years of exposure and content
    analysis of textbook changes
  required_identifiers:
  - student ID
  - province code
  - high school entry year (cohort)
  - curriculum adoption status
  spillovers: Students in the same school or cohort may influence each other's attitudes regardless of individual exposure;
    teachers may adapt their teaching to the new curriculum
research_compatibility:
  outcome_domains:
  - political attitudes
  - values
  - beliefs
  - trust in government
  - individualism/collectivism
  - civic participation
  - educational outcomes
  affected_populations:
  - Chinese high school students
  - young adults shaped by reformed education
  - teachers implementing new curriculum
  mechanism_channels:
  - reduced political indoctrination
  - changed values and beliefs
  - critical thinking promotion
  - altered worldview through curriculum content
  best_for:
  - Studying how education shapes political attitudes and values
  - understanding the long-run effects of curriculum content on ideology
  - testing theories of state-led ideological formation
  not_good_for:
  - Short-run test score effects of curriculum reform
  - estimating the effect of education quantity (only content changes)
design:
  affordances:
  - staggered provincial adoption
  - sharp cohort-based exposure
  - content analysis of textbook changes
  - large-scale survey data on attitudes
  candidate_designs:
  - staggered difference-in-differences
  - cohort analysis within provinces
  - event study around provincial adoption dates
  identifying_variation: The interaction of provincial adoption year with student cohort creates variation in curriculum exposure
    that is not chosen by individual students and is driven by provincial-level administrative decisions
  assumptions:
  - Provincial adoption timing is conditionally exogenous to student attitudes and not driven by local political climate
  - there are no other cohort-specific shocks that correlate with the adoption timing
  - students cannot select into provinces based on curriculum adoption
  diagnostics:
  - Test for pre-trends in student attitudes across cohorts before adoption
  - compare early vs late adopting provinces
  - test for differential selection into provinces by cohort
  - examine whether effects vary with years of exposure
  primary_strategy: Staggered difference-in-differences; event study; within-province cohort comparison; content analysis
    linking specific textbook changes to specific attitude changes
  estimand: The causal effect of the recorded exposure on Political attitudes (trust in government, views on democracy, individualism/collectivism),
    values, beliefs about the role of the state, conditional on the stated design assumptions.
  treatment_variable: Provincial adoption year × student high school entry cohort → binary or continuous exposure to new (less
    ideological) curriculum
  comparison_logic: 'Within-province: cohorts before vs after curriculum adoption; cross-province: early adopters vs late
    adopters in same year'
  estimation_notes: Staggered difference-in-differences; event study; within-province cohort comparison; content analysis
    linking specific textbook changes to specific attitude changes
threats:
- type: endogenous-adoption-timing
  basis: inferred
  condition: If provinces that adopted the new curriculum earlier were systematically different (more reformist, different
    political culture) from late adopters, the estimated effect of curriculum content may be confounded by provincial characteristics
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for provincial characteristics
  - test for pre-existing differences in attitudes across provinces
  - use only within-province variation
  - compare with non-school-attending cohorts
- type: cohort-confounds
  basis: inferred
  condition: Different cohorts of students are exposed to different social and economic conditions beyond the curriculum reform;
    cohort-specific shocks (e.g., the 2008 Olympics, the 2008 financial crisis) may confound the estimated effects
  evidence_refs:
  - E1
  possible_diagnostics:
  - control for cohort fixed effects
  - compare with unaffected groups
  - use within-province before/after comparisons
  - test for smooth cohort trends
empirical_requirements:
  contract_version: 1
  population: Chinese high school students and young adults across provinces, cohorts entering high school between 2001 and
    2010
  observation_unit: Individual (student)
  geography_level: Province
  time_start: 2004
  time_end: 2015
  minimum_frequency: cross-section or repeated cross-section
  minimum_pre_periods: 3
  minimum_post_periods: 5
  required_fields:
  - student province of high school
  - high school entry year
  - survey measures of political attitudes
  - values
  - beliefs
  - trust
  - demographic controls
  required_identifiers:
  - student ID
  - province code
  - high school entry cohort
  treatment_key:
  - province code
  - cohort
  - new curriculum exposure indicator
  - years of exposure
  treatment_source: Provincial education bureau records on curriculum adoption dates; textbook content analysis (comparing
    pre-reform and post-reform textbooks); survey data on student attitudes (China General Social Survey, China Family Panel
    Studies, specialized student surveys)
  measurement_risks:
  - self-reported attitudes subject to social desirability bias in China
  - precise measurement of which textbook version a student used
  - migration between provinces for high school
  - province-level adoption dates may not capture within-province variation in implementation
evidence:
- id: E1
  source_type: paper
  citation: 'Cantoni, Davide, Yuyu Chen, David Y. Yang, Noam Yuchtman, and Y. Jane Zhang. 2017. "Curriculum and Ideology."
    Journal of Political Economy 125 (2): 338–392.'
  url: https://doi.org/10.1086/690951
  date: 2017
  supports:
  - identity
  - assignment
  - design
  - main estimates
  - content analysis
  - attitude analysis
  verification_status: verified
design_applications:
- paper: Curriculum and Ideology
  doi: 10.1086/690951
  journal: Journal of Political Economy
  year: 2017
  research_question: Does the content of education — specifically the political and ideological content of textbooks — shape
    students' political attitudes and values?
  population: Chinese high school students across provinces, cohorts entering between 2001 and 2010
  outcome: Political attitudes (trust in government, views on democracy, individualism/collectivism), values, beliefs about
    the role of the state
  data_used: []
  treatment_encoding: Provincial adoption year × student high school entry cohort → binary or continuous exposure to new (less
    ideological) curriculum
  comparison: 'Within-province: cohorts before vs after curriculum adoption; cross-province: early adopters vs late adopters
    in same year'
  empirical_design: Staggered difference-in-differences; event study; within-province cohort comparison; content analysis
    linking specific textbook changes to specific attitude changes
  assumptions:
  - provincial adoption timing conditionally exogenous
  - no cohort-specific confounds
  - no selective migration across provinces for curriculum
  - students cannot choose their curriculum exposure
  threats_addressed:
  - endogenous adoption timing via province fixed effects and controls
  - cohort confounds via cross-province comparison
  - selection via mandatory nature of curriculum
  evidence_refs:
  - E1
readiness_blockers:
- Primary institutional evidence has not been independently verified; current institutional grounding relies on the research
  paper.
- At least one design application does not yet identify the data used and must be grounded from the paper or replication package.
method_transfer: null
---
## Institutional Background
Education systems are one of the primary channels through which states attempt to shape citizens' values, beliefs, and political attitudes. In China, pre-reform high school textbooks contained substantial explicit political and ideological content — praise for the Communist Party, Marxist ideology, collectivist values, and a particular historical narrative. In 2001, the central government announced the New Curriculum Reform, which included revised textbooks with substantially reduced political content. [E1]

## What Changed
The new textbooks, adopted on a staggered provincial schedule between 2004 and 2010, reduced the proportion of explicitly political and ideological content. The reform shifted emphasis toward critical thinking, individual development, and modern economic concepts. This was not a change in the quantity of education but in its content — students still went to school for the same number of years, but what they learned changed. [E1]

## Implementation and Assignment
Provincial adoption of the new curriculum was determined by administrative decisions at the provincial education bureau level, creating staggered timing variation. Students are "treated" if their province had adopted the new curriculum by the time they entered high school. Since individual students cannot choose which province's curriculum they are exposed to (migration for this purpose is negligible), the assignment is plausibly exogenous at the individual level. [E1]

## Why This Creates Empirical Variation
The staggered adoption creates a difference-in-differences design: within each province, cohorts entering high school before the reform received the old (more ideological) curriculum, while cohorts entering after received the new (less ideological) curriculum. The cross-province variation (early vs late adopters) controls for cohort-specific national trends. This design isolates the causal effect of curriculum content on political attitudes. [E1; analytical inference]

## Identification Risks
Provincial adoption timing may reflect underlying political and social characteristics that also shape student attitudes. If more liberal provinces adopted earlier, and students in those provinces would have held different attitudes anyway, the estimated effect conflates curriculum content with provincial political culture. Cohort-specific shocks that differentially affect provinces (e.g., localized economic shocks) could also confound the estimates. [E1; analytical inference]

## Data Requirements
Provincial curriculum adoption dates (from education bureau records), content analysis of pre- and post-reform textbooks (coding ideological and political content), survey data with measures of political attitudes, values, and beliefs for high school students and young adults (with province and year/cohort of high school entry), and provincial-level economic and demographic controls. [E1]

## Evidence Notes
E1 finds that exposure to the reformed (less politically ideological) curriculum indeed changed students' political attitudes and values. The paper carefully documents the textbook content changes through systematic content analysis and links these specific content changes to specific attitude changes in affected cohorts. The findings provide some of the strongest causal evidence that education content — not just education quantity — shapes political ideology.
