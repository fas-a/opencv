import cv2 as cv

vid = cv.VideoCapture("./video_capture/output.mp4")
if not vid.isOpened :
    print("failed open video")
    exit()
while True :
    ret, frame = vid.read()
    if not ret :
        print("frame not take")
        exit()
    cv.imshow("vid", frame)
    if cv.waitKey(25) & 0xFF == ord('q'):
        break
vid.release
cv.destroyAllWindows()