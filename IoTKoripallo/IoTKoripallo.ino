#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Initialize LCD at I2C address 0x27 with size 16x2
LiquidCrystal_I2C lcd(0x27, 16, 2);

/*
  HC-SR04 Ping distance sensor:
  VCC to Arduino 5v
  GND to Arduino GND
  Echo to Arduino pin 10
  Trig to Arduino pin 9

  RGB LED:
  Red to Arduino pin 6
  Green to Arduino pin 5
  Blue to Arduino pin 3

  Button:
  VCC to Arduino 5v
  GND to Arduino GND
  Signal to Arduino pin 2

  Piezo:
  VCC to Arduino 5v
  GND to Arduino GND
  Signal to Arduino pin 8

  LCD:
  SDA to Arduino pin A4
  SCL to Arduino pin A5
  VCC to Arduino 5v
  GND to Arduino GND
*/

const int PIN_TRIG = 9;
const int PIN_ECHO = 10;

const int PIN_RED = 6;
const int PIN_GREEN = 5;
const int PIN_BLUE = 3;

const int PIN_BUTTON = 2;

const int PIN_BUZZER = 8;

float duration, distance;
int score, buttonState;
bool scored;

void setup() {
  // Set pin modes for all the components
  pinMode(PIN_TRIG, OUTPUT);
  pinMode(PIN_ECHO, INPUT);

  pinMode(PIN_RED, OUTPUT);
  pinMode(PIN_GREEN, OUTPUT);
  pinMode(PIN_BLUE, OUTPUT);

  pinMode(PIN_BUTTON, INPUT);

  pinMode(PIN_BUZZER, OUTPUT);

  // Initialize LCD
  lcd.begin();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Score:");

  // Initialize serial communication
  Serial.begin(9600);

  // Set initial values
  buttonState = 0;
  score = 0;
  scored = false;
}

void loop() {
  // Read button state and reset score if button is pressed
  buttonState = digitalRead(PIN_BUTTON);
  if (buttonState == HIGH) {
    score = 0;
  }

  // Send a pulse to the sensor
  digitalWrite(PIN_TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(PIN_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIG, LOW);

  // Calculate distance from duration
  duration = pulseIn(PIN_ECHO, HIGH);
  distance = (duration * .0343) / 2;

  // Check if the ball is in the basket
  if (distance < 6 && distance > 0) {
    Serial.println("scored");
    if (!scored) {
      score = score + 1;
      updateLCDScore(score);
      tone(PIN_BUZZER, 1000);
      delay(500);
      noTone(PIN_BUZZER);
    }
    scored = true;
    setColor(0, 200, 0);
  } else {
    setColor(200, 20, 0);
    scored = false;
  }

  // Print score and distance to serial
  Serial.println("Score: " + score + " | Distance: " + distance);
  delay(100);
}

// Function to update score to LCD
void updateLCDScore(int score) {
  lcd.setCursor(0, 1);
  lcd.print("                ");
  lcd.setCursor(0, 1);
  lcd.print(score);
}

// Function to set the color of the RGB LED
void setColor(int R, int G, int B) {
  analogWrite(PIN_RED, R);
  analogWrite(PIN_GREEN, G);
  analogWrite(PIN_BLUE, B);
}
