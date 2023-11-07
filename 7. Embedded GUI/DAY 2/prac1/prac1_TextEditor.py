# 메모장 만들기 샘플 코드
# 구현 기능
# -1. 저장
# -2. 다른이름으로 저장
# -3. 파일 열기
# -4. 파일 닫기
# -5. 정보 창

from PySide6.QtWidgets import *
from PySide6.QtGui import *


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.setWindowTitle("조란잔 메모장")
        # text editor 용 QPlainTextEdit() 객체 선언
        self.edit = QPlainTextEdit()
        # MainWindow 의 CentralWidget 으로 설정
        self.setCentralWidget(self.edit)

        # menuBar 객체 선언
        self.menu = self.menuBar()
        # File, Help menu 추가
        self.menuFile = self.menu.addMenu("&File")
        self.menuHelp = self.menu.addMenu("&Help")

        # Open, Save, Save As, Close, About QAcion() 객체 생성
        self.openAction = QAction("&Open", self)
        self.saveAction = QAction("&Save", self)
        self.saveasAction = QAction("Save &As...", self)
        self.closeAction = QAction("&Close", self)
        self.aboutAction = QAction("&About", self)

        # 단축키 추가
        self.openAction.setShortcut(QKeySequence("Ctrl+O"))
        self.saveAction.setShortcut(QKeySequence("Ctrl+S"))
        self.saveasAction.setShortcut(QKeySequence("Ctrl+Shift+S"))

        # QAction과 slot 함수 등록
        self.openAction.triggered.connect(self.open_file)
        self.saveAction.triggered.connect(self.save)
        self.saveasAction.triggered.connect(self.save_as)
        self.closeAction.triggered.connect(self.close)
        self.aboutAction.triggered.connect(self.show_dialog)

        # menu에 QAction 등록
        self.menuFile.addAction(self.openAction)
        self.menuFile.addAction(self.saveAction)
        self.menuFile.addAction(self.saveasAction)
        self.menuFile.addAction(self.closeAction)
        self.menuHelp.addAction(self.aboutAction)

        # StatusBar() 객체 생성
        self.bar = self.statusBar()
        self.bar.showMessage("메모장 프로그램")

    # class 변수 path 선언
    path = None

    # 파일 open용 open_file() 생성
    def open_file(self):
        # 동작 확인용 message
        # self.bar.showMessage("open 메뉴 클릭")
        # 파일 열기 후 파일 경로를 path에 저장
        path = QFileDialog.getOpenFileName(self, "Open File")[0]
        # 파일 열기 정상적으로 동작한다면
        if path:
            # 객체 변수 self.path 에 path 값 저장
            self.path = path
            # 파일 read 후 textEditor 의 text로 설정
            self.edit.setPlainText(open(self.path).read())

    # 파일 저장용 save() 생성
    def save(self):
        self.bar.showMessage("save 메뉴 클릭")
        # 처음 파일 저장한다면
        # 파일을 처음 저장하면, 경로를 설정할 필요가 있으나, 저장된 파일을 수정한다면, 경로가 기록되어 있으니, 바로 덮어쓰기만 하기함위함
        if self.path is None:
            # save_as() 실행
            self.save_as()
        # 아니라면,
        else:
            # 파일 덮어쓰기 실행, textEditor는 수정됨으로 설정
            with open(self.path, 'w') as f:
                f.write(self.edit.toPlainText())
                self.edit.document().isModified()

    # 파일 다른이름으로 저장용 save_as() 생성
    def save_as(self):
        self.bar.showMessage("save as 메뉴 클릭")
        # 파일 저장용 dialog 표시 후 경로를 path에 저장
        path = QFileDialog.getSaveFileName(self, "Save As")[0]
        if path:
            # 파일 경로를 self.path에 저장
            self.path = path
            # save() 호출
            self.save()

    # About QAction 누르면, 나타나는 dialog용 함수
    def show_dialog(self):
        # HTML이 아니라 Qt의 rich text
        text = """<center>\
            <h1>Text Editor</h1>\
            </center>
            <p>Version 1.2.3<br>
            Copyright</p>
            """
        # QMessageBox() 객체 생성
        msg = QMessageBox()
        # About messageBox, 현재 애플리케이션의 빌드 시기 or 버전을 표시하는 정보 창
        msg.about(self, "About", text)

    # Close QAciton or 프로그램 닫기 버튼 클릭 시 나타나는 이벤트
    # QMainWindow의 멤버 함수를 재정의해서 사용
    def closeEvent(self, event):
        # 수정된 사항이 없다면, 바로 종료
        if not self.edit.document().isModified():
            return
        # 저장된 경로가 없다면, 바로 종료
        if self.path is None:
            return

        # 파일 저장 경로가 User마다 다르므로, 가장 마지막 경로만 파싱해서 MessageBox에 출력하기 위한 파싱
        path_parsing = self.path.split('/')[-1]
        msg = "변경 사항을 " + path_parsing + "에 저장하시겠습니까?"
        # 선택할 버튼으로 Save, Discard, Cancel 가진, QMessageBox의 question 메시지창 생성
        answer = QMessageBox.question(self, "하하호호메모장", msg,
                                      QMessageBox.Save |
                                      QMessageBox.Discard |
                                      QMessageBox.Cancel)
        # Save 버튼 눌렀다면, save() 호출
        if answer & QMessageBox.Save:
            self.save()
        # Cancel 버튼 눌렀다면, ignore() 호출 후 종료
        if answer & QMessageBox.Cancel:
            event.ignore()


if __name__ == '__main__':
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()