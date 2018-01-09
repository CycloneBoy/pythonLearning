#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 20:17
# @Author  : CycloneBoy
# @Site    : 
# @File    : cannyDemo.py
# @Software: PyCharm

import cv2
import  numpy as np

img = cv2.imread("../images/statue_small.jpg",0)
cv2.imwrite("../data/canny.jpg",cv2.Canny(img,200,300))
cv2.imshow("canny",cv2.imread("../data/canny.jpg"))
cv2.waitKey()
cv2.destroyAllWindows()
