from tkinter import *
import time


def start_timer():
	print("started timer")
	dis_text.config(text=f"Timer")
	countdown(WORK_MIN,0)
	
def setup_str(mins,sec):
		if mins <= 9:
			if sec <= 9:
				return f"0{mins}:0{sec}"
			else:
				return f"0{mins}:{sec}"
		else:
			if sec <= 9:
				return f"{mins}:0{sec}"
			else:
				return f"{mins}:{sec}"



def countdown(mins,sec):
	global work_data
	global work_index
	global job
	if (mins*60 +sec) > 0:
		if sec == 0:
			mins -= 1
			sec = 59
		canvas.itemconfig(timer_text,text=setup_str(mins,sec))
		job = window.after(1000,countdown,mins,sec-1)
	else:
		work_data[work_index] = "y"
		work_index += 1
		tick_label.config(text=str(tick_label.cget("text")+tick))
		dis_text.config(text=f"BREAK")
		if "n" in work_data:
			rest(SHORT_BREAK_MIN,0)
		else:
			tick_label.config(text="")
			work_index = 0
			work_data=["n","n","n","n"]
			rest(LONG_BREAK_MIN,0)

def rest(mins,sec):
	global job
	if (mins*60 +sec) > 0:
		if sec == 0:
			mins -= 1
			sec = 59
		canvas.itemconfig(timer_text,text=setup_str(mins,sec))
		job = window.after(1000,rest,mins,sec-1)
	else:
		dis_text.config(text=f"Timer")
		countdown(WORK_MIN,0)

def reset_timer():
	global job
	canvas.itemconfig(timer_text,text=f"00:00")
	dis_text.config(text=f"Timer")
	if job is not None:
		window.after_cancel(job)
		job = None
	print("reset")

job = None
work_data=["n","n","n","n"]
work_index = 0
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
tick = "✓"
t = time.localtime(time.time())

window = Tk()
window.config(bg=PINK,padx=60,pady=10)
window.minsize(400,400)
window.title("Pomodoro")
dis_text = Label(text="Timer",bg=PINK,fg=GREEN,font=(FONT_NAME,30,"bold"))
dis_text.grid(row=0,column=1)
tick_label = Label(text="",bg=PINK,fg=GREEN)
tick_label.grid(row=2,column=1)
canvas = Canvas(width=200,height=224,bg=PINK,highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=photo)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)
start_but = Button(text="Start",command=start_timer)
start_but.grid(row=3,column=0)
reset_but = Button(text="Reset",command=reset_timer)
reset_but.grid(row=3,column=2)
window.mainloop()