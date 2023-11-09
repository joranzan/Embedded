#openCV 로 이미지 가공하고, Qt로 출력하는 샘플코드

import cv2
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from MainUI import Ui_MainWindow
import numpy

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.img = QImage('burger.png')
        pixmap_img = QPixmap(self.img)
        self.origin_lbl.setPixmap(pixmap_img)

    def printImage(self, imgBGR):
        # cvtColor : cv2에서 가공한 image(BGR) 을 RGB로 변환
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        # shape : img 객체의 정보 return
        h, w, byte = imgRGB.shape
        # QImage : QImage 객체로 변환
        img = QImage(imgRGB, w, h, byte*w, QImage.Format_RGB888)
        #Label에 출력
        self.openCV_lbl.setPixmap(QPixmap(img))

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

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()