# src/parser/activity_parsers.py
from src.constants.activity import (
    HK_PHYSICAL_EFFORT,
    HK_STEP_COUNT,
    HK_FLIGHTS_CLIMBED,
    HK_EXERCISE_TIME,
    HK_ENERGY_BURNED,
)
from src.parsers.base_parser import BaseParser


class PhysicalEffortParser(BaseParser):
    def handle_element(self, elem):
        """Handles an XML element and processes it if it is a "Record" element of type HK_PHYSICAL_EFFORT."""
        if elem.tag == "Record" and elem.attrib.get("type") == HK_PHYSICAL_EFFORT:
            record = self.extract_common_fields(elem, "Physical Effort")
            self.data.append(record)


class ExerciseTimeParser(BaseParser):
    def handle_element(self, elem):
        """Handles an XML element and processes it if it is a "Record" element of type HK_EXERCISE_TIME."""
        if elem.tag == "Record" and elem.attrib.get("type") == HK_EXERCISE_TIME:
            record = self.extract_common_fields(elem, "Exercise Time")
            self.data.append(record)


class EnergyBurnedParser(BaseParser):
    def handle_element(self, elem):
        """Handles an XML element and processes it if it is a "Record" element of type HK_ENERGY_BURNED."""
        if elem.tag == "Record" and elem.attrib.get("type") == HK_ENERGY_BURNED:
            record = self.extract_common_fields(elem, "Energy Burned")
            self.data.append(record)


class StepCountParser(BaseParser):
    def handle_element(self, elem):
        """Processes an XML element and extracts specific health data records."""
        if elem.tag == "Record" and elem.attrib.get("type") == HK_STEP_COUNT:
            record = self.extract_common_fields(elem, "Step Count")
            self.data.append(record)


class FlightsClimbedParser(BaseParser):
    def handle_element(self, elem):
        """Processes an XML element and extracts specific health data records."""
        if elem.tag == "Record" and elem.attrib.get("type") == HK_FLIGHTS_CLIMBED:
            record = self.extract_common_fields(elem, "Flights Climbed")
            self.data.append(record)
