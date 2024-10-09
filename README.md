
# Health and Workout Data Parser

This project is a comprehensive parser and cleaner for health and workout data, such as sleep, heart rate, VO2 Max, physical activities, and more. It processes Apple Health XML exports, parses the data into structured JSON format, and then cleans and organizes it for further analysis.

## Features

- **XML Unzipping:** Automatically extracts Apple Health export files from a `.zip` archive.
- **Data Parsing:** Parses various health, activity, workout, and sleep data using multiple parsers.
- **Data Cleaning:** Cleans and processes parsed data for consistent and accurate results.
- **Logging:** Uses `loguru` for logging all steps, including parsing, cleaning, and error handling.
- **Modular Structure:** Organized into categories like health, activity, sleep, and workout data.

## Project Structure

```
.
├── src/
│   ├── constants/
│   │   └── paths.py            # Paths for data directories and files
│   ├── parsers/
│   │   ├── activity_parsers.py  # Parsers for activity data
│   │   ├── health_parsers.py    # Parsers for health-related data
│   │   ├── sleep_parsers.py     # Parsers for sleep data
│   │   └── workout_parser.py    # Parser for workout data
│   ├── cleaners/
│   │   ├── activity_cleaner.py  # Cleaner for activity data
│   │   ├── health_cleaner.py    # Cleaner for health data
│   │   ├── sleep_cleaner.py     # Cleaner for sleep data
│   │   └── workout_cleaner.py   # Cleaner for workout data
│   ├── data_loading.py          # Handles unzipping the export file
│   ├── data_parsing.py          # Parses all data categories
│   ├── data_cleaning.py         # Cleans all data categories
│   └── utils.py                 # Utility functions (e.g., saving data to JSON)
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/jacobjacobjacobjacobjacob/apple-health-data-parser.git
    cd health-workout-data-parser
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the required directories and paths. Update the `EXTRACTION_PATH`, `ZIP_FILE_PATH`, and other constants in the `constants/paths.py` file as per your setup.

## Usage
### 1. Export your Apple Health data
 Export your data from the "Health" app on your iPhone (Browse -> Profile -> Export All Health Data)

### 2. Unzipping the Apple Health Export
To unzip the `export.zip` file containing the Apple Health data:

```python
from src.data_loading import unzip_export

unzip_export()
```

### 3. Parsing Data
To parse all categories of data (health, sleep, activity, workout):

```python
from src.data_parsing import parse_all_data

parsed_data = parse_all_data()
```

This will parse the data into structured JSON files for each category and save them in the `PARSED_DATA_DIRECTORY`.

### 4. Cleaning Data
To clean the parsed data for further analysis:

```python
from src.data_cleaning import clean_all_data

clean_all_data()
```

This will clean and save the processed data into the `CLEANED_DATA_DIRECTORY`.

## Log Output
This project uses `loguru` for logging all operations. Logs include details on the number of records parsed, errors, and processing times.

## Contributing

Contributions are welcome! Feel free to submit a pull request or file an issue with any bug reports, feature requests, or suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
