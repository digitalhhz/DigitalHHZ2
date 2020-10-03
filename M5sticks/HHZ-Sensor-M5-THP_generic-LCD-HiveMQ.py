from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt
import hat
import hat

setScreenColor(0x000000)

hat_env1 = hat.get(hat.ENV)

m5mqtt = M5mqtt('clientid', 'broker.hivemq.com', 1883, '', '', 300)


room = None
deviceid = None
basetopic = None
interval = None
temperature = None
pressure = None
humidity = None



lcd.clear()
lcd.font(lcd.FONT_DefaultSmall)
room = 125
deviceid = 'm5stick1'
basetopic = (str('hhz/') + str(((str(room) + str(((str('/') + str(deviceid))))))))
m5mqtt.start()
interval = 60
m5mqtt.publish(str(((str(basetopic) + str('/status')))),str('Online'))
while True:
  lcd.print(((str('Charging:     ') + str((axp.getChargeState())))), 0, 0, 0xffffff)
  temperature = hat_env1.temperature
  lcd.print(((str('Temperature:') + str(temperature))), 0, 120, 0xffffff)
  m5mqtt.publish(str(((str(basetopic) + str('/temperature')))),str(temperature))
  pressure = hat_env1.pressure
  lcd.print(((str('Pressure:     ') + str(pressure))), 0, 80, 0xffffff)
  m5mqtt.publish(str(((str(basetopic) + str('/pressure')))),str(pressure))
  humidity = hat_env1.humidity
  lcd.print(((str('Humidity:     ') + str(humidity))), 0, 40, 0xffffff)
  m5mqtt.publish(str(((str(basetopic) + str('/humidity')))),str(humidity))
  wait(int(interval))
  wait_ms(2)
