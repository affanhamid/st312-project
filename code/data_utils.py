"""
Data Loading and Processing Utilities for F1 Analysis
ST312 Project - Candidates: 60276, 61881

This module provides helper functions for loading and preprocessing Formula 1 data
using the FastF1 library for the three research questions.
"""

import fastf1
import pandas as pd
import numpy as np
from typing import List, Dict, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

# Enable FastF1 cache
fastf1.Cache.enable_cache('f1_cache')


# ============================================================================
# CIRCUIT CLASSIFICATION
# ============================================================================

CIRCUIT_TYPES = {
    'street': [
        'Monaco', 'Singapore', 'Baku', 'Jeddah', 'Miami', 'Las Vegas',
        'Azerbaijan', 'Saudi Arabia'
    ],
    'high_speed': [
        'Monza', 'Spa', 'Silverstone', 'Suzuka', 'Red Bull Ring',
        'Austria', 'Belgium', 'Italy', 'Japan', 'United Kingdom'
    ],
    'technical': [
        'Barcelona', 'Hungaroring', 'Zandvoort', 'Circuit of the Americas',
        'Spain', 'Hungary', 'Netherlands', 'United States', 'Mexico',
        'Brazil', 'Abu Dhabi', 'Bahrain', 'Australia', 'Qatar', 'China'
    ]
}


def classify_circuit(circuit_name: str) -> str:
    """
    Classify circuit into street, high_speed, or technical based on name.

    Args:
        circuit_name: Name of the circuit or country

    Returns:
        Circuit type: 'street', 'high_speed', or 'technical'
    """
    for circuit_type, circuits in CIRCUIT_TYPES.items():
        if any(c.lower() in circuit_name.lower() for c in circuits):
            return circuit_type
    return 'technical'  # Default to technical if unknown


# ============================================================================
# DATA LOADING FUNCTIONS
# ============================================================================

def get_race_schedule(year: int) -> pd.DataFrame:
    """
    Get the race schedule for a given year.

    Args:
        year: Year to get schedule for (2018-2024)

    Returns:
        DataFrame with race schedule information
    """
    try:
        schedule = fastf1.get_event_schedule(year)
        return schedule
    except Exception as e:
        print(f"Error loading schedule for {year}: {e}")
        return pd.DataFrame()


def load_session(year: int, race_name: str, session_type: str = 'R',
                 load_laps: bool = True, load_telemetry: bool = False) -> Optional[fastf1.core.Session]:
    """
    Load a specific session with error handling.

    Args:
        year: Year of the race
        race_name: Name or round number of the race
        session_type: 'FP1', 'FP2', 'FP3', 'Q', 'S', 'R' (Race)
        load_laps: Whether to load lap data (required for RQ2, RQ3)
        load_telemetry: Whether to load telemetry data (optional, increases load time)

    Returns:
        Session object or None if loading fails
    """
    try:
        session = fastf1.get_session(year, race_name, session_type)
        session.load(laps=load_laps, telemetry=load_telemetry)
        return session
    except Exception as e:
        print(f"Error loading {year} {race_name} {session_type}: {e}")
        return None


def load_qualifying_race_data(years: List[int]) -> pd.DataFrame:
    """
    Load qualifying and race data for multiple years (RQ1).

    Args:
        years: List of years to load (e.g., [2022, 2023, 2024])

    Returns:
        DataFrame with columns: year, race, driver, team, quali_pos, race_pos,
                               circuit_type, grid_position
    """
    all_data = []

    for year in years:
        print(f"\nLoading {year} season data...")
        schedule = get_race_schedule(year)

        if schedule.empty:
            continue

        # Filter to only race events (exclude testing, sprint qualifying, etc.)
        races = schedule[schedule['EventFormat'] != 'testing']

        for idx, race in races.iterrows():
            race_name = race['EventName']
            print(f"  Processing {race_name}...", end=' ')

            # Load qualifying session (no laps needed, just results)
            quali = load_session(year, race_name, 'Q', load_laps=False)
            if quali is None:
                print("Quali failed")
                continue

            # Load race session (no laps needed, just results)
            race_session = load_session(year, race_name, 'R', load_laps=False)
            if race_session is None:
                print("Race failed")
                continue

            # Get results
            quali_results = quali.results
            race_results = race_session.results

            # Merge qualifying and race positions
            for driver in quali_results['Abbreviation']:
                try:
                    quali_pos = quali_results[quali_results['Abbreviation'] == driver]['Position'].values[0]
                    race_pos = race_results[race_results['Abbreviation'] == driver]['Position'].values[0]
                    team = quali_results[quali_results['Abbreviation'] == driver]['TeamName'].values[0]

                    # Skip if positions are invalid
                    if pd.isna(quali_pos) or pd.isna(race_pos):
                        continue

                    all_data.append({
                        'year': year,
                        'race': race_name,
                        'driver': driver,
                        'team': team,
                        'quali_pos': int(quali_pos),
                        'race_pos': int(race_pos),
                        'grid_pos': int(quali_pos),  # Grid position (may differ due to penalties)
                        'circuit_type': classify_circuit(race_name),
                        'position_change': int(race_pos) - int(quali_pos)
                    })
                except Exception as e:
                    continue

            print("✓")

    df = pd.DataFrame(all_data)
    print(f"\nLoaded {len(df)} driver-race observations")
    return df


def load_teammate_data(years: List[int]) -> pd.DataFrame:
    """
    Load lap time and pit stop data for teammate comparisons (RQ2).

    Args:
        years: List of years to load

    Returns:
        DataFrame with lap times, pit stops, tyre data by driver
    """
    all_laps = []

    for year in years:
        print(f"\nLoading {year} season lap data...")
        schedule = get_race_schedule(year)

        if schedule.empty:
            continue

        races = schedule[schedule['EventFormat'] != 'testing']

        for idx, race in races.iterrows():
            race_name = race['EventName']
            print(f"  Processing {race_name}...", end=' ')

            race_session = load_session(year, race_name, 'R')
            if race_session is None:
                print("Failed")
                continue

            # Get all laps
            laps = race_session.laps

            # Filter out invalid laps (pit laps, safety car, etc.)
            laps = laps[laps['IsAccurate'] == True]

            for idx, lap in laps.iterrows():
                try:
                    all_laps.append({
                        'year': year,
                        'race': race_name,
                        'driver': lap['Driver'],
                        'team': lap['Team'],
                        'lap_number': lap['LapNumber'],
                        'lap_time': lap['LapTime'].total_seconds() if pd.notna(lap['LapTime']) else None,
                        'compound': lap['Compound'],
                        'tyre_life': lap['TyreLife'],
                        'stint': lap['Stint'],
                        'track_status': lap['TrackStatus'],
                        'is_personal_best': lap['IsPersonalBest']
                    })
                except Exception as e:
                    continue

            print("✓")

    df = pd.DataFrame(all_laps)
    print(f"\nLoaded {len(df)} lap observations")
    return df


def load_tyre_strategy_data(years: List[int]) -> pd.DataFrame:
    """
    Load tyre compound, degradation, and stint data (RQ3).

    Args:
        years: List of years to load

    Returns:
        DataFrame with tyre strategy information
    """
    # For now, this uses the same data as teammate analysis
    # but we can add additional telemetry features later
    laps_df = load_teammate_data(years)

    # Filter to only include laps with valid tyre data
    tyre_df = laps_df[laps_df['compound'].notna()].copy()

    # Add circuit classification
    tyre_df['circuit_type'] = tyre_df['race'].apply(classify_circuit)

    return tyre_df


def get_pit_stop_data(years: List[int]) -> pd.DataFrame:
    """
    Extract pit stop timing data for all races.

    Args:
        years: List of years to load

    Returns:
        DataFrame with pit stop durations and timing
    """
    all_pit_stops = []

    for year in years:
        print(f"\nLoading {year} pit stop data...")
        schedule = get_race_schedule(year)

        if schedule.empty:
            continue

        races = schedule[schedule['EventFormat'] != 'testing']

        for idx, race in races.iterrows():
            race_name = race['EventName']
            print(f"  Processing {race_name}...", end=' ')

            race_session = load_session(year, race_name, 'R')
            if race_session is None:
                print("Failed")
                continue

            # Get laps and identify pit stops
            laps = race_session.laps

            # Group by driver to find pit laps
            for driver in laps['Driver'].unique():
                driver_laps = laps[laps['Driver'] == driver].sort_values('LapNumber')

                # Pit stops occur when stint number changes
                pit_laps = driver_laps[driver_laps['Stint'].diff() > 0]

                for idx, pit_lap in pit_laps.iterrows():
                    try:
                        all_pit_stops.append({
                            'year': year,
                            'race': race_name,
                            'driver': driver,
                            'team': pit_lap['Team'],
                            'lap_number': pit_lap['LapNumber'],
                            'stint': pit_lap['Stint'],
                            'compound_before': driver_laps[driver_laps['LapNumber'] == pit_lap['LapNumber']-1]['Compound'].values[0] if pit_lap['LapNumber'] > 1 else None,
                            'compound_after': pit_lap['Compound'],
                            'pit_in_time': pit_lap['Time']
                        })
                    except:
                        continue

            print("✓")

    df = pd.DataFrame(all_pit_stops)
    print(f"\nLoaded {len(df)} pit stop observations")
    return df


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_team_pairs(df: pd.DataFrame) -> Dict[str, List[str]]:
    """
    Identify teammate pairs for a given dataset.

    Args:
        df: DataFrame with 'team' and 'driver' columns

    Returns:
        Dictionary mapping team names to list of driver pairs
    """
    team_pairs = {}

    for team in df['team'].unique():
        drivers = df[df['team'] == team]['driver'].unique()
        if len(drivers) >= 2:
            team_pairs[team] = list(drivers)

    return team_pairs


def calculate_position_correlation(df: pd.DataFrame, method: str = 'spearman') -> float:
    """
    Calculate correlation between qualifying and race positions.

    Args:
        df: DataFrame with 'quali_pos' and 'race_pos' columns
        method: Correlation method ('spearman' or 'pearson')

    Returns:
        Correlation coefficient
    """
    from scipy.stats import spearmanr, pearsonr

    if method == 'spearman':
        corr, _ = spearmanr(df['quali_pos'], df['race_pos'])
    else:
        corr, _ = pearsonr(df['quali_pos'], df['race_pos'])

    return corr


def print_data_summary(df: pd.DataFrame, title: str = "Data Summary"):
    """
    Print a summary of the loaded data.

    Args:
        df: DataFrame to summarize
        title: Title for the summary
    """
    print(f"\n{'='*60}")
    print(f"{title}")
    print(f"{'='*60}")
    print(f"Total observations: {len(df)}")
    print(f"Date range: {df['year'].min()} - {df['year'].max()}")
    print(f"Number of unique races: {df['race'].nunique() if 'race' in df.columns else 'N/A'}")
    print(f"Number of unique drivers: {df['driver'].nunique() if 'driver' in df.columns else 'N/A'}")
    print(f"Number of unique teams: {df['team'].nunique() if 'team' in df.columns else 'N/A'}")
    print(f"{'='*60}\n")
