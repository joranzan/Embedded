# QLineEdit 샘플코드
# QLineEdit() : 한 줄 입력받는 텍스트 에디터 객체 생성
# .text() : 해당 객체의 text data 가져오기
# .setText() : 객체의 text 설정하기
from PySide6.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.setWindowTitle("Qt GUI App")
        self.setGeometry(0, 0, 400, 300)

        # 한 줄 입력받는 텍스트에디터 생성
        self.lineEdit = QLineEdit(self)
        self.btn = QPushButton("버튼 클릭", self)
        self.btn.setGeometry(0, 50, 100, 50)
        self.btn.clicked.connect(self.KFC)
        self.lbl = QLabel("HOHO", self)
        self.lbl.setGeometry(0, 100, 100, 50)

    def KFC(self):
        # 버튼이 눌리면, 텍스트에디터에 적힌 text로 레이블의 text를 정한다.
        self.lbl.setText(self.lineEdit.text())
        print("click")


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()