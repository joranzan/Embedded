#ProgressBar 샘플코드
# 아래 두 함수의 옵션 값을 바꿔가며 테스트한다.
# .setOrientation() : Qt.Vertical / Qt.Horizontal, 수평 / 수직 방향 변경
# .setInvertedAppearance() : True, False, 정방향 / 역방향 변경

from PySide6.QtWidgets import *
from PySide6.QtCore import *

#Qt의 Horizontal, Vertical 값을 불러오기 위한 import
from PySide6.QtCore import Qt
from MainUI import Ui_MainWindow
class MyApp(QMainWindow, Ui_MainWindow):

    speed = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        #progressBar 의 값을 0으로 설정
        self.progressBar.setValue(0)
        #progressBar 의 진행 방향을 수직으로 설정, Qt.Horizontal 옵션을 넣으면, 수평 방향으로 바꿀 수 있다.
        self.progressBar.setOrientation(Qt.Vertical)
        #progressBar 의 진행 방향을 정방향으로 설정, True로 변경하면, 역방향이 된다.
        self.progressBar.setInvertedAppearance(True)

        # 슬라이더의 값이 변경될 때, run() 호출
        self.Slider.valueChanged.connect(self.speedChange)
        # 슬라이더의 pageStep 변경
        self.Slider.setPageStep(1)
        # 슬라이더의 최대값 변경
        self.Slider.setMinimum(1)
        self.Slider.setMaximum(30)

        self.SpeedLabel.setText("현재 속도 : 1")

    def Up(self):
        #progressBar 의 값을 현재 값 + 1 로
        currentVal = self.progressBar.value() - self.speed
        if currentVal <= 0:
            self.progressBar.setValue(0)
            self.timer.stop()
        self.progressBar.setValue( currentVal )


    def Down(self):
        #progressBar 의 값을 현재 값 + 1 로
        currentVal = self.progressBar.value()+self.speed
        if currentVal >= 100:
            self.progressBar.setValue(100)
            self.timer.stop()
        self.progressBar.setValue( currentVal )

    def upclick(self):
        #타이머를 이용해서 progressBar 움직이기
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.Up)
        self.timer.start()

    def downclick(self):
        #타이머를 이용해서 progressBar 움직이기
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.Down)
        self.timer.start()

    def upstop(self):
        self.timer.stop()

    def downstop(self):
        self.timer.stop()

    def speedChange(self, val):
        self.speed = val
        msg = "현재 속도 : "
        msg += str(val)
        self.SpeedLabel.setText(msg)
        print(val)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()