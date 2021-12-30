from PIL import Image, ImageGrab, ImageChops
import pyautogui as ctrl
import time
import sys


def check_runtime():
	try:
		time.sleep(5)
		# print(ctrl.position())
		ctrl.click(1645, 187)
		time.sleep(30)
		# connect button Point(x=1645, y=187)
		# close button Point(x=1154, y=651)
		# position of screen shot  Point(x=516, y=448) Point(x=1403, y=680)
		no_runtime_img = Image.open("C:\\Users\\SG704\\PythonProjects\\AI_Stuff\\colab_gpu_runtime\\no_runtime.png")
		img = ImageGrab.grab(bbox=(516, 448, 1403, 680))
		diff = ImageChops.difference(no_runtime_img, img)
		if diff.getbbox():
			sys.exit(0)
		else:
			ctrl.click(1154, 651)
			check_runtime()
	except KeyboardInterrupt:
		sys.exit(0)

ctrl.FAILSAFE = True
time.sleep(10)
check_runtime()