import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s %(asctime)s %(filename)s]: %(message)s:')

project_name = "swahiliNewsClassifier"


def create_file_with_directories(filepath: Path) -> None:
    """
    Create directories and an empty file if they don't exist.

    Args:
        filepath (Path): Path to the file.
    """
    if filepath.parent != Path(""):
        filepath.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creating directory: {filepath.parent}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Creating empty file: {filepath}")


list_of_files = [
    ".github/workflows/.gitkeep",
    ".github/workflows/codecov.yml",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/prepare_base_model.py",
    f"src/{project_name}/components/model_training.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/utils/_init__.py",
    f"src/{project_name}/utils/helper_functions.py",
    f"src/{project_name}/configuration/__init__.py",
    f"src/{project_name}/configuration/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/stage_01_data_ingestion.py",
    f"src/{project_name}/pipeline/stage_02_model_training.py",
    f"src/{project_name}/pipeline/stage_03_model_evaluation.py",
    f"src/{project_name}/pipeline/stage_04_prediction.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/entity.py",
    f"src/{project_name}/constants/__init__.py",
    "configuration/configuration.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "main.py",
    "dvc.yaml",
    "Dockerfile",
    "logs/example_logs.log",
    "research/01_data_ingestion.ipynb",
    "research/02_model_training.ipynb",
    "research/03_model_evaluation.ipynb",
    "templates/index.html",
    "app.py",
    "lint.py",
    ".env",
    "codecov.yml"
]

for filepath in list_of_files:
    create_file_with_directories(Path(filepath))