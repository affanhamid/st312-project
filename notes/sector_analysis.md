# Sector Decomposition Analysis: Where the Gaps Live (2018-2025)

## Research Question

The lap-time analysis estimated within-team gaps as a single coefficient per lineup. This summary tells us *whether* and *how large* a gap exists, but not *where* in the lap it occurs. The sector decomposition analysis breaks the lap-time gap into its three constituent sector contributions (Sector 1, Sector 2, Sector 3) to characterise the structural pattern of within-team performance differences.

This analysis serves a different role from the lap-time, pit-stop, and compound-allocation analyses. Those address *whether* gaps reflect skill or treatment. The sector decomposition addresses *what kind* of gap exists when one is present — adding interpretive depth to the headline lap-time finding rather than testing the favouritism question directly.

---

## Data

We extracted Sector1Time, Sector2Time, and Sector3Time alongside lap-level data from FastF1 for four selected lineups, chosen to span the range of patterns observed:

- **Mercedes 2019 (Hamilton vs Bottas)**: large lap-time gap (-0.20 s/lap)
- **Mercedes 2023 (Hamilton vs Russell, phases A and C)**: small to near-zero lap-time gap
- **Red Bull 2024 (Verstappen vs Pérez, phases B and D)**: very large lap-time gap (-0.58 to -0.84 s/lap)
- **Aston Martin 2024 (Alonso vs Stroll, phases A and C)**: moderate lap-time gap (+0.25 s/lap)

Same cleaning filters as the lap-time analysis: dry compounds only, green-flag laps, no pit in/out laps, statistical outlier exclusion, minimum 20 valid laps per driver per race.

---

## Statistical Model

For each lineup, we fitted four mixed-effects models — one per sector and one for the full lap time:

$$\text{SectorTime}_i = \beta_0 + \beta_1 \text{TyreLife}_i + \beta_2 \text{LapNumber}_i + \beta_3 \mathbb{1}[\text{Compound = Medium}]_i + \beta_4 \mathbb{1}[\text{Compound = Hard}]_i + \beta_5 \mathbb{1}[\text{IsDriver2}]_i + u_{\text{race}(i)} + \varepsilon_i$$

Same fixed and random effects as the main lap-time analysis. The coefficient on `IsDriver2` for each sector is the systematic within-lineup gap *for that sector specifically*, in seconds.

### Sanity check: sector coefficients sum to lap-time coefficient

Lap time is by construction the sum of the three sector times. If our models are well-specified, the sector IsDriver2 coefficients should sum to the lap-time IsDriver2 coefficient. Across our four lineups, the sums match the lap totals to within 0.001s — confirming the decomposition is consistent.

---

## Results

### Mercedes 2019: Hamilton-Bottas

| Sector | Coefficient | 95% CI | Share of lap gap |
|---|---|---|---|
| S1 | -0.028 | [-0.050, -0.006] | 14% |
| S2 | -0.043 | [-0.075, -0.011] | 21% |
| S3 | -0.132 | [-0.161, -0.102] | 65% |
| **Lap** | **-0.202** | **[-0.268, -0.136]** | 100% |

**~65% of Hamilton's advantage was concentrated in Sector 3** — typically the final sector containing high-speed corners and the start-finish straight. This is consistent with Hamilton's reputation for late-braking and aggressive final-sector pace.

### Red Bull 2024: Verstappen-Pérez

| Phase | S1 | S2 | S3 | Lap |
|---|---|---|---|---|
| Phase B | -0.149 (26%) | -0.266 (46%) | -0.169 (29%) | -0.583 |
| Phase D | -0.200 (24%) | -0.421 (50%) | -0.221 (26%) | -0.842 |

**~50% of Verstappen's advantage was in Sector 2** — typically the technical, mid-speed sector with complex corner sequences. The pattern is stable across phases B and D (same shape, different magnitudes), indicating a reproducible cornering-pace advantage rather than circuit- or phase-specific noise.

### Mercedes 2023: Hamilton-Russell

| Phase | S1 | S2 | S3 | Lap |
|---|---|---|---|---|
| Phase A | +0.070 | +0.025 | +0.060 | +0.155 (Russell faster) |
| Phase C | -0.049 | +0.061 | +0.029 | +0.041 (negligible) |

In phase A, Russell's 0.16 s/lap advantage was distributed roughly evenly across S1 and S3 with little contribution from S2. In phase C, where the lap-level gap is essentially zero, **Hamilton was 0.05 s/lap faster in Sector 1, while Russell was 0.06 s/lap faster in Sector 2** — the two drivers had genuinely different sector strengths that cancelled at the lap level. A pure lap-time analysis would miss this style asymmetry entirely.

### Aston Martin 2024: Alonso-Stroll

| Sector | Coefficient | Share of lap gap |
|---|---|---|
| S1 | +0.083 | 33% |
| S2 | +0.088 | 35% |
| S3 | +0.078 | 31% |
| **Lap** | **+0.249** | 100% |

Stroll's deficit was distributed **almost perfectly evenly across all three sectors** (~31-35% each). There is no specific sector weakness; the deficit is uniform.

---

## Interpretation

### Sector decomposition reveals interpretable patterns

Each lineup shows a distinct sector signature:

- **Hamilton's edge over Bottas**: concentrated in Sector 3 (high-speed corners + straights)
- **Verstappen's edge over Pérez**: concentrated in Sector 2 (technical mid-speed corners)
- **Hamilton vs Russell 2023 phase C**: cancelling sector strengths (Hamilton in S1, Russell in S2)
- **Alonso vs Stroll**: uniform deficit across all sectors

These patterns are interpretable as driving-style differences: Hamilton attacks final-sector cornering speed; Verstappen excels in mid-speed technical corners; Russell and Hamilton have complementary strengths; Stroll is uniformly slower without specific sector weakness.

### Implications for the favouritism question

If lap-time gaps were primarily driven by team-level treatment (setup, equipment, strategy), we might expect *uniform* sector distributions across all lineups (since favouritism would not be sector-specific). We observe heterogeneous, driver-specific sector signatures instead — different lineups show qualitatively different decompositions. This is more consistent with **driving-style heterogeneity** than with **uniform team-level treatment asymmetry**.

The Aston Martin case — uniform across sectors — is the closest to what favouritism would look like. However, "uniform sector deficit" is also what general skill differences look like, so the pattern is ambiguous between the two interpretations and does not on its own indicate favouritism.

### What sector decomposition adds to the overall analysis

Sector decomposition is a *characterisation* tool, not an evidentiary one for favouritism. The lap-time, pit-stop, and compound-allocation analyses already address whether team treatment is asymmetric. The sector analysis tells us, given that within-team gaps exist, what their structural shape is — providing interpretable detail consistent with skill-based explanations.

---

## Limitations

1. **Small sample of lineups**: only 4 lineups (8 phases) were decomposed. The patterns observed are illustrative, not population-level.
2. **Sector definitions vary by circuit**: Sector 1 at Monza is structurally different from Sector 1 at Monaco. Within-lineup conclusions average over all circuits a lineup raced on; circuit-specific analysis would require finer-grained decomposition.
3. **Sectors are not mechanistically interpretable**: "Sector 2 is mid-speed corners" is approximate. A full mechanistic decomposition would require corner-by-corner analysis (e.g., from telemetry speed/throttle/brake traces), beyond the scope of this study.

---

## Conclusion

Sector decomposition of within-team gaps reveals interpretable, driver-specific patterns: Hamilton's advantage at Mercedes was concentrated in the final sector; Verstappen's at Red Bull in the technical middle sector; Stroll's deficit at Aston Martin was uniform across all sectors. These patterns are most consistent with driving-style differences as the source of within-team gaps. The Mercedes 2023 phase C case — where Hamilton and Russell had cancelling sector strengths producing a near-zero lap gap — illustrates that lap-level summaries can obscure substantive performance differences when teammates have complementary skills.

This analysis supplements the main favouritism findings (no concordant pit-stop or compound allocation asymmetries) by adding interpretive structure to the lap-time gaps it identified.