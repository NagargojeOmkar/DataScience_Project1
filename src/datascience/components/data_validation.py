#src/datascience/components/data_validation.py

import pandas as pd
import yaml
from pathlib import Path
from datetime import datetime

from src.datascience.utils.logger import logging
from src.datascience.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            # =========================
            # Step 0: Check file exists
            # =========================
            if not Path(self.config.local_data_file).exists():
                raise FileNotFoundError(
                    f"File not found: {self.config.local_data_file}"
                )

            # =========================
            # Step 1: Load Data
            # =========================
            data = pd.read_csv(self.config.local_data_file, sep=";")
            logging.info(f"Data loaded from: {self.config.local_data_file}")

            # =========================
            # Step 2: Extract Columns
            # =========================
            all_columns = set(data.columns)
            all_schema = set(self.config.all_schema.keys())

            logging.info(f"Total columns in data: {len(all_columns)}")
            logging.info(f"Total columns in schema: {len(all_schema)}")

            # =========================
            # Step 3: Validation Check
            # =========================
            missing_columns = list(all_schema - all_columns)
            extra_columns = list(all_columns - all_schema)

            validation_status = True

            if missing_columns:
                logging.error(f"Missing columns: {missing_columns}")
                validation_status = False

            if extra_columns:
                logging.warning(f"Extra columns: {extra_columns}")

            if validation_status:
                logging.info("All columns are valid")

            # =========================
            # Step 4: Create Directory
            # =========================
            Path(self.config.root_dir).mkdir(parents=True, exist_ok=True)

            # =========================
            # Step 5: Save Status YAML
            # =========================
            status_data = {
                "validation_status": validation_status,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "missing_columns": missing_columns,
                "extra_columns": extra_columns,
                "total_columns_data": len(all_columns),
                "total_columns_schema": len(all_schema),
                "file_path": str(self.config.local_data_file)
            }

            with open(self.config.STATUS_FILE, "w") as f:
                yaml.dump(status_data, f)

            logging.info(f"Validation report saved at: {self.config.STATUS_FILE}")

            return validation_status

        except Exception as e:
            logging.error(f"Error occurred during validation: {e}")
            raise e