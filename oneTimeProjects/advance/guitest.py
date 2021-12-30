import tkinter
import time
from pytube import YouTube

'''
def hide(l):
	l.destroy()
	pass


root = tkinter.Tk()

label = tkinter.Label(root,text="Test")
label.pack()
button = tkinter.Button(root,text="delete",command=lambda: hide(label))
button.pack()
root.geomen

root.mainloop()
'''

link = input('Enter the link: ')

yt = YouTube(link)
#Title of video
print("Title: ",yt.title)
