import sys
from src.student.logger import logging
from src.student.exception import CustomException
from src.student.components.data_ingestion import DataIngestion
from src.student.components.data_transformation import DataTransformation

if __name__ == '__main__':
    try:
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        data_transformation = DataTransformation()
        data_transformation.data_transformation(train_data_path,test_data_path)

    except Exception as e:
        raise CustomException(e,sys)
    # logging.info('execution started')