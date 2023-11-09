# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUI.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.Btn2 = QPushButton(self.centralwidget)
        self.Btn2.setObjectName(u"Btn2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn2.sizePolicy().hasHeightForWidth())
        self.Btn2.setSizePolicy(sizePolicy)
        self.Btn2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 16pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color: rgb(255, 170, 255);")

        self.gridLayout.addWidget(self.Btn2, 1, 1, 1, 1)

        self.Btn3 = QPushButton(self.centralwidget)
        self.Btn3.setObjectName(u"Btn3")
        sizePolicy.setHeightForWidth(self.Btn3.sizePolicy().hasHeightForWidth())
        self.Btn3.setSizePolicy(sizePolicy)
        self.Btn3.setStyleSheet(u"font: 700 16pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.Btn3, 1, 2, 1, 1)

        self.Btn1 = QPushButton(self.centralwidget)
        self.Btn1.setObjectName(u"Btn1")
        sizePolicy.setHeightForWidth(self.Btn1.sizePolicy().hasHeightForWidth())
        self.Btn1.setSizePolicy(sizePolicy)
        self.Btn1.setStyleSheet(u"font: 700 16pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.Btn1, 1, 0, 1, 1)

        self.lay = QGridLayout()
        self.lay.setObjectName(u"lay")

        self.gridLayout.addLayout(self.lay, 0, 0, 1, 3)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Btn1.clicked.connect(MainWindow.chart1)
        self.Btn2.clicked.connect(MainWindow.chart2)
        self.Btn3.clicked.connect(MainWindow.chart3)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn2.setText(QCoreApplication.translate("MainWindow", u"Chart2", None))
        self.Btn3.setText(QCoreApplication.translate("MainWindow", u"Chart3", None))
        self.Btn1.setText(QCoreApplication.translate("MainWindow", u"Chart1", None))
    # retranslateUi

