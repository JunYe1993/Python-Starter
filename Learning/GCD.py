print 'Enter two numbers...'
m = int(raw_input('Number 1: '))
n = int(raw_input('Number 2: '))
while n != 0:
   r = m % n
   m = n
   n = r
print 'GCD: {0}'.format(m)

numbers = [10, 20, 30]
squares = []
for number in numbers:
    squares.append(number ** 2)
print squares

numbers = [10, 20, 30]
print [number ** 2 for number in numbers]