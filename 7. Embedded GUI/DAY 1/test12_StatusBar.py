# QMainWindow 의 StatusBar 사용하기
# QMainWindow 에는 StatusBar 를 다루기 위한 메서드들이 정의되어 있다.
# StatusBar() : statusBar 객체 생성
# .showMessage() : statusBar에 메시지를 출력한다.

from PySide6.QtWidgets import *


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

        mainWidget = QWidget()
        mainWidget.setLayout(self.vlay)
        self.setCentralWidget(mainWidget)

        # statusBar() 객체 생성
        self.bar = self.statusBar()
        # statusBar에 메시지 출력
        self.bar.showMessage("BBQ")


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()