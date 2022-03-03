import subprocess
from minio import Minio
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
load_dotenv()

topic = 'DHHZ/024/RearArea/Motion3'
lastDays = 1

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


def writeLastDaysToMinIO(lastDays):
    end = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    start = (datetime.now() - timedelta(days=lastDays)).strftime('%Y-%m-%dT%H:%M:%SZ')

    query = """"SELECT temperature, illuminance, occupancy FROM digitalhhz2.autogen.mqtt_consumer WHERE occupancy = 1 OR occupancy = 0 AND time <= '""" + str(end) + """' and time >= '""" + str(start) + """'  AND topic='DHHZ/024/EntryArea/Motion1'" """
    cmd = "influx -database 'digitalhhz2' -execute " + query + " -format csv > influxData.csv"

    print('running: ' + cmd)
    subprocess.call(cmd, shell=True)

    f = open( "influxQueryLast" + str(lastDays) + "Days.sql", 'w' )
    f.write( cmd + '\n' )
    f.close()

    # Upload 'influxData' to bucket 'database'.
    client.fput_object(
        "database", "influxDataLast" + str(lastDays) + "Days.csv", "./influxData.csv",
    )
    print(
        "influxDataLast" + str(lastDays) + "Days.csv is successfully uploaded as to bucket 'database'."
    )

    # Upload 'influxQuery' to bucket 'database'.
    client.fput_object(
        "database", "influxQueryLast" + str(lastDays) + "Days.sql", "./influxQueryLast" + str(lastDays) + "Days.sql",
    )
    print(
        "influxQueryLast" + str(lastDays) + "Days.sql is successfully uploaded as to bucket 'database'."
    )

writeLastDaysToMinIO(1)
writeLastDaysToMinIO(7)
writeLastDaysToMinIO(30)
writeLastDaysToMinIO(90)
