# Qt Designer 에서 signal/slot 등록 후 등록한 slot 함수 ( click() ) 를 재정의해서 사용하는 샘플 코드

from PySide6.QtWidgets import *
from DownloadUI import Ui_MainWindow
from time import sleep


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        pass

    # designer 에서 등록한 click() 재정의해서 사용
    def click1(self):
        print('You pressed a Button1!')
        value = 0
        while True:
            self.progressBar.setValue(value)
            if value == 100: break
            value += 1
            sleep(0.05)



    def click2(self):
        print('You pressed a Button2!')
        value = 0
        while True:
            self.progressBar_2.setValue(value)
            if value == 100: break
            value += 1
            sleep(0.05)

    def click3(self):
        print('You pressed a Button3!')
        value = 0
        while True:
            self.progressBar_3.setValue(value)
            if value == 100: break
            value += 1
            sleep(0.05)

    def click4(self):
        print('You pressed a Button4!')
        value = 0
        while True:
            self.progressBar_4.setValue(value)
            if value == 100: break
            # print(value)
            value += 1
            sleep(0.05)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()