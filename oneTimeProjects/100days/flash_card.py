from flash_data_work import Data
from tkinter import *
import time

def show_card():
	global start_job
	if start_job != None:
		screen.after_cancel(start_job)
		start_job = None
	canvas.itemconfig(can_id,image=back_photo)
	canvas.itemconfig(lang_id,text="English")
	canvas.itemconfig(word_id,text=data.load_card("en"))

def start_all_over():
	global start_job
	canvas.itemconfig(can_id,image=front_photo)
	canvas.itemconfig(lang_id,text="French")
	canvas.itemconfig(word_id,text=data.load_card("fr"))
	start_job = screen.after(3000,show_card)

def on_right():
	data.send_to_pre()
	start_all_over()

def on_wrong():
	start_all_over()


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

data = Data()
screen = Tk()
screen.title("Flash-Cards")
screen.config(bg=BACKGROUND_COLOR,padx=30,pady=20)
screen.minsize(400,300)
canvas = Canvas(width=800,height=600,bg=BACKGROUND_COLOR,highlightthickness=0)
front_photo = PhotoImage(file="flashcard_front.png")
back_photo = PhotoImage(file="flashcard_back.png")
right_photo = PhotoImage(file="flash_right.png")
wrong_photo = PhotoImage(file="flash_wrong.png")
can_id = canvas.create_image(400,300,image=front_photo)
lang_id = canvas.create_text(400,200,text="French",fill="black",font=(FONT_NAME,30,"normal"))
word_id = canvas.create_text(400,300,text=data.load_card("fr"),fill="black",font=(FONT_NAME,40,"bold"))
canvas.grid(row=0,column=1,columnspan=2)
Label(text="",bg=BACKGROUND_COLOR).grid(row=1,column=0)
right_but = Button(image=right_photo,bg=BACKGROUND_COLOR,command=on_right)
right_but.grid(row=1,column=1,pady=20)
wrong_but = Button(image=wrong_photo,bg=BACKGROUND_COLOR,command=on_wrong)
wrong_but.grid(row=1,column=2,pady=20)
start_job = screen.after(3000,show_card)
screen.mainloop()
