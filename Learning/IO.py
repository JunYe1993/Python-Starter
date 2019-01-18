import sys

file = open(sys.argv[1], 'r')
for line in file.readlines():
     print line.decode('utf-8')
file.close()