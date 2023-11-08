#QSlider 사용하는 샘플 코드
#QSlider 는 수직, 수평 변경이 가능하다.
#.setPageStep() 으로 pageStep을 조절할 수 있다.
#.setMaximum() 으로 슬라이더 최대 값 변경이 가능하다.
#signal : valueChanged

from PySide6.QtWidgets import *
from MainUI import Ui_MainWindow

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        #슬라이더의 값이 변경될 때, run() 호출
        self.hslider.valueChanged.connect(self.run)
        #슬라이더의 pageStep 변경
        self.hslider.setPageStep(30)
        #슬라이더의 최대값 변경
        self.hslider.setMaximum(255)

    def run(self, val):
        self.lbl.setText( str(val) )
        print(val)

if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()