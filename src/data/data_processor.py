import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def process_data(df: pd.DataFrame, columns_to_impute: list, target_column: str = None) -> tuple[pd.DataFrame, pd.Series]:
    """
    Procesa los datos:
    - Imputa los valores faltantes
    - Escalar las variables numéricas

    Args:
        data (pd.DataFrame): DataFrame con los datos a procesar.

    Returns:
        pd.DataFrame: DataFrame con los datos procesados
    """

# 