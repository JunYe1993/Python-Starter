# Python 2.7.13
# coding=utf-8

import os

filename = raw_input("FileName : ")
file1 = open(filename, 'r')
# file1 = open(os.path.dirname(__file__) + "/" + filename, 'r')
text = file1.read()
file1.close()

print text.decode('utf-8'), type(text)
print len(text)

text = u"真。超級大便人"
print text, type(text)
print len(text)

print 4 >> 1