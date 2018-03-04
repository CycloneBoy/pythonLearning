#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/4 12:20
# @Author  : CycloneBoy
# @Site    : 破解简单替代密码
# @File    : simpleSubHacker.py
# @Software: PyCharm

import os, re, copy, pprint
from LearningOpenCV3WithPython.passwordDecipher import simpleSubCipher
from LearningOpenCV3WithPython.passwordDecipher import makeWordPatterns

# 创建单词模式
if not os.path.exists('wordPatterns.py'):
    makeWordPatterns.main()
from LearningOpenCV3WithPython.passwordDecipher import wordPatterns

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersOrSpacePattern = re.compile('[^A-Z\s]') #匹配任何不是A-Z的字符

# 破解简单替代密码
def hackSimpleSub(message):
    intersectedMap = getBlankCipherletterMapping()
    cipherwordList = nonLettersOrSpacePattern.sub('',message.upper()).split()

    for cipherword in cipherwordList:
        # 获取密字映射
        newMap = getBlankCipherletterMapping()

        # 获取单词的模式
        wordPattern = makeWordPatterns.getWordPattern(cipherword)
        if wordPattern not in wordPatterns.allPatterns:
            continue

        # 对每一个潜在的候选单词进行处理
        for candidate in wordPatterns.allPatterns[wordPattern]:
            newMap = addLettersToMapping(newMap, cipherword, candidate)

        intersectedMap = intersectMappings(intersectedMap, newMap)

    # 移除已经解密的字母
    return removeSolvedLettersFromMapping(intersectedMap)

# 从密字映射创建密匙
def decryptWithCipherletterMapping(ciphertext, letterMapping):
    key = ['x'] * len(LETTERS)

    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')

    key = ''.join(key)
    print('key:',key)

    return simpleSubCipher.decryptMessage(key, ciphertext)

# 获取空白的密字映射
def getBlankCipherletterMapping():
    # Returns a dictionary value that is a blank cipherletter mapping:
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [],
           'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [],
           'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [],
           'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

# 构建字母映射表 密码词 候选词
def addLettersToMapping(letterMapping, cipherword, candidate):
    letterMapping = copy.deepcopy(letterMapping)
    for i in range(len(cipherword)):
        if candidate[i] not in letterMapping[cipherword[i]]:
            letterMapping[cipherword[i]].append(candidate[i])
    return letterMapping

# 获取两个密字映射的交集
def intersectMappings(mapA, mapB):
    intersectedMapping = getBlankCipherletterMapping()

    for letter in LETTERS:
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
def removeSolvedLettersFromMapping(letterMapping):
    letterMapping = copy.deepcopy(letterMapping)
    loopAgain = True
    while loopAgain:
        loopAgain = False

        solveLetters = []
        # 处理一个潜在解密字母的字母表
        for cipherletter in LETTERS:
            if len(letterMapping[cipherletter]) == 1:
                solveLetters.append(letterMapping[cipherletter][0])

        for cipherletter in LETTERS:
            for s in solveLetters:
                if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
                    letterMapping[cipherletter].remove(s)
                    if len(letterMapping[cipherletter]) == 1:
                        loopAgain = True
    return letterMapping


def main():
    message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'

    print('开始破解...')
    letternMapping = hackSimpleSub(message)

    print('映射关系:')
    pprint.pprint(letternMapping)
    print()
    print('原始密文:')
    print(message)
    print('破解后的消息')
    hackedMessage = decryptWithCipherletterMapping(message, letternMapping)
    print(hackedMessage)

# 测试程序
def testMain():
    print("开始第1个密词:")
    letterMapping1 = getBlankCipherletterMapping()
    print(letterMapping1)
    print()

    word = 'OLQIHXIRCKGNZ'
    wordPat = makeWordPatterns.getWordPattern(word)
    print(wordPat)
    print()

    candidates = wordPatterns.allPatterns[wordPat]
    print(candidates)
    print()

    letterMapping = addLettersToMapping(letterMapping1, word, candidates[0])
    print(letterMapping1)
    print()

    letterMapping1 = addLettersToMapping(letterMapping1, word, candidates[1])
    print(letterMapping1)
    print()

    print("开始第2个密词:")
    word2 = 'PLQRZKBZB'
    letterMapping2 = getBlankCipherletterMapping()
    wordPat2 = makeWordPatterns.getWordPattern(word2)
    candidates2 = wordPatterns.allPatterns[wordPat2]
    print(candidates2)
    print()

    for candidate in candidates2:
        letterMapping2 = addLettersToMapping(letterMapping2, word2, candidate)

    print(letterMapping2)
    print()

    print("获取连个密词映射的交集")
    intersectedMapping = intersectMappings(letterMapping1, letterMapping2)
    print(intersectedMapping)
    print()

    print("开始第3个密词:")
    word3 = 'MPBKSSIPLC'
    letterMapping3 = getBlankCipherletterMapping()
    wordPat3 = makeWordPatterns.getWordPattern(word3)
    candidates3 = wordPatterns.allPatterns[wordPat3]
    print(candidates3)
    print()

    for candidate in candidates3:
        letterMapping3 = addLettersToMapping(letterMapping3, word3, candidate)

    print(letterMapping3)
    print()

    print("获取连个密词映射的交集")
    intersectedMapping = intersectMappings(intersectedMapping, letterMapping3)
    print(intersectedMapping)
    print()

    cipherWord = 'OLQIHXIRCKGNZ PLQRZKBZB MPBKSSIPLC'
    message = decryptWithCipherletterMapping(cipherWord, intersectedMapping)
    print(message)


if __name__ == '__main__':
    main()
