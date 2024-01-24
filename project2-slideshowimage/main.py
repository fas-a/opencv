import cv2 as cv
import numpy as np
x, y, z = 1.0, 0.0, 0.0
sumx, sumy, sumz = -0.1, 0.1, 0.0
img1 = cv.imread(".\image_proccess\photo.jpg")
img2 = cv.imread(".\image_proccess\photo2.png")
img3 = cv.imread(".\image_proccess\photo3.jpg")

cv.namedWindow("Display window")
while True:
    cv.imshow("Display window", cv.addWeighted(cv.addWeighted(img1, x, img2, y, 0), 1.0-z, img3, z, 0))
    if x >= 1.0:
        x = 1.0
        y = 0.0
        z = 0.0
        sumx, sumy, sumz = -0.1, 0.1, 0.0
    elif y >= 1.0:
        x = 0.0
        y = 1.0
        z = 0.0
        sumx, sumy, sumz = 0.0, -0.1, 0.1
    elif z >= 1.0:
        x = 0.0
        y = 0.0
        z = 1.0
        sumx, sumy, sumz = 0.1, 0.0, -0.1
    x += sumx
    y += sumy
    z += sumz
    if cv.waitKey(30) == ord('q') :
        break
cv.destroyAllWindows()