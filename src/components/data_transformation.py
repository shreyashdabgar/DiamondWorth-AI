## All feture engineering will be done here 

import sys 
import os 
import numpy as np 
import pandas as pd 
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging
from sklearn.preprocessing import OrdinalEncoder
from src.utils import save_object

@dataclass
class datatransformatinconfig():
    pickle_path = os.path.join('artifacts', 'data_tarnsform.pkl')

class datatransformation():
    def __init__(self):
        self.transformation_config = datatransformatinconfig()# initializing the class datatransformatinconfig to one object
    
    # creating feture engineering automation in this function
    def feture_engineering(self):
        logging.info ("staring the feture engineering into data")
        try :
            catogerical_features = ['cut', 'color', 'clarity']
            numeric_features = ['carat', 'depth', 'table', 'x', 'y', 'z']

            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            
            num_pipline = Pipeline(steps = [
                ('imputer', SimpleImputer(strategy='mean')),
                ('scaler', StandardScaler())
                
            ])

            cat_pipline = Pipeline(

                steps = [
                    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
                    ('onehot', OrdinalEncoder(categories=[cut_categories, color_categories, clarity_categories])),
                    ('scaler', StandardScaler())
                ]
            )

            logging.info(f"catogerical features are : {catogerical_features}")
            logging.info(f"numerical features are : {numeric_features}")
            logging.info("combining both pipline using column transformer")

            preporcessor = ColumnTransformer(
                [
                    ('num', num_pipline, numeric_features),
                    ('cat', cat_pipline, catogerical_features)
                ]

            )
            logging.info("feture engineering is completed succesfully")
            return preporcessor
        
        except Exception as e :
            raise CustomException("error in feture engineering", e, sys)
        

    # and after automation of feture engineering we will apply the feture engineering on the train and test data
    def intiate_data_transform(self,train, test):
        try:
            train_df = pd.read_csv(train)# we reading data from this file 
            test_df = pd.read_csv(test) # we reading data from this file

            logging.info("reading the train and test data")
            logging.info("applying the feture engineering on train and test data")
            
            # we intiate preprocesser object(which contain feture engineering aumation pipline) and store into one variable called preprocesing_obj
            preprocesing_obj = self.feture_engineering()
            
            # getting target feture(dependent feature(y)) from the train data
            target_columns = 'price'

            # we are drop unwanted columns and traget columns from the train and test data
            drop_columns = [target_columns,'id']
            x_input = train_df.drop(columns=drop_columns, axis = 1 )
            y_input = train_df[target_columns]#storing the target feture in ouput(dependent) feture variable 

            x_output = test_df.drop(columns=drop_columns, axis = 1 )
            y_output = test_df[target_columns]#storing the target feture in ouput(dependent) feture variable 


            ##apply the transformation on the train data
            logging.info("applying the transformation on the train data")
            x_input_transformd  = preprocesing_obj.fit_transform(x_input)
            x_output_transformed = preprocesing_obj.transform(x_output)

            # merging y_train and test to x_train_transformd and test_tranformed 
            train_arr = np.c_[x_input_transformd, np.array(y_input)]
            test_arr = np.c_[x_output_transformed, np.array(y_output)]


            #creating pickle file and save into the location that we are intlizing first(class datatransformatinconfig())
            save_object(

                file_path = self.transformation_config.pickle_path,
                obj = preprocesing_obj

            )



            return (
                train_arr,
                test_arr,
                self.transformation_config.pickle_path
            )

            

        except Exception as e :
            raise CustomException("error in data transformation", e) 
        
        




