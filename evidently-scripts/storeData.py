import pandas as pd
import subprocess
from minio import Minio
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab, CatTargetDriftTab, ClassificationPerformanceTab

from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection, CatTargetDriftProfileSection, ClassificationPerformanceTab

import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

load_dotenv()


# Get environment variables
ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

client = Minio(
    "10.0.105.60:9000",
    access_key=ACCESS_KEY,
    secret_key=SECRET_KEY,
    secure=False
)

# Make 'evidently' bucket if not exist

found = client.bucket_exists("evidently")
if not found:
    client.make_bucket("evidently")
else:
    print("Bucket 'evidently' already exists")

data = client.get_object("evidently","influxDataLast30Days.csv")

# save data as file
with open("tmp.csv", "w") as file:
    print(data.data.decode('ascii'),file=file)
# save data as dataframe
iris_frame = pd.read_csv("tmp.csv")

# load data from minio
data = client.get_object("database","influxDataLast1Days.csv")

# save data as file
with open("test.csv", "w") as file:
    print(data.data.decode('ascii'),file=file)
# save data as dataframe
currentData = pd.read_csv("test.csv")


iris_frame['target'] = iris_frame.occupancy
currentData['target'] = currentData.occupancy

current = int(len(iris_frame.index)*0.03)

#Target and Data Drift Dashboard
iris_data_and_target_drift_dashboard = Dashboard(tabs=[DataDriftTab(verbose_level=0), CatTargetDriftTab(verbose_level=0), ClassificationPerformanceTab(verbose_level=0)])
iris_data_and_target_drift_dashboard.calculate(iris_frame, currentData, column_mapping=None)
iris_data_and_target_drift_dashboard.show()

iris_data_and_target_drift_dashboard.save('index.html')
# load HTML file to MinIO
client.fput_object(
    "evidently", "index.html", "./index.html",
)
print(
    "HTML file is successfully uploaded to bucket 'evidently'."
)
