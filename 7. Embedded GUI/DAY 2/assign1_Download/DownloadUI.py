# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DownloadUI.ui'
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
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 1070)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 90, 531, 471))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.progressBar_2 = QProgressBar(self.gridLayoutWidget)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(0)

        self.gridLayout.addWidget(self.progressBar_2, 1, 0, 1, 1)

        self.progressBar = QProgressBar(self.gridLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 1)

        self.progressBar_3 = QProgressBar(self.gridLayoutWidget)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setValue(0)

        self.gridLayout.addWidget(self.progressBar_3, 2, 0, 1, 1)

        self.progressBar_4 = QProgressBar(self.gridLayoutWidget)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setValue(0)

        self.gridLayout.addWidget(self.progressBar_4, 3, 0, 1, 1)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(580, 241, 131, 161))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn1 = QPushButton(self.verticalLayoutWidget)
        self.btn1.setObjectName(u"btn1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.btn1)

        self.btn2 = QPushButton(self.verticalLayoutWidget)
        self.btn2.setObjectName(u"btn2")
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.btn2)

        self.btn3 = QPushButton(self.verticalLayoutWidget)
        self.btn3.setObjectName(u"btn3")
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.btn3)

        self.btn4 = QPushButton(self.verticalLayoutWidget)
        self.btn4.setObjectName(u"btn4")
        sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.btn4)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 10, 691, 73))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
"font: 700 18pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 0, 0);")
        self.label.setTextFormat(Qt.PlainText)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.btn1, self.btn2)

        self.retranslateUi(MainWindow)
        self.btn4.clicked.connect(MainWindow.click4)
        self.btn3.clicked.connect(MainWindow.click3)
        self.btn1.clicked.connect(MainWindow.click1)
        self.btn2.clicked.connect(MainWindow.click2)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"Download 1", None))
        self.btn2.setText(QCoreApplication.translate("MainWindow", u"Download 2", None))
        self.btn3.setText(QCoreApplication.translate("MainWindow", u"Download 3", None))
        self.btn4.setText(QCoreApplication.translate("MainWindow", u"Download 4", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ubd88\ubc95 \ub2e4\uc6b4\ub85c\ub4dc", None))
    # retranslateUi

