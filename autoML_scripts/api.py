from pyexpat import model
import shutil
import pickle
import os

from dotenv import load_dotenv
import pandas as pd
from supervised.automl import AutoML
from sklearn.metrics import accuracy_score
from minio import Minio

from flask import Flask, request
app = Flask(__name__)


# load minio secret key & access key
load_dotenv()
access_key = os.getenv('access_key')
secret_key = os.getenv('secret_key')
# load data from minio
client = Minio("10.0.105.60:9000", access_key=access_key,
                    secret_key=secret_key,
                    secure=False)

@app.route('/')
def start_screen():
    return 'Welcome to the occupancy model!'

@app.route('/prediction', methods=["POST"])
def prediction():
    df = pd.DataFrame()
    # load model from minio
    model = client.get_object("mlflowbucket","automl_ki_lab_occupancy.pkl")
    model = pickle.loads(model.data)
    AutoML_zip = client.get_object("mlflowbucket","AutoML_1.zip")
    with open("AutoML_1.zip", 'wb') as f:
        pickle.dump(AutoML_zip.data, f)
    shutil.unpack_archive("./AutoML_1.zip","./AutoML_1")

    content_type = request.headers.get('Content-Type')
    if(content_type == 'application/json'):
        json = request.json
        # "illuminance","time","temperature"
        df["illuminance"] = [json["illuminance"]]
        df["time"] = [json["time"]]
        df["temperature"] = [json["temperature"]]
        pred = str(model.predict(df)[0])
        shutil.rmtree("./AutoML_1", ignore_errors=True)
        shutil.rmtree("./AutoML_1.zip", ignore_errors=True)
        return pred
    else: 
        return 'Content-Type not supported!'
        
    

if __name__ == "__main__":
    app.run(host="0.0.0.0")