import tkinter as tk
from tkinter import filedialog
import os

def end_all():
	global job_id
	if job_id != None:
		root.after_cancel(job_id)
		job_id = None
	root.quit()

def insert_text(file):
	global ex
	if os.path.exists(file):
		if ex == 0:
			with open(file, "w") as file:
				file.write(text)
			ex = 1
			textarea.delete("1.0", "end")
		else:
			with open(file, "a") as file:
				file.write(text)
			textarea.delete("1.0", "end")


def check_text():
	global job_id
	global text
	now_text = textarea.get(1.0, "end-1c")
	if text == now_text:
		insert_text(filename)
		text = now_text
	else:
		text = now_text
	job_id = root.after(10000, check_text)

def writingpanel():
	global job_id
	global text
	global textarea
	if os.path.exists(filename):
		root.title(filename)
		openbt.destroy()
		createbt.destroy()
		textarea = tk.Text(root, height=30, width=50)
		textarea.grid(row=0,column=0,padx=30,pady=40)
		textarea.focus_set()
		closebt = tk.Button(root, text="close", command=end_all)
		closebt.grid(row=1,column=0,padx=100,pady=5)
		if pre_text != None and pre_text != "":
			textarea.insert(tk.END, pre_text)
			text = pre_text
		check_text()


def openfile():
	global filename
	global pre_text
	filename = filedialog.askopenfilename(initialdir = "/",
		title = "Select file",
		filetypes = (("text files","*.txt"),("all files","*.*")))
	if os.path.exists(filename):
		file = open(filename,"r")
		pre_text = file.read()
		file.close()
	writingpanel()

def createfile():
	global filename
	filename = filedialog.asksaveasfilename(initialdir = "/",
		title = "Select file",
		filetypes = (("text files","*.txt"),("all files","*.*")))
	if not os.path.exists(filename):
		if filename != "":
			file = open(filename,"w")
			file.close()
	writingpanel()

ex = 0
textarea = None
job_id = None
text = ""
filename = None
pre_text = None
root = tk.Tk()
root.title("Text-Editor")
root.minsize(width=300,height=100)
openbt = tk.Button(root, text="Open", command=openfile)
openbt.grid(row=0,column=0,padx=20,pady=30)
createbt = tk.Button(root, text="Create file", command=createfile)
createbt.grid(row=0,column=1,padx=20,pady=30)
root.mainloop()