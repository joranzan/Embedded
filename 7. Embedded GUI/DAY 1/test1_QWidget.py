# app 꾸미기 샘플코드
# .setWindowTitle() : 창의 제목정하는 API
# .setGeometry() : 창의 위치와 가로 세로 크기 정하는 API

from PySide6.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        # App Title
        self.setWindowTitle("Qt GUI App")
        # 윈도우 x좌표, y좌표, 가로크기, 세로크기
        self.setGeometry(0, 0, 400, 300)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()