import serial
import time

PORT = "/dev/ttyUSB0"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)

print("Listening to ESP32...")

try:
    while True:
        line = ser.readline().decode(errors="ignore").strip()
        if line:
            print(line)
except KeyboardInterrupt:
    pass
finally:
    ser.close()
