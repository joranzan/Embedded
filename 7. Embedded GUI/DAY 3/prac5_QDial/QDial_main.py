# QDial 샘플 코드
# QDial 을 돌리면 레이블에 Dial 의 value 를 출력한다.
# -signal : valueChanged

from PySide6.QtWidgets import *
from MainUI import Ui_MainWindow


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        # dial의 valueChanged 시그널이 발생하면, run() 를 호출한다.
        self.dial.valueChanged.connect(self.run)

    def run(self, val):
        # 레이블의 text는 문자열이므로 형변환 한다.
        self.lbl.setText(str(val))
        print(val)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()