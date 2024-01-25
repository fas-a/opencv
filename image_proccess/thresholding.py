# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt
# img = cv.imread('./image_proccess/gradient.png', cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"
# ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
# ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
# ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
# ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# img = cv.imread('./image_proccess/messi5.jpg', cv.IMREAD_GRAYSCALE)
vid = cv.VideoCapture(0)
# assert img is not None, "file could not be read, check with os.path.exists()"
while True:
    _,img = vid.read()
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.medianBlur(img,5)
    ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
    th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
    th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
    # titles = ['Original Image', 'Global Thresholding (v = 127)',
    #             'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    # images = [img, th1, th2, th3]
    # for i in range(4):
    #     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    #     plt.title(titles[i])
    #     plt.xticks([]),plt.yticks([])
    cv.imshow('gray', img)
    cv.imshow('th1', th1)
    cv.imshow('th2', th2)
    cv.imshow('th3', th3)
    if cv.waitKey(1) == ord('q'):
        break
vid.release()