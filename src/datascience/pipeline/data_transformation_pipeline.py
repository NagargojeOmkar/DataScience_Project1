import yaml
from src.datascience.components.data_transformation import DataTransformation
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.utils.logger import logging

STAGE_NAME = "Data Transformation Stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            # Read validation status
            with open("artifacts/data_validation/status.yaml", "r") as f:
                status_data = yaml.safe_load(f)

            status = status_data["validation_status"]

            if status:
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()

                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_split()

            else:
                raise Exception("Data Validation failed. Cannot proceed.")

        except Exception as e:
            logging.error(f"Error in Data Transformation: {e}")
            raise e


# ================= RUN =================

if __name__ == "__main__":
    try:
        logging.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")

        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()

        logging.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")

    except Exception as e:
        logging.exception(e)
        raise e