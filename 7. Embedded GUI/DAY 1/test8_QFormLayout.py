# QFormLayout 샘플코드
# Form 레이아웃은 text와 함께 widget을 추가 할 수 있다.
# Form 형식의 App 개발 시 개발속도를 단축시켜준다.
# .addRow() : text와 함께 widget을 추가하는 API

from PySide6.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.setWindowTitle("Qt GUI App")
        self.setGeometry(0, 0, 300, 300)

        # Form 레이아웃 생성
        self.form = QFormLayout(self)
        self.edit = QLineEdit()
        # "name" text와 함께, 텍스트 에디터를 추가한다.
        self.form.addRow("name", self.edit)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()