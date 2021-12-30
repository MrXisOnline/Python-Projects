import smtplib
import imapclient
import pprint
import datetime
import email

def smtp():
	try:
		smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
		ehlo = smtpObj.ehlo()
		if ehlo[0] == 250:
			print("Connected")
			tls = smtpObj.starttls()
			if tls[0] == 220:
				print("Started TLS")
				s_mail = "hackingwithbhai@gmail.com"
				s_pass = input("Password: ")
				log = smtpObj.login(s_mail, s_pass)
				if log[0] == 235:
					print("Authentication Successful!")
					dic = smtpObj.sendmail(s_mail, "sg704992@gmail.com", "Subject: Testing\n Hey This is Suraj!")
					if dic == {}:
						print("Mail Sent!")
						quit = smtpObj.quit()
						if quit[0] == 221:
							print("Connection Ended!")
	except:
		print("Error Occured!")

def imap():
	imapObj = imapclient.IMAPClient("imap.gmail.com", ssl=True)
	s_mail = "hackingwithbhai@gmail.com"
	s_pass = input("Password: ")
	imapObj.login(s_mail, s_pass)
	pprint.pprint(imapObj.list_folders())
	imapObj.select_folder("INBOX", readonly=True)
	date = datetime.datetime.now()
	uids = imapObj.search(['FROM', 'sg704992@gmail.com'])
	for uid in uids:
		# print("%d messages from our best friend" % len(uids))
		# rawMessage = imapObj.fetch(uids ,['BODY[]'])
		fetch_data = imapObj.fetch(uid, ['RFC822'])
		parsed = email.message_from_bytes(fetch_data[uid][b'RFC822'])
		pprint.pprint(parsed)
	imapObj.logout()

imap()
