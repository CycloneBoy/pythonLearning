# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(966, 595)
        self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 951, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_VedioShow = QtWidgets.QWidget()
        self.tab_VedioShow.setObjectName("tab_VedioShow")
        self.label_ShowImg = QtWidgets.QLabel(self.tab_VedioShow)
        self.label_ShowImg.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.label_ShowImg.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_ShowImg.setObjectName("label_ShowImg")
        self.groupBox_data_info = QtWidgets.QGroupBox(self.tab_VedioShow)
        self.groupBox_data_info.setGeometry(QtCore.QRect(660, 90, 271, 401))
        self.groupBox_data_info.setObjectName("groupBox_data_info")
        self.label_5 = QtWidgets.QLabel(self.groupBox_data_info)
        self.label_5.setGeometry(QtCore.QRect(10, 34, 54, 12))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_data_info)
        self.label_7.setGeometry(QtCore.QRect(10, 230, 81, 21))
        self.label_7.setObjectName("label_7")
        self.label_target_number = QtWidgets.QLabel(self.groupBox_data_info)
        self.label_target_number.setGeometry(QtCore.QRect(80, 340, 54, 21))
        self.label_target_number.setObjectName("label_target_number")
        self.label_10 = QtWidgets.QLabel(self.groupBox_data_info)
        self.label_10.setGeometry(QtCore.QRect(10, 340, 54, 21))
        self.label_10.setObjectName("label_10")
        self.label = QtWidgets.QLabel(self.groupBox_data_info)
        self.label.setGeometry(QtCore.QRect(10, 140, 54, 12))
        self.label.setObjectName("label")
        self.textEditSpeed = QtWidgets.QTextEdit(self.groupBox_data_info)
        self.textEditSpeed.setGeometry(QtCore.QRect(70, 250, 161, 81))
        self.textEditSpeed.setObjectName("textEditSpeed")
        self.textEditLocation = QtWidgets.QTextEdit(self.groupBox_data_info)
        self.textEditLocation.setGeometry(QtCore.QRect(70, 50, 161, 81))
        self.textEditLocation.setObjectName("textEditLocation")
        self.textEditSize = QtWidgets.QTextEdit(self.groupBox_data_info)
        self.textEditSize.setGeometry(QtCore.QRect(70, 150, 161, 81))
        self.textEditSize.setObjectName("textEditSize")
        self.groupBox_button = QtWidgets.QGroupBox(self.tab_VedioShow)
        self.groupBox_button.setGeometry(QtCore.QRect(660, 10, 271, 81))
        self.groupBox_button.setObjectName("groupBox_button")
        self.pushButtonEndDetection = QtWidgets.QPushButton(self.groupBox_button)
        self.pushButtonEndDetection.setGeometry(QtCore.QRect(110, 20, 75, 23))
        self.pushButtonEndDetection.setObjectName("pushButtonEndDetection")
        self.pushButtonOutputData = QtWidgets.QPushButton(self.groupBox_button)
        self.pushButtonOutputData.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.pushButtonOutputData.setObjectName("pushButtonOutputData")
        self.pushButtonBeginDetection = QtWidgets.QPushButton(self.groupBox_button)
        self.pushButtonBeginDetection.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pushButtonBeginDetection.setObjectName("pushButtonBeginDetection")
        self.tabWidget.addTab(self.tab_VedioShow, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        mainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 966, 22))
        self.menuBar.setObjectName("menuBar")
        mainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(mainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(mainWindow)
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "目标检测v1.0"))
        self.label_ShowImg.setText(_translate("mainWindow", "视频显示"))
        self.groupBox_data_info.setTitle(_translate("mainWindow", "检测结果"))
        self.label_5.setText(_translate("mainWindow", "目标位置:"))
        self.label_7.setText(_translate("mainWindow", "目标移动速度:"))
        self.label_target_number.setText(_translate("mainWindow", "xxx"))
        self.label_10.setText(_translate("mainWindow", "目标个数:"))
        self.label.setText(_translate("mainWindow", "目标大小:"))
        self.groupBox_button.setTitle(_translate("mainWindow", "控制按钮"))
        self.pushButtonEndDetection.setText(_translate("mainWindow", "结束检测"))
        self.pushButtonOutputData.setText(_translate("mainWindow", "数据导出"))
        self.pushButtonBeginDetection.setText(_translate("mainWindow", "开始检测"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_VedioShow), _translate("mainWindow", "目标检测界面"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "其他"))

