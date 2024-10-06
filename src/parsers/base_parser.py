# src/parsers/base_parser.py
import os
import xml.etree.ElementTree as ET

from loguru import logger


class BaseParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data: list = []

    def parse(self) -> list:
        """Parses the XML file specified by the file_path attribute.."""
        if not os.path.exists(self.file_path):
            logger.error(f"File not found: {self.file_path}")
            return []

        for _, elem in ET.iterparse(self.file_path, events=("end",)):
            self.handle_element(elem)
            elem.clear()
        return self.data

    def handle_element(self, elem):
        # This method will be overridden in subclasses
        pass

    def extract_common_fields(self, elem, record_type):
        """Extracts common fields such as date, value, unit, and type from the element."""
        return {
            "date": elem.attrib.get("startDate"),
            "value": elem.attrib.get("value"),
            "unit": elem.attrib.get("unit"),
            "type": record_type,
        }

