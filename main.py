# main.py
from src.data_loading import unzip_export
from src.data_parsing import parse_all_data
from src.data_cleaning import clean_all_data

def main() -> None:
    unzip_export()
    parse_all_data()
    clean_all_data()

if __name__ == "__main__":
    main()
