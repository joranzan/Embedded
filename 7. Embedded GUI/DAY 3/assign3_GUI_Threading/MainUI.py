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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(753, 632)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 90, 531, 471))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.progressBar2 = QProgressBar(self.gridLayoutWidget)
        self.progressBar2.setObjectName(u"progressBar2")
        self.progressBar2.setValue(0)

        self.gridLayout.addWidget(self.progressBar2, 1, 0, 1, 1)

        self.progressBar1 = QProgressBar(self.gridLayoutWidget)
        self.progressBar1.setObjectName(u"progressBar1")
        self.progressBar1.setValue(0)

        self.gridLayout.addWidget(self.progressBar1, 0, 0, 1, 1)

        self.progressBar4 = QProgressBar(self.gridLayoutWidget)
        self.progressBar4.setObjectName(u"progressBar4")
        self.progressBar4.setValue(0)

        self.gridLayout.addWidget(self.progressBar4, 3, 0, 1, 1)

        self.progressBar3 = QProgressBar(self.gridLayoutWidget)
        self.progressBar3.setObjectName(u"progressBar3")
        self.progressBar3.setValue(0)

        self.gridLayout.addWidget(self.progressBar3, 2, 0, 1, 1)

        self.progressBar5 = QProgressBar(self.gridLayoutWidget)
        self.progressBar5.setObjectName(u"progressBar5")
        self.progressBar5.setValue(0)

        self.gridLayout.addWidget(self.progressBar5, 4, 0, 1, 1)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 10, 691, 73))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
"font: 700 20pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 0, 0);")
        self.label.setTextFormat(Qt.PlainText)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.Btn = QPushButton(self.centralwidget)
        self.Btn.setObjectName(u"Btn")
        self.Btn.setGeometry(QRect(583, 255, 129, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn.sizePolicy().hasHeightForWidth())
        self.Btn.setSizePolicy(sizePolicy)
        self.Btn.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 255, 255);")
        self.Reset = QPushButton(self.centralwidget)
        self.Reset.setObjectName(u"Reset")
        self.Reset.setGeometry(QRect(580, 421, 129, 61))
        sizePolicy.setHeightForWidth(self.Reset.sizePolicy().hasHeightForWidth())
        self.Reset.setSizePolicy(sizePolicy)
        self.Reset.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 753, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Btn.clicked.connect(MainWindow.click4)
        self.Reset.clicked.connect(MainWindow.reset)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ubd88\ubc95 \ub2e4\uc6b4\ub85c\ub4dc", None))
        self.Btn.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.Reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi

