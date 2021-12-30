from turtle import Turtle, Screen

class Score:
	"""Ping pong scoreboard"""
	def __init__(self):
		self.s = Turtle()
		self.score_l = 0
		self.score_r = 0
		self.s.color("white")
		self.s.hideturtle()
		self.prep(self.score_l, self.score_r)

	def prep(self,l,r):
		self.score_l = l
		self.score_r = r
		self.s.clear()
		self.s.setposition(0,0)
		self.s.pendown()
		self.s.setposition(0, 260)
		self.s.setposition(0, -260)
		self.s.setheading(90)
		self.s.forward(100)
		self.s.penup()
		self.s.setposition(-150, 270)
		self.s.write(f"Score :{self.score_l}", align="left", font=("Arial",15,"normal"))
		self.s.setposition(100, 270)
		self.s.write(f"Score :{self.score_r}", align="left", font=("Arial",15,"normal"))
	
	def game_over(self):
		self.s.setposition(-50,0)
		self.s.write(f"GAME-OVER", align="left", font=("Arial",15,"normal"))