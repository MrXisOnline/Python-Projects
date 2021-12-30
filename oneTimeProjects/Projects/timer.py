from tkinter import *
import time

def start(e,b,r):
	text=e.get()
	e.destroy()
	b.destroy()
	mss = text.split(":")
	ms = [int(mss[0]), int(mss[1])]
	secs = int((ms[0] * 60) + ms[1])
	ltime = Label(r,text=str(text))
	ltime.pack()
	for i in range(secs-1,0,-1):
		time.sleep(1)
		ltime.destroy()
		ltime = Label(r,text=str(i))
		ltime.pack()



root = Tk()
root.title("Timer")
root.geometry("300x300")
inputbox = Entry(width=20)
inputbox.pack()
start_but = Button(root,text="START",command=lambda : start(inputbox,start_but,root))
start_but.pack()
root.mainloop()