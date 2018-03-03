import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import numpy as np
import csv, pyodbc

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
days = mdates.DayLocator()
yearsFmt = mdates.DateFormatter('%Y/%m/%d')
hours = mdates.HourLocator()

tableNameSTemp = 'STemp'
tableNameBTemp = 'BTemp'

def PlotDemo1():
    fig  = plt.figure()
    fig.suptitle('figure title demo', fontsize=14, fontweight='bold')

    ax1 = fig.add_subplot(1,1,1)
    dateA50, dataA50, columnNameA50= selectData(tableNameSTemp,2)
    line1 = ax1.plot(dateA50, dataA50, label=columnNameA50)

    dateB50, dataB50, columnNameB50 = selectData(tableNameBTemp,6)
    line2 = ax1.plot(dateB50, dataB50, label=columnNameB50)

    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    ax1.set_title("axes title")
    ax1.set_xlabel('Tempture')
    ax1.set_ylabel('DateTime')

    ax1.grid(True)

    # format the ticks
    ax1.xaxis.set_major_locator(days)
    ax1.xaxis.set_major_formatter(yearsFmt)
    ax1.xaxis.set_minor_locator(mdates.HourLocator(byhour=range(0,24),interval=3))


    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(90)


    plt.show()


# 数据库查询内容
def selectData(TableName,columnIndex):
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
        print(row.column_name)
        columnNameList.append(row.column_name)

    # 查询所有
    for row in cur.execute("select * from " + TableName + " where ID = 1"):
        print("{}".format(row))

    SQL = 'SELECT * FROM ' + TableName + ' ;'
    rows = cur.execute(SQL).fetchall()
    print(len(rows))

    # 过滤显示的数据
    dateList = []
    dataList = []

    beginQueryDatatime = datetime.datetime(2016, 10, 18, 0, 0, 0)
    endQueryDatatime = datetime.datetime(2016, 10, 28, 0, 0, 0)
    print("查询时间: ",str(beginQueryDatatime), str(endQueryDatatime))
    for row in rows:
        if row.时间 > beginQueryDatatime and row.时间 < endQueryDatatime:
            # print(row.ID, row.时间, row.A50,row.气温)
            dateList.append(row[1])
            dataList.append(row[columnIndex])

    cur.close()
    con.close()

    return dateList, dataList, TableName[0] + '-' + columnNameList[columnIndex]


if __name__ == '__main__':
    PlotDemo1()
    # selectData()
