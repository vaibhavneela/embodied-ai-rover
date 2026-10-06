/*
  Embodied AI Rover - ESP32 controller

  Serial commands received from Raspberry Pi:
    FORWARD
    BACKWARD
    LEFT
    RIGHT
    STOP

  ESP32 sends:
    ROVER_READY
    DIST:<distance_cm>

  IMPORTANT:
  Motor pin assignments below are the reconstructed project interface.
  Verify the physical wiring before powering the motors.
*/

#define ENA 25
#define IN1 26
#define IN2 27

#define ENB 14
#define IN3 12
#define IN4 13

#define TRIG_PIN 5
#define ECHO_PIN 18

void stopMotors() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}

void forward() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void backward() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void leftTurn() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void rightTurn() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

float readDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH, 30000);

  if (duration == 0) {
    return -1;
  }

  return duration * 0.0343 / 2.0;
}

void handleCommand(String command) {
  command.trim();
  command.toUpperCase();

  if (command == "FORWARD") {
    forward();
  } else if (command == "BACKWARD") {
    backward();
  } else if (command == "LEFT") {
    leftTurn();
  } else if (command == "RIGHT") {
    rightTurn();
  } else if (command == "STOP") {
    stopMotors();
  }
}

void setup() {
  Serial.begin(115200);

  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  pinMode(ENB, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  digitalWrite(ENA, HIGH);
  digitalWrite(ENB, HIGH);

  stopMotors();

  Serial.println("ROVER_READY");
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    handleCommand(command);
  }

  static unsigned long lastSensorRead = 0;

  if (millis() - lastSensorRead >= 500) {
    lastSensorRead = millis();

    float distance = readDistance();

    if (distance >= 0) {
      Serial.print("DIST:");
      Serial.println(distance, 2);
    }
  }
}
