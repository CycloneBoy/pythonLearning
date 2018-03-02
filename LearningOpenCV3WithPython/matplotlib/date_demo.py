import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import numpy as np
import csv, pyodbc


def PlotDemo1():
    fig  = plt.figure()
    fig.suptitle('figure title demo', fontsize=14, fontweight='bold')
    ax = fig.add_subplot(1,1,1)
    # ax.plot([1,2,3,4],[2,3,4,5])
    ax.set_title("axes title")
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")
    plt.show()

    filename = "mytable.csv"
    dates, close = np.loadtxt(filename, delimiter=",", unpack=True,
                              converters={0: mdates.strpdate2num('%Y-%m-%d')})
    ax.plot(dates, close)


def selectData():
    # set up some constants
    MDB = 'D:\python\measurement data.mdb'
    DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'
    PWD = ''

    # connect to db
    con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV, MDB, PWD))
    cur = con.cursor()

    for table_info in cur.tables(tableType='TABLE'):
        print(table_info.table_name)

    # for row in cur.execute("select * from STemp"):
    #     print(row.ID, row.时间, row.A50)

    columnNameList = []
    for row in cur.columns(table='STemp'):
        print(row.column_name)
        columnNameList.append(row.column_name)

    # run a query and get the results
    SQL = "SELECT 时间, A50 FROM STemp WHERE 时间 >= '2016/10/17 0:00:00' and 时间 <= '2016/10/17 23:59:59';"  # your query goes here
    rows = cur.execute(SQL).fetchall()

    for row in rows:
        print(row)

    cur.close()
    con.close()


if __name__ == '__main__':
    # PlotDemo1()
    selectData()
