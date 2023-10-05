#!/usr/bin/env python3

def get_max_range():
    while True:
        high = input('Enter maximum of range: ')
        if high.isdigit() == True:
            high = int(high)
            if high > 1000:
                print('Try again. Limit is 1000.')
                continue
            break
        else:
            continue
    return high

def get_divisor(high):
    while True:
        divisor = input('Enter divisor: ')
        if divisor.isdigit():
            divisor = int(divisor)
            if divisor > high:
                print('Choose number less than maximum of range.')
                continue
            break
        else:
            continue
    return divisor

def main():
    print('Check Divisibility in Range of Numbers\n')
    
    try:
        high = get_max_range()
        divisor = get_divisor(high)
    except Exception as err:
        print('Error:', err)

    sep = '  ' # Used multiple times below
    result = 0
    print('\nDivisible numbers in range:')
    print(sep, end = '')
    for i in range(1, high):
        if i % divisor == 0:
            result += 1
            print(f'{i:3} ', end = '')
            if result != 0 and result % 10 == 0:
                print(f'\n{sep}', end = '')

    print('\n')
    print(f'Count of numbers under {high} divisible by {divisor}: {result}')

if __name__ == "__main__":
    main()