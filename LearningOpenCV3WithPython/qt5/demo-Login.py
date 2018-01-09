#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 16:29
# @Author  : CycloneBoy
# @Site    : 
# @File    : demo-Login.py
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import QApplication

from LearningOpenCV3WithPython.qt5.LoginDemo2 import LoginDemo

app = QApplication(sys.argv)
login = LoginDemo()

if login.exec():
    print("登录成功")
else:
    print("登录失败")

sys.exit(app.exec())