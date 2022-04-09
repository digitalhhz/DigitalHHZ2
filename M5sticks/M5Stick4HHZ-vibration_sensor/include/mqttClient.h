//
// Created by gra001 on 20.05.2021.
//

#ifndef M5STICK_MQTTCLIENT_H
#define M5STICK_MQTTCLIENT_H
#include <PubSubClient.h>
#include <WiFi.h>
#include <Esp.h>
#include "dislpay.h"
#include <NTPClient.h>
#include <ezTime.h>
#include <WiFiUdp.h>


/**************** wifi ****************************************/


void setupWifi(const char * SSID, const char * PSK);


/**************** mqtt ****************************************/

void setupMQTTClient(const char * BROKER, unsigned int Port, const char * USER, const char * PASSWORD);

bool startLoop();

void sendMQTTMessage(char * topic ,char * payload);

/**************** ntp ****************************************/
void setupNTP();
String getTime();
String getTimeStamp();

#endif //M5STICK_MQTTCLIENT_H
