import re
import sys
import os

try:
	os.system("dir")
	a = input("Enter File Name :>")
	file = open(a, 'r')
	data = file.read()
	file.close()
except KeyboardInterrupt:
	print("[CTRL-C] Detected ...")
	print("Program Stoped!!!")
	sys.exit(0)
except:
	print("File Error")
	sys.exit(0)

email_pattern = re.compile(r'[a-zA-Z0-9.]+@[a-z]+\.[a-z]{2,4}')
matched_data = email_pattern.findall(data)
for mail in matched_data:
	print(mail)