#include "SenseBoxMCU.h"
#include <stdio.h>
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"
#include "SparkFun_SCD30_Arduino_Library.h"
#include <Adafruit_NeoPixel.h>
#define ARDUINOJSON_USE_LONG_LONG 1
#include <ArduinoJson.h>
#include <ezTime.h>

#define OLED_RESET 4

/* WiFi defines */
#define WIFI_NAME  "your_wifi_ssid"       //tbd
#define WIFI_PW    "your_wifi_password"   //tbd

/* MQTT defines*/
#define SERVER     "your_mqtt_server"     //tbd
#define SERVERPORT 1883
#define USERNAME   "your_username"        //tbd
#define PASS       "your_password"        //tbd

/* MQTT topic defines */
#define DHHZ_NAME       "DHHZ"
#define LOC_MACRO       "your_room_no"    //tbd
#define LOC_MICRO       "your_location"   //tbd
#define DEVICE_ID       "your_device_id"  //tbd
#define DEVICETYPE      "SENSEBOX"      
#define SENSORTYPE_TEMP "Temperature"   
#define SENSORTYPE_CO2  "CO2"           
#define SLASH           "/"

/* MQTT payload defines */
#define SI_TEMP         "°C"            
#define SI_CO2          "ppm"           

#define TOPIC_TEMP      DHHZ_NAME SLASH LOC_MACRO SLASH LOC_MICRO SLASH DEVICETYPE DEVICE_ID \
  SLASH SENSORTYPE_TEMP

#define TOPIC_CO2       DHHZ_NAME SLASH LOC_MACRO SLASH LOC_MICRO SLASH DEVICETYPE DEVICE_ID \
  SLASH SENSORTYPE_CO2

uint32_t co2;
float temperature;

Bee* b = new Bee();
Adafruit_SSD1306 display(OLED_RESET);
Adafruit_NeoPixel rgb_led_1 = Adafruit_NeoPixel(1, 1, NEO_GRB + NEO_KHZ800);
WiFiClient client;
Adafruit_MQTT_Client mqtt(&client, SERVER, SERVERPORT, USERNAME, PASS);
SCD30 airSensor;
Adafruit_MQTT_Publish temp_pub = Adafruit_MQTT_Publish(&mqtt, TOPIC_TEMP);
Adafruit_MQTT_Publish co2_pub  = Adafruit_MQTT_Publish(&mqtt, TOPIC_CO2);
DynamicJsonDocument json_temp(1024);
DynamicJsonDocument json_co2(1024);

char h_tim_buf[] = "2018-08-25T14:23:45.846+00:00";
char time_buf[] = "YYYY-MM-ddTHH:mm:ss.SSSZ";
char co2_buf[256];
char temp_buf[256];

void setup()
{
  b->connectToWifi(WIFI_NAME, WIFI_PW);
  delay(1000);
  senseBoxIO.powerI2C(true);
  delay(2000);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3D);
  display.display();
  delay(100);
  display.clearDisplay();
  rgb_led_1.begin();
  rgb_led_1.setBrightness(50);
  Wire.begin();
  if (airSensor.begin() == false)
  {
    display.clearDisplay();
    while (1);
  }

  /* time setup */
  waitForSync();
}


void loop()
{
  MQTT_connect();

  /* clear and rewrite json docs */
  json_temp.clear();
  json_temp["deviceid"] = DEVICE_ID;
  json_temp["si"] = SI_TEMP;
  json_temp["value"] = 0.0;
  json_temp["timestamp"] = 0;

  json_co2.clear();
  json_co2["deviceid"] = DEVICE_ID;
  json_co2["si"] = SI_CO2;
  json_co2["value"] = 0;
  json_co2["timestamp"] = 0;
  
  /* get current timestamp and save to helper array */
  memset(h_tim_buf, 0, 29);
  memset(time_buf, 0, 23);
  UTC.dateTime(RFC3339_EXT).toCharArray(h_tim_buf, sizeof(h_tim_buf));

  /* format according to hhz definitions and store in time array */
  for (int i = 0; i < 23; i++)
  {
    time_buf[i] = h_tim_buf[i];
  }

  // get values
  co2 = (uint32_t)airSensor.getCO2();
  temperature = airSensor.getTemperature();

  // led stuff
  if (( co2 <= 1000))
  {
    rgb_led_1.setPixelColor(0, rgb_led_1.Color(51, 204, 0));
    rgb_led_1.show();
  }
  else if (( co2 <= 1500))
  {
    rgb_led_1.setPixelColor(0, rgb_led_1.Color(255, 153, 0));
    rgb_led_1.show();
  }
  else
  {
    rgb_led_1.setPixelColor(0, rgb_led_1.Color(255, 0, 0));
    rgb_led_1.show();
  }

  // payload preparation: deviceid+si-einheit+value+timestamp
  json_temp["value"] = temperature;
  json_temp["timestamp"] = time_buf;
  memset(temp_buf, 0, 256);
  serializeJson(json_temp, temp_buf);

  json_co2["value"] = co2;
  json_co2["timestamp"] = time_buf;
  memset(co2_buf, 0, 256);
  serializeJson(json_co2, co2_buf);

  // mqtt publishing
  (void)co2_pub.publish(co2_buf);
  (void)temp_pub.publish(temp_buf);

  // Display stuff
  display.clearDisplay();
  printOnDisplay("CO2", String(co2), "ppm", "Temperature", String(temperature), "Celsius");
  display.display();
  delay(10000);
}

// Function to connect and reconnect as necessary to the MQTT server.
// Should be called in the loop function and it will take care if connecting.
void MQTT_connect()
{
  int8_t ret;
  // Stop if already connected.
  if (mqtt.connected())
  {
    return;
  }
  while ((ret = mqtt.connect()) != 0)
  { // connect will return 0 for connected
    mqtt.disconnect();
    display.clearDisplay();
    delay(5000);  // wait 5 seconds
  }
}

void printOnDisplay(String title1, String measurement1, String unit1, String title2, String measurement2, String unit2)
{
  display.setCursor(0, 0);
  display.setTextSize(1);
  display.setTextColor(WHITE, BLACK);
  display.println(title1);
  display.setCursor(0, 10);
  display.setTextSize(2);
  display.print(measurement1);
  display.print(" ");
  display.setTextSize(1);
  display.println(unit1);
  display.setCursor(0, 30);
  display.setTextSize(1);
  display.println(title2);
  display.setCursor(0, 40);
  display.setTextSize(2);
  display.print(measurement2);
  display.print(" ");
  display.setTextSize(1);
  display.println(unit2);
}
