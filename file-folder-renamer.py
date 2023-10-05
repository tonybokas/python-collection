# File and Folder Renamer | Copyright (C) 2021 Antonios J. Bokas | github.com/ajbokas
# Purpose: Renames files and folder within a root directory per regular expression.

import os
import re
import shutil
from pathlib import Path

print('File and Folder Renamer\n\nRename files and folders in a root directory.')

while true:

	while true:
		root = input('\nEnter root (e.g., C:\\Users\\name\\Documents): ')
		print('')
		if os.path.isdir(root) == False:
			print('   Error: Invalid path.')
			continue
		else:
			print('   Directory located.')
			return [false]

	pattern = re.compile((\w.+)_) # Need to create right regex

	for folder_name, sub_folders, file_names in os.listdir(root):
		print('Updating names in folder: ' + root_folder)

		for sub_folder in sub_folders:
			# rename matched parts of folder name per regex

		for file_name in file_names:
			# rename matched parts of file name per regex
			
	again = input('\nEnter (y) to target new root or press enter to quit: ')
	if again.lower() == 'y':
		continue
	else:
		return false