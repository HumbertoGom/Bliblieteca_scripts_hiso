# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'work_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 401, 301))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Label1 = QLabel(self.gridLayoutWidget)
        self.Label1.setObjectName(u"Label1")
        font = QFont()
        font.setPointSize(40)
        self.Label1.setFont(font)

        self.gridLayout.addWidget(self.Label1, 0, 0, 1, 1)

        self.Label2 = QLabel(self.gridLayoutWidget)
        self.Label2.setObjectName(u"Label2")
        self.Label2.setFont(font)

        self.gridLayout.addWidget(self.Label2, 0, 1, 1, 1)

        self.Button1 = QPushButton(self.gridLayoutWidget)
        self.Button1.setObjectName(u"Button1")

        self.gridLayout.addWidget(self.Button1, 1, 0, 1, 1)

        self.Button2 = QPushButton(self.gridLayoutWidget)
        self.Button2.setObjectName(u"Button2")

        self.gridLayout.addWidget(self.Button2, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Label1.setText(QCoreApplication.translate("Form", u"L1", None))
        self.Label2.setText(QCoreApplication.translate("Form", u"L2", None))
        self.Button1.setText(QCoreApplication.translate("Form", u"B1", None))
        self.Button2.setText(QCoreApplication.translate("Form", u"B2", None))
    # retranslateUi

