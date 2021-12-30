class User:			
	def __init__(self, name):		
		self.name = name			
		print("Creating user")

	def update_name(n):					# Here we created a method that update name
		self.name = self.name + " " + str(n)
		print("Updated")

user1 = User("Suraj")		
print(user1.name)
user1.update_name("Gupta")				# executing that method
print(user1.name)