import pyautogui as pag
import time
pag.FAILSAFE = True
while True:
	try:
		a = pag.position()
		pag.click(1694, 727)
		pag.write('!work', interval=0.10)
		pag.press('enter')
		time.sleep(3)
		pag.write("!dep all", interval=0.10)
		pag.press('enter')
		pag.moveTo(a[0], a[1])
		time.sleep(120)
	except KeyboardInterrupt:
		break

# pag.moveTo(100,100)
