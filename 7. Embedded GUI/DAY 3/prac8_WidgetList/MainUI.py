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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(474, 346)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pb1 = QProgressBar(self.centralwidget)
        self.pb1.setObjectName(u"pb1")
        self.pb1.setValue(24)

        self.verticalLayout.addWidget(self.pb1)

        self.pb2 = QProgressBar(self.centralwidget)
        self.pb2.setObjectName(u"pb2")
        self.pb2.setValue(24)

        self.verticalLayout.addWidget(self.pb2)

        self.pb3 = QProgressBar(self.centralwidget)
        self.pb3.setObjectName(u"pb3")
        self.pb3.setValue(24)

        self.verticalLayout.addWidget(self.pb3)

        self.pb4 = QProgressBar(self.centralwidget)
        self.pb4.setObjectName(u"pb4")
        self.pb4.setValue(24)

        self.verticalLayout.addWidget(self.pb4)

        self.pb5 = QProgressBar(self.centralwidget)
        self.pb5.setObjectName(u"pb5")
        self.pb5.setValue(24)

        self.verticalLayout.addWidget(self.pb5)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.btn = QPushButton(self.centralwidget)
        self.btn.setObjectName(u"btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn.sizePolicy().hasHeightForWidth())
        self.btn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 474, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn.clicked.connect(MainWindow.go)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn.setText(QCoreApplication.translate("MainWindow", u"Download", None))
    # retranslateUi