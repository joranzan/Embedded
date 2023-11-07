# Qt Designer 에서 signal/slot 등록 후 등록한 slot 함수 ( click() ) 를 재정의해서 사용하는 샘플 코드

from PySide6.QtWidgets import *
from LCD_DialUI import Ui_MainWindow


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        pass

    # designer 에서 등록한 click() 재정의해서 사용
    def on_click(self):
        print('ON')

    def off_click(self):
        print('OFF')

    def valueChange(self):
        self.lcdNumber.intValue = self.dial.value
        self.lcdNumber.display(self.lcdNumber.intValue())
        print(self.lcdNumber.intValue())



if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()