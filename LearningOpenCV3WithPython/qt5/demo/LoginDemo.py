#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 16:20
# @Author  : CycloneBoy
# @Site    : 
# @File    : LoginDemo.py
# @Software: PyCharm

from PyQt5.QtWidgets import QDialog

from LearningOpenCV3WithPython.qt5.demo.Login import Ui_Dialog


class LoginDemo(QDialog):
    """login window"""

    def __init__(self,parent = None):
        super(LoginDemo,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.labelInfo.hide()

        # 连接信号与槽
        self.ui.pushButtonOk.clicked.connect(self.slotLogin)

        self.ui.pushButtonCanel.clicked.connect(self.slotCancle)

    def slotLogin(self):
        if self.ui.lineEditUsername.text() != "admin" or self.ui.lineEditPassword.text() != "123456" :
            self.ui.labelInfo.show()
            self.ui.labelInfo.setText("用户名或者密码错误")
        else:
            self.accept()

    def slotCancle(self):
        self.reject()





