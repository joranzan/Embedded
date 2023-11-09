#Qt의 이미지 출력 샘플코드
#img 파일을 QImage() 객체로 불러온 뒤,
#QPixmap()객체로 변환해서 레이블로 출력한다.

from PySide6.QtWidgets import *
from PySide6.QtGui import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        img = QImage('burger.png')
        pixmap_img = QPixmap(img)
        self.lbl = QLabel()
        self.lbl.setPixmap(pixmap_img)
        self.lbl.adjustSize()

        self.setCentralWidget(self.lbl)

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()