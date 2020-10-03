#!/usr/bin/env python
import time
import os
try:
    import paho.mqtt.client as mqtt
except:
    os.system("pip install paho-mqtt")
    import paho.mqtt.client as mqtt

try:
    import pandas as pd
except:
    os.system("pip install pandas")
    import pandas as pd

def replay(df, factor, simulation_room):
    client = mqtt.Client()
    client.connect("mqtt.eclipse.org", 1883, 60)
    client.loop_start()
    print('Replay läuft')
    for ind in df.index:
        orig_topic = str(df['mqtt_consumer.topic'][ind])
        new_topic= orig_topic.split('/')
        topic = 'hhz/' + str(simulation_room)
        for element in new_topic[2:]:
            topic =topic +'/'+ element
        #client.publish(df['mqtt_consumer.topic'][ind], df['mqtt_consumer.value'][ind])
        client.publish(topic, df['mqtt_consumer.value'][ind])
        a = df['time1'][ind]
        b = df['time1'][ind + 1]
        sleeptime = (b - a) / 1000000000/ factor
        print('Sleeptime: ' + str(sleeptime))
        time.sleep(sleeptime)
def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 800)
    print('Hallo das ist das Digital HHZ CSV Replay-Tool')
    name = str(input('Name der CSV-Datei ohne Dateiendung: '))
    speed_factor = int(input('Beschleunigungsfaktor normal = 1 doppelte Geschwindigkeit = 2: '))
    simulation_room = str(input('Simulationstopic: '))
    file = str(name + '.csv')
    df = pd.read_csv(file)
    data = df.drop([0], axis=0)
    data['time'] = pd.to_datetime(data['time'], format ='%Y-%m-%d %H:%M:%S.%f', origin='unix')
    print(type(data['time']))
    data['time1'] = pd.Series.astype(data['time'], 'int64')
    print(data.head())
    print('Lesen erfolgreich')
    replay(data, speed_factor, simulation_room)
if __name__ == "__main__":
    main()