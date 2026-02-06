"""
Create a presentation-ready figure for RQ2: Intra-Team Performance Dynamics

This script generates a high-quality visualization showing lap time differences
between teammates across different F1 teams.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

import data_utils as du

# Set style for publication-quality figures
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Configuration
YEARS = [2022, 2023, 2024]
FIGURE_SIZE = (16, 10)
DPI = 300

print("="*80)
print("RQ2: Creating Presentation Figure - Teammate Performance Comparison")
print("="*80)

# Load data
print("\nLoading lap timing data...")
print("Note: This will use cached data if available.\n")
laps_df = du.load_teammate_data(YEARS)

# Filter to valid lap times only
valid_laps = laps_df[laps_df['lap_time'].notna()].copy()
print(f"Valid lap observations: {len(valid_laps):,}")

# Get teammate pairs
team_pairs = du.get_team_pairs(valid_laps)
print(f"Teams analyzed: {len(team_pairs)}")

# Calculate teammate lap time differences
teammate_diffs = []

for team, drivers in team_pairs.items():
    if len(drivers) < 2:
        continue

    # Take first two drivers (main teammates)
    for i in range(min(len(drivers), 2)):
        for j in range(i+1, min(len(drivers), 2)):
            driver1, driver2 = drivers[i], drivers[j]

            d1_laps = valid_laps[valid_laps['driver'] == driver1]['lap_time']
            d2_laps = valid_laps[valid_laps['driver'] == driver2]['lap_time']

            if len(d1_laps) > 100 and len(d2_laps) > 100:  # Minimum data requirement
                diff = d1_laps.mean() - d2_laps.mean()

                teammate_diffs.append({
                    'team': team,
                    'driver1': driver1,
                    'driver2': driver2,
                    'driver1_mean': d1_laps.mean(),
                    'driver2_mean': d2_laps.mean(),
                    'time_diff_sec': abs(diff),
                    'faster_driver': driver1 if diff < 0 else driver2,
                    'slower_driver': driver2 if diff < 0 else driver1,
                    'n_laps_d1': len(d1_laps),
                    'n_laps_d2': len(d2_laps)
                })

teammate_diff_df = pd.DataFrame(teammate_diffs)
teammate_diff_df = teammate_diff_df.sort_values('time_diff_sec', ascending=False)

print(f"\nTeammate pairs with sufficient data: {len(teammate_diff_df)}")

# ============================================================================
# CREATE PRESENTATION FIGURE
# ============================================================================

print("\nCreating presentation figure...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIGURE_SIZE)

# LEFT PLOT: Teammate lap time gap by team
# ============================================================================

# Select top teams with biggest gaps
top_n = min(10, len(teammate_diff_df))
top_teams = teammate_diff_df.head(top_n).copy()

# Create labels with driver names
labels = [f"{row['team']}\n({row['faster_driver']} vs {row['slower_driver']})"
          for _, row in top_teams.iterrows()]

# Color based on gap size
colors = plt.cm.RdYlGn_r(np.linspace(0.3, 0.9, len(top_teams)))

bars = ax1.barh(range(len(top_teams)), top_teams['time_diff_sec'],
                color=colors, edgecolor='black', linewidth=1.5)

# Add value labels on bars
for i, (bar, val) in enumerate(zip(bars, top_teams['time_diff_sec'])):
    ax1.text(val + 0.01, bar.get_y() + bar.get_height()/2,
            f'{val:.3f}s',
            va='center', ha='left', fontsize=10, fontweight='bold')

ax1.set_yticks(range(len(top_teams)))
ax1.set_yticklabels(labels, fontsize=10)
ax1.set_xlabel('Average Lap Time Difference (seconds)', fontsize=13, fontweight='bold')
ax1.set_title('Teammate Performance Gap: Top 10 Teams\n(2022-2024)',
              fontsize=15, fontweight='bold', pad=20)
ax1.grid(True, alpha=0.3, axis='x')
ax1.axvline(0.1, color='red', linestyle='--', linewidth=2, alpha=0.5,
           label='0.1s threshold')
ax1.legend(fontsize=11)

# Add interpretation text
ax1.text(0.98, 0.02,
         'Larger gaps suggest systematic\nperformance differences',
         transform=ax1.transAxes,
         fontsize=10, style='italic',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
         verticalalignment='bottom', horizontalalignment='right')

# RIGHT PLOT: Distribution of teammate gaps across all teams
# ============================================================================

# Histogram with KDE overlay
ax2.hist(teammate_diff_df['time_diff_sec'], bins=20,
         edgecolor='black', alpha=0.7, color='steelblue', density=True)

# Add KDE curve
from scipy import stats as sp_stats
kde_x = np.linspace(teammate_diff_df['time_diff_sec'].min(),
                     teammate_diff_df['time_diff_sec'].max(), 200)
kde = sp_stats.gaussian_kde(teammate_diff_df['time_diff_sec'])
ax2.plot(kde_x, kde(kde_x), 'r-', linewidth=3, label='Density curve')

# Add vertical lines for statistics
mean_gap = teammate_diff_df['time_diff_sec'].mean()
median_gap = teammate_diff_df['time_diff_sec'].median()

ax2.axvline(mean_gap, color='orange', linestyle='--', linewidth=2.5,
           label=f'Mean: {mean_gap:.3f}s')
ax2.axvline(median_gap, color='green', linestyle='--', linewidth=2.5,
           label=f'Median: {median_gap:.3f}s')

ax2.set_xlabel('Lap Time Difference (seconds)', fontsize=13, fontweight='bold')
ax2.set_ylabel('Density', fontsize=13, fontweight='bold')
ax2.set_title('Distribution of Teammate Performance Gaps\nAcross All Teams',
              fontsize=15, fontweight='bold', pad=20)
ax2.legend(fontsize=11, loc='upper right')
ax2.grid(True, alpha=0.3)

# Add summary statistics box
stats_text = f"""Summary Statistics:
Mean Gap: {mean_gap:.3f}s
Median Gap: {median_gap:.3f}s
Std Dev: {teammate_diff_df['time_diff_sec'].std():.3f}s
Max Gap: {teammate_diff_df['time_diff_sec'].max():.3f}s
Teams: {len(teammate_diff_df)}"""

ax2.text(0.98, 0.97, stats_text,
         transform=ax2.transAxes,
         fontsize=10, family='monospace',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8),
         verticalalignment='top', horizontalalignment='right')

# Overall figure title
fig.suptitle('Research Question 2: Intra-Team Performance Dynamics in Formula 1 (2022-2024)',
             fontsize=17, fontweight='bold', y=0.98)

# Methods section at top
methods_text = """METHODS: Linear mixed effects models with nested random effects for drivers and teams.
Comparing lap time distributions, pit stop timing, and tyre allocation between teammates.
Paired t-tests and chi-square tests for systematic differences."""

fig.text(0.5, 0.94,
         methods_text,
         ha='center', fontsize=11,
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lightblue', alpha=0.3, edgecolor='navy', linewidth=2),
         wrap=True)

# Expected findings at bottom
expected_text = """EXPECTED FINDINGS: We anticipate identifying teams with systematic performance gaps >0.1s per lap,
revealing potential resource allocation differences. We expect to find evidence of favoritism through faster pit stops
and preferential tyre strategies for championship contenders. Statistical significance will indicate whether observed
gaps are due to driver skill or systematic team support differences."""

fig.text(0.5, 0.02,
         expected_text,
         ha='center', fontsize=11,
         bbox=dict(boxstyle='round,pad=0.8', facecolor='lightyellow', alpha=0.4, edgecolor='darkred', linewidth=2),
         wrap=True)

# Data source footer
fig.text(0.5, -0.01,
         'Data Source: FastF1 | ST312 Project - Candidates: 60276, 61881',
         ha='center', fontsize=9, style='italic', color='gray')

plt.tight_layout(rect=[0, 0.06, 1, 0.92])

# Save figure
output_file = 'RQ2_presentation_figure.png'
plt.savefig(output_file, dpi=DPI, bbox_inches='tight', facecolor='white')
print(f"\n✓ Figure saved as: {output_file}")
print(f"  Resolution: {FIGURE_SIZE[0]*DPI} x {FIGURE_SIZE[1]*DPI} pixels")
print(f"  DPI: {DPI}")

# Also save as PDF for vector graphics (scalable)
output_pdf = 'RQ2_presentation_figure.pdf'
plt.savefig(output_pdf, bbox_inches='tight', facecolor='white')
print(f"  PDF version: {output_pdf}")

plt.show()

print("\n" + "="*80)
print("KEY INSIGHTS FROM FIGURE:")
print("="*80)
print(f"1. Average teammate gap: {mean_gap:.3f} seconds per lap")
print(f"2. Largest gap: {teammate_diff_df.iloc[0]['time_diff_sec']:.3f}s ({teammate_diff_df.iloc[0]['team']})")
print(f"3. Smallest gap: {teammate_diff_df.iloc[-1]['time_diff_sec']:.3f}s ({teammate_diff_df.iloc[-1]['team']})")
print(f"4. {(teammate_diff_df['time_diff_sec'] > 0.1).sum()} out of {len(teammate_diff_df)} teams show gaps >0.1s")
print(f"5. Distribution shows {'substantial' if teammate_diff_df['time_diff_sec'].std() > 0.1 else 'moderate'} variation across teams")
print("="*80)
