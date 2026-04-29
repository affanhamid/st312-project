# RQ2: Intra-Team Performance Dynamics — Key Findings (2024 Season)

## Analysis 1: Lap Time Gaps (Linear Mixed Effects Model)

- The overall mixed effects model finds **no significant systematic lap time bias** between teammates after controlling for tyre compound, tyre life, stint, and position (is_driver1 coefficient = -0.014s, p = 0.699)
- The random effect variance for the driver indicator (0.204) suggests teammate gaps **vary meaningfully across team-race combinations**, even if the average effect is near zero
- Intermediate and wet tyres add ~9.6s and ~15.5s respectively compared to hards, confirming weather/compound as a major confounder that must be controlled for
- Tyre life has a small but significant negative effect (-0.021s per lap, p < 0.001), meaning lap times slightly decrease with tyre age after controlling for other factors — likely a fuel effect artefact
- Higher track position (further back) is associated with slower laps (+0.05s per position, p < 0.001)

## Analysis 1b: Per-Team Paired t-tests on Teammate Gaps

- **McLaren** (NOR-PIA): Norris is systematically faster by 0.27s on average (p = 0.0006)
- **Red Bull** (PER-VER): Verstappen is faster by 0.84s on average — the largest gap of any team (p = 0.001)
- **Haas** (HUL-MAG): Hulkenberg is faster by 0.27s on average (p = 0.009)
- **Aston Martin** (ALO-STR): Alonso is faster by 0.22s on average (p = 0.010)
- The remaining 6 teams (Williams, Alpine, Mercedes, RB, Ferrari, Kick Sauber) show **no statistically significant teammate gap** (all p > 0.05)
- These per-team gaps likely reflect genuine skill differences rather than favouritism, as they align with public perception of driver quality within each pairing

## Analysis 2: Pit Stop Durations (Paired t-tests)

- **No team shows a statistically significant pit stop duration bias** between teammates (all p > 0.05)
- The overall paired t-test across all teams is also non-significant (t = -0.945, p = 0.346)
- The mean absolute pit gap is 1.45s, but this variance is spread roughly equally in both directions — consistent with random mechanical variation rather than systematic favouritism
- This suggests F1 teams service both drivers with **comparable efficiency**, contradicting conspiracy theories about deliberate slow pit stops

## Analysis 3: Tyre Allocation (Chi-Square Tests)

- **Mercedes** shows a highly significant imbalance: Hamilton received 11.4% soft tyre laps vs Russell's 3.5% (chi-squared = 48.7, p < 0.001) — the strongest evidence of differential treatment
- **Aston Martin**: Stroll received more soft laps (9.1%) than Alonso (6.1%) (p = 0.014)
- **McLaren**: Norris received slightly more soft laps (5.7%) than Piastri (3.8%) (p = 0.036)
- The remaining teams (Kick Sauber, Red Bull, and the 5 teams with insufficient soft tyre data) show **no significant allocation difference**
- Note: unequal soft tyre allocation does not necessarily indicate favouritism — it may reflect different strategic choices (e.g. a driver running longer stints on hards), race circumstances (safety cars, rain), or the leading driver inheriting a different strategy window

## Overall Conclusions

- **Lap times**: Significant gaps exist at 4/10 teams, but are consistent with known driver quality differences rather than resource favouritism
- **Pit stops**: No evidence of systematic bias at any team — both drivers receive comparable service
- **Tyre allocation**: Mercedes stands out with a large, statistically significant imbalance in soft tyre usage favouring Hamilton; two other teams show smaller but significant differences
- The combined evidence suggests that **observable performance differences between teammates are primarily skill-driven**, with limited evidence of systematic strategic favouritism — though the Mercedes tyre allocation finding warrants further investigation across multiple seasons
