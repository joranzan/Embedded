# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LCD_DialUI.ui'
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
from PySide6.QtWidgets import (QApplication, QDial, QGridLayout, QLCDNumber,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1195, 820)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lcdNumber, 1, 0, 1, 2)

        self.onBtn = QPushButton(self.centralwidget)
        self.onBtn.setObjectName(u"onBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onBtn.sizePolicy().hasHeightForWidth())
        self.onBtn.setSizePolicy(sizePolicy)
        self.onBtn.setStyleSheet(u"background-color: rgb(0, 255, 0);\n"
"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.onBtn, 0, 0, 1, 1)

        self.offBtn = QPushButton(self.centralwidget)
        self.offBtn.setObjectName(u"offBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.offBtn.sizePolicy().hasHeightForWidth())
        self.offBtn.setSizePolicy(sizePolicy1)
        self.offBtn.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";")

        self.gridLayout.addWidget(self.offBtn, 0, 1, 1, 1)

        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")
        self.dial.setStyleSheet(u"background-color: rgb(170, 255, 255);")

        self.gridLayout.addWidget(self.dial, 3, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1195, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.onBtn.clicked.connect(MainWindow.on_click)
        self.offBtn.clicked.connect(MainWindow.off_click)
        self.dial.valueChanged.connect(MainWindow.valueChange)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.onBtn.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.offBtn.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
    # retranslateUi

