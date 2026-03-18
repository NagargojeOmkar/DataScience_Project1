import os
import yaml
import json
import joblib

from pathlib import Path
from typing import Any

from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError

from src.datascience.utils.logger import logging


# =========================
# 1️⃣ READ YAML FILE
# =========================

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads yaml file and returns ConfigBox object
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"YAML file loaded successfully from: {path_to_yaml}")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("YAML file is empty")

    except Exception as e:
        raise e


# =========================
# 2️⃣ CREATE DIRECTORIES
# =========================

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"Created directory at: {path}")


# =========================
# 3️⃣ SAVE JSON FILE
# =========================

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save data to json file
    """

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"JSON file saved at: {path}")


# =========================
# 4️⃣ LOAD JSON FILE
# =========================

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load json file data
    """

    with open(path) as f:
        content = json.load(f)

    logging.info(f"JSON file loaded from: {path}")
    return ConfigBox(content)


# =========================
# 5️⃣ SAVE BINARY FILE (MODEL)
# =========================

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary file (model, scaler, etc.)
    """

    joblib.dump(data, path)
    logging.info(f"Binary file saved at: {path}")


# =========================
# 6️⃣ LOAD BINARY FILE
# =========================

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary file
    """

    data = joblib.load(path)
    logging.info(f"Binary file loaded from: {path}")
    return data