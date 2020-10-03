from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt
import hat
import hat

setScreenColor(0x000000)

hat_env1 = hat.get(hat.ENV)

m5mqtt = M5mqtt(___O_26Mqz__v_P5_KG_, 'hhzpi.fritz.box', 1883, '', '', 300)


interval = None
room = None
basetopic = None
deviceid = None
temperature = None
pressure = None
humidity = None


def fun__basetopic_____interval___(topic_data):
  global interval, room, basetopic, deviceid, temperature, pressure, humidity
  interval = topic_data
  pass
m5mqtt.subscribe(str(((basetopic + '/interval'))), fun__basetopic_____interval___)


room = 125
deviceid = 'm5stick1'
basetopic = ('hhz/' + ((room + (('/' + deviceid)))))
m5mqtt.start()
interval = 60
m5mqtt.publish(str(((basetopic + '/status'))),str('Online'))
while True:
  lcd.print((('Ladestatus: ' + (axp.getChargeState()))), 10, 10, 0xffffff)
  temperature = hat_env1.temperature
  lcd.print((('Temperature: ' + temperature)), 10, 40, 0xffffff)
  m5mqtt.publish(str(((basetopic + '/temperature'))),str(temperature))
  pressure = hat_env1.pressure
  lcd.print((('Pressure: ' + pressure)), 10, 30, 0xffffff)
  m5mqtt.publish(str(((basetopic + '/pressure'))),str(pressure))
  humidity = hat_env1.humidity
  lcd.print((('Humidity: ' + humidity)), 10, 20, 0xffffff)
  m5mqtt.publish(str(((basetopic + '/humidity'))),str(humidity))
  wait(int(interval))
  wait_ms(2)
