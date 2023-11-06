# Form 레이아웃에 2개 widget 배치하기
# 다른 레이아웃 이용해서 widget을 여러 개 배치하면 된다.

from PySide6.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.setWindowTitle("Qt GUI App")
        self.setGeometry(0, 0, 300, 300)

        self.form = QFormLayout(self)
        self.edit = QLineEdit()
        self.btn = QPushButton("확인")
        # 텍스트에디터와 버튼을 담을 수평배치 레이아웃 생성
        hlay = QHBoxLayout()

        # 수평배치 레이아웃에 텍스트에디터와 버튼을 추가한다.
        hlay.addWidget(self.edit)
        hlay.addWidget(self.btn)

        # Form 레이아웃에 수평배치 레이아웃을 text와 함께 추가한다.
        self.form.addRow("name", hlay)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()