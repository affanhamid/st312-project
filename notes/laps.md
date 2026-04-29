### Predictor justifications

- **`TyreLife`** (continuous): tire degradation. Older tires are slower; expected coefficient ~+0.04 s/lap of tire age.
- **`LapNumber`** (continuous): proxy for fuel load. Cars get faster as fuel burns off; expected ~−0.03 s/lap.
- **`Compound`** (categorical, soft as baseline): soft compounds are faster than mediums than hards by 0.5-1.5 s/lap typically.
- **`IsDriver2`** (binary): variable of interest. The coefficient $\beta_5$ is the systematic within-lineup teammate gap, expressed as "driver2 minus driver1 in seconds per lap".
- **Random intercept by `RaceID`**: races vary by ~10-30 seconds in baseline lap time depending on circuit length. The random effect absorbs this so the fixed effects estimate within-race contrasts.

### Why mixed effects rather than OLS

Lap-level observations are not iid — laps within a race are highly correlated (shared track conditions, weather, race phase). OLS would treat 60 laps from the same race as 60 independent observations, dramatically underestimating standard errors. A random intercept per race correctly accounts for this clustering.

### Why frequentist (lme4-style) rather than Bayesian

We considered the Bayesian rank-ordered logit framework of van Kesteren & Bergkamp (2023). However, their model uses finishing position as outcome (one observation per driver per race), which discards the lap-level structure that lets us isolate driver pace from strategic and traffic effects. Our continuous lap-time outcome required a linear mixed-effects model. Frequentist estimation via `statsmodels.MixedLM` was sufficient given the size of our dataset (~60,000 laps), avoiding the additional complexity of MCMC sampling and prior specification.

---

## Sensitivity Analyses and Robustness

- **German GP 2019 exclusion**: a chaotic wet race left only ~9 valid laps per driver. Excluding this lineup left coefficients unchanged to within 0.001 s, confirming the result was not driven by outlier races.
- **Min-races filter (5 vs 3)**: large-magnitude outlier estimates from one-race "phase" lineups (e.g., one-off substitute drivers) were removed under the 5-race threshold. Headline conclusions are unchanged.
- **Convergence diagnostics**: Mixed-effects models converged for 134/136 lineups. Two failures (`Toro Rosso 2018_E`, `Williams 2018_C`) involved tiny single-race phases; these are excluded as not meeting the min-races threshold.

---

## Results

### Headline numbers

- 136 lineups fitted across 8 seasons and 15 teams.
- Distribution of teammate gaps: median ≈ -0.05 s/lap, IQR roughly [-0.30, +0.15].
- Most lineups (~70%) show small gaps (|gap| < 0.25 s/lap); a minority show large gaps (>0.5 s/lap).
- The signs of significant gaps are dispersed across teams: **no single team systematically favours one driver across multiple teammates**.

### Anchor-driver patterns

Examining individual drivers across multiple teammates within the same team reveals striking consistency:

- **Verstappen at Red Bull**: across 5 teammates and 7 seasons (2018-2025), Verstappen is faster in 15 of 16 lineups. Mean gap -0.69 s/lap, median -0.66 s/lap. Gap magnitude scales with teammate quality: smallest vs Ricciardo (~0 s, 2018) and Pérez (peak), largest vs Tsunoda (-1.20 s, 2025).
- **Russell at Williams**: faster than every Williams teammate across 4 lineups (2019-2021). Gaps ranged from -0.67 (vs Kubica, 2019) to -0.16 (vs Latifi, 2021 phase C).
- **Hamilton's edge is teammate-specific**: -0.20 to -0.43 s/lap vs Bottas (2018-2021); approximately zero vs Russell (2022-2024); +0.28 s/lap (Hamilton slower) vs Leclerc at Ferrari in 2025.
- **Alonso pattern matches Verstappen's**: dominant against weaker teammates (Vandoorne, Stroll), modest against competitive ones (Ocon).

### Mercedes 2019 case study

For the Mercedes-Hamilton-Bottas lineup in 2019 (the worked example):

- IsDriver2 (HAM): -0.199 ± 0.033 s/lap (Hamilton faster)
- TyreLife: +0.038 ± 0.002 s/lap (positive, expected)
- LapNumber: -0.056 ± 0.001 s/lap (negative, expected — fuel burn)
- Compound[Medium]: ~-0.20 s/lap relative to baseline
- Group Var (RaceID): ~140 s² (large; race baselines genuinely differ)
- N observations: 2,040 laps across 20 races

Hamilton's 0.20 s/lap × ~60 laps/race ≈ 12s/race, consistent with the published season-end championship margin (87 points, Hamilton 4 race wins ahead).

---

## Interpretation

### What the lap-time gap measures

The IsDriver2 coefficient is the systematic lap-time difference between teammates after controlling for tire age, fuel load, compound, and race-level baseline. It does **not** distinguish between:

1. Driver skill differences
2. Setup or equipment asymmetries
3. Strategic priority (better stint timing, cleaner air)
4. Effort asymmetry (championship pressure)
5. Pit crew quality differences

All of these manifest as faster lap times for the favoured driver. The lap-time analysis quantifies the **magnitude** of within-team gaps but not their **cause**.

### What the pattern of gaps suggests

Two observations are consistent with skill being the primary driver of observed gaps, rather than systematic team-level treatment:

1. **Anchor patterns**. Verstappen, Russell, and Alonso each show consistently large gaps against multiple teammates within the same team. If teams were favouring one driver, the gap should be roughly constant across teammates. Instead, gap magnitude *scales with teammate quality* — small against capable teammates, large against weaker ones. This is the predicted pattern under a "real driver-skill differences" model.

2. **No team-level systematic bias**. Across all 136 lineups, no single team shows a consistent direction of gap across multiple driver pairings. If, for example, Aston Martin favoured Stroll structurally (his father owns the team), we would expect Stroll to have positive gaps against multiple different teammates. We do not observe this.

### What the lap-time analysis cannot rule out

Asymmetric team execution (pit stops, strategy timing, compound allocation) could exist independently of lap-time gaps. A team could give one driver consistently faster pit stops while both drivers' raw pace was equal, and our lap-time analysis would miss this. The pit-stop and compound-allocation analyses are needed to address this, and are reported separately.

---

## Conclusion

We estimated within-team teammate gaps for 136 lineups across 2018-2025 using linear mixed-effects models on lap-level data. The distribution of gaps is centred near zero with substantial variation; most lineups show small differences (≤0.25 s/lap) while a minority show large gaps (>0.5 s/lap). 

Anchor-driver analyses show that gap magnitudes scale with teammate-quality differences rather than team identity, with consistent signs of large gaps across multiple teammates concentrated in a few exceptional drivers (Verstappen, Russell, Alonso). This pattern is consistent with the implicit assumption in van Kesteren & Bergkamp (2023) that within-team treatment is approximately symmetric; observed gaps appear to reflect genuine driver-skill differences rather than systematic team-level favouritism.

We note however that lap times alone bundle skill with all team-level asymmetries (setup, strategy, execution). Direct tests of treatment asymmetry require examining mechanisms less confounded with driver skill — pit stop durations and compound allocation — which we report in companion analyses.

This is a really informative plot. A few things jump out immediately, and they tell a coherent story.

## What I see

**Red Bull Racing dominates the bottom (most negative).** Look at the cluster: Red Bull 2025_F (-1.2), Red Bull 2020_A (-1.0), Red Bull 2019_E (-0.85), Red Bull 2024_D (-0.75), Red Bull 2024_B (-0.5), Red Bull 2023_C (-0.55), Red Bull 2021_E (-0.4), Red Bull 2022_A (-0.3). Almost every Red Bull lineup since 2019 shows the alphabetically-second driver as substantially faster.

This isn't favouritism — it's Verstappen. Alphabetically: ALB, GAS, LAW, PER, RIC, TSU, VER. Verstappen is alphabetically last in every pair, so he's always Driver2. Across 7 years and 6+ different teammates, he's consistently 0.4-1.2 s/lap faster.

**That's actually a stunning finding.** It's exactly the kind of evidence your project framing wants. A driver beating *six different teammates* by similar margins, in the same car, year after year, is about as close to a controlled experiment for "this is driver skill" as F1 ever provides. It's the inverse of favouritism — Red Bull aren't favouring Verstappen; he's just genuinely much faster than every teammate they've put in the car.

**Williams 2019_A near the bottom (-0.7).** That's KUB-RUS — Russell utterly outclassed Kubica in his rookie year. Combined with Williams 2020_A and 2021_A also showing -0.4 (Russell vs Latifi), you see another single-driver-anchor pattern: Russell is consistently 0.4-0.7 s/lap faster than every Williams teammate.

**Williams 2022_A at the top (+0.8).** Latifi vs Albon, Albon utterly dominating. This is interesting because it's the same Williams car as Williams 2021 (where Latifi vs Russell was -0.4). So Latifi loses by ~0.4s to Russell *and* loses by ~0.8s to Albon. That tells you Latifi was just genuinely slow, and the magnitude depended on how good his teammate was.

**McLaren 2021_A (+0.5).** Norris vs Ricciardo. Famously, Ricciardo struggled massively at McLaren — the data confirms it cleanly.

**Mercedes is mid-pack.** Mercedes lineups cluster around -0.2 to -0.4 (Hamilton vs Bottas), then 0 to +0.1 (Hamilton vs Russell). Notably tighter than Red Bull's gaps, which makes sense — Mercedes paired Hamilton with strong teammates.

**Most lineups cluster near zero.** Look at the middle band — there's a thick cluster between -0.2 and +0.2. For most teams in most years, teammates are within a couple of tenths.

## The story this suggests

You have at least three substantive findings just from looking at the plot:

1. **Most teammates are close.** The modal gap is small (within ±0.2 s/lap). Which means the 88/12 car/driver split from van Kesteren & Bergkamp is broadly consistent with within-team data — driver effects are small-to-moderate within a competitive team.

2. **A few drivers are exceptional.** Verstappen and Russell each show up as anchors in clusters of large negative gaps across multiple teammates. This is the kind of evidence that suggests "true" driver-level differences — when one driver beats *every* teammate by similar margins across years, it's hard to attribute to team treatment.

3. **The largest gaps come from weak drivers, not favoured drivers.** Mazepin, Latifi, Stroll-vs-Alonso, Ricciardo-at-McLaren — these are cases where one teammate was visibly underperforming. The "treatment asymmetry" interpretation is harder to sustain when you can identify specific drivers who just weren't good enough.

## What this means for your "test van Kesteren's assumption" framing

Honest read: **the data doesn't strongly support a favouritism story.** It supports a "drivers genuinely differ" story.

For your final report, the framing might shift to:

> "We test van Kesteren & Bergkamp's implicit assumption that within-team treatment is symmetric. Across 136 lineups, we find substantial variation in within-team gaps, but the pattern is most consistent with genuine driver-skill differences (with some drivers — notably Verstappen and Russell — beating multiple teammates by similar margins) rather than systematic team favouritism. The pit-stop and compound-allocation analyses [forthcoming] provide additional evidence on this question."

That's actually a stronger, more interesting claim than "we found favouritism!" — it directly addresses van Kesteren & Bergkamp's assumption and contributes empirical support for it, while also identifying the rare exceptions.

## What you should do next

1. **Compute Verstappen's gap vs each of his teammates separately and tabulate.** That single table will be one of the most striking things in your report.
2. **Same for Russell across his Williams years.**
3. **Move to the pit-stop analysis** to see if any team execution asymmetries exist independent of the lap-time gap.
4. **Start writing the methods section** — your data is now stable enough that the methodology won't change.

This is genuinely a strong dataset and you have a real story. Want help with the Verstappen-anchored table, or move to pit stops?

Verstappen
This is honestly extraordinary data. 16 lineups, 5 different teammates, spanning 2018-2025, all in (essentially) the same Red Bull car. Some observations:
Only one lineup shows him not faster. Red Bull 2018_A (RIC vs VER, +0.003 ± 0.065). That's Ricciardo's last year, when he was still genuinely competitive. Even there, the point estimate is dead even.
Every other lineup: Verstappen significantly faster. The gaps range from -0.26 (Pérez, peak Pérez) to -1.20 (Tsunoda, 2025). Mean -0.69, median -0.66 s/lap.
The pattern across teammates is intuitive:

vs Ricciardo (2018, established WDC contender): essentially equal, then -0.45 by year-end
vs Gasly (2019): -0.87 (Gasly was demoted mid-season; data confirms why)
vs Albon (2020): -0.96 (Albon also demoted)
vs Pérez (2022-24): -0.26 to -0.75 (Pérez initially close, then declined sharply)
vs Tsunoda (2025): -1.05 to -1.20 (modern Verstappen vs sub-elite teammate)

The 2018 data point is interesting. It shows Verstappen genuinely was on Ricciardo's level early on, and the relative gap grew as he matured. That's the right shape — it would be suspicious if a 20-year-old Verstappen had already been crushing a multi-time race winner.
Implication for your project: This is your single strongest piece of evidence that within-team gaps reflect driver skill rather than team treatment. If Red Bull were systematically favouring Verstappen with car/strategy/setup, you'd expect the gap to be roughly constant against any teammate. But it scales cleanly with teammate quality (small vs Ricciardo, huge vs Tsunoda). That's exactly the pattern you'd predict from "Verstappen is genuinely much faster" + "different teammates have different ability levels."
Russell at Williams
Tighter sample but same shape. Four lineups, all negative, gap shrinking over time:

2019 vs Kubica: -0.67 (Russell's rookie year, against an injured veteran on his last legs)
2020 vs Latifi: -0.42 (Russell second year, Latifi rookie)
2021 vs Latifi: -0.35 / -0.16 (both drivers in second/third year, gap narrowed)

The narrowing gap probably reflects Latifi getting marginally less terrible, not Russell getting slower. Worth noting that even when Latifi was at his most competitive, Russell was still significantly faster.

Hamilton
vs Bottas (2018-2021): consistent -0.20 to -0.43 advantage. Stable, large.
The 2021_C row is wild. Hamilton -0.73 vs Bottas in the second phase of 2021 (whatever the lineup phase split is — probably a small-sample artefact of how lineup phases got assigned to a few specific races). With 11 races though, it's not negligible.
vs Russell (2022-2024): essentially zero, sometimes slightly negative for Hamilton (-0.12 in 2023_A). 2024_A shows +0.075 — Hamilton was actually slower than Russell over a full 20-race sample. Modest but real.
vs Leclerc (2025): Hamilton +0.276 — Leclerc significantly faster than Hamilton at Ferrari. Confirms the early-2025 narrative that Hamilton struggled to adapt to the Ferrari.
So Hamilton's "edge" was really specific to Bottas. Against Russell he was even; against Leclerc he's been beaten. This is genuinely consistent with the "GOAT in decline" narrative without being inflammatory — just data.
Alonso
vs Vandoorne (2018): -0.53 then -0.17. Alonso utterly dominating his teammate.
vs Ocon (2021-22): much smaller gaps (-0.04 to -0.15). Ocon was a real challenge.
vs Stroll (2023-25): consistently large negative gaps (-0.23 to -0.59). Alonso destroying Stroll.
What's interesting: Alonso's gap to teammates scales with teammate quality, just like Verstappen's. Against a competent teammate (Ocon) he's modestly faster. Against a weaker one (Stroll, Vandoorne) he's much faster. Same pattern as Verstappen but smaller magnitude.
Leclerc
vs Vettel (2019-2020): Leclerc beat Vettel slightly in 2019 (+0.108 means Vettel faster — wait, check sign convention).
Actually let me re-examine. anchor_gap = "Leclerc minus teammate" by your function. So +0.108 means Leclerc slower than Vettel by 0.1 in 2019. That's correct — 2019 Vettel was actually still fast. Then 2020 (Ferrari's terrible car) Leclerc dominated -0.50.
vs Sainz (2021-2024): mostly small gaps in either direction, mostly within ±0.2. Two well-matched competitors.
vs Hamilton (2025): -0.28 — Leclerc significantly faster. Confirms the Hamilton-2025 finding.
What this means for your project
You now have a really clean version of the central story:

The largest within-team gaps come from drivers who are anchors against multiple weak teammates. The smallest come from pairs of competent professionals. There's no evidence of a single team systematically favouring one driver across multiple teammates — the gap pattern follows driver pairings, not team identity.

The "Verstappen at Red Bull" narrative is supported by Hamilton's, Alonso's, and Leclerc's data showing the same pattern: big drivers + weak teammates = big gaps; comparable drivers = small gaps.
This does support van Kesteren & Bergkamp's assumption (no major team-level treatment asymmetry). What it adds to the literature is showing the distribution of within-team gaps, identifying the rare exceptional cases (Verstappen, Russell-at-Williams), and demonstrating that gap magnitude scales with teammate-quality differences.