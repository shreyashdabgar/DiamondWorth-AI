from flask import Flask,request,render_template
import numpy as np 
import pandas as pd 

from sklearn.preprocessing import StandardScaler
from src.piplines.prediction_pipeline import CustomData,PredictPipeline

application = Flask(__name__)
app = application
app.config["DEBUG"] = True

# route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predicted', methods = ['GET','POST'])
def predict_data():
    if request.method == 'GET':
        return render_template('predction.html')
    else :
        data = CustomData(
            carat=request.form.get('carat'),
            depth=request.form.get('depth'),
            table=request.form.get('table'),
            x=request.form.get('x'),
            y=request.form.get('y'),
            z=request.form.get('z'),
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')

        )
        pred_df = data.get_data_as_dataframe()
        print(pred_df)

        predict_pipline = PredictPipeline()
        results = predict_pipline.predict(pred_df)
        return render_template('predction.html', results =  results[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0')