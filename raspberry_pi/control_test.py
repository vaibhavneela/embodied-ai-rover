import serial
import time

PORT = "/dev/ttyUSB0"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)

commands = {
    "w": "FORWARD",
    "s": "BACKWARD",
    "a": "LEFT",
    "d": "RIGHT",
    "x": "STOP",
}

print("W=forward S=backward A=left D=right X=stop")
print("Press Ctrl+C to exit.")

try:
    while True:
        key = input("Command: ").strip().lower()
        if key in commands:
            command = commands[key]
            ser.write((command + "\n").encode())
            print("Sent:", command)
        else:
            print("Unknown command")
except KeyboardInterrupt:
    pass
finally:
    ser.write(b"STOP\n")
    ser.close()
