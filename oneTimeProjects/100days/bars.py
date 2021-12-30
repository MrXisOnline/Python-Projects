from turtle import Turtle

class Bar:
	def __init__(self,x):
		"""Create the Bars for ping Pong"""
		self.bar = Turtle()
		self.bar.color("white")
		self.bar.shape("square")
		self.bar.shapesize(30,1)
		self.bar.penup()
		self.bar.setposition(x, 0)
		self.bar.speed(10)

	def move_up(self):
		y = self.bar.ycor() + 35
		self.bar.setposition(self.bar.xcor(), y)

	def move_down(self):
		y = self.bar.ycor() - 35
		self.bar.setposition(self.bar.xcor(), y)

	
