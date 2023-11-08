#QLCDNumber 샘플코드
#숫자 값을 보여주는 display
#.display() : 값을 LCD에 보여준다.

from PySide6.QtWidgets import *
from MainUI import Ui_MainWindow

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        #슬라이더를 움직이면, run() 호출
        self.hslider.valueChanged.connect(self.run)

    def run(self, val):
        #슬라이더 값을 LCD에 표시한다.
        self.lcd.display(val)

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()