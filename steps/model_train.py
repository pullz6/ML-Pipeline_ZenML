import logging
import pandas as pd 
from zenml import step 
from src.model_dev import LinearRegressionModel
from sklearn.base import RegressorMixin 
from .config import ModelNameConfig
config = ModelNameConfig(modelname="LinearRegression")

from zenml.client import Client 

experiment_tracker = Client().active_stack.experiment_tracker

import mlflow 



@step(experiment_tracker=experiment_tracker.name)
def train_model(X_train: pd.DataFrame,X_test:pd.DataFrame,y_train:pd.DataFrame,y_test:pd.DataFrame, model_name: str  = "LinearRegression" ) -> RegressorMixin: 
    """
    Trains the model on the ingested data 
    
    Args: 
        df: the ingested data 
    
    """
    try: 
        if model_name == 'LinearRegression': 
            mlflow.sklearn.autolog()
            model=LinearRegressionModel()
            trained_model = model.train(X_train,y_train)
            return trained_model 
        else: 
            raise ValueError("Model {} not supported".format(config.modelname))
    except Exception as e: 
        logging.error("Error in training model: {}".format(e))
        raise e
        