import cv2 as cv
import numpy as np
def nothing(x):
    pass
drawing = False
r, g, b, size = 0,0,0,0
def drawcircle(event, x, y, flag, param):
    global drawing
    if event == cv.EVENT_LBUTTONDOWN :
        drawing = True
        cv.circle(img, (x, y), size, (b, g, r), -1)
    elif event == cv.EVENT_MOUSEMOVE :
        if drawing :
            cv.circle(img, (x, y), size, (b, g, r), -1)
    elif event == cv.EVENT_LBUTTONUP :
        drawing = False

img = 255 * np.ones((512,512,3), np.uint8)
color = np.zeros((512,512,3), np.uint8)
barrier = 255 * np.ones((512,2,3), np.uint8)
cv.namedWindow("Paint")
cv.setMouseCallback("Paint", drawcircle)
cv.createTrackbar('R', "Paint", 0, 255, nothing)
cv.createTrackbar('G', "Paint", 0, 255, nothing)
cv.createTrackbar('B', "Paint", 0, 255, nothing)
cv.createTrackbar('Size', "Paint", 0, 50, nothing)
while True:
    r = cv.getTrackbarPos('R',"Paint")
    g = cv.getTrackbarPos('G',"Paint")
    b = cv.getTrackbarPos('B',"Paint")
    size = cv.getTrackbarPos('Size',"Paint")
    color[:] = [b,g,r]
    concat = np.hstack((img, barrier,color))
    cv.imshow("Paint", concat)
    if cv.waitKey(1) == ord('q') :
        break
cv.destroyAllWindows