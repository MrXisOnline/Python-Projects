from tkinter import *

def on_click_num(e,num):
	e["state"] = NORMAL
	text = e.get()
	if len(text) < 6:
		e.delete(0,END)
		text = text + str(num)
		e.insert(0,text)
		e["state"] = DISABLED
	else:
		e["state"] = DISABLED


def result(e,number1,number2,operator):
	global num1
	global num2
	global op
	e["state"] = NORMAL
	text = e.get()
	num2 = int(text)
	if op == "+":
		res = int(num1 + num2)
		e.delete(0,END)
		e.insert(0,str(res))
		e["state"] = DISABLED
		num1 = None
		num2 = None
		op = None
	elif op == "-":
		res = int(num1 - num2)
		e.delete(0,END)
		e.insert(0,str(res))
		e["state"] = DISABLED
		num1 = None
		num2 = None
		op = None
	elif op == "*":
		res = int(num1 * num2)
		e.delete(0,END)
		e.insert(0,str(res))
		e["state"] = DISABLED
		num1 = None
		num2 = None
		op = None
	elif op == "/":
		res = int(num1 / num2)
		e.delete(0,END)
		e.insert(0,str(res))
		e["state"] = DISABLED
		num1 = None
		num2 = None
		op = None
	else:
		e["state"] = DISABLED


def on_click_op(e,operator):
	global num1
	global num2
	global op
	e["state"] = NORMAL
	text = e.get()
	if op == "":
		num1 = int(text)
		print(num1)
		op = operator
		print(op)
		e.delete(0,END)
		e["state"] = DISABLED
	else:
		e["state"] == DISABLED


num1=None
num2=None
op = ""
root_scr = Tk()
root_scr.title("Calculator")
root_scr.geometry("400x420")
inputbox = Entry(width=26,font=("Arial",15),state=DISABLED)
inputbox.place(x=40,y=30)
but_1 = Button(root_scr, text="1",width=7,bg="yellow",font=("Arial",10),fg="red",command=lambda : on_click_num(inputbox,1))
but_1.place(x=25,y=100)
but_2 = Button(root_scr, text="2",width=7,bg="yellow",font=("Arial",10),fg="red",command=lambda : on_click_num(inputbox,2))
but_2.place(x=115,y=100)
but_3 = Button(root_scr, text="3",width=7,bg="yellow",font=("Arial",10),fg="red",command=lambda : on_click_num(inputbox,3))
but_3.place(x=205,y=100)
but_4 = Button(root_scr, text="4",width=7,bg="yellow",font=("Arial",10),fg="red",command=lambda : on_click_num(inputbox,4))
but_4.place(x=25,y=170)
but_5 = Button(root_scr, text="5",width=7,bg="yellow",font=("Arial",10),fg="red",command=lambda : on_click_num(inputbox,5))
but_5.place(x=115,y=170)
but_6 = Button(root_scr, text="6",width=7,bg="yellow",font=("Arial",10),fg="red",command=lambda : on_click_num(inputbox,6))
but_6.place(x=205,y=170)
but_7 = Button(root_scr, text="7",width=7,bg="yellow",font=("Arial",10),fg="red",command=lambda : on_click_num(inputbox,7))
but_7.place(x=25,y=240)
but_8 = Button(root_scr, text="8",width=7,bg="yellow",font=("Arial",10),fg="red",command=lambda : on_click_num(inputbox,8))
but_8.place(x=115,y=240)
but_9 = Button(root_scr, text="9",width=7,bg="yellow",font=("Arial",10),fg="red",command=lambda : on_click_num(inputbox,9))
but_9.place(x=205,y=240)
but_0 = Button(root_scr, text="0",width=7,bg="yellow",font=("Arial",10),fg="red",command=lambda : on_click_num(inputbox,0))
but_0.place(x=115,y=310)
but_00 = Button(root_scr, text="00",width=7,bg="yellow",font=("Arial",10),fg="red",command=lambda : on_click_num(inputbox,"00"))
but_00.place(x=115,y=360)
but_eq = Button(root_scr, text="=",width=7,height=5,bg="yellow",font=("Arial",10),fg="red",command=lambda : result(inputbox,num1,num2,op))
but_eq.place(x=25,y=310)
but_div = Button(root_scr,text="/",width=5,height=5,bg="yellow",font=("Arial",10),fg="red",command=lambda : on_click_op(inputbox,"/"))
but_div.place(x=295,y=100)
but_mul = Button(root_scr,text="*",width=5,height=5,bg="yellow",font=("Arial",10),fg="red",command=lambda : on_click_op(inputbox,"*"))
but_mul.place(x=295,y=200)
but_sub = Button(root_scr,text="-",width=5,height=5,bg="yellow",font=("Arial",10),fg="red",command=lambda : on_click_op(inputbox,"-"))
but_sub.place(x=295,y=310)
but_plus = Button(root_scr,text="+",width=7,height=5,bg="yellow",font=("Arial",10),fg="red",command=lambda : on_click_op(inputbox,"+"))
but_plus.place(x=205,y=310)
root_scr.mainloop()