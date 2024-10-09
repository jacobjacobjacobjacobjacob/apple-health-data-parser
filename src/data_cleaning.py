# src/data_cleaning.py
import time
import os
from loguru import logger
from src.constants.paths import CLEANED_DATA_DIRECTORY
from src.constants.paths import (
    PARSED_WORKOUT_DATA_PATH,
    PARSED_HEALTH_DATA_PATH,
    PARSED_ACTIVITY_DATA_PATH,
    PARSED_SLEEP_DATA_PATH,
)
from src.cleaners.workout_cleaner import WorkoutCleaner
from src.cleaners.health_cleaner import HealthCleaner
from src.cleaners.activity_cleaner import ActivityCleaner
from src.cleaners.sleep_cleaner import SleepCleaner


def clean_all_data() -> dict:
    logger.info("Cleaning all data.")
    start_time = time.time()

    if not os.path.exists(CLEANED_DATA_DIRECTORY):
        os.makedirs(CLEANED_DATA_DIRECTORY)

    # # Workout data
    if os.path.exists(PARSED_WORKOUT_DATA_PATH):
        cleaner = WorkoutCleaner(PARSED_WORKOUT_DATA_PATH)
        cleaner.clean_data()

    # Health data
    if os.path.exists(PARSED_HEALTH_DATA_PATH):
        cleaner = HealthCleaner(PARSED_HEALTH_DATA_PATH)
        cleaner.clean_data()

    # Activity data
    if os.path.exists(PARSED_ACTIVITY_DATA_PATH):
        cleaner = ActivityCleaner(PARSED_ACTIVITY_DATA_PATH)
        cleaner.clean_data()

    # Sleep data
    if os.path.exists(PARSED_SLEEP_DATA_PATH):
        cleaner = SleepCleaner(PARSED_SLEEP_DATA_PATH)
        cleaner.clean_data()


    end_time = time.time()
    duration = end_time - start_time
    logger.info(f"Cleaning complete in {duration:.2f} seconds.")
