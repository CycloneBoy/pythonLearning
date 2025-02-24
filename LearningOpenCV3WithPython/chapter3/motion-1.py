#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 15:18
# @Author  : CycloneBoy
# @Site    : 
# @File    : motion-1.py
# @Software: PyCharm
import cv2
import numpy as np

camera = cv2.VideoCapture(0)

es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,4))
kernel = np.ones((5,5),np.uint8)
background = None

while(True):
    ret,frame = camera.read()
    if background is None:
        background = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        background = cv2.GaussianBlur(background,(21,21),0)
        continue

    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame,(21,21),0)

    diff = cv2.absdiff(background,gray_frame)
    diff = cv2.threshold(diff,25,255,cv2.THRESH_BINARY)[1]
    diff = cv2.dilate(diff,es,iterations= 2)
    image,cnts,hierarchy = cv2.findContours(diff.copy(),
                        cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        if cv2.contourArea(c) <1500:
            continue
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("contours",frame)
    cv2.imshow("diff",diff)
    if cv2.waitKey(80 ) & 0xff == ord("q"):
        break

cv2.destroyAllWindows()
camera.release()