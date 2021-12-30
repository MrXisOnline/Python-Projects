from turtle import Turtle

class Writer:
	"""Writer class for breaking-out"""
	def __init__(self):
		self.writer = Turtle()
		self.writer.color("black")
		# self.writer.pensize(5)
		self.writer.penup()
		self.writer.hideturtle()

	def game_over(self):
		self.writer.setposition(0, 0)
		self.writer.pendown()
		self.writer.write("Game-Over", align="center", font=("Arial", 20, "bold"))
		self.writer.penup()

	def win(self):
		self.writer.setposition(0, 0)
		self.writer.pendown()
		self.writer.write("You Win", align="center", font=("Arial", 20, "bold"))
		self.writer.penup()