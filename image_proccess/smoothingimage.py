import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('./image_proccess/opencv_logo.jpg')
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
blur = cv.blur(img,(2,2))
blur = cv.GaussianBlur(img,(5,5),0)
median = cv.medianBlur(img,3)
blur = cv.bilateralFilter(img,9,75,75)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()