import os
import pickle
import sys
import pandas as pd

from dotenv import load_dotenv
from urllib.parse import quote_plus
from src.student.logger import logging
from src.student.exception import CustomException
from sqlalchemy import create_engine

import dotenv

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
dbname = os.getenv('dbname')

## we are using this because in password we have @ in it so parser is confusing
password = quote_plus(os.getenv("password"))

def fetch_data():
    logging.info('reading data from database started')
    try:
        mydb = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}/{dbname}"
        )
        logging.info("Connection Established")
        df = pd.read_sql_query('Select * from student_performance', mydb)
        print(df.head())
        logging.info('data fetched successfully')
        return df


    except Exception as e:
        raise CustomException(e,sys)


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)