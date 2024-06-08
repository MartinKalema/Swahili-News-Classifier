import pytest
from unittest.mock import patch
from swahiliNewsClassifier.entity.entities import DataIngestionConfig
from swahiliNewsClassifier.components import DataIngestion

@pytest.fixture
def mock_config():
    return DataIngestionConfig(
        train_source_URL="https://drive.google.com/file/d/15stuLDZkXNOgBUC1rnx5yXYdVPViUjNB/view?usp=sharing",
        test_source_URL="https://drive.google.com/file/d/1mjmYzMdnn_UwSEgTQ7i-cJ5WSOokt9Er/view?usp=sharing",
        train_data_file="artifacts/data_ingestion/compressed/train_data.zip",
        test_data_file="artifacts/data_ingestion/compressed/test_data.zip",
        unzip_dir="artifacts/data_ingestion/decompressed"
    )

@pytest.fixture
def data_ingestion(mock_config):
    return DataIngestion(config=mock_config)

@patch("swahiliNewsClassifier.data_ingestion.gdown.download")
def test_download_file(mock_gdown, data_ingestion):
    mock_gdown.return_value = None 
    
    data_ingestion.download_file()
    
    assert mock_gdown.call_count == 2
    mock_gdown.assert_any_call("https://drive.google.com/file/d/15stuLDZkXNOgBUC1rnx5yXYdVPViUjNB/view?usp=sharing", 
                               "artifacts/data_ingestion/compressed/train_data.zip")
    mock_gdown.assert_any_call("https://drive.google.com/file/d/1mjmYzMdnn_UwSEgTQ7i-cJ5WSOokt9Er/view?usp=sharing", 
                               "artifacts/data_ingestion/compressed/test_data.zip")

@patch("zipfile.ZipFile.extractall")
@patch("zipfile.ZipFile.__init__")
def test_extract_zip_file(mock_zip_init, mock_extractall, data_ingestion):
    mock_zip_init.return_value = None 
    
    data_ingestion.extract_zip_file()
    
    assert mock_zip_init.call_count == 2
    assert mock_extractall.call_count == 2
    mock_extractall.assert_any_call("artifacts/data_ingestion/decompressed")
