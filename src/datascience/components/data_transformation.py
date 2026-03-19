import os
from src.datascience.constants import *
from src.datascience.utils.logger import logging
from sklearn.model_selection import train_test_split
from src.datascience.utils.common import read_yaml, create_directories
from pathlib import Path
import pandas as pd
from src.datascience.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):  # ✅ fixed name
        # create folder
        Path(self.config.root_dir).mkdir(parents=True, exist_ok=True)

        logging.info("Reading the data from the data path")

        df = pd.read_csv(self.config.data_path, sep=";")  # ✅ fixed

        logging.info("Splitting the data into train and test sets")

        train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

        logging.info("Saving transformed data")

        train_df.to_csv(self.config.transformed_train_file, index=False)
        test_df.to_csv(self.config.transformed_test_file, index=False)

        logging.info("Data transformation completed")

        logging.info(f"Train file: {self.config.transformed_train_file}")
        logging.info(f"Test file: {self.config.transformed_test_file}")

        logging.info(f"Train shape: {train_df.shape}")
        logging.info(f"Test shape: {test_df.shape}")


