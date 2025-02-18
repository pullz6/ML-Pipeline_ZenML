import logging
from zenml import step 
import pandas as pd
from sklearn.base import RegressorMixin 
from zenml.client import Client 
import mlflow
from src.evaluation import MSE,RMSE, R2 
from typing import Tuple
from typing_extensions import Annotated

@step 
def evaluate_model(model: RegressorMixin, X_test: pd.DataFrame, y_test: pd.DataFrame ) -> Tuple[Annotated[float, 'r2'],Annotated[float, 'rmse']]: 
    """
    Evaluates the model on the ingested data. 
    
    Args: 
    df: the ingested data 
    """
    try: 
        experiment_name = "customer-satisfaction-experiment"
        mlflow.set_experiment(experiment_name)
        prediction = model.predict(X_test)
        mse_class = MSE()
        mse = mse_class.calculate_scores(y_test, prediction)
        mlflow.log_metric("mse",mse)
        
        r2_class = R2()
        r2 = r2_class.calculate_scores(y_test, prediction)
        mlflow.log_metric("r2",mse)
        
        rmse_class = RMSE()
        rmse = rmse_class.calculate_scores(y_test, prediction)
        mlflow.log_metric("rmse",mse)
        
        return r2, rmse
    except Exception as e: 
        logging.error("Evalutating the model {}".format(e))
        raise e
    
    

