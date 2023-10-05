from pathlib import Path
print('Path import completed.')

myFiles = ['your_Name-AJB.py', 'your_Name-2-AJB.py']
for filename in myFiles:
    print(Path(r'C:\Users\anton\documents\Python', filename))

print(Path('spam', 'bacon', 'eggs'))

directoryPath = Path('C:/Users/anton/Documents')
subFolder = Path('Python')
print(directoryPath / subFolder)

print(Path('spam') / Path('bacon'))

print(str(directoryPath / subFolder))