# QVBoxLayout 샘플코드
# 버튼 2개를 수직배치에 넣은 샘플 코드
# 반응형 App 제작을 위해 레이아웃을 사용한다.
# .addWidget() 으로 widget을 레이아웃에 추가한다.

from PySide6.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.setWindowTitle("Qt GUI App")
        self.setGeometry(0, 0, 300, 300)

        self.btn1 = QPushButton("Top")
        self.btn2 = QPushButton("Bottom")

        # 수직배치 객체 생성
        self.vlay = QVBoxLayout(self)
        # .addWidget() 으로 레이아웃에 btn1 추가
        self.vlay.addWidget(self.btn1)
        # .addWidget() 으로 레이아웃에 btn2 추가
        self.vlay.addWidget(self.btn2)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()