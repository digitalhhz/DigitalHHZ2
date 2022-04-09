#include <Arduino.h>
#include <M5StickC.h>
#include <Wire.h>

#include "dislpay.h"
#include "zx_gesture.h"
#include "mqttClient.h"
#include "jsonString.h"

const int ledPin = 10;
const char* SSID = "*****";
const char* PSK = "*****";
const char * MQTT_BROKER = "*****";
const char * BROKER_PSK = "*****";
const char * BROKER_USER = "*****";
const unsigned int port = 1883;


void setup() {
    M5.begin(true, true, true);
    M5.Lcd.setRotation(1);
    printlnString("running....");
    delay(1000);
    Serial.begin(115200);
    initializeGesture();

    setupWifi(SSID, PSK);
    setupMQTTClient(MQTT_BROKER,port, BROKER_USER,BROKER_PSK);
    delay(1000);
//  gesture sensore
}

void loop() {
    //debounce time

//    gesture sensor ---------->
    const char *gesture = readGesture();
    if (gesture != "NO_GESTURE") {
        startLoop();
        setupDisplay();
        sendMQTTMessage("DHHZ/229/door/M5stick/gesture",
                        createJsonString("M5stick-11",  getTimeStamp().c_str(), "None", gesture));
        printString("gesture detected!");
    }
    delay(200);


}