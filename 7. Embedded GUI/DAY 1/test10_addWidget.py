# Form Layout에 addWidget을 사용하면, text 없이 widget을 추가할 수 있다.

from PySide6.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.setWindowTitle("Qt GUI App")
        self.setGeometry(0, 0, 300, 300)

        self.form = QFormLayout(self)
        self.lbl = QLabel("SSAFY")

        # addWidget() 를 사용해서 text 없이 레이블을 추가한다.
        self.form.addWidget(self.lbl)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()