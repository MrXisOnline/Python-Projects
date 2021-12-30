from turtle import Turtle

class Bar:
	"""Bar class of breaking-out"""
	def __init__(self):
		self.bar = Turtle()
		self.bar.color("black")
		self.bar.shape("square")
		self.bar.shapesize(1,3)
		self.bar.penup()
		self.bar.setposition(0, -220)
		self.bar.speed(10)

	def move_left(self):
		cur_x = self.bar.xcor()
		if cur_x > -200:
			x = self.bar.xcor() - 20
			self.bar.setposition(x, self.bar.ycor())

	def move_right(self):
		cur_x = self.bar.xcor()
		if cur_x < 200:
			x = self.bar.xcor() + 20
			self.bar.setposition(x, self.bar.ycor())
