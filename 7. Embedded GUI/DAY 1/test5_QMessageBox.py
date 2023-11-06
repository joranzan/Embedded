# QMessageBox 샘플코드
# 버튼이 눌리면, 텍스트에디터에 적힌 글자가 메시지 박스에 출력되는 코드
# QMessageBox는 독립적인 창이 생성되기 때문에, .exec() 를 이용해서 User가 닫기 전까지 실행되도록 해야 한다.

from PySide6.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.setWindowTitle("Qt GUI App")
        self.setGeometry(0, 0, 300, 150)
        self.lineEdit = QLineEdit(self)
        self.btn = QPushButton("클릭", self)
        self.btn.setGeometry(150, 0, 50, 50)
        self.btn.clicked.connect(self.KFC)

    # 버튼이 눌리면,
    def KFC(self):
        # QMessageBox 객체 생성
        self.msg = QMessageBox()
        # QMessageBox의 text를 텍스트에디터에 적힌 text로 정한다.
        self.msg.setText(self.lineEdit.text())
        # QMessageBox는 독립적인 창이므로, User가 닫기 버튼을 누를 때까지 실행될 수 있게 .exec() 사용한다.
        self.msg.exec()


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()