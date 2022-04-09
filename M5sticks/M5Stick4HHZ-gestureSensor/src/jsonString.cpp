//
// Created by gra001 on 19.05.2021.
//
#include "jsonString.h"

char buffer[200];

char *createJsonString(const char *device, const char *timestamp, const char *SI, int value) {
    snprintf(buffer, sizeof(buffer), R"({"deviceid": "%s", "timestamp": "%s", "SI": "%s","value": %d})", device, timestamp,
             SI, value);
    return buffer;
}

char * createJsonString(const char *device, const char *timestamp, const char *SI, float value) {
    snprintf(buffer, sizeof(buffer), R"({"deviceid": "%s", "timestamp": "%s", "SI": "%s","value": %f})", device, timestamp,
             SI, value);
    return buffer;
}

char * createJsonString(const char *device, const char *timestamp, const char *SI, byte value) {
    snprintf(buffer, sizeof(buffer), R"({"deviceid": "%s", "timestamp": "%s", "SI": "%s","value": %d})", device, timestamp,
             SI, value);
    return buffer;
}

char *createJsonString(const char *device, const char *timestamp, const char *SI, const char *value) {
    snprintf(buffer, sizeof(buffer), R"({"deviceid": "%s", "timestamp": "%s", "SI": "%s","value": "%s"})", device, timestamp,
             SI, value);
    return buffer;
}