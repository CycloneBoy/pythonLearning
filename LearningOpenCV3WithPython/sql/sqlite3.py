#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 0:26
# @Author  : CycloneBoy
# @Site    : 
# @File    : sqlite3.py
# @Software: PyCharm


import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")
c = conn.cursor()

sql = '''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);'''

c.execute(sql)
print("Table created successfully")
conn.commit()
conn.close()