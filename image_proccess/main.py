import cv2
import sys

img = cv2.imread(".\image_proccess\photo.jpg")
if img is None:
    sys.exit("Could not read the image.")
cv2.imshow("Display window", img)
k = cv2.waitKey(0)

if k == ord("s"):
    cv2.imwrite(".\image_proccess\photo2.png", img)
elif k == ord("q"):
    sys.exit()