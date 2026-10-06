# Embodied AI Rover 🤖🚗

A low-cost embodied-AI rover prototype built using a Raspberry Pi, ESP32, L298N motor driver, USB camera, and sensors.

## Current prototype

- Differential-drive rover movement
- Raspberry Pi ↔ ESP32 serial communication
- Forward / backward / left / right / stop commands
- HC-SR04 distance sensing
- Flask web dashboard
- USB webcam support through OpenCV
- YOLO object-detection test pipeline
- Foundation for object-following/autonomous behavior

## Architecture

```text
USB Camera
    ↓
OpenCV / YOLO
    ↓
Raspberry Pi
    ↓ USB Serial (115200)
ESP32
    ↓
L298N Motor Driver
    ↓
DC Motors
```

Sensor data flows in the opposite direction:

```text
HC-SR04 → ESP32 → Serial → Raspberry Pi
```

## Hardware

- Raspberry Pi 4 Model B
- ESP32 DevKit
- L298N motor driver
- 2-wheel rover chassis with DC motors
- HC-SR04 ultrasonic sensor
- USB webcam
- OLED/sensor hardware used during development

## Software

- Python 3
- Flask
- PySerial
- OpenCV
- Ultralytics YOLO (for the detection test)

## Important note

This repository represents the prototype stage of the project. The motor-control, serial communication, dashboard and sensor portions were developed for the physical rover. The YOLO/OpenCV files are organized as the computer-vision layer and can be extended into closed-loop object following.

No passwords, API keys, virtual environments, or machine-specific device paths should be committed.

## Project status

**Prototype / Active Development**

Future work:
- closed-loop person/object following
- obstacle avoidance
- voice commands
- autonomous navigation
- agentic task planning
