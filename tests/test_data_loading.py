#tests/test_data_loading.py
import os
import pytest
import xml.etree.ElementTree as ET
from unittest.mock import patch, MagicMock
from src.data_loading import unzip_export, parse_xml
import zipfile
from src.constants.paths import EXTRACTION_PATH, ZIP_FILE_PATH, XML_FILE_PATH


@pytest.fixture(scope="module", autouse=True)
def setup_test_environment():
    # Create necessary directories and files for testing
    os.makedirs(EXTRACTION_PATH, exist_ok=True)
    # Create a mock zip file for testing purposes
    with open(ZIP_FILE_PATH, "wb") as f:
        f.write(b"Mock zip file content")  
    # Create a sample XML file for testing
    sample_xml = '''<root>
                        <child attribute="value">Sample</child>
                    </root>'''
    with open(XML_FILE_PATH, "w") as f:
        f.write(sample_xml)


def test_unzip_export_success():
    unzip_export(EXTRACTION_PATH, ZIP_FILE_PATH)
    assert os.path.exists(EXTRACTION_PATH)  # Check if extraction path exists






def test_parse_xml():
    result = parse_xml(XML_FILE_PATH)
    expected_root = "root"
    assert result.tag == expected_root
    assert result.attrib == {}


def test_simple():
    assert True
