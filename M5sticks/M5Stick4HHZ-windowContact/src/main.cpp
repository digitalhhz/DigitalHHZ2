#include <Arduino.h>
#include <M5StickC.h>

#include "dislpay.h"
#include "jsonString.h"
#include "MQTTClient.h"
#include "WindowContact.h"

const int ledPin = 10;
//@home
const char* SSID = "*****";
const char* PSK = "*****";
const char * MQTT_BROKER = "*****";
const char * BROKER_PSK = "*****";
const char * BROKER_USER = "*****";
const unsigned int port = 1883;

WindowContact winCon;

void windowContact_wrapper(){
    winCon.windowContact_change();
}

void setup() {
    M5.begin();
    M5.Lcd.setRotation(1);
    printlnString("running....");
    delay(1000);
    setupWifi(SSID,PSK);
    setupMQTTClient(MQTT_BROKER,port, BROKER_USER,BROKER_PSK);
    Serial.begin(115200);
    pinMode (ledPin, OUTPUT);
    pinMode(winCon.getWindowContactPin(),INPUT_PULLUP);
    attachInterrupt(winCon.getWindowContactPin(),windowContact_wrapper,CHANGE);


}

void loop() {
    //debounce time
    winCon.setInterrupTime(millis());

    /**********************************************************************************************
     * */


    if (winCon.getWindowContactState()) {
        printWindowContact(winCon.getWindowContactState());
        digitalWrite(ledPin, LOW);
        startLoop();
        setupDisplay();
        sendMQTTMessage("DHHZ/229/window1/M5stick/contact",createJsonString("M5stick-14",getTimeStamp().c_str(),"bool", winCon.getWindowContactState()));
        printString("Open for fresh air!");
        delay(1000);

    } else {
        digitalWrite(ledPin, HIGH);  // turn on the LED
        delay(500); // wait for half a second or 500 milliseconds
        digitalWrite(ledPin, LOW); // turn off the LED
        delay(500); // wait for half a second or 500 milliseconds
        printWindowContact(winCon.getWindowContactState());
        startLoop();
        setupDisplay();
        sendMQTTMessage("DHHZ/229/window1/M5stick/contact",createJsonString("M5stick-14", getTimeStamp().c_str(),"bool", winCon.getWindowContactState()));
        printString("Closed!");
        delay(1000);

    }
}