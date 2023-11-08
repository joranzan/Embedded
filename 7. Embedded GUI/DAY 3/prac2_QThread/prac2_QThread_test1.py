# QThread를 이용해서 멀티태스킹 구현

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from time import sleep


# QThread를 상속 받은 class 생성
class MyThread(QThread):
    def __init__(self):
        super().__init__()

    flag = False

    # thread 가 start() 되면, 동작하는 함수
    def run(self):
        self.flag = True
        while self.flag:
            print("NEW Thread")
            sleep(1)

    # thread 가 stop() 되면, 동작하는 함수
    def stop(self):
        self.flag = False
        print("Thread Stop")


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        # 버튼을 눌러서 thread 중지
        self.btn = QPushButton("클릭")
        self.btn.clicked.connect(self.thread_stop)

        self.setCentralWidget(self.btn)

        # MyThread() 객체 생성
        self.th = MyThread()
        # thread 시작 -> MyThread() 의 run() 실행
        self.th.start()

    # 버튼 누르면 호출되는 함수
    def thread_stop(self):
        # thread 중지 -> MyThread() 의 stop() 실행
        self.th.stop()


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()