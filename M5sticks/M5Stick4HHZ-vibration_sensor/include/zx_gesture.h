////
//// Created by gra001 on 12.05.2021.
// gesture sensore
//Hardware Connections:
//
//M5stickC Pin  ZX Sensor Board  Function
//---------------------------------------
//5V           VCC              Power
//GND          GND              Ground
//G26          DA               I2C Data
//G0           CL               I2C Clock
//G36          DR               Data Ready



#ifndef M5STICK_ZX_GESTURE_H
#define M5STICK_ZX_GESTURE_H
#include <ZX_Sensor.h>
#include <Wire.h>
#include "dislpay.h"

#define SDA 26
#define SCL 0
// Global Variables
const int ZX_ADDR = 0x10;  // ZX Sensor I2C address
//ZX_Sensor * zx_sensor;  //= ZX_Sensor(ZX_ADDR);
void initializeGesture();
String readGesture();
#endif //M5STICK_ZX_GESTURE_H
