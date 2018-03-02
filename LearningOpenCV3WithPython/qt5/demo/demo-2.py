#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 14:20
# @Author  : CycloneBoy
# @Site    : 
# @File    : demo-2.py
# @Software: PyCharm

import sys
from PyQt5 import QtCore ,QtWidgets

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(400,100)
widget.setWindowTitle("This is a demo for PyQt Widget.")
widget.show()

exit(app.exec_())
