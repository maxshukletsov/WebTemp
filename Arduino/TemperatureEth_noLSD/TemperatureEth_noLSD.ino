//for ds18b20
#include <OneWire.h> 
//for OLED 
#include <SPI.h>
#include <Wire.h>
#include <EtherEncLib.h>
#include <avr/pgmspace.h>

static unsigned char ipaddr[] = { 192, 168, 0, 126 };
static unsigned char macaddr[] = { 0x00, 0x11, 0x22, 0x44, 0x00, 0x26 };
const PROGMEM char resp200Txt[] = {"HTTP/1.0 200 OK\n\rContent-Type: text/html\n\rPragma: no-cache\n\r\n\r"};
OneWire ds(2);
float temperature = -56;
long lastUpdateTime = 0;
const int TEMP_UPDATE_TIME = 10000;
EtherEncLib lib(80);
char msgBuffer[20];

void setup() {
  pinMode(10,OUTPUT);  //--- ? -- SS pin must be output
  lib.begin(ipaddr, macaddr);
  Serial.begin(9600);
}

void loop() {
  detectTemperature();
  Serial.print("Temp: ");
  Serial.print(temperature);
  Serial.print(" C");
  
  if ( lib.available() )
  {
    
    lib.print((char *)&resp200Txt[0],strlen_P(&resp200Txt[0]));
    lib.print(dtostrf(temperature, 6, 2, msgBuffer));
    
    lib.close();
  }
 }
float detectTemperature(){
  byte data[2];
  ds.reset();
  ds.write(0xCC);
  ds.write(0x44);
  if (millis() - lastUpdateTime > TEMP_UPDATE_TIME)
  {
    lastUpdateTime = millis();
    ds.reset();
    ds.write(0xCC);
    ds.write(0xBE);
    data[0] = ds.read();
    data[1] = ds.read();

    temperature = ((data[1] << 8) | data[0]) * 0.0625; 
  }
}
