# src/cleaners/workout_cleaner.py
import re

import pandas as pd
from loguru import logger

from src.cleaners.base_cleaner import BaseCleaner
from src.constants.paths import CLEANED_DATA_DIRECTORY
from ..utils import save_csv_to_file


class WorkoutCleaner(BaseCleaner):
    def __init__(self, file_path: str):
        super().__init__(file_path)

    @staticmethod
    def fetch_activity_type(workout_type: str):
        """Slice the string to only get the workout type using regex"""
        pattern = r"HKWorkoutActivityType(\w+)"
        match = re.search(pattern, workout_type)
        return match.group(1) if match else "Unknown"

    def calculate_start_end_times(self) -> pd.DataFrame:
        """Calculates 'start_time' and 'end_time' based on the 'date' and 'duration' columns."""
        # Check that required columns exist
        if "date" not in self.df.columns or "duration" not in self.df.columns:
            raise ValueError(
                'The DataFrame must contain "date" and "duration" columns.'
            )

        # Convert 'date' column to datetime
        self.df["start_time"] = pd.to_datetime(self.df["date"])

        # Calculate end_time by adding the duration in minutes
        self.df["end_time"] = self.df["start_time"] + pd.to_timedelta(
            self.df["duration"], unit="m"
        )

        # Format 'start_time' and 'end_time' as HH:MM
        self.df["start_time"] = self.df["start_time"].dt.strftime("%H:%M")
        self.df["end_time"] = self.df["end_time"].dt.strftime("%H:%M")

        return self.df

    def clean_data(self):
        """Orchestrates the data cleaning process."""
        logger.info("Loading JSON data for cleaning.")
        self.df = self.load_json_data()

        if self.df is not None:
            logger.info("Cleaning workout data.")

            # Extract workout types
            self.df["workout_type"] = self.df["workout_type"].apply(
                self.fetch_activity_type
            )

            self.df = self.calculate_start_end_times()
            self.df = self.split_datetime_columns()
            self.df = self.reorder_datetime_columns()

            # Drop workouts that have a duration of less than 5 minutes and conert to int
            self.df = self.df[self.df["duration"] >= 5]
            self.df["duration"] = pd.to_numeric(self.df["duration"], errors="coerce").round(0).astype(int)



            # Reorder columns
            column_order = [
                "day",
                "month",
                "year",
                "day_of_week",
                "workout_type",
                "start_time",
                "end_time",
                "duration",
            ]
            self.df = self.df[column_order]

        # Save to CSV file
        save_csv_to_file(self.df, CLEANED_DATA_DIRECTORY, "cleaned_workout_data.csv")
        return self.df
