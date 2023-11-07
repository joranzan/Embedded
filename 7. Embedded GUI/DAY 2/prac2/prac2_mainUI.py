# Qt Designer로 제작한 .ui 파일을 .py로 변환한 mainUI1.py 를 Import 한 뒤, ui를 가져오는 샘플 코드
# pyside6-uic.exe 로 mainUI.ui 를 mainUI1.py 로 변환하는 코드
#   .\venv\Scripts\pyside6-uic.exe .\mainUI.ui -o .\mainUI1.py

from PySide6.QtWidgets import *
# mainUI1.py 파일을 Ui_MainWindow Class import 한다.
# 파일명이 mainUI1.py 가 아닌 경우 변경해야 한다.
from mainUI1 import Ui_MainWindow


# Ui_MainWindow class 도 상속한다.
class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Ui를 Ui_MainWindow에서 갖고온다.
        self.setupUi(self)
        self.main()

    def main(self):
        pass


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()