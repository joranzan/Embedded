from PySide6.QtWidgets import *
from PySide6.QtCore import *
from MainUI import Ui_MainWindow

class MyThread(QThread):
    mySignal = Signal(int)

    def __init__(self, val):
        super().__init__()
        self.val = val

    flag = True

    def run(self):
        if self.flag:
            for i in range(101):
                self.mySignal.emit(i)
                self.msleep(50)  # 100ms마다 업데이트

    def stop(self):
        self.flag = False

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    pblist = []
    threads = []
    currentIndex = 0

    def main(self):
        lay = self.gridLayout
        for i in range(lay.count()):
            self.pblist.append(lay.itemAt(i).widget())
        self.pblist[0], self.pblist[1] = self.pblist[1], self.pblist[0]
        self.pblist[2], self.pblist[3] = self.pblist[3], self.pblist[2]

    def click4(self):
        if self.currentIndex <= 4:
            th = MyThread(self.currentIndex)
            self.currentIndex += 1
            th.mySignal.connect(self.settingUI)
            th.start()
            self.threads.append(th)

    def reset(self):

        for i in self.threads:
            i.stop()
        self.threads = []

        for i in range(5):
            self.pblist[i].setValue(0)
        self.currentIndex = 0

    def settingUI(self, val):
        sender_thread = self.sender()
        if sender_thread in self.threads:
            index = self.threads.index(sender_thread)
            self.pblist[index].setValue(val)

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()
