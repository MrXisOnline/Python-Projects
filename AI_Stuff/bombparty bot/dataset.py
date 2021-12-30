from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np
# import tensorflow as tf

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
text = [i+j+k for i in letters for j in letters for k in letters] + [i+j for i in letters for j in letters]
print(len(text))
bg = Image.open("bg.png")
font = ImageFont.truetype("callibri_bold.ttf", 16)
font_color = (255, 255, 255)
i = 0
for t in text:
	n_bg = bg.copy()
	draw = ImageDraw.Draw(n_bg)
	draw_coords = (0,0)
	draw.text(draw_coords, t, font_color, font=font)
	# if i == 0:
	# 	img_array = np.array([n_bg])
	# 	i = 1
	# else:
	# 	np.append(img_array, n_bg)
	break
n_bg.save("test.png")