from pyexpat import model
import shutil
import pickle
import os

from dotenv import load_dotenv
import pandas as pd
from supervised.automl import AutoML
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
from minio import Minio
from minio.error import S3Error
from minio.select import SelectRequest, CSVInputSerialization, CSVOutputSerialization
from supervised.preprocessing.eda import EDA
from sklearn.model_selection import train_test_split

# load minio secret key & access key
load_dotenv()
access_key = os.getenv('access_key')
secret_key = os.getenv('secret_key')
# load data from minio
client = Minio("10.0.105.60:9000", access_key=access_key,
                    secret_key=secret_key,
                    secure=False)
# load model from minio
model = client.get_object("mlflowbucket","automl_ki_lab_occupancy.pkl")
model = pickle.loads(model.data)
AutoML_zip = client.get_object("mlflowbucket","AutoML_1.zip")
with open("AutoML_1.zip", 'wb') as f:
    pickle.dump(AutoML_zip.data, f)
shutil.unpack_archive("./AutoML_1.zip","./AutoML_1")
# load data from minio
data = client.get_object("database","influxDataLast1Days.csv")
# save data as file
with open("test.csv", "w") as file:
    print(data.data.decode('ascii'),file=file)
# save data as dataframe
df = pd.read_csv("test.csv")
# predictor and target 
X = df[["illuminance","time","temperature"]]
y = df["occupancy"]
# prediction
pred = model.predict(X)
print(pred)
# delete results
shutil.rmtree("./AutoML_1", ignore_errors=True)
os.remove("./AutoML_1.zip")



