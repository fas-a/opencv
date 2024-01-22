import cv2 as cv
import numpy

vid = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('./video_capture/output.mp4', fourcc, 30.0, (640, 480))

while vid.isOpened :
    ret, frame = vid.read()
    frame = cv.flip(frame, 1)
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
    
vid.release()
out.release()
cv.destroyAllWindows()