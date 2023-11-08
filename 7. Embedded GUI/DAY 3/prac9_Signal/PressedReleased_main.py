#버튼의 pressed/released signal 사용하는 샘플코드
#버튼을 누를 때, KFC 출력
#버튼에서 뗄 때, BBQ 출력

from PySide6.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.btn = QPushButton("클릭 해보셈", self)
        self.btn.pressed.connect(self.press)
        self.btn.released.connect(self.release)

    def press(self):
        print("KFC")
        self.btn.setText("press")

    def release(self):
        print("BBQ")
        self.btn.setText("release")


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()