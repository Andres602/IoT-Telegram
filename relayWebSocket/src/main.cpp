#include <Arduino.h>
#include <ESPAsyncWebServer.h>
#include <ESPAsyncWiFiManager.h>

#define   PORT            80

AsyncWebServer server(PORT);
DNSServer dns;

void setup() {
  Serial.begin(115200);
  // put your setup code here, to run once:
  AsyncWiFiManager wifiManager(&server,&dns);
  wifiManager.autoConnect();
  //wifiManager.resetSettings();
  Serial.println(WiFi.localIP());
}

void loop() {
  // put your main code here, to run repeatedly:
}