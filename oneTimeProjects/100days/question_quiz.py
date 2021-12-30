from trivia_data import Questions
from tkinter import *


def click_true():
	global question
	global canvas
	if ques.check_ans("True"):
		question = ques.give_question()
		canvas.itemconfig(text,text=question.question)
		score_label.config(text="Score: "+str(ques.score))
	else:
		question = ques.give_question()
		canvas.itemconfig(text,text=question.question)
		score_label.config(text="Score: "+str(ques.score))



def click_false():
	global question
	if ques.check_ans("False"):
		question = ques.give_question()
		canvas.itemconfig(text,text=question.question)
		score_label.config(text="Score: "+str(ques.score))
	else:
		question = ques.give_question()
		canvas.itemconfig(text,text=question.question)
		score_label.config(text="Score: "+str(ques.score))


# UI
screen = Tk()
screen.title("Quizzler")
screen.config(padx=30,pady=20,bg="#2F4F4F")
ques = Questions()
question = ques.give_question()
score_label = Label(text="Score: "+str(ques.score),fg="white",bg="#2F4F4F",font=("Arial",15,"bold"))
score_label.grid(row=0,column=1)
canvas = Canvas(width=600,height=300,bg="white")
canvas.create_image(300,150)
text = canvas.create_text(300,150,text=question.question,fill="black",font=("Arial",20,"italic"))
canvas.grid(row=1,column=0,columnspan=2,pady=20)
true_img = PhotoImage(file="true.png")
false_img = PhotoImage(file="false.png")
true_but = Button(image=true_img,command=click_true)
false_but = Button(image=false_img,command=click_false)
true_but.grid(row=2,column=0,pady=20)
false_but.grid(row=2,column=1,pady=20)
screen.mainloop()
