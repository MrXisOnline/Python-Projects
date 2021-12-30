from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog as fd


def get_bg():
	global bg_image
	file_name = fd.askopenfilename(
		title="Open Background Image",
		initialdir="/Users/",
		filetypes=(
			("jpg file", "*.jpg"),
			("png file", "*.png")
			)
		)
	if file_name != "":
		# bgimg_button.destroy()
		file_bg_label = tk.Label(root, text=file_name)
		file_bg_label.grid(row=0, column=1, pady=10, padx=20)
		bg_image = file_name

def get_watermark():
	global wm_image
	file_name = fd.askopenfilename(
		title="Open Watermark Image",
		initialdir="/Users/",
		filetypes=(
			("jpg file", "*.jpg"),
			("png file", "*.png")
			)
		)
	# print(file_name)
	if file_name != "":
		# wmimg_button.destroy()
		file_wm_label = tk.Label(root, text=file_name)
		file_wm_label.grid(row=1, column=1, pady=10, padx=20)
		wm_image = file_name

def process_image_save(bg,wm):
	# Image Processing
	if bg != None and wm != None:
		a = Image.open(bg)
		w = Image.open(wm)
		w = w.resize((50,50), Image.ANTIALIAS)
		w.putalpha(200)
		a = a.resize((1280,720), Image.ANTIALIAS)
		a.paste(w, (1210, 650), w)
		file_name = fd.asksaveasfilename(title="Save Image-As", initialdir="/Users/")
		if file_name != "":
			a.save(file_name, quality=95)
			file_save_label = tk.Label(root, text=f"Image Saved :{file_name}")
			file_save_label.grid(row=2, column=1, pady=10, padx=20)

bg_image = None
wm_image = None
root = tk.Tk()
root.title("Water-marker")
root.minsize(300,100)

bgimg_button = tk.Button(root, text="Background-Image", command=get_bg)
bgimg_button.grid(row=0, column=0, pady=10, padx=20)
wmimg_button = tk.Button(root, text="Watermark-Image", command=get_watermark)
wmimg_button.grid(row=1, column=0, pady=10, padx=20)
pcimg_button = tk.Button(root, text="Process-Image", command=lambda: process_image_save(bg_image, wm_image))
pcimg_button.grid(row=2, column=0, pady=10, padx=20)


root.mainloop()