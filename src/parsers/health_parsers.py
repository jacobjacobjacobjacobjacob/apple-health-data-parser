# src/parser/health_parsers.py
from src.constants.health import (
    HK_RESTING_HEARTRATE,
    HK_RUNNING_POWER,
    HK_RUNNING_SPEED,
    HK_RUNNING_VERTICAL_OSCILLATION,
    HK_VO2_MAX,
    HK_HEARTRATE_RECOVERY,
    HK_WALKING_STEP_LENGTH,
    HK_RESPIRATORY_RATE,
    HK_WALKING_SPEED,
    HK_STAIR_ASCENT_SPEED,
    HK_WALKING_HEARTRATE,
    HK_RUNNING_STRIDE_LENGTH,
    HK_RUNNING_GROUND_CONTACT_TIME,
)
from src.parsers.base_parser import BaseParser


class RestingHeartRateParser(BaseParser):
    """A parser for extracting resting heart rate records from Apple Health data."""
    def handle_element(self, elem):
        if elem.tag == "Record" and elem.attrib.get("type") == HK_RESTING_HEARTRATE:
            record = self.extract_common_fields(elem, "Resting Heartrate")
            self.data.append(record)


class Vo2MaxParser(BaseParser):
    """A parser for extracting VO2 Max records from Apple Health data."""
    def handle_element(self, elem):
        if elem.tag == "Record" and elem.attrib.get("type") == HK_VO2_MAX:
            record = self.extract_common_fields(elem, "VO2 Max")
            self.data.append(record)


class HeartrateRecoveryParser(BaseParser):
    """A parser for extracting heart rate recovery records from Apple Health data."""
    def handle_element(self, elem):
        if elem.tag == "Record" and elem.attrib.get("type") == HK_HEARTRATE_RECOVERY:
            record = self.extract_common_fields(elem, "Heartrate Recovery")
            self.data.append(record)


class WalkingStepLengthParser(BaseParser):
    """A parser for extracting walking step length records from Apple Health data."""
    def handle_element(self, elem):
        if elem.tag == "Record" and elem.attrib.get("type") == HK_WALKING_STEP_LENGTH:
            record = self.extract_common_fields(elem, "Walking Step Length")
            self.data.append(record)


class RespiratoryRateParser(BaseParser):
    """A parser for extracting respiratory rate records from Apple Health data."""
    def handle_element(self, elem):
        if elem.tag == "Record" and elem.attrib.get("type") == HK_RESPIRATORY_RATE:
            record = self.extract_common_fields(elem, "Respiratory Rate")
            self.data.append(record)


class WalkingSpeedParser(BaseParser):
    """A parser for extracting walking speed records from Apple Health data."""
    def handle_element(self, elem):
        if elem.tag == "Record" and elem.attrib.get("type") == HK_WALKING_SPEED:
            record = self.extract_common_fields(elem, "Walking Speed")
            self.data.append(record)


class StairAscentSpeedParser(BaseParser):
    """A parser for extracting stair ascent speed records from Apple Health data."""
    def handle_element(self, elem):
        if elem.tag == "Record" and elem.attrib.get("type") == HK_STAIR_ASCENT_SPEED:
            record = self.extract_common_fields(elem, "Stair Ascent Speed")
            self.data.append(record)


class WalkingHeartrateParser(BaseParser):
    """A parser for extracting walking heartrate records from Apple Health data."""
    def handle_element(self, elem):
        if elem.tag == "Record" and elem.attrib.get("type") == HK_WALKING_HEARTRATE:
            record = self.extract_common_fields(elem, "Walking Heartrate")
            self.data.append(record)


class RunningStrideLengthParser(BaseParser):
    """A parser for extracting running stride length records from Apple Health data."""
    def handle_element(self, elem):
        if elem.tag == "Record" and elem.attrib.get("type") == HK_RUNNING_STRIDE_LENGTH:
            record = self.extract_common_fields(elem, "Running Stride Length")
            self.data.append(record)


class RunningGroundContactTimeParsers(BaseParser):
    """A parser for extracting running ground contact time records from Apple Health data."""
    def handle_element(self, elem):
        if elem.tag == "Record" and elem.attrib.get("type") == HK_RUNNING_GROUND_CONTACT_TIME:
            record = self.extract_common_fields(elem, "Running Ground Contact Time")
            self.data.append(record)


class RunningVerticalOscillationParser(BaseParser):
    """A parser for extracting running vertical oscillation records from Apple Health data."""
    def handle_element(self, elem):
        if elem.tag == "Record" and elem.attrib.get("type") == HK_RUNNING_VERTICAL_OSCILLATION:
            record = self.extract_common_fields(elem, "Running Vertical Oscillation")
            self.data.append(record)


class RunningSpeedParser(BaseParser):
    """A parser for extracting running speed records from Apple Health data."""
    def handle_element(self, elem):
        if elem.tag == "Record" and elem.attrib.get("type") == HK_RUNNING_SPEED:
            record = self.extract_common_fields(elem, "Running Speed")
            self.data.append(record)


class RunningPowerParser(BaseParser):
    """A parser for extracting running power records from Apple Health data."""
    def handle_element(self, elem):
        if elem.tag == "Record" and elem.attrib.get("type") == HK_RUNNING_POWER:
            record = self.extract_common_fields(elem, "Running Power")
            self.data.append(record)
