print type(1)
print type(1L)
print type(3.14)
print type(True)
print type(3 + 4j)
print 2 ** 100

print 10 / 3
print 10 // 3
print 10 / 3.0

print repr(1.0 - 0.8)
print str(1.0 - 0.8)

print "c:\\toDaniel"
print "c:\toDaniel"
print r"c:\toDaniel"

name = "Daniel"
for ch in name:
     print ch

print name[1:6]
print name[:6]
print name[0:]
print name[0:6:2]
print name[::-1]

# 字串格式化，舊式寫法
print '%d %.2f %s' % (1, 99.3, 'Justin')
print '%(real)s is %(nick)s' % {'real' : 'Justin', 'nick' : 'caterpillar'}

# 字串格式化，Python 2.6 後
print '{0} is {1}'.format('Justin', 'caterpillar')
print '{real} is {nick}'.format(real = 'Justin', nick = 'caterpillar')
print '{0} is {nick}'.format('Justin', nick = 'caterpillar')