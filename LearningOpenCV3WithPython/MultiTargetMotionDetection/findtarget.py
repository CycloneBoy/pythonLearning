#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 22:15
# @Author  : CycloneBoy
# @Site    : 
# @File    : findtarget.py
# @Software: PyCharm

class FindTarget:
    '''发现的目标类'''

    def __init__(self, x , y , w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    # 比较两个框是否是差不多一个 and (abs(self.w - other.w) + abs(self.h - other.h) < 200 )
    def compare(self, other):
        if (((abs(self.x  - other.x ))**2 + (abs(self.y - other.y))**2) < 200) :
            return True
        else:
            return False

    def display(self):
        print("findTarget",self.x,self.y , self.w, self.h)
