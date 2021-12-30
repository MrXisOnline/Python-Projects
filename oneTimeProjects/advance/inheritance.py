class Animal:		# Parent Class
	def __init__(self):
		self.eyes = 2
	def breathe(self):
		print("Inhale | Exhale!")
class Fish(Animal):		# Fish class inherit properties of
						# Parent Class
	def __init__(self):
		super().__init__()	# used to trigger parent init
		self.gill = 2
	def swim(self):
		print("Swim")
		
fish = Fish()
fish.breathe()
fish.swim()
print(fish.eyes)
print(fish.gill)