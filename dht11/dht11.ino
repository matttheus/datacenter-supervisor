#include <dht.h>
#define    dht_pin    2

dht   my_dht;

int    temperatura = 0x00,
       umidade     = 0x00;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  my_dht.read11(dht_pin);

  temperatura = my_dht.temperature;
  umidade = my_dht.humidity;
  
  String data = "";
  data.concat(temperatura);
  data.concat("|");
  data.concat(umidade);
  

  Serial.println(data);
  delay(1000);
}
