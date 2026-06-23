import sys
import os
from src.student.exception import CustomException
from src.student.logger import logging
from src.student.utils import fetch_data

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    train_data_path = os.path.join('artifact','train.csv')
    test_data_path = os.path.join('artifact','test.csv')
    raw_data_path = os.path.join('artifact','raw.csv')

class DataIngestion:
    def __init__(self):
        self.dbconfig=DatabaseConfig()
        logging.info('Data fetching successfully done')
    def initiate_data_ingestion(self):
        try:
            df = fetch_data()
            os.makedirs(os.path.dirname(self.dbconfig.train_data_path),exist_ok=True)
            df.to_csv(self.dbconfig.raw_data_path,header=True,index=False)
            train_data,test_data = train_test_split(df,test_size=0.2,random_state=42)
            train_data.to_csv(self.dbconfig.train_data_path,header=True,index=False)
            test_data.to_csv(self.dbconfig.test_data_path,header=True,index=False)

            return(
                self.dbconfig.train_data_path,
                self.dbconfig.test_data_path
            )

        except Exception as e :
            raise CustomException(e,sys)
