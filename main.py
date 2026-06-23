import sys
from src.student.logger import logging
from src.student.exception import CustomException
from src.student.components.data_ingestion import DataIngestion

if __name__ == '__main__':
    try:
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        raise CustomException(e,sys)
    # logging.info('execution started')