#include <PubSubClient.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include "Internet.h"

#include "DHTesp.h"  //DHT11 Library for ESP
  
#define LED 2        //On board LED
#define DHTpin 14    //D5 of NodeMCU is GPIO14

DHTesp dht;

float humidity, temperature;

const char* ssid = "CASA MARTINEZ BEDOYA";
const char* password = "SEGURIDAD1";
const char* host = "34.226.49.60";

Internet internet(ssid, password);

WiFiClient espClient;
PubSubClient client(espClient);

void handleADC() {
  humidity = dht.getHumidity();
  temperature = dht.getTemperature();

  Serial.print("H:");
  Serial.println(humidity);
  Serial.print("T:");
  Serial.println(temperature); //dht.toFahrenheit(temperature));
}

void setup()
{
  Serial.begin(9600);
  Serial.println();
  dht.setup(DHTpin, DHTesp::DHT11); //for DHT11 Connect DHT sensor to GPIO 17

  internet.conectar();
  client.setServer(host, 44332);
}

void loop()
{
  char msg[16];
  char msg1[16];
  handleADC();
  sprintf(msg,"Temperatura: %.2f",dht.getHumidity());
  client.publish("cola1", msg);
  sprintf(msg1,"Humedad %.2f",dht.getTemperature());
  client.publish("cola1", msg1);

  delay(5000);
}
