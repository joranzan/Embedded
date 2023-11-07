# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MouseTrainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1298, 850)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(16777213, 50))
        self.label_2.setStyleSheet(u"font: 700 20pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.nameBtn = QPushButton(self.centralwidget)
        self.nameBtn.setObjectName(u"nameBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nameBtn.sizePolicy().hasHeightForWidth())
        self.nameBtn.setSizePolicy(sizePolicy1)
        self.nameBtn.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")

        self.gridLayout.addWidget(self.nameBtn, 2, 0, 1, 1)

        self.startBtn = QPushButton(self.centralwidget)
        self.startBtn.setObjectName(u"startBtn")
        sizePolicy1.setHeightForWidth(self.startBtn.sizePolicy().hasHeightForWidth())
        self.startBtn.setSizePolicy(sizePolicy1)
        self.startBtn.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 255, 0);\n"
"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";")

        self.gridLayout.addWidget(self.startBtn, 2, 2, 1, 1)

        self.colorBtn = QPushButton(self.centralwidget)
        self.colorBtn.setObjectName(u"colorBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.colorBtn.sizePolicy().hasHeightForWidth())
        self.colorBtn.setSizePolicy(sizePolicy2)
        self.colorBtn.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.colorBtn, 2, 1, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 200, 61, 40))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 700 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"border-color: rgb(0, 0, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.frame, 1, 0, 1, 3)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1298, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.nameBtn.clicked.connect(MainWindow.changeName)
        self.colorBtn.clicked.connect(MainWindow.changeColor)
        self.startBtn.clicked.connect(MainWindow.Start)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ub0a8\uc740 \uc2dc\uac04 : ", None))
        self.nameBtn.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub984 \ubcc0\uacbd", None))
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.colorBtn.setText(QCoreApplication.translate("MainWindow", u"\ubc30\uacbd \uc0c9\uc0c1 \ubcc0\uacbd", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uae40\uc2b9\ubc30", None))
    # retranslateUi

