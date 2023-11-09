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

    def blur(self):
        # imread: cv2를 이용해 image 파일 읽기
        self.openCV_img = cv2.imread('burger.png')
        # blur : (가로,세로) 값으로 Blur 처리
        self.blurImg = cv2.blur(self.openCV_img, (55,55))
        self.printImage(self.blurImg)
        print('blur')

    def gray(self):
        # imread : 이미지 파일 읽기
        self.openCV_img = cv2.imread('burger.png')
        # cvtColor : 이미지 파일 변환
        # COLOR_BGR2GRAY : BGR을 GRAY로 변환
        self.grayImg = cv2.cvtColor(self.openCV_img, cv2.COLOR_BGR2GRAY)
        self.printImage(self.grayImg)
        print('gray')

    def morpho(self):
        # imread : 이미지 파일 읽기
        self.openCV_img = cv2.imread('burger.png')
        # cvtColor : GRAY로 변환
        self.grayImg = cv2.cvtColor(self.openCV_img, cv2.COLOR_BGR2GRAY)
        # ones : 1로 채워진 nxn 행렬 만드는 함수
        kernel = numpy.ones((3,3))
        # morphologyEx : 모폴로지(형태학) 연산 함수
        # 영상 분야에서 노이즈 제거, 구멍 채우기, 끊어진 선 이어붙이기 등
        # 쓰이는 연산 기법
        self.morphoImg = cv2.morphologyEx(self.grayImg, cv2.MORPH_GRADIENT, kernel)
        self.printImage(self.morphoImg)
        print('morphology')

    def thresh(self):
        # imread : 이미지 파일 읽기
        self.openCV_img = cv2.imread('burger.png')
        # cvtColor : GRAY 변환
        self.grayImg = cv2.cvtColor(self.openCV_img, cv2.COLOR_BGR2GRAY)
        # threshold : 이미지 이진화 함수 (임계 넘으면 1 아니면 )
        ret, self.thresholdImg = cv2.threshold(self.grayImg, 120, 255, cv2.THRESH_BINARY)
        self.printImage(self.thresholdImg)
        print('threshold')

    def canny(self):
        # imread : 이미지 읽기
        self.openCV_img = cv2.imread('burger.png')
        # cvtColor : Gray 변환
        self.grayImg = cv2.cvtColor(self.openCV_img, cv2.COLOR_BGR2GRAY)
        # Canny : 테두리 감지 알고리즘
        # 매개변수 1,2 : threshold(임계값)
        self.cannyImg = cv2.Canny(self.grayImg, 50, 200)
        self.printImage(self.cannyImg)
        print('canny')

    def clear(self):
        self.openCV_lbl.clear()
        print('clear')

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