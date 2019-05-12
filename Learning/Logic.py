# coding=utf-8
from sys import argv

"""
if len(argv) > 1:
     print 'Hello, ' + argv[1]
else:
     print 'Hello, Guest'
"""
print 'Hello, ' + (argv[1] if len(argv) > 1 else 'Guest')