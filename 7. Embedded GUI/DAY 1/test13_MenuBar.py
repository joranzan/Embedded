# QMainWindow 의 Menu Bar 사용하기
# Menu Bar를 생성하고, QAction을 등록한다.
# QAction은 slot 함수를 등록해, User가 원하는 동작을 수행할 수 있다.
# QAciont은 단축키를 등록해 쉽게 조작이 가능하다.

from PySide6.QtWidgets import *
from PySide6.QtGui import *


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.setWindowTitle("Qt GUI App")
        self.setGeometry(0, 0, 300, 300)

        self.vlay = QVBoxLayout()
        self.lbl = QLabel("KFC")
        self.btn = QPushButton("클릭")
        self.vlay.addWidget(self.lbl)
        self.vlay.addWidget(self.btn)

        mainWidget = QWidget()
        mainWidget.setLayout(self.vlay)
        self.setCentralWidget(mainWidget)

        # menuBar객체 menu 생성, menuBar() 는 QMainWindow 에 멤버함수
        self.menu = self.menuBar()
        # menuBar 에 File 메뉴 추가(등록), &를 붙이면 단축키 사용이 가능하다. Alt+F
        self.menuFile = self.menu.addMenu("&File")
        # menuBar 에 Edit 메뉴 추가, &를 붙이면 단축키 사용이 가능하다. Alt+E
        self.menuEdit = self.menu.addMenu("&Edit")

        # QAction() 객체 생성(메뉴에 Action 등록), 단축키 사용
        self.openAction = QAction("&Open", self)
        # openAction 과 open() 를 연결, Open 메뉴 클릭 시, open() 호출
        self.openAction.triggered.connect(self.open)
        # 키보드 단축키 추가, Ctrl+O 누르면 Open 메뉴 선택
        self.openAction.setShortcut(QKeySequence("Ctrl+O"))

        # menuFile 에 openAction 객체 등록, File 메뉴 클릭 시, Open 메뉴 창이 나타난다.
        self.menuFile.addAction(self.openAction)

    def open(self):
        self.lbl.setText("Open 선택")


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()