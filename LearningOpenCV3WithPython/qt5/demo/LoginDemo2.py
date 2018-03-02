#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 16:35
# @Author  : CycloneBoy
# @Site    : 
# @File    : LoginDemo2.py
# @Software: PyCharm

from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class LoginDemo(QDialog):
    """login window"""


    def __init__(self, *args):
        super(LoginDemo, self).__init__(*args)
        loadUi("Login.ui",self) # 通过uic的loadUi加载UI

        self.labelInfo.hide()

        # 连接信号与槽
        self.pushButtonOk.clicked.connect(self.slotLogin)
        self.pushButtonCanel.clicked.connect(self.slotCancle)

    def slotLogin(self):
        if self.lineEditUsername.text() != "admin" or self.lineEditPassword.text() != "123456":
            self.labelInfo.show()
            self.labelInfo.setText("用户名或者密码错误")
        else:
            self.accept()

    def slotCancle(self):
        self.reject()
