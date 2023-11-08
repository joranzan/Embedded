# QTableWidget 의 data를 접근해서 출력하는 샘플 코드
# item() 는 PySide6.QtWidgets.QTableWidgetItem type으로 return 하기 때문에, 바로 출력할 수 없다.

from PySide6.QtWidgets import *
from MainUI import Ui_MainWindow


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        # 이중 for문으로 table data 출력하기
        for y in range(self.table.rowCount()):
            for x in range(self.table.columnCount()):
                # item함수로 바로 출력 못함
                data = self.table.item(y, x)
                if data:
                    print(data.text(), end=' ')
            print()

    def click(self):
        pass


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()