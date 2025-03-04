import os
import sys
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

from src.logger import logging
from src.exception import CustomException
from src.utils import *
from dataclasses import dataclass


@dataclass
class modeltrainerconfig:
    trained_model_pkl_file_path = os.path.join("artifacts", "model.pkl")


class model_trainer:
    def __init__(self):
        self.model_trainer_config = modeltrainerconfig()

    def start_model_training(self, train_arr, test_arr):
        try:
            logging.info("Starting train-test split")
            x_train, y_train, x_test, y_test = (
                train_arr[:, :-1],  # Features for training
                train_arr[:, -1],   # Target for training
                test_arr[:, :-1],   # Features for testing
                test_arr[:, -1]     # Target for testing
            )

            logging.info("Defining models")
            models = {
                "Linear Regression": LinearRegression(),
                "Ridge Regression": Ridge(),
                "Lasso Regression": Lasso(),
                "ElasticNet Regression": ElasticNet(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest": RandomForestRegressor(),
                # "Gradient Boosting": GradientBoostingRegressor(),
                # "AdaBoost": AdaBoostRegressor(),
                # "Support Vector Regressor": SVR(),
                # "K-Neighbors Regressor": KNeighborsRegressor()
                
            }

            model_report:dict = evaluate_models(models, x_train, y_train, x_test, y_test)
            print(model_report)
            logging.info(f'out model report is{model_report}')

            # getting best score from dictionary
           # Get the best model based on highest test_score
            best_model_name = max(model_report, key=lambda x: model_report[x]['test_score'])
            best_model_score = model_report[best_model_name]['test_score']

            # Ensure models dictionary has the best model
            if best_model_name not in models:
                raise ValueError(f"Model '{best_model_name}' not found in models dictionary.")

            best_model_object = models[best_model_name]


            print(f'checking best model name is {best_model_name} and best model score is {best_model_score}')

            save_object(
                file_path = self.model_trainer_config.trained_model_pkl_file_path,
                obj = best_model_object
            )

           

            logging.info("Model training completed for all models.")

        except Exception as e:
            raise CustomException(e, sys)