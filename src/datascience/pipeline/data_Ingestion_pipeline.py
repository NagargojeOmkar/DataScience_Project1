from src.datascience.components.data_ingestion import DataIngestion
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.utils.logger import logging

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(config=data_ingestion_config)

        data_ingestion.download_data()
        data_ingestion.unzip_data()

if __name__ == "__main__":
    try:
        logging.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.initiate_data_ingestion()
        logging.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
    except Exception as e:
        logging.exception(e)
        raise e