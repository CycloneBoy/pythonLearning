#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 21:28
# @Author  : CycloneBoy
# @Site    :
# @File    : motionDetectorDemo.py
# @Software: PyCharm

import sys
import cv2
import time
import numpy as np
from PIL import Image

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *

from PyQt5.QtWidgets import QFileDialog
from LearningOpenCV3WithPython.circleDetection.mainwindow import Ui_MainWindow


class MyWindow(QMainWindow):
    """加载主窗口 """

    def __init__(self, *args):
        self.video = "data/vtest.avi"
        self.urlVideo = "http://192.168.2.192:8080/?action=stream"
        # self._camera = cv2.VideoCapture(self.video)  # 参数0表示第一个摄像头
        self._camera = cv2.VideoCapture(0)  # 参数0表示第一个摄像头
        # self._camera = cv2.VideoCapture(self.urlVideo)
        # 判断视频是否打开
        if (self._camera.isOpened()):
            print('Open')
        else:
            print('摄像头未打开')

        self._vedioWidth = int(self._camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        self._vedioHeight = int(self._camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self._frame1 = None
        self._frame2 = None
        self._grayImage1 = None
        self._grayImage2 = None
        self._thresholdImage = None
        self._qImage = None
        self._differenceImage = None

        self._SENSITIVITY_VALUE = 60
        self._BLUR_SIZE = 10
        self._motionDetected = False
        self._debugMode = False
        self._bsknn = cv2.createBackgroundSubtractorKNN(detectShadows=True)
        self._isFindCircle = True

        print("vedio size", self._vedioWidth, self._vedioWidth)

        # 加载主窗口
        super(MyWindow, self).__init__(*args)

        # loadUi("mainwindow.ui", self)  # 通过uic的loadUi加载UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.label_ShowImg.resize(self._vedioWidth, self._vedioHeight)
        # self.ui.label_ShowImg.resize(self._vedioWidth, self._vedioHeight)

        self.image = QImage()
        self.image.load("test1.jpg")
        self.ui.label_ShowImg.setPixmap(QPixmap.fromImage(self.image))

        self.imageInfo = QImage("green-smile.png")
        self.imageWarning = QImage("red-info.png")
        self.showInfoImage(True)

        # 显示监控视频
        self.timer = QTimer(self)
        self.count = 0
        self.timer.timeout.connect(self.objectTrackingKNN)
        self.startCount()

        # 加载信号与槽
        self.ui.pushButtonOpenFile.clicked.connect(self.openMsg)
        self.ui.pushButtonOpenDebug.clicked.connect(self.openFindCircles)
        self.ui.pushButtonScreenShot.clicked.connect(self.saveImage)

        # 显示图片
        self.image = QImage()
        self.image.load("circle.jpg")
        self.ui.label_ShowImg.setPixmap(QPixmap.fromImage(self.image))
        self.ui.label_ShowImg_2.setPixmap(QPixmap.fromImage(self.image))




    # 保存图片
    def saveImage(self):
        cv2.imwrite("data\\"+self.getDateTime()+".png",self._frame1)


    # 显示报警信息
    def showInfoImage(self,val):
        print("# 显示报警信息")

    # 参数变化
    def parametersChange(self):
        self._SENSITIVITY_VALUE = self.ui.sliderMotionSensitive.value()
        self._BLUR_SIZE = self.ui.sliderBlurSize.value()
        print("参数变化：",self._SENSITIVITY_VALUE,self._BLUR_SIZE)


    def onBtnOpenDebugMode(self):
        if self._debugMode == True:
            self._debugMode = False
            # self.ui.pushButtonOpenDebug.setText("打开调试")
        else:
            self._debugMode = True
            # self.ui.pushButtonOpenDebug.setText("关闭调试")

    # 识别圆环
    # 寻找圆形
    def findCircles(self,img):
        # print('------------------------------')
        # 载入并显示图片

        cv2.imshow('my image', img)

        # 降噪（模糊处理用来减少瑕疵点）
        result = cv2.blur(img, (5, 5))
        # cv2.imshow('blur 2', result)

        # 灰度化,就是去色（类似老式照片）
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('cvtColor 3', gray)

        # param1的具体实现，用于边缘检测
        canny = cv2.Canny(img, 40, 80)
        # cv2.imshow('canny 4', canny)

        # 霍夫变换圆检测
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 50, param1=80,
                                   param2=30, minRadius=110, maxRadius=150)

        print(str(circles))

        print('-------------我是条分割线-----------------')
        # 根据检测到圆的信息，画出每一个圆
        if circles is not None:
            for circle in circles[0]:
                # 圆的基本信息
                print(circle[2])
                # 坐标行列(就是圆心)
                x = int(circle[0])
                y = int(circle[1])
                # 半径
                r = int(circle[2])
                # 在原图用指定颜色圈出圆，参数设定为int所以圈画存在误差
                img = cv2.circle(img, (x, y), r, (0, 255, 255), 3, 8, 0)

                ox = int(x + r / 2.0)
                oy = int(y + r / 2.0)
                img = cv2.circle(img, (x, y), 2, (0, 0, 255), 2, 8, 0)
        else:
            print("本帧图片没有发现圆形")

        # 显示新图像
        # cv2.imshow('find circle', img)
        return img

    def openFindCircles(self):
        self.image = QImage()
        if self._isFindCircle == True:
            self._isFindCircle = False
            self.image.load("find.jpg")
        else:
            self.image.load("circle.jpg")
            self._isFindCircle = True

        self.ui.label_ShowImg_2.setPixmap(QPixmap.fromImage(self.image))


    def outText(self,text):
        print(text)

    def startCount(self):
        self.timer.start(33)

    def objectTrackingKNN(self):
        ret, frame =  self._camera.read()
        fgmask = self._bsknn.apply(frame)
        th = cv2.threshold(fgmask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
        dilated = cv2.dilate(th,
                             cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                                       (3, 3)),
                             iterations=2)

        image, contours, hier = cv2.findContours(dilated.copy(),
                                                 cv2.RETR_EXTERNAL,
                                                 cv2.CHAIN_APPROX_SIMPLE)

        self._motionDetected = False

        for c in contours:
            if cv2.contourArea(c) > 1600:
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
                self._motionDetected = True

        if self._debugMode == True:
            cv2.imshow("mog", fgmask)
            cv2.imshow("thresh", th)
            cv2.imshow("detection", frame)
        else:
            cv2.destroyWindow("mog")
            cv2.destroyWindow("thresh")
            cv2.destroyWindow("detection")

        self.lableShowText(frame, self._motionDetected)
        # self.lableShowVideo(frame)


    def objectTracking(self):

        grabbed1, self._frame1 = self._camera.read()
        self._grayImage1 = cv2.cvtColor(self._frame1, cv2.COLOR_BGR2GRAY)
        grabbed2,self._frame2 = self._camera.read()
        self._grayImage2 = cv2.cvtColor(self._frame2, cv2.COLOR_BGR2GRAY)

        # 对于每个从背景之后读取的帧都会计算其与北京之间的差异，并得到一个差分图（different map）。
        # 还需要应用阈值来得到一幅黑白图像，并通过下面代码来膨胀（dilate）图像，从而对孔（hole）和缺陷（imperfection）进行归一化处理
        self._differenceImage = cv2.absdiff(self._grayImage1, self._grayImage2)
        # 二值化阈值处理
        self._thresholdImage = cv2.threshold(self._differenceImage,
                                             self._SENSITIVITY_VALUE, 255, cv2.THRESH_BINARY)[1]

        if self._debugMode == True:
            cv2.imshow("Difference Image",self._differenceImage)
            cv2.imshow("Threshold Image",self._thresholdImage)
        else:
            cv2.destroyWindow("Difference Image")
            cv2.destroyWindow("Threshold Image")

        self._thresholdImage = cv2.blur(self._thresholdImage,(self._BLUR_SIZE,self._BLUR_SIZE))

        self._thresholdImage = cv2.threshold(self._differenceImage,
                                             self._SENSITIVITY_VALUE, 255, cv2.THRESH_BINARY)[1]

        if self._debugMode == True:
            cv2.imshow("Final Threshold Image",self._thresholdImage)
        else:
            cv2.destroyWindow("Final Threshold Image")

        # 该函数计算一幅图像中目标的轮廓
        image, contours, hierarchy = cv2.findContours(self._thresholdImage.copy(),
                                                      cv2.RETR_EXTERNAL,
                                                      cv2.CHAIN_APPROX_SIMPLE)
        # if len(contours) > 0 :
        #     self._motionDetected = True
        # else:
        #     self._motionDetected = False
        self._motionDetected = False

        for c in contours:
            if cv2.contourArea(
                    c) < 2000:  # 对于矩形区域，只显示大于给定阈值的轮廓，所以一些微小的变化不会显示。对于光照不变和噪声低的摄像头可不设定轮廓最小尺寸的阈值
                continue
            (x, y, w, h) = cv2.boundingRect(c)  # 该函数计算矩形的边界框
            cv2.rectangle(self._frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            self._motionDetected = True

        self.lableShowText(self._frame1,self._motionDetected)

        self.lableShowVideo(self._frame1)

    # 在图片上显示文字
    def lableShowText(self,frameShow,isobjectFound):

        cv2.rectangle(frameShow, (0, 460), (200, 480), (255, 255, 255), -1)
        cv2.putText(frameShow, self.getDateTime(), (0, 475), 1, 1, (0, 0, 0),
                    1)
        if isobjectFound == True:
            self.showInfoImage(False)
            cv2.putText(frameShow, "Found moving object", (0, 20), 2, 1,
                        (0, 255, 0))
        else:
            self.showInfoImage(True)

    # 在标签上显示图片
    def lableShowVideo(self,frameShow):
        height, width, bytesPerComponent = frameShow.shape
        bytesPerLine = 3 * width
        rgbImage = cv2.cvtColor(frameShow, cv2.COLOR_BGR2RGB)
        img = QImage(rgbImage.data, width, height, bytesPerLine,
                     QImage.Format_RGB888)
        self.ui.label_ShowImg.setPixmap(QPixmap.fromImage(img))

    # 在标签上显示图片
    def lableShowVideo2(self, frameShow):
        height, width, bytesPerComponent = frameShow.shape
        bytesPerLine = 3 * width
        rgbImage = cv2.cvtColor(frameShow, cv2.COLOR_BGR2RGB)
        img = QImage(rgbImage.data, width, height, bytesPerLine,
                     QImage.Format_RGB888)
        self.ui.label_ShowImg_2.setPixmap(QPixmap.fromImage(img))

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "C:/",
                                               "All Files (*);;Text Files (*.txt)")
        self.ui.statusBar.showMessage(file)

    def getDateTime(self):
        time = QDateTime.currentDateTime()
        return time.toString("yyyy-MM-dd_hh-mm-ss")

    def playVideo(self):
        grabbed1, self._frame1 = self._camera.read()
        self.lableShowVideo(self._frame1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()

    sys.exit(app.exec_())

