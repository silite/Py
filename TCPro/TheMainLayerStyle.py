# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Pro\Py\TCPro\1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2688, 1740)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(2580, 8, 101, 61))
        self.pushButton.setText("")
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(2481, 8, 101, 61))
        self.pushButton_2.setText("")
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(2382, 8, 101, 61))
        self.pushButton_3.setText("")
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.line = QtWidgets.QFrame(Form)
        self.line.setEnabled(True)
        self.line.setGeometry(QtCore.QRect(5, 65, 2676, 10))
        self.line.setSizeIncrement(QtCore.QSize(20, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        file = QtCore.QFile('css.css')
        file.open(QtCore.QFile.ReadOnly)
        styleSheet = file.readAll()
        styleSheet = str(styleSheet, encoding='utf8')
        self.setStyleSheet(styleSheet)
