import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
    pass

vid = cv.VideoCapture(0)

cv.namedWindow('gray')
cv.createTrackbar('tres', 'gray', 0, 255, nothing)
while True:
    tres = cv.getTrackbarPos('tres', 'gray')
    _,img = vid.read()
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.medianBlur(img,5)
    ret,th1 = cv.threshold(img,tres,255,cv.THRESH_BINARY)
    th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
    th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
    cv.imshow('gray', img)
    cv.imshow('th1', th1)
    cv.imshow('th2', th2)
    cv.imshow('th3', th3)
    if cv.waitKey(1) == ord('q'):
        break
vid.release()