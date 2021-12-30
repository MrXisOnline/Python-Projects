from tkinter import *
window = Tk()
window.minsize(width=200,height=200)

label = Label(text="Hello").grid(row=0,column=0)
but1 = Button(text="Button1").grid(row=1,column=1)
but2 = Button(text="Button2").grid(row=0,column=2)
ent = Entry().grid(row=2,column=3)

window.mainloop()