import logging
import pandas as pd
from zenml import step

@step
def evaluate_mode(df: pd.DataFrame) -> None:
    pass