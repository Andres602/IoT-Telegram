/*
 *  This sketch demonstrates how to set up a simple HTTP-like server.
 *  The server will set a GPIO pin depending on the request
 *    http://server_ip/gpio/0 will set the GPIO2 low,
 *    http://server_ip/gpio/1 will set the GPIO2 high
 *  server_ip is the IP address of the ESP8266 module, will be
 *  printed to Serial when the module is connected.
 */

/*This cod came with the esp8266 arduino examples We just modify some parameters
an add
little specif changes*/

#include <ESP8266WiFi.h>
#include <string.h>

// D0 = 16;
// D1 = 5;
// D2 = 4;
// D3 = 0;
// D4 = 2;
// D5 = 14;
// D6 = 12;
// D7 = 13;
// D8 = 15;
// D9 = 3;
// D10 = 1;

const char *ssid = "ssid_name";
const char *password = "ssid_password";
const int pin = 2;

// Create an instance of the server
// specify the port to listen on as an argument
WiFiServer server(80);

void setup() {

  pinMode(pin, OUTPUT);
  Serial.begin(115200);
  delay(10);

  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  // setting Ip of device

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");

  // Start the server
  server.begin();
  Serial.println("Server started");

  // Print the IP address
  Serial.println(WiFi.localIP());
}

void loop() {
  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client) {
    // Serial.println("Client not founded");
    return;
  }

  // Wait until the client sends some data
  Serial.println("new client");
  while (!client.available()) {
    delay(1);
  }

  // Read the first line of the request
  String req = client.readStringUntil('/n');
  Serial.println(req);
  client.flush();

  // Match the request

  String pwmVal = "";
  if (req.indexOf("/gpio/0") != -1) {
    digitalWrite(pin, HIGH);
    pwmVal = "OFF";
  } else if (req.indexOf("/gpio/1") != -1) {
    digitalWrite(pin, LOW);
    pwmVal = "ON";
  } else {
    Serial.println("invalid request");
    client.stop();
    return;
  }

  client.flush();

  // Prepare the response
  String s = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<!DOCTYPE "
             "HTML>\r\n<html>\r\nLigth value is ";
  s += pwmVal;
  s += "</html>\n";

  // Send the response to the client
  client.println(s);
  delay(1);
  Serial.println("Client disonnected");

  // The client will actually be disconnected
  // when the function returns and 'client' object is detroyed
}
