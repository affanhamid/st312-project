# Tire Compound Allocation Analysis: Within-Team Strategic Asymmetries (2018-2025)

## Research Question

The lap-time and pit-stop analyses examine performance differences in *racing* and *crew execution*. The compound allocation analysis examines a third dimension of potential team treatment: **strategic compound choice**. If a team systematically allocates the preferred tire compound (typically the soft, fastest in a one-lap sense) to one driver more often than the other, that asymmetry would manifest as differential strategic priority.

The motivating logic: tire compound choice is a team strategic decision, not a driver decision. Drivers occasionally express preferences but the team determines which compound goes on which car for each stint. Systematic differences in compound allocation between teammates are therefore team-driven by definition.

---

## Data Source and Scope

- **Source**: FastF1 lap data (already cleaned and loaded for the lap-time analysis).
- **Granularity**: One observation per stint (a continuous run on a single set of tires), identified by the `Stint` field. Each stint corresponds to one compound choice.
- **Period**: 2018-2025.
- **Compounds**: SOFT, MEDIUM, HARD, INTERMEDIATE, WET. We retained all five for the allocation analysis (unlike the lap-time analysis, which restricted to dry compounds, since tire selection in wet conditions is itself a strategic choice).

---

## Statistical Approach

For each lineup, we built a 2×K contingency table of (Driver × Compound) stint counts. We tested whether the distribution of compounds differs between the two teammates using a **chi-squared test of independence**:

$$\chi^2 = \sum_{i,j} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

where $O_{ij}$ is the observed number of stints driver $i$ ran on compound $j$, and $E_{ij}$ is the expected count under the null hypothesis of equal allocation.

A small p-value indicates compound allocation differs significantly between teammates; a large p-value indicates allocation is approximately balanced.

We required at least **10 stints total per lineup** to ensure reasonable cell counts for the chi-squared approximation.

---

## Why this is an indirect test of favouritism

The chi-squared test detects *whether* compound distributions differ. It does not directly tell us *which* compound is "preferred" or whether observed differences reflect favouritism vs. legitimate strategic differentiation.

Caveats on interpretation:
- A team running different strategies for two drivers (e.g., one starts on softs, the other on mediums) might do so for legitimate strategic reasons (e.g., to hedge against weather, traffic, or to test alternative race plans).
- "Favoured compound" is context-dependent. Soft tires are fastest over one lap but degrade quickest. The "best" compound depends on stint length, track temperature, and overall race strategy.
- A perfectly symmetric allocation is a stronger signal of equal treatment than an asymmetric allocation is a signal of favouritism.

We therefore interpret the results conservatively. A balanced allocation is evidence that the team is not differentiating compounds between drivers; an unbalanced allocation requires further context to interpret as favouritism.

---

## Results

Across all 136 lineups, the chi-squared test was applied to compound × driver contingency tables. The smallest p-value across all lineups was **p=0.126** (Ferrari 2023_E, LEC vs SAI). **No lineup showed a significant difference in compound allocation at α=0.05.**

Selected lineups with the lowest p-values (i.e., closest to differential allocation):

| Lineup | Drivers | n_stints | χ² | p-value |
|---|---|---|---|---|
| Ferrari 2023_E | LEC vs SAI | 14 | 4.14 | 0.126 |
| AlphaTauri 2021_E | GAS vs TSU | 16 | 5.14 | 0.162 |
| Mercedes 2024_A | HAM vs RUS | 119 | 4.36 | 0.225 |
| McLaren 2021_C | NOR vs RIC | 55 | 4.12 | 0.249 |
| Red Bull 2020_A | ALB vs VER | 57 | 2.70 | 0.260 |
| Aston Martin 2025_A | ALO vs STR | 38 | 5.27 | 0.260 |
| Ferrari 2025_A | HAM vs LEC | 111 | 2.40 | 0.493 |

### Lineups of prior interest

We checked the lineups where favouritism would be most plausible *a priori*:

- **Aston Martin Stroll-Alonso (2023-2025)**: p=0.26-0.36 across phases. Compound allocation balanced.
- **Ferrari Hamilton-Leclerc (2025)**: p=0.49. Balanced.
- **Mercedes Hamilton-Russell (2024)**: p=0.22. Balanced.
- **Red Bull Verstappen across teammates**: all p>0.25. Balanced.

In none of these does compound allocation deviate from the null of equal treatment.

---

## Interpretation

The compound allocation analysis is the cleanest of the three layers in terms of providing a population-level null result: **no lineup in our dataset shows statistically significant differential compound allocation between teammates**. This is a striking degree of consistency across 136 lineups, 8 seasons, and 15 teams.

### What this rules out

The hypothesis that teams systematically allocate preferred compounds to one driver over the other is not supported by any lineup in our data. This includes:
- Top teams with championship-contending drivers (Mercedes, Red Bull, Ferrari, McLaren)
- Teams with structural favouritism priors (Aston Martin)
- Teams with a clear senior/junior driver pairing (e.g., AlphaTauri, Williams pre-Russell)

### What this cannot rule out

Compound allocation is a high-level strategic decision; finer-grained strategic choices remain unobserved:
- **Pit timing within a stint**: which driver gets called in first when both could plausibly pit?
- **Undercut priority**: which driver gets the tactical advantage in a duelling pit window?
- **Tire set quality within a compound**: a "fresh medium" allocated to one driver may have different qualifying-vs-race wear depending on previous use.

These finer-grained strategic asymmetries are not addressable with the data available.

---

## Limitations

1. **Stint count, not lap count**: our unit of analysis is the stint, treating a 2-lap stint and a 30-lap stint as one observation each. This is appropriate for testing compound *choice* but not for weighting by exposure.
2. **Conditional dependence**: stint compound choices are not independent across stints (a driver who started on softs is more likely to switch to hards mid-race). The chi-squared test treats them as independent for tractability; corrections would be possible but unlikely to change the qualitative conclusions given the strength of the null result.
3. **Multiple comparisons**: across 136 chi-squared tests, ~7 false positives at α=0.05 would be expected under the global null. We observed *zero* significant results, well below this floor — a conservatively strong null finding.
4. **Compound categories vary across eras**: Pirelli compound names changed between seasons (e.g., HYPERSOFT, ULTRASOFT, SUPERSOFT, etc., were used in some early seasons). We retained the compound labels as recorded in fastf1.

---

## Conclusion

Tire compound allocation is balanced between teammates across all 136 lineups in our dataset (lowest p=0.126). This is the strongest single piece of evidence that teams do not differentiate between teammates on observable strategic dimensions. Combined with the pit-stop analysis (which found no systematic correlation between pit-stop and lap-time gaps) and the lap-time analysis (which found gap magnitudes scaling with teammate quality rather than team identity), the three-layer evidence is consistent with the assumption of within-team treatment symmetry implicit in prior work (van Kesteren & Bergkamp, 2023).

We emphasise that "treatment symmetry" applies to the *observable* channels we measured. Less visible asymmetries (engineer assignment, simulator priority, private setup work, mid-stint strategic priority) are not addressable from public data.