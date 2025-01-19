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

    def GetImage(self):
        cam = self.cam
        if cam == None:
            return None
        if cam.isOpened():
            ret, image = cam.read()
            if ret:
                return image
            else:
                return None

    def ShowImage(self) -> bool:
        cam = self.cam
        if cam == None:
            return False
        if cam.isOpened():
            ret, img = cam.read()
            if ret:
                window_name = 'Cam name: ' + cam.getBackendName()
                cv.imshow(window_name, img)
                cv.waitKey(1)
                # cv.destroyWindow(window_name) # так можно закрыть окно по имени

    def SaveImage(self, file_name: str='img.jpg') -> None:
        cam = self.cam
        if cam == None:
            return False
        image = self.GetImage()
        if cam.isOpened():
            ret, image = cam.read()
            if ret:
                cv.imwrite(filename=file_name, img=image)


def main():

    cam = Camera()
    cam.CamOpen()

    for i in range(10):
        name = str(i) + '.jpg'
        cam.ShowImage()
        cam.SaveImage(name)
        time.sleep(0.1)

    cam.CamClose()

    return

if __name__ == '__main__':
    main()