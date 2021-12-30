import pyautogui as pag
import subprocess
import time

subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
time.sleep(3)
pag.click(300, 250); pag.typewrite("Hello,\n Suraj", 0.3)