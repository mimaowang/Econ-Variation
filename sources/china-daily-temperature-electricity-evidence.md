# China daily temperature and urban-rural electricity: recovered evidence

This note belongs to ground task `task-e2153627bc98`, reopening historical
`candidate-3e2659be43b7`. It is staging evidence, not a canonical variation or an
additional counted case. Inspection date: 2026-09-28.

## Source and construction now recovered

The published article is Bai, Cao, Huang, Xi and Zhang, *Journal of Development
Economics* 180 (2026), 103692, online 2025-11-29,
[DOI 10.1016/j.jdeveco.2025.103692](https://doi.org/10.1016/j.jdeveco.2025.103692).
The [author-hosted published PDF](https://pengzhang.weebly.com/uploads/3/1/7/6/31762679/1-s2.0-s0304387825002433-main.pdf)
was inspected at section 2.1, equations 1-2 and footnotes 13-23 (printed pages 3-4),
section 4 and the data-availability statement (pages 9 and 12).

Paper-reported construction: State Grid residential consumption for 186
Zhejiang/Jiangsu counties or districts, separately urban/rural, daily
2019-01-01--2022-06-30. NMIC weather product `SURF_CLI_CHN_MUL_DAY_V3.0`
supplies station observations, converted by inverse-distance weighting within
200 km; neighbouring-province stations are included. Ten Celsius bins are
`<0`, `[0,4)`, `[4,8)`, `[8,12)`, `[12,16)`, `[16,20)`, `[20,24)`, `[24,28)`,
`[28,32)` and `>=32`. The omitted bin is **[20,24)**, not the 16-24 comfort range
in the earlier candidate. Equation 2 interacts temperature with an urban dummy,
using county and area effects, prefecture-year-month effects, day-of-month,
day-of-week and holiday effects, weather/AQI controls, 2020 county-area population
weights and county clustering. Data sharing is explicitly not permitted.

## What primary documentation establishes, and what it does not

The paper's NOAA alternative is independently documented at the
[NCEI GSOD dataset page](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00516),
inspected in full at Dataset Overview and Time/Location. This is direct official
dataset documentation, not a search snippet: daily mean temperature and other
elements are derived from station observations; historical coverage includes the
study years. The raw units and day boundary differ from a casual Celsius/local-day
interpretation. That matters when constructing bins and joining electricity dates.
It does not establish the authors' exact NMIC baseline processing or prove that
the two sources implement an identical daily exposure. No raw station subset was
inspected and no numerical equivalence is claimed.

The baseline NMIC link in paper footnote 14, its `data.cma.cn` replacement and the
mobile dataset page were inaccessible during this task. The official page remains
indexed by search, but an indexed description is not inspected primary support.
Do not promote it on that basis or silently replace the baseline with GSOD.

## How to interpret the comparison faithfully

The exposure is short-run local temperature, not urban status assigned at random.
The interaction compares conditional responses of urban and rural consumption to
the same county-day exposure. It does not estimate a causal effect of becoming
urban. Preserve the exact fixed-effect structure: day-of-month/week/holiday effects
are not interchangeable with a saturated date fixed effect. Nor is an area dummy
automatically a county-by-area fixed effect.

Higher electricity response is not itself a measured comfort or welfare gain.
Cold-day responses can differ because households use different fuels. Sparse
stations and urban heat islands can undermine common county-day exposure; the
article reports alternative exposure checks, but supplementary estimates were
not independently reproduced. Long-run warming and income-channel exercises have
different variation and assumptions; do not merge them into a short-run natural
shock or count them as separate mature cases without further identity resolution.

## Remaining bounded work before admission

Recover baseline NMIC documentation and the authors' station subset, interpolation
power, missing-observation rules and day convention. Inspect the supplementary
county/area geography and figure A1, the actual urban/rural electricity definitions
and aggregation, zero/log handling and sample exclusions. Resolve data-access and
reconstruction feasibility without promising public State Grid microdata. Then
decide whether a grounded conditional record is justified; do not publish a new
extracted record merely to increase the count.
