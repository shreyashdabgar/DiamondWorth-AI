import os 
import sys 
import numpy as np 
import pandas as pd 
import pickle

from src.exception import CustomException
from sklearn.metrics import r2_score
import logging

# Fixing `save_object` function
def save_object(file_path, obj):
    try:
        dir_name = os.path.dirname(file_path)
        os.makedirs(dir_name, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(models, x_train, y_train, x_test, y_test):
        report = {}
        for name, model in models.items():
            logging.info(f"Training model: {name}")
            model.fit(x_train, y_train)
    
            y_train_predict = model.predict(x_train)
            y_test_predict = model.predict(x_test)
    
            train_model_score = r2_score(y_train, y_train_predict)
            test_model_score = r2_score(y_test, y_test_predict)
    
            report[name] = {
                "train_score": train_model_score,
                "test_score": test_model_score
            }
        return report