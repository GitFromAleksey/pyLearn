import cv2.cv2 as cv

print (cv.__version__)

cams_dict = {}
for i in range(10):
    cam = cv.VideoCapture(i)
    if cam.isOpened():
        cams_dict[i] = cam.getBackendName()
        print(cam.getBackendName(), i)

capture = cv.VideoCapture(0)
print(type(capture))
print('BackendName:', capture.getBackendName())
print('isOpened:', capture.isOpened())

ret, img = capture.read()
cv.imshow('Cam name: ' + capture.getBackendName(), img)
cv.imwrite('img.jpg',img)

capture.release()
