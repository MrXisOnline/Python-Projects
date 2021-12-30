import turtle
from turtle import Turtle
import random
# import numpy as np

colors = ["red", "yellow", "green", "brown", "blue"]
class Bar:
	def __init__(self):
		self.bars = []
		self.make_vertical_bar()

	def make_vertical_bar(self):
		b1 = [Turtle(), Turtle(), Turtle()]
		b2 = [Turtle(), Turtle(), Turtle()]
		temp_bar = [b1, b2]
		c = random.choice(colors)
		self.bars.append(b1)
		self.bars.append(b2)
		y_b1_alt = random.randint(0, 75)
		y_b2_alt = random.randint(0, 75)
		for t in self.bars:
			for b in t:
				b.penup()
				b.shape("square")
				b.shapesize(3, 1, 1)
		for bar in temp_bar:
			if temp_bar.index(bar) == 0:
				for b in bar:
					if bar.index(b) == 0:
						b.setposition(200, 200 - y_b1_alt)
						b.color(c)
					elif bar.index(b) == 1:
						b.setposition(200, 200 - y_b1_alt - 40)
						b.color(c)
					elif bar.index(b) == 2:
						b.setposition(200, 200 - y_b1_alt - 80)
						b.color(c)
			elif temp_bar.index(bar) == 1:
				for b in bar:
					if bar.index(b) == 0:
						b.setposition(200, -200 + y_b2_alt)
						b.color(c)
					elif bar.index(b) == 1:
						b.setposition(200, -200 + y_b2_alt + 40)
						b.color(c)
					elif bar.index(b) == 2:
						b.setposition(200, -200 + y_b2_alt + 80)
						b.color(c)

	def pass_bar(self):
		for bar in self.bars:
			for b in bar:
				b.setposition(b.xcor()-10, b.ycor())

	def check_bar_collision(self, bird):
		for bar in self.bars:
			for b in bar:
				if b.distance(bird.player) <= 20:
					return True
		return False
