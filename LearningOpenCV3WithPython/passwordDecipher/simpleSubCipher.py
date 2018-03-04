#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/4 10:46
# @Author  : CycloneBoy
# @Site    : 
# @File    : simpleSubCipher.py
# @Software: PyCharm

import LearningOpenCV3WithPython.passwordDecipher.Pyperclip
import sys
import random


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# LETTERS = r""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def main():
    ##加密测试
    myMessage = 'A malicious user could rename or add programs with these names, ' \
                'tricking Pyperclip into running them with whatever permissions ' \
                'the Python process has.'
    myMode = 'encrypt'

    # ##解密测试
    # myMessage = '''z/%3M\b\Zl2/l2O5/bZlM[/5O$3%O/Z5/3[[/g5Z!53%2/a\Y*/Y*O2O/$3%O2)/Y5\b<\$!/vCgO5bM\g/\$YZ/5l$$\$!/Y*O%/a\Y*/a*3YOoO5/gO5%\22\Z$2/Y*O/vCY*Z$/g5ZbO22/*32e'''
    # myMode = 'decrypt'
    # myMessage = 'L nlmswsptr trac wptmo caxlna pc loo bcpuclnr esji jiara xlnar, jcswksxu Bhbacwmsb sxjp ctxxsxu jian esji eiljaqac bacnsrrspxr jia Bhjipx bcpwarr ilr.'
    # myMode = 'decrypt'

    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    # myKey = r"""/{9@6hUf:q?_)^eTi|W1,NLD7xk(-SF>Iz0E=d;Bu#c]w~'VvHKmpJ+}s8y& XtP43.b[OA!*\Q<M%$ZgG52YloaRCn"`rj"""

    checkValidKey(myKey)

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print('Using key %s ' % myKey)
    print('The %sed message is:' % (myMode))
    print(translated)
    print()


# 检测密码
def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('There is an error in the key or symbol set.')

# 加密
def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

# 解密
def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

# 加解密
def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key

    if mode == 'decrypt':
        # 交换密码
        charsA, charsB = charsB, charsA

    for symbol in message:
        if symbol.upper() in charsA:
            # 加解密
            symbolIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symbolIndex].upper()
            else:
                translated += charsB[symbolIndex].lower()
            # symbolIndex = charsA.find(symbol)
            # translated += charsB[symbolIndex]
        else:
            # symbol is not in LETTRES
            translated += symbol

    return translated

# 获得随机KEY
def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)



if __name__ == '__main__':
    main()














