#include <Arduino.h>
#include <M5StickC.h>
#include <Wire.h>

#include "mqttClient.h"
#include "dislpay.h"
#include "vibrationSensor.h"
#include "jsonString.h"

const char* SSID = "*****";
const char* PSK = "*****";
const char * MQTT_BROKER = "*****";
const char * BROKER_PSK = "*****";
const char * BROKER_USER = "*****";
const unsigned int port = 1883;
const int ledPin = 10;
const unsigned int vibPIN= 26;


void setup() {
    M5.begin(true,true,true);
    M5.Lcd.setRotation(1);
    printlnString("running....");
    delay(1000);
    setupWifi(SSID,PSK);
    setupMQTTClient(MQTT_BROKER,port, BROKER_USER,BROKER_PSK);
    Serial.begin(115200);
    pinMode (ledPin, OUTPUT);
    setupVibrationSensor(vibPIN);
}

void loop() {
    int vib =getVibration(vibPIN);
    if (vib > 0) {
        setupNTP();
        startLoop();
        setupDisplay();
        sendMQTTMessage("DHHZ/229/officeAreaDesk1/M5stick/vibrations",createJsonString("M5stick-1", getTimeStamp().c_str(),"m/s^2", vib));
        printString("send some good vibrations!");

    }
    delay(200);
}