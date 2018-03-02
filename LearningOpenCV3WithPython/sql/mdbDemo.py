import csv, pyodbc

# set up some constants
MDB = 'D:\python\measurement data.mdb'
DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'
PWD = ''

# connect to db
con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV, MDB, PWD))

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=D:\python\measurement data.mdb;'
    )
# con = pyodbc.connect(conn_str)
cur = con.cursor()

for table_info in cur.tables(tableType='TABLE'):
    print(table_info.table_name)

# for row in cur.execute("select * from STemp"):
#     print(row.ID, row.时间, row.A50)

for indexX, row in enumerate(cur.execute("select * from STemp where ID = 1")):
    for indexY, column in enumerate(row):
        print("{} ，{} ：{}".format(indexX, indexY, column ))


for row in cur.execute("select * from STemp where ID = 1"):
    print("{}".format(row))

columnNameList = []
strColumnList = "("

# columns in table x
for row in cur.columns(table='STemp'):
    print(row.column_name)
    strColumnList += row.column_name + ', '
    columnNameList.append(row.column_name)


strColumnList += ")"
print(strColumnList)
print(columnNameList)

row = cur.execute("select * from STemp").fetchone()
rows = cur.execute("select * from STemp").fetchall()

# run a query and get the results
SQL = 'SELECT * FROM STemp;' # your query goes here
rows = cur.execute(SQL).fetchall()
cur.close()
con.close()

# you could change the mode from 'w' to 'a' (append) for any subsequent queries
with open('mytable.csv', 'w', newline='') as fou:
    csv_writer = csv.writer(fou)
    csv_writer.writerow(columnNameList)
    csv_writer.writerows(rows)
    # csv_writer.writerow(row)
