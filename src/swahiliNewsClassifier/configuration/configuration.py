from swahiliNewsClassifier.constants import *
from swahiliNewsClassifier.utilities.helper_functions import read_yaml, create_directories
from swahiliNewsClassifier.entity.entities import DataIngestionConfig


class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH):
        """
        Initialize ConfigurationManager with configuration and parameter files.

        Args:
            config_filepath (str): Path to the configuration YAML file.
            params_filepath (str): Path to the parameters YAML file.
        """
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Get the data ingestion configuration.

        Returns:
            DataIngestionConfig: Configuration object for data ingestion.
        """
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir=config.root_dir,
            train_source_URL=config.train_source_URL,
            test_source_URL=config.test_source_URL,
            train_data_file=config.train_data_file,
            test_data_file=config.test_data_file,
            unzip_dir=config.unzip_dir
        )
