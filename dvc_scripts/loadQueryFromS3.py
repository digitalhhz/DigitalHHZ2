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

# get query from minio
found =client.bucket_exists("database")
if not found:
    client.make_bucket("database")
else:
    print("bucket already exists!")

if not os.path.exists('/app/cogitat/query/'):
    os.makedirs('/app/cogitat/query/')

query = client.fget_object("database","influxQueryLast30Days.sql","influxQueryLast30Days.sql")
os.replace("./influxQueryLast30Days.sql","/app/cogitat/query/influxQueryLast30Days.sql")