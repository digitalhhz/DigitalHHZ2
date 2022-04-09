//
// Created by gra001 on 19.05.2021.
//

#ifndef M5STICK_JSONSTRING_H
#define M5STICK_JSONSTRING_H

#include <Arduino.h>

char *createJsonString(const char *device, const char *timestamp, const char *SI, int value);

char *createJsonString(const char *device, const char *timestamp, const char *SI, float value);

char *createJsonString(const char *device, const char *timestamp, const char *SI, byte value);

char *createJsonString(const char *device, const char *timestamp, const char *SI, const char *value);

#endif //M5STICK_JSONSTRING_H
