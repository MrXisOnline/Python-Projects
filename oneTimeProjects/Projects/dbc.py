import sqlite3

db = sqlite3.connect("phone_record.db")
c = db.cursor()
c.execute('''CREATE TABLE phonebook(name char[80], addr char[80], PHONE char[12])''')
db.commit()
