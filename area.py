import sys

def area(i, j):
    return i * j

try:
    i = int(input('Enter length: '))
    j = int(input('Enter width: '))
except:
    print ('Error: Only numeric input accepted.')
    sys.exit()

k = area(i, j)

if k > 15:
    print(str(k) + ' is a big number!', sep = '')
else:
    print(str(k) + ' is small number!', sep = '')

print ('Good night')

