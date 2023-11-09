# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1306, 520)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.cannyBtn = QPushButton(self.centralwidget)
        self.cannyBtn.setObjectName(u"cannyBtn")

        self.gridLayout.addWidget(self.cannyBtn, 2, 4, 1, 1)

        self.grayBtn = QPushButton(self.centralwidget)
        self.grayBtn.setObjectName(u"grayBtn")

        self.gridLayout.addWidget(self.grayBtn, 2, 1, 1, 1)

        self.threshBtn = QPushButton(self.centralwidget)
        self.threshBtn.setObjectName(u"threshBtn")

        self.gridLayout.addWidget(self.threshBtn, 2, 3, 1, 1)

        self.blurBtn = QPushButton(self.centralwidget)
        self.blurBtn.setObjectName(u"blurBtn")

        self.gridLayout.addWidget(self.blurBtn, 2, 0, 1, 1)

        self.morphBtn = QPushButton(self.centralwidget)
        self.morphBtn.setObjectName(u"morphBtn")

        self.gridLayout.addWidget(self.morphBtn, 2, 2, 1, 1)

        self.clearBtn = QPushButton(self.centralwidget)
        self.clearBtn.setObjectName(u"clearBtn")

        self.gridLayout.addWidget(self.clearBtn, 2, 5, 1, 1)

        self.origin_lbl = QLabel(self.centralwidget)
        self.origin_lbl.setObjectName(u"origin_lbl")
        self.origin_lbl.setMinimumSize(QSize(640, 427))

        self.gridLayout.addWidget(self.origin_lbl, 0, 0, 1, 3)

        self.openCV_lbl = QLabel(self.centralwidget)
        self.openCV_lbl.setObjectName(u"openCV_lbl")
        self.openCV_lbl.setMinimumSize(QSize(640, 427))
        self.openCV_lbl.setStyleSheet(u"background-color: rgb(255, 227, 84);")

        self.gridLayout.addWidget(self.openCV_lbl, 0, 3, 1, 3)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1306, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.blurBtn.clicked.connect(MainWindow.blur)
        self.grayBtn.clicked.connect(MainWindow.gray)
        self.morphBtn.clicked.connect(MainWindow.morpho)
        self.threshBtn.clicked.connect(MainWindow.thresh)
        self.cannyBtn.clicked.connect(MainWindow.canny)
        self.clearBtn.clicked.connect(MainWindow.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cannyBtn.setText(QCoreApplication.translate("MainWindow", u"Canny", None))
        self.grayBtn.setText(QCoreApplication.translate("MainWindow", u"Gray", None))
        self.threshBtn.setText(QCoreApplication.translate("MainWindow", u"threshold", None))
        self.blurBtn.setText(QCoreApplication.translate("MainWindow", u"Blur", None))
        self.morphBtn.setText(QCoreApplication.translate("MainWindow", u"Morphology", None))
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.origin_lbl.setText("")
        self.openCV_lbl.setText("")
    # retranslateUi