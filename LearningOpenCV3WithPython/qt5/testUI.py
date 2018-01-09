# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(732, 484)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(140, 80, 120, 80))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(30, 100, 104, 71))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(310, 100, 371, 321))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 10, 104, 71))
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.toolButton = QtWidgets.QToolButton(self.tab_2)
        self.toolButton.setGeometry(QtCore.QRect(100, 100, 121, 61))
        self.toolButton.setObjectName("toolButton")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.toolButton.setText(_translate("Form", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))

