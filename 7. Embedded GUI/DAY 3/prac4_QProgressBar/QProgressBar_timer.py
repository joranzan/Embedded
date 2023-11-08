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
        self.progressBar.setInvertedAppearance(False)

        #타이머를 이용해서 progressBar 움직이기
        self.timer = QTimer()
        self.timer.setInterval(30)
        self.timer.timeout.connect(self.run)
        self.timer.start()

    def run(self):
        #progressBar 의 값을 현재 값 + 1 로
        self.progressBar.setValue( self.progressBar.value()+1 )
        if self.progressBar.value() == 100:
            self.timer.stop()

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()