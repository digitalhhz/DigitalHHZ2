import subprocess
from minio import Minio
import os
from dotenv import load_dotenv
load_dotenv()

topic = 'DHHZ/024/RearArea/Motion3'
lastDays = 1

query = """"SELECT temperature AS temperature, illuminance AS illuminance FROM digitalhhz2.autogen.mqtt_consumer WHERE  time <= now() and time >= now() - """ + str(lastDays) + """d  AND topic='DHHZ/024/EntryArea/Motion1'" """
cmd = "influx -database 'digitalhhz2' -execute " + query + " -format csv > influxData.csv"

print('running: ' + cmd)
subprocess.call(cmd, shell=True)

# Get environment variables
ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

client = Minio(
    "10.0.105.60:9000",
    access_key=ACCESS_KEY,
    secret_key=SECRET_KEY,
    secure=False
)

# Make 'database' bucket if not exist.
found = client.bucket_exists("database")
if not found:
    client.make_bucket("database")
else:
    print("Bucket 'database' already exists")

# Upload 'influxData.csv' to bucket 'database'.
client.fput_object(
    "database", "influxData.csv", "./influxData.csv",
)
print(
    "'influxData.csv' is successfully uploaded as to bucket 'database'."
)
