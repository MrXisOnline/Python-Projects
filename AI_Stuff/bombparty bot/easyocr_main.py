import easyocr
import time
import pyautogui as pag
from PIL import ImageGrab
pag.FAILSAFE = True

def give_words_list(file):
	words = []
	with open(file, "r") as f:
		for line in f.readlines():
			if len(line[:-1]) > 5:
				words.append(line[:-1])
	return words

reader = easyocr.Reader(['ch_sim','en'])
words = give_words_list("words.txt")
run = True
try:
	li = time.time()
	while run:
		if time.time()-li > 2:
			start = time.time()
			time.sleep(5)
			im2 = ImageGrab.grab(bbox=(735, 547, 809, 584))
			im2.save("ntest.png")
			inis = reader.readtext('ntest.png')[0][1]
			for word in words:
				if inis in word:
					break
			pag.click(x=600,y=1000)
			pag.write(word, interval=0.05)
			pag.press("enter")
			li = time.time()
except KeyboardInterrupt:
	run = False
# print(time.time()-start)
# im2 = ImageGrab.grab(bbox=(362, 955, 1203, 1036))
