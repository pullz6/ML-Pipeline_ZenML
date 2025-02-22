import logging 
from abc import ABC, abstractmethod 

from sklearn.linear_model import LinearRegression

class Model(ABC): 
    @abstractmethod
    def train(self, X_train, y_train): 
        "Trains the model"
        
class LinearRegressionModel(Model): 
    def train(self,X_train,y_train,**kwargs): 
        try: 
            reg= LinearRegression(**kwargs)
            reg.fit(X_train,y_train)
            logging.info('Model Training completed')
            return reg
        except Exeption as e: 
            logging.error('Error in training model: {}'.format(e))
            raise e 
        