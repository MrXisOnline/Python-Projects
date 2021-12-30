from turtle import Turtle
import random

colors = ["red", "yellow", "white", "green", "purple", "pink", "magenta"]

class PlayerShip:
	def __init__(self):
		self.player = Turtle()
		self.player.shape("square")
		self.player.shapesize(1,1)
		# self.player.setheading(90)
		self.player.color(random.choice(colors))
		self.player.penup()
		self.player.setposition(0,-220)

	def move_left(self):
		cur_x = self.player.xcor()
		if cur_x > -230:
			x = self.player.xcor() - 20
			self.player.setposition(x, self.player.ycor())

	def move_right(self):
		cur_x = self.player.xcor()
		if cur_x < 230:
			x = self.player.xcor() + 20
			self.player.setposition(x, self.player.ycor())