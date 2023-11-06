# 버튼 샘플코드
# QPushButton() : 버튼 객체 생성, 레이블과 마찬가지로 생성하면서 text 지정 가능
# User가 버튼을 누르는 순간, 버튼이 눌리는 signal 인 clicked 가 발생
# slot은 버튼의 clicked 시그널이 발생하면, KFC() 호출한다.

from PySide6.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.setWindowTitle("Qt GUI App")
        self.setGeometry(0, 0, 400, 300)

        # "버튼 클릭" text를 가진 버튼 생성
        self.btn = QPushButton("버튼 클릭", self)
        self.btn.setGeometry(100, 0, 100, 100)
        # 버튼의 clicked 시그널이 발생 시, KFC() 호출하도록 연결
        self.btn.clicked.connect(self.KFC)

    # 버튼이 clicked 시그널 발생 시 호출되는 KFC()
    def KFC(self):
        print("click")


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()