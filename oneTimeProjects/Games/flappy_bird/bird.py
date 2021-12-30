import turtle
from turtle import Turtle, Screen
import time

class Bird:
	def __init__(self):
		self.player = Turtle()
		self.player.color("yellow")
		self.player.shape("turtle")
		self.player.penup()
		self.player.setposition(-200, 0)

	def jump(self):
		self.player.setposition(self.player.xcor(), self.player.ycor()+20)

	def down(self):
		self.player.setposition(self.player.xcor(), self.player.ycor()-20)

	def gravity(self):
		start = time.time()
		if time.time()-start > 0.1:
			if self.player.ycor() > -150:
				self.player.setposition(self.player.xcor(), self.player.ycor()-7)
			start = time.time()
