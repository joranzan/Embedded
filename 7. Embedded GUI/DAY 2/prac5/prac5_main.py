# styleSheet 를 코드로 직접 적용하는 샘플 코드
# styleSheet는 지정된 방식으로 설정해야 하며, 각각 rgb, CSS 스타일로 적용한 샘플 코드이다.

from PySide6.QtWidgets import *
from time import sleep

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.lbl = QLabel("BBQ")
        # rgb 로 적용
        self.lbl.setStyleSheet("background-color:rgb(255,255,0)")

        self.btn = QPushButton("KFC")
        # CSS 스타일로 적용
        color = "#FF0000"
        self.btn.setStyleSheet("background-color:%s" % color)

        self.vlay = QVBoxLayout()
        self.vlay.addWidget(self.lbl)
        self.vlay.addWidget(self.btn)

        mainWidget = QWidget()
        mainWidget.setLayout(self.vlay)
        self.setCentralWidget(mainWidget)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()