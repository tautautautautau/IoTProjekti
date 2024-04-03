int buttonPin = 12;

int score = 0;

void setup() {
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String new_score_string = Serial.readString();
    int new_score = new_score_string.toInt();
    score = new_score;
  }
  if (digitalRead(buttonPin) == LOW) {
    score = score + 1;
    Serial.println(score);
    delay(500);
  }
  delay(100);
}