from swahiliNewsClassifier.configuration.configuration import ConfigurationManager
from swahiliNewsClassifier.components.model_training import ModelTraining
from swahiliNewsClassifier import log

STAGE_NAME = "Model Training Stage"


class ModelTrainingPipeline:
    def __init__(self):
        """
        Initialize the ModelTrainingPipeline object.
        """
        self.config = ConfigurationManager()

    def main(self):
        """
        Execute the data ingestion process.
        """
        try:
            model_training_config = self.config.get_model_training_config()
            model_training = ModelTraining(model_training_config=model_training_config)
            model_training.run_pipeline()
        except Exception as e:
            log.exception(f"An error occurred during {STAGE_NAME}: {e}")
            raise e


if __name__ == '__main__':
    pipeline = ModelTrainingPipeline()
    pipeline.main()