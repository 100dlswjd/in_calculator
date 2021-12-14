# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_in_calculator(object):
    def setupUi(self, in_calculator):
        if not in_calculator.objectName():
            in_calculator.setObjectName(u"in_calculator")
        in_calculator.resize(260, 310)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(in_calculator.sizePolicy().hasHeightForWidth())
        in_calculator.setSizePolicy(sizePolicy)
        in_calculator.setMinimumSize(QSize(260, 310))
        in_calculator.setMaximumSize(QSize(260, 310))
        self.centralwidget = QWidget(in_calculator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_zero = QPushButton(self.centralwidget)
        self.btn_zero.setObjectName(u"btn_zero")
        self.btn_zero.setGeometry(QRect(10, 240, 121, 41))
        self.btn_one = QPushButton(self.centralwidget)
        self.btn_one.setObjectName(u"btn_one")
        self.btn_one.setGeometry(QRect(10, 200, 61, 41))
        self.btn_two = QPushButton(self.centralwidget)
        self.btn_two.setObjectName(u"btn_two")
        self.btn_two.setGeometry(QRect(70, 200, 61, 41))
        self.btn_three = QPushButton(self.centralwidget)
        self.btn_three.setObjectName(u"btn_three")
        self.btn_three.setGeometry(QRect(130, 200, 61, 41))
        self.btn_four = QPushButton(self.centralwidget)
        self.btn_four.setObjectName(u"btn_four")
        self.btn_four.setGeometry(QRect(10, 160, 61, 41))
        self.btn_five = QPushButton(self.centralwidget)
        self.btn_five.setObjectName(u"btn_five")
        self.btn_five.setGeometry(QRect(70, 160, 61, 41))
        self.btn_six = QPushButton(self.centralwidget)
        self.btn_six.setObjectName(u"btn_six")
        self.btn_six.setGeometry(QRect(130, 160, 61, 41))
        self.btn_seven = QPushButton(self.centralwidget)
        self.btn_seven.setObjectName(u"btn_seven")
        self.btn_seven.setGeometry(QRect(10, 120, 61, 41))
        self.btn_eight = QPushButton(self.centralwidget)
        self.btn_eight.setObjectName(u"btn_eight")
        self.btn_eight.setGeometry(QRect(70, 120, 61, 41))
        self.btn_nine = QPushButton(self.centralwidget)
        self.btn_nine.setObjectName(u"btn_nine")
        self.btn_nine.setGeometry(QRect(130, 120, 61, 41))
        self.btn_jeom = QPushButton(self.centralwidget)
        self.btn_jeom.setObjectName(u"btn_jeom")
        self.btn_jeom.setGeometry(QRect(130, 240, 61, 41))
        self.label_result = QLabel(self.centralwidget)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setGeometry(QRect(10, 40, 240, 30))
        self.label_result.setMaximumSize(QSize(240, 30))
        self.label_result.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_result.setIndent(-1)
        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(190, 160, 61, 41))
        self.btn_Cancel = QPushButton(self.centralwidget)
        self.btn_Cancel.setObjectName(u"btn_Cancel")
        self.btn_Cancel.setGeometry(QRect(10, 80, 61, 41))
        self.btn_div = QPushButton(self.centralwidget)
        self.btn_div.setObjectName(u"btn_div")
        self.btn_div.setGeometry(QRect(70, 80, 61, 41))
        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        self.btn_plus.setGeometry(QRect(130, 80, 61, 41))
        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        self.btn_sub.setGeometry(QRect(190, 80, 61, 41))
        self.btn_mul = QPushButton(self.centralwidget)
        self.btn_mul.setObjectName(u"btn_mul")
        self.btn_mul.setGeometry(QRect(190, 120, 61, 41))
        self.btn_enter = QPushButton(self.centralwidget)
        self.btn_enter.setObjectName(u"btn_enter")
        self.btn_enter.setGeometry(QRect(190, 200, 61, 81))
        self.label_prevresult = QLabel(self.centralwidget)
        self.label_prevresult.setObjectName(u"label_prevresult")
        self.label_prevresult.setGeometry(QRect(10, 10, 240, 30))
        self.label_prevresult.setMaximumSize(QSize(240, 30))
        self.label_prevresult.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_prevresult.setIndent(-1)
        in_calculator.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(in_calculator)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 260, 22))
        in_calculator.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(in_calculator)
        self.statusbar.setObjectName(u"statusbar")
        in_calculator.setStatusBar(self.statusbar)

        self.retranslateUi(in_calculator)

        QMetaObject.connectSlotsByName(in_calculator)
    # setupUi

    def retranslateUi(self, in_calculator):
        in_calculator.setWindowTitle(QCoreApplication.translate("in_calculator", u"\uc778\uc0b0\uae30", None))
        self.btn_zero.setText(QCoreApplication.translate("in_calculator", u"0", None))
        self.btn_one.setText(QCoreApplication.translate("in_calculator", u"1", None))
        self.btn_two.setText(QCoreApplication.translate("in_calculator", u"2", None))
        self.btn_three.setText(QCoreApplication.translate("in_calculator", u"3", None))
        self.btn_four.setText(QCoreApplication.translate("in_calculator", u"4", None))
        self.btn_five.setText(QCoreApplication.translate("in_calculator", u"5", None))
        self.btn_six.setText(QCoreApplication.translate("in_calculator", u"6", None))
        self.btn_seven.setText(QCoreApplication.translate("in_calculator", u"7", None))
        self.btn_eight.setText(QCoreApplication.translate("in_calculator", u"8", None))
        self.btn_nine.setText(QCoreApplication.translate("in_calculator", u"9", None))
        self.btn_jeom.setText(QCoreApplication.translate("in_calculator", u".", None))
        self.label_result.setText(QCoreApplication.translate("in_calculator", u"<html><head/><body><p><span style=\" font-size:16pt;\">\uacb0\uacfc</span></p></body></html>", None))
        self.btn_delete.setText(QCoreApplication.translate("in_calculator", u"\uc9c0\uc6b0\uae30", None))
        self.btn_Cancel.setText(QCoreApplication.translate("in_calculator", u"C", None))
        self.btn_div.setText(QCoreApplication.translate("in_calculator", u"/", None))
        self.btn_plus.setText(QCoreApplication.translate("in_calculator", u"+", None))
        self.btn_sub.setText(QCoreApplication.translate("in_calculator", u"-", None))
        self.btn_mul.setText(QCoreApplication.translate("in_calculator", u"*", None))
        self.btn_enter.setText(QCoreApplication.translate("in_calculator", u"Enter", None))
        self.label_prevresult.setText(QCoreApplication.translate("in_calculator", u"<html><head/><body><p>\uc774\uc804\uacb0\uacfc</p></body></html>", None))
    # retranslateUi

