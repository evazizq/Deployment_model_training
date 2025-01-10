import sys
import os
# Agregar la raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.data.data_loader import load_data
from src.data.data_processor import process_data
import pandas as pd
#from src.data.data_splitter import split_data
#from src.model.trainer import train_model
#from src.model.evaluator import evaluate_model
#from src.model.saver import save_model

def main():
    print("comienza a correr entrenamiento")
    # Cargar los datos
    data = load_data(file_path = "data/raw/heart_disease.csv")
    print(data.head())












if __name__ == "__main__":
    main()