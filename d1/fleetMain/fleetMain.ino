#include <ArduinoJson.h>

#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>

#define _SSID "MambaHome"
#define _PASSWORD ""

#define HOST "192.168.0.215"
#define PORT 8000
#define REPORT_ENDPOINT "/api/reading"

#define CONTENTTYPE "application/json"

#define HALF_HOUR 1800000

WiFiClient wifiClient;
int sensor_pin = A0;
int value ;
String MAC; 

void setup() {
  MAC = WiFi.macAddress();
  Serial.begin(115200);                 //Serial connection
  WiFi.begin(_SSID, _PASSWORD);   //WiFi connection
 
  while (WiFi.status() != WL_CONNECTED) {  //Wait for the WiFI connection completion
 
    delay(500);
    Serial.println("Waiting for connection");
 
  }


  Serial.println("connected");
 
}

void loop() {
  value= analogRead(sensor_pin);
  value = map(value,1024,392,0,100);
  Serial.print("Moisture : ");
  Serial.print(value);
  Serial.println("%");
  

  HTTPClient http;    //Declare object of class HTTPClient

  String url = "http://" + String(HOST) + ":" + String(PORT) + String(REPORT_ENDPOINT);
  http.begin(wifiClient, url);      //Specify request destination
  http.addHeader("Content-Type", CONTENTTYPE);  //Specify content-type header

  DynamicJsonDocument doc(1024);
  doc["macAddress"] = WiFi.macAddress();
  doc["reading"] = value;

  String BODY;
  serializeJson(doc, BODY);

  int httpCode = http.PUT(BODY);   //Send the request
  String payload = http.getString();                  //Get the response payload

  Serial.println(httpCode);   //Print HTTP return code
  Serial.println(payload);    //Print request response payload

  http.end();  //Close connection


  delay(HALF_HOUR);
}
