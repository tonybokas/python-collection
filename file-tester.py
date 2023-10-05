'''
File Tester
'''
import os, sys
from pathlib import Path

file_path = Path(input('\nEnter a file path: '))
new_file_name = Path(file_path.stem + str('_urls.html'))
new_file_location = Path(str(Path.home()), 'Desktop', str(new_file_name))
new_file = open(new_file_location, 'w')
new_file.write('<div><h1>Unique URLs Extracted From ' + str(file_path.name) + '</h1></div>')
new_file.close()

while True:

	print('\nEnd of script. Press Enter to quit.')
	exitResponse = input()

	if exitResponse == '':

		break