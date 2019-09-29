#include <Arduino.h>
#include <ESPAsyncWebServer.h>
#include <ESPAsyncWiFiManager.h>
#include <WebSocketsClient.h>
#include <Hash.h>

#define   PORT            80
#define   RED             2
#define   PINOUT          5
#define   ON              0
#define   OFF             1
#define   PORTSOCKET      8080

AsyncWebServer server(PORT);
DNSServer dns;

WebSocketsClient webSocket;
const char *onT="on";
const char *offT="off";
const char *ipSocket="74.208.88.185";

void webSocketEvent(WStype_t type, uint8_t * payload, size_t length) {

	switch(type) {
		case WStype_DISCONNECTED:
			Serial.printf("[WSc] Disconnected!\n");
			break;
		case WStype_CONNECTED: {
			Serial.printf("[WSc] Connected to url: %s\n", payload);

			// send message to server when Connected
			webSocket.sendTXT("Connected");
		}
			break;
		case WStype_TEXT:
			Serial.printf("[WSc] get text: %s\n", payload);
      if(strcmp((char*)payload,onT)==0)  digitalWrite(PINOUT,ON);
      if(strcmp((char*)payload,offT)==0) digitalWrite(PINOUT,OFF);

			// send message to server
			//webSocket.sendTXT("message here");
			break;
		case WStype_BIN:
			Serial.printf("[WSc] get binary length: %u\n", length);
			hexdump(payload, length);

			// send data to server
			// webSocket.sendBIN(payload, length);
			break;
        case WStype_PING:
            // pong will be send automatically
            Serial.printf("[WSc] get ping\n");
            break;
        case WStype_PONG:
            // answer to a ping we send
            Serial.printf("[WSc] get pong\n");
            break;
    }

}

void setup() {
  pinMode(PINOUT, OUTPUT);
  pinMode(RED, OUTPUT);
  digitalWrite(PINOUT,ON);
  digitalWrite(RED,ON);
  Serial.begin(115200);
  // put your setup code here, to run once:
  AsyncWiFiManager wifiManager(&server,&dns);
  wifiManager.autoConnect();
  //wifiManager.resetSettings();
  Serial.println(WiFi.localIP());
  digitalWrite(RED,OFF);

  //webSocket
  // server address, port and URL
	webSocket.begin(ipSocket, PORTSOCKET, "/","echo-protocol");

	// event handler
	webSocket.onEvent(webSocketEvent);

	// use HTTP Basic Authorization this is optional remove if not needed
	//webSocket.setAuthorization("user", "Password");

	// try ever 5000 again if connection has failed
	webSocket.setReconnectInterval(5000);
  
  // start heartbeat (optional)
  // ping server every 15000 ms
  // expect pong from server within 3000 ms
  // consider connection disconnected if pong is not received 2 times
  webSocket.enableHeartbeat(15000, 3000, 2);

}

void loop() {
  // put your main code here, to run repeatedly:
  webSocket.loop();
}