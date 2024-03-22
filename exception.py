from flask import Flask
from src.logger import logging
from src.exception import CustomException
import sys
app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():

    try:
        raise Exception("We are testing our custome exception file")
    
    except Exception as e:
        test = CustomException(e, sys)

    logging.info(test.error_message)

    return "One to One mentosdhip sesstion"


if __name__ == '__main__':
    app.run(debug=True) # 500                    