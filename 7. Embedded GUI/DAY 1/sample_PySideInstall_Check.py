# Qt GUI 개발 첫번째 샘플
# python Class 문법을 이용해 개발을 시작한다.
# 추후, Qt Designer 로 GUI 개발을 하면, Class 형식으로 개발되어 import 해 사용할 예정

# Qt GUI Widget 사용을 위한 Qt.Widgets 패키지 import
from PySide6.QtWidgets import *


# QWidget 을 상속받은 MyApp class 생성
class MyApp(QWidget):
    # 객체 생성시 가장 먼저 호출 되는 init() 생성자
    def __init__(self):
        # QWidget의 메서드를 호출하기 위한 super()
        super().__init__()
        self.main()

    def main(self):
        pass


# python 의 main
# import main.py 할 경우 실행되지 않는다.
if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()