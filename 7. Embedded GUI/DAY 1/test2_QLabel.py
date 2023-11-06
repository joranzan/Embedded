# 레이블 샘플코드
# QLabel() : Qt의 레이블 객체 생성, 생성하면서 레이블의 text를 정할 수 있다.
# .setGeometry() : 상위 객체의 위치를 기준으로 배치가 된다.

from PySide6.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.setWindowTitle("Qt GUI App")
        self.setGeometry(0, 0, 400, 300)

        # "Hello!" 문구와 함께 레이블을 win에 생성
        self.lbl = QLabel("Hello!", self)
        # 레이블의 위치를 win 기준으로 100,100 위치에 가로 50, 세로 50의 크기로 생성
        self.lbl.setGeometry(100, 100, 50, 50)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()