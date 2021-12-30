from turtle import Turtle

class State:
	"""State pointer for us state"""
	def __init__(self):
		self.pointer = Turtle()
		self.pointer.color("black")
		self.pointer.penup()
		self.pointer.hideturtle()
		self.pointer.speed(10)

	def writer(self, state, pos):
		self.pointer.setposition(*pos)
		self.pointer.write(state, align="left", font=("Arial", 10, "normal"))
	
		