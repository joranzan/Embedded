




from PySide6.QtWidgets import *
from MainUI import Ui_MainWindow
from matplotlib import pyplot
import random
# Matplotlib에서 지원하는 QT 포팅용 패키지
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = {'apple': 15, 'orange': 6, 'lemon': 21, 'lime': 7}
        self.names = list(self.data.keys())
        self.values1 = list(self.data.values())
        self.values2 = list(self.data.values())
        self.values3 = list(self.data.values())
        self.flag1 = False
        self.flag2 = False
        self.flag3 = False
        self.main()


    def main(self):
        # figure : 그래프 정보를 담고 있는 객체
        self.figure = pyplot.Figure()
        # 그래프를 Qt에 출력하는 객체
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.lay.addWidget(self.canvas)
        self.graph1 = self.figure.add_subplot(1, 3, 1)
        self.graph2 = self.figure.add_subplot(1, 3, 2)
        self.graph3 = self.figure.add_subplot(1, 3, 3)



    def drawGraph(self):
        self.figure.clear()
        self.graph1 = self.figure.add_subplot(1, 3, 1)
        self.graph2 = self.figure.add_subplot(1, 3, 2)
        self.graph3 = self.figure.add_subplot(1, 3, 3)

        if self.flag1:
            self.graph1.plot(self.names, self.values1)
        if self.flag2:
            self.graph2.scatter(self.names, self.values2)
        if self.flag3:
            self.graph3.bar(self.names, self.values3)
        self.canvas.draw()

    def chart1(self):
        self.flag1 = True
        # chart1 버튼 누르면 그린다
        for i in range(len(self.values1)):
            self.values1[i] = random.randint(0,20)
        self.drawGraph()

    def chart2(self):
        self.flag2 = True
        self.drawGraph()
        for i in range(len(self.values2)):
            self.values2[i] = random.randint(0, 20)
        self.drawGraph()

    def chart3(self):
        self.flag3 = True
        self.drawGraph()
        for i in range(len(self.values3)):
            self.values3[i] = random.randint(0, 20)

        self.drawGraph()

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()
