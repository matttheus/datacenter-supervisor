#include <MQ2.h>

int pin = A0;

MQ2 mq2(pin);

void setup(){
  Serial.begin(9600);
  mq2.begin();
}
void loop() {
  // put your main code here, to run repeatedly:
  float* values = mq2.read(false);
  // float lpg = mq2.readLPG();
  // float smoke = mq2.readSmoke();
  float co = mq2.readCO();
  
  Serial.print(co);

  delay(1000);
}
