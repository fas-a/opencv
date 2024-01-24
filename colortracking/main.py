import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

while True :
    ret, frame = cam.read()
    frame = cv.flip(frame, 1)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # lower_white = np.array([100, 15, 200])
    # upper_white = np.array([150, 60, 255])
    lower_white = np.array([40, 100, 100])
    upper_white = np.array([100, 255, 255])
    mask = cv.inRange(hsv, lower_white, upper_white)
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    if cv.waitKey(5) == ord('q'):
        break
cam.release
cv.destroyAllWindows