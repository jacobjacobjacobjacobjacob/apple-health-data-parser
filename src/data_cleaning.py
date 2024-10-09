# src/data_cleaning.py
import time
import os
from loguru import logger

from src.constants.paths import CLEANED_DATA_DIRECTORY
from src.constants.paths import PARSED_WORKOUT_DATA_PATH
from src.cleaners.base_cleaner import BaseCleaner
from src.cleaners.workout_cleaner import WorkoutCleaner


def clean_all_data() -> dict:
    logger.info("Cleaning all data.")
    start_time = time.time()

    if not os.path.exists(CLEANED_DATA_DIRECTORY):
        os.makedirs(CLEANED_DATA_DIRECTORY)
    
    # Load parsed workout data
    if os.path.exists(PARSED_WORKOUT_DATA_PATH):
        logger.info(f"Cleaning workout data from: {PARSED_WORKOUT_DATA_PATH}")
        cleaner = WorkoutCleaner(PARSED_WORKOUT_DATA_PATH)
        df = cleaner.clean_data()


    end_time = time.time()
    duration = end_time - start_time
    logger.info(
        f"Cleaning complete in {duration:.2f} seconds."
    )
    print(df.head())
    return df
