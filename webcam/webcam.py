import cv2 as cv
import argparse

print (f'cv2 version: {cv.__version__}')


def main():
    cam = cv.VideoCapture(0)
    while True: #cam.isOpened():
        ret, img = cam.read()
        if ret:
            cv.imshow('Cam name: ' + cam.getBackendName(), img)
            # cv.waitKey(0) # ожидание нажатия любой клавиши
            # cv.imwrite('img.jpg', img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()