#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 19:35
# @Author  : CycloneBoy
# @Site    : 
# @File    : multiTargetMotionDetection.py
# @Software: PyCharm


from __future__ import print_function
import sys
import cv2
import time
import numpy as np
from PIL import Image
from collections import deque

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *

from PyQt5.QtWidgets import QFileDialog
from LearningOpenCV3WithPython.MultiTargetMotionDetection.mainwindow import Ui_mainWindow
from LearningOpenCV3WithPython.MultiTargetMotionDetection.findtarget import FindTarget

from imutils.object_detection import non_max_suppression
from imutils import paths
import argparse
import imutils
import tablib


class MyWindow(QMainWindow):
    """加载主窗口 """

    def __init__(self, *args):
        # self.video = "data/vtest.avi"
        # self._camera = cv2.VideoCapture(self.video)  # 参数0表示第一个摄像头
        self._camera = cv2.VideoCapture(0)  # 参数0表示第一个摄像头
        # 等待两秒
        time.sleep(3)

        # 判断视频是否打开
        if (self._camera.isOpened()):
            print('Open')
        else:
            print('摄像头未打开')

        self._vedioWidth = int(self._camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        self._vedioHeight = int(self._camera.get(cv2.CAP_PROP_FRAME_HEIGHT))


        self._showSize = 400
        # self._vedioWidth = int(self._showSize)
        # self._vedioHeight = 300 # int(self._showSize)
        self._locationX = 0
        self._locationY = 0
        self._locationHeight = 0
        self._locationWidth = 0
        self._locationXOld = 0
        self._locationYOld = 0
        self._findTargetNumber = 0
        self._isOutputResult = False
        self._outputFile = None
        self._outputFileName = None
        self._outputFileExcel = None
        self._outputFileNameExcel = None

        print("vedio size", self._vedioWidth, self._vedioHeight)

        # 目标检测
        self._motionDetected = False
        self._debugMode = False
        self._bsknn = cv2.createBackgroundSubtractorKNN(detectShadows=True)
        self._isKnnDetect = False
        self._findTargetList = []
        self._findTargetListOld = []
        self._lineList = []

        self._sameFindTargetNumber = 0
        self._targetquen = deque()
        self._targetNewIndexList = []

        #输出数据
        self._outputData = []
        self._outputDataHeaders = ('时间','说明','数量','位置X','位置X','宽度','高度','速度dx','速度dy')
        self._outputDataFile = tablib.Dataset(*self._outputData, headers=self._outputDataHeaders)


        # 加载主窗口
        super(MyWindow, self).__init__(*args)

        # loadUi("mainwindow.ui", self)  # 通过uic的loadUi加载UI
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        # self.ui.label_ShowImg.resize(self._vedioWidth, self._vedioHeight)
        self.setWindowIcon(QIcon("./icon.png"))
        # 设置窗口固定大小
        # self.setFixedHeight(380)
        # self.setFixedWidth(640)

        # 显示监控视频
        self.timer = QTimer(self)
        self.count = 0

        self.timer.timeout.connect(self.objectTrackingKNN)
        self.startCount()

        # 加载信号与槽
        self.ui.pushButtonBeginDetection.clicked.connect(self.beginDetection)
        self.ui.pushButtonEndDetection.clicked.connect(self.endDetection)
        self.ui.pushButtonOutputData.clicked.connect(self.outputData)

    # 开始检测
    def beginDetection(self):
        print("开始检测")
        # self.startCount()
        self._isKnnDetect = True

    # 结束检测
    def endDetection(self):
        print("结束检测")
        # self.timer.stop()
        self._isKnnDetect = False


    # 输出检测数据
    def outputData(self):
        if self._isOutputResult == True:
            self._isOutputResult = False
            if self._outputFile != None:
                self._outputFile.close()
                self._outputFile = None

            if self._outputFileExcel != None:
                self._outputFileExcel.write(self._outputDataFile.export('xls'))
                self._outputFileExcel.close()
                self._outputFileExcel = None
            self.ui.pushButtonOutputData.setText("导出数据")
            print("结束输出检测数据")

        else:
            self._isOutputResult = True
            self._outputFileName = self.getDateTime()
            if self._outputFile == None:
                self._outputFile = open("./data/"+ self._outputFileName+ ".txt", 'w')
                self._outputFileExcel = open("./data/"+ self._outputFileName+ ".xls", 'wb')
                self._outputFile.write("# 发现行人：行人数量：{} 长宽：({}, {}) 位置：({}, {}) 速度:{}, {} \n")
            self.ui.pushButtonOutputData.setText("结束导出")
            print("开始输出检测数据")





    def startCount(self):
        self.timer.start(33)

    # 目标检测
    def objectTrackingKNN(self):
        ret, frame = self._camera.read()
        # print(ret, len(frame))

        # 视频是否播放完毕
        if ret != True:
            self.video = "data/vtest.avi"
            self._camera = cv2.VideoCapture(self.video)  # 参数0表示第一个摄像头
            ret, frame = self._camera.read()

        # 数据初始化
        self.initDetectParameter()

        # 打开检测
        if self._isKnnDetect == True:
            cv2.putText(frame, "begin...", (0, 10), 1, 1,
                        (0, 0, 255), 1)
            fgmask = self._bsknn.apply(frame)
            th = cv2.threshold(fgmask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
            dilated = cv2.dilate(th,
                                 cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                                           (3, 3)),
                                 iterations=2)

            image, contours, hier = cv2.findContours(dilated.copy(),
                                                     cv2.RETR_EXTERNAL,
                                                     cv2.CHAIN_APPROX_SIMPLE)

            for c in contours:
                if cv2.contourArea(c) > 1600:
                    (x, y, w, h) = cv2.boundingRect(c)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0),2)
                    self._targetDetected = True
                    self._findTargetNumber += 1
                    self._locationX = int(x + w/2)
                    self._locationY = int(y + h/2)
                    self._locationWidth = int(abs(w))
                    self._locationHeight = int(abs(h))
                    self.ui.textEditLocation.append("x:{:<5d}   y:{:<5d}".format(self._locationX, self._locationY))
                    self.ui.textEditSize.append("w:{:<5d}   h:{:<5d}".format(self._locationWidth, self._locationHeight))
                    findResult = FindTarget(int(x + w/2),int(y + h/2),int(abs(w)),int(abs(h)))
                    self._findTargetList.append(findResult)


        # 判断是否检测到目标
        if self._findTargetNumber > 0:
            print("检测到的数量,线的数量,新检测到的数量 ：", self._findTargetNumber,len(self._lineList),len(self._findTargetList))
            if len(self._lineList) < self._findTargetNumber:  # 还没有新的线
                self._lineList = [[] for i in range(self._findTargetNumber)]
                for index, targetNew in enumerate(self._findTargetList):
                    self._lineList[index].append(targetNew)

                print("创建好的线的列表：", self._lineList)
                for lineList in self._lineList:
                    for line in lineList:
                        # line.display()
                        print("长度：", len(lineList))
            else:
                print("存在历史的目标")
                existTargetOld = False
                self._targetNewIndexList.clear()
                for targetOld in self._lineList:
                    for index, targetNew in enumerate(self._findTargetList):
                        targetOldLast = targetOld[len(targetOld) - 1]
                        if targetNew.compare(targetOldLast):
                            # print("发现同一个矩形")
                            self._sameFindTargetNumber += 1
                            self.ui.textEditSpeed.append("dx:{} dy:{} ".format((targetNew.x - targetOldLast.x),(targetNew.y - targetOldLast.y)))
                            targetOld.append(targetNew)
                            existTargetOld = True
                            self._targetNewIndexList.append(index)
                            print("发现运动目标：{} 位置：({}, {}) 长宽：({}, {})  速度:{} {} "
                                  .format("历史目标",
                                          targetNew.x, targetNew.y,
                                          targetNew.w, targetNew.h,
                                          targetNew.x - targetOldLast.x,
                                          targetNew.y - targetOldLast.y
                                          ))

                            dataList = []
                            dataList.append(QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss"))
                            dataList.append("历史目标")
                            dataList.append(self._sameFindTargetNumber)
                            dataList.append(targetNew.x)
                            dataList.append(targetNew.y)
                            dataList.append(targetNew.w)
                            dataList.append(targetNew.h)
                            dataList.append(targetNew.x - targetOldLast.x)
                            dataList.append(targetNew.y - targetOldLast.y)


                            if self._isOutputResult == True:
                                self._outputFile.write(
                                    QDateTime.currentDateTime().
                                    toString("yyyy-MM-dd hh:mm:ss  ") +
                                    "发现运动目标：{} 位置：({}, {}) 长宽：({}, {})  速度:{} {} \n"
                                    .format("历史目标",
                                          targetNew.x, targetNew.y,
                                          targetNew.w, targetNew.h,
                                          targetNew.x - targetOldLast.x,
                                          targetNew.y - targetOldLast.y
                                            ))
                                self._outputDataFile.append(dataList)

                    if existTargetOld == False:
                        self._lineList.remove(targetOld)
                    else:
                        existTargetOld = False

                print("同一个目标的数量:", self._sameFindTargetNumber)
                print(self._lineList)
                for targetList in self._lineList:
                    target1 = targetList[0]
                    # print("每一个线的长度:", len(targetList))
                    for target in targetList:
                        cv2.line(frame, (target.x, target.y),
                                 (target1.x, target1.y), (255, 255, 0), 2)
                        target1 = target

                for index, targetNew in enumerate(self._findTargetList):
                    if not self._targetNewIndexList.count(index):
                        print("发现运动目标：{} 数量：{} 位置：({}, {}) 长宽：({}, {}) "
                              .format("新的目标",self._findTargetNumber - len(self._targetNewIndexList),
                                      targetNew.x, targetNew.y,
                                      targetNew.w, targetNew.h,
                                      ))
                        if self._isOutputResult == True:
                            self._outputFile.write(
                                QDateTime.currentDateTime().
                                toString("yyyy-MM-dd hh:mm:ss  ") +
                                "发现运动目标：{} 数量：{} 位置：({}, {}) 长宽：({}, {}) \n"
                                .format("新的目标",self._findTargetNumber - len(self._targetNewIndexList),
                                      targetNew.x, targetNew.y,
                                      targetNew.w, targetNew.h,
                                      ))

                            dataList = []
                            dataList.append(
                                QDateTime.currentDateTime().toString(
                                    "yyyy-MM-dd hh:mm:ss"))
                            dataList.append("新的目标")
                            dataList.append(self._findTargetNumber - len(self._targetNewIndexList))
                            dataList.append(targetNew.x)
                            dataList.append(targetNew.y)
                            dataList.append(targetNew.w)
                            dataList.append(targetNew.h)
                            dataList.append("")
                            dataList.append("")
                            self._outputDataFile.append(dataList)

            self.ui.label_target_number.setText(str(self._findTargetNumber))

            print()


            self._locationXOld = self._locationX
            self._locationYOld = self._locationY

            self._findTargetListOld = self._findTargetList.copy()

        else:
            self.showFindResult()

        # 显示视频图像
        self.lableShowVideo(frame)

    #  清空显示结果
    def initDetectParameter(self):
        self.ui.textEditLocation.clear()
        self.ui.textEditSize.clear()
        self.ui.textEditSpeed.clear()
        self._findTargetNumber = 0
        self._targetDetected = False
        self._findTargetList.clear()
        self._sameFindTargetNumber = 0

    # 木有发现的目标显示结果
    def showFindResult(self):
        showStr = "xxx"
        self.initDetectParameter()
        self.ui.textEditLocation.append("x:{}   y:{} ".format(showStr,showStr))
        self.ui.textEditSize.append("x:{}   y:{} ".format(showStr,showStr))
        self.ui.textEditSpeed.append("dx:{} dy:{} ".format(showStr,showStr))
        self.ui.label_target_number.setText("0")
        self._lineList.clear()
        self._sameFindTargetNumber = 0


        # print("没有发现运动目标")

    # 获取系统当前时间
    def getDateTime(self):
        time = QDateTime.currentDateTime()
        return time.toString("yyyy-MM-dd_hh-mm-ss")

    # 显示视频
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

    def exportData(self):
        print("test export data")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()

    sys.exit(app.exec_())

