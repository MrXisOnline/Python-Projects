import sqlite3
import sys


def add_single_quote(string):
	x = "'" + string +"'"
	return x


def check_int(string):
	try:
		a = int(string)
		return a
	except:
		print("[-] Input Error!!!")
		sys.exit(0)


def show_record(cursor, connection):
	try:
		cursor.execute("SELECT * FROM phonebook")
		connection.commit()
		data = cursor.fetchall()
		print("\n")
		print("NAME".ljust(20," ") + "| ADDRESS".ljust(20," ") + "| PHONE NO.".ljust(15," "))
		print()
		for row in data:
			print(row[0].ljust(20," ") + "| " + row[1].ljust(20," ") + "| " + row[2].ljust(15," "))
		print("\n")
	except:
		raise Exception("Input Error")


def insert_record(data, cursor, connection):
	try:
		com = "INSERT INTO phonebook VALUES(%s,%s,%s)" %(data[0],data[1],data[2])
		cursor.execute(com)
		connection.commit()
	except:
		raise Exception("Input Error")


def delete_record(data, cursor, connection):
	try:
		com = "DELETE FROM phonebook WHERE PHONE = %s" %data
		cursor.execute(com)
		connection.commit()
	except:
		raise Exception("Input Error")


conn = sqlite3.connect("phonerecords.db")
c = conn.cursor()

while True:
	try:
		print("PHONEBOOK".center(55,"*"))
		print("\n")
		print("1. Show Data")
		print("2. Insert Data")
		print("3. Delete Data")
		print("4. Exit Or [CTRL-C]")
		i = check_int(input("Choice :>"))
		if i == 1:
			show_record(c, conn)
		elif i == 2:
			print("Enter The Data You Need To Insert")
			name = add_single_quote(input("Name :"))
			addr = add_single_quote(input("Address :"))
			number = add_single_quote(input("Phone No. :"))
			data = (name, addr, number)
			insert_record(data, c, conn)
			print("Inserted Record")
		elif i == 3:
			print("Enter Phone Number You Want To Delete")
			del_num = add_single_quote(input("Phone No. :"))
			delete_record(del_num, c, conn)
			print("Deleted Record")
		elif i == 4:
			print("Exiting Phonebook")
			break
		else:
			print("Enter Between [1,2,3,4] ",end="")
			raise Exception("Input Error")
	except KeyboardInterrupt:
		sys.exit(0)
	except:
		print("Error Occured!!!")


#conn.commit()
conn.close()