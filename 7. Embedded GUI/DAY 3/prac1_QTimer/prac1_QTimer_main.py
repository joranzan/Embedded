#QTimer 샘플 코드

from PySide6.QtWidgets import *
from PySide6.QtCore import *
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        #QTimer() 객체 생성
        self.tm = QTimer()
        #timer interval 500ms 로 정하기
        self.tm.setInterval(500)
        #timer 동작 시, run() 호출
        self.tm.timeout.connect(self.run)
        #timer 시작
        self.tm.start()
        #timer interval, timer 동작 여부 출력
        print(self.tm.interval(), self.tm.isActive())

    num = 0
    def run(self):
        self.num += 1
        if self.num > 10:
            #timer 종료
            self.tm.stop()
            #timer 동작 여부 출력
            print(self.num, self.tm.isActive())
            return
        print(self.num)

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()