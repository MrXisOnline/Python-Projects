import os

path = "C:\\Windows\\System32\\config"
os.chdir(path)

file = open("SAM", "rb")
data = file.read()
file.close()