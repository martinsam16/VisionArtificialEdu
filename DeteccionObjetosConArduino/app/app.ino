int led = 13;
int PIR = 2;
int movimiento = 0;
int leido = 0;

void setup() {
  pinMode(led, OUTPUT);
  pinMode(PIR, INPUT);
  Serial.begin(9600);
}

void loop() {
  movimiento = digitalRead(PIR);
  if(movimiento == HIGH){
    Serial.write("M");
    if(Serial.available() > 0){
         leido = Serial.read();
         
         if(leido != 0){
          digitalWrite(led, HIGH);
          delay(100);
          digitalWrite(led, LOW);
         }
    }
  }

}
