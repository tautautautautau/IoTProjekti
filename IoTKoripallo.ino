const int trigPin = 9;
const int echoPin = 10;

float duration, distance;
int score;
bool korissa;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);

  score = 0;
  korissa = false;
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = (duration*.0343)/2;

  if (distance < 6 && distance > 0) {
    Serial.println("KORISSA");
    if (!korissa) {
      score = score + 1;
    }
    korissa = true;
    delay(1000);
  } else {
    korissa = false;
  }
  
  Serial.print("Score: ");
  Serial.print(score);
  Serial.print(" | Distance: ");
  Serial.println(distance);
  delay(100);
}
