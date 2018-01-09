#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 14:39
# @Author  : CycloneBoy
# @Site    : 
# @File    : demo-3.py
# @Software: PyCharm


import sys
from PyQt5 import QtCore ,QtGui,QtWidgets

from LearningOpenCV3WithPython.qt5 import demo

app = QtWidgets.QApplication(sys.argv)
qUI = demo.Ui_Form()

widget = QtWidgets.QWidget()
widget.resize(400,100)

qUI.setupUi(widget)

widget.show()

exit(app.exec_())
