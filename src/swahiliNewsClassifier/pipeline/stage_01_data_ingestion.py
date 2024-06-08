from swahiliNewsClassifier.configuration.configuration import ConfigurationManager
from swahiliNewsClassifier.components.data_ingestion import DataIngestion
from swahiliNewsClassifier import customlogger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        """
        Initialize the DataIngestionTrainingPipeline object.
        """
        self.config = ConfigurationManager()

    def main(self):
        """
        Execute the data ingestion process.
        """
        try:
            customlogger.info(f"Starting {STAGE_NAME}")
            data_ingestion_config = self.config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            customlogger.info(f"Completed {STAGE_NAME}\n\n")
            customlogger.info("**********************************")
        except Exception as e:
            customlogger.exception(f"An error occurred during {STAGE_NAME}: {e}")
            raise e

if __name__ == '__main__':
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
