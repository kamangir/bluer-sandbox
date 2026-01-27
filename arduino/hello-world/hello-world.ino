void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);  // LED on
  delay(50);                       // wait 50 ms
  digitalWrite(LED_BUILTIN, LOW);   // LED off
  delay(500);                       // wait 500 ms
}
