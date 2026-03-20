from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_dir: Path
    all_schema: dict
    local_data_file: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    transformed_train_file: Path
    transformed_test_file: Path
    data_path: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    transformed_train_file: Path
    transformed_test_file: Path
    data_path: Path

# CONFIG CLASS
# =========================
@dataclass
class ModelTrainerConfig:
    root_dir: Path
    training_data: Path
    testing_data: Path
    trained_model_file: Path
    alpha: float
    l1_ratio: float
    target_column: str

