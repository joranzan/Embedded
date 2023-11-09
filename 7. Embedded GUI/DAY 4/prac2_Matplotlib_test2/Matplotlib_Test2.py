from PySide6.QtWidgets import *
from MainUI import Ui_MainWindow
from matplotlib import pyplot
# Matplotlib에서 지원하는 QT 포팅용 패키지
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        # figure : 그래프 정보를 담고 있는 객체
        self.figure = pyplot.Figure()
        # 그래프를 Qt에 출력하는 객체
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.lay.addWidget(self.canvas)
        # add_subplot : 다단계 그래프용 plot
        self.graph1 = self.figure.add_subplot(1, 2, 1)
        self.graph2 = self.figure.add_subplot(1, 2, 2)
        print(type(self.figure))
        print(type(self.graph1))

    def chart1(self):
        # chart1 버튼 누르면 그린다
        x = [1, 2, 3, 4, 5]
        y1 = [10, 20, 30, 43, 54]
        y2 = [32, 54, 7, 34, 65]
        # linestyle : 선 종류
        # marker : 점 종류
        # legend : 범례
        self.graph1.plot(x, y1, linestyle='--', marker='o')
        self.graph1.plot(x, y2, linestyle=':', marker='*')
        self.graph1.legend(["BBQ", "KFC"])
        self.canvas.draw()

    def chart2(self):
        self.figure.clear()
        self.main()
        x = [1, 2, 3, 4, 5]
        y = [10, 1, 30, 43, 25]
        # bar : 막대 그래프 그리기
        self.graph2.bar(x, y)
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()