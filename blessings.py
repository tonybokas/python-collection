#!/usr/bin/env python3

years = []
with open('C:/Users/anton/desktop/test.txt', 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        years.append(int(line))
print(years)