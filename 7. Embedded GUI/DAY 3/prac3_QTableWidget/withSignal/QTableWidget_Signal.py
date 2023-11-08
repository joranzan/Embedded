# QTableWidget 의 signal 사용하기 샘플코드
# .cellEntered(int, int)
# .cellPressed(int, int)

from PySide6.QtWidgets import *
from MainUI import Ui_MainWindow


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        pass

    # Table의 Cell을 클릭하면, 해당 Cell의 좌표가 출력된다.
    def click(self, x, y):
        print(x, y)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()