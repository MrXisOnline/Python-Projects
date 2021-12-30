import pyautogui as pag
import time
import random
pag.FAILSAFE = True
with open("C:\\Users\\SG704\\PythonProjects\\oneTimeProjects\\assignment\\typing-speed\\words.txt") as file:
	word_text = file.read()
words = word_text.split(", ")
time.sleep(5)
while True:
	try:
		cur_pos = tuple(pag.position())
		r_word = random.choice(words)
		time.sleep(2)
		pag.click(1694, 727)
		pag.write(r_word, interval=0.10)
		pag.press('enter')
		time.sleep(0.7)
		pag.click(1946, 660, button="right")
		time.sleep(0.5)
		pag.click(1986, 729)
		time.sleep(0.5)
		pag.click(2102, 491)
		pag.moveTo(*cur_pos)
	except KeyboardInterrupt:
		break

