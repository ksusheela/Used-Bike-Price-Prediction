from flask import Flask, request, render_template
import pandas as pd
import os, sys
from src.pipeline.prediction_pipeline import CustomData, PredictionPipeline


app = Flask(__name__)

# localhost:5000

@app.route("/", methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        csv_data = pd.read_csv(os.path.join("artifacts", "raw.csv"))
        return render_template("form.html", bike_name = csv_data["bike_name"].unique(), city = csv_data["city"].unique())
    
    else:
        data = CustomData(
            bike_name = request.form.get("bike_name"),
            city = request.form.get("city"),
            kms_driven = float(request.form.get("kms_driven")),
            owner = int(request.form.get("owner")),
            age = float(request.form.get("age")),
            power = float(request.form.get("power")),
            brand = int(request.form.get("brand"))
        )

    final_data = data.get_data_as_data_frame()
    predict_pipeline = PredictionPipeline()
    pred = predict_pipeline.Predict(final_data)

    result = round(pred[0], 2)

    return render_template("form.html", final_result = "your bike price is: {}".format(result))


if __name__ == '__main__' :
    app.run(debug=True)   # locahost:5000    