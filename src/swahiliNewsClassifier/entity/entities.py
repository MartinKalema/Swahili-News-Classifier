from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration class for the data ingestion process.

    Attributes:
        root_dir (Path): The root directory where data will be stored or processed.
        train_source_URL (str): The URL from which the training data will be fetched.
        test_source_URL (str): The URL from which the test data will be fetched.
        train_data_file (Path): The local file path where the downloaded training data will be stored.
        test_data_file (Path): The local file path where the downloaded test data will be stored.
        unzip_dir (Path): The directory where the downloaded data will be extracted or unzipped.
    """
    root_dir: Path
    train_source_URL: str
    test_source_URL: str
    train_data_file: Path
    test_data_file: Path
    unzip_dir: Path