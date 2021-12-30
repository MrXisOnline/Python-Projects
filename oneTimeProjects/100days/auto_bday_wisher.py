import datetime as dt
import smtplib as smtp
import pandas as pd
import random

path = "C:\\Users\\SG704\\PythonProjects\\oneTimeProjects\\100days\\"
letters = ["letter_templates\\letter_1.txt","letter_templates\\letter_2.txt","letter_templates\\letter_3.txt"]
date = pd.read_csv("birthdays.csv")
month, day, name= int(date[date.email == "sg704992@gmail.com"].month), int(date[date.email == "sg704992@gmail.com"].day), date[date.email == "sg704992@gmail.com"].name.to_list()[0]
today = dt.datetime.now()
if today.month == month and today.day == day:
	temp_letter = random.choice(letters)
	with open(path+temp_letter) as file:
		text = file.read()
	letter = text.replace("[NAME]",name)
	with smtp.SMTP("smtp.gmail.com") as con:
		con.starttls()
		con.login("hackingwithbhai@gmail.com",input("Passcode: "))
		con.sendmail(from_addr="hackingwithbhai@gmail.com",to_addrs="sg704992@gmail.com",msg=f"subject:Happy Birthday\n\n{letter}")
		

	