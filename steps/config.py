from pydantic import BaseModel

class ModelNameConfig(BaseModel):
    """Configuration for model selection."""
    modelname: str = 'LinearRegression'
