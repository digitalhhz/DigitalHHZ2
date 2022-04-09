#include <Arduino.h>
#include <M5StickC.h>
#include <Wire.h>

#include <DHT12.h>
#include <Adafruit_BMP280.h>


#include "dislpay.h"
#include "mqttClient.h"
#include "jsonString.h"

const int ledPin = 10;
const char* SSID = "******";
const char* PSK = "******";
const char * MQTT_BROKER = ""******";";
const char * BROKER_PSK = "******";
const char * BROKER_USER = "******";
const unsigned int port = 1883;


//DHT12
DHT12 dht;
//global
float temp;
float humid;
bool dhtValuesArrived = false;


void pushTempHumid(void *parameter) {

    while (true) {
        dht.read();
        temp = dht.readTemperature();
        humid = dht.readHumidity();
        dhtValuesArrived = true;
        vTaskDelay(30000 / portTICK_PERIOD_MS); //30 sec period

    }
}


void setup() {
    M5.begin(true, true, true);
    M5.Lcd.setRotation(1);
    printlnString("running....");
    delay(1000);
    Serial.begin(115200);
//    Wire.begin();
    Wire.begin(0, 26);
    setupWifi(SSID, PSK);
    setupMQTTClient(MQTT_BROKER,port, BROKER_USER,BROKER_PSK);

//  DHT12 ------------------------>
    xTaskCreate(pushTempHumid, "pushDHTData", 30000, NULL, 1, NULL);

}


void loop() {
//    client.startLoop();
//printString(getTimeStamp());
//delay(10000);
    if(dhtValuesArrived) {
        startLoop();
        setupNTP();
        setupDisplay();
        sendMQTTMessage("DHHZ/229/workingPlaceTv/M5stick/humidity",
                        createJsonString("M5stick-10",getTimeStamp().c_str(), "%", humid));
        sendMQTTMessage("DHHZ/229/workingPlaceTv/M5stick/temperature",
                        createJsonString("M5stick-10", getTimeStamp().c_str(), "C", temp));
        printString("Hot & Wet");
        dhtValuesArrived= false;
    }


    delay(2000);
    setupDisplay();
}