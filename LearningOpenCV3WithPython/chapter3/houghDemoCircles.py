#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 21:16
# @Author  : CycloneBoy
# @Site    : 
# @File    : houghDemoCircles.py
# @Software: PyCharm

import cv2
import numpy as np

planets = cv2.imread("../images/planet_glow.jpg")
gray_img = cv2.cvtColor(planets,cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(gray_img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,120,
                            param1=100,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(planets,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(planets,(i[0],i[1]),2,(0,0,255),3)

cv2.imwrite("../data/planets_circles.jpg",planets)
cv2.imshow("HoughCirlces",planets)
cv2.waitKey()
cv2.destroyAllWindows()