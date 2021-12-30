import random
import json
from tkinter import *

alps_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
syms = ["!", '+', '#', '$', '%', '&', '*']
alps_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

PASS_LENGTH = 16
R_NUM = 2

def search_records():
	web = entry_web.get()
	if web == "":
		pass
	else:
		try:
			with open("pg_details.json", "r") as file:
				data = json.load(file)
				create_popup(f"Here are details seeded with {web}\n\nEmail: {data[web]['email']}\nPassword: {data[web]['password']}")
		except KeyError:
			pass
		except FileNotFoundError:
			pass

def password_generator():
	entry_pass.delete(0,END)
	r_ran = []
	for _ in range(4):
		r_ran.append(random.choice(nums))
		r_ran.append(random.choice(syms))
	for _ in range(12):
		l = random.choice([alps_lower,alps_upper])
		r_ran.append(random.choice(l))
	password = ""
	for _ in range(PASS_LENGTH):
		password = password + random.choice(r_ran)
	
	# entry_pass.clear()
	entry_pass.insert(END,password)
def create_popup(message):
	new_window = Toplevel(main_screen)
	new_window.title("pop-up")
	new_window.minsize(100,100)
	text_label = Label(new_window,text = message)
	text_label.grid(row=0,column=0,padx=30,pady=10)
	but_exit = Button(new_window,text="ok",width=20,command=new_window.destroy)
	but_exit.grid(row=1,column=0,padx=30,pady=10)


def add_detail():
	web = entry_web.get()
	uname = entry_uname.get()
	passcode = entry_pass.get()
	data = {web:{"email":uname,"password":passcode}}
	if web == "" or uname == "" or passcode == "":
		create_popup("Enter All Details")
	else:
		try:
			with open("pg_details.json", "r") as file:
				n_data = json.load(file)
		except FileNotFoundError:
			with open("pg_details.json", "w") as file:
				json.dump(data,file,indent=4)
		except json.decoder.JSONDecodeError:
			with open("pg_details.json", "w") as file:
				json.dump(data,file,indent=4)
		else:
			n_data.update(data)
			with open("pg_details.json", "w") as file:
				json.dump(n_data,file,indent=4)
		create_popup(f"{web} Details saved")
		entry_web.delete(0,END)
		entry_uname.delete(0,END)

main_screen = Tk()
main_screen.minsize(width=400,height=400)
main_screen.title("Password-Manager")
main_screen.config(padx=30,pady=10)
lock_img = PhotoImage(file="pm_logo.png")
canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)
label_web = Label(text="Website:")
label_web.grid(row=1,column=0,padx=5,pady=10)
entry_web = Entry(width=25)
entry_web.focus()
but_search = Button(text="Search",width=20,command=search_records)
but_search.grid(row=1,column=2,padx=10,pady=10)
entry_web.grid(row=1,column=1,padx=5,pady=10)
label_uname = Label(text="Email/Username:")
label_uname.grid(row=2,column=0,padx=20,pady=10)
entry_uname = Entry(width=57)
entry_uname.insert(0,"sg704992@gmail.com")
entry_uname.grid(row=2,column=1,columnspan=2,padx=20,pady=10)
label_pass = Label(text="Password:")
label_pass.grid(row=3,column=0,padx=20,pady=10)
entry_pass = Entry(width=25)
entry_pass.grid(row=3,column=1,padx=10,pady=10)
but_gpass = Button(text="Generate Password",width=20,command=password_generator)
but_gpass.grid(row=3,column=2,padx=10,pady=10)
but_add = Button(text="Add",width=50,command=add_detail)
but_add.grid(row=4,column=1,columnspan=2,padx=20,pady=10)
main_screen.mainloop()