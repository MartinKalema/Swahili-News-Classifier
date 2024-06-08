from swahiliNewsClassifier import classifierlogger
from swahiliNewsClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# from swahiliNewsClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
# from swahiliNewsClassifier.pipeline.stage_03_model_training import TrainingPipeline
# from swahiliNewsClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

def run_pipeline_stage(stage_name, pipeline_class):
    """
    Run a pipeline stage and handle logging and exceptions.

    Args:
        stage_name (str): The name of the stage to run.
        pipeline_class (class): The class of the pipeline stage to instantiate and run.
    """
    try:
        classifierlogger.info("*********************************\n")
        classifierlogger.info(f">>>>>> {stage_name} started <<<<<<")
        pipeline = pipeline_class()
        pipeline.main()
        classifierlogger.info(f">>>>>> {stage_name} completed <<<<<<<\n")
        classifierlogger.info("**********************************\n")
    except Exception as e:
        classifierlogger.exception(f"An error occurred during {stage_name}: {e}")
        raise e

if __name__ == '__main__':
    run_pipeline_stage("Data Ingestion Stage", DataIngestionTrainingPipeline)
    # run_pipeline_stage("Prepare Base Model Stage", PrepareBaseModelPipeline)
    # run_pipeline_stage("Model Training Stage", TrainingPipeline)
    # run_pipeline_stage("Model Evaluation Stage", EvaluationPipeline)
