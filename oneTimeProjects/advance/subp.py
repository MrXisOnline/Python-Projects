import os
import subprocess

os.chdir("C:\\Windows\\System32")

a = subprocess.Popen("calc.exe")
var = a.poll() is None
print(var)
a.wait()
a.poll()

