# -*- coding: UTF-8 -*-
import codecs
import sys
import re
import csv
import os
import codecs
from lxml import etree


rootdir = 'D:\python\download\SogouCS'
list = os.listdir(rootdir)
pattern1 = r'news.sohunews(.*?)<content>(.*?)</content>'
i= 0
for x in range(0,len(list)):
   path = os.path.join(rootdir, list[x])        #获取目录下文件名字
   if os.path.isfile(path):
      print(str(path))
      html = etree.parse(path)
      html_data = html.xpath('//*') < br >  # 打印是一个列表，需要遍历
      print(html_data)
      for i in html_data:
          print(i.text)