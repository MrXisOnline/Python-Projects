from turtle import Turtle

class Level:
	"""Level management for turtle crossing"""
	def __init__(self):
		self.level = 1
		self.l = Turtle()
		self.l.color("black")
		self.l.penup()
		self.l.hideturtle()
		self.l.setposition(-350, 250)
		self.l.write(f"Level :{self.level}", align="left", font=("Arial",15,"bold"))

	def update_level(self):
		self.l.clear()
		self.l.write(f"Level :{self.level}", align="left", font=("Arial",15,"bold"))
		
	def game_over(self):
		self.l.setposition(-20,0)
		self.l.write(f"GAME-OVER", align="left", font=("Arial",20,"bold"))
