import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.data.data_loader import load_data
from src.data.data_processor import process_data
import pandas as pd
from src.data.data_splitter import split_data
from src.model.trainer import train_model
from src.model.evaluator import evaluate_model
from src.model.saver import save_model

def main():

# Carga de datos
    data = load_data(file_path = "data/raw/heart_disease.csv")
    data.columns = data.columns.str.replace(' ', '')

# Preprocesamiento de datos
    processed_data, target = process_data(
                                        df=data, columns_to_impute=['trestbps', 'chol', 'thalach', 'oldpeak'],
                                        target_column='num'
                                        )

# Conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = split_data(processed_data, target_column='num')

    y_train_binary = (y_train > 0).astype(int)
    y_test_binary = (y_test > 0).astype(int)

# Entrenamiento del modelo
    model = train_model(X_train=X_train, y_train=y_train_binary)

# Evaluaacion del modelo
    accuracy, precision, recall, f1, auc = evaluate_model(model, test_data=X_test, y_test=y_test_binary)

# Impresion de metricas resultantes
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1: {f1:.2f}")
    print(f"AUC: {auc:.2f}")

# Model saver
    save_model(model, model_path="models/trained_model")

if __name__ == "__main__":
    main()
