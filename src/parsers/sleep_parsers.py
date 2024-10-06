# src/parser/sleep_parsers.py
from src.constants.sleep import HK_RECORDS_SLEEP_ANALYSIS, SLEEP_CATEGORIES
from src.parsers.base_parser import BaseParser


class SleepDataParser(BaseParser):
    def handle_element(self, elem):
        """Processes an XML element and extracts relevant health record data."""
        if elem.tag == "Record":
            record_type: str = elem.attrib.get("type")
            record_value: str = elem.attrib.get("value")

            if (
                record_type == HK_RECORDS_SLEEP_ANALYSIS
                and record_value in SLEEP_CATEGORIES
            ):
                record = {
                    "start_time": elem.attrib.get("startDate"),
                    "end_time": elem.attrib.get("endDate"),
                    "value": record_value,
                    "type": "Sleep Analysis",
                }
                self.data.append(record)
