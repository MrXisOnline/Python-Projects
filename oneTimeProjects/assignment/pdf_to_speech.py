import tkinter as tk
from tkinter import filedialog
from pdfminer.high_level import extract_text
from gtts import gTTS
import os

def get_pdf_text():
	global text
	if os.path.exists(filename):
		text = extract_text(filename)
		tts_en = gTTS(text, lang='en')
		savefile = filedialog.asksaveasfilename(initialdir = "/",
			title = "Save as file",
			filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
		root.title("Now wait to complete")
		if savefile != "":
			with open(savefile, "wb") as file:
				tts_en.write_to_fp(file)

def openfile():
	global filename
	filename = filedialog.askopenfilename(initialdir = "/",
		title = "Select file",
		filetypes = (("pdf files","*.pdf"),("all files","*.*")))
	get_pdf_text()

text = None
filename = None
root = tk.Tk()
root.title("Pdf To Speech")
root.minsize(width=400,height=100)
openbt = tk.Button(root, text="Open PDF", command=openfile)
openbt.pack(pady=20)
root.mainloop()