#define SOIL_SENSOR_PIN A0     
#define RELAY_PIN D1           

int moistureThreshold = 30;     

void setup() {
  Serial.begin(115200);

  pinMode(RELAY_PIN, INPUT);

  Serial.println("Auto Watering System Started...");
}

void loop() {
  int moistureRaw = analogRead(SOIL_SENSOR_PIN);

  int moisturePercent = map(moistureRaw, 1023, 0, 0, 100);

  Serial.print("Raw: ");
  Serial.print(moistureRaw);
  Serial.print(" | Moisture: ");
  Serial.print(moisturePercent);
  Serial.println(" %");

  if (moisturePercent < moistureThreshold) {
    pinMode(RELAY_PIN, OUTPUT);
    digitalWrite(RELAY_PIN, LOW);
    Serial.println("PUMP: ON");
  } else {
    pinMode(RELAY_PIN, INPUT);
    Serial.println("PUMP: OFF");
  }

  Serial.println("---------------------------");
  delay(5000);
}