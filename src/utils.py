# utils.py
import json
import os
import pandas as pd
from loguru import logger

def convert_to_json(data: list) -> str:
    return json.dumps(data, indent=4)

def save_json_to_file(data: list, directory: str, filename: str) -> None:
    """
    Save JSON data to a file in the specified directory.
    If the file already exists, it won't be overwritten.
    """

    # Create directory if it does not exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Define the full path for the output file
    file_path = os.path.join(directory, filename)

    # Check if the file already exists
    if os.path.isfile(file_path):
        return

    # Save the JSON data to a file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def save_csv_to_file(data: pd.DataFrame, directory: str, filename: str, overwrite: bool = True) -> None:
    """
    Save a DataFrame to a CSV file in the specified directory.
    """

    # Create directory if it does not exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Define the full path for the output file
    file_path = os.path.join(directory, filename)

    # Check if the file already exists and handle overwrite
    if os.path.isfile(file_path) and not overwrite:
        return

    # Save the DataFrame to a CSV file
    data.to_csv(file_path, index=False)
    logger.info(f"Data saved to: {file_path}")


def check_if_file_exists(file_path: str) -> bool:
    """
    Check if a file exists at the specified file path.
    """
    return os.path.isfile(file_path)