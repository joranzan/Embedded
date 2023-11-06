# 수직 배치, 수평 배치 레이아웃을 같이 사용한 샘플코드
# 디자인을 보고, 어떤 레이아웃을 사용할 지 결정하고 사용해야 한다.
# QHBoxLayout : 수평배치 레이아웃 생성
# .addLayout() : 레이아웃을 추가하는 API

from PySide6.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.setWindowTitle("Qt GUI App")
        self.setGeometry(0, 0, 300, 300)

        # 버튼 3개 생성
        self.btn1 = QPushButton("Top")
        self.btn2 = QPushButton("LEFT")
        self.btn3 = QPushButton("RIGHT")

        # 수직배치, 수평배치 레이아웃 생성
        self.vlay = QVBoxLayout(self)
        self.hlay = QHBoxLayout(self)

        # 수직배치 레이아웃에 btn1 추가
        self.vlay.addWidget(self.btn1)

        # 수평배치 레이아웃에 btn2, btn3 추가
        self.hlay.addWidget(self.btn2)
        self.hlay.addWidget(self.btn3)

        # 수직배치 레이아웃에 수평배치 레이아웃
        self.vlay.addLayout(self.hlay)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()