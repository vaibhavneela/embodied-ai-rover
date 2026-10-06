import cv2

CAMERA_INDEX = 0

cap = cv2.VideoCapture(CAMERA_INDEX)

if not cap.isOpened():
    raise RuntimeError("Could not open camera")

print("Camera opened. Press Q to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to read frame")
        break

    cv2.imshow("Rover Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
