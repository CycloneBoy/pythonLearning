#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 20:34
# @Author  : CycloneBoy
# @Site    : 
# @File    : singnalAndSlot-2.py
# @Software: PyCharm
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class SinClass(QObject):

    sin1 = pyqtSignal()
    sin2 = pyqtSignal(int)
    sin3 = pyqtSignal(int,str)
    sin4 = pyqtSignal(list)
    sin5 = pyqtSignal(dict)
    sin6 = pyqtSignal([int,str],[str])

    def __init__(self,parent = None):
        super(SinClass,self).__init__(parent)

        self.sin1.connect(self.sin1Call)
        self.sin2.connect(self.sin2Call)
        self.sin3.connect(self.sin3Call)
        self.sin4.connect(self.sin4Call)
        self.sin5.connect(self.sin5Call)
        self.sin6[int,str].connect(self.sin6Call)
        self.sin6[str].connect(self.sin6CallOverload)

        self.sin1.emit()
        self.sin2.emit(1)
        self.sin3.emit(1,"text")
        self.sin4.emit([1,2,3,4])
        self.sin5.emit({"name":"cycloneboy","age":25})
        self.sin6[int,str].emit(1,"text")
        self.sin6[str].emit("text")

    def sin1Call(self):
        print("sin1 emit")

    def sin2Call(self,val):
        print("sin2 emit,value:",val)

    def sin3Call(self,val,text):
        print("sin3 emit,value:",val,text)

    def sin4Call(self,val):
        print("sin4 emit,value:",val)

    def sin5Call(self,val):
         print("sin5 emit,value:",val)

    def sin6Call(self,val):
        print("sin6 emit,value:",val)

    def sin6CallOverload(self,val):
        print("sin6 overload emit,value:",val)

sin = SinClass()