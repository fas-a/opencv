import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def mouseposition(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN :
        print("mouse position : ", x, y)
        print("color : ", img[y,x])
        print("intensity : ", img2gray[y,x])
BLUE = [255,0,0]
img = cv.imread('.\image_proccess\logo.jpg')
constant= cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
cv.namedWindow("Display window")
cv.setMouseCallback("Display window", mouseposition)
img2gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# doll = img[248:617, 302:516]
# img[266:635, 920:1134] = doll
# img[:,:,0] = 0
cv.imshow("Display window", img2gray)
# plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
while True:
    plt.show()
    if cv.waitKey(0) == ord('q') :
        break
cv.destroyAllWindows()