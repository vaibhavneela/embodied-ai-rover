# Prototype status

## Confirmed during development

- ESP32 motor control
- Forward/backward/left/right/stop commands
- Raspberry Pi to ESP32 serial communication
- ESP32 sensor data returned to Raspberry Pi
- HC-SR04 distance readings
- Flask rover dashboard
- USB webcam recognized and used with OpenCV
- YOLO object-detection pipeline tested

## Important distinction

The project is at the prototype/integration stage. Detection and movement are working components, but a polished autonomous closed-loop agent still needs integration and tuning.

## Hardware note

The ESP32 pin assignments in `esp32/esp32_rover.ino` are reconstructed for this repository and should be checked against the actual wiring before use.
