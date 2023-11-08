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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Bar = QProgressBar(self.centralwidget)
        self.Bar.setObjectName(u"Bar")
        self.Bar.setGeometry(QRect(60, 140, 434, 150))
        self.Bar.setValue(0)
        self.goBtn = QPushButton(self.centralwidget)
        self.goBtn.setObjectName(u"goBtn")
        self.goBtn.setGeometry(QRect(60, 320, 117, 50))
        self.pauseBtn = QPushButton(self.centralwidget)
        self.pauseBtn.setObjectName(u"pauseBtn")
        self.pauseBtn.setGeometry(QRect(200, 320, 117, 50))
        self.resetBtn = QPushButton(self.centralwidget)
        self.resetBtn.setObjectName(u"resetBtn")
        self.resetBtn.setGeometry(QRect(340, 320, 117, 50))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.goBtn.clicked.connect(MainWindow.goclick)
        self.pauseBtn.clicked.connect(MainWindow.pauseclick)
        self.resetBtn.clicked.connect(MainWindow.resetclick)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.goBtn.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.pauseBtn.setText(QCoreApplication.translate("MainWindow", u"PAUSE", None))
        self.resetBtn.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
    # retranslateUi

