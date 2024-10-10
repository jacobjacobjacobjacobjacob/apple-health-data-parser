# src/cleaners/sleep_cleaner.py
import re
from loguru import logger
import pandas as pd
from src.cleaners.base_cleaner import BaseCleaner
from src.constants.paths import CLEANED_DATA_DIRECTORY
from src.utils import save_csv_to_file


class SleepCleaner(BaseCleaner):
    def __init__(self, file_path: str):
        super().__init__(file_path)

    @staticmethod
    def fetch_sleep_type(value: str):
        """Extract the sleep type using a regular expression."""
        pattern = r"HKCategoryValueSleepAnalysisAsleep(\w+)"
        match = re.search(pattern, value)
        return match.group(1) if match else "Unknown"

    def extract_date(self):
        """Extracts the date from the 'start_time' column."""
        self.df["date"] = self.df["start_time"].dt.date
        self.df["date"] = pd.to_datetime(self.df["date"])
        return self.df

    def format_time_columns(self):
        """Formats 'start_time' and 'end_time' columns to HH:MM format."""
        self.df["start_time"] = self.df["start_time"].dt.strftime("%H:%M")
        self.df["end_time"] = self.df["end_time"].dt.strftime("%H:%M")
        return self.df

    def calculate_sleep_duration(self):
        # Ensure datetime values
        self.df["start_time"] = pd.to_datetime(self.df["start_time"])
        self.df["end_time"] = pd.to_datetime(self.df["end_time"])
        self.df["duration"] = (
            self.df["end_time"] - self.df["start_time"]
        ).dt.total_seconds() / 60
        return self.df

    def clean_data(self):
        """Orchestrates the data cleaning process."""
        logger.info("Loading JSON data for cleaning.")
        self.df = self.load_json_data()

        if self.df is not None:
            logger.info("Cleaning sleep data.")

            if self.df is not None and not self.df.empty:
                # Extract sleep type from 'value' column
                self.df["sleep_type"] = self.df["value"].apply(self.fetch_sleep_type)
                self.df = self.extract_date()
                self.df = self.filter_by_year()
                self.df = self.calculate_sleep_duration()
                self.df = self.format_time_columns()
                # Group by date and sleep_type, summing up the duration for each group
                # Group by date and sleep_type, but keep the first start_time and last end_time for each group
                grouped = (
                    self.df.groupby(["date", "sleep_type"])
                    .agg(
                        duration=("duration", "sum"),
                        start_time=("start_time", "min"),  # Earliest start time
                        end_time=("end_time", "max"),  # Latest end time
                    )
                    .reset_index()
                )
                self.df = grouped
                self.df = self.split_datetime_columns()
                self.df = self.reorder_datetime_columns()

                # Save the cleaned DataFrame to a CSV file
                save_csv_to_file(
                    self.df, CLEANED_DATA_DIRECTORY, "cleaned_sleep_data.csv"
                )
        else:
            logger.error("Failed to load data.")

        return self.df
