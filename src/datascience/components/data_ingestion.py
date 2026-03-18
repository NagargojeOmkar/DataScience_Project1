#Component data ingestion

from src.datascience.utils.logger import logging
import os
import urllib.request
import zipfile

class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            logging.info(f"Downloading data from {self.config.source_URL} to {self.config.local_data_file}")
            urllib.request.urlretrieve(self.config.source_URL, self.config.local_data_file)
            logging.info("Data downloaded successfully.")

    def unzip_data(self):
        if not os.path.exists(self.config.unzip_dir):
            os.makedirs(self.config.unzip_dir)

        logging.info(f"Unzipping data from {self.config.local_data_file} to {self.config.unzip_dir}")

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)

        logging.info("Data unzipped successfully.")