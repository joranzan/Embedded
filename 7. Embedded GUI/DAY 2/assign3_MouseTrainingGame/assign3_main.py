# Qt Designer 에서 signal/slot 등록 후 등록한 slot 함수 ( click() ) 를 재정의해서 사용하는 샘플 코드

from PySide6.QtWidgets import *
from MouseTrain import Ui_MainWindow
import random
from PySide6.QtCore import *
class MyApp(QMainWindow, Ui_MainWindow):
    num = 0
    cnt = 0
    flag = 0
    basicmsg = "남은시간 : "
    timeleft = 60
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    # timerEvent() 재정의
    def timerEvent(self, event):

        if self.num >= 60:
            self.timer.stop()
            msg = ("1분 동안 클릭 성공 횟수 : ")
            msg += str(self.cnt)
            print(msg)
            self.msgbox = QMessageBox()
            self.msgbox.setText(msg)
            self.msgbox.exec()
            num = 0
            flag = 0
            # timer 종료
        else:
            self.num += 1
            if self.timeleft > 0:
                self.timeleft -= 1
            self.label_2.setText(self.basicmsg + str(self.timeleft))
            print(self.num)


            c = random.randrange(0, self.frame.width() - self.label.width())
            r = random.randrange(0, self.frame.height() - self.label.height())

            print(self.frame.x())
            print(self.frame.y())

            self.label.move(c, r)

    def mousePressEvent(self, event):
        if self.flag==1 :
            x = event.x()
            y = event.y() -self.label_2.height()

            label_x = self.label.x() + self.label.width()
            label_y = self.label.y() + self.label.height()


            if x >= self.label.x() and x <= label_x:
                if y>=self.label.y() and y<=label_y:
                    self.cnt += 1
            print(self.cnt)


    def main(self):
        self.setWindowTitle("미꾸라지 김승배 잡기")
        print("frame 시작 위치")
        print(self.frame.x())
        print(self.frame.y())

        print("frame 끝 위치")
        print(self.frame.x() + self.frame.width())
        print(self.frame.y() + self.frame.height())

    def Start(self):
        self.flag = 1
        self.label_2.setText(self.basicmsg + str(self.timeleft))
        #QBasicTimer() 객체 생성
        self.timer = QBasicTimer()
        #timer 시작, 500ms 에 한번 timerEvent() 호출
        self.timer.start(1000, self)



    # designer 에서 등록한 click() 재정의해서 사용
    def changeName(self):
        ret, ok = QInputDialog.getText(self, "이름 변경", "변경한 이름 입력")
        if ok:
            self.label.setText(ret)

        print('You Changed Name!')

    def changeColor(self):
        color = QColorDialog.getColor().name()
        if color:
            self.frame.setStyleSheet(u"background-color: %s" % color)



if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()