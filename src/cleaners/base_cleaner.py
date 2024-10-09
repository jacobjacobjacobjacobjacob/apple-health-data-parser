# src/cleaners/base_cleaner.py
from datetime import datetime
import pandas as pd
from loguru import logger


class BaseCleaner:
    """Base class for data cleaning."""
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None

    def load_json_data(self):
        """Loads data from a JSON file into a DataFrame."""
        try:
            self.df = pd.read_json(self.file_path)
            return self.df
        except FileNotFoundError:
            logger.error(f"Failed data loading: {self.file_path} not found.")
    
    def split_datetime_columns(self):
        """Splits a 'date' column into 'year', 'month', 'day', and 'day_of_week' columns."""
        if "date" not in self.df.columns:
            logger.error('The DataFrame must contain a "date" column.')
            raise ValueError('The DataFrame must contain a "date" column.')
        
        self.df["date"] = pd.to_datetime(self.df["date"])  # Convert to datetime

        # Split 'date' into 'year', 'month', 'day', and 'day_of_week'
        self.df["year"] = self.df["date"].dt.year
        self.df["month"] = self.df["date"].dt.month
        self.df["day"] = self.df["date"].dt.day
        self.df["day_of_week"] = self.df["date"].dt.weekday # Monday=1, Sunday=7
        self.df = self.df.drop(columns=["date"])

        return self.df

    def reorder_datetime_columns(self):
        """Reorders the DataFrame columns to have the datetime columns first."""
        column_order = ["day", "month", "year", "day_of_week"]
        remaining_columns = [col for col in self.df.columns if col not in column_order]
        self.df = self.df[column_order + remaining_columns]
        return self.df

    def drop_columns(self, columns):
        """Drops specified columns from the DataFrame."""
        missing_columns = [col for col in columns if col not in self.df.columns]
        if missing_columns:
            logger.warning(f"Columns not found: {missing_columns}")
        self.df = self.df.drop(columns=[col for col in columns if col in self.df.columns])
        return self.df
    
