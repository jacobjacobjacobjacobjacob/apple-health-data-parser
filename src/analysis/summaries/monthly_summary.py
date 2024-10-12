# src/analysis/summary/monthly_summary.py
from src.analysis.utils import MONTH_ORDER
import pandas as pd


def get_monthly_mean_summary(df):
    """
    Calculate the monthly mean summary for various metrics.

    Metrics and their respective units:
    - Month: String representing the month (e.g., Jan, Feb)
    - Energy Burned: Calories (kcal)
    - Exercise Time: Minutes per day (min)
    - Flights Climbed: Number of flights (count)
    - Physical Effort: Arbitrary effort score (unitless)
    - Step Count: Number of steps (count)
    - Heartrate Recovery: Beats per minute (bpm)
    - Respiratory Rate: Breaths per minute (breaths/min)
    - Resting Heartrate: Beats per minute (bpm)
    - Running Ground Contact Time: Milliseconds (ms)
    - Running Power: Watts (W)
    - Running Speed: Meters per second (m/s)
    - Running Stride Length: Meters (m)
    - Running Vertical Oscillation: Millimeters (mm)
    - Stair Ascent Speed: Meters per second (m/s)
    - VO2 Max: Milliliters of oxygen per kilogram per minute (ml/kg/min)
    - Walking Heartrate: Beats per minute (bpm)
    - Walking Speed: Meters per second (m/s)
    - Walking Step Length: Meters (m)
    - Workout Hours: Hours (h)
    - Sleep Hours: Hours (h)
    """
    df["Month"] = pd.Categorical(df["month"], categories=MONTH_ORDER, ordered=True)
    df = df.drop(columns=["year"])
    grouped_df = (
        df.groupby("Month", observed=False).mean(numeric_only=True).reset_index()
    )
    grouped_df = grouped_df.round(1)
    grouped_df = grouped_df.sort_values("Month")
    return grouped_df


def get_monthly_sum_summary(df):
    """
    Calculate the monthly sum summary for various metrics.

    Metrics and their respective units:
    - Month: String representing the month (e.g., Jan, Feb)
    - Energy Burned: Calories (kcal)
    - Exercise Time: Minutes (min)
    - Flights Climbed: Number of flights (count)
    - Physical Effort: Arbitrary effort score (unitless)
    - Step Count: Number of steps (count)
    - Workout Hours: Hours (h)
    - Sleep Hours: Hours (h)
    """
    # print(df.columns())
    df["Month"] = pd.Categorical(df["month"], categories=MONTH_ORDER, ordered=True)

    # Grouping the data
    grouped_df = (
        df.groupby("Month", observed=False).sum(numeric_only=True).reset_index()
    )

    grouped_df = grouped_df.round(1)
    # grouped_df = grouped_df.sort_values("Month")

    # Columns that we want to keep
    columns_to_keep = [
        "Month",
        "Energy Burned",
        "Physical Effort",
        "Step Count",
        "Exercise Time",
        "Flights Climbed",
        "Workout Hours",
        "Sleep Hours",
    ]

    # Only keep the columns that exist in the dataframe
    existing_columns_to_keep = [
        col for col in columns_to_keep if col in grouped_df.columns
    ]

    if not existing_columns_to_keep:
        raise KeyError("None of the required columns are present in the DataFrame.")

    grouped_df = grouped_df[existing_columns_to_keep]

    return grouped_df
