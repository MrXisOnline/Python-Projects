from turtle import Turtle

class Player:
	"""Turtle crossing player"""
	def __init__(self):
		self.p = Turtle()
		self.p.color("black")
		self.p.shape("turtle")
		self.p.shapesize(1,1)
		self.p.penup()
		self.p.setposition(0,-275)
		self.p.setheading(90)

	def move(self):
		self.p.forward(10)

	def up(self):
		self.p.setheading(90)
		self.move()

	def pass_level(self):
		pos = self.p.position()
		if int(pos[1]) >= 270:
			return True
		else:
			return False
