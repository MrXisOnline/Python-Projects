from tkinter import *

def settext(e,root):
	label = Label(root,text=e.get())
	label.pack()
	e["state"] = NORMAL
	e.delete(0,END)
	e.insert(0,"hello")
	e["state"] = DISABLED


root = Tk()
c = Entry(root,state=DISABLED)
c.pack()
b = Button(root,text="click",command=lambda : settext(c,root))
b.pack()
root.mainloop()