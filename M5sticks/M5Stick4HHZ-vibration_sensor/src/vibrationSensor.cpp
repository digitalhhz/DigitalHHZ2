//
// Created by gra001 on 17.05.2021.
//
#include "vibrationSensor.h"

void setupVibrationSensor(unsigned int vibPIN){
    pinMode(vibPIN,INPUT);
}

long unsigned int getVibration(unsigned int vibPIN) {
    long unsigned int vibration = pulseIn(vibPIN,HIGH);
    return vibration;
}