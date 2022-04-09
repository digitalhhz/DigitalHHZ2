//
// Created by gra001 on 17.05.2021.
//

#ifndef M5STICK_VIBRATIONSENSOR_H
#define M5STICK_VIBRATIONSENSOR_H
#include <Arduino.h>
void setupVibrationSensor(unsigned int vibPIN);
long unsigned int getVibration(unsigned int vibPIN);
#endif //M5STICK_VIBRATIONSENSOR_H
