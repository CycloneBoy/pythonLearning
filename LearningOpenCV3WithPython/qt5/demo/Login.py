# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(605, 394)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 99, 211, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelUsername = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelUsername.setObjectName("labelUsername")
        self.horizontalLayout.addWidget(self.labelUsername)
        self.lineEditUsername = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.horizontalLayout.addWidget(self.lineEditUsername)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(110, 130, 211, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelUsername_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.labelUsername_2.setObjectName("labelUsername_2")
        self.horizontalLayout_2.addWidget(self.labelUsername_2)
        self.lineEditPassword = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.horizontalLayout_2.addWidget(self.lineEditPassword)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(110, 160, 211, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelInfo = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.labelInfo.setText("")
        self.labelInfo.setObjectName("labelInfo")
        self.horizontalLayout_3.addWidget(self.labelInfo)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(110, 190, 211, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonOk = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.horizontalLayout_4.addWidget(self.pushButtonOk)
        self.pushButtonCanel = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButtonCanel.setObjectName("pushButtonCanel")
        self.horizontalLayout_4.addWidget(self.pushButtonCanel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelUsername.setText(_translate("Dialog", "用户名："))
        self.labelUsername_2.setText(_translate("Dialog", "密  码："))
        self.pushButtonOk.setText(_translate("Dialog", "确定"))
        self.pushButtonCanel.setText(_translate("Dialog", "取消"))

