# ST312 Project: Understanding Performance Dynamics in Modern Formula 1

**Candidates:** 60276, 61881

## Overview

This project analyzes Formula 1 performance dynamics using comprehensive telemetry data from 2018-2024. We investigate three key research questions:

1. **Qualifying-Race Performance Correlation**: How does qualifying position predict race outcomes across different circuits and regulation eras?
2. **Intra-Team Performance Dynamics**: Is there statistical evidence of systematic performance differences between teammates?
3. **Tyre Strategy Optimization**: How do compound choices and degradation patterns affect race performance?

## Project Structure

```
st312 project/
├── README.md                              # This file
├── proposal.md                            # Detailed research proposal
├── requirements.txt                       # Python dependencies
├── data_utils.py                          # Data loading utilities
├── f1_cache/                             # FastF1 cached data (gitignored)
├── RQ1_qualifying_race_correlation.ipynb  # Research Question 1 analysis
├── RQ2_intraTeam_dynamics.ipynb          # Research Question 2 analysis
└── RQ3_tyre_strategy.ipynb               # Research Question 3 analysis
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

**Required libraries:**
- `fastf1>=3.7.0` - Formula 1 data access
- `pandas>=2.3.0` - Data manipulation
- `numpy>=1.26.0` - Numerical computing
- `matplotlib>=3.9.0` - Plotting
- `seaborn>=0.13.0` - Statistical visualization
- `scipy>=1.15.0` - Statistical functions
- `jupyter>=1.1.0` - Notebook environment

### 2. Data Collection

The first time you run any notebook, FastF1 will download and cache race data. This may take:
- **RQ1**: 10-20 minutes (qualifying + race results)
- **RQ2**: 15-25 minutes (lap-by-lap timing data)
- **RQ3**: Uses RQ2 data (faster if already cached)

Data is cached in `f1_cache/` directory for subsequent runs.

### 3. Running the Notebooks

Start Jupyter:
```bash
jupyter notebook
```

Then open notebooks in order:
1. `RQ1_qualifying_race_correlation.ipynb` - Qualifying vs race analysis
2. `RQ2_intraTeam_dynamics.ipynb` - Teammate comparisons
3. `RQ3_tyre_strategy.ipynb` - Tyre degradation analysis

## Research Questions

### RQ1: Qualifying-Race Performance Correlation

**Question:** What is the relationship between qualifying session performance metrics and final race standings across different circuits, seasons, and regulatory eras?

**Key Analyses:**
- Spearman correlation between qualifying and race positions
- Circuit-type comparisons (street, high-speed, technical)
- Pole position conversion rates
- 2022 regulation impact assessment

**Expected Findings:**
- Strong correlation (ρ > 0.70) overall
- Variation by circuit type (Monaco > Monza)
- Potential weakening in 2022+ due to overtaking-friendly regulations

### RQ2: Intra-Team Performance Dynamics

**Question:** Does statistical evidence from lap times, pit stop timing, and tyre allocation indicate systematic performance differences between teammates?

**Key Analyses:**
- Lap time distribution comparisons
- Pit stop timing and frequency
- Tyre compound allocation patterns
- Stint length strategies

**Expected Findings:**
- Identify teams with systematic performance gaps
- Reveal potential resource allocation differences
- Quantify teammate performance deltas

### RQ3: Tyre Strategy Optimization

**Question:** How do tyre compound choices, degradation patterns, and pit stop timing affect race performance?

**Key Analyses:**
- Degradation curves by compound (SOFT, MEDIUM, HARD)
- Optimal stint lengths
- Circuit-specific compound performance
- Driver-specific tyre management abilities

**Expected Findings:**
- Quantify degradation rates per compound
- Identify optimal pit windows
- Classify drivers by tyre management skill

## Data Source

**FastF1** (https://docs.fastf1.dev/)
- Official FIA timing transponder data
- Real-time broadcast data archived in FastF1 database
- Coverage: 2018-2024 (focusing on 2022-2024 for current regulations)
- Granularity: Lap-by-lap for each driver in every session

**Data Volume (2022-2024):**
- ~72 races × 20 drivers × ~60 laps = ~86,400 lap observations
- Plus qualifying sessions, practice sessions, and telemetry data

## Methodology

### Current Phase: Exploratory Data Analysis (EDA)

This implementation focuses on **visualization and descriptive statistics**:
- Data loading and preprocessing
- Correlation analysis
- Distribution comparisons
- Trend visualization
- Descriptive statistics

### Future Phase: Statistical Modeling

Planned advanced analyses (beyond EDA):
- **RQ1**: Ordinal logistic regression with multilevel structure
- **RQ2**: Linear mixed effects models, paired t-tests, chi-square tests
- **RQ3**: Mixed effects models with interaction terms, driver clustering

## Utility Functions (data_utils.py)

The `data_utils.py` module provides:

### Data Loading Functions
- `load_qualifying_race_data(years)` - RQ1 data
- `load_teammate_data(years)` - RQ2 lap timing data
- `load_tyre_strategy_data(years)` - RQ3 tyre data
- `get_pit_stop_data(years)` - Pit stop timing

### Helper Functions
- `classify_circuit(circuit_name)` - Categorize circuit types
- `get_team_pairs(df)` - Identify teammate relationships
- `calculate_position_correlation(df)` - Spearman/Pearson correlations
- `print_data_summary(df)` - Display data overview

### Circuit Classification
- **Street**: Monaco, Singapore, Baku, Jeddah, Miami, Las Vegas
- **High-speed**: Monza, Spa, Silverstone, Suzuka, Red Bull Ring
- **Technical**: Barcelona, Hungaroring, COTA, Abu Dhabi, etc.

## Expected Outputs

Each notebook generates:
1. **Visualizations**: Charts, histograms, scatter plots, box plots
2. **Statistical summaries**: Correlation coefficients, descriptive stats
3. **Data exports**: Cleaned CSV files for further analysis
   - `data_rq1_qualifying_race.csv`
   - `data_rq2_lap_times.csv`
   - `data_rq2_pitstops.csv`
   - `data_rq3_tyre_strategy.csv`
   - `data_rq3_stint_analysis.csv`

## Key Findings (Preliminary)

*To be populated after running analyses*

## Literature References

See `proposal.md` for complete literature review.

**Key papers:**
- Weissbock & Mills (2025) - Qualifying predictive power
- Van Kesteren & Bergkamp (2023) - Bayesian multilevel models
- Bell et al. (2016) - Car vs driver performance decomposition
- Aguad & Thraves (2024) - Pit stop timing optimization

## Notes

- **Data caching**: First run downloads extensive data; subsequent runs are much faster
- **Missing data**: Crashes, retirements, and sensor failures may result in incomplete data
- **RQ3 flexibility**: May be modified or removed based on findings from RQ1 and RQ2
- **Time range**: Currently focused on 2022-2024 (ground-effect era); can extend to 2018-2021 for regulation comparisons

## Troubleshooting

### Import Errors
If you encounter import errors:
```bash
pip install --upgrade -r requirements.txt
```

### Data Loading Failures
- Check internet connection (required for first download)
- Ensure `f1_cache/` directory exists and is writable
- Some races may have incomplete data (COVID-affected seasons, Sprint races)

### Slow Performance
- First run will be slow due to data downloading
- Consider starting with a single year (e.g., 2024 only) for testing
- Use cached data by running cells sequentially

## Contributing

This is an academic project for ST312. For questions or issues:
- Review the `proposal.md` for detailed methodology
- Check FastF1 documentation: https://docs.fastf1.dev/
- Consult course materials for statistical modeling approaches

## License

Academic use only - ST312 Project, University of Warwick

---

**Last updated:** December 2024
