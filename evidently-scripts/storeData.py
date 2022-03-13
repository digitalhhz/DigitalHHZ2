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

print('running: ' + cmd)
subprocess.call(cmd, shell=True)

f = open( "influxQueryLast" + str(lastDays) + "Days.sql", 'w' )
f.write( cmd + '\n' )
f.close()

# load data from minio
data = client.fget_object("database","influxDataLast1Days.csv")

# save data as file
with open("test.csv", "w") as file:
    print(data.data.decode('ascii'),file=file)
# save data as dataframe
df = pd.read_csv("test.csv")

