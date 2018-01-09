#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 19:48
# @Author  : CycloneBoy
# @Site    :
# @File    : MyWindow.py
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
from work.mainwindow import Ui_MainWindow


class MyWindow(QMainWindow):
    """加载主窗口 """

    def __init__(self, *args):
        self._camera = cv2.VideoCapture(0)  # 参数0表示第一个摄像头
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

        print("vedio size", self._vedioWidth, self._vedioWidth)

        # 加载主窗口
        super(MyWindow, self).__init__(*args)

        # loadUi("mainwindow.ui", self)  # 通过uic的loadUi加载UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label_ShowImg.resize(self._vedioWidth, self._vedioHeight)


        self.image = QImage()

        # self.videowriter = cv2.cvCreateVideoWriter("test1.jpg",
        #                                            cv2.CV_FOURCC('j', 'p','g', '1'),
        #                                            25, cv2.cvSize(200, 200), 1)
        #
        # # 播放的视频位置
        # self.playcapture = cv2.cvCreateFileCapture("test.avi")

        #if self.image.load("test1.jpg"):

        self.image.load("test1.jpg")

        self.ui.label_ShowImg.setPixmap(QPixmap.fromImage(self.image))

        # # 设定定时器
        # self.timer = MyThread()  # 录制视频
        # self.timer.setIdentity("thread1")
        # self.timer.sinOut.connect(self.playVideo)
        # self.timer.setVal(6)
        #
        # self.playtimer = MyThread()  # 播放视频

        self.timer = QTimer(self)
        self.count = 0
        self.timer.timeout.connect(self.objectTracking)
        self.startCount()


        # 加载信号与槽
        self.ui.pushButtonOpenFile.clicked.connect(self.openMsg)

    def outText(self,text):
        print(text)

    def startCount(self):
        self.timer.start(33)


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
        self._thresholdImage = cv2.blur(self._thresholdImage,(self._BLUR_SIZE,self._BLUR_SIZE))

        self._thresholdImage = cv2.threshold(self._differenceImage,
                                             self._SENSITIVITY_VALUE, 255, cv2.THRESH_BINARY)[1]

        # 该函数计算一幅图像中目标的轮廓
        image, contours, hierarchy = cv2.findContours(self._thresholdImage.copy(),
                                                      cv2.RETR_EXTERNAL,
                                                      cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0 :
            self._motionDetected = True
        else:
            self._motionDetected = False

        for c in contours:
            if cv2.contourArea(
                    c) < 1500:  # 对于矩形区域，只显示大于给定阈值的轮廓，所以一些微小的变化不会显示。对于光照不变和噪声低的摄像头可不设定轮廓最小尺寸的阈值
                continue
            (x, y, w, h) = cv2.boundingRect(c)  # 该函数计算矩形的边界框
            cv2.rectangle(self._frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.rectangle(self._frame1,(0,460),(200,480),255,255,255)
        cv2.putText(self._frame1,self.getDateTime(),(0,480),1,1,(0,0,0),2)

        if self._motionDetected == True:
            cv2.putText(self._frame1,"Found moving object",(0,240),2,1,(0,255,0))

        height, width, bytesPerComponent = self._frame1.shape
        bytesPerLine = 3 * width
        rgbImage = cv2.cvtColor(self._frame1, cv2.COLOR_BGR2RGB)

        img = QImage(rgbImage.data, width, height, bytesPerLine,
                     QImage.Format_RGB888)

        self.ui.label_ShowImg.setPixmap(QPixmap.fromImage(img))

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "C:/",
                                               "All Files (*);;Text Files (*.txt)")
        self.ui.statusBar.showMessage(file)

    def getDateTime(self):
        time = QDateTime.currentDateTime()
        return time.toString("yyyy-MM-dd_hh-mm-ss")

    def playVideo(self):
        grabbed1, self._frame1 = self._camera.read()
        height, width, bytesPerComponent = self._frame1.shape
        bytesPerLine = 3 * width
        rgbImage = cv2.cvtColor(self._frame1, cv2.COLOR_BGR2RGB)

        img = QImage(rgbImage.data, width, height, bytesPerLine,
                     QImage.Format_RGB888)

        self.ui.label_ShowImg.setPixmap(QPixmap.fromImage(img))



class MyThread(QThread):

    sinOut = pyqtSignal(str)

    def __init__(self,signal = "updateTimer",parent = None):
        super(MyThread,self).__init__(parent)
        self.stoped = False
        self.signal = signal
        self.mutex = QMutex()
        self.identity = None

    def setIdentity(self,text):
        self.identity = text

    def setVal(self,val):
        self.times = int(val)

        # 执行线程的run方法
        self.start()


    def run(self):
        with QMutexLocker(self.mutex):
            self.stoped = False
        #while self.times > 0 and self.identity:
        while True:
            if self.stoped:
                return

            # self.sinOut.emit(self.identity + " " + str(self.times))
            # self.times -= 1
            self.sinOut.emit(self.signal)
            time.sleep(0.04) #40毫秒发送一次信号，每秒25帧

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stoped = True

    def isStoped(self):
        with QMutexLocker(self.mutex):
            return self.stoped


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = MyWindow()
    myshow
    myshow.show()

    # while True:
    #     myshow.objectTracking()
    #
    #     key = cv2.waitKey(1) & 0xFF
    #     # 按'q'健退出循环
    #     if key == ord('q'):
    #         break


    sys.exit(app.exec_())