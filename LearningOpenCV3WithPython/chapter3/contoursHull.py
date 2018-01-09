#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 20:57
# @Author  : CycloneBoy
# @Site    : 
# @File    : contoursHull.py
# @Software: PyCharm

import cv2
import numpy as np

img = cv2.pyrDown(cv2.imread("../images/hammer.jpg"),cv2.IMREAD_UNCHANGED)


ret,thresh = cv2.threshold(cv2.cvtColor(img.copy(),
                cv2.COLOR_BGR2GRAY),127,255,cv2.THRESH_BINARY)
black = cv2.cvtColor(np.zeros((img.shape[1],img.shape[0]),dtype=np.uint8),cv2.COLOR_GRAY2BGR)

image ,contours ,hierarchy = cv2.findContours(thresh,
                    cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    epsion = 0.01 * cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsion,True)
    hull = cv2.convexHull(cnt)

    cv2.drawContours(black,[cnt],-1,(0,255,0),2)
    cv2.drawContours(black, [approx], -1, (255, 255, 0), 2)
    cv2.drawContours(black,[hull],-1,(0,0,255),2)


cv2.imshow("hull",black)
cv2.imwrite("../data/hammer-hull.png",black)
cv2.waitKey()
cv2.destroyAllWindows()