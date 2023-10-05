import os, pathlib

home = str(pathlib.Path.home())
origin = home + '\\Source\\blue-proposal\\src'
dest = home + '\\Desktop'
command = 'cp -r ' + origin + ' ' + dest

print('Starting backup...\n')
print('Home directory:', home)
print('Copying directory...\n', command, sep = '')

os.system(command)