#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>

// Replace with your network credentials
const char* ssid = "MiA3";
const char* password = "123456789";

ESP8266WebServer server(80);   //instantiate server at port 80 (http port)

String page = ""; //For the Web Server
String page2 = ""; //For updating Status of motor 1
String page3 = ""; //For updating status of motor 2
void setup(void)
{ 
  //the HTML of the web page
  page = "<center><h1>Motor Control Web Server</h1><body><p><a href=\"Forward\"><button>Forward</button></a><p><a href=\"Backward\"><button>Backward</button></a></p><p><a href =\"Left\"><button>Left</button></a>&nbsp;<a href=\"Stop\"><button>Stop</button></a><a href=\"Right\"><button>Right</button></a></p></body></center>";
  pinMode(14, OUTPUT);   // inputs for motor 1
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);   // inputs for motor 2
  pinMode(15, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT); // For status of WiFi connection
  delay(1000);
  Serial.begin(115200);
  WiFi.begin(ssid, password); //begin WiFi connection
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  digitalWrite(LED_BUILTIN, HIGH);    // when connected turns high
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());   //provides IP address
  server.on("/", []() {
    server.send(200, "text/html", page + page2);
  });
  server.on("/Forward", Forward);
  server.on("/Backward", Backward);
  server.on("/Left", Left);
  server.on("/Right", Right);

  server.on("/Stop", []() {                            // turns all the motor input pins low
    page2 = "<center><p> motor 1 Status : Off</p></center>";
    page3 = "<center><p> motor 2 Status : off</p></center>";
    server.send(200, "text/html", page + page2 + page3);
    digitalWrite(14, LOW);
    digitalWrite(12, LOW);
    digitalWrite(13, LOW);
    digitalWrite(15, LOW);
    delay(200);
  });
  server.begin();
  Serial.println("Web server started!");
}
void loop(void)
{
  server.handleClient();
}

void Forward()
{
  digitalWrite(14, HIGH);
  digitalWrite(13, HIGH);
  digitalWrite(12, LOW);
  digitalWrite(15, LOW);
  Serial.println("Forward");
  page2 = "<center><p> motors Status : On</p></center>";
  server.send(200, "text/html", page + page2 + page3);
  delay(200);
}
void Left()
{
  page3 = "<center><p> motor 2 Status : On</p></center>";
  server.send(200, "text/html", page + page2 + page3);
  digitalWrite(12, LOW);
  digitalWrite(14, HIGH);
  digitalWrite(13, LOW);
  digitalWrite(15, LOW);
  Serial.println("Left");
  delay(200);
}
void Right()
{
  page3 = "<center><p> motor 1 Status : On</p></center>";
  server.send(200, "text/html", page + page2 + page3);
  digitalWrite(12, LOW);
  digitalWrite(14, LOW);
  digitalWrite(13, HIGH);
  digitalWrite(15, LOW);
  Serial.println("Right");
  delay(200);
}
void Backward()
{
  page2 = "<center><p> motors Status : Backward On</p></center>";
  server.send(200, "text/html", page + page2 + page3);
  digitalWrite(14, LOW);
  digitalWrite(13, LOW);
  digitalWrite(12, HIGH);
  digitalWrite(15, HIGH);
  Serial.println("Back");
  delay(200);
}
