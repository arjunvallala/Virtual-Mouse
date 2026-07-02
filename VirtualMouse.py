import cv2
import mediapipe as mp
import time
import numpy as np
import HandTrackingModule as hmt
import autopy
import math

# Screen Size
w, h = autopy.screen.size()

# Constants
FRAME_REDUCTION = 100
CLICK_DISTANCE = 40
SMOOTHENING = 5

# Previous Cursor Position
plocX, plocY = 0, 0

# Webcam Setup
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Click and Drag Variables
clickTime = 0
dragging = False

# FPS and Hand Detector
ptime = 0
Detector = hmt.HandDetector()

while True:

    # Read Frame
    success, img = cap.read()
    if not success:
        break

    # Mirror Webcam
    img = cv2.flip(img, 1)

    # Detect Hand
    img = Detector.findHands(img, draw=False)
    lmList = Detector.findPosition(img, draw=False)

    # Draw Active Region
    cv2.rectangle(
        img,
        (FRAME_REDUCTION, FRAME_REDUCTION),
        (640 - FRAME_REDUCTION, 480 - FRAME_REDUCTION),
        (0, 0, 255),
        3,
    )

    if len(lmList) != 0:

        # Get Finger States
        fingers = Detector.fingersUp()

        # Index and Middle Finger Coordinates
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # Drag Mode
        distance, img, _ = Detector.findDistance(img, p1=4, p2=8)
        if distance < 50:
            if not dragging:
                autopy.mouse.toggle(autopy.mouse.Button.LEFT, True)
                dragging = True
        else:
            if dragging:
                autopy.mouse.toggle(autopy.mouse.Button.LEFT, False)
                dragging = False

        # Move Mode
        if fingers[1] and not fingers[2]:

            cv2.circle(img, (x1, y1), 8, (0, 255, 0), cv2.FILLED)

            # Convert Camera Coordinates to Screen Coordinates
            mouseX = np.interp(
                x1,
                (FRAME_REDUCTION, 640 - FRAME_REDUCTION),
                (0, w),
            )

            mouseY = np.interp(
                y1,
                (FRAME_REDUCTION, 480 - FRAME_REDUCTION),
                (0, h),
            )

            # Smooth Cursor Movement
            clocX = plocX + (mouseX - plocX) / SMOOTHENING
            clocY = plocY + (mouseY - plocY) / SMOOTHENING

            # Move Cursor
            autopy.mouse.move(clocX, clocY)
            # Use the line below instead if cursor feels reversed.
            # autopy.mouse.move(w - clocX, clocY)

            # Update Previous Position
            plocX, plocY = clocX, clocY

        # Click Mode
        elif fingers[1] and fingers[2]:

            distance, img, _ = Detector.findDistance(img, p1=8, p2=12)

            if distance < CLICK_DISTANCE:
                if time.time() - clickTime > 1.0:
                    autopy.mouse.click()
                    clickTime = time.time()

    # Calculate FPS
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    # Display FPS
    cv2.putText(
        img,
        str(int(fps)),
        (30, 50),
        cv2.FONT_HERSHEY_COMPLEX,
        2,
        (0, 100, 240),
        2,
    )

    # Show Output
    cv2.imshow("Virtual Mouse", img)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release Resources
cap.release()
cv2.destroyAllWindows()