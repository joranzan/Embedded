from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from MainUI import Ui_MainWindow
import cv2
import numpy
from time import sleep
# os.environ : OpenCV4의 Qt.qpa 사용을 위한 path 설정
import os
del os.environ['QT_QPA_PLATFORM_PLUGIN_PATH']

class MyThread(QThread): # Camera로 찍은 이미지를 처리하는 Thread
    # 원본과 이미지 처리한 결과를 동시에 Signal 전송
    mySignal = Signal(QPixmap, QPixmap)

    #Thread 시작 시 촬영
    def __init__(self):
        super().__init__()
        # 0번 카메라 객체 생성
        self.cam = cv2.VideoCapture(0)
        # 3 : Width Size
        self.cam.set(3, 480)
        # 4 : Height Size
        self.cam.set(4, 320)

    flag = False
    def run(self):
        # Thread 동작 시 Camera로 0.1초에 한번 이미지 촬영
        self.flag = True
        while self.flag:
            ret, self.img = self.cam.read()
            if ret:
                # 촬영한 이미지를 printImage로 보냄
                self.printImage(self.img)
            sleep(0.1)

    def stop(self):
        # Thread 종료 시 run() 종료
        self.flag = False

    def printImage(self, imgBGR):
        # openCV로 촬영한 이미지 객체를 QPixmap() 객체로 변환
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte*w, QImage.Format_RGB888)
        q_img1 = QPixmap(img)

        grayImg = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)
        cannyImg = cv2.Canny(grayImg, 50, 200)
        imgRGB = cv2.cvtColor(cannyImg, cv2.COLOR_BGR2RGB)
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte * w, QImage.Format_RGB888)
        # canny 알고리즘을 적용한 이미지를 QPixmap() 객체로 변환
        q_img2 = QPixmap(img)
        #원본과 canny 이미지 전송
        self.mySignal.emit(q_img1, q_img2)

class MyApp(QMainWindow, Ui_MainWindow):
    # UI 출력용 Thread
    # MyThread로부터 QPixmap() 객체를 전송 받아 출력
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        # MyThread 객체 생성
        self.th = MyThread()
        # "mySignal" Signal이 감지되면 setImage 호출
        self.th.mySignal.connect(self.setImage)

    def setImage(self, img, img2):
        # cam_lbl 과 openCV_lbl 에 MyThread로 전달받은 QPixmap() 객체를 출력
        self.cam_lbl.setPixmap(img)
        self.openCV_lbl.setPixmap(img2)

    def play(self):
        # Thread 시작
        print('play')
        self.th.start()

    def mode(self):
        # 이미지 처리 전환용 API
        print('mode')

    def closeEvent(self, event):
        # App의 닫기 버튼을 누르거나 종료가 될 때 호출되는 API
        #  Thread 종료
        self.th.stop()
        #self.th.wait(3000)
        self.close()

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()