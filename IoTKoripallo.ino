#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,16,2);

const int trigPin = 9;
const int echoPin = 10;

const int PIN_RED   = 6;
const int PIN_GREEN = 5;
const int PIN_BLUE  = 3;

const int buttonPin = 2;

const int piezoPin = 8;

float duration, distance;
int score, buttonState;
bool korissa;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  pinMode(PIN_RED,   OUTPUT);
  pinMode(PIN_GREEN, OUTPUT);
  pinMode(PIN_BLUE,  OUTPUT);

  pinMode(buttonPin, INPUT);
  buttonState = 0;

  pinMode(piezoPin, OUTPUT);

  lcd.begin();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Score:");
  //Serial.begin(9600);

  score = 0;
  korissa = false;
}

void loop() {
  buttonState = digitalRead(buttonPin);

  if (buttonState == HIGH) {
    score = 0;
  }

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
      tone(piezoPin, 1000);
      delay(500);
      noTone(piezoPin);
    }
    korissa = true;
    setColor(0,127,0);
    delay(1000);
  } else {
    setColor(200,20,0);
    korissa = false;
  }
  
  Serial.print("Score: ");
  Serial.print(score);
  Serial.print(" | Distance: ");
  Serial.println(distance);
  lcd.setCursor(0,1);
  lcd.print("                ");
  lcd.setCursor(0,1);
  lcd.print(score);
  delay(100);
}

void setColor(int R, int G, int B) {
  analogWrite(PIN_RED,   R);
  analogWrite(PIN_GREEN, G);
  analogWrite(PIN_BLUE,  B);
}
