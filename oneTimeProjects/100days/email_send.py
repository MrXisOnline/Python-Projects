import smtplib as smtp

my_mail = "hackingwithbhai@gmail.com"
connection = smtp.SMTP("smtp.gmail.com")	# creates a connection b/w you and server
connection.starttls()		# start tls encryption for connection
connection.login(user=my_mail,password=input("Password :"))	# Login to user account
connection.sendmail(from_addr=my_mail,to_addrs="sg704992@gmail.com",msg="Test Mail")
connection.close()	# Close connection