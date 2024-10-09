# src/data_parsing.py
import os
import time

from loguru import logger

from src.constants.paths import PARSED_DATA_DIRECTORY, XML_FILE_PATH
from src.parsers.sleep_parsers import SleepDataParser
from src.parsers.health_parsers import (
    RestingHeartRateParser,
    Vo2MaxParser,
    HeartrateRecoveryParser,
    WalkingStepLengthParser,
    RespiratoryRateParser,
    WalkingSpeedParser,
    StairAscentSpeedParser,
    WalkingHeartrateParser,
    RunningStrideLengthParser,
    RunningGroundContactTimeParsers,
    RunningVerticalOscillationParser,
    RunningSpeedParser,
    RunningPowerParser,
)
from src.parsers.activity_parsers import (
    ExerciseTimeParser,
    EnergyBurnedParser,
    StepCountParser,
    FlightsClimbedParser,
    PhysicalEffortParser,
)
from src.parsers.workout_parser import WorkoutDataParser
from .utils import save_json_to_file


def parse_all_data() -> dict:
    """Parses all health data from XML files using various data parsers and saves the parsed data as JSON files."""
    logger.info("Parsing all data...")
    start_time = time.time()
    total_records = 0
    data = {}

    if not os.path.exists(PARSED_DATA_DIRECTORY):
        os.makedirs(PARSED_DATA_DIRECTORY)

    # Group parsers into respective data categories
    parsers = {
        "health": [
            RestingHeartRateParser,
            Vo2MaxParser,
            HeartrateRecoveryParser,
            WalkingStepLengthParser,
            RespiratoryRateParser,
            WalkingSpeedParser,
            StairAscentSpeedParser,
            WalkingHeartrateParser,
            RunningStrideLengthParser,
            RunningGroundContactTimeParsers,
            RunningVerticalOscillationParser,
            RunningSpeedParser,
            RunningPowerParser,
        ],
        "sleep": [SleepDataParser],
        "activity": [
            EnergyBurnedParser,
            ExerciseTimeParser,
            PhysicalEffortParser,
            StepCountParser,
            FlightsClimbedParser,
        ],
        "workout": [WorkoutDataParser],
    }

    # Process each category of data
    for category, parser_classes in parsers.items():
        category_start_time = time.time()  # Start timer for the category
        category_data = []
        logger.info(f"Started parsing category: {category}")

        for parser_class in parser_classes:
            try:
                parser_start_time = time.time()  # Start timer for the specific parser
                parser = parser_class(XML_FILE_PATH)
                parsed_data = parser.parse()
                category_data.extend(
                    parsed_data
                )  # Combine all data from parsers in the same category
                parser_duration = (
                    time.time() - parser_start_time
                )  # Calculate the parser's duration
                logger.info(
                    f"Parsed {len(parsed_data)} records with {parser_class.__name__} in {parser_duration:.2f} seconds."
                )
                total_records += len(parsed_data)
            except Exception as e:
                logger.error(
                    f"Error parsing {category} with {parser_class.__name__}: {e}",
                    exc_info=True,
                )
        # Save data per category
        json_filename = f"{category}_data.json"
        save_json_to_file(category_data, PARSED_DATA_DIRECTORY, json_filename)
        data[category] = category_data

    end_time = time.time()
    duration = end_time - start_time
    logger.info(
        f"Parsing complete. Parsed {total_records} records in {duration:.2f} seconds."
    )

    return data
