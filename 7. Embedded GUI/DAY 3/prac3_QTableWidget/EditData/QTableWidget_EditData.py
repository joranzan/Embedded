#QTableWidget 에 data 추가하는 샘플 코드
#공백인 Item에 data를 추가한다.

from PySide6.QtWidgets import *
from MainUI import Ui_MainWindow
class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        for y in range( self.table.rowCount() ):
            for x in range( self.table.columnCount() ):
                data = self.table.item(y,x)
                #data가 있다면,
                if data:
                    print( data.text(), end = ' ')
                #data가 없다면,
                else:
                    #setItem() 로 데이터를 추가한다.
                    self.table.setItem(y,x, QTableWidgetItem("HI"))
                    print("HI")
            print()

    def click(self):
        pass

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()