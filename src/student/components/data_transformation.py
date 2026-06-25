import os
import sys

from sklearn.preprocessing import StandardScaler
from src.student.exception import CustomException
from src.student.logger import logging
from src.student.utils import save_object
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import pandas as pd
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    transformation_path = os.path.join('artifact','transformation.pkl')

class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()

    @staticmethod
    def initiate_data_transformation(self):

        try:
            numerical_columns = ['Hours Studied','Previous Scores','Sleep Hours','Sample Question Papers Practiced']
            categorical_column = ['Extracurricular Activities']

            numerical_pipeline = Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='mean')),
                ('scaler',StandardScaler())
            ])

            categorical_pipeline = Pipeline(steps=[
                ('encoder',OneHotEncoder()),
                ('scaler',StandardScaler(with_mean=False))
            ])

            preprocessor = ColumnTransformer([
                ('numerical_pipeline',numerical_pipeline,numerical_columns),
                ('categorical_pipeline',categorical_pipeline,categorical_column)
            ]
            )
            logging.info('data preprocessed successfully')
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)


    def data_transformation(self,train_path,test_path):
        try:
            train_data= pd.read_csv(train_path)
            test_data= pd.read_csv(test_path)

            logging.info("Reading data from datasets")

            preprocessor_obj= self.initiate_data_transformation(self)

            target = 'Performance Index'
            numerical_columns = ['Hours Studied', 'Previous Scores', 'Sleep Hours', 'Sample Question Papers Practiced']

            ## dividing both training and testing datasets into dependent and independent features
            train_df = train_data.drop([target],axis=1)
            target_feature_train_data = train_data[target]

            test_df = test_data.drop([target],axis=1)
            target_feature_test_data = test_data[target]

            logging.info("Applying data transformation")
            train_data_df=preprocessor_obj.fit_transform(train_df)
            test_data_df =preprocessor_obj.transform(test_df)

            ## Combining both dependent and independent variables
            train_arr = np.c_[train_data_df,np.array(target_feature_train_data)]
            test_arr = np.c_[test_data_df,np.array(target_feature_test_data)]

            logging.info('Data transformed successfully')

            save_object(
                file_path= self.config.transformation_path,
                obj=preprocessor_obj
            )

            return(
                train_arr,
                test_arr,
                self.config.transformation_path
            )



        except Exception as e:
           raise CustomException(e,sys)