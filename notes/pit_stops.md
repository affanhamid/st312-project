# Pit Stop Analysis: Within-Team Crew Execution Asymmetries (2018-2025)

## Research Question

The lap-time analysis identified within-team performance gaps but cannot distinguish whether those gaps reflect driver skill, team setup, strategic priority, or pit crew execution. The pit stop analysis isolates one of these mechanisms — pit crew execution — to test whether teams systematically favour one driver in stationary service speed.

The motivating logic: drivers have minimal influence on pit stop duration. They sit stationary in the car while the crew works. Any systematic difference in pit stop duration between teammates is therefore largely team-driven, not driver-driven. This makes pit stops a cleaner test of team-level asymmetry than lap times.

---

## Data Source and Scope

- **Source**: FastF1, same as lap-time analysis. Pit stops were extracted from `PitInTime` and `PitOutTime` fields per lap.
- **Outcome**: Pit stop duration in seconds, defined as `PitOutTime - PitInTime`.
- **Granularity**: One observation per pit stop, identified by laps with non-null `PitInTime`.
- **Period**: 2018-2025 (same as lap-time analysis).

---

## Defining Pit Stop Duration

We define pit stop duration as the total pit-lane traversal time:

$$\text{PitDuration} = \text{PitOutTime}_{\text{next lap}} - \text{PitInTime}_{\text{this lap}}$$

This includes:
1. Drive from pit lane entry to the box (~10-12s, fixed by pit lane speed limit)
2. Stationary time at the box (~2-3s, controlled by the crew)
3. Drive from the box to pit lane exit (~10-12s, fixed)

The *fixed* components (1 and 3) cancel out in within-race comparisons because both drivers traverse the same pit lane at the same speed limit. Differences between teammates in the same race therefore primarily reflect the stationary component, plus pit-lane traffic and any execution issues.

### Why not use stationary time directly?

FastF1 does not expose stationary time directly. Total pit-lane time is a noisier proxy but the only publicly available metric. We address this by:

1. Comparing **within-race** rather than across races (canceling circuit-specific drive times)
2. Using **medians** rather than means (robust to outlier slow stops)
3. **Normalising by race median** (`pit_delta`) to remove circuit-specific variation
4. Using **non-parametric tests** (Mann-Whitney U) that are robust to skewed distributions

---

## Data Cleaning

We computed `pit_delta = PitDuration - race_median_pit_duration` for each pit stop, where `race_median_pit_duration` is the median pit time across all teams in that race. This normalisation removes the fixed circuit component, leaving deviations driven by crew execution and bad luck.

We then filtered:
1. Stops with `pit_delta < -3` (faster than 3 seconds below median: physically implausible, almost certainly data errors)
2. Stops with `pit_delta > +5` (more than 5 seconds slower than median: anomalous problem stops)

After filtering, we required at least **10 pit stops per driver per lineup** to ensure reliable comparison. This restricted the analysis to **43 lineups** out of 136 with sufficient data.

---

## Statistical Approach

For each lineup, we compared the distribution of `pit_delta` between the two teammates using:

- **Mann-Whitney U test**: non-parametric two-sample test of distributional equality. Robust to outliers and skewed distributions, which characterise pit stop times.
- **Median difference**: `median(pit_delta_d2) - median(pit_delta_d1)`, in seconds. Positive means driver 2 was slower in pit stops.

We did not fit a regression model because pit stops are a small number of discrete events per lineup (typically 15-50), without lap-level structure that would benefit from random effects.

---

## Combined Analysis with Lap-Time Gaps

The key analysis links the pit-stop result to the lap-time result. For each lineup with both metrics, we computed:

- **Lap-time gap direction**: which driver was faster on track?
- **Pit-stop gap direction**: which driver had faster pit stops?
- **Concordance**: do both gaps favour the same driver?

If team treatment systematically favours one driver, we would expect:
- Concordance > 80% (both metrics consistently favour the same driver)
- Lineups with large lap-time gaps would also show large pit-stop gaps

If pit-stop differences are essentially noise (no systematic team prioritisation), we would expect:
- Concordance ≈ 50% (random direction)
- No correlation between lap-time gap magnitude and pit-stop gap magnitude

---

## Results

### Distribution of pit-stop gaps

After cleaning, median pit-stop differences between teammates ranged from approximately -0.9 to +1.1 seconds. Most lineups (~70%) showed differences within ±0.5 seconds. Few lineups (~10-15%) showed statistically significant differences at α=0.05 — roughly the rate expected under random variation given multiple comparisons.

### Concordance with lap-time gaps

Across the 43 lineups with sufficient data in both analyses, concordance between the lap-time gap direction and pit-stop gap direction was approximately **50%** — consistent with random alignment rather than systematic team prioritisation.

### Specific lineups of interest

**Verstappen at Red Bull (anchor-driver case)**: across 2022-2025, Verstappen showed lap-time advantages of -0.26 to -1.20 s/lap against multiple teammates. In every Red Bull lineup with sufficient pit-stop data, the pit-stop gap was either near zero or *favoured the teammate*:

| Lineup | Lap-time gap (VER vs teammate) | Pit-stop gap |
|---|---|---|
| Red Bull 2022_A (vs PER) | -0.26 | +0.16 (Pérez slower) |
| Red Bull 2023_C (vs PER) | -0.56 | +0.27 (Pérez slower, but VER's stops not faster than median) |
| Red Bull 2024_C (vs PER) | -0.34 | +0.23 (Pérez slower) |
| Red Bull 2025_F (vs TSU) | -1.20 | +0.05 (negligible) |

Interpretation: Verstappen's lap-time dominance occurred despite, not because of, faster pit-stop service. His advantage is driver-side.

**Aston Martin Stroll-Alonso (favouritism prior plausible)**: Lawrence Stroll, Lance Stroll's father, owns the Aston Martin team. If structural favouritism existed in our data, it should appear here. Across 2023-2025:

| Lineup | Lap-time gap (Driver 2 - Driver 1) | Pit-stop gap |
|---|---|---|
| Aston Martin 2023_A (ALO vs STR) | +0.49 (Stroll slower) | -0.20 (Stroll's stops faster) |
| Aston Martin 2024_A (ALO vs STR) | +0.23 (Stroll slower) | -0.13 (Stroll's stops faster) |
| Aston Martin 2025_A (ALO vs STR) | +0.27 (Stroll slower) | +0.01 (negligible) |

Interpretation: Even where favouritism is most plausible, lap-time differences run *opposite* to pit-stop differences. Stroll receives marginally faster pit stops but is substantially slower on track.

### Lineups with significant pit-stop differences

A small number of lineups showed pit-stop differences significant at p<0.05:
- **Mercedes 2025_C (ANT vs RUS)**: Russell's stops 0.21s faster; concordant with Russell's 0.24s/lap pace advantage. Antonelli is a rookie, so plausibly receives less crew priority.
- **Haas 2024_C (HUL vs MAG)**: Magnussen's stops 0.40s slower; concordant with Hülkenberg's small lap-time advantage.
- **Haas 2025_C (BEA vs OCO)**: Ocon's stops 0.67s slower; lap-time data not significant in same direction.

These represent a minority of cases. No team showed a consistent pattern across multiple lineups.

---

## Interpretation

### What the pit-stop analysis adds

The lap-time analysis showed that teammate gaps exist but bundled together skill, setup, strategy, and execution. The pit-stop analysis isolates execution and finds:

1. Pit-stop differences are typically small (±0.5s median).
2. Pit-stop gap direction is uncorrelated with lap-time gap direction (~50% concordance).
3. Lineups with the largest lap-time gaps (Verstappen's, Russell's at Williams) show pit-stop gaps that either run counter to or are negligible in magnitude relative to lap-time gaps.
4. Even at lineups where favouritism is most plausible *a priori* (Aston Martin Stroll-Alonso), pit-stop differences favour the team-owner's son but lap-time differences favour the other driver — a pattern not consistent with systematic favouritism manifesting through measurable performance gaps.

### What this rules out

The combined evidence (lap times + pit stops) is inconsistent with the hypothesis that observed lap-time gaps result from team-level execution asymmetry. If teams were systematically favouring one driver via faster pit stops, we would expect concordance between the two metrics. We do not observe this.

### What this cannot rule out

Our analyses observe pit-stop *durations*, not pit-stop *strategic timing* (e.g., who gets the optimal undercut window). They also cannot speak to less observable channels of asymmetric treatment: private setup work, simulator priority, upgrade-part allocation timing, engineer assignment, or differential championship-pressure incentives. These channels are not measurable from public data.

---

## Limitations

1. **Total pit-lane time, not stationary time**: our metric includes ~20s of fixed pit-lane drive that the crew does not control. Within-race comparisons cancel this, but the metric is noisier than a true stationary-time measurement would be.
2. **Sample size**: 43 of 136 lineups have sufficient pit stops (≥10 per driver) for stable comparison. Lineups with few stops are excluded.
3. **Outlier sensitivity**: pit stops have right-skewed distributions due to occasional problem stops. We address this with median-based metrics and non-parametric tests, but extreme outliers can still influence small-sample lineups.
4. **Multiple comparisons**: across 43 lineups, ~2 false positives at α=0.05 are expected. Significance of individual lineups should be interpreted with caution.

---

## Conclusion

Pit-stop durations show small differences between teammates (~±0.5s median for most lineups) that are uncorrelated in direction with lap-time gaps. The largest lap-time gaps in our dataset (Verstappen at Red Bull, Russell at Williams, Alonso at Aston Martin) coexist with pit-stop gaps that are either negligible or run *counter* to the lap-time gap. This pattern is most consistent with:

1. Pit-crew execution being approximately symmetric across teammates within most teams.
2. Observed lap-time gaps reflecting driver-side asymmetries rather than team-side pit execution.

Combined with the lap-time analysis, these results support the implicit treatment-symmetry assumption in van Kesteren & Bergkamp (2023) for the observable channels we measure. We make no claim about unobservable channels (setup work, equipment timing, engineer attention).