# Qt Widget의 list 화
# 수직배치에 들어 있는 5개의 Progress Bar ( pb1, pb2, pb3, pb4, pb5 ) 를 list에 담고 값을 변경하는 샘플 코드
# Qt는 별도로 widget의 list화를 지원하지 않는다.
# Python의 list를 이용해 widget을 list 에 담아 처리한다.

from PySide6.QtWidgets import *
from MainUI import Ui_MainWindow
from time import sleep


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    # Widget을 담을 리스트 생성
    pblist = []

    def main(self):
        # 수직배치를 lay 변수에 저장
        lay = self.verticalLayout
        # 수직배치의 항목 수만큼 반복, 5개 pb, 5회 반복
        for i in range(lay.count()):
            # 수직배치의 i번째 항목의 widget 을 pblist 에 추가
            self.pblist.append(lay.itemAt(i).widget())

        for i in range(5):
            self.pblist[i].setValue(0)

    def go(self):
        for n in range(5):
            for val in range(101):
                self.pblist[n].setValue(val)
                sleep(0.01)


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()