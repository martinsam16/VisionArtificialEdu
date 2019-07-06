const int pinLed = 13;
const int pinPir = 2;
int val = 0;

void setup() {
  pinMode(pinLed, OUTPUT);
  pinMode(pinPir, INPUT);
  Serial.begin(9600);
}

void loop() {

  if (digitalRead(pinPir) == HIGH) {
    Serial.println("M");

    if (Serial.available() > 0) {

      if (Serial.read() == '2') {
        digitalWrite(pinLed, HIGH);
      } else {
        digitalWrite(pinLed, LOW);
      }
    }
  } else {
    digitalWrite(pinLed, LOW);
  }
  delay(1000);

}
