# src/data_loading.py
import xml.etree.ElementTree as ET
import zipfile

from loguru import logger

from .constants.paths import EXTRACTION_PATH, ZIP_FILE_PATH


def unzip_export(
    extraction_path: str = EXTRACTION_PATH, zip_file: str = ZIP_FILE_PATH
) -> None:
    try:
        with zipfile.ZipFile(zip_file, "r") as zip_ref:
            zip_ref.extractall(extraction_path)
            logger.info(f"{zip_file} extracted successfully to {extraction_path}.")
    except zipfile.BadZipFile:
        logger.error(f"Failed to extract {zip_file}: Bad zip file.")
    except FileNotFoundError:
        logger.error(f"Failed to extract: {zip_file} not found.")
    except Exception as e:
        logger.error(f"An unexpected error occurred while extracting {zip_file}: {e}")
