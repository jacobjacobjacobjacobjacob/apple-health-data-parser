# src/cleaners/health_cleaner.py
from loguru import logger
from src.cleaners.base_cleaner import BaseCleaner
from src.constants.paths import CLEANED_DATA_DIRECTORY
from src.utils import save_csv_to_file


class HealthCleaner(BaseCleaner):
    def __init__(self, file_path: str):
        super().__init__(file_path)

    def clean_data(self):
        """Orchestrates the data cleaning process."""
        logger.info("Loading JSON data for cleaning.")
        self.df = self.load_json_data()

        if self.df is not None:
            logger.info("Cleaning health data.")

            if self.df is not None and not self.df.empty:
                self.df = self.filter_by_year()
                self.df = self.group_by_date(agg_type="mean")
                self.df = self.split_datetime_columns()
                self.df = self.reorder_datetime_columns()
                self.df = self.round_column_values(column="value")

                # Save the cleaned DataFrame to a CSV file
                save_csv_to_file(
                    self.df, CLEANED_DATA_DIRECTORY, "cleaned_health_data.csv"
                )
            else:
                logger.warning("The DataFrame is empty after filtering by year.")
        else:
            logger.error("Failed to load data.")

        return self.df
