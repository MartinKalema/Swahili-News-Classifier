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

@dataclass(frozen=True)
class ModelTrainingConfig:
    """
    Configuration class for model training using ULMFiT (Universal Language Model Fine-tuning).

    Attributes:
        test_size (float): Proportion of the dataset to include in the test split.
        learning_rate_1 (float): Learning rate for training the language model learner.
        learning_rate_2 (float): Learning rate for the first phase of classifier training.
        learning_rate_3 (float): Learning rate for the second phase of classifier training.
        learning_rate_4 (float): Learning rate for the third phase of classifier training.
        learning_rate_5 (float): Learning rate for the fourth phase of classifier training.
        batch_size_1 (int): Batch size for language model training.
        batch_size_2 (int): Batch size for text classifier training.
        epochs_1 (int): Number of epochs for training the language model learner.
        epochs_2 (int): Number of epochs for the first phase of classifier training.
        epochs_3 (int): Number of epochs for the second phase of classifier training.
        epochs_4 (int): Number of epochs for the third phase of classifier training.
        epochs_5 (int): Number of epochs for the fourth phase of classifier training.
        training_data (Path): Path to the training data CSV file.
        number_of_classes (int): Number of target classes in the classification task.
        root_dir (Path): Root directory for storing model artifacts.
    """
    test_size: float
    learning_rate_1: float
    learning_rate_2: float
    learning_rate_3: float
    learning_rate_4: float
    learning_rate_5: float
    batch_size_1: int
    batch_size_2: int
    epochs_1: int
    epochs_2: int
    epochs_3: int
    epochs_4: int
    epochs_5: int
    training_data: Path
    number_of_classes: int
    root_dir: Path