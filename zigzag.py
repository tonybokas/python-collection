import time, sys

print('Zigzag Printer\nby Al Swiegart\nModified by Antonios J. Bokas\n')

max_zigzag = int(input('Enter how many lines you want to zigzag for: '))
print('\n')

count = 0
indent = 0
right = True

while count < max_zigzag:

    print(' ' * indent, '********')
    time.sleep(0.05)

    if right:
        indent += 1
        if indent == 10:
            right = False
    
    else:
        indent -= 1
        if indent == 0:
            right = True
            
    count += 1
        
print('\nAll done!')