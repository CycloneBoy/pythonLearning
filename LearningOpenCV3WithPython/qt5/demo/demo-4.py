#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 15:15
# @Author  : CycloneBoy
# @Site    : 
# @File    : demo-4.py
# @Software: PyCharm
import sys

from PyQt5 import QtWidgets

from LearningOpenCV3WithPython.qt5.demo import testUI

app = QtWidgets.QApplication(sys.argv)
qUI = testUI.Ui_Form()

widget = QtWidgets.QWidget()
widget.resize(400,100)

qUI.setupUi(widget)

widget.show()

exit(app.exec_())