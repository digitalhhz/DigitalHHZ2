////
//// Created by gra001 on 12.05.2021.
////
//
#include "zx_gesture.h"

void initializeGesture() {
//    zx_sensor= new ZX_Sensor(ZX_ADDR);
    ZX_Sensor zx_sensor =ZX_Sensor(ZX_ADDR);
    Wire.begin(SDA,SCL);
    uint8_t ver;
    if ( zx_sensor.init() ) {
        printlnString("ZX Sensor initialization complete");
    } else {
        printlnString("Something went wrong during ZX Sensor init!");
    }

    // Read the model version number and ensure the library will work
    ver = zx_sensor.getModelVersion();
    if ( ver == ZX_ERROR ) {
        printlnString("Error reading model version number");
    } else {
        Serial.print("Model version: ");
        Serial.println(ver);
    }
    if ( ver != ZX_MODEL_VER ) {
        printlnString("Model version needs to be ");
        printlnString(String(ZX_MODEL_VER).c_str());
        printlnString(" to work with this library. Stopping.");
        while(1);
    }

    // Read the register map version and ensure the library will work
    ver = zx_sensor.getRegMapVersion();
    if ( ver == ZX_ERROR ) {
        printlnString("Error reading register map version number");
    } else {
        printlnString("Register Map Version: ");
        printUInt8(ver);
    }
    if ( ver != ZX_REG_MAP_VER ) {
        printlnString("Register map version needs to be ");
        printUInt8(ZX_REG_MAP_VER);
        printlnString(" to work with this library. Stopping.");
        while(1);
    }
}

const char * readGesture(){
    ZX_Sensor zx_sensor =ZX_Sensor(ZX_ADDR);
    uint8_t gesture;
    if (zx_sensor.gestureAvailable()) {
        setupDisplay();
        gesture=  zx_sensor.readGesture();
        switch ( gesture ) {
            case RIGHT_SWIPE:
                printString("RIGHT_SWIPE");
                return "RIGHT_SWIPE";
            case LEFT_SWIPE:
                printString("LEFT_SWIPE");
                return "LEFT_SWIPE";
            case UP_SWIPE:
                printString("UP_SWIPE");
                return "UP_SWIPE";
            default:
                printString("NO_GESTURE");
                return "NO_GESTURE";
        }
    }
    return "NO_GESTURE";
}