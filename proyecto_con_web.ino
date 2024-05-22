#include <WiFi.h>
#include <HTTPClient.h>
#include <Stepper.h>
#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN 13 // Configurable, see typical pin layout above
#define SS_PIN 15 // Configurable, see typical pin layout above

Stepper motor1(2048, 2, 14, 4, 17);
int TRIG = 5;
int ECO = 21;
int LED = 12;

int DISTANCIA;
int DURACION;

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance

const char* ssid = "Monitor Sanitario"; // Replace with your WiFi SSID
const char* password = "monitor12345"; // Replace with your WiFi password
const char* serverName = "http://192.168.105.71/save_data.php"; // Replace with your server IP or domain

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");

  SPI.begin();
  mfrc522.PCD_Init();

  motor1.setSpeed(15);
  pinMode(TRIG, OUTPUT);
  pinMode(ECO, INPUT);
  pinMode(LED, OUTPUT);
}

void loop() {
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  DURACION = pulseIn(ECO, HIGH);
  DISTANCIA = DURACION / 58.2;
  Serial.println(DISTANCIA);
  delay(200);

  if (DISTANCIA < 15) {
    if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
      digitalWrite(LED, HIGH);
      Serial.print("Card UID:");
      String cardID = "";
      for (byte i = 0; i < mfrc522.uid.size; i++) {
        cardID += String(mfrc522.uid.uidByte[i] < 0x10 ? "0" : "");
        cardID += String(mfrc522.uid.uidByte[i], HEX);
      }
      cardID.toUpperCase();
      Serial.println(cardID);
      
      // Enviar datos al servidor
      if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;
        http.begin(serverName);
        http.addHeader("Content-Type", "application/x-www-form-urlencoded");

        String httpRequestData = "cardID=" + cardID;
        int httpResponseCode = http.POST(httpRequestData);

        if (httpResponseCode > 0) {
          String response = http.getString();
          Serial.println(httpResponseCode);
          Serial.println(response);
        } else {
          Serial.print("Error on sending POST: ");
          Serial.println(httpResponseCode);
        }
        http.end();
      }

      mfrc522.PICC_HaltA();
      motor1.step(2048);
      delay(20);
      motor1.step(2048);
      digitalWrite(LED, LOW);
    }
  }
}
