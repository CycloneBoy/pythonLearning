#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 14:45
# @Author  : CycloneBoy
# @Site    : 
# @File    : pedestrainDetection.py
# @Software: PyCharm

from __future__ import print_function
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
from LearningOpenCV3WithPython.detection.mainwindow import Ui_mainWindow


from imutils.object_detection import non_max_suppression
from imutils import paths
import argparse
import imutils


class MyWindow(QMainWindow):
    """加载主窗口 """

    def __init__(self, *args):
        # self.video = "data/vtest.avi"
        # self._camera = cv2.VideoCapture(self.video)  # 参数0表示第一个摄像头
        self._camera = cv2.VideoCapture(0)  # 参数0表示第一个摄像头
        # 判断视频是否打开
        if (self._camera.isOpened()):
            print('Open')
        else:
            print('摄像头未打开')

        self._vedioWidth = int(self._camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        self._vedioHeight = int(self._camera.get(cv2.CAP_PROP_FRAME_HEIGHT))


        # 行人检测
        self._hog = cv2.HOGDescriptor()
        self._hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        self._showSize = 400
        self._vedioWidth = int(self._showSize)
        self._vedioHeight = int(self._showSize)
        self._isHogDetect = False
        self._isDetectPedestrain = False
        self._locationX = 0
        self._locationY = 0
        self._locationHeight = 0
        self._locationWidth = 0
        self._locationXOld = 0
        self._locationYOld = 0
        self._findPedestrainNumber = 0
        self._isOutputResult = False
        self._outputFile = None
        self._outputFileName = None

        print("vedio size", self._vedioWidth, self._vedioHeight)

        # 加载主窗口
        super(MyWindow, self).__init__(*args)

        # loadUi("mainwindow.ui", self)  # 通过uic的loadUi加载UI
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.ui.label_ShowImg.resize(self._vedioWidth, self._vedioHeight)

        # 显示监控视频
        self.timer = QTimer(self)
        self.count = 0

        # self.timer.timeout.connect(self.objectTrackingKNN)
        self.timer.timeout.connect(self.pedestrainDetectionHOG)
        self.startCount()

        # 加载信号与槽
        self.ui.pushButtonBeginDetection.clicked.connect(self.beginDetection)
        self.ui.pushButtonEndDetection.clicked.connect(self.endDetection)
        self.ui.pushButtonOutputData.clicked.connect(self.outputData)

    # 开始检测
    def beginDetection(self):
        print("开始检测")
        # self.startCount()
        self._isHogDetect = True

    # 结束检测
    def endDetection(self):
        print("结束检测")
        # self.timer.stop()
        self._isHogDetect = False


    # 输出检测数据
    def outputData(self):
        if self._isOutputResult == True:
            self._isOutputResult = False
            if self._outputFile != None:
                self._outputFile.close()
                self._outputFile = None

            self.ui.pushButtonOutputData.setText("导出数据")
            print("结束输出检测数据")

        else:
            self._isOutputResult = True
            self._outputFileName = self.getDateTime()
            if self._outputFile == None:
                self._outputFile = open("./data/"+ self._outputFileName+ ".txt", 'w')
                self._outputFile.write("# 发现行人：行人数量：{} 长宽：({}, {}) 位置：({}, {}) 速度:{}, {} \n")
            self.ui.pushButtonOutputData.setText("结束导出")
            print("开始输出检测数据")

    def startCount(self):
        self.timer.start(33)

    # HOG行人检测
    def pedestrainDetectionHOG(self):
        ret, image = self._camera.read()

        image = imutils.resize(image, width=min(self._showSize, image.shape[1]))
        self._findPedestrainNumber = 0

        if self._isHogDetect == True:
            cv2.putText(image, "begin...", (0, 10), 1, 1,
                        (0, 0, 255),1)

            # detect people in the image
            (rects, weights) = self._hog.detectMultiScale(image,
                                                          winStride=(4, 4),
                                                          padding=(8, 8),
                                                          scale=1.05)

            rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
            pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

            # draw the final bounding boxes
            for (xA, yA, xB, yB) in pick:
                cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
                self._findPedestrainNumber += 1
                self._locationX = (xA + xB)/ 2
                self._locationY = (yA + yB) / 2
                self._locationWidth = abs(xA - xB)
                self._locationHeight = abs(yA - yB)

        if self._findPedestrainNumber > 0:

            self.ui.label_length.setText(str(self._locationHeight))
            self.ui.label_width.setText(str(self._locationWidth))
            self.ui.label_target_location_x.setText(str(self._locationX))
            self.ui.label_target_location_y.setText(str(self._locationY))
            self.ui.label_target_speed_dx.setText(str(self._locationX - self._locationXOld))
            self.ui.label_target_speed_dy.setText(str(self._locationY - self._locationYOld))
            self.ui.label_target_number.setText(str(self._findPedestrainNumber))

            print("发现行人：数量：{} 长宽：({}, {}) 位置：{}, {} 速度:{} {} "
                                    .format(self._findPedestrainNumber,
                                            self._locationHeight,
                                            self._locationWidth,
                                            self._locationX, self._locationY,
                                            self._locationX - self._locationXOld,
                                            self._locationY - self._locationYOld
                                            ))

            if self._isOutputResult == True:
                self._outputFile.write(QDateTime.currentDateTime().
                                       toString("yyyy-MM-dd hh:mm:ss  " ) +
                                    "发现行人：行人数量：{} 长宽：({}, {}) 位置：({}, {}) 速度:{}, {} \n"
                                    .format(self._findPedestrainNumber,
                                            self._locationHeight,
                                            self._locationWidth,
                                            self._locationX, self._locationY,
                                            self._locationX - self._locationXOld,
                                            self._locationY - self._locationYOld

                                            ))

            self._locationXOld = self._locationX
            self._locationYOld = self._locationY
        else:
            self.showFindResult()

        # 显示视频图像
        self.lableShowVideo(image)

    def showFindResult(self):
        showStr = "xxx"
        self.ui.label_length.setText(showStr)
        self.ui.label_width.setText(showStr)
        self.ui.label_target_location_x.setText(showStr)
        self.ui.label_target_location_y.setText(showStr)
        self.ui.label_target_speed_dx.setText(showStr)
        self.ui.label_target_speed_dy.setText(showStr)
        self.ui.label_target_number.setText("0")
        # print("没有发现行人")

    # 获取系统当前时间
    def getDateTime(self):
        time = QDateTime.currentDateTime()
        return time.toString("yyyy-MM-dd_hh-mm-ss")

    def playVideo(self):
        grabbed1, self._frame1 = self._camera.read()
        self.lableShowVideo(self._frame1)

    # 在标签上显示图片
    def lableShowVideo(self,frameShow):
        height, width, bytesPerComponent = frameShow.shape
        bytesPerLine = 3 * width
        rgbImage = cv2.cvtColor(frameShow, cv2.COLOR_BGR2RGB)
        img = QImage(rgbImage.data, width, height, bytesPerLine,
                     QImage.Format_RGB888)
        self.ui.label_ShowImg.setPixmap(QPixmap.fromImage(img))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()

    sys.exit(app.exec_())

