// Versão Final:
//   * Retirado display LCD       Versão anterior: https://github.com/Roberto-Gomes/Projeto-01/blob/master/projeto_v_com_lcd.ino

#include <DHT.h> // https://github.com/adafruit/DHT-sensor-library      dependências: https://github.com/adafruit/Adafruit_Sensor

DHT sensor_dht(2, DHT11); //( Conectado no pino digital 2 do arduino ,tipo de sensor da familia DHT)
int mq2_pin = A0;
int tempo = 5000;
String dados;

void setup() {

  Serial.begin(9600);
  sensor_dht.begin();
  pinMode(3, OUTPUT); // led 1 (Verde) indicador visual de envio de informações.
  pinMode(5, OUTPUT); // led 2 (Vermelho) aceso estático indica presença de gás. Atenção! Se o led 2 estiver piscando indica perda da comunicação com o sensor DHT11(Verifique as conexões).
  delay(2000);
}
void loop() {

  int leitura_mq2 = analogRead(mq2_pin);
  float umidade = sensor_dht.readHumidity();
  int temperatura = sensor_dht.readTemperature();

  if (isnan(umidade) || isnan(temperatura)) { // Se as informações de umidade e temperatura não sejam valores númericos, o led 2 irá piscar e led 1 será desligado.
    digitalWrite(5, HIGH); delay(100);
    digitalWrite(5, LOW);  delay(300);
    digitalWrite(3, LOW);
  }
  else {

    // Informações enviadas pela porta serial
    dados = String(umidade) + "|" + String(temperatura) + "|" + String(leitura_mq2);
    Serial.println(dados);
    digitalWrite(3, LOW);
    delay(tempo);
    digitalWrite(3, HIGH);
  }

  if (leitura_mq2 >= 350) { // Leituras maiores ou igual a esse limiar acionará o Buzzer e led 2 ficará aceso de forma estática
    digitalWrite(5 , HIGH);
    for (int freq = 40; freq <= 440; freq++) { // frequência de 40hz-440hz
      tone(4, freq);
      delay(1);
    }
  }
  else {
    digitalWrite(5, LOW);
    noTone(4);
  }
}
