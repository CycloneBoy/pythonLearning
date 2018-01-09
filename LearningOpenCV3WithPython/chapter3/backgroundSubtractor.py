#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 15:41
# @Author  : CycloneBoy
# @Site    : 
# @File    : backgroundSubtractor.py
# @Software: PyCharm

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

mog = cv2.createBackgroundSubtractorMOG2()

while True:
    ret ,frame = cap.read()
    fgmask = mog.apply(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(80 ) & 0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()