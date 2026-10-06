from flask import Flask, render_template, jsonify
import serial
import threading
import time

app = Flask(__name__)

PORT = "/dev/ttyUSB0"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=0.2)
time.sleep(2)

latest_distance = None
lock = threading.Lock()


def serial_reader():
    global latest_distance

    while True:
        try:
            line = ser.readline().decode(errors="ignore").strip()
            if not line:
                continue

            print("ESP32:", line)

            if line.startswith("DIST:"):
                try:
                    distance = float(line.split(":", 1)[1])
                    with lock:
                        latest_distance = distance
                except ValueError:
                    pass
        except Exception as exc:
            print("Serial read error:", exc)
            time.sleep(1)


threading.Thread(target=serial_reader, daemon=True).start()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/move/<command>")
def move(command):
    allowed = {"FORWARD", "BACKWARD", "LEFT", "RIGHT", "STOP"}
    command = command.upper()

    if command not in allowed:
        return jsonify({"ok": False, "error": "Invalid command"}), 400

    ser.write((command + "\n").encode())
    return jsonify({"ok": True, "command": command})


@app.route("/distance")
def distance():
    with lock:
        value = latest_distance

    return jsonify({"distance": value})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
