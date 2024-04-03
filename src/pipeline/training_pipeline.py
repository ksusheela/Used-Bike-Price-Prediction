import os, sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTraining

# TO Execute our Training Pipeline

if __name__=="__main__":
    obj = DataIngestion()
    train_data_path,test_data_path = obj.initiated_data_ingestion()

    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initatie_data_transformation(train_data_path, test_data_path)
    #print(train_arr.shape, test_arr.shape)

    model_training = ModelTraining()
    model_training.initaied_model_training(train_arr, test_arr)