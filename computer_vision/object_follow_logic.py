"""
Basic visual-following decision logic.

This file intentionally does NOT directly drive the motors. It converts
an object's bounding box position into a rover command.

Use it as the decision layer between YOLO/OpenCV and the ESP32 serial
motor-control layer.
"""

def follow_command(frame_width, box, target_distance=None):
    """
    box = (x1, y1, x2, y2)

    Returns one of:
        LEFT, RIGHT, FORWARD, BACKWARD, STOP
    """

    x1, y1, x2, y2 = box

    center_x = (x1 + x2) / 2
    box_width = x2 - x1

    center = frame_width / 2
    dead_zone = frame_width * 0.12

    # Optional distance-based stop/approach thresholds.
    if target_distance is not None:
        if target_distance < 50:
            return "STOP"
        if target_distance > 150:
            return "FORWARD"

    if center_x < center - dead_zone:
        return "LEFT"

    if center_x > center + dead_zone:
        return "RIGHT"

    return "FORWARD"
