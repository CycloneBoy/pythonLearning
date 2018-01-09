#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 20:30
# @Author  : CycloneBoy
# @Site    : 
# @File    : singnalAndSlot.py
# @Software: PyCharm

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def sinTest():
    btn.setText("按钮文本改变")

app = QApplication([])

main = QWidget()
main.resize(200,100)
btn = QPushButton("按钮文本",main)
btn.clicked.connect(sinTest)
main.show()

app.exec_()
