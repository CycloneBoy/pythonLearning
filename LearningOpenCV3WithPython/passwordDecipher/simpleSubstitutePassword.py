#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/4 14:35
# @Author  : CycloneBoy
# @Site    : 
# @File    : simpleSubstitutePassword.py
# @Software: PyCharm

import random
import string
import sys
import os, re, copy, pprint
from LearningOpenCV3WithPython.passwordDecipher import simpleSubCipher
from LearningOpenCV3WithPython.passwordDecipher import makeWordPatterns
from LearningOpenCV3WithPython.passwordDecipher import wordPatterns

class SimpleSubstitutePassword:
    """简单替代密码加解密 """


    def __init__(self, message=None):
        self.message = message
        self.cipherMessage = ""
        self.key = "LFWOAYUISVKMNXPBDCRJTQEGHZ"
        self.mode = 'encrypt'

        self.LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.nonLettersOrSpacePattern = re.compile('[^A-Z\s]') #匹配任何不是A-Z的字符

        self.hackedKey = ""
        self.hackerCipherMessage = ""
        self.hackedMessage = ""
        self.letternMapping = None

    def setMessage(self,message):
        self.message = message

    def setCipherMessage(self,cipherMessage):
        self.cipherMessage = cipherMessage

    # 检测密码
    def checkValidKey(self, key):
        keyList = list(key)
        lettersList = list(self.LETTERS)
        keyList.sort()
        lettersList.sort()
        if keyList != lettersList:
            # sys.exit('There is an error in the key or symbol set.')
            print('There is an error in the key or symbol set.')

    # 加密
    def encryptMessage(self, key, message):
        return self.translateMessage(key, message, 'encrypt')

    # 解密
    def decryptMessage(self, key, message):
        return self.translateMessage(key, message, 'decrypt')

    # 加解密
    def translateMessage(self, key, message, mode):
        translated = ''
        charsA = self.LETTERS
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
    def getRandomKey(self):
        key = list(self.LETTERS)
        random.shuffle(key)
        return ''.join(key)



    # 破解简单替代密码
    def hackSimpleSub(self, message):
        intersectedMap = self.getBlankCipherletterMapping()
        cipherwordList = self.nonLettersOrSpacePattern.sub('',
                                                      message.upper()).split()

        for cipherword in cipherwordList:
            # 获取密字映射
            newMap = self.getBlankCipherletterMapping()

            # 获取单词的模式
            wordPattern = makeWordPatterns.getWordPattern(cipherword)
            if wordPattern not in wordPatterns.allPatterns:
                continue

            # 对每一个潜在的候选单词进行处理
            for candidate in wordPatterns.allPatterns[wordPattern]:
                newMap = self.addLettersToMapping(newMap, cipherword, candidate)

            intersectedMap = self.intersectMappings(intersectedMap, newMap)

        # 移除已经解密的字母
        return self.removeSolvedLettersFromMapping(intersectedMap)

    # 从密字映射创建密匙
    def decryptWithCipherletterMapping(self, ciphertext, letterMapping):
        key = ['x'] * len(self.LETTERS)

        for cipherletter in self.LETTERS:
            if len(letterMapping[cipherletter]) == 1:
                keyIndex = self.LETTERS.find(letterMapping[cipherletter][0])
                key[keyIndex] = cipherletter
            else:
                ciphertext = ciphertext.replace(cipherletter.lower(), '_')
                ciphertext = ciphertext.replace(cipherletter.upper(), '_')

        key = ''.join(key)
        print('key:', key)
        self.hackedKey = key

        return simpleSubCipher.decryptMessage(key, ciphertext)

    # 获取空白的密字映射
    def getBlankCipherletterMapping(self):
        # Returns a dictionary value that is a blank cipherletter mapping:
        return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [],
                'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [],
                'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [],
                'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

    # 构建字母映射表 密码词 候选词
    def addLettersToMapping(self, letterMapping, cipherword, candidate):
        letterMapping = copy.deepcopy(letterMapping)
        for i in range(len(cipherword)):
            if candidate[i] not in letterMapping[cipherword[i]]:
                letterMapping[cipherword[i]].append(candidate[i])
        return letterMapping

    # 获取两个密字映射的交集
    def intersectMappings(self, mapA, mapB):
        intersectedMapping = self.getBlankCipherletterMapping()

        for letter in self.LETTERS:
            if mapA[letter] == []:
                intersectedMapping[letter] = copy.deepcopy(mapB[letter])
            elif mapB[letter] == []:
                intersectedMapping[letter] = copy.deepcopy(mapA[letter])
            else:
                for mappedLetter in mapA[letter]:
                    if mappedLetter in mapB[letter]:
                        intersectedMapping[letter].append(mappedLetter)

        return intersectedMapping

    # 从密字映射中移除已经破解的字母
    def removeSolvedLettersFromMapping(self, letterMapping):
        letterMapping = copy.deepcopy(letterMapping)
        loopAgain = True
        while loopAgain:
            loopAgain = False

            solveLetters = []
            # 处理一个潜在解密字母的字母表
            for cipherletter in self.LETTERS:
                if len(letterMapping[cipherletter]) == 1:
                    solveLetters.append(letterMapping[cipherletter][0])

            for cipherletter in self.LETTERS:
                for s in solveLetters:
                    if len(letterMapping[cipherletter]) != 1 and s in \
                            letterMapping[cipherletter]:
                        letterMapping[cipherletter].remove(s)
                        if len(letterMapping[cipherletter]) == 1:
                            loopAgain = True
        return letterMapping

    # 简单替代密码破解测试
    def testHacker(self):
        message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'

        print('开始破解...')
        letternMapping = self.hackSimpleSub(message)

        print('映射关系:')
        pprint.pprint(letternMapping)
        print()
        print('原始密文:')
        print(message)
        print('破解后的消息')
        hackedMessage = self.decryptWithCipherletterMapping(message, letternMapping)
        print(hackedMessage)

    # 破解封装
    def decrypt(self):
        self.letternMapping = self.hackSimpleSub(self.hackerCipherMessage)
        self.hackedMessage = self.decryptWithCipherletterMapping(self.hackerCipherMessage,self.letternMapping)


    # 简单替代密码加密测试
    def testCipher(self):
        myMessage = 'A malicious user could rename or add programs with these names, ' \
                    'tricking Pyperclip into running them with whatever permissions ' \
                    'the Python process has.'
        myMode = 'encrypt'
        myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'

        self.checkValidKey(myKey)

        if myMode == 'encrypt':
            translated = self.encryptMessage(myKey, myMessage)
        elif myMode == 'decrypt':
            translated = self.decryptMessage(myKey, myMessage)

        print('Using key %s ' % myKey)
        print('The %sed message is:' % (myMode))
        print(translated)
        print()

if __name__ == '__main__':
    print("测试")
    simpleSub = SimpleSubstitutePassword()
    simpleSub.testHacker()

    print()
    simpleSub.testCipher()