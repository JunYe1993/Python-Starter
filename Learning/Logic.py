# coding=utf-8
from sys import argv

text = "哈哈"
print type(argv[1]) 
msg = text.encode('utf8')
print type(text), type(msg)
text = msg.decode('utf-8')
if len(argv) > 1:
     print 'Hello, ' + argv[1] + str(text)
else:
     print 'Hello, Guest'