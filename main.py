from src.datascience.utils.logger import logging
from src.datascience.pipeline.data_Ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline


# =========================
# Data Ingestion Stage
# =========================
STAGE_NAME = "Data Ingestion Stage"

try:
    logging.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")

    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()

    logging.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")

except Exception as e:
    logging.exception(e)
    raise e


# =========================
# Data Validation Stage
# =========================
STAGE_NAME = "Data Validation Stage"

try:
    logging.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")

    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.initiate_data_validation()

    logging.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")

except Exception as e:
    logging.exception(e)
    raise e


# =========================
# Data Transformation Stage
# =========================

STAGE_NAME = "Data Transformation Stage"

try:
    logging.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation() 
    logging.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
except Exception as e:
    logging.exception(e)
    raise e