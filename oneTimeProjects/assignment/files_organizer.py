import os
import shutil

path = "C:\\Users\\SG704\\Downloads"
os.chdir(path)
file_paths = []
dir_paths = []
for file in os.listdir():
	if os.path.isfile(os.path.join(path, file)):
		file_paths.append(file)
	elif os.path.isdir(os.path.join(path, file)):
		dir_paths.append(file)
for f in file_paths:
	sp = os.path.splitext(f.lower())
	if sp[1][1:] in dir_paths:
		pass
	else:
		os.mkdir(sp[1][1:])
		dir_paths.append(sp[1][1:])
	sec_path = os.path.join(os.path.join(path, dir_paths[dir_paths.index(sp[1][1:])]), f)
	shutil.move(os.path.join(path, f), sec_path)