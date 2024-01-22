import cv2 as cv

vid = cv.VideoCapture("./video_capture/vid.mp4")
if not vid.isOpened :
    print("failed open video")
    exit()
while True :
    ret, frame = vid.read()
    if not ret :
        print("frame not take")
        exit()
    cv.imshow("vid", frame)
    cv.waitKey(5)
    if cv.waitKey(1) == ord('q'):
        break
vid.release
cv.destroyAllWindows()