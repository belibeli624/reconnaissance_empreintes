
#include <Adafruit_Fingerprint.h>
#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3); // RX, TX
Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);

void setup() {
  Serial.begin(9600);
  while (!Serial);  // For Leonardo/Micro/Zero
  delay(100);
  finger.begin(57600);
  if (finger.verifyPassword()) {
    Serial.println("Capteur d'empreinte détecté avec succès.");
  } else {
    Serial.println("Échec de détection du capteur d'empreinte.");
    while (1) { delay(1); }
  }
}

void loop() {
  Serial.println("Place ton doigt sur le capteur...");
  int id = getFingerprintID();
  if (id != -1) {
    Serial.print("Empreinte reconnue, ID: ");
    Serial.println(id);
  }
  delay(2000);
}

int getFingerprintID() {
  uint8_t p = finger.getImage();
  if (p != FINGERPRINT_OK) return -1;

  p = finger.image2Tz();
  if (p != FINGERPRINT_OK) return -1;

  p = finger.fingerFastSearch();
  if (p != FINGERPRINT_OK) return -1;

  return finger.fingerID;
}
