import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

while True :
    ret, frame = cam.read()
    frame = cv.flip(frame, 1)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # lower_white = np.array([100, 15, 200])
    # upper_white = np.array([150, 60, 255])
    lower_green = np.array([40, 100, 100])
    upper_green = np.array([110, 255, 255])
    lower_yellow = np.array([100, 100, 100])
    upper_yellow = np.array([150, 255, 255])
    mask = cv.inRange(hsv, lower_green, upper_green)
    mask2 = cv.inRange(hsv, lower_yellow, upper_yellow)
    mask3 = cv.bitwise_or(mask, mask2)
    res = cv.bitwise_or(frame, frame, mask=mask3)
    cv.imshow('frame', frame)
    cv.imshow('mask3', mask3)
    cv.imshow('res', res)
    if cv.waitKey(5) == ord('q'):
        break
cam.release
cv.destroyAllWindows