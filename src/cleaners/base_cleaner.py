# src/cleaners/base_cleaner.py
from loguru import logger
import pandas as pd

class BaseCleaner:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None

    def load_json_data(self):
        try:
            self.df = pd.read_json(self.file_path)
            return self.df
        except FileNotFoundError:
            logger.error(f"Failed data loading: {self.file_path} not found.")
        