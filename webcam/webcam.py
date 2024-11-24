import time
import cv2 as cv
import argparse

print (f'cv2 version: {cv.__version__}')

class Camera:

    def __init__(self) -> None:
        self.cam = None

    def __del__(self):
        self.CamClose()

    def CamOpen(self) -> bool:
        self.cam = cv.VideoCapture(0)
        return self.cam.isOpened()

    def CamClose(self) -> None:
        if self.cam:
            self.cam.release()

    def ShowImage(self) -> bool:
        cam = self.cam
        if cam == None:
            return False
        if cam.isOpened():
            ret, img = cam.read()
            if ret:
                cv.imshow('Cam name: ' + cam.getBackendName(), img)

    def SaveImage(self):
        cam = self.cam
        if cam == None:
            return False
        if cam.isOpened():
            ret, img = cam.read()
            if ret:
                cv.imshow('Cam name: ' + cam.getBackendName(), img)
                cv.imwrite('img.jpg', img)


def main():

    cam = Camera()
    cam.CamOpen()
    cam.SaveImage()
    cam.CamClose()


    return

    cam = cv.VideoCapture(0)
    while True: #cam.isOpened():
        ret, img = cam.read()
        if ret:
            cv.imshow('Cam name: ' + cam.getBackendName(), img)
            # cv.waitKey(0) # ожидание нажатия любой клавиши
            # cv.imwrite('img.jpg', img)
            time.sleep(1)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()