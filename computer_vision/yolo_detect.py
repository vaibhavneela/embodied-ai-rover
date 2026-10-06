import cv2
from ultralytics import YOLO

CAMERA_INDEX = 0
MODEL = "yolo11n.pt"  # Ultralytics will download it on first use.

model = YOLO(MODEL)
cap = cv2.VideoCapture(CAMERA_INDEX)

if not cap.isOpened():
    raise RuntimeError("Could not open camera")

print("YOLO detection started. Press Q to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to read frame")
        break

    results = model(frame, verbose=False)
    annotated = results[0].plot()

    cv2.imshow("Rover YOLO Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
