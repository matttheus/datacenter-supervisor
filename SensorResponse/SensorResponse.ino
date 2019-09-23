/*
  Sensor Response

  This is the code resonsible for send sensor data through
  the Serial communication.
  
*/

void setup() {
  // Serial Port Started
  Serial.begin(9600);
}

void loop() {
  Serial.print("Data from sensor");
  delay(1000);
}
