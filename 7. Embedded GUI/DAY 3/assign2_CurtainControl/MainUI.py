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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(592, 577)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(55, 50, 291, 453))
        self.progressBar.setValue(24)
        self.upBtn = QPushButton(self.centralwidget)
        self.upBtn.setObjectName(u"upBtn")
        self.upBtn.setGeometry(QRect(368, 49, 141, 111))
        self.upBtn.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 18pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.downBtn = QPushButton(self.centralwidget)
        self.downBtn.setObjectName(u"downBtn")
        self.downBtn.setGeometry(QRect(368, 190, 141, 111))
        self.downBtn.setStyleSheet(u"background-color: rgb(255, 170, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 18pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.Description = QLabel(self.centralwidget)
        self.Description.setObjectName(u"Description")
        self.Description.setGeometry(QRect(372, 340, 134, 31))
        self.Description.setStyleSheet(u"font: 700 14pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(0, 0, 0);")
        self.Description.setAlignment(Qt.AlignCenter)
        self.Slider = QSlider(self.centralwidget)
        self.Slider.setObjectName(u"Slider")
        self.Slider.setGeometry(QRect(369, 391, 136, 41))
        self.Slider.setOrientation(Qt.Horizontal)
        self.SpeedLabel = QLabel(self.centralwidget)
        self.SpeedLabel.setObjectName(u"SpeedLabel")
        self.SpeedLabel.setGeometry(QRect(372, 455, 131, 31))
        self.SpeedLabel.setStyleSheet(u"font: 700 12pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 592, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.upBtn.pressed.connect(MainWindow.upclick)
        self.downBtn.pressed.connect(MainWindow.downclick)
        self.upBtn.released.connect(MainWindow.upstop)
        self.downBtn.released.connect(MainWindow.downstop)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.upBtn.setText(QCoreApplication.translate("MainWindow", u"UP", None))
        self.downBtn.setText(QCoreApplication.translate("MainWindow", u"DOWN", None))
        self.Description.setText(QCoreApplication.translate("MainWindow", u"\ubaa8\ud130 \uc18d\ub3c4 \uc81c\uc5b4", None))
        self.SpeedLabel.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac \uc18d\ub3c4 : ", None))
    # retranslateUi

