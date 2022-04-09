//
// Created by gra001 on 20.05.2021.
//

#include "MQTTClient.h"

WiFiClient espClient;
PubSubClient client(espClient);   // mqtt client for the message service
/**************** wifi ****************************************/
void setupWifi(const char *SSID, const char *PSK) {
    printlnString("start connecting to WiFi ... ");
    printlnString(SSID);
    delay(10);
    WiFi.mode(WIFI_STA);
    WiFi.begin(SSID, PSK);
    while (WiFi.status() != WL_CONNECTED) {
        printString(".");
        delay(500);
    }
    setupDisplay();
    printlnString("WiFi connected");
    printlnString("IP address: ");
    printlnString(WiFi.localIP().toString());
    delay(2000);
}

/**************** NTP ****************************************/
void setupNTP(){
    setInterval(60);
    waitForSync();
}

String getTimeStamp(){
    char time[26];
//    time = UTC.dateTime("Y-m-d\\TH:i:s.v").c_str();
    strcpy(time,UTC.dateTime("Y-m-d\\TH:i:s.v").c_str());
    strcat(time,"z");
    return time;
}

String getTime(){
    WiFiUDP ntpUDP;
    NTPClient ntpClient(ntpUDP); //NTP client to get current date
    String formattedTime;
    while(!ntpClient.update()) {
        ntpClient.forceUpdate();
    }
    formattedTime = ntpClient.getFormattedTime();
    return formattedTime;
}

/**************** mqtt ****************************************/


void setupMQTTClient(const char *BROKER, unsigned int Port, const char * USER, const char * PASSWORD) {
    Serial.println("Setup MQTT client");
    client.setServer(BROKER, Port);
    String clientId = "M5client-";
    clientId += String(random(0xffff), HEX);
    const char *clientID = clientId.c_str();
    delay(2000);
    client.connect(clientID,USER,PASSWORD);
    delay(1000);
    if (client.connected()) {
        printlnString("MQTT client connected!");
        delay(1000);
    } else if (client.connected()) {
        delay(1000);
        printlnString("Reconnecting...");
        while (!client.connected()) {
            String clientId = "M5client-";
            clientId += String(random(0xffff), HEX);
            if (!client.connect(clientId.c_str())) {
                setupDisplay();
                printlnString(String(client.state()));
                printlnString(" retrying in 5 seconds");
                delay(5000);
            }
        }
    }
}

bool startLoop(){
    printString("start loop");
//    while(!client.loop()){
    for (int i = 0; i < 20; i++) {
        if (WiFi.status() != WL_CONNECTED) {
            printString("reboot system for Wifi connection!");
            delay(1000);
            ESP.restart();
        }
        if (client.loop()) {
            return true;
        } else if (i == 18) {
            printString("reboot system");
            delay(1000);
            ESP.restart();
        }
        delay(500);
        printString(".");
    }
    return false;
}


void sendMQTTMessage(char *topic, char *payload) {
    setupDisplay();
    bool messagePublished = client.publish(topic, payload);
    while (!messagePublished) {
        messagePublished = client.publish(topic, payload);
        delay(500);
    }
    printString("message published: ");
    printString(String(messagePublished));
    printString("\n");
}
