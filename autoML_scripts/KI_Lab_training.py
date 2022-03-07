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
data = client.get_object("database","influxDataLast90Days.csv")
# save data as file
with open("test.csv", "w") as file:
    print(data.data.decode('ascii'),file=file)
# save data as dataframe
df = pd.read_csv("test.csv")
# predictor and target 
X = df[["illuminance","time","temperature"]]
y = df["occupancy"]
# split data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
# train model
model = AutoML(total_time_limit=10)
# model.results_path("./AutoML_results")
print(model.results_path)
model.fit(X_train,y_train)
# ## Extended EDA
# To do extended bivariate data analysis of the data, mljar has `extended_eda` method.
# This will do the bivariate analysis of features in the dataframe against the passed target feature.
EDA.extensive_eda(X_train,y_train,save_path="/AutoML_1/")
# save results as dataframe
df_result = pd.read_csv("./AutoML_1/leaderboard.csv")
# track metric on mlflow
mlflow.set_tracking_uri("http://10.0.105.60:5000")
for i in df_result.index:
    with mlflow.start_run():    
        mlflow.set_experiment(f'KI_lab_occupancy_{df_result["name"][i]}')
        mlflow.log_metrics({df_result["metric_type"][i]: df_result["metric_value"][i], "train_time": df_result["train_time"][i]})
        print(df_result["name"][i])
with mlflow.start_run():    
    mlflow.set_experiment(f'KI_lab_occupancy_{df_result["name"][i]}')
    mlflow.log_metrics({df_result["metric_type"][i]: df_result["metric_value"][i], "train_time": df_result["train_time"][i]})
#save model
with open("automl_ki_lab_occupancy.pkl", 'wb') as f:
    pickle.dump(model, f)
# save model and leaderboard on minio
found =client.bucket_exists("mlflowbucket")
if not found:
    client.make_bucket("mlflowbucket")
else:
    print("bucket already exists!")

result_model = client.fput_object("mlflowbucket","automl_ki_lab_occupancy.pkl","./automl_ki_lab_occupancy.pkl")
result_leaderboard = client.fput_object("mlflowbucket","leaderboard_ki_lab_occ.csv","./AutoML_1/leaderboard.csv")

print(
    f"created {result_model.object_name} object; etag: {result_model.etag}, version-id: {result_model.version_id}"
    )
print(
    f"created {result_leaderboard.object_name} object; etag: {result_leaderboard.etag}, version-id: {result_leaderboard.version_id}"
    )
# delete results
shutil.rmtree("./AutoML_1", ignore_errors=True)

