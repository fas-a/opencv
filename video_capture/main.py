import cv2 as cv
import numpy

cam = cv.VideoCapture(0)
if not cam.isOpened :
    print("failed open camera")
    exit()
while True :
    ret, frame = cam.read()
    if not ret :
        print("frame not take")
        exit()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("cam", gray)
    if cv.waitKey(1) == ord('q'):
        break
cam.release
cv.destroyAllWindows