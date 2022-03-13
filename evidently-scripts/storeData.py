import subprocess
from minio import Minio
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
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

# Make 'evidently' bucket if not exist. Durch Evidently existiert schon eins

found = client.bucket_exists("evidently")
if not found:
    client.make_bucket("evidently")
else:
    print("Bucket 'evidently' already exists")
    
cmd = client.get_object("evidently","influxQueryLast30Days.sql")
query= cmd.data.decode('ascii')


print('running: ' + query)
subprocess.call(query, shell=True)

iris_frame = pd.read_csv("influxData.csv")

# load data from minio
data = client.fget_object("database","influxDataLast1Days.csv")

# save data as file
with open("test.csv", "w") as file:
    print(data.data.decode('ascii'),file=file)
# save data as dataframe
current = pd.read_csv("test.csv")

iris_frame['target'] = iris_frame.occupancy

#Target and Data Drift Dashboard
iris_data_and_target_drift_dashboard = Dashboard(tabs=[DataDriftTab(verbose_level=0), CatTargetDriftTab(verbose_level=0)])
iris_data_and_target_drift_dashboard.calculate(iris_frame[:current], iris_frame[current:], column_mapping=None)
iris_data_and_target_drift_dashboard.show()

iris_data_and_target_drift_dashboard.save('index.html')
# load HTML file to MinIO
client.fput_object(
    "evidently", "index.html", "./index.html",
)
print(
    "HTML file is successfully uploaded to bucket 'evidently'."
)
