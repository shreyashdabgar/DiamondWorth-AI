import os 
import sys 
import pandas as pd
from src.exception import coustemexception # custom exception created in exception.py
from src.logger import logging # logger created in logger.py
from src.components.data_transformation import datatransformatinconfig,datatransformation

from sklearn.model_selection import train_test_split
from dataclasses import dataclass # dataclass is used to create a class with attributes and methods

@dataclass # we are using this dectorater becuse we doesnt need to create the __init__ method
class dataingestionconfig():
    train_data_path = os.path.join('artifacts', "train.csv") #basically this is we assigning the path of the where to store train.csv file
    test_data_path  = os.path.join('artifacts', "test.csv") #basically this is we assigning the path of the where to store test.csv file
    raw_data_path = os.path.join('artifacts', "data.csv") #basically this is we assigning the path of the where to store data.csv(full data)

class dataingestion():
    def __init__(self):
        self.ingestion_config = dataingestionconfig() # we created here one object(ingestion_config) that store our class dataingestionconfig()

    def read_data(self):
        logging.info("data ingestion is started")        
        try:
            df = pd.read_csv('notbook\gemstone.csv') # reading the dataset
            logging.info("reading the dataset")

            # here we are assuming that our artifacts folder is not created so we are creating the artifacts folder
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            logging.info("creating the artifacts folder")

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True) # here we are saving the df in the raw_data_path

            ## splitting the data into train and test
            train, test = train_test_split(df, test_size= 0.3, random_state=43)
            train.to_csv(self.ingestion_config.train_data_path, index = False, header=True) # here we are saving the train data in the train_data_path
            test.to_csv(self.ingestion_config.test_data_path, index=False, header=True) # here we are saving the test data in the test_data_path

            logging.info("ingestion of data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            ) ## we return only train atest becuase we didnt need raw data in data transformation
        
        except Exception as e:
            logging.error("error in data ingestion")
            raise coustemexception("error in data ingestion",e,sys)
        
if __name__ == "__main__":
    obj = dataingestion()
    train_data ,test_data = obj.read_data()

    data_transformation = datatransformation()
    data_transformation.intiate_data_transform(train_data,test_data)