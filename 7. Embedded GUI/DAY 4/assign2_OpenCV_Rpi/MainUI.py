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
        MainWindow.resize(1259, 749)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.Btn2 = QPushButton(self.centralwidget)
        self.Btn2.setObjectName(u"Btn2")
        self.Btn2.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 24pt \"\ub9d1\uc740 \uace0\ub515\";")

        self.gridLayout.addWidget(self.Btn2, 2, 0, 1, 1)

        self.Btn1 = QPushButton(self.centralwidget)
        self.Btn1.setObjectName(u"Btn1")
        self.Btn1.setStyleSheet(u"font: 700 24pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 255, 0);")

        self.gridLayout.addWidget(self.Btn1, 1, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1259, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Btn1.clicked.connect(MainWindow.play)
        self.Btn2.clicked.connect(MainWindow.mode)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn2.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.Btn1.setText(QCoreApplication.translate("MainWindow", u"Play", None))
    # retranslateUi

