import sys
import random
import matplotlib

import datetime
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import numpy as np
import csv, pyodbc

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class MyMplCanvas(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):

        self.tableNameSTemp = 'STemp'
        self.tableNameBTemp = 'BTemp'

        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 新建一个figure
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        # self.ax1.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
        self.ax1.set_xlabel('幅值')
        self.ax1.set_ylabel('时间')
        self.ax1.set_ylim(top=60.0,bottom=0.)

        self.ax1.grid(True)
        # plt.ylim(ymin=0,ymax=60)

        # format the ticks
        self.ax1.xaxis.set_major_locator(mdates.DayLocator())
        self.ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
        self.ax1.xaxis.set_minor_locator(
            mdates.HourLocator(byhour=range(0, 24), interval=3))
        for label in self.ax1.xaxis.get_ticklabels():
            label.set_rotation(30)



        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        '''定义FigureCanvas的尺寸策略，这部分的意思是设置FigureCanvas，使之尽可能的向外填充空间。'''
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    # 绘制左边的图
    def start_plot_left(self,dateA50, dataA50, columnNameA50, dataB50, columnNameB50):
        # dateA50, dataA50, columnNameA50 = self.selectData(tableName, columnIndexOne,queryBeginTime,queryBeginEnd)
        print("左边的图数据：",len(dateA50),len(dataA50) ,columnNameA50, columnNameB50)
        self.ax1.clear()
        line1 = self.ax1.plot(dateA50, dataA50, label=columnNameA50)

        # dateB50, dataB50, columnNameB50 = self.selectData(tableName, columnIndexTwo,queryBeginTime,queryBeginEnd)
        line2 = self.ax1.plot(dateA50, dataB50, label=columnNameB50)

        # self.selfAxSetting()
        self.ax1.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
        self.ax1.set_xlabel('幅值')
        self.ax1.set_ylabel('时间')
        self.ax1.grid(True)

        # format the ticks
        self.ax1.xaxis.set_major_locator(mdates.DayLocator())
        self.ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
        self.ax1.xaxis.set_minor_locator(
            mdates.HourLocator(byhour=range(0, 24), interval=3))
        for label in self.ax1.xaxis.get_ticklabels():
            label.set_rotation(30)

        self.draw()

    # 绘制右边的图
    def start_plot_right(self,dateA50, dataA50, columnNameA50):
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        # dateA50, dataA50, columnNameA50 = self.selectData(tableName, columnIndexOne,queryBeginTime,queryBeginEnd)
        print("右边的图数据：", len(dateA50), columnNameA50 )
        self.ax1.clear()
        line1 = self.ax1.plot(dateA50, dataA50, label=columnNameA50)

        # self.selfAxSetting()
        self.ax1.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
        self.ax1.set_xlabel('幅值')
        self.ax1.set_ylabel('时间')
        self.ax1.grid(True)

        # format the ticks
        self.ax1.xaxis.set_major_locator(mdates.DayLocator())
        self.ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
        self.ax1.xaxis.set_minor_locator(
            mdates.HourLocator(byhour=range(0, 24), interval=3))
        for label in self.ax1.xaxis.get_ticklabels():
            label.set_rotation(30)

        self.draw()


    # 图显示设置
    def selfAxSetting(self):
        self.ax1.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
        self.ax1.set_xlabel('幅值')
        self.ax1.set_ylabel('时间')
        self.ax1.grid(True)

        # format the ticks
        self.ax1.xaxis.set_major_locator(mdates.DayLocator())
        self.ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
        self.ax1.xaxis.set_minor_locator(
            mdates.HourLocator(byhour=range(0, 24), interval=3))
        for label in self.ax1.xaxis.get_ticklabels():
            label.set_rotation(30)

        self.draw()

    # 绘制图形
    def plotTableData(self):
        fig = plt.figure()
        fig.suptitle('figure title demo', fontsize=14, fontweight='bold')

        ax1 = fig.add_subplot(1, 1, 1)
        dateA50, dataA50, columnNameA50 = self.selectData(self.tableNameSTemp, 2)
        line1 = ax1.plot(dateA50, dataA50, label=columnNameA50)

        dateB50, dataB50, columnNameB50 = self.selectData(self.tableNameBTemp, 6)
        line2 = ax1.plot(dateB50, dataB50, label=columnNameB50)

        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        ax1.set_title("axes title")
        ax1.set_xlabel('幅值')
        ax1.set_ylabel('时间')

        ax1.grid(True)

        # format the ticks
        ax1.xaxis.set_major_locator(mdates.DayLocator())
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
        ax1.xaxis.set_minor_locator(
            mdates.HourLocator(byhour=range(0, 24), interval=3))

        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(90)

        plt.show()

    # 数据库查询内容
    def selectData(self,TableName, columnIndex,queryBeginTime,queryBeginEnd):
        # set up some constants
        MDB = 'D:\python\measurement data.mdb'
        DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'
        PWD = ''

        # connect to db
        con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV, MDB, PWD))
        cur = con.cursor()

        # 打印数据库表格名称
        for table_info in cur.tables(tableType='TABLE'):
            print(table_info.table_name)

        columnNameList = []
        for row in cur.columns(table=TableName):
            # print(row.column_name)
            columnNameList.append(row.column_name)

        # # 查询所有
        # for row in cur.execute("select * from " + TableName + " where ID = 1"):
        #     print("{}".format(row))

        SQL = 'SELECT * FROM ' + TableName + ' ;'
        rows = cur.execute(SQL).fetchall()
        print(len(rows))

        # 过滤显示的数据
        dateList = []
        dataList = []

        beginQueryDatatime = datetime.datetime(2016, 10, 18, 0, 0, 0)
        endQueryDatatime = datetime.datetime(2016, 10, 28, 0, 0, 0)
        print("查询时间: ", str(queryBeginTime), str(queryBeginEnd))

        for row in rows:
            if row.时间 > queryBeginTime and row.时间 < queryBeginEnd:
                # print(row.ID, row.时间, row.A50,row.气温)
                dateList.append(row[1])
                dataList.append(row[columnIndex])

        cur.close()
        con.close()

        return dateList, dataList, TableName[0] + '-' + columnNameList[
            columnIndex]


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.mpl = MyMplCanvas(self, width=5, height=6, dpi=100)

        self.mpl_ntb = NavigationToolbar(self.mpl, self)  # 添加完整的 toolbar

        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntb)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()

    ui.show()
    sys.exit(app.exec_())
