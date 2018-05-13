#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/11 14:07
# @Author  : CycloneBoy
# @Site    : 
# @File    : jobScrapy.py
# @Software: PyCharm

#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib import request
import re
import os,glob
import xlwt

book = xlwt.Workbook()
sheet = book.add_sheet('sheet', cell_overwrite_ok=True)
path = 'D:\\python\\scrapy'
os.chdir(path)
result11=[]
result21=[]
result31=[]
result41=[]
result51=[]

for k in range(1,91):
    html=request.urlopen("http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%e5%85%a8%e5%9b%bd&kw=%e6%95%b0%e6%8d%ae%e5%88%86%e6%9e%90%e5%b8%88&sm=0&isfilter=0&fl=489&isadv=0&sg=aae5284f62664af8b14611bda6d68315&p="+str(k)).read()    #读取网页源代码内容


    pat1 = 'onclick="submitLog.*?">(.*?)</a>'
    pat2 = '<td class="gsmc"><a href="https://ask.hellobi.com/(.*?)" target='
    pat3 = '<td class="zwyx">(.*?)</td>'
    pat4 = '<td class="gzdd">(.*?)</td>'
    pat5 = 'target="_blank">(.*?)<'
    #pat6 = '<span>(.*?)</span>'
    #pat7 = 'target="_blank">(.*?)</a>'

    result1 = re.compile(pat1).findall(str(html,"utf-8"))
    result2 = re.compile(pat2).findall(str(html,"utf-8"))
    result3 = re.compile(pat3).findall(str(html,"utf-8"))
    result4 = re.compile(pat4).findall(str(html,"utf-8"))
    result5 = re.compile(pat5).findall(str(html,"utf-8"))
    result11.extend(result1)
    result21.extend(result2)
    result31.extend(result3)
    result41.extend(result4)
    result51.extend(result5)


j = 0
for i in range(0,len(result11)):
    try:
        zhiwei = result11[i]
        wangzhi = result21[i]
        gongzi = result31[i]
        gongzuodidian = result41[i]
        gongsimingcheng = result51[i]

        sheet.write(i + 1, j, zhiwei)
        sheet.write(i + 1, j + 1, wangzhi)
        sheet.write(i + 1, j + 2, gongzi)
        sheet.write(i + 1, j + 3, gongzuodidian)
        sheet.write(i + 1, j + 4, gongsimingcheng)

    except Exception as e:
        print('出现异常：' + str(e))
        continue

book.save('D:\\python\\scrapy\\shujufenxishi.xls')