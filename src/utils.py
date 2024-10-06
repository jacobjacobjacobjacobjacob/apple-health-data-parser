# utils.py
import json
import os

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

def check_if_file_exists(file_path: str) -> bool:
    """
    Check if a file exists at the specified file path.
    """
    return os.path.isfile(file_path)