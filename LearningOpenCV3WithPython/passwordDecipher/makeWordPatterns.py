#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/4 12:03
# @Author  : CycloneBoy
# @Site    : 计算单词模式
# @File    : makeWordPatterns.py
# @Software: PyCharm
import  pprint


# 获取单词的模式
def getWordPattern(word):
    # Returns a string of the pattern from of the given word.
    word = word.upper()
    nextNum = 0
    letterNums = {}
    wordPattern = []

    for letter in word:
        if letter not in letterNums:
            letterNums[letter] = str(nextNum)
            nextNum += 1
        wordPattern.append(letterNums[letter])
    return '.'.join(wordPattern)


# main
def main():
    allPatterns = {}

    fo = open('dictionary.txt')
    wordList = fo.read().split('\n')
    fo.close()

    for word in wordList:
        # Get the pattern for each string in wordList
        pattern = getWordPattern(word)

        if pattern not in allPatterns:
            allPatterns[pattern] = [word]
        else:
            allPatterns[pattern].append(word)

    # This is code that writes code. The makeWordPatterns.py file contains
    # one very, very large assignment statement.
    fo = open('wordPatterns.py', 'w')
    fo.write('allPatterns = ')
    fo.write(pprint.pformat(allPatterns))
    fo.close()


if __name__  == '__main__':
    main()