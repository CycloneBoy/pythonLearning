#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 20:58
# @Author  : CycloneBoy
# @Site    : 
# @File    : SingalAndSlot-3.py
# @Software: PyCharm

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class SinClass(QObject):

    sin1 = pyqtSignal()

    sin2 = pyqtSignal(int)

    def __init__(self,parent=None):
        super(SinClass,self).__init__(parent)

        self.sin1.connect(self.sin1Call)
        self.sin2.connect(self.sin2Call)

        self.sin2.connect(self.sin1)

        self.sin1.emit()
        self.sin2.emit(1)

        self.sin1.disconnect(self.sin1Call)
        self.sin2.disconnect(self.sin2Call)
        self.sin2.disconnect(self.sin1)

        self.sin1.connect(self.sin1Call)
        self.sin2.connect(self.sin1Call)

        self.sin1.emit()
        self.sin2.emit(2)

    def sin1Call(self):
        print("sin1 emit")

    def sin2Call(self):
        print("sin2 emit")

sin = SinClass()

