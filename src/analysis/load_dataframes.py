# src/analysis/load_dataframes.py
import os
import pandas as pd
from loguru import logger
from utils import map_weekdays_and_months


class DataFrameLoader:
    def __init__(self, directory: str):
        self.directory = directory
        self.dataframes = {}

    def load_all_dataframes(self) -> dict:
        """Load all CSV files in the directory into a dictionary of DataFrames."""
        logger.info(f"Loading CSV files from directory: {self.directory}")

        # Get all CSV files in the directory
        for filename in os.listdir(self.directory):
            if filename.endswith(".csv"):  # Only consider .csv files
                file_path = os.path.join(self.directory, filename)

                try:
                    # Load the CSV into a DataFrame
                    df = pd.read_csv(file_path)

                    # Use filename (without .csv) as the key
                    key = filename.rsplit(".", 1)[0]
                    self.dataframes[key] = df

                    logger.info(f"{filename} loaded into dataframe")
                except Exception as e:
                    logger.error(f"Error loading {filename}: {e}")
        logger.info(
            f"Finished loading {len(self.dataframes)} DataFrames from {self.directory}"
        )


        return self.dataframes
    