import datetime as dt
import smtplib
import random

def make_quote_list():
	with open("quotes.txt", encoding="utf-8") as file:
		text = file.read()
	quotes = text.split("\n")
	all_quotes = [i.split("–") for i in quotes]
	return all_quotes


def send_mail():
	r_quote = random.choice(make_quote_list())
	mail = "hackingwithbhai@gmail.com"
	password = input("Password: ")
	message = f"subject:Motivational Quote\n\n{r_quote[0]}\nBy{r_quote[1]}".encode("utf-8")
	with smtplib.SMTP("smtp.gmail.com") as conn:
		conn.starttls()
		conn.login(user=mail,password=password)
		conn.sendmail(from_addr=mail,to_addrs="sg704992@gmail.com",msg=message)
	

now = dt.datetime.now()
if now.weekday() == 3:
	send_mail()
# print(now.weekday())