import logging
import os, sys
from datetime import datetime

LOG_DIR = "logs" # Folder / Directory


LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

os.makedirs(LOG_DIR, exist_ok= True)

#logs/2024-03-08:19:16.log

#logs/log_2024-03-08:19:16.log


CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

file_name = f"log_{CURRENT_TIME_STAMP}.log"

log_file_name = os.path.join(LOG_DIR, file_name)

logging.basicConfig(filename=log_file_name,
                    filemode = 'w', 
                    format= '%(asctime)s %(levelname)s %(name)s %(message)s',
                    level=logging.INFO)
                    