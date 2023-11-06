# QMainWindow 사용하기
# QMainWidnow 는 CentralWidget 영역에 Widget을 배치해야 한다.
# 여러 개의 Widget을 배치하기 위해 레이아웃을 이용해 Design 후, CentralWidget 에 레이아웃을 등록한다.
from PySide6.QtWidgets import *


# QMainWindow class 를 상속받은 MyApp Class
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.setWindowTitle("Qt GUI App")
        self.setGeometry(0, 0, 300, 300)

        self.vlay = QVBoxLayout()
        self.btn1 = QPushButton("Top")
        self.btn2 = QPushButton("Bottom")
        self.vlay.addWidget(self.btn1)
        self.vlay.addWidget(self.btn2)

        # QWidget() 객체 생성
        mainWidget = QWidget()
        # Qwidget 객체에 수평배치 레이아웃을 등록한다.
        mainWidget.setLayout(self.vlay)

        # QMainWindow의 CentralWidget 으로 mainWidget을 등록한다.
        # CentralWidget은 1개의 Widget만 등록이 가능하다.
        self.setCentralWidget(mainWidget)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()