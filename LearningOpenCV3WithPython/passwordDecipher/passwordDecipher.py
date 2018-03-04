#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 19:28
# @Author  : CycloneBoy
# @Site    : 
# @File    : passwordDecipher.py
# @Software: PyCharm


from __future__ import print_function

import random
import string
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
from LearningOpenCV3WithPython.passwordDecipher.mainwindow import Ui_mainWindow
from LearningOpenCV3WithPython.passwordDecipher.simpleSubstitutePassword import SimpleSubstitutePassword


class MyWindow(QMainWindow):
    """加载主窗口 """

    def __init__(self, *args):
        self.simpleSubPwd = SimpleSubstitutePassword()

        # 加载主窗口
        super(MyWindow, self).__init__(*args)

        # loadUi("mainwindow.ui", self)  # 通过uic的loadUi加载UI
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("./icon.jpg"))

        # 加载信号与槽
        self.ui.pushButtonEncryption.clicked.connect(self.encryption)
        self.ui.pushButtonCracked.clicked.connect(self.decrypt)
        self.ui.pushButtonGeneratePwd.clicked.connect(self.onPushButtonGeneratePwd)
        self.ui.pushButtonClearHackMessage.clicked.connect(self.onPushButtonClearHackMessage)
        self.ui.pushButtonClearMessage.clicked.connect(self.onPushButtonClearMessage)

    # 加密
    def encryption(self):
        clearText = self.ui.textEditCleartext.toPlainText()
        self.simpleSubPwd.message = clearText
        self.simpleSubPwd.key = self.ui.lineEditSetPwd.text().strip().upper()
        print(self.simpleSubPwd.key)
        # self.simpleSubPwd.checkValidKey(self.simpleSubPwd.key)
        print("正在加密中,请稍后....")
        self.ui.groupBox.setTitle("正在加密中,请稍后....")
        print("加密:" + clearText)
        password = self.simpleSubPwd.encryptMessage(self.simpleSubPwd.key,self.simpleSubPwd.message)
        self.cipherMessage = password

        self.ui.textEditCiphertext.setText(password)
        self.ui.groupBox.setTitle("加密完成")
        print("加密完成")
        print("加密后的密文:" + password)

    # 解密
    def decrypt(self):
        print("正在破解中,请稍后....")
        self.ui.groupBox.setTitle("正在破解中,请稍后....")
        password = self.ui.textEditCiphertext.toPlainText()

        self.simpleSubPwd.hackerCipherMessage = password
        self.simpleSubPwd.decrypt()

        self.ui.groupBox.setTitle("破解完成")
        print("破解完成")
        clearText = self.simpleSubPwd.hackedMessage
        print("解密:" + password)
        self.ui.textEditCleartext.setText(clearText)
        print("解密后的明文:" + clearText)
        self.ui.lineEditGeneratePwd.setText(self.simpleSubPwd.hackedKey)

    # 产生密匙
    def onPushButtonGeneratePwd(self):
        self.simpleSubPwd.key = self.simpleSubPwd.getRandomKey()
        print(self.simpleSubPwd.key)
        self.ui.lineEditSetPwd.setText(self.simpleSubPwd.key)

    def onPushButtonClearHackMessage(self):
        self.ui.textEditCiphertext.clear()

    def onPushButtonClearMessage(self):
        self.ui.textEditCleartext.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()

    sys.exit(app.exec_())



