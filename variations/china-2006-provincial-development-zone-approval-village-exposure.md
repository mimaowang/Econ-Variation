---
schema_version: 2
id: china-2006-provincial-development-zone-approval-village-exposure
name: 2006 Provincial Development-Zone Approval and Village Exposure in China
aliases:
- Lu-Wang-Zhu 2019 economic zone program
- 2006 provincial development-zone cohort
- 2006年省级开发区审核与村级暴露
status: design-documented
provenance:
  task_id: task-b0c3721a8107
scope:
  country: China
  regions: [mainland China; villages in counties represented in the 2004 and 2008 economic censuses]
  domains: [regional-economics, urban-economics, development-economics, firms, industrial-policy]
  variation_type: pilot-assignment
  knowledge_role: china-variation
  china_relevance: >
    Lu, Wang and Zhu study mainland Chinese manufacturing activity in villages
    covered by the 2006 cohort of province-level economic-zone approvals. The
    empirical exposure is location within a designated zone, not the famous
    1979 coastal special economic zones or every Chinese industrial park.
identity:
  instrument: >
    Provincial-level approval and delineation of economic development zones
    in the 2006 cohort used by Lu, Wang and Zhu. Approval changes formal zone
    status and access to a locally administered bundle of land, infrastructure
    and preferential business policies; it does not prove that industrial
    activity or the park site first appeared in 2006.
  authority: >
    Provincial governments approve province-level zones. National agencies
    audited and published the compliant-zone directory and confirmed their
    boundaries during the 2003-2007 cleanup [E1; E2]. The paper obtained a
    Ministry of Land and Resources zone dataset and reconstructed village
    membership [E3, reported application].
  legal_identifiers:
  - 中国开发区审核公告目录（2006年版）; 国家发展改革委、国土资源部、建设部公告2007年第18号
  - 国办发明电〔2003〕30号; pause on new development-zone approvals, cited by the 2007 announcement
  implementation_regime: >
    The 2006 cohort consists of province-level economic and technological,
    high-tech and specialized industrial zones. The paper excludes 19
    national-level zones approved in 2005 because their authority and
    overlapping export-processing locations differ [E3, pp. 333, 338-339].
    The official 2007 directory reports each listed zone's original name,
    approving authority, approval month, approved area and announcement
    number [E1]. A 2006 approval can formalize or reorganize an earlier
    industrial park; it should not be read as a guaranteed greenfield opening.
  assignment_mechanism: >
    A provincial approval and recognized four-sided zone boundary place
    particular villages or communities inside the zone. The authors join
    zone-village membership to manufacturing firms' 12-digit location codes
    and addresses; firms outside the zone in the same county form a main
    comparison [E3, pp. 336-339]. The site and approval choices are not random.
  parent: null
  related_variations: [china-industrial-parks-edge-city-spillovers, china-industrial-park-political-connection-rotation]
timeline:
  announcement: '2007-03-27 national directory announcement for audited zones; individual provincial approvals occurred earlier'
  effective: null
  implementation_start: 2006
  implementation_end: 2006
  local_timing: >
    The paper codes 663 province-level zones as its 2006 cohort and compares
    2004 with 2008 census outcomes [E3, Table 1 and §III]. For any individual
    zone, use the provincial approval month in the official directory, not
    the 2007 directory publication date, as the formal-status anchor [E1].
    The paper's baseline binary post period cannot identify when a particular
    parcel was serviced or when each incentive became usable.
  anticipation: >
    The cleanup, local application, infrastructure work and an earlier park
    name could precede formal approval. The official directory's "original
    name" column and the continuing national pause on new zones make a
    sudden, unanticipated 2006 greenfield shock an unsafe interpretation
    [E1; E2].
  last_verified: '2026-10-02'
assignment:
  unit: village or community by observation year; manufacturing firms inherit exposure through their location code
  treated: >
    A village/community that the authors map inside a 2006-approved
    province-level zone, observed in the post-approval 2008 economic census.
  comparison_pool: >
    Non-zone villages in the same county that are not covered by an earlier
    zone; the boundary-DID version compares firms in areas within 1 km on
    opposite sides of a zone boundary. Nearby non-zone villages can still
    receive spillovers [E3, §§II-III].
  rule: >
    Identify a 2006 province-level approval, recover its recognized boundary
    and constituent villages/communities, then join the village's 12-digit
    administrative code and firm address to the 2004/2008 census [E3].
    Directory inclusion alone is not a firm-level treatment indicator.
  intensity: >
    Main exposure is binary inside-zone status. The paper additionally
    examines distance rings around zone villages and a 1-km inside/outside
    boundary contrast, without treating these as separate policy instruments.
  exemptions:
  - National-level zones in the 2005 cohort, mostly overlapping export-processing zones, are excluded from the main analysis.
  - Villages in older zones are excluded from the clean comparison construction.
  compliance: >
    Formal approval and the published boundary establish recognized zone
    status. Neither source proves identical tax rates, infrastructure delivery
    or firm take-up across zones; local committees could vary the bundle.
  exposure_construction: >
    Match the authors' zone-village/community list to economic-census firm
    addresses and 12-digit location codes; aggregate firm capital, employment,
    output and counts to village-year. The boundary analysis geocodes firms
    and infers a 1-km boundary neighborhood from close inside/outside firm
    pairs because complete village polygons were unavailable [E3, §III].
  required_identifiers: [zone identifier and approval month, zone-village membership, 12-digit village/community code, firm address or coordinates, county identifier, census year]
  spillovers: >
    Firms can relocate between zone and non-zone villages, while nearby
    non-zone places can gain or lose activity. The article estimates county
    spillover and 2-20 km ring specifications; a local treated-area gain is
    not automatically a national net gain [E3, §II.B].
research_compatibility:
  outcome_domains: [manufacturing entry and exit, capital, employment, output, productivity, wages]
  affected_populations: [manufacturing firms in newly approved zone villages, neighboring non-zone firms, local workers and landholders]
  mechanism_channels: [formal zone governance, land and infrastructure provision, local tax and customs preferences, agglomeration and firm entry]
  best_for:
  - Comparing manufacturing changes inside formally approved provincial zones with other villages in the same counties, conditional on siting and pretrend evidence.
  - Testing whether gains are driven by new firm entry or incumbent growth when firm identity and location can be linked.
  not_good_for:
  - Treating a 2006 approval as proof that no industrial park or economic activity existed there before approval.
  - Extrapolating the local 2004-2008 manufacturing estimate to all Chinese zones, long-run welfare or a uniform tax-rate shock.
design:
  claim_type: causal
  affordances: [2004 pre and 2008 post manufacturing censuses, village-level inside/outside assignment, within-county comparisons, boundary-neighborhood comparison]
  candidate_designs: [village-level difference-in-differences, boundary difference-in-differences, county-level difference-in-differences]
  identifying_variation: >
    The same county contains villages formally included and excluded from
    the 2006 province-level zone cohort. The paper compares their 2004-to-2008
    changes, and separately contrasts narrow inside/outside areas near
    zone boundaries [E3, §§II-III].
  primary_strategy: >
    Village and county-year fixed effects with baseline village traits
    interacted with year; county-clustered errors. The boundary-DID uses
    area fixed effects and zone-neighborhood-by-year effects, clustering
    at the zone [E3, equations 1-2].
  estimand: >
    A conditional local difference in manufacturing outcomes for villages
    inside the 2006-approved provincial-zone cohort relative to comparison
    villages over 2004-2008. It is not a pure effect of a single subsidy or
    of the physical construction of entirely new industrial sites.
  treatment_variable: >
    Inside-zone village indicator multiplied by the post-2006 period;
    the boundary-DID uses an inside-zone indicator for the paired 1-km
    neighborhood after approval [E3, equations 1-2; E4, Tables A2-A3].
  comparison_logic: >
    Compare treated and untreated villages within counties before and after
    zone approval, excluding pre-existing zone locations. Test whether the
    result changes near a boundary or when nearby non-zone villages are
    removed from the control group [E3, §II].
  estimation_notes: >
    The census DID has one pre (2004) and one post (2008) observation for
    59,949 villages in 580 counties, including 3,963 zone villages. ASIF
    2004-2008 supplies village pretrend checks and wage outcomes; TFP stops
    in 2007 because 2008 ASIF lacks needed inputs [E3, pp. 336-339;
    E4, Tables A2-A3].
  assumptions:
  - In the absence of formal zone exposure, treated and comparison villages would have followed comparable conditional manufacturing trends.
  - Earlier park activity, zone applications and boundary placement do not generate the observed differential trend independently of the approved-zone bundle.
  - The boundary contrast is not contaminated by sharply different pre-existing land uses or strong spillovers across the boundary.
  diagnostics: [ASIF pre-approval trends, original-name and earlier-site audit, baseline village balance, within-county comparison, 1-km boundary DID, non-zone distance rings]
threats:
- type: preexisting-site-and-approval-timing
  basis: documented
  condition: >
    The official directory lists original names and the 2007 announcement
    says new-zone approvals were still paused during cleanup. Some 2006
    approvals may regularize operating sites; approval month is not the
    first date of industrial activity [E1; E2].
  evidence_refs: [E1, E2]
  possible_diagnostics: [compare original-name and local founding dates by zone, inspect 2004 baseline firms in future zone villages, separate new sites from formalized older parks]
- type: endogenous-siting
  basis: documented
  condition: >
    The article reports zone locations were selected partly for available
    land and local prospects; treated villages differed at baseline [E3].
  evidence_refs: [E3]
  possible_diagnostics: [conditional pretrends, baseline balance, boundary DID, county-year fixed effects]
- type: local-displacement-and-boundary-error
  basis: reported
  condition: >
    Nearby untreated villages can be affected by relocation or spillovers,
    and the boundary study reconstructs 1-km areas without complete village
    polygon data [E3].
  evidence_refs: [E3]
  possible_diagnostics: [ring exclusions, county spillover specification, alternative geocoding and boundary definitions]
empirical_requirements:
  contract_version: 1
  population: Manufacturing firms located in villages of counties covered by the 2006 provincial-zone cohort and suitable non-zone comparators.
  observation_unit: village-year aggregation of firm outcomes
  geography_level: village/community within county
  time_start: 2004
  time_end: 2008
  minimum_frequency: two census waves; annual ASIF needed for trend and wage or productivity extensions
  minimum_pre_periods: 1
  minimum_post_periods: 1
  required_fields: [zone approval month and type, zone-village/community membership, 2004 and 2008 firm capital and employment and output, firm address or village code, county ID, baseline village characteristics]
  required_identifiers: [zone ID, 12-digit village/community code, county ID, census year]
  treatment_key: [12-digit village/community code, 2006 cohort status, post-approval year]
  treatment_source: >
    NDRC 2006 development-zone directory supplies formal approval identity;
    the paper's Ministry of Land and Resources zone dataset and reconstructed
    village list supply assignment to firms. The zone-village crosswalk is
    paper-reported and must be obtained or rebuilt for replication [E1; E3].
  measurement_risks: [approval is not first economic activity, zone names and village codes can change, incomplete village boundary polygons, 2004 census cannot test its own pretrend]
evidence:
- id: E1
  source_type: official-data
  citation: NDRC, Ministry of Land and Resources and Ministry of Construction, China Development Zone Review and Announcement Directory (2006 edition), announced 2007.
  url: https://www.ndrc.gov.cn/xxgk/zcfb/gg/200704/W020190905487497735524.pdf
  date: '2007-03-27'
  supports: [identity.authority, identity.legal_identifiers, identity.implementation_regime, timeline.local_timing, timeline.anticipation, assignment.rule, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: 'Directory table headers and sampled entries, e.g. pp. 16-18 and 34-35, show zone name, original name, approving authority, approval month, approved area and announcement number; inspected 2026-10-02. Does not supply the paper-specific village crosswalk.'
- id: E2
  source_type: policy-document
  citation: NDRC, Ministry of Land and Resources and Ministry of Construction, Announcement 2007 No. 18, 27 March 2007; NDRC policy-research explanation, 19 April 2007.
  url: https://www.ndrc.gov.cn/xxgk/zcfb/gg/200704/t20070406_961289.html
  date: '2007-03-27'
  supports: [identity.implementation_regime, identity.assignment_mechanism, timeline.announcement, timeline.anticipation, threats.condition]
  verification_status: verified
  access_level: official-document
  locator: 'Announcement paragraphs 1-3: 2003 cleanup, audited-zone directory, four-sided boundaries and continuing pause on new provincial-zone approval; inspected 2026-10-02.'
- id: E3
  source_type: paper
  citation: 'Lu, Yi, Jin Wang and Lianming Zhu. 2019. Place-Based Policies, Creation, and Agglomeration Economies: Evidence from China’s Economic Zone Program. American Economic Journal: Economic Policy 11(3):325-360. DOI 10.1257/pol.20160272.'
  url: https://cep.hkust.edu.hk/sites/default/files/publications_media/full_paper/Place-Based%20Policies,%20Creation,%20and%20Agglomeration%20Economies%20Evidence%20from%20China%E2%80%99s%20Economic%20Zone%20Program.pdf
  date: '2019'
  supports: [identity.assignment_mechanism, assignment.treated, assignment.comparison_pool, assignment.exposure_construction, assignment.spillovers, design.primary_strategy, design.estimand, design.treatment_variable, design.comparison_logic, design.estimation_notes, empirical_requirements.observation_unit, empirical_requirements.required_fields, design_applications.empirical_design, design_applications.data_used]
  verification_status: verified
  access_level: full-text
  locator: 'Published article pp. 329-339 §§I-III, Table 1 and equations 1-2; pp. 340-346 results and diagnostics; pp. 355-357 Appendix A-B. Inspected 2026-10-02. Supports authors’ coding and findings, not independent proof every listed park was physically new in 2006.'
- id: E4
  source_type: appendix
  citation: Lu, Wang and Zhu, online supplemental appendix to AEJ Economic Policy 2019 article.
  url: https://swlb2.aeaweb.org/articles/materials/11281
  date: '2019'
  supports: [design.treatment_variable, design.diagnostics, empirical_requirements.measurement_risks, design_applications.threats_addressed]
  verification_status: verified
  access_level: appendix
  locator: 'Online Appendix Figures A3-A5 and Tables A2-A3, pp. 3-8: reconstructed boundary, 2-20 km ring analyses and ASIF village event coefficients; inspected 2026-10-02.'
- id: E5
  source_type: paper
  citation: American Economic Association, publication page for Lu, Wang and Zhu 2019, DOI 10.1257/pol.20160272.
  url: https://doi.org/10.1257/pol.20160272
  date: '2019'
  supports: [design_applications.paper, design_applications.doi, design_applications.journal, design_applications.year]
  verification_status: verified
  access_level: metadata
  locator: 'AEA article page title, authors, journal 11(3), pages 325-360 and DOI; inspected 2026-10-02. Bibliographic identity only.'
design_applications:
- paper: 'Place-Based Policies, Creation, and Agglomeration Economies: Evidence from China’s Economic Zone Program'
  doi: 10.1257/pol.20160272
  journal: 'American Economic Journal: Economic Policy'
  year: 2019
  research_question: Do formally designated Chinese development zones change local manufacturing activity, and are gains driven by entry or incumbent firms?
  population: 2006 province-level zone villages and comparison villages in the 2004/2008 manufacturing censuses; baseline 59,949 villages in 580 counties.
  outcome: Village-level manufacturing capital, employment, output and firm counts; ASIF-based TFP and wages.
  data_used: [2004 and 2008 economic censuses, 2004-2008 Annual Survey of Industrial Firms, Ministry of Land and Resources zone information, zone-village/community crosswalk, village addresses and 12-digit codes]
  treatment_encoding: Village lies inside a 2006-approved provincial zone and is observed after the 2006 cohort; 2005 national-level approvals are excluded.
  comparison: Non-zone villages in the same county, excluding old-zone exposure; a separate 1-km inside/outside zone-boundary comparison.
  empirical_design: Village DID with village and county-year fixed effects and baseline controls by year; boundary DID and spillover-distance checks.
  assumptions: [conditional parallel trends, no untreated-site differential shock from prior park activity, interpretable local spillovers]
  threats_addressed: [baseline imbalance, nonrandom siting, older-zone overlap, near-zone spillovers, boundary reconstruction]
  evidence_refs: [E1, E2, E3, E4, E5]
method_transfer: null
readiness_blockers: []
---

## Institutional Background

The empirical object is a **province-level development-zone status and boundary**, not a single national tax law. Provincial governments approved such zones; local committees then managed land, infrastructure and firm-facing preferences. During a national cleanup beginning in 2003, central agencies audited surviving zones and published a directory with approval months, original names and approved areas [E1; E2]. That official history changes how to read the paper's word “established”: some 2006-approved sites had earlier park identities. Formal status and the first day of industrial activity need not coincide.

## What Changed

Lu, Wang and Zhu isolate 663 province-level zones in the 2006 cohort, rather than the older coastal zones or the 19 national-level approvals of 2005 [E3, Table 1 and §III]. A village inside the recognized zone boundary could face a package of local governance, land access, infrastructure and preferential treatment. Neither the article nor the directory establishes that every village received the same package on the same day. The directory's 2007 publication is an audit announcement, not the treatment year assigned in the paper [E1; E2].

## Implementation and Assignment

The published study uses the Ministry's zone information to identify villages and communities inside each zone, then joins that list to manufacturers through addresses and 12-digit location codes [E3, pp. 336-339]. The official directory independently identifies approval authority, month and recognized area but does not publish this study's complete zone-to-village crosswalk [E1]. A reader can reconstruct the logic of exposure; replication still requires that crosswalk or a documented rebuild. Earlier parks, location-code changes and local reorganization must be checked before calling the 2004 observation unexposed.

## Why This Creates Empirical Variation

The authors compare manufacturing changes from 2004 to 2008 in approved-zone villages against non-zone villages within the same counties. Their boundary DID compares narrow areas on either side of a zone boundary, while ASIF years support pretrend and wage or productivity checks [E3; E4]. These are comparisons created by spatial designation and cohort timing, conditional on placement and prior activity. They do not randomize provincial approval or isolate any one subsidy from the zone bundle.

## Identification Risks

The sharpest risk is institutional timing: the official announcement says new provincial-zone approvals remained paused while existing zones were reviewed, and the directory preserves former park names [E1; E2]. A 2006 approval may therefore formalize an operating site, so “zone birth” should not be substituted for “formal approval.” Location selection and nearby displacement remain separate threats. The paper checks baseline differences, ASIF trends, a boundary contrast and 2-20 km rings [E3; E4]; those checks strengthen the local design without proving a clean national welfare effect.

## Data Requirements

The baseline needs 2004 and 2008 manufacturing-census outcomes aggregated by village, official approval timing, a zone-village list and 12-digit codes that remain joinable across waves. Annual ASIF data are needed for the paper's trend and wage/productivity extensions; the 2008 ASIF does not support the same TFP construction [E3; E4]. This repository describes the data contract and sources, not a copy of restricted NBS microdata.

## Evidence Notes

E1 and E2 verify formal status, cleanup and the timing caveat; E3 and E4 document how the authors coded and analyzed exposure. The AEA DOI page (E5) verifies article identity. The record is usable for a conditional research decision because the assignment, comparison and data join are explicit, but a new study must audit whether its chosen zone sites were already active before approval. The formal approval and economic-opening questions should never be silently merged.
