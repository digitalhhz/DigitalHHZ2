import os
import shutil
from minio import Minio
from dotenv import load_dotenv
from pathlib import Path

# load minio secret key & access key
load_dotenv()

# load data from minio
client = Minio("10.0.105.60:9000", access_key=os.getenv('S3_USER_DVC'),
                    secret_key=os.getenv('S3_SECRET_DVC'),
                    secure=False)

# get model and leaderboard from minio
found =client.bucket_exists("mlflowbucket")
if not found:
    client.make_bucket("mlflowbucket")
else:
    print("bucket already exists!")

if not os.path.exists('/app/cogitat/data/'):
    os.makedirs('/app/cogitat/data/')
    
pkl = client.fget_object("mlflowbucket","automl_ki_lab_occupancy.pkl","automl_ki_lab_occupancy.pkl")
os.replace("./automl_ki_lab_occupancy.pkl","/app/cogitat/data/automl_ki_lab_occupancy.pkl")
leaderboard = client.fget_object("mlflowbucket","leaderboard_ki_lab_occupancy.csv","leaderboard_ki_lab_occupancy.csv")
os.replace("./leaderboard_ki_lab_occupancy.csv","/app/cogitat/data/leaderboard_ki_lab_occupancy.csv")
automl_zip = client.fget_object("mlflowbucket","AutoML_1.zip","AutoML_1.zip")
os.replace("./AutoML_1.zip","/app/cogitat/data/AutoML_1.zip")