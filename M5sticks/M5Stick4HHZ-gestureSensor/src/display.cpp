//
// Created by gra001 on 03.05.2021.
//

#include "dislpay.h"

void setupDisplay() {
    M5.Lcd.fillScreen(BLACK);
    M5.Lcd.setCursor(0, 10);
    M5.Lcd.setTextColor(WHITE);
    M5.Lcd.setTextSize(1);
}

void printWindowContact(bool closed) {
    M5.Lcd.fillScreen(BLACK);
    M5.Lcd.setCursor(0, 10);
    M5.Lcd.setTextColor(WHITE);
    M5.Lcd.setTextSize(1);
    if (closed){
        M5.Lcd.printf("window closed: true");
    }
    else {
        M5.Lcd.printf("window closed: false");
    }
}

void printlnString(String text){
    M5.Lcd.println(text.c_str());
}
void printString(String text){
    M5.Lcd.print(text.c_str());
}

void printUInt8(uint8_t num) {
    M5.Lcd.println(num);
}