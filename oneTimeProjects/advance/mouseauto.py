import pyautogui as pag
import time
# pag.FAILSAFE = False
print(pag.size())
time.sleep(1)
print(pag.position())
time.sleep(1)
pag.click(1141, 191)
pag.moveTo(100,100)
'''
# Create a Square with mouse
for exe in range(11):
	pag.moveTo(100, 100, duration=0.25)
	time.sleep(0.5)
	pag.moveTo(200, 100, duration=0.25)
	time.sleep(0.5)
	pag.moveTo(200, 200, duration=0.25)
	time.sleep(0.5)
	pag.moveTo(100, 200, duration=0.25)
	time.sleep(0.5)
'''