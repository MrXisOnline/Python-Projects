import sqlite3

# Creating a Database or connecting to a database
conn = sqlite3.connect("costumer.db")

# Creating cursor
c = conn.cursor()

'''
# Create a Table
c.execute("CREATE TABLE customers(ID integer,NAME text)")
'''

'''
# Inserting data into table
c.execute("INSERT INTO customers VALUES(003,'Alok Kumar')")
print("Executed")
'''

'''
# Insert many data into table
many_records = [(4, "Priya"), (5, "Akashay")]
c.executemany("INSERT INTO customers VALUES (?,?)", many_records)
'''

'''
# Fetch data from table
c.execute("SELECT * FROM customers")
# print(c.fectchone())
# print(c.fetchmany(3))
rows = c.fetchall()
for row in rows:
	print("%d %s" %(row[0],row[1]))
'''

'''
# WHERE clause
c.execute("SELECT NAME FROM customers WHERE ID = 4")
print(c.fetchall())
'''

'''
# Updata data from table
c.execute("UPDATE customers SET NAME = 'Ram' WHERE ID = 5")
conn.commit()

c.execute("SELECT * FROM customers")
rows = c.fetchall()
for row in rows:
	print("%d %s" %(row[0],row[1]))
'''

'''
# Delete data from table
c.execute("DELETE from customers WHERE ID = 5")
conn.commit()

c.execute("SELECT * FROM customers")
rows = c.fetchall()
for row in rows:
	print("%d %s" %(row[0],row[1]))
'''

'''
# Order By Result
c.execute("SELECT * FROM customers ORDER BY ID DESC")
rows = c.fetchall()
for row in rows:
	print("%d %s" %(row[0],row[1]))
'''

'''
# Drop table
c.execute("DROP TABLE customers")
c.commit()
'''

# Commiting data into database
conn.commit()

# Closing Connection from database
conn.close()
