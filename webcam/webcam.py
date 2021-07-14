import cv2.cv2 as cv

print (cv.__version__)

capture = cv.VideoCapture(0)

ret, img = capture.read()
cv.imshow('', img)

capture.release()
