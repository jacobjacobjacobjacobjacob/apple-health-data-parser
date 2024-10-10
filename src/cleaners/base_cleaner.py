# src/cleaners/base_cleaner.py
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

    def filter_by_year(self, year: int = 2024):
        """Filters the DataFrame by the specified year in the 'date' column."""
        # Ensure the DataFrame is loaded
        if self.df is None:
            logger.error("No data loaded. Please load the data first.")
            return None

        # Make sure 'date' column is in datetime format and make a copy
        self.df = self.df.copy()
        self.df.loc[:, "date"] = pd.to_datetime(self.df["date"])

        # Filter for the specified year
        self.df = self.df[self.df["date"].dt.year == year]

        return self.df

    def group_by_date(self, agg_type: str):
        """Groups the DataFrame by the 'date' column."""
        self.df["date"] = pd.to_datetime(self.df["date"])
        self.df["just_date"] = self.df["date"].dt.date

        df_grouped = (
            self.df.groupby(["just_date", "type"])
            .agg(
                {"value": agg_type, "unit": "first"}
            )  # Aggregate the data by aggregation type
            .reset_index()
        )
        df_grouped.rename(columns={"just_date": "date"}, inplace=True)

        return df_grouped

    def split_datetime_columns(self):
        """Splits a 'date' column into 'year', 'month', 'day', and 'day_of_week' columns."""
        if "date" not in self.df.columns:
            logger.error('The DataFrame must contain a "date" column.')
            raise ValueError('The DataFrame must contain a "date" column.')

        self.df["date"] = pd.to_datetime(self.df["date"])  # Convert to datetime

        # Split 'date' into 'year', 'month', 'day', and 'day_of_week'
        self.df["year"] = self.df["date"].dt.year
        self.df["month"] = self.df["date"].dt.month
        
        self.df["day_of_week"] = self.df["date"].dt.weekday + 1  # Monday=1, Sunday=7
        
        return self.df

    def reorder_datetime_columns(self):
        """Reorders the DataFrame columns to have the datetime columns first."""
        column_order = ["date", "day_of_week", "month", "year"]
        remaining_columns = [col for col in self.df.columns if col not in column_order]
        self.df = self.df[column_order + remaining_columns]
        

        return self.df

    def drop_columns(self, columns):
        """Drops specified columns from the DataFrame."""
        missing_columns = [col for col in columns if col not in self.df.columns]
        if missing_columns:
            logger.warning(f"Columns not found: {missing_columns}")
        self.df = self.df.drop(
            columns=[col for col in columns if col in self.df.columns]
        )
        return self.df

    def round_column_values(self, column):
        """Rounds the values in the specified column."""
        if column not in self.df.columns:
            logger.error(f"Column not found: {column}")
            return None
        self.df[column] = self.df[column].round(1)
        return self.df
