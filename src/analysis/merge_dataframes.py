# src/analysis/merge_dataframes.py
import pandas as pd
from loguru import logger

from src.analysis.utils import MONTH_MAPPING, WEEKDAY_MAPPING


class DataFrameMerger:
    def __init__(self, dataframes: dict):
        # Extract necessary dataframes from the dictionary
        self.sleep_df = dataframes.get("cleaned_sleep_data")
        self.activity_df = dataframes.get("cleaned_activity_data")
        self.health_df = dataframes.get("cleaned_health_data")
        self.workout_df = dataframes.get("cleaned_workout_data")

    def sum_and_convert_to_hours(self, df, group_cols, sum_col, new_col_name):
        """Groups by columns, sums the values, and converts to hours."""

        try:
            summed_df = df.groupby(group_cols)[sum_col].sum().reset_index()
            summed_df[new_col_name] = summed_df[sum_col] / 60
            return summed_df.drop(columns=[sum_col])
        except Exception as e:
            logger.error(f"Error summing and converting {sum_col}: {e}")
            raise

    def pivot_data(self, df, index_cols, pivot_col, value_col):
        """Pivots the dataframe based on specified index and column values."""
        try:
            pivoted_df = df.pivot_table(
                index=index_cols, columns=pivot_col, values=value_col
            ).reset_index()
            return pivoted_df
        except Exception as e:
            logger.error(f"Error pivoting data: {e}")
            raise

    def map_weekdays_and_months(self, df):
        try:
            df["day_of_week"] = df["day_of_week"].map(WEEKDAY_MAPPING)
            df["month"] = df["month"].map(MONTH_MAPPING)
            return df
        except Exception as e:
            logger.error(f"Error mapping weekdays and months: {e}")
            raise

    def merge_dataframes(self):
        """Merges all dataframes on common date columns."""
        try:
            # Summing and converting sleep and workout durations
            summed_sleep_df = self.sum_and_convert_to_hours(
                self.sleep_df,
                ["date", "day_of_week", "month", "year"],
                "duration",
                "Sleep Hours",
            )
            summed_workout_df = self.sum_and_convert_to_hours(
                self.workout_df,
                ["date", "day_of_week", "month", "year"],
                "duration",
                "Workout Hours",
            )
            # Pivoting activity and health data
            pivoted_activity_df = self.pivot_data(
                self.activity_df,
                ["date", "day_of_week", "month", "year"],
                "type",
                "value",
            )
            pivoted_health_df = self.pivot_data(
                self.health_df,
                ["date", "day_of_week", "month", "year"],
                "type",
                "value",
            )
            # Merging the dataframes on 'date' and other columns
            merged_df = pivoted_activity_df.merge(
                pivoted_health_df,
                on=["date", "day_of_week", "month", "year"],
                how="inner",
            )

            merged_df = merged_df.merge(
                summed_workout_df,
                on=["date", "day_of_week", "month", "year"],
                how="left",
            )

            merged_df = merged_df.merge(
                summed_sleep_df, on=["date", "day_of_week", "month", "year"], how="left"
            )

            # Convert 'date' to datetime format
            merged_df["date"] = pd.to_datetime(merged_df["date"])
            logger.info("Successfully merged all dataframes.")

            # Map weekdays and months
            merged_df = self.map_weekdays_and_months(merged_df)
            return merged_df
        except Exception as e:
            logger.error(f"Error merging dataframes: {e}")
            raise
