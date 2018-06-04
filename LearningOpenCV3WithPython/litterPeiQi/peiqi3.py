#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 23:36
# @Author  : CycloneBoy
# @Site    : 
# @File    : peiqi3.py
# @Software: PyCharm

#coding:utf-8
from PIL import Image
#要索引的字符列表
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
length = len(ascii_char)
img = Image.open('peiqi.jpg')      #读取图像文件
(width,height) = img.size
img = img.resize((int(width*0.5),int(height*0.2)))  #对图像进行一定缩小,图片的大小可以根据上传图片的大小来按需调节，
print(img.size)
def convert(img):
    img = img.convert("L")  # 转为灰度图像
    txt = ""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            gray = img.getpixel((j, i))     # 获取每个坐标像素点的灰度
            unit = 256.0 / length
            txt += ascii_char[int(gray / unit)] #获取对应坐标的字符值
        txt += '\n'
    return  txt

def convert1(img):
    txt = ""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            r,g,b = img.getpixel((j, i))           #获取每个坐标像素点的rgb值
            gray = int(r * 0.299 + g * 0.587 + b * 0.114)   #通过灰度转换公式获取灰度
            unit = (256.0+1)/length
            txt += ascii_char[int(gray / unit)]  # 获取对应坐标的字符值
        txt += '\n'
    return txt

txt = convert(img)
f = open("03_convert.txt","w")
f.write(txt)            #存储到文件中
f.close()

