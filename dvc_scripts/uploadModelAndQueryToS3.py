import os
import shutil
from minio import Minio
from dotenv import load_dotenv
from pathlib import Path

# load minio secret key & access key
load_dotenv()

client = Minio("10.0.105.60:9000", access_key=os.getenv('S3_USER_DVC'),
                    secret_key=os.getenv('S3_SECRET_DVC'),
                    secure=False)

# upload model and leaderboard to minio mlflowbucket bucket
found =client.bucket_exists("mlflowbucket")
if not found:
    client.make_bucket("mlflowbucket")
else:
    print("bucket already exists!")

pkl = client.fput_object("mlflowbucket","automl_ki_lab_occupancy.pkl","/app/cogitat/data/automl_ki_lab_occupancy.pkl")
leaderboard = client.fput_object("mlflowbucket","leaderboard_ki_lab_occ.csv","/app/cogitat/data/leaderboard_ki_lab_occ.csv")
automl_zip = client.fput_object("mlflowbucket","AutoML_1.zip","/app/cogitat/data/AutoML_1.zip")

# upload query to minio evidently bucket
found =client.bucket_exists("evidently")
if not found:
    client.make_bucket("evidently")
else:
    print("bucket already exists!")

query = client.fput_object("evidently","influxQueryLast30Days.sql","/app/cogitat/query/influxQueryLast30Days.sql")