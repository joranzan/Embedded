# Thread 사이에서 통신하는 샘플 코드
# Signal() 을 이용해 signal을 생성 후 보낸다.

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from time import sleep


class MyThread(QThread):
    # main Thread 로 보낼 Signal() 객체 생성, int, str 타입의 data 전송
    mySignal = Signal(int, str)

    def __init__(self):
        super().__init__()

    flag = False

    def run(self):
        self.val = 0
        self.flag = True
        while self.flag:
            # .emit() 이용해서 data 전송
            self.mySignal.emit(self.val, "KFC")
            self.val += 1
            sleep(1)

    def stop(self):
        self.flag = False
        print("Thread Stop")


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.btn = QPushButton("클릭")
        self.btn.clicked.connect(self.thread_stop)

        self.setCentralWidget(self.btn)

        self.th = MyThread()
        self.th.start()
        # 객체.시그널.connect(슬롯함수) format 그대로 작성
        # Thread에서 보낸 mySignal 에 settingUI 함수를 연결했다.
        self.th.mySignal.connect(self.settingUI)

    def thread_stop(self):
        self.th.stop()

    # 넘어온 data 받아줄 settingUI() 생성
    def settingUI(self, val, msg):
        # 버튼의 text로 msg 정하기
        self.btn.setText(msg)
        print(val, msg)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()