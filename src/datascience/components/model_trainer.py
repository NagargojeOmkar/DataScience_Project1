import pandas as pd
import yaml
from pathlib import Path
from datetime import datetime

from src.datascience.utils.logger import logging
from src.datascience.entity.config_entity import ModelTrainerConfig
from sklearn.linear_model import ElasticNet
import joblib



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self):
        # create directory
        Path(self.config.root_dir).mkdir(parents=True, exist_ok=True)

        # check files
        if not self.config.training_data.exists():
            raise FileNotFoundError(f"❌ Training file not found: {self.config.training_data}")

        if not self.config.testing_data.exists():
            raise FileNotFoundError(f"❌ Testing file not found: {self.config.testing_data}")

        logging.info("Reading training data")
        train_df = pd.read_csv(self.config.training_data)

        logging.info("Reading testing data")
        test_df = pd.read_csv(self.config.testing_data)

        # split
        X_train = train_df.drop(columns=[self.config.target_column])
        y_train = train_df[self.config.target_column]

        X_test = test_df.drop(columns=[self.config.target_column])
        y_test = test_df[self.config.target_column]

        # train model
        logging.info("Training ElasticNet model")
        model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio)
        model.fit(X_train, y_train)

        from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
        import numpy as np
        
        # Predict
        y_pred = model.predict(X_test)
        
        # Metrics
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        
        # Logging
        logging.info(f"MAE: {mae}")
        logging.info(f"MSE: {mse}")
        logging.info(f"RMSE: {rmse}")
        logging.info(f"R2 Score: {r2}")

        # save model
        joblib.dump(model, self.config.trained_model_file)

        logging.info(f"✅ Model saved at: {self.config.trained_model_file}")
