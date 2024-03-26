import os
import sys 
import pickle
import pandas as pd
import numpy as  np 
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
#from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

## This Function is Save Pickel file

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)