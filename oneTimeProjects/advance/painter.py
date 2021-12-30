import pyautogui as pag
import time
import subprocess
def orbits():
	pag.moveTo(100,200)
	pag.click()
	distance = 200
	while distance > 0:
		pag.dragRel(distance, 0, duration=1)
		distance += -5
		pag.dragRel(0, distance, duration=1)
		pag.dragRel(-distance, 0, duration=1)
		distance += -5
		pag.dragRel(0, -distance, duration=1)


subprocess.Popen('C:\\Windows\\System32\\mspaint.exe')
time.sleep(3)

orbits()