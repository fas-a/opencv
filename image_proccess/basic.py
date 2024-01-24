import numpy as np
import cv2 as cv

def mouseposition(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN :
        print("mouse position : ", x, y)
        print("color : ", img[y,x])
img = cv.imread('.\image_proccess\photo.jpg')
cv.namedWindow("Display window")
cv.setMouseCallback("Display window", mouseposition)
doll = img[248:617, 302:516]
img[266:635, 920:1134] = doll
while True:
    cv.imshow("Display window", img)
    if cv.waitKey(0) == ord('q') :
        break
cv.destroyAllWindows()